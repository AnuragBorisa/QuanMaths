from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
import numpy as np

def qaoa_cost(beta,gamma,shots=2000):
    qc = QuantumCircuit(2,2)

    qc.h([0,1])

    qc.cx(0,1)
    qc.rz(2*gamma,1)
    qc.cx(0,1)

    qc.rx(2*beta,[0,1])

    qc.measure([0,1],[0,1])

    sim = AerSimulator()
    qc_t = transpile(qc,sim)
    job = sim.run(qc_t,shots=shots)
    result = job.result()
    counts = result.get_counts()

    zz = (
        counts.get('00',0) + counts.get('11',0) - counts.get('01',0) - counts.get('10',0)
    ) / shots

    return (1-zz)/2

betas = np.linspace(0,2*np.pi,10)
gammas = np.linspace(0,2*np.pi,10)

best = {"cost":-1.0,"beta":None,"gamma":None}

for b in betas:
    for g in gammas:
        cost = qaoa_cost(b,g)
        if cost > best['cost']:
            best.update(cost=cost,beta=b,gamma=g)

print(f"Optimal cost ⟨C⟩ = {best['cost']:.4f}")
print(f" at β = {best['beta']:.3f}, γ = {best['gamma']:.3f}")