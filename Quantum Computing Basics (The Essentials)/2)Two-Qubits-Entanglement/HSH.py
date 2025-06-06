from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1,1)
qc.h(0)
qc.s(0)
qc.h(0)
qc.measure(0,0)

sim = AerSimulator()
qc_t = transpile(qc,sim)

job = sim.run(qc_t,shots=1024)
result = job.result()
counts = result.get_counts()

print(counts)