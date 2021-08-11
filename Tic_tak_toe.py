# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def display_board(board):
    print('\n'*100)
    print(f"""{board[0]} | {board[1]} | {board[2]}\n--|---|--
{board[3]} | {board[4]} | {board[5]}\n--|---|--
{board[6]} | {board[7]} | {board[8]}""")
    
def player_input():
#sym represents the marker X or O
    sym=' '
    
    while sym!='X' and sym!='O':
        sym = input('Player 1, choose between X and O: ')
    player1 = sym
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'Player 1 has chosen {player1} and Player 2 is {player2}.')
    return (player1, player2) 

def place_marker(board, marker, position):
    
    board[position-1] = marker
    
def win_check(board, mark):
    
    if board[0]==mark and board[1]==mark and board[2]==mark:
        return True
    elif board[3]==mark and board[4]==mark and board[5]==mark:
        return True
    elif board[6]==mark and board[7]==mark and board[8]==mark:
        return True
    elif board[0]==mark and board[3]==mark and board[6]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[0]==mark and board[4]==mark and board[8]==mark:
        return True
    elif board[2]==mark and board[4]==mark and board[6]==mark:
        return True
    else:
        return False
    
from random import randint

def choose_first():
    player = randint(1,2)
    print(f'Player {player} will start first!')
    return player

def space_check(board, position):
    
    if board[position-1] == ' ':
        return True
    else:
        return False
    
def full_board_check(board):
    
    for x in board:
        if x == ' ':
            return False
        else:
            return True
        
def player_choice(board):
    
    position = int(input('Enter your next move: '))
    if space_check(board,position) == True:
        return position
    else:
        print('Position already occupied. Try again.')
        position = int(input('Enter your next move: '))
        return position
    
def replay():
    
    play_again = input('Do you want to play another match? Type in Yes or No: ')
    if play_again == 'Yes'.lower():
        return True
    else:
        return False
    

print('Welcome to Tic Tac Toe!')

board=[' ']*9
new = True

while full_board_check(board) == False:
    while new == True:
        player1_marker,player2_marker = player_input()
        player = choose_first()
        display_board(board)
        new = False
    
    #player 1
    while player == 1:
        position = player_choice(board)
        place_marker(board,player1_marker,position)
        display_board(board)
        player=2
        break
        
    if win_check(board,player1_marker) == True:
        print('Player 1 has won!')
        if replay() == True:
            board=[' ']*9
            new = True
        else:
            print('Thank you for playing Tic Tak Toe!')
            break
    else:
        pass
    
    #player 2
    while player == 2:
        position = player_choice(board)
        place_marker(board,player2_marker,position)
        display_board(board)
        player=1
        break
        
    if win_check(board,player2_marker) == True:
        print('Player 2 has won!')
        if replay() == True:
            board=[' ']*9
            new = True
        else:
            print('Thank you for playing Tic Tak Toe!')
            break
    else:
        pass





