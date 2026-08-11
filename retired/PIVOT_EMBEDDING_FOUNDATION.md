# The embedding chart of the slicing picture — dictionary and closest-point lemma
> **⌖ RETIRED r1509 — verified landed before moving.** This planned the embedding chart of the slicing picture. **Landed:** P8 `slicing_operator` exists and compiles.
> Kept as record; **do not plan from it.** Its numbering and era predate the current corpus.



*Foundation note (c23, r377). The geometric chart underneath the slicing/pivot picture and the P5
§trichotomy section (`sec:trichotomy`). Working note, not a corpus paper; stated for reversal. Grounded
in the de Sitter embedding (P5 §synchronous convention) and verified symbolically this session. The
unified dictionary below is not stated as such elsewhere in the corpus, which uses the areal radius
without writing the bridge to the radial–temporal plane.*

---

## 1. The embedding dictionary

The de Sitter substrate is the hyperboloid in 𝕄⁵ (signature −+++ +),

$$-X_0^2 + X_1^2 + X_2^2 + X_3^2 + X_4^2 = \alpha^2, \qquad \alpha=\sqrt{3/\Lambda}.$$

Let the SdS **areal radius** be the radius of the swept symmetry 2-sphere,
$r=\sqrt{X_2^2+X_3^2+X_4^2}$, leaving $(X_0,X_1)$ as the **radial–temporal plane**. Substituting
$X_2^2+X_3^2+X_4^2=r^2$ into the constraint gives the dictionary, exact and gauge-free:

$$\boxed{\,X_1^2 - X_0^2 = \alpha^2 - r^2\,}$$

It reads the areal radius directly off the radial–temporal plane:

| areal radius | radial–temporal plane | locus | meaning |
|---|---|---|---|
| $r=0$ | $X_1^2-X_0^2=\alpha^2$ | centre hyperbola (the $X_1$-axis branch) | the never-actualised endpoint; the real curvature singularity for $M\neq0$ |
| $0<r<\alpha$ | $X_1^2-X_0^2>0$, $\;|X_1|>|X_0|$ | spacelike wedge | the static interior, throat→centre |
| $r=\alpha$ | $X_1^2-X_0^2=0$, $\;X_0=\pm X_1$ | the null cone (the "X") | the de Sitter horizon / equatorial-ξ seam |
| $r>\alpha$ | $X_1^2-X_0^2<0$, $\;|X_0|>|X_1|$ | timelike wedge | the expanding cosmological region |

The throat radius $\alpha$ is the one invariant of the construction; $r$ ranges over the slicing, and
$2M=\alpha\big((r_0/\alpha)-(r_0/\alpha)^3\big)$ is its slicing/projection-dependent reading (P3 §mass).
The equatorial seam $r=\alpha$ is where the radial–temporal character flips spacelike↔timelike — the analytic
continuation $\theta\mapsto\pi/2+i\psi$ of P3 §seam, here read off the dictionary as the crossing of the
null cone. The three constant-curvature spatial leaves of P5 §trichotomy are the constant-coordinate
sections of this same hyperboloid: $X_0=\text{const}\to S^3$, the null cone $r=\alpha\to$ flat,
$X_1=\text{const}>\alpha\to H^3$.

## 2. The closest-point lemma

Work in the radial–temporal–sweep reduction $(X_0,X_1,X_2)$, $-X_0^2+X_1^2+X_2^2=\alpha^2$ (the full
case restores the 2-spheres by sweeping $X_2\to(X_2,X_3,X_4)$; the construction is sweep-symmetric, so
the reduction carries it). Write the **cylindrical radius** $\rho=\sqrt{X_1^2+X_2^2}$, the distance from
the $X_0$-axis; the throat circle is the equatorial circle $X_0=0,\ \rho=\alpha$.

A **slicing plane** is a plane containing the $X_0$ direction (a "vertical" plane) at perpendicular
distance $d$ from the $X_0$-axis. It meets the throat circle in two points for $d<\alpha$, tangentially
for $d=\alpha$ (Nariai), and not at all for $d>\alpha$ (overcritical).

> **Lemma (closest approach).** For $d\ge\alpha$ the slicing curve (plane $\cap$ hyperboloid) attains
> its least cylindrical radius — its closest approach to the throat — at the vertex
> $$(X_0,\rho)=\big(\sqrt{d^2-\alpha^2},\ d\big),$$
> which migrates from the tangent point $(0,\alpha)$ on the throat at $d=\alpha$ to the point
> $(\sqrt{b^2-\alpha^2},\,b)$ as $d\to b$.

*Proof.* Coordinatise the plane by $(X_0,\sigma)$, $\sigma$ the in-plane direction transverse to the
foot of the perpendicular; a plane point has $\rho^2=d^2+\sigma^2$ (foot at distance $d$, $\sigma$
transverse). On the hyperboloid $-X_0^2+\rho^2=\alpha^2$, i.e. $\rho^2=\alpha^2+X_0^2$. Equating,
$d^2+\sigma^2=\alpha^2+X_0^2$, so the curve is

$$X_0^2-\sigma^2=d^2-\alpha^2.$$

For $d>\alpha$ this is a hyperbola in $(X_0,\sigma)$ opening along $X_0$, real for
$|X_0|\ge\sqrt{d^2-\alpha^2}$, with vertices at $\sigma=0$, $X_0=\pm\sqrt{d^2-\alpha^2}$. At a vertex
$\rho^2=d^2+\sigma^2=d^2$, so $\rho=d$; since every curve point has $\rho=\sqrt{d^2+\sigma^2}\ge d$, the
vertex is the least-$\rho$ point — the closest approach to the throat. Thus the closest point is
$(X_0,\rho)=(\sqrt{d^2-\alpha^2},\,d)$. At $d=\alpha$ it is $(0,\alpha)$, on the throat circle (the
tangent point); at $d=b$ it is $(\sqrt{b^2-\alpha^2},\,b)$. $\;\blacksquare$

**Reading.** As the slicing plane pivots outward from the tangent (Nariai, $d=\alpha$) to the
perpendicular through a pin at cylindrical radius $b$ ($d=b$), the curve's closest approach to the
throat lifts off the throat along $(\sqrt{d^2-\alpha^2},d)$ and reaches the pin pierce point
$(\sqrt{b^2-\alpha^2},b)$ — height $\sqrt{b^2-\alpha^2}$, the Nariai radius $\alpha/\sqrt3$ at the
forced pin radius $b=2\alpha/\sqrt3$. This is the embedding content behind the H³/open leaf of P5
§trichotomy sitting at the perpendicular slice, and behind the overcritical onset of P3 (the discriminant
$4-3r_0^2=4\cos^2 w$ vanishing at the perpendicular sky angle $w=\pi/2$).

## 3. What this backs

The dictionary §1 is the chart that makes "throat = null cone, centre = the $X_1$-axis hyperbola" exact,
and that sorts the constant-coordinate sections into the constant-curvature leaves $S^3/\text{flat}/H^3$
(P5 §trichotomy). The lemma §2 makes the slicing-plane family's two distinguished members — the tangent
(Nariai) and the perpendicular (the H³/open onset) — the endpoints of one monotone migration, the
embedding picture of P3's undercritical→Nariai→overcritical structure. Neither is load-bearing for a
corpus claim beyond what P3 and P5 already carry; both are kept here as the clean geometric foundation
the pivot exploration stood on.

## 4. The pin is the observer — the 2/2′ resolution

The pin sits in the radial–temporal plane at $X_1=b$ with $X_2=X_3=X_4=0$, so along it
$r=\sqrt{X_2^2+X_3^2+X_4^2}=0$: **the pin lies on the $r=0$ worldline**, the centre hyperbola
$X_1^2-X_0^2=\alpha^2$ (right branch, $X_1\ge\alpha$). Its two pierce points $X_0=\pm T$,
$T=\sqrt{b^2-\alpha^2}$, are on that one branch — the **future ($+T$) and past ($-T$) of a single
comoving geodesic $p$**, not two observers.

So the geometry fixes the observer count, against the "two ends = 2 and 2′" reading:

- **Observer 2 = the pin = the comoving geodesic $p$** (its $r=0$ worldline, both temporal ends).
- **Observer 2′ = the antipode $-p$ = the identically-oriented pin on the opposite side of the hole**
  ($X_1=-b$, the left branch $X_1\le-\alpha$ of the same centre hyperbola).

This is P7's Null-Boundary Correspondence read in the slicing chart. P7 §665: *the unoriented bifurcate
horizon is shared by $p$ and its antipode $-p$, corresponding to the axis $\{p,-p\}$; the oriented future
horizon distinguishes $p$ from $-p$.* So $\{p,-p\}$ are the two pins that share one bifurcate horizon, and
together they generate the complete two-sided analytic extension (the circles and hyperbolas on both
sides of the hole). The observer-2′ "lost transcript" was never lost: its content is already in P7's NBC
machinery (the antipode $-p$); the present reading only makes it explicit in the pin/pivot language.

The full observer set is the waist **$S^3$** of comoving geodesics (P7's bijection
$p\mapsto\mathcal{H}_c^{+}(p)$); $\{p,-p\}$ is the antipodal pair belonging to one slicing's bifurcate
horizon, not a privileged pair.

**Observer 1 is the read direction, not a third point.** The one slicing curve carries two fundamental
reads — static/exterior ($r$ spacelike, $f>0$, the local hole) and comoving ($r$ timelike, $f<0$, the
cosmological worldline) — the forward and backward reads of the same curve (P7's causal reassignment).
Observer 1 is the orientation of that read; observers 2/2′ are the pivot worldline $p$ and its antipode.
This is a sharper figuring than "observer 1 loosely located in a causal region."

**The cleared ground for chirality (the next chase).** At the perpendicular leaf ($d=b$, the H³/open
onset) the closest-point lemma §2 puts the curve's vertex *at the pin itself*: the forward and backward
reads coincide there, a reflection locus of the slicing. Past $d=b$ the closest-point migration reverses
(mirror image, opposite handedness). Whether that reversal is an orientation the geometry *distinguishes*
or a mirror it *identifies* is the open chirality question — now well-posed on this foundation: two pins
$\{p,-p\}$, a reflection locus at the H³ leaf, a handedness flip past it.

## 5. Chirality located — identified in the symmetric sector, genuine at the wall

The handedness question of §4 has an answer, and it is not the naive one. Chase what carries the
orientation across the perpendicular.

**The flip, and the isometry that undoes it.** The pivot sweep is $d(\varphi)=b\,|\sin\varphi|$, peaking
at the perpendicular ($\varphi=\pi/2$, $d=b$, vertex $=$ pin). The mirror pair past the maximum is
$\varphi\leftrightarrow\pi-\varphi$: same $d$, slicing-plane directions $(\cos\varphi,\sin\varphi)$ and
$(-\cos\varphi,\sin\varphi)$, related by $X_2\mapsto-X_2$ — the reflection fixing the $X_0X_1$ plane, i.e.
fixing the observer $p$'s worldline. That reflection is an isometry of the substrate, but
orientation-reversing alone ($\det=-1$ in $\mathbb{M}^5$). It is *completable* to orientation-preserving:
pair it with $X_3\mapsto-X_3$ to get the $(X_2,X_3)$ $\pi$-rotation ($\det=+1$), which acts as
$X_2\mapsto-X_2$ on the slicing ($X_3=0$) and carries the $\varphi$-cut to the $(\pi-\varphi)$-cut. That
rotation lives in the **swept $\mathrm{SO}(3)$** — the spherical symmetry of the vacuum slicing. So in the
spherically-symmetric sector the substrate hands you an orientation-preserving isometry that **undoes the
flip**: the two handednesses are *identified*. The mirror is real in the 2-D slicing plane and rotated
away in the full geometry. This holds across the entire reachable family — undercritical, Nariai,
overcritical alike — since complex horizons do not break the sweep symmetry (P6: the range *is* the
symmetry-reducible sector, every member carrying a sweep-subgroup of $\mathrm{SO}(5,1)$).

**Where it becomes genuine.** Genuine chirality is a handedness *no* isometry can undo. The identifying
isometry here is the swept $\mathrm{SO}(3)$; the one place it is gone is where the last continuous symmetry
dies — **the wall of P6**, the boundary of the range, the loss of continuous symmetry (P6 §wall: *"the
boundary of the range is the loss of continuous symmetry"*; *"only the loss of all confining symmetry
frees the graviton's two transverse polarizations — the type-N plane wave, beyond the wall"*). The two
transverse polarizations **are** the handedness. P5 §open says it directly: *"the loss of the last
isometry is precisely the point at which the wave's polarization must turn from place to place."* The
polarization-turning *is* the handedness becoming un-undoable — there is no longer a rotation to rotate
$X_2\mapsto-X_2$ into the orientation-preserving class.

**The two distinguished places, on the null-degeneracy axis.** P6 §97 lays the reachable sector along one
axis with the **seam/Nariai** as inner boundary (maximal-but-frozen symmetry, still Type D) and the
**wall** as outer boundary (all degeneracy lost into the single propagating null direction, Type N). The
H³ reflection locus ($d=b$) sits inside this sector, where the mirror is *exact* (forward and backward
reads coincide); the wall is where the mirror can no longer be *taken*. Chirality lives in the gap: a
mirror the geometry identifies everywhere the sweep survives, and a genuine handedness exactly where it
does not.

**Verdict.** Chirality is *located*, not *found in the vacuum family*. Identified (a mirror, undone by the
swept $\mathrm{SO}(3)$) throughout the symmetric sector; genuine (the freed graviton polarization) at the
wall. The kinematic skeleton we cleared — two pins $\{p,-p\}$, the H³ reflection locus, the flip — is what
becomes a physical chirality when radiation turns on. That is why it would *gift*: a handedness that
cannot be undone is physical, and it arrives *with* the wave.

**Named target for the actual computation.** The chirality chase is hereby the **wall (P6) and the type-N
polarization (P9's confined transverse-traceless wave is the nearest worked case, pinned by one residual
isometry)**. The computation: track the survival of the mirror-undoing isometry across the sequence
*symmetric → confined (edge) → type-N (beyond wall)* — fully available in the symmetric sector, reduced at
the edge where one isometry remains, gone beyond the wall. The handedness becomes genuine exactly as the
last isometry that could undo it dies. That is first-principles and computable, the way 2/2′ and the H³
leaf were done.

## 6. Chirality computed — the turning of the polarization plane

The chase of §5 is now carried out at the wall, and the criterion falls out by computation, not assertion.

**The wall geometry.** P9 (prop:wall) fixes the wall as the Type-N vacuum, the plane-fronted (Brinkmann)
wave
$$ds^2 = 2\,du\,dv + H(u,x,y)\,du^2 + dx^2 + dy^2,\qquad H = h_+(u)\,(x^2-y^2) + 2h_\times(u)\,xy.$$
Direct computation (sympy, clean): the Ricci tensor **vanishes for any** $h_+(u),h_\times(u)$ — the two
transverse-traceless polarizations are free and independent. ($H$ is the harmonic quadratic; the trace
part is the matter bend, absent in vacuum.)

**The two operations on the polarization pair.**
- *Transverse reflection* $x\mapsto-x$: computed, $H\mapsto H-4xy\,h_\times$, i.e. $h_\times\mapsto-h_\times$,
  $h_+$ fixed. This sends $(h_++ih_\times)\mapsto(h_+-ih_\times)$ — it is the **helicity-flipping parity**,
  swapping the two circular polarizations. It is a symmetry of the wave **iff $h_\times=0$** (one
  polarization).
- *Transverse rotation* by $\theta$: computed, $(h_++ih_\times)\mapsto e^{-2i\theta}(h_++ih_\times)$ — a
  **spin-2 doublet**. The polarization angle is $\tfrac12\arg(h_++ih_\times)$.

**The criterion.**
- **Fixed polarization** — $h_\times=0$, or any constant ratio $h_+:h_\times$ (a linear polarization along
  a fixed, possibly tilted, axis): a fixed reflection axis *is* a symmetry, so parity identifies the two
  helicities $\to$ **no genuine chirality.** This is the polarized Gowdy of P9 §gowdy at the Type-I edge:
  one polarization pinned to a fixed global orientation by the residual $T^2$ (P9 §strata).
- **Turning polarization** — $\tfrac12\arg(h_++ih_\times)$ varies with $u$ (the plane reorients along the
  wave): **no** fixed reflection axis is a symmetry for all $u$, so no isometry identifies the helicities
  $\to$ **genuine chirality.** P9 §wall: *"the polarization must reorient from place to place."* That phrase
  is now not a slogan but the **criterion**. (Onset, refined in §7: this criterion bites from the loss of
  the swept $\mathrm{SO}(3)$ — Type D$\to$I — onward, not only at the wall; the wall is where it is
  generic.)

**The result.** Chirality is the **turning of the polarization plane**; the handedness is the $\mathbb{Z}_2$
sign of $\frac{d}{du}\arg(h_++ih_\times)$ — left vs right circular, helicity $\pm2$.

**Continuity with §5.** The reflection $x\mapsto-x$ at the wall is the descendant of the slicing picture's
$X_2\mapsto-X_2$. In the symmetric sector the swept $\mathrm{SO}(3)$ completed that reflection to an
orientation-preserving rotation and rotated it away (§5); at the wall the $\mathrm{SO}(3)$ is gone, so the
same reflection survives as genuine parity — and because the polarization turns, no fixed axis is left to
undo it. The same mirror, rotated away in the symmetric sector, un-undoable at the wall. Chirality lives
exactly in the gap §5 named.

**Scope, eyes open.** The helicity$\leftrightarrow$parity relation itself is standard gravitational-wave
physics; what is CR-specific and new here is the *placement and mechanism* — the symmetric sector
identifies the helicities (the swept $\mathrm{SO}(3)$ rotates the mirror away), the wall releases them, and
"polarization turns from place to place" is the exact chirality criterion drawn on the programme's own
stratification.

**Open interface — see §7.** What the helicity $\mathbb{Z}_2$ is, and where the chirality onset truly
sits, is settled (as far as the structure now allows) in §7.

## 7. What the helicity ℤ₂ is — the substrate parity, and the onset at the loss of spherical symmetry

The interface with the discrete skeleton (P9 §discrete, P10) is investigated here rather than labelled.

**The ℤ₂ is the substrate spatial parity.** The helicity-flipping reflection $x\mapsto-x$ (§6), the
wall-descendant of the slicing $X_2\mapsto-X_2$ (§5), is an *orientation-reversing* element of the
substrate isometry group: it lies in $\mathrm{O}(5,1)\setminus\mathrm{SO}_0(5,1)$, **outside the connected
group the algebroid acts by** (P10: the action algebroid is $\so(5,1)\ltimes\mathcal{C}$, the connected
$\mathrm{SO}_0(5,1)$). So the helicity $\mathbb{Z}_2$ is the substrate's **spatial-orientation
$\mathbb{Z}_2 = \mathrm{O}(5,1)/\mathrm{SO}_0(5,1)$**. It is *not* the Weyl $S_3$, which sits inside
$\mathrm{SO}_0(5,1)$ permuting the horizon roots (P10, groupoid).

**Absorbed in the spherical sector, released at the loss of the swept $\mathrm{SO}(3)$ — the true onset.**
§5 undid the parity with the $(X_2,X_3)$ $\pi$-rotation *of the swept $\mathrm{SO}(3)$*. But that
$\mathrm{SO}(3)$ is the isotropy of the **spherical** strata only (Type O/D: $\so(4,1)$,
$\mathbb{R}_t\times\mathrm{SO}(3)$). It is gone at Type I (Gowdy/Bianchi: isotropy the abelian $T^2$, no
$\mathrm{SO}(3)$ — P9 §strata, P10). So the parity is absorbed throughout the spherical sector and released
the moment the $\mathrm{SO}(3)$ dies — at Type D$\to$I, **not** at the wall. This refines §6: the spherical
sector carries no free radiation at all (Birkhoff, P6), so no helicity there; the first genuine
two-polarization wave is at the Type-I edge, where the *polarized* Gowdy (one fixed axis) is achiral and
the *unpolarized* Gowdy (two polarizations, turning) is the **first chiral case**; the wall (Type N) is
where chirality is *generic*. Chirality lives from the loss of the swept $\mathrm{SO}(3)$ onward; the wall
is its generic locus, not its onset.

**A clean corollary on where the chirality is visible.** At Type I the turning is carried by curvature with
nonzero polynomial invariants, so the handedness shows in a parity-odd invariant (the gravitational
Pontryagin density). At the wall (Type N) all polynomial curvature invariants vanish (VSI), so the
handedness is *not* in any polynomial invariant there — it lives in the wave's phase (the turning itself).
The chirality goes non-polynomial exactly as the geometry reaches the wall.

**Does it coincide with the $\mathrm{Aut}(A_2)$ mass-reflection $\mathbb{Z}_2$? Resolved — yes, on CR's
existence/occurrence ontology (P8, with P1 and P7).** (This supersedes both r382's "distinct" and r383's
"undecided": the corpus does settle it. r383 framed it as the open curve-vs-spacetime question; P8 answers
that question.) The mass-reflection $P:2M\mapsto-2M$ is realized geometrically as the **celestial
reflection** $w\mapsto-w$ — equivalently $r_0\mapsto-r_0$, since $r_0=\tfrac{2}{\sqrt3}\sin w$ (P3) — a
reflection of the observer's sky, hence a genuine **substrate isometry**, orientation-reversing, in
$\mathrm{O}(5,1)\setminus\mathrm{SO}_0(5,1)$. It induces $r\mapsto-r$ on the horizon roots automatically
($2M=r_0-r_0^3$ odd) and carries the $+M$ slicing-curve *on the substrate* to the $-M$ one, connecting them
across the $\mathrm{SO}_0$-orbits — consistent with the algebroid's "the *connected* action cannot reach
across the mass modulus" (the connected group cannot; a reflection can).

The $+M/-M$ non-isometry that r382 took as decisive lives at the level of the **Lorentzian record** $M$ —
the perspectival SdS metric, the groupoid's gauge freedom among causal assignments. P8 fixes which level is
the existent: *"What exists is the layer $\St$ — a real three-sphere evolving in a real de Sitter substrate;
the four-manifold $M$ is the representational record … its shadow."* Granting the records the status of
distinct *existents* is precisely the block-universe category error P8 dissolves — and it is the error r382
made. P1 and P7 supply the pieces: the horizon and $r=0$ are metric singularities **of the record**,
never-actualised features "no observer's present ever contains" (P8 citing P1); $r=0$ is real *as that
metric's*, never reached in cosmic time (P7); the de Sitter substrate beneath is smooth and symmetric, the
choice among Lorentzian causal readings a gauge organized by the groupoid (P8 §selection).

So on CR's ontology the substrate (existence) is fundamental and symmetric, and the mass-reflection and the
helicity are **one substrate-orientation $\mathbb{Z}_2 = \mathrm{O}(5,1)/\mathrm{SO}_0(5,1)$** — the same
parity, appearing as the mass-sign reflection in the symmetric-sector record and as the graviton helicity in
the radiating sector. The "distinct" reading is the shadow taken for the existent. (A block-universe reading
that grants the records existence would read them as distinct; that is the one stance CR rejects on
independent grounds — the CMB rest frame and the occurrence/existence distinction, P8 §necessity.)

**The $\mathbb{Z}_2$-level structure, resolved.**
1. **Weyl $S_3=W(A_2)$** — inside the connected $\mathrm{SO}_0(5,1)$; horizon permutation at fixed mass.
2. **The orientation $\mathbb{Z}_2=\mathrm{O}(5,1)/\mathrm{SO}_0(5,1)$** — the substrate's spatial parity,
   realized as the celestial reflection $w\mapsto-w$. It is *both* the $\mathrm{Aut}(A_2)$ diagram
   automorphism (mass-sign reflection, in the symmetric-sector record) *and* the graviton helicity (in the
   radiating sector): one parity, two perspectival guises.

So $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2$ reads cleanly — $S_3$ the Weyl group in the connected group,
the $\mathbb{Z}_2$ the substrate orientation — and the chirality of §5–§6 is that same orientation parity,
made un-undoable at the wall where the swept $\mathrm{SO}(3)$ that absorbed it is gone.

**The handling of P9 §discrete.** P9 records the wall as carrying none of the three cubic-organized markers
(root-collision, reassignment, signature flip), consistent with its being the purely-continuous generative
boundary. That stands: the helicity $\mathbb{Z}_2$ is **not** a fourth cubic-marker, nor the mass-reflection
$\mathbb{Z}_2$ (#2). It is the substrate-orientation parity (#3), a discrete structure of the **radiating**
sector (Type I onward), released when the swept $\mathrm{SO}(3)$ dies. So P9 §discrete needs no rewrite — an
*augmentation*: the radiating sector beyond the spherical strata carries the substrate-orientation
$\mathbb{Z}_2$ as the graviton helicity, a structure absent from the symmetric sector's $\mathrm{Aut}(A_2)$.
The wall is purely continuous as a generation boundary; the parity is released earlier, at the loss of
spherical symmetry, and is generic past the wall.
