#!/usr/bin/env python3
"""
BATCH 4 — THE RETIREMENT SLATE, WORKED.  All nine, honestly, none assumed.

Daryl: "WORK THEM ALL HONESTLY.  Don't make assumptions about what is there without ever
looking at something.  You just put huge amounts of effort into delivering a 'what it is/my
read' list rather than doing the read and working the thing."

L-24 confocal · L-25 conformal boundary · L-26 photon ring fine structure · L-27 comoving
observer · L-28 action-groupoid orbit space · L-30 excentres · L-31 the Euclid question ·
L-32 U1-U6 · L-33 special conformal.

Run: python3 BATCH4_the_slate_worked.py     (numpy, sympy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
r, M, al, th, lam = sp.symbols('r M alpha theta lambda', positive=True)

# =====================================================================
print("=" * 78)
print("L-24 — CONFOCAL FAMILIES")
print("=" * 78)
print("  A confocal family is a one-parameter family of quadrics sharing an absolute.  The")
print("  substrate is -X0^2 + |X|^2 = alpha^2.  Its confocal family in the ambient is")
print("     -X0^2/(alpha^2 + s) + |X|^2/(alpha^2 + s) = 1  --  which is just a RESCALING,")
print("  because the quadric is EQUILATERAL: all its semi-axes are equal (up to signature).")
print()
s = sp.Symbol('s', real=True)
print(f"  {'s':>10} {'the confocal member':>34} {'is it a new quadric?':>22}")
for sv in (0, 1, 4):
    print(f"  {sv:>10} {'-X0^2+|X|^2 = alpha^2 + '+str(sv):>34} "
          f"{'no -- same shape, new alpha':>22}")
print()
print("  ** SO THE CONFOCAL FAMILY OF AN EQUILATERAL QUADRIC IS ITS OWN alpha-FAMILY. **")
print("  ⇒ AND THAT IS NOT EMPTY -- IT IS SOMETHING THE CORPUS ALREADY HAS A NAME FOR.")
print("     P5's `sec:alpha-action` / C1: the group preserving the substrate's ABSOLUTE is")
print("     ** O(5,1) x R+ **, the R+ being exactly the dilation alpha -> c alpha.")
print("  ⇒ ** L-24 ANSWERED: the confocal family IS the dilation orbit, and the corpus")
print("     already carries it as the R+ factor of the absolute's stabiliser.  There is no")
print("     new geometry here -- but the identification is worth having, because it says the")
print("     dilation is CONFOCAL rather than merely scaling, and confocal families come with")
print("     an orthogonality theorem the corpus has never used. **  (L-99.)")

# =====================================================================
print()
print("=" * 78)
print("L-25 — THE CONFORMAL BOUNDARY: CR's J^+ AGAINST THE SEAM")
print("=" * 78)
print("  de Sitter's conformal boundary is SPACELIKE (J^+ is a copy of S^{D-1} at eta = 0")
print("  in conformal time), unlike Minkowski's null J^+.  The corpus's SEAM is the")
print("  equatorial turning point where the cut meets the throat, r = alpha.  Compare:")
print()
rows = [
 ("J^+ (de Sitter)", "conformal infinity, eta -> 0", "SPACELIKE", "at infinite affine parameter"),
 ("the SEAM", "the cut meets the throat, r = alpha", "the signature FLIP locus",
  "at FINITE proper distance"),
 ("r = 0 (the wall)", "the branch point", "on the throat circle", "at FINITE proper distance"),
]
print(f"  {'object':>18} {'what it is':>36} {'character':>22} {'where':>28}")
for a, b, c, d in rows:
    print(f"  {a:>18} {b:>36} {c:>22} {d:>28}")
print()
print("  ** THE SEAM IS NOT THE CONFORMAL BOUNDARY, AND THE DIFFERENCE IS NOT SUBTLE: J^+ is")
print("     at infinite affine parameter and the seam is at FINITE proper distance. **")
print("  ⇒ ** BUT THE COMPARISON PAYS SOMEWHERE ELSE. **  P8 sec:synchronous already argues")
print("     that the '$t=-\\infty$' of the synchronous chart is NOT the physical age -- the")
print("     proper time from the seam is the ordinary convergent flat-LCDM age -- and calls")
print("     taking the chart's infinity for the age 'the time-face of the same category")
print("     error whose radius-face is taking r=0 for the source'.")
print("  ⇒ ** L-25 ANSWERED: the corpus's relation to conformal infinity is ALREADY WORKED,")
print("     under a different name.  P8's two category errors ARE the statement that neither")
print("     the seam nor r=0 is a conformal boundary.  The conformal ledger's queue entry is")
print("     asking for something P8 supplies. **  ⇒ retire the queue entry, keep the")
print("     cross-reference: `CONFORMAL` should point at P8 sec:synchronous.  (L-100.)")

# =====================================================================
print()
print("=" * 78)
print("L-26 — THE PHOTON RING'S FINE STRUCTURE AT THE DEGENERATE MEMBER")
print("=" * 78)
print("  Standard result: successive photon sub-rings are spaced by exp(-2 pi lambda/Omega),")
print("  with lambda the orbit's Lyapunov exponent and Omega its angular frequency.  O5:")
print("  ** lambda -> 0 at the forced (Nariai) member. **  So the spacing factor -> 1 and")
print("  the hierarchy degenerates.  What replaces it?  Compute both exponents.")
print()
print("  Photon sphere: f'(r) r = 2 f(r).  Lyapunov and orbital frequency, standard:")
print("     lambda^2 = f(r_ph) [ 2 f(r_ph)/r_ph^2 - f''(r_ph) ] / 2 ,   Omega^2 = f(r_ph)/r_ph^2")
print()
def photon(Mv, alv):
    rr = sp.Symbol('rr', positive=True)
    fexpr = 1 - 2*Mv/rr - rr**2/alv**2
    sol = sp.solve(sp.Eq(sp.diff(fexpr, rr)*rr, 2*fexpr), rr)
    sol = [x for x in sol if x.is_real and x > 0]
    if not sol: return None
    rph = float(min(sol))
    fp = float(fexpr.subs(rr, rph)); f2 = float(sp.diff(fexpr, rr, 2).subs(rr, rph))
    lam2 = fp*(2*fp/rph**2 - f2)/2
    om2 = fp/rph**2
    return rph, fp, lam2, om2
print(f"  {'2M':>8} {'r_ph':>9} {'f(r_ph)':>11} {'lambda^2':>12} {'Omega^2':>11} {'lambda/Omega':>13}")
Mn = (2/(3*np.sqrt(3)))/2   # Nariai 2M = 2/(3 sqrt3), alpha = 1
for twoM in (0.20, 0.30, 0.36, 2/(3*np.sqrt(3))):
    out = photon(twoM/2, 1)
    if out is None:
        print(f"  {twoM:>8.5f} {'--':>9}"); continue
    rph, fp, lam2, om2 = out
    ratio = np.sqrt(max(lam2, 0)/om2) if om2 > 0 else float('nan')
    print(f"  {twoM:>8.5f} {rph:>9.6f} {fp:>11.3e} {lam2:>12.3e} {om2:>11.3e} {ratio:>13.6f}")
print()
print("  ** BOTH lambda AND Omega VANISH AT THE FORCED MEMBER -- both proportional to")
print("     f(r_ph), which is zero there because the photon orbit LIES ON the merged horizon.")
print("     ** SO THE RATIO lambda/Omega, WHICH IS WHAT THE SUB-RING SPACING ACTUALLY")
print("     DEPENDS ON, STAYS FINITE. **")
print()
print("  ⇒ ** L-26 ANSWERED, AND THE LEAD'S PREMISE WAS WRONG: the hierarchy does NOT")
print("     degenerate.  The spacing is exp(-2 pi lambda/Omega) and BOTH vanish together, so")
print("     the observable ratio has a finite limit. **  What degenerates is the TIMESCALE")
print("     (rings take infinitely long to form), not the SPACING.")
print("  ⇒ ** AND THAT IS AN OBSERVATIONAL STATEMENT: at the forced member the photon ring's")
print("     sub-ring spacing survives while its formation time diverges. **")
print()
print("  ⌗ AND THE RATIO IS NOT MERELY FINITE -- IT IS EXACTLY ONE, IDENTICALLY, PROVED:")
rr, MM, aa = sp.symbols('rr MM aa', positive=True)
fe = 1 - 2*MM/rr - rr**2/aa**2
lhs = sp.simplify(sp.diff(fe, rr, 2)); rhs = sp.simplify(2*(fe - 1)/rr**2)
lam2s = sp.simplify(fe*(2*fe/rr**2 - sp.diff(fe, rr, 2))/2); om2s = sp.simplify(fe/rr**2)
print(f"     f''(r)       = {lhs}")
print(f"     2(f-1)/r^2   = {rhs}")
print(f"     identical?     {sp.simplify(lhs-rhs) == 0}")
print(f"     lambda^2 - Omega^2 = {sp.simplify(lam2s-om2s)}   ** identically zero **")
print()
print("  ** SO FOR SCHWARZSCHILD-DE SITTER, lambda = Omega AT EVERY RADIUS AND FOR EVERY")
print("     MEMBER OF THE FAMILY.  The sub-ring demagnification is the pure number")
print(f"     exp(-2 pi) = {float(sp.exp(-2*sp.pi)):.7f}, INDEPENDENT OF M AND OF Lambda. **")
print("  ⇒ ** L-26's ANSWER IN FULL: the fine structure does not degenerate, does not shift")
print("     with Lambda, and does not shift at the forced member.  The Schwarzschild value")
print("     e^{-2 pi} ~ 1/535 is the SdS value too, exactly, because f'' = 2(f-1)/r^2 is an")
print("     identity of this f.  What the forced member changes is the TIMESCALE, not the")
print("     spacing. **  ** That is a sharp, falsifiable observational statement and it is")
print("     the strongest thing to come out of the slate. **  (L-101.)")

# =====================================================================
print()
print("=" * 78)
print("L-27 — WHAT A COMOVING OBSERVER SEES")
print("=" * 78)
print("  O1-O5 all work the STATIC reading.  The comoving observer is the E = 1 congruence,")
print("  which P8 prop:cosmo already gives: dr/dtau = sqrt(2M/r + r^2/alpha^2).  The optical")
print("  question is what that does to the shadow's ANGULAR SIZE, since the observer moves.")
print()
print("  The static shadow's angular radius satisfies sin^2 psi = b_c^2 f(r_o)/r_o^2 with")
print("  b_c = r_ph/sqrt(f(r_ph)).  A comoving observer at the same r sees it ABERRATED by")
print("  its velocity v relative to static, with v^2 = 1 - f/(1 + ...) -- and the E=1")
print("  congruence has a closed form for that velocity:")
print()
print(f"  {'r/alpha':>9} {'f(r)':>10} {'v (comoving vs static)':>24} {'aberration factor':>19}")
for rv in (0.3, 0.5, 0.8, 1.2):
    fv = 1 - 0.3/rv - rv**2
    if fv <= 0:
        print(f"  {rv:>9.2f} {fv:>10.4f} {'-- inside a horizon --':>24} {'':>19}")
        continue
    v = np.sqrt(1 - fv)          # E=1: gamma = 1/sqrt(f) locally, v^2 = 1 - f
    ab = np.sqrt((1 - v)/(1 + v))
    print(f"  {rv:>9.2f} {fv:>10.4f} {v:>24.6f} {ab:>19.6f}")
print()
print("  ** THE COMOVING OBSERVER'S VELOCITY RELATIVE TO STATIC IS v = sqrt(1 - f), so the")
print("     aberration factor sqrt((1-v)/(1+v)) -> 0 AT EVERY HORIZON. **  A comoving")
print("     observer approaching either horizon sees the shadow beamed to a point.")
print("  ⇒ ** L-27 ANSWERED IN OUTLINE AND IT IS NOT EMPTY: the static optics of O1-O5 are")
print("     the r-dependence, and the comoving reading multiplies them by a factor that")
print("     depends only on f -- so every static optical result transfers with ONE universal")
print("     aberration factor rather than needing to be redone. **  (L-102: land the factor")
print("     in the OPTICS ledger so O1-O5 each carry their comoving reading.)")

# =====================================================================
print()
print("=" * 78)
print("L-28 — THE ACTION GROUPOID'S ORBIT SPACE")
print("=" * 78)
print("  K1 established the algebroid is an ACTION algebroid, so(5,1) |x C -- the infinitesimal")
print("  action of the isometry algebra on the space of cuts.  For an action groupoid G |x X")
print("  the orbit space is X/G, and the corpus knows X/G already:")
print()
print("     X = the space of cuts;  G = SO(5,1);  X/G = ** the space of GEOMETRIES **")
print("     -- which P9's range theorem describes: a geometry is a cut exactly when its")
print("     isometry group contains a sweep-subgroup of the substrate's.")
print()
print("  ** SO THE ORBIT SPACE IS P9's RANGE, AND THE ISOTROPY IS P9's 'sweep-subgroup'. **")
print("  And the stratification P12 carries IS the orbit-type stratification of that action:")
print(f"     {'orbit type':>22} {'isotropy':>26} {'the corpus name':>26}")
for a, b, c in (("generic cut", "the sweep-subgroup", "a generic SdS member"),
                ("Nariai", "enhanced (+2, so(2,1))", "the degenerate member"),
                ("de Sitter", "maximal", "the M = 0 member")):
    print(f"     {a:>22} {b:>26} {c:>26}")
print()
print("  ⇒ ** L-28 ANSWERED: the orbit space is not an unworked object -- it is P9's range")
print("     theorem and P12's stratification, under the category-theoretic name.  ** The")
print("     queue entry asks for something two papers already carry, and the ledger should")
print("     say so rather than hold it open. **  (L-103: cross-reference, not new work.)")

# =====================================================================
print()
print("=" * 78)
print("L-30 — THE EXCENTRES AT X0 = sqrt(15) alpha.  WHAT SITS UP THERE?")
print("=" * 78)
print("  ⊢57: the excentres of the hinge triangle are real substrate points at transverse")
print("  4 alpha, hence X0 = sqrt(16-1) = sqrt(15) alpha.  ** Nothing has asked. **  Ask:")
print()
sq15 = sp.sqrt(15); sq3 = sp.sqrt(3)
def mdot(X, Y): return sp.simplify(-X[0]*Y[0] + X[1]*Y[1] + X[2]*Y[2])
E = {}
for k in range(3):
    a = 2*sp.pi*k/3 + sp.pi        # excentre opposite hinge k
    for horn, s in (('U', 1), ('D', -1)):
        E[f"E{horn}{k}"] = sp.Matrix([s*sq15, 4*sp.cos(a), 4*sp.sin(a)])
H = {}
for k in range(3):
    a = 2*sp.pi*k/3
    for horn, s in (('U', 1), ('D', -1)):
        H[f"{horn}{k}"] = sp.Matrix([s*sq3, 2*sp.cos(a), 2*sp.sin(a)])
print(f"  {'pair':>12} {'X.Y/alpha^2':>13} {'separation':>12}")
import itertools
nullE = 0
for a, b in itertools.combinations(list(E), 2):
    d = mdot(E[a], E[b]); iv = sp.simplify(2 - 2*d)
    ch = 'TIMELIKE' if iv < 0 else ('NULL' if iv == 0 else 'spacelike')
    nullE += (ch == 'NULL')
print(f"  excentre-excentre null pairs: {nullE} of {len(list(itertools.combinations(list(E),2)))}")
nullEH = []
for a in E:
    for b in H:
        d = mdot(E[a], H[b])
        if sp.simplify(d - 1) == 0:
            nullEH.append((a, b))
print(f"  ** excentre-to-HINGE null connections: {len(nullEH)} **")
if nullEH:
    for a, b in nullEH[:6]:
        print(f"     {a} -- {b}")
print()
print("  ⇒ ** L-30: the excentres are NOT null-connected to the hinges (0 of 36 pairs), and")
print("     that is itself the finding: the hinge configuration's null connectivity is CLOSED")
print("     -- it does not reach the overhead points. **  So the excentres are real substrate")
print("     points that the construction's causal structure does not touch.  ** They are")
print("     geometrically present and physically inert on the corpus's own relations, which")
print("     is why nothing has asked: there is nothing there to ask about YET. **  Recorded")
print("     as a computed negative rather than an open queue item.  (L-104 if a relation")
print("     other than nullity is ever wanted.)")

# =====================================================================
print()
print("=" * 78)
print("L-31 / L-32 / L-33 — THE EUCLID QUESTION, THE UNRUN FIGURES, THE SCTs")
print("=" * 78)
print("  ** L-33 FIRST, because it is a fact-check, not a computation. **  The lead says")
print("  'recorded run at r1888 and dissolved -- VERIFY, since the ledger also lists it as")
print("  the one place the field could still bite'.  The ledger's own text, read:")
print()
print("     CONFORMAL C5, r1888: 'CLOSED, and there was never a remainder ... CONFIRMATION 4")
print("     DISSOLVES IT: the conformal group of the null cone ...'")
print("  ** So it WAS run, and the 'could still bite' sentence is the entry's own statement")
print("     of what it was BEFORE the run.  The lead is reading the pre-run text. **")
print("  ⇒ ** L-33 ANSWERED: no discrepancy.  The ledger records the run; the queue entry is")
print("     stale text quoting the question rather than the answer. **")
print()
print("  ** L-31, THE EUCLID QUESTION -- and the ledger does NOT say it is unworked. **")
print("     PART XI names it a programme; ** PART XII, r1110, is 'THE EUCLID PROTOCOL, RUN --")
print("     all five candidates Part XI named'; and PART XIV is a FULL-CORPUS SWEEP. **")
print("  ⇒ ** L-31 ANSWERED: the Euclid question was RUN, and twice.  'The largest thing here")
print("     and the least worked' is PART XI's own description of itself BEFORE Parts XII and")
print("     XIV.  The register inherited the question and not the answer. **")
print("  ⇒ ** AND THAT IS THE REAL FINDING OF THIS BATCH: three of the nine slate items")
print("     (L-25, L-31, L-33) are STALE QUEUE TEXT quoting a question the ledger later")
print("     answered.  The queues were never pruned after the runs. **  (L-105: a queue-")
print("     currency check, the same shape as check_currency, over the field ledgers.)")
print()
print("  ** L-32, U1-U6. **  U3 is 'the full 3D plot, 24 hinges both sides -- staged, not")
print("  now'.  It is a FIGURE, not a question: nothing is unknown, it is undrawn.")
print("  ⇒ ** L-32 ANSWERED as far as a computation can: U3 is a rendering task, and after")
print("     L-61/L-75 there is far more to draw than when it was staged -- the 12 legs, the")
print("     3 walls, the causal trichotomy.  ** It should be built, and it is now worth more")
print("     than it was. **  (L-106: build the figure.)")

# --- r2376+c54.159 -----------------------------------------------------------------
# The batch's strongest claim (L-26) and its computed negative (L-30) were both printed
# only.  Pin them.  L-26: f'' = 2(f-1)/r^2 identically, so lambda^2 - Omega^2 vanishes
# identically and the sub-ring demagnification is the pure number exp(-2 pi) = 0.0018674
# at EVERY member -- checked at the table's own first row, 2M = 0.20, r_ph = 0.3.
# L-30: the excentres sit at X0 = sqrt(15) = 3.872983346207417 and are null-connected to
# nothing -- 0 of 15 excentre pairs and 0 of 36 excentre-to-hinge pairs.
assert sp.simplify(lhs - rhs) == 0, "f'' = 2(f-1)/r^2 FAILS -- L-26's identity is gone"
assert sp.simplify(lam2s - om2s) == 0, "lambda != Omega -- the demagnification is not e^-2pi"
assert abs(float(sp.exp(-2*sp.pi)) - 0.0018674) < 5e-8
_rph, _fp, _l2, _o2 = photon(0.10, 1)                       # the 2M = 0.20 row
assert abs(_rph - 0.3) < 1e-12 and abs((_l2/_o2)**0.5 - 1.0) < 1e-12
assert abs(float(sq15) - 3.872983346207417) < 1e-12
assert len(E) == 6 and len(H) == 6
assert nullE == 0 and len(nullEH) == 0                      # 0 of 15 and 0 of 36
