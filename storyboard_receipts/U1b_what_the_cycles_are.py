"""
WHAT THE FOUR CYCLES ARE. (r1110)  Successor to U1_twelve_by_two.py.

U1 returned a structure nobody expected and nobody has read: the 24 hinges, joined by their
rulings, form FOUR disjoint 6-cycles, on azimuths

        {0, 120, 240}   {30, 150, 270}   {60, 180, 300}   {90, 210, 330}

and the arithmetic is gcd(4,12)=4 -- NOT the stamp's coprime 3x4.

** WHY THIS IS WORTH ASKING, STATED BEFORE COMPUTING. ** The construction has produced
exactly two 4s and one 3 so far, and they are known objects:
    the TRIPLE's 3   -- three hinges 120 apart, the roots of one cubic          (P3)
    the STAMP's 4    -- the dial's fundamental domain, 360/4 = 90               (why_not_eight)
and 12 = 3 x 4 with the two coprime, ONE orbit (one_thirty).
The coupling now produces a THIRD partition: 4 classes of 3. Its 4 is a divisor where the
stamp's 4 was a generator. So the question is not "is there a 4" -- it is:

    ** IS THE COUPLING'S PARTITION THE SAME PARTITION AS THE STAMP'S, OR A NEW ONE? **

THE TWO CANDIDATE ANSWERS, both named now so the answer cannot be fitted:
  (A) the four cycles ARE the four stamp-copies -- i.e. the coupling just re-finds the
      stamp, and the "different question" is different only in method. Then each cycle's
      three azimuths would be ONE hinge-triple rotated, and the partition would be the
      stamp's own orbit decomposition.
  (B) the four cycles CUT ACROSS the stamp -- a genuinely new partition of the 24, invisible
      to the rotation. Then each cycle mixes stamp-copies, and the construction has a
      structure the 3x4 never saw.

COULD THIS RETURN OTHERWISE? Yes -- (A) and (B) are mutually exclusive and both are decided
by reading which azimuths land in which class. And there is a third possibility neither of
us named, which the computation is free to return.
"""
import numpy as np
from math import gcd

a = 1.0
S3 = np.sqrt(3)
X0H = S3*a
AZ = [30*k for k in range(12)]

# ---------------------------------------------------------------- the coupling's classes
# ruling family +1 : above at A  <->  below at A-120
# ruling family -1 : above at A  <->  below at A+120
edges = set()
for th in AZ:
    for fam in (+1, -1):
        ai = round(((th + fam*60) % 360)/30) % 12
        bi = round(((th - fam*60) % 360)/30) % 12
        edges.add((ai, bi))
adj = {('A', k): [] for k in range(12)}; adj.update({('B', k): [] for k in range(12)})
for (ai, bi) in edges:
    adj[('A', ai)].append(('B', bi)); adj[('B', bi)].append(('A', ai))
seen = set(); cycles = []
for v in adj:
    if v in seen: continue
    comp = []; stack = [v]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); comp.append(x); stack.extend(adj[x])
    cycles.append(sorted(comp))
cyc_az = [sorted({AZ[k] for (_, k) in c}) for c in cycles]

print("="*80)
print("1. THE COUPLING'S FOUR CLASSES")
print("="*80)
for i, az in enumerate(cyc_az):
    print(f"  cycle {i}: azimuths {az}    (mod 30: {az[0]//30} mod 4)")
print(f"\n  ** each class is one residue of the azimuth INDEX mod 4. **")
for i, az in enumerate(cyc_az):
    idx = sorted(AZ.index(x) for x in az)
    assert len({k % 4 for k in idx}) == 1
print("  verified: every class is {k : k = c mod 4}, c = 0,1,2,3.")

print("\n" + "="*80)
print("2. THE STAMP'S FOUR COPIES -- what the rotation's 4 actually partitions")
print("="*80)
print("""  The stamp: take the 3 hinges at 0/120/240 and rotate the whole figure by 90 degrees,
  four times. So stamp-copy s carries the azimuths {90s, 90s+120, 90s+240}.""")
stamp = [sorted([(90*s + 120*j) % 360 for j in range(3)]) for s in range(4)]
for s, az in enumerate(stamp):
    idx = sorted(AZ.index(x) for x in az)
    print(f"  stamp copy {s} (rotate {90*s} deg): azimuths {az}    indices {idx}   "
          f"mod 4: {sorted({k % 4 for k in idx})}")

print("\n" + "="*80)
print("3. ** ARE THEY THE SAME PARTITION? **")
print("="*80)
setC = {frozenset(c) for c in cyc_az}
setS = {frozenset(s) for s in stamp}
same = setC == setS
print(f"  the coupling's classes : {sorted(sorted(c) for c in cyc_az)}")
print(f"  the stamp's copies     : {sorted(sorted(s) for s in stamp)}")
print(f"\n  ** SAME PARTITION: {same} **")
if same:
    print("""
  ** ANSWER (A). THE COUPLING'S FOUR CYCLES *ARE* THE STAMP'S FOUR COPIES. **

  And that is a real result, not a null one, because the two arrive by routes that share
  nothing:
      the STAMP's 4  is a ROTATION of the figure -- an operation ON the overhead, chosen
                     as the dial's fundamental domain (why_not_eight.py: the physics is
                     invariant under {front/back} x {mirror} and under no quarter).
      the COUPLING's 4 is a RULING INCIDENCE -- the null lines of the embedding, which the
                     overhead cannot see at all (a ruling leaves the level; the overhead is
                     a level).
  ** ONE PARTITION OF THE 24, REACHED ONCE FROM THE PLANE AND ONCE FROM THE LIGHT CONE. **
  The stamp says which hinges are copies of each other. The rulings say which hinges are
  causally strung together. They are the same classes.""")
else:
    print("""
  ** ANSWER (B). THE COUPLING CUTS ACROSS THE STAMP -- a partition the rotation never saw. **""")

print("\n" + "="*80)
print("4. THE 3 INSIDE EACH CYCLE -- is it the hinge-triple?")
print("="*80)
print("""  Each cycle has 3 azimuths, 120 apart. So does each hinge-triple (P3: three roots of one
  cubic, 120 apart). Test whether a cycle's three azimuths ARE a triple's -- i.e. whether the
  cycle is one stamped copy of the original 3 hinges, or three hinges from three different
  copies.""")
base = [0, 120, 240]
for i, az in enumerate(cyc_az):
    rot = None
    for s in range(4):
        if sorted(((90*s + b) % 360) for b in base) == az:
            rot = 90*s; break
    print(f"  cycle {i}: {az}  ->  {'the base triple rotated by ' + str(rot) + ' deg' if rot is not None else 'NOT a rotated triple'}")
    assert rot is not None
print("""
  ** Every cycle is the base hinge-triple, rotated by one stamp step. **
  So the 6-cycle is: one triple's three hinges ABOVE, and the same triple's three BELOW,
  strung alternately by rulings. The cycle's 6 = 3 x 2, and the 2 is the level.""")

print("\n" + "="*80)
print("5. THE WALK -- what the 6-cycle actually is")
print("="*80)
c0 = [c for c in cycles if AZ[0] in {AZ[k] for (_, k) in c}][0]
start = ('A', 0)
walk = [start]; prev = None; cur = start
for _ in range(6):
    nxt = [x for x in adj[cur] if x != prev]
    nxt = nxt[0] if len(nxt) == 1 else [x for x in adj[cur] if x != prev][0]
    prev, cur = cur, nxt
    walk.append(cur)
print("  starting at the ABOVE hinge at 0 deg and following rulings:")
for (lv, k) in walk:
    print(f"    {'ABOVE' if lv == 'A' else 'below'}  {AZ[k]:>3} deg")
print(f"""
  ** The walk alternates level every step -- because every edge is a ruling, and a ruling
  cannot stay on a level (rulings_between_levels.py: a null line cannot stand still in time).
  Six steps returns to the start. **
  ** SO THE 6-CYCLE IS: THE TRIPLE, TRAVERSED TWICE -- ONCE ON EACH HORN -- AND THE RULINGS
  ARE WHAT SEW THE TWO TRAVERSALS TOGETHER. It is not 3 above plus 3 below; it is one
  closed light-path through all six. **""")

print("\n" + "="*80)
print("6. THE ARITHMETIC, STATED WHOLE -- why the same 4 does two opposite things")
print("="*80)
print(f"""  the STAMP:    step 90 deg = 3 slots of 30.   gcd(3, 12) = 3  -> 3 orbits? NO --
                the stamp acts on the FIGURE (3 hinges), not on the 12 slots. It maps
                triple -> triple, and 4 applications return. Its orbit on the TRIPLES
                is a single 4-cycle.
  the COUPLING: step 120 deg = 4 slots of 30.  gcd(4, 12) = 4  -> 4 orbits of 3.

  ** AND THE TWO PARTITIONS AGREE (section 3) BECAUSE 120 IS THE TRIPLE'S OWN STEP. **
  The coupling moves a hinge by 120 -- which is exactly the step WITHIN a triple. So it can
  never leave the triple, and its orbits ARE the triples. The stamp's copies ARE the triples.
  Same classes, and the reason is that the coupling's 120 is the triple's 120.

  ** WHICH IS WHY IT IS NOT THE 3x4 CLOSURE RE-WORN, AND ALSO NOT INDEPENDENT OF IT: **
  the 3x4 closure says the 12 is ONE orbit under the ROTATION (gcd(3,4)=1, coprime).
  the coupling says the 12 is FOUR orbits under the RULING (gcd(4,12)=4).
  Both are true. They are statements about DIFFERENT GROUP ACTIONS on the same 12 points --
  and the coupling's orbits are the stamp's copies, so the light cone and the rotation
  agree about which hinges belong together while disagreeing about whether the 12 is one
  thing or four.""")

print("\n" + "="*80)
print("WHAT THIS RETURNED")
print("="*80)
print(f"""  ** THE COUPLING'S FOUR CYCLES ARE THE STAMP'S FOUR COPIES. SAME PARTITION: {same}. **
  Reached by routes sharing nothing: the stamp is a ROTATION of the overhead (chosen as the
  dial's fundamental domain); the coupling is a RULING INCIDENCE in the embedding, which the
  overhead cannot see -- a ruling leaves the level, and the overhead IS a level.
  ** One partition of the 24, found once from the plane and once from the light cone. **

  AND EACH 6-CYCLE IS THE TRIPLE TRAVERSED TWICE, once per horn, sewn by rulings: the walk
  alternates level at every step, because a null line cannot stand still in time. Not
  "3 above + 3 below" but ONE CLOSED LIGHT-PATH THROUGH ALL SIX.

  THE REASON THE TWO PARTITIONS AGREE, and it is one line: THE COUPLING'S STEP IS 120, WHICH
  IS THE TRIPLE'S OWN STEP. The coupling cannot leave the triple, so its orbits are the
  triples, and the triples are the stamp's copies.

  SO c40's "different question" is confirmed AND placed: the 3x4 coprimality and the
  gcd(4,12)=4 splitting are statements about DIFFERENT GROUP ACTIONS on the same 12 points.
  The rotation says the 12 is one orbit. The rulings say it is four. Both true; they act
  differently; and they agree about which hinges belong together.

  ⚠ BOUNDED (face 35): this quantifies over the INCIDENCE and the AZIMUTH ARITHMETIC. No cut,
  no dial, no f, no 2M appears. What a cycle means physically -- whether a closed light-path
  through a triple's six hinges is anything -- is not asked here.""")
