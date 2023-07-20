import numpy as np


def calcScore(arr):
    arr_sum = np.sum(arr)
    abs_arr_sum = abs(arr_sum)
    return (arr_sum / abs_arr_sum) * (10 ** (abs_arr_sum - 1)) if arr_sum != 0 and abs_arr_sum >= np.sum(np.abs(arr)) else 0


def calc_scores(board, target, axis):
    score = 0
    for i in range(board.shape[axis] - target + 1):
        slices = [slice(i, i + target) if j == axis else slice(None)
                  for j in range(board.ndim)]
        score += calcScore(board[tuple(slices)])
    return score


def calc_row_scores(board, target):
    return np.sum([calc_scores(board, target, axis=1)])


def calc_column_scores(board, target):
    return np.sum([calc_scores(board, target, axis=0)])


def calc_diagonal_scores(board, target):
    diags = [board.diagonal(
        offset=i) for i in range(-board.shape[0] + 1 + target, board.shape[1] - target + 1)]
    flipped_diags = [np.fliplr(board).diagonal(
        offset=i) for i in range(-board.shape[0] + 1 + target, board.shape[1] - target + 1)]
    return np.sum([calcScore(diag) for diag in diags]) + np.sum([calcScore(diag) for diag in flipped_diags])


def get_board_tuple(board, target):
    return tuple(map(tuple, board)), target


def evaluate_board(board, target, memory={}):
    board_target_tuple = get_board_tuple(board, target)
    if board_target_tuple in memory:
        return memory[board_target_tuple]
    score = calc_row_scores(board, target) + calc_column_scores(board,
                                                                target) + calc_diagonal_scores(board, target)
    memory[board_target_tuple] = score
    return score
