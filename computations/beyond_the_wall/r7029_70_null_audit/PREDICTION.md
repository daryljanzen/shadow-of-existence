# r7029 item two — an independent audit of `cc66.64`'s comb null: PRE-REGISTRATION

*Node 70. Committed before any of the audit's nulls were computed. The audit script is committed after
this file.*

## What was already in hand when this was written, declared rather than tabled as open

These facts come from the instrument and the bins on disk. None of them is an amplitude this audit computes.

- **`cc66.64`'s receipt was re-run here and reproduces exactly:** a comb amplitude of 7.3038 at period 1.00,
  a null over 110 wrong periods with **mean 2.5279** and **max 5.5613**, and the scan's peak at 1.01.
  ⇒ *The quoted "null of 2.53" is the **mean** of the 110.*
- **The scan's resolution.** The 82 bins of bands 4–7 span q = 2.971–5.747, so T = 2.776. They are uniformly
  spaced at 0.0298, with one gap of 0.0564. The frequency resolution is 1/T = 0.360 per unit q. The scan
  covers frequencies 0.513–1.818, which is **about 3.6 independent frequencies**. The window excluded around
  the comb, |P − 1| ≤ 0.15, is 0.307 wide in frequency, **narrower than one resolution element.**
- **The bin Nyquist period** is about 0.06, far below the scan's lowest period of 0.55.
- **The band edges are at a 0.70 period**, which lies inside the null range.

⇒ So the first branch of question 1 is partly settled already. The 110 wrong periods are not 110 independent
draws, and the ones nearest the exclusion zone are not independent of period 1.00 at all. What stays open is
how much this matters, measured.

## The four questions, and what will be computed for each

**Q1. Is the period grid free of aliasing against the comb period and the band edges?**
- (a) The effective number of independent periods in the null, `N_eff`, measured from the correlation of
  `A(P)` across the grid under white noise sampled at the 82 real bin positions.
- (b) The leakage from period 1.00 into the null: under white noise, the fraction of the 110 null periods whose
  amplitude correlates with `A(1.00)` above 0.5.
- (c) Band-edge aliasing: the amplitude that a pure band-edge pattern projects at period 1.00. The pattern is a
  step train, and separately a per-band constant, at the 0.70 edges, sampled at the real bins and detrended as
  the receipt detrends.

**Q2. Is 110 enough, and is the null level the right statistic?**
- Answered from Q1(a) and from the ensembles below. The mean of a wrong-period scan is a *level*, not a
  significance. The statistic that belongs in its place is a tail probability from an ensemble of independent
  realisations, quoted with that ensemble named.

**Q3. Does the signal survive a differently constructed null?** Three nulls, each recomputing the receipt's
own `amp(1.00)` on the receipt's own detrended per-bin excess:
- (i) **Circular shift** of the detrended excess over bin index, all 81 non-zero shifts, with the q positions
  held fixed.
- (ii) **Phase randomisation**, 1,000 surrogates. ⚠ Stated before running: a phase-randomised surrogate keeps
  the periodogram. It cannot remove power concentrated at one frequency, so it is expected to be the wrong null
  for a periodicity question. If the surrogates return amplitudes near 7.30, that is a finding about the null's
  construction and **not** evidence for the comb.
- (iii) **Instrument noise, through the whole estimator.** The data is replaced by the control's fitted shape
  plus a draw from `N(0, COV)`, the likelihood's own covariance. The per-bin excess is rebuilt through the
  receipt's own `shape_fit`/`perbin`, then detrended and projected at period 1.00. 2,000 draws.
  *This asks whether noise, multiplied through a d that is itself a comb, can produce 7.30 at period 1.00.
  That is exactly the artefact the wrong-period null cannot see.*

**Q4. Does the five-sixths attribution survive?** The cross term `−2dᵀFr_c` (6.24) and the quadratic term
`dᵀFd` (1.08) are each set against nulls (i) and (iii) separately. The quadratic term has no noise in it, so
under (iii) it is a constant. That will be stated, not hidden.

## Outcome table, the one that costs `cc66.64` most tabled FIRST

| outcome | what it would mean for `cc66.64`'s null |
|---|---|
| **the comb does NOT survive null (iii)**: p > 0.01 | the 110-period null overstated the comb; reported to 66 for routing to cc66 |
| survives (iii) but NOT (i) | the result depends on the null's construction; reported with both |
| survives (i) and (iii) | the construction was loose but the conclusion holds against independent nulls |
| (ii) returns ≈ 7.30 | phase randomisation is confirmed as the wrong null for this question; not held against the comb |

**Decision thresholds, fixed now:**
- "Survives" means p ≤ 0.01 under (iii), with 2,000 draws.
- Under (i) it means no more than 1 of the 81 shifts returns ≥ 7.30.
- The attribution survives if the cross term's exceedance probability under (iii) is ≤ 0.01 **and** the cross
  term exceeds the quadratic term by more than 4× (the receipt's own gate) in the median of (iii).

## ⛔ NOT CLAIMED, whatever the outcome

- No verdict on whether the modulation is physical.
- No mechanism, no channel, no scoring.
- No re-run of `cc66`'s receipt beyond reproducing its printed numbers, and no edit to it.
- If a null is found wrong, it is reported to 66 for routing, and not corrected here.
