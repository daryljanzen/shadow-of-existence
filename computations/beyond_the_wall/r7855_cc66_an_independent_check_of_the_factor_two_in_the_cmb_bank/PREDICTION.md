# `r7855+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7855` (69), items ① and ②. Written and pushed in its own commit **before a line of the
computation exists**. Item ③ waits on 60 listing the receipts that pin absolute statements.

---

## ⚠ FIRST, A CORRECTION TO THE ORDER'S OWN PREMISE, FOUND BEFORE COMPUTING ANYTHING

The order says to compare against *"the CMB bank (`computations/beyond_the_wall`, the arrays `model6`
reads)"*. **Those arrays are not in the repository.** `model6` takes its CMB half from `model3`, and
`model3` reads them from an environment path:

    POL_DIR = os.environ.get('POL_DIR', '/tmp/claude-0/pol_grid')

`/tmp/claude-0/pol_grid` **does not exist in this container.** What *is* committed beside `model3`
is `ratio_grid3.npz`, and it carries only `ratio_tt`, `ratio_ee` and `dte_over_tt` — **sum-dependence
ratios, not absolute spectra** — plus a `divisor` of `93.14` that `model3` never reads. So the
absolute normalisation the factor two lives in is exactly what the repository does **not** hold.

⌗ **This is the THIRD time this line has lost banked work to a `/tmp` default**: 60's `555`-bin mask
at `r7847`, their `Φ`-derived bandpowers at `r7851`, and now the polarisation grid. I am naming it
again rather than working around it silently.

**⇒ SO THE CHECK IS ROUTED THROUGH THE BANK'S DEFINITION RATHER THAN ITS CACHE,** which is the
stronger test anyway. `gen_pol_batched.sh` regenerates the grid by running the instrument with
`POLSAVE` on; item ① needs **one point**, the control at `Σ = 0`. Re-running that point gives the
bank as the instrument *defines* it, so what gets compared is the definition and not 60's arithmetic
over a cache. ⌗ If that run proves infeasible here, I will say so and report what is blocked rather
than substituting 60's own banked intermediates and calling it independent.

---

## ① THE FACTOR, AND WHETHER IT IS FLAT IN `ℓ`

60 report the bank's binned TT at `0.504672` of CAMB's lensed TT, over `185` bins, ranging
`0.500015` to `0.510557`.

**Ⓐ THE FACTOR REPRODUCES.** The mean ratio over the TT bins comes out between **`0.49` and `0.52`**.
  ⇒ REFUTED outside that, which would mean 60's factor is not what an independent CAMB sees.

**Ⓑ IT IS FLAT, NOT SLOPED.** The per-bin ratio's spread (max − min) comes out **below `0.02`**, so
  the factor is a normalisation and not a shape error. 60's own range spans `0.0105`.
  ⇒ REFUTED if the spread exceeds `0.02`, which would mean something `ℓ`-dependent is mixed in and
  "a factor two" is the wrong description.

**Ⓒ ⚠ AND IT IS NOT EXACTLY ONE HALF — THIS IS THE BAND I MOST EXPECT TO BE INFORMATIVE.**
  `0.504672` differs from `0.5` by `0.93` per cent, which is **larger than the per-bin spread 60
  report**. So I register that the mean ratio differs from exactly `0.5` by **more than `0.002`**,
  and that the excess is therefore real rather than scatter.
  ⇒ REFUTED if the mean lands within `0.002` of `0.5`, which would make it a clean factor of two and
  make 60's `0.504672` an artefact of their binning rather than a property of the bank.
  ⌗ Why it matters: a clean `1/2` points at one mis-stated constant; a `1/2` plus a per-cent excess
  points at a constant AND something else, and the two have different repairs. 69 has ruled that 60
  locate the line, so the useful thing this check can hand them is **which of those two it is**.

---

## ② TT ALONE, OR ALL THREE

The bank carries TE and EE: `score_ttteee` scores `555` concatenated bins across all three blocks,
with `NTT`, `NTE`, `NEE` from plik_lite and ONE fitted amplitude across them.

**Ⓓ THE FACTOR IS IN ALL THREE, NOT CONFINED TO TT.** EE's mean ratio lands within **`0.02`** of
  TT's, and TE's within **`0.03`** (wider because TE changes sign three times inside this
  instrument's reach, so a ratio is numerically worse behaved there).
  ⇒ REFUTED if EE or TE comes out near `1.0` while TT is near `0.5`, which would localise the fault
  to the TT path alone and contradict a shared normalisation.
  ⌗ This is the band that distinguishes a single mis-normalisation upstream of all three from a
  TT-only defect, which is exactly what the order asks for.

**Ⓔ AND THE SIGN STRUCTURE OF TE SURVIVES THE RATIO.** TE's zero crossings sit at the same `ℓ` in
  bank and reference, so the disagreement is amplitude and not phase.
  ⇒ REFUTED if a crossing moves by more than one bin, which would make it a shape fault.

---

## ⚠ WHAT THIS CANNOT SETTLE, REGISTERED NOW

It cannot say **which** of the bank and CAMB is right: it measures a ratio, and a ratio names a
discrepancy without attributing it. ⌗ It also cannot locate the line — 69 has ruled that 60 do that,
and nothing here should be read as having found their line. And a factor near `1/2` is *consistent*
with the cancellation 60 describe against the baryon fault's factor two in the lensing power, but
this check does not test that cancellation and will not claim to.

⌗ **COST.** One instrument point under `POLSAVE`, idempotent: the output `.npz` is written once and
skipped if present, because this container is reclaimed unpredictably.
