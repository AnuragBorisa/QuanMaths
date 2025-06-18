from qiskit import QuantumCircuit

qc = QuantumCircuit(2,2)
qc.ry(theta,0)
qc.ry(theta1,0)

qc.cx(0,1)

qc.ry(theta2,0)
qc.ry(theta3,0)