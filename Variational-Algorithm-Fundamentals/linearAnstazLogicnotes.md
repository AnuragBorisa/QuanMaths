## Linear-Ansatz Initialization for QAOA

**Goal:**  
Provide a smooth “ramp” from pure mixing to pure cost, mimicking an adiabatic schedule.

---

### Formula

For QAOA depth \(p\), layer index \(k=1,2,\dots,p\), and chosen step‐sizes \(\Delta_\gamma,\Delta_\beta>0\):

\[
\begin{aligned}
\gamma_k &= k \times \Delta_\gamma,\\
\beta_k  &= (p - k + 1)\times \Delta_\beta.
\end{aligned}
\]

- \(\gamma_1 = 1\cdot\Delta_\gamma,\;\beta_1 = p\cdot\Delta_\beta\)  
- \(\gamma_p = p\cdot\Delta_\gamma,\;\beta_p = 1\cdot\Delta_\beta\)

---

### Intuition & Logic

1. **Adiabatic Inspiration**  
   - In continuous adiabatic algorithms, one slowly shifts the Hamiltonian from  
     \[
       H(0)=H_M \quad\longrightarrow\quad H(1)=H_C
     \]  
     over “time” \(s\in[0,1]\).  
   - Discretizing into \(p\) steps with \(s_k = k/p\) leads to gradually increasing cost‐phase weight and decreasing mixer‐weight.

2. **Early Layers (\(k\) small)**  
   - **Small \(\gamma_k\)**: the cost‐phase \(e^{-i\gamma_k H_C}\) barely biases toward any cut.  
   - **Large \(\beta_k\)**: the mixer \(e^{-i\beta_k H_M}\) strongly shuffles amplitudes, keeping the state highly exploratory.

3. **Late Layers (\(k\) large)**  
   - **Large \(\gamma_k\)**: cost‐phase dominates, locking in high‐quality cuts.  
   - **Small \(\beta_k\)**: mixing is dialed down, so the algorithm “settles” into a good solution.

---

### Practical Tips

- **Choosing \(\Delta_\gamma,\Delta_\beta\):**  
  - Common starting values:  
    \(\Delta_\gamma \approx 0.1,\;\Delta_\beta \approx 0.2\)  
  - You can sweep them (grid search) to find the best performance on your problem.

- **Experiment with depth \(p\):**  
  - Shallow (\(p=1\!-\!2\)) is faster but less expressive.  
  - Deeper (\(p>3\)) can approximate the ground state better, at the cost of more gates and harder classical optimization.

---

**Summary:**  
The linear-ansatz gives you a principled, “adiabatic-inspired” start: early layers explore broadly, and later layers focus on refining the solution.```
