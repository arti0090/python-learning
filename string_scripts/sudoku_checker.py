# sudoku_data = []
# while len(sudoku_data) != 9:
#     try:
#         row = input("Put the data for " + str(len(sudoku_data) + 1) + " row: ")
#         row = row.strip()

#         row_number = []
#         for char in row:
#             if not char.isdigit():
#                 raise ValueError
#             row_number.append(int(char))
        
#         sudoku_data.append(row_number)
#     except ValueError:
#         print("Row has incorrect value. Input row one more time.")

sudoku_data = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 2, 7], 
    [8, 7, 6, 1, 9, 2, 5, 4, 3], 
    [3, 8, 7, 4, 5, 9, 2, 1, 6], 
    [6, 1, 2, 3, 8, 7, 4, 9, 5], 
    [5, 4, 9, 2, 1, 6, 7, 3, 8], 
    [7, 6, 3, 5, 2, 4, 1, 8, 9], 
    [9, 2, 8, 6, 7, 1, 3, 5, 4], 
    [1, 5, 4, 9, 3, 8, 6, 7, 2]
]

sudoku_fake = [
    [1, 9, 5, 7, 4, 3, 8, 6, 2],
    [4, 3, 1, 8, 6, 5, 9, 2, 7],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 2, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [2, 5, 4, 9, 3, 8, 6, 7, 1]
]

def check_rows(sudoku_data):
    for row in sudoku_data:
        if len(row) != len(set(row)):
            return False
        
    return True

def check_columns(sudoku_data):
    column = []
    for row_num in range(len(sudoku_data)):
        for col_num in range(len(sudoku_data[row_num])):
            column.append(sudoku_data[row_num][col_num])
        
        if len(column) != len(set(column)):
            return False
        column = []

    return True

def check_squares(sudoku_data):
    return check_square(sudoku_data, 0, 0) \
        and check_square(sudoku_data, 3, 0) \
        and check_square(sudoku_data, 6, 0) \
        and check_square(sudoku_data, 0, 3) \
        and check_square(sudoku_data, 3, 3) \
        and check_square(sudoku_data, 6, 3) \
        and check_square(sudoku_data, 0, 6) \
        and check_square(sudoku_data, 3, 6) \
        and check_square(sudoku_data, 6, 6)

def check_square(sudoku_data, start_row, start_col):
    square = []

    for row_num in range(start_row, start_row + 3):
        for col_num in range(start_col, start_col + 3):
            square.append(sudoku_data[row_num][col_num])

    return len(square) == len(set(square))

def check_sudoku(sudoku_data):
    if check_rows(sudoku_data) and \
        check_columns(sudoku_data) and \
        check_squares(sudoku_data):
        print("Yes")
    else:
        print("No")

check_sudoku(sudoku_data)
check_sudoku(sudoku_fake)