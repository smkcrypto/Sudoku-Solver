def is_safe(board, row, col, num, rows, cols, boxes):
    # Check if `num` is not in the current row, column, or box
    box_index = (row // 3) * 3 + (col // 3)
    if num in rows[row] or num in cols[col] or num in boxes[box_index]:
        return False
    return True

def place_number(board, row, col, num, rows, cols, boxes):
    # Place the number and update the constraints
    board[row][col] = num
    rows[row].add(num)
    cols[col].add(num)
    boxes[(row // 3) * 3 + (col // 3)].add(num)

def remove_number(board, row, col, num, rows, cols, boxes):
    # Remove the number and update the constraints
    board[row][col] = 0
    rows[row].remove(num)
    cols[col].remove(num)
    boxes[(row // 3) * 3 + (col // 3)].remove(num)

def solve_sudoku(board):
    # Prepare constraints tracking
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Initialize constraints based on the board
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_safe(board, row, col, num, rows, cols, boxes):
                            place_number(board, row, col, num, rows, cols, boxes)
                            if backtrack():
                                return True
                            remove_number(board, row, col, num, rows, cols, boxes)
                    return False
        return True

    if backtrack():
        return True
    else:
        return False

def print_sudoku(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(num)
            else:
                print(str(num) + " ", end="")

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku
if solve_sudoku(sudoku_board):
    print_sudoku(sudoku_board)
else:
    print("No solution exists")
