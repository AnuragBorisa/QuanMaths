# here we will just look at the knobs as theta and how to caluclate the expecatation value which we use
from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt 

sim = AerSimulator()

def compute_zz(theta,shots=5000):
    qc = QuantumCircuit(2,2)
    qc.ry(theta,0)
    qc.ry(theta,1)
    qc.cx(0,1)
    qc.measure([0,1],[0,1])

    qc_t = transpile(qc,sim)
    job = sim.run(qc_t,shots=shots)
    result = job.result()
    counts = result.get_counts()

    exp = (
        counts.get('00',0)
       +counts.get('11',0)
       -counts.get('01',0)
       -counts.get('10',0)
    ) / shots
    return exp

thetas = np.linspace(0,2*np.pi,50)
expectations = [compute_zz(t) for t in thetas]

plt.plot(thetas,expectations,marker='o')
plt.xlabel('θ (radians)')
plt.ylabel('⟨Z⊗Z⟩')
plt.title('One-Layer Variational Circuit')
plt.show()