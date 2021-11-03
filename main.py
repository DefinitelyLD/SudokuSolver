from random import sample
base  = 3
side  = base*base
rows  =[]
cols=[]

# pattern for a baseline valid solution
def pattern(r,c):
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns
def shuffle(s): return sample(s,len(s))
rBase = range(base)

for i in shuffle(rBase):
    for j in shuffle(rBase):
        rows.append(i * base + j)

for i in shuffle(rBase):
    for j in shuffle(rBase):
        cols.append(i * base + j)

nums  = shuffle(range(1,10))

# Filling board
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

#Removing numbers from board
total_numbers = side*side
empties = total_numbers * 3//4
for p in sample(range(total_numbers),empties):
    board[p//side][p%side] = 0

def print_board(_board):
    for i in range(len(_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(_board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(_board[i][j])
            else:
                print(str(_board[i][j]) + " ", end="")

def find_empty_square(_board):
    for i in range (len(_board)):
        for j in range (len(_board[0])):
            if _board[i][j] == 0:
                return (i, j) #coords of empty square

    return None

def is_number_valid(_board, number, position):
    #Row check
    for i in range(len(_board[0])):
        if _board[position[0]][i] == number and position[1] != i:
            return False

    #Column check
    for i in range(len(_board)):
        if _board[i][position[1]] == number and position[0] != i:
            return False

    #Check 3x3 square
    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if _board[i][j] == number and (i,j) != position:
                return False

    return True

def solve(_board):
    empty = find_empty_square(_board)
    if not empty:
        return True #Solution found
    else:
        row, col = empty

    for i in range(1,10):
        if is_number_valid(_board, i, (row, col)):
            _board[row][col] = i

            if solve(_board):
                return True

            _board[row][col] = 0

    return False

print_board(board)
solve(board)
print("=======================")
print("Solving")
print("=======================")
print_board(board)

