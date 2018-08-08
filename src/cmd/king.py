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
            if direction in [Direction.DOWN.value, Direction.UP.value, Direction.RIGHT.value, Direction.LEFT.value, Direction.DOWNRIGHT.value, Direction.DOWNLEFT.value, Direction.UPRIGHT.value, Direction.UPLEFT.value]:
                return True
        return False
