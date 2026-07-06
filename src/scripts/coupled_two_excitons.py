#!/usr/bin/env python3
from src.models import *
import numpy as np

if __name__ == "__main__":
    g1 = 0.1
    Gamma_vec, n_avg, g2_vec = run_photon_sweep(g1=g1, n_target=2, system_type='excitons')
    qsave(g2_vec, '../data/two_excitons_g2')
    qsave(n_avg, '../data/two_excitons_n')
    print("Two excitons done.")
