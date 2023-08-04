import numpy as np

from board import *


def evaluate_small_large_board(ultimate_board, player, opponent, POS_X, POS_Y):
    return heur1(ultimate_board, player, opponent) + heur2(ultimate_board, player, opponent, POS_X, POS_Y)


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


def heur2(ultimate_board, player, opponent, current_board_POS_X, current_board_POS_Y):
    score = 0
    # print('NEXT POS_X, POS_Y', current_board_POS_X, current_board_POS_Y)
    center_board_terminated = terminated_small(ultimate_board[1][1])
    for i in range(3):
        for j in range(3):
            small_board = ultimate_board[i][j]
            if check_small_board_winner(small_board, player):
                score += 20
                # print(' check_small_board_winner player', i, j,  score)

            elif check_small_board_winner(small_board, opponent):
                score -= 20
                # print(' check_small_board_winner opponent', i, j,  score)

            # if already checked for the win, dont add points for center as well(already +-15)

            else:
                if (not center_board_terminated):
                    if small_board[1][1] == player:
                        score += 10
                        # print(' small_board center player', i, j,  score)
                    elif small_board[1][1] == opponent:
                        score -= 10
                        # print(' small_board center opponent', i, j,  score)

                if small_board[0][0] == player or small_board[0][2] == player or small_board[2][0] == player or small_board[2][2] == player:
                    score += 5
                    # print(' small_board corner player', i, j,  score)

                elif small_board[0][0] == opponent or small_board[0][2] == opponent or small_board[2][0] == opponent or small_board[2][2] == opponent:
                    score -= 5
                    # print(' small_board corner opponent', i, j,  score)

    for i in range(3):
        for j in range(3):
            # appearance_sum = 0
            # if (i == current_board_POS_X and j == current_board_POS_Y):
            #     for x in range(3):
            #         for y in range(3):
            # if terminated_small(ultimate_board[x][y]):
            # print("decreased the score", x, y)
            #     score -= 10
            for x in range(3):
                for y in range(3):
                    # if (i == current_board_POS_X and j == current_board_POS_Y):
                    #     if terminated_small(ultimate_board[x][y]):
                    # print("decreased the score", x, y)
                    #         score -= 10
                    #         continue
                    # appearance_sum += ultimate_board[i][j][x][y]
                    if is_winning_sequence(i, j, x, y):
                        if ultimate_board[i][j][x][y] == player and ultimate_board[x][y][i][j] == player and not i == j == x == y == 1:
                            # score += 6
                            score += 4
                            # print('is_winning_sequence player',
                            #       i, j, x, y,  score)

                        elif ultimate_board[i][j][x][y] == opponent and ultimate_board[x][y][i][j] == opponent and not i == j == x == y == 1:
                            # score += 6
                            score -= 4

                            # print(' is_winning_sequence opponent',
                            #       i, j, x, y,  score)

                    if is_winning_sequence(x, y, 1, 1):
                        if ultimate_board[i][j][x][y] == player and ultimate_board[i][j][1][1] == player:
                            # score += 8
                            score += 2
                            # print(
                            #     'is_winning_sequence player with center', i, j, x, y,  score)

                        elif ultimate_board[i][j][x][y] == opponent and ultimate_board[i][j][1][1] == opponent:
                            # score -= 8
                            score -= 2
                            # print(
                            #     'is_winning_sequence opponent with center', i, j, x, y,  score)

            # print(appearance_sum, ultimate_board[i][j])
            # score += appearance_sum

    return score


if __name__ == "__main__":
    # Sample ultimate_board
    ultimate_board = np.array([
        [
            [[0, 0, 0], [0, -1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ],
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 0, 0], [0, 1, -1], [0, 0, -1]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ],
        [
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        ]
    ])
    # ultimate_board = np.array([
    #     [
    #         [[1, 1, 1], [0, -1, 0], [0, 0, 0]],
    #         [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    #         [[-1, 0, 1], [0, -1, -1], [0, 0, 1]]
    #     ],
    #     [
    #         [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    #         [[-1, 0, 1], [-1, 1, 0], [1, 0, 0]],
    #         [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
    #     ],
    #     [
    #         [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #         [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    #         [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #     ]
    # ])

    # Player and opponent
    player = -1
    opponent = 1

    # Test the heuristic function
    print_ultimate_board(ultimate_board)
    result = heur2(ultimate_board, player, opponent, 1, 1)
    print("Heuristic Score:", result)
