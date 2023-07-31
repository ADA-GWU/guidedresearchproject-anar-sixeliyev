import numpy as np

from board import *
from minimax import *


def agent_minimax(agent_player, opp_player, game_board, NEXT_BOARD_X, NEXT_BOARD_Y, depth=3,  memory={}):
    board_size = 3
    target = 3
    memory = {}
    if len(game_board) == 0:
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)

    if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player):
        pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(
            game_board, target, agent_player, opp_player, 1, memory)
    else:
        pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(
            game_board, NEXT_BOARD_X, NEXT_BOARD_Y, target, agent_player, opp_player, 1, memory)

    game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
    NEXT_BOARD_X = pos_x
    NEXT_BOARD_Y = pos_y
    # print(game_board)
    print_ultimate_board(game_board)

    print("AI Played in postion ({},{}) - ({},{})".format(pos_X, pos_Y, pos_x, pos_y))
    print("====================")
    return game_board, NEXT_BOARD_X, NEXT_BOARD_Y


if __name__ == "__main__":
    agent_minimax(1, -1, [], -1, -1)
