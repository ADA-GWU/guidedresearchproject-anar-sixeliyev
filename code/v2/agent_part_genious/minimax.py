import numpy as np

# from board import *
# from evaluate import *
from . import evaluate
from . import heuristic
from . import board
# from heuristic import *


def minimax(small_board,
            depth,
            alpha,
            beta,
            target,
            isMax,
            agentNo,
            oppNo,
            memory={}):
    board_val = heuristic.evaluate_board(small_board, target, memory) * agentNo
    # board_val = evaluateBoard(board, agentNo, oppNo)
    if (depth == 0 or board.terminated(small_board, target)):
        return board_val
    # Maximizing player
    if (isMax):
        max_Val = -np.inf
        for i in range(small_board.shape[0]):
            for j in range(small_board.shape[1]):
                if (small_board[i][j] == 0):

                    small_board[i][j] = agentNo
                    val = minimax(small_board, depth - 1, alpha, beta, target, False,
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
        for i in range(small_board.shape[0]):
            for j in range(small_board.shape[1]):
                if (small_board[i][j] == 0):

                    small_board[i][j] = oppNo
                    # print('==================== depth', depth)
                    val = minimax(small_board, depth - 1, alpha, beta, target, True,
                                  agentNo, oppNo,  memory)
                    small_board[i][j] = 0

                    min_Val = min(min_Val, val)

                    # alph-beta
                    beta = min(beta, min_Val)
                    if (beta <= alpha):
                        break
        return min_Val


def best_next_move(small_board, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    # depth = 3
    print('====> board.shape', small_board.shape)
    for i in range(small_board.shape[0]):
        for j in range(small_board.shape[1]):
            if (small_board[i][j] == 0):
                small_board[i][j] = agentNo

                # optimization: if winning, then return
                if (board.game_end(small_board, target) == agentNo):
                    #                     print("game end with winning")
                    small_board[i][j] = 0
                    return [i, j]
                # calling minimax
                v = minimax(small_board, depth, -np.inf, np.inf, target, False,
                            agentNo, oppNo, memory)
                small_board[i][j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [i, j]
    return best_move
