import numpy as np


def get_board_tuple(board):
    board_tuple = tuple(map(tuple, board))
    return board_tuple


def get_ultimate_board_tuple(ultimate_board):
    ultimate_board_tuple = tuple(tuple(map(tuple, board))
                                 for board in ultimate_board)
    return ultimate_board_tuple


def convert_to_tuple(board):
    return tuple(map(tuple, board))


def evaluate_board_ult(ultimate_board, player, opponent, memory={}):
    board_tuple = tuple(tuple(convert_to_tuple(small_board)
                        for small_board in row) for row in ultimate_board)

    if (board_tuple in memory):
        print('=====> inside the memory')
        return memory[board_tuple]

    score = 0

    # Evaluate small boards
    for i in range(3):
        for j in range(3):
            small_board = ultimate_board[i][j]
            if check_small_board_winner(small_board, player):
                score += 100
            elif check_small_board_winner(small_board, opponent):
                score -= 100

    # Evaluate large board
    if check_large_board_winner(ultimate_board, player):
        score += 1000
    elif check_large_board_winner(ultimate_board, opponent):
        score -= 1000

    # Evaluate player's control over the next small board move
    player_control = count_next_small_board_moves(ultimate_board, player)
    opponent_control = count_next_small_board_moves(ultimate_board, opponent)
    # print('player_control, opponent_control', player_control, opponent_control)
    score += (player_control - opponent_control) * 10

    memory[board_tuple] = score

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

# def check_small_board_winner_2(small_board, player):
#     if np.all(small_board == player):
#         return True
#     for i in range(3):
#         if np.all(small_board[i] == player) or np.all(small_board[:, i] == player):
#             return True
#     if np.all(np.diag(small_board) == player) or np.all(np.diag(np.fliplr(small_board)) == player):
#         return True
#     return False

# def check_large_board_winner_2(ultimate_board, player):
#     for i in range(3):
#         if check_small_board_winner(ultimate_board[i][0], player) and \
#            check_small_board_winner(ultimate_board[i][1], player) and \
#            check_small_board_winner(ultimate_board[i][2], player):
#             return True
#         if check_small_board_winner(ultimate_board[0][i], player) and \
#            check_small_board_winner(ultimate_board[1][i], player) and \
#            check_small_board_winner(ultimate_board[2][i], player):
#             return True
#     if check_small_board_winner(ultimate_board[0][0], player) and \
#        check_small_board_winner(ultimate_board[1][1], player) and \
#        check_small_board_winner(ultimate_board[2][2], player):
#         return True
#     if check_small_board_winner(ultimate_board[0][2], player) and \
#        check_small_board_winner(ultimate_board[1][1], player) and \
#        check_small_board_winner(ultimate_board[2][0], player):
#         return True
#     return False


def check_large_board_winner(ultimate_board, player):
    # for i in range(3):
    #     if check_small_board_winner([ultimate_board[i][j] for j in range(3)], player):
    #         return True
    #     if check_small_board_winner([ultimate_board[j][i] for j in range(3)], player):
    #         return True
    # if check_small_board_winner([ultimate_board[i][i] for i in range(3)], player):
    #     return True
    # if check_small_board_winner([ultimate_board[i][2 - i] for i in range(3)], player):
    #     return True
    # return False
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


def count_next_small_board_moves(ultimate_board, player):
    count = 0
    previous_move = find_previous_move(ultimate_board)
    if previous_move is not None:
        small_board_x, small_board_y = previous_move
        small_board = ultimate_board[small_board_x][small_board_y]
        count = sum(1 for row in small_board for cell in row if cell == 0)
    return count


def find_previous_move(ultimate_board):
    for i in range(3):
        for j in range(3):
            small_board = ultimate_board[i][j]
            if not check_small_board_winner(small_board, 1) and not check_small_board_winner(small_board, -1):
                for x in range(3):
                    for y in range(3):
                        if small_board[x][y] == 0:
                            return i, j
    return None
