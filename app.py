import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
import random
import os

# Random greeting
greeting_words = [
    "Nice to see you", "Welcome back", "Hello there", "Glad you're here",
    "Good to have you back", "Hey, long time no see", "Happy to see you again",
    "Hello", "You’re looking great today", "It’s always a pleasure",
    "Welcome aboard", "Hey there, how’s it going", "Good day to you",
    "Great to have you here", "Let’s get started", "Hope you’re doing well",
    "Ready when you are", "Nice of you to drop by", "Let’s make today awesome",
    "You're just in time"
]

def on_enter_pressed(event):
    name = entry.get().strip()
    if name:
        print(f"Enter was pressed! User entered: {name}")
        welcome_frame.pack_forget()
        ai_frame.pack(fill="both", expand=True)

        # First-run
        data_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "architext-ai")
        flag_file = os.path.join(data_dir, "user_has_run.flag")
        os.makedirs(data_dir, exist_ok=True)
        first_time = not os.path.exists(flag_file)

        if first_time:
            print("This is your first time using the program!")
            with open(flag_file, "w") as f:
                f.write("User has run the program.")
            greeting_text = f"Welcome to Architext-AI, {name}!"
        else:
            print("Welcome back!")
            greeting_text = f"{random.choice(greeting_words)}, {name}!"

        # Typing animation for AI frame's greeting
        ai_greeting_label.config(text="")
        fade_in_label(ai_greeting_label, greeting_text)
    else:
        print("Enter was pressed, but no input.")

def fade_in_label(label, text, delay=40):
    for i in range(len(text)):
        window.after(i * delay, lambda i=i: label.config(text=text[:i+1]))

# Window setup
window = tk.Tk()
window.geometry("600x400")
window.configure(bg="#2c3e50")
window.resizable(False, False)

# Fonts
cool_font = tkFont.Font(family="Helvetica", size=18, weight="bold", slant="italic")
label_font = tkFont.Font(family="Helvetica", size=15)

# Welcome Frame
welcome_frame = tk.Frame(window, bg="#6e65c6")
welcome_frame.pack(fill="both", expand=True)

greeting_label = tk.Label(
    welcome_frame,
    text="Hi! Just need a few quick details to get started!",
    fg="black",
    bg="#6e65c6",
    font=cool_font,
)
greeting_label.pack(pady=(30, 20))

input_frame = tk.Frame(welcome_frame, bg="#6e65c6")
input_frame.pack()

separator = tk.Frame(input_frame, height=3, bg='black')
separator.pack(fill=tk.X, pady=(5, 15))

name_label = tk.Label(
    input_frame,
    text="Input name:",
    bg="#6e65c6",
    fg="black",
    font=label_font
)
name_label.pack(pady=(5, 8))

entry = tk.Entry(input_frame, font=label_font, width=30)
entry.pack()

# AI Frame
ai_frame = tk.Frame(window, bg="#6e65c6")

ai_greeting_label = tk.Label(
    ai_frame,
    text="",
    fg="black",
    bg="#6e65c6",
    font=cool_font,
)
ai_greeting_label.pack(pady=(30, 20))

entry.bind("<Return>", on_enter_pressed)

window.mainloop()
