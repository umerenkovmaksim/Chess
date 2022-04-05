WHITE = 1
BLACK = 2


def main():
    # Создаём шахматную доску
    board = Board()

    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход черных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

        # Белые пешки
        self.field[1][0] = Pawn(1, 0, WHITE)
        self.field[1][1] = Pawn(1, 1, WHITE)
        self.field[1][2] = Pawn(1, 2, WHITE)
        self.field[1][3] = Pawn(1, 3, WHITE)
        self.field[1][4] = Pawn(1, 4, WHITE)
        self.field[1][5] = Pawn(1, 5, WHITE)
        self.field[1][6] = Pawn(1, 6, WHITE)
        self.field[1][7] = Pawn(1, 7, WHITE)

        # Чёрные пешки
        self.field[6][0] = Pawn(6, 0, BLACK)
        self.field[6][1] = Pawn(6, 1, BLACK)
        self.field[6][2] = Pawn(6, 2, BLACK)
        self.field[6][3] = Pawn(6, 3, BLACK)
        self.field[6][4] = Pawn(6, 4, BLACK)
        self.field[6][5] = Pawn(6, 5, BLACK)
        self.field[6][6] = Pawn(6, 6, BLACK)
        self.field[6][7] = Pawn(6, 7, BLACK)

        # Остальные белые фигуры
        self.field[0][0] = Rook(0, 0, WHITE)
        self.field[0][1] = Knight(0, 1, WHITE)
        self.field[0][2] = Bishop(0, 2, WHITE)
        self.field[0][3] = Queen(0, 3, WHITE)
        self.field[0][4] = King(0, 4, WHITE)
        self.field[0][5] = Bishop(0, 5, WHITE)
        self.field[0][6] = Knight(0, 6, WHITE)
        self.field[0][7] = Rook(0, 7, WHITE)

        # Остальные чёрные фигуры фигуры
        self.field[7][0] = Rook(7, 0, BLACK)
        self.field[7][1] = Knight(7, 1, BLACK)
        self.field[7][2] = Bishop(7, 2, BLACK)
        self.field[7][3] = Queen(7, 3, BLACK)
        self.field[7][4] = King(7, 4, BLACK)
        self.field[7][5] = Bishop(7, 5, BLACK)
        self.field[7][6] = Knight(7, 6, BLACK)
        self.field[7][7] = Rook(7, 7, BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        if self.cell(row, col) != f'{self.cell(row, col)[0]}N':
            if self.color == WHITE:
                if self.cell(row1, col1)[0] == 'w':
                    return False
                else:
                    self.field[row1][col1] = None
            elif self.color == BLACK:
                if self.cell(row1, col1)[0] == 'b':
                    return False
                else:
                    self.field[row1][col1] = None
        else:
            if self.color == WHITE:
                if row == row1:
                    for i in range(col + 1, col1 + 1):
                        if self.cell(row, i) != '  ':
                            if self.cell(row1, col1)[0] == 'w':
                                return False
                            else:
                                self.field[row1][col1] = None
                if col == col1:
                    for i in range(row + 1, row1 + 1):
                        if self.cell(i, col) != '  ':
                            if self.cell(row1, col1)[0] == 'w':
                                return False
                            else:
                                self.field[row1][col1] = None

            elif self.color == BLACK:
                if row == row1:
                    for i in range(col1 + 1, col + 1):
                        if self.cell(row, i) != '  ':
                            if self.cell(row1, col1)[0] == 'b':
                                return False
                            else:
                                self.field[row1][col1] = None
                if col == col1:
                    for i in range(row1 + 1, row + 1):
                        if self.cell(i, col) != '  ':
                            if self.cell(row1, col1)[0] == 'b':
                                return False
                            else:
                                self.field[row1][col1] = None
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] is None:
                    continue
                else:
                    if self.field[i][j].get_color() == color:
                        if self.field[i][j].can_move(row, col):
                            return True
        return False


class Pawn:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'P'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if self.col != col:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if self.row + direction == row:
            return True

        # ход на 2 клетки из начального положения
        if self.row == start_row and self.row + 2 * direction == row:
            return True

        return False


class Rook(Pawn):
    def char(self):
        return 'R'

    def can_move(self, row, col):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if self.row != row and self.col != col:
            return False

        return True


class Queen(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if abs(row - self.row) == abs(col - self.col) or not (self.row != row and self.col != col):
                return True
        else:
            return False

    def char(self):
        return 'Q'


class Knight(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if (abs(row - self.row) == 2 and abs(col - self.col) == 1) or \
                    (abs(row - self.row) == 1 and abs(col - self.col) == 2):
                return True
        else:
            return False

    def char(self):
        return 'N'


class Bishop(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if abs(row - self.row) == abs(col - self.col):
                return True
        else:
            return False

    def char(self):
        return 'B'


class King(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if abs(row - self.row) == 1 and abs(col - self.col) == 1:
                return True
        else:
            return False

    def char(self):
        return 'K'
