> **⌖ RETIRED r1548.** A work package of the antimatter/conjugation front whose question is closed — see the correction above. Kept as record; **do not work from it.**


> **⚑ THE ITEM THIS DOCUMENT HOLDS OPEN IS DEAD (corrected r1548).** The sheet-to-ruling / antimatter-naming
> question was **KILLED at r1280** — `THE_OPEN_PROBLEMS_LEDGER` family 2, *resolved dead, migrated open→closed*
> — when P13's CPT factorisation `C = (Q↦−Q)_field ∘ (R∘K)_geometric` showed the rulings and the wings are
> **the linear and antilinear faces of one object**, not two candidates for a bijection. **And the naming is
> settled in the corpus:** P7 carries `thm:antimatter-progenitor` — *"The antimatter progenitor: our universe
> from an antimatter black hole"* — with the branch point exchanging the species.
> **Fourth and fifth documents found carrying this kill unpropagated**, after `THE_PLAN` (r1442), the
> entry-point register (r1498) and `ANTIMATTER_FRONT_PLAN` (r1542). **One closure, five documents.**


> **AUDIT CORRECTION (r989).** The sheet-assignment conclusions in this working record are
> WITHDRAWN as unsound. Both the 'A,B take the +-pi/3 wings' reading AND the '1+2 / B rides no
> sheet / B is a space' reading collapse the DOUBLE ruling of the one-sheeted hyperboloid. A and B
> are two GENUINELY DISTINCT null rulings (orthogonal at the waist, verified); neither is the other
> under a sign, and neither is the tau~<->conj(tau~) conjugate of the single cosmic-time continuation.
> DERIVED and kept: photon -> real (Im 0) crossing. OPEN, do-not-assert: the map from the two distinct
> rulings {A,B} to the two conjugate wings. See gate_notes_bead_audit.md and P7 thm:bead third fact /
> frontiers item, both de-asserted at r989. Read the reasoning below as an investigation, not a settlement.

---

# C3 — sheet-assignment by ruling-continuation: a partial close, and a mislabel found (r986)

Receipt: `computations/sheet_assignment.py`. Grounded in the verified ODEs
(`photon_cross_test.py`, thm:bead First fact / `bead_conjugate.py`). Status: the two computations
below are **solid**; the interpretation is **derived but to be confirmed against the A/B/photon
definitions in `slicing_operator.tex` before any corpus assertion**.

## What the computation establishes

Setup: at a given `r < 0` on the collapse side there are **three** values of cosmic time `τ̃(r)`
(the three cube-root sheets), at `Im τ̃ ∈ {0, +πα/3, −πα/3}`. The question is which physical
congruence takes which.

1. **Photon → the real sheet (Im τ̃ = 0). Derived.** The at-rest congruence, reassigned to the
   null geodesic `dχ/dτ̃ = 1/(1+r′)`, integrates in **real** τ̃ and crosses `r=0` staying on the
   real axis (this is `photon_cross_test.py`). So the photon rides the `Im τ̃ = 0` branch.

2. **The two ±πα/3 wings are the conjugate pair of the *matter* collapse leg. Derived.** The E=1
   comoving (matter) reading `τ̃(r) = ∫₀^r dr′/√(2M/r′+r′²)` goes complex for `−(2M)^{1/3} < r < 0`
   and reaches `Im τ̃ = ±πα/3` at the turnaround (numerically ±π/3 = ±1.0472 at Nariai, confirmed).
   The two signs are the **same** collapse leg read through the two branches of the square root —
   i.e. the `τ̃ ↦ τ̄̃` conjugate pair (thm:bead First fact). They are one congruence's two readings,
   at the **same** `r<0`.

## The consequence — a figure mislabel, and the antimatter link

The three sheets decompose **1 + 2**, not 1 + 1 + 1:

- `{Im τ̃ = 0}` — the **photon** (real crossing);
- `{Im τ̃ = ±πα/3}` — the **matter** congruence's collapse leg, as a `τ̃↔τ̄̃` **conjugate pair**.

So the plate's panel D, which draws **"blue A at +πα/3 and red B at −πα/3"** — two *distinct*
bundles on the two wings — is **not supported by the continuation**. The two wings are not A vs B;
they are the two conjugate readings of the *one* matter leg. The synchronous ruling **B**
(const-τ, a spatial slice) is not a worldline crossing the seam in time and does **not** separately
ride a cube-root time-sheet.

Why this matters for the antimatter front: reading the `−πα/3` wing as the **conjugate-dual /
"antimatter"** leg (the tempting move) would require identifying the wing-swap `τ̃↦τ̄̃`
(**operation a**, keeps `r<0` fixed, relates the two wings) with the matter↔dual reflection
`τ̃↦−τ̃ ⇒ r↦−r` (**operation b**, flips `r<0 ↔ r>0`). These are the **two involutions disentangled
in WP-A** — the overloaded `*`. Operation (a) relates the two wings *at the same r<0*; operation
(b) relates collapse (`r<0`) to expansion (`r>0`). They are different maps, so the `−πα/3` wing is
matter's own conjugate reading, **not** the antimatter leg — unless (a) and (b) are identified,
which is exactly the unproven step. The C3 result therefore **reconnects to WP-A**: the same
`*`-overloading that we cleaned in the figure legends is the load-bearing ambiguity here too.

## Honest status

- **Closed:** photon rides the real crossing; the ±πα/3 wings are the matter leg's `τ̃↔τ̄̃`
  conjugate pair. The "natural reading" (A on +, B on −) is **wrong as stated**.
- **Corrected target:** the sheet structure is **1 + 2** (photon | matter's conjugate pair), not a
  three-congruence bijection. Panel D should be relabelled accordingly (a WP-D item).
- **Still open / to ground at source:** whether *any* physical reading assigns a distinct congruence
  to the `−πα/3` wing (this is the op-a ≡ op-b question, unproven); and the precise geometric role
  of B in this frame. To be checked against `slicing_operator.tex:262–269` before corpus assertion.

## Downstream actions (proposed, not yet done)
- **Figure (WP-D):** relabel panel D's wings from "A / B" to "the matter leg's conjugate pair
  (`τ̃↔τ̄̃`)", photon on the real sheet. This is a second, deeper walk-back than WP-A's naming fix.
- **P7 caption/frontiers:** once source-confirmed, sharpen the sheet-assignment item from "which
  congruence rides which sheet (open)" to the derived 1+2 structure, with the residual op-a/op-b
  freedom named. Receipt `sheet_assignment.py`.
- **Source-grounding pass:** read `slicing_operator.tex` A/B/photon definitions and confirm the
  continuation reading before any assertion.

## Source-grounding (r986) — CONFIRMED, and sharpened

Read `slicing_operator.tex:262–269` (§"The synchronous space is the second ruling"):

- **A** = the *future* null generator, `X(τ)=e^{τ/α}A+e^{−τ/α}B` asymptoting to A as τ→+∞; A is
  per-worldline (the Null-Boundary map `p↦H⁺(p)`). Reassigned to timelike, A is the fundamental
  **matter** worldline — the bead. Its collapse-leg cosmic-time reading reaches Im τ̃ = +πα/3 (lap).
- **B** = the *past* generator, common to the whole congruence; **"the synchronous space *is* the
  second ruling"** — the level sets of η(X,B)=e^{τ/α}, horospheres normal to B. **B is a spatial
  slicing, not a worldline that crosses the seam in cosmic time.** It therefore does **not** ride a
  cube-root time-sheet. This is the decisive source fact.
- **Photon** = the at-rest *closed-cosh* comoving geodesics (synchronized to the timelike vertical,
  not to a ruling), reassigned to null; crosses the seam on the real axis (photon_cross_test).

So the grounded picture, now firm:

| sheet | rider | status |
|-------|-------|--------|
| `Im τ̃ = 0` (real crossing) | the **photon** (at-rest → null) | derived + source-consistent |
| `Im τ̃ = +πα/3` | the **matter** (A) collapse leg | derived (thm:bead) + source-consistent |
| `Im τ̃ = −πα/3` | the **τ̃↦τ̄̃ conjugate mirror** of that same matter leg | derived; **not** a separate congruence, **not** B |

**B rides no sheet** (it is the synchronous space). Hence the plate's panel D — "blue A at +πα/3,
red B at −πα/3" — is a **confirmed mislabel on two counts**: (i) B is a space and does not cross in
time; (ii) the −πα/3 wing is matter's own conjugate reading, not B. Reading −πα/3 as the
conjugate-dual/"antimatter" leg still requires op-(a) `τ̃↦τ̄̃` ≡ op-(b) `τ̃↦−τ̃`, which is unproven;
and B — the genuine dual/second ruling — is the synchronous space, a *different* object from the
−πα/3 wing, so the wing is not B/dual either way.

Note panel B is unaffected: there red = B = the const-τ synchronous space is correct (B genuinely
is that spatial slicing). The mislabel is confined to panel D's off-real sheets.

### Grounded, ready to propose (awaiting go)
1. **Panel D relabel:** real = photon (black); +πα/3 = matter (A, blue); −πα/3 = matter's τ̃↦τ̄̃
   conjugate reading (a paired blue tone or explicit "conjugate reading"), **not** red B.
2. **P7 frontiers sharpening:** replace "which congruence rides which sheet (open)" with the derived
   1+2 structure — photon real, matter's conjugate pair on ±πα/3, B a synchronous space that rides
   no time-sheet — leaving only the op-(a)/op-(b) identification (the antimatter register) open.
   Receipt `sheet_assignment.py`.
