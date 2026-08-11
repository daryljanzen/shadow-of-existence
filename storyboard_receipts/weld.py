"""
weld.py -- the r1073 weld, verified at source.  (r1088)

Daryl's physical input, r1073: "You flip an electron's charge and you get a positron.
Of course the two are wedded problems. Species and charge are the same thing, are they not?"

WHAT NEEDED CHECKING rather than taking: the weld's load-bearing claim is that
'charge is the R-even datum' is TRUE OF THE METRIC and FALSE OF THE POTENTIAL.
The existing receipt (charge_geometry.py) tests A_t under Q->-Q. It does NOT test
A_t under R. That is a different question, and it is the one the weld turns on.

TWO LOGGED NEGATIVES, kept per THE_CODA s"The negatives are the map" -- a face that
is NOT operative is as load-bearing as one that is:

[N1] MY OWN ERROR, r1088. First attempt implemented R as the SIMULTANEOUS
     substitution {r -> -r, M -> -M}, reading the glossary's "acts as r0 -> -r0
     (2M -> -2M) ... and IS the single reflection r -> -r" as two substitutions to
     apply together. It returned the mass term EVEN, contradicting the corpus's
     eigenspace split. THE CORPUS WAS RIGHT; I double-counted the flip.
     WHAT THE FAILURE TELLS US: (i) "one Z2, FOUR FACES" is not loose talk -- it is
     precisely the claim that these ARE one map, and part (A) below is its proof;
     (ii) the glossary's phrasing INVITES the misread by listing the mass flip as a
     separate action rather than as the same action re-read -- logged for a wording
     pass, not fixed here; (iii) it is the sixth face (the convention trap) in a new
     dress: the programme's own vocabulary read as if the words meant the usual thing.

[N3] SECOND ERROR OF MINE, r1088, same run. I read F_tr's parity off the naive
     substitution F_tr(r) -> F_tr(-r) and got EVEN -- which cannot be right if A is
     odd. F is a 2-FORM, F = F_tr dt^dr: under r -> -r the basis dr flips too, so
     (phi*F)_tr = F_tr(-r) x (dr'/dr) = -F_tr(-r), and F is ODD, consistent with A.
     A_t's naive substitution IS valid, because A = A_t dt and dt carries no r.
     WHAT THE FAILURE TELLS US: a parity read off a COMPONENT without its basis is
     not a parity at all. Two of the three quantities here are safe by accident (A_t,
     because dt is inert; F.F, because it is quadratic and the sign squares away) --
     which is exactly how the error survives a spot-check. Kept, because the next
     instance will reach for the same shortcut.

[N2] THE WELD'S OWN PHRASING IS LOOSE, and the fix is a sharpening, not a retreat.
     The ledger says "under R, the METRIC is invariant but the potential is ODD."
     f(r) is NOT invariant under R -- its mass term flips (part B: f is NEITHER even
     nor odd; that non-parity IS the eigenspace split). What is R-even is the metric's
     CHARGE TERM Q^2/r^2. The weld's finding is untouched; only its wording needed
     tightening, and the tightened form is what gets baked.
"""
import sympy as sp

r, Q, M, alpha = sp.symbols('r Q M alpha', real=True)

f  = 1 - 2*M/r + Q**2/r**2 - r**2/alpha**2     # RN-de Sitter slicing function
At = Q/r                                        # Maxwell potential, A = A_t dt


def R(expr):
    """R, the mass reflection: the SINGLE reflection r -> -r. 2M -> -2M is the same
       map re-read (part A), never a second substitution. See [N1]."""
    return sp.simplify(expr.subs(r, -r))


def parity(name, expr):
    im = R(expr)
    if sp.simplify(im - expr) == 0:   v = "EVEN  (fixed)"
    elif sp.simplify(im + expr) == 0: v = "ODD   (flips)"
    else:                             v = "NEITHER (it SPLITS)"
    print(f"  {name:34s} --R-->  {str(im):38s} {v}")
    return v


print("="*80)
print("(A)  Is 'r -> -r at fixed M' the same map as '2M -> -2M at fixed r'?")
print("="*80)
lhs, rhs = sp.simplify(f.subs(r, -r)), sp.simplify(f.subs(M, -M))
print(f"  f_M(-r)  = {lhs}")
print(f"  f_-M(+r) = {rhs}")
print(f"  IDENTICAL?  {sp.simplify(lhs - rhs) == 0}")
print()
print("  => ONE MAP, TWO READINGS. The r<0 branch of the M-bead IS the r>0 branch of")
print("     the (-M)-bead. This is the PROOF of the corpus's 'one Z2, four faces',")
print("     and the reason R must be applied as a single substitution r -> -r. [N1]")

print()
print("="*80)
print("(B)  What R does, term by term")
print("="*80)
parity("mass term        -2M/r", -2*M/r)
v_Q  = parity("charge term      +Q^2/r^2", Q**2/r**2)
parity("de Sitter term   -r^2/alpha^2", -r**2/alpha**2)
v_f  = parity("the metric f(r), whole", f)
v_At = parity("THE POTENTIAL    A_t = Q/r", At)
# F is a 2-FORM, F = F_tr dt^dr, so its parity is NOT the naive substitution:
# under r -> -r the basis dr flips too. [N3] -- see the header.
F_tr = sp.diff(At, r)                       # = -Q/r^2
F_pullback = sp.simplify(F_tr.subs(r, -r) * (-1))   # (phi*F)_tr = F_tr(-r) * (dr'/dr)
print(f"  {'field strength   F = F_tr dt^dr':34s} --R-->  {str(F_pullback):38s} "
      f"{'ODD   (flips)' if sp.simplify(F_pullback + F_tr) == 0 else 'CHECK'}")
print(f"     (as a FORM: (phi*F)_tr = F_tr(-r) x (dr'/dr) = {F_tr.subs(r,-r)} x (-1) = {F_pullback};")
print(f"      the naive component substitution alone would wrongly return EVEN. [N3])")
FF = sp.simplify(F_tr**2)                    # F.F ~ g^tt g^rr F_tr^2, even in the flip
print(f"  {'field invariant  F.F ~ F_tr^2':34s} --R-->  {str(sp.simplify(FF.subs(r,-r))):38s} "
      f"{'EVEN  (fixed)' if sp.simplify(FF.subs(r,-r) - FF) == 0 else 'CHECK'}")
print(f"     (F odd => F.F even: quadratic in F. The INVARIANT is blind to the flip.)")
print()
print("  mass ODD, charge EVEN: the corpus's eigenspace split, reproduced.")
print("  f whole is NEITHER -- and that non-parity IS the split (P5 rem:P-dS-Schw:")
print("  f = (1 - r^2/a^2)[R-even: the invariant dS geometry] + (-2M/r)[R-odd: the")
print("  perspectival Schwarzschild mass]). See [N2]: 'the metric is invariant' is")
print("  loose; the CHARGE TERM is what is R-even.")

print()
print("="*80)
print("(C)  THE WELD'S CLAIM, stated precisely")
print("="*80)
print(f"  metric's CHARGE TERM Q^2/r^2 under R : {v_Q}")
print(f"  potential A_t = Q/r under R          : {v_At}")
print()
print("  A_t = Q/r  and  r -> -r  gives  Q/(-r) = -Q/r.  ONE LINE.")
print("  So A = A_t dt is ODD under R, hence F = dA is ODD, hence the ELECTROMAGNETIC")
print("  FIELD FLIPS SIGN under R: R flips the charge AS SEEN. The metric cannot see")
print("  it, because it carries the charge only as Q^2.")
print()
print("  >> 'CHARGE IS THE R-EVEN DATUM' IS TRUE OF THE METRIC'S CHARGE TERM AND")
print("     FALSE OF THE POTENTIAL. R does not fail to touch the charge. The corpus's")
print("     stated reason is METRIC-ONLY -- and the metric is precisely the blind thing.")
print()
print("  A THIRD RIGGED TEST, logged before anyone runs it: the field INVARIANT")
print("  F.F ~ Q^2/r^4 is EVEN, so a discriminator built on the invariant is blind to")
print("  the flip too. Only the POTENTIAL / field strength sees it. (Companion to the")
print("  root test, which is rigged because Q enters solely as Q^2.)")

print()
print("="*80)
print("(D)  The weld: R and C agree on every label")
print("="*80)
print("  R preserves the PHYSICAL mass |2M| and flips only its SIGN:")
for m in (0.1, 0.3849, 2.0):
    print(f"     |2M| = {m:<7.4f}  --R-->  |{-m:+.4f}| = {abs(-m):.4f}   PRESERVED")
print()
print("  So [1]'s 'R is mass-ODD, C is mass-EVEN, therefore C != R' COMPARED A LABEL")
print("  TO A MASS. The sign of 2M is the relational branch label -- which side of r=0")
print("  you are on -- not a mass. C preserves an electron's mass and flips its charge;")
print("  R preserves |2M| and flips its sign. Both preserve the magnitude.")
print()
print(f"     {'':26s} {'R':>12s} {'C':>12s}")
for a, b, c in [("species  (3 <-> 3bar)", "flips", "flips"),
                ("charge   (via A_t)", "flips", "flips"),
                ("physical mass |2M|", "preserved", "preserved"),
                ("character", "LINEAR", "ANTILINEAR")]:
    tail = "   <-- the ONLY difference" if a == "character" else ""
    print(f"     {a:26s} {b:>12s} {c:>12s}{tail}")
print()
print("  => R and C agree on EVERY LABEL and differ ONLY IN CHARACTER. So")
print("     rem:C-not-R's conclusion SURVIVES -- via LINEARITY, always its real")
print("     argument -- but 'C is not R' is true while CONCEALING that R is part of C.")
print()
print("  CONVENTION, held (the sixth face): the corpus's 'C is antilinear' means the")
print("  CLASSICAL FIELD MAP psi^c = C gamma^0T psi*, its own stated usage. The QFT")
print("  OPERATOR convention -- C unitary and linear, T antiunitary -- is a DIFFERENT")
print("  convention; importing it would manufacture a dissonance that is not there.")
print("  Do not 'correct' the corpus into it.")

print()
print("="*80)
print("(E)  Scope -- what this does NOT establish")
print("="*80)
print("  NOT established: C = (linear face R) o (antilinear face tau~ <-> conj(tau~)).")
print("  That factorization is the DIRECTION the weld opens, not a result. Both faces")
print("  are geometric; whether their composite IS C is exactly the open [6], and it is")
print("  unanswerable on either real slice.   -> A3.   Held do-not-assert.")
