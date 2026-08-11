"""
THE FULL-CORPUS SWEEP, question 3: P4 AND P6.  (r1115)

Daryl: "I do wonder about p4. I think you might find some neat things here as well, though
perhaps of a different flavour."

** FIRST, THE VOCABULARY COUNT, because it decides how to ask. **
    P4 (modern_parallax):  angle 0 · null 0 · geodesic 0 · sphere 0 · triangle 0 · tangent 0
    P6 (shadow_of_existence): angle 0 · null 0 · tangent 0 · circle 0 · triangle 0
                              -- but shadow 24 · projection 18
** Neither paper has any geometric vocabulary. ** So the question cannot be "where does the
figure's geometry land in P4" -- there is nowhere for it to land. The different flavour Daryl
names is real and it is this: these two papers are not about geometry, they are about
** how a geometry is READ OFF AN APPEARANCE **. So ask that question instead.

THE QUESTIONS:
  Q1  P4 is titled the modern parallax, and parallax is a GEOMETRIC MEASUREMENT: read an angle
      on the sky, infer a distance you cannot reach. P3's slicing parameter is read off a sky
      angle, r0 = (2/sqrt3) sin w. ** Is P3's w a rangefinding measurement of the same kind --
      and if so, what does the dial's range mean? **
  Q2  P6's inference rule is "ask what world must exist for the appearances to arise", and its
      empirical engine is historiography. ** Steiner's 1826 move -- from a relation among
      segments to an invariant of the point -- is that rule executed on a circle. Is that a
      datum for P6, or a resemblance? **

COULD THIS RETURN OTHERWISE? Q1 is a computation and can simply fail. Q2 is a reading and is
recorded as one; it is tested against the alternative that it is a resemblance.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

print("="*80)
print("Q1 -- IS THE SKY ANGLE A RANGEFINDING MEASUREMENT?")
print("="*80)
print("""  Rangefinding: an object of known radius alpha, seen from distance d, has angular radius
        theta = arcsin(alpha / d).
  Read backwards -- the classical use, and parallax's cousin -- it gives the distance to
  something you cannot reach, from an angle on the sky.

  P3's hinge sits at d = 2 alpha. So the hole's angular radius there is:""")
theta = np.degrees(np.arcsin(a/(2*a)))
print(f"    arcsin(alpha / 2alpha) = arcsin(1/2) = {theta:.4f} deg")
assert abs(theta - 30.0) < 1e-12
print(f"""  ** 30 degrees. And 30 degrees is w = 30, the Nariai dial angle. **
  That is not yet a finding -- two 30s again, and this corpus's own faces forbid taking a
  numerical match for a map. ** Test whether the dial's w IS an angle within the hole's disc,
  by checking whether its RANGE is the hole's angular radius. **""")

print("\n" + "="*80)
print("Q1b -- THE DIAL'S RANGE, computed")
print("="*80)
print("""  The dial swings a plane about the hinge. Its perpendicular distance from the axis is
  d_perp = 2 alpha cos(psi), psi the swing. The sightline from the hinge that grazes the
  hole makes, with the hinge-to-centre line, the angle whose sine is alpha/2alpha. So the
  sightlines that MEET the hole occupy a cone of half-angle arcsin(1/2) = 30 deg, and no
  sightline from the hinge sees the hole further off-axis than that.""")
print(f"\n  {'sky angle from the hinge':>26} {'d_perp = 2a cos(90-b)':>22} {'meets the hole?':>17} {'regime':>14}")
for b in [0, 10, 20, 29, 30, 31, 45]:
    dperp = 2*a*np.sin(np.radians(b))
    meets = dperp < a - 1e-12
    graze = abs(dperp - a) < 1e-9
    reg = "NARIAI (tangent)" if graze else ("undercritical" if meets else "overcritical (misses)")
    print(f"  {b:>24} deg {dperp:>22.6f} {str(meets or graze):>17} {reg:>14}")
print(f"""
  ** THE DIAL'S RANGE IS THE HOLE'S ANGULAR RADIUS. ** Sightlines within 30 deg of the
  hinge-to-centre line cut the hole (undercritical, three horizons); at exactly 30 deg the
  sightline grazes it (Nariai); beyond 30 deg it misses (overcritical). ** So the swing angle
  IS an angle on the hinge's sky, its range IS the hole's apparent size, and:

      >>> NARIAI IS THE HOLE'S LIMB. The critical configuration of the whole construction is
          the sightline to the EDGE OF THE HOLE'S DISC AS SEEN FROM THE HINGE. <<<

  Not a coincidence of two 30s: the dial's endpoint and the hole's angular radius are the same
  angle because the dial's endpoint IS the grazing sightline, and the grazing sightline IS what
  an angular radius means. **""")

print("\n" + "="*80)
print("Q1c -- SO WHAT KIND OF MEASUREMENT IS P3's w?  (and here is the inversion)")
print("="*80)
print("""  Rangefinding, as ordinarily used: you know the object's SIZE, you measure its ANGLE, you
  infer your DISTANCE.   theta = arcsin(alpha/d)  ->  d = alpha / sin theta.
  P3 runs it with the distance FIXED (the hinge is at 2alpha, and that is forced -- Prop.
  twoalpha) and the angle VARYING over the disc. What comes out is not a distance. It is:""")
for w in [0, 10, 20, 30]:
    r0 = (2/S3)*np.sin(np.radians(w))
    M2 = (2/(3*S3))*np.sin(np.radians(3*w))
    print(f"    w = {w:>2} deg :  r0 = (2/sqrt3) sin w = {r0:.6f}    2M = (2/3sqrt3) sin 3w = {M2:.6f}")
print("""
  ** THE MASS. ** With the distance fixed and the size fixed, the free thing is WHERE ON THE
  DISC you look, and what that fixes is 2M. So P3's construction is rangefinding run backwards
  through its own third variable:
        ordinary rangefinding : size + angle    -> distance
        P3                    : distance + angle -> MASS
  and the object's apparent size is not an input to be measured but the RANGE OF THE
  INSTRUMENT -- the dial's own endpoints.

  ** WHICH IS THE PERSPECTIVAL THESIS, STATED AS AN INSTRUMENT. ** alpha is the invariant and
  M is what a vantage reads: here, literally, M is the reading on a dial whose scale is the
  hole's apparent size from where the observer stands.""")

print("\n" + "="*80)
print("Q1d -- AND THE HONEST BOUND ON THE P4 CONNECTION")
print("="*80)
print("""  ** P4 HAS NO GEOMETRIC LOCUS AND THIS DOES NOT GIVE IT ONE. ** P4's content is
  ln(1+z) = int H dt along cosmological sightlines through a lumpy universe, and an exclusion
  by three orders of magnitude. Nothing above touches it. The receipt above is about P3's
  figure, and it was reached BY ASKING P4's QUESTION (what does an angle on the sky measure?),
  not by finding P4's objects in the figure.

  ** So the connection to P4 is METHODOLOGICAL, and that is exactly the different flavour: **
      P4  : the sky's redshift isotropy is a MEASUREMENT of the foliation, not a convention --
            as stellar parallax made the Earth's motion a measured fact rather than an option.
      P3  : the sky's angle is a MEASUREMENT of the slicing -- "the slicing parameter is fixed
            by the geometry of observation", and r0 = (2/sqrt3) sin w with w a genuine angle.
  ** Both papers say: the sky is the instrument, and what it reads is not a convention. ** P4
  says it of the foliation and proves it with data; P3 says it of the slicing and proves it
  with geometry. ** Recorded as a shared epistemic structure, asserted as nothing more. ** A
  count of shared words is not a joint, and there is no computation here that runs from one
  paper's objects to the other's.""")

print("\n" + "="*80)
print("Q2 -- P6: IS STEINER'S MOVE P6's INFERENCE RULE?")
print("="*80)
print("""  P6's rule, in its own words: ** "ask what world must exist for the appearances to arise" **
  -- read the structure behind appearances. Its engine is historiography: each episode where a
  structure favoured by coherence ahead of a decisive measurement was later vindicated is a
  datum about the criteria.

  ** STEINER, 1826. ** The appearances: for a point E and a circle, every line through E meets
  it at A, B, and the product EA.EB comes out the same number whatever line you draw. Euclid
  proved that (III.35/36) and stopped -- it is a relation among segments. Steiner asked what
  must be true of E for the appearances to agree, and answered: E carries an INVARIANT,
  pow(E) = |d^2 - r^2|, a number belonging to the point and not to any line.""")
rng = np.random.default_rng(3)
E = np.array([1.7, 0.6])
prods = []
for _ in range(6):
    u = rng.normal(size=2); u /= np.linalg.norm(u)
    Eu = np.dot(E, u); D4 = Eu**2 - (np.dot(E,E) - a**2)
    if D4 < 0: continue
    r = np.sqrt(D4); t1, t2 = -Eu-r, -Eu+r
    prods.append(t1*t2)
print(f"\n  the appearances, for E = {E}: the products EA·EB over random lines:")
for pr in prods: print(f"    {pr:.12f}")
print(f"  the invariant behind them: |E|^2 - a^2 = {np.dot(E,E)-a**2:.12f}")
for pr in prods: assert abs(pr - (np.dot(E,E)-a**2)) < 1e-12
print("""
  ** The appearances vary (every line is different); the number does not. Steiner named the
  number and attached it to the point. That is P6's rule, executed on a circle in 1826. **

  ** AND IT IS THE CORPUS'S OWN MOVE, WHICH IS WHY THIS IS NOT DECORATION: **
      Steiner : the segment-products are what you measure; pow(E) is what E IS.
      CR      : 2M is what a vantage reads; alpha is what the geometry IS.
  Both: a family of readings, one invariant behind it, and the move is to name the invariant
  and hand it to the object rather than to the reading. ** P3 says exactly this of the mass --
  "a turning point, not a coefficient" -- and p0 §power now says it of the power. **

  ** THE HONEST WEIGHT, and the alternative it is tested against. ** Is this a datum for P6 or
  a resemblance? P6's data are episodes where a structure favoured AHEAD of a decisive
  measurement was VINDICATED by it. Steiner's move was not favoured-then-vindicated; it was a
  definition that proved fruitful. ** So it is NOT a datum for P6's historiographic engine. **
  What it is: a worked instance of P6's INFERENCE RULE, in a domain P6 does not currently draw
  from -- pure geometry, where the "appearances" are not observations but the outputs of a
  construction. ** Recorded as that: an instance of the rule, not a datum for the thesis. **""")

print("\n" + "="*80)
print("WHAT THE SWEEP'S THIRD QUESTION RETURNED")
print("="*80)
print("""  ** P4 AND P6 HAVE NO GEOMETRIC LOCUS, AND THE SWEEP RETURNING NOTHING THERE IS WHAT MAKES
  P2's THALES CIRCLE MEAN SOMETHING. ** Vocabulary counts: P4 has zero angles, nulls,
  geodesics, tangents, triangles; P6 has zero angles, nulls, tangents, circles. These are
  argumentative papers and the figure's geometry has nowhere in them to land. ** A sweep that
  found a connection in every paper would be a template, not a survey. **

  ** BUT ASKING P4's QUESTION OF P3's FIGURE PAID, AND THAT IS THE DIFFERENT FLAVOUR: **
  P4 is titled the modern parallax, and parallax is rangefinding -- read an angle, infer what
  you cannot reach. Asked of P3:
    * ⊢ ** THE DIAL'S RANGE IS THE HOLE'S ANGULAR RADIUS. ** Sightlines from the hinge within
      arcsin(alpha/2alpha) = 30 deg of the axis CUT the hole (undercritical, three horizons);
      at 30 deg exactly the sightline GRAZES it; beyond, it misses (overcritical).
      >>> NARIAI IS THE HOLE'S LIMB -- the critical configuration of the entire construction
          is the sightline to the EDGE OF THE HOLE'S DISC as seen from the hinge. <<<
      And that is not the two-30s coincidence the faces forbid: the dial's endpoint IS the
      grazing sightline, and a grazing sightline IS what an angular radius means.
    * ⊢ ** P3 IS RANGEFINDING RUN THROUGH ITS THIRD VARIABLE. ** Ordinary: size + angle ->
      distance. P3: distance FIXED (the hinge at 2alpha, forced) + angle -> ** MASS **. The
      object's apparent size is not an input but the RANGE OF THE INSTRUMENT. ** Which is the
      perspectival thesis stated as an instrument: alpha is the invariant, and M is the reading
      on a dial whose scale is the hole's apparent size from where the observer stands. **

  ** P6: Steiner's 1826 move IS P6's inference rule executed on a circle. ** The appearances
  are the segment products EA·EB, which vary line by line; the invariant behind them is
  pow(E), which does not (verified). Euclid proved the relation and stopped; Steiner asked what
  must be true of E and named the invariant. ** And that is the corpus's own move: 2M is what a
  vantage reads, alpha is what the geometry IS. ** ⚠ Tested against the alternative and
  DEMOTED accordingly: P6's data are structures favoured ahead of a decisive measurement and
  then vindicated; Steiner's was a fruitful definition, not a prediction. ** So it is an
  instance of P6's RULE, not a datum for P6's THESIS. Recorded as that and no more. **

  ⚠ BOUNDED: the P4 link is a shared EPISTEMIC STRUCTURE (the sky is the instrument, and what
  it reads is not a convention), asserted as nothing more. No computation runs from P4's
  objects to P3's. A count of shared words is not a joint.""")
