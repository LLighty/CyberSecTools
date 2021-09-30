import tkinter as Tk
import algorithms.algorithms as e_algorithms
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

    def encode_button(self, val):
        algorithm = self.check_algorithm()
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[0]:
            self.view.decode_text.delete('1.0', Tk.END)
            self.view.decode_text.insert(Tk.END, self.model.encode(self.get_string_to_encode(), algorithm,
                                                                   self.get_algorithm_options()))

    def decode_button(self, val):
        algorithm = self.check_algorithm()
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[0]:
            self.view.encode_text.delete('1.0', Tk.END)
            self.view.encode_text.insert(Tk.END, self.model.decode(self.get_string_to_decode(), algorithm,
                                                                   self.get_algorithm_options()))

    def check_algorithm(self):
        return self.view.choose_algorithm_value

    def get_string_to_encode(self):
        return self.view.encode_text.get("1.0", 'end-1c')

    def get_string_to_decode(self):
        return self.view.decode_text.get("1.0", 'end-1c')

    def get_algorithm_options(self):
        options = []
        for widget in self.view.algorithm_widgets:
            options.append(widget.get())
        return options
