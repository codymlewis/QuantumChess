# bishop.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
import piece
import functions
class Bishop(piece.Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'B ' + str(idT)
        piece.Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self,movement):
        moveArr = functions.splitMovement(movement)
        direction = moveArr[0]
        if direction == functions.Direction.UPLEFT or direction == functions.Direction.UPRIGHT or direction == functions.Direction.DOWNLEFT or direction == functions.Direction.DOWNRIGHT:
            for i in range(1, len(moveArr)):
                if(direction != moveArr[i]):
                    return False
            return True
        return False
