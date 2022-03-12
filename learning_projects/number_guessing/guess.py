#Gioco - Indovina il numero
#Progetto numero 2
from random import randint

def intPrompt(prompt):
    """Creo un sistema di input che accetta solo int.
    In caso non sia un int ritorna il prompt."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Invalid entry, please provide an integer.')
            #Return to the start of the loop
            
        else:
            #number is integer, so we proceed into the loop.
            break
    return value
 
#Serie di hint diverse da ciclare dopo i tentativi sbagliati
def hint1(n1):
    """Dato un numero n1, controllo se e' maggiore o minore di 50."""
    if n1 >= 50:
        print('Number is greater or equal to 50')
    elif n1 < 50: 
        print('Number is smaller than 50')

def hint2(n1):
    """Dato un numero n1, controllo se e' divisibile per 4"""
    if n1%4 == 0:
        print('Number is divisible for 4')
    else:
        print('Number is NOT divisible for 4')
 
def hint3(n1):
    """Dato un numero n1, controllo se e' divisibile per 5"""
    if n1%5 == 0:
        print('Number is divisible for 5')
    else:
        print('Number is NOT divisible for 5')
        
def hint4(num):
    """Dato un numero num, vedo se e' primo o no"""
    count = 0
    i=1
    
    while num >= i:
        if num % i == 0:
            count+= 1 
        i+=1
    if count >2:
        print(f'Number is NOT Prime.')
    else:
        print(f'Number is Prime.')

def hint5(num):
    if num >=80:
        print('Number is greater or equal to 80')
    elif num < 20:
        print('Number is smaller than 20')
    else:
        print('Number is between 20 and 80')
        
def hint6(num):
    if num%7 == 0:
        print('Number is divisible by 7')
    else:
        print('Number is NOT divisible for 7')

def hint7(num):
        if 20<num<50 and num < 35 :
            print('Number is smaller than 35')
        elif 20<num<50 and num>35 :
            print('Number is greater than 35')
        
        elif 50<num<80 and num<75:
            print('Number is smaller than 75')
        elif 50<num<80 and num>75:
            print('Number is greater than 75')
        if num<20 or num>80:
            if num%3 == 0:
                print('Number is divisible by 3')
            else:
                print('Number is NOT divisible for 3')

def hint8(num):
    if num%2 == 0:
        print('Number is divisible by 2')
    else:
        print('Number is NOT divisible for 2')  
        
#Finiscono le serie di hint.        

def lost(num):
    print(f'The number was {num}, you lost!')    
   
def guessing(n1):
    """Funzione che prende un guess e lo confronta con un numero n1"""
    #Prendo l'input dall'utente
    n2 = intPrompt('\nMake your guessing: ') 
    #Creo un Array con tutte le possibili hint.
    hints = [hint1,hint2,hint3,hint4,hint5,hint6,hint7,hint8]
    #Aggiorna poi il guess per riaggiornare il while.
    counter=1
    while n1 != n2 and (counter+2) <= len(hints):
        counter += 1
        print('Number is wrong. Retry again!')
        hints[counter-1](n1)
        #Richiedo il prompt dopo il nuovo hint.
        n2 = intPrompt('\nMake your guessing: ')
        
    if n1 == n2:
        print(f'Congratulations! You guessed {n2}, and it is correct!')
        print(f'Total guessing: {counter}')
    else:
        print('Number is wrong. Last try now...')
        hint8(n1)
        n2 = intPrompt('\nMake your guessing: ')
        if n1 == n2:
            print(f'Congratulations! You guessed {n2}, and it is correct!')
            print(f'Total guessing: {counter+1}')
        else:
            lost(n1)

a = 1
b = 100
print(f'\n-- -- -- --Guess the number!-- -- -- --\n\nTry to guess the number in a range from {a} to {b}.')
x = randint(a,b)
hint1(x)

guessing(x)












    
    

    




    










