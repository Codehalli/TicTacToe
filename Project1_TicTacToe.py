# Creates the Tic Tac Toe table
import random


def display_section(section):
    print(section[7] + '  |  ' + section[8] + '  |  ' + section[9])
    print('-------------')
    print(section[4] + '  |  ' + section[5] + '  |  ' + section[6])
    print('-------------')
    print(section[1] + '  |  ' + section[2] + '  |  ' + section[3])
    print()


# Assigns the test sections for the table
# test_section = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_section(test_section)

def player_input():
    symbol = ''

    while symbol != 'X' or symbol != '0':
        symbol = input('Player 1: What symbol would like to choose X or O? ').upper()

        if symbol == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'


def symbol_location(section, symbol, location):
    """

    :param location:
    :param symbol:
    :type section: object
    """
    section[location] = symbol


# symbol_location(test_section, '$', 8)
# display_section(test_section)


def win(section, symbol):
    # to check if if the sections share the same row of symbol

    return ((section[7] == section[8] == section[9] == symbol) or  # across the top
            (section[4] == section[5] == section[6] == symbol) or  # across the middle
            (section[1] == section[2] == section[3] == symbol) or  # across the bottom

            (section[7] == section[4] == section[1] == symbol) or  # down the middle
            (section[8] == section[5] == section[2] == symbol) or  # down the middle
            (section[9] == section[6] == section[3] == symbol) or  # down the right side

            (section[7] == section[5] == section[3] == symbol) or  # diagonal
            (section[9] == section[5] == section[1] == symbol))  # diagonal


# display_section(test_section)
# win(test_section, 'X')


def player_pick():
    toss = random.randint(0, 1)
    if toss == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def open_space(section, location) -> object:
    return section[location] == ' '


def closed_space(section):
    for i in range(1, 10):
        if open_space(section, i):
            return False
    # check for the spaces
    return True


def player_decide(section):
    location = 0
    while location not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not open_space(section, location):
        location = int(input('Choose any position in the corresponding number 1-9) '))

        return location


def replay():
    choice = input('Play again? Enter Yes or No')

    return choice == 'yes'


# Logic of the code
print('Welcome to the game of Tic Tac and Toe!!!')

while True:

    # Set up the game
    the_board = [' '] * 10
    player1_symbol, player2_symbol = player_input()
    turn = player_pick()
    print(turn + ' will go first.')

    play_game = input('Ready to play? yes or no? ')

    if play_game.lower() == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_section(the_board)
            position = player_decide(the_board)
            symbol_location(the_board, player1_symbol, position)

            if win(the_board, player1_symbol):
                display_section(the_board)
                print('Congrats Player 1')
                game_on = False
            else:
                if closed_space(the_board):
                    display_section(the_board)
                    print("Game is Tie")
                    game_on = False
                else:
                    turn = "Player 2"
        else:

            display_section(the_board)
            position = player_decide(the_board)
            symbol_location(the_board, player2_symbol, position)

            if win(the_board, player2_symbol):
                display_section(the_board)
                print('Congrats Player 2')
                game_on = False
            else:
                if closed_space(the_board):
                    display_section(the_board)
                    print('Tie Game')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
