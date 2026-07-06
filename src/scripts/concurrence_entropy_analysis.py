#!/usr/bin/env python3
from src.models import *
import numpy as np

if __name__ == "__main__":
    for sys_type in ['atoms', 'excitons']:
        g1 = 0.1
        kappas = 4*g1
        Gamma_vec = np.linspace(0.01, 80*(4*g1**2)/kappas, 300)
        conc_vec = []
        entropy_vec = []
        for Gamma in Gamma_vec:
            LG, _, _, _, _ = build_liouvillian(Gamma=Gamma, n_target=2, system_type=sys_type)
            rho_ss = steadystate(LG)
            conc, ent = calculate_concurrence_entropy(rho_ss, n_target=2)
            conc_vec.append(conc)
            entropy_vec.append(ent)
        qsave(conc_vec, f'../data/{sys_type}_concurrence')
        qsave(entropy_vec, f'../data/{sys_type}_entropy')
    print("Concurrence & entropy analysis completed.")
