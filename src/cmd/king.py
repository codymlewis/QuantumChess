# king.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
# Mod.: 24-FEB-2018
import piece
import functions
from functions import Direction
class King(piece.Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Ki' + str(idT)
        piece.Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = functions.splitMovement(movement)
        direction = moveArr[0]
        if(len(moveArr) == 1):
            if direction in [Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWNRIGHT, Direction.DOWNLEFT, Direction.UPRIGHT, Direction.UPLEFT]:
                return True
        return False
