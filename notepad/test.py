from random import randrange

def find_element_index(board, element):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == element:
                return (i, j)
    
    return None

def enter_move(board):
    value = input("Make your move: ")

    row, col = find_element_index(board, value)
    
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    free_spaces = []
    for row_index, row in enumerate(board):
        for col_index, element in enumerate(row):
            if element == 'O' or element == 'X':
                continue
            
            free_spaces.append((row_index, col_index))

    return free_spaces

def victory_for(board, sign):
    return (
        (board[0][0] == sign, board[0][1] == sign, board[0][2] == sign) or
        (board[1][0] == sign, board[1][1] == sign, board[1][2] == sign) or
        (board[2][0] == sign, board[2][1] == sign, board[2][2] == sign) or
        (board[0][0] == sign, board[1][0] == sign, board[2][0] == sign) or
        (board[0][1] == sign, board[1][1] == sign, board[2][1] == sign) or
        (board[0][2] == sign, board[1][2] == sign, board[2][2] == sign) or
        (board[0][0] == sign, board[1][1] == sign, board[2][2] == sign) or
        (board[2][0] == sign, board[1][1] == sign, board[0][2] == sign)
    )

def draw_move(board): 
    free_fields = make_list_of_free_fields(board)
    rand_number = randrange(len(free_fields))
    i, j = free_fields[rand_number]
    board[i][j] = 'X'

def display_board(board):
    top_line = '+-------+-------+-------+'
    empty_line = '|       |       |       |'
    numbered_line = '|   {}   |   {}   |   {}   |'

    for row in board:
        print(top_line)
        print(empty_line)
        print(numbered_line.format(row[0], row[1], row[2]))
        print(empty_line)
        
    print(top_line)

board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

moves = 0
while True:
    display_board(board)
    enter_move(board)
    moves += 1

    if moves > 4 and victory_for(board, 'O'):
        print("Human strong")
        break

    draw_move(board)
    moves += 1

    if moves > 5 and victory_for(board, 'X'):
        print("PC strong")
        break