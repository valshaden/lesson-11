import tkinter as tk
from my_module import study_entry

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Изучение элементов GUI")
    root.geometry("600x400+700+300")
    #tk.Button(root, text="Изучение полей ввода").pack()
    tk.Button(root, text="Изучение полей ввода", command=study_entry).pack(pady=20)
    
    
    
    root.mainloop()    
    