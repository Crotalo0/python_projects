#Reminder tests per app bere
import time 

remind = input("che devo remindare?  ")
time_min = float(input("E fra quanti minuti?  "))
time_sec = time_min * 60
print("Ti reminderò in: ",time_min, "minuti.")
time.sleep(time_sec)
print(remind)



