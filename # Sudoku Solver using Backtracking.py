def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    box_x = col // 3
    box_y = row // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
board = []
for i in range(9):
    while True:
        row = input(f"Row {i+1}: ")
        if len(row) == 9 and row.isdigit():
            board.append([int(x) for x in row])
            break
        else:
            print("⚠️ Please enter exactly 9 digits (use 0 for empty cells).")

# ------------------------------
print("\nSudoku puzzle:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\n❌ This Sudoku cannot be solved.")
