import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import Image, ImageTk
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
welcome_frame = tk.Frame(window, bg="RoyalBlue4")
welcome_frame.pack(fill="both", expand=True)

greeting_label = tk.Label(
    welcome_frame,
    text="Onboarding setup",
    fg="white",
    bg="RoyalBlue4",
    font=cool_font,
)
greeting_label.pack(pady=(30, 20))

separator = tk.Frame(welcome_frame, height=3, bg='white')
separator.pack(fill=tk.X, padx=50, pady=(0, 20))

# Add invisible spacer to push name label down
spacer = tk.Frame(welcome_frame, height=30, bg="RoyalBlue4")
spacer.pack()

name_label = tk.Label(
    welcome_frame,
    text="What should we call you?",
    bg="RoyalBlue4",
    fg="white",
    font=label_font
)
name_label.pack(pady=(0, 15))

entry = tk.Entry(welcome_frame, font=label_font, width=28)
entry.pack(pady=(0, 0))

try:
    pil_image = Image.open("architext-ai-logo.png")

    # Fixed size image placed right after the text
    target_height = 275
    aspect_ratio = pil_image.width / pil_image.height
    target_width = int(target_height * aspect_ratio)

    pil_image = pil_image.resize((target_width, target_height), Image.Resampling.LANCZOS)
    logo_image = ImageTk.PhotoImage(pil_image)

    logo_label = tk.Label(welcome_frame, image=logo_image, bg="RoyalBlue4")
    logo_label.pack(pady=(0, 0))

except Exception as e:
    print("Error loading image:", e)

# AI Frame
ai_frame = tk.Frame(window, bg="RoyalBlue4")

ai_greeting_label = tk.Label(
    ai_frame,
    text="",
    fg="white",
    bg="RoyalBlue4",
    font=cool_font,
)
ai_greeting_label.pack(pady=(30, 20))

entry.bind("<Return>", on_enter_pressed)

window.mainloop()
