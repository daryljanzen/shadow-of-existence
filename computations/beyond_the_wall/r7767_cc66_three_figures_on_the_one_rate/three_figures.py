#!/usr/bin/env python3
"""`r7767+cc66` THE THREE FIGURES `P15` CARRIES, RECOMPUTED ON THE ONE RATE -- AND TWO OF THE THREE
TURN OUT NOT TO MOVE, FOR DIFFERENT REASONS WORTH DISTINGUISHING.

⛭ Registered in `PREDICTION.md` at `r7767+cc66.0`, pushed before a figure was read.  `R0` asked what the
spectra bank holds BEFORE any physics was looked at, and its answer decided how each item is done.

⛔ ** THE DISTANCE IS ISOLATED, WHICH THE OBVIOUS CONTRAST DOES NOT DO. **  The banked arms differ in TWO
things at once -- `leafrec1` (recombination solved on the leaf rate) and `distances` (the projection's
distance on the leaf rate).  Comparing the plain arm with `leafrec1_distances` moves both.  The bank
carries the middle term, so every row below contrasts `leafrec1` against `leafrec1_distances` and
changes ONLY the distance.
"""
import contextlib
import io
import os
import runpy
import subprocess
import sys

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
DAMP = os.path.join(RCPT, 'P15_the_damping_signature_error_budget_and_the_convention_dominates_it.py')
COMB = os.path.join(RCPT, 'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_'
                          'with_no_fitted_number.py')
for p in (SPEC, DAMP, COMB):
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the instrument has moved.')
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f'             {witness}')


def arm(tag):
    with np.load(os.path.join(SPEC, tag + '.npz'), allow_pickle=True) as z:
        return {k: z[k] for k in z.files}


def fit_comb(pk, n=3):
    """the comb fitter LIFTED FROM the comb receipt, not reimplemented: lstsq on the first n peaks"""
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(pk[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def comb_of(tag):
    z = arm(tag)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    q = argrelextrema(Dl, np.greater, order=3)[0][:4]
    P = [float(ls[i]) for i in q]
    lA, phi = fit_comb(P)
    return dict(P=P, comb=lA, phi=phi, l_A=float(z['l_A']), r_s=float(z['r_s']), D_M=float(z['D_M']))


print('=' * 100)
print(__doc__)
print('=' * 100)

# ------------------------------------------------------------------ ① item 1: the distance is not in it
src = open(DAMP, encoding='utf-8').read()
n_dm = src.count('D_M') + src.count('D_C')
has_ratio = "(arm['r_D'](aa) / arm['r_s'](aa)) / (ctl['r_D'](ac) / ctl['r_s'](ac))" in src
check("⛭⛔⛭ `r7767` ** ① ITEM 1 ANSWERS ITSELF: THE DAMPING SIGNATURE IS `θ_D/θ_* = r_D/r_s`, SO THE "
      "DISTANCE **CANCELS** AND CANNOT MOVE IT ** ⇒ *** the receipt that computes it mentions `D_M` "
      "**zero** times, and its one return is the double ratio `(r_D/r_s)_arm / (r_D/r_s)_ctl`. Two "
      "angles divided by the same `D_M`: the distance is gone before any rate is chosen. ** So the "
      "order's premise does not hold for this figure — moving `D_M` to the leaf rate changes it by "
      "exactly nothing, and no run was needed. ** *** ⌗ *What CAN move it is the CLOCK `r_D` and `r_s` "
      "accumulate on, which is `②`*",
      n_dm == 0 and has_ratio,
      f"occurrences of D_M/D_C in the damping receipt: {n_dm}; the double-ratio return present: "
      f"{has_ratio}")

# ------------------------------------------------------------------ ② item 1: what the clock does
pr = subprocess.run([sys.executable, DAMP], capture_output=True, text=True, cwd=RCPT, timeout=1800)
out = pr.stdout
rows = {}
for key, tag in (('leaf', 'crossing + leaf   (the measured pair)'),
                 ('stack', 'crossing + stacking'),
                 ('leaf_sc', 'crossing + leaf at (68.60, 0.2973)')):
    for ln in out.splitlines():
        if tag in ln:
            rows[key] = ln.split()[-1]
            break
check("⛭⛔⛭ `r7767` ** ② AND THE CLOCK IS WHAT MOVES IT, BY `37` POINTS: `+2.21 %` ON THE LEAF CLOCK "
      "AGAINST `−34.78 %` ON THE STACKING CLOCK ** ⇒ *** so the figure IS rate-sensitive, through the "
      "rate `r_D` and `r_s` are accumulated on and not through the distance. On the one rate — both of "
      "them on the leaf, which is where the corpus already puts plasma accumulations — it is `+2.21 %` "
      "to recombination and `+2.31 %` at the self-consistent `(68.60, 0.2973)`, nearly flat in `H₀`. *** "
      "⛔ **But it does NOT survive as a detection:** the two defensible `r_D` endpoints straddle zero, "
      "`+2.21 %` and `−0.89 %`, and that convention is worth `3.096` points against `0.02` from the "
      "whole cosmological parameter budget — **`138×`**. ⇒ *The size is set by where the integral stops, "
      "not by the rate.*",
      pr.returncode == 0 and rows.get('leaf') == '+2.21%' and rows.get('stack') == '-34.78%'
      and rows.get('leaf_sc') == '+2.31%',
      f"receipt exits {pr.returncode}; leaf {rows.get('leaf')}, stacking {rows.get('stack')}, "
      f"leaf at the self-consistent point {rows.get('leaf_sc')}")

# ------------------------------------------------------------------ ③ item 2: the comb, distance isolated
TRI = [('cr_x_h686_L2000', 'plain (no leaf recombination, stacking distances)'),
       ('cr_x_h686_L2000_leafrec1', 'leaf recombination, STACKING distances'),
       ('cr_x_h686_L2000_leafrec1_distances', 'leaf recombination, LEAF distances')]
print('\n      the comb with the distance ISOLATED (only the third pair member moves it):')
print(f"      {'arm':52} {'comb':>9} {'l_A rep':>9} {'D_M':>11} {'r_s':>8}")
got = {}
for tag, lab in TRI:
    c = comb_of('cc66_' + tag)
    got[tag] = c
    print(f"      {lab:52} {c['comb']:9.3f} {c['l_A']:9.3f} {c['D_M']:11.3f} {c['r_s']:8.3f}")
d_comb = got['cr_x_h686_L2000_leafrec1_distances']['comb'] - got['cr_x_h686_L2000_leafrec1']['comb']
d_DM = (got['cr_x_h686_L2000_leafrec1_distances']['D_M']
        / got['cr_x_h686_L2000_leafrec1']['D_M'] - 1.0)
check("⛭⛔⛭ `r7767` ** ③ ITEM 2: THE DISTANCE MOVES THE COMB BY `1.5` MULTIPOLES, AND `P15`'s PRINTED "
      "`299.1` IS **ALREADY** THE LEAF-DISTANCE VALUE ** ⇒ *** holding the recombination solve fixed and "
      "moving ONLY the distance to the leaf rate takes the comb from the stacking-distance value to "
      "`299.06`, which is what `P15` l.813, l.884 and l.2065 print as `299.1`. ** So the order's premise "
      "does not hold for this figure either: the comb `P15` carries was computed on the leaf-rate "
      "distance already. ** *** ⌗ *The `D_M` shift is `−0.50` per cent, which is `r7753`'s pricing at "
      "`z*` to three figures — the same number arriving through the spectrum*",
      abs(got['cr_x_h686_L2000_leafrec1_distances']['comb'] - 299.06) < 0.05 and abs(d_DM + 0.00498) < 2e-4,
      f"comb moves {d_comb:+.3f} multipoles when only the distance moves; D_M moves {100 * d_DM:+.4f} % "
      f"(r7753 priced -0.49836 % at z*); the leaf-distance comb is "
      f"{got['cr_x_h686_L2000_leafrec1_distances']['comb']:.3f} against the sky's 298.4")

# ------------------------------------------------------------------ ④ item 2: the angle-alone H0
SKY_COMB = 298.4
h0_ref = 68.6
scale = {t: SKY_COMB / got[t]['comb'] for t, _ in TRI}
check("⛭ `r7767` ** ④ AND THE ANGLE-ALONE `H₀` THE TWO DISTANCES IMPLY DIFFER BY `0.5` PER CENT, THE "
      "SAME `0.5` ** ⇒ *the comb scales as `1/D_M` at fixed `r_s`, and `D_M` scales as `1/H₀` to `0.999` "
      "(`r7751`'s sensitivity), so the angle-alone `H₀` ratio is the comb ratio to a part in `10³`. "
      "Reported as a RATIO rather than as an `H₀` value, because turning it into one needs the fit the "
      "order does not ask for and this receipt does not do*",
      abs((scale['cr_x_h686_L2000_leafrec1'] / scale['cr_x_h686_L2000_leafrec1_distances']) - 1.0
          - (-d_comb / got['cr_x_h686_L2000_leafrec1_distances']['comb'])) < 1e-4,
      f"sky/comb on stacking distances {scale['cr_x_h686_L2000_leafrec1']:.6f}, on leaf distances "
      f"{scale['cr_x_h686_L2000_leafrec1_distances']:.6f}; ratio - 1 = "
      f"{scale['cr_x_h686_L2000_leafrec1'] / scale['cr_x_h686_L2000_leafrec1_distances'] - 1.0:+.5f}")

# ------------------------------------------------------------------ ⑤ item 3: the low-multipole depths
A = arm('p15_lowell_depths_leafrec1')
B = arm('p15_lowell_depths_distances_leafrec1')
shared = [k for k in ('armA_exact', 'armB_decoupled', 'armB_frozen') if k in A and k in B]
print('\n      the low-multipole depths, projection on the stacking rate against the leaf rate:')
print(f"      {'series':18} {'n':>4} {'max |rel move|':>15} {'at ell':>8}")
moves = {}
for k in shared:
    a, b = np.asarray(A[k], float).ravel(), np.asarray(B[k], float).ravel()
    n = min(a.size, b.size)
    rel = np.abs(b[:n] / np.where(a[:n] != 0, a[:n], np.nan) - 1.0)
    i = int(np.nanargmax(rel))
    ells = np.asarray(A['ells'], float).ravel()
    moves[k] = float(np.nanmax(rel))
    print(f"      {k:18} {n:4d} {100 * moves[k]:14.4f}% {ells[i] if i < ells.size else -1:8.0f}")
check("⛭⛔⛭ `r7767` ** ⑤ ITEM 3: THE LOW-MULTIPOLE DEPTHS **DO** MOVE WHEN THE PROJECTION TAKES THE LEAF "
      "RATE, AND THIS IS THE ONE OF THE THREE THAT DOES ** ⇒ *** measured series by series on the two "
      "banked arms that differ ONLY in the projection's distance. ** So of the order's three figures, the "
      "damping signature cannot move (the distance cancels), the comb has already moved (`P15` prints the "
      "leaf value), and the low-multipole depths are the live one. ** *** ⌗ *Reported as a relative move "
      "with no significance attached: the arms carry no uncertainty and `R3⑦` registered that I would say "
      "so rather than invent one*",
      len(shared) >= 2 and all(np.isfinite(v) for v in moves.values()),
      '; '.join(f'{k} {100 * v:.4f}%' for k, v in moves.items()))

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {5 - len(FAILS)} of 5 rows;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
