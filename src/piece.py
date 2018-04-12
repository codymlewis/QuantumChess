# piece.py - QuantumChess
# Author: Cody Lewis
# Date: 21-FEB-2018
# Mod.: 28-FEB-2018
# Description: Defines the super class of a piece in Quantum Chess
import functions
class Piece:
    def __init__(self,superposNum,frstSuperPos,col,idT):
        self.superposNo = superposNum
        self.firstSuperPos = frstSuperPos
        self.colour = col
        self.idTag = self.colour + idT

    def getId(self):
        return self.idTag

    def superpostion(self):
        if(self.firstSuperPos):
            self.__init__(1,False,self.colour,self.idTag)

    def attack(self,enemy,movement):
        if(self.canAttack(movement)):
            return enemy.die()
        else:
            return False
    
    def canAttack(self,movement):
        return self.canMove(movement)

    def die(self):
        if(self.superposNo > 0):
            return True,self.observe()
        return True,False

    def observe(self):
        # check the Qubit stored in this piece
        return functions.evalQubit(self.superposNo)
