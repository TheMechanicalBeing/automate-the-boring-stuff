import subprocess
import time


if __name__ == "__main__":
    time_to_pass = 60
    while time_to_pass:
        time_to_pass -= 1
        print(f"Time left {time_to_pass}")
        time.sleep(1)

    subprocess.Popen(["start", "alarm.wav"], shell=True)
