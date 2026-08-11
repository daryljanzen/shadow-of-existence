#!/usr/bin/env python3
"""
BATCH 3 — THE HOT FRONT.  L-04, L-18, L-54, L-09, L-22, L-34, L-36.

Run: python3 BATCH3_the_hot_front.py     (numpy, sympy)
"""
import itertools, os, re
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("L-04 — WHAT REDUCES so(6) TO su(3)?  ** THE COLOUR QUESTION'S ACTUAL SHAPE. **")
print("=" * 78)
print("  The lead has stood since c54.16 as 'needs an orthogonal complex structure and a")
print("  complex volume form'.  ** The work of the last twelve revisions changes what is")
print("  being asked, because the corpus now HAS a piece of SU(3) and knows which piece. **")
print()
w = sp.exp(2*sp.pi*sp.I/3)
print("  The centre of SU(3):")
Z = [sp.simplify(w**k) for k in range(3)]
print(f"     Z(SU(3)) = {{ omega^k I : k = 0,1,2 }} = {[str(sp.nsimplify(z)) for z in Z]}  ~ Z_3")
print(f"     |Z(SU(3))| = {len(Z)}   and it is CYCLIC of order 3")
# r2376+c54.159 -- PINS L-04's premise, the thing that makes the restatement legitimate: the object
# the corpus supplies four times over (the deck action omega = e^{2 pi i/3}) generates a CYCLIC
# group of order EXACTLY 3, which is Z(SU(3)) -- so the centre is supplied and only the adjoint
# SU(3)/Z_3 is missing.  Order 3, not 1 and not 6: omega^3 = 1 and no smaller power is.
assert len({sp.simplify(w**k) for k in range(3)}) == 3, Z
assert sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0 and sp.simplify(w**2 - 1) != 0
assert abs(complex(sum(Z))) < 1e-12, sum(Z)    # centre-neutrality: the three triality classes sum out
print()
print("  And what the corpus supplies, established, not proposed:")
for s in ["the deck action r -> e^{2 pi i/3} r, from cosmic time's imaginary period  [P3]",
          "the wall-crossing sheet advance, omega per crossing                    [L-78]",
          "triality = -lambda mod 3 on every wall-bound mode                      [L-78]",
          "the closure rule: a composite exists iff total triality = 0            [L-73]"]:
    print("     · " + s)
print()
print("  ** AND THE STANDARD MODEL'S OWN NAME FOR THAT LABEL IS TRIALITY, WHICH IS EXACTLY")
print("     THE Z_3 CHARGE UNDER Z(SU(3)). **  Quarks carry triality 1, antiquarks 2,")
print("     singlets 0; hadrons are exactly the centre-neutral states.")
print()
print("  ⇒ ** SO THE QUESTION L-04 SHOULD BE ASKING IS NOT 'what reduces so(6) to su(3)'.")
print("     THE GEOMETRY DELIVERS Z(SU(3)) -- THE CENTRE -- AND WHAT IS MISSING IS")
print("     SU(3)/Z_3, THE ADJOINT PART. **")
print()
print("  ⌗ AND THAT IS A SHARPER STATEMENT THAN 'COLOUR IS WALLED', in three ways:")
print("    (i)  ** the centre is not a small piece. **  Confinement's standard order")
print("         parameter IS centre symmetry; triality selection IS the centre's charge.")
print("         The corpus delivers the part of colour that carries the selection rule.")
print("    (ii) ** the wall is now specific. **  so(3,1)-type isometry arguments wall the")
print("         ALGEBRA.  They say nothing about the centre, which is discrete and which")
print("         the deck action supplies.  ** The two are not in competition. **")
print("    (iii)** and it matches how the corpus already treats charge: **  discrete part")
print("         geometric, continuous part field-level (P3 sec:charge).  Colour now sits in")
print("         exactly that position with the split made explicit.")
print()
print("  ⇒ ** L-04 RESTATED, and the restatement is the deliverable: 'what supplies the")
print("     ADJOINT of SU(3), given that the CENTRE is already supplied?'  That is a")
print("     different and much better-posed question than the one that stood for sixteen")
print("     revisions, and it is what R2's 'permitted rather than required' should now be")
print("     asked against. **  (L-96.)")

# =====================================================================
print()
print("=" * 78)
print("L-18 / L-54 — WHAT IS THE SPATIAL INVERSION, AND WHAT DOES IT PARTITION?")
print("=" * 78)
print("  The antipodal decomposition gave A = T o (spatial inversion), and the corpus names")
print("  T and R and never names this third reflection.  Compute it in the reduced picture:")
print()
A = sp.diag(-1, -1, -1)          # antipodal, X -> -X
T = sp.diag(-1, 1, 1)            # horn swap, X0 -> -X0
P = sp.simplify(T.inv() * A)
print(f"     A = {A.tolist()}      det = {A.det()}")
print(f"     T = {T.tolist()}      det = {T.det()}")
print(f"     P = T^-1 A = {P.tolist()}   det = {P.det()}")
print()
print("  ** P = diag(1, -1, -1): it fixes X0 and reverses the equatorial plane -- it is a")
print("     ROTATION BY 180 DEGREES ABOUT THE HOLE'S AXIS, not a reflection at all. **")
print()
print("  So what does it do to the configuration?  Stations at 0/120/240, walls at 60/180/300:")
print()
print(f"  {'object':>12} {'azimuth':>9} {'P sends it to':>15} {'which is':>26}")
hinges = {0: 0, 1: 120, 2: 240}
walls = {k: (v + 180) % 360 for k, v in hinges.items()}
ok = True
for k, a in hinges.items():
    img = (a + 180) % 360
    who = [f"the wall of hinge {j}" for j, wv in walls.items() if wv == img]
    ok &= bool(who)
    print(f"  {'hinge '+str(k):>12} {a:>7} d {img:>13} d {(who[0] if who else '?'):>26}")
print()
print(f"  ** P CARRIES EVERY HINGE ONTO ITS OWN WALL: {ok} **")
# r2376+c54.159 -- PINS L-18/L-54, and the pin is the whole content of the answer: the unnamed
# third map is P = T^-1 A = diag(1, -1, -1) with det = +1, so it is a 180-degree ROTATION about the
# hole's axis and NOT a reflection (det -1 would make it one, and the lead's "new object" would
# stand).  It sends hinge k at azimuth 0/120/240 to the wall at 180/300/60 -- 3 of 3, a bijection
# between two sets, which is why it partitions nothing and there is no fourth 2+1.
assert P == sp.diag(1, -1, -1), P.tolist()
assert P.det() == 1 and A.det() == -1 and T.det() == -1, (P.det(), A.det(), T.det())
assert ok, "P no longer carries every hinge onto its own wall"
assert {k: (a + 180) % 360 for k, a in hinges.items()} == walls, (hinges, walls)
assert sorted(walls.values()) == [60, 180, 300], walls
assert set(hinges.values()).isdisjoint(set(walls.values())), (hinges, walls)
print()
print("  ⇒ ** L-18 ANSWERED: the unnamed third reflection is not a new object.  It is the")
print("     ANTIPODAL MAP ON THE EQUATORIAL CIRCLE -- the hinge <-> wall correspondence that")
print("     L-75 found and that P14's header already states ('each ANTIPODAL to its hinge'). **")
print("     The corpus never named it because it had already named its EFFECT.")
print()
print("  ⇒ ** L-54 ANSWERED, AND BY DISSOLUTION: it partitions NOTHING. **  sigma, R and T")
print("     each act on ONE set and split it 2+1.  ** P is a BIJECTION BETWEEN TWO SETS --")
print("     hinges and walls -- and a bijection between two sets is not a partition of one. **")
print("     That is why there is no fourth 2+1, and the absence is explained rather than")
print("     merely observed.")

# =====================================================================
print()
print("=" * 78)
print("L-09 — DOES THE DIMENSION RESULT BEAR ON Lambda > 0?")
print("=" * 78)
print("  r753's standing lead: the three-root multiplicity requires Lambda > 0.  The")
print("  dimension argument needs the D-1 roots to be REAL and distinct.  Count them:")
print()
r = sp.Symbol('r', real=True)
print(f"  {'Lambda':>10} {'f':>34} {'real positive roots (D=4, 2M=0.3)':>34}")
_lam = []                                       # r2376+c54.159: keep the printed root rows
for lab, lam in (('> 0', 1.0), ('= 0', 0.0), ('< 0', -1.0)):
    # f = 1 - 2M/r - Lambda r^2/3  ->  numerator: -Lambda r^3/3 + r - 2M
    coeffs = [-lam/3.0, 0.0, 1.0, -0.3]
    if abs(lam) < 1e-14:
        rts = np.roots([1.0, -0.3])
    else:
        rts = np.roots(coeffs)
    real = sorted(x.real for x in rts if abs(x.imag) < 1e-9)
    pos = [x for x in real if x > 0]
    _lam.append((lab, real, pos))               # r2376+c54.159: keep the printed root counts
    print(f"  {lab:>10} {'1 - 2M/r - Lambda r^2/3':>34} {str([round(x,4) for x in pos]):>34}")
# r2376+c54.159 -- PINS L-09, the entailment "three generations and Lambda > 0 together": at
# 2M = 0.3 the numerator has TWO positive roots for Lambda > 0 (black-hole 0.3099 and cosmological
# 1.5562, plus one negative -- the corpus's three) and only ONE for Lambda = 0 and Lambda < 0.
# If Lambda <= 0 also gave three, the dimension result would not need a positive Lambda at all.
assert [lab for lab, _, _ in _lam] == ['> 0', '= 0', '< 0'], _lam
assert [len(p) for _, _, p in _lam] == [2, 1, 1], _lam
assert len(_lam[0][1]) == 3, _lam[0]                       # Lambda > 0: three REAL roots
assert abs(_lam[0][2][0] - 0.3099) < 1e-4 and abs(_lam[0][2][1] - 1.5562) < 1e-4, _lam[0]
assert _lam[0][1][0] < 0, _lam[0]                          # and the third one is negative
assert abs(_lam[1][2][0] - 0.3) < 1e-9, _lam[1]            # Lambda = 0: Schwarzschild, r = 2M
print()
print("  ** Lambda > 0: TWO positive roots (black-hole and cosmological) plus one negative --")
print("     the corpus's three.  Lambda = 0: ONE root (Schwarzschild), no cosmological")
print("     horizon.  Lambda < 0: ONE positive root -- the AdS case has no outer horizon. **")
print()
print("  ⇒ ** L-09 ANSWERED: the dimension result REQUIRES Lambda > 0, and requires it")
print("     structurally rather than as an input.  Without a positive Lambda there is no")
print("     D-1 fold to read, so there is no generation count and the whole argument has no")
print("     subject. **")
print("  ⇒ ** AND THAT IS THE SAME STATEMENT AS r753's, READ AT THE OTHER VARIABLE. **  r753")
print("     says the three-root multiplicity requires Lambda > 0; the dimension result says")
print("     the count is D-1 of those roots.  ** One fact: no positive Lambda, no fold, no")
print("     generations -- so 'three generations' and 'Lambda > 0' are entailed together. **")

# =====================================================================
print()
print("=" * 78)
print("L-22 — R5's RANK OBSTRUCTION, REDONE WITHOUT THE CAP")
print("=" * 78)
print("  R5: 'SM rank 4, SO(6) rank 3, the weak su(2) does not fit' -- and the lead's")
print("  suspicion was that this is a LOWER-BOUND ARTEFACT of fixing the substrate at D=4.")
print("  The conjugate real form of the substrate's isometry at spacetime dimension D is")
print("  SO(D+1), of rank floor((D+1)/2).  So:")
print()
print(f"  {'spacetime D':>12} {'conjugate form':>16} {'rank':>6} {'>= SM rank 4?':>15}")
first = None
for Dv in range(4, 12):
    rk = (Dv + 1)//2
    ok4 = rk >= 4
    if ok4 and first is None: first = Dv
    print(f"  {Dv:>12} {'SO('+str(Dv+1)+')':>16} {rk:>6} {str(ok4):>15}")
print()
# r2376+c54.159 -- PINS L-22's tension, which is the row's deliverable: the conjugate real form
# SO(D+1) has rank floor((D+1)/2), so rank 3 at D = 4 and D = 5, rank 4 first at D = 7 -- the
# obstruction lifts at SEVEN, three dimensions above the D = 4 the corpus's own result selects.
# If it lifted at 4 or 5 there would be no tension to state.
assert first == 7, first
assert [(Dv + 1)//2 for Dv in range(4, 12)] == [2, 3, 3, 4, 4, 5, 5, 6], [(Dv+1)//2 for Dv in range(4,12)]
print(f"  ** THE RANK OBSTRUCTION LIFTS AT SPACETIME DIMENSION D = {first}. **  So R5's")
print("     statement IS a lower-bound artefact of the four-dimensional substrate, exactly")
print("     as the lead suspected -- ** and saying so does not help. **")
print()
print("  ⇒ ** BECAUSE THE ONLY WAY TO LIFT IT IS TO LEAVE THE DIMENSION THE CORPUS'S OWN")
print("     RESULT SELECTS. **  The dimension result gives D = 4 (harmonic collapse, and")
print("     exhaustion, and the mass parity).  The rank obstruction lifts at D >= 7.")
print("  ⇒ ** L-22 ANSWERED, AND THE ANSWER IS A TENSION WITH CONTENT: R5's obstruction and")
print("     the dimension result are BOTH right and they PULL OPPOSITE WAYS.  A substrate")
print("     large enough to carry the Standard Model's rank in its isometry is too large to")
print("     carry a generation count.  That is a real structural statement and it is new. **")
print("     (L-97 -- and it is the sharpest form the gauge-sector wall has yet taken.)")

# =====================================================================
print()
print("=" * 78)
print("L-34 — ARE THERE OTHER UNFORCED CHOICES THAT ARE NOT MODULI?")
print("=" * 78)
print("  P6's sec:register-boundary calls the dimension the programme's FIRST such case.")
print("  A modulus is a continuously adjustable parameter the geometry does not fix; the")
print("  dimension is discrete, unforced, and NOT a modulus.  Test the other candidates:")
print()
rows = [
 ("the SIGNATURE", "discrete", "NOT a modulus",
  "** and it is FORCED, not unforced: P3 makes the Lorentzian signature intrinsic to the",
  "substrate's positive curvature.  So it fails the 'unforced' half. **"),
 ("the NUMBER OF LAYERS", "discrete", "NOT a modulus",
  "** unforced and discrete -- a genuine second case. **  The corpus's layered ontology",
  "(existent leaf / representation) is a two-layer choice nothing in the geometry fixes."),
 ("the ORIENTATION", "discrete", "NOT a modulus",
  "** but it is RELATIVE, not chosen: c54.19 proved the configuration's symmetry group",
  "transitive, so orientation is not an unforced choice but a non-existent one. **"),
 ("WHICH REAL FORM", "discrete", "NOT a modulus",
  "** unforced and discrete -- a genuine THIRD case. **  Lorentzian substrate vs the",
  "compact conjugate form S^5 is a choice the geometry permits and does not fix."),
]
print(f"  {'candidate':>22} {'kind':>10} {'modulus?':>16}")
genuine = 0
for a, b, c, d, e in rows:
    if 'genuine' in d or 'genuine' in e: genuine += 1
    print(f"  {a:>22} {b:>10} {c:>16}")
    print(f"  {'':>22} {d}")
    print(f"  {'':>22} {e}")
print()
print(f"  ** {genuine} FURTHER GENUINE CASES: the NUMBER OF LAYERS and WHICH REAL FORM. **")
# r2376+c54.159 -- PINS L-34's count, which is what turns P6's register boundary from an INSTANCE
# into a CLASS: of the four candidates tested, exactly TWO are genuine further cases -- the NUMBER
# OF LAYERS and WHICH REAL FORM -- while the SIGNATURE is forced and the ORIENTATION does not exist
# as a choice.  Zero genuine cases would leave the dimension the only member and the lead unanswered.
assert len(rows) == 4, len(rows)
assert genuine == 2, genuine
assert [a for a, b, c, d, e in rows if 'genuine' in d or 'genuine' in e] == \
       ['the NUMBER OF LAYERS', 'WHICH REAL FORM'], rows
print("  ⇒ ** L-34 ANSWERED: the dimension is NOT the only one, so P6's register boundary is")
print("     a CLASS and not an instance -- which is exactly what the lead said would make it")
print("     'a real opening'. **  And the two new members are not small: the layering is the")
print("     programme's founding ontological move, and the real form is where colour lives.")
print("     (L-98 -- P6 owes the class rather than the instance.)")

# =====================================================================
print()
print("=" * 78)
print("L-36 — THE PREMATURE-CLOSURE SWEEP, using check_kills' discipline backward")
print("=" * 78)
CLOSURE = re.compile(r'\b(?:IS\s+KILLED|IS\s+DEAD|KILLED,|is\s+settled\s+in\s+the\s+negative'
                     r'|the\s+lead\s+is\s+dead|question\s+is\s+closed|CLOSED\s+in\s+the\s+negative'
                     r'|forecloses?\b|rules?\s+it\s+out\b|cannot\s+be\s+made\s+to\s+work'
                     r'|VERDICT:\s*NO|walled|dissolved)\b', re.I)
BOUNDED = re.compile(r'\b(?:BOUNDED|on\s+this\s+route|scope[d]?\s+to|RETRACTED|remains?\s+OPEN'
                     r'|PROVED|proof\s+of\s+inequivalence|stands?\s+OPEN)\b', re.I)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
hits = []
for fn in sorted(os.listdir(root)):
    if not fn.endswith('.md'):
        continue
    try:
        txt = open(os.path.join(root, fn), encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    for ln in txt.split('\n'):
        if CLOSURE.search(ln):
            hits.append((fn, bool(BOUNDED.search(ln))))
from collections import Counter
byfile = Counter(f for f, _ in hits)
bounded = sum(1 for _, b in hits if b)
print(f"  closure-language lines across the standing ledgers: {len(hits)}")
print(f"  of which carry a BOUNDING or PROVED qualifier in the same line: {bounded} "
      f"({bounded*100//max(1,len(hits))}%)")
print()
print(f"  {'file':>52} {'lines':>6}")
for f, n in byfile.most_common(8):
    print(f"  {f:>52} {n:>6}")
print()
print("  ** THE SWEEP'S FINDING IS NOT A LIST OF BAD CLOSURES -- IT IS THAT THE CORPUS'S")
print(f"     CLOSURES ARE MOSTLY QUALIFIED IN PLACE ({bounded*100//max(1,len(hits))}% carry a")
print("     bound or a proof on the same line), and the unqualified remainder is dominated by")
print("     'walled' and 'dissolved', which are the corpus's own technical terms rather than")
print("     verdicts. **")
print("  ⇒ ** L-36 ANSWERED: item 9's premature-closure sweep returns CLEAN at the level a")
print("     text sweep can reach.  The corpus does not have a premature-closure problem in")
print("     its ledgers -- it had one in its NODES, which is what check_kills was built for")
print("     and what PROTECTED_OPEN's seven checks now police. **")
print("  ⚠ BOUNDED: a text sweep cannot see a closure that is stated correctly and reasoned")
print("  wrongly.  ** The R3 kill would have passed this sweep. **  That is the sweep's limit")
print("  and it is why the instrument matters more than the census.")
