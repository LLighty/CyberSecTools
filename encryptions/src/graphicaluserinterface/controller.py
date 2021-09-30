import tkinter as Tk
from .view import View
from .model import Model


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.bind_widgets()

    def run(self):
        self.root.title("Encoding and Decoding different encryptions")
        self.root.deiconify()
        self.root.mainloop()

    def bind_widgets(self):
        self.view.encode_button.bind("<Button>", self.encode_button)
        self.view.decode_button.bind("<Button>", self.decode_button)

    def encode_button(self):
        None

    def decode_button(self):
        None
