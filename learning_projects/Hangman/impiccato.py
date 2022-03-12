from time import sleep
import random

def pos(word,letter):
    '''Trova la posizione della lettera nella parola selezionata. '''
    counter=0
    positions = []
    for i in range(len(word)):
       if word[i] == letter:
            counter+=1
            positions.append(i)
    return positions
            

def wordHider(word):
    '''Prende una stringa e ne crea una di egual lunghezza ma composta da -.'''
    y = len(word)
    hidden = '-'*y
    return hidden

def firstLetter(word,letter):
    newStr=''
    for i in range(len(word)):
        if letter == word[i]:
            newStr += word[i]
        else:
            newStr +='-'
    return newStr

def wordReplacer(real_word,censored_word,letter):
    newStr1=''
    for i in range(len(censored_word)):
        if censored_word[i] == '-':
            if letter == real_word[i]:
                newStr1 += real_word[i]
            if letter != real_word[i]:
                newStr1+= '-'
        else:
            newStr1+=real_word[i]

    return newStr1

def wordPicker(word_file):
    '''Select a word from a list.'''
    with open(word_file) as file:
        allText = file.read()
        words = list(map(str, allText.split()))
    return random.choice(words)

def impiccato(parola):
    print('Hello, welcome to the game.')
    sleep(2)
    print('There is the word you must guess: ')
    print(wordHider(parola))
    lives=6
    while True and lives!=0:
        sleep(1)
        l1=input('Letter: ')
        if l1 not in parola:
            print(f'{l1} is not in the word.')
            lives = lives -1
            print(f'Lives: {lives}')       
        
        else:
            firstWord=firstLetter(parola, l1)
            print(firstWord)
            
            break
    if lives ==0:
        print('You did not even guess one letter right! D:')
    else:
        while '-' in firstWord and lives !=0:
            sleep(1)
            l2=input('Letter: ')
            if l2 not in parola:
                print(f'{l2} is not in the word.')
                lives = lives -1
                print(f'Lives: {lives}')

            else:
                firstWord = wordReplacer(parola, firstWord,l2)
                print(firstWord)

    if lives !=0:
        print('You Won.')
    else:
        print(f'You lost. The word was {parola}')

file_parole = 'parole.txt'
parola = wordPicker(file_parole)
impiccato(parola)
