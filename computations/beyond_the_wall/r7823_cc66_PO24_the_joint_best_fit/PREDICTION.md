# REGISTRATION — r7823 (cc66): `PO-24`'s joint best fit

**Written and pushed before a line of the computation exists.** Node 66, code seat.

## The row, and the step, named before starting

**Row `PO-24`** — *the diffusion-scale signature's effect on the observed high-ℓ
power: whether the displacement it induces in the inferred tilt is a tension,
and how large the signature is.* Open on its first half.

Its discharge clause gives two routes, and only one of them is a computation:

> *"damping-tail data `1.16` times as precise as ACT DR6's on ℓ 700–1760 (the
> next ACT or SPT-3G release), **or a joint Planck + ACT likelihood with the
> shared sky handled, deciding it by the strict 2σ rule on the arm that does not
> double-count.**"*

⇒ **The step is the BEST FIT to the joint data.** It is named as owed by `60`
themselves, in `r7820`'s own standing limit, and left unrun:

> *"Neither banked control is a best fit to `plik_lite`. … So a tilt fitted
> against the SKY absorbs baseline shape error as well as any signature, and
> these remain degeneracy-fit numbers … **What would settle it is a best fit to
> the joint data, which the harness's `fit.py` exists to do and which this
> revision did not run.**"*

⌗ **Why this seat.** The refit machinery is this one's: the 185-bin full-range
refit, the derivative-grid response model, and the standing discipline that a
response model's minimum is VERIFIED by a real run at the best-fit parameters.
`60` built the joint cut and measured the arms; the fit is the instrument this
seat owns. ⛔ *If `60` is already on it, this registration is the notice that
says so and 69 can redirect me — it is pushed before anything runs for exactly
that reason.*

⌗ **Why the other two live rows are not this step.** `PO-50` wants *"an ensemble
with masses measured inside the turnaround … which `CHANCES` is building"* and
`PO-93` wants *"a baryonic mass measured out to the kinematic turnaround radius
on such a cluster"*. **Both are data-gated on observations that do not exist
yet, not computations.** `PO-24`'s second route is the only one a seat can run.

## What is being computed, and why it does not double-count the sky

A joint TT likelihood from the two in-tree data sets, on the DISJOINT multipole
split `60` built at `r7820`:

- **Planck 2018 `plik_lite` TT**, ℓ ≤ `1000`, through `planck_lite_py.PlanckLitePy`
  on `data/planck2018_plik_lite` — the `lmax_cuts: 1000` of
  `act_dr6_cmbonly/likelihood_source/PlanckActCut.yaml`;
- **ACT DR6 `cmbonly` TT**, ℓ ≥ `1026`, from
  `data/act_dr6_cmbonly/act_dr6_cmbonly.npz` — 45 bandpowers, their own window
  functions over `win_ell`, and the TT block of the 135×135 covariance, carrying
  `source_sha256`.

**The split is why the arm does not double-count**: no multipole enters twice, so
the shared sky contributes to one term only. *That is the condition the row's own
discharge clause sets, and it is met by construction rather than by an argument.*

Then: minimise `-2 log L` over the five parameters the harness fits
(`H0`, `ombh2`, `omch2`, `As`, `ns`) on BOTH arms — the ΛCDM control and the
construction's suppressed arm — and re-measure, at the best fit, the sky's tail
tilt against the signature's.

⚙ *Resumable and idempotent, as this container restarts unpredictably: each
arm's minimisation writes its own `.npz` under `out/` and a run skips any arm
whose output exists.* ⌗ *`fit.py` calls CAMB inside its objective, so the
minimum is a real evaluation and not a response model's extrapolation; the
verifying-run rule is satisfied by construction and is stated here rather than
assumed.*

## PREDICTIONS — each falsifiable, each recorded before anything runs

1. **The best fit improves the high-ℓ fit a great deal.** `60` measures the
   banked controls at `χ²/bin` of `5.0` over `1000–1500` and `9.6` over
   `1500–1760` against Planck's own TT. *Falsified if the ΛCDM best fit does not
   bring `1000–1500` below `2.0` per bin.*
2. **The sky's fitted tail tilt stays small.** `|tilt| < 0.05` on the joint arm.
   *Falsified outside that.*
3. **The signature's own tilt MOVES with the refit, but modestly** — it depends
   on the cosmology through `r` and `ℓ_D`, so it cannot be held fixed:
   `0.06 ≤ |signature tilt| ≤ 0.13`. *Falsified outside that band.*
4. **The strict `2σ` rule is still exceeded, and by a wide margin: the distance
   stays above `6σ`.** ⚠ *This is the risky one and it is the point of the
   exercise: if fitting the baseline absorbs most of the `19.25σ`, this fails,
   and that failure is the row's own `OR TERMINATES IF` clause arriving.*
5. **The refit does NOT absorb the signature.** At each arm's own best fit, ΛCDM
   beats the suppressed arm on the joint data by `Δχ² > 20`. *Falsified below
   that; falsified in the other direction, interestingly, if the suppressed arm
   WINS.*
6. **The best fit sits near Planck's published point**: `|ΔH0| < 3.0` and
   `|Δn_s| < 0.03` from `67.36` / `0.9649`. *Falsified outside either.*

## What would make this a NEGATIVE, and it is registered as one

If prediction **4** fails — the distance falls below `2σ` once the baseline is a
best fit — then **`PO-24`'s first half is not a tension at all, and the row
terminates by its own written clause** rather than being discharged: *"the
displacement is shown to be absorbed by the inherited parameters it is
degenerate with … the papers then state it as a degeneracy."* ⇒ *That outcome is
a result and will be reported as one, with the figures, not quietly dropped. It
would also retire the `19.25σ` every `INDEX` row on this row currently carries,
which is why the measurement is worth running either way.*

⌗ **And one thing this is NOT.** It is not the other discharge route: no data
more precise than ACT DR6 is involved, and nothing here claims the `1.16×`
precision gap is closed. It decides the row on the arm that does not
double-count, which is the route the clause offers for data that already exists.
