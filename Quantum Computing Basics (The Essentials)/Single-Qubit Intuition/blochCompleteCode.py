import numpy as np
import matplotlib.pyplot as plt

try:
    from qiskit.visualization import plot_bloch_vector
    HAS_QISKIT = True
except ImportError:
    HAS_QISKIT = False
    print("⚠️  Qiskit not found; will compute Bloch coords but skip plotting.")



def strip_global_phase(alpha:complex,beta:complex):
    phase0 = np.angle(alpha)
    a = alpha * np.exp(-1j * phase0)
    b = beta * np.exp(-1j * phase0)

    if a.real < 0 and abs(a.imag) < 1e-8:
        a, b = -a, -b
    
    return a,b

def state_to_bloch(alpha:complex,beta:complex):
    a,b = strip_global_phase(alpha,beta)

    norm = np.linalg.norm([a, b])
    a /= norm
    b /= norm
    theta = 2*np.arccos(a.real)
    phi = np.angle(b)

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    return theta,phi,[x,y,z]

def plot_state(alpha:complex,beta:complex,title: str=""):
    theta,phi,vec = state_to_bloch(alpha,beta)

    if HAS_QISKIT:
        fig = plot_bloch_vector(vec)
        plt.show()

    print(f"{title}")
    print(f"  θ = {np.degrees(theta):.1f}°, φ = {np.degrees(phi):.1f}°")
    print(f"  Bloch vector = {vec}\n")

    return theta,phi,vec

if __name__ == "__main__":
     tests = [
        (0.3 + 0.4j,          0.7 - 0.1j,     "|ψ⟩ = (0.3 + 0.4i, 0.7 – 0.1i)"),
        (np.exp(1j*np.pi/5)/np.sqrt(2), 
                             np.exp(-1j*np.pi/5)/np.sqrt(2),
                                             "|ψ⟩ = (e^{iπ/5}/√2, e^{-iπ/5}/√2)")
     ]
     for alpha,beta,title in tests:
         plot_state(alpha,beta,title)