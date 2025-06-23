from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from scipy.optimize import minimize
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

x0 = np.array([0.1])

res_cobyla = minimize(
    fun = expectation_Z,
    x0= x0,
    method='COBYLA',
    options={'tol': 1e-2, 'maxiter': 100}
)

print("COBYLA result:")
print(" θ =", res_cobyla.x, ", C =", res_cobyla.fun)