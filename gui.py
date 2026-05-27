import customtkinter as ctk
import threading
import time
import cv2
import json

from PIL import Image, ImageTk

from webcam_detector import (
    get_frame,
    start_camera,
    stop_camera
)

from alarm import stop_alarm

# =========================
# APP SETTINGS
# =========================

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x850")
app.title("AMFOCUSED AI")

# =========================
# LOAD ICONS (FIXED SIZE)
# =========================

ICON_SIZE = (30, 30)

play_icon = ctk.CTkImage(
    light_image=Image.open("play.png"),
    dark_image=Image.open("play.png"),
    size=ICON_SIZE
)

pause_icon = ctk.CTkImage(
    light_image=Image.open("pause.png"),
    dark_image=Image.open("pause.png"),
    size=ICON_SIZE
)

restart_icon = ctk.CTkImage(
    light_image=Image.open("restart.png"),
    dark_image=Image.open("restart.png"),
    size=ICON_SIZE
)

standby_image = ctk.CTkImage(
    light_image=Image.open("standby.png"),
    dark_image=Image.open("standby.png"),
    size=(450, 300)
)

# =========================
# VARIABLES
# =========================

running = False
paused = False
total_seconds = 25 * 60

# =========================
# STATE SAVE
# =========================

def set_focus_state(state):
    with open("focus_state.json", "w") as file:
        json.dump({"focus_mode": state}, file)

# =========================
# UI LABELS
# =========================

timer_label = ctk.CTkLabel(
    app,
    text="25:00",
    font=("Arial", 70, "bold")
)
timer_label.pack(pady=20)

status_label = ctk.CTkLabel(
    app,
    text="Focus Mode Ready",
    font=("Arial", 22)
)
status_label.pack(pady=5)

camera_label = ctk.CTkLabel(
    app,
    text="",
    image=standby_image
)
camera_label.pack(pady=15)

# =========================
# CAMERA UPDATE LOOP
# =========================

def update_camera():
    global running

    if running:
        frame = get_frame()

        if frame is not None:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image = image.resize((450, 300))

            photo = ImageTk.PhotoImage(image)

            camera_label.configure(image=photo)
            camera_label.image = photo

    app.after(10, update_camera)

# =========================
# TIMER THREAD
# =========================

def countdown():
    global total_seconds, running

    while running and total_seconds >= 0:

        mins = total_seconds // 60
        secs = total_seconds % 60

        timer_label.configure(text=f"{mins:02d}:{secs:02d}")

        time.sleep(1)

        if running:
            total_seconds -= 1

# =========================
# START SESSION
# =========================

def start_session():
    global running, paused

    if not running:
        running = True
        paused = False

        set_focus_state(True)
        start_camera()

        status_label.configure(
            text="Focus Mode Active",
            text_color="green"
        )

        threading.Thread(target=countdown, daemon=True).start()

        play_pause_button.configure(image=pause_icon)

# =========================
# PAUSE / RESUME
# =========================

def pause_session():
    global running, paused

    if not running and not paused:
        start_session()
        return

    paused = not paused

    if paused:
        running = False
        set_focus_state(False)

        stop_camera()

        status_label.configure(
            text="Focus Session Paused",
            text_color="orange"
        )

        camera_label.configure(image=standby_image)
        play_pause_button.configure(image=play_icon)

    else:
        running = True
        set_focus_state(True)

        start_camera()

        status_label.configure(
            text="Focus Mode Active",
            text_color="green"
        )

        threading.Thread(target=countdown, daemon=True).start()

        play_pause_button.configure(image=pause_icon)

# =========================
# RESTART
# =========================

def restart_session():
    global total_seconds, running, paused

    running = False
    paused = False

    stop_alarm()
    stop_camera()

    total_seconds = 25 * 60

    timer_label.configure(text="25:00")
    camera_label.configure(image=standby_image)

    start_camera()
    running = True
    set_focus_state(True)

    status_label.configure(
        text="Focus Session Restarted",
        text_color="green"
    )

    threading.Thread(target=countdown, daemon=True).start()

    play_pause_button.configure(image=pause_icon)

# =========================
# BUTTON FRAME
# =========================

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

# =========================
# BUTTON SIZE FIXED
# =========================

BUTTON_SIZE = 60

play_pause_button = ctk.CTkButton(
    button_frame,
    text="",
    image=play_icon,
    width=BUTTON_SIZE,
    height=BUTTON_SIZE,
    command=pause_session,
    fg_color="transparent",
    hover_color="gray20"
)
play_pause_button.grid(row=0, column=0, padx=15)

restart_button = ctk.CTkButton(
    button_frame,
    text="",
    image=restart_icon,
    width=BUTTON_SIZE,
    height=BUTTON_SIZE,
    command=restart_session,
    fg_color="transparent",
    hover_color="gray20"
)
restart_button.grid(row=0, column=1, padx=15)

# =========================
# STOP ALARM BUTTON
# =========================

stop_alarm_button = ctk.CTkButton(
    app,
    text="STOP ALARM",
    command=stop_alarm,
    fg_color="red",
    hover_color="darkred",
    width=250,
    height=50,
    font=("Arial", 18, "bold")
)
stop_alarm_button.pack(pady=15)

# =========================
# INIT LOOP
# =========================

update_camera()

# =========================
# CLOSE HANDLER
# =========================

def on_closing():
    set_focus_state(False)
    stop_camera()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

# =========================
# RUN APP
# =========================

app.mainloop()