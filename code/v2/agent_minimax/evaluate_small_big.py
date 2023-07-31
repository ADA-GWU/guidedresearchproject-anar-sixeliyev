import numpy as np

from board import *


def evaluate_small_large_board(ultimate_board, player, opponent):
    return heur1(ultimate_board, player, opponent) + heur2(ultimate_board, player, opponent)


def is_winning_sequence(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2)

# Heuristic 1 (heur1)


def heur1(ultimate_board, player, opponent):
    if check_large_board_winner(ultimate_board, player):
        return 10000
    elif check_large_board_winner(ultimate_board, opponent):
        return -10000
    else:
        return 0

# Heuristic 2 (heur2)


def heur2(ultimate_board, player, opponent):
    score = 0

    for i in range(3):
        for j in range(3):
            small_board = ultimate_board[i][j]
            if check_small_board_winner(small_board, player):
                score += 5
            elif check_small_board_winner(small_board, opponent):
                score -= 5

            if small_board[1][1] == player:
                score += 10
            elif small_board[1][1] == opponent:
                score -= 10

            if small_board[0][0] == player or small_board[0][2] == player or small_board[2][0] == player or small_board[2][2] == player:
                score += 3
            elif small_board[0][0] == opponent or small_board[0][2] == opponent or small_board[2][0] == opponent or small_board[2][2] == opponent:
                score -= 3

    for i in range(3):
        for j in range(3):
            for x in range(3):
                for y in range(3):
                    if is_winning_sequence(i, j, x, y):
                        if ultimate_board[i][j][x][y] == player and ultimate_board[x][y][i][j] == player:
                            score += 4
                        elif ultimate_board[i][j][x][y] == opponent and ultimate_board[x][y][i][j] == opponent:
                            score -= 4
                    if is_winning_sequence(x, y, 1, 1):
                        if ultimate_board[i][j][x][y] == player and ultimate_board[i][j][1][1] == player:
                            score += 2
                        elif ultimate_board[i][j][x][y] == opponent and ultimate_board[i][j][1][1] == opponent:
                            score -= 2

    return score
