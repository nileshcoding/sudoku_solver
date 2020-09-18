# Sudoku solver using Backttracking Algorithm
'''
    function empty_position takes the board(sudoku matrix) as empty and returns the first empty position.
    when there is no empty position, it returns None.
'''

def empty_position(board):
    for i in  range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

"""
Function valid_number takes board, number and position(row,column) in the sudoku board.
it return True if the value is not present alredy in row or colum or 3*3 box
else it return False
"""
def valid_number(board,num,position):
    row,col = position

    for i in range(len(board[0])):
         if board[row][i] == num and i != col:
             return False

    for j in range(len(board)):
        if board[j][col] == num and j != row:
            return False

    box_i = row//3
    box_j = col//3

    for i in range(box_i*3, box_i*3+3):
        for j in range(box_j*3,box_j*3+3):
            if board[i][j] == num and i != row and j != col:
                return False

    return True


"""
main recursive function to solve the sudoku.
returns True if board is solved else False
only base case here is when there is no more empty position.
if a value(1-9) is valid for a position, it updates the position with that value and recursively call the function
if sudoku can't be solved it resets the position and backtracks. 

"""
def solve(board):
    pos = empty_position(board) #check for the empty position

    # if there is no empty position return true i.e board is solved
    if pos == None:
        return True
    
    # iterate for values ranging in 1 to 9
    for value in range(1,10):
        if valid_number(board,value,pos): #if a value is valid update the position
            row,col = pos
            board[row][col] = value

            if solve(board): #recurse
                return True
            else:
                board[row][col] = 0 #reset the position

    return False

board = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

solve(board)
