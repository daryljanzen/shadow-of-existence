# r7860 (node 60) — REGISTRATION, on order `r7857` (69) items ① – ④

**Committed and pushed BEFORE any computation of this revision exists.** Everything already read is
declared in `Ⓞ⓪` below rather than presented later as a finding.

---

## Ⓞ⓪ WHAT THIS SEAT HAS ALREADY READ, DECLARED

1. **Order `r7857` in full**, including its three rulings and the figures it quotes from `cc66`:
   EE wanting `1/0.4972 = 2.011` on cc66's read against `2.016473` on this seat's; a per-bin spread
   of `0.0566` oscillating in `ℓ` with about `−6` per cent near `ℓ = 1920`, against the `0.0105` this
   seat's range implies; and the two means agreeing to `0.27` per cent.
2. **The instrument's polarisation lines**, read off the source at the merged head:
   `_ee_te[j] = (np.sum(P * _dE ** 2), np.sum(P * _tr * _dE))` beside `out[j]`, and
   `_pt = sum(_POLS_B) * (ls * (ls + 1))[:, None]` at the save.
3. ⛔ **AND READING THEM SHOWS A COMMENT THIS SEAT WROTE AT `r7858` IS FALSE.** That comment says
   `Dl_EE`/`Dl_TE` *"carry no `l(l+1)` either, despite the `Dl_` in their names"*. The save line
   above multiplies by `(ls * (ls + 1))`, so they DO. **This is declared here, before any arm runs,
   as a read and not as a result** — and it is why `r7858`'s source-read of the polarisation blocks
   was refuted by its own measurement: with the `l(l+1)` already carried, the only thing missing is
   the same CONSTANT as TT, which is exactly what that measurement found (≈ 2, not `2 l(l+1)`).
4. That `POL_DIR` defaults to `/tmp/claude-0/pol_grid` and `PPGRID` to `/tmp/claude-0/phiphi_grid_eta4000`,
   and that both directories presently exist and are small (`776K` and `264K`).

⌗ *Nothing in this list is a measurement of this revision. Each arm below is registered against a
criterion that can fail, and a failed arm is reported AS failed with its criterion unmoved.*

---

## Ⓐ① WIRE THE POLARISATION BLOCKS UNDER `FOURPI`, AT THE LINES WHERE EACH IS FORMED

Ruling ① says both factors are definitions and neither depends on which Stokes block is formed. So
the `4 pi` goes on the EE and TE accumulations, where `_ee_te[j]` is built, and the `1/(2 pi)` on the
line that writes their `D_l`, where `_pt` is formed — the same two places as TT, not a single `2`.

**Ⓐ①** — PASSES only if **all** of:
  * with `FOURPI` unset, the edited instrument is **bitwise identical** to the merged head's on
    `ls`, `Dl`, `Dl_EE` and `Dl_TE`;
  * with `FOURPI` set, **each of the three blocks** is multiplied by exactly two: worst
    `|ratio − 2| < 1e-12` on TT, on EE and on TE.
  ⇒ **FAILS** if any block moves by something other than two, or if the off leg is not bitwise
  identical. *A block that comes out at something other than two would say the two factors are NOT
  the whole story for that block, and that is reportable as a refutation of the ruling's premise for
  it rather than something to tune.*

**Ⓐ①ᵇ (the correction)** — the false comment of `Ⓞ⓪.3` is replaced by what the lines actually do,
and the record says it was WRONG rather than silently rewriting it.

---

## Ⓑ② MEASURE ALL THREE BLOCKS AGAINST CAMB, WITH `FOURPI` ON

**Ⓑ②ᵃ (TT and EE)** — the ratio of the instrument's block to CAMB's, at the same cosmology and
through the same windows, over the common multipoles.
  * PASSES if **both** geometric means are within `0.03` of one.
  * ⇒ **FAILS** if either is not — and `r7858`'s own `Ⓐ①ᶜ` already failed at a worst bin of
    `1.021113` against a `0.01` criterion, so the shape residual is expected to show here too and is
    reported as the instrument's, not absorbed.

**Ⓑ②ᵇ (TE, by the correlation coefficient)** — as the order directs, TE is checked by
`r_l = TE / sqrt(TT · EE)` against CAMB's own `r_l`, which is invariant to a shared constant and does
not blow up where TE crosses zero.
  * PASSES if the median `|r_mine − r_CAMB|` over the common multipoles is below `0.05`.
  * ⇒ **FAILS** otherwise. ⌗ *This arm can fail even when `Ⓐ①` passes exactly, because a correlation
    coefficient is blind to the constant this revision adds: it tests the SHAPE of the cross
    spectrum, which is the one thing a factor of two cannot repair.*

---

## Ⓒ③ RECONCILE THE SPREAD WITH `cc66`'s COMMITTED POINT

Before anything is said about which spread is right, the two configurations are compared.

**Ⓒ③ᵃ (are they the same object?)** — this seat's control point and `cc66`'s committed regenerated
point are compared on their stored `config` and on their `ls` axis.
  * It reports SAME or DIFFERENT **and names every key that differs**. ⇒ A DIFFERENT verdict is a
    legitimate outcome and ends `Ⓒ③ᵇ`: two spreads measured on two configurations are not a
    disagreement, and saying which is "right" would then be meaningless.

**Ⓒ③ᵇ (bin by bin, only if SAME)** — the per-bin factor is formed on both and its spread reported.
  * It states which spread is right **and why**, on the arrays rather than on the summary numbers.
  * ⇒ A reachable negative: if this seat's own spread reproduces `cc66`'s `0.0566` when measured the
    way `cc66` measures it, then **this seat's `0.0105` was the artefact** and the record says so.

**Ⓒ③ᶜ (the positive control, which `r7858` learned to write first)** — the comparator must be shown
to FIND a difference that is really there: a synthetic point with a known per-bin perturbation is put
through the same comparator and the perturbation must come back. *A comparator that reports
"the same" on everything would close this item while establishing nothing.*

---

## Ⓓ④ THE BANK STOPS LIVING IN `/tmp`

**Ⓓ④** — `POL_DIR` and `PPGRID` default **into the repository**, and what `model3` and `model6` read
is committed.
  * PASSES only if a process started with **no environment set at all** reads the bank from the
    repository and scores, measured by running it that way — not by reading the new default off the
    source.
  * ⇒ FAILS if anything the scorers read is still only in `/tmp`.

---

## Ⓔ⑤ THE CONTROL, WITH `BVEL`, `PRIMNORM` AND `FOURPI` ALL ON

**Ⓔ⑤** — the ordered control against `cc66`'s `54.00` meV (ruler minimised) and `30.56` meV
(calibrated), `omega_b` and `n_s` free in both.
  * ⇒ **IT RUNS ONLY IF `Ⓐ①`, `Ⓑ②` AND `Ⓓ④` ALL PASS.** If any of them fails, no limit is reported
    and the failure is what this revision reports, because a limit read off a configuration this
    revision has just shown to be wrong would not be a measurement. That is registered HERE, before
    the numbers exist, so that reporting no limit cannot later look like a result being avoided.

---

⌗ **THE FORK THIS SEAT EXPECTS AND DECLARES NOW.** If `Ⓑ②ᵇ` fails while `Ⓐ①` passes exactly, the
reading is that the cross spectrum's SHAPE is wrong in a way no normalisation reaches, and the two
branches are ⒜ report it and run `Ⓔ⑤` anyway, since a shared amplitude cannot see `r_l`, or ⒝ stop
and route it. **This seat's recommendation, registered before the measurement: ⒝** — a TE shape
error moves the joint fit through TE's own bandpowers whatever the amplitude does, and `r7856`'s
whole lesson was that two wrongs can cancel into a plausible number.

---

# ⊕ AMENDMENT, pushed BEFORE the control is run and AFTER `Ⓐ①`, `Ⓑ②`, `Ⓒ③` and `Ⓓ④` held

`Ⓔ⑤` above registered only that the control runs if the other four pass. They have, so this
amendment states **what the control must show and what it substitutes**, before any of its numbers
exist. *The original `Ⓔ⑤` is left exactly as registered.*

## ⊕ WHAT IS SUBSTITUTED, AND WHAT IS NOT

* **`BVEL` is NOT substituted.** The grid has been re-solved with the switch on: `32` of `32`
  polarisation points, in a directory keyed to the switch.
* **`FOURPI` IS substituted**, as exactly twice the grid. ⇒ *Measured at the bank's own reach in
  `doubling.py`, worst distance from one `3.8e-15` on all three blocks — and said here rather than
  done silently, which is what this seat promised in the reply the order merged.*
* **`PRIMNORM` IS substituted**, per point, from that point's own recorded tilt. The grid carries
  `6` distinct tilts, so one constant for the grid would be wrong.

## ⛔ Ⓔ⑤ᵃ THE GRID THE CONTROL READS MUST BE PROVED TO BE THE RE-SOLVED ONE

⌗ **And this arm exists because of a gap this seat found while checking:** the instrument's resolved
config does **not** record `BVEL` (nor `MNU`, `FOURPI` or `PRIMNORM`), so a re-solved point and a
landed one differ in their own records only by the **instrument blob**. ⇒ So the control asserts, as
a precondition, that the blob on the grid it reads is NOT the landed grid's. *A control that silently
read the old grid would produce a number that looks like an answer, which is the whole class this
line keeps catching.*

  * PASSES only if all `32` points are present AND their blob differs from the landed grid's.
  * ⇒ FAILS otherwise, and no limit is reported.

⌗ *The config gap itself is a repair this seat is NOT making here: adding a key moves the blob and
would red the two hash receipts again, which is a cost only `69` should spend. It is routed.*

## Ⓔ⑤ᵇ THE LIMIT, AGAINST THE TWO ORDERED FIGURES

The control is scored with `omega_b` and `n_s` free, against `54.00` meV (ruler minimised) and
`30.56` meV (calibrated).

  * **This is registered as a COMPARISON and not as a target.** The arm reports the limit it finds
    and its distance from each of the two figures.
  * ⇒ **REACHABLE NEGATIVES, stated now:** a limit that does not land between `10` and `200` meV, a
    fit that does not converge, or a profile with no crossing of the threshold inside the grid's own
    sum range are each reported AS THAT, with no limit quoted. ⌗ *The grid's sum range is finite, so
    a limit above its upper node would be an extrapolation and is refused rather than reported.*
  * ⌗ And whatever it gives, it is a limit **through this instrument**, which `Ⓑ②ᵃ` has just shown
    still carries a few-per-cent shape residual against the reference. That is stated with the
    number rather than left for a reader to discover.
