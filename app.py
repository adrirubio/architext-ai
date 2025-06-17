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

def on_accept_pressed():
    name = name_entry.get().strip()
    api = api_entry.get().strip()
    if name:
        print(f"Enter was pressed! User entered: {name}")
        welcome_frame.pack_forget()
        ai_frame.pack(fill="both", expand=True)

        # First-run
        data_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "architext-ai")
        flag_file = os.path.join(data_dir, "user_has_run.flag")
        name_file = os.path.join(data_dir, "user_name.txt")
        api_file = os.path.join(data_dir, "user_api.txt")

        os.makedirs(data_dir, exist_ok=True)
        first_time = not os.path.exists(flag_file)

        # Save name to file
        with open(name_file, "w") as f:
            f.write(name)

        # Save api to file
        with open(api_file, "w") as f:
            f.write(api)

        if first_time:
            print("This is your first time using the program!")
            print(f"name= {name}")
            print(f"api= {api}")
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

def on_enter_pressed(event):
    name = name_entry.get().strip()
    api = api_entry.get().strip()
    if name:
        print(f"Enter was pressed! User entered: {name}")
        welcome_frame.pack_forget()
        ai_frame.pack(fill="both", expand=True)

        # First-run
        data_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "architext-ai")
        flag_file = os.path.join(data_dir, "user_has_run.flag")
        name_file = os.path.join(data_dir, "user_name.txt")
        api_file = os.path.join(data_dir, "user_api.txt")

        os.makedirs(data_dir, exist_ok=True)
        first_time = not os.path.exists(flag_file)

        # Save name to file
        with open(name_file, "w") as f:
            f.write(name)

        # Save api to file
        with open(api_file, "w") as f:
            f.write(api)

        if first_time:
            print(f"name= {name}")
            print(f"api= {api}")
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

def on_send():
    # Message
    text = message.get("1.0", "end-1c")
    print(f"Message for improvement:\n{text}")
    # Prompt guideline
    text = prompt_entry.get()
    print(f"\nGuideline:\n{text}")

def on_copy():
    text = response.get("1.0", "end-1c")
    if text:
        window.clipboard_clear()
        window.clipboard_append(text)
        window.update()

def on_clear():
    # Remove text in message widget
    message.delete("1.0", "end")
    # Remove text in prompt widget
    prompt_entry.delete(0, "end")
    # Remove text in response widget
    response.config(state="normal")
    response.delete("1.0", "end")
    response.insert("end", "Craft your message, set your guidelines, and let watch as the AI unveils a polished, upgraded version!\n")
    response.config(state="disabled")

def fade_in_label(label, text, delay=40):
    for i in range(len(text)):
        window.after(i * delay, lambda i=i: label.config(text=text[:i+1]))

# Window setup
window = tk.Tk()
window.geometry("700x500")
window.configure(bg="#2c3e50")
window.resizable(False, False)
window.tk.call("ttk::setTheme", "classic")

# Fonts
cool_font = tkFont.Font(family="Helvetica", size=18, weight="bold", slant="italic")
label_font = tkFont.Font(family="Helvetica", size=12)

# First-run
data_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "architext-ai")
flag_file = os.path.join(data_dir, "user_has_run.flag")
name_file = os.path.join(data_dir, "user_name.txt")
os.makedirs(data_dir, exist_ok=True)
first_time = not os.path.exists(flag_file)

# AI Frame
ai_frame = tk.Frame(
    window,
    bg="RoyalBlue4",
    width=700, height=500
)
ai_frame.pack_propagate(False)

ai_greeting_label = tk.Label(
    ai_frame,
    text="",
    fg="white",
    bg="RoyalBlue4",
    font=cool_font
)
ai_greeting_label.grid(row=0, column=0, columnspan=2, pady=(25, 15))

# Grid
ai_frame.grid_columnconfigure(0, weight=1)   # left  column
ai_frame.grid_columnconfigure(1, weight=1)   # right column

# Input box for message design
message_label = tk.Label(
    ai_frame,
    text="Design your message here:",
    fg="white",
    bg="RoyalBlue4",
    font=label_font
)
message_label.grid(row=1, column=0, padx=40, pady=(0, 5))

# Create frame for message text and scrollbar
message_frame = tk.Frame(ai_frame)
message_frame.grid(row=2, column=0, padx=40)

# Configure the frame
message_frame.grid_rowconfigure(0, weight=1)
message_frame.grid_columnconfigure(0, weight=1)

message = tk.Text(
    message_frame,
    height=7, width=50,
    wrap="word"
)
message.grid(row=0, column=0, sticky="nsew")

# Scrollbar
message_scrollbar = tk.Scrollbar(message_frame, orient="vertical", command=message.yview)
message_scrollbar.grid(row=0, column=1, sticky="ns")
message.config(yscrollcommand=message_scrollbar.set)

# Input box for prompt
prompt_label = tk.Label(
    ai_frame,
    text="How would you like your improved message?",
    fg="white",
    bg="RoyalBlue4",
    font=label_font,
    wraplength=220,
    justify="center"
)
prompt_label.grid(row=1, column=1, padx=40, pady=(0, 5))

prompt_entry = tk.Entry(
    ai_frame,
    font=label_font,
    width=42
)
prompt_entry.grid(row=2, column=1, padx=40, pady=43, sticky="new")

# Send button
send_btn = tk.Button(
    ai_frame,
    text="Send",
    bg="white",
    fg="RoyalBlue4",
    activebackground="blue",
    activeforeground="white",
    width=15,
    anchor="center",
    command=on_send
)
send_btn.grid(row=3, column=0, columnspan=2, pady=(30, 12))

# Add different colour span row
row4_bg = tk.Frame(ai_frame, bg="grey19")
row4_bg.grid(row=4, column=0, columnspan=2, sticky="nsew")

# Response label
response_label = tk.Label(
    ai_frame,
    text="Improved message:",
    fg="white",
    bg="grey19",
    font=label_font
)
response_label.grid(row=4, column=0, columnspan=2, sticky="n", pady=20)

# Create frame for message text and scrollbar
response_frame = tk.Frame(ai_frame)
response_frame.grid(row=4, column=0, columnspan=2, pady=50)

# Configure the frame
response_frame.grid_rowconfigure(4,  weight=1)
response_frame.grid_columnconfigure(0, weight=1)

# Response text box
response = tk.Text(
    response_frame,
    height=6,
    width=50,
    wrap="word"
)
response.pack(side="left", fill="both", expand=True)
response.insert("end", "Craft your message, set your guidelines, and let watch as the AI unveils a polished, upgraded version!\n")
response.config(state="disabled")

# Scrollbar
response_scrollbar = tk.Scrollbar(response_frame, orient="vertical", command=response.yview)
response_scrollbar.pack(side="right", fill="y")
response.configure(yscrollcommand=response_scrollbar.set)

# Copy button
copy_btn = tk.Button(
    ai_frame,
    text="Copy",
    bg="white",
    fg="grey19",
    activebackground="blue",
    activeforeground="white",
    width=10,
    anchor="center",
    command=on_copy
)
copy_btn.grid(row=4, column=1, sticky="e", padx=15)

# Clear button
clear_btn = tk.Button(
    ai_frame,
    text="Clear",
    bg="white",
    fg="grey19",
    activebackground="blue",
    activeforeground="white",
    width=10,
    anchor="center",
    command=on_clear
)
clear_btn.grid(row=4, column=0, sticky="w", padx=15)

if not first_time and os.path.exists(name_file):
    with open(name_file, "r") as f:
        name = f.read().strip()
    ai_frame.pack(fill="both", expand=True)
    greeting_text = f"{random.choice(greeting_words)}, {name}!"
    ai_greeting_label.config(text="")
    fade_in_label(ai_greeting_label, greeting_text)
else:
    # Welcome Frame
    welcome_frame = tk.Frame(window, bg="RoyalBlue4",
                         width=500, height=500)
    welcome_frame.pack(fill="both", expand=True)
    welcome_frame.pack_propagate(False)

    greeting_label = tk.Label(
        welcome_frame,
        text="Onboarding setup",
        fg="white",
        bg="RoyalBlue4",
        font=cool_font,
    )
    greeting_label.pack(pady=(20, 20))

    separator = tk.Frame(welcome_frame, height=3, bg='white')
    separator.pack(fill=tk.X, padx=50, pady=(0, 20))

    spacer = tk.Frame(welcome_frame, height=5, bg="RoyalBlue4")
    spacer.pack()

    name_label = tk.Label(
        welcome_frame,
        text="What should I call you?",
        bg="RoyalBlue4",
        fg="white",
        font=label_font
    )
    name_label.pack(pady=(0, 15))

    name_entry = tk.Entry(welcome_frame, font=label_font, width=28)
    name_entry.pack(pady=(0, 0))

    api_label = tk.Label(
        welcome_frame,
        text="What is your OPENAI API key?",
        bg="RoyalBlue4",
        fg="white",
        font=label_font
    )
    api_label.pack(pady=(20, 15))

    api_entry = tk.Entry(welcome_frame, font=label_font, width=28)
    api_entry.pack(pady=(0, 0))

    # Accept button
    button = tk.Button(
        welcome_frame,
        text="Accept",
        bg="RoyalBlue4",
        fg="white",
        command=on_accept_pressed
    )
    button.pack(pady=30)

    try:
        pil_image = Image.open("architext-ai-logo-small.png")

        target_height = 140
        aspect_ratio = pil_image.width / pil_image.height
        target_width = int(target_height * aspect_ratio)

        pil_image = pil_image.resize((target_width, target_height), Image.Resampling.LANCZOS)
        logo_image = ImageTk.PhotoImage(pil_image)

        logo_label = tk.Label(welcome_frame, image=logo_image, bg="RoyalBlue4")
        logo_label.pack(pady=(0, 0))

    except Exception as e:
        print("Error loading image:", e)

    # Only bind if entry exists
    api_entry.bind("<Return>", on_enter_pressed)

window.mainloop()
