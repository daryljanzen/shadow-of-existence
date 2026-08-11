"""
P03_step3_refused.py -- the three questions an earlier pass recorded instead of working.

I. THE ANTIPODAL Z_2 vs THE OFFSET PARITY -- KILLED, on an exact computation.
   In the ambient M^6 the antipodal map has det +1 and REVERSES X_0; the offset parity
   diag(1,1,-1,1,1,1) has det -1 and FIXES X_0.  Separated by determinant and by their
   action on time, so they cannot be one Z_2 read at two levels.  The kill is informative:
   the antipodal map is exactly T composed with spatial inversion, so it sits on T's side
   of the corpus's own T/R line -- the quadric ledger's orientation argument for refusing
   the projective quotient is the TIME orientation, while the parity that grades chirality
   is the SPATIAL one.

II. FIGURE R3 ("1+2 -> uud") -- ** A KILL WAS WRITTEN AND IS RETRACTED (same session,
   Daryl).**  The retracted argument: the geometric 2+1 splits by SIGN (species) while
   uud splits by FLAVOUR, so the mapping is the wrong kind.  P14 refutes it in one
   sentence -- "the 2+1 of a designated root against the ellipse pair is the diagonal
   designation sigma and the sign 2+1 ... the reflection through the origin" -- so there
   are at least TWO 2+1s in this geometry and R3 names neither.  This computation
   addressed the sign one; the designation 2+1 is a flavour-side structure, and P14's
   same paragraph records that the locus DOES carry a flavour-breaking structure.
   ** R3 REMAINS OPEN, and wider: it must first say WHICH 2+1. **
   What is established and bounded: (a) R3's stated reason is WITHDRAWN -- the split is
   not a real-slice artefact, since sign(r) is species; (b) the sign 2+1 tracks D's
   parity exactly, so it is the mass-parity in another register; (c) the corpus carries
   two 2+1s and the catalogues had not distinguished them.  None licenses a verdict.

III. The category bake's two ZEROS -- adjudicated in prose in that ledger: they are
   verdicts about what the FIELD brought and they STAND; what grew is a row, from a source
   outside the field.

ORIGIN: computations/dimension_question/step3_refused_items.py -- built r2376 (c54.13);
edit the origin, not this copy."""



import numpy as np
import sympy as sp

r, M = sp.symbols('r M', real=True)
print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("I. THE ANTIPODAL Z_2 AND THE OFFSET PARITY — the same, or not?")
print("=" * 78)
print("  Ambient M^6 with signature (-,+,+,+,+,+); the substrate is -X0^2+|X|^2 = alpha^2.")
print("  Three candidate involutions the corpus names:")
print("    A  the ANTIPODAL map            X -> -X            (the projective quotient")
print("                                                        CR refuses)")
print("    R  the OFFSET PARITY            diag(1,1,-1,1,1,1) (FIGURE ⊢54's own matrix;")
print("                                                        r0 -> -r0, 2M -> -2M)")
print("    T  the HORN SWAP / time reflection  X0 -> -X0      (P3's timelike reflection)")
print()
eta = sp.diag(-1, 1, 1, 1, 1, 1)
A = -sp.eye(6)
R = sp.diag(1, 1, -1, 1, 1, 1)
T = sp.diag(-1, 1, 1, 1, 1, 1)

def report(name, Mx):
    isom = sp.simplify(Mx.T * eta * Mx - eta) == sp.zeros(6, 6)
    det = sp.det(Mx)
    orthochronous = Mx[0, 0] > 0
    return name, isom, det, bool(orthochronous), sp.trace(Mx)

print(f"{'':>4} {'an isometry?':>13} {'det':>5} {'orthochronous?':>15} {'trace':>6}")
for nm, Mx in (('A', A), ('R', R), ('T', T)):
    name, isom, det, orth, tr = report(nm, Mx)
    print(f"{name:>4} {str(isom):>13} {str(det):>5} {str(orth):>15} {str(tr):>6}")

print()
print("  ⇒ ALL THREE ARE ISOMETRIES, AND NO TWO ARE THE SAME:")
print("     • A has det +1 and REVERSES TIME  — in SO(5,1) but not in the identity")
print("       component; it is the one an orientation argument must refuse.")
print("     • R has det -1 and FIXES TIME     — it lies in O(5,1) \\ SO(5,1), which is")
print("       exactly the disconnected component P13's index obstruction cannot reach.")
print("     • T has det -1 and reverses time.")
print(f"     • And the composition: A = T . (spatial inversion)?  "
      f"{sp.simplify(A - T*sp.diag(1,-1,-1,-1,-1,-1)) == sp.zeros(6,6)}")
print()
print("  ⇒ ANSWER: NO. The antipodal Z_2 and the offset parity are DISTINCT involutions,")
print("     separated by determinant AND by their action on X0.  They cannot be one Z_2")
print("     read at two levels.  ** The candidate identification is KILLED, on an exact")
print("     computation rather than on taste. **")
print()
print("  AND THE KILL IS INFORMATIVE, which is why it was worth running.  The corpus")
print("  already separates T (timelike, horn-flipping) from R (spacelike, horn-preserving)")
print("  and calls their agreement on the fundamental triple a RESONANCE and not an")
print("  identity.  The antipodal map sits on T's side of that same line, not R's — so")
print("  QUADRIC §2c's orientation argument for refusing the quotient is the TIME")
print("  orientation, and the parity that grades chirality is the SPATIAL one.")
print("  ** Two orientation Z_2's, and the corpus's own T/R distinction already had the")
print("     shape of the answer.  Nothing new is asserted; a tempting weld is refused. **")

# =====================================================================
print()
print("=" * 78)
print("II. FIGURE R3 — the unsourced reason, DERIVED OR WITHDRAWN")
print("=" * 78)
print("  The reason on the page: 'a real-r artifact; off that slice all three sheets are")
print("  alike'.  Test it, then test the claim it was guarding.")
print()
print("  ⌗ STEP 1 — IS THE 1+2 SPLIT AN ARTIFACT OF THE REAL SLICE?")
print("  The split is by the SIGN of the root.  And the corpus makes sign(r) physical:")
print("  §0's matter-frames card — 'species = sign(r), local along the ruling'; each")
print("  ruling laps through r=0 and CHANGES SPECIES at the equator.")
print("  ⇒ the sign of a root is not a slice artifact; it is the matter/antimatter")
print("    species assignment.  ** THE STATED REASON IS WITHDRAWN. **")
print()
print("  ⌗ STEP 2 — WHAT THE SPLIT ACTUALLY IS, at general D.")
print(f"{'D':>3} {'horizon polynomial':>26} {'roots':>7} {'positive':>9} {'negative':>9} "
      f"{'split':>8}")
for D in range(4, 9):
    # r^(D-1) - r^(D-3) + 2M = 0, at a representative sub-critical mass
    coeffs = [0] * D
    coeffs[0] = 1.0
    coeffs[2] = -1.0
    # pick 2M safely below the critical value: 2M_c = 2*(r_N^(D-3) - r_N^(D-1))
    rN = float(sp.sqrt(sp.Rational(D - 3, D - 1)))
    twoMc = rN**(D - 3) - rN**(D - 1)
    coeffs[-1] = 0.35 * twoMc
    rts = np.roots(coeffs)
    real = np.sort(rts[np.abs(rts.imag) < 1e-9].real)
    pos = int((real > 0).sum()); neg = int((real < 0).sum())
    poly = f"r^{D-1} - r^{D-3} + 2M"
    print(f"{D:>3} {poly:>26} {len(real):>7} {pos:>9} {neg:>9} "
          f"{f'{pos}+{neg}':>8}")
print()
print("  ⇒ AND THE SPLIT TRACKS THE PARITY OF D EXACTLY: 2+1 at even D, 2+2 at odd D.")
print("     That is not a new fact.  It IS the mass-parity, seen in the root signs:")
print("     2M = r0^(D-3) - r0^(D-1) is odd in r0 iff D is even, and an odd polynomial's")
print("     real roots cannot be sign-symmetric about zero while a sign-even one's are.")
print("     ** So R3's 1+2 and the chirality parity are ONE fact in two registers, not")
print("        two — and at D=5, where there is no parity, there is no 1+2 either. **")
print()
print("  ⌗ STEP 3 — A KILL WAS WRITTEN HERE AND IS RETRACTED.  It was a straw man.")
print("  The retracted argument: the geometric 2+1 splits by SIGN (species) while uud")
print("  splits by FLAVOUR, so the mapping is the wrong kind and R3 dies.")
print()
print("  ** P14 refutes it in one sentence: 'the 2+1 of a designated root against the")
print("     ellipse pair is the diagonal designation sigma and the SIGN 2+1 ... the")
print("     reflection through the origin.'  THERE ARE AT LEAST TWO 2+1s IN THIS")
print("     GEOMETRY, AND R3 NAMES NEITHER. **")
print()
print("  This computation addressed the SIGN one.  The other candidate -- the")
print("  DESIGNATION 2+1, sigma's own -- is a flavour-side structure, and P14's same")
print("  paragraph records that the locus DOES carry a flavour-breaking structure:")
print("  'the slicing singles one root against the ellipse pair', supplied with the")
print("  triplet in P13.  So the kill closed an open search using a result about a")
print("  different object.")
print()
print("  ⇒ R3 REMAINS OPEN, and WIDER than before: it must first say WHICH 2+1.")
print()
print("  WHAT THIS COMPUTATION DOES ESTABLISH, and it is bounded:")
print("    (a) R3's stated reason is WITHDRAWN -- the split is not a real-slice")
print("        artefact, because sign(r) is species.  The row's blocker is gone.")
print("    (b) the SIGN 2+1 tracks the parity of D exactly, so it is the mass-parity")
print("        in another register rather than a second fact.")
print("    (c) the corpus carries TWO 2+1s and the catalogues had not distinguished")
print("        them.  That is a finding, and it widens the search.")
print("  ** None of the three licenses a verdict on R3. **")

# --- r2376+c54.159 -----------------------------------------------------------------
# Item I's KILL was only printed.  Pin the exact invariants that separate the three
# involutions: all are isometries of eta, dets are (+1, -1, -1) and traces (-6, 4, 4),
# and A = T composed with the spatial inversion.  Item II's root split was only printed
# too; pin the last row of its table (D=8: 3 real roots, 2 positive, 1 negative).
assert report('A', A)[1] and report('R', R)[1] and report('T', T)[1]   # all three isometries
assert (sp.det(A), sp.det(R), sp.det(T)) == (1, -1, -1)
assert (sp.trace(A), sp.trace(R), sp.trace(T)) == (-6, 4, 4)
assert report('A', A)[3] is False and report('R', R)[3] is True        # A reverses X0, R fixes it
assert A != R and A != T and R != T                                    # KILL: no two are one Z_2
assert sp.simplify(A - T*sp.diag(1, -1, -1, -1, -1, -1)) == sp.zeros(6, 6)
assert (len(real), pos, neg) == (3, 2, 1)      # D=8, the table's last row: a 2+1 at even D
