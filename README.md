# Quantum-Theory-PhD

**Numerical Simulations of Quantum Light-Matter Interaction in Coupled Cavity Systems**

This repository contains the core simulation code developed during my Ph.D. research at TU Berlin on **open quantum systems** in cavity quantum electrodynamics (cavity QED).

> **Thesis:** *Quantum light-driven many-level systems in the weak and strong coupling limits*  
> **Author:** Shahabed Chatraee Azizabadi  
> **Supervisors:** Prof. Andreas Knorr · Dr. Thomas Koprucki  
> **Year:** 2018  
> **[Full Thesis (TU Berlin)](https://depositonce.tu-berlin.de/items/9218e477-b112-49e7-889f-44d0d24a8646)**

---

## Research Overview

The project studies **cascaded quantum systems** in which a **source** cavity, driven by incoherent or coherent light, emits quantum light that excites a **target** system consisting of a cavity containing a two- or four-level emitter.

The central scientific question is:

> *How does quantum light propagate through this cascaded system, and what photon statistics and quantum correlations does the target produce?*

The answer depends strongly on whether the cavities operate in the **weak** or **strong coupling** regime.

---

## Theoretical Framework

The simulations are built on three main pillars:

### 1. Open Quantum Systems
The system interacts with its environment (electromagnetic vacuum). This is described using the **Lindblad master equation**:

$$
\dot{\rho} = -\frac{i}{\hbar}[H, \rho] + \sum_k \left( L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\} \right)
$$

### 2. Cascaded Quantum Systems
The output field of the source becomes the input of the target. This directed (non-reciprocal) coupling is modeled using the **Gardiner-Carmichael cascaded systems** formalism.

### 3. Jaynes-Cummings Model
Each cavity is described as a quantized field mode coupled to a two- or four-level emitter — the foundational model of cavity QED.

---

## Key Results

- The **photon statistics** of the target system can be controlled via the pumping mechanism of the source.
- Weak vs. strong coupling in both cavities significantly changes the target output (thermal → antibunched light, modified g²(0), g³(0)).
- Tuning cavity parameters can produce exotic quasi-probability distributions, including nearly flat Fock-state distributions.
- Higher-order correlation functions of the target deviate strongly from those of the source, revealing mixed coherent/incoherent dynamics.
- Entanglement between emitters in the target cavity can be generated and controlled through cavity-mediated coupling.

---

## Repository Structure

```bash
Quantum-Theory-PhD/
├── src/
│   ├── cascaded_system.py       # Core cascaded master equation solver
│   ├── lindblad.py              # Lindblad operator construction
│   ├── jaynes_cummings.py       # Jaynes-Cummings Hamiltonian (2- and 4-level)
│   ├── photon_statistics.py     # g²(τ), photon number distributions
│   └── utils.py                 # Density matrix helpers, partial trace, expectation values
├── notebooks/
│   ├── 01_weak_coupling.ipynb
│   ├── 02_strong_coupling.ipynb
│   ├── 03_photon_statistics.ipynb
│   └── 04_four_level_emitter.ipynb
├── results/
│   └── figures/                 # Output plots
├── docs/
│   └── thesis_abstract.md
├── README.md
├── requirements.txt
└── LICENSE


## Technologies

- **Python 3**
- **[QuTiP](http://qutip.org/)** (Quantum Toolbox in Python) — used for density matrix evolution and operator algebra
- **NumPy / SciPy** — ODE solvers and sparse matrix operations
- **Matplotlib** — visualization and plotting

## Skills Demonstrated

- Numerical simulation of open quantum systems
- Master equation and Lindblad formalism
- Tensor-product Hilbert spaces and multi-partite quantum systems
- Calculation of photon correlation functions and entanglement measures
- Scientific Python development and data visualization

## How to Use

```bash
pip install -r requirements.txt
jupyter notebook notebooks/

## Reference

Chatraee Azizabadi, S. (2018). *Quantum light-driven many-level systems in the weak and strong coupling limits.* Ph.D. thesis, Technische Universität Berlin.

> **Note:** This repository contains research code from my Ph.D. work. While it has been reorganized for clarity, it reflects the iterative nature of scientific research. For the complete theoretical framework and results, please refer to the thesis linked above.
