from PySide6.QtGui import QTextCursor
import sys 
import asyncio
from main import stream_berry
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication,QWidget,QTextBrowser,QPushButton,QLineEdit
 

class BerryWorker(QThread):
    chunk_received = Signal(str)
    finished_response = Signal()
    error_occurred = Signal(str)

    def __init__(self, message):
        super().__init__()
        self.message = message

    async def get_reply(self):
        async for chunk in stream_berry(self.message):
            self.chunk_received.emit(chunk)

    def run(self):                  #runsin the background
        try:
            asyncio.run(self.get_reply())
        except Exception as e:
            self.error_occurred.emit(str(e))

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("BERRY AI")
window.resize(800,600)



# chat_area=QTextBrowser("Welcome to BERRY AI",window)
# chat_area.move(30,30)
# chat_area.setFixedWidth(5000)


chat_area=QTextBrowser()
chat_area.setParent(window)
chat_area.setGeometry(30, 30, 740, 400)
chat_area.setLineWrapMode(QTextBrowser.LineWrapMode.WidgetWidth)
chat_area.setStyleSheet("""
QTextBrowser{
background-color: #1e1e1e;

        color: #e6e6e6;

        border: none;

        padding: 12px;

        font-size: 14px;}""")


# input_box=QLineEdit(window)
# input_box.setPlaceholderText("Message BERRY...")



button=QPushButton("Click Me",window)
button.setGeometry(650, 450, 100, 45)


input_box=QLineEdit(window)
input_box.setPlaceholderText("Message BERRY...")
input_box.setGeometry(30,450,600,45)    


worker = None   

def show_chunk(chunk):
    chat_area.moveCursor(QTextCursor.MoveOperation.End)
    chat_area.insertPlainText(chunk)
    chat_area.ensureCursorVisible()


def enable_input():
    input_box.setEnabled(True)
    button.setEnabled(True)
    input_box.setFocus()


def send_message():
    global worker
    message = input_box.text().strip()
    if not message:
        return

    chat_area.append(f"You: {message}")
    chat_area.append("BERRY: ")

    input_box.clear()
    input_box.setEnabled(False)     
    button.setEnabled(False)

    worker = BerryWorker(message)
    worker.chunk_received.connect(show_chunk)
    worker.error_occurred.connect(lambda e: show_chunk(f"\nError: {e}"))
    worker.finished.connect(enable_input)   
    worker.start()


button.clicked.connect(send_message)
input_box.returnPressed.connect(send_message)

window.show()
sys.exit(app.exec())