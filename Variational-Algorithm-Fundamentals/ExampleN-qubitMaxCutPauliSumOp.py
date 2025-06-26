from qiskit.quantum_info import SparsePauliOp

def maxcut_hamiltonian(edges,n):
    terms = []

    for i,j in edges:
        label = ['I'] * n

        label[i] = 'Z'
        label[j] = 'Z'

        pauli_str = ''.join(label[::-1])
        terms.append((pauli_str,-0.5))
    
    const = 0.5 * len(edges)
    terms.append(('I' * n,const))

    H_C = SparsePauliOp.from_list(terms)
    return H_C;



