from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator


# prepare the bell states 
# (a) |Φ⁺⟩ = (|00⟩ + |11⟩)/√2
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0,1)

# (b) |Φ⁻⟩ = (|00⟩ − |11⟩)/√2
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0,1)
# qc.z(1)


# (c) |Ψ⁺⟩ = (|01⟩ + |10⟩)/√2
# qc = QuantumCircuit(2)
# qc.x(1)
# qc.h(0)
# qc.cx(0,1)

# (d) |Ψ⁻⟩ = (|01⟩ − |10⟩)/√2
# qc = QuantumCircuit(2)
# qc.x(1)
# qc.h(0)
# qc.cx(0,1)
# qc.z(1)

qc = QuantumCircuit(2,2)
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

sim = AerSimulator()

qc_t = transpile(qc,sim)

job = sim.run(qc_t,shots=1024)

counts = job.result().get_counts()
print(counts)






