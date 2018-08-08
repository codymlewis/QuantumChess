# Author: Cody Lewis
# Date: 12-APR-2018
# Description: The main game flow of the quantum chess game
import re
import board
if __name__ == "__main__":
    b = board.Board()
    i = 0
    col = 'B'
    pattern = '[Yy]e?s?'
    sp = False
    while(True):
        winVal = b.win()
        if(winVal == 'W'):
            print("White wins!")
            break
        elif(winVal == 'B'):
            print("Black wins!")
            break
        print(b.toString())
        i+=1
        if(col == 'W'):
            col = 'B'
            print("Blacks turn")
        else:
            col = 'W'
            print("Whites turn")
        while(True):
            superPos = str(input("Do you want to super-position (y/n)? "))
            if(re.match(pattern, superPos)):
                print('Super-position mode on')
                sp = True
            start = str(input("Choose your starting piece: "))
            end = str(input("Choose your end place: "))
            if(b.play(start, end, col, sp)):
                sp = False
                break
            else:
                print("Your move was invalid, try again")
