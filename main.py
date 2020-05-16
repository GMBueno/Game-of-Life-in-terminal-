import time
import random

try:
    h = int(input('how many rows? \t (5-200, default is 10)'))
    if h < 5 or h > 200:
        h = 10
except:
    h = 10

try:
    w = int(input('how many columns? \t (5-500, default is 40)'))
    if w < 5 or w > 500:
        w = 40
except:
    w = 40

try:
    bps = int(input('boards per second? \t (1-50, default is 1)'))
    if bps < 1 or bps > 50:
        bps = 1
except:
    bps = 1

'''
we add a 'mask' to ease count of neighbors on func 'neighbors()'.
This mask is a row and a col of dead cells before and after the board that
do not influence the logic (count of neighbors will be the same).
'''

def test_board():
    '''
    Just for testing. 1 is alive. 0 is dead.
    '''
    h, w  = 10, 40
    board = {}
    for row in range(h+2):
        for col in range(w+2):
            board[row, col] = 0

    ''' shapes/patterns '''

    # (oscillator) blinker
    board[3, 2] = 1
    board[3, 3] = 1
    board[3, 4] = 1

    # (oscillator) toad
    board[2,20] = 1
    board[2,21] = 1
    board[2,22] = 1
    board[3,19] = 1
    board[3,20] = 1
    board[3,21] = 1

    # (spaceship) glider
    board[2,10] = 1
    board[3,11] = 1
    board[4,11] = 1
    board[4,10] = 1
    board[4,9] = 1

    # (still life) bee-hive
    board[7,5] = 1
    board[7,6] = 1
    board[8,4] = 1
    board[8,7] = 1
    board[9,5] = 1
    board[9,6] = 1

    return board

def random_board():
    '''1 is alive. 0 is dead'''
    board = {}
    for row in range(h+2):
        for col in range(w+2):
            board[row, col] = 0
    for row in range(1, h+1):
        for col in range(1, w+1):
            board[row, col] = random.randint(0, 1)
    return board

def strfy(board):
    # we don't print the mask (first and last rows and cols)
    for row in range(1, h+1):
        text = ''
        for col in range(1, w+1):
            if board[row,col] == 1:
                text += '▣'
            elif board[row,col] == 0:
                # text += '▢'
                text += ' '
            else:
                text += '?'
        print(text)

def next_state(board):
    new_board = board.copy()
    # we never iterate/change cells of the mask (first and last rows and cols)
    for row in range(1, h+1):
        for col in range(1, w+1):
            cell = board[row, col]
            nei = neighbors(row, col, board)
            if nei == 3:
                new_board[row, col] = 1
            elif nei == 2:
                pass
            else:
                new_board[row, col] = 0
    return new_board

def neighbors(row, col, board):
    # pretty simple to count. Once we have a mask, we don't need to test edges
    count = 0
    # up, right, down, left
    if board[row-1, col] == 1: # up
        count += 1
    if board[row, col+1] == 1: # right
        count += 1
    if board[row+1, col] == 1: # down
        count += 1
    if board[row, col-1] == 1: # left
        count += 1
    # diagonals
    if board[row-1, col+1] == 1: # up right
        count += 1
    if board[row+1, col+1] == 1: # down right
        count += 1
    if board[row+1, col-1] == 1: # down left
        count += 1
    if board[row-1, col-1] == 1: # up left
        count += 1
    return count

# board = test_board()
board = random_board()
while True:
    print('\n'*h)
    strfy(board)
    board = next_state(board)
    time.sleep(1.0/bps)
