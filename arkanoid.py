import tkinter as tk

root = tk.Tk()
root.title("Арканоид")
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

paddle = canvas.create_rectangle(250, 350, 350, 370, fill="white")

root.mainloop()
