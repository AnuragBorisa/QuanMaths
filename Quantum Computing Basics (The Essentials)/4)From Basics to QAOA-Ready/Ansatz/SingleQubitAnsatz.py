from qiskit import QuantumCircuit

qc = QuantumCircuit(1,1)
qc.ry(0,theta=20)
qc.measure(0,0)