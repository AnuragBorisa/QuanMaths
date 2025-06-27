#  bring imports , write the function for making HC , write funtion for initial paramerets , write the funtion which runs the QAOA circuit
# write the main function , collect the eval and its engery in the history object of the callback function of QAOA . And then plot , use 
# use max_eval = 50 for fair estimate between SPSA , COBYLA 

import numpy as np
import matplotlib.pyplot as plt

from qiskit_aer import Aer 
from qiskit.quantum_info import SparsePauliOp
from qiskit_aer.primitives import Sampler as AerSampler
from qiskit_aer.noise import NoiseModel,depolarizing_error
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA,SPSA

def max_cut_hamiltonian(edges:list[tuple[int,int]],n)->SparsePauliOp:
    terms:list[tuple[int,int]] = []
    for i,j in edges:
        lables = ['I']*n
        lables[i] = lables[j] = 'Z'
        pauli_str = ''.join(lables[::-1])
        terms.append((pauli_str,-0.5))
    
    const = 0.5 * len(edges)
    terms.append(('I'*n,const))
    return SparsePauliOp.from_list(terms)

def init_para(p:int,d_gamma:float=0.1,d_beta:float=0.1)->np.ndarray:
    gammas = [k*d_gamma for k in range(1,p+1)]
    betas = [(p-k+1)*d_beta for k in range(1,p+1)]
    return np.array(gammas+betas)

noise_model = NoiseModel()

single_qubit_error = depolarizing_error(0.01,1)
noise_model.add_all_qubit_quantum_error(
    single_qubit_error,
    ["u1", "u2", "u3", "h", "x", "y", "z"]
)
two_qubit_error = depolarizing_error(0.01,2)
noise_model.add_all_qubit_quantum_error(
    two_qubit_error,
    ['cx']
)

# sampler_options = {
#     "method" : "density_matrix",
#     "noise_model": noise_model,
#     "shots" : 1024
# }

def run_QAOA(
        edges:list[tuple[int,int]],
        n:int , p:int , init_pt:np.ndarray,
        optimser,method:str,max_evals:int=50
)->float:
    H = max_cut_hamiltonian(edges=edges,n=n)
    Hc = -1 * H

    best_cut = -np.inf
    evals = 0

    history = {'eval':[],'engery':[]}
    def callback(eval_count,params,energy,metadata):
        nonlocal best_cut,evals
        evals+=1
        cut = -energy
        if cut > best_cut:
            best_cut = cut
        if evals >=max_evals:
            raise StopIteration
        
    
    sampler = AerSampler(
    
    backend_options={
        "method":      "density_matrix", 
        "noise_model": noise_model
    },
    
    run_options={
        "shots": 1024
    }
)

    qaoa = QAOA(
        sampler=sampler,
        optimizer=optimser,
        reps=p,
        initial_point=init_pt,
        callback=callback
    )

    try:
        _=qaoa.compute_minimum_eigenvalue(operator=H)
    except StopIteration:
        pass
    print(f"{method:6s} → best cut ≈ {best_cut:.4f}")
    return best_cut

if __name__ == "__main__":

    edges = [(0,1),(1,2),(0,2),(2,3)]
    n , p = 4,1

    init_pt = init_para(p)

    cobyla = COBYLA(maxiter=100)
    spsa = SPSA(maxiter=100)

    best_cobyla = run_QAOA(edges,n,p,init_pt,cobyla,"COBYLA")
    best_spsa = run_QAOA(edges,n,p,init_pt,spsa,"SPSA")

    labels = ["COBYLA", "SPSA"]
    values = [best_cobyla, best_spsa]

    plt.bar(labels, values, color=['C0','C1'])
    plt.ylabel("Best cut size after 50 evals")
    plt.title("Day 4: Noisy QAOA optimizer comparison (1% depolarizing)")
    # plt.ylim(0, len(edges))
    plt.show()



        


