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
        pos_x, pos_y = best_next_move(
            game_board, target, agent_player, opp_player)
        game_board[pos_x, pos_y] = agent_player
        print(game_board)
        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")


def main():
    local_playing()
    # board_size = 6
    # target = 4
    # dpth = 3
    # mem = {}
    # bf = 'board_evals/b_{}_{}.pkl'.format(board_size, target)
    # if os.path.isfile(bf):
    #     with open(bf, 'rb') as fp:
    #         mem = pickle.load(fp)
    #         print("Learned Boards:")
    #         print("Count of learned boards:{}".format(len(mem)))

    # if (len(mem) > 300000):
    #     mem = dict(itertools.islice(mem.items(), 300000))
    # with open(bf, 'wb') as fp:
    #     pickle.dump(mem, fp)
    #     print('dictionary saved successfully to file')


if __name__ == "__main__":
    main()
