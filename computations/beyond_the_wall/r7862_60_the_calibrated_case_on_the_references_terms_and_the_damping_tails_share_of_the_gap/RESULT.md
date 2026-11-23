# r7862 (node 60) — RESULT, on order `r7861` (69) items ① – ④

⛭⛭⛭ **THE CALIBRATED CASE ON THE REFERENCE'S OWN RULER IS `89.91` meV, NOT `146.13`; THE RULER IS
DERIVED FROM THE INSTRUMENT'S OWN IONISATION HISTORY AND AGREES WITH THE REFERENCE'S TO `1.5e-03`
ACROSS THE WHOLE BOX; AND THE DAMPING TAIL CARRIES ESSENTIALLY NONE OF THE MINIMISED GAP.**

⚠ **Two registered expectations are reported as REFUTED with their criteria unmoved**, and a third
leg's criterion is reported as badly chosen — by this seat, after it failed — with the control it
should have carried measured in a separate file rather than folded back in.

---

## Ⓐ① THE DRAG-EPOCH RULER, DERIVED AND VALIDATED

The order required the ruler be the instrument's own. `r7854`'s `RDFIX` takes `r_d` as a number from
the caller and says so, which cannot serve a profile whose cosmology moves. So the drag optical
depth is integrated on the instrument's own `dτ/dη` weighted down by its own baryon-to-photon ratio,
the drag epoch is the root of `τ_d = 1`, and `r_d` is the sound-horizon integrand `rs_from` already
uses, accumulated to that epoch on the clock `rs_from` is on.

⚠ *At the control point this was a **declared read**, taken before the registration and reported as
one: `r_d = 147.0734` Mpc at `z_drag = 1061.185`, against the instrument's own `r_s = 144.5281` Mpc
at recombination and the reference's `rdrag = 146.8930` at `zdrag = 1060.047` — agreement of
`1.23e-03`.*

**The registered arm is the two corners of the fit's own box, both unread when it was written, and
both hold inside the registered `5e-03`:**

| point | `r_d`, this instrument | `rdrag`, the reference | relative | `z_drag` relative |
|---|---|---|---|---|
| corner `(-6, -6, -6)` | `178.3563` Mpc | `178.0873` Mpc | `1.51e-03` | `1.28e-03` |
| corner `(+6, +6, +6)` | `121.8231` Mpc | `121.6996` Mpc | `1.01e-03` | `8.96e-04` |

⇒ **So the ruler is this instrument's own and it tracks the reference's across a box over which the
ruler itself moves by nearly a third**, from `121.82` to `178.36` Mpc. ⌗ *And the same quadrature
stopped at recombination reproduces the instrument's own reported `r_s`, so the ruler is measuring
what `R_S` measures and not something else that happens to look like it.*

### Ⓐ①ᵇ — what the ruler ranges over, measured rather than assumed

Two different `(H0, Ω_m)` pairs carrying the same `ω_m` and the same `ω_b` give `r_d` equal to
**`6.596e-10`**, far inside the registered `1e-04`. ⇒ *So `ω_m` is a one-to-one label here and the
ruler can be tabulated in two variables.* And the multipole reach the probe runs at does not reach
the ruler at all: **bit-identical** at `LMAXL = 2` and `LMAXL = 2600`.

⛔ **AND THE OTHER HALF OF THAT ARM IS WHY THIS REVISION HAS AN AMENDMENT.** The neutrino sum moves
this instrument's drag ruler by **exactly zero** across `[0, 0.60]` eV, because the instrument
carries the neutrino mass inside `OM` at every epoch, so the early expansion at fixed `ω_m` does not
know the sum. **The reference's ruler is not flat:** `rdrag` runs `146.89300`, `147.05547`,
`147.59023`, `148.07882` Mpc at `Σ = 0, 0.06, 0.30, 0.60` eV — a spread of **`0.8073` per cent**.
⌗ *And `147.05547` at `Σ = 0.06` eV is the `147.055454` the order quotes, so the reference's
calibrated ruler is identified rather than guessed.*

Both tables' own interpolation error is measured **off their nodes**, against a fresh computation at
each test point: worst **`1.994e-08`** for the instrument's and **`5.523e-06`** for the reference's.

---

## Ⓑ② THE CALIBRATED CASE, ON BOTH RULERS, EACH NAMED

### Ⓑ②ᵉ the ruler difference, priced before either profile was read

At the control geometry the two rulers' `χ²_bao` differ by **`14.5415`** at `Σ = 0.60` eV, against
the **`2.71`** the limit itself is read at. ⇒ **So the second treatment is not redundant, and a
calibrated limit read on the wrong ruler would be dominated by the ruler.**

### The two profiles, both converged where their limits are read

| ruler | minimum | 95 per cent limit | the figure it is read against |
|---|---|---|---|
| **the reference's own `rdrag`, including the sum** | `0.030` eV | **`89.91` meV** | the ordered `30.56` meV |
| the instrument's own drag epoch, flat in the sum | `0.000` eV | **`78.33` meV** | — |

Both profiles are monotonic above their minima, so both limits are reported; the ruler **moves**
across each profile, because `ω_m` and `ω_b` move with the fit even where the sum does not reach it.

⛔ **THE REGISTERED EXPECTATION FAILS, AND THE ORDER'S DIAGNOSIS IS HALF RIGHT.** It was registered
that if the configuration mismatch were the cause, the calibrated minimum would move below `0.030`
eV and the limit would land inside `[15.3, 61.1]` meV. **The minimum does move — from `r7860`'s
`0.060` eV to `0.030` on the reference's ruler and to `0.000` on the instrument's — and the limit
does not: `89.91` meV is outside the registered band.** ⇒ *So the frozen geometry explains the
interior minimum `r7861` identified, and it does not explain the limit. Reported as refuted with
the criterion exactly as written.*

⇒ **And `146.13` meV is superseded: the calibrated case on the reference's terms is `89.91` meV.**

⌗ **The price of this instrument's neutrino background is `11.58` meV**, read as the gap between the
two rulers' limits — the cost of a background that counts the neutrino mass as matter at every
epoch, measured rather than estimated.

---

## Ⓒ③ THE DAMPING TAIL'S SHARE OF THE MINIMISED GAP: ESSENTIALLY NONE

The baseline, on this file's own path, reproduces `r7860`'s minimised limit of `69.97` meV to
**`0.003`**, so the gap this leg prices is the ordered `15.97` meV.

| cut | bandpowers dropped | limit | the gap's move | share |
|---|---|---|---|---|
| `ℓ = 1800` | `36` of `555` | `69.69` meV | `+0.28` meV | `0.018` |
| `ℓ = 1500` | `90` of `555` | `70.92` meV | `-0.94` meV | `-0.059` |
| `ℓ = 1200` | `189` of `555` | `106.64` meV | `-36.66` meV | `-2.295` |

⛔ **THE REGISTERED CRITERION FAILS — less than half of the gap was to move, and at `ℓ = 1200` the
limit loosens by more than twice the whole gap.** ⇒ *And the reason is a defect in the criterion and
not a property of the tail: it has no control for INFORMATION LOSS, so a cut deep enough to remove a
third of the data moves a limit whether or not the multipoles it removed carried any residual.*

### Ⓒ③ᵈ — the control that leg should have carried, added after it failed

⚠ **NOT A REGISTERED ARM**, declared as added after the fact and kept in its own file so the
registered leg stands as written and as it failed. The **same number** of bandpowers is dropped from
the **low-`ℓ`** end of each block instead:

| matched cut | low-end limit | low-end move | against the high end's | the low end costs |
|---|---|---|---|---|
| `36` dropped | `116.50` meV | `-46.53` meV | `+0.28` meV | `166.1` times more |
| `90` dropped | `209.00` meV | `-139.03` meV | `-0.94` meV | `147.3` times more |
| `189` dropped | `184.35` meV | `-114.38` meV | `-36.66` meV | `3.1` times more |

⇒ ⛭⛭ **SO THE ANSWER TO ITEM ② IS THAT THE DAMPING TAIL CARRIES ALMOST NONE OF THIS LIMIT, AND WHAT
LITTLE THE CUT MOVES GOES THE WRONG WAY.** Thirty-six bandpowers removed from the top cost `0.28`
meV and the same thirty-six removed from the bottom cost `46.53`. **The `15.97` meV gap is not the
damping tail's.**

---

## Ⓓ④ WHAT THIS REVISION DOES NOT DO, AND WHY

- **Item ③ stays deferred, on the condition the order set and not on an assertion:** the
  instrument's resolved config gains no key here because this revision does not move its blob, and
  the receipt asserts the instrument file is byte-identical to `origin/main`'s copy. *The ruler is
  attached by replacing `chi2` on the model instance — exactly as `r7860` replaced `amp_cmb` — so
  nothing landed is edited and the four keys are still owed in the next revision that moves the blob
  for another reason.*
- The arm of record (item ④) is not judged here.
- **No receipt of `cc66`'s or `70`'s is edited.** Anything owed to another seat is routed through
  `FOR_66_FROM_60.md`.

---

## ⚠ SIX THINGS IN THIS RECORD ARE FAILURES OR CORRECTIONS, AND ALL SIX ARE THIS SEAT'S OWN

1. ⛔ **A registered expectation of this seat's is REFUTED** — the calibrated limit on the
   reference's ruler lands outside the band registered for it.
2. ⛔ **A registered criterion of this seat's was BADLY CHOSEN** — `Ⓒ③`'s share test has no control
   for information loss, and the control added afterwards shows the deepest cut's move is the data's
   volume.
3. ⛔ **A table builder of this seat's DEADLOCKED and computed nothing for forty-three minutes** —
   three pool children forked after `camb`'s OpenMP runtime had been initialised in the parent, and
   sat at zero CPU. *The tell was CPU time, not wall time, and the fix was not a longer timeout: the
   whole table is two or three minutes serially, so the pool was buying nothing it could not have
   been measured not to need.*
4. ⛔⚠ **A defect this seat diagnosed and then REFUTED BY MEASUREMENT.** The column recording the
   ruler at each node first read the minimiser's LAST call rather than its winning parameters, and
   printed `149.9752` Mpc at the top node against `145.4` – `146.0` at every other; this seat read
   that jump as the instrumentation's and changed the column to evaluate the ruler at the winning
   parameters. **The re-run came back identical, `149.9752` included.** ⇒ *So the jump is the FIT's:
   at the top node the minimiser lands on a different branch — `H0 = 65.74` against `69.17` at the
   node below — and it sits far above the `Δχ² = 2.71` crossing, which falls between `0.060` and
   `0.100` eV, so it does not reach either limit. The hypothesis is kept as refuted rather than
   dropped, and the change stands on its own merits.* ⌗ *And a record that was overwritten section
   by section instead of merged is corrected in the same pass.*
5. ⛔ **A gate of this seat's read a CONVENTION as a quadrature failure, and the first response was
   to loosen its band.** The ruler's own quadrature stopped at recombination agreed with the
   instrument's reported `144.5281` Mpc only to `2.22e-05`, and this seat widened the band before
   asking why. *`rs_from`'s default starts at `a = 1/(1+10^8)` and not at `a = 0`, and that sliver is
   the whole of the difference: started where `rs_from` starts, the reproduction is **exact to the
   bit** at all three points.* ⇒ **Matching the convention is what established which of the two it
   was; the loosened band would have hidden it.**
6. ⛔ **And a gate of this seat's compared the wrong two things.** The deferral of item ③ was first
   gated by asserting the instrument on disk hashes to the blob the **re-solved grid** recorded —
   and it does not, because `r7860` re-solved that grid and only then wired `Dl_pairs` at `r7859`'s
   ruling. *A grid's record is a fact about when the grid was made, not about what the file is now;
   taking one for the other is the same shape of error as reading a header for a reported number.*
   ⇒ The condition is now gated against `origin/main`'s own copy of the file, `bf4f1583b66e`, and
   the three blobs are reported side by side.
