from Queen import *
from Board import *

board = Board()

board.field = [([None] * 8) for i in range(8)]
board.field[0][0] = Rook(0, 0, WHITE)
board.field[1][2] = Bishop(1, 2, WHITE)
coords = ((0, 0), (1, 2))

print('White:')
for row in range(7, -1, -1):
    for col in range(8):
        if (row, col) in coords:
            print('W', end='')
        elif board.is_under_attack(row, col, WHITE):
            print('x', end='')
        else:
            print('-', end='')
    print()
