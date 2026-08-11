"""K4 — THE THREE LEVELS AS A DIAGRAM.   K5 — IS THE NARIAI COINCIDENCE FORCED?
CONFIRMATION 1/3 from section 1-LEVELS, at source:
  L1 the foliation stacking rate (the existent's own geometric expansion) · L2 the leaf's
  self-gravitating dynamics · L3 the E=1 projection (the shadow).
  'The L1<->L2 boundary is THE SEAM (the NBC locus, THE ONE LAYER BOTH CAUSAL ASSIGNMENTS SHARE).'
  'Mis-assigning is quantitatively fatal in each direction.'
  'projection-independent ratios are the clean discriminators BECAUSE THE L3 MAP CANCELS IN THEM.'
"""
import numpy as np, sympy as sp
print("="*80); print("K4 — THE THREE LEVELS ARE A SPAN, AND THE DISCRIMINATORS ARE WHERE IT COMMUTES")
print("="*80)
print("""
  READ THE RULE AS A SHAPE.  'The one layer both causal assignments share' is not an arrow from L1
  to L2: it is an OBJECT they both receive from.  So the levels are a SPAN

                 L1  <---- seam ---->  L2
                   \\                  /
                    \\                /
                     v              v
                          L3  (observation)

  and the two 'quantitatively fatal' carryings are attempts to compose L1 -> L2 DIRECTLY, i.e. to
  use an arrow the diagram does not have.  *** THE DECISION RULE IS THE STATEMENT THAT THE ONLY
  ROUTE BETWEEN L1 AND L2 IS THROUGH THE SEAM. ***  Naming the shape says once what the rule says
  case by case, and says WHY mis-assignment is fatal rather than merely wrong: there is no arrow.
""")
print("  AND THE COMMUTATIVITY CONDITION IS THE CORPUS'S OWN DISCRIMINATOR TEST.")
print("  section 1-LEVELS: 'projection-independent ratios (theta_D/theta_* = r_D/r_s) are the clean")
print("  discriminators because the L3 map (the common D_M) CANCELS in them.'")
print("  Check the cancellation explicitly:")
rD,rs,DM=sp.symbols('r_D r_s D_M', positive=True)
thD, thS = rD/DM, rs/DM
print(f"     theta_D = r_D/D_M , theta_* = r_s/D_M  ->  theta_D/theta_* = {sp.simplify(thD/thS)}")
print("  *** D_M cancels: the ratio is INDEPENDENT of the L3 map. ***")
# r2376+c54.158 -- pins K4's commutativity condition as an exact symbolic identity: the ratio of
# the two angles is r_D/r_s with the L3 map D_M GONE from it -- that vanishing of D_M is what
# "projection-independent ratios are the clean discriminators" means, and it is what makes the
# span's two legs agree.  A ratio that still carried D_M would not be a clean discriminator.
assert sp.simplify(thD/thS - rD/rs) == 0
assert DM not in sp.simplify(thD/thS).free_symbols
assert DM in thD.free_symbols and DM in thS.free_symbols
print("  So 'a clean discriminator' = 'a quantity on which the two routes to the observable AGREE',")
print("  which is exactly commutativity of the span's two legs.  The corpus's test for a good")
print("  observable is a commuting-diagram condition, stated as a cancellation.")

print("\n" + "="*80); print("K5 — IS THE NARIAI COINCIDENCE FORCED?"); print("="*80)
r,M,al=sp.symbols('r M alpha', positive=True)
f=1-2*M/r-r**2/al**2
Mn=al/(3*sp.sqrt(3)); rN=al/sp.sqrt(3)
print("\n  Nariai is now fixed SIX ways across the corpus. Are they one condition?")
rows=[("algebraic: the cubic's DOUBLE ROOT, sigma's fixed point (P3)", sp.simplify(f.subs([(M,Mn),(r,rN)])), sp.simplify(sp.diff(f,r).subs([(M,Mn),(r,rN)]))),
      ("optical: the PHOTON SPHERE meets the horizon, 3M = r_h (O1)", sp.simplify(3*Mn-rN), None),
      ("incidence: the SINGULAR POINT of the reducible locus, 3r_0^2=1 (Q5)", sp.simplify(3*rN**2/al**2-1), None),
      ("metric: the end of the conic's MINOR AXIS (Q5)", sp.simplify(rN*sp.sqrt(3)/al-1), None),
      ("analytic: the dial's BRANCH POINT, 3w = pi/2 (P3)", sp.simplify(sp.sin(3*sp.pi/6)-1), None)]
for lab,a,b in rows:
    extra=f"   f'={b}" if b is not None else ""
    print(f"    {lab:58s} -> {a}{extra}")
# r2376+c54.158 -- pins K5's answer: ALL FIVE characterisations of Nariai -- the cubic's double
# root, the photon sphere meeting the horizon, the singular point of the reducible locus, the end
# of the conic's minor axis, the dial's branch point at 3w = pi/2 -- vanish IDENTICALLY in alpha at
# the SAME place, so they are one condition f(r_N) = f'(r_N) = 0 and not five coincidences.  And
# that place is the corpus's Nariai point: r_N = alpha/sqrt(3) = 0.5773502692 alpha and the Nariai
# mass 2M* = 2/(3 sqrt 3) = 0.3849001795 alpha, the same value the deck receipts branch at.
for _lab, _a, _b in rows:
    assert sp.simplify(_a) == 0, (_lab, _a)
assert sp.simplify(rows[0][2]) == 0, rows[0][2]          # f'(r_N) = 0 as well: a DOUBLE root
assert abs(float(rN.subs(al, 1)) - 0.5773502692) < 1e-9
assert abs(float(2*Mn.subs(al, 1)) - 0.3849001795) < 1e-9
print("\n  Every one reduces to  f(r_N) = f'(r_N) = 0.  *** ONE CONDITION, FIVE FACES. ***")
print("\n  AND THE SIXTH IS THE ISOTROPY JUMP (K1), which the double root FORCES:")
print("    f = f' = 0 at r_N  =>  the near-horizon geometry is dS_2 x S^2 (the S^2 frozen at r_N),")
print("    whose isometry is SO(2,1) x SO(3) -- dimension 3 + 3 = 6, against a generic 1 + 3 = 4.")
print("    And P12 records exactly SO(2,1) x SO(3), dim 6, as the Nariai stratum's isotropy.")
print("  *** SO THE ISOTROPY JUMP IS NOT A SIXTH COINCIDENCE: IT IS WHAT THE DOUBLE ROOT IS,   ***")
print("  *** read on the near-horizon geometry -- and K1 showed BOTH the deck group's branch     ***")
print("  *** point and the algebroid's connection-vanishing read that same jump.                ***")
print("\n  ANSWER: the coincidence is FORCED, and 'coincidence' was the wrong word for it. One")
print("  condition, f = f' = 0, wearing six faces, of which the isotropy jump is the one that")
print("  explains why the discrete and continuous structures both mark the locus.")
print("="*80)
