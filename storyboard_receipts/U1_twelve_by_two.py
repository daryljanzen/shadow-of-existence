"""
U1 — THE 12x2 CLOSURE UNDER THE COUPLING. (r1110)

Named unrun by c40 at r1107 -- the last thing it was about to draw. Run here.

THE QUESTION, in c40's words (C40_EXTRACTION_r1107.md):
    "whether the 12x2 grid closes under the coupling the way the 12 closes under 3x4
     coprimality. DIFFERENT QUESTION -- the 12 is a ROTATIONAL ORBIT; the x2 is a RULING
     INCIDENCE. c40 was about to draw it; nobody has computed it."

WHAT IS ALREADY ESTABLISHED (rulings_between_levels.py, r1107):
    * the hinges sit at overhead radius X=2a, so X0 = +-sqrt3 a: TWELVE ABOVE, TWELVE BELOW
    * a null ruling through the equator at azimuth th reaches X=2a at th +- 60
    * family A : (th-60, BELOW) <-> equator th <-> (th+60, ABOVE)
    * NO RULING STAYS ON A LEVEL -- a null line cannot stand still in time
    * "the doubling is not a mirror pair, it is THE COUPLING: the 12 above and the 12 below
       are the two ENDS of the rulings, and every ruling has one end in each."

SO THE OBJECT IS A BIPARTITE GRAPH, not a set of 24 points:
    vertices = 12 hinges ABOVE + 12 hinges BELOW
    edges    = the null rulings, each joining one above to one below
And "does it close" is a question about THAT GRAPH. c40's own framing says what it is not:
not a rotational orbit (that is the 12), but an INCIDENCE.

THE QUESTIONS, made precise before computing -- so the answer cannot be fitted to them:
    Q1  is every hinge ON a ruling that reaches the other level, and how many?
    Q2  is the incidence a PERFECT MATCHING (each above to exactly one below) or richer?
    Q3  does the graph CONNECT -- can you walk from any hinge to any other along rulings?
    Q4  is the closure the 3x4 one re-worn, or a genuinely different arithmetic?

COULD THIS RETURN OTHERWISE? Yes at every step: the incidence either exists or it does not;
the graph is connected or it is not; the component count is what it is. And Q4 has a named
falsifier: if the answer were "12" or "3x4" the coupling would be the rotation re-worn, and
c40's "different question" would be wrong.
"""
import numpy as np
from math import gcd

a = 1.0
S3 = np.sqrt(3)
X0H = S3*a                      # the hinge height, from |X|=2a on -X0^2+|X|^2=a^2

def pt(X0, th_deg):
    """a point of the hyperboloid at height X0 and azimuth th."""
    R = np.sqrt(a**2 + X0**2)
    t = np.radians(th_deg)
    return np.array([X0, R*np.cos(t), R*np.sin(t)])

def ds2(P, Q):
    d = Q - P
    return -d[0]**2 + d[1]**2 + d[2]**2

# the 12 hinge azimuths: 3 hinges x 4 stamps = 30-degree spacing  (one_thirty.py)
AZ = [30*k for k in range(12)]
ABOVE = {k: pt(+X0H, AZ[k]) for k in range(12)}
BELOW = {k: pt(-X0H, AZ[k]) for k in range(12)}

print("="*80)
print("0. THE OBJECT -- 24 hinges, and the rulings that join them")
print("="*80)
print(f"  12 azimuths, 30 deg apart: {AZ}")
print(f"  each at X0 = +-{X0H:.6f} = +-sqrt3 a   (overhead radius 2a)")
print(f"  sanity: |X| at a hinge = {np.linalg.norm(ABOVE[0][1:]):.6f} = 2a")
assert abs(np.linalg.norm(ABOVE[0][1:]) - 2*a) < 1e-12

print("\n" + "="*80)
print("Q1 -- IS THE SEGMENT FROM AN ABOVE-HINGE TO A BELOW-HINGE EVER NULL?")
print("     (and is it a chord, or does it lie IN the surface -- i.e. a ruling?)")
print("="*80)
print(f"  {'above':>6} {'below':>6} {'delta az':>9} {'ds^2':>12} {'null?':>7} {'in surface?':>12}")
null_pairs = []
for j in range(12):
    P, Q = ABOVE[0], BELOW[j]
    s = ds2(P, Q)
    isnull = abs(s) < 1e-9
    # does the straight segment lie IN the hyperboloid?  test the midpoint.
    Mid = 0.5*(P + Q)
    onsurf = abs(-Mid[0]**2 + Mid[1]**2 + Mid[2]**2 - a**2) < 1e-9
    d = (AZ[j] - AZ[0]) % 360
    if isnull:
        null_pairs.append((0, j, d, onsurf))
    if isnull or j < 6:
        print(f"  {0:>6} {j:>6} {d:>9.0f} {s:>12.6f} {str(isnull):>7} {str(onsurf):>12}")
print(f"\n  null above-below pairs from hinge 0: {[(j, f'{d:.0f} deg') for _,j,d,_ in null_pairs]}")

print("\n" + "="*80)
print("** THE ANSWER TO Q1, AND IT IS NOT WHAT THE NAME 'the 12x2' SUGGESTS **")
print("="*80)
print("""  The straight line joining an above-hinge to a below-hinge is null ONLY at the azimuth
  separations found above -- and it is a RULING only if it also lies IN the surface. Read
  the 'in surface?' column: a null chord between two points of the hyperboloid need NOT be a
  ruling. The rulings are the null lines that lie in the surface; a null CHORD is a null line
  that cuts through. THE COUPLING IS ABOUT RULINGS, so only the in-surface ones count.""")
rulings = [(i, j, d) for (i, j, d, onsurf) in null_pairs if onsurf]
print(f"\n  from hinge 0, above -> below, TRUE RULINGS: "
      f"{[(j, f'{d:.0f} deg') for _,j,d in rulings] if rulings else 'NONE'}")

print("\n" + "="*80)
print("Q1b -- SO WHERE DO THE RULINGS FROM A HINGE ACTUALLY GO? (the established rule)")
print("="*80)
print("""  rulings_between_levels.py established: a null ruling through the equator at azimuth th
  reaches X=2a at th +- 60. Read backwards from a hinge: the ruling through the ABOVE hinge
  at azimuth A came up through the equator at A-60, and continues DOWN to the below-hinge at
  A-120. The other family does A+60 / A+120.""")
def ruling_through(th_eq, fam):
    """the straight null line through the equator at azimuth th_eq. fam=+1 or -1.
       returns (P_below, P_eq, P_above) at the hinge levels."""
    sgn = fam
    return (pt(-X0H, th_eq - sgn*60), pt(0.0, th_eq), pt(+X0H, th_eq + sgn*60))
ok = 0
for th in AZ:
    for fam in (+1, -1):
        B, E, A_ = ruling_through(th, fam)
        # collinear?  and null?
        v1, v2 = E - B, A_ - E
        cross = np.linalg.norm(np.cross(v1, v2))
        s1, s2 = ds2(B, E), ds2(E, A_)
        if cross < 1e-9 and abs(s1) < 1e-9 and abs(s2) < 1e-9:
            ok += 1
print(f"\n  straight-and-null through (below, equator, above) for all 12 azimuths x 2 families:"
      f"  {ok}/24 verified")
assert ok == 24
print("  ** every one collinear to machine zero and null on both segments. **")

print("\n" + "="*80)
print("Q2 -- THE INCIDENCE: is it a perfect matching?")
print("="*80)
print("  Each ruling joins ONE above-hinge to ONE below-hinge. Tabulate, by family:")
edges = set()
for th in AZ:
    for fam in (+1, -1):
        ai = round(((th + fam*60) % 360)/30) % 12
        bi = round(((th - fam*60) % 360)/30) % 12
        edges.add((ai, bi))
print(f"\n  {'above':>6} -> {'below (family +)':>17} {'below (family -)':>17}")
for k in range(12):
    fp = [b for (aa, b) in edges if aa == k]
    print(f"  {AZ[k]:>4}deg -> {str(sorted(set(fp))):>35}")
deg_a = {k: sum(1 for (aa, bb) in edges if aa == k) for k in range(12)}
deg_b = {k: sum(1 for (aa, bb) in edges if bb == k) for k in range(12)}
print(f"\n  degree of every ABOVE hinge: {sorted(set(deg_a.values()))}")
print(f"  degree of every BELOW hinge: {sorted(set(deg_b.values()))}")
print(f"  total edges: {len(edges)}")
print(f"""
  ** NOT a perfect matching. Each hinge sits on TWO rulings -- one per family -- so the
  graph is 2-REGULAR on 24 vertices with {len(edges)} edges. A 2-regular graph is a DISJOINT
  UNION OF CYCLES. So 'does the 12x2 close' is exactly: WHAT ARE THE CYCLES? **""")

print("\n" + "="*80)
print("Q3 -- THE CYCLES: walk the graph")
print("="*80)
adj = {('A', k): [] for k in range(12)}
adj.update({('B', k): [] for k in range(12)})
for (ai, bi) in edges:
    adj[('A', ai)].append(('B', bi))
    adj[('B', bi)].append(('A', ai))
seen = set(); comps = []
for v in adj:
    if v in seen: continue
    comp = []; stack = [v]
    while stack:
        x = stack.pop()
        if x in seen: continue
        seen.add(x); comp.append(x)
        stack.extend(adj[x])
    comps.append(sorted(comp))
print(f"  connected components: {len(comps)}")
for c in comps:
    az = sorted({AZ[k] for (_, k) in c})
    lv = sorted({s for (s, _) in c})
    print(f"    size {len(c):>2}: levels {lv}, azimuths {az}")
print(f"""
  ** {len(comps)} COMPONENT{'S' if len(comps) != 1 else ''}. **""")

print("\n" + "="*80)
print("Q4 -- IS THE CLOSURE THE 3x4 RE-WORN, OR A DIFFERENT ARITHMETIC?")
print("="*80)
print("""  The coupling's step, read on the azimuth circle: a ruling takes an ABOVE hinge at az A
  to a BELOW hinge at A -/+ 120. So the walk 'follow family +, then family -' advances the
  azimuth by a fixed amount, and the cycle length is the order of that step in Z/12.""")
step = 120 // 30                      # 120 degrees = 4 slots of 30
g = gcd(step, 12)
print(f"\n  the coupling's step on the 12 azimuths: 120 deg = {step} slots")
print(f"  gcd({step}, 12) = {g}   ->  its orbit has 12/{g} = {12//g} azimuths, and there are {g} orbits")
print(f"""
  ** SO THE COUPLING'S ARITHMETIC IS gcd(4, 12) = 4 -- NOT the 3x4 coprimality. **
  The 12's closure was: the stamp is 4|n, and the 3 and the 4 are coprime so 3x4 = 12 is a
  single orbit. THE COUPLING'S 120-degree step is NOT coprime to 12 -- it has gcd 4 -- so it
  does NOT sweep the 12. It splits them.

  ** c40 WAS RIGHT THAT IT IS A DIFFERENT QUESTION, AND THE COMPUTATION SAYS WHY: **
     the 12 closes because 3 and 4 are COPRIME (one orbit).
     the coupling splits because 4 and 12 are NOT (four orbits).
  Same 4. Opposite role. The rotation's 4 is a GENERATOR; the coupling's 4 is a DIVISOR.""")

print("\n" + "="*80)
print("WHAT U1 RETURNED")
print("="*80)
print(f"""  ** THE 12x2 IS A 2-REGULAR BIPARTITE GRAPH ON 24 HINGES -- {len(edges)} rulings, every hinge
  on exactly two (one per ruling family). A 2-regular graph is a disjoint union of cycles,
  so the closure question is 'what are the cycles', and the answer is {len(comps)}
  component{'s' if len(comps)!=1 else ''}. **

  ** AND IT DOES NOT CLOSE THE WAY THE 12 DOES, for a reason that is one line of arithmetic: **
    the 12's closure is 3x4 with gcd(3,4)=1 -- COPRIME, so the stamp sweeps all twelve as ONE
    orbit. The coupling's step is 120 deg = 4 slots of 30, and gcd(4,12)=4 -- NOT coprime, so
    it splits the twelve into 4 orbits of 3. THE ROTATION'S 4 IS A GENERATOR; THE COUPLING'S 4
    IS A DIVISOR. Same number, opposite role. c40's "different question" is confirmed, and the
    difference is exactly coprimality.

  ESTABLISHED EN ROUTE:
    * a null CHORD between two hinges is not the same as a RULING -- the ruling must lie IN
      the surface. Checked explicitly rather than assumed; it is the distinction the whole
      question turns on.
    * all 24 rulings (12 azimuths x 2 families) verified straight-and-null through
      (below, equator, above), collinear to machine zero.

  BOUNDED (face 35): this receipt quantifies over the INCIDENCE STRUCTURE of the 24 hinges
  and their rulings. It says nothing about what the cycles MEAN physically -- no cut, no dial,
  no f, no 2M appears in it. That is a different receipt.""")
