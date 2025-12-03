import random

print("=== Welcome to Tic Tac Toe ===")
print("Select a game mode:\n1. Player vs Player\n2. Player vs Computer")
modeSelection = input('Enter 1 or 2: ')

def show_board(board, current_player):
    print("\n    A   B   C")
    print("  +---+---+---+")
    for i in range(1, 4):
        print(f"{i} | {board[i-1][0]} | {board[i-1][1]} | {board[i-1][2]} |")
        print("  +---+---+---+")
    print(f"\n{current_player}'s turn\n")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

board = [[" " for _ in range(3)] for _ in range(3)]
valid_positions = {
    'A1': (0, 0), 'A2': (1, 0), 'A3': (2, 0),
    'B1': (0, 1), 'B2': (1, 1), 'B3': (2, 1),
    'C1': (0, 2), 'C2': (1, 2), 'C3': (2, 2)
}
if modeSelection == '1':
    player1 = input('Enter Player 1 name (X): ')
    player2 = input('Enter Player 2 name (O): ')

    current_player = player1
    current_symbol = "X"

    while True:
        show_board(board, current_player)
        move = input("Enter position (A1–C3): ").upper()

        if move not in valid_positions:
            print("Invalid position! Try again.\n")
            continue

        x, y = valid_positions[move]
        if board[x][y] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        board[x][y] = current_symbol

        winner = check_winner(board)
        if winner:
            show_board(board, current_player)
            print(f"{current_player} wins!")
            break

        if all(cell != " " for r in board for cell in r):
            show_board(board, current_player)
            print("It's a draw!")
            break

        if current_player == player1:
            current_player = player2
            current_symbol = "O"
        else:
            current_player = player1
            current_symbol = "X"


elif modeSelection == '2':
    print('You will vs a Computer')
    player1 = input('Enter Player 1 name (X): ')
    computer = 'Computer'

    current_player = player1
    current_symbol = "X"

    while True:
        show_board(board, current_player)

        if current_player == player1:
            move = input("Enter your move (A1–C3): ").upper()
            if move not in valid_positions:
                print("Invalid move! Try again.")
                continue
            x, y = valid_positions[move]
            if board[x][y] != " ":
                print("That spot is taken! Try again.")
                continue
        else:
            move = random.choice([
                k for k, v in valid_positions.items()
                if board[v[0]][v[1]] == " "
            ])
            print(f"Computer chose {move}")
            x, y = valid_positions[move]

        board[x][y] = current_symbol

        winner = check_winner(board)
        if winner:
            show_board(board, current_player)
            if current_player == player1:
                print(f"{player1} wins!")
            else:
                print("Computer wins!")
            break

        if all(cell != " " for r in board for cell in r):
            show_board(board, current_player)
            print("It's a draw!")
            break

        if current_player == player1:
            current_player = computer
            current_symbol = "O"
        else:
            current_player = player1
            current_symbol = "X"

else:
    print("Invalid selection! Please restart the game.")

