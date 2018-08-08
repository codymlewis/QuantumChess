# pawn.py - QuantumChess
# Author: Cody Lewis
# Date: 23-FEB-2018
# Mod.: 23-FEB-2018
import piece
import functions
from functions import Direction
class Pawn(piece.Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'P ' + str(idT)
        piece.Piece.__init__(self, superposNum, frstSuperPos, col, idT)
        self.firstMove = True

    def canMove(self, movement):
        moveArr = functions.splitMovement(movement)
        if(self.firstMove):
            moveNum = 2
            self.firstMove = False
        else:
            moveNum = 1
        if(len(moveArr) <= moveNum):
            if(self.colour == 'W'):
                direction = Direction.UP.value
            else:
                direction = Direction.DOWN.value
                print(direction)
            for i in range(len(moveArr)):
                if(not moveArr[i] == direction):
                    return False
            return True
        return False

    def canAttack(self, movement):
        moveArr = functions.splitMovement(movement)
        if(self.colour == 'W'):
            dir1 = Direction.UPLEFT.value
            dir2 = Direction.UPRIGHT.value
        else:
            dir1 = Direction.DOWNLEFT.value
            dir2 = Direction.DOWNRIGHT.value
        if(len(moveArr) == 1 and (moveArr[0] == dir1 or moveArr[0] == dir2)):
            return True
        else:
            return False
