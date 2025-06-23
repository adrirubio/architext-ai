# architext-ai

Architect AI is your blueprint for perfect writing. It's a minimalist desktop app that uses the power of AI to instantly rebuild and enhance your text.

<p align="left">
  <img src="architext-ai-logo-small.png"
       alt="architext-ai-logo"
       width="200">
</p>

## Demo

Watch a quick preview below (GIF)

### 🔹 Preview (GIF)
![Architext AI - Preview](https://github.com/adrirubio/demo-files/raw/main/demo-architext-ai.gif)

## Installation

### Prerequisites
- Python 3.8 or higher
- An OpenAI API key

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/adrirubio/architext-ai.git
   cd architext-ai
   ```

2. **Install dependencies**
   ```bash
   pip install openai>=1.0.0 Pillow>=8.0.0 pynput
   ```

3. **Set up your OpenAI API key**

   Create a `config.py` file in the project directory:
   ```python
   OPENAI_API_KEY = "your-api-key-here"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

### Optional: Global Hotkey Setup (F5)

To launch Architext AI with the F5 key from anywhere on your system:

1. **Start the hotkey daemon**
   ```bash
   python hotkey_daemon.py
   ```

2. **Keep it running in the background**
   - The daemon will listen for F5 key presses
   - Press F5 anytime to launch Architext AI
   - Press Ctrl+C to stop the daemon

3. **Auto-start on boot (Linux)**

   Add to your startup applications or create a systemd service:
   ```bash
   # Create a systemd service file
   sudo nano /etc/systemd/system/architext-hotkey.service
   ```

   Add the following content:
   ```ini
   [Unit]
   Description=Architext AI Hotkey Daemon
   After=graphical.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/python3 /path/to/architext-ai/hotkey_daemon.py
   Restart=on-failure
   User=YOUR_USERNAME

   [Install]
   WantedBy=default.target
   ```

   Enable and start the service:
   ```bash
   sudo systemctl enable architext-hotkey
   sudo systemctl start architext-hotkey
   ```

## Usage

1. **Launch the app** using either:
   - Direct command: `python app.py`
   - F5 hotkey (if daemon is running)

2. **Enter your prompt** in the text field

3. **Select and paste text** you want to enhance

4. **Get instant results** with AI-powered text refinement

