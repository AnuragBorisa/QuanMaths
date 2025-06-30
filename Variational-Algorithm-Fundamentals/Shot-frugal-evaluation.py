import numpy as np
import matplotlib.pyplot as plt 
from qiskit import QuantumCircuit,transpile
from qiskit_aer.primitives import Sampler as AerSampler
from qiskit.quantum_info import SparsePauliOp


def max_cut_hamiltonian(edges:list[tuple[int,int]],n:int)->SparsePauliOp:
    terms:list[tuple[int,int]]= []
    for i,j in edges:
        lables = ['I']*n
        lables[i] = 'Z'
        lables[j] = 'Z'
        pauli_str = ''.join(lables[::-1])
        terms.append((pauli_str,-0.5))
    
    const = 0.5 * len(edges)
    terms.append(('I'*n,const))
    return SparsePauliOp.from_list(terms)

def expectation(counts: dict[str,int], H: SparsePauliOp) -> float:
    n = H.num_qubits
    total = sum(counts.values())
    exp = 0.0

    for outcome, weight in counts.items():
        
        bitstr = outcome if isinstance(outcome, str) else format(outcome, f'0{n}b')

        
        E_x = 0.0
        for pauli_str, coeff in H.to_list():
            eig = 1
            for q, p in enumerate(pauli_str[::-1]):
                if p == 'Z':
                    eig *= (1 if bitstr[q] == '0' else -1)
            E_x += coeff * eig

        exp += (weight/total) * E_x

    return exp


def qaoa_circuit(params:np.ndarray,edges:list[tuple[int,int]])->QuantumCircuit:
    gamma , beta = params
    n = 3
    qc = QuantumCircuit(n)

    qc.h(range(n))

    for i,j in edges : 
        qc.cx(i,j)
        qc.rz(2*gamma,j)
        qc.cx(i,j)
    
    for q in range(n):
        qc.rx(2*beta,q)
    
    qc.measure_all()
    return qc

def finite_diff_grad(
    i : int,
    params : np.ndarray,
    edges:list[tuple[int,int]],
    sampler:AerSampler,
    H:SparsePauliOp,
    eps:float = 1e-2
) ->float : 
    
    shift = np.zeros_like(params)
    shift[i] = eps

    qc_p = qaoa_circuit(params+shift,edges)
    counts_p = sampler.run(qc_p).result().quasi_dists[0]
    E_p = expectation(counts_p,H)

    qc_n = qaoa_circuit(params-shift,edges)
    counts_n = sampler.run(qc_n).result().quasi_dists[0]
    E_n = expectation(counts_n,H)

    return (E_p - E_n) / (2*eps)

if __name__ == "__main__":

    edges = [(0,1),(1,2),(0,2),()]
    H = max_cut_hamiltonian(edges,n=3)
    sampler = AerSampler(
        backend_options={"method":"density_matrix"},
        run_options={"shots":2048}
    )

    n_steps = 50
    lr = 0.05
    eps = 1e-2
    params = np.array([0.8,0.4])
    history = []

    for step in range(n_steps):

        i = np.random.randint(len(params))

        grad_i = finite_diff_grad(i,params,edges,sampler,H,eps)

        params[i]+= lr*grad_i

        qc = qaoa_circuit(params,edges)
        counts = sampler.run(qc).result().quasi_dists[0]
        history.append(expectation(counts,H))
    
    
    plt.plot(history, marker='o')
    plt.xlabel("Iteration")
    plt.ylabel("⟨Cost⟩")
    plt.title("3-qubit Max-Cut: Coord-Descent FD (2 calls/step)")
    plt.show()

    