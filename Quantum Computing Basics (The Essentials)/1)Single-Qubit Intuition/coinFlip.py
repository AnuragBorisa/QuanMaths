from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt

def quantum_coin_flip(shots=1000):
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)

    backend = Aer.get_backend('aer_simulator')
    result = backend.run(qc,shots=shots).result().get_counts()
    heads = result.get('0',0)
    tails = result.get('1',0)

    print(f"Heads (0):{heads},Tails (1):{tails}")
    plt.bar(['Heads','Tails'], [heads, tails])
    plt.ylabel('Counts')
    plt.title(f'Quantum Coin Flip ({shots} shots)')
    plt.show()

quantum_coin_flip(1000)