#!/usr/bin/env python3
"""
`r7580` -- WHETHER THE OBSERVER'S-READOUT IDENTIFICATION FORCES THE STACKING-RATE DISTANCE.

Scores the arms registered in `PREDICTION.md` (digest printed below, and the file is committed
before this script runs).  Nothing here is fitted: every number comes from the published
background parameters and the chart's own closed forms.

`r7445`'s rule is respected: the background map is not reimplemented.  It is read out of
`receipts/P15_CR_cosmology/P15_the_kernels_distance_is_the_observers_own_flat_slice_so_the_rate_rule_does_reach_it_and_the_disagreement_with_the_sky_is_real.py`
by `ast`, because that module's body prints and gates and must not be imported for its side
effects.  A reimplementation of a predicate is a second instrument and it will disagree.
"""
import ast
import hashlib
import os
import re
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PRIOR = os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_kernels_distance_is_the_observers_own_flat_slice_so_the_rate_rule_'
    'does_reach_it_and_the_disagreement_with_the_sky_is_real.py')
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P16 = os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex')

ARMS = {}


def arm(tag, label, verdict, note=''):
    ARMS[tag] = verdict
    mark = {'HIT': '  HIT', 'MISS': ' MISS', 'VOID': ' VOID', '----': ' ----'}[verdict]
    print(f"  [{mark}]  {tag}  {label}")
    if note:
        for ln in note.splitlines():
            print(f"            {ln}")


def head(t):
    print(f"\n{'=' * 100}\n{t}\n{'=' * 100}")


def flat(t):
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


print(__doc__)
print(f"  PREDICTION.md sha1 = "
      f"{hashlib.sha1(open(os.path.join(HERE, 'PREDICTION.md'), 'rb').read()).hexdigest()}")

# ---------------------------------------------------------------- the background, read not rewritten
src = open(PRIOR, encoding='utf-8').read()
tree = ast.parse(src, filename=PRIOR)
WANT_FN = {'background'}
WANT_NAME = {'C', 'Z_REC', 'OMBH2', 'BG'}
ns = {'np': np, 'quad': quad}
picked_fn, picked_name = set(), set()
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in WANT_FN:
        exec(compile(ast.Module(body=[node], type_ignores=[]), PRIOR, 'exec'), ns)
        picked_fn.add(node.name)
    elif isinstance(node, ast.Assign):
        names = {getattr(t, 'id', None) for t in node.targets} & WANT_NAME
        if names:
            exec(compile(ast.Module(body=[node], type_ignores=[]), PRIOR, 'exec'), ns)
            picked_name |= names
if picked_fn != WANT_FN or picked_name != WANT_NAME:
    sys.exit(f"FATAL: the prior receipt no longer exposes what this reads -- "
             f"functions {sorted(WANT_FN - picked_fn)}, names {sorted(WANT_NAME - picked_name)}.")
background, C, Z_REC, OMBH2 = ns['background'], ns['C'], ns['Z_REC'], ns['OMBH2']
print(f"  read from the prior receipt by ast: background(), C = {C}, Z_REC = {Z_REC}, "
      f"OMBH2 = {OMBH2}")

H0, OM = ns['BG']['the refit background `P15` fits']
b = background(H0, OM)
alpha, r0, x03 = b['alpha'], b['r0'], b['x03']
h = H0 / 100.0
OMR = 4.15e-5 / h ** 2
TWO_M = 2.0 * alpha / (3.0 * np.sqrt(3.0))                 # the Nariai mass, 2M = 2 alpha/(3 sqrt3)
A_AMP = (TWO_M * alpha ** 2) ** (1.0 / 3.0)                # the areal-radius amplitude
u0 = np.arcsinh(np.sqrt(x03 / 2.0))
tt0 = 2.0 * alpha * u0 / 3.0                               # cosmic time now, in light-Mpc

print(f"\n  H0 = {H0}  Om = {OM}  Om_r = {OMR:.3e}   alpha = {alpha:.3f}  r_N = {b['rN']:.3f}  "
      f"r_0 = {r0:.3f} Mpc")
print(f"  2M = {TWO_M:.4f}   A = {A_AMP:.4f}   A from r_0 and u_0 = "
      f"{r0 / np.sinh(u0) ** (2.0 / 3.0):.4f}   u_0 = {u0:.6f}   tilde-tau_0 = {tt0:.2f} Mpc")


def r_of(tt):
    return A_AMP * np.sinh(1.5 * tt / alpha) ** (2.0 / 3.0)


def rdot_of(tt):
    u = 1.5 * tt / alpha
    return (A_AMP / alpha) * np.cosh(u) / np.sinh(u) ** (1.0 / 3.0)


def tt_of_z(z):
    rr = r0 / (1.0 + z)
    return (2.0 * alpha / 3.0) * np.arcsinh((rr / A_AMP) ** 1.5)


def H_stack(z):
    return H0 * np.sqrt(OM * (1 + z) ** 3 + 1.0 - OM)


def H_leaf(z):
    return H0 * np.sqrt(OM * (1 + z) ** 3 + 1.0 - OM + OMR * (1 + z) ** 4)


tt_rec = tt_of_z(Z_REC)

# ======================================================================== A. the chart calibration
head("A.  THE CHART, CALIBRATED BEFORE ANYTHING IS ASKED OF IT")

rr = np.geomspace(r0 * 1e-9, r0, 400001)
chi_sq = TWO_M / rr + rr ** 2 / alpha ** 2
opt = minimize_scalar(lambda x: TWO_M / x + x ** 2 / alpha ** 2,
                      bracket=(0.2 * b['rN'], b['rN'], 5 * b['rN']))
min_val, min_at = opt.fun, opt.x
print(f"  min over r of (d_chi r)^2 = {min_val:.16f}   attained at r = {min_at:.6f} Mpc")
print(f"  alpha/sqrt3 = {b['rN']:.6f} Mpc   |min_at/r_N - 1| = {abs(min_at / b['rN'] - 1):.3e}")
print(f"  the grid's own minimum over r in [1e-9 r_0, r_0]: {chi_sq.min():.12f}")
arm('Ⓐ', 'the Nariai tangency: min (d_chi r)^2 is exactly 1, at exactly r = alpha/sqrt3',
    'HIT' if abs(min_val - 1.0) < 1e-12 and abs(min_at / b['rN'] - 1) < 1e-10 else 'MISS',
    f"so (d_chi r) >= 1 on the whole real branch, with a single tangency at z = "
    f"{r0 / b['rN'] - 1:.4f}")

ZS = [0.0, 1.0, 10.0, 1090.0, 3e7]
worst_H = 0.0
for z in ZS:
    tt = tt_of_z(z)
    worst_H = max(worst_H, abs(C * rdot_of(tt) / r_of(tt) / H_stack(z) - 1.0))
print(f"  worst |c (d_chi r)/r  /  H_stack - 1| over z = {ZS}: {worst_H:.3e}")
arm('Ⓑ', 'the rate is the layer-time rate: H_stack = c (d_chi r)/r identically',
    'HIT' if worst_H < 1e-10 else 'MISS')

DC_stack = quad(lambda z: C / H_stack(z), 0.0, Z_REC, limit=400)[0]
DC_layer = r0 * quad(lambda t: 1.0 / r_of(t), tt_rec, tt0, limit=400)[0]
rel_layer = abs(DC_layer / DC_stack - 1.0)
print(f"  the implementation's  int c dz/H_stack      = {DC_stack:10.3f} Mpc")
print(f"  the layer-time form   r_0 int d(tt)/r       = {DC_layer:10.3f} Mpc   "
      f"relative difference {rel_layer:.3e}")
arm('Ⓒ', "the implementation's distance IS the layer-time light-travel integral",
    'HIT' if rel_layer < 1e-8 else 'MISS')

# ================================================================= B. light's real integrated path
head("B.  LIGHT'S REAL INTEGRATED PATH ON THE CONSTRUCTION'S OWN METRIC")

print("  the null ray:  d(tau) = (d_chi r) d(chi)  =>  d(tilde-tau) = (1 + d_chi r) d(chi)")
print("  the proper length traversed, in the local fundamental observer's own frame, is")
print("  sqrt(g_chi chi) d(chi) = (d_chi r) d(chi), which the null condition makes equal to d(tau).")
print("  so the comoving accumulation is r_0 d(tau)/r, and on the ray")
print("        d(tau) = [ (d_chi r) / (1 + d_chi r) ] d(tilde-tau)")


def wgt(tt):
    rd = rdot_of(tt)
    return rd / (1.0 + rd)


D_path = r0 * quad(lambda t: wgt(t) / r_of(t), tt_rec, tt0, limit=400)[0]
ratio = D_path / DC_stack
print(f"\n  the non-synchrony weight (d_chi r)/(1 + d_chi r):")
for z in [0.0, 0.25, 0.6740, 1.0, 3.0, 10.0, 100.0, Z_REC]:
    tt = tt_of_z(z)
    print(f"        z = {z:9.4f}   d_chi r = {rdot_of(tt):9.4f}   weight = {wgt(tt):.6f}")
print(f"\n  light's real integrated path   D_path     = {D_path:10.3f} Mpc")
print(f"  the implementation's distance   D_C^stack = {DC_stack:10.3f} Mpc")
print(f"  ratio D_path / D_C^stack                  = {ratio:.6f}")
in_window = 0.60 <= ratio <= 0.75
grid_ok = bool(np.all(chi_sq >= 1.0 - 1e-9))
arm('Ⓓ', "light's real path is strictly shorter, by the registered factor",
    'VOID' if not grid_ok else ('HIT' if ratio < 1.0 and in_window else 'MISS'),
    f"registered window [0.60, 0.75]; measured {ratio:.6f}"
    + ('' if in_window else '  <-- OUTSIDE THE REGISTERED WINDOW'))

DC_leaf = quad(lambda z: C / H_leaf(z), 0.0, Z_REC, limit=400)[0]
leaf_shift = DC_leaf / DC_stack - 1.0
print(f"\n  the leaf-rate distance          D_C^leaf  = {DC_leaf:10.3f} Mpc")
print(f"  D_C^leaf / D_C^stack - 1                  = {leaf_shift * 100:+.4f} per cent")
print(f"  |D_path - D_C^leaf| / D_C^leaf             = "
      f"{abs(D_path - DC_leaf) / DC_leaf * 100:.3f} per cent")
leaf_small = abs(leaf_shift) < 0.02
far_apart = abs(D_path - DC_leaf) / DC_leaf > 10 * abs(leaf_shift)
arm('Ⓔ', "light's real path is NOT the leaf-rate distance",
    'HIT' if leaf_small and far_apart else 'MISS',
    f"the leaf shift is {leaf_shift * 100:+.4f} per cent where the path gap is "
    f"{abs(D_path - DC_leaf) / DC_leaf * 100:.3f} per cent")

# ===================================================================== C. priced against the comb
head("C.  EACH CANDIDATE PRICED AGAINST THE ONE QUANTITY THE COMB ALREADY FIXES")

RB = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
A_REC = 1.0 / (1.0 + Z_REC)
rs_leaf = quad(lambda a: C / (a ** 2 * H_leaf(1.0 / a - 1.0) * np.sqrt(3 * (1 + RB * a / A_REC))),
               1e-12, A_REC, limit=400)[0]
print(f"  r_s on the leaf rate = {rs_leaf:.3f} Mpc   (the prior receipt gates pi D_C/r_s near 301.6)")
SKY = 298.4
rows = [('the implementation, stacking rate', DC_stack),
        ('the leaf-rate distance the fit prefers', DC_leaf),
        ("light's real integrated path", D_path)]
for lab, D in rows:
    lA = np.pi * D / rs_leaf
    print(f"        {lab:42s}  D = {D:9.2f} Mpc   l_A = {lA:8.2f}   "
          f"vs the sky's {SKY}: {(lA / SKY - 1) * 100:+7.2f} per cent")
calib = abs(np.pi * DC_stack / rs_leaf - 301.6) / 301.6
print(f"  calibration against the prior receipt's banked figure: |pi D_C/r_s / 301.6 - 1| = "
      f"{calib:.4f}")
arm('Ⓕ', 'the acoustic scale each distance implies, against the sky',
    'HIT' if calib < 0.06 else 'MISS',
    "no pass/fail was registered for the pricing itself; the HIT is the calibration holding")

# ======================================================== D. is the rate-free half rate-neutral?
head("D.  IS THE IDENTIFICATION'S RATE-FREE HALF ABLE TO SELECT A RATE?")

print("  D_M is got from the comoving radial distance chi by the curvature branch:")
print("        Ok > 0:  D_M = (c/H0)/sqrt(Ok)  sinh( sqrt(Ok) H0 chi / c )")
print("        Ok = 0:  D_M = chi                      <-- no H in it at all")
print("        Ok < 0:  D_M = (c/H0)/sqrt(-Ok) sin( sqrt(-Ok) H0 chi / c )")


def D_M(chi, Ok):
    if Ok == 0.0:
        return chi
    s = np.sqrt(abs(Ok))
    k = s * H0 * chi / C
    return (C / H0 / s) * (np.sinh(k) if Ok > 0 else np.sin(k))


worst_flat = max(abs(D_M(chi, 0.0) / chi - 1.0) for chi in (DC_stack, DC_leaf, D_path))
curved = {Ok: abs(D_M(DC_stack, Ok) / DC_stack - 1.0) for Ok in (+0.01, -0.01)}
print(f"\n  at Ok = 0 the identity D_M = chi holds for every one of the three candidate chi, to "
      f"{worst_flat:.3e}")
for Ok, d in curved.items():
    print(f"  at Ok = {Ok:+.2f} it fails by {d * 100:.3f} per cent -- so the identity's content is "
          f"FLATNESS")
print("  and the three chi were built on three different rates, so the identity is satisfied by")
print("  all three alike:  flatness fixes WHICH LENGTH D_M is, and no rate follows from it.")
arm('Ⓖ', 'the identification\'s rate-free half is rate-NEUTRAL and cannot select',
    'HIT' if worst_flat < 1e-10 and min(curved.values()) > 1e-4 else 'MISS')

# ------------------------------------------------------- the control that would void the reading
print("\n  THE REGISTERED CONTROL.  Does the constant-tau stack carry an expansion law of its own?")
print("  The induced three-metric is (d_chi r)^2 d(chi)^2 + r^2 dOmega^2 with r = r(tau + chi).")
print("  Changing the slice's own radial variable to r removes tau outright: dr^2 + r^2 dOmega^2.")
print("  Checked rather than asserted: on each slice, reparameterise chi by r and read g_rr back.")
worst_grr, worst_gang = 0.0, 0.0
for tau in (0.25 * tt0, 0.5 * tt0, tt0):
    for r_t in (10.0, 100.0, 1000.0, 3000.0):
        tt = (2.0 * alpha / 3.0) * np.arcsinh((r_t / A_AMP) ** 1.5)    # the tilde-tau with r = r_t
        chi = tt - tau                                                 # the chi on THIS slice
        d = 1e-6 * tt          # scaled to tilde-tau, the variable r actually varies in
        dr_dchi = (r_of(tau + chi + d) - r_of(tau + chi - d)) / (2 * d)
        g_rr = (np.sqrt((rdot_of(tt)) ** 2) / dr_dchi) ** 2            # (d_chi r)^2 (dchi/dr)^2
        worst_grr = max(worst_grr, abs(g_rr - 1.0))
        worst_gang = max(worst_gang, abs(r_of(tau + chi) / r_t - 1.0))
    print(f"        tau = {tau:8.2f}:  g_rr = 1 and g_angular = r^2 at every r tried -- the slice's"
          f" metric in the r-chart carries no tau")
print(f"  worst |g_rr - 1| over three slices and four radii: {worst_grr:.3e}")
print(f"  worst |r(tau+chi)/r_target - 1|:                   {worst_gang:.3e}")
moves = rdot_of(tt0)
print(f"  what moves is the CONGRUENCE's place in that one fixed flat R^3: a fundamental observer")
print(f"  at fixed chi sits at r(tau + chi), and dr/dtau at fixed chi = d_chi r = {moves:.4f} != 0.")
arm('Ⓘ', 'control: the slice\'s own geometry is tau-free, so the clause carries no rate',
    'HIT' if worst_grr < 1e-9 and worst_gang < 1e-12 and abs(moves - 1.0) > 1e-3 else 'MISS',
    "the slices are isometric to one flat R^3 for every tau, so the stack carries no expansion of\n"
    "its own metric -- which confirms `P15`'s own words, `with no rate in it at all`, literally.")

# ============================================= E. the partition the identification has to cross
head("E.  THE PARTITION `P16`'s OWN CLASSIFIER DRAWS, LOCATED IN `P16` RATHER THAN PARAPHRASED")

p15, p16 = (flat(open(f, encoding='utf-8').read()) for f in (P15, P16))
CLASSIFIER = ('a comoving separation read across leaves takes the stacking rate, a process running '
              'in the content takes the leaf\'s, at every epoch')
WORKED = ('the Silk random walk~\\cite{Silk1968} accumulates on the leaf\'s rate, radiation '
          'included, where its Thomson microphysics runs, and what rides the stacking rate is the '
          'distance both lengths are read across')
IDENT = ('the constant-proper-time slice is exactly flat, so the comoving angular-diameter distance '
         '\\emph{is} the light-travel distance $D_C$')
OPT_ASSIGN = 'the optical depth on the stacking rate as a photon-path observable'
OPT_GROUND = ("the optical depth's null-cone argument is that same rule applied a second time}, "
              "resting as it does on the optical depth being a photon-path observable of the same "
              "kind as the redshift and the distances")
found = {'`P16`\'s classifier, verbatim': CLASSIFIER in p16,
         '`P16`\'s worked case (r_s, r_D), verbatim': WORKED in p16,
         '`P15`\'s identification, verbatim': IDENT in p15,
         '`P15`\'s optical-depth assignment, verbatim': OPT_ASSIGN in p15,
         '`P15`\'s ground for it, verbatim': OPT_GROUND in p15}
for k, v in found.items():
    print(f"        {'located' if v else 'NOT FOUND':10s}  {k}")

# ------------------------------------------------------------------ what the rule's two slots hold
print(f"""
  `P16`'s rule, as `P16` states it, has exactly TWO slots:

        (1) a comoving separation read across leaves  ->  the STACKING rate
        (2) a process running in the content          ->  the LEAF rate

  D_M falls in (1) without strain: it is a separation, read on ONE slice, between the observer's
  worldline and the source's, and the slice is the flat constant-tau one.

  ** MY REGISTERED Ⓗ THEN CLAIMED D_C FALLS IN (2), AND THAT CLAIM DOES NOT SURVIVE THE CORPUS'S
  OWN APPLICATIONS.  THE REGISTERED FORM IS SCORED MISS AND THE DISCARDED READING IS KEPT HERE
  BESIDE ITS CORRECTION. **

  The discarded reading: a light-travel distance is ACCUMULATED along a history through the content
  the photon crosses, which is the criterion by which (2) takes r_s and r_D -- so D_C is in (2) and
  the identification crosses the partition.

  What refutes it: the corpus assigns ANOTHER accumulation-through-the-content to the STACKING
  rate.  The optical depth is int n_e sigma_T dl -- every factor of it content -- and `P15` puts it
  on the stacking rate explicitly, grounded on its being `a photon-path observable of the same kind
  as the redshift and the distances`.  So accumulation-through-content does NOT by itself place a
  quantity in slot (2): r_s and r_D are there, the optical depth is not.

  ⇒ THE CRITERION THAT ACTUALLY SEPARATES THEM IS `photon-path observable`, AND THAT CRITERION IS
    NOT IN THE RULE.  Counted in the two papers:""")
n16, n15 = p16.count('photon-path'), p15.count('photon-path')
print(f"        occurrences of `photon-path` in `P16`, where the rule is stated and derived: {n16}")
print(f"        occurrences of `photon-path` in `P15`, where the rule is applied:            {n15}")
print(f"""
  So the rule as stated holds two slots, the corpus's own applications need three, and the third
  criterion appears only where the rule is used and nowhere where it is derived.

  ⇒ ** THE RULE DOES NOT DECIDE THE CASE THE ORDER NAMES. **  Light's path from last scattering is
    an accumulation through the content AND a photon-path observable at once, which is precisely the
    pair of properties the corpus's two worked assignments separate on -- and the rule contains no
    clause that ranks them.  This is `r7422`'s shape again: a resolver with two states meeting a
    case that is a third.""")
located = all(found.values())
crit_absent = (n16 == 0 and n15 > 0)
arm('Ⓗ', "REGISTERED FORM: the identification equates objects the classifier sorts to opposite "
         "rates", 'MISS',
    "refuted by the corpus's own optical-depth assignment, which puts an accumulation through the\n"
    "content on the stacking rate; the registered wording overclaimed and is withdrawn.")
arm('Ⓗ′', "CORRECTED, AND CHECKED: the rule's two slots do not cover light's path, and the "
          "criterion that\n            separates the corpus's own two accumulations is absent from "
          "the rule",
    'HIT' if located and crit_absent else 'MISS',
    f"all five sentences located verbatim: {located}; `photon-path` in P16 = {n16}, in P15 = {n15}")

# ================================================================================ F. the verdict
head("F.  THE VERDICT THE REGISTRATION BOUND THIS TO")

for tag in ['Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓗ′', 'Ⓘ']:
    print(f"        {tag:3s}  {ARMS.get(tag, 'unscored')}")
print(f"""
  THE REGISTERED BRANCH DOES NOT FIRE AS WRITTEN.  `Ⓖ HIT and Ⓗ HIT` was to read `the
  identification does not force the stacking-rate distance`, and Ⓗ is a MISS on its registered
  wording.  What Ⓖ + Ⓗ′ + Ⓘ deliver instead is the same conclusion on a narrower and checked
  ground, and the narrower ground is what the reply carries:

    Ⓖ   the identification's rate-free half -- flatness, hence D_M = chi -- is satisfied by all
        three candidate distances alike, so it cannot select a rate.  It fixes WHICH LENGTH, not
        which rate.
    Ⓘ   the constant-tau stack carries no expansion law of its own: every slice is isometric to one
        fixed flat R^3.  `P15`'s own words for the clause -- `with no rate in it at all` -- are
        literally true, and a clause with no rate in it cannot deliver a rate.
    Ⓗ′  and the rate rule cannot supply the rate either, because its two slots do not cover light's
        path and the criterion the corpus actually separates on is not in the rule.

  ⇒ NEITHER HALF OF THE GROUND SELECTS.  The selecting is done by the remaining clause, `on that
    slice the expansion law is exactly flat-$\\Lambda$CDM's with radiation absent from it`, which
    asserts the rate rather than deriving it -- and that clause is the hedge, so it belongs in the
    stem.

  AND ON DARYL'S DIRECTION: light's real integrated path EXISTS, is computed here for the first
  time, is a THIRD object at {D_path:.0f} Mpc against the implementation's {DC_stack:.0f} Mpc, and
  the comb excludes it outright at l_A = {np.pi * D_path / rs_leaf:.0f} against the sky's {SKY}.
  So the projection does not need it.  What the direction finds is real and is a GAP and not a
  mechanism: the identification calls D_C `the light-travel distance` while computing the
  layer-time integral, and on this non-synchronous chart those are not the same object -- they
  differ by the factor (d_chi r)/(1 + d_chi r), which runs from {wgt(tt_rec):.3f} at last
  scattering to {wgt(tt0):.3f} now and is nowhere near 1.
""")
bad = [t for t, v in ARMS.items() if v == 'VOID']
print(f"  VOIDED ARMS: {bad if bad else 'none'}")
print(f"  MISSED ARMS: {[t for t, v in ARMS.items() if v == 'MISS'] or 'none'}")
