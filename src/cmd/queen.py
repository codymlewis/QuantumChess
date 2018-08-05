# queen.py - QuantumChess
# Author: Cody Lewis
# Date: 24-FEB-2018
import piece
import functions
from functions import Direction
class Queen(piece.Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Q ' + str(idT)
        piece.Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = functions.splitMovement(movement)
        direction = moveArr[0]
        if direction in [Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWNRIGHT, Direction.DOWNLEFT, Direction.UPRIGHT, Direction.UPLEFT]:
            for i in range(1, len(moveArr)):
                if(direction != moveArr[i]):
                    return False
            return True
        return False
