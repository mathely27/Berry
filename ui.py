import tkinter as tk
from main import ask_berry

# ─── Window Setup ───
window = tk.Tk()
window.title("🫐 BERRY - AI Assistant")
window.geometry("800x600")
window.configure(bg="#1a1a2e")
window.minsize(600, 400)

# ─── Title Label ───
title_label = tk.Label(
    window,
    text="🫐 BERRY",
    font=("Helvetica", 28, "bold"),
    bg="#1a1a2e",
    fg="#a78bfa"
)
title_label.pack(pady=(15, 5))

subtitle_label = tk.Label(
    window,
    text="Your Personal AI Assistant",
    font=("Helvetica", 12),
    bg="#1a1a2e",
    fg="#64748b"
)
subtitle_label.pack(pady=(0, 10))

# ─── Chat Display Area ───
chat_frame = tk.Frame(window, bg="#6c63ff", padx=2, pady=2)
chat_frame.pack(padx=20, pady=(5, 10), fill="both", expand=True)

chat = tk.Text(
    chat_frame,
    bg="#16213e",
    fg="#e2e8f0",
    font=("Courier", 14),
    wrap="word",
    relief="flat",
    padx=10,
    pady=10,
    state="disabled",
    cursor="arrow"
)
chat.pack(fill="both", expand=True)

# Configure text tags for colored messages
chat.tag_config("user_tag", foreground="#a78bfa")
chat.tag_config("berry_tag", foreground="#4ade80")
chat.tag_config("msg_tag", foreground="#e2e8f0")

# ─── Bottom Bar (Input + Button) ───
bottom_frame = tk.Frame(window, bg="#1a1a2e")
bottom_frame.pack(padx=20, pady=(0, 15), fill="x")

# Input box with visible border frame
input_frame = tk.Frame(bottom_frame, bg="#6c63ff", padx=2, pady=2)
input_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))

input_box = tk.Text(
    input_frame,
    bg="#16213e",
    fg="white",
    font=("Helvetica", 14),
    height=1,
    wrap="word",
    relief="flat",
    padx=8,
    pady=6,
    insertbackground="white"
)
input_box.pack(fill="x", expand=True)

# Send button
send_button = tk.Button(
    bottom_frame,
    text="SEND 🫐",
    command=lambda: send_message(),
    font=("Helvetica", 13, "bold"),
    bg="#6c63ff",
    fg="white",
    activebackground="#7c73ff",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)
send_button.pack(side="right")

# ─── Welcome Message ───
chat.config(state="normal")
chat.insert("end", "🫐 BERRY: ", "berry_tag")
chat.insert("end", "Hey! Main Berry hoon, tera AI assistant. Kuch bhi pooch! 😊\n\n", "msg_tag")
chat.config(state="disabled")


# ─── Send Message Function ───
def send_message():
    user = input_box.get("1.0", "end-1c").strip()
    if not user:
        return

    # Show user message
    chat.config(state="normal")
    chat.insert("end", "👤 YOU: ", "user_tag")
    chat.insert("end", user + "\n", "msg_tag")
    chat.config(state="disabled")
    chat.see("end")

    # Clear input
    input_box.delete("1.0", "end")

    # Update window to show user message immediately
    window.update()

    # Get Berry's response
    try:
        resp = ask_berry(user)
    except Exception as e:
        resp = f"Error: {str(e)}"

    # Show Berry's response
    chat.config(state="normal")
    chat.insert("end", "🫐 BERRY: ", "berry_tag")
    chat.insert("end", resp + "\n\n", "msg_tag")
    chat.config(state="disabled")
    chat.see("end")


# ─── Enter Key Binding ───
def on_enter(event):
    send_message()
    return "break"  # Prevents newline in input box

input_box.bind("<Return>", on_enter)


# ─── Start ───
window.mainloop()