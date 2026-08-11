"""
U5 — THE EXCIRCLES. (r1110)  Named unrun in euclid7_nine_point.py; run here.

THE QUESTION, as it was named:
    Feuerbach's theorem says the nine-point circle is tangent to the incircle AND to the
    three EXCIRCLES. Here the nine-point circle IS the throat and the incircle IS the throat
    (both radius a, centre O) -- so that half of Feuerbach DEGENERATES to identity. But the
    excircles are NOT degenerate with anything. For the equilateral hinge triangle they sit
    at 3a with radius 3a.

    ** A THIRD SCALE, IN A CONSTRUCTION THAT HAS INSISTED ON EXACTLY ONE. **

    The whole ledger's claim is "one input, and the input is the gauge." If a classical
    theorem forces a length of 3a into the figure, either it is a of a, or the claim needs
    qualifying. Nobody has asked. Asking.

COULD THIS RETURN OTHERWISE? Yes, and both ways are live:
  (a) the excircle radius could fail to be a clean multiple of a -- it is not obviously 3a,
      that is a claim to check, not a given;
  (b) Feuerbach's tangency could fail numerically, which would mean the identification of
      the nine-point circle with the throat is wrong somewhere;
  (c) the excircles could turn out to be a-derived (a re-reading, no new scale) or NOT
      (a genuine second scale, which would be a real dent in the ledger's headline).
The receipt is written so (c) can return either answer.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def X0(P):
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12: return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]
A, B, C = hinges

def side(P, Q): return np.linalg.norm(P-Q)

print("="*80)
print("1. THE HINGE TRIANGLE'S CLASSICAL CIRCLES")
print("="*80)
sa, sb, sc = side(B, C), side(C, A), side(A, B)
s = (sa+sb+sc)/2
area = abs((B-A)[0]*(C-A)[1] - (B-A)[1]*(C-A)[0])/2
R  = sa*sb*sc/(4*area)          # circumradius
r_in = area/s                   # inradius
print(f"  side length          = {sa:.9f}   = sqrt3 * 2a = {S3*2*a:.9f}")
print(f"  circumradius R       = {R:.9f}   = 2a          ** the hinge's placement **")
print(f"  inradius r           = {r_in:.9f}   = a           ** the throat **")
print(f"  nine-point radius    = {R/2:.9f}   = a           ** the throat, again (euclid7) **")
assert abs(R - 2*a) < 1e-12 and abs(r_in - a) < 1e-12

print("\n" + "="*80)
print("2. THE EXCIRCLES -- computed, not assumed")
print("="*80)
# exradius opposite vertex A: r_A = area/(s - a_side)
ex_r = [area/(s - x) for x in (sa, sb, sc)]
# excentre opposite A: (-sa*A + sb*B + sc*C)/(-sa+sb+sc)
def excentre(P, Q, Rr, p, q, r):
    return (-p*P + q*Q + r*Rr)/(-p+q+r)
ex_c = [excentre(A, B, C, sa, sb, sc),
        excentre(B, C, A, sb, sc, sa),
        excentre(C, A, B, sc, sa, sb)]
for i, (c_, r_) in enumerate(zip(ex_c, ex_r)):
    print(f"  excircle {i}: centre ({c_[0]:+.6f}, {c_[1]:+.6f})   |centre| = {np.linalg.norm(c_):.9f}   radius = {r_:.9f}")
for r_ in ex_r:
    assert abs(r_ - 3*a) < 1e-9
for c_ in ex_c:
    assert abs(np.linalg.norm(c_) - 4*a) < 1e-9
print(f"""
  ** ALL THREE: radius exactly 3a -- and centres at 4a, NOT 3a. **

  ** THE NAMED VALUE WAS HALF WRONG, AND IT WAS MINE. ** euclid7_nine_point.py wrote
  "they sit at 3a with radius 3a". The radius is 3a; the centres are at 4a. I asserted the
  centre distance from inference and never computed it. Caught here by the receipt, which is
  face 35's own prescription: put the verdict inside the assert, where it can fail.
  (For an equilateral triangle the excentre opposite a vertex is at -A+B+C, i.e. the
  antipode of that vertex through O scaled by 2 -- |excentre| = 2R = 4a. A fact about
  equilateral triangles, and one line of algebra I skipped.)""")

print("\n" + "="*80)
print("3. FEUERBACH -- does the throat actually touch them? (a real test: if it fails,")
print("   euclid7's 'the nine-point circle IS the throat' is wrong somewhere)")
print("="*80)
print("  the throat: centre O, radius a.  each excircle: centre at 4a, radius 3a.")
print(f"\n  {'excircle':>9} {'|centre|':>10} {'r_ex + r_throat':>16} {'r_ex - r_throat':>16}  verdict")
for i, (c_, r_) in enumerate(zip(ex_c, ex_r)):
    d = np.linalg.norm(c_)
    ext = abs(d - (r_ + a)) < 1e-9          # externally tangent
    inte = abs(d - abs(r_ - a)) < 1e-9      # internally tangent
    v = "EXTERNAL" if ext else ("INTERNAL" if inte else "NOT TANGENT")
    print(f"  {i:>9} {d:>10.6f} {r_+a:>16.6f} {abs(r_-a):>16.6f}  ** {v} **")
    assert ext
print("""
  ** ALL THREE: EXTERNALLY TANGENT. |centre| = 4a = 3a + a = r_ex + r_throat, exactly. **
  The throat and each excircle sit OUTSIDE one another and touch at a single point. (Not
  internal -- that would need |centre| = r_ex - r_throat = 2a, and it is 4a.)""")
print(f"\n  {'excircle':>9} {'tangency point':>26} {'|point|':>10}  on the throat?")
for i, (c_, r_) in enumerate(zip(ex_c, ex_r)):
    u = c_/np.linalg.norm(c_)
    P = c_ - r_*u                          # the excircle's point nearest O, along the centre line
    print(f"  {i:>9} ({P[0]:+.6f}, {P[1]:+.6f}) {np.linalg.norm(P):>10.6f}  "
          f"{'** YES **' if abs(np.linalg.norm(P) - a) < 1e-9 else 'no'}")
    assert abs(np.linalg.norm(P) - a) < 1e-9
print("""
  ** Each excircle touches the throat at exactly one point, on the line from O through its
  excentre, at |P| = a. Feuerbach's excircle tangency HOLDS -- and it is a second, independent
  confirmation of euclid7: if the nine-point circle were not the throat, this would fail. **""")

print("\n" + "="*80)
print("4. ** THE QUESTION U5 WAS ASKED: IS 3a A THIRD SCALE? **")
print("="*80)
print("""  For ANY triangle: r_ex(A) = area/(s - a_side), and for an EQUILATERAL triangle of
  circumradius R this reduces to r_ex = 3 * r_in = 3 * (R/2). So:

        r_ex = 3 * R/2 = 3a   BECAUSE   R = 2a   BECAUSE   the hinge is at 2a.

  ** IT IS NOT A NEW SCALE. IT IS 3 x (R/2), AND R/2 IS THE THROAT. **
  The 3 is the triangle's own -- the equilateral exradius/inradius ratio, a fact about
  3-fold symmetry and nothing else. Check that the ratio is exactly 3 and that it tracks R:""")
print(f"\n  {'R (hinge placement)':>21} {'r_in = R/2':>12} {'r_ex':>10} {'r_ex/r_in':>11}")
for RR in [1.0, 2.0, 3.0, 5.0]:
    V = [np.array([RR*np.cos(t), RR*np.sin(t)]) for t in np.radians([0, 120, 240])]
    ss = [side(V[1],V[2]), side(V[2],V[0]), side(V[0],V[1])]
    sp = sum(ss)/2; ar = abs((V[1]-V[0])[0]*(V[2]-V[0])[1] - (V[1]-V[0])[1]*(V[2]-V[0])[0])/2
    rin = ar/sp; rex = ar/(sp - ss[0])
    print(f"  {RR:>21.4f} {rin:>12.6f} {rex:>10.6f} {rex/rin:>11.6f}")
    assert abs(rex/rin - 3.0) < 1e-9
print("""
  ** The ratio is 3 at EVERY R -- it is the equilateral triangle's, not the construction's.
  So 3a is a * (2/2) * 3: the gauge, times the hinge's own 2, times the triangle's own 3.
  NO NEW SCALE. The ledger's headline survives, and it survives by computation rather than
  by assertion, which is the point of asking. **""")

print("\n" + "="*80)
print("5. WHAT THE EXCIRCLES ARE, IN THE EMBEDDING -- the reading, and its bound")
print("="*80)
print(f"  {'object':>26} {'|X|':>9} {'X0':>12}")
print(f"  {'the throat (waist)':>26} {a:>9.4f} {X0(np.array([a,0.0])):>12.4f}")
print(f"  {'a hinge':>26} {2*a:>9.4f} {X0(hinges[0]):>12.6f}   = sqrt3 a")
for i, c_ in enumerate(ex_c[:1]):
    print(f"  {'an excentre':>26} {np.linalg.norm(c_):>9.4f} {X0(c_):>12.6f}   = sqrt15 a")
print(f"  {'an excircle tangency pt':>26} {a:>9.4f} {0.0:>12.4f}   = on the waist")
ex0 = ex_c[0]
print(f"""
  The excentres sit at |X| = 4a, so X0 = sqrt(16-1) a = {X0(ex0):.6f} a = sqrt15 a. They are
  REAL points of the overhead -- far higher than the hinges (sqrt3 a). And each excircle
  touches the waist at exactly one point.

  ** THE BOUND, and it is face 35's guard applied to this receipt (r1110). **
  What is COMPUTED: the excircle radii, centres, and their tangency to the throat; and that
  3a is a-derived and not a new scale.
  What is NOT computed, and must not be inferred from the above: any PHYSICAL reading of the
  excircles. This receipt's question quantified over LENGTHS IN THE OVERHEAD. It says nothing
  about whether an excircle is a slicing, a horizon, a locus, or anything else -- because no
  cut, no dial, no f, and no 2M appears anywhere in it. To ask that is a different receipt.

  NAMED, UNRUN (the honest successor): does the excircle appear in the DIAL? A plane through
  a hinge at perpendicular distance d has a physical regime fixed by d alone (the_isometry).
  The excircles are not planes and no d has been assigned to them. Whether they are visible
  to the dial at all is unasked.""")

print("\n" + "="*80)
print("WHAT U5 RETURNED")
print("="*80)
print("""  ** ANSWERED: 3a IS NOT A THIRD SCALE. **
    r_ex = 3 * r_in = 3 * (R/2) = 3a, and the ratio 3 is the EQUILATERAL TRIANGLE'S OWN
    (verified: exactly 3 at every R, so it tracks the triangle's symmetry and not this
    construction). 3a = the gauge x the hinge's 2 x the triangle's 3. The ledger's headline
    -- "one input, and the input is the gauge" -- survives, by computation.

  PROVED (this receipt):
    * the hinge triangle: circumradius 2a, inradius a, nine-point radius a, exradii 3a,
      excentres at ** 4a ** (= 2R, equilateral) -- every one a-derived
    * Feuerbach's EXCIRCLE half HOLDS: each excircle touches the throat at exactly one point,
      on the line from O through its excentre, at |P| = a. So euclid7's identification of the
      nine-point circle with the throat is confirmed from a second direction -- if it were
      wrong, this tangency would fail.
    * Feuerbach here is therefore HALF degenerate and half not: the incircle half collapses to
      identity (both circles ARE the throat); the excircle half is an honest tangency.
    * the excentres are real overhead points at X0 = sqrt15 a -- ** far higher than the hinges **
    * ** AND euclid7's "they sit at 3a with radius 3a" IS CORRECTED HERE: the RADIUS is 3a,
      the CENTRES are at 4a. ** I inferred the centre distance and never computed it. The
      assert caught it. Face 35, on this session's own hand, one turn after banking it.

  BOUNDED (face 35, this session's own guard, applied to itself):
    this receipt quantifies over LENGTHS IN THE OVERHEAD. It licenses no physical reading of
    the excircles. No cut, no dial, no f, no 2M appears in it.

  NAMED, UNRUN: whether the excircles are visible to the DIAL at all. They are not planes;
  no d has been assigned. Unasked.""")
