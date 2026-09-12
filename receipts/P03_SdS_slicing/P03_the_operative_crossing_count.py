"""
P03_the_operative_crossing_count
================================
WHAT IT ASKS.  P3 sec:winding assigns a constituent its WINDING -- "the signed number
of graze points its equatorial route crosses, in units of one third of a lap" -- and
the two routes between punctures at different hinges cross ONE and TWO graze points,
differing by exactly one lap.

Under the three-vantage reading the corpus adopted (P14R28, reading (ii)) a crossing
of wall W branches only W's OWNER.  So for a mode bound in vantage k, the crossings
that act on its own component are the crossings of WALL k, and no others.

** So there are two counts on the same route: the TOTAL graze-point count n, which is
what P3's winding measures, and the OWN-WALL count nu, which is what the monodromy
acts by. **  This computes both, over every route in the geometry, and asks how they
are related.

GEOMETRY, taken from the corpus and not re-derived here: hinges at azimuth 0/120/240;
wall_j at (120j + 180) mod 360, antipodal to hinge j and canonically its own (L-75,
P03_wall_is_the_graze_point); owner = the inverse map.

WHAT WOULD FALSIFY THE HEADLINE.  If nu were a free function of the route -- if some
n = 1 route crossed its own wall and some did not -- there would be no relation to
report, and the winding would carry no information about the monodromy.
"""
hinge = {j: 120 * j for j in range(3)}
wall = {j: (120 * j + 180) % 360 for j in range(3)}
owner = {v: k for k, v in wall.items()}

def arc_crossings(a, b, direction):
    """Walls strictly inside the arc from azimuth a to b in the given direction."""
    out = []
    step = 1 if direction > 0 else -1
    x = a
    while True:
        x = (x + step) % 360
        if x == b:
            break
        if x in owner:
            out.append(x)
    return out

print("=" * 78)
print("PART 1 — THE GEOMETRY, AS THE CORPUS FIXES IT")
print("=" * 78)
for j in range(3):
    print(f"  hinge {j} at {hinge[j]:>3}deg   its wall r_{j}=0 at {wall[j]:>3}deg (antipodal)")
print()

print("=" * 78)
print("PART 2 — EVERY ROUTE, BOTH COUNTS")
print("=" * 78)
print(f"  {'constituent':>12} {'route':>14} {'walls crossed':>18} {'n':>3} {'nu':>4}  {'monodromy on own slot':>24}")
rows = []
for k in range(3):                      # constituent bound in vantage k, at hinge k
    for j in range(3):                  # travelling to hinge j
        if j == k:
            continue
        for d, dname in ((+1, "ccw"), (-1, "cw")):
            crossed = arc_crossings(hinge[k], hinge[j], d)
            n = len(crossed)
            nu = sum(1 for c in crossed if owner[c] == k)
            mono = "omega^(-lambda)" if nu % 3 else "1"
            rows.append((k, j, dname, tuple(owner[c] for c in crossed), n, nu))
            print(f"  {('vantage '+str(k)):>12} {('h'+str(k)+'->h'+str(j)+' '+dname):>14}"
                  f" {str(tuple('wall'+str(owner[c]) for c in crossed)):>18} {n:>3} {nu:>4}  {mono:>24}")

print()
print("=" * 78)
print("PART 3 — THE RELATION")
print("=" * 78)
pairs = sorted({(n, nu) for *_, n, nu in rows})
print(f"  (n, nu) pairs realised over all routes: {pairs}")
ok = all(nu == n - 1 for n, nu in pairs)
print(f"  nu = n - 1 on every route: {ok}")
print()
print("  ** So the two counts are locked, and not equal. **  The route crossing ONE")
print("  graze point never crosses the constituent's own wall; the route crossing TWO")
print("  always does.  Reason, and it is forced by the antipodal map: wall_m lies")
print("  between hinges i and j whenever {i,j,m} = {0,1,2}, so the short route from")
print("  hinge k crosses only the THIRD hinge's wall, and the long route crosses")
print("  hinge k's own wall and the destination's.")

print()
print("=" * 78)
print("PART 3b — THE SCOPE OF nu = n - 1, STATED BECAUSE IT IS NOT GENERAL")
print("=" * 78)
print("  The relation is computed over routes between punctures at DISTINCT hinges,")
print("  which is exactly the domain P3 sec:winding defines a winding on (\'between two")
print("  punctures at different hinges there are exactly two equatorial routes\').")
print("  It does NOT extend to closed circuits:")
for nm, tot, own in (("trivial route", 0, 0), ("one full lap", 3, 1), ("two full laps", 6, 2)):
    print(f"    {nm:>14}:  n={tot}, nu={own}   ->  nu = n-1 ? {own == tot-1}")
print("  ** A lap crosses each wall once, so nu = 1 while n = 3. **  The relation is a")
print("  fact about the two inter-hinge routes and their one-lap difference, not a")
print("  general identity, and it is used below only on that domain.")

print()
print("=" * 78)
print("PART 4 — WHAT THAT DOES TO THE OPEN CONDITION")
print("=" * 78)
print("  The open condition was  n = t (mod 3)  -- that a constituent's route-crossing")
print("  count equals its own triality (P3R47).  What acts on the mode is not n but nu:")
print("  the monodromy on its own slot is omega^(-lambda*nu) = omega^(t*nu).")
print()
print("  With nu = n - 1:   monodromy on own slot = omega^(t(n-1)).")
print()
for n in (1, 2):
    for t in (0, 1, 2):
        print(f"    n={n}, t={t}:  nu={n-1}  ->  own-slot monodromy = omega^{(t*(n-1)) % 3}")
print()
print("  ** So n and t enter the monodromy as a PRODUCT t(n-1), and the condition n = t")
print("  is not what the geometry imposes on it. **  A route with n=1 leaves the mode's")
print("  own component untouched whatever its triality; a route with n=2 multiplies it")
print("  by omega^t.  The two labels remain independent: nu is fixed by the route and t")
print("  by the angular problem, and nothing computed here relates them.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  DERIVED: nu = n - 1 on every route in the geometry, forced by the antipodal")
print("  wall map.  The count that acts on a bound mode is not the count P3's winding")
print("  measures; they differ by one, uniformly.")
print()
print("  NOT DERIVED, and this is the honest answer to the question the dig opened:")
print("  the identification n = t (mod 3) is NOT forced by the binding.  The binding")
print("  fixes WHICH crossings act (own-wall only) and the geometry fixes nu = n - 1,")
print("  but the mode's triality t is set by the angular problem and is free of both.")
print("  The condition stands open, now with its operative count identified.")
