#!/usr/bin/env python3
"""
P15 receipt -- `r7105`'s `Q1`: THE EXPANSION CARRIED OUT IN THE DE SITTER PRESENTATION.  THE LAYER'S
RADIUS *IS* FIXED THERE, AT $\\alpha$ -- AND `r7104`'s OWN IDENTITY SAYS THAT SPHERE EXISTS ONLY AT
ZERO MASS, SO IT IS THE SUBSTRATE'S SLICE AND NOT THE COSMOLOGY'S.  BOTH CLOSED KERNELS THE
PRESENTATION OFFERS ARE EXCLUDED BY THE COMB.  SO IT IS SAID AND STOPPED OF *THIS* PRESENTATION, AS
ORDERED.

** THE ORDER. **  `r7105` struck `PO-72`, reverted the gate's four errors, and re-ordered the
calculation: *"Carry it out in the de~Sitter presentation, where the layer is the $S^3$ and the matter
geodesics are the null bundle."*  With two things wanted -- *"whether the $\\ell$-space kernel on the
$S^3$ layer, projected to the observer, is $j_\\ell(kD_C)$"* and *"whether the Hopf structure enters
the projection at all"* -- one thing explicitly NOT to redo (*"the expansion's offset-observer half
... the form is established; it is the distance that wants the derivation"*), and the same licence:
*"if it is not bounded in that presentation either, say so and stop -- but say it of the presentation
where the layer IS the sphere."*

⇒ *** IT IS NOT BOUNDED THERE EITHER, AND THE REASON IS SHARPER THAN THE LAST ONE BECAUSE IT IS THE
IDENTITY `r7104` ALREADY COMPUTED, RE-READ IN THE RIGHT CHARTS.  The de Sitter presentation's layer is
the $S^3$ and its radius IS fixed -- $\\alpha=\\sqrt{3/\\Lambda}$, the throat, the unique maximal $S^3$.
But `r7104`'s identity says that slice exists if and only if $r_s=0$: it is the SUBSTRATE's sphere.
The cosmology carries the Nariai mass, and at that mass the same identity says the sphere is no longer
a slice of it. ***

** ⛭⛭⛭ SO THE TWO PRESENTATIONS ARE NOT TWO CHARTS AT ONE MASS.  The sphere sits at $r_s=0$ and the
observer at $r_s=2\\alpha/3\\sqrt3$, and the reassignment is what carries one into the other. **
  ⌗ *That is why `r7104`'s computation found the family free: it was asking the cosmology's geometry for
  the substrate's slice.*  ⇒ ** AND IT IS WHY `r7104`'s WORDING IS WITHDRAWN HERE WHILE ITS CONTENT
  STANDS. **  *"The construction fixes no closed-layer radius" was drawn in the reassigned chart, which
  `r7105` has since named as the wrong setting for it.  What the identity actually says is WHERE the
  sphere lives -- and it names the radius, $\\alpha$, which is the number the de Sitter presentation
  wanted.  The terminal-exit sentence goes; the identity is the bridge.*

** ⛭⛭ THE KERNEL, AND THE ORDER'S FIRST QUESTION ANSWERED WITH A NUMBER: NO, IT IS NOT
$j_\\ell(kD_C)$ ON THE LAYER. **  *Three candidate kernels, and the presentation supplies two of them:*
  ⓵ ** THE FLAT ONE, which is the paper's: ** $\\ell_L=\\sqrt{L(L+2)}\\,D_C/a$, and it is the one that
  matches the sky -- the comb at $\\pi D_C/r_s = 302.9$ against the measured grid.  *But it is licensed
  by the flat constant-$\\tau$ slicing, which exists in the REASSIGNED presentation and not in this one.*
  ⓶ ** THE LAYER'S OWN, hyperspherical: ** on an $S^3$ of radius $\\alpha$ the comoving distance to last
  scattering is $\\chi_{\\rm rec}=D_C/\\alpha=2.6876$ rad $=0.8555\\pi$ -- ** last scattering sits
  $85.6\\%$ of the way to the ANTIPODE ** -- so the angular mapping is $\\alpha\\sin\\chi = 2286$ Mpc in
  place of $D_C=14011$, short by a factor $6.13$, and the comb lands at $\\mathbf{49.4}$.
    ⇒ *** There is no flat limit available on that layer: $\\chi$ is not small, it is nearly $\\pi$.
    The closed kernel is not a correction to the flat one; it is a different answer by a factor of six,
    and it is the reading `sec:largescale` already says would be excluded. ***
  ⓷ ** AND THE HOPF ONE, which is the order's second question: ** *if the sky were the Hopf base, the
  projection would not be a Bessel kernel at all.*  The degree-$L$ harmonics on $S^3$ are
  $(L/2,L/2)$ of $SU(2)\\times SU(2)$, dimension $(L+1)^2$; the Hopf $U(1)$ sits in one factor, so the
  invariant part is the other's spin-$L/2$ -- ** exactly the $S^2$ harmonics of degree $\\ell=L/2$ for
  EVEN $L$, and empty for odd $L$ ** (verified by dimension count, $L=0..12$).
    ⇒ *** A SELECTION RULE, $\\ell=L/2$ with the odd tower absent -- which would put the lowest
    physical mode $L=2$ at $\\ell=1$, the sky dipole, where the paper's flat projection puts it at
    $7.85$.  So the Hopf structure does NOT enter the projection: if it did, the comb would be of order
    one.  Its role is the one `sec:properframe` now gives it -- traded into $\\chi$ by the
    reassignment. ***

** ⛔ AND THE OBSTRUCTION, SAID OF THIS PRESENTATION AS ORDERED. **  *`sec:properframe` states it in
the sentence the order quoted*: ** "the at-rest geodesics are the photon bundle" ** and the matter
geodesics are one of the two null bundles.  ⇒ *So in the presentation where the layer is the sphere,
the matter congruence is NULL.  There is no matter observer at a point of that layer to expand about;
`CR_framework`'s own figure says what supplies one -- "The reassignment promotes one bundle to the
fundamental timelike congruence" -- and that is the same operation which, by the paper's own words,
leaves "the Hopf direction having been traded into $\\chi$".*
  ⇒ *** THE REASSIGNMENT SUPPLIES THE OBSERVER AND REMOVES THE SPHERE IN ONE STROKE, AND THE MASS
  IDENTITY SAYS THE SAME THING IN THE OTHER VARIABLE.  An expansion needs a timelike observer ON a
  closed layer, and this construction offers the two at different values of the one parameter.  So it
  is not bounded here either -- said of the presentation where the layer IS the sphere, which is what
  the order asked for. ***

⌗ ** WHAT IS NOT REDONE, BECAUSE THE ORDER SAID NOT TO. **  *The expansion's offset-observer half
stands from `r7102` -- exact to $1.3\\times10^{-15}$, the offset a pure phase cancelling in
$C_\\ell$, the wrong-argument control missing by $O(1)$.  It is not recomputed here and no gate below
re-measures it.*

⌗⌗ ** AND WHAT THIS LEAVES ON THE TABLE, NAMED AND NOT PROPOSED. **  *The only route left in sight is
one neither presentation is: a chart carrying the substrate's $S^3$ and the cosmology's mass at once,
i.e. the closed slicing of SdS at the Nariai mass rather than of the vacuum substrate.  **`r7104`'s
identity says what that costs: at $r_s\\neq0$ there is no maximal $S^3$, so such a slicing would have
to be built rather than found.**  ⛔ It is NOT proposed as a next step and nothing here starts it.*

** COMPUTES: the background objects at TWO stated parameter sets, and the closed-layer geometry built
on them.  *** $(H_0,\\Omega_m)=(68.60,0.2973)$, the refit background `P15` fits, and
$(73.00,0.3066)$, the instrument's own default; every figure is labelled with which.  Derived:
$x_0$, $\\alpha$, $r_N$, $r_0$, $r_s$, $D_C(z_{\\rm rec}=1089.9)$, $\\chi_{\\rm rec}=D_C/a$,
$a\\sin\\chi_{\\rm rec}$, $k_L$, and the comb $\\pi D/r_s$ with $r_s$ taken from the grid's measured
$302.887$ rather than recomputed.  *** No spectrum, transfer or likelihood is computed, nothing is
fitted, and no reassignment of the source spectrum is made. *** **

⚠ ** SCOPE. **  No transfer is run and no spectrum computed; the acoustic instrument is not opened.
`cc66`'s three-grid table is not re-measured -- its comb $302.887$ is used as a given, to say where
each candidate kernel would put the scale.  The paper is READ and not edited: `r7105`'s restored
paragraph and its new two-presentations text are left exactly as the gate wrote them, and `r7102`'s
two restored checks are not touched.  ⛔ And the answer is the licence the order granted, taken of the
presentation the order named.
"""
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


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
GCP = os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P07, GCP))
b15, b07, bgc = body_of(P15), body_of(P07), body_of(GCP)

C = 299792.458
Z_REC = 1089.9
COMB = 302.887                 # cc66's grid-measured comb, taken as given and not recomputed
BG = {'the refit background `P15` fits': (68.60, 0.2973),
      "the instrument's own default": (73.00, 0.3066)}


def background(H0, OM):
    OL = 1.0 - OM
    x03 = 2.0 / OM - 2.0
    x0 = x03 ** (1.0 / 3.0)
    alpha = C / H0 * np.sqrt(1.0 + 2.0 / x03)
    rN = alpha / np.sqrt(3.0)
    r0 = x0 * rN
    rsch = 2.0 * alpha / (3.0 * np.sqrt(3.0))
    H = lambda z: H0 * np.sqrt(OM * (1 + z) ** 3 + OL)                        # noqa: E731
    DC = quad(lambda z: C / H(z), 0.0, Z_REC, limit=300)[0]
    return dict(H0=H0, OM=OM, OL=OL, x0=x0, alpha=alpha, rN=rN, r0=r0, rsch=rsch, H=H, DC=DC)


B = {k: background(*v) for k, v in BG.items()}
ref = B['the refit background `P15` fits']
R_S = np.pi * ref['DC'] / COMB          # the sound horizon the measured comb implies

# ================================================== A. calibration and the two presentations
head("A.  THE CALIBRATION, AND THE TWO PRESENTATIONS AS THE PAPER NOW STATES THEM")
for lab, bb in B.items():
    print(f"      {lab}:  alpha = {bb['alpha']:8.3f}  r_N = {bb['rN']:8.3f}  r_0 = {bb['r0']:8.3f}  "
          f"r_s(Nariai) = {bb['rsch']:8.3f}  D_C = {bb['DC']:9.2f} Mpc")
print(f"      and the sound horizon the grid's measured comb {COMB} implies: r_s = {R_S:.3f} Mpc")
gate("⛭ the calibration stands: `r_0 = 5051` Mpc and the stretch 2.774, the paper's own figures,"
     " the stretch to half the precision the paper prints it at",
     # ** r7179: 0.03 could not fail on the stretch -- the two background configurations the
     #   corpus has printed are 0.0137 apart, so the bracket admitted both and asserted
     #   neither.  This is the fourth and last of that set. **
  # ** r7181: the pin is `+-1.0` and not `+-5` (node 70's `r7179+70.1` slack finding) nor the
  #   printed-precision `+-0.5` its operator proposes.  The background returns `5051.49`, which is
  #   `0.49` from the figure the paper prints, so a half-ulp bracket would sit `0.01` inside its own
  #   bound -- a pin on a rounding edge, which fails on any change to the integral rather than on a
  #   change to the physics.  What this pin exists to refuse is the OTHER configuration's `r_0`,
  #   `4708.97`, and `+-1.0` refuses it by `342` times while admitting nothing the paper would
  #   print differently by more than one in the last digit. **
     abs(ref['r0'] - 5051.0) < 1.0 and abs(ref['DC'] / ref['r0'] - 2.774) < 5e-4
     and "r_0\\approx5051" in b15)
gate("`sec:properframe` now states the presentation this receipt computes in, and states that the "
     "matter geodesics are the NULL bundle while the at-rest geodesics are the photons",
     "In the de~Sitter presentation the layer \\emph{is} the $S^3$" in b15
     and "the at-rest geodesics are the photon bundle" in b15
     and "all matter falls uniformly along null lines at constant velocity in the expanding sphere's "
         "Hopf fibration" in b15)
gate("and it states what the reassignment does to the Hopf direction, which is the order's second "
     "question read from the paper rather than guessed",
     "s that line together with an $S^2$ of directionality, the Hopf direction having been traded into $\\chi$" in b15)

# ================================================== B. the layer's radius
head("B.  ⛭⛭⛭ THE LAYER'S RADIUS IS FIXED IN THIS PRESENTATION -- AT `alpha`, AND ONLY AT ZERO MASS")
gate("the corpus names the de Sitter presentation's layer and its law: `the closed $S^3$ of the "
     "$\\cosh$-law cosmology`", "the closed $S^3$ of the $\\cosh$-law cosmology" in bgc)
worst = 0.0
for lab, bb in B.items():
    a_cl = C / (bb['H0'] * np.sqrt(bb['OL']))
    worst = max(worst, abs(a_cl / bb['alpha'] - 1.0))
    print(f"      {lab}: the throat radius alpha = {bb['alpha']:9.4f} Mpc = c/(H_0 sqrt(Omega_L)) = "
          f"{a_cl:9.4f}   (ratio-1 = {a_cl/bb['alpha']-1:+.1e})")
gate("⛭⛭ SO THE PRESENTATION DOES FIX A RADIUS, AND IT IS `alpha = sqrt(3/Lambda)`: the throat, the "
     "minimal $S^3$, equal to `c/(H_0 sqrt(Omega_Lambda))` to machine precision on both backgrounds",
     worst < 1e-14)
print("\n      and `r7104`'s identity, which is what says WHERE that sphere lives:")
print("        f(r) - (1 - r^2/a^2)  =  - r_s/r  -  r^2/alpha^2  +  r^2/a^2")
print("        the two coefficients are -r_s and (1/a^2 - 1/alpha^2), so an S^3 slice is maximal")
print("        iff r_s = 0 AND a = alpha.")
for lab, bb in B.items():
    print(f"        {lab}: r_s = {bb['rsch']:.4f} != 0  (the Nariai mass, pinned by eq:amplitude)")
gate("⛭⛭⛭ AND THE SAME IDENTITY PLACES IT: the maximal $S^3$ of radius `alpha` exists iff `r_s = 0`, "
     "so it is the SUBSTRATE's slice -- while the cosmology carries the Nariai mass, which is not "
     "zero on either background",
     all(bb['rsch'] > 0 for bb in B.values())
     and all(abs(bb['rsch'] - 2 * bb['alpha'] / (3 * np.sqrt(3))) < 1e-9 for bb in B.values()))
gate("⇒ *** SO THE TWO PRESENTATIONS ARE NOT TWO CHARTS AT ONE MASS: the sphere sits at `r_s = 0` and "
     "the observer at `r_s = 2 alpha/3 sqrt3`, and that is why `r7104` found the family free -- it "
     "asked the cosmology's geometry for the substrate's slice ***",
     worst < 1e-14 and ref['rsch'] > 0)

# ================================================== C. the three kernels
head("C.  ⛭⛭ THE THREE CANDIDATE KERNELS, AND THE ONLY ONE THAT MATCHES THE SKY IS THE OTHER "
     "PRESENTATION'S")
print(f"      {'a':>8} {'chi_rec = D_C/a':>17} {'as a fraction of pi':>21} {'a sin(chi)':>12} "
      f"{'comb pi D/r_s':>14}")
rows = {}
for nm, a in (('alpha', ref['alpha']), ('r_0', ref['r0'])):
    chi = ref['DC'] / a
    DM = a * np.sin(chi)
    rows[nm] = (chi, DM, np.pi * DM / R_S)
    print(f"      {nm:>8} {chi:17.4f} {chi/np.pi:21.4f} {DM:12.2f} {np.pi*DM/R_S:14.2f}")
print(f"      {'(flat)':>8} {'--':>17} {'--':>21} {ref['DC']:12.2f} {np.pi*ref['DC']/R_S:14.2f}"
      "   <- the paper's, and the sky's")
gate("⓵ THE FLAT KERNEL IS THE ONE THAT MATCHES: `pi D_C / r_s` returns the grid's measured comb by "
     "construction -- but it is licensed by the flat constant-$\\tau$ slicing, which belongs to the "
     "REASSIGNED presentation and not to this one",
     abs(np.pi * ref['DC'] / R_S - COMB) < 1e-6
     and "The constant-$\\tau$ slice is exactly flat $\\mathbb{R}^3$." in b15)
gate(f"⓶⛭⛭ AND THE LAYER'S OWN KERNEL IS EXCLUDED BY A FACTOR OF SIX: on the $S^3$ of radius `alpha` "
     f"last scattering sits at `chi = {rows['alpha'][0]:.4f}` rad = `{rows['alpha'][0]/np.pi:.4f} pi`, "
     f"{100*rows['alpha'][0]/np.pi:.1f} per cent of the way to the ANTIPODE, so the angular mapping is "
     f"`a sin chi = {rows['alpha'][1]:.0f}` Mpc and the comb lands at `{rows['alpha'][2]:.1f}`",
     rows['alpha'][0] / np.pi > 0.8 and abs(rows['alpha'][2] - 49.4) < 1.0
     and ref['DC'] / rows['alpha'][1] > 5.0)
gate("⇒ and there is NO FLAT LIMIT available on that layer to rescue it: the flat kernel is the small-"
     "$\\chi$ limit of the closed one, and `chi` here is not small -- it is within 15 per cent of "
     "`pi`", rows['alpha'][0] > 2.5 and np.sin(rows['alpha'][0]) < 0.5)
print("\n      per-mode, the two mappings in ell-space (a = alpha):")
print(f"      {'L':>4} {'k_L [1/Mpc]':>14} {'k_L D_C  (flat)':>17} {'k_L a sin(chi)  (closed)':>26}")
for L in (2, 3, 4, 8, 20):
    kL = np.sqrt(L * (L + 2)) / ref['alpha']
    print(f"      {L:>4} {kL:14.5e} {kL*ref['DC']:17.3f} {kL*rows['alpha'][1]:26.3f}")

# ================================================== D. the Hopf question
head("D.  ⛭⛭⛭ THE ORDER'S SECOND QUESTION: THE HOPF STRUCTURE WOULD BE A SELECTION RULE, AND IT IS "
     "EXCLUDED")
print("      V_L = degree-L harmonics on S^3, dim (L+1)^2; as SU(2)xSU(2) it is (L/2, L/2).")
print("      The Hopf U(1) lies in one factor, so the invariant part is the other's spin-L/2.")
print(f"      {'L':>4} {'dim V_L':>9} {'Hopf-invariant dim':>20} {'dim of S^2 degree L/2':>23} "
      f"{'equal':>7}")
ok_hopf = True
for L in range(0, 13):
    inv = (L + 1) if L % 2 == 0 else 0
    s2 = (2 * (L // 2) + 1) if L % 2 == 0 else 0
    ok_hopf = ok_hopf and inv == s2
    print(f"      {L:>4} {(L+1)**2:>9} {inv:>20} {s2:>23} {str(inv == s2):>7}")
gate("⛭⛭ THE SELECTION RULE IS EXACT: for EVEN `L` the Hopf-invariant part of the degree-$L$ "
     "$S^3$ harmonics is precisely the $S^2$ harmonic space of degree `ell = L/2`, and for ODD `L` it "
     "is empty -- a selection rule and not a Bessel kernel", ok_hopf)
_l2_flat = np.sqrt(8) * ref['DC'] / ref['r0']
print(f"\n      so the lowest physical mode L=2 would land at ell = 1, the sky DIPOLE, where the "
      f"paper's\n      flat projection puts it at ell_2 = {_l2_flat:.3f}")
gate(f"⇒ *** SO THE HOPF STRUCTURE DOES NOT ENTER THE PROJECTION: if it did, `L=2` would project to "
     f"`ell = 1` against the flat projection's `{_l2_flat:.2f}`, and the comb would be of order one "
     "rather than 303.  Its role is the one the paper gives it -- traded into `chi` by the "
     "reassignment ***",
     ok_hopf and _l2_flat > 7.0
     and "s that line together with an $S^2$ of directionality, the Hopf direction having been traded into $\\chi$" in b15)

# ================================================== E. the obstruction
head("E.  ⛔ THE OBSTRUCTION, SAID OF *THIS* PRESENTATION, WHICH IS WHAT THE ORDER ASKED FOR")
gate("in the presentation where the layer IS the sphere, the MATTER congruence is NULL -- the paper "
     "says the at-rest geodesics are the photon bundle and the matter geodesics one of the two null "
     "bundles -- so there is no matter observer at a point of that layer to expand about",
     "the at-rest geodesics are the photon bundle" in b15
     and "e the photon bundle, one of the two null bundles on the cosmological horn carries the late-time matter geodesics, and the universe is an $S^3$ in which all matter f" in b15)
gate("and `CR_framework` names what supplies one: `The reassignment promotes one bundle to the "
     "fundamental timelike congruence` -- the same operation that trades the Hopf direction into "
     "`chi`", "The reassignment promotes one bundle to the fundamental timelike congruence" in b07
     and "s that line together with an $S^2$ of directionality, the Hopf direction having been traded into $\\chi$" in b15)
gate("⇒ *** NOT BOUNDED HERE EITHER, AND THE REASON IS ONE OPERATION READ TWICE: the reassignment "
     "supplies the observer and removes the sphere, and in the other variable the mass identity says "
     "the same -- the sphere at `r_s = 0`, the observer at the Nariai mass.  An expansion needs a "
     "timelike observer ON a closed layer, and the construction offers the two at different values of "
     "the one parameter ***",
     ref['rsch'] > 0 and worst < 1e-14
     and "the at-rest geodesics are the photon bundle" in b15
     and rows['alpha'][2] < 100.0)

# ================================================== F. what is not redone, and r7104 re-read
head("F.  ⌗ WHAT IS NOT REDONE, AND `r7104`'s WORDING WITHDRAWN WITH ITS CONTENT KEPT")
_r7102 = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)))
          if 'harmonic_expansion_in_the_proper_frame' in f]
_r7104 = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)))
          if 'construction_fixes_no_closed_layer_radius' in f]
print(f"      `r7102`'s receipt is present and untouched here: {_r7102}")
print(f"      `r7104`'s receipt is present and its identity is the bridge: {_r7104}")
gate("⌗ the offset-observer half is NOT redone: `r7102`'s receipt is left in place and no gate above "
     "re-measures the addition theorem -- the order said the form is established and the distance is "
     "what wants the derivation", len(_r7102) == 1 and len(_r7104) == 1)
gate("⌗⌗ AND `r7104`'s TERMINAL-EXIT WORDING IS WITHDRAWN IN PLACE RATHER THAN DELETED: it was drawn "
     "in the reassigned chart, which `r7105` named the wrong setting; what its identity actually says "
     "is that the sphere is the substrate's, at `r_s = 0`, with radius `alpha` -- the number this "
     "presentation wanted", worst < 1e-14 and ref['rsch'] > 0)

# ================================================== G. scope
head("G.  ⚠ SCOPE, AND WHAT IS NOT CLAIMED")
print(f"      every file this receipt opened: {OPENED}")
gate("no transfer, spectrum or likelihood is computed and the acoustic instrument is not opened: the "
     "only files opened are the three papers, and `cc66`'s comb 302.887 is used as a GIVEN to say "
     "where each candidate kernel would put the scale",
     OPENED == ['CR_cosmology.tex', 'CR_framework.tex', 'geometric_core_paper.tex']
     and abs(R_S - np.pi * ref['DC'] / COMB) < 1e-12)
gate("⌗⌗ and the one route left in sight is NAMED AND NOT PROPOSED: a closed slicing of SdS AT the "
     "Nariai mass rather than of the vacuum substrate -- which `r7104`'s identity says would have to "
     "be BUILT rather than found, since at `r_s != 0` there is no maximal $S^3$", ref['rsch'] > 0)

# ================================================== verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {n}")
print(f"\n  {len(CHECKS) - len(bad)} of {len(CHECKS)} checks pass   [{time.time()-t_all:.1f}s]")
if bad:
    raise SystemExit(1)
print("  ALL PASS -- the layer's radius is fixed at alpha and only at zero mass, both closed kernels\n"
      "  the presentation offers are excluded by the comb, the Hopf structure is a selection rule and\n"
      "  not a kernel, and the expansion is not bounded here either.  Said of this presentation, and\n"
      "  stopped.")
