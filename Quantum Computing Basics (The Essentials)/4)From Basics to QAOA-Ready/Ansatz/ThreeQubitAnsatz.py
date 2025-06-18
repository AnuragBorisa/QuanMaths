from qiskit import QuantumCircuit

qc = QuantumCircuit(3,3)

for i in range(3):
    qc.ry(theta[i],i)


qc.cx(0,1)
qc.cx(1,2)
qc.cx(2,0)

for i in range(3):
    qc.rz(phi[i],i)

qc.measure([0,1,2],[0,1,2])