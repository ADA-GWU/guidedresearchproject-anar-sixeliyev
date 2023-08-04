import numpy as np


def calcScore(arr):
    arr_sum = np.sum(arr)
    abs_arr_sum = abs(arr_sum)
    if (arr_sum == 0):
        return 0
    if (abs_arr_sum < np.sum(np.abs(arr))):
        return 0

    return (arr_sum / abs_arr_sum) * (10**(abs_arr_sum - 1))


def calc_row_scores(board, target):
    score = 0
    for x in range(board.shape[0]):
        for y in range(board.shape[0] - target + 1):
            score = score + calcScore(board[x, y:y + target])
    return score


def calc_column_scores(board, target):
    score = 0
    for x in range(board.shape[0] - target + 1):
        for y in range(board.shape[0]):
            score = score + calcScore(board[x:x + target, y])
    return score


def calc_diagonal_scores(board, target):
    score = 0
    for x in range(board.shape[0] - target + 1):
        for y in range(board.shape[0] - target + 1):
            score = score + calcScore(np.diag(board[x:x+target,y:y+target]))\
                    +calcScore(np.diag(np.fliplr(board[x:x+target,y:y+target])))
    return score

def get_board_tuple(board, target):
    board_tuple = tuple(map(tuple, board))
    board_target_tuple = (board_tuple, target)
    return board_target_tuple


def evaluate_board(board, target, memory={}):
    if (get_board_tuple(board, target) in memory):
        return memory[get_board_tuple(board, target)]
    score = calc_row_scores(board, target) + calc_column_scores(
        board, target) + calc_diagonal_scores(board, target)
    memory[get_board_tuple(board, target)] = score
    return score
