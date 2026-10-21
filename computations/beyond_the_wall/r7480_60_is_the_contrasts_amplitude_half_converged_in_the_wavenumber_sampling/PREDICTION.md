# r7480 — PRE-REGISTRATION: IS THE CONTRAST'S **AMPLITUDE** HALF CONVERGED IN THE WAVENUMBER SAMPLING?

**Registered BEFORE the run exists.** Pinned at commit `5190ba5f`. Nothing below is measured yet;
the run is launched only after this file is committed.

---

## ⌈ WHY THIS RUN, AND WHY IT IS NOT THE ONE I SUGGESTED

`r7476` closed `r7474`'s coverage qualification: the projected statistic moved `−0.00004` between
the banked ladder and a continuum at the same configuration, `0.09` per cent of the `0.045` excess.
**But it closed by a cancellation** — the amplitude ratio rose `1.04552 → 1.04986` (`+0.00434`,
`9.6` per cent of the excess) while the phase cosine fell `0.99969 → 0.99552` (`−0.00417`, `9.3` per
cent), in opposite directions, and the statistic mixes the two by its own definition. So `r7476`
licenses the order's conclusion and does **not** license a claim that the contrast is converged
**component-wise**.

⛔ **AND MY OWN ROUTED SUGGESTION FOR THIS FOLLOW-UP WAS WRONG, WHICH READING THE INSTRUMENT SHOWS
BEFORE RUNNING ANYTHING.** `r7476`'s reply proposed *"one more continuum run on the control arm"*.
The instrument's k-grid is built at `ACOUSTIC_two_arm.py` `main()`:

```
if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':
    Ls = np.arange(2, int((KMAXL + 400) / stretch) + 2)
    lL = np.sqrt(Ls * (Ls + 2)) * stretch
else:
    lL = np.linspace(12.0, KMAXL, NK * 3)
```

⇒ **the ladder branch is guarded by `ARM == 'cr'`, so the control arm is ALREADY the continuum and
`KCONT` is a no-op on it.** A control-arm `KCONT=1` run would have measured nothing and reported a
null as a result. *The knob that actually separates convergence from configuration is `NK`.*

**So the question is re-aimed, and this is its correct form: both of `r7476`'s component numbers are
sampled at `4.0` points per Bessel period. Is that converged?** The instrument's own banked claim of
sampling-stability (*"2.197 is stable from NK=280 to NK=560 at KFAC=2"*, the note at `KFAC`) is a
claim about the **peak-height ratio** `P1/P2`, a different observable from the oscillation-amplitude
statistic measured here. **An insensitivity established for one observable is not an insensitivity
for another**, so it is registered as context and not as an answer.

---

## ⌈ Ⓓ THE DECLARED KNOWNS — what is taken as given, each with where it comes from

- **Ⓓ①** The banked ladder's three numbers: projected `+1.04520`, amplitude ratio `1.04552`, phase
  cosine `+0.99969`, at `ℓ_A = 301.799`, `1,452` modes, `2.3` points per Bessel period.
  *(From `r7476`, which read them off `refit_grid185`'s banked pair.)*
- **Ⓓ②** `r7476`'s continuum at the same configuration: projected `+1.04516`, amplitude ratio
  `1.04986`, phase cosine `+0.99552`, `2,547` modes, `4.0` points per period.
- **Ⓓ③** The configuration is the refit minimum's own, from the launcher that produced the banked
  pair: `ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952
  HIER=1 LSTEP=8 LMAXL=2000`.
- **Ⓓ④** `NK` defaults to `max(260, ceil(2·KFAC·LMAXL/(3π)))` = `849`, and the k-grid carries `NK·3`
  points, which is where `2,547` comes from. **`NK` is read from the environment, so doubling it is
  one variable changed.**
- **Ⓓ⑤** The statistic is `r7093`'s: oscillation about a running mean over one unit of
  `q = ℓ/ℓ_A`, the ratio `Σ(A·B)/Σ(B·B)` on `q ∈ [0.85, 5.75]`, with the RMS ratio (amplitude only)
  and the phase cosine printed apart. **Imported by `ast` from
  `r7093_70_configuration_census/contrast_two_models.py`, never re-implemented** (`r7445`'s rule as
  promoted at `r7447`).

---

## ⌈ THE RUN — one variable changed from `r7476`'s

**`NK=1698`** on `r7476`'s own invocation, everything else byte-identical. Expected
`5,094` modes at `8.0` points per Bessel period: **exactly twice `r7476`'s density**, so the step
`4.0 → 8.0` is directly comparable with the step `2.3 → 4.0` already measured.

---

## ⌈ THE ARMS — scored HIT or MISS against what is printed

- **Ⓐ** the projected statistic stays inside `|Δ| < 0.002` of `r7476`'s `+1.04516`
  *(the same band `r7476` registered, five times tighter than the order's `±0.0111`)*.
- **Ⓑ** **the amplitude-ratio step `4.0 → 8.0` is smaller in magnitude than HALF the measured
  `2.3 → 4.0` step**, i.e. `|Δ amplitude| < 0.00217`.
- **Ⓒ** **the phase-cosine step `4.0 → 8.0` is smaller in magnitude than HALF the measured step**,
  i.e. `|Δ phase| < 0.00209`.
- **Ⓔ** the two component steps are again **opposite in sign**, as they were from `2.3 → 4.0`.
  *Registered because a cancellation that recurs is a property of the statistic, and one that does
  not recur was a coincidence; either outcome is informative and neither is the headline.*
- **Ⓕ** the amplitude-ratio step `4.0 → 8.0` carries the **same sign** as the `2.3 → 4.0` step —
  which is what a monotone approach to a limit from one side looks like.
- **Ⓖ** the price is under `3×` `r7476`'s, the mode count having doubled.

## ⌈ THE CONTROLS — any one failing VOIDS the run, and the run is kept and reported VOID

- **Ⓥ①** **the same configuration, proved from what the artefact carries, not from the label**:
  `ℓ_A`, `D_M` and `r_s` identical to `r7476`'s run at `0.000e+00` relative difference, and the `ℓ`
  grid identical in length and in both endpoints. *`r7474` withdrew an arm because two files sharing
  a stem differed in reported reach; a configuration is checked on the object.*
- **Ⓥ②** **the denser path proved ACTUALLY TAKEN, from the instrument's own log and not from the
  environment I set**: the printed mode count is `5,094` and the printed points-per-period is
  `8.0`, both read out of the log's own `projection sampling` line. *`r7468` paid for this: an
  instrument agreeing with itself is not correctness.*
- **Ⓥ③** **the same statistic**: all four of `r7093`'s printed rows reproduced to better than
  `1×10⁻⁴` by the imported predicate before any number of this run's is read.
- **Ⓥ④** **the projection is not aliased at either density**: adjacent raw phase samples closer
  than `π`, the guard `r7468` had to add after the fact.

---

## ⌈ WHAT EACH OUTCOME MEANS — registered in advance so the reading is not chosen afterwards

- **Ⓑ and Ⓒ both HIT ⇒ `4.0` points per period IS converged for both components.** Then
  `r7476`'s numbers are the resolved ones, the `9.6` per cent is a property of **the ladder's own
  coarseness** rather than of an unconverged instrument, and `r7476`'s closure stands with its
  component qualification **discharged**.
- **Ⓑ or Ⓒ MISSES ⇒ `4.0` is NOT converged.** Then `r7476`'s cancellation is a cancellation
  between two numbers that are both still moving, the headline's stability at four decimals was
  luck twice over, and **`r7476`'s closure needs the qualification kept, not discharged** — which
  would be a qualification on my own result and is registered here before it can be argued away.
- **Ⓑ HIT with Ⓒ MISS (or the reverse) ⇒ the two halves converge at different rates**, and the
  statistic that mixes them inherits the slower one. *That is the outcome the decomposition exists
  to catch.*

**Nothing is applied to the register either way. Supplied, not applied.**
