# represting the single qubit state using ket and bra notation . 

import numpy as np

# |0> and |1> 
zero = np.array([[1],[0]]);
one = np.array([[0],[1]]);

# compute inner product 
print("⟨0|0⟩ =",np.vdot(zero,zero)) 
print("⟨1|1⟩ =",np.vdot(one,one))
print("⟨0|1⟩ =",np.vdot(zero,one))
print("⟨1|0⟩ =",np.vdot(one,zero))

# Compute ⟨ψ∣ψ⟩.
# ∣ψ⟩ =  1/root2 |0⟩ + 1/root2 |1⟩ ,

psi = (zero + one) / np.sqrt(2)

norm = np.vdot(psi,psi)

print("⟨ψ|ψ⟩ =", norm)

phi = (1j*zero + one) / np.sqrt(2)

norm2 = np.vdot(phi,phi)

print("⟨ψ|ψ⟩ =", norm2)

