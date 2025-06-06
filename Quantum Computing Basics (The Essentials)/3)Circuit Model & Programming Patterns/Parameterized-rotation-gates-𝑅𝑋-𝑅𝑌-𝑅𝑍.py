import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector


sim = AerSimulator(method = 'statevector')

def prob_after_rotation(theta):
    qc = QuantumCircuit(1)
    qc.ry(theta,0)
    qc.save_statevector()

    qc_t = transpile(qc,sim)
    job = sim.run(qc_t)
    result = job.result()

    data = result.data(0)['statevector']
    
    sv = Statevector(data)

    probs = sv.probabilities()

    return probs[1]

theta_values = np.linspace(0,2*np.pi,200)
probabilities = [prob_after_rotation(theta) for theta in theta_values ]

plt.figure(figsize=(8, 4))
plt.plot(theta_values, probabilities, label='P(1) via Statevector.probabilities()')
plt.title("P(1) after RY(θ) |0⟩")
plt.xlabel("θ (radians)")
plt.ylabel("P(1)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


    

    
