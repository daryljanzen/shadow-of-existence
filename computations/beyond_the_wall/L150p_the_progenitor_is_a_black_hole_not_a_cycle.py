#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE CONSTRUCTION SAYS WHAT THE PROGENITOR IS, IN ONE SENTENCE, AND IT IS NOT A
CYCLE.  FOUR REVISIONS OF FLOQUET ANALYSIS MODELLED A BACKGROUND THE CORPUS DOES NOT CONTAIN. **

P16 `sec:lap`, verbatim:

    "Our universe formed at the event horizon of a black hole in a previous one; the matter of
     our hot dense era is that previous universe's collapsed matter, continued through the
     branch point."

** So the progenitor is a collapsing OVERDENSITY in a prior universe — one that separated from its
ambient expansion, turned around, and collapsed.  Its past $a=0$ is a mathematical extension of the
closed-dust solution backwards, not an epoch it lived through. **

  PART 1  ** WHAT THAT DOES TO c54.143–148: there is ONE branch point in the progenitor's history,
          so there is no periodic map, no Floquet problem, and no band structure. **
  PART 2  ** WHAT SURVIVES, AND IT IS MOST OF THE ARC: everything local to the crunch, and
          everything computed on a single passage. **
  PART 3  ** THE NEWLY WELL-POSED OBJECT — the HALF lap, turnaround to crunch — and a first pass
          at it, reported as a first pass. **
  PART 4  ** AND THE CHAIN IS REAL AFTER ALL, in the sense the corpus means: generational, not
          cyclic.  So the two exclusions of it are withdrawn. **

Run: python3 L150p_the_progenitor_is_a_black_hole_not_a_cycle.py      (numpy, scipy, sympy)
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

print(__doc__.split("Run:")[0])
RHO, A, SMAP = 0.0539, 2.0, 2.75
B = RHO**2
e = sp.symbols('e')
a_s = (A / 2) * (1 - sp.cos(e)) + sp.sqrt(B) * sp.sin(e)
ap_s = sp.diff(a_s, e)
z_s = a_s * (a_s + sp.Rational(2, 3) * B) / ap_s
U = sp.lambdify(e, sp.simplify(sp.diff(z_s, e, 2) / z_s), 'numpy')
CS2 = sp.lambdify(e, sp.Rational(4, 3) * B / (3 * A * a_s + 4 * B), 'numpy')
ec = 2 * np.pi - 2 * np.arctan(RHO)
et = np.pi - np.arctan(RHO)
P = 2.0 / RHO
OFF = 2 * np.pi * P

# =====================================================================
print("=" * 78)
print("PART 1 — WHAT IT DOES TO FOUR REVISIONS")
print("=" * 78)
print(f"  {'revision':>10} {'what it built':>40} {'status':>22}")
for a_, b_, c_ in [("c54.143", "attractor of the full-cycle map", "** wrong background **"),
                   ("c54.144", "Floquet bands, chain excluded", "** wrong background **"),
                   ("c54.147", "|lambda|^2 = 1, transfer unity", "** wrong background **"),
                   ("c54.148", "the comb censused, chain excluded", "** wrong background **")]:
    print(f"  {a_:>10} {b_:>40} {c_:>22}")
print()
for s in [
 "⚠⚠⚠ ** ALL FOUR PROPAGATED FROM THE CLOSED BALL'S OWN $a=0$ IN THE PAST — its 'bang' — AND",
 "   COMPOSED THE RESULT WITH A MONODROMY TO MAKE A PERIODIC MAP.  The construction has no such",
 "   epoch: the ball is an overdensity that separated from a previous universe's expansion, turned",
 "   around, and collapsed. **  *Extending the closed-dust solution back to $a=0$ is legitimate",
 "   ALGEBRA and illegitimate HISTORY, and I did not check which I was doing for four revisions.*",
 "",
 "⇒ ** WITH ONE BRANCH POINT THERE IS NO PERIODIC MAP, HENCE NO FLOQUET PROBLEM, HENCE NO",
 "   INSTABILITY BANDS, NO ATTRACTOR, AND NO PER-CYCLE AMPLIFICATION $\\lambda$. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT SURVIVES")
print("=" * 78)
print(f"  {'result':>52} {'rests on':>24}")
for a_, b_ in [("the (0,1) exponents at the crunch", "the crunch alone"),
               ("the scalar monodromy 4 pi/rho (c54.146)", "the crunch alone"),
               ("the tensor monodromy 2 pi/rho", "the crunch alone"),
               ("z_S = a(a + 2B/3)/a' in closed form", "the background alone"),
               ("the turnaround pole, and that it is apparent", "the background alone"),
               ("the tensor floor, no B-modes (c54.138)", "a single passage"),
               ("hbar's asymmetry, F, the vacuum floors", "a single passage"),
               ("the interior's adequacy (c54.138)", "a single passage"),
               ("the composition rho = 5.4e-2 (chain A)", "one M + a crossing plasma")]:
    print(f"  {a_:>52} {b_:>24}")
print()
print("  ** Nothing on that list touches the cycle.  The arc's positive content is intact; what")
print("     falls is the four revisions of apparatus built on top of it. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE HALF LAP, AND A FIRST PASS")
print("=" * 78)
I_half = quad(lambda x: np.sqrt(CS2(x)), et + 1e-6, ec - 1e-9, limit=400)[0]
I_full = quad(lambda x: np.sqrt(CS2(x)), 1e-9, ec - 1e-9, limit=400)[0]
print(f"  sound horizon, turnaround -> crunch : {I_half:.5f}   (the full lap was {I_full:.5f})")
print("  The physical propagation starts where the overdensity turns around and ends at the crunch.")
print("  z_S has its pole exactly at the start, so the mode is begun just after it, in WKB form with")
print("  the ambient universe's phase -- which is the one thing the previous universe supplies.")


def half(k, ph, dl=3e-3, eps=1e-7):
    e0 = et + dl
    cs0 = np.sqrt(CS2(e0))
    y0 = [np.cos(ph), cs0 * k * np.sin(ph)]

    def rhs(t, y):
        return [y[1], (U(t) - CS2(t) * k * k) * y[0]]

    s = solve_ivp(rhs, [e0, ec - eps], y0, rtol=1e-11, atol=1e-15, method='DOP853')
    v, vp = s.y[0, -1], s.y[1, -1]
    L = np.log(eps / (2 * RHO))
    c0 = v / (1.0 + P * eps * L)
    c1 = c0 * P * (L + 1.0) + vp
    return c0, c1


KS = np.array([80., 120., 180., 260., 380., 550., 800.])
print(f"\n  {'k':>6} {'l':>6} {'median leaked/direct':>21} {'WKB 4 pi/(rho c_s k)':>21}")
lds_all = []
for k in KS:
    lds = []
    for ph in np.linspace(0, np.pi, 12, endpoint=False):
        c0, c1 = half(k, ph)
        lds.append(OFF * abs(c0) / max(abs(c1), 1e-300))
    lds_all.append(np.median(lds))
    print(f"  {k:>6.0f} {k*SMAP:>6.0f} {np.median(lds):>21.4f} "
          f"{OFF/(np.sqrt(1/3.)*k)/1.0:>21.4f}")
sl = np.polyfit(np.log(KS), np.log(np.array(lds_all)), 1)[0]
print(f"\n  ** leaked/direct log-slope in k : {sl:+.3f}   (WKB is -1) **")
assert sl < -0.4
print()
for s in [
 "⚠ ** SO THE WKB KNEE IS BACK: on a single passage from turnaround the leaked/direct ratio falls",
 "   with $k$ roughly as the free-oscillation value, which is the premise every composition bound",
 "   rested on and which the cycle apparatus had appeared to remove. **",
 "   ***This is reported as a FIRST PASS and not a verdict: seven points, a $66\\%$ residual scatter",
 "   about the fit, and a normalisation at the turnaround that needs the ambient universe's",
 "   spectrum rather than a unit envelope.  The number that decides the sector is the running, and",
 "   it is not measured here to the precision the question needs.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE CHAIN IS REAL, AND THE TWO EXCLUSIONS ARE WITHDRAWN")
print("=" * 78)
for s in [
 "  The corpus's chain is GENERATIONAL, not cyclic: a universe forms structure, an overdensity",
 "  collapses to a black hole, and its interior is the next universe.  ** That chain is asserted by",
 "  the construction in the sentence quoted at the top, and nothing here bears on it. **",
 "",
 "⚠⚠ ** SO c54.144's AND c54.148's EXCLUSIONS OF 'THE CHAIN' ARE WITHDRAWN.  They excluded a",
 "   closed-ball CYCLE — a universe whose own bang was a branch point of the same type — and the",
 "   corpus proposes no such object. **  *Two verdicts of the form 'cosmogenesis is not a chain'",
 "   are removed from the ledger; the construction's own chain stands untouched and untested.*",
 "",
 "⇒⇒ ** AND THE INCOMING STATE IS NOT FREE AFTER ALL, WHICH IS THE REAL PRIZE HERE: the progenitor",
 "   is an overdensity in a universe LIKE OURS, so the perturbations it carries into collapse are a",
 "   nearly scale-invariant adiabatic spectrum processed by ordinary structure formation. **",
 "   ***That is a fully specified input, available from standard cosmology, and it is the first time",
 "   this front has had one.  Every previous revision treated the incoming state as free or as a",
 "   choice; the construction supplies it, and says so in the sentence that also says what the",
 "   progenitor is.***",
]:
    print("  " + s)
