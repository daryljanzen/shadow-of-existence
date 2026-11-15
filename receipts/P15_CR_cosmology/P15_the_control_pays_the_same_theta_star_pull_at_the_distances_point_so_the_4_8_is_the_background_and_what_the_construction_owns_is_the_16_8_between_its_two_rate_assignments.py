"""
** THE CONTROL PAYS THE SAME theta_* PULL AT THE DISTANCES' POINT, SO THE $+4.84\sigma$ IS THE
BACKGROUND'S AND NOT THE CONSTRUCTION'S -- AND WHAT THE CONSTRUCTION DOES OWN IS THE $16.757\sigma$
BETWEEN ITS TWO RATE ASSIGNMENTS, WHICH IS LARGER THAN THE PULL IT IS BEING CHARGED WITH. **

P15 prints the construction's theta_* pull on the corpus's definition at two points: $+4.84\sigma$
at the distances' point and $+2.33\sigma$ at the leaf-rate refit minimum.  The order (r7803, node 69)
asked how much of that belongs to the background and how much to the construction, and named the
discriminator: *"If the control also sits several sigma high at the distances' point, the +4.8 is the
background's tension between the baryon-acoustic and microwave data, not the construction's."*

** THE ANSWER IS 69'S FIRST BRANCH, AND IT IS NOT A CLOSE CALL -- IT IS AN IDENTITY. **  The corpus's
definition puts the sound horizon ALWAYS on `E_leaf`, and `E_leaf` IS flat LCDM's own E(z): matter,
radiation at the standard photon+neutrino density `WR/h^2`, and `Lambda = 1 - Om`.  So with the
projection distance also on the leaf rate BOTH integrals are LCDM's, and the construction's
leaf-rate theta_* at a parameter point and the LCDM control's theta_* at that same point are THE
SAME EXPRESSION.  They are equal to machine precision at equal `z_hi` (GATE 4), and the entire
difference between the printed $+4.837\sigma$ and the control's $+5.044\sigma$ is the upper limit of
the sound-horizon integral -- the construction stops at the arm's start $3\times10^{7}$, LCDM carries
it to infinity, and that limit is worth $+0.2072\sigma$.

** AND THE UN-REFITTED CONTROL, AT ITS OWN BACKGROUND POINT, PAYS VERY NEARLY THE SAME: **
$+4.944\sigma$ at Planck's $(67.40, 0.3150, 0.02237)$ against the construction's $+5.044\sigma$ at
the distances' point -- $0.101\sigma$ apart.  Neither background point is theta_*-matched on this
definition and both pay about five sigma for it.

  ⌗ ** WHAT THE CONSTRUCTION OWNS INSTEAD. **  At the distances' point the projection distance on
  the STACKING rate gives $-11.920\sigma$ and on the LEAF rate $+4.837\sigma$.  That swing,
  $16.757\sigma$, is purely the construction's choice of rate for the distance -- it is the one
  theta_* number here that LCDM cannot produce, and it is 3.464 times the pull the sentence is
  currently charging to the construction.

** A LIMIT ON HOW FAR THIS DEFINITION CAN BE PUSHED, MEASURED NOT ASSUMED (GATES 7-8). **  Against
CAMB's exact theta_* -- its own recombination, its own z_* -- the corpus's simplified definition
(trapezoid r_s at a fixed `z_rec = 1090`) runs high by between $+0.384\sigma$ and $+1.684\sigma$ across
the five points here, a point-to-point spread of $1.301\sigma$.  The first reading survives that by a
factor of 3.9 ($5.044$ against $1.301$).  ⛔ ** THE SECOND DOES NOT: ** the gap between the control's
refit minimum and the construction's is $+0.103\sigma$ on this definition and $-0.949\sigma$ on CAMB's
-- OPPOSITE IN SIGN.  So the sentence may say the $+4.8$ is the background's, and may NOT yet say
which arm's refit lands closer to Planck's angle.  On CAMB's exact calculation the control's own
refit minimum returns to Planck's angle ($+0.96\sigma$, against CAMB's $+1.12\sigma$ at Planck's own
published point) while the construction's stops $0.949\sigma$ short -- a reading this definition
cannot confirm and a measurement for whoever takes it next.

  ⌗ ** AND A THIRD THING, WHICH NOBODY ASKED FOR (GATE 10). **  Part of the un-refitted control's
  own pull is not a data tension at all but its background point's parameterisation: the corpus
  carries the control as $(67.40, \Omega_m\,0.3150)$, and deriving $\omega_c$ from that
  $\Omega_m$ at that $h$ gives $0.120727$, which is $+0.000727$ from Planck 2018 base LCDM's
  $0.1200$.  On CAMB that one difference carries $+2.44\sigma$ of the control's $+3.95\sigma$:
  swapping $\omega_c$ alone back to $0.1200$ at the same $H_0$ takes the control from
  $+3.95\sigma$ to $+1.51\sigma$, against $+1.12\sigma$ at Planck's own published point.  So "the
  background's tension" is the right attribution for the $+4.8$, but the control's own share of it
  is part DESI-versus-Planck and part the corpus's choice of control point.

** COMPUTES: ** nothing new.  `theta_corpus.py`'s background functions are EXECUTED FROM ITS OWN
SOURCE (the prefix up to its `POINTS` table), so there is no second copy of `E_leaf`, `E_stack`,
`D_M`, `r_snd` to drift; `r_snd`'s sample count is scaled with `z_hi` to hold the step in
`ln(1+z)` fixed.  The control's own refit minimum is not chosen here: it is parsed from
`refit_grid185/verify.sh`'s own recipe line, the command that produced the banked
`spectra/cc66_r185_verify_lcdm.npz`, and the 132-bin minimum is cross-read beside it.

Built r7803+cc66 (node 66, code seat), registered at
`computations/beyond_the_wall/r7803_cc66_theta_star_of_the_control/PREDICTION.md`.
11 gates, rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~1 min)
"""
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SRC = os.path.join(BW, 'r7749_70_leafgeom_refit', 'theta_corpus.py')
JSON = os.path.join(BW, 'r7749_70_leafgeom_refit', 'theta_corpus.json')
VSH = os.path.join(BW, 'refit_grid185', 'verify.sh')
SP = os.path.join(BW, 'spectra')
fail = []


def G(n, ok, msg):
    print(f"  {'✅' if ok else '⛔'} GATE {n}  {msg}")
    if not ok:
        fail.append(f'gate {n}: {msg}')


# ======================================================================================= GATE 1 ===
# The definition is LCDM's.  Parsed from theta_corpus.py's source, then checked NUMERICALLY against
# an independently written flat-LCDM E(z).
_txt = open(SRC).read()
_always_leaf = re.search(r'return r_snd\(H0, Om, wb, z_hi, ZREC, E_leaf\) / D_M\(ZREC, H0, Om, Egeom\)', _txt)
CORPUS = {'__file__': SRC, '__name__': 'theta_corpus_defs'}
exec(compile(_txt[:_txt.index('POINTS = {')], SRC, 'exec'), CORPUS)                       # noqa: S102
E_stack, E_leaf, D_M, r_snd = CORPUS['E_stack'], CORPUS['E_leaf'], CORPUS['D_M'], CORPUS['r_snd']
ZREC, TOBS, TSIG = CORPUS['ZREC'], CORPUS['THETA_OBS'], CORPUS['THETA_SIG']
WG, WR = CORPUS['WG'], CORPUS['WR']
_lits = (WG, WR, ZREC, TOBS, TSIG) == (2.47e-5, 4.15e-5, 1090.0, 0.0104085, 3.1e-6)


def E_lcdm(z, Om, h):
    """flat LCDM: matter + radiation at the standard photon+neutrino density + Lambda. Written here."""
    return np.sqrt(Om * (1.0 + z) ** 3 + (WR / h ** 2) * (1.0 + z) ** 4 + (1.0 - Om))


_zg = np.concatenate([np.linspace(0, 10, 97), np.logspace(1, 8, 211)])
_leaf_is_lcdm = max(float(np.max(np.abs(E_leaf(_zg, om, h) - E_lcdm(_zg, om, h))))
                    for om, h in ((0.2973, 0.686), (0.3150, 0.674), (0.309826, 0.6741)))
# relative, because at z = 1e8 the radiation term is ~1e28 and subtracting it costs the last bits
_stack_has_no_rad = max(float(np.max(np.abs(E_stack(_zg, om, h) ** 2
                                            - (E_lcdm(_zg, om, h) ** 2 - (WR / h ** 2) * (1 + _zg) ** 4))
                                     / E_lcdm(_zg, om, h) ** 2))
                        for om, h in ((0.2973, 0.686), (0.3150, 0.674)))
G(1, bool(_always_leaf) and _lits and _leaf_is_lcdm == 0.0 and _stack_has_no_rad < 1e-15,
  f"the definition is LCDM's: r_snd unconditionally on E_leaf ({bool(_always_leaf)}), the five "
  f"literals as banked ({_lits}), E_leaf - E_lcdm = {_leaf_is_lcdm:.3g} EXACTLY, and E_stack is "
  f"E_leaf with the radiation term removed to {_stack_has_no_rad:.3g} RELATIVE)")


# ======================================================================================= GATE 2 ===
# theta_corpus's own three points reproduced from its own functions, at its own z_hi.
def theta_at(H0, Om, wb, z_hi, Egeom):
    """theta_corpus's theta(), with r_snd's sample count scaled so the step in ln(1+z) is held fixed
    as z_hi grows.  The scaling turns out NOT to be load-bearing -- failability.py's probe 2 found
    that r_snd's default n=60000 is already converged out to z_hi=1e14, because in u=ln(1+z) the
    integrand falls as (1+z)^-1 once radiation dominates E, so the added range contributes almost
    nothing.  It is kept because it costs nothing and makes the convergence independent of n."""
    span, ref = np.log(1 + z_hi) - np.log(1 + ZREC), np.log(1 + 3e7) - np.log(1 + ZREC)
    n = int(round(60000 * max(1.0, span / ref)))
    return r_snd(H0, Om, wb, z_hi, ZREC, E_leaf, n=n) / D_M(ZREC, H0, Om, Egeom)


def pull(t):
    return (t - TOBS) / TSIG


DIST = (68.60, 0.2973, 0.02237)
AOR = (68.570730, 0.291246, 0.021643)
LEAF = (68.585672, 0.294463, 0.022181)
import json                                                                              # noqa: E402
BANK = json.load(open(JSON))
_pre = {'dist': "distances' point", 'aor': 'arm of record refit point',
        'leaf': 'leaf-rate refit minimum'}
_keys = {t: next(k for k in BANK if k.startswith(v)) for t, v in _pre.items()}
assert len(set(_keys.values())) == 3, 'theta_corpus.json no longer carries three distinct points'
_AR, _LF = 'arm of record (D_M on stacking rate)', 'leaf-rate assignment (D_M on leaf rate)'
_worst, _n = 0.0, 0
for tag, p in (('dist', DIST), ('aor', AOR), ('leaf', LEAF)):
    for gname, Eg in ((_AR, E_stack), (_LF, E_leaf)):
        got = theta_at(*p, 3e7, Eg)
        _worst = max(_worst, abs(got - BANK[_keys[tag]][gname]['theta_zstart']))
        _n += 1
P_DIST_CR = pull(theta_at(*DIST, 3e7, E_leaf))
P_DIST_STACK = pull(theta_at(*DIST, 3e7, E_stack))
P_LEAF_CR = pull(theta_at(*LEAF, 3e7, E_leaf))
G(2, _worst < 1e-12 and _n == 6 and abs(round(P_DIST_CR, 2) - 4.84) < 1e-9
  and abs(round(P_LEAF_CR, 2) - 2.33) < 1e-9,
  f"70's banked theta_corpus.json reproduced from its own functions: {_n}/6 values, worst "
  f"|delta theta| {_worst:.3g}; P15's two printed pulls come back as {P_DIST_CR:+.3f} -> "
  f"{round(P_DIST_CR, 2):+.2f} and {P_LEAF_CR:+.3f} -> {round(P_LEAF_CR, 2):+.2f}")


# ======================================================================================= GATE 3 ===
# The z_hi -> infinity limit converges, and its reach is measured.
_t = {z: theta_at(*DIST, z, E_leaf) for z in (3e7, 1e8, 1e12, 1e14)}
CONV = abs(100 * (_t[1e14] - _t[1e12]))
REACH = pull(_t[1e14]) - pull(_t[3e7])
G(3, CONV < 1e-8 and abs(REACH - 0.2072) < 0.002 and abs(pull(_t[1e8]) - pull(_t[3e7]) - 0.1450) < 0.002,
  f"the limit converges: 100theta* at z_hi=1e12 and 1e14 agree to {CONV:.2g} in 100theta*, which "
  f"is {CONV / (100 * TSIG):.1g} sigma; the reach from the "
  f"arm's start 3e7 to infinity is {REACH:+.4f} sigma, of which 3e7->1e8 is "
  f"{pull(_t[1e8]) - pull(_t[3e7]):+.4f} -- so the 0.2-sigma bound registered in PREDICTION.md "
  f"from the 1e8 step was 0.0072 sigma too tight, and prediction (1) is FALSIFIED AS STATED -- "
  f"its substance held (+5.044 is inside the registered +4.7..+5.1) but its tolerance was taken "
  f"from the 3e7->1e8 step when the quantity it bounded is the 3e7->infinity reach")


# ======================================================================================= GATE 4 ===
# THE IDENTITY: at the same point and the same z_hi the control and the construction's leaf-rate
# assignment are the same expression, so they agree to machine precision -- bit-identical, not close.
_id = max(abs(theta_at(*p, z, E_leaf) - theta_at(*p, z, E_lcdm))
          for p in (DIST, AOR, LEAF) for z in (3e7, 1e8, 1e12))
P_DIST_CTL = pull(_t[1e14])
G(4, _id == 0.0 and abs(P_DIST_CTL - 5.044) < 0.004 and abs(P_DIST_CTL - P_DIST_CR - 0.2068) < 0.002,
  f"the control AT THE DISTANCES' POINT is the construction's leaf-rate theta_*: substituting an "
  f"independently written flat-LCDM E(z) for E_leaf moves theta_* by {_id:.3g} at 9 of 9 "
  f"point/limit combinations.  The control's pull there is {P_DIST_CTL:+.3f} sigma against the "
  f"printed {P_DIST_CR:+.3f}; ALL the construction adds is the limit, "
  f"{P_DIST_CTL - P_DIST_CR:+.4f} sigma  ⇒ PREDICTION (2) HELD: the +4.84 is the BACKGROUND'S")


# ======================================================================================= GATE 5 ===
# The control's own refit minimum is not chosen here: it is the recipe that made the banked spectrum.
_vsh = open(VSH).read()
_mc = re.search(r'verify_lcdm\s+ARM=lcdm LH0=([\d.]+) LOM=([\d.]+) WBH2=([\d.]+) NS=([\d.]+)', _vsh)
_ma = re.search(r'verify_cr\s+ARM=cr CRH0=([\d.]+) CROM=([\d.]+)', _vsh)
CTL185 = tuple(float(g) for g in _mc.groups()[:3]) if _mc else None
_bank_arm = None
if os.path.exists(os.path.join(SP, 'cc66_r185_verify_lcdm.npz')):
    with np.load(os.path.join(SP, 'cc66_r185_verify_lcdm.npz'), allow_pickle=True) as z:
        _bank_arm = str(z['arm'].item() if z['arm'].shape == () else z['arm'])
CTL132 = (67.4054, 0.3095, 0.0220)
PLANCK = (67.40, 0.3150, 0.02237)
P_CTL185 = pull(theta_at(*CTL185, 1e14, E_leaf)) if CTL185 else None
P_CTL132 = pull(theta_at(*CTL132, 1e14, E_leaf))
P_PLANCK = pull(theta_at(*PLANCK, 1e14, E_leaf))
P_LEAF_INF = pull(theta_at(*LEAF, 1e14, E_leaf))
G(5, CTL185 == (67.410309, 0.309826, 0.021966) and _bank_arm == 'lcdm' and bool(_ma)
  and abs(P_CTL185 - 2.643) < 0.004 and abs(P_CTL132 - 1.489) < 0.004 and abs(P_PLANCK - 4.944) < 0.004,
  f"the control's own refit minimum is parsed from the recipe that made the bank: "
  f"verify.sh gives {CTL185} and spectra/cc66_r185_verify_lcdm.npz carries arm={_bank_arm!r}, the "
  f"like-for-like companion of its own verify_cr line.  Pulls: own 185-bin minimum "
  f"{P_CTL185:+.3f}, own 132-bin minimum {P_CTL132:+.3f}, Planck's un-refitted point "
  f"{P_PLANCK:+.3f}  ⇒ PREDICTION (4) HELD on this definition (+1 to +5 predicted)")


# ======================================================================================= GATE 6 ===
# What the construction owns: the swing between its two rate assignments.
SWING = P_DIST_CR - P_DIST_STACK
G(6, abs(P_DIST_STACK + 11.920) < 0.004 and abs(SWING - 16.757) < 0.006 and SWING > abs(P_DIST_CR),
  f"what the construction owns at the distances' point is the RATE ASSIGNMENT: the projection "
  f"distance on the stacking rate gives {P_DIST_STACK:+.3f} sigma and on the leaf rate "
  f"{P_DIST_CR:+.3f}, a swing of {SWING:.3f} sigma -- {SWING / abs(P_DIST_CR):.2f} times the pull "
  f"the sentence charges to the construction  ⇒ PREDICTION (3) HELD (16.7-16.8 predicted)")


# ======================================================================================= GATE 7 ===
# How far this definition can be pushed: measured against CAMB's exact theta_*, not assumed.
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                              # noqa: E402


def camb_theta(H0, Om, wb):
    h = H0 / 100.0
    pars = camb.set_params(H0=H0, ombh2=wb, omch2=Om * h ** 2 - wb, mnu=0.06, omk=0, tau=0.054,
                           As=2.1e-9, ns=0.965, lmax=2500)
    return camb.get_background(pars).get_derived_params()['thetastar'] / 100.0


CPTS = [('Planck, un-refitted', PLANCK), ("control, own 185-bin minimum", CTL185),
        ('control, own 132-bin minimum', CTL132), ("distances' point", DIST),
        ('leaf-rate refit minimum', LEAF)]
BIAS, CAMBP = {}, {}
for nm, p in CPTS:
    CAMBP[nm] = pull(camb_theta(*p))
    BIAS[nm] = pull(theta_at(*p, 1e14, E_leaf)) - CAMBP[nm]
BLO, BHI = min(BIAS.values()), max(BIAS.values())
SPREAD = BHI - BLO
G(7, 0.30 < BLO < 0.45 and 1.60 < BHI < 1.76 and abs(SPREAD - 1.31) < 0.06 and all(b > 0 for b in BIAS.values()),
  f"the definition's own bias, measured against CAMB's exact theta_*: it runs HIGH at all 5 points, "
  f"by between {BLO:+.3f} and {BHI:+.3f} sigma -- a point-to-point spread of {SPREAD:.3f} sigma. "
  f"(lowest at the distances' point, highest at the control's 185-bin minimum)")


# ======================================================================================= GATE 8 ===
# THE CONSEQUENCE: the first reading survives that systematic by a factor of 3.9; the second reverses.
GAP_CORPUS = P_CTL185 - P_LEAF_INF
GAP_CAMB = CAMBP['control, own 185-bin minimum'] - CAMBP['leaf-rate refit minimum']
G(8, P_DIST_CTL / SPREAD > 3.5 and abs(GAP_CORPUS) < SPREAD and GAP_CORPUS * GAP_CAMB < 0
  and abs(GAP_CORPUS - 0.103) < 0.006 and abs(GAP_CAMB + 0.95) < 0.05,
  f"so the first reading is carried and the second is not: {P_DIST_CTL:+.3f} sigma against a "
  f"{SPREAD:.3f}-sigma systematic is a factor of {P_DIST_CTL / SPREAD:.1f}, but the control-minus-"
  f"construction gap at the two refit minima is {GAP_CORPUS:+.3f} on this definition and "
  f"{GAP_CAMB:+.3f} on CAMB's -- SMALLER THAN THE SYSTEMATIC AND OPPOSITE IN SIGN.  On CAMB the "
  f"control's refit returns to Planck's angle ({CAMBP['control, own 185-bin minimum']:+.2f} against "
  f"{CAMBP['Planck, un-refitted']:+.2f} un-refitted) and the construction's stops "
  f"{abs(GAP_CAMB):.2f} sigma short")


# ======================================================================================= GATE 9 ===
# Both arms' refits move the same way and by the same amount -- on BOTH definitions.
MV_CR = P_LEAF_INF - P_DIST_CTL
MV_CTL = P_CTL185 - P_PLANCK
MV_CR_C = CAMBP['leaf-rate refit minimum'] - CAMBP["distances' point"]
MV_CTL_C = CAMBP['control, own 185-bin minimum'] - CAMBP['Planck, un-refitted']
_ratio, _ratio_c = MV_CR / MV_CTL, MV_CR_C / MV_CTL_C
G(9, MV_CR < 0 and MV_CTL < 0 and MV_CR_C < 0 and MV_CTL_C < 0
  and 1 / 3 < _ratio < 3 and 1 / 3 < _ratio_c < 3 and abs(_ratio - 1.088) < 0.02,
  f"the refit buys both sides the same relief: construction {P_DIST_CTL:+.3f} -> {P_LEAF_INF:+.3f} "
  f"({MV_CR:+.3f}) and control {P_PLANCK:+.3f} -> {P_CTL185:+.3f} ({MV_CTL:+.3f}), ratio "
  f"{_ratio:.3f}; on CAMB {MV_CR_C:+.2f} and {MV_CTL_C:+.2f}, ratio {_ratio_c:.3f}  ⇒ PREDICTION "
  f"(5) HELD on the magnitudes; its 'neither reaches it' half FAILS for the control on CAMB's "
  f"exact calculation, where the control's refit does reach Planck's angle")


# ====================================================================================== GATE 10 ===
# WHY the un-refitted control sits four sigma high: its background point is not Planck's.  The corpus
# carries the control as (67.40, Om 0.3150), and deriving omega_c from that Om at that h gives
# 0.120727 -- 0.0007 ABOVE Planck 2018 base LCDM's 0.1200.  Planck's own published point is run here
# so the control's zero is visible rather than assumed.
WC_CORPUS = 0.3150 * 0.674 ** 2 - 0.02237
WC_PLANCK = 0.1200
H0_PUB, WB_PUB = 67.36, 0.02237
OM_PUB = (WC_PLANCK + WB_PUB) / (H0_PUB / 100.0) ** 2
P_PUB_CAMB = pull(camb_theta(H0_PUB, OM_PUB, WB_PUB))
P_PUB_CORPUS = pull(theta_at(H0_PUB, OM_PUB, WB_PUB, 1e14, E_leaf))
OM_SWAP = (WC_PLANCK + 0.02237) / 0.674 ** 2          # the corpus's H0, Planck's omega_c
P_SWAP_CAMB = pull(camb_theta(67.40, OM_SWAP, 0.02237))
G(10, abs(WC_CORPUS - 0.120727) < 5e-6 and abs(P_PUB_CAMB - 1.12) < 0.05
  and abs(P_SWAP_CAMB - 1.51) < 0.05 and P_PUB_CAMB < CAMBP['Planck, un-refitted'] - 2.5,
  f"the un-refitted control's four sigma is its BACKGROUND POINT, not the data: the corpus carries "
  f"the control as (67.40, Om 0.3150), whose derived omega_c is {WC_CORPUS:.6f} -- "
  f"{WC_CORPUS - WC_PLANCK:+.6f} from Planck 2018 base LCDM's {WC_PLANCK}.  CAMB puts Planck's own "
  f"published point (67.36, omega_c 0.1200) at {P_PUB_CAMB:+.2f} sigma and the corpus's control "
  f"background at {CAMBP['Planck, un-refitted']:+.2f}; swapping ONLY omega_c back to 0.1200 at the "
  f"same H0 recovers {P_SWAP_CAMB:+.2f}, so the derived omega_c carries "
  f"{CAMBP['Planck, un-refitted'] - P_SWAP_CAMB:+.2f} of it (the corpus's own definition puts that "
  f"published point at {P_PUB_CORPUS:+.2f})")


# ====================================================================================== GATE 11 ===
# EVERY FIGURE THE INDEX ROW PRINTS, PINNED HERE -- and each pin checked against
# check_figures_pinned's OWN allowance, max(0.5*10**-decimals, 5e-4*|x|), because a tolerance looser
# than that allowance does not count as a pin at all (the lesson r7799 and r7801 each paid for).
def allowance(printed):
    x = float(printed)
    return max(0.5 * 10 ** -len(printed.split('.')[1]), 5e-4 * abs(x))


# Each figure is pinned by an EXPLICIT comparison against a LITERAL, because check_figures_pinned
# parses this source: a pin whose constant lives in a data structure is invisible to it, the same
# way a tuple equality is not a pin.  `allowance` recomputes the gate's own tolerance ceiling,
# max(0.5*10**-decimals, 5e-4*|x|), and GATE 11 asserts every pin below is inside it -- which caught
# two of my own printings mid-build (3.464 does not round to 3.46 within the allowance, and 0.100779
# rounds to 0.101, not 0.100).
PINNED = [
    ('5.044', abs(P_DIST_CTL - 5.044) < 0.002, 0.002, "the control at the distances' point"),
    ('4.837', abs(P_DIST_CR - 4.837) < 0.002, 0.002, "the construction's leaf-rate pull there"),
    ('11.920', abs(abs(P_DIST_STACK) - 11.920) < 0.004, 0.004, 'the arm of record at that point'),
    ('16.757', abs(SWING - 16.757) < 0.006, 0.006, 'the swing between the two rate assignments'),
    ('3.464', abs(SWING / abs(P_DIST_CR) - 3.464) < 0.0015, 0.0015, 'that swing over the charged pull'),
    ('0.207', abs(REACH - 0.207) < 0.0004, 0.0004, "the limit's whole reach to infinity"),
    ('4.944', abs(P_PLANCK - 4.944) < 0.002, 0.002, 'the un-refitted control at its background'),
    ('2.643', abs(P_CTL185 - 2.643) < 0.001, 0.001, "the control at its OWN 185-bin minimum"),
    ('1.489', abs(P_CTL132 - 1.489) < 0.0005, 0.0005, "the control at its own 132-bin minimum"),
    ('2.540', abs(P_LEAF_INF - 2.540) < 0.001, 0.001, 'the construction at the leaf-rate minimum'),
    ('0.101', abs((P_DIST_CTL - P_PLANCK) - 0.101) < 0.0004, 0.0004, 'each at its own background'),
    ('0.103', abs(GAP_CORPUS - 0.103) < 0.0004, 0.0004, 'control minus construction, both refitted'),
    ('2.505', abs(abs(MV_CR) - 2.505) < 0.001, 0.001, "the construction's refit relief"),
    ('2.301', abs(abs(MV_CTL) - 2.301) < 0.001, 0.001, "the control's refit relief"),
    ('67.410309', abs(CTL185[0] - 67.410309) < 0.00001, 0.00001, "the control's minimum, H0"),
    ('0.309826', abs(CTL185[1] - 0.309826) < 0.00001, 0.00001, "the control's minimum, Omega_m"),
    ('0.021966', abs(CTL185[2] - 0.021966) < 0.000005, 0.000005, "the control's minimum, omega_b"),
    ('68.60', abs(DIST[0] - 68.60) < 0.001, 0.001, "the distances' point, H0"),
    ('0.2973', abs(DIST[1] - 0.2973) < 0.00005, 0.00005, "the distances' point, Omega_m"),
    ('67.40', abs(PLANCK[0] - 67.40) < 0.001, 0.001, "the control background, H0"),
    ('0.3150', abs(PLANCK[1] - 0.3150) < 0.00005, 0.00005, 'the control background, Omega_m'),
    ('0.120727', abs(WC_CORPUS - 0.120727) < 0.00001, 0.00001, "that background's DERIVED omega_c"),
    ('0.1200', abs(WC_PLANCK - 0.1200) < 0.00001, 0.00001, "Planck 2018 base LCDM's omega_c"),
    ('1090.0', abs(ZREC - 1090.0) < 0.1, 0.1, 'z_rec, inherited'),
    ('0.0104085', abs(TOBS - 0.0104085) < 0.000001, 0.000001, 'theta_obs, inherited'),
]


def allowance(printed):
    x = float(printed)
    return max(0.5 * 10 ** -len(printed.split('.')[1]), 5e-4 * abs(x))


_unheld = [(t, w) for t, ok, tol, w in PINNED if not ok]
_slack = [(t, tol, allowance(t)) for t, ok, tol, w in PINNED if tol > allowance(t) * (1 + 1e-9)]
G(11, not _unheld and not _slack and len(PINNED) == 25,
  f"all {len(PINNED)} figures the INDEX row prints hold against an explicit literal comparison here, "
  f"and every one of those pins is inside check_figures_pinned's own allowance "
  f"max(0.5*10**-d, 5e-4*|x|) -- tightest margin "
  f"{min(allowance(t) / tol for t, ok, tol, w in PINNED):.2f}x"
  + ('' if not _unheld else f'  -- UNHELD: {_unheld}')
  + ('' if not _slack else f'  -- LOOSER THAN THE ALLOWANCE, so not pins at all: {_slack}'))

print()
print('  ' + '=' * 100)
if fail:
    print('  ⛔ ' + f'{len(fail)} GATE(S) FAILED:')
    for f in fail:
        print(f'     - {f}')
    raise SystemExit(1)
print("  ⇒ ⛔⛔ ** THE CONTROL SITS AT "
      f"{P_DIST_CTL:+.3f} SIGMA AT THE DISTANCES' POINT -- 69'S FIRST BRANCH. **  The construction's")
print(f"  leaf-rate theta_* at a point IS the control's theta_* at that point, the same expression; "
      f"the whole")
print(f"  difference from the printed {P_DIST_CR:+.3f} is the sound-horizon integral's upper limit, "
      f"{REACH:+.4f} sigma.")
print(f"  ** SO THE +4.84 IS THE BACKGROUND'S TENSION BETWEEN THE BARYON-ACOUSTIC AND THE MICROWAVE "
      f"DATA. **")
print(f"  ⌗ And what the construction DOES own is the {SWING:.3f} sigma between its two rate "
      f"assignments --")
print(f"    {P_DIST_STACK:+.3f} on the stacking rate against {P_DIST_CR:+.3f} on the leaf rate -- "
      f"which is {SWING / abs(P_DIST_CR):.2f} times")
print(f"    the pull the sentence is currently charging to it.  ⛔ The definition's own "
      f"{SPREAD:.3f}-sigma spread")
print(f"    carries that reading by a factor of {P_DIST_CTL / SPREAD:.1f} and does NOT carry the "
      f"comparison of the two refit")
print(f"    minima, which reverses sign ({GAP_CORPUS:+.3f} here, {GAP_CAMB:+.3f} on CAMB's exact "
      f"theta_*).")
print('  ' + '=' * 100)
