from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt 

qc = QuantumCircuit(2,2)

qc.h([0,1])

qc.measure([0,1],[0,1])

sim = AerSimulator()
qc_t = transpile(qc,sim)
job = sim.run(qc_t,shots=1024)
result = job.result()
counts = result.get_counts()

print("Counts:", counts)
zero = counts.get('00',00)
one  = counts.get('01',00)
two  = counts.get('10',00)
three = counts.get('11',00)

print((0,zero),(1,one),(2,two),(3,three))

fig = plot_histogram(counts,bar_labels=False)
plt.title("Quantum 2-qubit Dice (0–3 Uniform)")
plt.show()
