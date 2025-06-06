import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer


def parse_state(raw:str)->complex:
    """Safely eval a user-entered complex number."""
    return complex(eval(raw, {"__builtins__":None, "sqrt":np.sqrt, "np":np}))

def normalise(alpha:complex,beta:complex):
    norm = np.linalg.norm([alpha,beta])
    alpha = alpha/norm
    beta = beta/norm

    return alpha , beta 

def to_bloch(alpha:complex,beta:complex):
    phase = np.angle(alpha)
    a,b = alpha*np.exp(-1j*phase) , beta*np.exp(-1j*phase)
    theta = 2*np.arccos(a.real)
    phi = np.angle(b)

    return theta,phi

def simulate_with_aer(alpha:complex,beta:complex,shots:int = 1000):
    qc = QuantumCircuit(1,1)
    qc.initialize([alpha,beta],0)
    qc.measure(0,0)

    backend = Aer.get_backend('aer_simulator')
    result = backend.run(qc,shots=shots).result().get_counts()
    return result.get('0',0) ,result.get('1',0)

def plots_counts(c0:int,c1:int,shots:int):
    plt.bar(['0','1'],[c0,c1])
    plt.xlabel('Outcome')
    plt.ylabel('Counts')
    plt.title(f'Z-basis Measurement ({shots} shots)')
    plt.show()



def main():
    alpha = parse_state(input("α = ").strip())
    beta  = parse_state(input("β = ").strip())

    alpha ,beta = normalise(alpha,beta)

    θ, φ = to_bloch(alpha, beta)
    print(f"θ = {θ:.4f} rad, φ = {φ:.4f} rad")

    shots = 1000
    c0,c1 = simulate_with_aer(alpha, beta, shots)
    print(f"Counts → |0>: {c0}, |1>: {c1}")

    plots_counts(c0, c1, shots)

if __name__=="__main__":
    main()