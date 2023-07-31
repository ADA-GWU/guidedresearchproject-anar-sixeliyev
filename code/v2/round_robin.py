import argparse
import csv
import os
import time

import numpy as np
from agent_alpha_beta.agent_alpha_beta_compete import *
from agent_minimax.agent_minimax_compete import *
from board import *
from heuristic import *
from minimax import *


def ab_vs_ab():
    opp_1 = 1
    opp_2 = -1
    game_board = []
    NEXT_BOARD_X = -1
    NEXT_BOARD_Y = -1
    moves = []  # Store game moves
    results = None
    start_time = time.time()

    while True:
        if len(game_board) != 0:
            if check_large_board_winner(game_board, opp_1):
                print("GAME_OVER: opp_1")
                results = "opp_1"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: opp_2 WINS")
                results = "opp_2"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_alpha_beta(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))
        opp_1 *= -1
        opp_2 *= -1
    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "opp_1":
        winner = "Agent 1 (opp_1)"
    elif results == "opp_2":
        winner = "Agent 2 (opp_2)"
    else:
        winner = "TIE"

    num_moves = len(moves)
    final_game_board = moves[-1][0]

    # Output insights
    print(f"\nGame Result: {winner}")
    print(f"Total Moves: {num_moves}")
    print("Final Game Board:")
    print_ultimate_board(final_game_board)

    # Check if the file exists
    output_file = "results_ab_vs_ab.csv"
    file_exists = os.path.exists(output_file)

    # Append the moves and results to the CSV file
    with open(output_file, "a", newline="") as csvfile:
        fieldnames = ["Game Result", "Total Moves",
                      "Average Game Time", "Final Game Board"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            # Write header if the file does not exist
            writer.writeheader()

        # Append the game result to the CSV file

        writer.writerow({
                        "Game Result": winner,
                        "Total Moves": num_moves,
                        "Average Game Time": f"{game_time:.2f}",
                        "Final Game Board": final_game_board,
                        })


def ab_vs_minmax():
    opp_1 = 1
    opp_2 = -1
    game_board = []
    NEXT_BOARD_X = -1
    NEXT_BOARD_Y = -1
    moves = []  # Store game moves
    results = None
    start_time = time.time()

    while True:
        if len(game_board) != 0:
            if check_large_board_winner(game_board, opp_1):
                print("GAME_OVER: opp_1")
                results = "opp_1"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: opp_2 WINS")
                results = "opp_2"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_alpha_beta(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_minimax(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "opp_1":
        winner = "Agent 1 (opp_1)"
    elif results == "opp_2":
        winner = "Agent 2 (opp_2)"
    else:
        winner = "TIE"

    num_moves = len(moves)
    final_game_board = moves[-1][0]

    # Output insights
    print(f"\nGame Result: {winner}")
    print(f"Total Moves: {num_moves}")
    print("Final Game Board:")
    print_ultimate_board(final_game_board)

    # Check if the file exists
    output_file = "results_ab_vs_minmax.csv"
    file_exists = os.path.exists(output_file)

    # Append the moves and results to the CSV file
    with open(output_file, "a", newline="") as csvfile:
        fieldnames = ["Game Result", "Total Moves",
                      "Average Game Time", "Final Game Board"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            # Write header if the file does not exist
            writer.writeheader()

        # Append the game result to the CSV file

        writer.writerow({
                        "Game Result": winner,
                        "Total Moves": num_moves,
                        "Average Game Time": f"{game_time:.2f}",
                        "Final Game Board": final_game_board,
                        })


def minmax_vs_ab():
    opp_1 = 1
    opp_2 = -1
    game_board = []
    NEXT_BOARD_X = -1
    NEXT_BOARD_Y = -1
    moves = []  # Store game moves
    results = None
    start_time = time.time()

    while True:
        if len(game_board) != 0:
            if check_large_board_winner(game_board, opp_1):
                print("GAME_OVER: opp_1")
                results = "opp_1"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: opp_2 WINS")
                results = "opp_2"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_minimax(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_alpha_beta(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "opp_1":
        winner = "Agent 1 (opp_1)"
    elif results == "opp_2":
        winner = "Agent 2 (opp_2)"
    else:
        winner = "TIE"

    num_moves = len(moves)
    final_game_board = moves[-1][0]

    # Output insights
    print(f"\nGame Result: {winner}")
    print(f"Total Moves: {num_moves}")
    print("Final Game Board:")
    print_ultimate_board(final_game_board)

    # Check if the file exists
    output_file = "results_minmax_vs_ab.csv"
    file_exists = os.path.exists(output_file)

    # Append the moves and results to the CSV file
    with open(output_file, "a", newline="") as csvfile:
        fieldnames = ["Game Result", "Total Moves",
                      "Average Game Time", "Final Game Board"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            # Write header if the file does not exist
            writer.writeheader()

        # Append the game result to the CSV file

        writer.writerow({
                        "Game Result": winner,
                        "Total Moves": num_moves,
                        "Average Game Time": f"{game_time:.2f}",
                        "Final Game Board": final_game_board,
                        })


if __name__ == "__main__":
    # play_game()
    # ab_vs_ab()
    # ab_vs_minmax()
    minmax_vs_ab()
