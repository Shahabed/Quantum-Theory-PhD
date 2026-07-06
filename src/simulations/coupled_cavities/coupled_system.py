#!/usr/bin/env python3
"""
Coupled cavity system simulations - one/two atoms or excitons in target.
"""

import numpy as np
import matplotlib.pyplot as plt
from qutip import *

def calculate_steady_state_photon_stats(g1, g2, kappas, kappat, Gamma, Gammat=0.1,
                                      gamma=0.02, n_atoms=1, N1=4, N2=4):
    """Compute <n> and g2(0) for target cavity."""
    # Build operators (simplified - adjust tensor dimensions based on n_atoms)
    a = tensor(destroy(N1), qeye(2), destroy(N2), *[qeye(2)] * n_atoms)
    c = tensor(qeye(N1), qeye(2), qeye(N2), *[qeye(2)] * n_atoms)  # adjust
    # Define sm1 (source), sm_target...
    # ... (full implementation would expand this)

    # Liouvillians for source + target + coupling
    # ... (consolidated from your scripts)

    rho_ss = steadystate(LG)
    n_target = expect(c.dag() * c, rho_ss)
    g2 = expect(c.dag()*c.dag()*c*c, rho_ss) / (n_target**2) if n_target > 0 else 0
    return n_target, g2


def calculate_spectrum(g1, g2, kappas, kappat, Gamma, Gammat, wlist=None, tlist=None):
    """Spectrum and correlation function."""
    if wlist is None:
        wlist = np.linspace(-2, 2, 500) * 2 * np.pi
    if tlist is None:
        tlist = np.linspace(0, 100, 500)

    # Build full Liouvillian LG (consolidated logic from your files)
    # ... 

    rhoss = steadystate(LG)
    spec = spectrum(LG, wlist, [], c_op, c_op)   # adjust operators
    corr = correlation_2op_1t(LG, rhoss, tlist, [], c_op.dag(), c_op)
    return wlist/(2*np.pi), spec, tlist, corr


def run_photon_statistics_sweep():
    """Example: sweep pump rate."""
    Gamma_vec = np.logspace(-3, 2, 300)
    n_vec, g2_vec = [], []

    for Gamma in Gamma_vec:
        n, g2 = calculate_steady_state_photon_stats(g1=0.1, g2=0.1, kappas=0.4, kappat=0.2,
                                                   Gamma=Gamma, n_atoms=1)
        n_vec.append(n)
        g2_vec.append(g2)

    # Plotting (clean version of your plots)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].plot(Gamma_vec, n_vec)
    axs[0].set_xscale('log')
    axs[0].set_xlabel(r'$\Gamma$')
    axs[0].set_ylabel(r'$\langle n \rangle$')

    axs[1].plot(Gamma_vec, g2_vec)
    axs[1].set_xscale('log')
    axs[1].set_xlabel(r'$\Gamma$')
    axs[1].set_ylabel(r'$g^{(2)}(0)$')
    plt.tight_layout()
    plt.savefig('results/coupled_photon_stats.pdf')
    plt.close()
