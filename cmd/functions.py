# functions.py - QuantumChess
# Author: Cody Lewis
# Date: 23-FEB-2018
# Description:
# defines misc. functions for the Quantum Chess program
from enum import Enum
from qiskit import *
def evalQubit(qrNo): # check if the most occurring qubit is all ones
    try:
        qr = QuantumRegister(qrNo)
        cr = ClassicalRegister(qrNo)
        qc = QuantumCircuit(qr, cr)

        isPiece = ''
        for i in range(qrNo):
            qc.h(qr[i])
            isPiece = isPiece + '1'
        qc.measure(qr, cr)
        result = execute(qc, Aer.get_backend("local_qasm_simulator")).result()
        counts = result.get_counts(qc)
        return isPiece == getGreatestCount(qrNo, counts)
    except QISKITError as ex:
        print("There was an error in the circuit! Error = {}".format(ex))
    except RegisterSizeError as ex:
        print("Error in the number of registers! Error = {}".format(ex))

def getGreatestCount(qrNo, counts):
    # increment throught dict, find greatest value, return index
    greatestCount = ''
    gc = 0
    perms = 2**qrNo
    for i in range(0, perms):
        index = bin(i)[2:]
        if len(index) < qrNo:
            while len(index) < qrNo:
                index = '0' + index
        if counts[index] > gc:
            greatestCount = index
            gc = counts[index]
    return greatestCount

def splitMovement(movement):
    # split the string movement into individual characters and store them in the returned array
    # movement key: f = up dia left, u = up, q = up dia right, r = right, l = left, h = down dia left, d = down, g = down dia right
    # Note: The move movement directions are from a birds eye view with the white pieces on the bottom
    moveArr = []
    for i in range(len(movement)):
        moveArr.append(movement[i:i+1])
    return moveArr

class Direction(Enum):
    UPLEFT = "f"
    UP = "u"
    UPRIGHT = "q"
    RIGHT = "r"
    LEFT = "l"
    DOWN = "d"
    DOWNLEFT = "h"
    DOWNRIGHT = "g"
