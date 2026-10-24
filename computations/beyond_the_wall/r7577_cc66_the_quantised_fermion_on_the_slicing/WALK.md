---
kind: WALK
row: PO-95
revision: r7577+cc66.2
scores: PREDICTION.md
---

# `PO-95` — the walk, scored against `PREDICTION.md` and not against a reconstruction of it

`spectrum.py` → `spectrum_out.txt`, 40 checks, 0 failures, five controls. Every number below is in that
output. **Nothing from `receipts/L221_the_bridge` is reported as mine**, and nothing from the three lines
the source question turned up at the write-up (`L-246`, `L-264`/`L-275`, `L-265`) is either.

## ⚠ The source question, run a second time, found three lines the pre-registration had missed

The pre-registration's table covered `L221_the_bridge` and stated the residue narrowly on that basis. It
was not enough. Running the same question against the **receipts** rather than the papers — `L-276`'s own
withdrawal note states the rule: *"ask the receipts, not only the papers — what the corpus publishes and
what it has already decided are different sets"* — turned up:

| line | what it already establishes | status |
|---|---|---|
| `L-246` / `W2` (`PO-22`) | the wall zero-mode **recomputed** on `B60`'s operator; the near-throat exponent is `exp(-i√2λ√r/√M)`, **neither `r^{±λ}` nor `r^{±iλ}`** | worked `PO-22`, r3110 |
| `L-264` / `K1` | the limit-point/limit-circle question **asked at the branch point**, and answered **limit-point** from `ψ~r^{∓λ}` with the `|λ|<3/4` window | ✔✔ |
| `L-265` / `L1` | that verdict **inverts** on the corrected operator: **limit-circle, deficiency (1,1)** — and names the open item: ***"which self-adjoint extension the geometry selects"*** | ✔ |
| `L-275` / `U1` | the corpus asks its self-adjointness question at `a=0` and not at `r=0`; records the two verdicts as **opposite** | ✔✔ |
| `L-276` / `V1` | reconciled to limit-circle at r3319 — **and was WITHDRAWN at r3339** back to limit-point | withdrawn |

⇒ **So ⒝ was not mine to predict: it was already computed, twice, with opposite answers.** What that costs
the pre-registration is stated plainly in the scoring below: ⒝ scores as *not mine*, not as a hit.

## The scoring

| # | prediction | band | measured | verdict |
|---|---|---|---|---|
| ⒜ | pure point in the leaf measure, no continuum branch | 0 continuum branches, band 0–1 | **0**; spacing `1.73719` against `π/L = 1.77830`, min gap `1.25387`, spacing cv `0.060`, on an instrument that reproduces `B26`'s barrier (`1.96307` at `r=0.30378` vs `0.30385`) | **HIT** |
| ⒝ | limit-circle at 3 of 3 walls, a family of extensions admitted | 3 of 3, band 0–3 | limit-circle on branch A at every wall (`m` is `ℓ^{-2/3}`, `L¹`, `∫m dℓ = 6^{1/3}`) — **but this is `L-265`'s result and not mine**, and on branch B the same walls are limit-point | **NOT MINE** |
| ⒞ | the monodromy `ω^{-λ}` selects the extension | — | **it does not, and it cannot** | **FAIL, reported and not rounded** |
| ⒟ | completeness closes by compact resolvent, not Kato–Rellich — two measures, two theorems | — | holds: `L²(dr_*) ⊂ L²(dℓ)` strictly, `B27` closes the tortoise half by Kato–Rellich, the leaf half closes by compact resolvent on a finite closed curve | **HIT** |
| ⒠ | the matching is closed-form near `r=0`, `∝exp(ic√|r|)` | — | `exp(-i√2λ√r/√M)` on branch A — **which is `W2`'s own exponent**, found at the write-up, so the prediction is right and the credit is not mine; `r^{-λ}` on branch B | **HIT, not mine** |

### ⒞, written out, because it is the one I named in advance as least sure

The pre-registration said: *"If that is how it falls, ⒞ fails and I will report it as a failure, not round
it."* It fell, and it fell for a reason the pre-registration did not anticipate — **not** that the geometry
leaves a free choice, but that **there is no choice for the monodromy to make**:

- on **branch A** the mode near the wall is a **bounded phase in `√r`**. Transporting it across the wall is
  not multiplication by a constant, so there is no multiplicative monodromy to select an extension with;
- on **branch B** the wall is **limit-point**, so there is no extension to select;
- and the thing that actually removes the freedom on branch A is **neither**: it is that `r=0` is an
  **interior** locus of one closed curve carrying an `L¹` coefficient, so the solution continues absolutely
  continuously and uniquely. Measured: `‖T−I‖` across `|ℓ|<ε` falls `1.02 → 7.37e-4` over six decades at
  exponent **`0.3323`** against the `1/3` the `L¹` norm predicts, equal to the analytic `∫m dℓ` to four
  figures, and independent of `E` (`0, 5, 50` → `7.361e-2, 7.362e-2, 7.371e-2`).

⌗ **And the first version of this section was worse than a failed prediction — it was a confident
over-reading.** `spectrum.py` §6 originally ended *"the only datum a crossing carries is the monodromy
phase, and the geometry supplies it."* Two things wrong with it: the `ω^{-λ}` phase is read off `ψ~r^{-λ}`,
which is the pairing `PO-22` struck; and *"no boundary"* does not by itself remove a freedom, since an
interior limit-circle point is exactly a locus at which a transmission condition **can** be chosen. The
note now sits at the line that carried it, and the check there carries only the geometric fact it can carry.

## The controls, and what each was for

1. **`B26` reproduced** (tortoise barrier): peak `1.96307` at `r=0.30378` vs `B26`'s `0.30385`, and `|V|`
   decaying toward the horizon. ⇒ a silence about the continuum in the leaf measure is the operator's and
   not the machinery's.
2. **The integrability classifier** on a known pair: `ℓ^{-1/2}`, `ℓ^{-2/3}` `L¹`; `ℓ^{-1}`, `ℓ^{-3/2}` not. 4 of 4.
3. **The leaf length** reproduces `P14_leaf_compactness`'s `1.8138 α` at Nariai (`1.8128 → 1.8137 → 1.8138`).
4. **The `M=0` member**, where `f(0)=1`, both pairings coincide and `r^{±λ}` **is** the right exponent —
   `W2`'s own control. ⇒ the fork's discriminator is `f` blowing up at the wall, not algebra style.
5. **The non-`L¹` coefficient**: at `ℓ^{-1}` and `ℓ^{-4/3}` the window integral **diverges**
   (`5.66→39.59`; `62.27→793683`) and the transfer does **not** settle (`‖T−I‖` spanning `0.53…2.00`),
   while at `ℓ^{-2/3}` the increments shrink to `4e-4`. ⇒ the convergence is a finding about this operator.

⌗ Two of this file's checks failed on their comparators and were repaired at the comparator, never at the
threshold: a fixed `‖T−I‖<1e-2` at a fixed `ε` tests the choice of `ε` and not the operator, so the test
became a **limit** test (monotone decrease, measured rate, agreement with the Gronwall quantity) with the
ladder extended rather than the bar lowered; and a convergence test that compared the **first** cutoff to
the last was replaced by the increment test `P14_leaf_compactness` itself uses. A third repair removed a
`nan`: the controls now use the exact `E=0` form, because **a `nan` is not a measurement**.

## Which pre-registered outcome this is, and the verdict

The pre-registration enumerated four. The measurement is **none of them exactly**, and saying so is part of
the scoring: outcome 1 needed ⒞, outcome 2 needed ⒞ to fail *because the extension is a free choice*, and
⒞ failed because **there is no choice at all**. Outcome 2's *conclusion* is nevertheless the one the
evidence forces, and by a cleaner route than outcome 2's reasoning:

> **`PO-95`'s two halves close, and the row ends as a STATED LIMIT.**
>
> **⒜ Completeness, in the leaf's own measure: it holds.** The leaf is a closed curve of finite length; the
> coefficient is bounded except at the three walls where it is `L¹`; there is no endpoint anywhere and no
> free transmission parameter at any wall. So the operator has **compact resolvent**: pure point spectrum,
> a complete orthonormal eigenbasis, Weyl counting `N(E)~LE/π` measured. **The wall-bound modes are
> complete in the leaf measure together with *nothing*** — in this measure there is no continuum to be
> complete with. The continuum is the **tortoise** measure's, where `B27` closed completeness by
> Kato–Rellich. The row's own sentence — *"the completeness of the wall-bound modes together with the
> continuum, shown in the leaf's own measure"* — therefore asks for an object that does not exist in that
> measure, and the honest answer to it is the pair of theorems and not the single one.
>
> **⒝ The matching, across the locus the geometry already crosses: it is determined** — on **both** branches
> of the operator dispute, for two different reasons, and in closed form on each.
>
> **And the terminal clause holds.** Every theorem used is textbook: Carathéodory continuation for an `L¹`
> first-order system, compact resolvent on a compact domain, Weyl asymptotics. The closed domain through
> `r=0` and the finite leaf length are **read off** the fixed background, which is what *"a Dirac operator
> on a fixed background"* means. **Nothing in the closure is a mechanism the construction supplies**, and
> the one thing I expected to be the construction's own — the wall's `ω^{-λ}` fixing the extension — is not.

The verdict sits inside an assert that can fail (`spectrum.py` §9), conjoining the four measurements it
rests on: the window transfer's limit, the control that could have said otherwise, the Weyl count against
the leaf's own length, and the compactness of both arcs.

## Routed, not claimed

1. **The operator dispute is incoherent in the corpus's own record, and the row does not need it settled.**
   `receipts/INDEX.md`'s row for `L-276` reads *"THE TWO BRANCH-POINT VERDICTS RECONCILED: LIMIT-CIRCLE
   STANDS"* (written r3319), while that receipt's own head reads **WITHDRAWN r3339** and reverts to
   limit-point; and `P14` sec:chirality currently carries `ψ'/ψ=λ/(r√f)` — branch A — citing `W2`. Three
   records, two verdicts. ⌗ *One observation inside it, offered as an observation: `L-276`'s withdrawal test
   substitutes candidate solutions into `ψ'=(λ/r)ψ`, which is the disputed pairing's own equation, so it
   returns `r^{+λ}` by construction; and `L-265`'s displayed exponent `-iλr/2M` pairs a `d/dr` coefficient
   with `dℓ`, which is the same species of mismatch its own finding is about — its verdict is unaffected,
   since both exponents are bounded.* **This is `69`'s to settle and no paper or register is touched here.**
2. **The inner segment does not converge at Nariai.** As the horizons merge, `∫_0^{r_b} dr/√|f|` **grows**
   (`1.5617 → 2.8935 → 4.2228 → 5.5520` as `ε` falls to `1e-8`), the increments not shrinking — the simple
   pole's signature — while `P14_leaf_compactness`'s **between-horizon** object converges to `1.8138 α`.
   Compactness of the leaf at Nariai therefore rests on the itinerary, which is `P3`'s and not this file's.
3. **`r7577`'s new rule fires.** The result bears on `P14` sec:chirality's own sentence that *"the quantised
   field, its mode completeness, and the join between the static region's continuum and the wall … remain
   open"*, and on `P7`'s `frontier:fermion`. Named in the reply so `69` adds the row to
   `computations/beyond_the_wall/r7577_69_the_census_refresh/items_keyed.tsv`.

## Scope held

`P14` and `P7` are **not edited**. The instruments stay frozen: no new gate, ledger, census or receipt about
receipts, and no register repaired. The `λ` spectrum is not computed (`P14_mode_monodromy_at_the_wall`'s own
*"what is not computed"*), the three-generation count is untouched, and no claim is made about `B27`
reaching further than it states.
