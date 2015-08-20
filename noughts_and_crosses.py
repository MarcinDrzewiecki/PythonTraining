__author__ = 'drzewko'

X = "X"
O = "O"
NUM_SQUARES = 9
EMPTY = " "


def display_board(board):
    print"\n \t", board[0], "|", board[1], "|", board[2]
    print"\t", "---------"
    print"\n\t", board[3], "|", board[4], "|", board[5]
    print"\t", "---------"
    print"\n\t", board[6], "|", board[7], "|", board[8], "\n"
    print"\t", "---------"


def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def human_move(board):
    move = None
    legal = legal_moves(board)
    while move not in legal:
        move = ask_number("What is your move?: ", 0, 8)
        if move not in legal:
            print "Wybierz inne pole"
        print "Dobry wybor"
    return move


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board(square) == EMPTY:
            moves.append(square)
    return moves


board = new_board()
display_board(board)
human_move(board)