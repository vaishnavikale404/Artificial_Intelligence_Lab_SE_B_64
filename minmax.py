import math

# Function to print the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

# Function to check winner or draw
def evaluate(board):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] != ' ':
            return +1 if board[state[0]] == 'X' else -1
    if ' ' not in board:
        return 0  # draw
    return None   # game not over

# Minimax function
def minimax(board, is_maximizing):
    score = evaluate(board)
    if score is not None:
        return score
    
    if is_maximizing:  # MAX = 'X'
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, False))
                board[i] = ' '
        return best
    else:  # MIN = 'O'
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, True))
                board[i] = ' '
        return best

# Find best move for AI (X)
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, False)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

# Main game loop
def play_game():
    board = [' '] * 9
    print("Welcome to Tic Tac Toe! You are O, Computer is X.\n")
    print_board(board)
    
    while True:
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move, try again.")
            continue
        board[move] = 'O'
        print_board(board)
        
        if evaluate(board) is not None:
            break
        
        # Computer move
        best_move = find_best_move(board)
        board[best_move] = 'X'
        print("Computer places X at position", best_move)
        print_board(board)
        
        if evaluate(board) is not None:
            break
    
    # Result
    score = evaluate(board)
    if score == +1:
        print("Computer Wins!")
    elif score == -1:
        print("You Win!")
    else:
        print("It's a Draw!")

# Run the game
if __name__ == "__main__":
    play_game()

