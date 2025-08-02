from flask import Flask, render_template, request, jsonify
from logic import check_winner, is_board_full, get_ai_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board = data['board']
    player_symbol = data['player']
    difficulty = data.get('difficulty', 'hard')

    ai_symbol = 'O' if player_symbol == 'X' else 'X'
    row, col = data['move']
    board[row][col] = player_symbol

    winner = check_winner(board)
    if winner:
        message = "Player wins!" if winner == player_symbol else "Computer wins!"
        return jsonify({'board': board, 'winner': winner, 'message': message})

    if is_board_full(board):
        return jsonify({'board': board, 'winner': 'Draw', 'message': "It's a Draw!"})

    ai_move = get_ai_move(board, ai_symbol, player_symbol, difficulty)
    if ai_move:
        ai_row, ai_col = ai_move
        board[ai_row][ai_col] = ai_symbol

    winner = check_winner(board)
    if winner:
        message = "Player wins!" if winner == player_symbol else "Computer wins!"
        return jsonify({'board': board, 'winner': winner, 'message': message})

    if is_board_full(board):
        return jsonify({'board': board, 'winner': 'Draw', 'message': "It's a Draw!"})

    return jsonify({'board': board, 'winner': None})

if __name__ == '__main__':
    app.run(debug=True)