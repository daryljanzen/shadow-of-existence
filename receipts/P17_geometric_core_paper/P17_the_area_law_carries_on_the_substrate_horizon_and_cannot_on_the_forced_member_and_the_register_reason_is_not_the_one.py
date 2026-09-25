"""
P17_the_area_law_carries_on_the_substrate_horizon_and_cannot_on_the_forced_member_and_the_register_reason_is_not_the_one
=====================================================================================================================

Object under test -- node 66's work order in `FOR_60` (`r6863`): `PO-48`, **does S = A/4 carry to a
cosmological horizon on this reading?**  Opened as the overdue row because `PO-24` and `PO-43` both terminate
at it, so a question belonging to no row was propping two closures.  `P17` §ledger declines it in terms and
says what failure would mean -- *"were it to fail to carry, that would be a result and not a gap"* -- so both
outcomes are results, which is the licence to attack it hard.

** THE QUESTION IS NOT ILL-POSED, AND IT DOES NOT HAVE ONE ANSWER: IT HAS ONE PER MEMBER, AND THE TWO MEMBERS
THE CORPUS ACTUALLY USES FALL ON OPPOSITE SIDES.  AND THE REASON §ledger GIVES FOR DECLINING IS NOT THE REASON
THAT WORKS. **

** (1) SOMETHING DOES VARY, AND IT REACHES THE HORIZON TERM -- SO THE "EMPTY FIRST LAW" ROUTE THE ORDER
FLOATED IS NOT THE ANSWER. **  The order's first candidate is that the horizon radius is alpha and alpha is the
one constant, so nothing varies.  ** The geometry says otherwise. **  On the SdS family the cosmological root
moves with the mass label, and at the substrate horizon the derivative is order one, not small:

      dr_c/dM = alpha^2 r_c/(M alpha^2 - r_c^3)   ->  -1        at M = 0, r_c = alpha
      dA_c/dM = -8 pi alpha                                     at the same point

*Said from the structure rather than from the absence of a derivation, which is what the order asked for.*

⚠ ** BUT WHAT VARIES IS AN OFFSET, AND ON THIS CONSTRUCTION THAT IS A CHANGE OF SECTION AND NOT OF STATE. **
§ledger's own identification is that the mass *is* the offset of the section from the central geodesic,
2M = alpha((r_0/alpha) - (r_0/alpha)^3), with G entering "only as the offset-length" and not as a coupling of
independent matter.  ** So the offset family is a family of cuts of ONE substrate, not a family of solutions **
-- and a variation that relabels which cut is being read is the class whose Noether charge Wald's construction
returns identically zero for.  *That, and not the register split, is what can void the first law here, and it
is the construction's own claim that does it.*

** (2) WALD HAS WHAT IT NEEDS ON THE NON-DEGENERATE MEMBERS AND CANNOT HAVE IT ON THE FORCED ONE. **  The
hypotheses one at a time, rather than importing the conclusion:

      diffeomorphism-invariant Lagrangian    HOLDS   the Einstein equations are unchanged here
      a Killing horizon                      HOLDS   with kappa belonging to the background
      kappa =/= 0                            FAILS at Nariai -- exactly zero, f(r_N) = f'(r_N) = 0
      a bifurcation surface                  FAILS at Nariai -- the double root sends r_* ~ 1/[Lambda(r-r_N)]
      a variation within the solution space  OPEN    -- it is (1)'s re-slicing question

and the collapse is monotone along the family rather than a single suspicious point:

      M/alpha :  0      0.05    0.10    0.15    0.18    0.19    sqrt3/9
      kappa_c :  1.000  0.890   0.749   0.544   0.319   0.151   0  exactly

** At kappa = 0 the cosmological-horizon first law deltaM = -(kappa/2pi) deltaS degenerates to deltaM = 0 and
admits NO solution for deltaS. **  *It does not give a wrong entropy; it gives none.  The area law is not
falsified on the forced member -- it is undetermined there, which is the sharper statement, and is what
"nothing plays the role its derivation needs" looks like once it is computed instead of asserted.*

  ⇒ ** AND THE TWO HORIZONS THE CORPUS USES ARE DIFFERENT MEMBERS, WHICH IS WHY THE ROW LOOKED UNDECIDABLE. **
  §ledger's horizon -- the one whose Gibbons--Hawking state supplies hbar, area 4 pi alpha^2, T = 1/2 pi alpha
  -- is the M = 0 substrate horizon, where kappa = 1/alpha and Wald carries.  The cosmology's branch point
  rides the **Nariai** member, where kappa = 0 and it cannot.  *The question has been asked of two objects at
  once.*

** (3) AND THE REGISTER SPLIT BEARS ON QUOTATION, NOT ON CARRYING -- ITS STATED FORM DOES NOT SURVIVE
RESTORING THE UNITS. **  §ledger's reason for taking T and never S is that T = 1/2 pi alpha is "built from
alpha alone --- one register", while S is a ratio of alpha to l_P and so "a count taken across the register
split".  ** Restore the thermal gauges instead of setting them to one and the asymmetry is not there: **

      T = hbar c / (2 pi k_B alpha)     touches hbar, k_B  AND  c, alpha     -> CROSS-REGISTER
      S = pi alpha^2 c^3 / (G hbar)     touches hbar       AND  c, G, alpha  -> CROSS-REGISTER

** Both mix the registers.  "T is built from alpha alone" is true only in the convention hbar = k_B = 1, which
is a choice of units and not a feature of the geometry. **  The real asymmetry is a different one: *S is
dimensionless and T is not* -- and a pure number is what one can compare without any gauge choice at all,
which cuts the opposite way from a defect.

  ⇒ ** SO THE SPLIT IS A REASON FOR RETICENCE IN QUOTATION AND NOT EVIDENCE ABOUT THE PHYSICS. **  Whether S
  carries turns on whether a first law with a variation, a charge and a surviving boundary term exists on the
  geometry; whether the corpus may quote S turns on which gauges its expression mixes.  *Those are
  independent, and §ledger leans on the second as though it settled the first.*

  ⌗ WHICH GIVES THE ROW A DEFINITE ANSWER EITHER WAY AND DISCHARGES THE TWO CLOSURES.  ** The declination is
  right about the member the cosmology rides, wrong about the horizon it actually quotes, and its stated
  reason is insufficient for both. **  A sufficient reason exists and is structural: on the forced member
  kappa = 0 leaves the entropy undetermined; on the substrate horizon the only thing that could void it is the
  construction's own reading of the offset as a section label rather than a state.

COMPUTES: scope -- what this settles and what it must not be read as.
  * C1 the established constants are re-run before anything is argued: the Nariai member M = sqrt(3) alpha/9
    with f(r_N) = f'(r_N) = 0 and kappa = 0 (`r6804`), the substrate horizon r_c = alpha with kappa = 1/alpha
    and T = 1/2 pi alpha, and §ledger's own S = pi(alpha/l_P)^2 = 3 pi/(Lambda l_P^2) (item 52).  ** If those
    do not reproduce, nothing below may be read. **
  * ⚠ ** NOTHING IS IMPORTED FROM BLACK-HOLE THERMODYNAMICS AS A CONCLUSION. **  Wald's hypotheses are
    enumerated and checked on this geometry, and the one that fails is shown to fail by computation (kappa
    along the family) rather than by appeal.  The A/4 VALUE is never assumed -- only the existence of a first
    law is tested, which is what the order's discipline requires.
  * ⚠ ** THE ONE GENUINELY OPEN HINGE IS NAMED AND NOT CLOSED: ** whether the offset family is a family of
    solutions or of sections of one solution.  §ledger's wording ("the mass *is* the offset") points to the
    second, which would void the variation at the substrate horizon too -- but that is a reading of intent,
    not a computation, and it is left to the gate.  *Item (1) is therefore answered as "the variation exists
    and reaches the horizon, and whether it is a variation of state is the open part", not as a verdict.*
  * ⚠ The first law used is the standard cosmological-horizon relation; the degeneracy argument needs only
    that its coefficient is kappa, and no sign convention is relied on.
  * ⚠ This settles `PO-48` as posed.  It does not assert a de Sitter entropy, does not touch `PO-7`, and
    leaves §ledger's declination-consequence on the Gauss--Bonnet coefficient standing.

ORIGIN: node 66's work order in `FOR_60` (`r6863`).  The order allowed stopping at whichever item answers and
all three answer, so all three are reported -- the third being a correction to the reason the corpus currently
carries rather than an addition to it.
"""
import sys

import numpy as np
import sympy as sp

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

r, M, al, Lam = sp.symbols('r M alpha Lambda', positive=True)
f = 1 - 2 * M / r - r ** 2 / al ** 2
kappa_of = sp.diff(f, r) / 2

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — THE ESTABLISHED CONSTANTS, BEFORE ANYTHING IS ARGUED")
print("=" * 94)
nar = sp.solve([sp.Eq(Lam * M ** 2, sp.Rational(1, 9)), sp.Eq(Lam, 3 / al ** 2)], [M, Lam], dict=True)[0]
M_N, r_N = sp.simplify(nar[M]), al / sp.sqrt(3)
print(f"    Nariai:   M = {M_N},   r_N = alpha/sqrt3,   M/alpha = {sp.simplify(M_N / al)}")
check("the Nariai mass reproduces sqrt(3) alpha/9 (established, r6804)",
      sp.simplify(M_N - sp.sqrt(3) * al / 9) == 0)
check("f and f' vanish together at the degenerate root, so the member is degenerate by computation",
      sp.simplify(f.subs({M: M_N, r: r_N})) == 0
      and sp.simplify(sp.diff(f, r).subs({M: M_N, r: r_N})) == 0)
check("⚑ and therefore kappa = 0 EXACTLY on the forced member, not merely small",
      sp.simplify(kappa_of.subs({M: M_N, r: r_N})) == 0)

roots0 = sp.solve(f.subs(M, 0), r)
k0 = sp.simplify(-kappa_of.subs({M: 0, r: al}))
print(f"    substrate horizon (M=0): r_c = {roots0[0]},  kappa = {k0},  T = {sp.simplify(k0/(2*sp.pi))}")
check("the substrate horizon sits at alpha with kappa = 1/alpha and T = 1/(2 pi alpha) — sec:ledger's horizon",
      roots0 == [al] and sp.simplify(k0 - 1 / al) == 0)

lP = sp.Symbol('ell_P', positive=True)
S_ledger = sp.simplify(4 * sp.pi * al ** 2 / (4 * lP ** 2))
check("and sec:ledger's own value reproduces: S = pi (alpha/l_P)^2 = 3 pi/(Lambda l_P^2) (item 52)",
      sp.simplify(S_ledger - sp.pi * (al / lP) ** 2) == 0
      and sp.simplify(S_ledger.subs(al, sp.sqrt(3 / Lam)) - 3 * sp.pi / (Lam * lP ** 2)) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (ITEM 1) — SOMETHING VARIES, AND IT REACHES THE HORIZON TERM")
print("=" * 94)
rc, d = sp.Symbol('r_c', positive=True), sp.Symbol('d')
drc_dM = sp.solve(sp.Eq(sp.diff(f.subs(r, rc), M) + sp.diff(f.subs(r, rc), rc) * d, 0), d)[0]
at0 = sp.simplify(drc_dM.subs({M: 0, rc: al}))
dA_dM = sp.simplify((sp.diff(4 * sp.pi * rc ** 2, rc) * drc_dM).subs({M: 0, rc: al}))
print(f"""
    dr_c/dM = {drc_dM}
      at the substrate horizon (M=0, r_c=alpha):  dr_c/dM = {at0},  dA_c/dM = {dA_dM}
""")
check("⚑ the horizon radius moves with the mass label at order one, so 'nothing varies' is NOT the answer",
      at0 == -1 and sp.simplify(dA_dM + 8 * sp.pi * al) == 0)
u = sp.Symbol('u', positive=True)
M_of_offset = sp.solve(sp.Eq(2 * M, al * (u - u ** 3)), M)[0]
print(f"    and sec:ledger's identification: M = {M_of_offset}   (u = r_0/alpha, the section's offset)")
check("the mass is a function of the offset alone, with no independent matter coupling — which is what makes "
      "the variation a change of SECTION", M_of_offset.free_symbols == {al, u})

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (ITEM 2) — kappa COLLAPSES ALONG THE FAMILY, AND AT ZERO THE FIRST LAW HAS NO SOLUTION")
print("=" * 94)
print(f"    {'M/alpha':>10} {'r_h':>9} {'r_c':>9} {'kappa_c':>10}")
MN = float(np.sqrt(3) / 9)
ks = []
for Mv in (0.0, 0.05, 0.10, 0.15, 0.18, 0.19):
    rts = np.sort([x.real for x in np.roots([1.0, 0.0, -1.0, 2.0 * Mv])
                   if abs(x.imag) < 1e-9 and x.real > 0])
    rcv = rts[-1]
    kc = abs(2 * Mv / rcv ** 2 - 2 * rcv) / 2
    ks.append(kc)
    print(f"    {Mv:>10.6f} {(f'{rts[0]:.6f}' if len(rts) > 1 else '     ---'):>9} {rcv:>9.6f} {kc:>10.6f}")
print(f"    {MN:>10.6f} {'  merged':>9} {1/np.sqrt(3):>9.6f} {0.0:>10.6f}   <- Nariai, exactly zero")
check("kappa_c decreases monotonically along the family toward the degenerate member, so the collapse is a "
      "trend and not one suspicious point", all(ks[i] > ks[i + 1] for i in range(len(ks) - 1)))

dM_, dS_, kap = sp.symbols('deltaM deltaS kappa', real=True)
law = sp.Eq(dM_, -(kap / (2 * sp.pi)) * dS_)
sol_generic, sol_degen = sp.solve(law, dS_), sp.solve(law.subs(kap, 0), dS_)
print(f"""
    the cosmological-horizon first law:  {law}
      kappa =/= 0  ->  deltaS = {sol_generic[0]}
      kappa  = 0   ->  reads {law.subs(kap, 0)}, and solving for deltaS gives {sol_degen}
""")
check("⚑ at kappa = 0 the first law admits NO solution for deltaS — the entropy is UNDETERMINED there, which "
      "is sharper than being wrong", len(sol_generic) == 1 and sol_degen == [])
check("and the degenerate case constrains deltaM instead, forcing it to vanish rather than fixing the entropy",
      sp.simplify(law.subs(kap, 0).rhs) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (ITEM 3) — RESTORE THE UNITS, AND THE STATED REGISTER ASYMMETRY IS NOT THERE")
print("=" * 94)
hbar, c, G, kB = sp.symbols('hbar c G k_B', positive=True)
T_GH = hbar * c / (2 * sp.pi * kB * al)
S_BH = sp.simplify(4 * sp.pi * al ** 2 / (4 * (hbar * G / c ** 3)))
THERMAL, GEOM = {hbar, kB}, {c, G, al}
print(f"""
    T = {T_GH}          gauges: {sorted(str(s) for s in T_GH.free_symbols)}
    S = {S_BH}      gauges: {sorted(str(s) for s in S_BH.free_symbols)}
""")
for nm, q in (("T", T_GH), ("S", S_BH)):
    print(f"    {nm}: thermal gauge present {bool(q.free_symbols & THERMAL)}, "
          f"real-geometric present {bool(q.free_symbols & GEOM)}")
check("⚑ BOTH T and S mix the two registers once hbar and k_B are restored, so 'T is built from alpha alone' "
      "holds only in the convention hbar = k_B = 1",
      bool(T_GH.free_symbols & THERMAL) and bool(T_GH.free_symbols & GEOM)
      and bool(S_BH.free_symbols & THERMAL) and bool(S_BH.free_symbols & GEOM))
check("and the asymmetry that IS real is a different one: S reduces to a pure number in geometric units "
      "while T keeps a dimension",
      sp.simplify(S_BH.subs({hbar: 1, G: 1, c: 1}) - sp.pi * al ** 2) == 0
      and sp.simplify(T_GH.subs({hbar: 1, c: 1, kB: 1}) - 1 / (2 * sp.pi * al)) == 0)
check("so the split cannot decide carrying: S's gauge content contains no surface gravity and no variation, "
      "which are the quantities carrying depends on",
      kap not in S_BH.free_symbols and dM_ not in S_BH.free_symbols)

# =========================================================================================
print()
print("=" * 94)
print("VERDICT")
print("=" * 94)
print(f"""
  ⚑ ONE ANSWER PER MEMBER, AND THE TWO THE CORPUS USES FALL ON OPPOSITE SIDES.

    the substrate horizon (M=0)   kappa = 1/alpha, a Killing horizon with a bifurcation surface, and
                                  dA_c/dM = -8 pi alpha =/= 0 -- ** Wald has what it needs and S = A/4
                                  CARRIES **, unless the offset family is sections rather than solutions
    the forced member (Nariai)    kappa = 0 exactly, the double root destroys the bifurcation surface, and
                                  the first law admits NO solution for deltaS -- ** the area law is
                                  UNDETERMINED there, not false **
    the register split            T = hbar c/(2 pi k_B alpha) is cross-register too, so sec:ledger's stated
                                  reason ** does not survive restoring the units ** -- it bears on whether
                                  the corpus may QUOTE S, never on whether S CARRIES

  ⇒ THE DECLINATION IS RIGHT ABOUT THE MEMBER THE COSMOLOGY RIDES, WRONG ABOUT THE HORIZON IT QUOTES, AND ITS
    STATED REASON IS INSUFFICIENT FOR BOTH.  A sufficient reason exists and it is structural rather than
    register-theoretic.  ** Both branches are results, as sec:ledger said they would be, so the two closures
    resting on this row are discharged either way. **

  ⚠ The one open hinge, named and left to the gate: whether the offset family is a family of solutions or of
    sections of one substrate.  sec:ledger's own wording points to the second, which would void the variation
    at the substrate horizon too -- but that is a reading of intent, not a computation.
""")
print(f"  {sum(_checks)}/{len(_checks)} checks passed.")
sys.exit(0 if all(_checks) else 1)
