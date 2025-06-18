from qiskit import QuantumCircuit

qc = QuantumCircuit(2,2)
qc.ry(theta,0)
qc.ry(theta1,1)
qc.measure([0,1],[0,1])