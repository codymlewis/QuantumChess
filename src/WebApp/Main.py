from qiskit import QuantumProgram
from flask import (
    Blueprint, render_template, url_for, redirect, current_app, g, session, request, flash
)
bp = Blueprint("Main", __name__, url_prefix="/")

@bp.route("/")
def index():
    return redirect(url_for("Main.home"))

@bp.route("/home/")
def home():
    return render_template("index.html")

def evalQubit(qrNo): # check if the most occurring qubit is all ones
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
        return isPiece == getGreatestCount(qrNo, counts)
    except QISKITError as ex:
        print("There was an error in the circuit! Error = {}".format(ex))
    except RegisterSizeError as ex:
        print("Error in the number of registers! Error = {}".format(ex))

def getGreatestCount(qrNo,counts):
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
class Piece:
    def __init__(self, superposNum, frstSuperPos, col, idT):
        self.superposNo = superposNum
        self.firstSuperPos = frstSuperPos
        self.colour = col
        self.idTag = self.colour + idT

    def getId(self):
        return self.idTag

    def getSuperPosNum(self):
        return self.superPosNo

    def superposition(self):
        self.superposNo += 1
        self.idTag = self.idTag + str(self.superposNo)
        if self.firstSuperPos:
            self.firstSuperPos = False

    def attack(self,enemy,movement):
        if self.canAttack(movement):
            return enemy.die()
        else:
            return False,False

    def canAttack(self,movement):
        return self.canMove(movement)

    def die(self):
        if self.superposNo > 0:
            return True, self.observe()
        return True, False

    def observe(self):
        # check the Qubit stored in this piece
        return evalQubit(self.superposNo)