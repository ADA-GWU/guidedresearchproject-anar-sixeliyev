import numpy as np
import argparse


def local_playing():
    board_size = 3
    target = 3
    agent_player = 1
    memory = {}
    game_board = np.zeros((board_size, board_size, 3, 3), dtype=np.int32)
    opp_player = -agent_player

    if agent_player == 1:
        print("AI Plays...")
        pos_x, pos_y = best_next_move(game_board, target, agent_player,
                                      opp_player, 3, memory)
        game_board[pos_x, pos_y] = agent_player
        print(game_board)
        print("AI Played in position ({},{})".format(pos_x, pos_y))
        print("====================")

    current_small_board = None

    while True:
        if check_large_board_win(game_board, target) == agent_player:
            print("GAME_OVER: COMPUTER WINS")
            break
        if check_large_board_win(game_board, target) == opp_player:
            print("GAME_OVER: HUMAN WINS")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break

        print("Human Plays...")
        pos_x, pos_y = opp_play()
        while (game_board[current_small_board[0], current_small_board[1], pos_x, pos_y] != 0):
            print("Select an empty cell please:")
            pos_x, pos_y = opp_play()
        game_board[current_small_board[0],
                   current_small_board[1], pos_x, pos_y] = opp_player
        print(game_board)
        print("Human Played")
        print("====================")

        if check_small_board_win(game_board[current_small_board[0], current_small_board[1]], target) == opp_player:
            print("Small Board Won by HUMAN")
            game_board[current_small_board[0],
                       current_small_board[1]] = np.full((3, 3), opp_player)

        if check_large_board_win(game_board, target) == opp_player:
            print("GAME_OVER: HUMAN WINS")
            break

        if tie_game(game_board):
            print("GAME_OVER: TIE")
            break

        print("AI Plays...")
        pos_x, pos_y = best_next_move(game_board, target, agent_player,
                                      opp_player, 3, memory)
        game_board[pos_x, pos_y] = agent_player
        print(game_board)
        print("AI Played in position ({},{})".format(pos_x, pos_y))
        print("====================")

        if check_small_board_win(game_board[pos_x, pos_y], target) == agent_player:
            print("Small Board Won by COMPUTER")
            game_board[pos_x, pos_y] = np.full((3, 3), agent_player)

        current_small_board = (pos_x % 3, pos_y % 3)


# Rest of the code remains the same

# ... (the rest of the code remains the same)

# Modify the minimax function to handle NumPy arrays correctly
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
                if np.all(board[i, j] == 0):  # Use np.all to check the entire array

                    board[i, j] = agentNo
                    val = minimax(board, depth - 1, alpha, beta, target, False,
                                  agentNo, oppNo, memory)
                    board[i, j] = 0

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
                if np.all(board[i, j] == 0):  # Use np.all to check the entire array

                    board[i, j] = oppNo
                    val = minimax(board, depth - 1, alpha, beta, target, True,
                                  agentNo, oppNo, memory)
                    board[i, j] = 0

                    min_Val = min(min_Val, val)

                    # alph-beta
                    beta = min(beta, min_Val)
                    if (beta <= alpha):
                        break
        return min_Val


# Modify the best_next_move function to handle NumPy arrays correctly
def best_next_move(board, target, agentNo, oppNo, depth=3, memory={}):
    best_move = []
    best_val = -np.inf
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if np.all(board[i, j] == 0):  # Use np.all to check the entire array
                board[i, j] = agentNo

                if check_large_board_win(board, target) == agentNo:
                    board[i, j] = 0
                    return [i, j]

                v = minimax(board, depth, -np.inf, np.inf, target, False,
                            agentNo, oppNo, memory)
                board[i, j] = 0
                if (v > best_val):
                    best_val = v
                    best_move = [i, j]
    return best_move


# Add these functions to check for small board wins and get the next move from the human player
def check_large_board_win(board, target):
    for x in range(board.shape[0] - target + 1):
        for y in range(board.shape[0] - target + 1):
            if np.all(np.diag(board[x:x + target, y:y + target]) == 1):
                return 1
            elif np.all(np.diag(board[x:x + target, y:y + target]) == -1):
                return -1

            if np.all(np.diag(np.fliplr(board[x:x + target, y:y + target])) == 1):
                return 1
            elif np.all(np.diag(np.fliplr(board[x:x + target, y:y + target])) == -1):
                return -1

            if np.all(np.sum(board[x:x + target, y:y + target], axis=0) == target) or np.all(
                    np.sum(board[x:x + target, y:y + target], axis=0) == -target):
                return 1
            if np.all(np.sum(board[x:x + target, y:y + target], axis=1) == target) or np.all(
                    np.sum(board[x:x + target, y:y + target], axis=1) == -target):
                return 1
    return 0

# Add these functions to check for small board wins and get the next move from the human player


def check_small_board_win(board, target):
    for x in range(board.shape[0]):
        for y in range(board.shape[0] - target + 1):
            if np.all(board[x, y:y + target] == 1):
                return 1
            elif np.all(board[x, y:y + target] == -1):
                return -1
    return 0


def tie_game(board):
    return np.count_nonzero(board) == board.size


def check_rows(board, target):
    for x in range(board.shape[0]):
        for y in range(board.shape[0]-target+1):
            if np.all(board[x, y:y+target] == 1):
                return 1
            elif np.all(board[x, y:y+target] == -1):
                return -1
    return 0


def check_columns(board, target):
    for x in range(board.shape[0]-target+1):
        for y in range(board.shape[0]):
            if np.all(board[x:x+target, y] == 1):
                return 1
            elif np.all(board[x:x+target, y] == -1):
                return -1
    return 0


def check_diagonals(board, target):
    for x in range(board.shape[0]-target+1):
        for y in range(board.shape[0]-target+1):
            if np.all(np.diag(board[x:x+target, y:y+target]) == 1):
                return 1
            elif np.all(np.diag(board[x:x+target, y:y+target]) == -1):
                return -1

            if np.all(np.diag(np.fliplr(board[x:x+target, y:y+target])) == 1):
                return 1
            elif np.all(np.diag(np.fliplr(board[x:x+target, y:y+target])) == -1):
                return -1
    return 0


def game_end(board, target):
    r = check_rows(board, target)
    if r != 0:
        return r
    c = check_columns(board, target)
    if c != 0:
        return c
    d = check_diagonals(board, target)
    if d != 0:
        return d

    return 0


def terminated(board, target):
    return game_end(board, target) != 0 or tie_game(board)


def get_successors(board, player):
    arr_successors = []
    for i in range(board.shape[0]):
        for j in range(board.shape[0]):
            if board[i][j] == 0:
                temp_board = board.copy()
                temp_board[i][j] = player
                arr_successors.append(temp_board)
    return arr_successors


def opp_play():
    x, y = map(int, input("Enter row and column (space-separated): ").split())
    return x, y


if __name__ == "__main__":
    local_playing()
