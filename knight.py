# knight.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
# Mod.: 24-FEB-2018
import piece
import functions
class Knight(piece.Piece):
    def __init__(self,superposNum,frstSuperPos,col,idT):
        idT = 'Kn' + str(idT)
        piece.Piece.__init__(self,superposNum,frstSuperPos,col,idT)

    def canMove(self,movement):
        moveArr = functions.splitMovement(movement)
        if(len(moveArr) == 2): # need the L movement
            if(self.__isL(moveArr)):
                return True
        return False

    def __isL(self,moveArr):
        if(moveArr[0] == 'u'):
            if(moveArr[1] == 'f' or moveArr[1] == 'q'):
                return True
        elif(moveArr[0] == 'd'):
            if(moveArr[1] == 'h' or moveArr[1] == 'g'):
                return True
        elif(moveArr[0] == 'l'):
            if(moveArr[1] == 'q' or moveArr[1] == 'g'):
                return True
        elif(moveArr[0] == 'r'):
            if(moveArr[1] == 'f' or moveArr[1] == 'h'):
                return True
        else:
            return False
