# Thesis summary 

**Title:** Quantum light-driven many-level systems in the weak and strong coupling limits  
**Institution:** Technische Universität Berlin, 2018  
**Full text:** [TU Berlin repository](https://depositonce.tu-berlin.de/items/9218e477-b112-49e7-889f-44d0d24a8646)

---

## The core question

Imagine two boxes (cavities), each containing a tiny atom. They are connected by a very thin optical wire — a waveguide — that only carries light in one direction: from the source cavity to the target. If I shine light into the source and drive it, what kind of light comes out of the target? And how does that depend on how tightly the light and atom are coupled inside each cavity?

This thesis answers that question numerically, by simulating the full quantum mechanical system.

## Why it's hard

Quantum light is not classical light. Its photon statistics — whether photons arrive bunched together, independently, or one at a time — carry information that has no classical analogue. Transferring this quantum light through a cascaded system disturbs the statistics in ways that depend strongly on the coupling regime of each cavity.

In the **weak coupling** regime, the cavity damps light faster than the atom and cavity can exchange energy. In the **strong coupling** regime, the atom and cavity field are so tightly coupled that they form hybrid states (dressed states / polaritons) with a characteristic Rabi splitting in the spectrum.

The cascaded formalism (Gardiner 1993, Carmichael 1993) provides the mathematical framework to handle the directed, non-reciprocal coupling between the two cavities within the Lindblad master equation.

## What we found

- The photon statistics of the target can be controlled by how the source is pumped (coherent vs. incoherent driving)
- Strong vs. weak coupling in either cavity strongly alters the output photon number distribution and higher-order correlation functions
- Tuning the cavity parameters can produce flat Fock state distributions — an exotic quasi-probability distribution without a classical analogue
- Higher-order correlation functions g²(τ) and g³ of the target diverge strongly from those of the source, showing a mixture of coherent and incoherent quantum dynamics

## Methods used

| Method | Purpose |
|---|---|
| Lindblad master equation | Time evolution of the open quantum system density matrix |
| Cascaded quantum systems formalism | Unidirectional source → target coupling |
| Jaynes-Cummings model | Cavity QED: atom + quantised field mode |
| Quantum regression theorem | Computing two-time correlation functions g²(τ) |
| Fock space truncation | Numerical representation of the cavity field |

## Code

The Python simulations use `NumPy`, `SciPy`, and `QuTiP`. Core modules:

- `lindblad.py` — Liouvillian construction and density matrix time evolution
- `jaynes_cummings.py` — Hamiltonian and collapse operators for a cavity-atom system
- `cascaded_system.py` — Full source-target cascaded master equation
- `photon_statistics.py` — g²(0), g²(τ), photon number distributions, Mandel Q
