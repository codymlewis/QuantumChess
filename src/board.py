# board.py - QuantumChess
# Author: Cody Lewis
# Date: 26-FEB-2018
# Mod.: 04-MAY-2018
# Description:
# The board for the Quantum Chess
# the board is indexed with a birds eye view with the white pieces on the bottom
import re # regex
import pawn # the various pieces
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
                if(i == 97 or i==97+self.rows): # essentially a factory method
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

    def addMovement(self,i,move): # add an atomic movement unit to the index
        if(move == 'u'):
            i = chr(ord(i[0:1])-1) + str(int(i[1:]))
        elif(move == 'd'):
            i = chr(ord(i[0:1])+1) + str(int(i[1:]))
        elif(move == 'r'):
            i = i[0:1] + str(int(i[1:])-1)
        elif(move == 'l'):
            i = i[0:1] + str(int(i[1:])+1)
        elif(move == 'q'):
            i = chr(ord(i[0:1])-1) + str(int(i[1:])-1)
        elif(move == 'g'):
            i = chr(ord(i[0:1])+1) + str(int(i[1:])-1)
        elif(move == 'h'):
            i = chr(ord(i[0:1])+1)  + str(int(i[1:])+1)
        else:
            i = chr(ord(i[0:1])-1) + str(int(i[1:])+1)
        return i
    
    def play(self,start,end,colour,sp):
        # check if inputs are valid
        if(end != start and self.checkPoint(start) and self.checkPoint(end)):
            if(self.playBoard[start] != '0'):
                # check if colour matches
                if(colour == self.playBoard[start].getId()[0:1]):
                    # evaluate the path travelled
                    dy = ord(start[0:1]) - ord(end[0:1]) # +ve: up, -ve: down
                    dx = int(start[1:]) - int(end[1:])   # +ve: right, -ve: left
                    movement = self.pathToString(dx,dy)
                    i = start
                    i = self.addMovement(i,movement[0:1]) 
                    if(i != end and self.playBoard[i] != '0'): # make sure nothing is in the way
                        return False
                    if(len(movement) > 1):
                        for j in range(1,len(movement)):
                            i = self.addMovement(i,movement[j:j+1])
                            if(i != end and self.playBoard[i] != '0'):
                                return False
                    # output path as string into piece
                    if(self.playBoard[end] == '0'):
                        if(self.playBoard[start].canMove(movement)):
                            if(sp):
                                self.playBoard[start].superposition()
                                self.playBoard[end] = self.playBoard[start]
                            else:
                                self.playBoard[end] = self.playBoard[start]
                                self.playBoard[start] = '0'
                            return True
                        else:
                            return False
                    # check for attack
                    else: # ends at another piece
                        if(sp):
                            return False
                        if(self.playBoard[start].getId()[0:1] != self.playBoard[end].getId()[0:1]): # canMove function is contained in attack
                            # then do the attack
                            kill,supKill = self.playBoard[start].attack(self.playBoard[end],movement)
                            if(kill):
                                if(supKill):
                                    self.findAndDestroyParent(end)
                                self.playBoard[end] = self.playBoard[start]
                                self.playBoard[start] = '0'
                                return True
                            return False
                        else:
                            return False
        return False

    def checkPoint(self,p): # check whether a point is on the board
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

    def findAndDestroyParent(self,point):
        # search board for all matching pieces and destroy them
        ident = self.playBoard[point].getId() # identifier
        num = int(ident[len(ident)-1:len(ident)])
        parent = ident[0:len(ident)-1] + '.'
        for i in range(97,98+self.rows):
            for j in range(1,self.columns+1):
                index = chr(i) + str(j)
                if(self.playBoard[index] != '0'):
                    if(index != point and re.match(parent,self.playBoard[index].getId())):
                        otherId = self.playBoard[index].getId()
                        otherNum = int(otherId[len(otherId)-1:len(otherId)])
                        if(otherNum >= num):
                            self.playBoard[index] = '0'

    def win(self): # find if one of the players have no kings left
        blackWin = True
        bkPat = 'BKi.*'
        whiteWin = True
        wkPat = 'WKi.*'
        for i in range(97,98+self.rows):
            for j in range(1,self.columns+1):
                index = chr(i) + str(j)
                if(self.playBoard[index] != '0'):
                    currId = self.playBoard[index].getId()
                    if(re.match(bkPat,currId)):
                        whiteWin = False
                    elif(re.match(wkPat,currId)):
                        blackWin = False
        if(whiteWin):
            return 'W'
        elif(blackWin):
            return 'B'
        else:
            return '0'

    def toString(self):
        string = ''
        for i in range(97,99+self.rows): # iterate through the letter part of the index
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
            if(i < 98+self.rows): # put a pipe at the end of the line
                string = string + '|\n'
        return string
