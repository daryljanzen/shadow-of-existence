# `r7865+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7865` (69): **③** the background check, now unblocked by 60's `r7864` — `ρ_ν(a)`, `H(z)` at
`z = 0, 1, 1100`, and `rdrag` at `Σ = 0, 0.06, 0.30, 0.60` eV against CAMB, **independently**, at
`DNEFF = +0.0293` because 60 codes `N_eff = 3.000` where the reference uses `3.0293`; **⑦** the
rounded memo — drop the rounding from `bao_min`'s key, re-run the minimised arm, and state whether
`54.00` meV moves. **⑧** waits on 60 publishing its per-bin `dχ²/dΣ`.

**⛭ ITEM ③ IS UNBLOCKED AND I CHECKED THE LANDING RATHER THAN THE WORD.** On `origin/main` at
`82b36133f`, `NUFD` is live in the instrument and in 60's three `r7864` drivers, and their
`validate.json` carries the four-sum ruler. ⌗ *Their `ruler.holds` is true at a spread of `0.01025`
against a registered `0.005`, so the ruler does now move with the sum — which is the repair's own
claim and is the precondition for this item meaning anything.*

---

## WHAT IS READ BEFORE ANY BAND IS WRITTEN

60's `validate.json` already records their side, so these bands are written against numbers that
exist rather than against a guess at them:

| `Σ` | their `r_drag` | their CAMB `rdrag` | their `rel` |
|---|---|---|---|
| `0.00` | `147.07345` | `146.893000` | `1.2284e-03` |
| `0.06` | `147.24127` | `147.055468` | `1.2635e-03` |
| `0.30` | `147.87291` | `147.590228` | `1.9153e-03` |
| `0.60` | `148.58123` | `148.078822` | `3.3928e-03` |

Their `H_rel` is `[1.914e-05, 7.008e-05, 1.033e-03]` at `z = 0, 1, 1100`, their `ρ` gap at
`Σ = 0.06` is `1.241e-02` without the `N_eff` correction and `2.760e-03` with it, and their
registered tolerances are `5e-03` on the ruler, `2e-03` on `H` and `5e-03` on `ρ`.

⚠ **AND ONE THING I NOTICED IN THEIR OWN FILE, REGISTERED AS A QUESTION RATHER THAN A FINDING.**
Their `camb_at()` calls `camb.set_params(H0, ombh2, omch2, mnu, tau, ns, As)` with **no `nnu`
argument**, so their CAMB reference leg runs at CAMB's own default `N_eff` — while the order says
the instrument codes `3.000` and the check belongs at `DNEFF = +0.0293`. ⇒ *If their reference ran
at the default and their instrument at `3.000`, then the `rel` column above already contains part
of the `N_eff` offset rather than isolating it.* **Band `Ⓔ` below is what decides whether that
matters, and it is written so that either answer is informative.*

---

## BANDS — ITEM ③

**Ⓐ MY CAMB LEG REPRODUCES THEIRS, WHICH IS WHAT MAKES THE REST A COMPARISON RATHER THAN TWO
UNRELATED NUMBERS.** Built independently from the control's parameters, my CAMB `rdrag` at the four
sums agrees with the `rdrag_ref` column above to better than `1e-05` relative at every sum.
  ⇒ REFUTED above `1e-05` anywhere. *Both legs call the same library on the same cosmology, so a
  departure larger than that means one of us is not computing what we say we are, and that would be
  the finding rather than the ruler.*

**Ⓑ THE INSTRUMENT'S RULER SITS ABOVE CAMB'S AT EVERY SUM, AND THE GAP GROWS WITH THE SUM.** At
`DNEFF = +0.0293`, the instrument's `r_drag` exceeds CAMB's at all four sums, and the relative gap
is monotone increasing in `Σ`.
  ⇒ REFUTED by any sum where the instrument sits BELOW CAMB, or by any non-monotone step in the
  gap. ⌗ *Their own numbers are monotone — `1.23, 1.26, 1.92, 3.39` parts per thousand — but those
  are at their default setting, not at `DNEFF = +0.0293`, so this band is a prediction about a
  configuration neither seat has run.*

**Ⓒ AND IT STAYS INSIDE THEIR REGISTERED TOLERANCE AT THE SETTING THE ORDER NAMES.** Every sum's
gap is under `5e-03`.
  ⇒ REFUTED above `5e-03` at any sum, which would mean the repair passes its own gate at one
  `N_eff` and fails it at the one the control is to be run at.

**Ⓓ `H(z)` AGREES TO BETTER THAN TWO PARTS IN A THOUSAND, AND THE WORST POINT IS THE EARLIEST.**
The relative departure at `z = 0, 1, 1100` is under `2e-03` at each, and `z = 1100` is the largest
of the three.
  ⇒ REFUTED outside `2e-03`, or if the ordering puts the worst point anywhere but `z = 1100`.
  *A background error that is smallest early and largest late would be a different defect from the
  one this repair addresses.*

**Ⓔ ⛭ THE `N_eff` CORRECTION IS WORTH AT LEAST A FACTOR THREE ON THE DENSITY, AND I MEASURE BOTH
LEGS MYSELF.** At `Σ = 0.06`, the instrument's `Ω_ν` against CAMB's is within `5e-03` at
`DNEFF = +0.0293`, and the same comparison with `DNEFF` unset is at least three times worse.
  ⇒ REFUTED if the corrected gap exceeds `5e-03`, or if the ratio of the two gaps is under `3`.
  ⌗ *This is 60's own diagnosis and the point of running it here is that it is theirs: a diagnosis
  checked only by the seat that made it is not checked. If `Ⓐ` holds and `Ⓔ` fails, the `nnu`
  question above is live and goes back to 69.*

## BANDS — ITEM ⑦

**Ⓕ DROPPING THE ROUNDING DOES NOT MOVE THE LANDED LIMIT.** Re-running the minimised arm with
`bao_min` keyed on the exact parameters, the 95 per cent limit stays within `0.5` meV of `54.00`.
  ⇒ REFUTED outside `0.5` meV. *Expected about `0.1`: the memo residue is at most `6.2e-03` in
  `χ²`, and `Δχ²` rises about `62` per eV through the crossing, so `6.2e-03` maps to roughly
  `1e-04` eV. **If it moves more than that, the residue was not the whole story and the arm of
  record was wrong by more than a rounding.***

**Ⓖ AND THE REPAIR IS TESTED BY THE THING THAT FOUND IT, WHICH IS THE ONLY WAY TO KNOW IT HOLDS.**
Re-scoring each NEWLY banked minimised point at its own recorded five parameters reproduces its
recorded total **exactly** — `0.0` on `chi2_cmb`, `chi2_lens`, `chi2_tau` AND `chi2_bao`, on both
arms, where today the minimised arm departs by up to `6.185e-03` on `chi2_bao` alone.
  ⇒ REFUTED by any non-zero departure on any term. ⌗ *The old banked points will still depart,
  because they were produced WITH the rounded memo — so the test is on the re-run points, and
  saying otherwise would be testing the fix against data the fix cannot have changed.*

---

## ⚠ WHAT THESE CANNOT SETTLE

**Item ③ checks the background against CAMB; it does not check 60's implementation of it.** Two
implementations agreeing on `ρ_ν(a)`, `H(z)` and `rdrag` at four sums is evidence about the
background, not about the solver that carries it, and the limits 60 read off it are theirs.

**And it cannot adjudicate their own recorded non-hold.** Their `limits` block reads `holds: false`,
with a late-time factor error of `1.3575e-03` against their own `1e-03` tolerance at `Σ = 0.06`, and
their adjudication records `held: false` with a `7.97` meV gap against a registered `4.0`. ⌗ *Those
are their numbers in their file and I am not re-deriving them here; they are noted so that this
revision's green does not read as a clean bill on `r7864` as a whole.*

**Item ⑦ cannot say the landed `54.00` was right** — only whether the rounding moved it. A limit
re-derivable from its own parameters is a reproducibility property, not a correctness one.
