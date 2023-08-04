import numpy as np

from board import *
from agent_random import *


def agent_random(agent_player, opp_player, game_board, NEXT_BOARD_X, NEXT_BOARD_Y, depth=3,  memory={}):
    board_size = 3
    target = 3
    memory = {}
    if len(game_board) == 0:
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)

    pos_X, pos_Y, pos_x, pos_y = random_agent(
        game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

    game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
    NEXT_BOARD_X = pos_x
    NEXT_BOARD_Y = pos_y
    # print(game_board)
    print_ultimate_board(game_board)

    print("AI Played in postion ({},{}) - ({},{})".format(pos_X, pos_Y, pos_x, pos_y))
    print("====================")
    return game_board, NEXT_BOARD_X, NEXT_BOARD_Y


if __name__ == "__main__":
    agent_random(1, -1, [], -1, -1)
