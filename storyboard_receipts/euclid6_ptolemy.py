"""
THE EUCLID PROTOCOL, candidate 6: PTOLEMY. (r1110)

THE PROTOCOL (Daryl, r1108): take a classical theorem about circles, chords, tangents and
triangles in the plane; read it on the throat's overhead; carry it back up the embedding;
and the signature does the rest.

Outputs so far -- and note what they have in common:
  * Euclid III tangent-secant  ==  the NULL condition                (power_is_null.py)
  * the triple-angle identity  ==  Nariai                            (one_thirty.py)
  * pole & polar               ==  the hinge's horizon               (euclid3_pole_polar.py)
  * the radical axis           ==  that horizon, independently        (euclid4_radical_axis.py)
  * inversion                  ==  power = height; Thales -> horizon (euclid5_inversion.py)

Every metric fact so far has come back NULL. That is the pattern, and a pattern is a thing
to test, not to extend.

CANDIDATE 6. PTOLEMY: for a cyclic quadrilateral ABCD, AC*BD = AB*CD + BC*AD. A pure METRIC
identity on four concyclic points -- the most Euclidean object on the list.

THE PREDICTION, NAMED BEFORE RUNNING (this is the falsifier for the pattern itself):
    Ptolemy on the THROAT must stay SPACELIKE and return nothing.
    The throat is X0 = 0. Every chord of it has dX0 = 0, so ds^2 = |dX|^2 > 0 -- spacelike,
    every one. A theorem about chords of the throat CANNOT become a null statement. If the
    protocol returns null here it is the protocol that is wrong, not the geometry.

    Ptolemy on the THALES circle is the one that can bite, because that circle carries points
    at DIFFERENT heights: the hinge at X0 = sqrt3 a, the tangent points at X0 = 0, and the
    hole's centre at no height at all.

COULD THIS RETURN OTHERWISE? Yes, both ways: the identity holds numerically or it does not,
and the spacelike/null verdict is read off the computed ds^2, not asserted.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def X0(P):
    s = np.dot(P, P) - a**2
    return np.sqrt(s) if s >= 0 else float('nan')

def ds2(P, Q):
    """embedding interval between two overhead points, each lifted to its own height."""
    return -(X0(P) - X0(Q))**2 + np.dot(P-Q, P-Q)

def ptolemy(A, B, C, D):
    d = lambda P, Q: np.linalg.norm(P-Q)
    return d(A,C)*d(B,D), d(A,B)*d(C,D) + d(B,C)*d(A,D)

O  = np.array([0.0, 0.0])
A  = np.array([2*a, 0.0])                                  # the hinge
Tp = a*np.array([np.cos(np.radians(60)),  np.sin(np.radians(60))])   # tangent point +
Tm = a*np.array([np.cos(np.radians(-60)), np.sin(np.radians(-60))])  # tangent point -
PIN = np.array([0.8*a, 0.6*a])                             # the pin, on the throat
POLE = np.array([0.0, a])

print("="*80)
print("1. PTOLEMY ON THE THROAT -- the prediction says it must stay SPACELIKE")
print("="*80)
quad = [np.array([a,0.0]), PIN, POLE, np.array([-a,0.0])]   # four of the eight throat points
lhs, rhs = ptolemy(*quad)
print(f"  four concyclic points of the throat (beta = 0, 36.87, 90, 180):")
for P in quad:
    print(f"    ({P[0]:+.4f},{P[1]:+.4f})   |P| = {np.linalg.norm(P):.6f}   X0 = {X0(P):.6f}")
print(f"\n  Ptolemy:  AC*BD = {lhs:.9f}   AB*CD + BC*AD = {rhs:.9f}   diff {abs(lhs-rhs):.1e}")
assert abs(lhs-rhs) < 1e-12
print("  ** holds exactly -- as it must; they are concyclic by construction. **")
print(f"\n  and every chord of the throat, lifted:")
for (P, Q, nm) in [(quad[0], PIN, "0 -> pin"), (PIN, POLE, "pin -> pole"), (quad[0], quad[3], "0 -> 180")]:
    s = ds2(P, Q)
    print(f"    {nm:>14}   ds^2 = {s:+.6f}   {'SPACELIKE' if s > 1e-12 else '??'}")
    assert s > 1e-12
print("""
  ** PREDICTION CONFIRMED, AND IT IS A NEGATIVE. ** Every chord of the throat is spacelike,
  because the throat is the waist: X0 = 0 on all of it, so dX0 = 0 and ds^2 = |dX|^2 > 0.
  Ptolemy on the throat is a Euclidean identity that STAYS Euclidean. The protocol returns
  nothing here, and it cannot: there is no minus sign to put in.

  >>> THE PROTOCOL'S BOUNDARY, FOUND: a classical theorem translates only if its points
      sit at DIFFERENT HEIGHTS. On the waist, Euclid is just Euclid. <<<""")

print("\n" + "="*80)
print("2. PTOLEMY ON THE THALES CIRCLE -- where the heights differ, and it bites")
print("="*80)
print("  the Thales circle carries points at three different heights:")
for (P, nm) in [(A, "the hinge"), (Tp, "tangent point +"), (O, "the hole's centre"), (Tm, "tangent point -")]:
    on = abs(np.linalg.norm(P - np.array([a,0.0])) - a)
    print(f"    {nm:>18}  ({P[0]:+.4f},{P[1]:+.4f})   on Thales: {on:.1e}   X0 = {X0(P)}")
    assert on < 1e-12
# cyclic order around the Thales circle: A(0 deg), Tp(120), O(180), Tm(240)
lhs, rhs = ptolemy(A, Tp, O, Tm)
print(f"\n  cyclic order A, T+, O, T-:")
print(f"    AC*BD        = |OA| * |T+T-|      = {lhs:.9f}")
print(f"    AB*CD+BC*AD  = |AT+|*|OT-| + |T+O|*|AT-| = {rhs:.9f}   diff {abs(lhs-rhs):.1e}")
assert abs(lhs-rhs) < 1e-12
d = lambda P,Q: np.linalg.norm(P-Q)
print(f"""
  and every one of those five lengths is a named object of the construction:
    |OA|   = {d(O,A):.6f} = 2a          the hinge's placement
    |T+T-| = {d(Tp,Tm):.6f} = sqrt3 a   ** THE HORIZON CHORD ** (cands 3/4/5: x = a/2)
    |AT+|  = {d(A,Tp):.6f} = sqrt3 a   ** THE TANGENT ** -- null (power_is_null.py)
    |AT-|  = {d(A,Tm):.6f} = sqrt3 a   the other tangent
    |OT+|  = {d(O,Tp):.6f} = a          the throat radius
    |OT-|  = {d(O,Tm):.6f} = a

  so Ptolemy here reads   2a * sqrt3 a  =  sqrt3 a * a  +  a * sqrt3 a
  -- true, and it is the SAME statement twice, because |AT+| = |AT-| = |T+T-|.""")

print("\n" + "="*80)
print("3. ** THE FINDING ** -- THE HORIZON CHORD, THE TANGENT, AND THE HEIGHT ARE ONE LENGTH")
print("="*80)
L   = np.sqrt(np.dot(A,A) - a**2)
print(f"  the horizon chord  |T+T-|        = {d(Tp,Tm):.9f}")
print(f"  the tangent length |AT+|         = {d(A,Tp):.9f}")
print(f"  the hinge's height X0(A)         = {X0(A):.9f}")
print(f"  sqrt(power) of the hinge         = {L:.9f}")
for v in [d(A,Tp), X0(A), L]:
    assert abs(d(Tp,Tm) - v) < 1e-12
print(f"""
  ** FOUR THINGS, ONE NUMBER: sqrt3 a. **  This EXTENDS tab11 (which had
  60 deg = arctan sqrt3 = X0/a = L_tan/a = sqrt(power)/a) by one more member -- the HORIZON
  CHORD -- and that one is new, because cands 3/4/5 found WHERE the horizon is and never
  measured HOW LONG it is.

  AND THE TWO ARE OF OPPOSITE SIGNATURE, WHICH IS THE CONTENT:""")
print(f"    the tangent A -> T+ : ds^2 = {ds2(A,Tp):+.3e}   ** NULL **      (drops sqrt3 a, runs sqrt3 a)")
print(f"    the chord  T+ -> T- : ds^2 = {ds2(Tp,Tm):+.9f}   ** SPACELIKE ** (drops 0, runs sqrt3 a)")
assert abs(ds2(A,Tp)) < 1e-12 and ds2(Tp,Tm) > 1e-12
print("""
  >>> THE HINGE'S HORIZON IS EXACTLY AS LONG, SPACELIKE, AS ITS LIGHT RAY IS, NULL. <<<
  The same number sqrt3 a is the hinge's DROP (timelike), its light ray's REACH (null), and
  its horizon's WIDTH (spacelike). One length wearing all three signatures -- which is what
  a light cone IS, written in Ptolemy's own quantities.""")

print("\n" + "="*80)
print("THE FALSIFIER -- must fail off 2a, or it is a fact about circles and not about alpha")
print("="*80)
print(f"  {'|hinge|':>9} {'horizon chord':>15} {'tangent':>10} {'height':>10}  all equal?")
found = []
for R in [1.4, 1.7, 2.0, 2.4, 3.0]:
    H = np.array([R, 0.0])
    al = np.arccos(a/R)
    tp = a*np.array([np.cos(al), np.sin(al)]); tm = a*np.array([np.cos(al), -np.sin(al)])
    ch, tg, ht = d(tp,tm), d(H,tp), X0(H)
    eq = abs(ch-tg) < 1e-9 and abs(ch-ht) < 1e-9
    if eq: found.append(R)
    print(f"  {R:>9.4f} {ch:>15.6f} {tg:>10.6f} {ht:>10.6f}  {'** YES **' if eq else 'no'}")
print(f"\n  the three lengths coincide only at |hinge| = {found}")
assert found == [2.0]
print("  ** Only at 2a. It is alpha doing it, once more, not a generic fact about circles. **")

print("\n" + "="*80)
print("WHAT CANDIDATE 6 RETURNED")
print("="*80)
print("""  ** THE PROTOCOL'S BOUNDARY, and it is the first one found: **
    Ptolemy on the THROAT is a Euclidean identity that STAYS Euclidean. Every chord of the
    waist is spacelike (X0 = 0 on all of it, so dX0 = 0), so there is no minus sign to put
    in. A classical theorem translates ONLY IF ITS POINTS SIT AT DIFFERENT HEIGHTS. On the
    waist, Euclid is just Euclid. The prediction was named before the run and it held.

  PROVED (this receipt), on the Thales circle, where the heights DO differ:
    * ** the horizon chord, the tangent, and the hinge's height are ONE LENGTH: sqrt3 a. **
      This extends tab11 by a new member. Cands 3/4/5 found WHERE the horizon is; none of
      them measured HOW LONG it is.
    * and the same number carries all three signatures: sqrt3 a is the hinge's DROP
      (timelike), its light ray's REACH (null: ds^2 = 0 exactly), and its horizon's WIDTH
      (spacelike: ds^2 = +3a^2). >>> THE HINGE'S HORIZON IS EXACTLY AS LONG, SPACELIKE, AS
      ITS LIGHT RAY IS, NULL. <<< That is a light cone written in Ptolemy's own quantities.
    * falsifier: the three lengths coincide only at |hinge| = 2a. Alpha, once more.

  AND THE PATTERN IS NOW BOUNDED, WHICH IS WORTH MORE THAN ANOTHER CONFIRMATION.
  Five candidates returned null. This one says WHY, and where it stops: the protocol works
  on objects that span heights, and returns Euclid unchanged on objects that do not. The
  minus sign can only enter where there is a dX0 for it to act on.""")
