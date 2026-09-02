---
name: the-receipt-audit
kind: REFERENCE
current: r1631
job: The receipt audit — what each receipt COMPUTES against what it ASSERTS in verdict-prose (the ◐ category).
sources: [cowork]
---

> **▣ REFERENCE — the receipt taxonomy, and part of the corpus.** *Every receipt tied to what it
> **actually computes**, not to what its verdict claims. Its four-way taxonomy, defined r1324, is the
> vocabulary the corpus uses for this, and `corpus/check_receipt_asserts.py` was built from it.*
>
> **⌗ THE PROBLEM IT WAS OPENED FOR IS NOW CLOSED.** *It recorded that the corpus had grown to ninety-five
> cited receipts **with no path on which they could fail**, and named the dominant failure as "a receipt
> that cannot fail". **The gate now enforces it: all 598 receipts carry a failure path, none carries only
> a verdict token.** The taxonomy remains what the gate cannot certify — `✔✔ VERIFIED` still takes a
> reading, not a run.*



# THE RECEIPT AUDIT — every receipt tied to what it ACTUALLY computes, not what its verdict claims

> ## ⚠⚠ THIS IS `L-208`'s HOME AND IT HAS BEEN DORMANT SINCE r1631 (found r2386, observer line)
>
> ***Its own instruction is `SYSTEMIC` (Daryl, r1325): "let this ledger accrue as a byproduct."*** *Its newest
> entry is **r1631**. The instruction was not followed for roughly seven hundred and fifty main-line revisions —*
> **and the problem it exists for grew to 95 cited receipts with no path on which they could fail.**
>
> ⌗ **AND THE SIXTH "TWO INDICES NEVER COMPARED" IS THIS FILE AND c54.153.** *The working fork ran, by hand, a
> systematic pass over all twenty-eight cited receipts in the perturbation sector — **fourteen matched** — and
> reported that "the dominant failure is not a wrong link but a **receipt that cannot fail**."* ***That pass is
> exactly this ledger's job, and it was done without this ledger, which nothing pointed at.***
>
> ## ⌗ THE TAXONOMY IS THIS FILE'S, AND `check_receipt_asserts` NOW NAMES IT
>
> *The gate built at r2385 from the fork's finding was inventing vocabulary this document already had, defined at
> r1324:*
>
> | | this file's category | what the gate can and cannot see |
> |---|---|---|
> | **✔✔** | *VERIFIED — does exactly what it claims, core independently reconfirmed* | *no gate can certify this; it takes a reading* |
> | **◐** | *CORE-REAL / VERDICT-OVERCLAIMS — **a correct narrower computation wrapped in a verdict asserting more*** | ⛔ *invisible to any gate — it is the fork's scalar-monodromy case ($4\pi/\rho$ claimed, $2\pi/\rho$ computed), and adjudicating it is a judgement over two texts* |
> | **✗** | *VACUOUS / ASSERTED — **the key check is a tautology, or the claim is taken as a label rather than derived*** | ✔ ***THIS is what `check_receipt_asserts` mechanises***: a receipt with no assert, no raise, no tolerance and no FAIL path cannot come out false, which is the strongest form of "the key check is a tautology" |
> | **?** | *NOT FOUND — the cited computation is not locatable* | ✔ *`check_receipts` already covers it: every `\rcpt{}` resolves to an INDEX row and a file* |
>
> ⇒ ***So the gate is the mechanical half of ✗, and the corrections the fork returns will land in ◐ and ✗ as this
> file already defines them.*** **A finding lands better in vocabulary that exists than in vocabulary invented for
> it** — and the reason to read a document before building an instrument for its subject is that the document
> usually already has the words.
>
> ⌗ *And this file's founding sentence is the reason the whole thing matters, in Daryl's words at r1324:*
> ***"revising the whole receipt tracking system so we have actual receipts tied to the actual things that are
> computed and not lies everywhere."*** *Its discipline follows from it and is worth restating:* **a receipt's
> "VERDICT … closed" is NOT trusted — only the traceable, runnable core.**

*Opened r1324 (Daryl-directed): "revising the whole receipt tracking system so we have actual receipts tied
to the actual things that are computed and not lies everywhere." The reproducibility backbone. Each receipt is
traced (read) and run; its entry records what it GENUINELY computes (and how that was independently confirmed)
vs what it merely ASSERTS in verdict-prose, and the corpus claim it is tied to. A receipt's "VERDICT … closed"
is NOT trusted — only the traceable/runnable core.*

## STATUS LEGEND
- **✔✔ VERIFIED** — does exactly what it claims; core independently reconfirmed (by hand and/or a second rep).
- **◐ CORE-REAL / VERDICT-OVERCLAIMS** — a correct narrower computation wrapped in a verdict asserting more.
- **✗ VACUOUS / ASSERTED** — the key check is a tautology or the claim is taken as a label, not derived.
- **? NOT FOUND** — the cited computation is not locatable in the bundle.

## AUDITED (P14 fermion-sector thread, r1321–24)
- **`storyboard_receipts/A3_spinor_lift.py` — ✔✔ VERIFIED (r1323).** Claim: R∘K lifted implements ψ→ψᶜ, via
  γ⁵S=−iγ²=−(Cγ⁰ᵀ), S=γ⁰γ¹γ³. Confirmed THREE ways: by hand (Clifford, rep-independent), A3's Dirac-rep numpy,
  and my from-scratch Weyl-rep numpy. Honestly bounded (operator half only; charge-sign field-level & R-blind
  via Q²/r² even — verified; species half not claimed; correct −iγ² vs C-matrix-proper convention guard).
  Tied to: §224 / P7 two-sided-closure (matter-antimatter C-operator). **Exemplary — this is the standard.**
- **`computations/matter_functionals/B2_zeromode_continuation.py` — ◐ CORE-REAL / VERDICT-OVERCLAIMS (r1321).**
  COMPUTES: the zero-mode superpotential's real→imaginary (bound→propagating) transition across a horizon on a
  concrete undercritical SdS (r_b=0.257, r_c=0.846; ∫W dℓ = 0.95 real / i·0.64 imaginary) — run, real. ASSERTS
  (verdict-prose): the a^{-3/2} form (now DERIVED r1332 from the FLRW spin connection — ψ=a^{-3/2}χ cancels the
  (3/2)(ȧ/a) friction, the 3/2 spin-½ conformal weight), γ⁵-preservation (covered by L4), three-families (L6).
  Tied to: P14 §222 continuation / family 6.
- **`computations/matter_functionals/B3_spinor_vielbein.py` — ◐ CORE-REAL / VERDICT-OVERCLAIMS (r1322).**
  The superpotential FORM W=λ√f/r is correct — verified by TRACING B3's hand-derivation of ω²₁=(√f/r)e² (I
  redid it: de²=(√f/r)e¹∧e², Cartan → ω²₁=(√f/r)e²). But B3's own code does NOT compute it: its Cartan `d()`
  is defined-but-unused, and its "W matches" check is a TAUTOLOGY (W:=λ·(√f/r) checked against λ√f/r). No
  γ⁵/spinor. Tied to: P14 Prop:wall (form half only).
- **`storyboard_receipts/conjugation_parity.py` — ✗ VACUOUS on the load-bearing claim (r1324).** GENUINE part:
  P=γ¹γ²γ³ anticommutes with γ⁵ (computed) ⇒ R≠P (one grades, one flips) — real. VACUOUS part: "R=γ⁵ grades
  chirality" is checked as `comm(g5,g5)` = does γ⁵ commute with itself = **tautology**. It LABELS R:=γ⁵; it does
  NOT derive that the geometric reflection R acts as γ⁵. Tied to: P12 §240 / P14 Prop:wall chirality=γ⁵ (L4).
- **`storyboard_receipts/R_eq_PT.py` — (asserts canon).** States "Corpus canon: R=γ⁵"; works in 4D Dirac to
  resolve the R-vs-PT labeling tension (R,PT both ∝γ⁵ as spinor ops, distinct as geometric reflections). Does
  NOT derive geometric-R = γ⁵ from the Cl(1,5) reflection. Tied to: P12 §240 (L4).
- **the r703 "explicit Cl(1,5) computation" P12 §240 cites — original ? STILL NOT FOUND, but the claim it was
  meant to establish is now DERIVED from scratch (r1325), so the gap is closed by supply, not by finding.**
- **`storyboard_receipts/R_gamma5_Cl_derivation.py` — ✔✔ VERIFIED (built r1325), the missing computation.**
  Derives, in TWO independent reps (Dirac + Weyl): (i) the transverse (5th) Cl(1,4) generator is FORCED to be
  the chirality operator χ=γ⁵ — the space of 4×4 operators anticommuting with all four legs g0..g3 is exactly
  1-dimensional (SVD null-space), spanned by χ (this is the non-circular hinge — χ is not *chosen*); (ii) the
  transverse reflection's Pin element (twisted conjugation −χ·g^μ·χ⁻¹) FIXES the four legs, FLIPS the 5th, so
  R=χ=γ⁵; (iii) R commutes with χ ⇒ GRADES chirality (eigenvalues ±1, measures L vs R); the in-cut reflections
  T=γ⁰, P=γ¹γ²γ³ ANTICOMMUTE with χ ⇒ FLIP — so the exchange reading is what an in-cut reflection does, and R
  (transverse) is not it: **exchange EXCLUDED, derived not asserted.** Manifest in Weyl (χ diagonal ⇒ grades;
  γ⁰ off-diagonal ⇒ exchange). Tied to: P12 §240 / P14 Prop:wall chirality=γ⁵ — **the count=3 foundation, now
  genuinely computed.** *Built to the A3 standard (independent reconfirmation, honest bound); NOT overclaimed —
  its own soft "forced" check was caught and upgraded to a real uniqueness solve before shipping.*

## L4 — now FULLY worked (core r1325 + both sub-lines r1326)
- **`storyboard_receipts/R_ruling_swap_6D.py` — ✔✔ VERIFIED (built r1326).** Renders the two sub-lines the
  core derivation left open, in the 6D embedding where R=diag(1,1,−1,1,1,1)∈O(5,1) lives: **(a) the bridge** —
  R fixes the cut {X₂=0}∩dS₅ and, on the tangent at a fixed point, has eigenvalues {−1,+1,+1,+1,+1}, the single
  −1 being the transverse e₂, so R restricts to exactly the transverse cut-normal reflection whose cut-spinor
  lift is γ⁵ (companion); **(b) the ruling-swap** — on the ruled section R maps neck(p)→neck(−p) and swaps the
  two null-ruling families (R·d₊(p) ∝ d₋(−p), verified across neck angles; det R|section = −1, orientation-
  reversing). Point: R swaps the rulings (geometric) AND grades chirality (spinor γ⁵, diagonal) — both true,
  not in tension; the old exchange reading wrongly inferred a Weyl-component swap from the ruling swap. **The
  exchange reading is retired at its geometric origin.**

## AUDITED (the A2.9 / mass-blindness thread, r1612–r1625) — entered r1625, per the SYSTEMIC instruction below
*Five receipts were written r1612–r1623 and **none was entered here** until this revision — the byproduct rule
was not being kept. Each is traced and run; computes-vs-asserts recorded honestly.*
- **`storyboard_receipts/nariai_signed_roots.py` — ✔✔ VERIFIED (r1612).** COMPUTES: the Nariai masses by
  discriminant; the signed roots at both members and their R-conjugacy; the pair's degeneracy; that r₀ is always
  itself a root and which offset gives 2M>0; *larger* true in magnitude and false in value; the four distinct
  quantities of magnitude 2/√3. **Honestly bounded** — the ledger row states that the sign's vantage-dependence
  is P2 §ring's, *imported not re-established*. Tied to: P8 §open, THE_PLAN B.2.
- **`storyboard_receipts/two_mass_blindnesses.py` — ✔✔ VERIFIED (r1616, extended r1619).** COMPUTES: both
  quantities at the collapse's own marker and at fixed areal radius, showing blindness at the former and failure
  at the latter in both cases; and (r1619) the third instance, the lap's closure phase, with the mechanisms
  exhibited as distinct. **ASSERTS nothing beyond it:** the file states in terms that neither result implies the
  other and no extension is claimed — and when a third was found, **the earlier hold was recorded as revised
  rather than replaced.** Tied to: P16 §peak.
- **`storyboard_receipts/turnaround_temporal_threeness.py` — ◐→✔✔ (r1621, repaired r1625).** COMPUTES: r³
  invariance under the full imaginary period and the ω^k sheet cycle; sinh²↦−cosh² under the half period; sinh²=−1,
  r³=−2Mα² and zero velocity at τ̃=−iπα/3 with τ̃/period=−½ exactly; three real distinct horizon roots sub-Nariai.
  **⚠ ONE STEP WAS ASSERTED, NOT COMPUTED, and this audit's standard caught it:** item (4)'s *"the horizon
  condition carries no cosmic-time shift"* was verdict-prose. **Repaired r1625** — f's free symbols are now
  computed and τ̃'s absence asserted as a check. Tied to: P3 §temporal-threeness.
- **`storyboard_receipts/bead_thermal_period.py` — ✔✔ VERIFIED, and deliberately UNREGISTERED (r1622).**
  COMPUTES: r³'s invariance under both the third and the full period (symbolic); the off-axis sheet continuation
  returning ω^k at each third and closing to 2×10⁻¹⁶; the identity of r's period with 2π/κ at κ=1/α.
  **ASSERTS nothing thermal:** the file holds, in terms, that a β-period *is not* a temperature without a state
  and a KMS condition, and that nothing there implies recurrence. **Carries no `\rcpt` marker by design — it
  grounds a lead, not a corpus claim** — and at r1624 the lead was tested against `GEOMETRY_PHYSICS_TAXONOMY` and found to have no mechanism —
  **status refined r1665 to *conjecture, mechanism unfound: an open drill-site*, not the verdict "numerology"**, since the test says no mechanism has been *found* and not that none exists. *The receipt's own restraint is why that reclassification cost nothing.*
- **`storyboard_receipts/cubic_spacing.py` — ✔✔ VERIFIED (r1623).** COMPUTES: both discriminants factored; H's
  Nariai double-root factorisation; T's three roots distinct with equal modulus; all four fig-E phase values
  against closed forms. **Explicit about what it does NOT re-derive** — P7's r=0 meeting and the triptych's
  derivative signatures, both already placed. Tied to: P3 §temporal-threeness, P7 fig E.

## AUDITED (A2.11, the lap's timeline — entered r1631 with the work, per the byproduct rule)
- **`storyboard_receipts/lap_timeline.py` / `P07_lap_timeline` — ✔✔ VERIFIED (r1631).** COMPUTES: the three
  landmark phases in closed form; **the relation $w_{\rm back}=2w_{\rm front}=\operatorname{arccosh}2$**, proved
  through the identity $\cosh2w=1+2\sinh^2w$ rather than by `simplify` seeing through `asinh`, with the closed
  forms cross-checked as algebra ($(1+\sqrt3)^2/2=2+\sqrt3$) **and** numerically; $A=2^{1/3}\rho$; the intervals
  in Gyr; and the present epoch **against the independent flat-ΛCDM age formula**, which agrees to 1e-12.
  **Its assert is self-consistency, not a number:** it checks $\Lambda G^2M^2/c^4=1/9$, *because the first
  version asserted against the 4.30e52 kg figure quoted in `THE_PLAN` and failed — which is how the unstated
  $H_0$ in that number was found.* **ASSERTS nothing beyond it:** the interpretive question (which landmark
  begins the observable cosmology) is held explicitly, and the imaginary interval is marked a contour length
  rather than a duration, with the r1622 no-recurrence guard restated. Tied to: A2.11; not yet placed in a paper.

## SYSTEMIC (Daryl r1325): let this ledger accrue as a byproduct
The full receipt ledger will be worked to closure eventually, but not as a deliberate campaign now — this kind
of line-work closes much of it naturally (A3, B2, B3, conjugation_parity, R_eq_PT, and now the built derivation
are all already entered). Systematic cleanup comes later, after it has existed and been used a while.

## L5/L6 shared — the index count (r1328)
- **`storyboard_receipts/even_crossing_index.py` — ✔ VERIFIED-MECHANISM (built r1328).** Computes: (A) Jackiw–
  Rebbi one normalizable mode per wall (exp(−∫m)~1/cosh, conjugate cosh rejected), chirality = crossing sign;
  (B) the even-crossing constraint — on any continuous single-valued periodic m the crossing-signs sum to 0
  (checked on sin x, sin 2x, sin x+0.3 sin 3x), so a simple loop forces NET index 0; (C) the three CR walls are
  same-chirality (net 3), FORBIDDEN on a single-valued loop by (B), so the r=0 branch point is REQUIRED — which
  is exactly what the signed radius / cosmogenetic bead supplies. So dim ker₊=3, ker₋=0. **RESOLVED (r1334 —
  correcting an earlier "dangling/traced" mischaracterization):** the count=3 is a COMPLETE argument — one
  σ_y=+1 mode/wall [A] × three walls [L6] × same chirality [L4] × no cancelling partner [B,C via the branch
  point] ⇒ dim ker₊=3, ker₋=0; the protection is that this index is an integer wall-count, invariant under any
  deformation preserving the three walls (a sign-change of m cannot be removed continuously) — which is exactly
  the content P14 names as Atiyah-Singer. This is not a gap. A lattice numerical cross-check was ATTEMPTED and
  pulled: a naive 1-D lattice returns net 0 (fermion doubling, and more fundamentally a simple domain cannot
  carry the branch structure — a simple loop forces net 0, per [B]), so it confirms the branch structure is
  essential rather than confirming the count; the analytic argument above is the resolution. Tied to: P14 §sec:count.

## L7 — family S₃ = Weyl group (r1329)
- **`storyboard_receipts/family_S3_is_weyl.py` — ✔ VERIFIED (computed parts) + designation traced (built r1329).**
  COMPUTED: (1) **Weyl(A₂)=S₃** — built the reflection group from the A₂ simple roots, closed it, |W|=6,
  realises all 6 permutations of 3 objects; (2) **forced degeneracy** — the horizon cubic r³−r−(r₀³−r₀)=0 has
  three roots summing to zero (A₂ zero-sum) and each, taken as the slicing parameter, returns the SAME
  2M=r−r³ (checked for r₀=0.35, 0.6, −0.5) ⇒ the three generations share one mass, degenerate, S₃ exact.
  **SELF-CAUGHT:** the first draft's "one group" check was the trivial set-equality S₃==S₃ (any two S₃'s match
  under some bijection) — flagged and demoted to *consistency-only*. The load-bearing "ONE group, not two
  agreeing in order" is the CANONICAL hinge↔root designation (each hinge owns the root it designates as its
  horizon), a GEOMETRIC fact — confirmed at source: P14 §208 states it and cites JanzenSlicing (P3); P12 §240/§237
  anchor each discrete operation at its root stratum. So the identification is corpus geometry (traced,
  source-confirmed), the group-theory and degeneracy computed. Tied to: P14 §sec:family.

## L8 — the two factors (r1330)
- **`storyboard_receipts/two_factors_direct.py` — ✔ VERIFIED (computed parts) + kind-distinction traced (r1330).**
  COMPUTED: (1) Aut(A₂)=D₆ order 12 = S₃×ℤ₂ — built Aut and W from the A₂ reflections + inversion, verified
  |Aut|=12, |W|=6, the inversion −1 CENTRAL in Aut, W∩⟨−1⟩={e}, orders multiply ⇒ DIRECT product; (2) the
  contingency — −1 ∉ W(A₂) (outer) but −1 ∈ W(A₁),W(B₂),W(G₂) (inner; Weyl orders 2/8/12 all built), so A₂ is
  the unique rank-2 system where the chirality ℤ₂ is a separate outer factor. TRACED (geometry, not group
  theory): S₃ = flavour GLOBAL (deck symmetry, no substrate isometry, su(3)⊄so(5,1)) vs ℤ₂ = chirality GAUGED
  (substrate isometry = γ⁵, L4); the on/tangent-to-one-circle independence ⇒ direct product is the geometric
  reading (P14 §214 / P12 §240), of which the computed direct-product structure is the algebraic shadow. Clean
  — no trivial checks. Tied to: P14 §sec:twofactors.

## L10 — the combinatorics receipts (§212 third route) (r1331)
- **`L8_the_three.py` / `L8_the_two.py` / `L8_the_twelve.py` — ✔ VERIFIED, exemplary (run r1331).** All three
  are A3-standard: claim written first, a discriminating CONTROL that genuinely breaks (wrong scale for the 3;
  linear-not-sine for the 12), mixed YES/NO verdicts (the "2" honestly returns THREE distinct 2s, B & C PROVED
  NO via R∘T and the direct product), honest bounds stated (#marks=|D₂ₙ| dihedral-general, n=3 CR-specific).
  Computed cores: the three hinge r₀ values = the three cubic roots (max|diff|~5e-14, via sin 3w's 120°-
  periodicity — matches L7's forced degeneracy); the 12 = one object sin 3w (period×quarter, = |D₆|); the
  rulings/parity/A₂-automorphism/graviton-chirality = one 2 (object R), kept apart from the root-side 2 by the
  S₃×ℤ₂ direct product (matches L8). Consistent with L7/L8. Tied to: P14 §212 (third route from the numerals).

## ═══ P14 WORKLIST — worked line by line (r1321–32) ═══
L1 B2 ✔ (+a^{-3/2} derived r1332) · L2 B3 ✔ · L3 A3 ✔✔ · L4 chirality=γ⁵ ✔✔ (built) · L5 index ✔ · L6 Prop:forced ✔ · L7 family=Weyl ✔ · L8 two factors ✔ · L9 P7 placement ✔ (underclaim FIXED r1332) · L10 combinatorics ✔ · L11 compile ✔ (re-verified 0/0/50pp r1332) · L12 collector ✔ · L13 jargon ✔ · L14 map-card ⏸.
**Honest status:** the load-bearing chirality=γ⁵ (once propped by a `comm(g5,g5)` tautology, its r703 receipt not found) is derived from scratch + the 6D ruling-swap rendered; every other result verified or (where it invokes an established theorem) honestly traced. **Two spots I had FLAGGED-not-done and Daryl caught (r1332): the L9 intro underclaim (now fixed in P7 §265/§276 — ONE paper edit this sweep, owning the built discrete skeleton at weight, recompiled 0/0/50pp) and B2's a^{-3/2} form (now derived from the FLRW spin connection).** Residuals held honestly, NOT swept: (i) ~~the index~~ **RESOLVED r1334** — the count=3 is a complete argument (mode-counting L4+L6+even-crossing) and its protection is integer wall-count invariance (what Atiyah-Singer names); a lattice cross-check was attempted, returned 0 (a simple domain can't carry the branch structure), and was pulled rather than dressed as a pass; (ii) ~~B3's λ=j+1/2~~ **VERIFIED r1334** (`B3_sphere_spectrum.py` — the Dirac-on-S² eigenvalue derived from the edth algebra: |eigenvalue|=j+1/2 ∈ {1,2,3,...} for j=1/2,3/2,…, not merely cited); (iii) L14 map-card banners left as dated record (a numbering-reconciliation would be a separate meta pass). Do not read "worked" as "closed" — the remaining identifiable work is (ii) and the P16 `fig_history` figure, named not buried.
