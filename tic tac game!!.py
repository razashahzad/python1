


def display_board(board):

    print('   |    |')
    print(' ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   |    |')
    print('--------------')
    print('   |    |')
    print(' ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('   |    |')
    print('--------------')
    print('   |    |')
    print(' ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('   |    |')


def player_input():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('player 1 : u want X or O ???').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board,marker,position):
    board[position] = marker

    def win_check(board, mark):
        for i in range(1, 8, 3):
            if (board[i] == mark and board[i + 1] == mark and board[i + 2] == mark):
                return true
        for i in range(1, 4):
            if (board[i] == mark and board[i + 3] == mark and board[i + 6] == mark):
                return true
        return ((board[1] == mark and board[5] == mark and board[9] == mark) or
                (board[3] == mark and board[5] == mark and board[7] == mark))


def win_check(board,mark):
    for i in range(1,8,3):
        if(board[i]==mark and board[i+1]==mark and board[i+2]==mark):
            return True
    for i in range(1,4):
        if(board[i]==mark and board[i+3]==mark and board[i+6]==mark):
            return True
    return((board[1]==mark and board[5]==mark and board[9]==mark) or
           (board[3]==mark and board[5]==mark and board[7]==mark))


import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
         return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = ' '
    l = '1 2 3 4 5 6 7 8 9'.split()
    while position not in l or not space_check(board,int(position)):
        position = input('choose your next position: (1 to 9)')

    return int(position)


def replay():
    a = input('do you want to play again? Y or N').lower()
    if a =='n':
        return False
    else:
        return True

print('Welcome to tic tac toe!!')
position = ' '
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will play first')

    game_on = True
    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('congratulations.....player 1 has won!!!')
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('the game is draw....')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('congratulations.....player 2 has won!!!')
                game_on = False

            elif full_board_check(theBoard):
                    display_board(theBoard)
                    print('the game is draw....')
                    break

            else:
                turn = 'Player 1'
    if not replay():
        break
