# functions.py - QuantumChess
# Author: Cody Lewis
# Date: 23-FEB-2018
# Mod.: 25-FEB-2018
# Description:
# defines misc. functions for the Quantum Chess program
def evalQubit(qrNo):
    from qiskit import QuantumProgram
    qp = QuantumProgram()
    try:
        qr = qp.create_quantum_register("qr",qrNo)
        cr = qp.create_classical_register("cr",qrNo)
        qc = qp.create_circuit("superposition", [qr], [cr])
        
        isPiece = ''
        for i in range(qrNo):
            qc.h(qr[i])
            isPiece = isPiece + '1'
        qc.measure(qr, cr)
        result = qp.execute(["superposition"], backend="local_qasm_simulator", shots=1024)
        counts = result.get_counts("superposition")
        return isPiece == getGreatestCount(qrNo,counts)
    except QISKITError as ex:
        print("There was an error in the circuit! Error = {}".format(ex))
    except RegisterSizeError as ex:
        print("Error in the number of registers! Error = {}".format(ex))

def getGreatestCount(qrNo,counts):
    # increment throught dict, find greatest value, return index
    greatestCount = ''
    gc = 0
    perms = pow(2,qrNo)
    for i in range(0,perms):
        index = bin(i)[2:]
        if(len(index) < qrNo):
            while(len(index) < qrNo):
                index = '0' + index
        if(counts[index] > gc):
            greatestCount = index
            gc = counts[index]
    return greatestCount

def pow(n,i):
    if(i == 0 or i == 1):
        return n
    else:
        return n*pow(n,i-1)

def splitMovement(movement):
    # split the string movement into individual characters and store them in the returned array
    # movement key: f = up dia left, u = up, q = up dia right, r = right, l = left, h = down dia left, d = down, g = down dia right
    # Note: The move movement directions are from a birds eye view with the white pieces on the bottom
    moveArr = []
    for i in range(len(movement)):
        moveArr.append(movement[i:i+1])
    return moveArr
