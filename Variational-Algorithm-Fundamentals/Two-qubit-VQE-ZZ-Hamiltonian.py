from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

sim = AerSimulator()
costs = []

def expectation_ZZ(thetas):
    theta1 , theta2 = thetas

    qc = QuantumCircuit(2,2)
    qc.ry(theta1,0)
    qc.cx(0,1)
    qc.ry(theta2,1)
   
    qc.measure([0,1],[0,1])

    qc_t = transpile(qc,sim)
    job = sim.run(qc_t,shots=1024)
    result = job.result()
    counts = result.get_counts()
    total = sum(counts.values())
    zz = ((counts.get('00',0)+counts.get('11',1))-(counts.get('10',0)+counts.get('01',0)))/total
    costs.append(zz)
    return zz;
  
def main():
    intial_thetas = np.array([0.1,0.1])

    res_cobyla = minimize(
    fun=expectation_ZZ,
    x0=intial_thetas,
    method='COBYLA',
    options={'tol': 1e-2, 'maxiter': 100}
    )

    theta1_optimised , theta2_optimised = res_cobyla.x
    print(f"Optimal angles: θ₀ = {theta1_optimised:.4f}, θ₁ = {theta2_optimised:.4f}")
    print(f"Minimum ⟨ZZ⟩ = {res_cobyla.fun:.4f}")

    plt.figure(figsize=(6,4))
    plt.plot(costs,marker='o')
    plt.title("VQE Convergence: ⟨ZZ⟩ vs. Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Energy ⟨ZZ⟩")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()





    