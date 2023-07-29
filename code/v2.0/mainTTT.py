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
    print("Enter the coordinates x, y:")
    x = int(input())
    y = int(input())
    return x, y


def select_board():
    print("Enter the positions of the board and position of the next mark X, Y:")
    X = int(input())
    Y = int(input())
    return X, Y


def local_playing():
    # board_size = int(input("Please enter board size: "))
    board_size = 3
    # target = int(input("Please enter consecutive symbol size: "))
    target = 3
    agent_player = int(input("Choose agent side as 1 or -1: "))
    memory = {}
    game_board = np.zeros(
        (board_size, board_size, board_size, board_size), dtype=np.int32)
    # print(game_board[0][0][0][0])
    # print_board(game_board)
    opp_player = -agent_player

    if agent_player == 1:
        print("AI Plays...")
        pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(game_board, target, agent_player,
                                                        opp_player, 1, memory)
        # pos_X, pos_Y, pos_x, pos_y = best_next_move_small(game_board, target, agent_player,
        #                                                 opp_player, 1, memory)

        game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
        NEXT_BOARD_X = pos_x
        NEXT_BOARD_Y = pos_y
        # print_board(game_board[pos_X, pos_Y])
        # print(game_board)
        print_ultimate_board(game_board)

        # print('~~~~MOVE MADE - UPDATED BOARD: \n', game_board)
        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")

    while True:
        if check_large_board_winner(game_board, agent_player):
            print("GAME_OVER: COMPUTER WINS")
            break
        if check_large_board_winner(game_board, opp_player):
            print("GAME_OVER: HUMAN WINS")
            break

        # if tie_game(game_board):
        #     print("GAME_OVER: TIE")
        #     break

        print("Human Plays...")
        if (check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player)):
            print('<====BOARD {} {} IS WON, SELECT A NEW BOARD====>\n'.format(
                NEXT_BOARD_X, NEXT_BOARD_Y))
            NEXT_BOARD_X, NEXT_BOARD_Y = select_board()
            while (check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player)):
                NEXT_BOARD_X, NEXT_BOARD_Y = select_board()
        pos_x, pos_y = opp_play()
        while (game_board[NEXT_BOARD_X, NEXT_BOARD_Y][pos_x, pos_y] != 0):
            print("Select an empty cell please:")
            pos_x, pos_y = opp_play()

        game_board[NEXT_BOARD_X, NEXT_BOARD_Y][pos_x, pos_y] = opp_player
        NEXT_BOARD_X = pos_x
        NEXT_BOARD_Y = pos_y
        # print(game_board)
        print_ultimate_board(game_board)

        print("Human Played")
        print("====================")

        if check_large_board_winner(game_board, opp_player):
            print("GAME_OVER: HUMAN WINS")
            break

        # if tie_game(game_board):
        #     print("GAME_OVER: TIE")
        #     break

        print("AI Plays...")
        if (check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player)):
            print('<====BOARD {} {} IS WON====>\n'.format(
                NEXT_BOARD_X, NEXT_BOARD_Y))
            # NEXT_BOARD_X, NEXT_BOARD_Y = select_board()
            pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(game_board, target, agent_player,
                                                            opp_player, 1, memory)
        # POS_X, POS_Y, pos_x, pos_y = best_next_move_ult(game_board, POS_X, POS_Y, target, agent_player,
        #                                                 opp_player, 1, memory)
        else:
            print('=== RUNNED best_next_move_small_large')
            # pos_X, pos_Y, pos_x, pos_y = best_next_move_small(game_board, pos_x, pos_y, target, agent_player,
            #                                                   opp_player, 1, memory)
            pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(game_board, pos_x, pos_y, target, agent_player,
                                                                    opp_player, 1, memory)
        game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
        NEXT_BOARD_X = pos_x
        NEXT_BOARD_Y = pos_y

        # print(game_board)
        print_ultimate_board(game_board)

        print("AI Played in postion ({},{}) - ({},{})".format(pos_X, pos_Y, pos_x, pos_y))
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
