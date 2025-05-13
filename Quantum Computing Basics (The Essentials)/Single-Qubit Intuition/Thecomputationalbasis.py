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
