from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import HGate

H = HGate()
sv0 = Statevector.from_label("0").evolve(H)
sv1 = Statevector.from_label("1").evolve(H)

print("H|0> =", sv0.data)  # [1/√2, 1/√2]
print("H|1> =", sv1.data)  # [1/√2, -1/√2]

qc = QuantumCircuit(1,1)
qc.h(0)
qc.h(0)
qc.measure(0,0);
counts = Aer.get_backend('aer_simulator').run(qc,shots=1000).result().get_counts()
print(counts)