from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.quantum_info import Statevector, Pauli

# prepare |0>
sv0 = Statevector.from_label("0")
print("X|0> =",     sv0.evolve(Pauli('X')).data)
print("Y|0> =",     sv0.evolve(Pauli('Y')).data)

# plus‐state
qc_h = QuantumCircuit(1)
qc_h.h(0)
sv_plus = sv0.evolve(qc_h)
print("Z|+> =",     sv_plus.evolve(Pauli('Z')).data)

# measurement routine
shots = 1000
sim   = Aer.get_backend("aer_simulator")

def measure_pauli(pauli: str):
    qc = QuantumCircuit(1, 1)
    qc.initialize([1, 0], 0)   # start in |0>
    if   pauli == "x": qc.h(0)
    elif pauli == "y": qc.rx(-3.14159/2, 0)
    qc.measure(0, 0)
    counts = sim.run(qc, shots=shots).result().get_counts()
    print(f"Measure {pauli.upper()}:  {counts}")

measure_pauli("z")   # ≈1000 '0'
measure_pauli("x")   # ≈500/500
measure_pauli("y")   # ≈500/500
