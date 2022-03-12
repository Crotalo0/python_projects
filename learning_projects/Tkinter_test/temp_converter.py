import tkinter as tk

def converter_f_to_c():
	fahrenheit = float(ent_temperature.get())
	celsius = (5/9) * (fahrenheit - 32)
	lbl_result["text"] = f"{(celsius)} °C"
	
def converter_c_to_f():
	celsius = float(ent_temperature1.get())
	fahrenheit = celsius * (9/5) + 32
	lbl_result1["text"] = f"{(fahrenheit)} °F"

window = tk.Tk()
window.title("Temperature Converter")

frm_entry = tk.Frame(master=window)

ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="°F")

ent_temperature1 = tk.Entry(master=frm_entry, width=10)
lbl_temp1 = tk.Label(master=frm_entry, text="°C")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

ent_temperature1.grid(row=1, column=0, sticky="e")
lbl_temp1.grid(row=1, column=1, sticky="w")

btn_convert = tk.Button(master=frm_entry,text="Convert", command = converter_f_to_c)
btn_convert1 = tk.Button(master=frm_entry,text="Convert", command = converter_c_to_f)

lbl_result = tk.Label(master=frm_entry, text="°C")
lbl_result1 = tk.Label(master=frm_entry, text="°F")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=2, pady=10)
btn_convert1.grid(row=1, column=2, pady=10)
lbl_result.grid(row=0, column=3, padx=10)
lbl_result1.grid(row=1, column=3, padx=10)
 
window.mainloop()


