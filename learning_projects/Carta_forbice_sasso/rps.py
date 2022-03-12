# Rock paper scissors game.
from random import choice
from time import sleep


def game():
    rps_list = ['rock', 'paper', 'scissors']
    rps_random = choice(rps_list)
    rps_user = input('Make your guess(rock, paper or scissors): ').lower()
    print(f'Computer guessed {rps_random}, you guessed {rps_user}.')

    if rps_user != 'rock' and rps_user != 'paper' and rps_user != 'scissors':
        return 'Not a valid entry.'

    sleep(2)

    if rps_random == 'rock':
        if rps_user == 'rock':
            return 'tie.'
        elif rps_user == 'paper':
            return 'User won.'
        else:
            return 'Computer won.'

    if rps_random == 'paper':
        if rps_user == 'paper':
            return 'tie.'
        elif rps_user == 'scissors':
            return 'User won.'
        else:
            return 'Computer won.'

    if rps_random == 'scissors':
        if rps_user == 'scissors':
            return 'tie.'
        elif rps_user == 'rock':
            return 'User won.'
        else:
            return 'Computer won.'


print(game())
