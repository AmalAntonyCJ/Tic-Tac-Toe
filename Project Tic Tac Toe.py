
import random
Computer = '0'
Player   = 'X'

Board = [' '] * 10

def display_board (Board):
    print (f'{Board [1]} | {Board [2]} | {Board [3]}')
    print (f'{Board [4]} | {Board [5]} | {Board [6]}')
    print (f'{Board [7]} | {Board [8]} | {Board [9]}')
    print ('-' * 10)

def check ():
    if  Board [1] == Board [2] == Board [3] and Board [1] != ' ':
            return True
    elif Board [4] == Board [5] == Board [6] and Board [4] != ' ':
            return True
    elif Board [7] == Board [8] == Board [9] and Board [7] != ' ':
            return True
    elif Board [1] == Board [4] == Board [7] and Board [1] != ' ':
            return True
    elif Board [2] == Board [5] == Board[8] and Board [2] != ' ':
            return True
    elif Board [3] == Board [6] == Board [9] and Board [3] != ' ':
            return True
    elif Board [1] == Board [5] == Board [9] and Board [1] != ' ':
            return True
    elif Board [7] == Board [5] == Board [3] and Board [7] != ' ':
        return True
    else :
        return False
    
def is_available(pos):
    return True if Board [pos] == ' ' else False

def insert(letter,pos):
    if is_available(pos):
        Board [pos] = letter
        display_board (Board)
        if check ():
            if letter == 'X':
                print('Player win')
            else:
                print('Computer win')
                exit()
        

def human_move(letter):
    pos = random.randint(1,9)
    insert(letter,pos)

def computer_move(letter):
    pos = random.randint(1,9)
    insert(letter,pos)

while not check ():

    display_board (Board)
    computer_move(Computer)
    human_move(Player)
