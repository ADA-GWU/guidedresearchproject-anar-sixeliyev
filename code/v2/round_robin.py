import argparse
import csv
import os
import time
import sys
# print('=======> sys.path ROUND_ROBIN', sys.path)
import numpy as np
from agent_alpha_beta.agent_alpha_beta_compete import *
from agent_minimax.agent_minimax_compete import *
from agent_part_genious.agent_part_genious_comp import *
from agent_random.agent_random_compete import *
# from board import *
# from heuristic import *
# from minimax import *


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
                print("GAME_OVER: ab")
                results = "ab"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: minmax WINS")
                results = "minmax"
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
    if results == "ab":
        winner = "Agent 1 (ab)"
    elif results == "minmax":
        winner = "Agent 2 (minmax)"
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
                print("GAME_OVER: minmax")
                results = "minmax"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: ab WINS")
                results = "ab"
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
    if results == "minmax":
        winner = "Agent 1 (minmax)"
    elif results == "ab":
        winner = "Agent 2 (ab)"
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


def random_vs_ab():
    # random
    opp_1 = 1
    # AB
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
                print("GAME_OVER: random")
                results = "random"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: ab WINS")
                results = "ab"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_random_comp(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)
        if check_large_board_winner(game_board, opp_1):
            print("GAME_OVER: random")
            results = "random"
            break
        if check_large_board_winner(game_board, opp_2):
            print("GAME_OVER: ab WINS")
            results = "ab"
            break

        if tie_game_big(game_board):
            print("GAME_OVER: TIE")
            results = "TIE"
            break
        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_alpha_beta(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "random":
        winner = "Agent 1 (random)"
    elif results == "ab":
        winner = "Agent 2 (ab)"
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
    output_file = "results_random_vs_ab.csv"
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


def random_vs_minmax():
    # random
    opp_1 = 1
    # minmax
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
                print("GAME_OVER: random")
                results = "random"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: minmax WINS")
                results = "minmax"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_random_comp(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)
        if check_large_board_winner(game_board, opp_1):
            print("GAME_OVER: random")
            results = "random"
            break
        if check_large_board_winner(game_board, opp_2):
            print("GAME_OVER: minmax WINS")
            results = "minmax"
            break

        if tie_game_big(game_board):
            print("GAME_OVER: TIE")
            results = "TIE"
            break
        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_minimax(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "random":
        winner = "Agent 1 (random)"
    elif results == "minmax":
        winner = "Agent 2 (minmax)"
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
    output_file = "results_random_vs_minmax.csv"
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


def part_geni_vs_ab():
    # part_geni
    opp_1 = 1
    # AB
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
                print("GAME_OVER: part_geni")
                results = "part_geni"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: ab WINS")
                results = "ab"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_part_genious_comp(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_alpha_beta(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "part_geni":
        winner = "Agent 1 (part_geni)"
    elif results == "ab":
        winner = "Agent 2 (ab)"
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
    output_file = "results_part_geni_vs_ab.csv"
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


def part_geni_vs_minmax():
    # part_geni
    opp_1 = 1
    # minmax
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
                print("GAME_OVER: part_geni")
                results = "part_geni"
                break
            if check_large_board_winner(game_board, opp_2):
                print("GAME_OVER: minmax WINS")
                results = "minmax"
                break

            if tie_game_big(game_board):
                print("GAME_OVER: TIE")
                results = "TIE"
                break

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_part_genious_comp(
            opp_1, opp_2, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        game_board, NEXT_BOARD_X, NEXT_BOARD_Y = agent_minimax(
            opp_2, opp_1, game_board, NEXT_BOARD_X, NEXT_BOARD_Y)

        # Record the move
        moves.append((game_board.copy(), NEXT_BOARD_X, NEXT_BOARD_Y))

    end_time = time.time()
    game_time = end_time - start_time
    # Extract insights
    if results == "part_geni":
        winner = "Agent 1 (part_geni)"
    elif results == "minmax":
        winner = "Agent 2 (minmax)"
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
    output_file = "results_part_geni_vs_minmax.csv"
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


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-ab_vs_ab",
                        "--ab_vs_ab",
                        dest="ab_vs_ab",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    parser.add_argument("-ab_vs_minmax",
                        "--ab_vs_minmax",
                        dest="ab_vs_minmax",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    parser.add_argument("-minmax_vs_ab",
                        "--minmax_vs_ab",
                        dest="minmax_vs_ab",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)
    parser.add_argument("-random_vs_ab",
                        "--random_vs_ab",
                        dest="random_vs_ab",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)
    parser.add_argument("-random_vs_minmax",
                        "--random_vs_minmax",
                        dest="random_vs_minmax",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    parser.add_argument("-part_geni_vs_ab",
                        "--part_geni_vs_ab",
                        dest="part_geni_vs_ab",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    parser.add_argument("-part_geni_vs_minmax",
                        "--part_geni_vs_minmax",
                        dest="part_geni_vs_minmax",
                        # help="If you want whether play locally or globally",
                        action=argparse.BooleanOptionalAction,
                        default=False)

    args = parser.parse_args()

    ab_vs_ab_mode = args.ab_vs_ab
    ab_vs_minmax_mode = args.ab_vs_minmax
    minmax_vs_ab_mode = args.minmax_vs_ab
    random_vs_ab_mode = args.random_vs_ab
    random_vs_minmax_mode = args.random_vs_minmax
    part_geni_vs_ab_mode = args.part_geni_vs_ab
    part_geni_vs_minmax_mode = args.part_geni_vs_minmax

    if ab_vs_ab_mode:
        ab_vs_ab()
    if ab_vs_minmax_mode:
        ab_vs_minmax()
    if minmax_vs_ab_mode:
        minmax_vs_ab()
    if random_vs_ab_mode:
        random_vs_ab()
    if random_vs_minmax_mode:
        random_vs_minmax()
    if part_geni_vs_ab_mode:
        part_geni_vs_ab()
    if part_geni_vs_minmax_mode:
        part_geni_vs_minmax()


if __name__ == "__main__":
    main()
