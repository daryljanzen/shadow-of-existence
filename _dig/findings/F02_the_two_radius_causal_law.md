# F02 — The causal trichotomy at two independent radii, in closed form

*status: OFFERED (a compression, not a new substrate fact). Receipt: `DRAFT_P03_the_two_radius_causal_law.py`, runs clean, rc=0.*
*touches: P3 `sec:tour` / `sec:hinge-geometry`; `P03_the_sixth_equivalence`, `P03_hexagon_null_triple`, `P03_batch1_cheap_owed` (L-53), `THE_GEOMETRY_AND_THE_PHYSICS` §II.*
*for reversal: if this law is already written where I did not look, strike the receipt rather than merge it. A second statement of an existing law is worse than none.*

---

## How I got here, because it bears on the weight

I was reading `P03_the_sixth_equivalence` — the receipt that turns L-104's expected negative
("the excentres carry no relation the substrate can see") into a positive by running the causal
trichotomy over 36 hinge–excentre and 15 excentre–excentre pairs. It is a good receipt and it
records its own refutation honestly. What caught me was Part 6: it derives
`s² = 4α² − ρ²` for a cross-horn pair at equal radius ρ and 120° separation, and reads off that
the pair goes null at ρ = 2α.

That derivation does not use the 120° except at the last step, so I ran it at general separation
and general radius, and the thing collapsed.

## The law

Write **β = arccos(α/ρ)** — the angle at the *centre* between a point's own radius and the point
where its tangent meets the throat. (β is the complement of P3's half-subtense
w = arcsin(α/ρ): w + β = 90° identically, being the two acute angles of the tangency right
triangle O–P–T. `dial_360` already uses ψ for a ray direction at the hinge, so β is a fresh
letter and would need a §0 canon entry if this is kept.)

For two substrate points at transverse radii ρ₁, ρ₂, azimuthal separation Δ, on horns ε₁, ε₂:

> **s² = 2α² · [ cos(β₁ − ε₁ε₂ β₂) − cos Δ ] / (cos β₁ cos β₂)**

— the **sum** β₁+β₂ across horns, the **difference** β₁−β₂ within one. Since cos βᵢ > 0 strictly,
the whole trichotomy is one comparison of angles:

| | timelike | null | spacelike |
|---|---|---|---|
| **cross-horn** | Δ < β₁+β₂ | Δ = β₁+β₂ | Δ > β₁+β₂ |
| **same horn** | Δ < \|β₁−β₂\| | Δ = \|β₁−β₂\| | Δ > \|β₁−β₂\| |

Verified symbolically (residual exactly 0 in both horn cases) and against the raw embedding at
200 000 random (ρ₁, ρ₂, Δ, horn), max deviation 2×10⁻¹³. A deliberately wrong law — sum and
difference swapped — misses by O(100), so the check has teeth.

## What it buys

**① The null condition is chord-tangency, at any two radii.** Δ = β₁+β₂ says the tangent drawn
from P₁ toward P₂ and the tangent drawn from P₂ toward P₁ touch the throat at the *same* point.
So:

> **Two substrate points are null-separated iff the chord joining their transverse shadows is
> tangent to the throat.**

The corpus has the one-point version of this and calls it a keystone —
`THE_GEOMETRY_AND_THE_PHYSICS` §II: *"The tangent from any point to the throat is a null line of
the embedding. The power of a point and the null condition are the same equation."* This is its
two-point form, and it is what makes the keystone usable on a *pair* rather than on a point.
`prop:twoalpha`(iii)'s midpoint tangency is the equal-radius case: β₁ = β₂ puts the contact at
the chord's midpoint. Unequal radii move the contact off the midpoint but do not move the
tangency — which is exactly the freedom the hinge triangle does not have and the excentre
configuration does.

Checked at ρ = (2,2), (2,4), (1.05,6), (3,1.5), (4,4): distance from axis to chord = α to twelve
places, s² = 0 to machine zero, every time.

**② `P03_the_sixth_equivalence`'s two tables are the law's evaluation table.** All 51 pairs fall
into ten classes, and all ten are β(2α) = 60° and β(4α) = arccos(¼) = 75.522° put into the
comparison above. Every row agrees with brute-force embedding. In particular the receipt's
striking result — *"the excentres are null-inert but not causally inert; the cross class has
moved past nullity"* — is just 2β(4α) = 151.045° > 120°: the excentres overshoot. And its
own-wall rule — *"an excentre over the hinge's own wall is spacelike in both horns"* — is
Δ = 180° > 135.522° = β(2α)+β(4α).

**③ The hinge radius, said causally.** *2α is the radius whose tangency angle is half the
threeness separation*: 2β = 120° ⟺ β = 60° ⟺ α/ρ = ½. This is the same sentence L-53 already
writes at general D (`R = α/cos(π/(D−1))`, null iff one station step). The two-radius form adds
that the excentres at 4α — which lie on **no** station polygon, so L-53's statement does not
reach them — fall out of the same rule.

## A restatement of sin 3w = 1, offered at that weight

In the tangency right triangle, w + β = 90° always; the hinge placement is β = 2w; therefore
**3w = 90°**, which is P3's `sin 3w = 1`. So the triple-angle identity's "3" is *the number of
half-subtenses in a right angle*, and Nariai-at-the-hinge is the statement that the tangency
triangle is the **30–60–90**.

At general D, β = π/(D−1), so β = 2w forces 3π/(D−1) = π, i.e. **D = 4 and no other**. The
matching uniqueness in the ratio: arccos x = 2 arcsin x reduces to 4x³ − 3x + 1 = (x+1)(2x−1)²,
whose only positive root is x = ½ — so ρ = 2α is the *unique* radius at which the throat's
tangency angle equals its subtense angle. P3 lists both 60° facts among its five equivalences;
this says why they are the same 60°, and that they are so at one radius only.

`FIGURE_THEOREM_LEDGER` ⊢5 reaches 3w = 90 by *"a sine peaks a quarter turn from its zero"* and
⊢31 by the kaleidoscope 360/(3×4). This is a third route and its only advantage is that D−1
appears in it explicitly, so the D = 4 selection is *read off* rather than checked. Recorded as a
restatement.

## Honest weight, and what is not claimed

The algebra is elementary and every specialisation the corpus needed, the corpus had — at 2α
(`P03_hexagon_null_triple`), at general D on one polygon (L-53), at two radii by enumeration
(`P03_the_sixth_equivalence`), and at one point (`THE_GEOMETRY_AND_THE_PHYSICS` §II). **No new
substrate fact.** What is offered is that one line returns all four, carries the trichotomy off
the station polygon to arbitrary radii, and replaces a 51-pair enumeration with a comparison of
two angles.

Not claimed: any new dimensional selector (Part 6 renames the one the appendix's dimension sweep
already found when it split P3's five equivalences two-and-three); anything about the wall, the
seam, or the bead; any bearing on the matter-sector reading, which `P03_twelve_null_legs` is
explicit does not follow from this figure.

Where it might belong is a judgement for the source. My guess — offered as a guess — is that ①
is the part worth having in P3's own voice, because the paper's tangency equivalence is currently
a fact about a triangle and this makes it a fact about the substrate; and that ②–③ belong in the
receipt layer as a consolidation of `P03_the_sixth_equivalence` rather than as new claims.
