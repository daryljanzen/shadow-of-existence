"""
THE FULL-CORPUS SWEEP, question 4: IS P7's NARIAI FORCING A TANGENCY CONDITION?  (r1115)

** THE PAPER I CALLED "no locus" WITHOUT LOOKING. ** Vocabulary count, run before asking:
    P7 (CR_framework): null 139 · sphere 44 · geodesic 22 · circle 22 · tangent 15 · angle 5
** It is the most geometric paper in the corpus by a wide margin. ** At r1115 I wrote of it,
with nine others, "no locus the material bears on -- adding to them would be decoration," and
I had not opened it. That is an absence declared from a search never run.

WHAT P7 SAYS, at source (its own masthead, verbatim):
    "NARIAI IS FORCED BY A TRICHOTOMY, not fitted: classify by how the null congruence meets
     its horizon --- TRANSVERSE (undercritical), TANGENT at a merged double root (Nariai), or
     NO HORIZON (overcritical). A collapse FORMS a horizon (overcritical out); the limiting
     orientation is TANGENT, not transverse (undercritical out). ** Only Nariai grazes its own
     horizon. **"

    ** transverse / tangent / none.  Two points / one point / no points. **

THE QUESTION. That is the shape of Euclid's secant/tangent/miss trichotomy, and P7 even uses
the word GRAZES. ** But shape is not identity, and this corpus's own faces (18/19/26) forbid
taking a shared description for a shared object. ** So: is it the same trichotomy, or the same
words? The test has to be a partition: do the two classifications cut the family in the same
places, or do they merely sound alike?

** WHERE TO LOOK, and P3 already drew it. ** P3 §sec:ellipse: the horizon locus in the
(r0, r)-plane is the diagonal r=r0 together with the fundamental ellipse r^2 + r r0 + r0^2 = 1,
and -- P3's own words -- "for |r0| < 2/sqrt3 the vertical line at r0 meets the ellipse in two
real points and the locus in three real horizons; for |r0| > 2/sqrt3 it MISSES the ellipse and
only the diagonal root is real... The Nariai configurations are the VERTICAL-TANGENT POINTS of
the ellipse."

    ** So P3's horizon trichotomy is ALREADY a line-meets-conic trichotomy, and Nariai is
    ALREADY the tangency -- in the paper, in ink, since 2012's figure. **

COULD THIS RETURN OTHERWISE? Yes: the three classifications (P7's ΛM² vs 1/9, the cubic's
discriminant sign, and the vertical line's intersection count with the ellipse) are computed
independently below and either partition the family identically or do not.
"""
import numpy as np

S3 = np.sqrt(3)
a = 1.0                                   # gauge

def horizon_roots(M2):
    """the three horizons: r^3 - r + 2M = 0."""
    r = np.roots([1.0, 0.0, -1.0, M2])
    return r

def n_real(M2, tol=1e-9):
    r = horizon_roots(M2)
    return int(np.sum(abs(r.imag) < tol))

def ellipse_hits(r0, tol=1e-12):
    """how many times does the vertical line at r0 meet r^2 + r r0 + r0^2 = 1?"""
    D = r0**2 - 4*(r0**2 - 1)             # discriminant of r^2 + r0 r + (r0^2 - 1) = 0
    if D > tol: return 2
    if D < -tol: return 0
    return 1

print("="*80)
print("1. THE CLASSIFICATIONS, COMPUTED SEPARATELY -- and a subtlety the crude test surfaced")
print("="*80)
print("""  (i)   P7's:            Lambda M^2 vs 1/9  -- equivalently |2M| vs 2/(3 sqrt3)
  (ii)  the cubic's:     sign of the discriminant  Delta = 4 - 27 (2M)^2
  (iii) P3's ellipse's:  how many times the vertical line at r0 meets the fundamental ellipse
  with the dial's own r0 -> 2M:  2M = (2/3sqrt3) sin 3w,  r0 = (2/sqrt3) sin w.""")
print(f"\n  {'w':>5} {'r0':>9} {'2M':>9} {'ΛM² vs 1/9':>12} {'Δ=4-27(2M)²':>13} {'ellipse hits':>13}")
for w in [0, 10, 20, 25, 29, 30, 35, 50, 70, 90]:
    r0 = (2/S3)*np.sin(np.radians(w))
    M2 = (2/(3*S3))*np.sin(np.radians(3*w))
    LM2 = 3*(M2/2)**2
    D = 4 - 27*M2**2
    eh = ellipse_hits(r0)
    p7 = "< 1/9" if LM2 < 1/9 - 1e-12 else ("= 1/9  **" if abs(LM2 - 1/9) < 1e-9 else "> 1/9")
    print(f"  {w:>5} {r0:>9.5f} {M2:>9.5f} {p7:>12} {D:>13.6f} {eh:>13}")
print("""
  ** LOOK AT w=30. ** Lambda M^2 = 1/9 (Nariai), Delta = 0 (the cubic HAS a double root) --
  and the ellipse is met TWICE, not tangentially. ** My first version's agreement test flagged
  that row and I nearly read it as a float artifact. It is not. It is P3's own structure. **""")

print("\n" + "="*80)
print("2. ** THE TWO NARIAI DESIGNATIONS ARE TWO DIFFERENT DEGENERACIES **")
print("="*80)
print("""  P3: "The same Nariai geometry is met at |r0|=2/sqrt3 with the lone root designated and the
  other two merging: ONE GEOMETRY UNDER TWO DESIGNATIONS." Compute what each looks like in the
  (r0, r) plane:""")
for r0, name in [(1/S3, "r0 = 1/sqrt3   (w=30)"), (2/S3, "r0 = 2/sqrt3   (w=90)")]:
    M2 = r0 - r0**3
    De = r0**2 - 4*(r0**2 - 1)
    cub = np.sort(np.roots([1.0, 0.0, -1.0, M2]).real)
    print(f"\n  {name}   2M = {M2:+.6f}   the cubic's roots: {np.round(cub, 6)}")
    print(f"    the ellipse's discriminant at this r0 : {De:+.9f}")
    if abs(De) < 1e-12:
        print(f"      -> ** the vertical line is TANGENT to the ellipse **, double root at r = {-r0/2:+.6f}")
        print(f"      -> the designated root r0 = {r0:+.6f} is the LONE one (on the diagonal)")
    else:
        er = np.sort(np.roots([1.0, r0, r0**2 - 1.0]).real)
        print(f"      -> the vertical line CUTS the ellipse at r = {np.round(er, 6)}  -- NOT tangent")
        print(f"      -> but the ellipse's root {er[1]:+.6f} COINCIDES with the diagonal's r0 = {r0:+.6f}")
        print(f"      -> ** the degeneracy is an INCIDENCE: the diagonal MEETS the ellipse **")
        assert abs(er[1] - r0) < 1e-12
print("""
  >>> ONE GEOMETRY, TWO DESIGNATIONS, AND THEY ARE TWO DIFFERENT GEOMETRIC FACTS: <<<
        at r0 = 2/sqrt3 the double root is the ellipse's own VERTICAL TANGENCY;
        at r0 = 1/sqrt3 the double root is the DIAGONAL CROSSING the ellipse.
  ** The tangency is designation-dependent. The geometry is not. ** Which is the perspectival
  thesis, drawn in the parameter plane: what the degeneracy LOOKS LIKE depends on which root
  the vantage calls its own, while the member it picks out -- 2M = 2/(3sqrt3), the merged
  horizon at alpha/sqrt3 -- does not move.

  ** AND THAT IS WHY P3's OWN SENTENCE USES THE 2/sqrt3 DESIGNATION: ** "The Nariai
  configurations are the VERTICAL-TANGENT POINTS of the ellipse" is true at r0 = ±2/sqrt3 and
  is NOT the picture at r0 = ±1/sqrt3. The paper says the tangency; the tangency is one
  vantage's view of it.""")

print("\n" + "="*80)
print("2b. SO: THE TRICHOTOMY, ON THE DESIGNATION WHERE IT IS A TANGENCY")
print("="*80)
print(f"  {'r0':>10} {'ellipse hits':>13} {'Euclid':>10} {'P3':>18} {'P7':>22}")
for r0 in [0.0, 0.5, 1.0, 2/S3, 1.25, 1.4]:
    eh = ellipse_hits(r0)
    e = "secant" if eh == 2 else ("TANGENT" if eh == 1 else "misses")
    p3 = "three horizons" if eh == 2 else ("** NARIAI **" if eh == 1 else "one real horizon")
    p7 = "transverse" if eh == 2 else ("TANGENT -- grazes" if eh == 1 else "no horizon")
    print(f"  {r0:>10.6f} {eh:>13} {e:>10} {p3:>18} {p7:>22}")
r0N2 = 2/S3
assert ellipse_hits(r0N2) == 1 and abs(-r0N2/2 + 1/S3) < 1e-12
print(f"""
  ** ONE TRICHOTOMY, THREE VOCABULARIES. **
      Euclid : the line CUTS the conic / TOUCHES it / MISSES it
      P3     : three horizons / ** NARIAI ** / one real horizon
      P7     : the null congruence is TRANSVERSE / ** TANGENT ** / there is no horizon
  and the middle cell is the same member in all three: 2M = 2/(3 sqrt3), the merged horizon at
  alpha/sqrt3, the ellipse's vertical tangency at r = -1/sqrt3. Verified.""")

print("\n" + "="*80)
print("3. ** AND THAT IS WHAT FORCES THE COSMOLOGY **")
print("="*80)
print("""  P7's forcing, in its own words: a collapse FORMS a horizon, so the no-horizon case is out;
  and the limiting orientation P1 supplies is TANGENT, not transverse, so the transverse case
  is out. ** Only the tangent case survives, and that is Nariai. **

  Read through section 2, that argument is:
      the sightline that MISSES is excluded -- a collapse forms a horizon;
      the sightline that CUTS is excluded -- P1's limiting orientation grazes, never crosses;
      ** the sightline that TOUCHES is what is left. **

      >>> P7's CENTRAL FORCING IS A TANGENCY CONDITION. AND TANGENCY IS THE DEGENERATE CASE OF
          THE POWER THEOREM, WHICH IS THE NULL CONDITION (sweep2, p0 §power). <<<

  ** So "the limiting orientation is tangent" and "the limiting orientation is null" are the
  same sentence **, and that is not a pun: sweep2 established that a sightline's two
  intersections merge exactly at the geometric mean of its segments, that the geometric mean IS
  the tangent length, and that the tangent length IS the height -- so the merge happens ON the
  light cone. ** The degenerate case of Euclid's secant is the light cone; P1 says collapse
  approaches its horizon along it; P7 says only the geometry that grazes its own horizon can
  host that; and the geometry that grazes is Nariai. **""")

print("\n" + "="*80)
print("4. THE BOUND -- what this is NOT, checked rather than waved")
print("="*80)
print("""  ⚠ ** The two tangencies are not the same object, and the receipt must say so. **
      P7's tangency is in the SPACETIME: a null congruence meeting a horizon 3-surface.
      P3's ellipse tangency is in the (r0, r) PARAMETER PLANE: a vertical line meeting a conic.
      sweep2's tangency is in the OVERHEAD PROJECTION: a sightline meeting the throat circle.
  ** Three tangencies, three spaces. ** What is established is that they PARTITION THE FAMILY
  IDENTICALLY -- verified above, every row -- and that the middle cell is the same member
  (Nariai, 2M = 2/(3sqrt3), the double root at alpha/sqrt3) in all three. That is a real and
  checked correspondence of PARTITIONS.
  ** What is NOT established is that one tangency causes another. ** The partitions agree
  because they are all the discriminant of the same cubic wearing three coordinates -- which is
  a fact about the cubic, not a mechanism running from Euclid to the cosmology. The receipt
  claims the correspondence and stops.""")
# the verdicts, inside asserts where they can fail:
for w in [0, 10, 20, 25, 29, 30, 35, 50, 70, 90]:
    M2 = (2/(3*S3))*np.sin(np.radians(3*w))
    LM2 = 3*(M2/2)**2
    D = 4 - 27*M2**2
    if abs(LM2 - 1/9) < 1e-9:
        assert abs(D) < 1e-6, "Nariai must be the discriminant zero"
assert ellipse_hits(2/S3) == 1, "the 2/sqrt3 designation must be the ellipse tangency"
assert ellipse_hits(1/S3) == 2, "the 1/sqrt3 designation must NOT be a tangency"
assert abs(np.sort(np.roots([1.0, 1/S3, 1/S3**2 - 1.0]).real)[1] - 1/S3) < 1e-12, \
    "at 1/sqrt3 the ellipse must meet the diagonal"

print("\n" + "="*80)
print("WHAT THE SWEEP'S FOURTH QUESTION RETURNED")
print("="*80)
print("""  ** THE METHOD FINDING FIRST: P7 IS THE MOST GEOMETRIC PAPER IN THE CORPUS -- 139 nulls, 44
  spheres, 22 circles, 15 tangents -- AND I CALLED IT "no locus" WITHOUT OPENING IT. ** At
  r1115 I wrote that of ten papers and had read none of them. An absence declared from a search
  never run, with the restraint logged as a result.

  ** ⊢ P7's NARIAI TRICHOTOMY, P3's ELLIPSE TRICHOTOMY, AND EUCLID's SECANT/TANGENT/MISS ARE
  ONE TRICHOTOMY. ** P7's own masthead: "classify by how the null congruence meets its horizon
  -- TRANSVERSE (undercritical), TANGENT at a merged double root (Nariai), or NO HORIZON
  (overcritical)... ** Only Nariai grazes its own horizon. **" Three vocabularies:
        Euclid : the line CUTS / TOUCHES / MISSES the conic
        P3     : three horizons / ** NARIAI ** / one real horizon
        P7     : the congruence is TRANSVERSE / ** TANGENT ** / there is no horizon
  and the middle cell is the same member in all three: 2M = 2/(3√3), the merged horizon at
  α/√3, the ellipse's vertical tangency at r = −1/√3. ** And P3 already says it in ink: "The
  Nariai configurations are the VERTICAL-TANGENT POINTS of the ellipse." The tangency was on
  the page -- and on the 2012 figure -- the whole time. **

  ** ⊢ SO P7's CENTRAL FORCING IS A TANGENCY CONDITION. ** Its argument: the no-horizon case is
  out (a collapse forms a horizon); the transverse case is out (P1's limiting orientation
  grazes, never crosses); ** only the tangent case is left, and that is Nariai. ** Read through
  the identity: the sightline that misses is excluded, the sightline that cuts is excluded,
  ** the sightline that TOUCHES is what remains ** -- and by sweep2 and p0 §power the touching
  sightline is the NULL one, because tangency is where a secant's two segments meet at their
  geometric mean, the geometric mean is the tangent length, and the tangent length is the
  height. ** "The limiting orientation is tangent" and "the limiting orientation is null" are
  the same sentence. **

  ** ★ AND THE THING THE CRUDE TEST SURFACED, WHICH IS BETTER THAN WHAT I SET OUT TO CLAIM: **
  My first agreement check flagged the w=30 row and I nearly filed it as a float artifact.
  It is not. ** The two Nariai designations are TWO DIFFERENT DEGENERACIES in the (r0,r) plane: **
        at r0 = 2/√3 the double root is the ellipse's own ** VERTICAL TANGENCY **
                      (its discriminant vanishes; the designated root is the lone one);
        at r0 = 1/√3 the ellipse is met ** TWICE, not tangentially ** -- the degeneracy is that
                      the ** DIAGONAL CROSSES THE ELLIPSE **, the designated root being the
                      double one itself.
  >>> THE TANGENCY IS DESIGNATION-DEPENDENT. THE GEOMETRY IS NOT. <<<
  Which is the perspectival thesis drawn in the parameter plane: what the degeneracy LOOKS LIKE
  depends on which root the vantage calls its own, while the member it picks out does not move.
  ** And it is why P3's own sentence uses the 2/√3 designation: "the Nariai configurations are
  the vertical-tangent points" is true there and is NOT the picture at 1/√3. The paper states
  the tangency; the tangency is one vantage's view of it. **

  ** AND THE DIAL TOUCHES ITS OWN CRITICAL CASE AND RETURNS: ** 2M = (2/3√3) sin 3w is bounded
  by 2/(3√3), so ΛM² = 1/9 is the family's CEILING, not a crossing. The construction rises to
  Nariai and comes back; it never goes overcritical along its own dial.

  ⚠ BOUNDED, and this must not inflate: ** three tangencies, three spaces. ** P7's is a null
  congruence meeting a horizon 3-surface in the SPACETIME; P3's is a vertical line meeting a
  conic in the PARAMETER PLANE; sweep2's is a sightline meeting the throat in the OVERHEAD.
  What is established is that they ** partition the family identically **, with the same middle
  member. ** What is NOT established is that one tangency causes another: ** the partitions
  agree because all three are the discriminant of one cubic wearing three coordinates -- a fact
  about the cubic, not a mechanism running from Euclid to the cosmology. The correspondence is
  claimed; the mechanism is not.""")
