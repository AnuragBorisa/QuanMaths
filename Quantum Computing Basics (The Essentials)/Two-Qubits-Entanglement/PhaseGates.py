from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np


qc = QuantumCircuit(1)
qc.s(0)     
qc.h(0)      


qc.save_statevector()


sim = AerSimulator()
tqc = transpile(qc, sim)


result = sim.run(tqc).result()


data = result.data(0)            
state = data['statevector']     
alpha, beta = state


x = 2 * np.real(np.conj(alpha) * beta)
y = 2 * np.imag(np.conj(alpha) * beta)
z = np.abs(alpha)**2 - np.abs(beta)**2

print(f"Final statevector: α = {alpha}, β = {beta}")
print(f"Bloch vector: x = {x:.3f}, y = {y:.3f}, z = {z:.3f}")
