import numpy as np
from qiskit.visualization import plot_bloch_vector

plot_bloch_vector([0,0,1],title="|0⟩ — north pole")
plot_bloch_vector([0,0,-1],title="|1⟩ — south pole")
plot_bloch_vector([1,0,0],title="|+⟩ — +X eigenstate")

theta = np.deg2rad(60)
phi = np.deg2rad(45)
vec = [np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)]
plot_bloch_vector(vec,title="θ=60°, φ=45° state")
