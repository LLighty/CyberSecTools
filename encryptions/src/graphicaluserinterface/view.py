import tkinter as tk
from tkinter import messagebox
import random
from algorithms.algorithms import IMPLEMENTED_ALGORITHMS


class View:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.encode_text = None
        self.decode_text = None
        self.encode_button = None
        self.decode_button = None
        self.choose_algorithm = None
        self.algorithm_options = None
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
        self.algorithm_options = tk.StringVar(side_bar)
        self.algorithm_options.set(IMPLEMENTED_ALGORITHMS[0])
        self.choose_algorithm_value = IMPLEMENTED_ALGORITHMS[0]
        self.choose_algorithm = tk.OptionMenu(side_bar, self.algorithm_options, *IMPLEMENTED_ALGORITHMS)
        #                                              command=self.update_selected_algorithm)
        self.encode_button.pack(side=tk.TOP, pady=200)
        self.choose_algorithm.pack()
        self.decode_button.pack(side=tk.BOTTOM, pady=200)
        side_bar.pack(expand=False, fill='both', side='right', anchor='nw')
        return side_bar

    # Creates the widget needed for the algorithm. For example a text box asking the number of rotations for Caesar
    # Cipher.
    def create_algorithm_widget(self, algorithm, master):
        self.clear_algorithm_widgets()
        self.algorithm_widgets = []
        if algorithm == IMPLEMENTED_ALGORITHMS[0]:
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
        if algorithm == IMPLEMENTED_ALGORITHMS[1]:
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
        if algorithm == IMPLEMENTED_ALGORITHMS[2]:
            self.algorithm_widgets.append(tk.Button(master, bd=2, text="Set Alphabet"))
        if algorithm == IMPLEMENTED_ALGORITHMS[3]:
            self.algorithm_widgets.append(tk.Label(master, bd=2, text="Private Key"))
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
            self.algorithm_widgets.append((tk.Label(master, bd=2, text="Public Key")))
            self.algorithm_widgets.append(tk.Entry(master, bd=2))
            self.algorithm_widgets.append(tk.Button(master, bd=2, text="Randomise Keys"))
        for widget in self.algorithm_widgets:
            widget.pack()

    def clear_algorithm_widgets(self):
        for widget in self.algorithm_widgets:
            widget.destroy()


class SubPopupWindow:
    def __init__(self, controller):
        self.controller = controller
        self.frame = tk.Tk()
        self.frame.title("Substitution Alphabet")
        self.frame.protocol("WM_DELETE_WINDOW", self.close)
        self.labels = []
        self.entries = []
        self.main_frame = self.create_main_frame(self.frame)
        self.main_frame.pack()
        self.save_frame = self.create_save_frame(self.frame)
        self.characters_not_used = {}

    def create_main_frame(self, root):
        main_frame = tk.Frame(root)
        row = 0
        col = 0
        current_character = 'a'
        for i in range(26):
            if i % 7 == 0:
                row += 1
                col = 0
            self.labels.append(tk.Label(main_frame, text=current_character))
            self.labels[i].grid(row=row, column=col)
            col += 1
            self.entries.append(tk.Entry(main_frame, bd=2))
            self.entries[i].grid(row=row, column=col)
            col += 1
            current_character = chr(ord(current_character) + 1)
        return main_frame

    def create_save_frame(self, root):
        save_frame = tk.Frame(root)
        randomise_button = tk.Button(root, text="Randomise", command=self.randomise_command)
        save_button = tk.Button(root, text="Save", command=self.save_command)
        randomise_button.pack()
        save_button.pack()
        return save_frame

    def save_command(self):
        self.controller.sub_alphabet = {}
        current_character = 'a'
        for i in range(26):
            self.controller.sub_alphabet[current_character] = self.entries[i].get()[:1]
            current_character = chr(ord(current_character) + 1)
        if not self.check_all_characters():
            print("You did not specify all characters of the alphabet, each character needs a unique substitution")
            self.controller.sub_alphabet = {}
            message = messagebox.showinfo("info", self.get_message_box_content())
            return
        print("Save was successful")
        self.close()

    def check_all_characters(self):
        current_char = 'a'
        for i in range(26):
            if current_char not in self.controller.sub_alphabet.values():
                return False
            current_char = chr(ord(current_char) + 1)
        return True

    def randomise_command(self):
        not_used_characters = []
        current_char = 'a'
        for i in range(26):
            not_used_characters.append(current_char)
            current_char = chr(ord(current_char) + 1)
        current_index = 0
        while len(not_used_characters) > 0:
            random_char_index = random.randint(0, len(not_used_characters)-1)
            self.entries[current_index].delete(0, tk.END)
            self.entries[current_index].insert(0, not_used_characters[random_char_index])
            not_used_characters.remove(not_used_characters[random_char_index])
            current_index += 1

    def get_message_box_content(self):
        message = "Characters which still need to be entered: {0}".format(self.get_not_entered_characters())
        return message

    def get_not_entered_characters(self):
        not_entered_characters = []
        current_char = 'a'
        for i in range(26):
            if current_char not in self.controller.sub_alphabet.values():
                not_entered_characters.append(current_char)
            current_char = chr(ord(current_char) + 1)
        return not_entered_characters

    def close(self):
        for label in self.labels:
            label.destroy()
        for entry in self.entries:
            entry.destroy()
        self.main_frame.destroy()
        self.save_frame.destroy()
        self.frame.destroy()
        self.controller.sub_popup_active = False
