import tkinter as Tk
import algorithms.algorithms as e_algorithms
from .view import View, SubPopupWindow
from .model import Model


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.bind_widgets()
        self.sub_popup_active = False
        self.sub_alphabet = {}

    def run(self):
        self.root.title("Encoding and Decoding different encryptions")
        self.root.deiconify()
        self.root.mainloop()

    def bind_widgets(self):
        self.view.encode_button.bind("<Button>", self.encode_button)
        self.view.decode_button.bind("<Button>", self.decode_button)
        self.view.algorithm_options.trace('w', self.update_algorithm_options)

    def encode_button(self, val):
        self.view.decode_text.delete('1.0', Tk.END)
        algorithm = self.check_algorithm()
        algorithm_options = self.get_algorithm_options()
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[2]:
            algorithm_options.append(self.sub_alphabet)
        self.view.decode_text.insert(Tk.END, self.model.encode(self.get_string_to_encode(), algorithm,
                                                               algorithm_options))

    def decode_button(self, val):
        self.view.encode_text.delete('1.0', Tk.END)
        algorithm = self.check_algorithm()
        algorithm_options = self.get_algorithm_options()
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[2]:
            algorithm_options.append(self.sub_alphabet)
        self.view.encode_text.insert(Tk.END, self.model.decode(self.get_string_to_decode(), algorithm,
                                                               algorithm_options))

    def update_algorithm_options(self, *args):
        self.view.choose_algorithm_value = self.view.algorithm_options.get()
        self.view.create_algorithm_widget(self.view.algorithm_options.get(), self.view.side_bar)
        self.check_binds(self.view.algorithm_options.get())

    def check_binds(self, algorithm):
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[2]:
            self.view.algorithm_widgets[0].bind("<Button>", self.create_sub_popup_window)

    def check_algorithm(self):
        return self.view.choose_algorithm_value

    def get_string_to_encode(self):
        return self.view.encode_text.get("1.0", 'end-1c')

    def get_string_to_decode(self):
        return self.view.decode_text.get("1.0", 'end-1c')

    def get_algorithm_options(self):
        options = []
        for widget in self.view.algorithm_widgets:
            try:
                options.append(widget.get())
            except AttributeError as e:
                None
        return options

    def create_sub_popup_window(self, *args):
        if not self.sub_popup_active:
            sub_popup_window = SubPopupWindow(self)
            self.sub_popup_active = True
