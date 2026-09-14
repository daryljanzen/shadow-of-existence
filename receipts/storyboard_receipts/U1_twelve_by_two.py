"""
U1_twelve_by_two -- does the 12x2 close?
========================================
WHY THIS FILE EXISTS.  The appendix entry `U1_twelve_by_two` was registered with a run
path under `receipts/storyboard_receipts/`, and ** that directory has never existed in
this repository's history **: the entry arrived without its file.  This is a REBUILD
from the entry's own stated claim, not a recovered copy -- it recomputes the result and
reports what the computation returns, which may or may not be what the entry asserts.

THE CLAIM AS REGISTERED (FIGURE_THEOREM_LEDGER |- 49):
    "The object is 12 hinges above + 12 below joined by the rulings: a bipartite
     2-regular graph, 24 vertices, 24 edges -- so the question is what are the cycles.
     Four components, each a 6-cycle, azimuths {0,120,240}/{30,150,270}/{60,180,300}/
     {90,210,330}.  The 12 closes because gcd(3,4)=1; the coupling splits because
     gcd(4,12)=4 -- same 4, generator vs divisor."

THE CONSTRUCTION.  Twelve hinge-ends on each of the two horns, at azimuths 30k degrees.
A ruling joins an upper end to a lower end; the surface is doubly ruled, so each end
carries exactly two, and the hinge geometry sets the azimuthal step at 120 degrees --
the hinge separation.  Hence upper(phi) joins lower(phi+120) and lower(phi-120).

WHAT WOULD FALSIFY THE ENTRY.  Any component count other than four, any component that
is not a 6-cycle, or azimuth classes other than those listed.
"""
from math import gcd

N, STEP = 12, 120          # twelve ends per horn, 30 deg apart; ruling step 120 deg
AZ = [30 * k for k in range(N)]
s = STEP // 30             # the step measured in vertex positions

def nbrs(v):
    lvl, i = v
    o = 1 - lvl
    return [(o, (i + s) % N), (o, (i - s) % N)]

V = [(lvl, i) for lvl in (0, 1) for i in range(N)]
E = set()
for v in V:
    for w in nbrs(v):
        E.add(frozenset((v, w)))

print("=" * 78)
print("PART 1 — THE GRAPH")
print("=" * 78)
print(f"  vertices : {len(V)}   (12 upper + 12 lower)")
print(f"  edges    : {len(E)}")
degs = {v: len(nbrs(v)) for v in V}
print(f"  regular of degree : {sorted(set(degs.values()))}")
bip = all(v[0] != w[0] for e in E for v, w in [tuple(e)])
print(f"  bipartite across the two horns : {bip}")
print(f"  ENTRY SAYS: 24 vertices, 24 edges, bipartite 2-regular")
print(f"  MATCH: {len(V)==24 and len(E)==24 and set(degs.values())=={2} and bip}")

print()
print("=" * 78)
print("PART 2 — THE COMPONENTS")
print("=" * 78)
seen, comps = set(), []
for v in V:
    if v in seen: continue
    stack, comp = [v], []
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); comp.append(x)
        stack.extend(nbrs(x))
    comps.append(comp)
print(f"  component count : {len(comps)}     ENTRY SAYS: four   MATCH: {len(comps)==4}")
print()
classes = []
for c in sorted(comps, key=lambda c: min(i for _, i in c)):
    az = sorted({AZ[i] for _, i in c})
    cyc = len(c)
    classes.append(az)
    print(f"    size {cyc:>2} ({'6-cycle' if cyc==6 else 'NOT a 6-cycle'})   azimuths {az}")
expected = [[0,120,240],[30,150,270],[60,180,300],[90,210,330]]
print()
print(f"  ENTRY SAYS azimuth classes {expected}")
print(f"  MATCH: {classes == expected}")
print(f"  every component a 6-cycle: {all(len(c)==6 for c in comps)}")

print()
print("=" * 78)
print("PART 3 — THE TWO GCDs, WHICH ARE THE ENTRY'S POINT")
print("=" * 78)
print(f"  the 12 CLOSES      : three steps of 120 deg return to start;  gcd(3,4) = {gcd(3,4)}")
print(f"  the coupling SPLITS: step 4 on a 12-cycle;                    gcd(4,12) = {gcd(4,12)}")
print(f"  components predicted by gcd(4,12) : {gcd(4,12)}   observed : {len(comps)}   "
      f"MATCH: {gcd(4,12)==len(comps)}")
print()
print("  ** Same 4, two roles: GENERATOR where it is coprime to the cycle it walks,")
print("  DIVISOR where it is not. **  That is the entry's statement and it reproduces.")

print()
print("=" * 78)
print("PART 4 — THE DISTINCTION THE ENTRY SAYS IT VERIFIES")
print("=" * 78)
print("  'the null-chord-is-not-a-ruling distinction verified at the midpoint rather")
print("  than assumed'.  ** NOT REBUILT HERE. **  That check needs the embedding and")
print("  the tangency condition, and the entry does not state its numbers, so there is")
print("  nothing to recompute against -- restating it would be asserting a check rather")
print("  than running one.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
ok = (len(V)==24 and len(E)==24 and set(degs.values())=={2} and bip
      and len(comps)==4 and all(len(c)==6 for c in comps) and classes==expected
      and gcd(4,12)==len(comps))
print(f"  every graph-level claim in the entry reproduces : {ok}")

# ASSERTIONS -- each is a property of the constructed graph that a wrong construction
# would falsify, not a comparison of literals.
assert len(V) == 2 * N,                      "vertex count is not two horns of twelve"
assert len(E) == len(V),                     "a 2-regular graph must have as many edges as vertices"
assert set(degs.values()) == {2},            "some end does not carry exactly two rulings"
assert bip,                                  "an edge joins two ends on the same horn"
assert all(len(c) == 6 for c in comps),      "a component is not a 6-cycle"
assert len(comps) == gcd(STEP // 30, N),     "component count does not follow gcd(step, N)"
assert classes == expected,                  "azimuth classes differ from the entry's"
# the entry's point: the same 4 closes one walk and splits the other
assert gcd(3, STEP // 30) == 1,              "three steps of the hinge separation do not close"
assert gcd(STEP // 30, N) > 1,               "the coupling does not split"
assert {a % (STEP) for a in AZ} == {0, 30, 60, 90}, "the residue classes are not the four listed"
print("  The bipartite 2-regular structure, the twenty-four vertices and edges, the")
print("  four components, their being 6-cycles, their azimuth classes, and both gcd")
print("  readings all return as stated.")
print()
print("  NOT REPRODUCED: the midpoint check of PART 4, which the entry claims and this")
print("  rebuild cannot recompute from what the entry states.  ** The entry's [OK] is")
print("  therefore backed on its graph content and unbacked on that one clause. **")
