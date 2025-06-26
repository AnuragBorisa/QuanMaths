import numpy as np
import matplotlib.pyplot as plt 

from qiskit_aer import Aer
from qiskit.quantum_info import SparsePauliOp
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms.minimum_eigensolvers import MinimumEigensolver
from qiskit_aer.primitives import Sampler as AerSampler


def max_cut_hamiltonian(edges:list[tuple[int,int]],n:int)->SparsePauliOp:
    terms:list[tuple[str,float]] = []
    for i,j in edges:
        label = ['I']*n
        label[i] = 'Z'
        label[j] = 'Z'
        pauli_str = ''.join(label[::-1])
        terms.append((pauli_str,-0.5))
    
    const = 0.5 * len(edges)
    terms.append(('I'*n,const))
    return SparsePauliOp.from_list(terms)


def linear_init(p:int,d_gamma:float=0.1,d_beta:float=0.1)->np.ndarray:
    gammas = [k * d_gamma for k in range(1,p+1)]
    betas = [(p-k+1)*d_beta for k in range(1,p+1)]
    return np.array(gammas+betas)

def random_init(p:int)->np.ndarray:
    return  np.random.uniform(0,np.pi,size=2*p)

def run_QAOA(
        edges:list[tuple[int,int]],
        n:int,
        p:int,
        initial_points:np.ndarray
)->tuple[MinimumEigensolver,dict]:
    
    Hc = max_cut_hamiltonian(edges,n)
    H = -1*Hc

    optimiser = COBYLA(maxiter=100)

    history = {'eval':[],'energy':[]}
    def callback(eval_count,params,energy,metadata):
        history['eval'].append(eval_count)
        history['energy'].append(energy)
    sampler = AerSampler()
    qaoa = QAOA(
        sampler=sampler,
        optimizer=optimiser,
        reps=p,
        initial_point=initial_points,
        callback=callback,
    )

    result =  qaoa.compute_minimum_eigenvalue(operator=H)
    return result,history

if __name__ == "__main__":
    
    edges = [(0,1), (1,2), (0,2)]
    n = 3
    p = 3

    inits = {
        "linear": linear_init(p),
        "random1": random_init(p),
        "random2": random_init(p),
    }

    results = {}
    histories = {}
    for name, init_pt in inits.items():
        res, hist = run_QAOA(edges, n, p, init_pt)
        results[name] = res.eigenvalue
        histories[name] = hist
        print(f"{name:7s} → final energy = {res.eigenvalue:.4f}")
    
    for name, hist in histories.items():
        plt.plot(hist["eval"], hist["energy"], label=name)
    plt.xlabel("Optimizer Evaluations")
    plt.ylabel("⟨H_C⟩")
    plt.title(f"QAOA Convergence (p={p}) on Triangle")
    plt.legend()
    plt.show()


    


     

     
