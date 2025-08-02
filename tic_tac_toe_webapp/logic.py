import random

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, is_maximizing, ai_symbol, human_symbol):
    winner = check_winner(board)
    if winner == ai_symbol:
        return 1
    elif winner == human_symbol:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = ai_symbol
            score = minimax(board, False, ai_symbol, human_symbol)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_available_moves(board):
            board[i][j] = human_symbol
            score = minimax(board, True, ai_symbol, human_symbol)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def get_ai_move(board, ai_symbol, human_symbol, difficulty):
    available_moves = get_available_moves(board)

    if difficulty == 'easy':
        return random.choice(available_moves) if available_moves else None

    elif difficulty == 'medium':
        if random.random() < 0.25:
            return random.choice(available_moves) if available_moves else None

    # Hard mode (minimax)
    best_score = -float('inf')
    best_move = None
    for i, j in available_moves:
        board[i][j] = ai_symbol
        score = minimax(board, False, ai_symbol, human_symbol)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move
