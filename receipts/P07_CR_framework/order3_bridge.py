"""
order3_bridge.py -- what identifies, and what does not, the two order-three structures on the
cosmogenetic bead: the groupoid's Z/3 (on the horizon cubic r^3-r+2M=0, from f=0) and the bead's
Z/3 (on the comoving cubic r^3+2M=0, from 1-f=0).

ESTABLISHED HERE (each computed below):
  * the cosmic-time law satisfies (dr/dtau~)^2 = 1-f, so cosmic time turns where 1-f=0 while the
    slicing turns where f=0 -- two different turning conditions                        [stage 4a]
  * horizon roots are three colinear real points (casus irreducibilis, sub-Nariai); comoving roots
    are an equilateral triangle                                                        [stage 4c]
  * therefore NO AFFINE map r -> a r + b carries one root configuration to the other: affine maps
    preserve colinearity. There is no identification of the two ROOT SETS by change of variable
    in r, at fixed cubic                                                               [stage 4d]
  * the two Z/3's cover different bases (mass line vs cosmic-time line), branch at different loci
    (Nariai vs the seam r=0), and degenerate oppositely at Nariai                       [stages 2-3]
  * even granted, an order-three iso would label bead sheets by horizon-root index, not by
    congruence, so it is not sufficient for the sheet-assignment                        [stage 4f]

THE SCOPE OF THAT NEGATIVE, STATED EXACTLY (stage 5, and the reason this file was rewritten r1430):
  The obstruction above is to an identification AT FIXED CUBIC, by an affine map of r. It is not a
  statement that the two cubics are unrelated, and it cannot be -- an affine test is structurally
  blind to a relation that DEFORMS one cubic into the other. Such a relation exists and is
  geometric. Radial geodesics obey (dr/dtau)^2 = E^2 - f and turn on

        r^3 + (E^2 - 1) a^2 r + 2 M a^2 = 0,

  one family indexed by the conserved energy, whose two ends ARE these two cubics:
        E = 1  (marginally bound, k = 0, the flat leaf) -> r^3 + 2M a^2       : the COMOVING cubic
        E = 0  (k = +1, maximally bound)                -> r^3 - a^2 r + 2M a^2 : the HORIZON cubic
  so the separating term is the coefficient E^2 - 1 = -k, the Friedmann curvature constant. The
  corpus already carries this family (slicing_operator.tex sec.306, eq:Ek, "the three slicings are
  one congruence at three energies"); it had simply never been connected to these two cubics. The
  two root configurations differ because the family crosses its own discriminant between the ends,
        Delta(E) = 4 a^4 ( a^2 (1-E^2)^3 - 27 M^2 ) = 0   at   1 - E^2 = 3 (M/a)^{2/3},
  and at the Nariai mass that crossing arrives exactly at E = 0, which is the same statement as the
  horizon cubic's double root there. The affine obstruction is that crossing seen from its two ends.

WHAT REMAINS OPEN (not claimed, unchanged): whether the A_2 structure the E=0 end carries survives
  the crossing to the E=1 end -- i.e. whether the two root sets are identified in any nontrivial
  sense. The family makes that question exact; it does not answer it. Nothing here bears on the
  separate, walled question of a realised colour isometry (su(3) not in so(5,1)).

[P7 CR_framework -- lem:twoturnings and rem:tworealisations]
STATUS: verified. The affine obstruction is exact; the energy family and its discriminant crossing
  are exact; the identification of root sets is not claimed and is NOT decided by this file.
HISTORY: r986 as an investigation whose docstring and VERDICT stated the negative far more broadly
  than the computation supports ("THE BRIDGE DOES NOT CLOSE", "verified NEGATIVE structural result").
  That phrasing cost real work: at r1428 a node read the header, took it as a general negative, and
  retracted sound results without tracing the reasoning. The over-broad statements are REMOVED, not
  annotated -- a receipt that carries a false verdict is not made safe by a warning above it
  (AVENUE_11 sec.1: resolve or elevate, never flag-and-leave; avenue 1: removal, not softening).
  The computations below are unchanged and correct; stage 5 supplies what the original lacked.
RUN: python3 order3_bridge.py   RUNTIME: ~6s
ORIGIN: computations/order3_bridge.py; verified r1356; scope corrected and stage 5 added r1430.
ORIGIN-DIVERGENCE: origin is the r986 investigation whose VERDICT stated the negative far more broadly; this copy is the rescoped version and says so in its HISTORY line. Adjudicated r2376 (c54.3): THIS COPY AUTHORITATIVE, origin kept as record of the broader negative.
"""
import sympy as sp

r, M, w, u, tau, k = sp.symbols('r M w u tau k', complex=True)
Mr = sp.symbols('M', real=True, positive=True)
print("="*78)
print("STAGE 1 -- the two cubics and their order-three actions")
print("="*78)

# ---- (1a) the HORIZON cubic  f=0  ->  r^3 - r + 2M = 0 --------------------------
Ch = r**3 - r + 2*M
print("\n[1a] horizon cubic  C_h(r) = r^3 - r + 2M   (from f = 1 - 2M/r - r^2 = 0)")
# trig parameterisation claimed in the groupoid paper: r0 = (2/sqrt3) sin w, 2M = (2/(3 sqrt3)) sin 3w
r_w = (2/sp.sqrt(3))*sp.sin(w)
twoM_w = (sp.Rational(2,3)/sp.sqrt(3))*sp.sin(3*w)
check = sp.simplify(Ch.subs({r:r_w, M:twoM_w/2}))
print("    substitute r=(2/sqrt3) sin w, 2M=(2/(3sqrt3)) sin 3w into C_h  ->", check,
      " (0 confirms the parameterisation)")
# the three roots are w, w+2pi/3, w+4pi/3 (same 2M, since sin 3w is 2pi/3-periodic)
print("    three roots: r_k = (2/sqrt3) sin(w + 2 pi k/3), k=0,1,2  (all share the same 2M)")
roots_w = [sp.simplify((2/sp.sqrt(3))*sp.sin(w + 2*sp.pi*kk/3)) for kk in range(3)]
sum_roots = sp.simplify(sum(roots_w))
prod_pairs = sp.simplify(roots_w[0]*roots_w[1]+roots_w[1]*roots_w[2]+roots_w[2]*roots_w[0])
prod_roots = sp.simplify(roots_w[0]*roots_w[1]*roots_w[2])
print("    Vieta check: sum r_k =", sum_roots, " (want 0);  sum r_i r_j =", prod_pairs,
      " (want -1);  prod r_k =", sp.simplify(prod_roots - (-twoM_w)), "+ (-2M)  (want 0)")
print("    => groupoid Z/3 is  w -> w + 2pi/3 : a 3-CYCLE of the three horizon roots.")

# ---- (1b) the BEAD cubic (sheets at fixed cosmic time) -------------------------
# r = A sinh^{2/3}(3 tau~/2)  =>  r^3 = A^3 sinh^2(3 tau~/2).  Let s = A^3 sinh^2(...).
# At fixed cosmic time the three sheets are the cube roots r_k = s^{1/3} e^{2pi i k/3}.
print("\n[1b] bead law  r = A sinh^{2/3}(3 tau~/2),  A^3 = 2M   =>   r^3 = 2M sinh^2(3 tau~/2)")
print("    bead cubic in r (fixed tau~):  C_b(r) = r^3 - 2M sinh^2(3 tau~/2)   -- PURE cube (no linear term)")
print("    three sheets: r_k = (2M sinh^2)^{1/3} e^{2 pi i k/3}, k=0,1,2")
print("    => bead Z/3 is  r -> e^{2pi i/3} r : rotation by a cube root of unity.")
# verify the e^{2pi i/3} arises from tau~ -> tau~ + i 2pi/3  (u = 3tau~/2 -> u + i pi)
uu = sp.symbols('uu', complex=True)
ratio = sp.simplify(sp.sinh(uu + sp.I*sp.pi)/sp.sinh(uu))   # sinh(u+i pi) = -sinh u
print("    sinh(u+i*pi)/sinh(u) =", ratio, " so [sinh]^{2/3} picks up (-1)^{2/3} =",
      sp.simplify(sp.exp(sp.Rational(2,3)*sp.I*sp.pi)), "= e^{2pi i/3}. Confirmed.")

print("\n[1c] SHAPE COMPARISON of the two cubics-in-r:")
print("    horizon:  r^3 - r + 2M         (depressed, p = -1  != 0)")
print("    bead:     r^3 - 2M sinh^2(.)   (pure cube, p = 0)")
print("    Different depressed-cubic shape.  A Z/3 exists on BOTH, but they are the")
print("    Galois/cube-root Z/3 of DIFFERENT cubics.  Whether a canonical map identifies")
print("    them is Stages 2-3.")

print("\n"+"="*78)
print("STAGE 2 -- branch loci and monodromy of the two covers")
print("="*78)

# ---- (2a) horizon cover over the M-plane --------------------------------------
disc_h = sp.discriminant(Ch, r)
print("\n[2a] horizon cubic as a 3-sheeted cover of the M-plane:")
print("    discriminant_r(r^3 - r + 2M) =", sp.simplify(disc_h))
sols = sp.solve(sp.Eq(disc_h, 0), M)
print("    branch points (disc=0) at M =", sols, " i.e. M = +-1/(3 sqrt3) = +- Nariai mass")
print("    => the groupoid cover branches at the NARIAI points; monodromy there is the")
print("       transposition sigma (two roots collide).  Base space = the M (mass / sky-angle) line.")

# ---- (2b) bead cover over the cosmic-time (u) plane, fixed Nariai M ------------
print("\n[2b] bead cover r^3 = 2M sinh^2(u),  u = 3 tau~/2,  at FIXED M = Nariai:")
print("    as a cover of the u-plane, r = (2M)^{1/3} sinh^{2/3}(u) branches where sinh(u)=0")
print("    => u = i pi n  (n in Z);  the n=0 branch point is u=0 i.e. r=0, THE SEAM.")
print("    Base space = the cosmic-time (u) line, at the single mass M = Nariai.")

print("\n[2c] the mismatch, stated plainly:")
print("    - groupoid Z/3: cover of the MASS line, branched at NARIAI (M=+-1/(3sqrt3)).")
print("    - bead Z/3:     cover of the TIME line at fixed Nariai mass, branched at the SEAM r=0.")
print("    Different base spaces; different branch loci.  The bead lives OVER a single point")
print("    (Nariai) of the groupoid's base.")

print("\n"+"="*78)
print("STAGE 3 -- what each order-three does AT the Nariai point")
print("="*78)
MN = sp.Rational(1,3)/sp.sqrt(3)     # Nariai mass, 1/(3 sqrt3)
print("\n[3a] Nariai mass M_N = 1/(3 sqrt3) =", sp.nsimplify(MN), "~", float(MN))
Ch_N = (r**3 - r + 2*MN)
roots_N = sp.solve(Ch_N, r)
print("    horizon cubic at Nariai:  r^3 - r + 2/(3sqrt3) = 0")
print("    roots:", [sp.simplify(x) for x in roots_N], " (numerically", [complex(sp.N(x)) for x in roots_N],")")
print("    => a DOUBLE root at +1/sqrt3 and a single root at -2/sqrt3: the groupoid Z/3 has")
print("       DEGENERATED here (two of the three roots have collided). sigma's fixed point.")
print("\n[3b] the bead at Nariai is where its clean 3 sheets LIVE (r -> e^{2pi i/3} r, all distinct).")
print("    So at the very point where the groupoid Z/3 degenerates, the bead Z/3 is nondegenerate.")
print("\n[3c] where does r=0 (the bead branch point / seam) sit in the groupoid?")
print("    horizon cubic at r=0:  0 - 0 + 2M = 2M != 0, so r=0 is NOT a horizon root.")
print("    In the groupoid, r=0 is the fixed locus of the mass-reflection R (2M -> -2M),")
print("    a Z/2 (NOT the Z/3).  So the bead's Z/3-branch = the groupoid's Z/2-fixed point.")

print("\n"+"="*78)
print("PRELIMINARY READING (to be pressure-tested in stage 4, not a conclusion):")
print("  Both are 'the cube-root Z/3', but they are the cube-root Z/3 of different cubics,")
print("  over different base spaces, branched at different loci, and they behave OPPOSITELY")
print("  at Nariai (groupoid degenerates; bead is clean). A canonical identification is NOT")
print("  automatic. Stage 4 searches for a genuine bridge map before drawing any verdict.")
print("="*78)

print("\n"+"="*78)
print("STAGE 4 -- which cubic does each order-three actually belong to?")
print("="*78)

import sympy as sp
rr, Msym, tt = sp.symbols('rr M tt', positive=True)
A = (2*Msym)**sp.Rational(1,3)
r_of = A*sp.sinh(sp.Rational(3,2)*tt)**sp.Rational(2,3)          # bead law, alpha=1
drdt = sp.diff(r_of, tt)
f_expr = 1 - 2*Msym/rr - rr**2
one_minus_f = sp.simplify((1 - f_expr).subs(rr, r_of))
lhs = sp.simplify(drdt**2 - one_minus_f)
print("\n[4a] what ODE does the cosmic-time law r=A sinh^{2/3}(3tau~/2) satisfy?")
print("    (dr/dtau~)^2 - (1 - f)|_(r=bead)  simplifies to:", sp.simplify(lhs), " (0 => (dr/dtau~)^2 = 1 - f)")
print("    => COSMIC TIME turns where 1 - f = 0;  the SLICING curve (dr/dl)^2=|f| turns where f = 0.")
print("       Two DIFFERENT turning conditions (the corpus's own scope note, CR_framework:750).")

print("\n[4b] the two turning cubics (clear denominators, alpha=1):")
print("    slicing / HORIZON  (f=0):        r^3 - r + 2M = 0     <- groupoid Z/3 lives here")
print("    cosmic-time / COMOVING (1-f=0):  r^3 + 2M     = 0     <- bead Z/3 lives here")

# root CONFIGURATIONS in the complex r-plane
Msub = sp.Rational(3,20)      # 0.15, sub-Nariai (Nariai = 0.19245)
for label, cub in [("HORIZON r^3-r+2M", rr**3-rr+2*Msym), ("COMOVING r^3+2M", rr**3+2*Msym)]:
    rts = sp.nroots(cub.subs(Msym, Msub))
    pts = [complex(x) for x in rts]
    print(f"\n    [{label}] at M=0.15 -> roots:")
    for p in pts: print(f"        {p.real:+.4f} {p.imag:+.4f}i   |arg|={abs(sp.arg(sp.N(p)))*180/sp.pi.evalf():.1f} deg" if abs(p)>1e-9 else f"        {p.real:+.4f} {p.imag:+.4f}i  (origin)")
    imags = [abs(p.imag) for p in pts]
    print(f"        max|Im| = {max(imags):.4f}  ->", "ALL REAL (colinear on real axis)" if max(imags)<1e-9 else "has complex roots")

print("\n[4c] the geometric distinction in the complex r-plane:")
print("    HORIZON roots (sub-Nariai): three REAL, COLINEAR points on the real axis.")
print("    COMOVING roots: an EQUILATERAL TRIANGLE (one real + conjugate pair at +-120 deg).")
print("    The groupoid Z/3 3-cycles three colinear real roots (casus irreducibilis);")
print("    the bead Z/3 rotates an equilateral triangle by e^{2pi i/3}. Different realisations.")

print("\n[4d] are the two cubics affinely/Moebius equivalent (could a change of variable identify them)?")
# a pure cube r^3 = c has equianharmonic roots (equilateral); r^3 - r + 2M does not for generic M.
print("    r^3 + 2M has equianharmonic (equilateral) roots for every M != 0.")
print("    r^3 - r + 2M has equilateral roots ONLY if its linear term vanishes, i.e. never (p=-1).")
print("    An affine map r->a r+b preserves the roots' shape (ratios); it cannot turn colinear-real")
print("    into equilateral. => the two cubics are NOT affinely equivalent. No canonical iso by")
print("    change of variable.")

print("\n[4e] the only sense in which they are trivially 'the same order-three':")
print("    S_3 contains a UNIQUE order-3 subgroup (the alternating A_3). So each cubic's Galois")
print("    Z/3 is 'the' Z/3 abstractly -- as is every Z/3. Identifying the TWO S_3's (hence the two")
print("    Z/3's) requires identifying the two ROOT SETS, which is the A_2 resemblance the corpus")
print("    holds not claimed. Stage 4d rules out doing so by an affine map at fixed cubic; it does")
print("    NOT rule out a relation that deforms one cubic into the other. Stage 5 exhibits one.")

print("\n[4f] does an order-three bridge -- even if granted -- close the SHEET-ASSIGNMENT question?")
print("    No. A groupoid<->bead Z/3 iso would label bead sheets by HORIZON-ROOT index, not by")
print("    congruence (A / B / photon). The congruence labels come from the ruling geometry")
print("    (slicing_operator), an independent structure. So the order-three bridge is neither")
print("    established NOR sufficient for the sheet-assignment.")

print("\n"+"="*78)
print("VERDICT (scoped exactly):")
print("  ESTABLISHED: the two order-threes are the Z/3's of two different turning cubics -- horizon")
print("  f=0 (r^3-r+2M, three colinear real roots) vs comoving 1-f=0 (r^3+2M, equilateral). They")
print("  cover different bases, branch at different loci (Nariai vs seam), degenerate oppositely at")
print("  Nariai, and NO AFFINE map of r identifies their root sets. 'Same order-three' is true only")
print("  in the trivial sense that S_3 has a unique Z/3.")
print("  NOT ESTABLISHED, and not decidable by the above: that the two cubics are unrelated. The")
print("  affine test acts at FIXED cubic and is blind to a deformation between them; stage 5 exhibits")
print("  the deformation -- they are the E=1 and E=0 ends of one energy family of turning points,")
print("  separated by a discriminant crossing that lands exactly at E=0 for the Nariai mass.")
print("  OPEN (not claimed): whether the A_2 structure at the E=0 end survives that crossing, i.e.")
print("  whether the two root sets are identified in any nontrivial sense. Not answered here.")
print("="*78)

# -- APPENDED ASSERT-VERIFICATION (r1356, Arthur): lock the discriminating basis of the negative verdict --
import numpy as _np
# [1a] the trig parameterisation solves the HORIZON cubic
assert sp.simplify((r**3 - r + 2*M).subs({r:(2/sp.sqrt(3))*sp.sin(w), M:((sp.Rational(2,3)/sp.sqrt(3))*sp.sin(3*w))/2}))==0, "param solves horizon cubic"
# [1b] the bead's e^{2pi i/3} arises from tau~ -> tau~ + i 2pi/3  (sinh(u+i pi) = -sinh u)
_u=sp.Symbol('u_chk', complex=True)
assert sp.simplify(sp.sinh(_u+sp.I*sp.pi)/sp.sinh(_u)) == -1, "sinh(u+i pi) = -sinh u"
assert abs(complex(sp.exp(sp.Rational(2,3)*sp.I*sp.pi)) - complex(-0.5, 3**0.5/2)) < 1e-12, "(-1)^(2/3)=e^(2pi i/3)"
# [4a] the bead law satisfies (dr/dtau~)^2 = 1 - f  (cosmic time turns at 1-f=0, NOT f=0)
assert sp.simplify(lhs)==0, "bead law satisfies (dr/dtau~)^2 = 1-f"
# [4c/4d] SHAPE: horizon roots colinear-real; comoving roots equilateral -> NOT affinely equivalent
_Msub=sp.Rational(3,20)
_h=[complex(x) for x in sp.nroots((rr**3-rr+2*Msym).subs(Msym,_Msub))]
_c=[complex(x) for x in sp.nroots((rr**3+2*Msym).subs(Msym,_Msub))]
assert max(abs(x.imag) for x in _h) < 1e-9,  "horizon roots all REAL (colinear)"
assert max(abs(x.imag) for x in _c) > 0.1,   "comoving roots have a complex pair"
# comoving = equilateral: equal radii from centroid 0 (cube roots of -2M); horizon = NOT equilateral
assert max(abs(x) for x in _c)-min(abs(x) for x in _c) < 1e-9, "comoving roots EQUILATERAL (equal |r|)"
_hc=sum(_h)/3; assert max(abs(x-_hc) for x in _h)-min(abs(x-_hc) for x in _h) > 0.1, "horizon roots NOT equilateral"
print("\n>> AVENUE 11 ASSERTS PASSED: bead law obeys (dr/dtau~)^2=1-f; groupoid Z/3 on r^3-r+2M (colinear real)")
print("   vs bead Z/3 on r^3+2M (equilateral) -- different cubics, NOT AFFINELY EQUIVALENT, so no change of")
print("   variable in r identifies their root sets. That is the whole of the negative; see stage 5 for the")
print("   energy family that does relate the two cubics, and which the affine test cannot see.")

# =============================================================================================
# STAGE 5 -- the relation the affine test is structurally blind to, and a control that breaks
# =============================================================================================
print("\n"+"="*78)
print("STAGE 5 -- the two cubics are the E=1 and E=0 ends of ONE family of turning points")
print("="*78)
_r,_E,_M = sp.symbols('r E M', positive=True)
_f = 1 - 2*_M/_r - _r**2                                   # alpha = 1
_turn = sp.expand(sp.numer(sp.together(_E**2 - _f)))       # radial geodesics turn where E^2 = f
print("\n[5a] (dr/dtau)^2 = E^2 - f  =>  turning locus:", _turn, "= 0")
assert sp.expand(_turn - (_r**3 + (_E**2-1)*_r + 2*_M)) == 0, "turning locus is not the E-family"
assert sp.expand(_turn.subs(_E,1) - (_r**3 + 2*_M)) == 0,     "E=1 end is not the comoving cubic"
assert sp.expand(_turn.subs(_E,0) - (_r**3 - _r + 2*_M)) == 0,"E=0 end is not the horizon cubic"
print("     E=1 (marginally bound, k=0, flat leaf) ->", sp.expand(_turn.subs(_E,1)), " = the COMOVING cubic")
print("     E=0 (k=+1, maximally bound)            ->", sp.expand(_turn.subs(_E,0)), " = the HORIZON cubic")
print("     so the separating term is the coefficient E^2-1 = -k, the Friedmann curvature constant")
print("     (slicing_operator.tex sec.306 eq:Ek already carries the family: -k = E^2 - 1).")

_D = sp.factor(sp.discriminant(_r**3 + (_E**2-1)*_r + 2*_M, _r))
assert sp.simplify(_D - 4*((1-_E**2)**3 - 27*_M**2)) == 0, "discriminant of the E-family"
print("\n[5b] Delta(E) = 4( (1-E^2)^3 - 27 M^2 )  ->  zero at  1-E^2 = 3 M^{2/3}")
import numpy as _np
_MN = 1/(3*_np.sqrt(3))
for _Mv in (0.02, 0.08, 0.15, _MN):
    _lam = 3*_Mv**(2/3)
    print(f"     M={_Mv:.5f} -> crossing at 1-E^2={_lam:.4f}  (E*={_np.sqrt(max(0,1-_lam)):.4f})")
    assert 0 < _lam <= 1 + 1e-12, "crossing outside the family"
assert abs(3*_MN**(2/3) - 1.0) < 1e-12, "at Nariai the crossing must arrive exactly at E=0"
print("     at Nariai the crossing arrives exactly at E=0 -- the same statement as the horizon")
print("     cubic's double root there. So the affine obstruction IS this crossing, seen from its ends.")

print("\n[5c] DISCRIMINATING CONTROL -- the claim must be able to fail:")
# the family must actually change the root configuration across the crossing, and must NOT
# do so for a family that never crosses (control: take M above the crossing for all E in [0,1])
def _shape(Ev, Mv):
    _rt = _np.roots([1, 0, Ev**2 - 1, 2*Mv])
    if _np.ptp(_np.abs(_rt)) < 1e-9:            return 'equilateral'
    if _np.abs(_rt.imag).max() < 1e-9:          return 'colinear-real'
    return 'intermediate'
_seen = {_shape(Ev, 0.15) for Ev in (1.0, 0.7, 0.0)}
print("     M=0.15 across E=1,0.7,0:", _shape(1.0,0.15), "->", _shape(0.7,0.15), "->", _shape(0.0,0.15))
assert _seen == {'equilateral','intermediate','colinear-real'}, "family must change shape across the crossing"
# control: a cubic family with NO discriminant crossing keeps one shape -- here, M so large that
# 3 M^{2/3} > 1, so Delta < 0 for every E in [0,1] and no colinear-real end exists
_Mbig = 0.5
_ctrl = {_shape(Ev, _Mbig) for Ev in (1.0, 0.7, 0.0)}
print(f"     CONTROL M={_Mbig} (3M^2/3 = {3*_Mbig**(2/3):.3f} > 1, no crossing):", sorted(_ctrl))
assert 'colinear-real' not in _ctrl, "control failed: a non-crossing family must not reach colinear-real"
print("     control holds: without a crossing the colinear-real configuration is never reached, so the")
print("     shape change at M=0.15 is the crossing and not an artefact of the parameterisation.")

print("\n>> STAGE 5 PASSED. The negative of stages 1-4 is exact and is a statement about AFFINE maps")
print("   at fixed cubic. The two cubics ARE related, as two energies of one congruence.")

# =============================================================================================
# STAGE 6 -- does the A_2 structure survive along the family?  ANSWERED, via the deck group.
# =============================================================================================
print("\n"+"="*78)
print("STAGE 6 -- the monodromy over the mass line: S_3 for every E<1, Z/3 exactly at E=1")
print("="*78)
print("\n  prop:autA2 (groupoid paper) realises the corpus's S_3 = W(A_2) as the DECK GROUP of the")
print("  3-sheeted cover of the mass line. So 'does the A_2 survive to E=1' is a monodromy question,")
print("  and a cubic's Galois group lies in A_3 = Z/3 iff its discriminant is a SQUARE in the base.")
_a = sp.Symbol('alpha', positive=True)
_Ms = sp.Symbol('M', positive=True)
_rs = sp.Symbol('r')
def _galois(Eval):
    _cub = _rs**3 + (Eval**2 - 1)*_a**2*_rs + 2*_Ms*_a**2
    _Dl  = sp.factor(sp.discriminant(_cub, _rs))
    _rat = sp.simplify(sp.sqrt(_Dl)).is_rational_function(_Ms)
    return _Dl, _rat
for _Ev in (sp.Integer(0), sp.Rational(1,2), sp.Rational(9,10), sp.Rational(99,100), sp.Integer(1)):
    _Dl, _rat = _galois(_Ev)
    print(f"    E={str(_Ev):>6}  sqrt(Delta) rational in M? {str(_rat):>5}  ->  deck group = {'Z/3' if _rat else 'S_3'}")
    if _Ev == 1: assert _rat,     "E=1 must have square discriminant (deck group Z/3)"
    else:        assert not _rat, "E<1 must have non-square discriminant (deck group S_3)"
print("\n  the reduction is EXACTLY at E=1, not at the discriminant crossing: Delta is a square in M")
print("  iff a^2(1-E^2)^3 - 27M^2 is a perfect square, and a quadratic c - 27M^2 is a perfect square")
print("  iff c = 0, i.e. iff (1-E^2)^3 = 0.  Branch structure agrees: E<1 branches at two masses")
print("  (transpositions, S_3); E=1 branches only at M=0 (a single 3-cycle, Z/3).")
print("\n  ANSWER TO THE STANDING QUESTION -- and it is a COMPLEMENTARITY, not a loss.")
print("  In depressed form r^3+pr+q with p=(E^2-1)a^2 and q=2M a^2: the roots are EQUILATERAL iff")
print("  p=0, and (p being M-free while q is linear in M) Delta = -4p^3-27q^2 is a SQUARE in M iff")
print("  p=0 as well. THE SAME CONDITION -- met at E=1 alone. Hence:")
print("     E<1 : colinear real roots, NO symmetry as a figure  |  monodromy = FULL S_3")
print("     E=1 : the equilateral A_2 weight triangle, S_3 as    |  monodromy = Z/3 only")
print("           the figure's OWN symmetry                      |")
print("  Neither end lacks W(A_2)=S_3. The deformation EXCHANGES how it is carried -- from the")
print("  monodromy of the cover to the symmetry of the configuration -- and one condition (p=0)")
print("  governs the exchange. The two cubics are geometrically related throughout; this is the")
print("  structure of the relation, not an obstruction to it.")
print("  NOTE the scope: this concerns the bead<->groupoid pair. It says nothing about the separate,")
print("  walled question of a realised colour isometry (su(3) not in so(5,1)).")
# the equivalence, asserted so it can fail
for _Ev in (sp.Integer(0), sp.Rational(1,2), sp.Rational(9,10), sp.Integer(1)):
    _pv = (_Ev**2 - 1)
    _equi = (_pv == 0)
    _Dl  = sp.discriminant(_rs**3 + _pv*_a**2*_rs + 2*_Ms*_a**2, _rs)
    _sqr = sp.simplify(sp.sqrt(sp.factor(_Dl))).is_rational_function(_Ms)
    assert _equi == _sqr, f"equilateral-figure and square-discriminant must coincide (E={_Ev})"
import numpy as _np2
_rt1 = _np2.roots([1, 0, 0, 0.30])
assert _np2.ptp(_np2.abs(_rt1)) < 1e-9, "E=1 roots must be equilateral (S_3 as the figure)"
_rt0 = _np2.roots([1, 0, -1, 0.30])
assert _np2.abs(_rt0.imag).max() < 1e-9 and _np2.ptp(_np2.abs(_rt0)) > 0.1, "E=0 roots colinear, not equilateral"
print("  [asserted] equilateral-figure <=> square-discriminant, at every E tested.")
print("  NOT asserted: that E=1's uniqueness here carries physical significance. It is recorded as a")
print("  fact about the family -- the flat leaf k=0 is its one member with reduced monodromy.")
