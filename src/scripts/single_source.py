#!/usr/bin/env python3
from src.models import *
import numpy as np

if __name__ == "__main__":
    g = 0.1
    kappa = 4 * g
    gamma = 0.02
    N = 4
    Gamma_max = 80 * (4*g**2) / kappa
    Gamma_vec = np.linspace(0.01, Gamma_max, 1500)
    n_avg_vec = []
    g2_vec = []
    
    for Gamma in Gamma_vec:
        a = tensor(destroy(N), qeye(2))
        sm = tensor(qeye(N), destroy(2))
        H = g * (a.dag() * sm + a * sm.dag())
        c_ops = [sqrt(kappa) * a, sqrt(gamma) * sm, sqrt(Gamma) * sm.dag()]
        rho_ss = steadystate(H, c_ops)
        n = expect(a.dag() * a, rho_ss)
        g2 = expect(a.dag()*a.dag()*a*a, rho_ss) / (n**2) if n > 1e-8 else 0
        n_avg_vec.append(n)
        g2_vec.append(g2)
    
    qsave(g2_vec, '../data/source_g2')
    qsave(n_avg_vec, '../data/source_n')
    print("Single source completed.")
