import tkinter as tk
import random

def rolling():
	lbl_value["text"] = f"{random.randint(1,6)}"

window = tk.Tk()

window.rowconfigure([0,1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn_roll = tk.Button(master=window, text="Roll", width=15,height=3,command=rolling, relief=tk.RAISED, borderwidth=2 )
btn_roll.grid(row=0,column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=1, column=0)

window.mainloop()

