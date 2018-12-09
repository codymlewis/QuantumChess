# knight.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
# Mod.: 24-FEB-2018
import piece
import functions
from functions import Direction
class Knight(piece.Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Kn' + str(idT)
        piece.Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = functions.splitMovement(movement)
        if(len(moveArr) == 2): # need the L movement
            if(self.__isL(moveArr)):
                return True
        return False

    def __isL(self, moveArr):
        if moveArr[0] == Direction.UP.value:
            if moveArr[1] == Direction.UPLEFT.value or moveArr[1] == Direction.UPRIGHT.value:
                return True
        elif moveArr[0] == Direction.DOWN.value:
            if moveArr[1] == Direction.DOWNLEFT.value or moveArr[1] == Direction.DOWNRIGHT.value:
                return True
        elif moveArr[0] == Direction.LEFT.value:
            if moveArr[1] == Direction.UPLEFT.value or moveArr[1] == Direction.DOWNLEFT.value:
                return True
        elif moveArr[0] == Direction.RIGHT.value:
            if moveArr[1] == Direction.UPRIGHT.value or moveArr[1] == Direction.DOWNRIGHT.value:
                return True
        else:
            return False
