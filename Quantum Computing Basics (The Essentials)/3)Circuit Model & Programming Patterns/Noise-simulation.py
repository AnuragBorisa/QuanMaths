from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel , depolarizing_error

shots = 2048
p = 0.10

qc_ideal = QuantumCircuit(1,1)
qc_ideal.h(0)
qc_ideal.measure(0,0)

qc_noisy = QuantumCircuit(1,1)
qc_noisy.h(0)
qc_noisy.h(0)
# why two h because if there were no noise, two Hadamards in a row do nothing so you’d get back ket0 every time. But in our noisy simulation you’ve attached depolarizing noise after each H gate. So the real sequence is: ket0 to ket+ through h a noise kicks in and now its not pure ket+ so then when you apply the second h it takes that mixed ket+ to z basis so now you dont ket ket0 but a mix ket0+ket1
qc_noisy.measure(0,0)

noise_model = NoiseModel()
single_error = depolarizing_error(p,1)

noise_model.add_all_qubit_quantum_error(single_error,['h'])

sim_ideal = AerSimulator()
sim_noisy = AerSimulator(noise_model=noise_model,method='density_matrix')

tqc_ideal = transpile(qc_ideal,sim_ideal)
result_ideal = sim_ideal.run(tqc_ideal,shots=shots).result()
counts_ideal = result_ideal.get_counts()

tqc_noisy = transpile(
    qc_noisy,
    sim_noisy,
    optimization_level=0,      # turn off gate cancellation
    basis_gates=noise_model.basis_gates 
)
result_noisy = sim_noisy.run(tqc_noisy, shots=shots).result()
counts_noisy = result_noisy.get_counts()

print("Ideal counts:", counts_ideal)
print("Noisy counts:", counts_noisy)


# the above circuit will produce error after every H so to do have only one error account you have to do like this . 

# # 
# p = 0.10
# error = depolarizing_error(p, 1)        # a QuantumError
# kraus_inst = error.to_instruction()  
# shots = 2048

# qc_noisy_once = QuantumCircuit(1, 1)
# qc_noisy_once.h(0)                  # 1) prepare |+>
# qc_noisy_once.append(kraus_inst, [0], [])  # 2) inject depolarizing noise here
# qc_noisy_once.h(0)                  # 3) second H, no noise this time
# qc_noisy_once.measure(0, 0)

# sim = AerSimulator(method='density_matrix')
# tqc = transpile(qc_noisy_once, sim)
# result = sim.run(tqc, shots=shots).result()
# counts = result.get_counts()
# print("Counts with noise only after the first H:", counts)