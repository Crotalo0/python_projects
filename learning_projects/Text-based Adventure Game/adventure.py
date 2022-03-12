#Text-based Adventure Game Idea
#Progetto numero 3 

from time import sleep

#Zona funzioni
def inputMethod_cage(prompt):
    """Un comando input con delle funzioni specifiche."""
    #Creo un array con i comandi legali possibili.
    cage_commands = ['intro','help','watchAround','north','south','east','ovest'] 
    
    answer = input(prompt)
    ans = answer.lower()
    
    #Controllo se la parola scritta dall'utente e' nella lista dei comandi validi per il gioco.
    if ans in cage_commands:
        #Assegno a command_pos il valore della posizione del comando nell'array
        command_pos =cage_commands.index(ans)
        com_pos = int(command_pos)
        #Richiamo la funzione in base alla posizione nell'array
        print(com_pos)
        
        
   

def intro():
    print("""
    ---+---+---+---+---+---
    Welcome to the Text-based Adventure Game!
    Let's start with the story...
    
    You are in an old and small cage.
    (If you need help write help)
    """) 
   
    c1 = inputMethod_cage('What do you do? ')
    sleep(2)
  
def help():
    print("""
    This is an adventure game controlled only with words.
    There is no fixed objective, the story will be decided by your actions.
    For example, you can decide to watch around the cage by writing 'watch around'.
    The program doesn't care if it is written in uppercase or lowercase.
    Then try guessing and find out new things!
    """)    
 
def watchAround():
    print('Ok')

def north():
    print('Ok')

def south():
    print('Ok')

def east():
    print('Ok')

def ovest():
    print('Ok')    
        # elif c1.upper() == 'WATCH AROUND':
            # print("""   
    # You decide to watch around you.
    # The first thing you notice is the disgusting state of the cage.
    # There are insects everywhere, rats escrements and other nasty things.
            
    # You see a rusty cage door north to you.
    # To the south, behind you, there is a dead body firmly secured with chain to the wall.
    # To the east, there is only a wall with ruined blocks,
    # To the west there are some rats wandering.
    # """)
            # ans = 'correct'
            # c1 = input('What do you do? ')
            
        # else:
            # print('Sorry, your input is not valid.')
            # c1 = input('What do you do? ')
#Fine zona funzioni  


#Inizio programma

#Lista dei comandi possibili

hello = inputMethod_cage('EWEEW ')










    