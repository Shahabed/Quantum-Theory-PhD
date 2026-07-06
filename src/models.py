#!/usr/bin/env python3
"""
Core models for coupled cavity QED simulations.
Consolidated from all three batches.
"""

import matplotlib
matplotlib.use('Agg')
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import *

def build_operators(N1=4, N2=4, n_target=1, system_type='atoms'):
    """Build tensor operators for source + target cavity system."""
    if system_type == 'atoms' or system_type == 'excitons':
        a = tensor(destroy(N1), qeye(2), qeye(N2), *[qeye(2)] * n_target)
        c = tensor(qeye(N1), qeye(2), destroy(N2), *[qeye(2)] * n_target)
        sm_source = tensor(qeye(N1), sigmam(), qeye(N2), *[qeye(2)] * n_target)
        sm_target = []
        for i in range(n_target):
            ops = [qeye(N1), qeye(2), qeye(N2)] + [qeye(2)]*i + [sigmam()] + [qeye(2)]*(n_target-i-1)
            sm_target.append(tensor(ops))
        return a, c, sm_source, sm_target
    return None, None, None, None

def build_liouvillian(g1=0.1, g2=0.1, kappas=None, kappat=None, gammar=0.02, gammap=0.02,
                     Gamma=0.5, Gammat=0.5, n_target=1, system_type='excitons', N1=4, N2=4):
    """Build full Liouvillian LG for the coupled system."""
    if kappas is None: kappas = 4 * g1
    if kappat is None: kappat = g2 if system_type == 'excitons' else g2
    
    a, c, sm1, sm_t = build_operators(N1=N1, N2=N2, n_target=n_target, system_type=system_type)
    
    # Hamiltonians
    Hs = g1 * (sm1 * a.dag() + sm1.dag() * a)
    LHs = liouvillian(Hs, [])
    
    Ht_terms = [g2 * (sm * c.dag() + sm.dag() * c) for sm in sm_t]
    LHct = sum(liouvillian(Ht, []) for Ht in Ht_terms)
    
    # Source collapse
    LRs = Gamma*(2*spre(sm1.dag())*spost(sm1) - spre(sm1*sm1.dag()) - spost(sm1*sm1.dag())) + \
          gammar*(2*spre(sm1)*spost(sm1.dag()) - spre(sm1.dag()*sm1) - spost(sm1.dag()*sm1))
    Ls = LHs + LRs
    
    # Target collapse + cross terms
    LRct = kappas*(2*spre(a)*spost(a.dag()) - spre(a.dag()*a) - spost(a.dag()*a)) + \
           kappat*(2*spre(c)*spost(c.dag()) - spre(c.dag()*c) - spost(c.dag()*c))
    LRct += -2*np.sqrt(kappat*kappas) * (spre(c.dag()*a) + spost(a.dag()*c) - spre(a)*spost(c.dag()) - spre(c)*spost(a.dag()))
    
    for sm in sm_t:
        LRct += Gammat*(2*spre(sm)*spost(sm.dag()) - spre(sm.dag()*sm) - spost(sm.dag()*sm))
        LRct += gammap*(2*spre(sm)*spost(sm.dag()) - spre(sm.dag()*sm) - spost(sm.dag()*sm))
    
    Lct = LHct + LRct
    LG = Ls + Lct
    return LG, a, c, sm1, sm_t

def calculate_photon_stats(LG, c):
    """Compute steady state photon number and g2."""
    rho_ss = steadystate(LG)
    n_cavity = expect(c.dag() * c, rho_ss)
    g2 = expect(c.dag() * c.dag() * c * c, rho_ss) / (n_cavity ** 2) if n_cavity > 1e-8 else 0
    return n_cavity, g2, rho_ss

def calculate_concurrence_entropy(rho_ss, n_target=2):
    target_indices = list(range(3, 3 + n_target))
    rho_target = rho_ss.ptrace(target_indices)
    conc = concurrence(rho_target)
    entropy_vn = entropy_vn(rho_target)
    return conc, entropy_vn

def plot_wigner_fock(rho_ss, filename="wigner_fock.pdf", title=""):
    rho_cavity = rho_ss.ptrace([2])
    xvec = np.linspace(-5, 5, 200)
    W = wigner(rho_cavity, xvec, xvec)
    wlim = abs(W).max()
    
    fig, axes = plt.subplots(1, 2, figsize=(12,6))
    cont = axes[1].contourf(xvec, xvec, W, 100, norm=matplotlib.colors.Normalize(-wlim, wlim), cmap=plt.get_cmap('RdBu'))
    axes[1].set_xlabel(r'Im $\alpha$')
    axes[1].set_ylabel(r'Re $\alpha$')
    fig.colorbar(cont, ax=axes[1])
    
    axes[0].bar(np.arange(len(rho_cavity.diag())), np.real(rho_cavity.diag()), color="blue", alpha=0.6)
    axes[0].set_xlabel('Fock number')
    axes[0].set_ylabel('Occupation probability')
    axes[0].set_ylim(0, 1)
    plt.suptitle(title)
    plt.savefig(filename)
    plt.close()

def run_photon_sweep(g1=0.1, n_target=1, system_type='excitons', N1=4, N2=4, n_points=800):
    kappas = 4 * g1
    Gamma_max = 80 * (4*g1**2) / kappas
    Gamma_vec = np.linspace(0.01, Gamma_max, n_points)
    n_avg = []
    g2_vec = []
    
    for Gamma in Gamma_vec:
        LG, a, c, _, _ = build_liouvillian(g1=g1, Gamma=Gamma, n_target=n_target, system_type=system_type, N1=N1, N2=N2)
        n, g2, _ = calculate_photon_stats(LG, c)
        n_avg.append(n)
        g2_vec.append(g2)
    
    return Gamma_vec, n_avg, g2_vec
