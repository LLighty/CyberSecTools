import tkinter as tk
from algorithms.algorithms import IMPLEMENTED_ALGORITHMS


class View:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.encode_text = None
        self.decode_text = None
        self.encode_button = None
        self.decode_button = None
        self.choose_algorithm = None
        self.choose_algorithm_value = None
        self.algorithm_widgets = []
        self.main_frame = self.create_main_frame(master)
        self.side_bar = self.create_side_panel(master)
        self.create_algorithm_widget(IMPLEMENTED_ALGORITHMS[0], self.side_bar)

    def create_main_frame(self, root):
        main_frame = tk.Frame(root, bg='#CCC', width=500, height=500)
        self.encode_text = tk.Text(main_frame)
        self.decode_text = tk.Text(main_frame)
        self.encode_text.pack(expand=True, fill='both')
        self.decode_text.pack(expand=True, fill='both')
        main_frame.pack(expand=True, fill='both', side='left')
        return main_frame

    def create_side_panel(self, root):
        side_bar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
        self.encode_button = tk.Button(side_bar, width=10, text="Encode")
        self.decode_button = tk.Button(side_bar, width=10, text="Decode")
        algorithm_options = tk.StringVar(side_bar)
        algorithm_options.set(IMPLEMENTED_ALGORITHMS[0])
        self.choose_algorithm_value = IMPLEMENTED_ALGORITHMS[0]
        self.choose_algorithm = tk.OptionMenu(side_bar, algorithm_options, *IMPLEMENTED_ALGORITHMS, command=self.update_selected_algorithm)
        self.encode_button.pack(side=tk.TOP, pady=200)
        self.choose_algorithm.pack()
        self.decode_button.pack(side=tk.BOTTOM, pady=200)
        side_bar.pack(expand=False, fill='both', side='right', anchor='nw')
        return side_bar

    # Creates the widget needed for the algorithm. For example a text box asking the number of rotations for Caesar
    # Cipher.
    def create_algorithm_widget(self, algorithm, master):
        self.clear_algorithm_widgets()
        if algorithm == IMPLEMENTED_ALGORITHMS[0]:
            self.algorithm_widgets = []
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
            for widget in self.algorithm_widgets:
                widget.pack()
        if algorithm == IMPLEMENTED_ALGORITHMS[1]:
            self.algorithm_widgets = []
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
            for widget in self.algorithm_widgets:
                widget.pack()

    def clear_algorithm_widgets(self):
        for widget in self.algorithm_widgets:
            widget.destroy()

    def update_selected_algorithm(self, value):
        self.choose_algorithm_value = value
        self.create_algorithm_widget(value, self.side_bar)
