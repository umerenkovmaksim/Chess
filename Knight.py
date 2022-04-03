from Pawn import Pawn
from function import *


class Knight(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if (abs(row - self.row) == 2 and abs(col - self.col) == 1) or \
                    (abs(row - self.row) == 1 and abs(col - self.col) == 2):
                return True
            else:
                return False
        else:
            return False

    def char(self):
        return 'N'
