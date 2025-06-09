import tkinter as tk
import tkinter.font as tkFont
import random

def on_enter_pressed(event):
    name = entry.get()
    if name:
        print(f"Enter was pressed! User entered: {name}")

        # Destroy all widgets in the window
        for widget in window.winfo_children():
            widget.destroy()

    else:
        print("Enter was pressed, but no input.")

window = tk.Tk()
window.geometry("500x300")
window.configure(bg="grey21")

# Define a custom font
cool_font = tkFont.Font(family="Helvetica", size=20, weight="bold", slant="italic")
label_font = tkFont.Font(family="Helvetica", size=14)

# Greeting Label
greeting = tk.Label(
    text="Hello!",
    fg="white",
    bg="grey21",
    font=cool_font,
)
greeting.pack(pady=(30, 20))

# Name Label and Entry
frame = tk.Frame(window, bg="grey21")
frame.pack()

label = tk.Label(
    frame,
    text="Input name:",
    bg="grey21",
    fg="white",
    font=label_font
)
label.pack()

entry = tk.Entry(frame, font=label_font, width=20)
entry.pack(side="left")

# Bind Enter key to the entry widget
entry.bind("<Return>", on_enter_pressed)

# Pick a random greeting
greeting_words = [
    "Nice to see you",
    "Welcome back",
    "Hello there",
    "Glad you're here",
    "Good to have you back",
    "Hey, long time no see",
    "Happy to see you again",
    "Hello",
    "You’re looking great today",
    "It’s always a pleasure",
    "Welcome aboard",
    "Hey there, how’s it going",
    "Good day to you",
    "Great to have you here",
    "Let’s get started",
    "Hope you’re doing well",
    "Ready when you are",
    "Nice of you to drop by",
    "Let’s make today awesome",
    "You're just in time"
]

random_greeting = random.choice(greeting_words)
print(random_greeting)

window.mainloop()
