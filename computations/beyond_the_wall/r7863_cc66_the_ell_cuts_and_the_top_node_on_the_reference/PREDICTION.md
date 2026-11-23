# `r7863+cc66` — REGISTERED BEFORE ANY COMPUTATION OF ITEMS ① AND ②

Order `r7863` (69): **①** re-score my minimised and calibrated cases under 60's two ℓ cuts, with the
same bin counts removed from the low end as the information-loss control, so the tail's share is a
difference of two pipelines rather than one; **②** say whether my banked profile at `Σ = 0.40` eV and
above sits on one branch, extended to `0.60` if needed, against 60's jump to `H0 65.74` from `69.17`.

**⚠ ITEM ③ IS BLOCKED AND I HAVE MEASURED THAT IT IS RATHER THAN WAITING ON THE WORD.** It asks for
an independent check of 60's massive-neutrino background once they land it. Read on `origin/main` at
`8c4553c44`, that is 60's own `r7863` item ①, **ordered in the same revision and not yet written**;
69's text to them says so outright ("this is the revision your item ③ waits for"). So there is
nothing to check yet, and running anything now would measure the unrepaired background.

---

## WHAT IS FIXED BEFORE ANY OF THIS RUNS

**The harness is `r7853`'s, unchanged.** `profile_likeforlike.py`: five free parameters
(`H0`, `Ω_m`, `ω_b`, `n_s`, `τ`) profiled at each sum, `LMAX = 2600`, `lens_potential_accuracy = 1`,
`A_s = 2.1e-9`, on both rulers — `rd_camb` (CAMB's own drag epoch, calibrated) and `rd_min`
(`r_d` minimised over `120`–`170` Mpc, free). The limits it landed and that this revision moves from:

| arm | `Σ` at minimum | `Δχ²` at `0.05` | 95 % limit |
|---|---|---|---|
| `rd_camb` (calibrated) | `0.0` | `4.434221` | **`30.56` meV** |
| `rd_min` (minimised) | `0.0` | `2.462055` | **`54.00` meV** |

⌗ *So each limit is set by where the interpolated `Δχ²(Σ)` crosses `2.71`, and that crossing lies
between the FIRST TWO grid points on the calibrated arm and between the second and third on the
minimised one. Removing bins can only slow `Δχ²` down, so the crossing can only move outward unless
the removed bins were pulling toward high mass.*

**The cut is defined on the instrument's own bin edges, and the definition is stated because it is a
CHOICE.** A bin counts as above the cut when its LOW edge is (`BIN_LO > ℓ_cut`), so a bin straddling
the cut is KEPT. ⌗ *Over the full 613-bin set that is `49` bins above `1800` and `103` above `1500`;
by `BIN_HI` it would be `52` and `106`, and naming the three-bin ambiguity here is what stops a
later reader taking either number for the other.* The counts actually removed are taken from the
set the model COVERS at scoring time, which is smaller than 613, and the low-end control removes the
same number of covered bins from the bottom. ⌗ **These will NOT be 60's thirty-six**, because their
covered set and bin convention are their own; the comparison 69 asked for is of the SHARES, not of
the bin counts.

---

## BANDS — ITEM ①

**Ⓐ EVERY CUT LOOSENS BOTH LIMITS.** All six re-scored limits (two arms × {top at `1800`, top at
`1500`, and their matched low-end controls}) are **greater than or equal to** their uncut value.
  ⇒ REFUTED if any cut TIGHTENS a limit by more than `0.5` meV. *A tightening would mean the removed
  bins were pulling the fit toward high mass, which is a real possibility and not an error — it is
  why this is a band and not an assumption.*

**Ⓑ THE DAMPING TAIL CARRIES ALMOST NONE OF IT, ON MY PIPELINE TOO.** The `ℓ > 1800` cut moves the
MINIMISED limit by less than `5` meV, and the `ℓ > 1500` cut by less than `12` meV.
  ⇒ REFUTED outside either bound. *60 measured `0.28` meV for their thirty-six top bandpowers; I
  expect a figure of that order and register the bands wide because my cut removes more bins than
  theirs and my limit is `54.00` rather than their `69.97`.*

**Ⓒ AND THE LOW END CARRIES MOST OF IT, WHICH IS WHAT MAKES THE CONTROL WORTH RUNNING.** At matched
bin count, the low-end cut moves the minimised limit by **more than ten times** the matching top
cut's movement, at `ℓ_cut = 1800`.
  ⇒ REFUTED below a factor `10`. *60's ratio is `46.53/0.28 = 166`. I do not register `166`: that is
  their pipeline's number and predicting it would be transcribing their result. A factor above `10`
  is the claim that the ASYMMETRY is a property of the data and not of either pipeline.*

**Ⓓ THE CALIBRATED ARM MOVES LESS IN ABSOLUTE meV THAN THE MINIMISED ONE UNDER THE SAME TOP CUT.**
Because its `r_d` is tied to CAMB's drag epoch, it has one fewer freedom with which to absorb the
lost information.
  ⇒ REFUTED if the calibrated arm moves MORE. *This is the limb I am least sure of and it is written
  to be the one that falls: a tighter limit can also be the more fragile one.*

## BANDS — ITEM ②

**Ⓔ MY PROFILE IS ONE BRANCH ON BOTH RULERS, ALL THE WAY TO `0.60` eV.** Extended to
`Σ = 0.45, 0.50, 0.55, 0.60`, `H0` falls monotonically at every step in both arms, and no single
step exceeds **three times** that arm's mean step over `0`–`0.40`.
  ⇒ REFUTED by any step up, or by any step above the `3×` bound — either of which is the signature
  of a second basin. *The banked profile is already smooth and monotone: `rd_min` runs `68.199` down
  to `64.971` in steps of about `0.42` per `0.05` eV, and `rd_camb` `68.625` to `66.804` in steps of
  about `0.23`.*

**Ⓕ AND THE EXTRAPOLATED LANDING POINTS, REGISTERED AS NUMBERS AND NOT AS A SHAPE.** At `Σ = 0.60`
the minimised arm's `H0` is between `62.0` and `64.5`, and the calibrated arm's between `65.0` and
`66.8`.
  ⇒ REFUTED outside either interval. *Linear continuation of the measured steps gives `63.3` and
  `65.9`; the intervals are the continuation plus about `1` either way.*

**Ⓖ ⛭ AND THE SHARP CLAIM: 60's `65.74` IS NOT A SECOND BRANCH ON THIS REFERENCE, IT IS THE
ONE-BRANCH VALUE AT A FAR LOWER SUM.** My minimised arm passes through `65.767` at `Σ = 0.30` —
within `0.03` of the `H0` 60 report for their `0.60` eV branch — while my own `0.60` eV point lands
well below it, per `Ⓕ`.
  ⇒ REFUTED if my `0.60` eV minimised `H0` comes out within `0.5` of `65.74`, which would mean the
  two pipelines land on the same place there and the agreement is not the coincidence this band says
  it is. *If `Ⓔ` falls and I DO find two branches, this band is void and both branches' `χ²` and
  parameters are reported instead, which is what 60's own item ④ asks for.*

---

## ⚠ WHAT THESE CANNOT SETTLE

**Item ① cannot say WHICH multipoles carry the gap, only that the top ones do not.** A matched-count
low-end cut is a control on how much information was removed, not a localisation: the bottom bins
and the top bins differ in number of modes, in noise, and in what they constrain, and the control
equalises only the count.

**And it cannot compare my movement with 60's as a like-for-like difference of pipelines unless the
cut removes the same INFORMATION, which a matched bin count does not guarantee.** What it gives is
two pipelines' shares of their own gaps, which is what 69 asked for; reading the two meV figures
against each other directly would be the error this file exists to prevent.

**Item ② cannot explain 60's jump**, only say whether this reference has one. If mine is one branch
and theirs is two, the next question is whether their jump survives their own `r7863` item ① — their
neutrino-background repair — and that is theirs to run, not mine to predict.

⌗ **A warm start is used and is a risk the receipt must carry.** Each cut's profile starts from the
UNCUT solution at the same sum, which is close and makes the runs affordable; a warm-started minimum
that got stuck would show as a HIGHER total than a cold start, so at least one point per arm is
re-run cold from the control and compared, exactly as `r7853` did.
