from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from turtle import bgcolor

root = ttk.Tk()
root.geometry("400x450")
root.title("Gestor BBDD")
root.resizable(False, False)
root.iconbitmap(r"C:\Users\manu-\Desktop\Python\practica\favi.ico")
root.config(background="#454545")

miFrame = ttk.Frame(root)

miFrame.pack()

miFrame.config(background="#454545", pady=20)


cuadroID = ttk.Entry(miFrame)
cuadroID.grid(row=0, column=1)
cuadroID.configure(bg="#999999")
labelID = Label(miFrame, text="ID:")
labelID.grid(row=0, column=0, sticky="e", padx=10, pady=10)
labelID.config(bg="#454545", fg="white")

root.mainloop()