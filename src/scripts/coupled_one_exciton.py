#!/usr/bin/env python3
from src.models import *
import numpy as np

if __name__ == "__main__":
    g1 = 0.1
    Gamma_vec, n_avg, g2_vec = run_photon_sweep(g1=g1, n_target=1, system_type='excitons')
    qsave(g2_vec, '../data/one_exciton_g2')
    qsave(n_avg, '../data/one_exciton_n')
    print("One exciton sweep done.")
