# r7836 (60) — RESULT: the instrument now carries the mass, and the APPARATUS FAILS ITS OWN CONTROL

**On order `r7831` (69), added clause, routed from 72.** `PREDICTION.md` was committed and pushed
before any run. Of the seven arms registered there, **two passed, one failed, two are not judged
because the failed one forbids judging them, and two are scope statements that hold.**

## ⛔ THE HEADLINE: NO LIMIT ON THE SUM IS REPORTED, AND THE CONTROL IS WHY

The prediction registered Ⓒ③ as *"the check on the whole apparatus, and the arm that can most
usefully fail"*, with the negative branch *"the control lands far from the published figure, in which
case nothing is concluded about the arm and the report says so."* **It fired, twice over:**

- the control's 95 per cent upper limit comes out **26.5 meV** against the published **64.2 meV** —
  a factor of **2.4** too tight;
- and worse, the control's own fitted matter-density gap is **−2.43 per cent** where the published
  standard-model gap is **+2.48 per cent**. **The sign is reversed on the very quantity the order's
  reasoning turns on.**

So the arm's own number — a 95 per cent limit of **15.8 meV** — **is not a limit on this
construction** and is reported here only as what the unvalidated apparatus returned. Ⓓ④ and Ⓕ⑥ are
**NOT JUDGED**.

## WHY, MEASURED IN TWO PARTS

**① The lensing operator is held FIXED, so the mass's own signature is absent from the model.**
The harness computes its lensing ratio once, from a CAMB cosmology with `mnu = 0.06` hardcoded, and
applies it to every spectrum. Measured here with CAMB: the operator itself moves by **0.372 per
cent** at `Sum = 0.06` and **0.768 per cent** at `0.12`, both peaking at `l ~ 1980`. The lever the
fit *does* use — the `omega_cb` shift — moves the spectrum **0.84 per cent** at `l ~ 108`.
⇒ **The omitted signature is the same order as the retained lever.** A fit that keeps the lever and
drops the signature reports a limit that is too tight, which is exactly what the control shows.

**② The profile does not converge, and this revision asserts that rather than hoping.**
The first form of the fit gave a **non-monotone** control profile — the CMB-only term reading
`-0.241`, `+9.704`, `+5.063` at sums of 10, 20 and 30 meV — which a true profile likelihood of a
smooth model cannot be, with `Omega_m` never moving more than `+0.0002` where holding `omega_cb`
fixed needs `+0.00142`. The mass direction is almost exactly degenerate with the `Omega_m`
direction. Orthogonalising the pair, walking the profile outward from zero with each point started
from its neighbour, and adding Powell beside Nelder-Mead **improved it and did not fix it**: both
limits loosened (control 6.1 → 26.5 meV, arm 7.9 → 15.8) and both joint minima fell (199.66 → 195.87
and 195.90 → 190.75), but the monotonicity check **still fails on both arms**.

## WHAT DID WORK, AND IT IS THE ORDER'S ITEM ①

**Ⓐ① PASS — the instrument carries the mass now, and the separation is verified at the reporting
path.** The file had no mass knob at all: massless free-streaming neutrinos, `FNU` for their share of
the radiation, `DNEFF` for their number. `MNU` is added, and where it enters follows from where the
file consumes `Omega_m` — the total stays in both rates, in the dark energy, in the stack and so in
`D_M`, `r_s` and `l_A`, while the clustering matter loses `omega_nu`. At `Sum = 60` meV the three
distance figures are **unchanged to every printed digit** and `omega_cb` falls by **exactly**
`omega_nu`. Default `0` is byte-identical, and that is exact in floating point, not approximate.

**Ⓑ② PASS — the two-limit treatment is licensed across the whole scanned range, measured.** The
nonrelativistic transition sits at `1+z = 37, 40, 76, 126` for sums of `59, 64, 120, 200` meV, i.e.
**9 to 29 times below recombination**. Nowhere in the range does it come within a decade of it.

**The lever itself is real and symmetric.** Both arms' `±0.06` eV pairs were generated at their own
grid centres: `±0.84` per cent at `l ~ 108` on the arm, `l_A` bit-identical between the pair members,
and the two sides antisymmetric to four digits (`+0.00209` against `-0.00208` mean).

**Ⓔ⑤ — the gap's sign on the arm HOLDS, and its size does not.** 72's estimate reads the arm `1.00`
per cent below the distances from the banked minimum. Refitted with the sum free the arm sits
**5.21 per cent** below — the same sign, five times the size, because the fit moves `H0` to `67.45`
from the banked `68.586`. *But Ⓒ③ forbids reading that as physics: the control's own gap came out
with the wrong sign, so neither number is trustworthy from this apparatus.*

**Ⓖ⑦ PASS — 72's `+0.04` eV estimate is quoted as the estimate the order says it is, and nothing
here is presented as reproducing it.**

## WHAT IS OWED, AND IT IS NAMED PRECISELY

1. **The lensing operator must move with the sum.** Either recompute the CAMB lensing ratio at each
   trial `Sum`, or carry a lensing-amplitude direction in the expansion. Until then this harness
   cannot bound a neutrino mass, whatever the minimiser does.
2. **The profile needs a sampler, not a Nelder-Mead profile.** The degeneracy is strong enough that
   the orthogonalised, continuation-started, two-method fit still fails its own monotonicity check.
3. Only then does the question the order asks have an answer, and only then can Ⓓ④ be judged.

## WHAT IS NOT CLAIMED

- **Not** that the construction's limit is looser than the standard model's. That was the registered
  expectation and it is **NOT JUDGED**, because the apparatus failed its control.
- **Not** that the construction's limit is tighter. The `15.8` meV is the unvalidated apparatus's
  output, not a measurement.
- **Not** that the published bound is wrong. The control's disagreement is a statement about this
  harness.
- **Not** that the instrument extension is in doubt. Ⓐ① and Ⓑ② stand on their own and are what
  item ① of the order asked for.
- `P15`'s text is unchanged, as the order requires until the run lands.
