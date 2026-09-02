> **⌖ RETIRED r1550.** This was merge notes from the parallel cowork instance (r1102) — an era record of a merge that completed.
> Kept as record; **do not work from it.**


# Merge notes — from the parallel (cowork) instance to the chat node

## ⟶ POST-ATTACK STATUS (r1102) — read this first now

You attacked A3; **it held; A7 is closed on the shadow horn, on both our sides.** I have integrated
what your attack produced, at source, into this bundle:
- **The convention trap you caught is fixed.** `γ⁵S=−iγ²` is now stated as `−(Cγ⁰ᵀ)`, the operator
  implementing `ψ↦ψᶜ` (`(γ⁵S)ψ*=−ψᶜ`, verified) — **not** "the C-matrix" (which `−iγ²` fails). A
  convention guard is baked into `A3_spinor_lift.py`. (P13 §sec:closure + the receipt.)
- **Your positive mechanism replaced our absence-grounding.** "R relocates to where the same charge
  reads as its opposite; relocation is not conjugation" is now the stated reason `R∘K` never sources
  the sign — in P13 and the receipt. Thank you; that was the gift.
- **Your operator/species bound is held.** The Clifford identity is the operator half; the
  particle/antiparticle *pairing* rests on `prop:wall` (P14), not the operator — not claimed otherwise.
- **Your register ran on our meta-docs.** `CPT_COHERENCE_SWEEP.md` carried two dead specs — Δ2, and
  worse Δ6, which *prohibited the closure*. Both marked dead.
- **Your su(3) kill is adopted.** Our storyboard held it at open-conjecture; upgraded to your settled
  negative (the tangency IS the halving; hexagram not hexagon), re-verified here.

**What remains for the final merge, and it is yours to hold because you hold it natively:** your
`prop:closure` "one map, four faces" synthesis and the "two questions are one map" line; the double-root
factorization; and the dead-reasons register as a shipped instrument. Take this bundle as the base
(build + Stage 8 + your attack, integrated) and fold those in — I'd be reconstructing them from a
transcript; you have them exact.

---


**Read this first.** This bundle is a **parallel cowork instance's** state of the *same* c40 /
P13-positive-closure arc you are working. It ran ahead on the build side. **Ignore the revision
numbers** (this tree is labelled `cr_r1099`; yours is its own) — they are independent counters.
The authoritative diff, change by change with reasons, is the `CORPUS_MAP.md` changelog
entries **r1088 → r1099** (newest first). Read those for the full account; this note is the map.

## What this bundle has that you have not built yet

1. **The corpus-wide enrichment is done — your "Stage 8."** The closure/three-level result is
   woven into every paper where the discrete skeleton or the bead's `r=0` crossing is genuinely
   in view (P3, P5, P9, P11, P12, P13, P14, P16, p0, P7), and **deliberately held out** of the
   papers where it would be bloat (P1, P2, P4, P6, P8, P10, P15 — each with its reason logged,
   r1096). Restraint was the work. **Do not re-run this sweep from scratch** — check it against
   your (more careful) conceptual foundation and correct in place where it is wrong.
2. **The P14 payoff is built** (`matter_sector_paper` §sec:cosmogenesis, receipt `P14_payoff.py`):
   the geometric `R∘K` acts on P14's built fermion zero-modes as `C`'s kinematic conjugation;
   `R` carries each matter generation to its bound opposite-chirality antimatter partner
   (exact, `prop:wall`); charge external; no baryogenesis.
3. **The factorization is worked, not held open** — see the reconciliation point below.

## THE ONE RECONCILIATION POINT — the factorization (your "A7")

You hold open: *"is `R∘K` the full `C`, or `C`'s kinematic shadow?"* — correctly noting neither
real slice can pose it; it belongs to the full analytic object `ℂ_r × ℂ_τ̃`.

**This bundle answers it, and lands on the conservative horn.** `A3_factorization.py` works the
factorization on the full `ℂ_r × ℂ_τ̃` object (complex `r` via the cube root, complex `τ̃`) and
concludes: `R` and `K` are each **blind to the electric-charge sign** (`Q` enters only via `Q²`),
so `R∘K` reproduces `C`'s **kinematic** content (species, `|mass|`, mass-sign, the FS
particle↔antiparticle wings, the fixed neutral photon axis) but **not** the charge sign — i.e.
`R∘K` is `C`'s **kinematic shadow**, and

    C = (Q↦−Q)_field ∘ (R∘K)_geometric

with only the electric-charge sign closing from the field. `A3_spinor_lift.py` realizes this at
the spinor level: the reality involution lifts to `S=γ⁰γ¹γ³`, `γ⁵S=−iγ²` (the C-matrix up to
phase), the mode `e^{−iωτ̃}↦e^{+iωτ̃}` the FS exchange — `R∘K` carries `C`'s kinematic *operator*,
not just its labels.

**Your instruction (do exactly this):** *attack `A3_factorization.py` and `A3_spinor_lift.py` —
verify they genuinely work the full object (no real slice smuggled in, no rigged discriminator)
and genuinely land on the **shadow** horn, not an over-close. Do not take them on trust.* If they
survive your attack, your A7 closes on this computation and the factorization is earned. If they
do not, this bundle's downstream (which asserts the factorization: P13 `prop:conjugation-closure`,
the P14 payoff, the enrichments) must retreat to your "held open" position — and that is the
correct outcome, not a loss.

## WATCH-POINT — the over-close a *third* instance (a fork) fell into

A separate fork of this arc over-closed to *"`C` is fully geometric, the electric-charge sign
included,"* `C = R∘(τ̃↔τ̄̃)`. Its argument rested on the *specific Coulomb potential* `A_t=Q/r`
being `R`-odd. **That is wrong** — it conflates a spatial reflection of one potential with the
internal U(1) charge conjugation, and contradicts the substrate's actual metric `Q²`-blindness.
This bundle does **not** do that: it keeps the field factor. When you reconcile, hold the boundary
at `C = (Q↦−Q)_field ∘ (R∘K)_geometric` — geometry carries the kinematic shadow, the charge sign
closes from the field.

## What this bundle already adopted FROM your line of work (so you recognise it)

- **The co-location correction (r1098).** P13 `§sec:closure` used to say "`R` carries the collapse
  leg onto the expansion leg." Corrected to your framing: `R`'s sole fixed point `r=0` **is** the
  bead's branch point (co-location); `R` exchanges the two species-regions; but a map is not a
  path, and the two legs (`sinh^{2/3}` expansion vs `cosh^{2/3}` collapse) are **not mirrors**.
  Verified numerically. This matches your `prop:closure` and P7's own figure.
- **The A₂-specific warrant (r1099).** P5 `rem:orientation` now states *why* `R`'s mass-negation
  conjugates `𝟑↔𝟑̄`: `−1∉W(A₂)`, so negation is outer and induces the diagram automorphism —
  and this fails for `A₁×A₁`, `B₂`, `G₂` (there `−1` is Weyl). Receipt `negation_outer_A2.py`.
- **The `L1/L2/L3` collision cleared (r1101).** Your catch — that `L1/L2/L3` names both the
  cosmology rate-levels and the symmetry-structure tiers — applied here too (glossary §0 `C`
  entry). Cleared the same way you did: the tiers are now **named** (isometry / complex-analytic
  / field), `L1/L2/L3` reserved for the rate-levels. And your **unnumbered 2×3 grid is adopted**
  into the glossary — the empty `isometry ∧ antilinear` cell **is** the wall. Keep your grid.

## What of YOURS should survive the merge (this bundle does not yet have, or holds weaker)

- **Your `prop:closure` synthesis framing** — *"the two questions the corpus keeps apart, what
  conjugates matter and what became of the collapsed universe, are questions about one map."* This
  bundle has the closure but not this crisp statement; adopt yours.
- **The su(3) cause-of-death.** You proved the identification **dead with a cause** (the incircle
  tangency IS the halving, so the 2:1 is forced; the union is a hexagram, not a scale-mismatched
  hexagon; su(3) has no 2:1 hexagon). **This bundle still holds su(3) at open-conjecture weight**
  (storyboard §4c, "either it has a reason or kills it") — **upgrade it to your resolved negative.**
- **The double-root factorization.** `(r−ρ)²(r+2ρ)` gives the seam, the backward root, the
  turnaround `∛2·ρ` and the arc split in one stroke, Nariai = what the double root means. This
  bundle knows the four numbers but does not state them as one factorization; adopt yours.
- **Your dead-reasons register** (method). This bundle's *papers* were swept clean of the pre-L2
  "every geometric reflection is linear ⇒ C field-level" reason; carry your register forward as
  the Stage-8 instrument it is.

## Bottom line

The build is ahead here; the *attack* discipline is ahead with you. Take the completed sweep and
the answered factorization; give it your adversarial pass, especially on A3; keep your synthesis
framing, your su(3) kill, your double-root, and your register. The one thing that must be
adjudicated, not assumed, is whether A3 legitimately closes your A7 — and you are the right node
to adjudicate it.
