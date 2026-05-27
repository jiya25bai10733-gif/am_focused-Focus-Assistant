import time

def start_timer(minutes):

    seconds = minutes * 60

    while seconds:

        mins = seconds // 60
        secs = seconds % 60

        timer = f"{mins:02d}:{secs:02d}"

        print(timer, end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nSession Complete!")