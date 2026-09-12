"""
P03_closure_under_the_three_vantage_reading
===========================================
WHAT IT ASKS.  P14R28 (P14_the_wall_is_a_wall_of_a_hinge) decided a fork about the
signed areal radius in favour of reading (ii): THREE radii, one per vantage, each
vanishing at its OWN wall and at neither of the other two, so a wall crossing branches
only the vantage that owns it and the monodromy is diagonal in the vantage basis.

Its decision table checked three things against the fork -- triality = -lambda mod 3,
the thirds and the three classes, and route-dependence -- and found all three
insensitive.  ** It did not check the composite ADMISSION RULE. **

P3 sec:winding states that rule in the form reading (i) supplies: "to close is to
return to the same branch, and admitting a composite exactly when its TOTAL fractional
part vanishes", i.e. sum_i n_i = 0 (mod 3) on the total crossing count.  Under (i) --
one radius, every crossing sending r -> omega r -- total crossings IS the sheet
advance and that rule is exactly "return to the same branch".

This asks whether the rule keeps that meaning under (ii).

WHAT WOULD FALSIFY THE HEADLINE.  If, under (ii), monodromy-triviality and
sum n = 0 (mod 3) picked out the same configurations, the rule would be
fork-insensitive like the other three entries and there would be nothing to report.
"""
import itertools

WALLS = ("A", "B", "C")          # the three walls = the three graze points = r_j = 0

def monodromy(mult, lam):
    """(ii): crossing wall W multiplies the OWNER's slot by omega^(-lambda).
    Returned as the triple of exponents of omega on the three vantage slots."""
    return tuple((-lam * mult[W]) % 3 for W in WALLS)

def trivial(mult, lam):
    return monodromy(mult, lam) == (0, 0, 0)

def total_crossings(mult):
    return sum(mult[W] for W in WALLS)

print("=" * 78)
print("PART 1 — THE TWO CONDITIONS, UNDER READING (ii)")
print("=" * 78)
print("  monodromy of a circuit crossing wall W with multiplicity m_W, on a mode of")
print("  index lambda:   diag( omega^(-lambda m_A), omega^(-lambda m_B), omega^(-lambda m_C) )")
print()
print("  IDENTITY  iff  lambda * m_W = 0 (mod 3)  for EVERY wall separately.")
print("  P3's rule iff  sum_W m_W = 0 (mod 3)     on the TOTAL only.")
print()

print("=" * 78)
print("PART 2 — DO THEY COINCIDE?  exhaustive over multiplicities 0..3 and lambda 1,2")
print("=" * 78)
sep = []
for lam in (1, 2):
    for mA, mB, mC in itertools.product(range(4), repeat=3):
        mult = dict(zip(WALLS, (mA, mB, mC)))
        n = total_crossings(mult)
        if n == 0:
            continue
        p3 = (n % 3 == 0)
        ii = trivial(mult, lam)
        if p3 != ii:
            sep.append((lam, (mA, mB, mC), n, p3, ii))
print(f"  configurations where P3's rule and (ii)-triviality DISAGREE: {len(sep)}")
for lam, m, n, p3, ii in sep[:6]:
    print(f"    lambda={lam}  m=(A:{m[0]},B:{m[1]},C:{m[2]})  total n={n}"
          f"   P3 admits={p3}   monodromy trivial={ii}")
print("    ...")
print()
print("  ** THE SMALLEST IS THE LAP ITSELF: m=(1,1,1), n=3. **")
m = dict(zip(WALLS, (1, 1, 1)))
for lam in (1, 2, 3):
    print(f"    one full lap, lambda={lam}:  total n=3 -> P3 admits=True ;"
          f"  monodromy={monodromy(m, lam)} -> trivial={trivial(m, lam)}")
print()
print("  This is P14R28's own headline read from the other side: 'under (ii) the lap")
print("  acts by omega^(-lambda), and only triality zero returns'.  The lap has")
print("  total crossing number 3, so P3's rule admits it for every lambda.")

print()
print("=" * 78)
print("PART 3 — WHICH WAY THE IMPLICATION RUNS")
print("=" * 78)
nec = suf = True
for lam in (1, 2):
    for mA, mB, mC in itertools.product(range(4), repeat=3):
        mult = dict(zip(WALLS, (mA, mB, mC)))
        if total_crossings(mult) == 0:
            continue
        if trivial(mult, lam) and (total_crossings(mult) % 3 != 0):
            nec = False
        if (total_crossings(mult) % 3 == 0) and not trivial(mult, lam):
            suf = False
print(f"  (ii)-triviality  ==>  sum n = 0 (mod 3)   :  {nec}   [P3's rule is NECESSARY]")
print(f"  sum n = 0 (mod 3) ==> (ii)-triviality     :  {suf}   [P3's rule is SUFFICIENT]")
print()
print("  So under (ii) P3's total-crossing rule is a NECESSARY condition for closure")
print("  and not a sufficient one: closure is per-wall, sum n = 0 is its shadow on the")
print("  total.  Under (i) the two coincide, because there is one branch to return to.")

print()
print("=" * 78)
print("PART 4 — IS THE ELEVEN-CHANNEL RESULT AFFECTED?")
print("=" * 78)
print("  The eleven are stated in constituent content (q, qbar), not in per-wall")
print("  multiplicities, so the test set does not resolve m_W and cannot see the")
print("  difference.  Both rules return the same verdict on it, as P3R47 showed for")
print("  the winding/triality pair.")
print("  ** So nothing in the tested result moves.  What moves is the STATEMENT of the")
print("  rule: 'total fractional part vanishes' is (i)'s form of a condition that is")
print("  per-wall under the reading the corpus adopted. **")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  P14R28's decision table checked triality, the thirds, the three classes and")
print("  route-dependence against the (i)/(ii) fork and found them insensitive.")
print("  The composite ADMISSION RULE is not on that table, and it is NOT insensitive:")
print("  under (ii) closure is per-wall (lambda m_W = 0 mod 3 for each W), of which")
print("  P3's sum_i n_i = 0 (mod 3) is a necessary consequence and not an equivalent.")
print()
print("  NOT CLAIMED: that P3's rule is wrong.  It is the correct rule under (i) and a")
print("  correct necessary condition under (ii); every configuration the corpus has")
print("  tested is admitted or refused identically by both.")
print("  NOT CLAIMED: that the fork should be reopened.  (ii) stands on the sentence")
print("  P14R28 used to decide it.")
print("  WHAT IS CLAIMED: one entry is missing from the decision table, and it is the")
print("  entry on which P3 sec:winding's own statement of the rule depends.")
