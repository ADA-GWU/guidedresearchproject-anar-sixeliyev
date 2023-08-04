import random

import numpy as np
from board import *


def get_random_move(ultimate_board, pos_X=-1, pos_Y=-1):
    valid_moves = get_valid_moves(ultimate_board, pos_X, pos_Y)
    if not valid_moves:
        return None
    return random.choice(valid_moves)


def get_valid_moves(ultimate_board, pos_X, pos_Y):
    valid_moves = []
    if ((pos_X == -1 and pos_Y == -1) or terminated_small(ultimate_board[pos_X][pos_Y])):
        for i in range(3):
            for j in range(3):
                if not check_small_board_winner(ultimate_board[i][j], 1) and not check_small_board_winner(ultimate_board[i][j], -1):
                    for x in range(3):
                        for y in range(3):
                            if ultimate_board[i][j][x][y] == 0:
                                valid_moves.append((i, j, x, y))
    else:
        for x in range(3):
            for y in range(3):
                if ultimate_board[pos_X][pos_Y][x][y] == 0:
                    valid_moves.append((pos_X, pos_Y, x, y))
    return valid_moves
