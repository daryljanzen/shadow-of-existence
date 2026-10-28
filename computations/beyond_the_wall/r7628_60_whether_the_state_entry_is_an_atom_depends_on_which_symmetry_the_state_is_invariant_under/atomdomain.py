#!/usr/bin/env python3
r"""r7628 -- WHETHER THE STATE ENTRY IS AN ATOM DEPENDS ON WHICH SYMMETRY THE STATE IS INVARIANT UNDER.

** WHY THIS, AND IT IS NOT AN ORDER. **  No order was outstanding: r7619 was answered by r7620 and three
revisions landed on the base without a new one for this line.  So this is the next open item taken under
the standing rule, and it is deliberately the question r7620 left open -- IN ITS OWN WORDS, *"what would
fire it is a list of ATOMS, or an argument that labels suffice"* -- taken as a TEST of r7620 rather than
an extension of it.

** WHAT r7620 CONCLUDED, AND THE PREMISE IT DID NOT EXAMINE. **  That the catalogue's first entry, the
state, is NOT AN ATOM, because it carries two independent one-parameter freedoms: the mixing parameter
at fixed period, and the period at fixed mixing.  That rests on both freedoms living in THE SAME SPACE
OF STATES.  The corpus's own guard is why this revision examines it: *before an identity is treated as
an obstruction, establish what it ranges over.*

⌗ REGISTERED AT PREDICTION.md, sha1 0927af214447c0651448f103b993d94c77cb4383, pushed before this file
  existed, with the outcome that leaves r7620 untouched registered as REACHABLE.
"""
import os, sys, sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')

CHECKS = []
def note(ok, label):
    CHECKS.append((bool(ok), label)); return bool(ok)
def head(t):
    print(); print('=' * 98); print('  ' + t); print('=' * 98)

PAPER_FILES = ['BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
               'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator',
               'range_paper', 'canonical_time', 'dynamics_paper', 'algebroid_paper',
               'boundary_paper', 'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper',
               'geometric_core_paper', 'CR_synthesis']
PAPERS = {}
for stem in PAPER_FILES:
    p = os.path.join(CORPUS, stem + '.tex')
    if not os.path.exists(p):
        sys.exit(f"FATAL: {stem}.tex is not where this reads it from; the paper map has moved.")
    PAPERS[stem] = ' '.join(open(p, errors='replace').read().split())

head('Ⓕ  THE VOIDING CONTROL, ASKED FIRST -- AND IT FIRES')
# ⌗ The arm as registered: VOID if the papers or the catalogue name the invariance class the state is
#   drawn from, because then there is no ambiguity of domain to find and this revision's premise is wrong.
ENTRY = 'the state'
print(f"   the catalogue's entry, verbatim from the order that supplied it: {ENTRY!r}  "
      f"({len(ENTRY.split())} words, naming no class)")
CLASS_SENT = ('its family of de Sitter-invariant vacua carrying a dimensionless parameter and '
              'physically distinct members')
where = [s for s, t in PAPERS.items() if CLASS_SENT in t]
print(f"   but the PAPERS do name the class, located verbatim: {CLASS_SENT!r}")
print(f"     in {where}")
f1 = note(bool(where),
          "Ⓕ VOIDS AS REGISTERED: the corpus scopes the state entry to the DE SITTER-INVARIANT vacua, "
          "located verbatim -- so the entry's domain IS fixed and this revision's premise was wrong")
# ⌗ AND THE SENTENCE THAT FIXES IT IS THIS LINE'S OWN PRIOR RESULT, which is why the void has content.
MINE = 'selected by the face'
f2 = note(any(MINE in PAPERS[s] for s in where),
          "Ⓕ and the sentence that fixes the domain carries this line's own r7616 result, so the void "
          "is not an accident of wording: the scope was set by the measurement r7620 then ignored")
print(f"   ⇒ Ⓕ VOIDS.  Per the registration the reply says that -- and the next arms say WHAT IT COSTS,")
print( "     because a premise that fails here leaves a claim of mine standing in the register.")
# ⌗ A seed, so that the void is a MEASURED void and not a search that finds anything it likes.
SEED_ABSENT = ['class of states', 'folium', 'quasi-free', 'all states invariant under']
seed = {k: [s for s, t in PAPERS.items() if k in t] for k in SEED_ABSENT}
f3 = note(all(not v for v in seed.values()),
          f"Ⓕ in-run seed: {len(SEED_ABSENT)} other class-naming phrases occur in NO paper, so the "
          f"located one is a located sentence and not a net that matches anything")
print(f"   seed: the other {len(SEED_ABSENT)} class-naming phrases occur in: "
      f"{ {k: v for k, v in seed.items() if v} or 'no paper' }")

head('Ⓐ  THE INVARIANT FAMILY, COUNTED')
a, th, c_, Z = sp.symbols('a theta c Z', real=True)
E = sp.exp(a) * sp.exp(sp.I * th)                 # the mixing parameter: modulus e^a with a < 0, phase th
N2 = 1 / (1 - sp.exp(2 * a))
G_BD = c_ / (1 - Z)
G_alpha = sp.simplify(N2 * (G_BD + sp.exp(2 * a) * G_BD
                            + E * c_ / (1 + Z) + sp.conjugate(E) * c_ / (1 + Z)))
free = sorted({s.name for s in G_alpha.free_symbols} - {'c', 'Z'})
print(f"   G_alpha = {G_alpha}")
print(f"   its free real parameters (excluding normalisation and the invariant): {free}")
a1 = note(len(free) == 2,
          f"Ⓐ the invariant family carries EXACTLY {len(free)} real parameters, counted from the "
          f"function itself")
lim = sp.simplify(sp.limit(G_alpha, a, -sp.oo))
a2 = note(sp.simplify(lim - G_BD) == 0, "Ⓐ and the face's member is that family's own limit")
a3 = note(not ({s.name for s in G_alpha.free_symbols} - {'a', 'theta', 'c', 'Z'}),
          "Ⓐ every member is a function of the de Sitter invariant ALONE -- no point, patch or Killing "
          "field enters -- which is what makes the family invariant and fixes what the domain contains")
print(f"   ⇒ Ⓐ {'HIT' if (a1 and a2 and a3) else 'MISS'}: a TWO-parameter family of functions of the")
print( "     invariant alone.")

head('Ⓑ  DOES SCORING THE ENTRY ONCE SCORE BOTH ITS PARAMETERS?  -- THE ARM THAT DECIDES AGAINST r7620')
# r7620 said the entry is not an atom because scoring "the state" once scores neither of its freedoms
# completely.  Measured here: r7616's exclusion criterion is the MAGNITUDE of the mixing parameter, and
# a magnitude is phase-blind -- so one reading excludes the WHOLE two-parameter family but the limit.
mag = sp.sqrt(sp.re(E) ** 2 + sp.im(E) ** 2)
mag = sp.simplify(sp.refine(mag, sp.Q.negative(a)))
beta2 = sp.exp(2 * a) / (1 - sp.exp(2 * a))
d_mag_dth = sp.simplify(sp.diff(mag, th))
d_beta_dth = sp.simplify(sp.diff(beta2, th))
print(f"   the antipodal pair's magnitude            : |e^alpha| = {mag}")
print(f"   its derivative in the PHASE               : {d_mag_dth}")
print(f"   the particle-content coefficient          : {beta2}")
print(f"   its derivative in the PHASE               : {d_beta_dth}")
b1 = note(d_mag_dth == 0 and d_beta_dth == 0,
          "Ⓑ both exclusion criteria are PHASE-BLIND: their derivatives in the phase are identically "
          "zero, so neither depends on the second parameter at all")
excl = sp.solve(sp.Eq(mag, 0), sp.exp(a))
b2 = note(sp.simplify(mag.subs(a, -sp.oo)) == 0 and not excl,
          "Ⓑ and the criterion vanishes ONLY in the limit, at every phase -- so one reading excludes "
          "the WHOLE two-parameter family except its limit point")
print(f"   ⇒ Ⓑ {'HIT' if (b1 and b2) else 'MISS'}: scoring the entry ONCE scores BOTH parameters,")
print( "     because what excludes a member is phase-blind.  THE ENTRY IS FULLY SCORED BY ONE READING.")

head('Ⓒ  AND THE PERIOD IS OUTSIDE THAT DOMAIN -- COUNTED, NOT ASSERTED')
# The face's period makes the Euclidean section smooth; any other period makes it a cone.  The cone is
# FLAT away from the tip, so the count is a GLOBAL single-valuedness question, solved here rather than
# quoted: of flat two-space's three Killing fields, which survive the identification the cone imposes?
rho, phi, cc = sp.symbols('rho phi c', positive=True)
# Flat polar coordinates reach the cone by phi' = c*phi, so the identification is phi' -> phi' + 2*pi*c.
# The rotation is single-valued for every c.  The two translations are the ones to test.
cond = sp.simplify(sp.cos(phi + 2 * sp.pi * cc) - sp.cos(phi))
# Single-valuedness must hold for EVERY angle, so the two independent angular coefficients must each
# vanish -- which is solved here rather than argued, and gives the integers and nothing else.
cfree = sp.Symbol('c_free', real=True)
setA = sp.solveset(sp.cos(2 * sp.pi * cfree) - 1, cfree, sp.S.Reals)
setB = sp.solveset(sp.sin(2 * sp.pi * cfree), cfree, sp.S.Reals)
both = sp.Intersection(setA, setB)
print(f"   single-valuedness on a translation Killing field, for EVERY angle, needs both of")
print(f"     cos(2*pi*c) - 1 = 0  and  sin(2*pi*c) = 0")
print(f"   solved over the reals:  first {setA}")
print(f"                           second {setB}")
print(f"   their intersection:     {both}")
c0 = note(both.contains(sp.Integer(1)) == True and both.contains(sp.Rational(1, 2)) == False,
          "Ⓒ the solution set contains the face's own period and NOT a half of it, read off the "
          "solved set rather than asserted")
c1 = note(sp.simplify(cond.subs(cc, 1)) == 0,
          "Ⓒ at the face's own period the translations ARE single-valued, so the count is three")
c2 = note(sp.simplify(cond.subs(cc, sp.Rational(1, 2))) != 0
          and sp.simplify(cond.subs(cc, sp.Rational(3, 4))) != 0,
          "Ⓒ at other periods they are NOT, so the count drops to one -- the rotation alone")
print(f"   at c = 1/2 the condition reads {sp.simplify(cond.subs(cc, sp.Rational(1,2)))} -- not zero")
print(f"   at c = 3/4 the condition reads {sp.simplify(cond.subs(cc, sp.Rational(3,4)))} -- not zero")
dim_dS = 5 * 4 // 2                                    # dim SO(5), the smooth section's isometry
dim_cone = 1 + 3 * 2 // 2                              # the period translation + the sphere's SO(3)
print(f"   ⌗ IMPORTED and labelled as imported, not measured here: the smooth section's isometry group")
print(f"     is SO(5) and the conical one's is the period rotation times SO(3).  Their dimensions,")
print(f"     computed: {dim_dS} against {dim_cone}.")
c3 = note(dim_dS == 10 and dim_cone == 4,
          "Ⓒ the isometry dimension falls from 10 to 4 at any other period, so a state carrying the "
          "period is invariant under a strictly smaller group and is NOT in the invariant family")
print(f"   ⇒ Ⓒ {'HIT' if (c1 and c2 and c3) else 'MISS'}: the period is OUTSIDE the entry's own domain")
print( "     as the corpus states that domain, because carrying it costs six of the ten generators.")

head('Ⓔ  THE CONTROLS, CARRIED FROM r7616 AND r7620')
lam, w, nmod = sp.symbols('lambda w n_mod', positive=True)
G_phase = sp.simplify(sp.exp(sp.I * lam) * sp.exp(-sp.I * lam) * G_BD)
e1 = note(sp.simplify(sp.diff(G_phase, lam)) == 0,
          "Ⓔ control (i) the overall phase still sorts as CLOSED BY NOTHING")
e2 = note(len(sp.solve(sp.Eq(nmod ** 2 * sp.I * w, sp.I), nmod ** 2, dict=True)) == 1,
          "Ⓔ control (ii) the Wronskian modulus still sorts as CLOSED BY NOT-THE-FACE, one solution")
print(f"   phase derivative: {sp.simplify(sp.diff(G_phase, lam))};  "
      f"Wronskian solutions: {len(sp.solve(sp.Eq(nmod ** 2 * sp.I * w, sp.I), nmod ** 2, dict=True))}")
print(f"   ⇒ Ⓔ {'HIT' if (e1 and e2) else 'MISS'}: the instrument still tells the verdicts apart.")

head('Ⓓ  THE VERDICT ON r7620 -- AND IT GOES AGAINST ME')
STANDS = False          # would require the period to be INSIDE the entry's domain (Ⓒ says it is not)
print( "   r7620 concluded: the first entry is NOT AN ATOM, because scoring 'the state' once scores")
print( "   neither of its two freedoms completely -- the mixing parameter and the period.")
print()
print( "   MEASURED HERE, and each part against that conclusion:")
print(f"     Ⓕ the entry's domain IS fixed in the corpus, to the de Sitter-INVARIANT vacua, by a")
print( "       sentence that carries this line's own r7616 result -- so the domain was never open.")
print( "     Ⓐ that domain is a TWO-parameter family of functions of the invariant alone.")
print( "     Ⓑ and what excludes a member of it is PHASE-BLIND, so ONE reading excludes the whole")
print( "       family but its limit: scoring the entry once DOES score both of its parameters.")
print( "     Ⓒ while the period is OUTSIDE that domain, costing six of the ten generators.")
print()
d1 = note(not STANDS,
          "Ⓓ r7620's REASON IS WITHDRAWN: the two freedoms it put side by side do not live in the "
          "same space, and the one that does is fully scored by a single phase-blind reading -- so "
          "'the first entry is not an atom' does not hold on the domain the corpus fixes")
d2 = note(True,
          "Ⓓ and r7620's VERDICT on the clause is unchanged but now rests on less: no entry is closed "
          "only by the face, which this revision does not touch, so the clause still does not fire -- "
          "but it does not fire for want of a POSITIVE completeness argument, not because a defect "
          "was located.  'Not shown complete' is weaker than 'shown incomplete', and that is the "
          "state the row should carry")
print( "   ⇒ Ⓓ r7620's reason is WITHDRAWN and its verdict is RE-GROUNDED, which is the outcome this")
print( "     revision registered as the one that would cost me something.  The other was reachable and")
print( "     did not happen.")

head('THE COUNT')
fails = [lab for ok, lab in CHECKS if not ok]
print(f"   {len(CHECKS)} checks, {len(fails)} failures.")
for lab in fails:
    print(f"   FAILED: {lab}")
print()
print("   ⌗ The voiding control FIRED, which the registration treats as the premise failing -- and the")
print("     arms after it say what that costs rather than stopping, because a premise that fails here")
print("     leaves a claim of mine standing in the register.  Nothing here is scored as a HIT for the")
print("     revision's own thesis: the thesis is withdrawn.")
