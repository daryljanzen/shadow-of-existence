#!/usr/bin/env python3
"""
RECEIPT — P17 (the constant ledger): ** NEITHER REAL FORM OF THE SUBSTRATE SUPPLIES A SECOND SCALE,
SO THE CONSTRUCTION CANNOT FORCE A DIMENSIONLESS MAGNITUDE.  THE SILENCE IS A PROPERTY, NOT A GAP. **

  PART 1  the Wick rotation carries the defining quadric to S^5 of the SAME radius alpha
  PART 2  every curvature invariant on both faces is a pure power of 1/alpha^2
  PART 3  the enumeration of every other candidate, and what remains

rc=0 on success.  Run: python3 P17_no_second_scale_on_either_face.py     (sympy)
"""
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])
al = sp.symbols('alpha', positive=True)
X = sp.symbols('X0:6', real=True)

print("=" * 78)
print("PART 1 — THE ROTATION CARRIES THE RADIUS")
print("=" * 78)
dS = -X[0]**2 + sum(X[i]**2 for i in range(1, 6))
wick = dS.subs(X[0], sp.I * X[0])
S5 = sum(X[i]**2 for i in range(0, 6))
print(f"  dS_5 :  {dS} = alpha^2")
print(f"  X0 -> i X0 :  {sp.simplify(wick)} = alpha^2   =  S^5 of radius alpha")
assert sp.simplify(wick - S5) == 0
print("  ** the rotation acts on the COORDINATE and leaves the right-hand side untouched, so no")
print("     step exists at which a second radius could enter.  The two faces are the two real")
print("     forms of one complex quadric, and a real form does not choose its own radius. **")

print()
print("=" * 78)
print("PART 2 — THE INVARIANTS ON BOTH FACES")
print("=" * 78)
n, K = 5, 1 / al**2
inv = [("Ricci scalar", n * (n - 1) * K),
       ("Ricci squared", n * ((n - 1) * K)**2),
       ("Kretschmann", 2 * n * (n - 1) * K**2)]
for nm, v in inv:
    p = sp.simplify(sp.diff(v, al) * al / v)
    print(f"  {nm:>16} = {str(v):>16}   d ln/d ln alpha = {p}")
    assert p.is_Integer
print("  ** each is a pure power of 1/alpha^2 on both faces: no second constant exists with which")
print("     to form a dimensionless ratio. **")

print()
print("=" * 78)
print("PART 3 — THE ENUMERATION")
print("=" * 78)
for a, b in [("the compact face's radius", "= alpha, forced"),
             ("curvature invariants, either face", "powers of 1/alpha^2"),
             ("the horizon period 2 pi alpha", "built from alpha"),
             ("M and r_0", "moduli: label which solution"),
             ("2/(3 sqrt 3) at Nariai", "one member's value, not a constant")]:
    print(f"  {a:>36}   {b}")
print()
print("  ** SO A DIMENSIONLESS MAGNITUDE CANNOT BE FORCED: it needs two invariants and the")
print("     substrate has one by construction. **")
print("  This is the common root of three separate verdicts already banked: the winding quantises")
print("  and cannot measure a strength; the flat bundle selects and cannot couple; the branch point")
print("  filters and cannot supply a content.")
print()
print("  BOUND: this is about the two faces' GEOMETRY.  Fields living on either face may carry")
print("  their own scales -- but those are CONTENT, adjoined rather than derived, and adjoining one")
print("  is what the corpus's own admissibility criterion rejects.  ** The escape exists and costs")
print("  the thing the programme is for. **")
print()
print("ALL PASS")
sys.exit(0)
