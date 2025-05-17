import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_vector

# vectors = [
#     ([0,0,1], "|0⟩ — north pole"),
#     ([0,0,-1], "|1⟩ — south pole"),
#     ([1,0,0], "|+⟩ — +X eigenstate"),
# ]
# theta = np.deg2rad(60)
# phi   = np.deg2rad(45)
# vectors.append((
#     [np.sin(theta)*np.cos(phi),
#      np.sin(theta)*np.sin(phi),
#      np.cos(theta)],
#     "θ=60°, φ=45°"
# ))

# for vec, title in vectors:
#     plot_bloch_vector(vec, title=title)
#     plt.show()  # <–– pop up each figure

vectors = [[0,0,1],[np.sqrt(3)/2,0,1/2],[np.sqrt(2)/2,np.sqrt(2)/2,0]]

for vec in vectors:
    plot_bloch_vector(vec)
    plt.show()


