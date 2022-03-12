import tkinter as tk
from tkinter import ttk, messagebox
#Creo la finestrella
window = tk.Tk()

#Creo contenuti nella finestrella
my_label= ttk.Label(window, text='hello world!')

#Error popup
messagebox.showinfo("Information","Informative message")
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")

#Yes/no questions (return is boolean and None if 'cancel' button selected.)
answer = messagebox.askokcancel("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")

#SIstemo la posizione del contenuto
my_label.grid(row=1, column=1)

#Starto la GUI
window.mainloop()