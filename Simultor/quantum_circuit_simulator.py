"""
quantum_circuit_simulator.py

A simple quantum circuit simulator in Python.
Demonstrates:
- Single-qubit superposition using Hadamard gate
- Two-qubit entanglement (Bell state) using H and CNOT gates
- Measurement of quantum states
"""

import numpy as np
from collections import Counter

# Define single-qubit basis states
zero = np.array([1, 0], dtype=complex)
one  = np.array([0, 1], dtype=complex)

# Define common gates
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)
S = np.array([[1, 0], [0, 1j]], dtype=complex)

# Apply a single-qubit gate on a multi-qubit state
def apply_gate(state, gate, qubit, num_qubits):
    I = np.eye(2, dtype=complex)
    ops = [gate if i == qubit else I for i in range(num_qubits)]
    full_op = ops[0]
    for op in ops[1:]:
        full_op = np.kron(full_op, op)
    return full_op @ state

# Apply a CNOT gate between control and target qubits
def apply_cnot(state, control, target, num_qubits):
    dim = 2 ** num_qubits
    new_state = np.zeros(dim, dtype=complex)
    for i in range(dim):
        bits = list(format(i, f'0{num_qubits}b'))
        if bits[control] == '1':
            bits[target] = '1' if bits[target] == '0' else '0'
            j = int(''.join(bits), 2)
        else:
            j = i
        new_state[j] += state[i]
    return new_state

# Measure the state with given number of shots
def measure(state, num_qubits, shots=1024):
    probs = np.abs(state) ** 2
    outcomes = []
    for _ in range(shots):
        r = np.random.rand()
        cumulative = 0
        for idx, p in enumerate(probs):
            cumulative += p
            if r < cumulative:
                outcomes.append(format(idx, f'0{num_qubits}b'))
                break
    return Counter(outcomes)

# Print probability of each basis state
def print_state_probs(state, num_qubits):
    probs = np.abs(state) ** 2
    for idx, p in enumerate(probs):
        print(f"|{format(idx, f'0{num_qubits}b')}>: {p:.3f}")

if __name__ == "__main__":
    # Single-qubit superposition
    print("Single-qubit superposition:")
    psi = zero.copy()  # start in |0>
    psi = apply_gate(psi, H, 0, 1)
    print_state_probs(psi, 1)

    # Two-qubit entanglement (Bell state)
    print("\nTwo-qubit Bell state:")
    phi = np.kron(zero, zero)  # start in |00>
    phi = apply_gate(phi, H, 0, 2)
    phi = apply_cnot(phi, 0, 1, 2)
    print_state_probs(phi, 2)

    # Simulated measurement
    print("\nMeasurement (1000 shots) of Bell state:")
    counts = measure(phi, 2, shots=1000)
    print(counts)
