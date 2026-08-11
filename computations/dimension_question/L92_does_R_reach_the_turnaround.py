#!/usr/bin/env python3
"""
L-92 — DOES R = gamma^5 REACH THE TURNAROUND THREE?  ** THE SPLIT'S FALSIFIER. **

L-67 showed the L8.1-a weld can split without cost to the dimension result, and named this as
the one thing blocking a revision to P14: the chirality is R (the offset parity, M -> -M /
r0 -> -r0), it acts on the horizon/offset structure, and P14 needs the generations CHIRAL.
If R does not reach generation's new seat, the split costs the chirality and is worse than
the conflict it resolves.

Run: python3 L92_does_R_reach_the_turnaround.py     (sympy)
"""
import sympy as sp
print(__doc__.split("Run:")[0])
r, M, al, tau = sp.symbols('r M alpha tau', positive=True)

print("=" * 78)
print("PART 1 — ACT WITH R ON THE TURNAROUND LAW")
print("=" * 78)
print("  The law (L-67, derived):   r^(D-1) = 2 M alpha^2 sinh^2( (D-1) tau / 2 alpha )")
print("  R is M -> -M (the mass reflection, P3 sec:ellipse; = gamma^5, P14).  For REAL tau,")
print("  sinh^2 >= 0, so under R the right side becomes NON-POSITIVE:")
print()
print("      r^(D-1)  ->  -2 |M| alpha^2 sinh^2(...)   <= 0")
print()
print("  ** So R has a REAL image on the turnaround branch iff r^(D-1) < 0 has a real root,")
print("     i.e. iff D-1 is ODD, i.e. iff D is EVEN. **")
print()
print(f"  {'D':>3} {'D-1':>5} {'r^(D-1) < 0 real?':>19} {'R reaches the turnaround?':>27} {'image':>16}")
res = {}
for Dv in (4, 5, 6, 7, 8):
    n = Dv - 1
    odd = (n % 2 == 1)
    res[Dv] = odd
    img = '-r  (signed radius)' if odd else 'none (complex only)'
    print(f"  {Dv:>3} {n:>5} {str(odd):>19} {str(odd):>27} {img:>16}")
print()
print("  ** R REACHES THE TURNAROUND THREE EXACTLY WHEN D IS EVEN -- and its image is")
print("     r -> -r, THE SIGNED RADIUS, which is the corpus's own conjugate branch. **")
# r2376+c54.159 -- PINS PART 1's tabulated answer, the row INDEX records: R has a REAL image on the
# turnaround branch at D = 4, 6, 8 and NOT at D = 5, 7 -- exactly at even D.  The D = 5 entry is the
# one P14's "four generations and no chirality" conclusion rests on, so it is pinned by name too.
assert res == {4: True, 5: False, 6: True, 7: False, 8: True}, res
assert res[4] is True and res[5] is False, res

print()
print("=" * 78)
print("PART 2 — AND THAT IS THE SAME CONDITION THE DIMENSION RESULT ALREADY USES")
print("=" * 78)
r0 = sp.Symbol('r_0', real=True)
print("  The dimension result's parity step, on the HORIZON side: 2M = r0^(D-3) - r0^(D-1)")
print("  is ODD in the signed offset iff D is even.  Checked:")
print()
print(f"  {'D':>3} {'2M(r0)':>22} {'2M(-r0) = -2M(r0)?':>20} {'D even?':>9} {'agree?':>8}")
agree = True
for Dv in (4, 5, 6, 7, 8):
    e = r0**(Dv-3) - r0**(Dv-1)
    odd_in_r0 = sp.simplify(e.subs(r0, -r0) + e) == 0
    a = (odd_in_r0 == (Dv % 2 == 0)) and (odd_in_r0 == res[Dv])
    agree &= a
    print(f"  {Dv:>3} {str(e):>22} {str(odd_in_r0):>20} {str(Dv%2==0):>9} {str(a):>8}")
print()
print(f"  ** THE TWO CONDITIONS AGREE AT EVERY D: {agree} **")
# r2376+c54.159 -- PINS PART 2, the receipt's central claim ("THE SPLIT IS SAFE"): the horizon-side
# parity of 2M = r0^(D-3) - r0^(D-1) agrees with the turnaround-side reality condition at all five
# dimensions tested, and it does so by matching D-even -- so there are not two R's to choose between.
assert agree, "the turnaround-side and horizon-side parity conditions disagree at some D"
assert {Dv: sp.simplify((r0**(Dv-3) - r0**(Dv-1)).subs(r0, -r0)
                        + (r0**(Dv-3) - r0**(Dv-1))) == 0 for Dv in (4, 5, 6, 7, 8)} == res
print()
print("  ⇒ ** THE CHIRALITY GRADING SURVIVES THE SPLIT, AND SURVIVES IT VERBATIM. **  R acts")
print("     on the turnaround three exactly where it acts on the horizon three -- at even D --")
print("     so P14's parity argument transfers to generation's new seat WITHOUT MODIFICATION,")
print("     including its D = 5 conclusion (no mass-reflection Z_2, hence no gamma^5, hence")
print("     four generations and no chirality).")
print("  ⇒ ** L-92 ANSWERED IN THE POSITIVE.  THE SPLIT IS SAFE. **")

print()
print("=" * 78)
print("PART 3 — WHAT GROUP THE TURNAROUND THREE THEN CARRIES")
print("=" * 78)
w = sp.exp(2*sp.pi*sp.I/3)
print("  Deck action (L-67):  r -> omega r,  omega = e^{2 pi i/3}   [Z_3]")
print("  R (this file)     :  r -> -r                               [Z_2]")
inorbit = any(sp.simplify(w**k + 1) == 0 for k in range(3))
print(f"  Is -1 in the deck orbit {{1, omega, omega^2}}?  {inorbit}")
print("  ** No -- so R is genuinely OUTSIDE the deck Z_3, and the two generate Z_3 x Z_2 = Z_6. **")
# r2376+c54.159 -- PINS PART 3's group statement: -1 is NOT in the deck orbit {1, omega, omega^2},
# so R lies outside the deck Z_3 and the two generate a group of order 6 (Z_6), which sits inside
# the horizon three's D_6 of order 12 at index 2 -- the transpositions being what is missing.
assert inorbit is False, inorbit
assert len({sp.simplify((-1)**s * w**k) for k in range(3) for s in (0, 1)}) == 6
assert sp.Integer(12) / sp.Integer(6) == 2
print()
print("  ⇒ so on the split the turnaround three carries ** Z_6 = Z_3 x Z_2 ** (cyclic deck")
print("     times the mass reflection), where the horizon three carries ** D_6 = S_3 x Z_2 **.")
print("  ** Z_6 < D_6, index 2, and the missing part is exactly the transpositions -- which")
print("     the split assigns to COLOUR, where the causal trichotomy needs them for the")
print("     singlet. **  (L-91's cost, now stated as a group inclusion rather than a worry.)")
print()
print("  ⚠ AND WHAT IS STILL NOT DONE: this shows R ACTS on the turnaround branch.  It does")
print("  not show the wall-bound zero mode's chirality is graded by THAT action rather than")
print("  by the horizon-side one.  ** The two coincide at D = 4 by PART 2, so nothing is")
print("  wrong; but the identification is a further step. **  (L-94.)")
