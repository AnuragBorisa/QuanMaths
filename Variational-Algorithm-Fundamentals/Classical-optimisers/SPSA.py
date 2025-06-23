from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit_algorithms.optimizers import SPSA
import numpy as np
import matplotlib.pyplot as plt

sim = AerSimulator()

def expectation_Z(theta):
    qc = QuantumCircuit(1,1)
    qc.rx(theta[0],0)
    qc.measure(0,0)
    
    qc_t = transpile(qc,sim)
    job = sim.run(qc_t,shots=1024)
    result = job.result()
    counts = result.get_counts()

    return (counts.get('0',0) - counts.get('1',0)) / 1024

spsa = SPSA(
    maxiter=100,
    learning_rate=0.2,
    perturbation=0.1,
    last_avg=5
)

res_spsa = spsa.minimize(
    fun=lambda x: expectation_Z(x),
    x0=np.array([0.1])
)

print("SPSA result:")
print(" θ =", res_spsa.x, ", C =", res_spsa.fun)