#Progetto 4 
#Simulatore lancio dado

from random import randint

def diceRoll(low,high):
    x = randint(low,high)
    return x

def diceRollSix():
    return diceRoll(1,6)

def main():
    repeat='y'
    while repeat == 'y':
        print(f"Result of dice roll is: {diceRollSix()}.")
        repeat = input("Would you like to roll the dice again? ('y' or 'n')")

if __name__ == '__main__':
    main()       

