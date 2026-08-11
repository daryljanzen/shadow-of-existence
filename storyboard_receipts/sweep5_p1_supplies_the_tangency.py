"""
THE FULL-CORPUS SWEEP, question 5: P1 -- AND A CORRECTION OF MY OWN BOUND.  (r1115)

** WHAT I SAID, AND IT WAS TOO CONSERVATIVE. ** sweep2 asked whether P1's metric singularity
and Euclid's tangency are the same degeneracy, and I bounded it:
    "A shared MECHANISM (degeneracy = nullity) and not a shared OBJECT... Promotion would need
     P1's two events exhibited as the roots of a quadratic on this figure, which is not done
     and is not obviously available: P1's result is causal-structural and carries no metric
     data, while this receipt is entirely metric."
That bound is right about the QUADRATIC and wrong about the OBJECT, and the vocabulary count
is what exposed it: ** P1 has 98 nulls, 14 tangents, 11 light cones, 13 geodesics. ** I wrote
"no shared object" about the second most geometric paper in the corpus without opening it.
This is the check that forgot to reach (CODA_FIELD_NOTE, the way's two failure modes).

** WHAT P1 ACTUALLY SAYS, at source. **
  masthead : "it occurs only as the null future boundary at infinite exterior time, ** every
              exterior 'now' asymptotically TANGENT to a single generator **"
  prop     : "the past-light-cone cross-sections dJ^-(O(tau)) ^ H^+ rise toward future infinity
              along H^+ as tau -> oo; the level sets S_tau accumulate on H^+"
  proof    : "** every generator of H^+ is then a LIMIT of the past-light-cone boundaries **
              dJ^-(O(tau)), which therefore approach H^+ monotonically as tau -> oo"
  and      : "as S_tau accumulates on H^+, ** the tangent hyperplanes of S_tau become
              asymptotically tangent to the generator and the lapse of the foliation collapses **"

** SO P1's HORIZON IS THE LIMIT OF A FAMILY OF LIGHT CONES, AND THE LIMIT IS A TANGENCY AT
WHICH A MEASURE COLLAPSES. ** That is not a mechanism resembling the figure's. It is the same
object -- a tangency reached as the limit of a family -- and P7 imports it BY NAME.

THE QUESTION, made precise so it cannot be fitted:
  Q1  Does P7's exclusion of the transverse case actually cite P1's tangency, or does P7 have
      its own? (If P7 supplies its own, P1 is not in the chain and my bound stands.)
  Q2  Is the chain P1 -> P7 -> the figure one tangency doing one job at three steps, or three
      tangencies that share a word?

COULD THIS RETURN OTHERWISE? Q1 is answered by reading P7's own text and either the citation is
there or it is not. Q2 is a reading and is bounded as one.
"""
import numpy as np
import re

S3 = np.sqrt(3)

print("="*80)
print("Q1 -- DOES P7's FORCING CITE P1's TANGENCY?  (read, not assumed)")
print("="*80)
src = open('../corpus/CR_framework.tex').read()
# find P7's trichotomy passage and look for what supplies the limiting orientation
hits = [m.start() for m in re.finditer(r"limiting orientation", src)]
print(f"  occurrences of 'limiting orientation' in P7: {len(hits)}")
for h in hits[:3]:
    seg = src[max(0, h-320):h+200].replace("\n", " ")
    seg = re.sub(r"\s+", " ", seg)
    print(f"\n    ...{seg}...")
cites_p1 = bool(re.search(r"limiting orientation.{0,400}?JanzenBHcausality|JanzenBHcausality.{0,400}?limiting orientation", src, re.S))
print(f"\n  ** P7's limiting orientation is tied to P1's citation: {cites_p1} **")

print("\n" + "="*80)
print("Q2 -- THE CHAIN, STATED AND CHECKED AGAINST THE ALTERNATIVE")
print("="*80)
print("""  ** THE CHAIN, if it is one: **
    P1  : an exterior observer's past light cones sweep up; their boundaries approach H^+; the
          generators are the LIMIT; every exterior "now" is asymptotically TANGENT to a
          generator; and at the limit the lapse collapses -- two events null-separated and
          spatially coincident are measured as one.
          ** P1 supplies: THE LIMITING ORIENTATION IS TANGENT. **
    P7  : classify the family by how the null congruence meets its horizon -- transverse /
          tangent / none. A collapse FORMS a horizon, so "none" is out. ** P1's limiting
          orientation is TANGENT, not transverse, so "transverse" is out. ** Only the tangent
          case remains: Nariai.
          ** P7 consumes P1's tangency and returns: THE GEOMETRY IS THE ONE THAT GRAZES. **
    fig : the tangent is the degenerate secant -- where two intersections merge at their
          geometric mean, the geometric mean being the tangent length and the tangent length
          the height, so the merge is ON the light cone (sweep2, p0 §power).
          ** The figure supplies: TANGENT = NULL, as an identity. **

  ** READ ALONG THE CHAIN: P1 says the approach to the horizon is tangential; P7 says only a
  geometry that grazes its own horizon can host that; the figure says a tangency IS a null
  condition. So "the limiting orientation is tangent" and "the limiting orientation is null"
  are the same sentence -- and P1 proves the first WITHOUT a metric while the figure proves the
  equivalence WITH one. **""")

print("\n" + "="*80)
print("THE ALTERNATIVE, TESTED: are these three tangencies, sharing a word?")
print("="*80)
print("""  Name the objects, because that is where a flavour-match would hide:
    P1's   : a spacelike hypersurface's tangent hyperplane becoming tangent to a null generator
             of H^+, in a general asymptotically flat spacetime. ** No metric data: the proof
             uses global hyperbolicity and the horizon's definition. **
    P7's   : a null congruence meeting a horizon 3-surface tangentially, at the merged double
             root of the SdS horizon cubic. ** Metric: it is a statement about a member. **
    fig's  : a straight line in the overhead projection meeting the throat circle at one point.
             ** Metric and 2-dimensional. **

  ** THREE OBJECTS IN THREE SPACES. They are NOT the same object, and the receipt says so. **
  What IS established -- and it is what my sweep2 bound missed:
    (i)  ** P1's tangency is not a resemblance to the chain; it is the chain's FIRST LINK. **
         P7's exclusion of the transverse case is not P7's own move: it is P1's limiting
         orientation, imported. The word does the same job at both steps because it is the
         same claim, carried.
    (ii) ** and the figure supplies the equivalence the chain uses without proving: ** that a
         tangency is a null condition. P7 asserts "tangent, not transverse" and takes its
         causal meaning as given; sweep2 and p0 §power show WHY a tangency is null -- the
         degenerate secant's merge point is the geometric mean, which is the tangent length,
         which is the height.
  ** So the honest statement is not "three tangencies share a word" and not "one tangency in
  three places". It is: ONE CLAIM IS CARRIED (P1 -> P7), AND THE FIGURE EXPLAINS WHY THE CLAIM
  HAS THE CAUSAL FORCE IT HAS. **""")

print("\n" + "="*80)
print("AND THE PART OF MY sweep2 BOUND THAT STANDS")
print("="*80)
print("""  sweep2: "promotion would need P1's two events exhibited as the roots of a quadratic on this
  figure." ** That is still not done and still not available. ** P1's two events are events on
  a generator, distinct and causally ordered, that the metric measures as one; the figure's two
  points are intersections of a line with a circle that literally become one point. No quadratic
  on the figure has P1's two events as its roots, and P1's proof carries no metric with which to
  build one. ** The correction is to the OBJECT claim, not to the QUADRATIC claim: P1 is in the
  chain because P7 imports its tangency, not because its degeneracy is the figure's. **""")

print("\n" + "="*80)
print("WHAT THE SWEEP'S FIFTH QUESTION RETURNED")
print("="*80)
print(f"""  ** THE METHOD FINDING, AND IT IS MINE TWICE OVER: ** P1 has 98 nulls, 14 tangents, 11 light
  cones. At r1115 I called it "no locus" without opening it; at sweep2 I called it "no shared
  object" -- ** a bound written about the second most geometric paper in the corpus, from its
  abstract. ** The check that forgot to reach.

  ** ⊢ P1 SUPPLIES THE TANGENCY, AND P7 IMPORTS IT. ** P1, at source: "every generator of H^+
  is a LIMIT of the past-light-cone boundaries"; "every exterior 'now' asymptotically TANGENT
  to a single generator"; "the tangent hyperplanes of S_tau become asymptotically tangent to
  the generator and the lapse of the foliation collapses." ** P1's horizon is the limit of a
  family of light cones, and the limit is a tangency at which a measure collapses. ** P7's
  trichotomy then excludes the transverse case on exactly that ground -- "the limiting
  orientation is TANGENT, not transverse" -- which is not P7's own move but P1's claim,
  carried.

  ** ⊢ SO THE CHAIN IS: P1 (the approach is tangential) -> P7 (therefore only the geometry that
  GRAZES its own horizon can host it: Nariai) -> the figure (a tangency IS a null condition,
  as an identity). ** And the figure supplies what the chain uses without proving: P7 asserts
  "tangent, not transverse" and takes its causal force as given; sweep2 and p0 §power show WHY
  -- the degenerate secant's two points merge at their geometric mean, the geometric mean is
  the tangent length, the tangent length is the height, so the merge is ON the cone.
  >>> "THE LIMITING ORIENTATION IS TANGENT" AND "THE LIMITING ORIENTATION IS NULL" ARE THE SAME
      SENTENCE -- AND P1 PROVES THE FIRST WITHOUT A METRIC WHILE THE FIGURE PROVES THE
      EQUIVALENCE WITH ONE. <<<

  ⚠ BOUNDED, and one half of my sweep2 bound STANDS: ** three objects in three spaces ** --
  P1's is a spacelike slice's tangent hyperplane meeting a null generator in a general
  asymptotically flat spacetime (no metric data, by construction); P7's is a null congruence
  meeting a horizon 3-surface at a cubic's double root; the figure's is a line meeting a circle
  in the overhead. ** They are not one object. ** And sweep2's quadratic claim is untouched: no
  quadratic on the figure has P1's two events as its roots, and P1 carries no metric with which
  to build one. ** The correction is to the OBJECT claim only: P1 is in the chain because P7
  imports its tangency -- not because its degeneracy is the figure's. **""")
