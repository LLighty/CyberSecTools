import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


start_stop_clicker_key = KeyCode(char='a')
stop_key = KeyCode(char='s')
mouse = Controller()


class AutoClicker(threading.Thread):
    def __init__(self, delay, button):
        super(AutoClicker, self).__init__()
        self.delay = delay
        self.mouse_button = button
        self.click_running = False
        self.program_running = True

    def begin_clicking(self):
        self.click_running = True

    def end_clicking(self):
        self.click_running = False

    def exit(self):
        self.end_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.click_running:
                mouse.click(self.mouse_button)
                time.sleep(self.delay)
            time.sleep(0.1)


clicker = AutoClicker(0.1, Button.left)
clicker.start()


def on_press(key):
    if key == start_stop_clicker_key:
        if clicker.click_running:
            clicker.end_clicking()
        else:
            clicker.begin_clicking()
    elif key == stop_key:
        clicker.exit()
        listener.stop()


listener = Listener(on_press=on_press)
listener.start()
listener.join()
