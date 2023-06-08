from timeit import default_timer as timer

import numpy as np
from board import *
from heuristic import *
from minimax import *


def opp_play():
    print("Enter the positions for x and y:")
    i = int(input())
    j = int(input())
    return i, j


def local_playing():
    board_size = int(input("Please enter board size: "))
    target = int(input("Please enter consecutive symbol size: "))
    agent_player = int(input("Choose agent side as 1 or -1"))

    game_board = np.zeros((board_size, board_size), dtype=np.int32)
    opp_player = -agent_player
    # memory = {}
    if agent_player == 1:
        print("AI Plays...")
        pos_x, pos_y = best_next_move(
            game_board, target, agent_player, opp_player)
        game_board[pos_x, pos_y] = agent_player
        #         print_board(game_board)
        print(game_board)
        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")

    #   game progress


def main():
    local_playing()


if __name__ == "__main__":
    main()
