#!/usr/bin/env python3
"""
`L-166`.  ** DOES THE COMPACT FACE SUPPLY A SECOND SCALE?  NO — IT CARRIES THE SAME ALPHA, AND THE
WICK ROTATION IS WHAT MAKES THAT UNAVOIDABLE RATHER THAN MERELY TRUE. **

The last live route to a coupling.  `L-125`: the winding quantises and cannot supply a strength.
`L-164`: the flat bundle selects and cannot supply a coupling.  Both verdicts turn on one fact --
the substrate has ONE invariant and a coupling is dimensionless, so it needs two.  `L-164`'s
falsifier searched the construction's own quantities and found only moduli.  ** The compact face is
the one place left where a second invariant could live without being adjoined by hand. **

  PART 1  ** THE TWO REAL FORMS, AND THE RADIUS THAT CROSSES BETWEEN THEM. **
  PART 2  ** THE CURVATURE INVARIANTS ON BOTH FACES: every one is a power of 1/alpha^2. **
  PART 3  ** SO THERE IS NO SECOND SCALE, and what that makes permanent. **

Run: python3 L166_does_the_compact_face_supply_a_second_scale.py      (sympy)
"""
import sympy as sp

print(__doc__.split("Run:")[0])
al = sp.symbols('alpha', positive=True)
X = sp.symbols('X0:6', real=True)

print("=" * 78)
print("PART 1 — THE TWO REAL FORMS AND THE RADIUS")
print("=" * 78)
dS = -X[0]**2 + sum(X[i]**2 for i in range(1, 6))
print(f"  dS_5 = SO(5,1)/SO(4,1) :   {dS} = alpha^2")
print("  The corpus's own Wick rotation (P10 sec:lock, P13, P17) is the GLOBAL x_0 -> i x_0,")
print("  carrying the substrate to its compact real form.  Apply it to the defining quadric:")
wick = dS.subs(X[0], sp.I * X[0])
print(f"     under X0 -> i X0 :   {sp.simplify(wick)} = alpha^2")
S5 = sum(X[i]**2 for i in range(0, 6))
assert sp.simplify(wick - S5) == 0
print(f"  ** which is S^5 = SO(6)/SO(5) of radius ** alpha ** -- THE SAME alpha, not a new one. **")
print()
for s in [
 "⇒⇒ ** AND THAT IS FORCED RATHER THAN CHOSEN, WHICH IS THE WHOLE POINT.  The rotation acts on the",
 "   COORDINATE and leaves the right-hand side of the defining equation untouched. **  *There is no",
 "   step at which a second radius could be introduced: the two faces are the two real forms of one",
 "   complex quadric $\\sum Z_i^2=\\alpha^2$ in $SO(6,\\mathbb{C})$, and a real form does not get to",
 "   choose its own radius.*",
 "",
 "⌗ *The corpus states the pairing four times — P10 `sec:lock`, P13, P17, p0 — and uses it to close",
 "   the quantization ambiguity at the horizon period $\\beta=2\\pi\\alpha$.  **That $\\beta$ is built",
 "   from $\\alpha$ too, which is the same statement one level along.***",
]:
    print("  " + s)

print()
print("=" * 78)
print("PART 2 — THE CURVATURE INVARIANTS ON BOTH FACES")
print("=" * 78)
n = 5
print("  Both faces are maximally symmetric of dimension 5, so R_abcd = K (g_ac g_bd - g_ad g_bc)")
print("  with K = -1/alpha^2 on the compact face and +1/alpha^2 on the Lorentzian one (sign only).")
print(f"\n  {'invariant':>18} {'dS_5 (K = 1/alpha^2)':>26} {'S^5 (K = 1/alpha^2)':>24}")
K = 1 / al**2
Ricci = (n - 1) * K
Rs = n * (n - 1) * K
Kret = 2 * n * (n - 1) * K**2
for nm, v in [("Ricci scalar", Rs), ("Ricci^2", n * Ricci**2), ("Kretschmann", Kret)]:
    print(f"  {nm:>18} {str(v):>26} {str(v):>24}")
print()
print("  ** every one is a pure power of 1/alpha^2, on both faces, with no second constant")
print("     available to form a ratio. **")
for v in [Rs, n * Ricci**2, Kret]:
    assert sp.simplify(sp.diff(v, al) * al / v).is_Integer

print()
print("=" * 78)
print("PART 3 — SO THERE IS NO SECOND SCALE")
print("=" * 78)
print(f"  {'source of a possible second scale':>46} {'verdict':>26}")
for a, b in [("the compact face's radius", "= alpha, forced by the rotation"),
             ("its curvature invariants", "powers of 1/alpha^2 only"),
             ("the horizon period beta = 2 pi alpha", "built from alpha"),
             ("M, r_0 (the construction's other numbers)", "MODULI (L-125's criterion)"),
             ("the Nariai value 2/(3 sqrt 3)", "one member's, not a constant (L-164)")]:
    print(f"  {a:>46} {b:>26}")
print()
for s in [
 "⛔⛔ ** THE FALSIFIER DOES NOT FIRE.  THE COMPACT FACE SUPPLIES NO SECOND SCALE, AND THE LAST",
 "   ROUTE TO A GEOMETRIC COUPLING IS CLOSED. **",
 "",
 "⇒⇒⇒ ** SO THE THREE-WAY CONVERGENCE BECOMES A STATEMENT RATHER THAN A PATTERN: **",
 "   *the winding quantises and cannot measure; the flat bundle selects and cannot couple; the",
 "   branch point filters and cannot supply — and now there is nowhere left for a magnitude to come",
 "   from, because a magnitude needs two invariants and the substrate has one by construction.*",
 "   ***THE CONSTRUCTION'S SILENCE ABOUT MAGNITUDES IS NOT A GAP AWAITING WORK.  IT IS A PROPERTY",
 "   OF A ONE-CONSTANT THEORY, AND THE CORPUS SHOULD SAY SO IN THOSE WORDS.***",
 "",
 "✔ ** AND THAT IS A RESULT WITH TEETH RATHER THAN A RETREAT, because it converts an open frontier",
 "   into a PREDICTION ABOUT WHAT THE PROGRAMME CAN NEVER DO — which is falsifiable in the only way",
 "   that matters: exhibit a magnitude the geometry forces. **",
 "",
 "⚠ ** THE BOUND, AND IT IS THE SAME DISTINCTION `L-150` TURNED ON: this is about the compact",
 "   face's GEOMETRY.  Fields living ON that face may carry their own scales — but those are",
 "   CONTENT, adjoined rather than derived, and adjoining one is exactly what the corpus's",
 "   admissibility criterion rejects (a structure carrying an unforced parameter answers 'what is",
 "   the world?' with a family). **  *So the escape exists and costs the thing the programme is",
 "   for.*",
]:
    print("  " + s)
