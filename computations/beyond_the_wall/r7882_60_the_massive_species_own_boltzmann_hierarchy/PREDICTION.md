# r7882+60 — REGISTRATION: item ② of order `r7879`, the massive species' own Boltzmann hierarchy

**Committed and pushed BEFORE any measurement of this revision runs, and before the switch exists.**

`r7879` (69): *"**(a) is the repair.** The massive species' own Boltzmann hierarchy, momentum-binned,
in the standard form CAMB itself integrates (Ma & Bertschinger 1995): ℓ-moments beyond the
quadrupole, the mass entering through each bin's energy, the Fermi–Dirac weight from the background
already built. No fitted quantity: the q-grid and ℓ-cutoff are numerical and are converged, not
tuned. Behind a switch, default off, byte-identical off, closure kept (W always on). **Validate
jointly:** TT's `A` within `0.03` of one and EE within `0.03` of one, at `0.30` and `0.60` eV, read
on both fitters. Only then a limit."*

---

## READS TAKEN BEFORE THIS REGISTRATION, DECLARED

All structural, from the instrument's own source. **Nothing has been run and nothing fitted.**

1. **The sector's gauge and variables.** The perturbation equations are conformal-Newtonian in
   Ma & Bertschinger's own convention — `δ' = −(1+w)θ + 3(1+w)Φ'` and
   `θ' = −ℋ(1−3w)θ − (w'/(1+w))θ + (c_s²/(1+w))k²δ − k²σ + k²Ψ` — with `Ph` the curvature potential
   and `Ps` the Newtonian one. ⌗ *Established FIRST, because a hierarchy written in the wrong gauge
   would be a different object wearing the same name.*
2. **A massless ℓ-hierarchy is already there.** `F[:, i]` carries `F_{i+2}` to depth `LN = 12`, with
   the standard massless recursion and the standard `(LN+1)/η` truncation, and `F[:, 0]` is the
   shear the potential's source already reads through `sig`.
3. **The Fermi–Dirac machinery the order points at is already built**: the weight
   `f₀(q) = 1/(e^q+1)` written as `exp(−q)/(1+exp(−q))`, the dimensionless momentum `q` in units of
   the present neutrino temperature, `y(a) = (Σ/3)·a/T_ν0`, and the energy and pressure integrals
   that `NUF_of` and `NUW_of` are splined from.
4. **The state vector's layout** — `NV = 7 + (LN−1) + 1 + (1 if BVEL else 0)`, with the baryon
   contrast required to stay at the last index when `BVEL` is off.

---

## WHAT IS BUILT

Per momentum node `q_j`, moments `Ψ_ℓ(q_j)` for `ℓ = 0 … ℓmax`, in the gauge of read ⓵, with
`ε_j(a) = √(q_j² + y(a)²)` and `g(q) ≡ dln f₀/dln q = −q/(1+e^{−q})`:

```
Ψ_0' = −(q k/ε) Ψ_1            − Φ' g(q)
Ψ_1' = + (q k/3ε) (Ψ_0 − 2Ψ_2) − (ε k/3q) Ψ_N g(q)
Ψ_ℓ' = + (q k/((2ℓ+1)ε)) (ℓ Ψ_{ℓ−1} − (ℓ+1) Ψ_{ℓ+1})          for ℓ ≥ 2
```

truncated at `ℓmax` in the same `(ℓ+1)/η` form the massless hierarchy already uses, so the two
truncations are one convention and not two. The sector's `δ`, `θ` and `σ` are the `q`-integrals of
`Ψ_0`, `Ψ_1` and `Ψ_2` against `q² ε f₀`, `q³ f₀` and `q⁴/ε f₀`, normalised by the same background
integral the instrument already carries.

**⛔ THE SWITCH REFUSES TO RUN BESIDE THE FLUID APPROXIMATION.** *The guard: when a fork names two
objects, check that the thing they are alternatives FOR has a slot for only one of them.* The
hierarchy and `r7876`'s fluid approximation are two models **of the same sector**, and that sector
has one slot. So the switch refuses `NUPERT=1` and the hierarchy together, rather than silently
letting one overwrite the other. It also refuses without `NUFD=1` and a non-zero sum, as the fluid
switch does.

**Closure is kept:** the source weight change is always on under the hierarchy, as `r7879` requires,
so the configuration the hierarchy is validated in is a closure-respecting one.

**Default off and byte-identical off**, measured on output both ways of being off — absent and `0` —
as `r7878`'s switch arms did.

---

## ⛔ THE CONVERGENCE CRITERIA, FIXED NOW AND IN RESOLUTION-INDEPENDENT FORM

*No number below was chosen by looking at a grid. `r7879` says the grid and the cutoff are
"numerical and are converged, not tuned", so what makes them numerical is that the criteria are
fixed before the first grid is tried.*

| | gate | criterion | why this number |
|---|---|---|---|
| **Ⓠ⓵** | **the quadrature against the background already built** | the `q`-grid's own integrals must reproduce `NUF_of` and `NUW_of` — the instrument's own `ρ_ν(a)/ρ_ν⁰` and `w_ν(a)` — to **`1e-04` relative, at every decade of `a` from `1e-10` to `1`** | these two splines are already validated machinery; a grid that cannot reproduce them is not integrating the species the background describes, and this gate is cheap and runs before any spectrum |
| **Ⓠ⓶** | **the `q`-grid** | doubling the number of nodes must move the fitted `A` in TT and in EE by less than **`0.003`** at both sums | one tenth of the `0.03` validation band `r7879` fixed: the numerical error must not be able to decide the verdict |
| **Ⓠ⓷** | **the `ℓ`-cutoff** | raising `ℓmax` by half must move the fitted `A` in TT and in EE by less than **`0.003`** at both sums | the same tenth of the same band, for the same reason |
| **Ⓠ⓸** | **the massless limit** | at `Σ → 0` the hierarchy's spectra must agree with the landed massless hierarchy to the fit's own resolution | the massive hierarchy reduces to the massless one when the mass vanishes; if it does not, it is not the same object continued |

⛔ **Ⓠ⓵ AND Ⓠ⓸ RUN BEFORE ANY VALIDATION NUMBER IS READ**, and if either fails the validation is
not reported at all — a hierarchy that neither reproduces the background it is built on nor reduces
to the limit it extends has nothing to say about `A`.

⌗ **AND THE COST IS DECLARED AS A RISK, NOT AS A RESULT.** The state vector grows by
`n_q × (ℓmax+1)` per mode, so the integration cost grows with it, and the convergence study is run
at REDUCED spectral resolution while the validation legs are run at the banked resolution. If the
validation legs do not fit in one revision, **that is reported as a measured cost and the item is
split**, with the convergence study landing first — not quietly dropped and not run at a resolution
the banks cannot be compared against.

---

## THE VALIDATION, ON `r7879`'s OWN BANDS

`A` and `ε` refitted against CAMB by the fit of record, executed and not re-implemented, its
reproduction leg required to return `1.15162`, `1.29592`, `1.01405`, `1.04630` first.

| | condition | verdict |
|---|---|---|
| **Ⓐ** | `\lvert A−1 \rvert ≤ 0.03` in **TT and EE**, at **both** sums | **the repair validates jointly, and a limit may be read** — which is the first time any candidate reaches this |
| **Ⓑ** | TT inside `0.03` at both sums, EE outside at either | **refused by the constraint**, and no limit is read |
| **Ⓒ** | EE inside `0.03` at both sums, TT outside at either | **the hierarchy does not close the TT excess**, and the fraction it does close is reported per sum |
| **Ⓓ** | both outside at either sum, but TT closer to one than the fluid approximation gave at both | **a better model of the sector and still not the repair**, with the improvement reported as a fraction |
| **Ⓔ** | TT no closer than the fluid approximation gave at either sum | **the sector is not where the excess is**, and that is the finding |

⛔ **The five rows are written to be mutually exclusive and the receipt checks that exactly one
fires.** *`r7878`'s item ① had two fire at once because its registration did not make them
exclusive; `r7880`'s had a row whose condition was not defined; neither is repeated here.*

**Both fitters**: this seat's fit of record, and `cc66`'s second fitter, which reads the banked legs.
⛔ **The legs are banked for that second fit whatever the verdict**, so the reading is not this
seat's alone — and if `cc66`'s fit disagrees with this one beyond its own reproduction tolerance,
**that disagreement is the finding and no limit is read through either.**

⛔ **NO LIMIT IS READ IN THIS REVISION even under `Ⓐ`.** `r7879` puts the limit in item ③, on the
closed cross-seeded envelope, and that is a separate revision with its own registration.

---

## REACHABLE NEGATIVES, NAMED

- **Ⓠ⓵ can fail**: a quadrature that reproduces `w_ν` but not `ρ_ν`, or either only at late times.
- **Ⓠ⓶ or Ⓠ⓷ can fail to converge at all** within a cost this revision can pay, which is a result
  about the method's cost and is reported as one.
- **Ⓠ⓸ can fail**: the massless limit is where a sign or a normalisation error shows, and it is the
  one place the answer is already known independently.
- **Ⓔ is reachable**: the hierarchy may move TT no further than the fluid approximation did, and
  `r7878` measured that the fluid family's whole span is `0.42`–`0.69` of the excess.
- **And Ⓐ is reachable**: if it fires, the sector was the right object all along and the fluid
  approximation was simply too coarse — which is `r7879`'s own reading.

## WHAT IS NOT CLAIMED

- The hierarchy is **not** tuned to the validation. The only numbers it carries are `n_q` and
  `ℓmax`, both fixed by the gates above and not by `A`.
- `r7878`'s `NUPARTS` and `NUCA` are **not removed**. They stay as the fluid approximation's own
  switches, and the hierarchy refuses to run beside them rather than replacing them in place.

---

## AMENDMENT, DECLARED: WHAT Ⓠ⓸ ASSERTS, AND THE FLOOR UNDER IT

⛔ **THIS IS A DECLARED READ, NOT A FRESH REGISTRATION.** `Ⓠ⓸` was measured before this section
was written and its criteria are NOT moved by it. What was seen is stated first, in full:

- A first run reported a worst relative difference of **`4.345e-01`** at both sums, flat across the
  decade. That was a STRUCTURAL defect and it is fixed: the hierarchy's seeding sat inside the CR
  arm's branch of the initial-condition `if`/`else`, so on `lcdm` — the arm every validation number
  in this revision is read on — `Ψ` started at zero and grew from the sources alone. `δ` was a
  factor eight short at `e/e_rec = 0.01` and only caught up by recombination. The seeding now sits
  outside the `if`/`else`, where one block serves both arms.
- With that fixed the worst relative difference is **`2.335e-05`** at `Σ = 1e-3` and **`2.446e-05`**
  at `1e-4`, and the hierarchy's `δ` and `θ` track the landed fluid's to `≈ 3e-05` relative from the
  first sample to recombination.
- **The residual is FLAT across the mass decade** (factor `1.0`), which is why `limit.py`'s shrink
  test still reports `Ⓠ⓸` as not met.

**The registered criterion in the gate table is agreement `to the fit's own resolution`.** The
shrink test is `limit.py`'s reading of it, and that reading is strictly stronger than what is
registered. It is also unsatisfiable by construction: the massless map `Ψ_ℓ = -g M_ℓ/4` is inverted
by a FINITE quadrature, so the on/off comparison carries the `q`-grid's own representation error,
which depends on `NQ` and NOT on the mass. A mass-independent floor cannot shrink with the mass
however correct the physics is, so a shrink test cannot separate a defect from the floor.

⛔ **So the floor is IDENTIFIED rather than assumed, by one arm registered here before it is run:**

| | arm | criterion | what each outcome means |
|---|---|---|---|
| **Ⓠ⓸ᵃ** | **the floor is the quadrature's** | re-run the same comparison at `NQ` doubled to `24`, mass decade unchanged: the worst relative difference must **fall by at least a factor `3`** AND stay flat across the decade to within a factor `2` | the floor is the `q`-grid's representation error, it is not the mass, and `Ⓠ⓸`'s registered criterion is then read on `Ⓠ⓸ᵇ` |
| | | it does **not** fall | the floor is NOT the quadrature's, something mass-independent is still wrong in the hierarchy, and `Ⓠ⓸` is reported FAILED with no validation number read |
| | | it falls but becomes mass-DEPENDENT | the mass term is entangled with the grid, which is its own defect, reported as one with no validation number read |
| **Ⓠ⓸ᵇ** | **the registered criterion itself** | at `Σ = 1e-4` the fit of record, executed on the hierarchy-on and hierarchy-off spectra, must return an `A` in TT and in EE differing by **less than `0.003`** — the same tenth of `r7879`'s `0.03` band that `Ⓠ⓶` and `Ⓠ⓷` are held to | this is `to the fit's own resolution` asserted on the quantity the fit actually reads, which is the clause `Ⓠ⓸`'s argument reasons FROM: that at `Σ → 0` nothing the fit reads moves |
| | | `A` moves by `0.003` or more in either spectrum | `Ⓠ⓸` FAILED on its own registered criterion, and no validation number is read |

**Both rows can fail and the negatives are reachable:** a `3e-05` difference in the spectra is only
*presumed* small for the fit until the fit is run on it, and `Ⓠ⓸ᵇ` is the arm that can refuse that
presumption. `Ⓠ⓸ᵃ` can fail outright if the floor is a residual defect rather than the grid.

⛔ **`limit.py`'s shrink test is NOT deleted and its verdict is NOT overwritten.** It stays in the
record as run, reporting what it reports, and `RESULT.md` carries both it and these two arms.

### Ⓠ⓸ᵇ, HOW IT IS RUN — DECLARED BEFORE THE LEGS ARE BUILT

⛔ **AN ERROR IN THE ROW ABOVE, NAMED RATHER THAN QUIETLY REPAIRED.** `Ⓠ⓸ᵇ` says *"at
`Σ = 1e-4` the fit of record ... must return an `A` ... differing by less than `0.003`"*, and the
fit of record CANNOT BE RUN AT THAT SUM as written: `shift.py` reads a bank whose slots ARE the
validation sums `0.30` and `0.60`, and it fits `A` against the CAMB spectrum at those sums. There is
no CAMB target at `1e-4`.

**What makes the arm runnable is that it is a DIFFERENCE AT A FIXED TARGET.** `Ⓠ⓸ᵇ` compares
`A(hierarchy on)` against `A(hierarchy off)` on legs built at the SAME sum and fitted against the
SAME CAMB spectrum. The target therefore cancels out of the comparison and need not be the right
target for that sum — what must hold is only that both legs share it, which they do by construction.
`A` itself will sit far from one in these legs and ⛔ **no `A` from them is a validation number or is
reported as one**; only the on-against-off DIFFERENCE is read.

So the two bank slots carry the two limit sums, and one fit reads both:

| slot | sum built into it | what the slot's `A` difference reads |
|---|---|---|
| `S030` | **`Σ = 1e-3`** | the hierarchy's effect on what the fit reads, at the upper limit sum |
| `S060` | **`Σ = 1e-4`** | the same, a decade down |
| `S000` | the zero leg, **reused from `r7874` and not rebuilt** | mass-independent by construction, and `NUHIER` refuses a zero sum, so it is the same spectrum either way |

⛔ **The criterion is UNCHANGED**: `∣A(on) − A(off)∣ < 0.003` in TT and in EE, now read at BOTH limit
sums rather than one, which is strictly harder than what the row registered.

⛔ **AND THE COST IS MEASURED HERE, NOT LATER.** These four legs are the FIRST legs built at the
banked resolution (`HIER=1 LMAXL=2000 LSTEP=8`) with the hierarchy on, so their wall time is the
measurement the declared cost risk asks for. The state vector grows from `20` to `176` per mode. If
these four do not fit, the validation legs do not either, and the item splits with the convergence
study landing first — **reported as a measured cost, which is what the risk registered.**

### THE LABEL IN ROWS Ⓨ AND Ⓛ IS MANY-TO-ONE — REGISTERED BEFORE THE VALIDATION LEGS ARE FITTED

⛔ **NOTHING BELOW HAS BEEN MEASURED YET.** The validation legs were still running when this was
written, no fit had been run on them, and `Ⓠ⓸` had just been met. This fixes a reading, not a
result.

Rows `Ⓨ` and `Ⓛ` compare this revision's TT against *"the fluid approximation"*. **By the guard on
many-to-one labels, that label has to be checked before two things are identified by it — and it
does not pick out one number.** `r7878` measured FIVE fluid arms and they disagree, read off its own
`refit_parts.json` rather than recalled:

| arm | what it is | `∣A−1∣` in TT at `0.30`, `0.60` | the same in EE |
|---|---|---|---|
| `W` | the weight change alone | **`0.00490`**, **`0.05621`** | `0.04005`, `0.05961` |
| `C` | continuity alone | `0.13111`, `0.26394` | `0.01237`, `0.04361` |
| `E` | Euler alone | `0.05464`, `0.13902` | `0.00060`, `0.02019` |
| `CE` | the named subset | `0.08759`, `0.18952` | `0.00769`, `0.03424` |
| `A1` | all three, exact `c_a²` | `0.07885`, `0.09214` | `0.04650`, `0.07225` |

So "the fluid approximation gave" could mean `A1`, the full fluid model, or `W`, which is the one
`r7879` rules stays in every candidate, and the two differ by a factor sixteen in TT at `0.30`. A
row read on `A1` is far easier to pass than the same row read on `W`.

⛔ **THE READING FIXED HERE, AND IT IS THE HARDEST ONE:** `Ⓨ` and `Ⓛ` are read against **the
fluid family's BEST TT at each sum, whichever arm achieves it** — which the table above makes
`W` at both: `0.00490` at `0.30 eV` and `0.05621` at `0.60 eV`. The baseline is written to
`fluid_baseline.json` by a script that reads `r7878`'s record, so the number in the receipt is the
record's and not a transcription.

**Why the hardest reading rather than the fairest-sounding one:** `Ⓨ` and `Ⓛ` exist to ask whether
the hierarchy is a better model of this sector than the fluid approximation was. If the hierarchy
cannot beat the best thing the fluid family already did, then on this evidence it is not better, and
a baseline chosen to be beatable would turn that finding into its opposite. ⌗ *And it is already
visible in the table — before any number of this revision's is read — that `W`'s TT at `0.30` is
INSIDE the `0.03` band on its own. So `Ⓨ` is a real bar: at `0.30 eV` the hierarchy must get TT
within `0.00490` of one to clear it, which is tighter than the validation band itself.*

⌗ **`Ⓑ`, `Ⓒ` and `Ⓐ` do not touch this label** — they are read against `r7879`'s `0.03` band alone,
and they are unaffected by which arm the baseline is. Only `Ⓨ` and `Ⓛ` needed a reading.
