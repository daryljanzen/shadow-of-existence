# `r7853+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7853` (69), items ③ and ⑤. Written and pushed in its own commit **before a line of either
computation exists**. Every band below has a reachable negative; none is restated after the fact.

⌗ 69's ruling on my ④ is accepted and not re-argued: the dual criterion is withdrawn, and 60's
control is now judged against this seat's reference on 60's own likelihood. Item ⑤ **is** that
reference, so it is the number their repaired control will be set against — which is why its
registration is the more consequential half of this revision.

---

## ③ THE REPAIRED TRANSFER AGAINST CAMB

Re-run of `r7851`'s `transfer_vs_camb.py` against 60's `phi_shape(4000)` under `BVEL=1`. The
pre-repair measurement was `+0.149` per cent at `k = 0.001`, **`-31.78` per cent at `k = 0.05`**,
worst `-31.89` at `k = 0.0933`, and a decay-ratio agreement of `3.39` per cent.

**Ⓐ THE DEFICIT COLLAPSES.** `|frac|` at `k = 0.05` comes out **below `5` per cent**, from `31.78`.
  ⌗ 60 report the shape against this reference "within `2.5` per cent", so this band is deliberately
  wider than their claim — it tests that the repair works, not that their number is exact.
  ⇒ REFUTED if the deficit stays above `5` per cent, which would mean `BVEL=1` is not the whole fault.

**Ⓑ THE SUPER-HORIZON END DOES NOT MOVE.** `Phi(k -> 0)` stays within `0.010` of `-0.901`, because
  the normalisation was already right pre-repair and the fault was a *shape* in `k`.
  ⇒ REFUTED if it moves further, which would mean the repair also changed the amplitude and that
  `r7851`'s super-horizon agreement was itself an accident.

**Ⓒ THE DECAY-RATIO AGREEMENT IMPROVES.** Comes out **below `3.39`** per cent, i.e. at least no
  worse than pre-repair. ⚠ This is the band most likely to fail: the pre-repair agreement was
  already good, and the repair was aimed at the shape, not the decay. A *worse* ratio would be a
  real finding and is registered as reachable.

**Ⓓ THE STATE LAYOUT MOVED, AND I DO NOT TRUST THE SLOT INDEX.** Under `BVEL=1`, `NV` comes out
  **strictly larger** than under `BVEL=0`, and the baryon slot `I_DB` moves. `phi_shape` reads
  slot `6` unconditionally; 60's own `repair.py` reads `Y[:, :, 6]` on both sides, so slot `6` is
  expected to still be `Phi` — but this is **verified by `Phi(k -> 0)` landing near `-0.9`, not
  assumed from the index**. ⇒ REFUTED if `NV` is unchanged, or if slot `6` under `BVEL=1` returns
  something whose super-horizon limit is not near `-0.9`.
  ⌗ This band exists because `r7851` was nearly defeated twice by exactly this class — CAMB's
  `Weyl` carrying a `k^2`, and the carry/transfer confusion. A moved state layout read by a
  hardcoded index is the same shape of error, and it would corrupt item ③ silently.

---

## ⑤ THE LIKE-FOR-LIKE REFERENCE

CAMB on **60's own subset and 60's own freedoms**: the `555` binned `plik_lite` bins with the `tau`
prior, the nine Planck 2018 **conservative** lensing bandpowers, 60's `distances.chi2_bao` term,
and `omega_b` and `n_s` **FREE** rather than held at the control. Reported on **both** rulers
(`r_d` from CAMB's own drag-epoch sound horizon, and `r_d` minimised as `model3.bao_direct` does),
each with a `95` per cent upper limit and an effective mass.

`r7849` gave, with `omega_b` and `n_s` **HELD**: `26.06` meV calibrated, `54.28` meV minimised.

**Ⓔ FREEING TWO PARAMETERS LOOSENS BOTH LIMITS.** Both come out **above** their `r7849` values.
  ⇒ This is the band the whole item turns on, and it is the one I argued for at `r7849` when I said
  the held-parameter comparison was an UPPER BOUND on 60's instrument's share and not a measurement.
  If a limit *tightens* instead, that argument was wrong and I will report it as refuted.
  Bands: calibrated between **`30` and `70`** meV; minimised between **`60` and `120`** meV.

**Ⓕ THE RULER STILL MATTERS, AND BY MORE THAN A TENTH.** The minimised limit exceeds the calibrated
  one by **more than `30` per cent** of the looser. ⇒ REFUTED if freeing the two parameters absorbs
  the ruler's effect and the spread collapses below `30` per cent, which would mean `r7849`'s
  "`52` per cent" was partly the held parameters rather than the ruler.

**Ⓖ THE EFFECTIVE MASS COMES OUT NEGATIVE.** Between **`-150` and `+50`** meV on the calibrated
  ruler, when the sum is allowed below zero. ⇒ REFUTED outside that interval.

**Ⓗ IT STAYS TIGHTER THAN 60's PRE-REPAIR CONTROL.** The calibrated limit comes out **below**
  `111.38` meV. ⇒ REFUTED if freeing the parameters loosens it past their pre-repair number, which
  would remove the gap this line has been reading as an instrument residue.

**⚠ WHAT THIS REFERENCE STILL WILL NOT SETTLE, REGISTERED NOW SO IT CANNOT BE CLAIMED LATER.**
Even with `omega_b` and `n_s` freed, CAMB's `A_s` treatment and the published analysis's
marginalisations are not identical to 60's, and the published baseline likelihood is **CamSpec with
SimAll and Commander**, which neither instrument scores. So this reference is like-for-like against
**60's harness**, and is NOT a reproduction of the published `64.2` meV. Any agreement with the
published figure would be a coincidence of two different likelihoods and will be reported as such.

**⚠ COST, AND THE IDEMPOTENCY THIS CONTAINER FORCES.** Freeing two parameters multiplies the profile
cost. The driver will write **one checkpoint per grid point** and skip what already exists, so a
container restart loses at most one point — the failure mode that nearly cost `r7849` its whole run.
