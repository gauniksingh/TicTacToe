from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print (board[7] + '|' + board[8] + '|' + board[9])
    print (board[4] + '|' + board[5] + '|' + board[6])
    print (board[1] + '|' + board[2] + '|' + board[3])

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
test_board = ['#','X ','O','X','O','X','O','X','O','X']
'''
def input_user():
    
    within_range = False
    player = 1
    choice = 'WRONG'

    while choice.isdigit() == False or within_range == False:
        choice = input(f"Player {player} Please enter a number between 1-9:\t")

        if choice.isdigit() == False:
            print('This is not a digit!\n')
       
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
                player = player+1
            else:
                within_range = False
                print(f'{choice} is not between 1 and 9')
    return int(choice)
'''

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position between (1-9)'))
    
    return position



def player_input():
    marker=''
    while marker != 'X' and marker!= 'O':
        marker = input('Choose X or O:  ')

        player1 = marker

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        
    return (player1,player2)


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        else:
            return True


def replay():
    choice = input("Play Again? Yes or no:\t")

    return choice == 'Yes'

print('\nWelcome to Tic Tac Toe\n')

while True:
    the_board = [' ']*10

    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will play first')

    play_game = input('Ready to play? y or n: \t')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    

    while game_on == True:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLayer 1 has won!!!')
                game_on = False
            else:
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLayer 2 has won!!!')
                game_on = False
            else:
                if fullboard_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 1'
        
    if not replay():
        break
