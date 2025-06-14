from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt 

qc = QuantumCircuit(1,1)
qc.h(0)
qc.measure(0,0)

sim = AerSimulator()
qc_t = transpile(qc,sim)
backend = sim.run(qc_t,shots=1024)
result = backend.result()
counts = result.get_counts()

label_map = {'0':'Left','1':'Right'}
count_pos = {label_map[k]:v for k,v in counts.items()}

plot_histogram(
    count_pos,
    title='One-step Quantum Random Walk (1 000 trials)'
)
plt.ylabel('Number of trials')
plt.show()

