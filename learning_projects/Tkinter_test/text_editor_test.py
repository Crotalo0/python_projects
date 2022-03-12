import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import askopenfilename



def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    window.title(f"Simple Text Editor - {filepath}")
    
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        
        
window = tk.Tk()
window.title("Text Editor")

window.columnconfigure(1, weight=1, minsize=800)
window.rowconfigure(0,weight=1, minsize=800)

txt_edit = tk.Text(master=window)
fr_buttons = tk.Frame(master = window, relief=tk.SUNKEN, borderwidth=3) #Frame per i pulsanti open e save
btn_open = tk.Button(master = fr_buttons, text="Open File", command=open_file)
btn_save = tk.Button(master = fr_buttons, text="Save As...", command= save_file)


btn_open.pack(padx=5, pady=5)
btn_save.pack(padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
