# `r7875+cc66` — REGISTRATION, pushed before a line of either computation exists

Order `r7875` (69), two items. ⑬ an independent check of `60`'s shift–amplitude fit `A`, from my own
CAMB leg and my own fitting code against `60`'s banked instrument ratios, for TT and EE at
`Σ = 0.30` and `0.60` eV over `ℓ = 100`–`420`, with `ε`'s allowance taken from `θ*` as `60` did,
stating whether I get `1.152` and `1.296`. ⑭ the two-start midpoint test at `Σ = 0.20`, `0.30`,
`0.50` and `0.60` eV on both rulers.

**What is READ and what is COMPUTED, stated now so neither can be swapped later.**

READ, not recomputed:
- `60`'s instrument ratios, from `bank/pol_grid_bvel1_nufd_only/lcdm_S000.npz`, `lcdm_S030.npz`,
  `lcdm_S060.npz` — keys `ls`, `Dl` (TT), `Dl_EE`, and `l_A`. `238` multipoles, of which **`41`
  fall in `ℓ = 100`–`420`**. I have no instrument of my own; this side must be `60`'s.
- the control cosmology, from `60`'s `model3.ARMS['lcdm']['centre']` at run time, and `τ`, `A_s`,
  `lmax` from my own `r7871` record, which is where `60` took them from.

COMPUTED fresh here:
- my CAMB leg, run now rather than read out of `r7871`'s `sum_response.json`.
- the `(A, ε)` fit, in my own code.

⌗ `60`'s `shift.py` reads my `r7871` record **only for those control parameters** and runs CAMB
itself through its own `camb_one`. So the CAMB side is genuinely two independent runs, not one run
read twice, and this check can disagree with `60` on CAMB as well as on the fit.

---

## ⑬ — the independent check of `A`

**Ⓐ①** The control is read at run time, never retyped, and `τ` is declared: `H0 = 67.40`,
`Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965`, `τ = 0.054`, `A_s = 2.1e-9`, `lmax = 1200`.

**Ⓑ②** ⛔ A CONTROL BEFORE ANY FIT. My fresh CAMB ratio must agree with my own `r7871` record's
ratio for the same block and sum. ** If my two runs disagree, nothing downstream is readable and no
`A` is reported. ** Band: agreement to `1e-6` in the ratio, which is far tighter than any `A`
difference that would matter.

**Ⓒ③** The instrument ratio is `Dl(S)/Dl(0) − 1` on the bank's own `41` in-band multipoles. ** The
multipole set is `60`'s, not every `ℓ`: ** a fit on `321` multipoles would be a different
measurement, and I state which I used rather than discovering the difference afterwards. I report
`A` on **both** sets, because if they differ the choice is load-bearing and must be visible.

**Ⓓ④** `ε`'s allowance from `θ*`, as `60` did: `f_inst = l_A(S)/l_A(0) − 1`, and
`f_camb = −(θ*(S)/θ*(0) − 1)` because `ℓ` scales as `1/θ*`; the allowance is `|f_inst − f_camb|`.
REGISTERED REPRODUCTION TARGET, from `60`'s record: `2.563e-04` at `Σ = 0.30` and `5.170e-04` at
`0.60`, with `l_A` of `301.374817`, `300.120258` and `298.831268`. `l_A` is read, so only `θ*` is
mine; a disagreement here is a disagreement about CAMB's `θ*`, not about the fit.

**Ⓔ⑤** THE ITEM'S QUESTION. My own fit of `r_inst(ℓ) ≈ A · r_camb(ℓ(1+ε))`, `A` by least squares at
each `ε` and `ε` by grid then refinement. ** REGISTERED EXPECTATION: `A = 1.152` (TT `0.30`),
`1.296` (TT `0.60`), `1.014` (EE `0.30`), `1.046` (EE `0.60`), each to within `0.005`. ** That is
`60`'s `1.1516250`, `1.2959240`, `1.0140521`, `1.0462960`. A miss is a REAL DISAGREEMENT and is
reported as one, not reconciled.

**Ⓕ⑥** ⛔ THE FIT MUST BE ABLE TO RETURN SOMETHING ELSE. A planted `(A, ε)` imposed on the CAMB
ratio must be recovered to `1e-3` in `A` and to the `ε` grid's own step. A fitter that always
returns about `1.15` on TT would agree with `60` for no reason at all. This is the same positive
control the `MassiveNuMethod` knob needed at `r7871` and the custom-source path needed at `r7873`.

**Ⓖ⑦** The interpolation of `r_camb` onto `ℓ(1+ε)` is a choice of mine and is declared. I measure
how far `A` moves between two schemes (linear and cubic). ** A difference from `60` SMALLER than
that sensitivity is not a disagreement, and I will not report it as one. **

**Ⓗ⑧** ⛔ REGISTERED AS AT RISK, BECAUSE `60`'s OWN RECORD SAYS THE MODEL DOES NOT FIT INSIDE THE
ALLOWANCE. `60` report `eps_within_allowed = false` for all four fits, with `eps_over_allowed` from
`2.73` to `6.63`. So the best-fit `ε` is `3`–`7` times the shift a registration may legitimately
carry. ** I therefore report `A` twice: at `ε` FREE, and at `ε` PINNED to the allowance boundary. **
Quoting only the free-`ε` `A` would hide that the fit buys its amplitude with a shift the geometry
does not allow. I expect the pinned `A` to differ, and if it does not, that is worth knowing too.

**Ⓘ⑨** I do not expect to settle whether the excess is real physics. `60`'s verdict is AMPLITUDE and
`69` has routed the epoch-consistent perturbations to `60`. This item checks a NUMBER.

---

## ⑭ — the branch scan at the other sums

**Ⓙ⑩** ⛔ TWO OF THE FOUR SUMS HAVE NO BANKED BEST FIT. `r7853`'s bank holds `0.000`–`0.300` and
`0.400` on both rulers. ** `Σ = 0.50` and `0.60` ARE NOT BANKED. ** At `r7873` the two-start test
set the other four parameters to the banked best fit for that ruler; with no bank there is nothing
to read. So for `0.50` and `0.60` a cold profile run produces that point FIRST, and it is declared
here rather than substituted quietly. `0.20` and `0.30` read their banked points as `r7873` did.

**Ⓚ⑪** The criterion is `r7873`'s, scaled: the midpoint of the two converged five-parameter points
is scored, and a barrier is compared against the profiler's own `fatol = 5e-3` and against the
one-parameter unit `Δχ² = 1`. A ridge under either is NOT a basin boundary. ** The unscaled form is
not used: at `r7873` it called a barrier a hundredth of `fatol` a second basin, and that was my
defect. **

**Ⓛ⑫** ⛔ REGISTERED AS AT RISK: THE BOX MAY DECIDE THIS BEFORE THE LIKELIHOOD DOES. `BOX` caps
`Ω_m` at `0.40` and `τ` at `0.12`. At `Σ = 0.400` the `rd_min` best fit already sat at
`Ω_m = 0.34387`. At `0.50` and `0.60` the fit may land ON a boundary, and a midpoint test between
two boundary points measures the box, not the basin. ** Interiority is checked and reported per sum
and per ruler, and a boundary hit is reported as NO VERDICT AT THAT SUM — not as one basin. **

**Ⓜ⑬** EXPECTATION: one basin at every sum, extending `r7873`'s `Σ = 0.400` result across the
range. The honest alternatives, both registered: a boundary hit at the top of the range (`Ⓛ⑫`),
and a genuine ridge exceeding `fatol`, which would mean `r7869`'s "one branch to `0.60` eV" fails
somewhere between `0.400` and `0.600`.

**Ⓝ⑭** The run is long — up to twenty profile minimisations. The launcher is IDEMPOTENT: it skips
any output already on disk, so a container restart costs only the run in flight. Nothing is
reported from a partial scan except as partial, named sum by sum.

---

## AMENDMENT, before any of ⑬ was computed — two errors of fact in my own `Ⓐ①` and `Ⓑ②`

Found by reading `r7871`'s record and `60`'s `shift.py`, not by running anything. Both are errors
about WHAT EXISTS, not adjustments made after seeing a result, and the amendment is committed before
item ⑬'s first computation.

**⒜ `Ⓐ①` named the wrong `lmax`.** I wrote `lmax = 1200`. That is `r7873`'s `LMAX_CALC`, not
`r7871`'s. My `r7871` record carries `lmax_calc = 2600`, and `60` took `LMAX` from that record, so
`60` ran at `2600`. ** A like-for-like check must run at `2600`, and that is what ⑬ will use. ** The
`1200` in `Ⓐ①` is struck.

**⒝ `Ⓑ②` asked for a comparison the record cannot support.** I registered that my fresh CAMB ratio
must agree with `r7871`'s "ratio" to `1e-6`. ** `r7871` banks NO per-`ℓ` ratio array. ** It banks
summary statistics and, under `standard`, the ratio at six NAMED multipoles — `ℓ = 100`, `220`,
`500`, `1000`, `1500`, `1996` — for each of TT, TE, EE at sums `0.06`, `0.30`, `0.60`.

So `Ⓑ②` is rebuilt on what is actually there, and NARROWED, which is the honest direction:

> **`Ⓑ②′`** My fresh CAMB ratio must reproduce `r7871`'s banked `standard` values for TT and EE at
> `Σ = 0.30` and `0.60`. Two of the six multipoles, `ℓ = 100` and `220`, fall inside ⑬'s band; the
> other four lie outside it and are checked as well, because a CAMB leg that matches in the band and
> departs outside it is not the same run. Band: `1e-9` relative, since both runs are the same code
> at the same settings and any real difference would be a changed setting, not noise. ** If this
> fails, no `A` is reported. **

⌗ The weaker control is the one the record can bear. Registering a tighter one against data that
does not exist would have produced a control that could only ever pass by being skipped.
