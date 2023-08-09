def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 8)

def handle_move(board, player):
    print(f"Player {player}'s turn.")
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))
        
        #handle inputs
        if (row or col)>2 or (row or col)<0:
            print("Invalid number. please enter valid number.")
            
        elif board[row][col] == "":
            board[row][col] = player
            break
        else:
            print("Invalid move. Try again.")

def check_win(board, player):
    # Check rows
    for row in board:
        if all(square == player for square in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True

def play_game():
    board = [[""] * 3 for _ in range(3)]
    current_player = "X"

    while True:
        # Print the current state of the game board
        print_board(board)

        # Handle the current player's move
        handle_move(board, current_player)

        # Check if the current player has won
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if there is a tie
        if check_tie(board):
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
