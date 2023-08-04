from board import *
# from minimax import *
# import minimax
from . import minimax
import random
import numpy as np
import sys
print('=======> BEFORE sys.path', sys.path)
sys.path.append(sys.path[0]+'/agent_part_genious')
print('=======> AFTER sys.path', sys.path)


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
                v = minimax.minimax(board, depth, -np.inf, np.inf, target, False,
                            agentNo, oppNo, memory)
                board[i][j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [i, j]
    return best_move


def get_random_board(ultimate_board):
    valid_moves = get_valid_boards(ultimate_board)
    if not valid_moves:
        return None
    return random.choice(valid_moves)


def get_valid_boards(ultimate_board):
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if not terminated(ultimate_board[i][j], 3):
                valid_moves.append((i, j))
    return valid_moves


def terminated(board, target):
    return game_end(board, target) != 0 or tie_game_small(board)


def terminated_small(board):
    return check_small_board_winner(board, 1) or check_small_board_winner(board, -1) or tie_game_small(board)


def agent_part_genious_comp(agent_player, opp_player, game_board, NEXT_BOARD_X, NEXT_BOARD_Y, depth=3,  memory={}):
    board_size = 3
    target = 3
    memory = {}
    if len(game_board) == 0:
        game_board = np.zeros(
            (board_size, board_size, board_size, board_size), dtype=np.int32)

    if NEXT_BOARD_X == -1 or NEXT_BOARD_Y == -1 or terminated_small(game_board[NEXT_BOARD_X][NEXT_BOARD_Y]):
        pos_X, pos_Y = get_random_board(game_board)

        small_board = game_board[pos_X, pos_Y]
        pos_x, pos_y = best_next_move(small_board, target, agent_player,
                                      opp_player, 1, memory)
        game_board[pos_X, pos_Y][pos_x, pos_y] = agent_player

    else:
        small_board = game_board[NEXT_BOARD_X, NEXT_BOARD_Y]

        pos_x, pos_y = best_next_move(small_board, target, agent_player,
                                      opp_player, 1, memory)
        game_board[NEXT_BOARD_X, NEXT_BOARD_Y][pos_x, pos_y] = agent_player

    NEXT_BOARD_X = pos_x
    NEXT_BOARD_Y = pos_y
    # print(game_board)
    # print_ultimate_board(game_board)

    print("AI Played in postion ({},{}) - ({},{})".format(NEXT_BOARD_X, NEXT_BOARD_Y, pos_x, pos_y))
    # print("====================")
    return game_board, NEXT_BOARD_X, NEXT_BOARD_Y


if __name__ == "__main__":
    agent_part_genious_comp(1, -1, [], -1, -1)
