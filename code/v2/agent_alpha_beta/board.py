
import numpy as np

# from heuristic import *


def tie_game_small(board):
    return np.count_nonzero(board) == board.size


def tie_game_big(ultimate_board):
    # Check if all small boards are full and there is no winner in the large board
    for i in range(3):
        for j in range(3):
            if not check_small_board_winner(ultimate_board[i][j], 1) and not check_small_board_winner(ultimate_board[i][j], -1) and not tie_game_small(ultimate_board[i][j]):
                return False

    # Check if the large board itself is not won by any player
    return not check_large_board_winner(ultimate_board, 1) and not check_large_board_winner(ultimate_board, -1)


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


def terminated(board):
    return check_large_board_winner(board, 1) or check_large_board_winner(board, -1) or tie_game_big(board)

def terminated_small(board):
    return check_small_board_winner(board, 1) or check_small_board_winner(board, -1) or tie_game_small(board)


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


def print_ultimate_board(ultimate_board):
    for large_row in range(3):
        for small_row in range(3):
            for large_col in range(3):
                for small_col in range(3):
                    cell = ultimate_board[large_row][large_col][small_row][small_col]
                    if cell == "":
                        print(" ", end=" ")
                    else:
                        if (cell == 1):
                            print("X", end=" ")
                        elif (cell == -1):
                            print("O", end=" ")
                        else:
                            print("*", end=" ")
                    if small_col < 2:
                        print("|", end=" ")
                if large_col < 2:
                    print(" || ", end=" ")
            print()
            # print("-" * 9)
            if small_row > 1:
                print("-" * 40)
                print("-" * 40)

    # print("=" * 71)


def check_small_board_winner(small_board, player):
    for i in range(3):
        if small_board[i][0] == small_board[i][1] == small_board[i][2] == player:
            return True
        if small_board[0][i] == small_board[1][i] == small_board[2][i] == player:
            return True
    if small_board[0][0] == small_board[1][1] == small_board[2][2] == player:
        return True
    if small_board[0][2] == small_board[1][1] == small_board[2][0] == player:
        return True
    return False


def check_large_board_winner(ultimate_board, player):
    for i in range(3):
        if check_small_board_winner(ultimate_board[i][0], player) and check_small_board_winner(ultimate_board[i][1], player) and check_small_board_winner(ultimate_board[i][2], player):
            return True
        if check_small_board_winner(ultimate_board[0][i], player) and check_small_board_winner(ultimate_board[1][i], player) and check_small_board_winner(ultimate_board[2][i], player):
            return True
    if check_small_board_winner(ultimate_board[0][0], player) and check_small_board_winner(ultimate_board[1][1], player) and check_small_board_winner(ultimate_board[2][2], player):
        return True
    if check_small_board_winner(ultimate_board[0][2], player) and check_small_board_winner(ultimate_board[1][1], player) and check_small_board_winner(ultimate_board[2][0], player):
        return True
    return False
