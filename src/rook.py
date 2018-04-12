# rook.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
# Mod.: 24-FEB-2018
import piece
import functions
class Rook(piece.Piece):
    def __init__(self,superposNum,frstSuperPos,col,idT):
        idT = 'R ' + str(idT)
        piece.Piece.__init__(self,superposNum,frstSuperPos,col,idT)

    def canMove(self,movement):
        moveArr = functions.splitMovement(movement)
        direction = moveArr[0]
        if(direction == 'u' or direction == 'r' or direction == 'l' or direction == 'd'):
            for i in range(1,len(moveArr)):
                if(direction != moveArr[i]):
                    return False
            return True
        return False
