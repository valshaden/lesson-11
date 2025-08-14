import tkinter as tk
from tkinter import messagebox

def study_entry():
    window = tk.Toplevel()
    window.title("Поля ввода")
    window.geometry("300x200")
    
    
    tk.Label(window, text="Имя:").pack(pady=5)
    entry1 = tk.Entry(window)
    entry1.pack(pady=5)
    
    tk.Label(window, text="Пароль:").pack(pady=5)
    entry2 = tk.Entry(window, show="*")
    entry2.pack(pady=5)
    
    #def show_values():
    #    name = entry1.get()
    #    password = entry2.get()
    #    print("Имя:", name)
    #    print("Пароль:", password)
    
    def show_values():
        messagebox.showinfo("Значения полей ввода", f"Имя: {entry1.get()}\nПароль: {entry2.get()}")
    #    name = entry1.get()
    #    password = entry2.get()
    #    print("Имя:", name)
    #    print("Пароль:", password)

    tk.Button(window, text="Показать", command=show_values).pack(pady=10)
                                       
