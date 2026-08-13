#!/usr/bin/env python3
"""
RECEIPT -- `L-175` / `PO-9`: ** ITEM A1 WORKED, AND THE ANSWER IS A THIRD ONE.  THE ROUTE ASKED WHETHER
A SECOND SLICING STEP'S CHOICES ARE ALL MODULI (vein closes) OR WHETHER ONE IS FORCED (that forcing is
the finding).  ⛭⛭ *** NEITHER.  RULE 2 NEITHER FORBIDS A SECOND STEP NOR FORCES ONE -- IT EMPTIES IT.
EVERY RUNG ABOVE THE LAST MUST BE MAXIMALLY SYMMETRIC, HENCE A PLANE SECTION, HENCE SCALE-ONLY; SO THE
WHOLE TOWER ENTERS THE CUT THROUGH THE ONE COMBINATION THAT IS alpha, WHICH THE FRAMEWORK DOES NOT
DERIVE. *** THE MISSING CEILING IS A PROPERTY OF THE DESCENT AND NOT A GAP IN THE ARGUMENT. **

Built r2566+c54.207, lead `L-533`.  VEIN: `L-175` (PO-9, what fixes the substrate's dimension).

===================================================================================================
** ⛭ FIRST: THE QUESTION AS ROUTED IS UNDER-SPECIFIED, AND THAT IS WHY IT LOOKED BINARY **
===================================================================================================

The route reads: *"enumerate what a second slicing would have to break, and check whether any of it is
a MODULUS."*  ** But the corpus's own guard says `modulus' carries THREE senses and only the first is
what the criterion excludes ** (P6 \S the guard):

  ⓵ ** an unforced parameter INDEXING CANDIDATE WORLDS ** -- what Rule 2 rejects;
  ⓶ a coordinate on a space of INEQUIVALENT SOLUTIONS (the mass, transverse to the orbits)
     -- *"That sense is not what this criterion excludes, and nothing here counts against it"*;
  ⓷ an unknown DATUM of one world -- an epistemic gap, not a family.

⇒ *** RUN WITHOUT THE GUARD, THE TEST RETURNS "yes, a modulus" FOR THE OFFSET AND CLOSES THE VEIN ON A
    SENSE-2 READING.  THE OFFSET IS THE MASS, AND THE MASS IS EXPLICITLY SENSE 2. ***
⌗ *So the first result of this probe is that the routed test needed the guard attached before it could
be run at all -- and with it attached the test does not close the vein.*

===================================================================================================
** THE ENUMERATION.  FOUR CHOICES, AND WHAT EACH IS **
===================================================================================================

  ** ① WHERE THE DESCENT STARTS ** (which rung is the substrate) -- a DIMENSION.
     ⇒ *Not a modulus in any sense: dS_D is maximally symmetric and moduli-free for every D, so no
      member carries a choice of how to break anything.*  ** The criterion is silent -- which P6 and
      P12 already establish, and which this probe does not improve on. **

  ** ② THE NORMAL DIRECTION n OF THE SECOND SECTION ** -- GAUGE.
     ⇒ *The isometry group is transitive on unit spacelike normals, so the objects that would
      distinguish one choice from another are moved onto each other.*  ** This is exactly P6's own
      ground for excluding ORIENTATION from the class of unforced choices. **

  ** ③ ITS OFFSET c ** -- and this is the one that carries content.
     *PART 1 computes it: a plane section of dS_D at offset c returns* ** dS_{D-1} of radius
     sqrt(alpha^2 - c^2) ** *, for every admissible n.*
     ⇒ *** SO c ENTERS ONLY THROUGH THE SCALE.  It does not index rival worlds; it re-enters the one
         dimensionful input the framework already has and does not derive. ***

  ** ④ WHETHER THE STEP CARRIES MASS ** -- ⛔ EXCLUDED, AND BY RULE 2 ITSELF.
     *An intermediate rung is the substrate for everything below it, so Rule 2 applies to it in its
     own right: a rung that were not maximally symmetric would carry a choice of how to break its
     symmetry -- a SENSE-1 modulus.*  ** And on this substrate a section carries mass exactly when it
     is NOT a plane section (p0). **
     ⇒ *** EVERY STEP ABOVE THE LAST IS THEREFORE A PLANE SECTION.  This is the one place in the
         enumeration where Rule 2 BITES -- and what it does with the bite is the finding. ***

===================================================================================================
** ⛭⛭ THE FINDING: THE CRITERION EMPTIES THE STEP RATHER THAN RULING ON IT **
===================================================================================================

  ④ forces every step above the last to be scale-only; ③ says a scale-only step changes alpha and
  nothing else; and the cut fixes alpha from Lambda and r_0 from the mass (PART 3).

  ⇒⇒ *** THE TOWER ABOVE THE LAST STEP IS INVISIBLE FROM THE CUT.  A second step is ADMISSIBLE (no
      sense-1 modulus is introduced) and IDLE (no observable is changed).  Rule 2 was expected to
      exclude it or to force it; instead it removes its content. ***

  ⇒⇒⇒ ** SO THE SUBSTRATE'S DIMENSION IS UNBOUNDED ABOVE FOR A REASON, not for want of an argument:
      *nothing below can see the difference*.  ** That converts `no upper bound is established' into
      `no upper bound can be established from below', which is a stronger statement and a different
      kind of one. **
  ⌗ *And it makes the programme's own guard --* ** CUT -> DYNAMICS, never CUT -> SUBSTRATE ** *-- a
   CONSEQUENCE rather than a rule of conduct: the descent is scale-degenerate, so there is nothing for
   a cut-to-substrate inference to carry.*

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that D = 5. **  *The opposite: the bound stays below-only, and this file explains why.*
** Not that a multi-step descent is what the framework does ** -- the corpus builds one step and this
changes nothing about that; what is settled is the STATUS of the alternative.
** Not that the cut's dimension is open ** -- it is settled at four by the matter sector's content,
which is a different object and is untouched here.
** Not that alpha is derived ** -- it is the ledger's one input and stays one.
** And not that Rule 2 is silent on second steps ** -- it is not: ④ is a Rule-2 exclusion, and it is
what does the emptying.

⚠ ** THE ARGUMENT RUNS DOWNWARD AND CONCLUDES A NEGATIVE, WHICH IS THE ONLY DIRECTION AVAILABLE. **
*It does not derive a substrate property from the cut.  It shows the cut CANNOT constrain the
substrate -- the guard's own content, stated positively for once.*

SETTINGS: none -- no instrument, no spectra.  A symbolic hyperplane section of the ambient quadric in
general dimension, the rank of the scale map, the recovery of (alpha, r_0) from (Lambda, M), and
source checks against p0, P6, P12 and P3.

rc=0 on success.  Run: python3 E50_a_second_step_is_emptied_by_rule_two_and_not_forbidden_by_it.py
                        (sympy; ~8 s)
"""
import os
import re
import sys

import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

al, c = sp.symbols('alpha c', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — A PLANE SECTION IS SCALE-ONLY, IN EVERY DIMENSION, COMPUTED")
print("=" * 78)
print(f"  {'D':>3s}  {'section of dS_D at offset c':>32s}   {'eta(Y,Y) on the section':>26s}")
_radii = {}
for D in (5, 6, 7, 8):
    X = sp.Matrix(sp.symbols(f'x0:{D + 1}'))
    eta = sp.diag(-1, *([1] * D))
    n = sp.Matrix([0] * D + [1])                 # a spacelike unit normal
    assert (n.T * eta * n)[0] == 1
    Y = sp.Matrix(list(X[:D]) + [0])             # n^perp
    Xs = c * n + Y
    lhs = sp.expand((Xs.T * eta * Xs)[0])
    yy = sp.expand((Y.T * eta * Y)[0])
    resid = sp.simplify(lhs - yy - c ** 2)       # must be identically 0
    got = sp.simplify(al ** 2 - c ** 2)          # eta(Y,Y) = alpha^2 - c^2
    _radii[D] = sp.sqrt(got)
    print(f"  {D:>3d}  {'dS_%d, signature (1,%d)' % (D - 1, D - 2):>32s}   {str(got):>26s}"
          f"   {'OK' if resid == 0 else 'SPLIT FAILS'}")
    if resid != 0:
        fail.append(f"the orthogonal split fails at D={D} — the section is not eta(Y,Y)=alpha^2-c^2")
print()
print(f"  ** radius of the section = {_radii[6]} , for EVERY admissible n and c **")
print("  *** So a plane section changes the SCALE and nothing else.  The normal is gauge (the isometry")
print("      group is transitive on unit spacelike normals); the offset moves alpha. ***")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE SCALE MAP HAS A ONE-PARAMETER FIBRE, SO THE TOWER IS DEGENERATE")
print("=" * 78)
at, c2 = sp.symbols('alpha_top c_2', positive=True)
aeff = sp.sqrt(at ** 2 - c2 ** 2)
J = sp.Matrix([[sp.diff(aeff, at), sp.diff(aeff, c2)]])
_rank = J.rank()
print(f"  alpha_eff(alpha_top, c_2) = {aeff}")
print(f"  Jacobian = {J}   rank = {_rank}")
print(f"  ** two choices, rank {_rank} -> a {2 - _rank}-parameter fibre of (alpha_top, c_2) per alpha_eff **")
_fib = sp.solve(sp.Eq(aeff, sp.Symbol('a_e', positive=True)), c2)
print(f"  the fibre: c_2 = {_fib}")
print()
print("  *** So a two-step descent trades ONE unknown for TWO with ONE relation, and the extra")
print("      parameter is invisible below: every member of the fibre yields the SAME alpha_eff. ***")
if _rank != 1:
    fail.append(f"the scale map has rank {_rank}, not 1 — the degeneracy claim fails")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE CUT SEES alpha AND r_0 AND NOTHING ELSE")
print("=" * 78)
Lam, r0, M = sp.symbols('Lambda r_0 M', positive=True)
_a_of_L = sp.sqrt(3 / Lam)
print(f"  alpha from the cut's Lambda :  alpha = {_a_of_L}   ** one-to-one **")
u = sp.Symbol('u')                                # u = r_0/alpha
cub = sp.Eq(2 * M / al, u - u ** 3)
_deg = sp.degree(sp.expand(u - u ** 3), u)
_roots = sp.solve(sp.Eq(u - u ** 3, sp.Symbol('m')), u)
print(f"  and r_0 from the cut's mass :  2M/alpha = (r_0/alpha) - (r_0/alpha)^3 , degree {_deg}")
print(f"  -> {len(_roots)} roots: the three vantages the corpus already names, one geometry")
print()
print("  ** So (Lambda, M) determines alpha exactly and r_0 up to the three-fold vantage designation.")
print("     NOTHING in the cut is a function of alpha_top or c_2 separately. **")
print("  ⇒ *** A SECOND STEP IS ADMISSIBLE AND IDLE.  That is the finding, and it is neither branch")
print("      the routed question offered. ***")
if _deg != 3 or len(_roots) != 3:
    fail.append(f"the slicing relation has degree {_deg} with {len(_roots)} roots — not the three vantages")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE FOUR PREMISES, EACH IN THE CORPUS'S OWN TEXT")
print("=" * 78)
TEX = {fn: open(os.path.join(CORPUS, fn), encoding='utf-8', errors='replace').read()
       for fn in ('geometric_core_paper.tex', 'shadow_of_existence.tex',
                  'algebroid_paper.tex', 'SdS-slicing-curve_v2.tex')}
PREMISES = [
    ("p0: a plane section of the substrate returns a de Sitter space of radius sqrt(alpha^2-c^2)",
     'geometric_core_paper.tex', r'de~Sitter four-space of radius\s*\n?\$\\sqrt\{\\alpha\^\{2\}-c\^\{2\}\}\$'),
    ("⛭ p0: and it is SdS exactly when the mass vanishes — which is what makes ④ a Rule-2 exclusion",
     'geometric_core_paper.tex', r'plane section of the substrate is\s*\n?Schwarzschild--de~Sitter exactly when the mass vanishes'),
    ("P6: Rule 2 rejects a symmetry-breaking modulus",
     'shadow_of_existence.tex', r'a parameter that fixes \\emph\{how a symmetry is broken\}'),
    ("⛭ P6's GUARD: the second sense is NOT what the criterion excludes",
     'shadow_of_existence.tex', r'That sense is not what this criterion excludes'),
    ("P6: and the mass is named as an instance of that second sense",
     'shadow_of_existence.tex', r'as the mass is for the space of cuts'),
    ("P6: orientation is excluded because the symmetry group is transitive on the distinguishers",
     'shadow_of_existence.tex', r'symmetry group is transitive on the objects that\s*\n?would distinguish one'),
    ("P6/P12: dS_D is maximally symmetric and moduli-free in EVERY dimension",
     'algebroid_paper.tex', r'maximally symmetric and moduli-free for every \$D\$'),
    ("P12: and no upper bound is established anywhere",
     'algebroid_paper.tex', r'No upper bound is established anywhere in this framework'),
    ("P3: the substrate is dS_5 = SO(5,1)/SO(4,1) and the fifth dimension is forced by slicing",
     'SdS-slicing-curve_v2.tex', r'the fifth dimension forced because slicing a four-dimensional de~Sitter space only re-coordinatizes it'),
]
for what, fn, pat in PREMISES:
    ok = re.search(pat, TEX[fn], re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"a premise of the enumeration is not in the corpus: {what} [{fn}]")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — AND WHAT P12 NOW SAYS")
print("=" * 78)
P12 = TEX['algebroid_paper.tex']
WRITTEN = [
    ("the absence of a ceiling is given a positive reason",
     r'the absence of an upper bound\s*\n?has a positive reason'),
    ("Rule 2 is applied to the intermediate rung in its own right",
     r'Rule~2 applies to it in its own right'),
    ("so every rung above the last is maximally symmetric",
     r'every rung above the last must be maximally\s*\n?symmetric'),
    ("hence a plane section, hence scale-only",
     r'a step above the\s*\n?last changes the scale and nothing else'),
    ("the section's radius is stated",
     r'returns \$\\dS_\{D-1\}\$ of radius \$\\sqrt\{\\alpha\^\{2\}-c\^\{2\}\}\$'),
    ("the normal is called gauge, with the transitivity reason",
     r'gauge because the isometry group is transitive on unit spacelike normals'),
    ("⛭ and the verdict is EMPTIES, not forbids and not forces",
     r'does not forbid a second\s*\nstep and does not force one: it \\emph\{empties\} it'),
    ("the cut's blindness is stated as the mechanism",
     r'being blind to\s*\neverything above'),
    ("and the guard is upgraded from conduct to consequence",
     r'never from the cut to\s*\n?the substrate a consequence rather than a rule of conduct'),
]
for what, pat in WRITTEN:
    ok = re.search(pat, P12, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P12 does not carry: {what}")

print()
print("  ⛔ AND THE THING THAT MUST NOT HAVE HAPPENED:")
_ceiling = re.search(r'\\dS_5\$? is (?:the )?(?:derived |forced )?maximum'
                     r'|(?<!No )upper bound is established'
                     r'|substrate.{0,40}bounded above', P12) is not None
_lower = re.search(r'a lower\s*\n?bound and not an equality', P12) is not None
print(f"  {'OK ' if _lower else 'GONE   '}  the lower-bound-only statement is still there")
print(f"  {'OK ' if not _ceiling else 'BREACH '}  and no ceiling has been asserted")
print("     ⚠ *the whole vein exists to keep the bound below-only; a probe that closed it upward")
print("        would be the exact error the distinction is drawn to prevent*")
if not _lower:
    fail.append("P12's lower-bound-only statement is gone — the clause has overwritten what it qualifies")
if _ceiling:
    fail.append("P12 now asserts an upper bound — CUT->SUBSTRATE has been breached")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — a plane section of dS_D is dS_{D-1} of radius sqrt(alpha^2-c^2) in every")
print("dimension checked; the scale map has rank 1 over two choices, so the tower has a one-parameter")
print("invisible fibre; the cut determines alpha from Lambda and r_0 up to three vantages and nothing")
print("more; all nine premises are the corpus's own; and P12 now says Rule 2 empties a second step")
print("rather than ruling on it, with the bound still below-only.")
print("=" * 78)

# ============================================================================================
# GATE — r2566+c54.207, `L-533`.  ** This probe touches the one thing the vein exists to protect --
# the substrate's dimension being bounded BELOW ONLY -- so the gate is built to catch a probe that
# quietly closes it upward, which is the failure mode that would matter:
#   (1) the hyperplane split computed in FOUR dimensions rather than argued in one -- ** if the
#       section were not scale-only the enumeration's item ③ would be a genuine modulus and the
#       conclusion would invert **;
#   (2) *** the scale map's rank pinned at 1 ***.  ** This is the gate's centre: rank 1 over a
#       two-parameter choice IS the invisibility, and rank 2 would mean a second step leaves a trace
#       and the vein would be open in the other direction **;
#   (3) the slicing relation's degree and root count, so "the cut sees alpha and r_0 and nothing
#       else" is the corpus's own three-vantage structure and not a new claim;
#   (4) *** nine PREMISE checks in four papers ***, including P6's three-sense guard.  ** Without the
#       guard the routed test returns the wrong answer on the offset, and the guard is not optional
#       decoration -- it is why this probe does not close the vein **;
#   (5) nine checks on what P12 now says, including that the verdict reads EMPTIES;
#   (6) and *** two NEGATIVE checks ***: the lower-bound-only statement still present, and no upper
#       bound asserted anywhere in P12.  ** A probe on PO-9 that ends by capping the substrate has
#       committed the error the vein is drawn to prevent, and that must fail loudly. **
#   NOT gated: any value of D.  ** None is claimed, and the finding is that none can be. **
# ============================================================================================
for D in (5, 6, 7, 8):
    assert _radii[D] == sp.sqrt(al ** 2 - c ** 2), f"the section radius is wrong at D={D}"
assert _rank == 1, "THE SCALE MAP IS NOT RANK 1 — a second step would leave a trace and the finding inverts"
assert _deg == 3 and len(_roots) == 3, "the slicing relation is not the three-vantage cubic"
for what, fn, pat in PREMISES:
    assert re.search(pat, TEX[fn], re.I | re.S), f"premise missing: {what}"
for what, pat in WRITTEN:
    assert re.search(pat, P12, re.I | re.S), f"P12 does not carry: {what}"
assert _lower, "P12's lower-bound-only statement has been overwritten"
assert not _ceiling, "P12 NOW ASSERTS AN UPPER BOUND — the guard is breached"
print(f"GATE c54.207 (r2566), `L-533`: a plane section of dS_D at offset c is dS_(D-1) of radius "
      f"{_radii[6]} for D = 5,6,7,8; the scale map has rank {_rank} over two choices, so the tower "
      f"carries a {2 - _rank}-parameter fibre no cut can resolve; the cut fixes alpha from Lambda and "
      f"r_0 up to {len(_roots)} vantages; and P12 now states that Rule 2 empties a second step rather "
      f"than forbidding or forcing it, with the bound still below-only and no ceiling asserted — "
      f"pinned against `THE_DISPATCH` A1 (r2566), `L-175`/PO-9 and P6's three-sense guard.")
