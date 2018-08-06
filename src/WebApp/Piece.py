import Functions
from Functions import Direction
class Piece:
    def __init__(self, superposNum, frstSuperPos, col, idT):
        self.superposNo = superposNum
        self.firstSuperPos = frstSuperPos
        self.colour = col
        self.idTag = self.colour + idT

    def getId(self):
        return self.idTag

    def getSuperPosNum(self):
        return self.superposNo

    def superposition(self):
        self.superposNo += 1
        self.idTag = self.idTag + str(self.superposNo)
        if self.firstSuperPos:
            self.firstSuperPos = False

    def attack(self, enemy, movement):
        if self.canAttack(movement):
            return enemy.die()
        else:
            return False, False

    def canAttack(self, movement):
        return self.canMove(movement)

    def die(self):
        if self.superposNo > 0:
            return True, self.observe()
        return True, False

    def observe(self):
        # check the Qubit stored in this piece
        return Functions.evalQubit(self.superposNo)

class Pawn(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'P ' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)
        self.firstMove = True

    def canMove(self, movement):
        moveArr = Functions.splitMovement(movement)
        if(self.firstMove):
            moveNum = 2
            self.firstMove = False
        else:
            moveNum = 1
        if(len(moveArr) <= moveNum):
            if(self.colour == 'W'):
                direction = Direction.UP
            else:
                direction = Direction.DOWN
            for i in range(len(moveArr)):
                if(not moveArr[i] == direction):
                    return False
            return True
        return False

    def canAttack(self, movement):
        moveArr = Functions.splitMovement(movement)
        if(self.colour == 'W'):
            dir1 = Direction.UPLEFT
            dir2 = Direction.UPRIGHT
        else:
            dir1 = Direction.DOWNLEFT
            dir2 = Direction.DOWNRIGHT
        if(len(moveArr) == 1 and (moveArr[0] == dir1 or moveArr[0] == dir2)):
            return True
        else:
            return False

class Bishop(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'B ' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self,movement):
        moveArr = Functions.splitMovement(movement)
        direction = moveArr[0]
        if direction in [Direction.UPLEFT, Direction.UPRIGHT, Direction.DOWNLEFT, Direction.DOWNRIGHT]:
            for i in range(1, len(moveArr)):
                if(direction != moveArr[i]):
                    return False
            return True
        return False

class King(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Ki' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = Functions.splitMovement(movement)
        direction = moveArr[0]
        if(len(moveArr) == 1):
            if direction in [Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWNRIGHT, Direction.DOWNLEFT, Direction.UPRIGHT, Direction.UPLEFT]:
                return True
        return False

class Knight(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Kn' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = Functions.splitMovement(movement)
        if(len(moveArr) == 2): # need the L movement
            if(self.__isL(moveArr)):
                return True
        return False

    def __isL(self, moveArr):
        if(moveArr[0] == Direction.UP):
            if(moveArr[1] == Direction.UPLEFT or moveArr[1] == Direction.UPRIGHT):
                return True
        elif(moveArr[0] == Direction.DOWN):
            if(moveArr[1] == Direction.DOWNLEFT or moveArr[1] == Direction.DOWNRIGHT):
                return True
        elif(moveArr[0] == Direction.LEFT):
            if(moveArr[1] == Direction.UPLEFT or moveArr[1] == Direction.DOWNLEFT):
                return True
        elif(moveArr[0] == Direction.RIGHT):
            if(moveArr[1] == Direction.UPRIGHT or moveArr[1] == Direction.DOWNRIGHT):
                return True
        else:
            return False

class Queen(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'Q ' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = Functions.splitMovement(movement)
        direction = moveArr[0]
        if direction in [Direction.DOWN, Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWNRIGHT, Direction.DOWNLEFT, Direction.UPRIGHT, Direction.UPLEFT]:
            for i in range(1, len(moveArr)):
                if(direction != moveArr[i]):
                    return False
            return True
        return False

class Rook(Piece):
    def __init__(self, superposNum, frstSuperPos, col, idT):
        idT = 'R ' + str(idT)
        Piece.__init__(self, superposNum, frstSuperPos, col, idT)

    def canMove(self, movement):
        moveArr = Functions.splitMovement(movement)
        direction = moveArr[0]
        if direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
            for i in range(1, len(moveArr)):
                if direction != moveArr[i]:
                    return False
            return True
        return False
