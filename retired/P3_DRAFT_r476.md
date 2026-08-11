# P3 REWRITE — working prose draft (r476). Conceptual-depth draft, stated for reversal.
> **⌖ RETIRED r1521 — superseded, verified.** This is P3 REWRITE working prose draft (r476). **The paper it drafted exists and compiles at 40pp**; this predates the renumber and ~1040 revisions of work on it.
> Kept as record; **do not work from it.**


# Structure = P3_SKELETON (in P3_REWRITE_NOTES.md). To be formalized into .tex once the structure settles.
# Drafted section by section; l never primary (Q2); Schwarzschild/de Sitter never via a degeneracy (Q0).

## 1. The substrate and the cut

The construction takes place on a single de Sitter manifold: the maximally symmetric Lorentzian
geometry, of constant radius alpha = sqrt(3/Lambda) fixed by the cosmological constant. For the
spherically symmetric sector its structure is carried faithfully by a low-dimensional stand-in --
the one-sheet hyperboloid -X0^2 + X1^2 + X2^2 = alpha^2 in the flat ambient space -- on which the
whole construction can be drawn. The radius alpha is the invariant of the construction: fixed by
Lambda, and never taken to a limit. The Schwarzschild--de Sitter geometries, with their Schwarzschild
and de Sitter members, are not separate manifolds but cuts of this one substrate, and the body of the
paper exhibits them as such.

At the waist X0 = 0 the substrate meets its equatorial throat, the circle X1^2 + X2^2 = alpha^2 of
radius alpha. We coordinate it by the position angle theta measured from the +X1 axis; the back of the
circle, theta = 180deg (X1 = -alpha), is the point we will write as r = 0.

A geometry is cut from the substrate by a plane. The plane contains a fixed line -- the hinge, meeting
the equatorial plane at X1 = 2alpha -- and swings about it like a door; the slicing curve is the
section the plane cuts from the hyperboloid. The swing angle w is the single family parameter: as w
runs from 0 to 180deg, the plane sweeps the entire family of cuts, with Schwarzschild at w = 0 and de
Sitter at w = 180deg. The hinge is the pivot of that swing -- the line the family turns about. It is
neither an observer nor a point of the slicing curve; its role as the centre about which the
observational chart's sky angle turns is made precise in Section 4.

The slicing curve is therefore given intrinsically -- by its position theta around the throat and by
the swing w that selects the family member. Proper radial distance along it, with which a metric-first
account would begin, is not a primary object of this construction; it is recorded only as a closing
remark, where its one notable feature is located. To lead with it, as the natural metric coordinate,
is to obscure exactly the structure the swing makes plain.

## 2. Three parameters, and what each one hides

The slicing curve is one object, but no single coordinate displays it whole. It carries three faithful
parameters, and the organizing fact of the construction -- stated here, before any of them is put to
work -- is that each is faithful to one feature of the curve precisely by absorbing a symmetry, and so
is blind to the structure that symmetry carried. None is the curve; each is a true shadow of it. The
construction is read through all three together, and the recurring error it is built to avoid is
asking one of them to report what it has flattened away.

theta -- position around the throat circle, the angle of Section 1. Along the lap it is the natural
arc-length-type coordinate, and the areal radius runs linearly in it, which is what makes the curve
legible as a wave. What theta flattens is the family: it is tied to a single circle, and every member
of the swing presents to it as a circle, so theta cannot tell which member it is on.

w -- the swing angle of Section 1, equivalently the observer's sky angle of Section 4. This is the
family parameter: it is what distinguishes Schwarzschild, Nariai, and de Sitter, and it carries the
family into its overcritical continuation. What w flattens is the involution that exchanges the two
roles of a seam: w and pi/3 - w name the same configuration read two ways (so 30deg and 150deg are
both Nariai), and w by itself cannot say which of the two horizons it has designated.

r0 -- the signed areal radius of the designated seam, the value in which the horizon relation and the
fundamental ellipse are written. This is the parameter tied to the algebra. What r0 flattens is the
fold of the sine: r0 = (2/sqrt3) sin w caps at 2/sqrt3 and sends two different swings to the same
value, so on the real axis it cannot separate the undercritical regime from its overcritical
continuation -- that distinction reappears only when r0 is allowed to go complex. Being a single
value, r0 is also blind to where on the lap the curve sits.

So theta sees position but not family, w sees family but folds the seam-involution, r0 sees the
designated value but folds the sine and the lap. Each has quotiented out one symmetry, and the
structure that symmetry carried becomes invisible in that coordinate. The construction uses all three,
and never asks one to carry what it flattened. This is the single discipline that a metric-first
ordering -- beginning from proper distance, one coordinate made to stand for the whole -- silently
breaks; the closing remark on proper distance returns to why that ordering stages the most regular
member of the family as its apparent pathology.

## 3. The horizon structure, read in r0

A horizon is a zero of the metric function f = 1 - 2M/r - r^2/alpha^2. Clearing the denominator, in the
gauge alpha = 1, gives the horizon cubic

    r^3 - r + 2M = 0,

whose three roots are the three horizons of the geometry. The construction becomes transparent the
moment the slicing parameter is taken to be one of those roots -- the moment we write 2M = r0 - r0^3,
which says exactly that r0 is a root. With that designation the cubic factors cleanly:

    r^3 - r + 2M = (r - r0)(r^2 + r r0 + r0^2 - 1) = 0.

The designated root is r0; the other two are (-r0 +/- sqrt(4 - 3 r0^2))/2, the roots of the fundamental
quadratic r^2 + r r0 + r0^2 = 1. All three sum to zero -- a horizon triplet that can never share a sign.

The discriminant of that quadratic, 4 - 3 r0^2, is the whole regime structure, read off r0 and nothing
else:
- 4 - 3 r0^2 > 0  (|r0| < 2/sqrt3): three distinct real horizons -- the undercritical regime.
- 4 - 3 r0^2 = 0  (|r0| = 2/sqrt3): two horizons merge into a double root -- Nariai.
- 4 - 3 r0^2 < 0  (|r0| > 2/sqrt3): one real horizon and a complex-conjugate pair -- overcritical
  (taken up in Section 4: the continuation past the Nariai crest, not a separate construction).

This is the point of leading with r0: the three regimes are fixed by a single algebraic quantity, the
discriminant, with no appeal to a proper distance diverging and no "two limits of one object." Nariai is
not a pathology reached by something blowing up; it is simply the value of r0 at which the quadratic's
discriminant vanishes.

The three roots are interchangeable labels of one geometry, and the map that swaps them is explicit. The
root-exchange involution

    sigma(r0) = (-r0 + sqrt(4 - 3 r0^2))/2

carries r0 to the second positive root of its own cubic, is its own inverse, and fixes r0 = 1/sqrt3 --
the Nariai configuration, here read with the designated root sitting on the merged pair. (The same Nariai
geometry is met at |r0| = 2/sqrt3, where the designated root is instead the lone one and the other two
merge; the two are one geometry under two designations, which is exactly the content of the involution.)
It exchanges the endpoints r0 = 0 and r0 = 1.

That the roots are interchangeable is not a relabelling convenience but a symmetry of the geometry itself.
Designating the second positive root rather than r0 leaves the mass parameter -- and therefore the entire
metric function -- unchanged: 2M = r0 - r0^3 = rB - rB^3, since both are roots of the same cubic, and f
depends on the designation only through 2M. This involution is the sigma symmetry that, in Section 2, the
swing angle w was seen to flatten: w and pi/3 - w designate the same configuration two ways. Reading it
here in r0 is what makes it a literal symmetry of the line element; reading it in w is what folds it from
view.

Taken over all slicing parameters at once, the three roots trace a definite locus in the (r0, r) plane:
the diagonal r = r0 -- the designated root -- together with the tilted conic r^2 + r r0 + r0^2 = 1
carrying the other two. The conic is a 45-degree tilted ellipse, and its major axis is the backward-radial
direction -- the long-way-round sense of the radial coordinate -- which carries the negative-root horizon,
the horizon reached through r = 0. That negative root is not a bookkeeping artefact; Section 5 reaches it
as the close of the lap.

## 4. The family in w, and the two readings at the throat

The slicing plane swings about the hinge, and the swing angle w is the family parameter -- the same
angle the gnomonic projection reads as the observer's sky angle (Section 1). At each w > 0 the cut
takes three horizons: the cosmological horizon, the black-hole horizon standing above r = 0, and r = 0
itself fixed at the back of the circle. The mass is nonzero and is the slicing-dependent factor,
2M = alpha[(r0/alpha) - (r0/alpha)^3], with alpha = sqrt(3/Lambda) the one fixed invariant -- never a
free parameter, never reached by a limit. In the sky angle this is the triple-angle
2M = (2/3sqrt3) sin 3w, cresting at Nariai (w = 30 deg), with r0 = (2/sqrt3) sin w. The sigma
involution of Section 3 is here the reflection w <-> pi/3 - w, fixing Nariai; the chart involution and
the root-exchange involution are one map (the conjugacy chi.g1 = f.chi).

Now swing the plane down toward w = 0. The black-hole horizon shrinks until it merges into r = 0 at the
back; the cosmological horizon swings to the polar-opposite point and becomes the horizon, with
0 < r < 2M wrapping the half-equator and the exterior opening out beyond it. The slicing mass has gone
to zero -- the black hole has shrunk away -- and the cut is now one curve: the equator taken
diametrically, which is exactly P2's Schwarzschild curve, the meridian-hyperbola -> equatorial-circle
-> meridian-hyperbola of the maximal analytic extension, r = M(1 + cos z) continued through both
critical points.

This single w = 0 curve carries two readings, and the map between them is the involution -- this is the
de Sitter <-> Schwarzschild correspondence, exact, at fixed alpha, and it is neither a limit nor a mass
relabelled to zero. Read from the pivot's perspective -- the natural reading as the hinge settles to
w = 0, the curve seen from the swing-pivot looking down -- it is Schwarzschild: the 2M/r term carried
perspectivally (P2's reading), the horizon and r = 0 the two metric singularities of one genus, the
curvature at r = 0 belonging to the perspectival metric over the parameter r and not to the underlying
manifold. Rotate the vantage through 180 degrees -- look from the uphill side, the worldline staring
straight up the r = 0 axis -- and the same curve is de Sitter: f = 1 - r^2/alpha^2, the cosmological
geometry, r = 0 now the axis rather than a mass-laden centre. One curve, one fixed alpha, two vantages
the involution swaps. The underlying invariant geometry is de Sitter; the Schwarzschild mass is the
perspectival reading's, carried by the vantage, not a second invariant.

This is the excision, stated plainly, because the prior draft reached this same throat by two routes
that have to go.

  (i) Schwarzschild is NOT the alpha -> infinity limit. alpha is the fixed invariant the whole
  construction lives inside; sending it to infinity dismantles the throat, the circle, and the family
  in one stroke. The correspondence is reached by swinging the hinge to w = 0 at fixed alpha and
  reading the curve from the pivot -- not by deforming the geometry.

  (ii) r0 = 0 is NOT a "massless Schwarzschild." A massless Schwarzschild is a contradiction in terms:
  Schwarzschild is the geometry with a mass and the cosmological term off; M = 0 with the cosmological
  term on is de Sitter, by definition. The prior draft (prop r0zero) was right that r0 = 0 carries two
  readings of one slicing -- that is precisely the involution -- but wrong to gloss the Schwarzschild
  side as "the massless limit 2M = 0." The slicing mass is zero there because the underlying geometry
  is de Sitter; the Schwarzschild reading is the pivot-vantage of that same curve, its mass
  perspectival, alpha untouched.

Past Nariai the same curve continues overcritically -- the seam continuation sin theta -> cosh psi,
i.e. theta -> pi/2 + i psi -- one analytic continuation of the one slicing curve, not a separate
relation and not a redefinition of w. Its geometry is Section 5.

[FIGURE -- fundamental ellipse, from Daryl's PhD thesis (offered for coopting): the continuous picture
in which r0 runs through the family in the black-hole-shrinking-to-zero sense and lands on de Sitter at
r0 = 0; the locus of Section 3 (diagonal + tilted ellipse) is this figure's algebraic face. Place with
Section 3 (locus) or Section 4 (the w -> 0 shrink); confirm orientation against the thesis original.]

## 5. The seam, the lap, and the conjugate branch

A turning point of the slicing curve is a point where it runs tangent to the throat circle; we call it
a seam, and the seam is where the de Sitter <-> Schwarzschild correspondence becomes an explicit,
invertible analytic continuation. Take the de Sitter slicing for concreteness, r = alpha sin theta with
theta = l/alpha. For theta in [0, pi/2] the curve rises from r = 0 to the seam at r = alpha, and the
two-dimensional slicing-surface line element is the round spherical one, ds^2 = dtheta^2 + sin^2 theta
dOmega^2, of Riemannian signature (+,+). At the seam the tangent dr/dtheta = cos theta vanishes -- the
curve meets the throat tangentially.

Continue theta past the seam, off the real axis: theta -> pi/2 + i psi. Then dtheta = i dpsi and
sin theta = cosh psi, and the spherical element becomes the de Sitter element
ds^2 = -dpsi^2 + cosh^2 psi dOmega^2, of Lorentzian signature (-,+). The signature flip is not imposed
-- it follows from dtheta = i dpsi squaring the continuation factor to -1. The two pieces, spherical
and de Sitter, are one analytic object: sin theta continued from [0, pi/2] onto the line pi/2 + i psi
*is* cosh psi, with the seam the branch point and a C^1 join at r = alpha. This is the correspondence
in concrete form, and it is invertible because sin and cosh are one analytic function -- a geometry
obtained as a slicing of de Sitter keeps, in that invertibility, its membership in de Sitter.

What flips is the signature of the two-dimensional SLICING-SURFACE metric: the radial direction reads
spacelike on the hole-side piece (r < alpha) and timelike on the cosmological-side piece (r > alpha),
flipping as the curve crosses the throat. It is NOT the signature of the spacetime, which is Lorentzian
throughout. The substrate is one Lorentzian manifold; the continuation relates two real regions of it
and never carries the geometry onto a Euclidean one. The (+,+) is a fact about the slice, not the world.

The overcritical regime is the same continuation, applied now to the horizon angle. The boundary
|2M| = 2/(3sqrt3) is the crest of sin 3w; writing 3w = pi/2 + i beta gives sin 3w = cosh beta > 1, the
horizon angle continued off the real axis exactly as theta -> pi/2 + i psi at the seam, with the Nariai
crest the branch point. Read straight off the locus of Section 3: for |r0| > 2/sqrt3 the vertical
slicing line misses the real ellipse and meets only the diagonal -- one real horizon, the
backward-radial root carried by the major axis -- while the other two continue as a conjugate pair on
the ellipse's complex extension. The ellipse does not disappear; the real line simply ceases to meet
it. The overcritical slicing curve has lost both forward turning points -- f < 0 for every r > 0, so
dr/dl = sqrt|f| never vanishes there and the forward branch runs out unbounded, r(l) ~ e^{l/alpha} --
and retains a single real turning point on the backward branch, the negative root.

That negative root is where the lap closes. The radial coordinate r is signed -- g_thetatheta = r^2,
so area never requires r > 0 -- and its sign is grounded in the fundamental ellipse of the thesis: the
negative branch is the backward-radial direction, the long way from r = 0, which is the ellipse's major
axis (the anti-diagonal r = -r0) and the negative root of the cubic. The curve, continued, runs in
along a ruling and conjugates around the throat circle, through r = 0, to close on this negative-root
horizon. r = 0 is no barrier: the substrate is C^infinity smooth through it (P2's result on the
underlying function), and the divergence there lives only in the areal-radius reading -- a function of
position on the circle -- with no intrinsic status in the Nariai/SdS geometry, where it is sweep-induced
(Section 6). The negative-root horizon reached this way is not a fourth object: it is the same substrate
point as the merged pair, the triple seam read once on the real side and once on the backward-radial
branch, with r = 0 the branch point between the two readings. The conjugate region -- the
backward-radial branch carrying that closing root -- is a continuation within the one Lorentzian
substrate, the real signed-(r<0) branch of the same manifold (the back-seam the companion reaches by
z -> pi + i rho' onto r < 0), never a Euclidean excursion. The lap the locus of Section 3 promised
closes here, on the root reached the long way round.

## 6. The intrinsic curvature, and the sweep that accounts for it

Swept through one angular direction, the slicing curve generates a surface of revolution
ds^2 = dl^2 + r(l)^2 dphi^2, and its Gaussian curvature is a direct computation:

    K_G = -f'(r)/2r = 1/alpha^2 - M/r^3.

Three things follow, and together they close the interior. First, K_G is finite and smooth for every
r > 0: the slicing surface is regular throughout the static region between the horizons. The de Sitter
term 1/alpha^2 and the Schwarzschild term -M/r^3 stand together at fixed alpha -- no limit isolates
either -- and the sole divergence is the M/r^3 pole as r -> 0, the Schwarzschild curvature singularity
of the companion paper, simply absent when M = 0, where K_G reduces to the constant 1/alpha^2 of de
Sitter. Second, the curvature does not detect the horizons: at a horizon r_h, K_G = 1/alpha^2 - M/r_h^3
is a finite number that neither diverges nor vanishes nor spikes -- the horizon is a metric and chart
feature, not a curvature feature, exactly as the companion found for Schwarzschild. Third, the
curvature changes sign once, at r_star = (M alpha^2)^{1/3}: Schwarzschild-like (negative,
mass-dominated) inside, de Sitter-like (positive, Lambda-dominated) outside, the crossover distinct
from the horizons and lying between them. Curvature structure and horizon structure are independent
features of one surface.

The single divergence -- the M/r^3 pole at r = 0 -- is the one thing left to account for, and the sweep
does it. The de Sitter <-> Schwarzschild correspondence of Section 5 is, in this language, one slicing
curve swept from two vantages, and we can now say what each vantage does. A description is built by
sweeping the radial curve through the throat 2-sphere's angular symmetries to recover the spatial
geometry, and the sweep needs an axis. The de Sitter vantage sweeps the complete arc about the
manifold's own axis of symmetry: no symmetry is broken, and the recovered geometry is smooth de Sitter
throughout. The Schwarzschild vantage cannot do this -- viewing the hole from outside in the timelike
orientation, where the symmetric sweep is precisely the unavailable de Sitter one, it is forced to take
a selected point as its pivot. The point it is forced onto is r = 0, the off-axis critical point at the
back of the throat circle. This is not a second symmetry break standing beside the first; it is the
cascade the one break -- locating the hole -- forces.

That forced pivot is the geometric origin of the asymmetry. On the substrate the two critical points,
the horizon and r = 0, are topologically identical: two matching turning points of one intrinsic curve,
exchanged by its involution. They are not metrically identical -- the swept geometry's curvature is
lopsided, the M/r^3 pole divergent at the pivot r = 0 and finite at the horizon. The divergence at
r = 0 is the chain-rule shadow of the forced pivot; the asymmetric classification tracks the asymmetric
sweep, not the curve, which is symmetric. The de Sitter sweep, taken about the manifold's own axis,
needs no pivot and manufactures no such singularity. The whole horizon-versus-singularity asymmetry --
present in the Schwarzschild reading, absent in the de Sitter one -- is the signature of that single
cascading break.

This leaves one objection, and answering it fixes the status of M itself. The Kretschmann scalar is
coordinate-independent, so its divergence as r -> 0 is a fact no relabelling removes. It is a fact --
about the perspectival Schwarzschild metric, whose curvature scalar it is. But the mass that metric
carries is not an intrinsic coefficient. Restoring the throat radius,
2M = alpha[(r0/alpha) - (r0/alpha)^3] = alpha sin u cos^2 u: the mass is the throat radius alpha
multiplied by a pure-number slicing profile, and the two factors have sharply different status.
alpha = sqrt(3/Lambda) is the invariant -- fixed by Lambda, not a slicing choice, unchanged by the
reading-swap (which acts only on r0) and by the projection (every observer sees the same hole). M is
the slicing-dependent factor -- alpha read through a turning of the slicing, ranging over
[0, alpha . 2/(3sqrt3)] with the maximum at Nariai, vanishing at r0 = 0. M is not a coefficient of a
spacetime; it is a turning point, the throat radius projected through the slicing. So the Kretschmann
objection is correct of the shadow and silent about the geometry: the divergence is real as the
perspectival metric's, but the M it carries is the projection, and the de Sitter manifold beneath --
carrying no mass term, constant curvature 1/alpha^2 -- has no invariant that diverges anywhere.

The manifold, then, has no horizons and no singularities; the readings do, and each reading's catalogue
is a feature of its causal vantage. The construction does not relate black-hole and cosmological
geometry -- it identifies them as one object differently read: one de Sitter manifold, one slicing of
it, two causal vantages its seam joins.

## 7. The slicing curve is intrinsic: a groupoid of descriptions

The construction so far was carried out from one fixed vantage -- the charting observer of Section 1,
viewing the hole pole-on, on whose celestial sphere the gnomonic image is the chart that reads the
slicing parameter r0. This section says what changes, and what does not, when that vantage moves, and
the answer closes the loop: the slicing curve is intrinsic to the manifold, the geometry is rigid, and
the de Sitter and Schwarzschild readings are two descriptions of one slicing.

Two observers must be kept apart. The charting observer sits off the manifold and fixes the projection.
The other lies on the de Sitter manifold, and its slicing curve is the radial curve r(l) of Section 1
-- a curve traced on the manifold itself, the spherical arc continued through the equatorial seam onto
its Lorentzian piece (Section 5). The slicing curve and the parameter r0 are intrinsic: the curve is a
locus of manifold points, r0 marks a point on it, and neither refers to the charting observer. So the
horizon relation 2M = r0 - r0^3 is read off the intrinsic curve, and everything it determines -- f, the
horizon cubic, the curvature of Section 6 -- is a property of the manifold, not of any chart of it.

Now move the charting observer. It may be placed anywhere off the manifold from which the hole is
visible: pole-on the throat images as a circle, off-axis as an ellipse, and the slicing curve images
accordingly. Each placement gives a different image -- but the geometry does not move with it.

  RIGIDITY. The horizon relation 2M = r0 - r0^3, and hence f and the SdS geometry it determines, is
  independent of the placement of the charting observer.

The proof is immediate: the curve and r0 are defined on the manifold without reference to the charting
observer, so a change of placement re-projects the image without acting on the manifold, the curve, or
r0; every geometric quantity is unchanged. The placements therefore form a structure acting not on the
geometry but on its descriptions -- objects the admissible charting vantages, morphisms the maps
between the images they produce of one fixed slicing curve, composition associative, each invertible,
identity the unchanged vantage. It is a groupoid, and the geometry is its single orbit-invariant: the
groupoid of observer descriptions.

This is a different move from the sweep of Section 6, and the two must not be run together. The sweep
changes the causal orientation and so generates two geometries -- de Sitter from within, Schwarzschild
from without -- from one curve. The groupoid here fixes one geometry and changes only the chart that
images it. One changes the geometry; the other changes the description. The de Sitter <-> Schwarzschild
correspondence is the first; the rigidity groupoid is the second.

The groupoid's symmetry is the discrete structure already met in Sections 3 and 4. The reflection
w <-> pi/3 - w (the cubic involution) and the chart involution, conjugate by the closed-form map chi,
are vantage-changes that permute the descriptions while fixing the geometry; with the periodicity of
the sky angle they generate the symmetry of the horizon triplet -- the three roots as the three sky
angles carrying one value of 2M. The groupoid is rigid (it carries no continuous modulus under change
of charting vantage) and is therefore discretely generated, the involution and the sky-angle
periodicity its forced generators. The within-geometry group is D3 = S3; the full discrete symmetry of
the solution space, established in the companion groupoid paper, is Aut(A2) = S3 x Z2 = D6.

We are explicit about scope. What is established is the generator structure: the slicing curve is
intrinsic, the geometry rigid, the descriptions a groupoid, and that groupoid discretely generated by
the involution and the sky-angle periodicity. The relations among the generators, the within-geometry
reassignments at fixed alpha not yet classified -- in particular the overcritical slicings of Section
5, reached at fixed alpha past the Nariai crest -- and the action of vantages between distinct de
Sitter representations at different alpha are left to a later pass.

## Remark: proper distance, demoted to a derived quantity

The proper radial distance l, primary in an earlier ordering of this material, is here a derived
quantity, and the demotion is deliberate. It remains defined by dl = dr/sqrt|f|, and it remains
physically meaningful -- but it is read off r, not the reverse. The reason it cannot be primary is
visible at Nariai. There the two positive horizons merge into a double root; f acquires a double zero,
f ~ (1/2)f''(r - r_h)^2, so sqrt|f| ~ |r - r_h| and dl = dr/sqrt|f| ~ dr/|r - r_h| -- the proper
distance to the merged horizon diverges logarithmically. This is correct physics, not a defect: at the
Nariai crest the horizons are infinitely far apart in proper distance, while the curvature
K_G(r_h) = 1/alpha^2 - M/r_h^3 there is finite. Reading l as the primary variable inverts that -- it
makes the regular Nariai configuration present as a pathology (something blowing up) and hides the
finite-curvature fact behind a diverging coordinate. That inversion is what the earlier l-first
ordering did, and it is the root of the false impression that Nariai is reached by a divergence. With r
the primary radial variable the regimes are read off the discriminant (Section 3), Nariai is the value
where it vanishes, and the surface metric and curvature of Section 6 stand without reference to l. The
primary parametrisation of the curve is the swing angle w; the cosmological synchronisation of the same
congruence is carried by the sinh^{2/3} clock of the companion cosmology paper. Proper distance is the
closing remark, not the spine.
