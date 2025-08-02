# Tic-Tac-Toe Game with AI using Minimax Algorithm
import math

# Step 2: Create 3x3 board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n  0   1   2")
    for idx, row in enumerate(board):
        print(idx, ' | '.join(row))
        if idx < 2:
            print("  ---------")

# Step 3: Player move
def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers between 0 and 2.")

# Step 4: AI move using Minimax
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Minimax algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Step 5: Check for winner or draw
def check_winner(board):
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        # columns
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Step 6: Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player turn
        player_move(board)
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"🏆 Player ({winner}) wins!")
            break
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

        # AI turn
        print("AI is making a move...")
        ai_move(board)
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"🏆 Player ({winner}) wins!")
            break
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

if __name__ == "__main__":
    play_game()
