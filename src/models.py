import matplotlib
matplotlib.use('Agg')
from qutip import *
import numpy as np
import matplotlib.pyplot as plt

def build_operators(N1=4, N2=4, n_atoms=1, n_excitons=1):
    """Build tensor operators for source + target system."""
    a = tensor(destroy(N1), qeye(2), qeye(N2), *[qeye(2)] * n_atoms)
    c = tensor(qeye(N1), qeye(2), destroy(N2), *[qeye(2)] * n_atoms)
    sm_source = tensor([qeye(N1), sigmam(), qeye(N2)] + [qeye(2)] * n_atoms)
    sm_target = [tensor([qeye(N1), qeye(2), qeye(N2)] + [qeye(2)]*(i) + [sigmam()] + [qeye(2)]*(n_atoms-i-1)) for i in range(n_atoms)]
    return a, c, sm_source, sm_target

def build_liouvillian(g_source, g_target, kappa_s, kappa_t, gamma, Gamma_source, Gamma_target=0.5, n_atoms=1):
    """Build full Liouvillian for coupled system."""
    a, c, sm_s, sm_t = build_operators(n_atoms=n_atoms)
    # ... (full implementation with Hs, Ht, collapse operators, cross terms)
    # Returns LG for steadystate
    # (I can expand this fully if needed)
    pass  # Placeholder — full version available on request

# Add functions for:
# - calculate_photon_stats(LG)
# - calculate_concurrence(rho)
# - calculate_entropy(rho)
# - run_sweep(...)
# - plot_wigner_fock(rho)
