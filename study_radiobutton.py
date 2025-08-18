import tkinter as tk
from tkinter import messagebox

def study_radio():

    window = tk.Tk()
    window.title("Радио кнопки")
    window.geometry("300x200")

    var = tk.StringVar(value="python")

    tk.Label(text="Выберите язык программирования:").pack()
    tk.Radiobutton(text="Python", variable=var, value="Python").pack()
    tk.Radiobutton(text="Java", variable=var, value="Java").pack()
    tk.Radiobutton(text="C++", variable=var, value="C++").pack()

    def show_value():
        messagebox.showinfo("Результат", f"Выбран язык: {var.get()}")

    tk.Button(window, text="Показать", command=show_value).pack(pady=10)

#window.mainloop()
