#!/usr/bin/env python3
"""Reproduce A.139's 'source phase shift' the way A.139 measured it: the FIRST EXTREMUM
IN k of the SW source Theta-hat = Theta_0 + Psi evaluated at eta_rec, expressed as
k*rs/pi (undriven -> 1; shift = k*rs/pi - 1).  Run on the CR arm both ways: stacking rate
(LEAFPERT=0, the pre-leaf-correction rate A.139 ran on) and leaf rate (LEAFPERT=1).
Also measure the undriven first extremum, so the calibration is MEASURED not assumed."""
import os, sys, numpy as np
import importlib.util
from scipy.signal import argrelextrema

AC = '/home/user/shadow-of-existence/computations/beyond_the_wall/ACOUSTIC_two_arm.py'

def load(leafpert):
    os.environ['ARM'] = 'cr'
    os.environ['LEAFPERT'] = '1' if leafpert else '0'
    spec = importlib.util.spec_from_file_location('ac', AC)
    ac = importlib.util.module_from_spec(spec); spec.loader.exec_module(ac)
    return ac

def first_extremum_in_k(ac, driven):
    ac.DRC, ac.DRE = (1.0, 1.0) if driven else (0.0, 0.0)
    # fine k-grid across the first-peak region; l ~ k*D_M
    kk = np.linspace(30.0/ac.D_M, 400.0/ac.D_M, 220)
    sol, nk, NV = ac.evolve(kk, e_end=ac.eta_rec)
    Y = sol.sol(ac.eta_rec).reshape(nk, NV)
    dg = Y[:, 2]; Ph = Y[:, 6]; sig = Y[:, 7] / 2
    Hc = float(ac.Hl_of(ac.eta_rec) if ac.LEAFPERT else ac.Hc_of(ac.eta_rec))
    Onv = float(ac.On_of(ac.eta_rec))
    Ps = Ph - 6 * Hc**2 * Onv * sig / kk**2
    That = dg/4 + Ps                                    # the SW source, A.139's quantity
    # first extremum in k with k*eta_rec>1 (sub-horizon), same spirit as A.139's coarse scan
    ext = sorted(list(argrelextrema(That, np.greater, order=3)[0]) +
                 list(argrelextrema(That, np.less, order=3)[0]))
    ext = [q for q in ext if kk[q]*ac.eta_rec > 1.0]
    if not ext:
        return None
    q = ext[0]
    k1 = kk[q]
    return k1, k1*ac.D_M

for leaf in (False, True):
    ac = load(leaf)
    rate = 'LEAF (corrected)' if leaf else 'STACKING (pre-correction = A.139 rate)'
    rs_stack = ac.R_S
    rs_leaf = ac.sound_phase(ac.ETA_S, ac.eta_rec)      # int c_s d eta on the active clock
    print("="*74)
    print(f"  CR arm  --  {rate}")
    print(f"  D_M={ac.D_M:.1f}  rs_stack(R_S)={rs_stack:.2f}  rs_leaf(sound_phase)={rs_leaf:.2f}")
    print("="*74)
    for driven in (False, True):
        r = first_extremum_in_k(ac, driven)
        tag = 'DRIVEN  ' if driven else 'undriven'
        if r is None:
            print(f"  {tag}: no extremum found"); continue
        k1, l1 = r
        qs = k1*rs_stack/np.pi
        ql = k1*rs_leaf/np.pi
        print(f"  {tag}: 1st source extremum  l={l1:6.1f}  k={k1:.4f}   "
              f"k*rs_stack/pi={qs:.3f} (shift {qs-1:+.3f})   "
              f"k*rs_leaf/pi={ql:.3f} (shift {ql-1:+.3f})")
    print()
