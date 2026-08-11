"""D2 — THE KLEIN CORRESPONDENCE on the corpus's own line configuration.
CONFIRMATION 4 — the objects, stated before anything runs:
  * The corpus's doubly-ruled surface is the EQUATORIAL hyperboloid -X0^2 + X1^2 + X2^2 = alpha^2,
    a 2-surface in R^3.  Its rulings are therefore LINES IN P^3 -- which is exactly Klein's setting.
  * Klein sends a line in P^3 to a point of the KLEIN QUADRIC, a signature-(3,3) quadric in P^5.
  * ** THAT P^5 IS NOT THE CORPUS'S P^5. ** The substrate dS_5 sits in ambient M^6, whose
    projectivisation is also a P^5 -- a DIFFERENT one (Plucker space of lines in a 3-space vs the
    projectivised ambient of the substrate).  The queue's 'CR has a P^5' is a coincidence of dimension
    and is recorded as such before the probe, so the probe cannot quietly trade on it.
  * The distinguished configuration: P3's SKEW HEXAGON of six null rulings through the six hinges,
    U0 -> D120 -> U240 -> D0 -> U120 -> D240 -> U0, each edge tangent to the throat at its midpoint.
THE QUESTION: under Klein the six lines become six points on the Klein quadric, and 'two lines meet'
becomes 'the two points are conjugate'.  What configuration do they make?"""
import numpy as np, itertools
al=1.0; s3=np.sqrt(3)
def hinge(sign, deg):  # X0 = sign*sqrt3, transverse 2 at angle deg
    a=np.radians(deg); return np.array([sign*s3, 2*np.cos(a), 2*np.sin(a)])
U={d:hinge(+1,d) for d in (0,120,240)}; D={d:hinge(-1,d) for d in (0,120,240)}
eta=np.diag([-1.0,1,1])
print("="*78); print("D2 — THE SKEW HEXAGON UNDER THE KLEIN CORRESPONDENCE"); print("="*78)
print("\nSTEP 1 — the six hinges are on the hyperboloid:")
_hinge_eta=[]                                  # r2376+c54.159: keep the printed eta(P,P)
for lab,P in [('U0',U[0]),('U120',U[120]),('U240',U[240]),('D0',D[0]),('D120',D[120]),('D240',D[240])]:
    print(f"   {lab:5s} = ({P[0]:+.4f},{P[1]:+.4f},{P[2]:+.4f})   eta(P,P) = {P@eta@P:+.6f}")
    _hinge_eta.append((lab, P[0], np.hypot(P[1],P[2]), P@eta@P))
# r2376+c54.159 -- PINS STEP 1: all six hinges sit ON the equatorial hyperboloid eta(P,P) = alpha^2
# = 1, at X0 = +-sqrt3 = +-1.7320508076 and transverse radius exactly 2.alpha = 2 (P3's placement).
assert len(_hinge_eta)==6, _hinge_eta
assert all(abs(e - 1.0) < 1e-12 for *_, e in _hinge_eta), _hinge_eta
assert all(abs(abs(x0) - 1.7320508076) < 1e-9 for _, x0, _, _ in _hinge_eta), _hinge_eta
assert all(abs(rt - 2.0) < 1e-12 for _, _, rt, _ in _hinge_eta), _hinge_eta

cyc=[('U0',U[0]),('D120',D[120]),('U240',U[240]),('D0',D[0]),('U120',U[120]),('D240',D[240])]
print("\nSTEP 2 — the six EDGES of the hexagon, and a check that each is NULL and tangent to the throat.")
edges=[]
_edge_geom=[]                                  # r2376+c54.159: keep nullness and closest approach
for i in range(6):
    (la,A),(lb,B)=cyc[i],cyc[(i+1)%6]
    d=B-A
    nullness=d@eta@d
    # distance of the line from the axis in the equatorial plane: closest approach of its (X1,X2) part
    t=-(A[1]*d[1]+A[2]*d[2])/(d[1]**2+d[2]**2)
    foot=A[1:]+t*d[1:]
    edges.append((f"{la}->{lb}", A, B))
    _edge_geom.append((nullness, np.linalg.norm(foot)))
    print(f"   {la:5s}->{lb:5s}  eta(d,d) = {nullness:+.2e}  (null)   closest approach to axis = {np.linalg.norm(foot):.6f} (= alpha)")
# r2376+c54.159 -- PINS STEP 2: each of the six hexagon edges is a NULL chord (eta(d,d) = 0) whose
# closest approach to the axis is exactly alpha = 1.000000 -- i.e. every edge is tangent to the
# THROAT, which is what makes them rulings of the hyperboloid rather than generic null chords.
assert len(_edge_geom)==6, _edge_geom
assert all(abs(nl) < 1e-12 for nl, _ in _edge_geom), _edge_geom
assert all(abs(fo - 1.0) < 1e-12 for _, fo in _edge_geom), _edge_geom

def plucker(A,B):
    P=np.append(A,1.0); Q=np.append(B,1.0)     # homogenise into P^3
    return np.array([P[i]*Q[j]-P[j]*Q[i] for i,j in itertools.combinations(range(4),2)])
pl=[plucker(A,B) for _,A,B in edges]
def klein_form(p,q):   # p01 q23 - p02 q13 + p03 q12 + p12 q03 - p13 q02 + p23 q01
    i={'01':0,'02':1,'03':2,'12':3,'13':4,'23':5}
    return (p[i['01']]*q[i['23']] - p[i['02']]*q[i['13']] + p[i['03']]*q[i['12']]
          + p[i['12']]*q[i['03']] - p[i['13']]*q[i['02']] + p[i['23']]*q[i['01']])
print("\nSTEP 3 — each Plucker point lies ON the Klein quadric (<p,p> = 0), as every line must:")
for (lab,_,_),p in zip(edges,pl):
    print(f"   {lab:14s} <p,p> = {klein_form(p,p):+.3e}")
print("\nSTEP 4 — THE CONJUGACY PATTERN.  <p,q> = 0  <=>  the two lines MEET.")
n=len(pl); print("        " + "  ".join(f"{lab.split('->')[0]:>5s}" for lab,_,_ in edges))
for i in range(n):
    row=[]
    for j in range(n):
        v=klein_form(pl[i],pl[j])
        row.append(" MEET" if abs(v)<1e-9 else f"{v:+5.1f}")
    print(f"   {edges[i][0].split('->')[0]:5s} " + "  ".join(f"{r:>5s}" for r in row))

# r2376+c54.159 -- PINS STEPS 3-5, the whole reading of the table.  Every Plucker point is ON the
# Klein quadric (<p,p> = 0, as any line must be); the six split into two triples by PARITY, and the
# only non-meeting pairs are the same-parity ones, at the printed values +36 (even) and -36 (odd);
# every even-odd pair MEETS.  That 3+3 with 9 meets is the signature of the two ruling families.
_gram=[[klein_form(pl[_i],pl[_j]) for _j in range(6)] for _i in range(6)]
assert all(abs(_gram[_i][_i]) < 1e-9 for _i in range(6)), [_gram[_i][_i] for _i in range(6)]
_meets = sorted((_i,_j) for _i in range(6) for _j in range(_i+1,6) if abs(_gram[_i][_j]) < 1e-9)
assert len(_meets) == 9, _meets                       # 3 x 3 across the two families
assert all((_i+_j) % 2 == 1 for _i,_j in _meets), _meets           # exactly the even-odd pairs
assert all(abs(_gram[_i][_j] - 36.0) < 1e-9 for _i,_j in ((0,2),(0,4),(2,4))), _gram
assert all(abs(_gram[_i][_j] + 36.0) < 1e-9 for _i,_j in ((1,3),(1,5),(3,5))), _gram

print("\n" + "="*78)
print("STEP 5 — READ THE PATTERN.  Label the edges 0..5 around the hexagon.")
print("   Non-meeting pairs: (0,2),(0,4),(2,4) all +36  and  (1,3),(1,5),(3,5) all -36.")
print("   Meeting pairs: EVERY even-odd pair.")
print("   Even edges start at U-hinges; odd edges start at D-hinges.")
print("   *** SO THE SIX SPLIT INTO TWO TRIPLES: within a triple no two meet; across triples all meet.")
print("       THAT IS THE SIGNATURE OF THE TWO RULING FAMILIES. Same family -> skew; opposite -> meet. ***")
print("   And it explains the hexagon's LENGTH: a closed circuit alternating between the two families")
print("   must have EVEN length, and six is the least that visits all six hinges.  P3 draws the hexagon;")
print("   this says why a hexagon is the only closed figure those rulings can make.")

print("\nSTEP 6 — WHERE DO THE OPPOSITE EDGES MEET?  (0,3), (1,4), (2,5) -- the three new points.")
def meet(A1,B1,A2,B2):
    d1=B1-A1; d2=B2-A2
    Mx=np.array([d1,-d2]).T
    sol,res,rank,sv=np.linalg.lstsq(Mx, A2-A1, rcond=None)
    return A1+sol[0]*d1
_cross3=[]                                     # r2376+c54.159: keep the three new points
for i in (0,1,2):
    j=i+3
    (_,A1,B1)=edges[i]; (_,A2,B2)=edges[j]
    X=meet(A1,B1,A2,B2)
    _cross3.append(X)
    print(f"   edge{i} ({edges[i][0]:12s}) x edge{j} ({edges[j][0]:12s})  ->  "
          f"({X[0]:+.6f},{X[1]:+.6f},{X[2]:+.6f})   eta(X,X) = {X@eta@X:+.6f}")
# r2376+c54.159 -- PINS STEP 6: the three opposite-edge crossings lie at X0 = 0 (the throat plane),
# on the throat circle itself (eta(X,X) = alpha^2 = 1, |transverse| = 1), and they are the three
# printed points (0,+0.500000,+0.866025), (0,-1.000000,0), (0,+0.500000,-0.866025).
assert len(_cross3)==3, _cross3
assert all(abs(X[0]) < 1e-9 for X in _cross3), _cross3
assert all(abs(X@eta@X - 1.0) < 1e-9 for X in _cross3), _cross3
assert abs(_cross3[0][1] - 0.5) < 1e-9 and abs(_cross3[0][2] - 0.8660254038) < 1e-9, _cross3[0]
assert abs(_cross3[1][1] + 1.0) < 1e-9 and abs(_cross3[1][2]) < 1e-9, _cross3[1]
assert abs(_cross3[2][1] - 0.5) < 1e-9 and abs(_cross3[2][2] + 0.8660254038) < 1e-9, _cross3[2]
print("\n   *** THE THREE OPPOSITE-EDGE INTERSECTIONS ARE ON THE AXIS, AT X0 = 0 -- ***")
print("   *** i.e. ON THE THROAT CIRCLE ITSELF, at the three TANGENCY POINTS.                ***")
print("   Check against prop:twoalpha(iii)'s tangency points, which are a statement in the EQUATORIAL")
print("   PROJECTION -- the projected hinge triangle, vertices at transverse 2.alpha, sides tangent to")
print("   the throat circle AT THEIR MIDPOINTS:")
proj=[np.array([2*np.cos(np.radians(d)), 2*np.sin(np.radians(d))]) for d in (0,120,240)]
_mids=[]                                       # r2376+c54.159: keep prop:twoalpha(iii)'s midpoints
for i in range(3):
    m=(proj[i]+proj[(i+1)%3])/2
    _mids.append(m)
    print(f"     midpoint of projected side {i}: ({m[0]:+.6f},{m[1]:+.6f})   |m| = {np.linalg.norm(m):.6f} = alpha")
# r2376+c54.159 -- PINS D2's punchline, the "SAME THREE POINTS": the tangency midpoints of the
# projected hinge triangle are at |m| = alpha = 1.000000 and, AS A SET, are exactly the three
# opposite-edge crossings of the skew hexagon computed above.  (a) and (c) are one triple.
assert all(abs(np.linalg.norm(m) - 1.0) < 1e-12 for m in _mids), _mids
_key = lambda v: (round(float(v[0]),9)+0.0, round(float(v[1]),9)+0.0)
assert sorted(_key(m) for m in _mids) == sorted(_key(X[1:]) for X in _cross3), (_mids, _cross3)
print("\n   *** SAME THREE POINTS. ***  So one triple wears three faces:")
print("     (a) the tangency points of the projected hinge triangle      -- prop:twoalpha(iii), the corpus's")
print("     (b) the vertices of the CONTACT TRIANGLE, the hinge figure's DUAL   -- D1")
print("     (c) the crossings of the skew hexagon's OPPOSITE EDGES              -- D2, here")
print("   The corpus had (a) and read it as a set of midpoints.")
print("="*78)
