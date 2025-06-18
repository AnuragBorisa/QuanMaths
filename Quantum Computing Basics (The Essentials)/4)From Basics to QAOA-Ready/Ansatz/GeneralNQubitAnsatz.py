from qiskit import QuantumCircuit

def build_ansatz(qubits,reps):
    qc = QuantumCircuit(qubits,qubits)

    for r in range(reps):

        for i in range(qubits):
            qc.ry(theta[r][i],i)
            qc.rz(phi[r][i],i)

        for i in range(qubits-1):
            qc.cx(i,i+1)
        
        qc.cx(qubits-1,0)
    
    qc.measure(range(qubits),range(qubits))
    return qc
            