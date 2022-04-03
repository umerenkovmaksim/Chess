from Pawn import Pawn
from function import *


class Bishop(Pawn):
    def can_move(self, row, col):
        if correct_coords(row, col):
            if abs(row - self.row) == abs(col - self.col):
                return True
        else:
            return False

    def char(self):
        return 'B'
