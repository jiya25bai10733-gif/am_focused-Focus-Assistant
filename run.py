import subprocess
import threading
import time
import webbrowser

# =========================
# START WEBSITE AI SERVER
# =========================

def start_ai_server():

    subprocess.run([
        "python",
        "website_ai.py"
    ])

# =========================
# START GUI
# =========================

def start_gui():

    time.sleep(2)

    subprocess.run([
        "python",
        "gui.py"
    ])

# =========================
# OPEN CHROME EXTENSIONS
# =========================

def open_chrome_extensions():

    time.sleep(3)

    webbrowser.open(
        "chrome://extensions"
    )

# =========================
# RUN EVERYTHING
# =========================

threading.Thread(
    target=start_ai_server,
    daemon=True
).start()

threading.Thread(
    target=open_chrome_extensions,
    daemon=True
).start()

start_gui()