import random

import numpy as np
# from make_random_move import *
from board import *


def terminated_small(board):
    return check_small_board_winner(board, 1) or check_small_board_winner(board, -1) or tie_game_small(board)


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


def agent_random_comp(agent_player, opp_player, game_board, NEXT_BOARD_X, NEXT_BOARD_Y, depth=3,  memory={}):
    board_size = 3
    if len(game_board) == 0:
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)

    pos_X, pos_Y, pos_x, pos_y = get_random_move(
        game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

    game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
    NEXT_BOARD_X = pos_x
    NEXT_BOARD_Y = pos_y
    # print(game_board)
    # print_ultimate_board(game_board)

    print("AI Random Played in postion ({},{}) - ({},{})".format(pos_X, pos_Y, pos_x, pos_y))
    # print("====================")
    return game_board, NEXT_BOARD_X, NEXT_BOARD_Y


if __name__ == "__main__":
    agent_random_comp(1, -1, [], -1, -1)