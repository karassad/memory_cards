import tkinter as tk
from tkinter import messagebox

class MainWindow:

    def __init__(self, master, check_callback):
        self.master = master
        self.check_callback = check_callback
        self.popup = None
        self.current_display = ""
        self.current_hidden = ""

        self.color_yellow = "#fff9c4"  # Светло-желтый
        self.color_yellow_dark = "#fff176"  # Насыщенный желтый
        self.color_blue = "#e1f5fe"  # Светло-голубой
        self.color_blue_dark = "#b3e5fc"  # Насыщенный голубой


    def show_popup(self, display_text, hidden_text, mode):
        self.current_display = display_text
        self.current_hidden = hidden_text

        self.popup = tk.Toplevel(self.master)
        self.popup.title("Пора хардворкинга!!")
        self.popup.attributes("-topmost", True)
        self.popup.protocol("WM_DELETE_WINDOW", self.finish_and_next)
        self.popup.config(bg="white")

        screen_width = self.popup.winfo_screenwidth()
        screen_height = self.popup.winfo_screenheight()
        width = screen_width//7
        height = screen_height//10

        x = screen_width - width -30
        y = 30

        self.popup.geometry(f'{width}x{height}+{x}+{y}')

        self.card_btn = tk.Button(
            self.popup,
            text=self.current_display,
            font=("Verdana", 16, "bold"),
            bg=self.color_yellow,
            activebackground=self.color_yellow_dark,  # Цвет при клике
            relief="flat",  # Плоский вид без серых рамок
            bd=0,
            wraplength=200,
            command=self.flip_card
        )
        self.card_btn.pack(expand=True, fill='both', padx=10, pady=10)

        # tk.Label(self.popup, text="Нажми, чтобы перевернуть", font=("Arial", 16, "italic")).pack(pady=5)

    def flip_card(self):
        self.current_display, self.current_hidden = self.current_hidden, self.current_display
        self.card_btn.config(text=self.current_display)

        if self.card_btn.cget("bg") == self.color_yellow:
            self.card_btn.config(
                bg=self.color_blue,
                activebackground=self.color_blue_dark
            )
        else:
            self.card_btn.config(
                bg=self.color_yellow,
                activebackground=self.color_yellow_dark
            )

    def finish_and_next(self):
        if self.popup:
            self.popup.destroy()
            self.popup = None
        if self.check_callback:
            self.check_callback()