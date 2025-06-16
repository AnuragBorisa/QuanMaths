from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np


plt.style.use('dark_background')


sim    = AerSimulator()
shots  = 2000
gammas = np.linspace(0, 2*np.pi, 40)


p00, p01, p10, p11 = [], [], [], []

for g in gammas:
    qc = QuantumCircuit(2, 2)
   
    qc.h([0, 1])
   
    qc.crz(g, 0, 1)
    
    qc.h([0, 1])
    
    qc.measure([0, 1], [0, 1])

   
    qc_t   = transpile(qc, sim)
    job    = sim.run(qc_t, shots=shots)
    counts = job.result().get_counts()

   
    p00.append(counts.get('00', 0) / shots)
    p01.append(counts.get('01', 0) / shots)
    p10.append(counts.get('10', 0) / shots)
    p11.append(counts.get('11', 0) / shots)


plt.figure(figsize=(10, 6))
plt.plot(gammas, p00, label='P(00)', linewidth=2)
plt.plot(gammas, p01, label='P(01)', linewidth=2, linestyle='-.')
plt.plot(gammas, p10, label='P(10)', linewidth=2, linestyle=':')
plt.plot(gammas, p11, label='P(11)', linewidth=2, linestyle='--')

plt.title('CRZ Phase Interference — All Outcome Probabilities', fontsize=18)
plt.xlabel(r'$\gamma$ (rad)', fontsize=14)
plt.ylabel('Probability', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=12, loc='upper right')
plt.tight_layout()
plt.show()
