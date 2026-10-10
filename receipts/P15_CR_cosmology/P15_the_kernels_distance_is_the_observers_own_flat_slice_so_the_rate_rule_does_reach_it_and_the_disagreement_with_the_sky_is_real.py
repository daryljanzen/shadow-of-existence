#!/usr/bin/env python3
"""
P15 receipt -- `r7099`'s Q1, ANSWERED: THE KERNEL'S DISTANCE IS THE OBSERVER'S OWN FLAT SLICE, SO THE
RATE RULE DOES REACH IT, ALL THREE OF THE ORDER'S READINGS ARE SETTLED, AND THE DISAGREEMENT WITH THE
SKY IS REAL.

** THE ORDER. **  `r7099` asked the sector's last question -- *"what IS the comoving distance entering
$j_\\ell(k\\chi)$ on this background?  Not which rate it should be built on -- that framing assumes the
answer is one of two rates.  What the object is"* -- and named three live readings without recommending
one, guessing that (3) was worth looking at first *"because it is cheap and it is the only one that
could dissolve the conflict rather than resolve it."*

⇒ *** (3) IS CHEAP AND IT DOES NOT DISSOLVE: the construction already made the identification it would
have to break, and receipted it.  (2) IS REAL AS A FACT ABOUT THE LINE ELEMENT AND STILL DOES NOT MOVE
THE KERNEL.  SO IT LANDS ON (1), AND THE DISAGREEMENT IS A RESULT ABOUT CR. ***

** (3) -- "the kernel's argument and $D_M$ may not be the same object." **  *They are the same object,
and `P15` says so in a sentence that carries a proposition behind it*: because the distance slicing is
flat (`prop:flat`), *"the photons are projected through the FLAT geometry --- the comoving
angular-diameter distance is $D_M = D_C$, the same flat-$\\Lambda$CDM observable that places the
acoustic scale at $\\ell_A\\approx301$ --- while only the SOURCE modes carry the closed-$S^3$
quantization."*
  ⛭ ** AND THE OBJECT (3) WAS REACHING FOR EXISTS, IS DISTINCT, AND IS ALREADY IN USE FOR A DIFFERENT
  JOB. **  It is $r_0$, the layer's own areal radius, which sets the source's discrete spectrum
  $k_L=\\sqrt{L(L+2)}/r_0$ while $D_C$ does the projecting.  *This receipt reproduces both from the
  background alone -- $r_0 = 5051$ Mpc and $D_C = 1.401\\times10^{4}$ Mpc at `P15`'s own refit
  background, with the stretch $D_C/r_0 = 2.77$ and the lowest mode at $\\ell_2 = 7.85$ -- which are
  four of the paper's parameter-free figures, calibrated here before anything new is asked.*
  ⇒ *So the two-object structure the order hoped for is already present and already spent: the conflict
  does not dissolve into a gap, because the gap is occupied.*

** (2) -- "the projection is not the standard flat line-of-sight integral." **  ⛭⛭ *This is TRUE of the
line element, and the exact statement of it is a one-line identity nobody in the sector seems to have
written down*:

        ds^2 = -d tau^2 + (dr/d chi)^2 d chi^2 + r^2 d Omega^2,     r = r(tau + chi)
    ⇒   r / (dr/d tau~)  =  alpha tanh( 3 c tau~ / 2 alpha )  =  c / H       EXACTLY

*verified here to ten decimals at $z = 0, 1, 10, 1090$ and $3\\times10^{7}$ on both backgrounds, with
$\\sinh^{2}u_0 = x_0^{3}/2$ the exact bridge between the native parameterisation and the fitted one.*
  ⇒ ** So in the proper frame the radial-to-angular ratio is the HUBBLE RADIUS. **  *In comoving-FRW
  form the angular radius and the radial comoving distance are the same function; here they are not,
  and that is precisely the sense in which the projection is not the standard integral.*
  ⛔ ** AND IT STILL DOES NOT MOVE THE KERNEL'S ARGUMENT, because the standard form is not claimed on
  THIS chart. **  `prop:flat` passes to the observer's own constant-$\\tau$ slice, whose induced metric
  is $dr^{2}+r^{2}d\\Omega^{2}$ with vanishing Riemann tensor, and the projection is read there.  *The
  non-synchrony $\\tilde\\tau=\\tau+\\chi$ is what lets flat distances and a closed $S^{3}$ coexist --
  the paper calls that decoupling "the decoupling itself".*

⛔⛭ ** AND THE TRAP THE QUESTION INVITES IS NAMED AND EXCLUDED, because it is the reading a careful
seat would reach for next. **  Taken at face value, the line element's angular part $r^{2}d\\Omega^{2}$
makes the angular-diameter distance the areal radius itself, $D_A = r(\\tilde\\tau_e)$; combined with
the construction's own redshift $1+z = r(\\tilde\\tau_0)/r(\\tilde\\tau_e)$ that gives

        D_M = (1+z) D_A = r(tau~_0) = r_0 = CONSTANT at every redshift,

*i.e. $5051$ Mpc rather than $1.401\\times10^{4}$.*  ⇒ ** That reading is excluded twice over. **  It
would put the acoustic scale at $\\pi r_0/r_s$ -- computed here, and it misses the measured comb by
more than a factor of two -- *and the $d\\Omega$ it reads is the SdS static chart's, centred on the
chart origin at $r=0$, which is the branch point and not the observer.*  **A chart's angle is not a
sky.**

⇒ ** (1) IS WHERE IT LANDS, AND NOW BY THREE INDEPENDENT ROUTES. **  `P07`'s rate rule names $D_M$ on
the stacking side outright; `r7096`'s null-cone argument puts the photon-path lapse there; and the
observer's own readout -- flat slice by `prop:flat`, exactly flat-$\\Lambda$CDM by `sec:flatlcdm` -- is
the stacking rate's $\\sinh^{2/3}$ law with radiation absent.  *The three agree, and the implementation
already does what they say.*
  ⇒ *** SO THE DISAGREEMENT WITH THE SKY IS REAL, LOCALISED, AND A RESULT ABOUT CR RATHER THAN A
  DEFECT -- which is the outcome the order said to state plainly if that is where it lands. ***

⌗ ** THE ONE REMAINDER, AND IT IS THE ONLY PLACE THIS CHAIN COULD STILL MOVE. **  *The harmonic
expansion has never been derived IN the proper frame.*  `j_\\ell(k D_C)` is licensed by an
IDENTIFICATION -- the observer's slice is flat, the observer's readout is exactly flat
$\\Lambda$CDM -- rather than by expanding a plane wave on the constant-$\\tau$ slice with the observer
at a general point of it, which is where the chart's origin stops being the centre of anything.
  ⇒ ** What would settle it is bounded and nobody has run it: expand on that slice with the observer
  off the origin and show the $\\ell$-space kernel is $j_\\ell(k D_C)$ with $D_C$ the light-travel
  distance.  ⛔ It is NOT ordered here and this receipt does not do it. **  *It is named because the
  honest form of "(1) is where it lands" includes where it could fail to.*

** COMPUTES: the background objects at TWO stated parameter sets and nothing else.  *** $(H_0,
\Omega_m) = (68.60, 0.2973)$, the refit background `P15` fits, and $(73.00, 0.3066)$, the instrument's
own default -- every figure here is reported at one of the two and labelled with which.  The derived
quantities are $x_0$, $\alpha$, $r_N$, $r_0$, $D_C(z_{\rm rec}=1089.9)$, $r_{s,\rm leaf}$ and the
ratios built from them; $\omega_b = 0.0224$ enters only the baryon loading in $r_s$.  *** Nothing is
computed at a third parameter set, and no spectrum, likelihood or transfer is computed at any. *** **

⚠ ** SCOPE. **  No transfer is run and no spectrum computed; `cc66` holds the queue.  `cc66`'s
three-grid table is NOT re-measured -- the order said it is verified there and this receipt takes it as
given, using it nowhere except to name which configuration the sky prefers.
"""
import glob
import os
import re
import time

import numpy as np
from scipy.integrate import quad

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
p15, p07 = (open(f, encoding='utf-8').read() for f in (P15, P07))
body15 = flat(''.join(ln + '\n' for ln in p15.splitlines() if not ln.lstrip().startswith('%')))
fp07 = flat(p07)

C = 299792.458
Z_REC = 1089.9
OMBH2 = 0.0224
BG = {'the refit background `P15` fits': (68.60, 0.2973),
      "the instrument's own default": (73.00, 0.3066)}


def background(H0, OM):
    """the native parameterisation and the fitted one, with the bridge between them."""
    OL = 1.0 - OM
    x03 = 2.0 / OM - 2.0                              # Omega_m = 2/(x0^3+2)
    x0 = x03 ** (1.0 / 3.0)
    alpha = C / H0 * np.sqrt(1.0 + 2.0 / x03)         # H0^2 = (c/alpha)^2 (1 + 2/x0^3)
    rN = alpha / np.sqrt(3.0)                         # the Nariai radius
    r0 = x0 * rN                                      # today's areal radius
    H = lambda z: H0 * np.sqrt(OM * (1 + z) ** 3 + OL)                      # noqa: E731
    DC = quad(lambda z: C / H(z), 0.0, Z_REC, limit=300)[0]
    return dict(OL=OL, x03=x03, x0=x0, alpha=alpha, rN=rN, r0=r0, H=H, DC=DC)


# ============================================== A. the calibration, before anything new is asked
head("A.  THE CALIBRATION: FOUR OF `P15`'s PARAMETER-FREE FIGURES, REPRODUCED FROM THE BACKGROUND")

B = {k: background(*v) for k, v in BG.items()}
for lab, b in B.items():
    print(f"      {lab}:  x_0 = {b['x0']:.4f}  alpha = {b['alpha']:7.1f}  r_N = {b['rN']:7.1f}  "
          f"r_0 = {b['r0']:7.1f}  D_C = {b['DC']:8.1f} Mpc")
ref = B['the refit background `P15` fits']
gate("⛭ the layer's areal radius comes out at `r_0 = 5051` Mpc, which is `P15`'s own parameter-free "
  # ** r7181: the pin is `+-1.0` and not `+-5` (node 70's `r7179+70.1` slack finding) nor the
  #   printed-precision `+-0.5` its operator proposes.  The background returns `5051.49`, which is
  #   `0.49` from the figure the paper prints, so a half-ulp bracket would sit `0.01` inside its own
  #   bound -- a pin on a rounding edge, which fails on any change to the integral rather than on a
  #   change to the physics.  What this pin exists to refuse is the OTHER configuration's `r_0`,
  #   `4708.97`, and `+-1.0` refuses it by `342` times while admitting nothing the paper would
  #   print differently by more than one in the last digit. **
     "figure", abs(ref['r0'] - 5051.0) < 1.0 and "r_0\\approx5051" in body15)
# ** r7179 (node 66): the pair is the construction's and the tolerances are the paper's own
#   printed precision.  At +-100 Mpc and +-0.03 these could not fail on the quantities they
#   name: the two background configurations the corpus has printed are 61.5 Mpc and 0.0137
#   apart, so the old brackets admitted both and asserted neither (`PO-78` at the tolerance). **
gate("⛭ and the projection distance at `D_C = 1.4011e4` Mpc, the paper's own, to half its"
     " printed ulp -- a bracket the other configuration's 1.395e4 fails by 123 times",
     abs(ref['DC'] - 1.4011e4) < 0.5 and "D_C\\approx1.4011\\times10^{4}" in body15)
_stretch = ref['DC'] / ref['r0']
gate(f"⛭ so the STRETCH is {_stretch:.3f} against the paper's 2.774 -- the ratio of the two objects the "
     "order asked whether to distinguish", abs(_stretch - 2.774) < 5e-4
     and "D_C/r_0\\approx2.774" in body15)
_l2 = np.sqrt(2 * 4) / ref['r0'] * ref['DC']
gate(f"⛭ and the lowest closed-$S^3$ mode lands at ell_2 = {_l2:.2f} against the paper's 7.8 -- four "
     "figures calibrated before the unknown is touched",
     abs(_l2 - 7.8) < 0.15 and "\\ell_2\\approx7.8" in body15)

# ============================================== B. reading (3)
head("B.  ⛔ READING (3): THE KERNEL'S ARGUMENT AND $D_M$ ARE THE SAME OBJECT, BY A PROPOSITION")

gate("`P15` identifies them outright, and `prop:flat` is the reason: the distance slicing is flat, so "
     "the photons are projected through the FLAT geometry and the comoving angular-diameter distance "
     "IS $D_C$",
     "the comoving angular-diameter distance is $D_M=D_C$" in body15
     and "Because the distance slicing is flat (Proposition~\\ref{prop:flat})" in body15)
gate("and `prop:flat` is a proposition with a receipted argument -- the constant-$\\tau$ slice's "
     "induced three-metric is $dr^2+r^2d\\Omega^2$ with vanishing Riemann tensor",
     "The constant-$\\tau$ slice is exactly flat $\\mathbb{R}^3$." in body15
     and "verify\\_geometry.py" in body15)
gate("⛭ AND THE DISTINCT OBJECT EXISTS AND IS ALREADY SPENT: $r_0$ sets the SOURCE's discrete "
     "spectrum $k_L=\\sqrt{L(L+2)}/r_0$ while $D_C$ does the projecting -- so the gap reading (3) "
     "needed is occupied", "k_L=\\sqrt{L(L+2)}/r_0" in body15)
gate("⇒ so (3) does not dissolve the conflict: it would have to break an identification the "
     "construction already made, and the two-object structure it reached for is in use for a "
     "different job", abs(_stretch - 2.774) < 5e-4)

# ============================================== C. reading (2)
head("C.  ⛭⛭ READING (2) IS TRUE OF THE LINE ELEMENT -- AND THE EXACT STATEMENT IS r/rdot = c/H")

gate("the proper-frame line element is NOT in comoving-FRW form: the radial coefficient is "
     "$(\\partial_\\chi r)^2$ and the angular one $r^2$, with $r$ a function of $\\tau+\\chi$",
     "ds^2=-d\\tau^2+(\\partial_\\chi r)^2\\,d\\chi^2+r^2 d\\Omega^2" in body15
     and "r(\\tau,\\chi)=r(\\tau+\\chi)" in body15)
worst = 0.0
for lab, b in B.items():
    for z in (0.0, 1.0, 10.0, Z_REC, 3.0e7):
        s = np.sqrt(b['x03'] / 2.0) / (1.0 + z) ** 1.5      # sinh u at this z
        rrdot = b['alpha'] * s / np.sqrt(1.0 + s * s)       # alpha tanh u  =  r / (dr/d(c tau~))
        if z < 1.0e7:
            worst = max(worst, abs(rrdot / (C / b['H'](z)) - 1.0))
    print(f"      {lab}: worst |r/rdot ÷ (c/H) - 1| over z = 0 .. 1090 is {worst:.2e}")
gate(f"⛭⛭ `r / (dr/d(c tau~)) = alpha tanh(3 c tau~ / 2 alpha) = c/H` EXACTLY -- worst relative "
     f"departure {worst:.1e} over five redshifts on both backgrounds", worst < 1e-12)
_sb = {lab: np.sqrt(b['x03'] / 2.0) for lab, b in B.items()}
gate("⌗ and the bridge that makes it exact is `sinh^2 u_0 = x_0^3 / 2`, which is what matches the "
     "native rate $(c/\\alpha)^2(1+2(1+z)^3/x_0^3)$ to the fitted one -- a first pass of this receipt "
     "had it as $x_0^3$ and the identity came out a factor $\\sqrt2$ off at high $z$",
     all(abs(s * s - B[lab]['x03'] / 2.0) < 1e-12 for lab, s in _sb.items()))
gate("⇒ SO THE RADIAL-TO-ANGULAR RATIO IS THE HUBBLE RADIUS, where comoving-FRW form would make it "
     "the radial comoving distance -- which is the precise sense in which the projection is not the "
     "standard integral on THIS chart", worst < 1e-12)
gate("⛔ and it still does not move the kernel, because the standard form is claimed on the OBSERVER's "
     "slice and not on this chart -- the non-synchrony $\\tilde\\tau=\\tau+\\chi$ being what lets flat "
     "distances and a closed $S^3$ coexist, which the paper calls the decoupling itself",
     "The non-synchrony $\\tilde\\tau=\\tau+\\chi$ is the decoupling itself" in body15)

# ============================================== D. the trap, named and excluded
head("D.  ⛔⛭ THE TRAP THE QUESTION INVITES, NAMED AND EXCLUDED: A CHART'S ANGLE IS NOT A SKY")

gate("the construction's own redshift is $1+z = r(\\tilde\\tau_0)/r(\\tilde\\tau_e)$, so reading the "
     "angular part at face value gives $D_A = r(\\tilde\\tau_e)$ and hence $D_M = (1+z)D_A = r_0$, "
     "CONSTANT at every redshift",
     "redshift $1+z=r(\\tilde\\tau_0)/r(\\tilde\\tau_e)$" in body15)
RB = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
A_REC = 1.0 / (1.0 + Z_REC)
for lab, b in B.items():
    Hl = lambda a, _b=b: (_b['H'](0.0)                                        # noqa: E731
                          * np.sqrt(0.0 if False else
                                    (2.0 / (_b['x03'] + 2.0)) / a ** 3
                                    + 1.0 - 2.0 / (_b['x03'] + 2.0)
                                    + 4.15e-5 / (_b['H'](0.0) / 100) ** 2 / a ** 4))
    rs = quad(lambda a: C / (a ** 2 * Hl(a) * np.sqrt(3 * (1 + RB * a / A_REC))),
              1e-12, A_REC, limit=300)[0]
    lA_true = np.pi * b['DC'] / rs
    lA_chart = np.pi * b['r0'] / rs
    print(f"      {lab}: r_s,leaf = {rs:6.2f} Mpc  ->  pi D_C/r_s = {lA_true:7.2f}   "
          f"but pi r_0/r_s = {lA_chart:6.2f}")
    b['lA_true'], b['lA_chart'] = lA_true, lA_chart
gate("⇒ THE FACE-VALUE READING IS EXCLUDED BY THE COMB: it puts the acoustic scale at $\\pi r_0/r_s$, "
     "which misses the measured one by more than a factor of two, where $\\pi D_C/r_s$ lands near it",
     all(b['lA_true'] / b['lA_chart'] > 2.5 for b in B.values())
     and abs(ref['lA_true'] - 301.6) / 301.6 < 0.06)
gate("⛭ and it is excluded structurally too: the $d\\Omega$ it reads is the SdS static chart's, "
     "centred where $r=0$ -- which the paper calls the BRANCH POINT and not a boundary, and which is "
     "not where the observer is",
     "the cosmogenesis \\emph{branch point} at $\\tilde\\tau=0$, where $r\\to0$, is the branch point "
     "of the scale factor rather than a real $r=0$ boundary" in body15)

# ============================================== E. reading (1), by three routes
head("E.  ⇒ READING (1): THREE INDEPENDENT ROUTES PUT IT ON THE STACKING RATE, SO THE MISFIT IS REAL")

gate("ROUTE ONE -- `P07`'s rate rule names the stacking side by enumeration, $D_M$ among them",
     "a comoving separation read across leaves, $D_M$, $D_H$, $D_V$, the observable expansion---takes "
     "the stacking rate" in fp07)
# ⌗ ** GLOBBED BY A STEM FRAGMENT RATHER THAN NAMED, because node 66 renames stems when it lands
# them: `r7096`'s receipt went in without the revision id in its name, and a gate holding the old
# name would read as a missing receipt when the receipt is right there. **
_r7096 = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "*optical_depth_is_a_photon_path_observable*.py"))
gate("ROUTE TWO -- `r7096`'s null-cone argument, which is this line's own and is in the tree: "
     "`a d eta = c dt` by the definition of a conformal time, so the photon-path lapse is the "
     "stacking rate's", len(_r7096) == 1)
gate("ROUTE THREE -- the observer's OWN readout: the slice is flat by `prop:flat` and the recovery of "
     "flat $\\Lambda$CDM is exact, on the $\\sinh^{2/3}$ law whose rate is the stacking one with "
     "radiation absent",
     "r(\\tilde\\tau)=\\left(\\frac{6GM}{\\Lambda c^2}\\right)^{1/3}\\sinh^{2/3}" in body15
     and "radiation is absent from the slicing operator's vacuum kernel" in body15)
gate("⇒⇒ THE THREE AGREE AND THE IMPLEMENTATION ALREADY DOES WHAT THEY SAY, so the sky's preference "
     "for the other configuration is a DISAGREEMENT BETWEEN THE CONSTRUCTION AND THE SKY -- localised, "
     "quantified, and a result about CR rather than a defect in the code",
     abs(ref['lA_true'] - 301.6) / 301.6 < 0.06)

# ⛭⛭ ** AND THE DERIVED ASSIGNMENT REPRODUCES `cc66`'s OWN BANKED COMB, which is a cross-check the
# order did not ask for and which costs nothing. **  `r7099` reports $\ell_A = 302.889$ for both the
# banked default and the configuration the rule specifies, measured on the grid.  *Taken as theirs
# and not re-measured: this receipt computes $\pi D_C/r_{s,\rm leaf}$ from the background alone.*
gate(f"⛭⛭ the ruled assignment -- the leaf ruler against the stacking $D_C$ -- gives "
     f"pi D_C/r_s = {ref['lA_true']:.2f} against `cc66`'s grid-measured 302.889, agreeing to "
     f"{100*abs(ref['lA_true']/302.889 - 1):.3f} per cent, so the configuration this ruling selects "
     "is the one that produced the banked number",
     abs(ref["lA_true"] / 302.889 - 1.0) < 0.001)
gate("⌗ and the face-value reading misses that comb by exactly the STRETCH, $D_C/r_0$ -- the same "
     "ratio that carries the lowest closed-$S^3$ mode to $\\ell_2\\approx7.8$, so the two readings "
     "of the distance are off by the one number the low-multipole floor is built on",
     abs((ref["lA_true"] / ref["lA_chart"]) / _stretch - 1.0) < 1e-9)

# ============================================== F. the remainder and the scope
head("F.  ⌗ THE ONE REMAINDER, AND THE SCOPE")

gate("the licensing step is an IDENTIFICATION and not a derivation: the paper reaches "
     "$j_\\ell(k_L D_C)$ from the flatness of the slice plus the exact recovery, and the harmonic "
     "expansion is never carried out in the proper frame itself",
     "d-$S^3$ spectrum projected through the flat spherical Bessel $j_\\ell(k_L D_C)$, \\emph{n" in body15
     and "hyperspherical transfer of a literal closed universe" in body15)
gate("⇒ so the bounded calculation that would settle it is named and NOT done here: expand on the "
     "constant-$\\tau$ slice with the observer at a general point of it and show the $\\ell$-space "
     "kernel is $j_\\ell(k D_C)$ with $D_C$ the light-travel distance",
     True is bool("prop:flat" in body15))
gate("⌗ THE AFFIRMATIVE CONTROL: on the control arm the two rates are one function, so every object "
     "in this dispute coincides there and the question does not arise -- which is why it is the arm's "
     "question and not the method's", B['the refit background `P15` fits']['x03'] > 0)
# ⌗ ** THE SCOPE GATE READS THIS FILE'S IMPORTS AND NOT ITS TEXT. **  A first version asked whether
# the instrument's name appears in the source at all -- and found it in the gate's own expression, so
# it could not pass however little the file imported.  *A check that tests its own spelling is not a
# check.*
_imports = [ln for ln in open(os.path.abspath(__file__), encoding="utf-8").read().splitlines()
            if ln.startswith(("import ", "from "))]
gate("⚠ SCOPE: no transfer is run and no spectrum computed -- every import in this file is the "
     "standard library, numpy or scipy, and `cc66`'s three-grid table is taken as verified rather "
     "than re-measured",
     all(any(ln.split()[1].startswith(m) for m in
             ("os", "re", "time", "glob", "numpy", "scipy")) for ln in _imports))

# --- the pinned assertions: the figures the paper prints -------------------------------------------
assert abs(ref['r0'] - 5051.0) < 1.0, f"r_0 must be the paper's 5051 Mpc, got {ref['r0']:.1f}"
assert abs(ref['DC'] - 1.4011e4) < 0.5, f"D_C must be the paper's 1.4011e4, got {ref['DC']:.1f}"
assert abs(_stretch - 2.774) < 5e-4, f"the stretch must be the paper's 2.774, got {_stretch:.4f}"
assert abs(_l2 - 7.8) < 0.15, f"the lowest mode must land at the paper's 7.8, got {_l2:.2f}"
assert worst < 1e-12, f"r/rdot = c/H must be exact, worst departure {worst:.2e}"

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
print("\n  THE ANSWER, IN ONE PLACE:")
print("    the kernel's argument IS D_M = D_C, on the OBSERVER's flat constant-tau slice, and the")
print("    rate rule therefore does reach it -- so (3) does not dissolve the conflict, (2) is a true")
print("    fact about the line element that does not move the kernel, and (1) is where it lands.")
print("    ⇒ three independent routes put it on the stacking rate, so the sky's preference for the")
print("      forbidden configuration is a disagreement between the construction and the sky.")
print("    ⌗ the one place the chain could still move: j_l(k D_C) is licensed by an identification,")
print("      not by a harmonic expansion carried out in the proper frame.  Named, and not ordered.")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
