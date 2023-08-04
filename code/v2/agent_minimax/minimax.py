import numpy as np

from board import *
from evaluate_big import *
from evaluate_small_big import *


def best_next_move_ult(ultimate_board, target, agentNo, oppNo, depth=3, memory={}):
    best_move = None
    best_val = -np.inf

    for i in range(3):
        for j in range(3):
            if terminated_small(ultimate_board[i][j]):
                continue
            for x in range(3):
                for y in range(3):
                    if ultimate_board[i][j][x][y] == 0:
                        ultimate_board[i][j][x][y] = agentNo

                        # Optimization: if winning move, then return immediately
                        if check_small_board_winner(ultimate_board[i][j], agentNo):
                            ultimate_board[i][j][x][y] = 0
                            return (i, j, x, y)

                        val = minimax_ult(
                            ultimate_board, depth, target, False, agentNo, oppNo, memory)
                        ultimate_board[i][j][x][y] = 0

                        if val > best_val:
                            best_val = val
                            best_move = (i, j, x, y)

    return best_move


def minimax_ult(ultimate_board, depth, target, isMax, agentNo, oppNo, memory={}):
    board_val = evaluate_board_ult(ultimate_board, agentNo, oppNo)

    if depth == 0 or terminated(ultimate_board):
        return board_val

    # Maximizing player
    if isMax:
        max_Val = -np.inf
        for i in range(3):
            for j in range(3):
                if terminated_small(ultimate_board[i][j]):
                    continue

                for x in range(3):
                    for y in range(3):
                        if ultimate_board[i][j][x][y] == 0:
                            ultimate_board[i][j][x][y] = agentNo
                            val = minimax_ult(
                                ultimate_board, depth - 1, target, False, agentNo, oppNo, memory)
                            ultimate_board[i][j][x][y] = 0

                            max_Val = max(max_Val, val)
        return max_Val
    else:
        min_Val = np.inf
        for i in range(3):
            for j in range(3):
                if terminated_small(ultimate_board[i][j]):
                    # Small board is already won, skip it.
                    continue

                for x in range(3):
                    for y in range(3):
                        if ultimate_board[i][j][x][y] == 0:
                            ultimate_board[i][j][x][y] = oppNo
                            val = minimax_ult(
                                ultimate_board, depth - 1, target, True, agentNo, oppNo, memory)
                            ultimate_board[i][j][x][y] = 0

                            min_Val = min(min_Val, val)
        return min_Val


def best_next_move_small_large(board, POS_X, POS_Y, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    small_board = board[POS_X, POS_Y]

    for i in range(3):
        for j in range(3):
            if (small_board[i][j] == 0):
                small_board[i][j] = agentNo

                if (check_large_board_winner(board, agentNo) or check_large_board_winner(board, oppNo)):
                    small_board[i][j] = 0
                    return [POS_X, POS_Y, i, j]
                v = minimax_small_large(board, POS_X, POS_Y, depth, target, False,
                                        agentNo, oppNo, memory)
                small_board[i][j] = 0

                if (v > best_val):
                    best_val = v
                    best_move = [POS_X, POS_Y, i, j]
    return best_move


def minimax_small_large(board,
                        POS_X, POS_Y,
                        depth,
                        alpha,
                        beta,
                        target,
                        isMax,
                        agentNo,
                        oppNo,
                        memory={}):
    board_val = evaluate_small_large_board(board, agentNo, oppNo)
    small_board = board[POS_X, POS_Y]
    if (depth == 0) or terminated(board):
        return board_val

    # Maximizing player
    if (isMax):
        max_Val = -np.inf
        for i in range(3):
            for j in range(3):
                if (small_board[i][j] == 0):

                    small_board[i][j] = agentNo
                    val = minimax_small_large(board, POS_X, POS_Y, depth - 1, target, False,
                                              agentNo, oppNo, memory)
                    small_board[i][j] = 0

                    max_Val = max(max_Val, val)

        return max_Val
    else:
        min_Val = np.inf
        for i in range(3):
            for j in range(3):
                if (small_board[i][j] == 0):

                    small_board[i][j] = oppNo
                    val = minimax_small_large(board, POS_X, POS_Y, depth - 1, target, True,
                                              agentNo, oppNo, memory)
                    small_board[i][j] = 0

                    min_Val = min(min_Val, val)

        return min_Val
