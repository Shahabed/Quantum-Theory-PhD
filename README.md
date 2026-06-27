# Quantum light-driven many-level systems

Python simulations from my Ph.D. thesis at TU Berlin (2018).

> *"Quantum light-driven many-level systems in the weak and strong coupling limits"*  
> Supervisors: Prof. Andreas Knorr · Dr. Thomas Koprucki, TU Berlin

---

## What this is about

Two quantum systems — a **source** and a **target** — are coupled through a unidirectional waveguide. The source is driven (coherently or incoherently via spontaneous emission) and emits quantum light that excites the target. The target is a two- or four-level emitter sitting inside a cavity.

The central question: *how does quantum light transfer through this cascaded system, and what photon statistics does the target produce?*

The answer depends heavily on whether the cavities are in the **weak** or **strong coupling** regime — and that's what the thesis explores numerically.

---

## Physics

The simulations are built on three pillars:

**Open quantum systems** — the system interacts with its environment (the electromagnetic vacuum). This is handled via the Lindblad master equation for the density matrix:

$$\dot{\rho} = -\frac{i}{\hbar}[H, \rho] + \sum_k \left( L_k \rho L_k^\dagger - \frac{1}{2}\{L_k^\dagger L_k, \rho\} \right)$$

**Cascaded formalism** — the output field of the source becomes the input of the target. This is modelled using the Gardiner-Carmichael cascaded quantum systems approach, which extends the Lindblad framework to directed (non-reciprocal) coupling.

**Jaynes-Cummings model** — each cavity is modelled as a single quantized field mode coupled to a two- or four-level atom, the foundational model of cavity QED.

---

## Key results

- Photon statistics of the target can be controlled via the source pumping mechanism
- Different coupling regimes (weak vs. strong) in both cavities significantly alter the target output
- Tuning cavity parameters can produce exotic quasi-probability distributions — including flat Fock state distributions
- Higher-order correlation functions (g², g³) of the target deviate strongly from those of the source, showing mixed coherent/incoherent dynamics

---

## Repository structure

```
src/
  cascaded_system.py     # Core cascaded master equation solver
  lindblad.py            # Lindblad operator construction and time evolution
  jaynes_cummings.py     # Jaynes-Cummings Hamiltonian (2- and 4-level)
  photon_statistics.py   # g²(τ) and photon number distribution computation
  utils.py               # Density matrix helpers, partial trace, expect. values

notebooks/
  01_weak_coupling.ipynb         # Two coupled cavities, weak coupling regime
  02_strong_coupling.ipynb       # Strong coupling — Rabi splitting, dressed states
  03_photon_statistics.ipynb     # g²(0), Fock distributions, Wigner functions
  04_four_level_emitter.ipynb    # Four-level target system results

results/
  figures/               # Output plots from the notebooks

docs/
  thesis_abstract.md     # Summary of the thesis in plain language
```

---

## Stack

- `Python 3` · `NumPy` · `SciPy` (ODE solvers, sparse matrices) · `Matplotlib`
- [`QuTiP`](http://qutip.org/) — Quantum Toolbox in Python, used for density matrix evolution and operator algebra

---

## Reference

Chatraee Azizabadi, S. (2018). *Quantum light-driven many-level systems in the weak and strong coupling limits.* Ph.D. thesis, Technische Universität Berlin.  
→ [TU Berlin repository](https://depositonce.tu-berlin.de/items/9218e477-b112-49e7-889f-44d0d24a8646)
