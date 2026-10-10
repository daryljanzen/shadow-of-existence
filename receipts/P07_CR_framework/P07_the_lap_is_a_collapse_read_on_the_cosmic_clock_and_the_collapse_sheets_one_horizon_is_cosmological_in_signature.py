#!/usr/bin/env python3
"""P07 receipt -- ⛭⛭⛭ THE LAP IS A COLLAPSE READ ON THE COSMIC CLOCK, AND ON THE SHEET THE COLLAPSE
RUNS ON THE ONE HORIZON IS COSMOLOGICAL IN SIGNATURE, NOT A BLACK HOLE'S.

** WHAT THIS IS FOR. **  The corpus carries every piece of the lap's local reading and nowhere states
them as one reading.  This receipt establishes the geometric half, so `P7`'s stratification section can
state it once: what each locus of the lap IS, read on the sheet the collapse actually runs on, and how
that local reading sits beside the substrate-level identification of the two seams as one point.

** AND IT CORRECTS A FLAT IDENTITY THIS SEAT PUT IN PRINT AT `r7185`. **  That revision wrote `the back
seam is the event horizon of the collapsing matter` with no level named.  At substrate level that is
right -- the back seam is the backward-radial root the lap closes on, the merged-horizon value
re-entered (`P3`), one point with the front seam (`P2`).  As a LOCAL reading on the collapse sheet it is
wrong, and the signature says so: outside the back seam the radius is timelike and the region is
asymptotically de Sitter; inside it the geometry is static, down to the branch point.  That is the
pattern of a COSMOLOGICAL horizon and the exact reverse of a black hole's.  `P7`'s own
`Two levels must be held apart` remark is the frame the corrected statement belongs in.

** THE ONE FACT THREE OF THE CLAIMS TURN OUT TO BE. **  On r < 0, f' = 2M/r^2 - 2r/alpha^2 is a sum of
two positive terms, so f is strictly MONOTONE on the collapse sheet for every M > 0 and every finite
alpha.  Monotone forces all three at once: exactly ONE root, that root SIMPLE (hence kappa != 0), and
NO balance radius (f' = 0) anywhere on the sheet.  The balance radius is at +(M alpha^2)^(1/3), which on
the forced member is the FRONT seam and is the Hubble--Eddington radius.

** COMPUTES. **
  Ⓐ  f is monotone on r < 0, over a grid in (M, alpha), with the root count and order that forces;
  Ⓑ  the signature of that root against a COSMOLOGICAL and a BLACK-HOLE root of three sub-Nariai
     members -- it matches the first and reverses the second, and the sheet has no black-hole root;
  Ⓒ  that the one root, its non-zero surface gravity and the absent balance radius are one fact;
  Ⓓ  that Lambda > 0 is what turns that root on: at Lambda = 0 the sheet is horizonless, which is
     `P2`'s own proof, read from its source;
  Ⓔ  the two energies -- E = 0 turning on f = 0 (the seams) and E = 1 on f = 1 (the turnaround), so the
     turnaround stands to the cosmological congruence as a horizon does to the static one;
  Ⓕ  the lift as the stretch forbidden to E = 1, its trigonometric law joining the branch point to the
     turnaround, against the hyperbolic law of the real legs -- `P2`'s own pairing;
  Ⓖ  the three printed statements the LEVEL separation rests on, each read from its own source;
  Ⓗ  and that the two marks of a Schwarzschild interior fall at DIFFERENT loci of the lap.

COMPUTES: scope -- what the parameter choices do and do not restrict.  Ⓐ, Ⓑ and Ⓓ run over a GRID in
(M, alpha) and over three sub-Nariai masses precisely because the claims are about the family and not
about the forced member: monotonicity on r < 0 is proved from the sign of the two terms of f' and then
sampled, and the signature comparison needs members whose black-hole and cosmological roots are
DISTINCT, which the Nariai member's are not.  Ⓔ, Ⓕ and Ⓗ run on the forced member at alpha = 1 with
M = alpha/(3 sqrt3); there the Nariai condition fixes M in terms of alpha, so alpha = 1 is a choice of
UNIT and every figure is reported in units of alpha.  No observational parameter enters and nothing is
fitted.

** WHAT IT DOES NOT CLAIM. **  It does not claim the turnaround and the horizon are the same PLACE --
`P7`'s remark says they are turning points of two energies of one congruence, which is a statement
about kind and not about location, and that is the weight it is carried at here.  Ⓗ's parallel with a
Schwarzschild interior is a structural reading of signs the corpus computes, not a derivation that the
lap IS such an interior.  It does not re-derive the Nariai condition, `prop:flat`, or `P1`'s theorem.
It computes nothing about what any locus does to a mode crossing it; that remains `PO-75`'s open
question and is ORDERED elsewhere.

Built r7187 (node 66).  Stated for reversal.
"""
import io
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        fails.append(label)


def head(t):
    print('\n' + '=' * 100 + f"\n  {t}\n" + '=' * 100)


def body(name):
    """Paper source with whitespace collapsed, so a literal that straddles a LaTeX line wrap is
    still read.  A pin that fails on where the source breaks its lines is a defect in the pin."""
    raw = io.open(os.path.join(ROOT, 'corpus', name), encoding='utf-8').read()
    return ' '.join(raw.split())


def f_(r, m, a):
    return 1.0 - 2.0 * m / r - r * r / (a * a)


def fp_(r, m, a):
    return 2.0 * m / (r * r) - 2.0 * r / (a * a)


# ---------------------------------------------------------------- A
head("A -- ON THE COLLAPSE SHEET f IS MONOTONE, FOR EVERY MASS AND EVERY THROAT CONSTANT")
print("      f' = 2M/r^2 - 2r/alpha^2 .  For r < 0 the first term is > 0 and the second is -2r/a^2 > 0,")
print("      so f' is a sum of two POSITIVE terms and f is strictly increasing in r on the whole sheet.")
grid, ok_mono, ok_one, ok_simple = [], True, True, True
for a in (0.5, 1.0, 3.0, 25.0):
    for m in (0.001 * a, 0.05 * a, 0.19 * a, a / (3 * math.sqrt(3))):
        rr = -np.logspace(math.log10(1e-6 * a), math.log10(400.0 * a), 400001)
        v = f_(rr, m, a)
        d = fp_(rr, m, a)
        n = int((np.diff(np.sign(v)) != 0).sum())
        ok_mono &= bool((d > 0).all())
        ok_one &= (n == 1)
        # the root, by bisection, and its order: f(root)=0 while f'(root) != 0
        lo, hi = -400.0 * a, -1e-9 * a
        for _ in range(300):
            mid = 0.5 * (lo + hi)
            if f_(mid, m, a) < 0:
                lo = mid
            else:
                hi = mid
        rh = 0.5 * (lo + hi)
        ok_simple &= (abs(f_(rh, m, a)) < 1e-9 and abs(fp_(rh, m, a)) > 1e-9)
        grid.append((a, m, n, rh, fp_(rh, m, a), float(d.min())))
for a, m, n, rh, d, dmin in grid[:6] + grid[-3:]:
    print(f"        alpha={a:<6g} M={m:<10.6f} roots on r<0: {n}   root r={rh:+.8f}   "
          f"f'(root)={d:+.6f}   min f' on sheet={dmin:+.3e}")
print(f"      ... {len(grid)} (M, alpha) pairs in all")
check("Ⓐ①  f' > 0 at every sampled point of the collapse sheet, for all 16 (M, alpha) pairs -- f is "
      "strictly monotone there, which is read off the two terms' signs and not from this sample",
      ok_mono)
check("Ⓐ②  so the sheet carries EXACTLY ONE root of f, at every pair sampled",
      ok_one and all(n == 1 for *_, in [] ) is not False and all(g[2] == 1 for g in grid))
check("Ⓐ③  and that root is SIMPLE -- f vanishes there and f' does not, at every pair",
      ok_simple)
A1 = 1.0
MN = A1 / (3 * math.sqrt(3))
RB, RF = -2 * A1 / math.sqrt(3), A1 / math.sqrt(3)
check("Ⓐ④  on the forced member that root is the BACK SEAM, r = -2 alpha/sqrt3",
      abs(f_(RB, MN, A1)) < 1e-12 and abs(fp_(RB, MN, A1) - 9 / (2 * math.sqrt(3))) < 1e-12)

# ---------------------------------------------------------------- B
head("B -- AND ITS SIGNATURE IS A COSMOLOGICAL HORIZON'S, WHICH IS THE REVERSE OF A BLACK HOLE'S")
print("      f < 0 means r is TIMELIKE; f > 0 means the region is STATIC and r spacelike.")
print(f"      on the forced member: f(-10a)={f_(-10,MN,A1):+.4f}  f(-2a)={f_(-2,MN,A1):+.4f}  "
      f"f(seam)={f_(RB,MN,A1):+.1e}  f(-0.5a)={f_(-0.5,MN,A1):+.4f}  f(-0.01a)={f_(-0.01,MN,A1):+.2f}")
check("Ⓑ①  OUTSIDE the back seam the radius is timelike, INSIDE it the geometry is static -- and stays "
      "static all the way to the branch point, f diverging to +infinity as r -> 0 from below",
      f_(-10, MN, A1) < 0 and f_(-2, MN, A1) < 0
      and f_(-0.5, MN, A1) > 0 and f_(-0.01, MN, A1) > 0 and f_(-1e-8, MN, A1) > 1e7)
ok_sig, rows = True, []
for m in (0.05, 0.12, 0.19):
    c = sorted(x.real for x in np.roots([-1.0, 0.0, 1.0, -2 * m]) if abs(x.imag) < 1e-10)
    r3, rb, rc = c
    bh = (f_(rb * 0.97, m, 1.0), f_(rb * 1.03, m, 1.0))      # (inside, outside)
    cos = (f_(rc * 0.97, m, 1.0), f_(rc * 1.03, m, 1.0))
    thr = (f_(r3 * 0.97, m, 1.0), f_(r3 * 1.03, m, 1.0))     # (nearer r=0, further out)
    rows.append((m, r3, rb, rc, bh, cos, thr))
    print(f"        M={m}: r3={r3:+.6f} rb={rb:+.6f} rc={rc:+.6f}")
    print(f"           black-hole root : f inside={bh[0]:+.4f}  f outside={bh[1]:+.4f}   "
          f"(timelike INSIDE, static OUTSIDE)")
    print(f"           cosmological    : f inside={cos[0]:+.4f}  f outside={cos[1]:+.4f}   "
          f"(static INSIDE, timelike OUTSIDE)")
    print(f"           third root      : f nearer r=0={thr[0]:+.4f}  f further out={thr[1]:+.4f}   "
          f"-> the COSMOLOGICAL pattern")
    ok_sig &= (bh[0] < 0 < bh[1]) and (cos[0] > 0 > cos[1]) and (thr[0] > 0 > thr[1])
check("Ⓑ②  ** at three sub-Nariai members, where the black-hole and cosmological roots are DISTINCT, "
      "the third root carries the cosmological root's signature and the exact reverse of the "
      "black-hole root's ** -- static on the side towards r = 0, timelike on the far side",
      ok_sig)
check("Ⓑ③  and the collapse sheet carries NO black-hole root to compare with: by Ⓐ its only root is "
      "this one, so there is no locus on it with the black-hole signature at all",
      all(g[2] == 1 for g in grid))

# ---------------------------------------------------------------- C
head("C -- SO THE ONE ROOT, ITS NON-ZERO SURFACE GRAVITY AND THE ABSENT BALANCE RADIUS ARE ONE FACT")
print("      f' = 0  <=>  r^3 = M alpha^2 > 0, which has no negative real solution.")
print(f"      on the forced member the balance radius is (M a^2)^(1/3) = "
      f"{(MN*A1**2)**(1/3.):.10f} = alpha/sqrt3 = {RF:.10f}, the FRONT seam")
print(f"      f' on the sheet: f'(-2a)={fp_(-2,MN,A1):+.6f}  f'(seam)={fp_(RB,MN,A1):+.6f}  "
      f"f'(-0.5a)={fp_(-0.5,MN,A1):+.6f}  -- never zero")
check("Ⓒ①  the balance radius f' = 0 sits at +(M alpha^2)^(1/3) and so on NO collapse sheet, for any "
      "mass or throat constant -- r^3 = M alpha^2 is positive",
      abs((MN * A1 ** 2) ** (1 / 3.) - RF) < 1e-12)
check("Ⓒ②  ** and that is the SAME statement as the seam's surface gravity being non-zero: kappa = "
      "|f'|/2 at the root, and f' is what does not vanish on the sheet ** -- so one root, kappa != 0 "
      "and no balance radius are three readings of f' > 0 and not three facts",
      abs(abs(fp_(RB, MN, A1)) / 2 - 3 * math.sqrt(3) / 4) < 1e-12 and ok_mono)
P07 = body('CR_framework.tex')
check("Ⓒ③  and `P7` already prints the balance radius AT the front seam -- the Hubble--Eddington "
      "radius among the four readings that meet there",
      'the \\emph{Hubble--Eddington radius} $r_{\\mathrm{HE}}=(M\\alpha^{2})^{1/3}$' in P07)

# ---------------------------------------------------------------- D
head("D -- AND LAMBDA > 0 IS WHAT TURNS THAT ROOT ON: AT LAMBDA = 0 THE SHEET IS HORIZONLESS")
print("      at Lambda = 0 the second term of f is absent and f = 1 - 2M/r, which on r < 0 is 1 + 2M/|r|")
for m in (0.05, 0.19245, 1.0):
    vals = [1 - 2 * m / r for r in (-1e-4, -1.0, -1e4)]
    print(f"        M={m:<9g} f(-1e-4)={vals[0]:+.4e}  f(-1)={vals[1]:+.6f}  f(-1e4)={vals[2]:+.8f}"
          f"   -> all > 1, no root")
check("Ⓓ①  at Lambda = 0 the collapse sheet has NO root: f = 1 - 2M/r > 1 for every r < 0 and every "
      "M > 0, so the sheet is static and horizonless throughout",
      all(1 - 2 * m / r > 1 for m in (0.05, 0.19245, 1.0) for r in (-1e-4, -1.0, -1e4)))
P02 = body('janzen_circle_v3.tex')
check("Ⓓ②  which is `P2`'s own proof, read from its source -- f = coth^2 on the back-seam regions, so "
      "they contain no horizon and are static and asymptotically flat",
      'the back-seam regions contain no horizon, and are static and asymptotically flat as $r \\to '
      '-\\infty$' in P02)
check("Ⓓ③  ** so the collapse sheet's one horizon is exactly what the cosmological constant adds to "
      "it ** -- and `P2` records the two roots it adds as absent at Lambda = 0",
      'the cosmological horizon and its backward-radial partner---are absent' in P02)

# ---------------------------------------------------------------- E
head("E -- THE TWO ENERGIES: THE SEAMS ARE WHERE E=0 TURNS AND THE TURNAROUND IS WHERE E=1 DOES")
R_TURN = -(2 * MN * A1 ** 2) ** (1 / 3.)
for E in (0.0, 1.0):
    co = [1.0, 0.0, (E ** 2 - 1) * A1 ** 2, 2 * MN * A1 ** 2]
    rt = sorted(set(round(x.real, 10) for x in np.roots(co) if abs(x.imag) < 1e-7))
    print(f"      E={E}: r^3 + (E^2-1) a^2 r + 2 M a^2 = 0  ->  real roots {rt}")
check("Ⓔ①  E = 0 gives the HORIZON cubic, whose roots are the two seams -- f = 0 there",
      abs(f_(RB, MN, A1)) < 1e-12 and abs(f_(RF, MN, A1)) < 1e-12
      and abs(RB ** 3 - A1 ** 2 * RB + 2 * MN * A1 ** 2) < 1e-12
      and abs(RF ** 3 - A1 ** 2 * RF + 2 * MN * A1 ** 2) < 1e-12)
check("Ⓔ②  E = 1 gives r^3 + 2 M a^2 = 0, the comoving TURNAROUND at -(2 M a^2)^(1/3), where f = 1 "
      "exactly and the marginal rate 1 - f vanishes",
      abs(R_TURN ** 3 + 2 * MN * A1 ** 2) < 1e-12 and abs(f_(R_TURN, MN, A1) - 1.0) < 1e-12)
check("Ⓔ③  ** and the family is `P7`'s own result, read from its source: one congruence indexed by "
      "energy, the two ends being the horizon cubic and the turnaround cubic ** -- so the turnaround "
      "stands to the cosmological member as a horizon does to the maximally bound one, which is a "
      "statement about KIND and not about location",
      'The two turning cubics are two energies of one congruence]\\label{rem:tworealisations} The inequivalence of Lemma~\\ref{lem:twoturnings} is n' in P07
      and 'the marginally bound member $E=1$' in P07
      and 'gives $r^{3}-\\alpha^{2}r+2M\\alpha^{2}=0$, the horizon cubic $f=0$' in P07)

# ---------------------------------------------------------------- F
head("F -- THE LIFT IS THE STRETCH FORBIDDEN TO E=1, AND ITS LAW IS TRIGONOMETRIC AGAINST THE LEGS'")
print("      inside the turnaround f > 1, so (dr/dtau)^2 = 1 - f < 0 for the marginal congruence:")
for x in (0.99, 0.5, 0.1):
    r = R_TURN * x
    print(f"        r={r:+.6f}   f={f_(r,MN,A1):+.6f}   1-f={1-f_(r,MN,A1):+.6f}")
check("Ⓕ①  the whole stretch between the turnaround and the branch point is classically forbidden to "
      "the E = 1 member, 1 - f being negative throughout -- which is why cosmic time turns there",
      all(1 - f_(R_TURN * x, MN, A1) < 0 for x in (0.999, 0.9, 0.5, 0.1, 0.01)))
S_END = math.pi * A1 / 3.0
law = lambda s: -(2 * MN * A1 ** 2) ** (1 / 3.) * abs(math.sin(3 * s / (2 * A1))) ** (2 / 3.)
print(f"      lift law r(s) = -(2 M a^2)^(1/3) |sin(3 s / 2 a)|^(2/3), s the path length:")
for s in (0.0, 0.25 * S_END, 0.5 * S_END, 0.75 * S_END, S_END):
    print(f"        s = {s:.6f} a   r = {law(s):+.8f}")
check("Ⓕ②  that law joins the BRANCH POINT at s = 0 to the TURNAROUND at s = pi alpha / 3, monotonically "
      "-- the lift's own path length, and `P7`'s printed value for it",
      abs(law(0.0)) < 1e-12 and abs(law(S_END) - R_TURN) < 1e-12
      # r runs from 0 at the branch point DOWN to the turnaround, so monotone DECREASING in s
      and all(law(s) > law(s + 1e-3) for s in np.linspace(1e-3, S_END - 2e-3, 400))
      and 'of path length $\\pi\\alpha/3$' in P07)
check("Ⓕ③  ** against the real legs' HYPERBOLIC law, cosh^(2/3) on the collapse leg and sinh^(2/3) on "
      "the expansion leg ** -- so the lift is trigonometric where the legs are hyperbolic",
      'r(s)=-(2M\\alpha^{2})^{1/3}\\bigl\\lvert\\sin(3s/2\\alpha)\\bigr\\rvert^{2/3}' in P07
      # the collapse leg's own printed law, not a bare `sinh^{2/3}` fragment: that occurs in
      # several places in the paper and a pin on it is a pin on the file
      and 'r=(2M\\alpha^{2})^{1/3}\\sinh^{2/3}(3\\tilde\\tau/2\\alpha)' in P07)
check("Ⓕ④  and that pairing is `P2`'s own for the black hole itself -- one analytic curve, hyperbola "
      "then circle then hyperbola, the trigonometric functions becoming hyperbolic under the "
      "continuation that leaves the interior arc",
      's a single analytic curve---hyperbola, circle, hyperbola' in P02
      and 'The trigonometric functions become hyperbolic' in P02)

# ---------------------------------------------------------------- G
head("G -- AND THE TWO LEVELS ARE EACH IN PRINT, WHICH IS WHAT THE CORRECTED STATEMENT RESTS ON")
P03 = body('SdS-slicing-curve_v2.tex')
phi = lambda r: 2 * math.pi * r / (math.sqrt(3) * A1)
print(f"      phase phi = 2 pi r / sqrt3 alpha:  front seam {math.degrees(phi(RF)):+.4f} deg, "
      f"back seam {math.degrees(phi(RB)):+.4f} deg, difference "
      f"{math.degrees(phi(RF)-phi(RB)):+.4f} deg")
check("Ⓖ①  the two seams are ONE substrate point: in the phase they differ by exactly a full turn, "
      "360 degrees, which is `P2`'s own argument and its own conclusion",
      abs(math.degrees(phi(RF) - phi(RB)) - 360.0) < 1e-9
      and 'one point of the underlying geometry' in P02
      and 'the outer two differ by a full turn' in P02)
check("Ⓖ②  `P3` names the back seam for what it is at substrate level -- the backward-radial root the "
      "lap closes on, the merged-horizon value re-entered",
      'closing at the backward-radial root $-2\\alpha/\\sqrt3$, the merged-horizon value re-entered'
      in P03)
check("Ⓖ③  ** and `P7` already holds two levels apart for the neighbouring pair, in the remark this "
      "statement belongs beside ** -- the locus the causal reassignment acts on and the locus the "
      "observable cosmology begins at are distinct loci of one curve, claims at different levels and "
      "not competing ones",
      'Two levels must be held apart' in P07
      and 'the locus the reassignment acts on and the locus the observable cosmology begins at are '
          'distinct loci of the one curve, claims at different levels and not competing ones' in P07)
check("Ⓖ④  so the local reading and the substrate identification are claims at DIFFERENT levels, and "
      "the paper now says which is which rather than printing either as a flat identity",
      # the one sentence the paper actually carries, pinned whole rather than as a disjunction of
      # short phrases -- a three-way `or` over fragments is three pins on the file
      'the same locus presents as the cosmological horizon of the mass rather than as a black '
      "hole's" in P07)

# ---------------------------------------------------------------- H
head("H -- AND THE TWO MARKS OF A SCHWARZSCHILD INTERIOR FALL AT DIFFERENT LOCI OF THE LAP")
print("      inside a Schwarzschild horizon TWO things happen together: the static time stops being a")
print("      time, and the radius becomes the clock.  On the lap they are at different loci:")
print(f"        the LIFT       : 1 - f < 0, so cosmic time turns imaginary   "
      f"(1-f at mid-lift = {1-f_(R_TURN*0.5,MN,A1):+.6f})")
print(f"        the BRANCH POINT: f changes sign through infinity, r spacelike -> timelike   "
      f"(f(-0.01a) = {f_(-0.01,MN,A1):+.2f}, f(+0.01a) = {f_(0.01,MN,A1):+.2f})")
check("Ⓗ①  across the lift the marginal rate is imaginary while f stays POSITIVE -- the region is "
      "static in f and forbidden in the rate, so what turns there is the time and not the radius",
      all(f_(R_TURN * x, MN, A1) > 1 for x in (0.9, 0.5, 0.1)))
check("Ⓗ②  at the branch point f changes sign through INFINITY rather than through zero, so the radius "
      "turns from spacelike to timelike there and takes up the clock",
      f_(-0.01, MN, A1) > 0 and f_(0.01, MN, A1) < 0 and abs(f_(-1e-9, MN, A1)) > 1e8)
check("Ⓗ③  ** which is `P7`'s own stratification, read from its source: the back seam timelike to "
      "spacelike, and the branch point spacelike to timelike and imaginary to real together, through "
      "infinity rather than through zero **",
      'back seam (timelike to spacelike)' in P07
      and 'the branch point (spacelike to timelike and imaginary to real together, through infinity '
          'rather than through zero)' in P07)

head("J -- AND WHAT THE CAUSAL REASSIGNMENT ACTS ON, WHICH IS NOT ON THIS SHEET AT ALL")
check("Ⓙ①  `P7`'s trichotomy classifies by how the reassigned null congruence meets the horizon, and "
      "the case it selects is TANGENCY AT A MERGED DOUBLE ROOT -- read from its own source",
      'tangency at a merged double root' in P07
      and 'the limiting orientation the horizon selects is \\emph{tangent} rather than transverse'
      in P07)
check("Ⓙ②  and the merged double root is where the two POSITIVE horizons merge, which is the front "
      "seam at +alpha/sqrt3 -- so the locus the reassignment acts on lies on the r > 0 sheet",
      'the two positive horizons merge' in P07
      and abs(fp_(RF, MN, A1)) < 1e-12 and RF > 0)
check("Ⓙ③  ** which `P7` already names: the reassignment acts on a finite-curvature locus at "
      "alpha/sqrt3 ** -- so the collapse sheet's having no black-hole root is not a gap in the "
      "account.  The reassignment's locus is not on that sheet, and the back seam is that same "
      "substrate point met a lap earlier",
      'a finite-curvature locus at $\\alpha/\\sqrt3$' in P07
      and all(g[2] == 1 for g in grid))     # one root on r<0, from group A, at every (M, alpha)

print()
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print('      - ' + x)
    sys.exit(1)
print(f"""
==========================================================================================
  THE LAP IS A COLLAPSE READ ON THE COSMIC CLOCK.

  On the sheet the collapse runs on, f is MONOTONE -- f' is a sum of two
  positive terms for every r < 0.  That single fact forces three things at
  once: the sheet carries exactly ONE root of f, that root is SIMPLE, and
  there is NO balance radius anywhere on it.  So the back seam's non-zero
  surface gravity, kappa = 3 sqrt3 / 4 alpha, and the Hubble--Eddington
  radius sitting at the FRONT seam instead are not two facts but one.

  And the signature of that root is a COSMOLOGICAL horizon's, not a black
  hole's: timelike outside, static inside, verified against both root types
  of three sub-Nariai members where the two are still distinct.  Beyond it
  the region runs out asymptotically de Sitter; inside it the geometry is
  static down to the branch point, with no black-hole root on the sheet at
  all.  At Lambda = 0 the sheet has no root whatever, which is `P2`'s own
  proof -- so this one horizon is exactly what the cosmological constant
  adds.

  LEVELS.  At substrate level the back seam is the backward-radial root the
  lap closes on, the merged-horizon value re-entered, one point with the
  front seam a full turn away in the phase.  Locally, on the collapse sheet,
  it presents as the cosmological horizon of the mass.  Both hold, and `P7`
  already holds exactly this kind of pair apart for the reassignment's locus
  and the cosmology's beginning.

  THE REST OF THE LAP.  The turnaround is where the E = 1 member of one
  energy-indexed congruence turns, as the seams are where the E = 0 member
  does -- the same kind of point for two energies, which is `P7`'s own
  result and not a claim that they are the same place.  Inside the
  turnaround the E = 1 member is classically forbidden, 1 - f < 0
  throughout, so cosmic time turns imaginary across the lift; the lift's law
  is trigonometric, |sin(3s/2a)|^(2/3), joining the branch point at s = 0 to
  the turnaround at s = pi a / 3, against the hyperbolic law of both real
  legs -- `P2`'s own trigonometric-inside, hyperbolic-outside pairing.

  AND THE TWO MARKS OF A SCHWARZSCHILD INTERIOR ARE SPLIT.  Time ceasing to
  be real happens on the LIFT, where f stays positive and the rate goes
  imaginary.  The radius becoming the clock happens at the BRANCH POINT,
  where f changes sign through infinity.  One interior's two signatures, at
  two loci of one curve.
==========================================================================================
""")
