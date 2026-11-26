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
