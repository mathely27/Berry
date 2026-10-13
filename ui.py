import sys 
from main import ask_berry
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit
 

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("BERRY AI")
window.resize(800,600)



label=QLabel("Welcome to BERRY AI",window)
label.move(30,30)
label.setFixedWidth(5000)

button=QPushButton("Click Me",window)
button.move(30,70)


input_box=QLineEdit(window)
input_box.setPlaceholderText("Message BERRY...")
input_box.setGeometry(30,120,500,40)    


def send_message():
    message=input_box.text()
    response=ask_berry(message)
    label.setText(response)
    input_box.clear()

button.clicked.connect(send_message)


window.show()
sys.exit(app.exec())


