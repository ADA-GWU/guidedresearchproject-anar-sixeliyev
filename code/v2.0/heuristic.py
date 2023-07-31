import numpy as np


def calcScore(arr):
    arr_sum = np.sum(arr)
    abs_arr_sum = abs(arr_sum)
    # print('=====> arr', arr, arr_sum, abs_arr_sum, np.sum(np.abs(arr)))
    if (arr_sum == 0):
        return 0
    if (abs_arr_sum < np.sum(np.abs(arr))):
        return 0

    # player = arr_sum / abs_arr_sum
    # score = 10**(abs_arr_sum - 1)

    return (arr_sum / abs_arr_sum) * (10**(abs_arr_sum - 1))


def calc_row_scores(board, target):
    score = 0
    for x in range(board.shape[0]):
        for y in range(board.shape[0] - target + 1):
            # print(board)
            # print('=====> row score', score)
            score = score + calcScore(board[x, y:y + target])
    return score


def calc_column_scores(board, target):
    score = 0
    for x in range(board.shape[0] - target + 1):
        for y in range(board.shape[0]):
            # print('=====> ', x, y)

            score = score + calcScore(board[x:x + target, y])
    # print('=====> calc_column_scores', score)
    return score


def calc_diagonal_scores(board, target):
    score = 0
    for x in range(board.shape[0] - target + 1):
        for y in range(board.shape[0] - target + 1):
            score = score + calcScore(np.diag(board[x:x+target, y:y+target]))\
                + calcScore(np.diag(np.fliplr(board[x:x+target, y:y+target])))
    return score


# def extract_cols(matrix, m):
#   """
#   Extracts columns with m number of elements from matrix
#   """
#   n = matrix.shape[0]
#   shape = (n - m + 1, n, m)
#   strides = matrix.strides + (matrix.strides[0], )
#   windows = np.lib.stride_tricks.as_strided(matrix,
#                                             shape=shape,
#                                             strides=strides)
#   return windows.reshape(-1, m)

# def calc_row_col_scores(board, target):
#   score = 0
#   rc = np.vstack((extract_cols(board.T, target), extract_cols(board, target)))
#   for arr in rc:
#     score = score + calcScore(arr)
#   return score


def get_board_tuple(board, target):
    board_tuple = tuple(map(tuple, board))
    board_target_tuple = (board_tuple, target)
    return board_target_tuple


def evaluate_board(board, target, memory={}):
    if (get_board_tuple(board, target) in memory):
        print('=====> inside the memory')
        return memory[get_board_tuple(board, target)]

    score = calc_row_scores(board, target) + calc_column_scores(board,
                                                                target) + calc_diagonal_scores(board, target)
    # print('=====>', calc_row_scores(board, target), calc_column_scores(
    #     board, target), calc_diagonal_scores(board, target), score)
    #! TEMPORARILY - not using memorization
    # memory[get_board_tuple(board, target)] = score
    return score


def evaluate_small_large_board(ultimate_board, player, opponent):
    return heur1(ultimate_board, player, opponent) + heur2(ultimate_board, player, opponent)
# Helper function to check if two positions are part of a winning sequence


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


def check_small_board_winner(small_board, player):
    for i in range(3):
        if small_board[i][0] == small_board[i][1] == small_board[i][2] == player:
            return True
        if small_board[0][i] == small_board[1][i] == small_board[2][i] == player:
            return True
    if small_board[0][0] == small_board[1][1] == small_board[2][2] == player:
        return True
    if small_board[0][2] == small_board[1][1] == small_board[2][0] == player:
        return True
    return False


def check_large_board_winner(ultimate_board, player):
    for i in range(3):
        if check_small_board_winner(ultimate_board[i][0], player) and check_small_board_winner(ultimate_board[i][1], player) and check_small_board_winner(ultimate_board[i][2], player):
            return True
        if check_small_board_winner(ultimate_board[0][i], player) and check_small_board_winner(ultimate_board[1][i], player) and check_small_board_winner(ultimate_board[2][i], player):
            return True
    if check_small_board_winner(ultimate_board[0][0], player) and check_small_board_winner(ultimate_board[1][1], player) and check_small_board_winner(ultimate_board[2][2], player):
        return True
    if check_small_board_winner(ultimate_board[0][2], player) and check_small_board_winner(ultimate_board[1][1], player) and check_small_board_winner(ultimate_board[2][0], player):
        return True
    return False
