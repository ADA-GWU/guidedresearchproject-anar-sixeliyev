import numpy as np
from heuristic import *
from board import *
from evaluate import *
from evaluate_big import *


def minimax(board,
            depth,
            alpha,
            beta,
            target,
            isMax,
            agentNo,
            oppNo,
            memory={}):
    # board_val = evaluate_board(board, target, memory) * agentNo
    board_val = evaluateBoard(board, agentNo, oppNo)
    if (depth == 0 or terminated(board)):
        return board_val
    # Maximizing player
    if (isMax):
        max_Val = -np.inf
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if (board[i][j] == 0):

                    board[i][j] = agentNo
                    val = minimax(board, depth - 1, alpha, beta, target, False,
                                  agentNo, oppNo, memory)
                    board[i][j] = 0

                    max_Val = max(max_Val, val)

                    # alph-beta
                    alpha = max(alpha, max_Val)
                    if (beta <= alpha):
                        break
        return max_Val
    else:
        min_Val = np.inf
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if (board[i][j] == 0):

                    board[i][j] = oppNo
                    # print('==================== depth', depth)
                    val = minimax(board, depth - 1, alpha, beta, target, True,
                                  agentNo, oppNo, memory)
                    board[i][j] = 0

                    min_Val = min(min_Val, val)

                    # alph-beta
                    beta = min(beta, min_Val)
                    if (beta <= alpha):
                        break
        return min_Val


def best_next_move(board, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    # depth = 3
    print('====> board.shape', board.shape)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if (board[i][j] == 0):
                board[i][j] = agentNo

                # optimization: if winning, then return
                if (game_end(board, target) == agentNo):
                    #                     print("game end with winning")
                    board[i][j] = 0
                    return [i, j]
                # calling minimax
                v = minimax(board, depth, -np.inf, np.inf, target, False,
                            agentNo, oppNo, memory)
                # print("value is {} for coordinates({},{})".format(v, i, j))
                print("Board evaluation after playing {},{}:{}".format(
                    i, j, evaluate_board(board, target)))
                board[i][j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [i, j]
    return best_move


def best_next_move_ult(ultimate_board, target, agentNo, oppNo, depth=3, memory={}):
    best_move = None
    best_val = -np.inf

    for i in range(3):
        for j in range(3):
            if check_small_board_winner(ultimate_board[i][j], agentNo) or check_small_board_winner(ultimate_board[i][j], oppNo):
                continue
            for x in range(3):
                for y in range(3):
                    if ultimate_board[i][j][x][y] == 0:
                        ultimate_board[i][j][x][y] = agentNo

                        # Optimization: if winning move, then return immediately
                        if check_small_board_winner(ultimate_board[i][j], agentNo):
                            ultimate_board[i][j][x][y] = 0
                            return (i, j, x, y)

                        val = minimax_ult(ultimate_board, depth, -np.inf,
                                          np.inf, target, False, agentNo, oppNo, memory)
                        ultimate_board[i][j][x][y] = 0

                        if val > best_val:
                            best_val = val
                            best_move = (i, j, x, y)

    return best_move


def minimax_ult(ultimate_board, depth, alpha, beta, target, isMax, agentNo, oppNo, memory={}):
    board_val = evaluate_board_ult(ultimate_board, agentNo, oppNo)

    if depth == 0 or terminated(ultimate_board):
        return board_val

    # Maximizing player
    if isMax:
        max_Val = -np.inf
        for i in range(3):
            for j in range(3):
                if check_small_board_winner(ultimate_board[i][j], agentNo) or check_small_board_winner(ultimate_board[i][j], oppNo):
                    continue

                for x in range(3):
                    for y in range(3):
                        if ultimate_board[i][j][x][y] == 0:
                            ultimate_board[i][j][x][y] = agentNo
                            val = minimax_ult(
                                ultimate_board, depth - 1, alpha, beta, target, False, agentNo, oppNo, memory)
                            ultimate_board[i][j][x][y] = 0

                            max_Val = max(max_Val, val)
                            alpha = max(alpha, max_Val)

                            if beta <= alpha:
                                break
        return max_Val
    else:
        min_Val = np.inf
        for i in range(3):
            for j in range(3):
                if check_small_board_winner(ultimate_board[i][j], agentNo) or check_small_board_winner(ultimate_board[i][j], oppNo):
                    # Small board is already won, skip it.
                    continue

                for x in range(3):
                    for y in range(3):
                        if ultimate_board[i][j][x][y] == 0:
                            ultimate_board[i][j][x][y] = oppNo
                            val = minimax_ult(
                                ultimate_board, depth - 1, alpha, beta, target, True, agentNo, oppNo, memory)
                            ultimate_board[i][j][x][y] = 0

                            min_Val = min(min_Val, val)
                            beta = min(beta, min_Val)

                            if beta <= alpha:
                                break
        return min_Val


def best_next_move_small(board, POS_X, POS_Y, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    small_board = board[POS_X, POS_Y]
    print('====> board.shape', board.shape)
    for i in range(3):
        for j in range(3):
            if (small_board[i][j] == 0):
                small_board[i][j] = agentNo

                # optimization: if winning, then return
                if (game_end(small_board, target) == agentNo):
                    #                     print("game end with winning")
                    small_board[i][j] = 0
                    return [POS_X, POS_Y, i, j]
                # calling minimax
                v = minimax_ult(board, depth, -np.inf, np.inf, target, False,
                                agentNo, oppNo, memory)
                # print("value is {} for coordinates({},{})".format(v, i, j))
                # print("Board evaluation after playing {},{}:{}".format(
                #     i, j, evaluate_board_ult(board, target)))
                small_board[i][j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [POS_X, POS_Y, i, j]
    return best_move


def best_next_move_small_large(board, POS_X, POS_Y, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    small_board = board[POS_X, POS_Y]

    for i in range(3):
        for j in range(3):
            if (small_board[i][j] == 0):
                small_board[i][j] = agentNo

                # optimization: if winning, then return
                if (check_large_board_winner(board, agentNo) or check_large_board_winner(board, oppNo)):
                    #                     print("game end with winning")
                    small_board[i][j] = 0
                    return [POS_X, POS_Y, i, j]
                # calling minimax
                v = minimax_small_large(board, POS_X, POS_Y, depth, -np.inf, np.inf, target, False,
                                        agentNo, oppNo, memory)
                # print("value is {} for coordinates({},{})".format(v, i, j))
                # print("Board evaluation after playing {},{}:{}".format(
                #     i, j, evaluate_board_ult(board, target)))
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
                    val = minimax_small_large(board, POS_X, POS_Y, depth - 1, alpha, beta, target, False,
                                              agentNo, oppNo, memory)
                    small_board[i][j] = 0

                    max_Val = max(max_Val, val)

                    # alph-beta
                    alpha = max(alpha, max_Val)
                    if (beta <= alpha):
                        break
        return max_Val
    else:
        min_Val = np.inf
        for i in range(3):
            for j in range(3):
                if (small_board[i][j] == 0):

                    small_board[i][j] = oppNo
                    val = minimax_small_large(board, POS_X, POS_Y, depth - 1, alpha, beta, target, True,
                                              agentNo, oppNo, memory)
                    small_board[i][j] = 0

                    min_Val = min(min_Val, val)

                    # alph-beta
                    beta = min(beta, min_Val)
                    if (beta <= alpha):
                        break
        return min_Val
