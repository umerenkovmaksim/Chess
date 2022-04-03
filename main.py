from solution import *

# Я амогус
WHITE = 1
BLACK = 2

row0 = 4
col0 = 5
queen = Queen(row0, col0, BLACK)

print('white' if queen.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(queen.char(), end='')
        elif queen.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
