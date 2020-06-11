# throwing system notification using subprocess model
import subprocess
import emoji


def notify(title, message, timeout):
    subprocess.Popen(['notify-send', title, message, '-t'])


notify("Tip", "Stop wasting your time on watching tough videos", 1000)

