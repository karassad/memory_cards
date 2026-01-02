#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from data_managers.csv_manager import CSVManager
from view.main_window import MainWindow

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.manager = CSVManager("words.csv")
        self.view = MainWindow(self.root, self.schedule_next)

        self.interval = 20*60*1000
        self.schedule_next()
        self.root.mainloop()

    def schedule_next(self):
        self.root.after(self.interval, self.show_word)

    def show_word(self):
        display, hidden, mode = self.manager.get_random_word()
        self.view.show_popup(display, hidden, mode)

if __name__ == "__main__":
    App()