# pawn.py - QuantumChess
# Author: Cody Lewis
# Date: 23-FEB-2018
# Mod.: 23-FEB-2018
import piece
import functions
class Pawn(piece.Piece):
    def __init__(self,superposNum,frstSuperPos,col,idT):
        idT = 'P ' + str(idT)
        piece.Piece.__init__(self,superposNum,frstSuperPos,col,idT)
        self.firstMove = True

    def canMove(self,movement):
        moveArr = functions.splitMovement(movement)
        if(self.firstMove):
            moveNum = 2
            self.firstMove = False
        else:
            moveNum = 1
        if(len(moveArr) <= moveNum):
            if(self.colour == 'W'):
                direction = 'u'
            else:
                direction = 'd'
            for i in range(len(moveArr)):
                if(not moveArr[i] == direction):
                    return False
            return True
        return False

    def canAttack(self,movement):
        moveArr = functions.splitMovement(movement)
        if(self.colour == 'W'):
            dir1 = 'f'
            dir2 = 'q'
        else:
            dir1 = 'h'
            dir2 = 'g'
        if(len(moveArr) == 1 and (moveArr[0] == dir1 or moveArr[0] == dir2)):
            return True
        else:
            return False
