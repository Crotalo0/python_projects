import tkinter as tk
import tkinter as ttk
from datetime import datetime
import os.path

from tkinter.filedialog import askopenfile

filetto = os.path.exists("log.txt")
data = datetime.now()
giorno_settimana = data.strftime("%A")

def Log(testo):
    filetto = os.path.exists("log.txt")
    if(filetto != False):
        with open('Log.txt','a') as f:
            f.write(testo)
    else:
        with open('Log.txt','w') as f:
            f.write('#File log per Bevinator.\n')
            f.write(testo)

def acqua_max():
    """calcola quanta acqua va bevuta in un giorno rispetto al peso, temperatura e allenamento fisico"""
    peso = float(entry_1.get())
    workout = int(entry_2.get())
    bicchiere = int(entry_3.get())
    fa_caldo = entry_4.get()
    label_6["text"] = f"0"
    btn_2.config(state="active")
    lbl_result3["text"] = f""
	
    acqua_ml = peso * 30
    workout_factor = workout // 30
	
    if fa_caldo == "s" :
        acqua_tot = int(acqua_ml  + acqua_ml * 0.1 + workout_factor*(acqua_ml * 0.08 ))
        lbl_result["text"] = f"{acqua_tot}"
        lbl_result2["text"] = f"{acqua_tot}"
    else :
        acqua_tot = int(acqua_ml  + workout_factor*(acqua_ml * 0.08 ))
        lbl_result["text"] = f"{acqua_tot}"
        lbl_result2["text"] = f"{acqua_tot}"
    #Log(f"-----------------------------------------------------\nLog data:{giorno_settimana}, {data.day}/{data.month}/{data.year}\n")   
    Log(f"--------------------------------------------\nPeso: {peso} kg, Workout: {workout} minuti  Capienza bicchiere: {bicchiere} ml, Caldo: {fa_caldo} \n\n") 

def ho_bevuto():
    """calcola quanta acqua rimane dopo aver bevuto dal bicchiere"""
    bicchiere = int(entry_3.get())
    acqua_rimanente = int(lbl_result2["text"])
        
    local_time = datetime.now().strftime('%H:%M:%S')
    label_5["text"] = f"Ultimo click: {local_time}"
    counter = int(label_6["text"])
	
    if (acqua_rimanente) > bicchiere:
        acqua_rimanente = acqua_rimanente - bicchiere
        lbl_result2["text"] = f"{acqua_rimanente}"
        label_6["text"] = f"{counter +1}"
		
    else:
        lbl_result2["text"] = f"0"
        lbl_result3["text"] = f"Hai bevuto abbastanza per oggi!"
        btn_2.config(state="disabled")
        label_6["text"] = f"{counter +1}"
        acqua_rimanente = 0
    
    Log(f"Bicchiere n.{counter+1}, Acqua mancante: {acqua_rimanente}, Data: {giorno_settimana}, {data.day}/{data.month}/{data.year}\n")
   
def opasd():
    """fornisce s o n all'entry sudore"""
    test = chkValue.get()
    if test == True:
        entry_4.delete(0, 2)
        entry_4.insert(0,"s")
    elif test == False:	
        entry_4.delete(0, 2)
        entry_4.insert(0,"n")

def openNewWindow():
    file = askopenfile(mode="r", filetypes=[("file di log","log.txt")])
    if file is not None:
        content= file.read()
        print(content)
        

window = tk.Tk()
window.title("Bevinator")
window.columnconfigure(0, weight=1 )
window.rowconfigure(0,weight=1)

frame = ttk.Frame(master=window)
frame1 = ttk.Frame(master=window)
frame2 = ttk.Frame(master=window)
frame3 = ttk.Frame(master=window)

#Raccolgo le informazioni necessarie per calcolare quanto bere
label_1=ttk.Label(master=frame, text="Peso (in kg): ", height=1)
label_2=ttk.Label(master=frame, text="Minuti di allenamento: ", height=1)
label_3=ttk.Label(master=frame, text="Capienza bicchiere(in ml): ", height=1)
label_4=ttk.Label(master=frame, text="Fa molto caldo?: ", height=1)
label_5=ttk.Label(master=frame3, text="", height=1)
label_6=ttk.Label(master=frame3, text="0", height=1)
label_7=ttk.Label(master=frame3, text="Bicchieri bevuti: ", height=1)

lbl_result0 = ttk.Label(master=frame2, text="Acqua da bere totale (ml): ")
lbl_result = ttk.Label(master=frame2, text="-----")
lbl_result1 = ttk.Label(master=frame2, text="Acqua mancante (ml): ")
lbl_result2 = ttk.Label(master=frame2, text="-----")
lbl_result3 = ttk.Label(master=frame2)

entry_1=ttk.Entry(master=frame, width=6)
entry_2=ttk.Entry(master=frame, width=6)
entry_3=ttk.Entry(master=frame, width=6)
entry_4=ttk.Entry(master=frame, width=6)

chkValue = tk.BooleanVar() 
chkValue.set(False)

btn_si = ttk.Checkbutton(master = frame, var=chkValue, command=opasd)
entry_4.insert(0,"n")

btn_1 = ttk.Button(master = frame1, text="Calcola acqua da bere", command=acqua_max)
btn_2 = ttk.Button(master = frame1, text="Ho Bevuto!", command=ho_bevuto)
btn_3 = ttk.Button(master = frame1, text="mostra log", command=openNewWindow)

frame.grid(row=0, column=0, sticky="wesn")
frame1.grid(row=1, column=1, sticky="swne")
frame2.grid(row=0, column=1,sticky="eswn")
frame3.grid(row=1, column=0, sticky="wesn")

btn_si.grid(row=3, column=1)

btn_1.pack(side=tk.LEFT,padx=5, pady=5)	
btn_2.pack(side=tk.RIGHT,padx=5, pady=5)
#bottone mostra log
btn_3.pack(side=tk.LEFT,padx=5, pady=5)
	
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)

label_1.grid(row=0, column=0, sticky="e",padx=5,pady=5 )
label_2.grid(row=1, column=0,sticky="e",padx=5,pady=5 )
label_3.grid(row=2, column=0,sticky="e",padx=5,pady=5 )
label_4.grid(row=3, column=0,sticky="e",padx=5,pady=5 )
label_5.grid(row=1, column=0,sticky="e",padx=10,pady=10)
label_6.grid(row=0, column=1,sticky="e",padx=10,pady=10)
label_7.grid(row=0, column=0,sticky="e",padx=10,pady=10)

lbl_result0.grid(row=2,column=2 ,pady=5,padx=10)
lbl_result.grid(row=2, column=3,pady=5, padx=10)
lbl_result1.grid(row=3, column=2,pady=5, padx=10)
lbl_result2.grid(row=3, column=3,pady=5, padx=10)
lbl_result3.grid(row=1, column=2,pady=15, padx=10)

window.mainloop()




