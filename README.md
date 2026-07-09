# Quantum-Theory-PhD

**Numerical Simulations of Quantum Light-Matter Interaction in Coupled Cavity Systems**

This repository contains the numerical simulation code developed during my PhD research on open quantum systems in cavity quantum electrodynamics (cavity QED). The work focuses on **coupled optical cavities** interacting with multi-level quantum emitters under incoherent driving, exploring both weak and strong light-matter coupling regimes.

---

## Thesis Information

**Title:** Quantum light driven many level systems in the weak and strong coupling limits  
**Author:** Shahabed Chatraee Azizabadi  
**Institution:** Technische Universität Berlin  
**Year:** 2017  
**Thesis Link:** [TU Berlin DepositOnce](https://depositonce.tu-berlin.de/items/9218e477-b112-49e7-889f-44d0d24a8646)

---

## Research Overview

This project investigates **open quantum systems** consisting of coupled cavity-emitter systems driven by incoherent light. The central setup involves a **source cavity** that is incoherently pumped and coupled to a **target cavity** containing one or more two-level quantum emitters (atoms or excitons).

### Core Scientific Questions

- How can the photon statistics and quantum properties of a target system be controlled through the pumping of a source cavity?
- What are the differences between **atomic** and **excitonic** light-matter coupling models in open systems?
- How do **indirect** (cavity-mediated) and **direct** coupling mechanisms affect steady-state behavior and entanglement?
- Under which conditions can entanglement be generated and controlled in dissipatively coupled systems?

---

## Physical Systems Studied

The simulations cover several configurations:

1. **Single driven cavity** with a two-level emitter (source only)
2. **Coupled source-target cavities** with one emitter in the target
3. **Multi-emitter systems** (two or three emitters in the target cavity)
4. **Comparison between atomic and excitonic models**

Two main coupling paradigms were analyzed:
- **Atomic model**: Standard Jaynes-Cummings interaction
- **Excitonic model**: Modified coupling with different dissipation channels

---

## Methodology and Numerical Approach

### Theoretical Framework
- **Jaynes-Cummings Hamiltonian** for cavity-emitter interaction
- **Lindblad master equation** for open quantum system dynamics
- **Steady-state solutions** of the Liouvillian superoperator

### Numerical Implementation
- **QuTiP** (Quantum Toolbox in Python) for all simulations
- Tensor product construction of multi-partite Hilbert spaces
- Efficient steady-state solvers (`steadystate`)
- Parameter sweeps over pump rates, coupling strengths, and decay rates

### Key Observables Computed
- Average photon number: ⟨n⟩ = ⟨a†a⟩
- Second-order correlation function: g²(0)
- Wigner function of the cavity field
- **Concurrence** (two-qubit entanglement)
- **Von Neumann entropy** (mixedness and entanglement)
- Photon number distributions and Fock state populations

---

## Key Results

### 1. Control of Target Photon Statistics
The photon statistics of the target cavity (thermal, coherent, or antibunched) can be influenced by the incoherent pumping applied to the source cavity. Increasing the source pump rate can drive the target system across different statistical regimes.

### 2. Atomic vs Excitonic Coupling
Significant qualitative and quantitative differences were found between atomic and excitonic models, particularly in:
- Steady-state photon occupation
- Photon blockade and bunching behavior
- Entanglement generation between emitters

### 3. Indirect vs Direct Coupling
Cavity-mediated (indirect) coupling and direct dipole-dipole coupling lead to different steady-state properties. Indirect coupling can generate entanglement even under strong dissipation.

### 4. Entanglement in Open Systems
Using concurrence and von Neumann entropy, optimal parameter regimes for entanglement generation were identified. Entanglement depends critically on the pump rate, detuning, and the ratio of coupling to decay rates (g/κ).

### 5. Non-Classical Light Generation
Wigner function analysis revealed non-classical features (negative regions) under specific driving conditions, indicating the generation of non-classical states of light.

### 6. Multi-Emitter Systems
Systems with two and three emitters were studied, revealing collective effects and modified scaling of photon correlations and entanglement with emitter number.

---

## Repository Structure

```bash
Quantum-Theory-PhD/
├── src/
│   └── simulations/
│       ├── source_cavity/           # Single driven cavity simulations
│       ├── coupled_cavities/        # Source-target cavity systems
│       └── main_analysis/           # Multi-emitter and advanced analysis
├── notebooks/
│   └── analysis.ipynb               # Main analysis and visualizations
├── data/
│   └── results/                     # Saved simulation data (.qu files)
├── reports/
│   └── key_results.txt              # Technical summary of findings
├── README.md
├── requirements.txt
└── LICENSE
