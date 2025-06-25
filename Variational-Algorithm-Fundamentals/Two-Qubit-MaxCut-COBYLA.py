from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import minimize
from qiskit.circuit.library import RZZGate

sim = AerSimulator()
shots = 2000
last_score = None

def cost_layer(circuit:QuantumCircuit,gamma:float,q0:int=0,q1:int=1) -> QuantumCircuit:
    circuit.append(RZZGate(2*gamma),[q0,q1])
    return circuit

def mixer(circuit:QuantumCircuit,beta:float,qubits=[0,1])->QuantumCircuit:
    for q in qubits:
        circuit.rx(beta,q)
    return circuit

def qaoa_circuit(gamma:float,beta:float)->QuantumCircuit:
    qc = QuantumCircuit(2,2)
    qc.h([0,1])
    cost_layer(qc,gamma,q0=0,q1=1)
    mixer(qc,beta,qubits=[0,1])
    qc.measure([0,1],[0,1])
    return qc

def max_cut_score(counts:dict[str,int])->float:
    good = counts.get('01',0)+counts.get('10',0)
    return good/shots

def objective(angles:np.ndarray) -> float :
    global last_score 
    gamma ,beta = angles
    qc = qaoa_circuit(gamma=gamma,beta=beta)
    qc_t = transpile(qc,sim)
    job = sim.run(qc_t,shots=shots)
    counts = job.result().get_counts()
    score = max_cut_score(counts)
    last_score = score 
    return -score 


history = {'gamma':[],'beta':[],'score':[]}

def callback(iteration_angles):
    gamma_iteration ,beta_iteration = iteration_angles
    history['gamma'].append(gamma_iteration)
    history['beta'].append(beta_iteration)
    history['score'].append(last_score)
    

x0 = np.array([np.pi/4,np.pi/4])

cons = [
    {'type':'ineq','fun':lambda x: x[0] },
    {'type':'ineq','fun':lambda x: np.pi - x[0] },
    {'type':'ineq','fun':lambda x: x[1]},
    {'type':'ineq','fun':lambda x: np.pi - x[1] },
]

res = minimize(
    objective,
    x0,
    method='COBYLA',
    constraints=cons,
    callback=callback,
    options={'maxiter':50,'tol':1e-3}
)

best_gamma ,best_beta = res.x
best_score = -res.fun

print(f"\n🛠️  Optimizer result: gamma*={best_gamma:.3f}, gamma*={best_beta:.3f}, score={best_score:.4f}")

its = np.arange(len(history['score']))
plt.plot(its, history['score'], marker='o')
plt.xlabel('COBYLA iteration')
plt.ylabel('Avg. Max-Cut score')
plt.title(' COBYLA optimization trajectory')
plt.tight_layout()
plt.show()