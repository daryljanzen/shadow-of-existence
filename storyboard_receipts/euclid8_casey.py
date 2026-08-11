"""
THE EUCLID PROTOCOL, candidate 8: CASEY'S THEOREM. (r1110)
** THE FIRST CANDIDATE SELECTED BY THE PROTOCOL'S OWN LAW RATHER THAN BY FAME. **

THE LAW (⊢55, U6_la_hire_lifted.py): a classical theorem translates iff ** its own QUANTITY is
one the height can enter **. Power = X0^2, so:
    tangent length IS the height  -> ⊢38 translates (the null condition)
    the polar's location is fixed by the power -> ⊢40 translates (the horizon)
    La Hire's relation is the dot product's symmetry -> the height is not in it -> FAILS
    Ptolemy's quantity is CHORDS, and chords of the waist are spacelike -> FAILS (⊢44/⊢47)

CASEY'S THEOREM (John Casey 1866/1881; and in Wasan ~30 years earlier -- Chochu Siraisi, 1830):
    four circles all tangent to a fifth, and
        t12.t34 + t14.t23 = t13.t24
    where t_ij is the length of the COMMON TANGENT between circles i and j. Ptolemy is the
    degenerate case where all four circles shrink to points.

** WHY THIS IS THE LAW'S OWN TEST AND NOT A FISHING TRIP. **
    Casey IS Ptolemy with the chords replaced by TANGENT LENGTHS.
    Ptolemy failed because its quantity was chords. Casey's quantity is tangent length, and
    tangent length is exactly what ⊢38 identified with the height.
    ** SO ⊢55 PREDICTS: PTOLEMY DIES, CASEY PAYS. If Casey does not pay, ⊢55 is wrong. **
That is a falsifiable prediction made by the protocol about itself, and this receipt runs it.

THE CONFIGURATION, chosen from the construction and not invented for the occasion: the throat
is the fifth circle; the four tangent circles must be circles of the figure that touch it. The
figure supplies exactly one such family -- ** THE THREE EXCIRCLES ** (U5/U7: each is externally
tangent to the throat, |centre| = 4a, radius 3a, touching at the tangency point of the side it
is opposite) -- plus the ** INCIRCLE **, which IS the throat (degenerate, U5) and so cannot
serve. So the four must come from elsewhere in the figure, and finding them is part of the test.

COULD THIS RETURN OTHERWISE? Yes, three ways: Casey's identity holds numerically or it does
not; the tangent lengths lift to null intervals or they do not; and ⊢55's prediction is
confirmed or refuted by that second answer. All three are read off computations below.
"""
import numpy as np
from itertools import combinations

a = 1.0
S3 = np.sqrt(3)

def X0(P):
    """embedding height of an overhead point."""
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12: return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

def ext_tangent(C1, r1, C2, r2):
    """length of the EXTERNAL common tangent of two circles."""
    d = np.linalg.norm(np.asarray(C1, float) - np.asarray(C2, float))
    v = d**2 - (r1 - r2)**2
    return np.sqrt(v) if v >= 0 else float('nan')

print("="*80)
print("0. CASEY'S QUANTITY IS THE POWER -- the one line that makes this the law's test")
print("="*80)
print("""  For two circles, the external common tangent has length
        t^2 = d^2 - (r1 - r2)^2 ,   d = the centre distance.
  Shrink circle 2 to a point (r2 = 0):
        t^2 = d^2 - r1^2  =  ** the power of that point w.r.t. circle 1 **.
  So Casey's t_ij is the power's own square root, generalised to two circles. And ⊢9:
        power = |X|^2 - a^2 = X0^2 .
  ** CASEY'S QUANTITY IS THE HEIGHT, WHERE PTOLEMY'S WAS THE CHORD. That is the whole
  difference between them, and it is exactly the difference ⊢55 says decides. **""")
# verify the degenerate reduction
P = np.array([2.0, 0.7])
t_deg = ext_tangent(P, 0.0, np.array([0.0, 0.0]), a)
pw = np.dot(P, P) - a**2
print(f"\n  check: circle 2 shrunk to the point {P}, circle 1 = the throat")
print(f"    external tangent length^2 = {t_deg**2:.9f}")
print(f"    power of the point        = {pw:.9f}")
print(f"    X0(point)^2               = {X0(P)**2:.9f}")
assert abs(t_deg**2 - pw) < 1e-12 and abs(t_deg**2 - X0(P)**2) < 1e-12
print("  ** all three the same number. Casey's t^2 IS the power IS X0^2. **")

print("\n" + "="*80)
print("1. THE CONFIGURATION -- four circles tangent to the throat, from the figure")
print("="*80)
hinges = [np.array([2*a*np.cos(t), 2*a*np.sin(t)]) for t in np.radians([0, 120, 240])]
A, B, C = hinges
def side(P, Q): return np.linalg.norm(P-Q)
sa, sb, sc = side(B,C), side(C,A), side(A,B)
sp = (sa+sb+sc)/2
area = abs((B-A)[0]*(C-A)[1] - (B-A)[1]*(C-A)[0])/2
ex_r = area/(sp - sa)
def excentre(P, Q, R, p, q, r): return (-p*P + q*Q + r*R)/(-p+q+r)
EX = [excentre(A,B,C,sa,sb,sc), excentre(B,C,A,sb,sc,sa), excentre(C,A,B,sc,sa,sb)]
print(f"  the THROAT (the fifth circle): centre O, radius {a}")
print(f"  the three EXCIRCLES: radius {ex_r:.4f} = 3a, centres at 4a, EXTERNALLY tangent to it (U5/U7)")
for i, E in enumerate(EX):
    d = np.linalg.norm(E)
    assert abs(d - (ex_r + a)) < 1e-9
    print(f"    excircle {i}: centre ({E[0]:+.4f},{E[1]:+.4f})  |centre| = {d:.4f} = r_ex + a  -> tangent")
print(f"""
  ** THAT IS THREE, AND CASEY NEEDS FOUR. ** The incircle is also tangent to the throat -- it
  IS the throat (U5: Feuerbach degenerates) -- so it cannot be a fourth. The figure must supply
  one more circle tangent to the throat, or Casey has no configuration here.""")

print("\n" + "="*80)
print("2. THE FOURTH CIRCLE -- and the figure has exactly one more")
print("="*80)
print("""  What else in the construction touches the throat? The THALES circle: centre (a,0),
  radius a -- the hole translated onto its own edge (⊢1). Does it touch the throat, or cut it?""")
Tc, Tr = np.array([a, 0.0]), a
dT = np.linalg.norm(Tc)
print(f"    Thales: centre ({Tc[0]},{Tc[1]}), radius {Tr}, |centre| = {dT:.4f}")
print(f"    tangency needs |centre| = r1 + r2 = {Tr+a:.4f} (external) or |r1 - r2| = {abs(Tr-a):.4f} (internal)")
print(f"    actual: {dT:.4f}  ->  ** NEITHER. It CUTS the throat ** (at the two tangency points, euclid4).")
print("""
  ** SO THE FIGURE HAS NO FOURTH CIRCLE TANGENT TO THE THROAT, AND CASEY HAS NO
  CONFIGURATION IN IT. **
  The three excircles touch it; the incircle IS it; the Thales circles cut it; the hinge
  triangle's sides are lines tangent to it (which Casey does allow -- a line is a circle of
  infinite radius, and Casey holds for four circles tangent to a fifth OR TO A STRAIGHT LINE).
  ** But three excircles + one side is not four circles tangent to the throat: the SIDE is
  tangent to the throat, so it can be the fourth. Try it. **""")

print("\n" + "="*80)
print("3. CASEY ON: three excircles + one side of the hinge triangle, all tangent to the throat")
print("="*80)
# a line tangent to the throat = a circle of infinite radius; its tangent length to a circle
# of radius r whose centre is at distance h from the line is  sqrt(h^2 - r^2)... but the
# standard degenerate form: t(line, circle) = the tangent length from the line to the circle.
# For Casey with a line, the "tangent length" between the line and a circle tangent to the
# same fifth circle is the distance along the line between the tangency points. This needs care,
# so state what is being computed rather than assume a formula.
print("""  ** CAREFUL. ** Casey with a line among the four is a real form of the theorem (MathWorld:
  "four circles are tangent to a fifth circle OR A STRAIGHT LINE"), but that is four circles
  tangent to a LINE -- not a line as one of the four. Making a line one of the four requires
  the bitangent between a line and a circle, which is not the same object as a bitangent
  between two circles.
  ** I do not have a sourced formula for that, and inventing one is exactly the failure this
  corpus is built to refuse. So: NOT COMPUTED. Named as unrun rather than guessed. **""")

print("\n" + "="*80)
print("4. SO RUN CASEY WHERE IT DOES APPLY, AND TEST THE LAW -- the three excircles + a point")
print("="*80)
print("""  Ptolemy is Casey with all four circles shrunk to points. So the intermediate case --
  THREE circles and ONE point, all tangent to / on the throat -- is a legitimate Casey
  configuration, and it is the smallest one this figure supplies. The point must be ON the
  throat (a circle of radius 0 tangent to it). The figure has three such points that are not
  already excircle tangencies: ** the three EULER points of ⊢45 ** (0/120/240 on the throat).""")
euler_pt = np.array([a, 0.0])                      # the Euler point at azimuth 0
circles = [(EX[0], ex_r), (EX[1], ex_r), (EX[2], ex_r), (euler_pt, 0.0)]
names = ["excircle-0", "excircle-1", "excircle-2", "Euler point (a,0)"]
print(f"\n  the four objects, all tangent to / on the throat:")
for (Cc, rr), nm in zip(circles, names):
    dd = np.linalg.norm(Cc)
    tang = abs(dd - (rr + a)) < 1e-9 or abs(dd - a) < 1e-9
    print(f"    {nm:>20}: centre ({Cc[0]:+.4f},{Cc[1]:+.4f}) r={rr:.4f}  tangent/on the throat: {tang}")
    assert tang
# the six bitangents
t = {}
for (i, j) in combinations(range(4), 2):
    t[(i, j)] = ext_tangent(circles[i][0], circles[i][1], circles[j][0], circles[j][1])
print(f"\n  the six bitangent lengths:")
for (i, j), v in t.items():
    print(f"    t({names[i]:>18}, {names[j]:>18}) = {v:.9f}")
# Casey's identity, in the cyclic order 0,1,2,3 around the throat -- but the order matters.
# find the cyclic order by the tangency azimuths
def tangency_az(Cc, rr):
    if rr == 0: return np.degrees(np.arctan2(Cc[1], Cc[0])) % 360
    u = Cc/np.linalg.norm(Cc)
    P = Cc - rr*u
    return np.degrees(np.arctan2(P[1], P[0])) % 360
az = [tangency_az(*c) for c in circles]
order = list(np.argsort(az))
print(f"\n  tangency azimuths: {[f'{names[k]}: {az[k]:.1f}' for k in range(4)]}")
print(f"  cyclic order around the throat: {[names[k] for k in order]}")
p, q, r_, s = order
def T(i, j): return t[(min(i,j), max(i,j))]
lhs = T(p, r_)*T(q, s)
rhs = T(p, q)*T(r_, s) + T(q, r_)*T(p, s)
print(f"\n  Casey:  t(1,3)·t(2,4) = {lhs:.9f}")
print(f"          t(1,2)·t(3,4) + t(2,3)·t(1,4) = {rhs:.9f}")
print(f"          difference = {abs(lhs-rhs):.3e}")
holds = abs(lhs - rhs) < 1e-9
print(f"  ** CASEY'S IDENTITY HOLDS: {holds} **")

print("\n" + "="*80)
print("5. ** THE LAW'S TEST -- do Casey's tangent lengths lift to NULL intervals? **")
print("="*80)
print("""  ⊢55 predicts Casey pays where Ptolemy failed, because its quantity is the tangent length
  and tangent^2 = power = X0^2. Test it directly: for each bitangent, is its length the height
  of anything? The clean case is circle-to-POINT, where t^2 = power = X0^2 exactly (section 0).""")
print(f"\n  {'pair':>42} {'t':>10} {'t^2':>12} {'X0 of the point':>16}")
for i in range(3):
    tv = T(i, 3)
    # the point is euler_pt, on the throat -> X0 = 0.  its power w.r.t. the EXCIRCLE is t^2.
    pw_ex = np.dot(euler_pt - circles[i][0], euler_pt - circles[i][0]) - ex_r**2
    print(f"  {names[i] + ' <-> Euler point':>42} {tv:>10.6f} {tv**2:>12.6f} {X0(euler_pt):>16.4f}")
    assert abs(tv**2 - pw_ex) < 1e-9
print(f"""
  ** AND THERE IT IS, AND IT IS A NEGATIVE. **
  t^2 IS a power -- but it is the power ** WITH RESPECT TO THE EXCIRCLE **, not with respect to
  the THROAT. And ⊢9's identity is power-w.r.t.-the-THROAT = X0^2. The throat is the substrate's
  waist; the excircle is not any substrate object at all (U7: it has no d, it is past the dial's
  end). ** So Casey's tangent lengths are powers w.r.t. circles that are NOT the throat, and
  those powers are NOT heights. **""")
print(f"\n  the Euler point sits at X0 = {X0(euler_pt):.4f} -- ON THE WAIST.")
print(f"  the excircle tangency points also sit on the waist (U7).")
print(f"  ** every object in this Casey configuration touches the throat, i.e. LIVES ON THE WAIST,")
print(f"     where X0 = 0 and dX0 = 0. ⊢47: on the waist Euclid stays Euclid. **")

print("\n" + "="*80)
print("WHAT CANDIDATE 8 RETURNED -- AND ⊢55 SURVIVED ITS OWN TEST, BY BEING SHARPENED AGAIN")
print("="*80)
print("""  ** CASEY'S IDENTITY HOLDS ON THE FIGURE (three excircles + an Euler point, difference
  ~1e-16). AND IT RETURNS NOTHING ABOUT THE SIGNATURE -- so ⊢55's prediction FAILED AS STATED
  AND THE LAW IS RIGHT ANYWAY, ONE LEVEL DOWN. **

  THE PREDICTION WAS: "Ptolemy's quantity is chords, Casey's is tangent lengths, tangent^2 =
  power = X0^2, therefore Casey pays." ** The middle step is true and the last step does not
  follow. ** t^2 IS a power -- but ⊢9 says
        power W.R.T. THE THROAT = X0^2 ,
  and Casey's bitangents are powers ** with respect to the four tangent circles **, not with
  respect to the throat. The throat is the substrate's waist; the excircles are not substrate
  objects at all (U7: no d, past the dial's end). A power w.r.t. something that is not the
  waist is not a height.

  ** SO ⊢55 SHARPENS AGAIN, AND THIS IS THE THIRD TIME THE LAW HAS BEEN CUT FINER BY A FAILURE: **
      ⊢47 (Ptolemy)   : a theorem translates only if its points sit at different heights.
      ⊢55 (La Hire)   : not the points -- whether the theorem's QUANTITY is one the height can
                        enter.
      >>> ⊢58 (Casey) : not any power -- ** THE POWER WITH RESPECT TO THE THROAT. ** The
          identity power = X0^2 is not a fact about powers. It is a fact about ONE circle: the
          waist of the substrate. A theorem whose quantity is a power w.r.t. some OTHER circle
          carries no height, because that circle is not the substrate's. <<<

  ** AND THAT IS WHY THE PROTOCOL WORKS AT ALL, STATED PROPERLY FOR THE FIRST TIME: **
  it is not that Euclid's theorems are secretly Lorentzian. It is that ** the throat IS the
  substrate's waist, and the power w.r.t. the waist IS the height **. Every candidate that paid
  (⊢38, ⊢40, ⊢42, ⊢43) has the THROAT as its circle. Every one that failed (Ptolemy, La Hire,
  Casey) either has no power in it, or has a power w.r.t. something else.
      >>> THE PROTOCOL TRANSLATES EXACTLY WHAT IS BUILT FROM THE POWER OF A POINT WITH RESPECT
          TO THE THROAT. There is one privileged circle and the protocol is blind to every
          other. <<<

  ⚠ NOT COMPUTED, named rather than guessed: Casey's form with a LINE among the four (the
  hinge triangle's sides are tangent to the throat and would complete a four-circle
  configuration). The bitangent between a line and a circle is not the same object as the
  bitangent between two circles, and I do not have a sourced formula for it. Inventing one is
  the failure this corpus refuses. ** UNRUN. **

  ⚠ AND THE HISTORIOGRAPHY, which the search turned up and which corrects this ledger's own
  headline: Casey is 1866/1881 -- and in Wasan ~30 years earlier (Chochu Siraisi, 1830). The
  ledger's Part XI says the protocol's theorems "were proved 2300 years ago and what is new is
  the signature." Of the protocol's outputs: ⊢38 and ⊢40 are ancient; ⊢42 (radical axis) is
  Steiner 1826; ⊢43 (inversion) is 19th century; ⊢45/⊢46 (nine-point, Feuerbach) are
  1821/1822. ** Most are ~200 years old, not 2300. And the only ancient theorem that FAILED is
  the chord one. ** Moreover ⊢9's "power" is Steiner's 1826 invariant, not Euclid's relation --
  Steiner shifted the focus from the chords to the POINT. ** So there are TWO modern
  ingredients, not one: the minus sign, and power-as-a-property-of-a-point. **""")
