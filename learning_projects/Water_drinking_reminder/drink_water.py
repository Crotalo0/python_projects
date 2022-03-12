#Provo a creare uno script per ricordarmi di bere acqua.
import time
from plyer import notification

peso = float(input("Quanto pesi? (in kg):  "))
workout = int(input("Quanto ti sei allenato? (in minuti):  "))
bicchiere = int(input("Quanto è capiente il tuo bicchiere? (in ml):  "))
fa_caldo = input("Sudi tanto per il caldo? (y/n):  ")

print("Pesi",peso,"kg.")
print("Ti sei allenato",workout,"minuti.")

acqua_ml = peso * 30
workout_factor = workout // 30

if fa_caldo == "y" :
	acqua_tot = acqua_ml  + acqua_ml * 0.1 + workout_factor*(acqua_ml * 0.08 )
	print("Devi bere",acqua_tot,"millilitri.") 
elif fa_caldo == "n" :
	acqua_tot = acqua_ml  + workout_factor*(acqua_ml * 0.08 )
	print("Devi bere",acqua_tot,"millilitri.")	
	
while acqua_tot >= 0 :
	bevuto = input("hai bevuto? (y/n):  ")
	if bevuto == "y" :
		notification.notify(title = "BEVINATOR", message = "Bevi, non dimenticarti!", timeout = 100)
		time.sleep(60*60)
		acqua_tot = acqua_tot - bicchiere
		print("Mancano",acqua_tot, "millilitri.")
	else:
		print("E che aspetti? D:")

notification.notify(title = "BEVINATOR", message = "Ottimo! Hai bevuto il necessario per oggi!", timeout = 100)		
print("Hai bevuto abbastanza!")	



	
