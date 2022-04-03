from Pawn import Pawn
from function import *


class Queen(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if abs(row - self.row) == abs(col - self.col) or not(self.row != row and self.col != col):
                return True
        else:
            return False

    def char(self):
        return 'Q'
