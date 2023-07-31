import argparse
import itertools
import os
import pickle
import sys
import time
from timeit import default_timer as timer

import numpy as np

from board import *
from heuristic import *
from minimax import *


def ai_vs_ai(board_size: int = 3, target_size: int = 3, depth=3, memory={}):
    """
  This function is used to play tic-tac-toe between same AI vs AI.
  Goal of self playing is for memorizing board evaluations.
  """
    # s_all = timer()
    game_board = np.zeros((board_size, board_size), dtype=np.int32)
    agent1 = 1
    agent2 = -1

    while True:
        s1 = timer()
        print("AI_1 Plays...")
        pos_x, pos_y = best_next_move(game_board, target_size, agent1, agent2,
                                      depth, memory)
        game_board[pos_x, pos_y] = agent1
        #         print_board(game_board)
        print(game_board)
        e1 = timer()
        print("AI_1 Played in postion ({},{})".format(pos_x, pos_y))
        print("Execution time {}".format(e1 - s1))
        print("====================")

        is_game_end = game_end(game_board, target_size)
        if is_game_end == 1:
            print("AI_1 won the game")
            break
        if is_game_end == 2:
            print("AI_2 won the game")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break

        print("AI_2 Plays...")
        s2 = timer()
        pos_x, pos_y = best_next_move(game_board, target_size, agent2, agent1,
                                      depth, memory)
        game_board[pos_x, pos_y] = agent2
        #         print_board(game_board)
        print(game_board)
        print("AI_2 Played in postion ({},{})".format(pos_x, pos_y))
        e2 = timer()
        print("Execution time {}".format(e2 - s2))
        print("====================")

        is_game_end = game_end(game_board, target_size)
        if is_game_end == 1:
            print("AI_1 won the game")
            break
        if is_game_end == 2:
            print("AI_2 won the game")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break


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
