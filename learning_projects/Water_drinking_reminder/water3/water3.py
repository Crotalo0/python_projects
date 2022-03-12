import tkinter as tk
from tkinter import IntVar, ttk
from tkinter import filedialog, messagebox
from datetime import datetime
import os.path



class water_drinking_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Drinking helper app")
        self.window.iconbitmap('water.ico')
        self.create_widgets()

        self.radio_variable = tk.StringVar()
        self.combobox_value = tk.StringVar()

    def log_file(text):
        file_log = os.path.exists("log.txt")
        if file_log != False:
            with open('log.txt','a') as f:
                f.write(text)
        else:
            with open('log.txt','w') as f:
                f.write('#File log per Bevinator.\n')
                f.write(text) 

    def create_widgets(self):

        def acqua_max():
            """calcola quanta acqua va bevuta in un giorno rispetto al peso, temperatura e allenamento fisico"""
           
            peso = float(weight_entry.get())
            workout = int(train_entry.get())
            bicchiere = int(cap_entry.get())
            fa_caldo = var1.get()
            
            drunk_number_cup["text"] = f"0"
            # lbl_result3["text"] = f""
	
            acqua_ml = peso * 30
            workout_factor = workout // 30
	
            if fa_caldo == 1:
                acqua_tot = int(acqua_ml  + acqua_ml * 0.1 + workout_factor*(acqua_ml * 0.08 ))
                tot_number_label["text"] = f"{acqua_tot}"
                rem_number_label["text"] = f"{acqua_tot}"
            else :
                acqua_tot = int(acqua_ml  + workout_factor*(acqua_ml * 0.08 ))
                tot_number_label["text"] = f"{acqua_tot}"
                rem_number_label["text"] = f"{acqua_tot}"
            water_drinking_program.log_file(f"--------------------------------------------\nWeight: {peso} kg, Workout: {workout} minutes,  Glass capacity: {bicchiere} ml, Hot(1 yes, 0 no): {fa_caldo} \n\n") 
        
        def ho_bevuto():
            """calcola quanta acqua rimane dopo aver bevuto dal bicchiere"""
            data = datetime.now()
            giorno_settimana = data.strftime("%A")

            bicchiere = int(cap_entry.get())
            acqua_rimanente = int(rem_number_label["text"])
        
            local_time = datetime.now().strftime('%H:%M:%S')
            time_number_cup["text"] = f"{local_time}"
            counter = int(drunk_number_cup["text"])
	
            if (acqua_rimanente) > bicchiere:
                acqua_rimanente = acqua_rimanente - bicchiere
                rem_number_label["text"] = f"{acqua_rimanente}"
                drunk_number_cup["text"] = f"{counter +1}"
		
            else:
                rem_number_label["text"] = f"0"
                messagebox.showinfo("Information","Well done!\nYou drank enough for today!")
                complete_label["text"] = f"You drank enough for today!"
                drinking_button.config(state="disabled")
                drunk_number_cup["text"] = f"{counter +1}"
                acqua_rimanente = 0

    
            water_drinking_program.log_file(f"Glass n.{counter+1}, Remaining water: {acqua_rimanente}, Data: {giorno_settimana}, {data.day}/{data.month}/{data.year}\n")
        
        
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # - - - - - - - - - - - - - - - - - - - - -
        # The Data entry frame
        entries_frame = ttk.LabelFrame(self.window, text="Data entry", relief=tk.RIDGE)
        entries_frame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        button_label = ttk.Label(entries_frame, text="Weight (kg): ")
        button_label.grid(row=1, column=1, sticky=tk.W, pady=3)

        button_label = ttk.Label(entries_frame, text="Training min.: ")
        button_label.grid(row=2, column=1, sticky=tk.W, pady=3)

        menu_label = ttk.Label(entries_frame, text="Glass cap. (ml): ")
        menu_label.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=3)

        weight_entry = ttk.Entry(entries_frame)
        weight_entry.grid(row=1, column=2, sticky=tk.E, pady=3, padx=3)
        weight_entry.insert(tk.END, "")

        train_entry = ttk.Entry(entries_frame)
        train_entry.grid(row=2, column=2, sticky=tk.E, pady=3, padx=3)
        train_entry.insert(tk.END, "")

        cap_entry = ttk.Entry(entries_frame)
        cap_entry.grid(row=3, column=2, sticky=tk.E, pady=3, padx=3)
        cap_entry.insert(tk.END, "")

        var1 = IntVar()
        hot_checkbutton = ttk.Checkbutton(entries_frame, text="check if hot outside", variable=var1, onvalue=True, offvalue=False )
        hot_checkbutton.grid(row=4, column=2, pady=3)

        calculate_button = ttk.Button(entries_frame, text="Calculate water to drink",command=acqua_max)
        calculate_button.grid(row=5,column=2,sticky=tk.W ,pady=3)

        # - - - - - - - - - - - - - - - - - - - - -
        # The Drink Info frame
        cup_frame = ttk.LabelFrame(self.window, text="Drink information",
                                     relief=tk.RIDGE)
        cup_frame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        drunk_cup = ttk.Label(cup_frame, text='Glass number: ')
        drunk_cup.grid(row=1, column=1, sticky=tk.W, pady=3)

        time_cup = ttk.Label(cup_frame, text='Last glass time: ')
        time_cup.grid(row=2, column=1, sticky=tk.W, pady=3)

        drunk_number_cup = ttk.Label(cup_frame, text='---')
        drunk_number_cup.grid(row=1, column=2, sticky=tk.W, pady=3)

        time_number_cup = ttk.Label(cup_frame, text='---')
        time_number_cup.grid(row=2, column=2, sticky=tk.W, pady=3)


    # - - - - - - - - - - - - - - - - - - - - -
        # The drink button frame
        button_frame = ttk.LabelFrame(self.window, text="Drink button", relief=tk.RIDGE, padding=6)
        button_frame.grid(row=2, column=2, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)

        drinking_button = ttk.Button(button_frame, text="I drank one glass! :D",command =ho_bevuto)
        drinking_button.grid(row=1, column=1,padx=25,pady=3)


        # - - - - - - - - - - - - - - - - - - - - -
        # The drinking data frame
        drink_info_frame = ttk.LabelFrame(self.window, text="Drinking data",
                                        relief=tk.RIDGE)
        drink_info_frame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S, padx=6)

        complete_label = tk.Label(drink_info_frame, text="")
        complete_label.grid(row=1, column=1, sticky=tk.W + tk.N,pady=3)

        total_water_label = tk.Label(drink_info_frame, text="Total water (ml): ")
        total_water_label.grid(row=2, column=1, sticky=tk.W + tk.N,pady=3)

        remaining_label = tk.Label(drink_info_frame, text="Remaining water (ml): ")
        remaining_label.grid(row=3, column=1, sticky=tk.W + tk.N,pady=3)

        tot_number_label = tk.Label(drink_info_frame, text="----")
        tot_number_label.grid(row=2, column=2, sticky=tk.W + tk.N,pady=3)

        rem_number_label = tk.Label(drink_info_frame, text="----")
        rem_number_label.grid(row=3, column=2, sticky=tk.W + tk.N,pady=3)

        # - - - - - - - - - - - - - - - - - - - - -
        # Menus
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open log", command=filedialog.askopenfile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.window.quit)
        menubar.add_cascade(label="log File", menu=filemenu)

        self.window.config(menu=menubar)

def main(): 
    # Create the entire GUI program
    program = water_drinking_program()
    # Start the GUI event loop
    program.window.mainloop()


if __name__=='__main__':
    main()