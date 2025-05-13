# Day 1
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

# orthonormalaity check : 

plus = (zero + one) / np.sqrt(2);
minus = (zero - one) / np.sqrt(2);

inner_plus_plus = np.vdot(plus,plus);
inner_minus_minus = np.vdot(minus,minus);
inner_plus_minus = np.vdot(plus,minus);

print("⟨+|+⟩ =", inner_plus_plus )    
print("⟨-| -⟩ =", inner_minus_minus )  
print("⟨+| -⟩ =", inner_plus_minus )

# Day 2 
def print_statevector(alpha,beta):
     """
    Accepts real alpha, beta.
    Renormalizes so that alpha^2 + beta^2 = 1.
    Prints the resulting statevector [alpha, beta].
    Returns the normalized complex vector.
    """
     norm = np.hypot(alpha,beta)
     if norm == 0:
          raise ValueError("Both alpha and beta are zero; no valid state.")
     a, b = alpha/norm , beta/norm
     psi_new = np.array([a,b],dtype=complex)
     print(f"Normalized statevector: [{a:.4f}, {b:.4f}]ᵀ")
     return psi_new


print_statevector(1, 1)
# Output: Normalized statevector: [0.7071, 0.7071]ᵀ

print_statevector(0.6, 0.8)
# Output: Normalized statevector: [0.6000/1.0000, 0.8000/1.0000]ᵀ → [0.6000, 0.8000]ᵀ