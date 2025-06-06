from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from collections import Counter
import numpy as np

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

sim = AerSimulator()
qc_t = transpile(qc,sim)

job = sim.run(qc_t,shots = 1024)
counts = job.result().get_counts()

totalShots = sum(counts.values())

Pab = {
    (int(bitStr[0]),int(bitStr[1])) : cnt/totalShots
    for bitStr,cnt in counts.items()
}

Pa = { a:sum(p for (a2,b),p in Pab.items() if a2 == a) for a in (0,1)}
Pb = { b:sum(p for (a,b2),p in Pab.items() if b2 == b) for b in (0,1)}

E_A = Pa[1]
E_B = Pb[1]

E_AB = Pab.get((1,1),0.0)

sigma_A = np.sqrt(E_A * (1-E_A))
sigma_B = np.sqrt(E_B * (1-E_B))

rho = (E_AB - E_A * E_B) / (sigma_A * sigma_B)

print("Joint distribution P(A,B):", Pab)
print("Marginals P(A):", Pa, "P(B):", Pb)
print(f"Correlation ρ = {rho:.3f}")