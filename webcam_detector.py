import cv2
import time

from alarm import play_alarm, stop_alarm

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = None

focus_lost_start = None
focus_return_start = None

alarm_triggered = False

camera_running = False

# =========================
# START CAMERA
# =========================
def start_camera():

    global cap
    global camera_running

    cap = cv2.VideoCapture(0)

    camera_running = True

# =========================
# STOP CAMERA
# =========================
def stop_camera():

    global cap
    global camera_running

    camera_running = False

    if cap is not None:
        cap.release()

# =========================
# GET FRAME
# =========================
def get_frame():

    global focus_lost_start
    global focus_return_start
    global alarm_triggered

    if not camera_running or cap is None:
        return None

    ret, frame = cap.read()

    if not ret:
        return None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # =========================
    # FACE DETECTED
    # =========================
    if len(faces) > 0:

        focus_lost_start = None

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        cv2.putText(
            frame,
            "FOCUSED",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Auto stop alarm after 5s focused
        if alarm_triggered:

            if focus_return_start is None:
                focus_return_start = time.time()

            focused_time = time.time() - focus_return_start

            if focused_time >= 5:

                stop_alarm()

                alarm_triggered = False

                focus_return_start = None

        else:
            focus_return_start = None

    # =========================
    # NO FACE
    # =========================
    else:

        focus_return_start = None

        if focus_lost_start is None:
            focus_lost_start = time.time()

        elapsed = time.time() - focus_lost_start

        cv2.putText(
            frame,
            f"FOCUS LOST: {int(elapsed)}s",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        # Trigger alarm after 5 sec
        if elapsed >= 5 and not alarm_triggered:

            play_alarm()

            alarm_triggered = True

    return frame