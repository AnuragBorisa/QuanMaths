from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator   # note: qiskit_aer, not qiskit.providers.aer
import numpy as np

# 1) Build your 2-qubit circuit
qc = QuantumCircuit(2)
qc.h(0)    # |+> on qubit 0
qc.x(1)    # |1> on qubit 1
qc.save_statevector()  

# 2) Create the simulator and transpile
sim = AerSimulator()
tqc = transpile(qc, sim)

# 3) Run and get the statevector
job   = sim.run(tqc)
res   = job.result()
data = res.data(0)    
state = data['statevector']

print("Statevector:", state)

# 4) Verify against the expected tensor product
expected = np.kron([0,1],[1,1]/np.sqrt(2))
print("Expected:   ", expected)
print("Match?      ", np.allclose(state, expected))
