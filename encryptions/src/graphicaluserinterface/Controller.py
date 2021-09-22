import tkinter as Tk
from .View import View
from .Model import Model


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)

    def run(self):
        self.root.title("Encoding and Decoding different encryptions")
        self.root.deiconify()
        self.root.mainloop()
