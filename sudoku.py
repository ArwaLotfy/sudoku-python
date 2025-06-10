import random

# Initialize the matrix and backUp variables
matrix = []
backUp = []

def file_open(filename):
    global matrix, backUp
    matrix = []
    backUp = []
    try:
        file_var = open(filename, 'r')
        for i in range(9):
            line = file_var.readline().strip('\n')
            L = line.split(' ')
            if len(L) != 9:
                print(f"Invalid line length: {line}")
                return False
            try:
                LInt = [int(i) for i in L]
                LInt2 = [int(i) for i in L]
                matrix.append(LInt)
                backUp.append(LInt2)
            except ValueError:
                print(f"Skipping invalid line: {line}")
                return False
        file_var.close()
        return True
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False

def save_game(filename, board):
    try:
        file_var = open(filename, 'w')
        for row in board:
            line = ' '.join([str(i) for i in row])  # Convert each element to a string using list comprehension
            file_var.write(line + '\n')
        file_var.close()
    except IOError:
        print(f"Error saving the game to {filename}.")

def print_sudoku(board):
    for r in range(9):
        if r % 3 == 0:
            if r == 0:
                print("╔═══════╦═══════╦═══════╗")
            else:
                print("╠═══════╬═══════╬═══════╣")
        row_str = ""
        for c in range(9):
            if c % 3 == 0:
                row_str += "║ "
            row_str += str(board[r][c]) if board[r][c] != 0 else " "
            row_str += " "
        row_str += "║"
        print(row_str)
    print("╚═══════╩═══════╩═══════╝")

def is_position_reserved(board, r, c):
    return board[r - 1][c - 1] != 0  # Check if the position is non-zero (reserved)

def is_number_valid(n):
    return 1 <= n <= 9  # Check if number is in range 1 to 9

def input_position():
    while True:
        try:
            rr = input("Enter Row Number (1 to 9) or type 'esc' to quit: ")
            if rr.lower() == 'esc':
                return 'esc', 'esc'
            rr = int(rr)
            cc = int(input("Enter Column Number (1 to 9): "))
            if 1 <= rr <= 9 and 1 <= cc <= 9:
                return rr, cc
            else:
                print("Row and column must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

def input_value():
    while True:
        try:
            vv = int(input("Enter Value (1 to 9): "))
            if is_number_valid(vv):
                return vv
            else:
                print("Value must be between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def is_valid_move(board, row, col, num):
    # Check if the number is not in the current row
    if num in board[row]:
        return False
    # Check if the number is not in the current column
    if num in [board[r][col] for r in range(9)]:
        return False
    # Check if the number is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def fill_random_cells(board):
    empty_cells = random.randint(40, 50)
    filled_cells = 50 - empty_cells
    for _ in range(filled_cells):
        while True:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            if board[row][col] == 0 and is_valid_move(board, row, col, num):
                board[row][col] = num
                break

def play_sudoku(board, reserved_board, player_name):
    while True:
        print_sudoku(board)
        print("\nEnter your move (or type 'esc' to quit):")
        
        rr, cc = input_position()
        if rr == 'esc' or cc == 'esc':
            print("ESC key pressed. What would you like to do?")
            print("1. Pause and save the game")
            print("2. Exit the game")
            print("3. Continue playing")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                save_game(f"{player_name}.txt", board)
                print("Game saved. Exiting the game. Goodbye!")
                break
            elif choice == '2':
                print("Exiting the game. Goodbye!")
                break
            elif choice == '3':
                continue

        if is_position_reserved(reserved_board, rr, cc):
            print("Position is reserved. Choose another position.")
            continue

        vv = input_value()

        if is_valid_move(board, rr - 1, cc - 1, vv):
            board[rr - 1][cc - 1] = vv
            print("Value updated successfully!")
            if not any(0 in row for row in board):
                print("Congratulations! You solved the Sudoku puzzle.")
                break
        else:
            print("Invalid move. The number already exists in the row, column, or 3x3 subgrid.")

def main():
    print("Welcome to Sudoku!")
    player_name = input("Please enter your name: ")
    filename = f"{player_name}.txt"

    file_exists = False
    file_non_empty = False

    try:
        file_var = open(filename, 'r')
        file_exists = True
        if file_var.read().strip():
            file_non_empty = True
        file_var.close()
    except FileNotFoundError:
        pass

    if file_exists and file_non_empty:
        choice = input("A saved game was found. Do you want to continue the previous game? (yes/no): ").lower()
        if choice == 'yes':
            if not file_open(filename):
                print("Error reading the saved game file. Starting a new game.")
            else:
                # Initialize the board variable with the matrix data
                board = matrix
                reserved_board = [row[:] for row in board]  # Copy of the original board to track reserved cells
                play_sudoku(board, reserved_board, player_name)
                return
        else:
            print("Starting a new game.")
            # Initialize the board variable with the matrix data
            if not file_open('sudukoo.txt'):
                print("Error reading the Sudoku file. Please check the file content.")
                return
            board = matrix
            reserved_board = [row[:] for row in board]  # Copy of the original board to track reserved cells
            fill_random_cells(board)  # Fill the board with random values
            play_sudoku(board, reserved_board, player_name)
    else:
        print("Starting a new game.")
        # Initialize the board variable with the matrix data
        if not file_open('sudukoo.txt'):
            print("Error reading the Sudoku file. Please check the file content.")
            return
        board = matrix
        reserved_board = [row[:] for row in board]  # Copy of the original board to track reserved cells
        fill_random_cells(board)  # Fill the board with random values
        play_sudoku(board, reserved_board, player_name)

if __name__ == "__main__":
    main()
