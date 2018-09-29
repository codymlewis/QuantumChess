from qiskit import QuantumProgram
def evalQubit(qrNo):  # check if the most occurring qubit is all ones
    qp = QuantumProgram()
    try:
        qr = qp.create_quantum_register("qr", qrNo)
        cr = qp.create_classical_register("cr", qrNo)
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
