# r7466 — REGISTERED BEFORE MEASUREMENT

**THE ORDER.** `r7465` puts this seat on `PO-87` and says to work it as physics.

**THE QUESTION, IN THE CODE SEAT'S OWN WORDS** (`FOR_CC66.md`, left open on purpose):
*"The next question is **which quantity carries a running phase at correct spacing**, and you have
already named the two candidates."*

**WHY A NEW STATISTIC AND NOT A NEW SPECTRUM.** Two banked receipts close the free-period route and
both name the same shortfall. The period offset **is** a phase drift — a period of `312` and
`ℓ_A = 298` with a phase running linearly in `ℓ` are the *same two-dimensional model*, identical
residual sum of squares to `0`, so the offset is a drift of `−96.6°` across `104 ≤ ℓ ≤ 1886` and an
identity rather than a fit preference. And the free-period **slope** cannot say which term carries
it, because `n_s` — a primordial tilt with no acoustic phase in it — moves that statistic as much as
`ω_b` does. ⇒ **The owed object is a statistic that is a phase observable, measured on the bank.**

**THE STATISTIC.** The **per-peak** phase `φ_n = ℓ_n/ℓ_A − n` over the banked peak series, and its
**slope `s` in `n`** by least squares. It is built from peak POSITIONS and not from a
one-amplitude-fitted residual, which is the property the free-period slope lacked. The peak finder
is **imported** from `r7201`'s `analyse_ten.py` — `r7445`'s rule: a reimplementation of a predicate
is a second instrument and it will disagree.

**THE TARGET.** `−96.6°` is `0.2683` cycles across `Δℓ = 1782`; at `ℓ_A = 301.4` that range is
`5.912` peaks, so the drift the model would have to acquire is
**`|Δs| = 0.0454` cycles per peak.** ⌗ *Sign convention is derived in the run and not asserted here.*

---

## ⌈ Ⓓ WHAT I ALREADY KNOW, READ BEFORE THIS FILE WAS WRITTEN — NOT SCORED

**Ⓓ①** The two receipts' results: arm period `311.79 ± 2.99`, control `334.65 ± 35.52`, the ordered
difference `0.97σ` and not significant *because the control has no measurable period*; against
`ℓ_A = 298` (known to `0.15` per cent) the arm is `+14.00` at `4.69σ`; the `PART F` identity; the
second-harmonic artefact check leaving it at `4.90σ`.

**Ⓓ②** That the free-period slope fails as a phase observable, `n_s` moving it as much as `ω_b` at
every degree of marginalisation that leaves the statistic intact, `n_s` changing sign through zero at
degree `4`; and that the receipt's own prescription is *"it needs a grid, and it also needs a
different statistic."*

**Ⓓ③** The bank: two nine-run direction grids (`H0`, `OM`, `NS`, `WB`, each side, both arms, both
grids), the driving-off pair, and the `RBFAC` loading lever — `0.1`, `0.5`, `1.5` on the `CR` arm,
`0.1`, `0.5` on the control, `1.0` being the grids' own base. **`RBFAC` scales the baryon loading
ONLY**, which is the clean lever the earlier receipt recorded as *not* banked; it is banked now.

**Ⓓ④** `cc66.156`'s mean-phase numbers as `r7201`'s analysis prints them: `CR` `φ` running
`−0.21732 → −0.20124 → −0.19131` across `RBFAC = 0.1, 1.0, 1.5`, so `dφ/dlnRB = +0.01642`; and the
driving lever `dφ = +0.12589` on REMOVAL. **So on the MEAN phase the driving is `7.7×` the loading.**

**Ⓓ⑤** The printed gap series in units of `ℓ_A`. For `cr_base` it is `1.004, 0.895, 1.036, 0.980`.
⇒ **I therefore already know the per-peak phase increments are NOT monotone**: they are
`+0.004, −0.105, +0.036, −0.020`, dominated by one large negative step at the second gap, summing to
`−0.085` over four steps. **That a straight line in `n` may fit this badly is known before measuring
and is not scored as a finding.** What is NOT known is the slope's uncertainty, whether the tilt
moves it, and whether any lever reaches the target.

⌊

---

## ⌈ THE ARMS — registered now, each a number

**Ⓐ THE TILT CONTROL, WHICH IS THE WHOLE POINT.** `|Δs|` across the `NS` pair against `|Δs|` across
the `WB` pair, both grids, `CR` arm.
⇒ **PREDICT: the tilt moves `s` by less than one third of what `WB` does** — the new statistic is
more of a phase observable than the old one. *If it moves it as much, the statistic has failed in the
same way and that is the result.*

**Ⓑ THE CLEAN LOADING RESPONSE.** `ds/dlnRB` by central difference over `RBFAC = 0.5 → 1.5`, `CR`.
⇒ **PREDICT: non-zero and NEGATIVE, of order `0.01` cycles per peak per `ln RBFAC`** — more loading
delays the peaks progressively, which runs the phase down.

**Ⓒ THE DRIVING RESPONSE.** `Δs` on removing the driving, `CR` and control.
⇒ **PREDICT: larger in magnitude than the loading's by a factor between `3` and `20`**, by analogy
with the mean phase's `7.7×`, and **the same sign in both arms.**

**Ⓔ THE REACH.** The fractional shift each lever needs to supply `|Δs| = 0.0454`.
⇒ **PREDICT: NO single banked lever reaches it inside a shift the banked constraints allow** — the
peaks are reproduced within a grid step and `ℓ_A` to `0.15` per cent, so a lever that also moves
`ℓ_A` is spent before it reaches the target. **The loading alone needs more than a factor `2` in
`RBFAC`.**

**Ⓕ THE LINEARITY.** The straight-line fit's own quality on five peaks, reported as the residual
scatter about the line against the slope's own standard error.
⇒ **PREDICT: the fit is POOR — scatter at least `2×` the slope's standard error — because the second
gap dominates (`Ⓓ⑤`), so a linear `s` is a summary of a non-linear run and must be reported as one.**

**Ⓖ THE RESOLUTION, which is the honest cost statement.** The slope's standard error from the peak
positions' own spread against the target `0.0454`.
⇒ **PREDICT: the standard error is of the SAME ORDER as the target, so five peaks cannot settle the
carrier and the measured cost of settling it is more peaks** — which is the grid the earlier receipt
asked for, now priced rather than guessed.

⌊

---

## ⌈ THE CONTROLS — any one firing VOIDS the run

**Ⓥ① INSTRUMENT IDENTITY.** The imported peak finder must reproduce `r7201`'s printed `CR` base mean
phase `−0.20124` and alternation `+0.01511`, and `ℓ_A = 301.380`, to the digits printed.
**If it does not, this is a second instrument and the run is VOID.**

**Ⓥ② NOT BLIND TO A KNOWN PHASE CHANGE.** Removing the driving must move `s` by more than its own
standard error. **A statistic that cannot see the driving cannot attribute the drift, and the run is
VOID** — the failure `PO-56` was struck on, one level down.

**Ⓥ③ NO AMPLITUDE CONTAMINATION.** `s` recomputed with the global de-tilt turned OFF must agree with
the de-tilted `s` to within its standard error, because a global power law carries no phase.
**If the de-tilt moves `s`, the statistic is reading amplitude shape as phase — the exact defect that
sank the free-period slope — and the run is VOID.**

⌊

---

*⌗ **No new spectrum is run and none is refitted.** Everything is read off the bank. ⌗ `PO-87`'s
fourth-peak half is **data-gated** and is not touched: nothing below is reported against the
fourth-peak datum. ⌗ **The row is the register's**: whatever this returns is supplied, not applied.*
