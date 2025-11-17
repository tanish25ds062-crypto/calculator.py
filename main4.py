import tkinter as tk
from tkinter import scrolledtext
import random

# Knowledge base (fixed missing commas and typo in "your name")
responses = {
    "hello": ["Hi there! How can I help you?", "Hey! what's up?"],
    "how are you": ["I'm doing great!", "Feeling like a bot should--awesome!", "All good, thanks for asking!"],
    "your name": ["My name is PyBot", "You can call me PyBot!", "I'm PyBot, your assistant."],
    "bye": ["Goodbye", "See you later!", "Bye! Have a nice day!"]
}

def get_response(user_msg):
    user_msg = user_msg.lower()
    for key in responses:
        if key in user_msg:
            return random.choice(responses[key])  # Fixed typo: responses
    return "Sorry I do not understand that"  # Moved outside loop

def send_message():
    user_msg = entry.get()
    if user_msg.strip() == "":
        return
    # Fixed indentation and tag configuration
    chat_window.insert(tk.END, "You: " + user_msg + "\n", "user")
    entry.delete(0, tk.END)
    bot_msg = get_response(user_msg)
    chat_window.insert(tk.END, "Bot: " + bot_msg + "\n", "bot")
    chat_window.see(tk.END)  # Auto-scroll to latest message

# GUI setup (moved outside send_message function)
root = tk.Tk()
root.title("PyBot - Chatbot")
root.geometry("450x550")  # Fixed typo: * vs x

# Chat window with proper ScrolledText initialization
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_window.pack(pady=10)

# Configure message tags
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

# Input frame for better organization
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", lambda event: send_message())  # Enter key support

send_btn = tk.Button(input_frame, text="Send", command=send_message, width=10, bg="lightblue")
send_btn.pack(side=tk.LEFT)

root.mainloop()