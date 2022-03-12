import tkinter as tk
from tkinter import ttk

def process_event(event):
  print("The process_event function was called.")
  if event.x >10 and event.y > 20 :
    print('Ok')

def key_logger():
    x = my_entry.get()
    return x 


window = tk.Tk()

#Creo contenuti nella finestrella
my_label= ttk.Label(window, text='hello world!')
my_label.grid(row=3,column=1)

my_button = tk.Button(window, text="A", command=key_logger)
my_button.grid(row=2,column=2)

my_entry = ttk.Entry(window, width=40)
my_entry.grid(row=1, column=1, sticky=tk.W, pady=3)
my_entry.insert(tk.END, "")
my_entry.bind('<Key>',process_event)

   



#Sistemo la posizione del contenuto
my_label.grid(row=1, column=1)

#Starto la GUI
window.mainloop()