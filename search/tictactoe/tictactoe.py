"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count, o_count = 0, 0
    
    for row in board:
        for cell in row:
            if cell == 'X': 
                x_count += 1
            if cell == 'O': 
                o_count += 1
            
    if x_count > o_count: 
        return 'O'
    
    return 'X'
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for r in range(3):
        for c in range(3):
            if not board[r][c]: 
                possible_actions.add((r, c))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise ValueError("Invalid action")

    if action[0] not in list(range(3)) or action[1] not in list(range(3)):
        raise ValueError("Index is out of range")
    
    if board[action[0]][action[1]]: 
        raise ValueError("Not an empty cell")

    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check horizontal wins
    if (['X', 'X', 'X'] in board): 
        return 'X'
    if (['O', 'O', 'O'] in board): 
        return 'O'
    
    # Check vertical wins
    for c in range(3):
        vertical = []
        for r in range(3):
            vertical.append(board[r][c])
        if vertical == ['X', 'X', 'X']:
            return 'X'
        if vertical == ['O', 'O', 'O']:
            return 'O'
        
    # Check for diagonal wins
    diagonal = [board[0][0], board[1][1], board[2][2]]
    if diagonal == ['X', 'X', 'X']:
        return 'X'
    if diagonal == ['O', 'O', 'O']:
        return 'O'
    
    diagonal = [board[0][2], board[1][1], board[2][0]]
    if diagonal == ['X', 'X', 'X']:
        return 'X'
    if diagonal == ['O', 'O', 'O']:
        return 'O'
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or all(cell != EMPTY for row in board for cell in row):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    point = winner(board)
    if not point: 
        return 0
    elif point == 'X':
        return 1
    else:
        return -1 # O wins the game


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    
    if terminal(board):
        return None
    
    def get_max(board):
        if terminal(board):
            return utility(board)
        max_value = float('-inf')
        for action in actions(board):
            max_value = max(max_value, get_min(result(board, action)))
        return max_value
        
    def get_min(board):
        if terminal(board):
            return utility(board)
        min_value = float('inf')
        for action in actions(board):
            min_value = min(min_value, get_max(result(board, action)))
        return min_value
    
    best_action = None
    if turn == 'X':                       # maximise
        best_score = float("-inf")
        for a in actions(board):
            score = get_min(result(board, a))
            if score > best_score:
                best_score, best_action = score, a
    else:                                 # minimise
        best_score = float("inf")
        for a in actions(board):
            score = get_max(result(board, a))
            if score < best_score:
                best_score, best_action = score, a

    return best_action