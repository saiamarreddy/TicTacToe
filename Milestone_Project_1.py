import os
def init_msg():
    print '                            Welcome to Tic Tac Toe game!!!                      ' 
    print '                         ***********************************                    '
    print "Two players are allowed.                                                        "
    print "Player 1's input is printed as 'X' on the board                                 "
    print "Player 2's input is printed as 'O' on the board                                 "
    print "Enter a number between 0-8, here 0 corresponds to first cell and 8 to the last  "
    print "Type 'q' and hit enter to quit the game at any point of time!!!                 "

def take_input():
    while True:
        inp = raw_input('Player' + turn + "'s Turn:")
        if  inp == 'q':
            quit_game()
        try:
            inp = int(inp)
        except ValueError:
            print 'Invalid input, Only positive integers between 0-8 are allowed'
        else:
            if validate_inp(inp):
                break
        continue

def validate_inp(inp):
        if inp >= 0 and inp <= 8:
            if b[inp] == 'X' or b[inp] == 'O':
                # print 'Input is a duplicate on the board, please reenter valid input'
                print "That cell is already occupied, I can't believe you can't read the board"
                print "What are you? four year old? Try some empty cell, dumbo!!!"
                return False
            elif turn == '1':
                b[inp] = 'X'
                return True
            else:
                b[inp] = 'O'
                return True
        else:
            print 'Invalid input, Only positive integers between 0-8 are allowed'
            return False
    
def check_win():
    if b[4] in('X','O') :
        if b[1] == b[4] == b[7] or b[3] == b[4] == b[5]:
            return '1'
        elif b[0] == b[4] == b[8] or b[2] == b[4] == b[6]:
            return '1'
    if b[0] in('X','O'):
        if b[0] == b[1] == b[2] or b[0] == b[3] == b[6]:
            return '1'
    if b[8] in('X','O'):
        if b[6] == b[7] == b[8] or b[2] == b[5] == b[8]:
            return '1'
    return '0'

def check_tie():
    for i in range(len(b)):
        if b[i] == ' ':
            return '0'
    return '2'
            
def clear():
    os.system('cls')

def print_board():
    print '                                   ' + b[0] + '| ' + b[1] + '|' + b[2] + '                  '
    print '                                ____|__|____                                    '
    print '                                   ' + b[3] + '| ' + b[4] + '|' + b[5] + '                  '
    print '                                ____|__|____                                    '
    print '                                   ' + b[6] + '| ' + b[7] + '|' + b[8] + '                  '
    print '                                    |  |                                        '

def print_msg(cw,turn):
    if cw == '1' :
        if turn == '1':
            print 'Player 1: You have won, congratulations!!!'
            print 'Player 2: Sorry,  Better luck next time!!!'
        else:
            print 'Player 2: You have won, congratulations!!!'
            print 'Player 1: Sorry,  Better luck next time!!!'
    elif cw == '2':
        print 'The game is a tie, well played!!!'
    
def return_game():
    end_of_game = raw_input("Enter 'y' to continue the game, or enter any character to quit")
    if end_of_game.upper() == 'Y':
        clear()
        init_msg()
    else: quit_game()

def quit_game():
    print 'Quitting the game, Have a nice day!!!' 
    quit()
    
    
init_msg()
b = [' '] * 9
turn = '1'
inp = 0

while True:
    take_input()
    print_board()
    cw=check_win()
    if cw == '0':
        cw=check_tie()
    print_msg(cw,turn)
    if cw in('1','2'):
        return_game()       
        b = [' '] * 9
        turn = '0'
        inp = 0
    if turn == '1':
        turn = '2'
    else:
        turn = '1'
    continue
