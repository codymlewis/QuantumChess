# board.py - QuantumChess
# Author: Cody Lewis
# Date: 26-FEB-2018
# Mod.: 03-MAR-2018
# Description:
# The board for the Quantum Chess
# the board is indexed with a birds eye view with the white pieces on the bottom
import pawn
import rook
import bishop
import knight
import queen
import king
class Board:
    def __init__(self):
        self.playBoard = dict()
        self.rows = 8
        self.columns = 8
        for i in range(97,98+self.rows): # letters for columns, with 'a' at the top and 'i' at the bottom
            if(i == 97 or i == 98):
                colour = 'B'
            elif(i == 96+self.rows or i == 97+self.rows):
                colour = 'W'
            for j in range(1,self.columns+1): # numbers for rows, with 1 at the left and 8 at the right
                index = str(chr(i)) + str(j)
                if(i == 97 or i==97+self.rows):
                    if(j == 1 or j == 8):
                        self.playBoard[index] = rook.Rook(0,True,colour,j)
                    elif(j == 2 or j == 7):
                        self.playBoard[index] = knight.Knight(0,True,colour,j)
                    elif(j == 3 or j == 6):
                        self.playBoard[index] = bishop.Bishop(0,True,colour,j)
                    elif(j == 4):
                        self.playBoard[index] = queen.Queen(0,True,colour,j)
                    else:
                        self.playBoard[index] = king.King(0,True,colour,j)
                elif(i == 98 or i==96+self.rows):
                    self.playBoard[index] = pawn.Pawn(0,True,colour,j)
                else:
                    self.playBoard[index] = '0'
    
    def play(self,start,end,colour): # TODO: stop pieces from teleporting through eachother, modify the entanglement, add the superposition move
        # check if inputs are valid
        if(end != start and self.checkPoint(start) and self.checkPoint(end)):
            if(self.playBoard[start] != '0'):
                # check if colour matches
                if(colour == self.playBoard[start].getId()[0:1]):
                    # evaluate the path travelled
                    dy = ord(start[0:1]) - ord(end[0:1]) # +ve: up, -ve: down
                    dx = int(start[1:]) - int(end[1:])   # +ve: right, -ve: left
                    movement = self.pathToString(dx,dy)
                    # output path as string into piece
                    if(self.playBoard[end] == '0'):
                        if(self.playBoard[start].canMove(movement)):
                            self.playBoard[end] = self.playBoard[start]
                            self.playBoard[start] = '0'
                            return True
                        else:
                            return False
                    # check for attack
                    else: # ends at another piece
                        if(self.playBoard[start].getId()[0:1] != self.playBoard[end].getId()[0:1]): # canMove function is contained in attack
                            # then do the attack
                            kill,supKill = self.playBoard[start].attack(self.playBoard[end],movement)
                            if(kill): # maybe modify attack return values
                                self.playBoard[end] = self.playBoard[start]
                                self.playBoard[start] = '0'
                                if(supKill):
                                    self.findAndDestroyAllId(end)
                                return True
                            return False
                        else:
                            return False
        return False

    def checkPoint(self,p):
        charNum = ord(p[0:1])
        if(charNum > 96 and charNum < 98+self.rows):
            num = int(p[1:])
            if(num > 0 and num < 9):
                return True
        return False

    def pathToString(self,dx,dy):
        string = ''
        if(dx > 0): # goes right
            if(dy > 0): # goes up
                if(dx == 2 and  dy == 1): # L move
                    string = 'rq'
                elif(dx == 1 and dy == 2):
                    string = 'uq'
                elif(dx > dy):
                    diff = dx - dy
                    for i in range(dy):
                        string = string + 'q'
                    for i in range(diff):
                        string = string + 'r'
                elif(dx < dy):
                    diff = dy - dx
                    for i in range(dx):
                        string = string + 'q'
                    for i in range(diff):
                        string = string + 'u'
                else:
                    for i in range(dx):
                        string = string + 'q'
            elif(dy == 0):
                for i in range(dx):
                    string = string + 'r'
            else: # goes down
                if(dx == 2 and dy == -1):
                    string = 'rg'
                elif(dx == 1 and dy == -2):
                    string = 'dg'
                elif(dx > abs(dy)):
                    diff = dx - abs(dy) # dy is -ve
                    for i in range(abs(dy)):
                        string = string + 'g'
                    for i in range(diff):
                        string = string + 'r'
                elif(dx < abs(dy)):
                    diff = abs(dy) - dx
                    for i in range(dx):
                        string = string + 'g'
                    for i in range(diff):
                        string = string + 'd'
                else:
                    for i in range(dx):
                        string = string + 'g'
        elif(dx == 0):
            if(dy > 0): # up
                for i in range(dy):
                    string = string + 'u'
            else: # down (no change is an invalid input)
                for i in range(abs(dy)):
                    string = string + 'd'
        else: # goes left
            if(dy > 0): # goes up
                if(dx == -2 and  dy == 1): # L move
                    string = 'lf'
                elif(dx == -1 and dy == 2):
                    string = 'uf'
                elif(abs(dx) > dy):
                    diff = abs(dx) - dy
                    for i in range(dy):
                        string = string + 'f'
                    for i in range(diff):
                        string = string + 'l'
                elif(abs(dx) < dy):
                    diff = dy - abs(dx)
                    for i in range(abs(dx)):
                        string = string + 'f'
                    for i in range(diff):
                        string = string + 'u'
                else:
                    for i in range(abs(dx)):
                        string = string + 'f'
            elif(dy == 0):
                for i in range(abs(dx)):
                    string = string + 'l'
            else: # goes down
                if(dx == -2 and dy == -1):
                    string = 'lh'
                elif(dx == -1 and dy == -2):
                    string = 'dh'
                elif(abs(dx) > abs(dy)):
                    diff = abs(dx) - abs(dy) # dy is -ve
                    for i in range(abs(dy)):
                        string = string + 'h'
                    for i in range(diff):
                        string = string + 'l'
                elif(abs(dx) < abs(dy)):
                    diff = abs(dy) - abs(dx)
                    for i in range(abs(dx)):
                        string = string + 'h'
                    for i in range(diff):
                        string = string + 'd'
                else:
                    for i in range(abs(dx)):
                        string = string + 'h'
        return string
    def findAndDestroyAllId(self,index):
        # search board for all matching pieces and destroy them
        return ''

    def toString(self):
        string = ''
        for i in range(97,99+self.rows):
            if(i < 98+self.rows):
                string = string + chr(i)
            string = string + ' '
            for j in range(1,self.columns+1):
                index = str(chr(i)) + str(j)
                if(i == 98+self.rows):
                    string = string + '   ' + str(j)
                elif(self.playBoard[index] == '0'):
                    string = string + '|   '
                else:
                    idTag = self.playBoard[index].getId()[:3]
                    string = string + '|' + idTag
            if(i < 98+self.rows):
                string = string + '|\n'
        return string