import argparse
import itertools
import os
import pickle
import sys
import time
from timeit import default_timer as timer

import numpy as np
from board import *
from minimax import *


def ai_vs_ai(num_games=3):
    board_size = 3
    target = 3
    agent_player = 1
    memory = {}
    total_moves = 0
    total_time = 0
    ai1_wins = 0
    ai2_wins = 0
    ties = 0

    for game_num in range(1, num_games + 1):
        print(f"Game {game_num}:")
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)
        opp_player = -agent_player
        NEXT_BOARD_X, NEXT_BOARD_Y = -1, -1

        start_time = time.time()

        while True:
            if check_large_board_winner(game_board, agent_player):
                print("GAME_OVER: AI 1 WINS")
                print_ultimate_board(game_board)

                ai1_wins += 1
                break
            if check_large_board_winner(game_board, opp_player):
                print("GAME_OVER: AI 2 WINS")
                print_ultimate_board(game_board)

                ai2_wins += 1
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                print_ultimate_board(game_board)
                ties += 1
                break

            if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or terminated_small(game_board[NEXT_BOARD_X, NEXT_BOARD_Y]):
                print('<====BOARD {} {} IS WON, AI 1 SELECTS A NEW BOARD====>\n'.format(
                    NEXT_BOARD_X, NEXT_BOARD_Y))
                pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(
                    game_board, target, agent_player, opp_player, 1, memory)
            else:
                print('=== AI 1 RUNS best_next_move_small_large')
                pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(
                    game_board, pos_x, pos_y, target, agent_player, opp_player, 1, memory)

            game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
            NEXT_BOARD_X = pos_x
            NEXT_BOARD_Y = pos_y

            print_ultimate_board(game_board)
            total_moves += 1

            if check_large_board_winner(game_board, agent_player):
                print("GAME_OVER: AI 1 WINS")
                print_ultimate_board(game_board)

                ai1_wins += 1
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                print_ultimate_board(game_board)

                ties += 1
                break

            if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or terminated_small(game_board[NEXT_BOARD_X, NEXT_BOARD_Y]):
                print('<====BOARD {} {} IS WON, AI 2 SELECTS A NEW BOARD====>\n'.format(
                    NEXT_BOARD_X, NEXT_BOARD_Y))
                pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(
                    game_board, target, opp_player, agent_player, 1, memory)
            else:
                print('=== AI 2 RUNS best_next_move_small_large')
                pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(
                    game_board, pos_x, pos_y, target, opp_player, agent_player, 1, memory)
                # print('moves: ', pos_X, pos_Y, pos_x, pos_y)

            game_board[pos_X, pos_Y][pos_x, pos_y] = opp_player
            NEXT_BOARD_X = pos_x
            NEXT_BOARD_Y = pos_y

            print_ultimate_board(game_board)
            total_moves += 1

        end_time = time.time()
        game_time = end_time - start_time
        total_time += game_time
        print(
            f"Game {game_num} time: {game_time:.2f} seconds, total moves: {total_moves}")
        print("====================")

    print("AI 1 Wins:", ai1_wins)
    print("AI 2 Wins:", ai2_wins)
    print("Ties:", ties)
    print("Average Game Time:", total_time / num_games)
    print("Average Moves per Game:", total_moves / num_games)


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
    board_size = 3
    target = 3
    agent_player = int(input("Choose agent side as 1 or -1: "))
    memory = {}
    game_board = np.zeros(
        (board_size, board_size, board_size, board_size), dtype=np.int32)
    opp_player = -agent_player

    if agent_player == 1:
        print("AI Plays... ")
        pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(game_board, target, agent_player,
                                                        opp_player, 2, memory)

        game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
        NEXT_BOARD_X = pos_x
        NEXT_BOARD_Y = pos_y
        print_ultimate_board(game_board)

        print("AI Played in postion ({},{})".format(pos_x, pos_y))
        print("====================")
    elif agent_player == -1:
        NEXT_BOARD_X, NEXT_BOARD_Y = select_board()

    while True:
        if check_large_board_winner(game_board, agent_player):
            print("GAME_OVER: COMPUTER WINS")
            break
        if check_large_board_winner(game_board, opp_player):
            print("GAME_OVER: HUMAN WINS")
            break

        if tie_game_big(game_board):
            print("GAME_OVER: TIE")
            break

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

        if tie_game_big(game_board):
            print("GAME_OVER: TIE")
            break

        # print("AI Plays...")
        if (check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player)):
            print("AI Plays... best_next_move_ult")

            print('<====BOARD {} {} IS WON====>\n'.format(
                NEXT_BOARD_X, NEXT_BOARD_Y))
            pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(game_board, target, agent_player,
                                                            opp_player, 2, memory)
        else:
            print("AI Plays... best_next_move_small_large")

            pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(game_board, pos_x, pos_y, target, agent_player,
                                                                    opp_player, 2, memory)
        game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
        NEXT_BOARD_X = pos_x
        NEXT_BOARD_Y = pos_y

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

    parser.add_argument("-ai_vs_ai",
                        "--ai_vs_ai",
                        dest="ai_vs_ai",
                        help="If you want to play AI vs AI mode",
                        action=argparse.BooleanOptionalAction,
                        default=False)
    args = parser.parse_args()

    boolean_local = args.local_playing
    ai_vs_ai_mode = args.ai_vs_ai

    if boolean_local:
        local_playing()
    if ai_vs_ai_mode:
        ai_vs_ai()


if __name__ == "__main__":
    main()
