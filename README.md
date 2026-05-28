# AMFOCUSED AI 🎯

AI-powered productivity assistant with:

* ⏳ Focus Timer
* 🎥 Webcam Focus Detection
* 🔔 Smart Alarm System
* 🌐 Website Blocking
* 🧠 AI Website Classification
* 📺 YouTube Distraction Detection

---

# 🚀 Features

## ⏳ Smart Focus Timer

* 25-minute Pomodoro timer
* Pause / Resume support
* Restart focus sessions
* Clean modern UI

---

## 🎥 AI Webcam Focus Detection

AMFOCUSED uses AI-powered webcam monitoring to:

* Detect user presence
* Detect focus loss
* Trigger alarms after 5 seconds of distraction

---

## 🔔 Smart Alarm System

* Alarm starts when focus is lost
* Alarm stops automatically when focus returns
* Manual STOP ALARM button included

---

## 🌐 Website Blocking

Chrome Extension integration:

* Blocks distracting websites
* Works only during active focus sessions
* Reads focus state from Python backend

---

## 🧠 AI Website Classification

Python-based AI server:

* Detects productive vs distracting websites
* Uses editable database
* Custom training support

---

## 📺 YouTube Distraction Detection

Blocks distracting content such as:

* Shorts
* Gaming videos
* Memes
* Reactions
* Entertainment distractions

---

# 📁 Project Structure

```text
├── extension/
│   ├── manifest.json
│   ├── background.js
│   └── blocked.html
│
│
├── alarm.mp3
├── alarm.py
├── allowed_sites.json
├── focus_state.json
├── gui.py
├── main.py
├── pause.png
├── play.png
├── restart.png
├── run.py
├── standby.png
├── timer.py
├── webcam_detector.py
├── website_ai.py
├── website_database.json
└── requirements.txt
```

---

# 🛠 Requirements

Install Python:

https://www.python.org/downloads/

Recommended:

* Python 3.11+

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/jiya25bai10733-gif/am_focused-Focus-Assistant
```

Enter project folder:

```bash
cd am_focused-Focus-Assistant
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

### Mac/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Project

Run everything using:

```bash
python run.py
```

This automatically:

* Starts AI website server
* Starts GUI application
* Enables focus monitoring

---

# 🌐 Chrome Extension Setup

## 1️⃣ Open Chrome Extensions

Go to:

```text
chrome://extensions
```

---

## 2️⃣ Enable Developer Mode

Turn ON:

* Developer Mode

(top-right corner)

---

## 3️⃣ Load Extension

Click:

```text
Load unpacked
```

Select:

```text
am_focused-Focus-Assistant/extension
```

---

# 📺 YouTube AI Detection

AMFOCUSED blocks videos containing keywords like:

* gaming
* meme
* shorts
* reaction
* livestream
* minecraft
* gta
* valorant
* fortnite

---

# 🔥 How It Works

## Start Session

* Timer starts
* Camera activates
* AI monitoring activates
* Website blocking activates

---

## Lose Focus For 5 Seconds

* Alarm starts automatically

---

## Return To Focus

* Alarm stops automatically

---

## Pause Session

* Timer pauses
* Camera pauses
* Website blocking disables

---

# 🖥 Tested On

* Windows 10
* Windows 11
* Python 3.11+
* Google Chrome

---

# 📌 Future Features

* AI productivity analytics
* Daily focus tracking
* Deep learning focus model
* Cloud sync
* Mobile integration

---

# 👨‍💻 Built With

* Python
* OpenCV
* MediaPipe
* Flask
* CustomTkinter
* Chrome Extensions API

---

# 🎯 AMFOCUSED

Stay focused.
Block distractions.
Build consistency.
