# def evaluate(b, player, opponent):

#     # Checking for Rows for X or O victory.
#     for row in range(3):
#         if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
#             if (b[row][0] == player):
#                 return 10
#             elif (b[row][0] == opponent):
#                 return -10

#     # Checking for Columns for X or O victory.
#     for col in range(3):

#         if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

#             if (b[0][col] == player):
#                 return 10
#             elif (b[0][col] == opponent):
#                 return -10

#     # Checking for Diagonals for X or O victory.
#     if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

#         if (b[0][0] == player):
#             return 10
#         elif (b[0][0] == opponent):
#             return -10

#     if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

#         if (b[0][2] == player):
#             return 10
#         elif (b[0][2] == opponent):
#             return -10

#     # Else if none of them have won then return 0
#     return 0

def evaluateBoard(board, player, opponent):
    score = 0

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            score += 10
        if board[0][i] == board[1][i] == board[2][i] == player:
            score += 10
        if board[i][0] == board[i][1] == board[i][2] == opponent:
            score -= 10
        if board[0][i] == board[1][i] == board[2][i] == opponent:
            score -= 10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        score += 10
    if board[0][2] == board[1][1] == board[2][0] == player:
        score += 10
    if board[0][0] == board[1][1] == board[2][2] == opponent:
        score -= 10
    if board[0][2] == board[1][1] == board[2][0] == opponent:
        score -= 10

    return score
