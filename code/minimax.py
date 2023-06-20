import numpy as np
from heuristic import *
from board import *


def minimax(board,
            depth,
            alpha,
            beta,
            target,
            isMax,
            agentNo,
            oppNo,
            memory={}):
    board_val = evaluate_board(board, target, memory) * agentNo
    if (depth == 0 or terminated(board, target)):
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
                #                 print("value is {} for coordinates({},{})".format(v,i,j))
                #                 print("Board evaluation after playing {},{}:{}".format(i,j,evaluate_board(board,target)))
                board[i][j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [i, j]
    return best_move
