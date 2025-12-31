import tkinter as tk
from tkinter import messagebox

class MainWindow:

    def __init__(self, master, check_callback):
        self.master = master
        self.check_callback = check_callback
        self.popup = None
        self.answer_entry = None


    def show_popup(self, word, translation):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Пора хардворкинга!!")
        self.popup.attributes("-topmost", True)
        self.popup.protocol("WM_DELETE_WINDOW", self.finish_and_next)

        screen_width = self.popup.winfo_screenwidth()
        screen_height = self.popup.winfo_screenheight()
        width = screen_width//8
        height = screen_height//8

        x = screen_width - width -20
        y = 20

        self.popup.geometry(f'{width}x{height}+{x}+{y}')

        tk.Label(self.popup, text=f"Слово: {word}", font=("Arial", 10, "bold")).pack(pady=5)

        self.answer_entry = tk.Entry(self.popup)
        self.answer_entry.pack(pady=5, padx=10)
        self.answer_entry.focus_set()
        self.answer_entry.bind("<Return>", lambda e: self.on_submit(translation))

        self.result_label = tk.Label(self.popup, text="", font=("Arial", 9))
        self.result_label.pack(pady=5)

        self.action_btn = tk.Button(self.popup, text="Проверить", command=lambda: self.on_submit(translation))
        self.action_btn.pack(pady=5)

    def on_submit(self, correct_answer):
        user_answer = self.answer_entry.get().strip().lower()
        true_answer = str(correct_answer).strip().lower()
        print(f"DEBUG: Введено: '{user_answer}', Должно быть: '{true_answer}'")
        if user_answer == true_answer:
            self.result_label.config(text="✅ Верно!", fg="green")

        else:
            self.result_label.config(text=f"❌ Ошибка!\nПравильный перевод: {correct_answer}", fg="red")

        self.action_btn.config(state="disabled")
        self.answer_entry.config(state="disabled")

    def finish_and_next(self):
        if self.popup:
            self.popup.destroy()
            self.popup = None
        if self.check_callback:
            self.check_callback()