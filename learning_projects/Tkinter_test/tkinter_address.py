import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

window.rowconfigure([0,1,2,3,4,5,6,7], minsize=50)
window.columnconfigure(0, minsize=50)
window.columnconfigure(1, minsize=250)

frame = tk.Frame(master=window,relief = tk.SUNKEN, borderwidth=3 )
frame.pack()

frame1 = tk.Frame(master=window)
frame1.pack(side=tk.RIGHT)

button_1=tk.Button(master=frame1, text="Clear", relief=tk.RAISED, bd=2)
button_2=tk.Button(master=frame1, text="Submit", relief=tk.RAISED, bd=2)
button_1.pack(side=tk.LEFT,padx=5, pady=5)
button_2.pack(side=tk.RIGHT,padx=5, pady=5)

label_1=tk.Label(master=frame, text="First Name:", height=1)
label_2=tk.Label(master=frame, text="Last Name:", height=1)
label_3=tk.Label(master=frame, text="Address Line 1:", height=1)
label_4=tk.Label(master=frame, text="Address Line 2:", height=1)
label_5=tk.Label(master=frame, text="City:", height=1)
label_6=tk.Label(master=frame, text="State/Province:", height=1)
label_7=tk.Label(master=frame, text="Postal Code:", height=1)
label_8=tk.Label(master=frame, text="Country:", height=1)

entry_1=tk.Entry(master=frame,width=40)
entry_2=tk.Entry(master=frame,width=40)
entry_3=tk.Entry(master=frame,width=40)
entry_4=tk.Entry(master=frame,width=40)
entry_5=tk.Entry(master=frame,width=40)
entry_6=tk.Entry(master=frame,width=40)
entry_7=tk.Entry(master=frame,width=40)
entry_8=tk.Entry(master=frame,width=40)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)
entry_4.grid(row=3, column=1)
entry_5.grid(row=4, column=1)
entry_6.grid(row=5, column=1)
entry_7.grid(row=6, column=1)
entry_8.grid(row=7, column=1)

label_1.grid(row=0, column=0, sticky="e" )
label_2.grid(row=1, column=0,sticky="e")
label_3.grid(row=2, column=0,sticky="e")
label_4.grid(row=3, column=0,sticky="e")
label_5.grid(row=4, column=0,sticky="e")
label_6.grid(row=5, column=0,sticky="e")
label_7.grid(row=6, column=0,sticky="e")
label_8.grid(row=7, column=0,sticky="e")


def handle_click(event):
    print("The button was clicked!")


button_1.bind("<Button-1>", handle_click)
button_2.bind("<Button-1>", handle_click)


window.mainloop()
