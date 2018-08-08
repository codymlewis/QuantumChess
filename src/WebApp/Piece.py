from . import Functions
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
                direction = Functions.Direction.UP.value
            else:
                direction = Functions.Direction.DOWN.value
            for i in range(len(moveArr)):
                if(not moveArr[i] == direction):
                    return False
            return True
        return False

    def canAttack(self, movement):
        moveArr = Functions.splitMovement(movement)
        if(self.colour == 'W'):
            dir1 = Functions.Direction.UPLEFT.value
            dir2 = Functions.Direction.UPRIGHT.value
        else:
            dir1 = Functions.Direction.DOWNLEFT.value
            dir2 = Functions.Direction.DOWNRIGHT.value
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
        if direction in [Functions.Direction.UPLEFT.value, Functions.Direction.UPRIGHT.value, Functions.Direction.DOWNLEFT.value, Functions.Direction.DOWNRIGHT.value]:
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
            if direction in [Functions.Direction.DOWN.value, Functions.Direction.UP.value, Functions.Direction.RIGHT.value, Functions.Direction.LEFT.value, Functions.Direction.DOWNRIGHT.value, Functions.Direction.DOWNLEFT.value, Functions.Direction.UPRIGHT.value, Functions.Direction.UPLEFT.value]:
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
        if(moveArr[0] == Functions.Direction.UP.value):
            if(moveArr[1] == Functions.Direction.UPLEFT.value or moveArr[1] == Functions.Direction.UPRIGHT.value):
                return True
        elif(moveArr[0] == Functions.Direction.DOWN.value):
            if(moveArr[1] == Functions.Direction.DOWNLEFT.value or moveArr[1] == Functions.Direction.DOWNRIGHT.value):
                return True
        elif(moveArr[0] == Functions.Direction.LEFT.value):
            if(moveArr[1] == Functions.Direction.UPLEFT.value or moveArr[1] == Functions.Direction.DOWNLEFT.value):
                return True
        elif(moveArr[0] == Functions.Direction.RIGHT.value):
            if(moveArr[1] == Functions.Direction.UPRIGHT.value or moveArr[1] == Functions.Direction.DOWNRIGHT.value):
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
        if direction in [Functions.Direction.DOWN.value, Functions.Direction.UP.value, Functions.Direction.RIGHT.value, Functions.Direction.LEFT.value, Functions.Direction.DOWNRIGHT.value, Functions.Direction.DOWNLEFT.value, Functions.Direction.UPRIGHT.value, Functions.Direction.UPLEFT.value]:
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
        if direction in [Functions.Direction.UP.value, Functions.Direction.DOWN.value, Functions.Direction.LEFT.value, Functions.Direction.RIGHT.value]:
            for i in range(1, len(moveArr)):
                if direction != moveArr[i]:
                    return False
            return True
        return False
