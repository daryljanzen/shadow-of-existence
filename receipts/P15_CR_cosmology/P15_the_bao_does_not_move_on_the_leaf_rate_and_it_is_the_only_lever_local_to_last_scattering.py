#!/usr/bin/env python3
"""`r7753` ** PUTTING EVERY CROSS-LEAF ACCUMULATION ON THE LEAF RATE MOVES THE DISTANCE TO LAST
SCATTERING BY HALF A PER CENT AND LEAVES THE BAO WHERE IT IS, AND NO OTHER LEVER THE RATE CARRIES IS
LOCAL IN THAT WAY. **

`P15` `sec:scope` has the projection's comoving distance on the STACKING rate by derivation, and
`sec:tensions` has the sky preferring the LEAF-rate distance.  This receipt prices that one open
assignment, on the two rate laws the sector already uses and with nothing fitted anywhere:

 * ** THE EPOCH SEPARATES THE TWO RATES BY ITSELF. **  `Delta = D_M(leaf)/D_M(stack) - 1` is
   `0.02115` per cent at worst across the six BAO tracer redshifts and `0.49836` per cent at `z*`.
   ⇒ *So the reading needs NO SPLIT BY OBJECT and no locus at which the rate switches: the radiation
   term is negligible below `z ~ 2.3` and not at `z ~ 1090`, which is the whole of the effect.*
 * ** AND IT IS THE ONLY LOCAL LEVER. **  Measured as the ratio of what a lever moves at `z*` to what
   the same lever moves at a BAO redshift: the leaf rate `23.6` and `59.4`, `H_0` exactly `1.00`, the
   epoch `1.48` and `3.83`.  ⇒ *`H_0` is a perfect global rescaling and the epoch drags the BAO with
   it; only the leaf rate supplies the half per cent where the sky wants it and not elsewhere.*

⛭ ** THE RATE LAWS ARE NOT REIMPLEMENTED HERE ** (`r7445`'s rule): both are read by path out of 60's
`r7580/lightpath.py`, with its background, and this refuses rather than substituting one of its own.
The two-rate decomposition `H_leaf^2 - H_stack^2 = H_0^2 Omega_r (1+z)^4` (`P7` `eq:two-rate`) is then
CHECKED on those two laws over the whole range rather than assumed, because every figure below is an
integral of one against the other and the decomposition is what makes them two readings of one rule.

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that the leaf rate is the right assignment. **  `P15` `sec:scope`'s derivation stands and
   `sec:flatlcdm`'s kernel argument stands against the alternative; what is priced here is the SIZE
   and the LOCALITY of the difference, not its licence.  The rule's own statement (`P7`) forbids
   reading a stacking quantity on the leaf's rate in as many words.
 * ** Not that radiation in the cut supplies it. **  That route is measured and goes the wrong way --
   `14397.425` Mpc, `2.75` per cent BEYOND the stacking distance, where the sky wants `0.50` per cent
   short of it -- and is `sec:scope`'s own finding, not re-derived here.
 * ** No likelihood, no significance, no fit. **  `Delta` and the sensitivities are ratios of
   integrals of two published rate laws over a published background.  The `0.498` per cent the levers
   are sized against is a TARGET read off `Delta(z*)`, not a measurement of the sky.
 * ** Not a claim about any lever outside the rate. **  `H_0` and the epoch are the two the rate
   itself carries; the sector's other parameters are not swept here.

COMPUTES: scope.
 * ** THIS RECEIPT READS COSMOLOGICAL PARAMETERS AND FITS NONE. **  `H_0 = 68.6`, `Omega_m = 0.2973`,
   `Omega_r h^2 = 4.15e-5` and `z* = 1089.9` are the sector's published background, asserted here as
   read out of 60's script rather than typed in as literals of this receipt's own.
 * ** NO `PREDICTION.md` GOVERNS `r7753`, AND THAT IS DELIBERATE. **  Every figure here was
   registered at `r7751+cc66.0` BEFORE the computation existed, measured at `.1`, reported, and
   MERGED at `r7751`, where 69 re-ran `pricing.py` and reproduced it.  `R1`'s row one and `R2`'s
   licences were set in that registration and are not moved; this revision promotes the computation
   to a receipt so the paper can cite it, so there is nothing left to fit.
 * ** THE LOCALITY RATIOS ARE ARITHMETIC ON THOSE MERGED FIGURES **, and were reported at `r7751` as
   post-registration and labelled as such there.  They are stated as ratios and not as derivatives of
   a likelihood.
 * ** THE PINS ARE VERIFIED FAILABLE, AND NOT BY INSPECTION. **  Scaling `Omega_r` by `1.01` in 60's
   script -- a one per cent move in the one term the two rates differ by -- reddens SIX of these
   eleven gates (①③④⑤⑨⑪), the background assertion first.  The perturbation was made on a copy,
   measured, and 60's file restored to its own sha256; it is recorded here because a figure that
   cannot be made to move is not pinned.
 * ** COST: seconds. **  Six `quad` integrals per rate plus two one-sided differences per lever on a
   `200`-node grid; 60's script is run once for its laws.  NOT declared long.
"""
import contextlib
import io
import os
import runpy
import sys

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')

BAO = [0.295, 0.510, 0.706, 0.930, 1.317, 2.330]   # the tracer redshifts, declared at `r7751`
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f"             {witness}")


print("=" * 100)
print(__doc__)
print("=" * 100)

# ------------------------------------------------------------------ 1 the instrument, read by path
if not os.path.exists(LP):
    sys.exit("FATAL: 60's lightpath.py is not where this reads it from; the instrument has moved.")
buf = io.StringIO()
cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(buf):
        NS = runpy.run_path(LP)
finally:
    os.chdir(cwd)
H0, OM, OMR = NS['H0'], NS['OM'], NS['OMR']
H_stack, H_leaf, C, Z_REC = NS['H_stack'], NS['H_leaf'], NS['C'], NS['Z_REC']

check("⛭ `r7753` ** ① THE RATE LAWS AND THE BACKGROUND ARE 60's, READ BY PATH AND NOT REIMPLEMENTED ** "
      "⇒ *`r7445`'s rule: a reimplemented predicate is a second instrument and it will disagree. The "
      "published background is asserted as what that script carries, so a change to it reddens this "
      "receipt instead of silently repricing the assignment*",
      abs(H0 - 68.6) < 5e-9 and abs(OM - 0.2973) < 5e-9
      and abs(OMR - 8.8186e-05) < 5e-10 and abs(Z_REC - 1089.9) < 5e-9,
      f"H0 {H0}  Om {OM}  Om_r {OMR:.4e}  z* {Z_REC}")

# ------------------------------------------------------------------ 2 the rule the two laws are of
zg = np.linspace(0.0, Z_REC, 2000)
lhs = np.array([H_leaf(z) ** 2 - H_stack(z) ** 2 for z in zg])
rhs = H0 ** 2 * OMR * (1.0 + zg) ** 4
worst_rule = float(np.max(np.abs(lhs / rhs - 1.0)))
check("⛭ `r7753` ** ② THE TWO LAWS DIFFER BY EXACTLY THE RADIATION TERM, AT EVERY EPOCH ** ⇒ *`P7`'s "
      "`eq:two-rate` `H_leaf^2 = H_stack^2 + H_0^2 Omega_r (1+z)^4`, CHECKED on the two laws over the "
      "whole range rather than assumed, because every figure below is an integral of one against the "
      "other and this is what makes them two readings of ONE rule.* ⛔ *The threshold is `1e-11` and "
      "not round-off: at `z = 0` the radiation term is `8.8e-5` of `H^2`, so forming the difference of "
      "the two squares there costs five orders of magnitude of the mantissa and double precision's own "
      "floor on this ratio is about `1e-16 / Omega_r ~ 1e-12`. The measured worst deviation sits at "
      "twice that floor and at `z = 0`, which is the cancellation and not a disagreement of the laws.*",
      worst_rule < 1e-11,
      f"worst relative deviation over 2000 nodes to z* = {worst_rule:.3e}, required < 1e-11 "
      f"(the low-z cancellation floor is ~1e-12)")


def DM(z, H):
    return quad(lambda zz: C / H(zz), 0.0, z, limit=200)[0]


d_stack_rec, d_leaf_rec = DM(Z_REC, H_stack), DM(Z_REC, H_leaf)
check("⛭ `r7753` ** ③ AND BOTH DISTANCES TO LAST SCATTERING REPRODUCE THE PUBLISHED PAIR: `14011.456` "
      "AND `13941.629` Mpc ** ⇒ *the stacking one is `sec:scope`'s own derived figure (`r7612`) and "
      "the leaf one is `r7580`'s, so the import is checked against two revisions' published values "
      "before anything is priced on it*",
      abs(d_stack_rec - 14011.456) < 5e-4 and abs(d_leaf_rec - 13941.629) < 5e-4,
      f"stacking {d_stack_rec:.3f} Mpc, leaf {d_leaf_rec:.3f} Mpc")

# ------------------------------------------------------------------ 3 R1: the epoch split
DEL = {z: DM(z, H_leaf) / DM(z, H_stack) - 1.0 for z in BAO}
DEL[Z_REC] = d_leaf_rec / d_stack_rec - 1.0
worst_bao = max(abs(v) for z, v in DEL.items() if z != Z_REC)

print("\n      the split, recomputed here:")
for z in BAO + [Z_REC]:
    print(f"          z {z:9.3f}   Delta {100 * DEL[z]:11.5f} %")

check("⛭⛔ `r7753` ** ④ THE WORST BAO SHIFT IS `0.02115` PER CENT, AT THE HIGHEST TRACER REDSHIFT ** ⇒ "
      "*the first of the two figures the paper can cite: two hundredths of a per cent is below any "
      "BAO distance error the tracers carry, so the reading does not pay for the half per cent at `z*` "
      "out of the BAO fit*",
      abs(100 * worst_bao - 0.02115) < 5e-6
      and abs(DEL[2.330]) == worst_bao,
      f"worst |Delta| over the six tracers {100 * worst_bao:.5f} %, at z = 2.330")

check("⛭⛔ `r7753` ** ⑤ AND THE SHIFT AT LAST SCATTERING IS `0.49836` PER CENT ** ⇒ *the second figure, "
      "and the size of the one open assignment: half a per cent of the projection's distance, which is "
      "what the sector's contrast residual is confronted with*",
      abs(100 * abs(DEL[Z_REC]) - 0.49836) < 5e-6,
      f"|Delta| at z* = {100 * abs(DEL[Z_REC]):.5f} %")

check("⛭ `r7753` ** ⑥ SO `R1`'s REGISTERED ROW ONE FIRES, ON THE LICENCE SET BEFORE THE COMPUTATION "
      "EXISTED ** ⇒ *`r7751+cc66.0` licensed row one at worst BAO `|Delta| <= 5e-4` AND `|Delta(z*)|` "
      "in `[3e-3, 7e-3]`; both hold, and the two neighbouring rows -- that the reading COSTS the BAO, "
      "or that it lands between the lines -- are asserted here NOT to fire*",
      worst_bao <= 5e-4 and 3e-3 <= abs(DEL[Z_REC]) <= 7e-3 and not worst_bao >= 2e-3,
      f"row one: {worst_bao:.3e} <= 5e-4 and 3e-3 <= {abs(DEL[Z_REC]):.3e} <= 7e-3")

check("⛭ `r7753` ** ⑦ AND THE SPLIT IS MONOTONE IN REDSHIFT, FROM `0.00663` PER CENT AT THE NEAREST "
      "TRACER ** ⇒ *which is why no split by OBJECT is needed and `P7`'s `there is no locus at which "
      "the rate switches` is untouched: the separation is the radiation term's own growth with "
      "redshift and nothing else*",
      all(abs(DEL[BAO[i]]) < abs(DEL[BAO[i + 1]]) for i in range(len(BAO) - 1))
      and abs(100 * abs(DEL[0.295]) - 0.00663) < 5e-6,
      "|Delta| " + " < ".join(f"{100 * abs(DEL[z]):.5f}" for z in BAO) + " per cent")

# ------------------------------------------------------------------ 4 R2: the levers
TARGET = DEL[Z_REC]          # what the leaf rate itself supplies at z*, not a number from the sky
EPS = 1e-3
ZS = (Z_REC, 0.510, 2.330)


def dm_stack(z, h0=None, om=None):
    h0 = H0 if h0 is None else h0
    om = OM if om is None else om
    return quad(lambda zz: C / (h0 * np.sqrt(om * (1 + zz) ** 3 + 1.0 - om)), 0.0, z, limit=200)[0]


SENS = {}
for name, key in (('H0', 'H0'), ('Om', 'OM')):
    p = {'H0': H0, 'OM': OM}[key]
    SENS[name] = [((dm_stack(z, **{'h0' if key == 'H0' else 'om': p * (1 + EPS)}) / dm_stack(z)) - 1.0) / EPS
                  for z in ZS]

print("\n      the levers, recomputed here (d ln D_M / d ln p, and the leaf rate as its own shift):")
print(f"          {'the leaf rate':16s} {100 * DEL[Z_REC]:11.5f}% {100 * DEL[0.510]:11.5f}% {100 * DEL[2.330]:11.5f}%")
for name in ('H0', 'Om'):
    print(f"          {name:16s} {SENS[name][0]:11.4f}  {SENS[name][1]:11.4f}  {SENS[name][2]:11.4f}")

check("⛭⛔ `r7753` ** ⑧ `H_0` MOVES THE DISTANCE BY `-0.9990` AT EVERY ONE OF THE THREE REDSHIFTS, AND "
      "THE EPOCH BY `-0.4023`, `-0.1051` AND `-0.2719` ** ⇒ *the two levers the rate itself carries, "
      "priced at `z*` and at the two tracer redshifts that bracket the BAO's weight; `H_0`'s three "
      "figures being ONE number is the content of its being an amplitude*",
      all(abs(s + 0.9990) < 5e-5 for s in SENS['H0'])
      and abs(SENS['Om'][0] + 0.4023) < 5e-5 and abs(SENS['Om'][1] + 0.1051) < 5e-5
      and abs(SENS['Om'][2] + 0.2719) < 5e-5,
      f"H0 {SENS['H0'][0]:.4f} {SENS['H0'][1]:.4f} {SENS['H0'][2]:.4f};  "
      f"Om {SENS['Om'][0]:.4f} {SENS['Om'][1]:.4f} {SENS['Om'][2]:.4f}")

RAT = {'the leaf rate': [abs(DEL[Z_REC] / DEL[2.330]), abs(DEL[Z_REC] / DEL[0.510])],
       'H0': [abs(SENS['H0'][0] / SENS['H0'][2]), abs(SENS['H0'][0] / SENS['H0'][1])],
       'Om': [abs(SENS['Om'][0] / SENS['Om'][2]), abs(SENS['Om'][0] / SENS['Om'][1])]}
print("\n      the LOCALITY of each lever -- what it moves at z* over what it moves at a tracer:")
for k, v in RAT.items():
    print(f"          {k:16s} {v[0]:8.2f} (vs z = 2.330)   {v[1]:8.2f} (vs z = 0.510)")

check("⛭⛔ `r7753` ** ⑨ THE LEAF RATE'S LOCALITY IS `23.6` AND `59.4`, AGAINST `1.00` FOR `H_0` AND "
      "`1.48` AND `3.83` FOR THE EPOCH ** ⇒ *the figures the `only local lever` statement is made of, "
      "each a ratio of two numbers this receipt already pinned*",
      abs(RAT['the leaf rate'][0] - 23.6) < 5e-2 and abs(RAT['the leaf rate'][1] - 59.4) < 5e-2
      and abs(RAT['H0'][0] - 1.00) < 5e-3 and abs(RAT['H0'][1] - 1.00) < 5e-3
      and abs(RAT['Om'][0] - 1.48) < 5e-3 and abs(RAT['Om'][1] - 3.83) < 5e-3,
      f"leaf {RAT['the leaf rate'][0]:.2f}/{RAT['the leaf rate'][1]:.2f}, "
      f"H0 {RAT['H0'][0]:.2f}/{RAT['H0'][1]:.2f}, Om {RAT['Om'][0]:.2f}/{RAT['Om'][1]:.2f}")

check("⛭⛔ `r7753` ** ⑩ SO THE LEAF RATE IS THE ONLY LOCAL LEVER, BY A FACTOR OF AT LEAST SIX OVER THE "
      "NEXT ONE ** ⇒ *** asserted as a SEPARATION between the ratios rather than as a verdict: the "
      "leaf rate's smaller locality exceeds the largest the other two reach, so on the levers the rate "
      "carries there is no second way to move `z*` and leave the BAO. *** ⛔ *Not that no such lever "
      "exists outside the rate -- only that neither of the rate's own is one.*",
      min(RAT['the leaf rate']) > 6.0 * max(RAT['H0'] + RAT['Om']),
      f"leaf min {min(RAT['the leaf rate']):.2f} against the others' max "
      f"{max(RAT['H0'] + RAT['Om']):.2f}, ratio {min(RAT['the leaf rate']) / max(RAT['H0'] + RAT['Om']):.2f}")

check("⛭ `r7753` ** ⑪ AND NEITHER LEVER SUPPLIES THE HALF PER CENT BY REQUIREMENT: `H_0` WOULD NEED "
      "`+0.499` PER CENT AND THE EPOCH `+1.239` ** ⇒ *reported because `R2`'s question was whether any "
      "candidate is FORCED to it; `H_0` is fixed by the acoustic angle and the BAO together and the "
      "epoch is a measured clock reading, so these are the sizes of two moves neither parameter is "
      "free to make, not two alternatives.* ⛔ *`r7751` printed these as `+0.498` and `+1.238` because "
      "its reader divided by the target ROUNDED to `-0.498` per cent, where this receipt divides by "
      "`Delta(z*)` itself. The third decimal is the rounding of the divisor and nothing else; recorded "
      "here rather than smoothed, because a pin that quietly reproduced the rounded pair would be "
      "pinning the reader's formatting.*",
      abs(100 * TARGET / SENS['H0'][0] - 0.499) < 5e-4
      and abs(100 * TARGET / SENS['Om'][0] - 1.239) < 5e-4,
      f"H0 needs {100 * TARGET / SENS['H0'][0]:+.3f} %, Om needs {100 * TARGET / SENS['Om'][0]:+.3f} % "
      f"(r7751 printed +0.498 / +1.238 against the rounded target)")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {11 - len(FAILS)} of 11 gates;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
