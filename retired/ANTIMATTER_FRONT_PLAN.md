> **⌗ RETIRED r2380 under `RG-1` — ITS CONCLUSIONS ARE WITHDRAWN AND ITS ONE OPEN ITEM IS DEAD, BOTH BY ITS OWN
> HEADER.**
> *Its r989 audit correction withdraws the sheet-assignment conclusions as unsound — **both** the "A,B take the
> ±π/3 wings" reading and the "1+2 / B rides no sheet" reading, because both **collapse the DOUBLE ruling of the
> one-sheeted hyperboloid**: A and B are two genuinely distinct null rulings, orthogonal at the waist, neither
> the other under a sign.* *And its r1542 correction records that the one item the header left open — the map
> from $\{A,B\}$ to the two conjugate wings — **was KILLED at r1280**, the rulings and the wings being the
> linear and antilinear faces of one plate rather than two candidates for one assignment.*
>
> **⌗ WHAT IS DERIVED AND KEPT, stated so the retirement is not read as losing it:** *the photon → real
> ($\mathrm{Im}=0$) crossing.* ***And the collapse-the-double-ruling error it records is a standing guard***, in
> `gate_notes_bead_audit` and in `THE_WISDOM_LEDGER`'s partial-symmetry-flatten scrap: **hold the FULL symmetry
> while pulling at any piece, or you manufacture an asymmetry that is not there.**

---

> **AUDIT CORRECTION (r989).** The sheet-assignment conclusions in this working record are
> WITHDRAWN as unsound. Both the 'A,B take the +-pi/3 wings' reading AND the '1+2 / B rides no
> sheet / B is a space' reading collapse the DOUBLE ruling of the one-sheeted hyperboloid. A and B
> are two GENUINELY DISTINCT null rulings (orthogonal at the waist, verified); neither is the other
> under a sign, and neither is the tau~<->conj(tau~) conjugate of the single cosmic-time continuation.
> DERIVED and kept: photon -> real (Im 0) crossing.
> **⚑ AND THE ONE OPEN ITEM THIS HEADER NAMED IS DEAD (corrected r1542).** It read *"OPEN, not claimed: the
> map from the two distinct rulings {A,B} to the two conjugate wings."* **That item was KILLED at r1280** —
> `THE_OPEN_PROBLEMS_LEDGER` family 2, *resolved dead, migrated open→closed* — when P13's CPT factorisation
> `C = (Q↦−Q)_field ∘ (R∘K)_geometric` showed the rulings and the wings are **not two candidates for a
> bijection but the linear and antilinear faces of one object**. P7 now says so three times: *"not the
> sheet-to-ruling ($A,B\to$ wing) face-structure **the synthesis closes**."*
> **This is the THIRD document found carrying that kill unpropagated** — after `THE_PLAN`'s Lane 1 (struck
> r1442) and the entry-point register's seven rows (struck r1498). *One kill, three documents, ~260 revisions.*
> Read the reasoning below as an investigation, not a settlement.

---

# The antimatter / conjugation front — a bounded work plan (drafted r985)

Purpose: catch the formal proofs up to what the bead figures already show, decide honestly
what "antimatter" may be called and when, close the danglers, and do it **bounded** — without
overloading P7 (39p) or P3 (32p). Grounded in the r985 reconnaissance (citations inline).

---

## 0. The reframe the recon forced

The naive picture — "B is antimatter, we just haven't computed it" — is wrong in an important
way. The corpus has already worked this front and established a **proven wall**:

- **Antimatter = CPT = PT + C.**
- **PT is geometric and already (partly) yours.** B is the mass-reflected (R=γ⁵, r₀→−r₀)
  reassigned mirror cut — the "PT-mirror / conjugate dual" of A. Derivable, grounded
  (`COURSE_antimatter_telescope.md:18–31`; `matter_sector_paper.tex:212`).
- **C is provably NOT geometric.** `boundary_paper.tex:74–85`: C on a Dirac field is antilinear,
  every substrate isometry is linear ⇒ the metric is charge-conjugation blind ⇒ **no geometric
  CPT**. Corroborated `range_paper.tex:32`, `geometric_core_paper.tex:33`. This is a proven
  *negative*.
- **So "antimatter" is a field-level claim gated behind C**, which geometry does not supply.
  `matter_sector_paper.tex:212` names R=γ⁵ "the antimatter register" but holds it "a resonance,
  not an identity," and argues matter/antimatter is a P/R-parity register **distinct from the
  time reflection** — explicitly *not* a cosmogenesis (time) event.

**Honest derivable statement about B:** "the PT-mirror / conjugate (mass-reflected) dual of A."
Not "antimatter" — until C is supplied at field level.

---

## 0b. The debt this session's figure work created

- **The star `*` is overloaded.** The corpus's verified conjugation (`bead_conjugate.py:15`,
  `np.conj`) is **(a) complex conjugation τ̃→τ̄̃**, which keeps r **real** and swaps the ±πα/3
  wings (r → +r). The figure's "r(τ̃*) = −r(τ̃)" uses `*` to mean **(b) seam reflection τ̃→−τ̃**,
  which gives r → −r by oddness. Both maps are real and true, but they are **different
  operations**, and one symbol now denotes both — a latent inconsistency now sitting in the
  P7 caption (C) I edited this session.
- **The figure pre-commits to not claimed content.** Its colour code + panel D already assert
  the sheet assignment (photon = real cusp, A = +πα/3, B = −πα/3) and the "antimatter" label —
  exactly what `OPEN_PROBLEMS_MAP.md:410` holds open. The picture has outrun the proofs.

Reconciling this is WP-A and comes first.

---

## 1. Danglers sorted by status

**Bucket P — proven, needs only honest folding into text/figure**
- PT-mirror geometric identity of B (mass-reflected dual).
- Chiral zero-mode, chirality = R=γ⁵ (`matter_sector_paper.tex`, `prop:wall`).
- C-blindness / no geometric CPT (`boundary_paper.tex:74–85`) — the wall.
- Signed-r photon branch-point crossing (`photon_cross_test.py`).
- Complex-conjugate wing structure + 2πα/3 Wick period, r→e^{2πi/3} (`bead_conjugate.py`).
- r odd in τ̃ ⇒ r(−τ̃) = −r(τ̃) — trivially true but currently un-named.

**Bucket C — computable / provable, not yet done (the real targets)**
- **C1 · Disentangle the two involutions.** Name (a) conjugation τ̃→τ̄̃ (wing-swap, r real) and
  (b) seam reflection τ̃→−τ̃ (r→−r) as separate lemmas; fix the figure/caption to say which is
  which. Cheap, removes the overloaded star. *(Home: P7 caption + a two-line lemma; figure.)*
- **⌫ C2 · The order-three bridge theorem — CLOSED r1723 as mis-targeted and superseded.** *Drafted r985. Its
  target — "prove the isomorphism" between the sky-angle $\mathbb{Z}/3$ and the bead's imaginary-time
  $\mathbb{Z}/3$ — **is the identification `lem:twoturnings` forbids** (scope-corrected r1430: no affine change
  of variable identifies the two threefold symmetries). **And the relation it was reaching for was found at
  r1434 and is stronger than an isomorphism: the two cubics are the $E{=}1$ and $E{=}0$ ends of ONE family of
  turning points**, with $S_3$ carried as **monodromy of the cover** at $E<1$ and as **symmetry of the figure**
  at $E=1$ — *neither end lacks it; the deformation exchanges how it is carried*. **What survives as open is
  narrower and better stated elsewhere:** whether $E=1$'s monodromy drop and the flat leaf $k=0$ coincide for a
  reason — held and routed in `THE_PLAN` under SA-7 (r1688).* **Original text kept below as the record.**
- **C2 (original, r985) · The order-three bridge theorem.** The groupoid's Z/3 lives on the **sky angle** w
  (sin 3w; `groupoid_paper.tex prop:tau`); the bead's Z/3 lives on **imaginary cosmic time**
  (sinh^{2/3}, e^{2πi/3}; `bead_conjugate.py`). The corpus *asserts* they are "the same
  order-three" but **exhibits no map**. Prove the isomorphism via the shared horizon cubic /
  Nariai branch point, handling the **regime-dependent (non-uniform) S₃** realisation
  (`prop:deck` — only Z/2 survives over-critically; a real hazard). *(Home: groupoid paper P5,
  22p, has room.)*
- **C3 · Sheet↔bundle assignment.** If C2 lands, does it **force** the labelling
  (photon = real, A/B = ±πα/3), or is a separate canonical labelling of the three cubic roots
  by the three congruences still needed? State precisely what is forced vs chosen.
- **C4 · The "double-speed photon" rate.** Compute the proper-rate relation of the at-rest
  congruence as it is reassigned to null; **derive the factor or formally retract** "double
  speed." Also fix the dangling pointer: `thm:bead` (`CR_framework.tex:759`) sends this to
  §frontiers, but §frontiers (`:952–962`) doesn't contain it. *(Home: P7 §frontiers + receipt.)*
- **C5 · The field-level C / antimatter register.** Whether the matter sector can supply C so
  "antimatter" is *earned*. This is the A4 matter-sector frontier, already partly planned
  (`THE_PLAN.md` Lane 3 A4; `PROGRAMME_UNFINISHEDNESS_CATALOGUE.md §A4`). **Larger — likely out
  of bounds for this push.** *(Home: matter_sector_paper P15/16, 8p, most room.)*

**Bucket N — named-only, keep not claimed**
- B "is antimatter" (needs C5). Matter/antimatter selection (external, R-symmetric,
  `PHASE3_baryogenesis_analogue.md:11`). Baryogenesis analogue.

---

## 2. The naming gate for "antimatter"

Rule: the corpus writes **"antimatter"** for B only once **C** is supplied at field level (C5).
Until then, geometric figures/text say **"the conjugate / PT-mirror (mass-reflected) dual
bundle,"** with at most a flagged remark that its field-level register is R=γ⁵, held as
resonance. This keeps the figure legends and the paper prose in the same (honest) register and
stops the picture outrunning the proofs.

---

## 3. Work packages, homes, load budgets, stop-lines

| WP | Content | Home | Load | Stop-line |
|----|---------|------|------|-----------|
| **A** (do first) | C1 disentangle involutions; walk P7 caption/figure to conjugate/PT-mirror register (or add flag — see Decision 1); fix thm:bead→§frontiers pointer; add double-speed item to §frontiers; bibkey hygiene (JanzenCRframework/JanzenFramework) | P7 + figure | ~0 new pages | no new physics claims |
| **B** | C2 order-three bridge theorem (+C3 what's forced); receipt script | groupoid P5 | +1–2p | if non-uniform S₃ blocks a clean bridge, **log precisely and STOP** — do not force it |
| **C** | C4 compute the rate; derive or retract "double-speed"; pointer fix | P7 §frontiers + receipt | ~½p | one computation; if inconclusive, retract phrase, log open |
| **D** (optional, gated on B) | the missing figure: genuinely complex r + full 2πα/3 period (the C×C slice no panel shows); promote sheet assignment to asserted **only if** C3 earns it, else keep explicitly conjectural | P5 or standalone (**not** P7) | +1 fig | do not add to P7's 39p |
| **E** (out of bounds now) | C5 field-level C / earn "antimatter" | matter P15/16 | later | only after A–D settle |

---

## 4. Sequencing

WP-A → (WP-B + C3) ∥ WP-C → WP-D gated on B → (later) WP-E.
WP-A first: it is honesty debt sitting in a paper right now.

## 5. Scope guard — what we are NOT doing

- Not committing "antimatter" into paper prose until C5 (Decision 1 may override for the figure).
- Not adding figures/derivations to P7 (39p) or P3 (32p) beyond WP-A's small honesty fixes.
- Not forcing the sheet assignment if the bridge (C2) doesn't close.
- Not opening the matter-sector C question (C5/WP-E) in this push.

## 6. Decisions needed before any edits

1. **Figure/caption register** — walk back to "conjugate/PT-mirror," keep "antimatter" with an
   explicit field-level flag, or commit to *earning* it (pull WP-E in).
2. **Scope of this push** — minimal (WP-A), medium (A+B+C), or large (+D and/or E).
3. (Recommendation, not a blocker) new formal content lands in P5 (order-three) and, if pulled
   in, P15/16 (matter sector) — never P7/P3.

---

## Status log

### Decisions locked (r985)
1. **Register: walk back to "conjugate/PT-mirror" now.** Strip the premature "antimatter" from
   figure + text; let WP-E (field-level C) be what re-earns the word later, if it closes.
2. **Scope: Large (A+B+C plus D/E).** Full rigorous program, executed in bounded, checkpointed
   increments — not all at once.

### WP-A — DONE (r985)
- Figure `synthesis_figure.py`: docstring RED = "the conjugate dual (B; PT-mirror/mass-reflected)";
  panel A legend "antimatter"→"conjugate dual"; lap label →"(=matter+conjugate dual)";
  panel C red curve relabelled `r(-τ̃) = -r(τ̃)` (removes the overloaded `*`).
- P7 caption (C): "conjugate antimatter reading r(τ̃*)=−r(τ̃)" → "conjugate (mass-reflected)
  dual reading r(−τ̃)=−r(τ̃)".
- P7 caption (D): de-asserted — wings now "drawn blue/red for A/B by the natural reading; the
  sheet-to-bundle assignment is a genuine open question (§frontiers)", matching thm:bead.
- P7 §frontiers: added the missing item "The bead's sheet structure and the reassigned-congruence
  rate" — fixes the dangling thm:bead→§frontiers pointer; folds in both open questions
  (sheet-assignment; double-speed rate) at not claimed.
- Bibkey hygiene: `JanzenFramework`→`JanzenCRframework` in the 2 outlier papers
  (geometric_core, matter_sector); now 16/16 consistent. All three papers recompile clean.

### WP-B — WORKED (r986). **⚠ SCOPE-CORRECTED r1430: what does not close is an identification by an AFFINE
change of variable at fixed cubic. The two cubics are the E=1 and E=0 ends of one turning-point family
r³+(E²−1)α²r+2Mα², separated by a discriminant crossing; the affine test is blind to that deformation.
Only the A₂ identification of root sets remains unclaimed.** Full write-up: `retired/WP_B_ORDER3_BRIDGE.md`
(carries the correction); receipts `computations/order3_bridge.py` (scope warning prepended) and
`turnaround_excursion_work/two_realisations.py`.
The two order-three structures are the Galois/cube-root ℤ/3's of two **different, affinely
inequivalent** cubics — horizon `f=0` (`r³−r+2M`, three colinear real roots) vs comoving `1−f=0`
(`r³+2M`, an equilateral triangle) — over different bases, branched at different loci (Nariai vs
seam), degenerating oppositely at Nariai. "Same order-three" holds only trivially (S₃ has a unique
ℤ/3); identifying the two ROOT SETS is the not claimed A₂ resemblance, and even granted it would
not force the congruence sheet-assignment. **The obstruction is to an AFFINE identification at fixed
cubic.** The two cubics are nonetheless the `E=1` and `E=0` ends of one turning-point family
`r³+(E²−1)α²r+2Mα²` (the separating term being `E²−1 = −k`), separated by a discriminant crossing —
so this is not a stop-line on the question, only on identifying the root sets by change of variable.
Productive by-products: (i) the clean lemma `(dr/dτ̃)² = 1−f`; (ii) C3 must be reached by the
**ruling-continuation** route, not the groupoid; (iii) the comoving cubic's equilateral-triangle
roots ARE the missing complex-r figure for WP-D; (iv) ~~sharpen the P7 frontiers item from "open" to "the natural bridge does not close"~~ — **WITHDRAWN r1430: that would have closed an open item on an over-broad reading of an affine-only test. Never applied to P7, and must not be.**

### WP-A follow-through (r986): the two small P7 edits landed
Added Lemma `lem:twoturnings` ((dr/dτ̃)²=1−f; the two turning cubics; the two order-threes agree
only as abstract ℤ/3's); sharpened thm:bead First-fact and the frontiers item to cite it.
P7 recompiles clean, refs resolved.

### C3 — sheet-assignment by ruling-continuation: PARTIAL CLOSE + a mislabel found (r986). Note: `WP_C3_SHEET_ASSIGNMENT.md`; receipt `computations/sheet_assignment.py`.
Derived: **photon rides the real (Im τ̃=0) crossing sheet**; the **±πα/3 wings are the `τ̃↔τ̄̃`
conjugate pair of the ONE matter collapse leg** (not two distinct bundles). So the sheets are
**1 + 2** (photon | matter's conjugate pair), NOT a 3-congruence bijection — the figure's panel-D
"blue A / red B on the two wings" is a **mislabel** to fix. Reading the −πα/3 wing as
"antimatter/conjugate-dual" would require identifying op-(a) `τ̃↦τ̄̃` with op-(b) `τ̃↦−τ̃` — the same
overloaded-`*` from WP-A, unproven. Next: source-grounding pass against `slicing_operator.tex`
A/B/photon definitions before any corpus assertion; then panel-D relabel (WP-D) and the frontiers
sharpening.

### C3 source-grounding (r986): CONFIRMED. `slicing_operator.tex:262–269`.
A = future generator → reassigned matter worldline (bead, +πα/3 lap); **B = past generator = "the
synchronous space *is* the second ruling"**, a spatial slicing that rides **no** time-sheet; photon
= at-rest closed-cosh geodesics → real crossing. Grounded sheet table: real=photon, +πα/3=matter,
−πα/3=matter's τ̃↦τ̄̃ conjugate mirror; **B rides no sheet**. Panel-D "blue A/red B on the wings" is
a confirmed mislabel (B is a space; −πα/3 is matter's own conjugate). Panel B (red=B=const-τ) is
fine. Two fixes now grounded and ready, **awaiting go**: (1) panel-D relabel; (2) P7 frontiers
sharpening to the derived 1+2 structure, leaving only the op-a/op-b (antimatter) identification open.

### WP-E — the naming, SETTLED (r986). Note: `WP_E_ANTIMATTER_NAMING.md`.
Does B earn "antimatter"? The matter sector already answers **no**, and gives the reason: the
antimatter register is **R = γ⁵**, the *mass* reflection `r₀↦−r₀` (spacelike, horn-preserving); the
bead's conjugate branch is the *areal* reflection `r↦−r` = **P**, the cosmogenesis conjugate. R and
T/P are "a resonance, not an identity"; "matter/antimatter cannot be a cosmogenesis event"
(`matter_sector_paper.tex:212`). So B = **conjugate dual**, not antimatter — the WP-A walk-back was
right, and no field-level C build is needed to settle it (the C-blindness wall says the same from
the other side). Landed in P7 (frontiers item + thm:bead Third-fact), receipt `sheet_assignment.py`.

### CORRECTION (r987) — two of my own edits were wrong; fixed.
1. **The "rate" frontier was spurious.** I inflated a prior instance's unmotivated "double-speed
   photon" musing into a stated P7 frontier without working it. Worked from the reassignment source
   (§660–676): the reassignment is a causal-character *swap* (A null→timelike; at-rest timelike→null
   photon), already fully specified; a null congruence runs at the null rate by definition, so
   "twice the null rate" is a misdescription, not an open question. **Removed** from thm:bead
   Third-fact and the frontiers item.
2. **The antimatter naming is NOT settled — I took the corpus as gospel.** WP-E "closed" it by
   deferring to the matter sector's `R=γ⁵` "antimatter register" — but that is stated without being claimed in
   the corpus itself ("a resonance, not an identity"), so it settles nothing (faces r693 grounding
   in the assertion, r694 treating it as unoverturnable). **Reopened** as the genuine drill-site:
   geometrically B is the mass-reflected (r→−r) dual — the honest *description*, "conjugate dual" —
   but whether that is *antimatter* is not worked out on either side, stated without being claimed.

### FRONT STATUS (corrected r987).
A (honesty) ✓ · B (order-three: a resemblance, not a theorem) ✓ · C3 (sheet assignment = causal
characters on the foliation; photon real, both null bundles on the wings) ✓. The **antimatter
naming is the one genuine open drill-site** — not claimed, none of it worked out on either side.
The "rate" item was spurious and is gone. P7 compiles clean at 39pp.

### Superseded plan note (kept for record): WP-B — the order-three bridge (the first real theorem)
Concrete first step (a receipt computation, analogue of bead_conjugate.py): test whether a single
Wick map identifies the groupoid's sky-angle Z/3 (roots of the horizon cubic r³−r+2M=0 via
r₀=(2/√3)sin w, w→w+2π/3) with the bead's cube-root Z/3 (r→e^{2πi/3}r under τ̃→τ̃+2πiα/3), i.e.
whether the three trig-cubic roots and the three sinh^{2/3} sheets are the same Z/3-orbit under the
shared Nariai branch point. If it closes numerically → draft the bridge theorem in P5 and state
what C3 (sheet↔bundle) it forces. If the non-uniform S₃ (over-critical Z/2-only) blocks it → log
the obstruction precisely and stop. Report honestly either way.
