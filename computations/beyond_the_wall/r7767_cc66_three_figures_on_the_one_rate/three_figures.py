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

# ------------------------------------------------------------------ ③④ item 2, THE PAIR CORRECTED
# ⛔ `r7767+cc66.2` THE BANK'S `_distances` MEANS "AT THE DISTANCES' POINT" -- A PARAMETER POINT -- AND
#   NOT "THE LEAF-RATE DISTANCE".  The flag for the distance is `LEAFGEOM`, and `ACOUSTIC_two_arm.py`
#   l.235 says so.  70's own manifest on the arm below settles it: *"arm of record + LEAFGEOM=1 (the
#   projection distance on the leaf rate, radiation included)"*.  My first pair had neither member on
#   the leaf rate and would have reported a move the pair did not contain.
PAIR = [('cc66_cr_x_h686_L2000_leafrec1_distances', 'arm of record, STACKING-rate distance'),
        ('r7749_leafgeom_nofit_L2000_cr', 'LEAFGEOM=1, LEAF-rate distance (70, r7749)')]


def peaks_subgrid(ls, Dl, n=4):
    """the receipt's locator, then a PARABOLIC refinement -- because a `dl = 2` grid quantises the comb
    to integers, which is the grid speaking and not the spectrum.  `⑧` asserts the refinement moved it."""
    q = argrelextrema(Dl, np.greater, order=3)[0][:n]
    out = []
    for i in q:
        if 0 < i < ls.size - 1:
            y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
            den = (y0 - 2.0 * y1 + y2)
            shift = 0.5 * (y0 - y2) / den if den != 0 else 0.0
            out.append(float(ls[i] + shift * (ls[i + 1] - ls[i])))
        else:
            out.append(float(ls[i]))
    return out


print("\n      item 2, the distance ISOLATED -- same point, same r_s, LEAFGEOM the only difference:")
print(f"      {'arm':46} {'comb(sub-grid)':>15} {'comb(grid)':>11} {'l_A':>9} {'D_M':>11} {'r_s':>9}")
G = {}
for tag, lab in PAIR:
    z = arm(tag)
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    P = peaks_subgrid(ls, Dl)
    Pg = [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=3)[0][:4]]
    G[tag] = dict(comb=fit_comb(P)[0], comb_grid=fit_comb(Pg)[0], l_A=float(z['l_A']),
                  D_M=float(z['D_M']), r_s=float(z['r_s']), P=P)
    g = G[tag]
    print(f"      {lab:46} {g['comb']:15.3f} {g['comb_grid']:11.3f} {g['l_A']:9.3f} "
          f"{g['D_M']:11.3f} {g['r_s']:9.3f}")
A_, B_ = G[PAIR[0][0]], G[PAIR[1][0]]
d_comb = B_['comb'] / A_['comb'] - 1.0
d_DM = B_['D_M'] / A_['D_M'] - 1.0
d_lA = B_['l_A'] / A_['l_A'] - 1.0
check("⛭⛔⛭ `r7767` ** ③ ITEM 2, AND THE ANSWER IS NOT THE ONE THE RULER PREDICTS: `ℓ_A` MOVES "
      "`−0.498` PER CENT AND THE FITTED COMB MOVES `−0.055` — **NINE TIMES LESS** ** ⇒ *** the two arms "
      "sit at the SAME point with the SAME `r_s = 145.328`, so `LEAFGEOM` is the only difference and "
      "`D_M` is the only input that moves: `−0.4984` per cent, which is `r7753`'s priced `−0.49836` per "
      "cent at `z*` to four figures. The REPORTED ruler `ℓ_A = πD_M/r_s` follows it exactly, "
      "`302.889 → 301.380`. ** But the comb FITTED to where the peaks actually land moves only "
      "`−0.055` per cent: the peaks do not follow the ruler. ** *** ⇒ **So `P15`'s `299.1` is a fitted "
      "comb, and on the one rate it becomes about `298.94`, against the sky's `298.4` — `+0.18` per cent "
      "where it was `+0.23`. A slight improvement, not the half-per-cent move the ruler would predict.** "
      "⌷ *My draft of this row claimed the comb follows `D_M` and would have printed `297.6`. It does "
      "not, and the row caught it. Only the RATIO between these two arms is quoted, because this "
      "locator's absolute comb (`296.9`) is not the paper's seven-window matched locator's `299.1`.*",
      abs(d_DM + 0.004984) < 5e-5 and abs(d_lA + 0.004984) < 5e-4
      and abs(d_comb) < 0.002 and abs(d_comb / d_DM) < 0.3,
      f"D_M {100 * d_DM:+.4f} % (r7753 priced -0.49836 %); l_A {100 * d_lA:+.4f} %; fitted comb "
      f"{100 * d_comb:+.4f} %, which is {abs(d_comb / d_DM):.2f} of the ruler's move; applying the comb "
      f"ratio to the paper's 299.1 gives {299.1 * (1.0 + d_comb):.2f} against the sky's 298.4")

check("⛭⛔ `r7767` ** ④ AND THE SUB-GRID LOCATOR WAS NECESSARY: THE RAW GRID QUANTISES THE COMB TO "
      "INTEGERS ** ⇒ *my first pass read `298.000` and `297.000` off a `Δℓ = 2` grid and I nearly "
      "reported them. The parabolic refinement moves each comb off its node, and the row asserts the "
      "refinement CHANGED the answer rather than trusting that it did*",
      abs(A_['comb'] - A_['comb_grid']) > 1e-6 and abs(B_['comb'] - B_['comb_grid']) > 1e-6
      and abs(A_['comb_grid'] - round(A_['comb_grid'])) < 1e-9,
      f"stacking arm: grid {A_['comb_grid']:.6f} -> sub-grid {A_['comb']:.3f}; leaf arm: grid "
      f"{B_['comb_grid']:.6f} -> sub-grid {B_['comb']:.3f}")

# ------------------------------------------------------------------ ⑤ item 3: it needs a run, and why
dep = {t: arm(t) for t in ('p15_lowell_depths_leafrec1', 'p15_lowell_depths_distances_leafrec1')}
man = {t: str(v['manifest']) for t, v in dep.items()}
is_point_pair = ("the distances' point" in man['p15_lowell_depths_distances_leafrec1']
                 and 'the refit point' in man['p15_lowell_depths_distances_leafrec1'])
lg_ls = np.asarray(arm('r7749_leafgeom_nofit_L2000_cr')['ls'], float)
check("⛭⛔⛭ `r7767` ** ⑤ ITEM 3 CANNOT BE ANSWERED FROM THE BANK, AND I SAY SO RATHER THAN USING THE "
      "PAIR THAT LOOKS RIGHT ** ⇒ *** the two `p15_lowell_depths_*` arms differ by **PARAMETER POINT**, "
      "not by projection: their own manifests call them *\"the distances' point P15's low-ℓ section stays "
      "on\"* and *\"the refit point\"*. Comparing them measures a refit, not the projection's rate — **I "
      "measured `1.94` per cent at `ℓ = 3` from that pair before reading the manifests, and that number "
      "is withdrawn.** And the one arm that DOES carry the projection on the leaf rate starts at "
      "`ℓ = 100`, so it has no low-ℓ coverage at all. ** ⇒ Item 3 needs a low-ℓ run with the "
      "projection on the leaf rate; it is not in the bank and no banked pair stands in for it. ** *** ",
      is_point_pair and lg_ls.min() >= 100.0,
      f"the depths pair is two points, not two projections: {is_point_pair}; the LEAFGEOM arm's ells "
      f"start at {lg_ls.min():.0f}, so no low-l coverage")

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {5 - len(FAILS)} of 5 rows;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
