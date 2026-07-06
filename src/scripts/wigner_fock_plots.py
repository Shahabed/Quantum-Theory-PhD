#!/usr/bin/env python3
from src.models import *
import numpy as np

if __name__ == "__main__":
    g1 = 0.1
    for config in [(2, 'atoms', 0.5), (1, 'excitons', 1.0), (2, 'excitons', 0.05)]:
        n_target, stype, Gamma = config
        LG, a, c, _, _ = build_liouvillian(g1=g1, Gamma=Gamma, n_target=n_target, system_type=stype)
        rho_ss = steadystate(LG)
        plot_wigner_fock(rho_ss, f"../plots/{stype}_{n_target}_wigner_G{Gamma}.pdf", f"{stype} {n_target} - Gamma={Gamma}")
    print("Wigner plots generated.")
