from qiskit import QuantumCircuit,transpile ,QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt 

qr = QuantumRegister(2, name="q")
cr = ClassicalRegister(2, name="c")
qc = QuantumCircuit(qr, cr)
qc.h(qr[0])

qc.measure(qr[0], cr[0])

with qc.if_test((cr, 1)):
    qc.x(qr[1])

qc.measure(qr[1], cr[1])

print(qc.draw('mpl'))

sim = AerSimulator()
qc_t = transpile(qc,sim)
job = sim.run(qc_t,shots=1024)
result = job.result()
counts = result.get_counts()

plot_histogram(counts)
plt.show()