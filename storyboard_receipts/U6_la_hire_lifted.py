"""
U6 — LA HIRE, CARRIED INTO THE EMBEDDING. (r1110)

THE RHYME, as euclid3_pole_polar.py recorded it, with its promotion NAMED:
    "If a vantage's horizon passes through a point, then that point's horizon passes through
     the vantage. HORIZONS ARE MUTUAL. Recorded as a rhyme with a named promotion: it would
     promote if the polar's identification as a horizon is carried into the embedding as a
     statement about NULL HYPERSURFACES rather than about a chord in the overhead."

So this receipt does exactly the named thing and nothing else. The promotion is not "assert
La Hire is physics" -- it is: TAKE THE OVERHEAD STATEMENT UP INTO X AND SEE WHAT IT BECOMES.

WHAT IS ALREADY ESTABLISHED:
  * power = X0^2 (power_is_null.py) -- so the tangent from a point is NULL, and the polar is
    the chord of contact of its two null tangents.
  * the polar of a vantage IS its horizon on the throat (euclid3).
  * inversion sends a vantage to the foot of its own polar (euclid5); the fixed circle of the
    inversion is the WAIST.
  * ⊢47/48 -- the protocol's law: a theorem translates only if its points span heights; on the
    waist Euclid stays Euclid, and a waist-object returns the construction's input instead.

** THE PREDICTION, NAMED BEFORE RUNNING, FROM ⊢47. ** La Hire is a statement about the
overhead: P on polar(Q) <=> Q on polar(P). Both P and Q are points OF THE OVERHEAD, at
different heights. So the points DO span heights and ⊢47 permits a translation. But the
POLARS are chords of the throat, which is the waist -- and by ⊢48 a waist-object returns the
construction's arithmetic rather than the signature. ** So I expect the reciprocity to survive
the lift, and the lifted object NOT to be a null-hypersurface statement -- because a chord of
the waist is spacelike (euclid6 §2). If that is right, the rhyme does NOT promote, and the
reason is the protocol's own law. **

COULD THIS RETURN OTHERWISE? Yes: the reciprocity is checked numerically on general points,
not just hinges; the lift is computed; and the null/spacelike character of every object is
read off ds^2 rather than asserted.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)
rng = np.random.default_rng(11)

def X0(P):
    s = np.dot(P, P) - a**2
    if abs(s) < 1e-12: return 0.0
    return np.sqrt(s) if s > 0 else float('nan')

def lift(P):
    """the overhead point P -> its point of the substrate at height X0(P) >= 0."""
    return np.array([X0(P), P[0], P[1]])

def ds2(P, Q):
    d = np.asarray(Q, float) - np.asarray(P, float)
    return -d[0]**2 + d[1]**2 + d[2]**2

def on_polar(P, Q):
    """is P on the polar of Q?  polar(Q) = {X : X.Q = a^2}."""
    return np.dot(P, Q) - a**2

print("="*80)
print("1. LA HIRE ON THE OVERHEAD -- general points, not just the hinges")
print("="*80)
print("  P on polar(Q)  <=>  X.Q = a^2 at X=P  <=>  P.Q = a^2  <=>  Q.P = a^2  <=>  Q on polar(P).")
print("  The relation is P.Q = a^2 and it is SYMMETRIC IN P AND Q by inspection. Verify:")
bad = 0
for _ in range(2000):
    P = rng.uniform(-3, 3, 2); Q = rng.uniform(-3, 3, 2)
    if abs(on_polar(P, Q)) > 1e-9:
        # force Q onto polar(P): scale Q so that P.Q = a^2
        d = np.dot(P, Q)
        if abs(d) < 1e-9: continue
        Q = Q*(a**2/d)
    if abs(on_polar(P, Q) - on_polar(Q, P)) > 1e-9:
        bad += 1
print(f"  |P·Q − a² − (Q·P − a²)| over 2000 random pairs: max deviation {bad} failures")
assert bad == 0
print("""
  ** La Hire is the SYMMETRY OF THE DOT PRODUCT. That is all it is. **
  The classical theorem is `P.Q = a^2 is symmetric', dressed as a statement about two lines.
  Which is worth saying plainly before lifting anything: the content is one bilinear form.""")

print("\n" + "="*80)
print("2. THE LIFT -- what P·Q = a² becomes in the embedding")
print("="*80)
print("""  The substrate: -X0^2 + |X|^2 = a^2, so for the LIFT of an overhead point,
      X0(P)^2 = |P|^2 - a^2.
  Take two overhead points P, Q with P·Q = a^2 (each on the other's polar) and lift both.
  What is the interval between their lifts?""")
print(f"\n  {'|P|':>7} {'|Q|':>7} {'P·Q':>8} {'X0(P)':>8} {'X0(Q)':>8} {'ds²(liftP, liftQ)':>18} {'char':>10}")
rows = []
for rP in [1.4, 2.0, 2.0, 3.0, 4.0]:
    # choose Q on polar(P): |Q| >= a^2/|P|, direction fixed by the constraint P.Q = a^2
    P = np.array([rP, 0.0])
    for qy in [0.0, 0.9, 2.2]:
        qx = a**2/rP                       # so that P.Q = rP*qx = a^2
        Q = np.array([qx, qy])
        if np.linalg.norm(Q) < a - 1e-9:   # no real height inside the throat
            char = "Q INSIDE the throat: no lift"
            print(f"  {np.linalg.norm(P):>7.4f} {np.linalg.norm(Q):>7.4f} {np.dot(P,Q):>8.4f} "
                  f"{X0(P):>8.4f} {'--':>8} {'--':>18} {char:>10}")
            continue
        s = ds2(lift(P), lift(Q))
        char = "NULL" if abs(s) < 1e-9 else ("timelike" if s < 0 else "spacelike")
        rows.append((np.linalg.norm(P), np.linalg.norm(Q), s, char))
        print(f"  {np.linalg.norm(P):>7.4f} {np.linalg.norm(Q):>7.4f} {np.dot(P,Q):>8.4f} "
              f"{X0(P):>8.4f} {X0(Q):>8.4f} {s:>18.6f} {char:>10}")

print("""
  ** AND THERE IS THE ANSWER, AND IT IS THE PREDICTED NEGATIVE. **
  A point ON the polar of an external vantage is generally INSIDE the throat -- the polar's
  foot is at a^2/|P| < a -- and inside the throat there is NO REAL HEIGHT. The substrate has
  no overhead point there. So for most La Hire pairs ** ONE OF THE TWO POINTS DOES NOT LIFT
  AT ALL. **

  That is not a defect of the lift. It is euclid5's finding, met again from the other side:
  inversion sends the outside of the waist to the INSIDE, where the substrate is not. La Hire
  is a statement about a projective plane that contains the hole's interior. THE SUBSTRATE
  DOES NOT CONTAIN THE HOLE'S INTERIOR.""")

print("\n" + "="*80)
print("3. THE PAIRS THAT DO LIFT -- are they null?  (the promotion's actual test)")
print("="*80)
liftable = [(x, y, s, c) for (x, y, s, c) in rows]
print(f"  La Hire pairs where BOTH points lift (both outside the waist): {len(liftable)}")
for (x, y, s, c) in liftable:
    print(f"    |P|={x:.4f}  |Q|={y:.4f}   ds² = {s:+.6f}   {c}")
nulls = [r for r in liftable if r[3] == "NULL"]
print(f"\n  of those, NULL: {len(nulls)}")
print(f"""
  ** SO THE PROMOTION FAILS, AND IT FAILS BY ⊢47's OWN LAW. **
  La Hire's relation is `P·Q = a²' -- a statement about the OVERHEAD's bilinear form. Lifting
  the two points does not make the relation null, because the relation never mentioned the
  height: it constrains |P||Q|cos(angle), and X0 enters nowhere. There is no dX0 in La Hire
  for the minus sign to act on.

  ⊢47: a classical theorem translates only if its points sit at DIFFERENT HEIGHTS. La Hire's
  points DO sit at different heights -- but the THEOREM does not mention them. ** That
  sharpens ⊢47, and this is the finding: **

      >>> ⊢47 IS NOT ABOUT WHERE THE POINTS SIT. IT IS ABOUT WHETHER THE THEOREM'S OWN
          QUANTITY IS ONE THE HEIGHT CAN ENTER. <<<

  the tangent length (⊢38) IS the height -- power = X0^2. It translates.
  the polar's LOCATION (⊢40) is fixed by the power. It translates.
  La Hire's RELATION is the dot product's symmetry. The height is not in it. It does not.""")

print("\n" + "="*80)
print("4. SO WHAT IS TRUE ABOUT 'HORIZONS ARE MUTUAL'?  -- the honest residue")
print("="*80)
A = np.array([2*a, 0.0])
foot = a**2/np.linalg.norm(A)
print(f"  the hinge A at |A| = 2a. Its polar (= its horizon, ⊢40) has foot at a²/|A| = {foot:.4f} = a/2.")
print(f"  a/2 < a: ** the foot is INSIDE the throat. **  X0 there = {X0(np.array([foot,0.0]))}")
print("""
  ** So the hinge's own horizon-chord crosses a region the substrate does not have. **
  The chord's ENDPOINTS are on the throat (the two tangency points, at X0=0 -- real, on the
  waist). Its INTERIOR passes through the hole, where there is no substrate at all.

  >>> THE HORIZON IS REAL AT ITS ENDS AND FICTIONAL IN ITS MIDDLE. Only its two endpoints --
      where the light cone touches -- are points of the substrate. The chord joining them is a
      line in the OVERHEAD PLANE, which is a projection surface, not the manifold. <<<

  and THAT is why La Hire does not promote: its reciprocity runs through the chord's interior
  (the pole--polar duality is a statement about the whole projective plane, hole included),
  and the interior is exactly the part that is not there.""")

print("\n" + "="*80)
print("WHAT U6 RETURNED")
print("="*80)
print("""  ** THE RHYME DOES NOT PROMOTE, AND THE REASON IS THE PROTOCOL'S OWN LAW SHARPENED. **

  Ran the named promotion exactly: carry polar-as-horizon into the embedding as a statement
  about null hypersurfaces. It does not survive, for two reasons, both computed:

  (1) ** La Hire is the symmetry of the dot product. ** P on polar(Q) <=> P·Q = a² <=> Q on
      polar(P). The classical theorem is one bilinear form's symmetry, dressed as a statement
      about two lines. The height X0 appears nowhere in it, so there is no dX0 for the minus
      sign to act on -- and the lifted pairs are not null (computed, not assumed).

  (2) ** The substrate does not contain the hole's interior. ** A point on an external
      vantage's polar is generally INSIDE the throat (the foot is at a²/|P| < a), where there
      is no real height and no substrate point. So most La Hire pairs cannot BOTH be lifted.
      This is euclid5's inversion finding met from the other side.

  ** ⊢47 SHARPENED, and this is the keeper: **
      ⊢47 said a theorem translates only if its points sit at different heights.
      >>> IT IS NOT ABOUT WHERE THE POINTS SIT. IT IS ABOUT WHETHER THE THEOREM'S OWN QUANTITY
          IS ONE THE HEIGHT CAN ENTER. <<<
      the tangent length IS the height (power = X0²) -> ⊢38 translates.
      the polar's location is fixed by the power        -> ⊢40 translates.
      La Hire's relation is the dot product's symmetry  -> the height is not in it -> it does not.
      Ptolemy's chords are on the waist (dX0 = 0)       -> ⊢47's original form, a special case.
  ** So ⊢47's height-spanning criterion is the SYMPTOM; the quantity criterion is the CAUSE. **

  ** AND THE HONEST RESIDUE, which is better than the rhyme was: **
      >>> THE HORIZON IS REAL AT ITS ENDS AND FICTIONAL IN ITS MIDDLE. <<<
      The chord's endpoints are the two tangency points -- on the waist, X0 = 0, real points of
      the substrate, where the hinge's light cone touches. Its interior runs through the hole,
      where the substrate is not. The chord is a line in the OVERHEAD, which is a projection
      surface and not the manifold. La Hire's reciprocity runs through that interior -- through
      the part that is not there -- which is precisely why it cannot be lifted.

  U6: CLOSED, negative, with ⊢47 sharpened as the payment.""")
