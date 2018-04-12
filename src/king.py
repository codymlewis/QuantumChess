# king.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
# Mod.: 24-FEB-2018
import piece
import functions
class King(piece.Piece):
    def __init__(self,superposNum,frstSuperPos,col,idT):
        idT = 'Ki' + str(idT)
        piece.Piece.__init__(self,superposNum,frstSuperPos,col,idT)

    def canMove(self,movement):
        moveArr = functions.splitMovement(movement)
        direction = moveArr[0]
        if(len(moveArr) == 1):
            if(direction == 'd' or direction == 'u' or direction == 'r' or direction == 'l' or direction == 'f' or direction == 'q' or direction == 'h' or direction == 'g'):
                return True
        return False
