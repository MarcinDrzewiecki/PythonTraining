__author__ = 'drzewko'

import random

TIE = "TIE"
X = "X"
O = "O"
NUM_SQUARES = 9
EMPTY = " "


def display_board(board):
    print("\n \t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")
    print("\t", "---------")


def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def human_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("What is your move?: ", 0, 9)
        if move not in legal:
            print ("Illegal move, try different one")
        print ("Good move")
    return move


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def ask_yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
        return response


def pieces():
    question = ask_yes_no("Do you want to go first ? y/n ")
    if question == "y":
        human = X
        computer = O
    else:
        human = O
        computer = X
    return human, computer


def computer_move(board):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = random.randrange(0, 9)
    return move


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner):
    if the_winner != TIE:
        print (the_winner, "Congratulation!")
    else:
        print("It's a tie!")


def main():
    human, computer = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    congrat_winner(winner(board))


main()
