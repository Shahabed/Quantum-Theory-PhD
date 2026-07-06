#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Source Cavity - Jaynes-Cummings model with incoherent pumping
Quantum Optics simulations using QuTiP.
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import (tensor, destroy, qeye, steadystate, spectrum,
                   correlation_ss, spectrum_correlation_fft, expect)

# ============================= PARAMETERS =============================
N = 15                    # Number of Fock states for cavity
wc = 1.0 * 2 * np.pi      # Cavity frequency
wa = 1.0 * 2 * np.pi      # Atom frequency
n_th_a = 0.0              # Thermal photons

# ============================= CORE FUNCTIONS =============================

def jaynes_cummings_hamiltonian(g, detuning=0.0):
    """Return Jaynes-Cummings Hamiltonian."""
    a = tensor(destroy(N), qeye(2))
    sm = tensor(qeye(N), destroy(2))
    H = wc * a.dag() * a + wa * sm.dag() * sm + g * (a.dag() * sm + a * sm.dag())
    if detuning != 0:
        H += detuning * sm.dag() * sm
    return H, a, sm


def collapse_operators(kappa, gamma, Gamma):
    """Return list of collapse operators."""
    a = tensor(destroy(N), qeye(2))
    sm = tensor(qeye(N), destroy(2))
    c_ops = []

    # Cavity decay
    rate = kappa * (1 + n_th_a)
    if rate > 0:
        c_ops.append(np.sqrt(rate) * a)
    rate = kappa * n_th_a
    if rate > 0:
        c_ops.append(np.sqrt(rate) * a.dag())

    # Atom decay and pumping
    if gamma > 0:
        c_ops.append(np.sqrt(gamma) * sm)
    if Gamma > 0:
        c_ops.append(np.sqrt(Gamma) * sm.dag())

    return c_ops


def calculate_spectrum(g, kappa, gamma, Gamma, wlist=None):
    """Calculate power spectrum."""
    if wlist is None:
        wlist = np.linspace(-6, 6, 500) * 2 * np.pi

    H, a, _ = jaynes_cummings_hamiltonian(g)
    c_ops = collapse_operators(kappa, gamma, Gamma)

    spec = spectrum(H, wlist, c_ops, a.dag(), a)
    return wlist / (2 * np.pi), spec


def calculate_photon_statistics(g, kappa, gamma, Gamma):
    """Steady-state photon number and g2(0)."""
    H, a, _ = jaynes_cummings_hamiltonian(g)
    c_ops = collapse_operators(kappa, gamma, Gamma)

    rho_ss = steadystate(H, c_ops)
    n_cavity = expect(a.dag() * a, rho_ss)
    g2 = expect(a.dag() * a.dag() * a * a, rho_ss) / (n_cavity ** 2) if n_cavity > 0 else 0

    return n_cavity, g2


def plot_spectrum_vs_pump(Gamma_vec, g=0.1, kappa=0.4, gamma=0.02):
    """Plot spectrum for different pump rates."""
    # Implementation can be added here
    pass


# ============================= EXAMPLE RUNS =============================
def run_examples():
    """Run standard examples."""
    print("Running source cavity examples...")

    # Example 1: Spectrum
    wlist, spec = calculate_spectrum(g=0.1, kappa=0.4, gamma=0.0, Gamma=0.1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(wlist, spec, 'b-', lw=2)
    plt.xlabel('Frequency')
    plt.ylabel('Power spectrum')
    plt.title('Source Cavity Spectrum')
    plt.grid(True)
    plt.savefig('results/source_spectrum_example.pdf')
    plt.close()

    # Example 2: Photon statistics vs pump rate
    Gamma_vec = np.logspace(-3, 1, 200)
    n_vec = []
    g2_vec = []

    for Gamma in Gamma_vec:
        n, g2 = calculate_photon_statistics(g=3.0, kappa=0.1, gamma=0.02, Gamma=Gamma)
        n_vec.append(n)
        g2_vec.append(g2)

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].plot(Gamma_vec, n_vec, 'b-')
    axs[0].set_xlabel(r'$\Gamma_p$')
    axs[0].set_ylabel(r'$\langle n \rangle$')
    axs[0].set_xscale('log')

    axs[1].plot(Gamma_vec, g2_vec, 'b-')
    axs[1].set_xlabel(r'$\Gamma_p$')
    axs[1].set_ylabel(r'$g^{(2)}(0)$')
    axs[1].set_xscale('log')
    plt.tight_layout()
    plt.savefig('results/source_photon_statistics.pdf')
    plt.close()

    print("Plots saved in results/ folder.")


if __name__ == "__main__":
    run_examples()
