# `r7580` — THE IDENTIFICATION DOES NOT FORCE THE STACKING-RATE DISTANCE, AND LIGHT'S REAL INTEGRATED PATH IS A THIRD OBJECT THE COMB EXCLUDES

Registration: `PREDICTION.md`, sha1 `02da790f6ebe398eb57dbb5892b9942a4e96b879`, committed at
`fb00db0c` before `lightpath.py` was run. Nine arms were registered; **eight HIT and one MISS, and
the MISS is mine** — the registered wording of Ⓗ overclaimed and is withdrawn, with the discarded
reading kept beside its correction below.

## What was asked

`r7577`: `P16`'s rule puts *a comoving separation read across leaves* on the stacking rate and *a
process running in the content* on the leaf's, and **light's path from last scattering is the case
that rule has to be shown to decide**. Daryl's direction: *the projection may need light's real
integrated path distance*, with the fit's preference for the leaf-rate distance as the pointer.

## The answer, in one line

**The rule does not decide it, and the identification that stands in for the rule does not force the
stacking rate either. Neither half of the ground `P15` §refit-bound gives selects a rate; the clause
that does the selecting asserts it.** And light's real integrated path, computed here for the first
time, is a *third* object at `8787` Mpc against the implementation's `14011` Mpc, which the comb
excludes outright — so the projection does not need it, and Daryl's direction finds a real **gap**
rather than the mechanism.

## The chart, calibrated first (Ⓐ Ⓑ Ⓒ, all HIT)

| what | value |
|---|---|
| `min` over `r` of `(∂_χ r)²` | `1.0000000000000000`, at `r = 3009.892488` Mpc |
| `α/√3`, the merged Nariai radius | `3009.892488` Mpc — the minimiser, to `0` |
| the redshift of that single tangency | `z = 0.6783` |
| worst `\|c(∂_χ r)/r ÷ H_stack − 1\|` over `z = 0, 1, 10, 1090, 3×10⁷` | `2.3×10⁻¹⁵` |
| `∫c dz/H_stack` versus `r₀∫dτ̃/r` | `14011.456` Mpc both, differing by `7.8×10⁻¹⁵` |

Two of these are worth stating plainly because they are exact and were not in the sector before.
**`(∂_χ r)² ≥ 1` on the whole real branch with a single tangency, and the tangency is exactly the
Nariai radius** — the Nariai condition is precisely what makes the minimum equal `1` rather than
some other number. And **the rate the implementation's distance is built on is the layer-time rate**:
`H_stack = c(∂_χ r)/r` identically, so `∫c dz/H_stack` *is* `r₀∫dτ̃/r`, the integral taken against
the cosmic time `τ̃` that labels the layers.

## Light's real integrated path (Ⓓ HIT, Ⓔ HIT)

Derived in the registration before the run, from `P15` eq:proper-frame:

* a radial null ray has `dτ = (∂_χ r)dχ`, hence `dτ̃ = (1 + ∂_χ r)dχ`;
* the proper length the photon traverses, read in the local fundamental observer's own frame, is
  `√(g_χχ)dχ = (∂_χ r)dχ`, which the null condition makes **equal to `dτ`** — the observer's own
  proper time, not the layer time;
* so the light-travel comoving accumulation is `r₀dτ/r`, and on the ray
  `dτ = [(∂_χ r)/(1 + ∂_χ r)]dτ̃`.

**The two candidate "light-travel distances" therefore differ by exactly the non-synchrony factor,
epoch by epoch.** Measured:

| `z` | `∂_χ r` | weight `(∂_χ r)/(1 + ∂_χ r)` |
|---|---|---|
| `0` | `1.1559` | `0.536158` |
| `0.6740` (the tangency) | `1.0000` | `0.500001` |
| `3` | `1.2836` | `0.562092` |
| `10` | `2.0922` | `0.676605` |
| `100` | `6.3340` | `0.863650` |
| `1089.9` | `20.8167` | `0.954164` |

The weight is nowhere near `1`; it bottoms at exactly `1/2` at the tangency, which is the same
Nariai fact read on the light cone.

| candidate | `D` (Mpc) | `ℓ_A = πD/r_s` | against the sky's `298.4` |
|---|---|---|---|
| the implementation, stacking rate | `14011.46` | `302.87` | `+1.50 %` |
| the leaf-rate distance the fit prefers | `13941.63` | `301.36` | `+0.99 %` |
| light's real integrated path | `8787.24` | `189.94` | `−36.35 %` |

`r_s` on the leaf rate is `145.337` Mpc; the calibration against the prior receipt's banked
`πD_C/r_s ≈ 301.6` holds to `0.42 %`, which is the pricing arm Ⓕ.

**Registered prediction Ⓓ: shorter, ratio in `[0.60, 0.75]`. Measured `0.627147`. HIT.**
**Registered prediction Ⓔ: the leaf shift is under two per cent and the path gap is an order of
magnitude larger. Measured `−0.4984 %` against `36.971 %`. HIT.**

So the empirical pointer and the chart's gap point the **same way** — both distances are shorter than
the implementation's — and they are **not the same object**, by a factor of seventy-four in size.
The leaf-rate distance moves `ℓ_A` half a per cent toward the sky; light's real path moves it
thirty-six per cent away and is excluded by the comb without any likelihood being run.

## Why the identification does not force the stacking rate (Ⓖ HIT, Ⓘ HIT, Ⓗ′ HIT)

The ground, quoted whole from `P15` §refit-bound and located verbatim by the script:

> *The ground is the observer's own readout*: the constant-proper-time slice is exactly flat, so the
> comoving angular-diameter distance **is** the light-travel distance `D_C`, and on that slice the
> expansion law is exactly flat-ΛCDM's with radiation absent from it — a statement about the slice's
> induced three-metric, with no rate in it at all, which is why it can supply an identity a rule
> about rates cannot.

It has two halves and they were tested apart.

**Ⓖ — the flatness half is rate-neutral.** `D_M` follows from the comoving radial distance `χ` by the
curvature branch, and at `Ω_k = 0` that branch is `D_M = χ` with no `H` in it. Substituting all three
candidate `χ` — stacking, leaf, and light's real path — the identity holds for every one of them to
`0`, while at `Ω_k = ±0.01` it fails by `1.72 %` and `1.70 %`. **So the identity's content is
flatness, and flatness is satisfied by all three rates alike. It fixes which length `D_M` is; no
rate follows from it.**

**Ⓘ — and the clause's own words are literally true, which is why it cannot deliver a rate.** The
registered control was that the clause would win if the constant-`τ` stack carried an expansion law
of its own. It does not: reparameterising each slice by `r` returns `dr² + r²dΩ²` with `τ` nowhere in
it, checked rather than asserted at three slices and four radii — worst `|g_rr − 1| = 3.1×10⁻¹⁰`,
worst mismatch at matched `r` `1.9×10⁻¹³`. **Every constant-`τ` slice is isometric to one fixed flat
`ℝ³`.** What moves is the congruence's place in it: an observer at fixed `χ` sits at `r(τ+χ)` and
`dr/dτ|_χ = ∂_χ r = 1.1559 ≠ 0`. So the stack carries no expansion of its own metric, `P15`'s
parenthetical *"with no rate in it at all"* is exact — **and a clause with no rate in it cannot
supply one.**

**Ⓗ — my registered wording, withdrawn.** I registered that `D_M` sits in the rule's first slot and
`D_C` in its second, so that the identification crosses the rule's own partition. **That does not
survive the corpus's own applications and is scored MISS.** The discarded reading is kept here: a
light-travel distance is accumulated along a history through the content the photon crosses, which
is the criterion by which the second slot takes `r_s` and `r_D`. What refutes it: `P15` puts **the
optical depth** — `∫n_e σ_T dl`, every factor of it content — **on the stacking rate**, grounded on
its being *"a photon-path observable of the same kind as the redshift and the distances"*. So
accumulation-through-content does not by itself place a quantity in the second slot.

**Ⓗ′ — the corrected finding, and it is stronger.** The criterion that actually separates the
corpus's two accumulations is *photon-path observable*, and **that criterion is not in the rule.**
Counted: `photon-path` occurs **`0`** times in `P16`, where the rule is stated and derived, and
**`3`** times in `P15`, where it is applied. The rule as stated holds two slots; the corpus's own
applications need three; the third criterion appears only where the rule is used and nowhere where
it is derived. And light's path from last scattering is an accumulation through the content **and** a
photon-path observable at once — exactly the pair of properties the two worked assignments separate
on — with no clause in the rule ranking them. **This is `r7422`'s shape again: a resolver with two
states meeting a case that is a third.**

## What this means for the live clause

Neither half of the ground selects. The flatness half is rate-neutral (Ⓖ); the three-metric half has
no rate in it, as the paper itself says and as the control confirms (Ⓘ); and the rate rule cannot be
appealed to in their place, because its two slots do not cover the case (Ⓗ′). **What is left doing
the selecting is the one remaining clause — `on that slice the expansion law is exactly flat-ΛCDM's
with radiation absent from it` — which asserts which rate the distance is built on rather than
deriving it.** By the guard, the hedge is load-bearing and belongs in the stem.

**That is not a refutation of the assignment.** The assignment may well be right; three independent
routes were claimed for it at `r7099` and the two that survive are the two tested here. What is
established is that **the identification does not *force* it**, so the sky's preference for the
leaf-rate distance is not up against a theorem — it is up against an assertion of the same logical
kind, and the comparison between them is open rather than settled.

## What is owed, and the standing rule `r7577` added

`P15` §refit-bound carries the sentence *"So the support is one established theorem rather than a
count"*. On this reading the support is one **assertion** and not one theorem, and that sentence
owes a correction. It is a sentence about what is open — it states that the sector's one ground is
settled — so **`r7577`'s new standing rule applies: `check_open_item_coherence` re-reads the papers
and will fail on an edit here until `PO-87`'s row in `r7577_69`'s `items_keyed.tsv` is read again.**
This revision does **not** edit the paper. The correction is routed, with its text, in
`FOR_66_FROM_60.md`, so that `69` can land the sentence and the keyed row together.

## Scope

No instrument was added: no gate, ledger, census or receipt-about-receipts, per `r7471` and `r7577`.
No parameter is pinned, so no `COMPUTES:` scope header is owed. No new quote-pin key is minted — the
five sentences the script locates are located by containment, not pinned. The background map is read
out of the prior `P15` receipt by `ast` rather than reimplemented, per `r7445`.
