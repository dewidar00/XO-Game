import os
import time

# ╔════════════════════════════════════════════════════════════════╗
# ║                    XO GAME - TIC TAC TOE                       ║
# ║                   with Minimax AI Algorithm                    ║
# ╚════════════════════════════════════════════════════════════════╝

# ============== GAME DATA ==============
# The board is represented as a list of 9 cells
# Positions are numbered 1-9:
#   1 | 2 | 3
#   ---------
#   4 | 5 | 6
#   ---------
#   7 | 8 | 9

def create_board():
    """Create an empty game board."""
    return [' ' for _ in range(9)]

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the game header."""
    print("\n")
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║                                           ║")
    print("  ║        ██╗  ██╗ ██████╗                   ║")
    print("  ║        ╚██╗██╔╝██╔═══██╗                  ║")
    print("  ║         ╚███╔╝ ██║   ██║                  ║")
    print("  ║         ██╔██╗ ██║   ██║                  ║")
    print("  ║        ██╔╝ ██╗╚██████╔╝                  ║")
    print("  ║        ╚═╝  ╚═╝ ╚═════╝                   ║")
    print("  ║                                           ║")
    print("  ║           TIC  TAC  TOE                   ║")
    print("  ║                                           ║")
    print("  ╚═══════════════════════════════════════════╝")
    print("\n")

def print_welcome_message():
    """Print welcome message."""
    print("  ┌───────────────────────────────────────────┐")
    print("  │                                           │")
    print("  │   Hello! Welcome to XO Game!              │")
    print("  │                                           │")
    print("  │   Battle against an unbeatable AI        │")
    print("  │   powered by the Minimax algorithm!      │")
    print("  │                                           │")
    print("  └───────────────────────────────────────────┘")
    print("\n")

def print_board(board):
    """Print the game board with a nice UI."""
    print()
    print("        ┌───────────────────────┐")
    print("        │     GAME  BOARD       │")
    print("        └───────────────────────┘")
    print()
    
    # Helper to display cell (show position number if empty)
    def cell(index):
        if board[index] == ' ':
            return f' {index + 1} '  # Show position number (1-9)
        else:
            return f' {board[index]} '
    
    print("             ┌───┬───┬───┐")
    print(f"             │{cell(0)}│{cell(1)}│{cell(2)}│")
    print("             ├───┼───┼───┤")
    print(f"             │{cell(3)}│{cell(4)}│{cell(5)}│")
    print("             ├───┼───┼───┤")
    print(f"             │{cell(6)}│{cell(7)}│{cell(8)}│")
    print("             └───┴───┴───┘")
    print()

def print_board_guide():
    """Print a guide showing position numbers."""
    print("        ┌───────────────────────┐")
    print("        │   Position Numbers:   │")
    print("        │                       │")
    print("        │      1 │ 2 │ 3        │")
    print("        │     ───┼───┼───       │")
    print("        │      4 │ 5 │ 6        │")
    print("        │     ───┼───┼───       │")
    print("        │      7 │ 8 │ 9        │")
    print("        │                       │")
    print("        └───────────────────────┘")
    print()

# ============== WIN DETECTION ==============
# All possible winning combinations (indices)
WINNING_COMBINATIONS = [
    [0, 1, 2],  # Top row
    [3, 4, 5],  # Middle row
    [6, 7, 8],  # Bottom row
    [0, 3, 6],  # Left column
    [1, 4, 7],  # Middle column
    [2, 5, 8],  # Right column
    [0, 4, 8],  # Diagonal top-left to bottom-right
    [2, 4, 6],  # Diagonal top-right to bottom-left
]

def check_winner(board, symbol):
    """Check if the given symbol has won."""
    for combo in WINNING_COMBINATIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def check_draw(board):
    """Check if the game is a draw (no empty cells and no winner)."""
    return ' ' not in board

def is_game_over(board):
    """Check if the game has ended (win or draw)."""
    return check_winner(board, 'X') or check_winner(board, 'O') or check_draw(board)

def get_game_result(board, player_symbol, ai_symbol):
    """Get the result of the game."""
    if check_winner(board, player_symbol):
        return 'player_wins'
    elif check_winner(board, ai_symbol):
        return 'ai_wins'
    elif check_draw(board):
        return 'draw'
    return None

# ============== MINIMAX AI ALGORITHM ==============
# The Minimax algorithm explores all possible game states
# and chooses the optimal move assuming perfect play.
#
# How it works:
# 1. AI is the "maximizer" - wants highest score
# 2. Player is the "minimizer" - wants lowest score  
# 3. Scores: AI win = +10, Player win = -10, Draw = 0
# 4. Recursively evaluate all possible moves
# 5. Choose the move with the best score for AI

def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    """
    Minimax algorithm implementation.
    
    Args:
        board: Current game board
        depth: How deep in the game tree we are
        is_maximizing: True if it's AI's turn (maximizing)
        ai_symbol: The AI's symbol (X or O)
        player_symbol: The player's symbol
    
    Returns:
        The best score for the current board state
    """
    # Base cases - check for terminal states
    if check_winner(board, ai_symbol):
        return 10 - depth  # AI wins (prefer faster wins)
    if check_winner(board, player_symbol):
        return depth - 10  # Player wins (prefer slower losses)
    if check_draw(board):
        return 0  # Draw
    
    available_moves = get_available_moves(board)
    
    if is_maximizing:
        # AI's turn - maximize the score
        best_score = float('-inf')
        for move in available_moves:
            # Try this move
            board[move] = ai_symbol
            # Recursively evaluate
            score = minimax(board, depth + 1, False, ai_symbol, player_symbol)
            # Undo the move
            board[move] = ' '
            # Keep the best score
            best_score = max(score, best_score)
        return best_score
    else:
        # Player's turn - minimize the score
        best_score = float('inf')
        for move in available_moves:
            # Try this move
            board[move] = player_symbol
            # Recursively evaluate
            score = minimax(board, depth + 1, True, ai_symbol, player_symbol)
            # Undo the move
            board[move] = ' '
            # Keep the best score (lowest for minimizer)
            best_score = min(score, best_score)
        return best_score

def get_ai_move(board, ai_symbol, player_symbol):
    """
    Get the best move for the AI using Minimax.
    
    Returns:
        The best position (1-9) for the AI to play
    """
    best_score = float('-inf')
    best_move = None
    
    available_moves = get_available_moves(board)
    
    for move in available_moves:
        # Try this move
        board[move] = ai_symbol
        # Evaluate using minimax
        score = minimax(board, 0, False, ai_symbol, player_symbol)
        # Undo the move
        board[move] = ' '
        
        # Keep track of the best move
        if score > best_score:
            best_score = score
            best_move = move
    
    # Return position (1-9 format)
    return best_move + 1

def print_result(result):
    """Print the game result with a nice UI."""
    print()
    if result == 'player_wins':
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║                                           ║")
        print("  ║      CONGRATULATIONS! YOU WIN!            ║")
        print("  ║                                           ║")
        print("  ╚═══════════════════════════════════════════╝")
    elif result == 'ai_wins':
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║                                           ║")
        print("  ║          GAME OVER - AI WINS!             ║")
        print("  ║        Better luck next time!             ║")
        print("  ║                                           ║")
        print("  ╚═══════════════════════════════════════════╝")
    elif result == 'draw':
        print("  ╔═══════════════════════════════════════════╗")
        print("  ║                                           ║")
        print("  ║           IT'S A DRAW!                    ║")
        print("  ║       Great game! Well played!            ║")
        print("  ║                                           ║")
        print("  ╚═══════════════════════════════════════════╝")
    print()

# ============== MOVE HANDLING ==============

def get_available_moves(board):
    """Return list of available positions (0-8)."""
    return [i for i in range(9) if board[i] == ' ']

def is_valid_move(board, position):
    """Check if a move is valid (position 1-9, cell is empty)."""
    if position < 1 or position > 9:
        return False
    return board[position - 1] == ' '

def make_move(board, position, symbol):
    """Place a symbol on the board at the given position (1-9)."""
    board[position - 1] = symbol

def get_player_move(board, player_symbol):
    """Get and validate player's move input."""
    while True:
        print(f"        Your turn ({player_symbol})")
        print()
        try:
            move = input("  >>> Enter position (1-9): ").strip()
            
            if not move:
                print("  [!] Please enter a number.\n")
                continue
                
            position = int(move)
            
            if position < 1 or position > 9:
                print("  [!] Please enter a number between 1 and 9.\n")
                continue
            
            if not is_valid_move(board, position):
                print("  [!] That position is already taken! Choose another.\n")
                continue
            
            return position
            
        except ValueError:
            print("  [!] Invalid input! Please enter a number.\n")

def ai_thinking_animation():
    """Show a thinking animation for the AI."""
    print("        AI is thinking", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    time.sleep(0.3)
    print()

def play_again():
    """Ask if the player wants to play again."""
    print()
    while True:
        choice = input("  >>> Play again? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("  [!] Please enter 'y' or 'n'.\n")

def choose_player_symbol():
    """Let the player choose X or O."""
    print("  ┌───────────────────────────────────────────┐")
    print("  │         Choose your symbol:               │")
    print("  │                                           │")
    print("  │           [1]  X                          │")
    print("  │           [2]  O                          │")
    print("  │                                           │")
    print("  └───────────────────────────────────────────┘")
    print()
    
    while True:
        choice = input("  >>> Enter your choice (1 or 2): ").strip()
        
        if choice == '1':
            print("\n  [OK] You chose X! You will go first.\n")
            return 'X', 'O'
        elif choice == '2':
            print("\n  [OK] You chose O! AI (X) will go first.\n")
            return 'O', 'X'
        else:
            print("  [!] Invalid choice! Please enter 1 or 2.\n")

def display_game_state(board, player_symbol, ai_symbol, message=None):
    """Helper to display the current game state."""
    clear_screen()
    print_header()
    print(f"        You: {player_symbol}  │  AI: {ai_symbol}")
    print()
    print_board(board)
    if message:
        print(f"  {message}")
        print()

def game_loop(player_symbol, ai_symbol):
    """Run a single game."""
    board = create_board()
    
    # Determine who goes first (X always goes first)
    current_turn = 'X'
    
    display_game_state(board, player_symbol, ai_symbol)
    
    # If AI is X, AI goes first
    if ai_symbol == 'X':
        ai_thinking_animation()
        ai_position = get_ai_move(board, ai_symbol, player_symbol)
        make_move(board, ai_position, ai_symbol)
        display_game_state(board, player_symbol, ai_symbol, 
                          f"AI placed {ai_symbol} at position {ai_position}")
        current_turn = 'O'
    
    # Main game loop
    while not is_game_over(board):
        if current_turn == player_symbol:
            # Player's turn
            position = get_player_move(board, player_symbol)
            make_move(board, position, player_symbol)
            display_game_state(board, player_symbol, ai_symbol,
                              f"You placed {player_symbol} at position {position}")
            
            # Check for game end after player's move
            result = get_game_result(board, player_symbol, ai_symbol)
            if result:
                print_result(result)
                return
            
            current_turn = ai_symbol
        else:
            # AI's turn
            ai_thinking_animation()
            ai_position = get_ai_move(board, ai_symbol, player_symbol)
            make_move(board, ai_position, ai_symbol)
            display_game_state(board, player_symbol, ai_symbol,
                              f"AI placed {ai_symbol} at position {ai_position}")
            
            # Check for game end after AI's move
            result = get_game_result(board, player_symbol, ai_symbol)
            if result:
                print_result(result)
                return
            
            current_turn = player_symbol

def print_goodbye():
    """Print goodbye message."""
    print()
    print("  ╔═══════════════════════════════════════════╗")
    print("  ║                                           ║")
    print("  ║     Thanks for playing XO Game!           ║")
    print("  ║            See you soon!                  ║")
    print("  ║                                           ║")
    print("  ╚═══════════════════════════════════════════╝")
    print()

def main():
    """Main function - Entry point."""
    clear_screen()
    print_header()
    print_welcome_message()
    
    input("  Press ENTER to start...")
    
    while True:
        clear_screen()
        print_header()
        
        player_symbol, ai_symbol = choose_player_symbol()
        
        # Play the game
        game_loop(player_symbol, ai_symbol)
        
        # Ask to play again
        if not play_again():
            break
    
    clear_screen()
    print_header()
    print_goodbye()

if __name__ == "__main__":
    main()



