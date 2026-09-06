#!/usr/bin/env python3
"""
RECEIPT -- PO-35: ** THE GROWTH-FACTOR NORMALISATION'S ROOT IS A SMOOTH SURFACE WITH
NO FEATURE AT THE PHYSICAL POINT, SO THE AGREEMENT IS A COINCIDENCE -- AND IT IS THE
STANDARD MODEL'S, NOT THIS CONSTRUCTION'S. **

*The published note observes that the normalisation integral of the flat-LambdaCDM
linear growth factor,

    J(Om) = int_0^inf dz (1+z) / [Om (1+z)^3 + (1-Om)]^(3/2),

crosses unity once, at Om* = 0.315162, consistent with the concordance matter
density.  It states the observation and asserts no explanation.  PO-35 asks whether
that is a coincidence, an artefact of some analysis, or a property of the growth
factor at the matter-Lambda crossover.  This receipt settles it.*

** THE THREE CANDIDATES, AND WHAT DECIDES BETWEEN THEM. **

  (1) AN ARTEFACT OF SOME ANALYSIS.  ** Ruled out. **  J is a forced, dimensionless
      function of Om alone: the integrand's form comes from the growth equation, and
      writing H in units of H_0 is what makes the quantity dimensionless rather than
      a choice among alternatives.  Nothing is free to be set, and the note's root
      reproduces here to six figures.

  (2) A PROPERTY AT THE MATTER-LAMBDA CROSSOVER.  ** Ruled out, and this is the
      decisive test. **  Embed the integral in its natural families -- the exponent
      p, the dark-energy equation of state w, and the curvature Om_k -- and ask
      whether the root Om*(p, w, Om_k) does anything at the physical point.  ** It
      does not. **  The root is smooth and monotone through p = 3/2, through w = -1,
      and through Om_k = 0, with no stationary point, no kink and no divergence at
      any of them.  A property OF the crossover would leave a mark there.  There is
      none.

  (3) A COINCIDENCE.  ** What remains. **  A smooth map with no distinguished point,
      whose image at the physical parameters happens to agree with an independently
      measured density.

** AND THE DISCRIMINATING MEASUREMENT SAYS WHOSE COINCIDENCE IT IS. **  J = 0.99966
at Planck's 0.3153 -- agreement to 0.03% -- but J = 1.02142 at this corpus's own DESI
DR2 fit of 0.3066, a 2.1% miss.  ** The coincidence tracks the standard model's
matter density and not the geometric rate's, which is evidence against reading it as
a feature of this construction. **

** WHAT THIS DOES NOT CLAIM. **  It does not claim no explanation exists, only that
the crossover reading -- the one candidate with a mechanism attached -- is excluded
by the absence of any feature at the physical point, and that the remaining agreement
belongs to the standard model rather than to this corpus.  The note's own practical
point, that omitting the factor biases growth-based inference toward Om*, is
untouched and is not what this row asked about.
"""
import sys
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

FAILED = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


def J(Om, p=1.5, w=-1.0, Ok=0.0):
    """The normalisation integral, in its natural three-parameter family."""
    def E2(z):
        return (Om * (1 + z) ** 3 + Ok * (1 + z) ** 2
                + (1 - Om - Ok) * (1 + z) ** (3 * (1 + w)))
    return quad(lambda z: (1 + z) / E2(z) ** p, 0, np.inf, limit=500)[0]


def root(p=1.5, w=-1.0, Ok=0.0, lo=0.03, hi=0.97):
    return brentq(lambda Om: J(Om, p, w, Ok) - 1.0, lo, hi, xtol=1e-12)


print()
print("  THE GROWTH-FACTOR NORMALISATION -- coincidence, artefact, or property?")
print("  " + "=" * 70)
print()

# ------------------------------------------------------------------ reproduce
r0 = root()
print(f"  the note's root: Om* = {r0:.6f}   (published value 0.315162)")
check("the published root reproduces to six figures", abs(r0 - 0.315162) < 1e-5)
print()

# --------------------------------------------------- (2) the decisive test
print("  the root across the three natural families -- looking for ANY feature")
print(f"      {'exponent p':>12} {'Om*':>10}")
ps = [1.30, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70]
rp = [root(p=p) for p in ps]
for p, r in zip(ps, rp):
    print(f"      {p:>12.2f} {r:>10.6f}")
print()
print(f"      {'w':>12} {'Om*':>10}")
ws = [-1.20, -1.10, -1.05, -1.00, -0.95, -0.90, -0.80]
rw = [root(w=w) for w in ws]
for w, r in zip(ws, rw):
    print(f"      {w:>12.2f} {r:>10.6f}")
print()
print(f"      {'Om_k':>12} {'Om*':>10}")
ks = [-0.04, -0.02, -0.01, 0.00, 0.01, 0.02, 0.04]
rk = [root(Ok=k) for k in ks]
for k, r in zip(ks, rk):
    print(f"      {k:>12.2f} {r:>10.6f}")
print()


def strictly_monotone(v):
    return all(b > a for a, b in zip(v, v[1:])) or all(b < a for a, b in zip(v, v[1:]))


def no_kink(xs, ys, tol=0.12):
    """Second differences small relative to first: no kink at the interior points."""
    d1 = np.diff(ys) / np.diff(xs)
    return np.max(np.abs(np.diff(d1))) / np.max(np.abs(d1)) < tol * len(d1)


check("the root is strictly monotone in the exponent", strictly_monotone(rp))
check("the root is strictly monotone in w", strictly_monotone(rw))
check("the root is strictly monotone in the curvature", strictly_monotone(rk))
check("no kink in the root at p = 3/2", no_kink(ps, rp))
check("no kink in the root at w = -1", no_kink(ws, rw))
check("no kink in the root at Om_k = 0", no_kink(ks, rk))

# a property AT the crossover would make the physical point stationary
d_w = (root(w=-0.99) - root(w=-1.01)) / 0.02
d_k = (root(Ok=0.005) - root(Ok=-0.005)) / 0.01
print()
print(f"      dOm*/dw   at w = -1     : {d_w:+.4f}")
print(f"      dOm*/dOm_k at Om_k = 0  : {d_k:+.4f}")
check("the physical point is NOT stationary in w -- no feature there",
      abs(d_w) > 0.1)
check("the physical point is NOT stationary in curvature -- no feature there",
      abs(d_k) > 0.1)

print()
print("  " + "-" * 70)
# ------------------------------------------------- (1) not an artefact: it is steep
dJ = (J(0.316) - J(0.314)) / 0.002
print(f"  dJ/dOm at the root = {dJ:+.4f}, so J moves 1% per dOm = {0.01/abs(dJ):.4f}")
check("the crossing is steep rather than flat, so it is not a broad-band near-unity",
      abs(dJ) > 1.0)

print()
# ---------------------------------------------------- whose coincidence is it
print("  the discriminating measurement:")
for name, Om in (("Planck 2018", 0.3153), ("the root", 0.315162),
                 ("this corpus's DESI DR2 fit", 0.3066)):
    print(f"      {name:<28} Om = {Om:<9} J = {J(Om):.5f}   |J-1| = {abs(J(Om)-1)*100:.3f}%")
print()
check("J agrees with unity at the standard model's density to better than 0.1%",
      abs(J(0.3153) - 1.0) < 1e-3)
check("** and MISSES at this corpus's own fitted density by over 2% **",
      abs(J(0.3066) - 1.0) > 0.02)

print()
print("  " + "=" * 70)
if FAILED:
    print(f"  {len(FAILED)} check(s) FAILED")
    for f in FAILED:
        print(f"    - {f}")
    sys.exit(1)
print("  The root is a smooth, monotone, feature-free surface through the physical")
print("  point in every direction tested.  A property OF the matter-Lambda crossover")
print("  would leave a mark there and there is none, so that reading is excluded and")
print("  the artefact reading was never available -- J is forced and dimensionless.")
print("  ** What remains is a coincidence, and the discriminating measurement says")
print("  ** it is the standard model's and not this construction's.")
print()
sys.exit(0)
