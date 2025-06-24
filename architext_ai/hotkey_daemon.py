#!/usr/bin/env python3
import subprocess
import sys
import os
import time
from pynput import keyboard
from pynput.keyboard import Key

# Track last launch time to prevent spam
last_launch_time = 0
LAUNCH_COOLDOWN = 2  # seconds

def launch_app():
    """Launch the Architext AI application"""
    global last_launch_time

    current_time = time.time()
    if current_time - last_launch_time < LAUNCH_COOLDOWN:
        print("Launch blocked - too soon after last launch")
        return

    try:
        app_path = os.path.join(os.path.dirname(__file__), "app.py")
        
        subprocess.Popen([sys.executable, app_path],
                        cwd=os.path.dirname(__file__))
        last_launch_time = current_time
        print("Architext AI launched!")
    except Exception as e:
        print(f"Error launching app: {e}")

def on_press(key):
    """Handle key press events"""
    try:
        if key == Key.f5:
            launch_app()
    except AttributeError:
        # Special keys (like F5) don't have char
        pass

def main():
    """Main daemon loop"""
    print("Hotkey daemon started. Press F5 to launch Architext AI.")
    print("Press Ctrl+C to stop.")

    # Set up the listener
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nHotkey daemon stopped.")

if __name__ == "__main__":
    main()
