"""
THE FULL-CORPUS SWEEP, question 2: IS THE SECANT'S DISCRIMINANT THE INTERVAL?  (r1115)

WHERE THIS CAME FROM. ⊢10's own bound says: "the power theorem is about SECANTS; the null
condition is the DEGENERATE CASE where the two points merge -- and the tangent is exactly
where the light cone is." And P1's whole result is a DEGENERACY of a different kind: the
event horizon is a metric singularity, where two events that are null-separated (ds^2=0) and
spatially coincident (dx=0) are assigned vanishing temporal separation -- two distinct,
causally ordered points the metric measures as ONE.

Two degeneracies, both described as "two things becoming one". ** That is exactly the shape of
a flavour-match (faces 18/19/26), so it is not to be asserted. It is to be computed. **

THE SETUP. A line through an external point P of the overhead, in direction u (a unit vector),
meets the throat |X| = alpha where
        |P + t u|^2 = alpha^2
    ->  t^2 + 2 t (P.u) + (|P|^2 - alpha^2) = 0
a quadratic in t. Its two roots are the secant's two intersection points, and their product is
    t+ t- = |P|^2 - alpha^2 = pow(P)                              <- Euclid, and Steiner
Its discriminant decides how many there are:
        D/4 = (P.u)^2 - (|P|^2 - alpha^2) = (P.u)^2 - pow(P)
    D > 0 : two points   (a secant)
    D = 0 : one point    (a tangent)
    D < 0 : none         (the line misses)

THE QUESTION. ⊢9 says pow(P) = X0^2, the square of P's height. So
        D/4 = (P.u)^2 - X0^2 .
And (P.u) is the distance along the line from P to the foot -- a SPATIAL run in the overhead --
while X0 is P's height, the TIME DROP to the throat (which sits at X0 = 0). So D/4 looks like
(spatial run)^2 - (time drop)^2, which is ds^2 with the sign the other way up.

    ** IS THE DISCRIMINANT OF EUCLID'S SECANT MINUS THE INTERVAL OF THE SEGMENT? **
    And if so: is Euclid's secant/tangent/miss trichotomy the timelike/null/spacelike one?

COULD THIS RETURN OTHERWISE? Yes, and the danger is real: (P.u) is a run in the OVERHEAD, and
the segment whose interval we want runs from P's LIFT to a point of the throat. Those are not
obviously the same length, and if they are not the identification is false. Checked below
rather than assumed.
"""
import numpy as np

a = 1.0
rng = np.random.default_rng(7)

def X0(P):
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12: return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

def lift(P):
    return np.array([X0(P), P[0], P[1]])

def ds2(A, B):
    d = np.asarray(B, float) - np.asarray(A, float)
    return -d[0]**2 + d[1]**2 + d[2]**2

print("="*80)
print("1. THE QUADRATIC, AND WHAT ITS PIECES ARE")
print("="*80)
P = np.array([2.0, 0.0])
print(f"  take P = the hinge = {P},  |P| = {np.linalg.norm(P)} = 2a")
print(f"  the line through P in direction u meets |X|=a where")
print(f"      t^2 + 2t(P.u) + (|P|^2 - a^2) = 0")
print(f"  product of roots  t+ t- = |P|^2 - a^2 = {np.dot(P,P)-a**2:.6f} = pow(P)   <- Euclid/Steiner")
print(f"  and pow(P) = X0(P)^2 = {X0(P)**2:.6f}                                     <- the hyperboloid")
assert abs((np.dot(P,P)-a**2) - X0(P)**2) < 1e-12
print("  ** the product of the secant's two roots IS the square of P's height. **")

print("\n" + "="*80)
print("2. ** THE TEST: is D/4 minus the interval? ** -- and the trap checked first")
print("="*80)
print("""  THE TRAP: (P.u) is a run in the OVERHEAD. The interval we want runs from P's LIFT (at
  height X0) to a point ON THE THROAT (at height 0). Is the overhead run the spatial part of
  that segment? It is -- because the lift adds only a time component, x_0, and leaves the two
  spatial components alone. So the spatial separation between lift(P) and lift(Q) IS |P - Q|
  in the overhead, for any Q. Verified before it is used:""")
for _ in range(3):
    Q = rng.uniform(-3, 3, 2)
    if np.linalg.norm(Q) < a: continue
    A, B = lift(P), lift(Q)
    spatial = np.sqrt((B[1]-A[1])**2 + (B[2]-A[2])**2)
    print(f"    |P-Q| overhead = {np.linalg.norm(P-Q):.9f}   spatial part of lift(P)->lift(Q) = {spatial:.9f}")
    assert abs(spatial - np.linalg.norm(P-Q)) < 1e-12
print("  ** confirmed. The lift is vertical; the overhead run IS the spatial run. **")

print("\n" + "="*80)
print("** A FALSE START, KEPT: I nearly measured to a point that is not on the manifold **")
print("="*80)
print("""  My first version computed ds^2 from lift(P) to the line's FOOT (the closest point to the
  axis), placed at height 0, and predicted D/4 = -ds^2. ** Both halves were wrong and the
  assert refused. ** The sign was backwards; and worse, ** off tangency the foot is not on the
  throat at all **, so putting it at height 0 puts it on no point of the substrate, and the
  "interval" to it measures nothing. The foot lies on the throat exactly when the line is
  tangent -- which is the one case the error could not detect.
  ** Kept per THE_CODA §"the negatives are the map": the tell was a prediction about a
  trichotomy made before checking that its two outer cases had objects to measure. **""")

print("\n" + "="*80)
print("2. THE HONEST OBJECT: the two INTERSECTIONS, which are on the throat by construction")
print("="*80)
print("""  The line meets |X| = a at t± = -(P.u) ± sqrt(D/4). Those two points ARE on the throat, so
  their lift sits at X0 = 0, and the interval from P's lift to each is
        ds^2(t) = -X0^2 + t^2 = t^2 - pow(P) = t^2 - t+ t- ,
  the last step being Euclid: ** the product of the secant's two segments IS the power **.""")
def cuts(P, u):
    """the two intersection parameters. NOTE the clamp: at exact tangency D/4 is ~-4e-16 in
    float, so a bare `if D4 < 0: return None` DROPS the tangency row -- the one row the whole
    point rests on. Clamp at the discretisation, not below it (CODA_FIELD_NOTE face 37)."""
    Pu = np.dot(P, u); D4 = Pu**2 - (np.dot(P,P) - a**2)
    if D4 < -1e-12: return None
    r = np.sqrt(max(D4, 0.0))
    return sorted([-Pu - r, -Pu + r], key=abs)
print(f"\n  P = the hinge {P}, X0 = {X0(P):.6f} = sqrt3 a, pow = {np.dot(P,P)-a**2:.6f} = 3a^2")
print(f"\n  {'angle':>7} {'t- (near)':>11} {'t+ (far)':>11} {'t-·t+':>9} {'ds²(near)':>11} {'ds²(far)':>11}  near / far")
rows = []
for deg in [0, 10, 20, 25, 29, 30]:
    u = np.array([np.cos(np.radians(180+deg)), np.sin(np.radians(180+deg))])
    tt = cuts(P, u)
    if tt is None: continue
    tm, tp = tt
    A = P + tm*u; B = P + tp*u
    s_near = ds2(lift(P), np.array([0.0, A[0], A[1]]))
    s_far  = ds2(lift(P), np.array([0.0, B[0], B[1]]))
    cn = "timelike" if s_near < -1e-9 else ("NULL" if abs(s_near) < 1e-9 else "spacelike")
    cf = "timelike" if s_far  < -1e-9 else ("NULL" if abs(s_far)  < 1e-9 else "spacelike")
    rows.append((s_near, s_far, cn, cf))
    print(f"  {deg:>7} {tm:>11.6f} {tp:>11.6f} {tm*tp:>9.6f} {s_near:>11.6f} {s_far:>11.6f}  {cn} / {cf}")
    assert abs(tm*tp - (np.dot(P,P)-a**2)) < 1e-9
print("""
  ** t-·t+ = pow at every angle -- Euclid III.36, holding. **
  ** AND THE TWO INTERSECTIONS STRADDLE THE LIGHT CONE: the NEAR one is TIMELIKE-separated
  from P, the FAR one SPACELIKE -- and at tangency they merge and both go NULL. **""")
for (sn, sf, cn, cf) in rows[:-1]:
    assert cn == "timelike" and cf == "spacelike", (cn, cf)
assert rows[-1][2] == "NULL" and rows[-1][3] == "NULL"

print("\n" + "="*80)
print("3. ** AND THAT IS EUCLID III.36 ITSELF, READ CAUSALLY **")
print("="*80)
print("""  ds^2(t) = t^2 - t+ t- vanishes exactly at t = sqrt(t+ t-) -- ** the GEOMETRIC MEAN of the
  secant's two segments **. And Euclid III.36 says precisely that the tangent length is that
  geometric mean: tangent^2 = PA·PB.

      >>> SO THE LIGHT CONE FROM P CROSSES THE SIGHTLINE AT THE GEOMETRIC MEAN OF THE
          SECANT'S TWO SEGMENTS -- WHICH IS THE TANGENT LENGTH. EUCLID III.36 IS THE
          STATEMENT OF WHERE THE LIGHT CONE IS. <<<

  The near intersection lies inside P's light cone (timelike), the far one outside
  (spacelike), and the geometric mean between them is on it. As the line swings to tangency
  the two segments close on their own geometric mean, the two points merge, and the merge
  happens ON the cone -- which is why the tangent is null and not merely short.""")
tm, tp = cuts(P, np.array([np.cos(np.radians(180+20)), np.sin(np.radians(180+20))]))
gm = np.sqrt(tm*tp)
print(f"\n  at 20 deg:  t- = {tm:.6f},  t+ = {tp:.6f}")
print(f"    geometric mean sqrt(t- t+) = {gm:.6f}")
print(f"    tangent length sqrt(pow)   = {np.sqrt(np.dot(P,P)-a**2):.6f}   = X0(P) = {X0(P):.6f}")
assert abs(gm - X0(P)) < 1e-9
print(f"    ** the same number, and it is the hinge's height. **")

print("\n" + "="*80)
print("4. AND THE JOINT TO P1 -- named carefully, because this is where a flavour-match would go")
print("="*80)
print("""  P1's metric singularity is a MEASURE COLLAPSE: a null hypersurface along whose generators
  the spatial extent contracts to zero, so two events that are null-separated (ds^2=0) and
  spatially coincident (dx=0) are assigned vanishing temporal separation -- two distinct,
  causally ordered points the metric measures as ONE.
  Section 3's degeneracy is a DISCRIMINANT COLLAPSE: two intersection points merging into one.

  ** ARE THEY THE SAME DEGENERACY? THE HONEST ANSWER IS: THEY ARE THE SAME EQUATION AND NOT
  THE SAME STATEMENT, AND THE DIFFERENCE IS WHAT THE TWO POINTS ARE. **""")
u = np.array([np.cos(np.radians(180+30)), np.sin(np.radians(180+30))])
Pu = np.dot(P, u); D4 = Pu**2 - (np.dot(P,P)-a**2)
T = P + (-Pu)*u
print(f"    at tangency (30 deg): D/4 = {D4:.2e}, the two roots merge at t = {-Pu:.6f}")
print(f"    the merged point: ({T[0]:+.6f}, {T[1]:+.6f}), |T| = {np.linalg.norm(T):.6f} = a  -> ON THE THROAT")
print(f"    ds^2 from lift(P) to it: {ds2(lift(P), np.array([0.0, T[0], T[1]])):.2e}  -> NULL")
print("""
  * SHARED: both are 'ds^2 = 0 with the two things the measure would separate collapsing into
    one', and section 2 shows the vanishing discriminant IS the vanishing interval. So the
    ALGEBRA is common: a degenerate quadratic and a null separation are one condition.
  * NOT SHARED: P1's two points are two EVENTS ON A GENERATOR of the horizon -- distinct
    points of the manifold, causally ordered, that the metric cannot tell apart. Here the two
    points are two INTERSECTIONS OF A LINE WITH A CIRCLE -- and at tangency they are literally
    the same point, not two the measure fails to separate.
  ** So this is a shared MECHANISM (degeneracy = nullity) and not a shared OBJECT. Recorded as
  that and no more. ** To promote it one would have to exhibit P1's two events as the two roots
  of a quadratic on this figure, which is not done here and is not obviously available: P1's
  result is causal-structural and carries no metric data (its cor:nonspherical turns on exactly
  that), while this receipt is entirely metric.""")

print("\n" + "="*80)
print("WHAT THE SWEEP'S SECOND QUESTION RETURNED")
print("="*80)
print("""  ** ⊢ THE SECANT'S TWO INTERSECTIONS STRADDLE THE LIGHT CONE, AND EUCLID III.36 SAYS WHERE
  THE CONE IS. **
    For any sightline from a point P of the overhead through the throat, the interval from P's
    lift to an intersection is  ds^2(t) = t^2 - pow(P) = t^2 - t+ t- , the last step being
    Euclid's own (the product of the secant's two segments IS the power). So:
        the NEAR intersection  (t-)  is TIMELIKE-separated from P     ds^2 = t-(t- - t+) < 0
        the FAR  intersection  (t+)  is SPACELIKE-separated from P    ds^2 = t+(t+ - t-) > 0
        and ds^2 vanishes at  t = sqrt(t+ t-)  -- ** THE GEOMETRIC MEAN **
    which is exactly the quantity Euclid III.36 identifies as the TANGENT LENGTH.

  >>> THE LIGHT CONE FROM P CROSSES ITS OWN SIGHTLINE AT THE GEOMETRIC MEAN OF THE SECANT'S
      TWO SEGMENTS. EUCLID III.36 IS A STATEMENT ABOUT WHERE THE LIGHT CONE IS. <<<

  ** AND THAT IS WHY ⊢10 IS AN IDENTITY AND NOT A COINCIDENCE, and it strictly generalises it. **
  ⊢10 said the TANGENT is null. It is now visible why: as the line swings to tangency the two
  segments close on their own geometric mean, the two points merge -- and they merge ON the
  cone, because the geometric mean is where the cone always was. The tangent is not null
  because it is short. It is null because tangency IS the two roots meeting at their geometric
  mean, and the geometric mean IS the tangent length, and the tangent length IS the height.

  ** TWO FALSE STARTS, BOTH CAUGHT BY THE ASSERT AND BOTH KEPT: **
    (i) I predicted D/4 = -ds^2 -- a "secant/tangent/miss = timelike/null/spacelike"
        trichotomy. ** The sign was backwards AND the object was wrong: ** I measured to the
        line's FOOT placed at height 0, but off tangency the foot is not on the throat, so
        that point is on no part of the substrate and the interval to it measures nothing. The
        foot lies on the throat exactly when the line is tangent -- the one case the error
        could not detect. ** A prediction about a trichotomy, made before checking that its two
        outer cases had objects to measure. **
    (ii) The tangency row then vanished from the table: D/4 at exact tangency is ~-4e-16, and
        a bare `if D4 < 0` dropped the one row the result rests on. Clamped at the
        discretisation (face 37, on this receipt's own hand).

  THE JOINT TO P1, at its weight: P1's metric singularity (two events the measure cannot
  separate) and this degeneracy (two intersections merging at their geometric mean) share the
  MECHANISM -- degeneracy is nullity -- but not the OBJECT: P1's two points are events on a
  generator, distinct and causally ordered; these two are intersections of a line with a
  circle, and at tangency they are the same point. ** A shared mechanism, not a shared object.
  ** Promotion would need P1's two events exhibited as the roots of a quadratic on this figure
  -- not done, and not obviously available: P1 is causal-structural and carries no metric data
  (its cor:nonspherical turns on exactly that), while this receipt is entirely metric.""")
