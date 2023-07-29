
import numpy as np


def tie_game(board):
    return np.count_nonzero(board) == board.size


def check_rows(board, target):
    for x in range(board.shape[0]):
        for y in range(board.shape[0]-target+1):
            if np.all(board[x, y:y+target] == 1):
                return 1
            elif np.all(board[x, y:y+target] == -1):
                return -1
    return 0


def check_columns(board, target):
    for x in range(board.shape[0]-target+1):
        for y in range(board.shape[0]):
            if np.all(board[x:x+target, y] == 1):
                return 1
            elif np.all(board[x:x+target, y] == -1):
                return -1
    return 0


def check_diagonals(board, target):
    for x in range(board.shape[0]-target+1):
        for y in range(board.shape[0]-target+1):
            if np.all(np.diag(board[x:x+target, y:y+target]) == 1):
                return 1
            elif np.all(np.diag(board[x:x+target, y:y+target]) == -1):
                return -1

            if np.all(np.diag(np.fliplr(board[x:x+target, y:y+target])) == 1):
                return 1
            elif np.all(np.diag(np.fliplr(board[x:x+target, y:y+target])) == -1):
                return -1
    return 0


def game_end(board, target):
    r = check_rows(board, target)
    if r != 0:
        return r
    c = check_columns(board, target)
    if c != 0:
        return c
    d = check_diagonals(board, target)
    if d != 0:
        return d

    return 0


def terminated(board, target):
    return game_end(board, target) != 0 or tie_game(board)


def get_successors(board, player):
    arr_successors = []
    for i in range(board.shape[0]):
        for j in range(board.shape[0]):
            if board[i][j] == 0:
                temp_board = board.copy()
                temp_board[i][j] = player
                arr_successors.append(temp_board)
    return arr_successors


def print_board(board):
    for i in range(3):
        for j in range(3):
            print("Board ({}, {}):".format(i, j))
            for row in board[i][j]:
                print(" | ".join(cell if cell else 0 for cell in row))
                print("-" * 9)
