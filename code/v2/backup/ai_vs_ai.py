import argparse
import itertools
import os
import pickle
import sys
import time
from timeit import default_timer as timer

import numpy as np
import csv

from board import *
from heuristic import *
from minimax import *


def ai_vs_ai(num_games=10):
    board_size = 3
    target = 3
    agent_player = 1
    memory = {}
    total_moves = 0
    total_time = 0
    ai1_wins = 0
    ai2_wins = 0
    ties = 0
    duration_of_games = []

    for game_num in range(num_games):
        print(f"Game {game_num}:")
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)
        opp_player = -agent_player
        NEXT_BOARD_X, NEXT_BOARD_Y = -1, -1

        start_time = time.time()

        while True:
            if check_large_board_winner(game_board, agent_player):
                print("GAME_OVER: AI 1 WINS")
                ai1_wins += 1
                break
            if check_large_board_winner(game_board, opp_player):
                print("GAME_OVER: AI 2 WINS")
                ai2_wins += 1
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                ties += 1
                break

            if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player):
                # print('<====BOARD {} {} IS WON, AI 1 SELECTS A NEW BOARD====>\n'.format(
                #     NEXT_BOARD_X, NEXT_BOARD_Y))
                pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(
                    game_board, target, agent_player, opp_player, 1, memory)
            else:
                # print('=== AI 1 RUNS best_next_move_small_large')
                pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(
                    game_board, pos_x, pos_y, target, agent_player, opp_player, 1, memory)

            game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player
            NEXT_BOARD_X = pos_x
            NEXT_BOARD_Y = pos_y

            # print_ultimate_board(game_board)
            total_moves += 1

            if check_large_board_winner(game_board, agent_player):
                print("GAME_OVER: AI 1 WINS")
                ai1_wins += 1
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                ties += 1
                break

            if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], agent_player) or check_small_board_winner(game_board[NEXT_BOARD_X, NEXT_BOARD_Y], opp_player):
                # print('<====BOARD {} {} IS WON, AI 2 SELECTS A NEW BOARD====>\n'.format(
                #     NEXT_BOARD_X, NEXT_BOARD_Y))
                pos_X, pos_Y, pos_x, pos_y = best_next_move_ult(
                    game_board, target, opp_player, agent_player, 1, memory)
            else:
                # print('=== AI 2 RUNS best_next_move_small_large')
                pos_X, pos_Y, pos_x, pos_y = best_next_move_small_large(
                    game_board, pos_x, pos_y, target, opp_player, agent_player, 1, memory)

            game_board[pos_X, pos_Y][pos_x, pos_y] = opp_player
            NEXT_BOARD_X = pos_x
            NEXT_BOARD_Y = pos_y

            # print_ultimate_board(game_board)
            total_moves += 1

        end_time = time.time()
        game_time = end_time - start_time
        duration_of_games.append(f"{game_time:.2f}")
        total_time += game_time
        print(
            f"Game {game_num} time: {game_time:.2f} seconds, total moves: {total_moves}")
        print("====================")

    print("AI 1 Wins:", ai1_wins)
    print("AI 2 Wins:", ai2_wins)
    print("Ties:", ties)
    print("Average Game Time:", total_time / num_games)
    print("Average Moves per Game:", total_moves / num_games)

    #
    with open(f"results_AI1_vs_AI2.csv", "w", newline="") as csvfile:
        fieldnames = ["Game Number", "AI 1 Wins",
                      "AI 2 Wins", "Ties", "Total Moves", "Average Game Time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for game_num in range(num_games):
            writer.writerow({
                "Game Number": game_num,
                "AI 1 Wins": ai1_wins,
                "AI 2 Wins": ai2_wins,
                "Ties": ties,
                "Total Moves": total_moves,
                # "Average Game Time": f"{game_time:.2f}"
                "Average Game Time": duration_of_games[game_num]
            })


def main():
    parser = argparse.ArgumentParser()

    # parser.add_argument("-ai_vs_ai",
    #                     "--ai_vs_ai",
    #                     dest="ai_vs_ai",
    #                     help="If you want to play AI vs AI mode",
    #                     action=argparse.BooleanOptionalAction,
    #                     default=False)
    # args = parser.parse_args()

    # ai_vs_ai_mode = args.ai_vs_ai

    # if ai_vs_ai_mode:
    ai_vs_ai()


if __name__ == "__main__":
    main()
