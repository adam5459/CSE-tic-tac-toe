
import math , copy 

X = 'X'
O = 'O'
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],]

def player(board):
    xcount, ocount = 0, 0
    for row in board:
        for item in row:
            if item == X:
                xcount += 1
            elif item == O:
                ocount += 1
    if xcount > ocount:
        return O
    else:
        return X

def actions(board):
    possibilitys = set()
    for row_index in range(len(board)):
        for item_index in range(len(board[0])):
            if board[row_index][item_index] == EMPTY:
                possibilitys.add((row_index, item_index))
    return possibilitys

def result(board, action):
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result

def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    if winner(board) is not None or (not any(EMPTY in row for row in board) and winner(board) is None):
        return True
    else: 
        return False

def utility(board):
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        a, _ = min_value(result(board, action))
        if a > v:
            v = a
            move = action
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        a, _ = max_value(result(board, action))
        if a < v:
            v = a
            move = action
    return v, move

def minimax(board):
    if terminal(board):
        return None
    else:
        if player(board) == X:
            _, move = max_value(board)
            return move
            
        else:
            _, move = min_value(board)
            return move
