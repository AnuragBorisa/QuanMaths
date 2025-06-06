from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
import numpy as np

qc = QuantumCircuit(2)
qc.h(0)
qc.save_statevector(label="state_after_h")
qc.cx(0,1)
qc.save_statevector(label="state_after_cx")

sim = AerSimulator()
qc_t = transpile(qc,sim)
job = sim.run(qc_t)
result = job.result()
data = result.data(0)

state_after_h = data["state_after_h"]
state_after_cx = data["state_after_cx"]

np.set_printoptions(precision=4, suppress=True)

print("=== Statevector after Hadamard on q0 ===")
print(state_after_h)  

print("\n=== Statevector after CNOT(0→1) ===")
print(state_after_cx)

