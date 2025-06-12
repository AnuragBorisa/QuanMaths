from qiskit import QuantumCircuit,transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

bell_builder = QuantumCircuit(2,name="bell_pair")
bell_builder.h(0)
bell_builder.cx(0,1)
bell_instruction = bell_builder.to_instruction()
print(bell_instruction)
print(bell_instruction.definition)

qc = QuantumCircuit(4,4)
qc.append(bell_builder,[0,1])
qc.append(bell_builder,[2,3])
qc.measure(range(4),range(4))

backend = AerSimulator()
qc_t = transpile(qc,backend)
job = backend.run(qc_t,shots=1024)
counts = job.result().get_counts()
plot_histogram(counts)
plt.show()




