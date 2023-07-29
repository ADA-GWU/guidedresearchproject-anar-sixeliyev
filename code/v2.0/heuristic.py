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
