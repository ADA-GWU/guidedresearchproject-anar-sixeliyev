import argparse
import itertools
import os
import pickle
import sys
import time
from timeit import default_timer as timer

import numpy as np

from api_wrapper import APIWrapper
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
    agent_player = int(input("Choose agent side as 1 or -1: "))
    memory = {}
    game_board = np.zeros((board_size, board_size), dtype=np.int32)
    opp_player = -agent_player

    if agent_player == 1:
        print("AI Plays...")
        pos_x, pos_y = best_next_move(game_board, target, agent_player,
                                      opp_player, 3, memory)
        game_board[pos_x, pos_y] = agent_player
        #         print_board(game_board)
        print(game_board)
        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")

    while True:
        if game_end(game_board, target) == agent_player:
            print("GAME_OVER: COMPUTER WINS")
            break
        if game_end(game_board, target) == opp_player:
            print("GAME_OVER: HUMAN WINS")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break

        print("Human Plays...")
        pos_x, pos_y = opp_play()
        while (game_board[pos_x, pos_y] != 0):
            print("Select an empty cell please:")
            pos_x, pos_y = opp_play()
        game_board[pos_x, pos_y] = opp_player
        print(game_board)
        print("Human Played")
        print("====================")

        if game_end(game_board, target) == opp_player:
            print("GAME_OVER: HUMAN WINS")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break
        print("AI Plays...")
        pos_x, pos_y = best_next_move(game_board, target, agent_player,
                                      opp_player, 3, memory)
        game_board[pos_x, pos_y] = agent_player
        print(game_board)
        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-local",
                        "--local",
                        dest="local_playing",
                        help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    args = parser.parse_args()

    boolean_local = args.local_playing

    if boolean_local:
        local_playing()


if __name__ == "__main__":
    main()
