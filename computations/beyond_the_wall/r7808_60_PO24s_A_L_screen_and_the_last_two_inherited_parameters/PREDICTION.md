# r7808 (60) — PO-24's A_L screen and fit, and whether τ and ω_m need banks at all

**Order `r7807` (69).** Screen the lensing amplitude on the post-tilt residual; fit it if the screen
leaves room; judge any excursion against the `A_L` the corpus carries, and if `P15` or `P16` carries
none, say so and use Planck's. Then say, from the screen and the physics, whether `τ` or `ω_m` needs
a bank — and if neither does, the inherited-parameter route to terminating `PO-24` is fully closed.

---

## ⌗ FOUR THINGS ESTABLISHED BEFORE REGISTERING

**① THE CORPUS CARRIES NO `A_L`, AND I SAY SO RATHER THAN SUPPLYING ONE.** `P16` has no lensing
amplitude anywhere. `P15` contains the phrase exactly twice: once in the `sec:coherence` sentence
`r7806` wrote, naming it as not yet computed, and once **disclaiming** that a procedure measures
one — *"rather than measuring a lensing amplitude"*. Three `1.07`-shaped figures elsewhere in `P15`
are a lobe ratio, a band ratio and a sigma count, none of them an `A_L`. ⇒ **There is no corpus
value and no corpus precision for this parameter**, so the order's fallback applies.

**② AND "PLANCK'S `A_L`" IS ITSELF SEVERAL NUMBERS, which is `r7806`'s lesson again.** The value
depends on the data combination, and they disagree by more than their errors:

| combination | `A_L` | from unity |
|---|---|---|
| **`TT`+lowE** | **`1.243 ± 0.096`** | `2.5σ` |
| `TT,TE,EE`+lowE | `1.180 ± 0.065` | `2.8σ` |
| `TT,TE,EE`+lowE (CamSpec) | `1.149 ± 0.072` | — |
| PR4/NPIPE `TTTEEE`+lowE (CamSpec) | `1.095 ± 0.056` | — |

**The referent is decided by the metric, not by which is the headline.** This harness scores against
**`plik_lite` `TT` bandpowers** — temperature alone. So the like-for-like constraint is the
**`TT`+lowE** one, `1.243 ± 0.096`, and that is what the excursion is judged against. The joint
`TT,TE,EE`+lowE value is reported beside it because it is the headline, and the excursion is reported
absolutely as well. **A disjunction beats a pin.**

⌗ *This matters more than a referent usually does, because Planck's `A_L` is not centred on unity.*
The datum itself prefers more lensing than ΛCDM predicts — the lensing anomaly — so the question
"is the excursion affordable" is being asked against a constraint that is both **the widest of the
four** (`7.7 %` against `N_eff`'s `5.7`, `ω_b`'s `0.65`, `Y_He`'s `0.6`) **and offset from one**.

**③ THE BANK IS BUILT DIFFERENTLY FROM THE OTHER THREE, and two consequences follow.** It is not a
re-run of the instrument: it is *"CAMB's lensing operator (`lensed_cls`, `TT`) applied to the
instrument's unlensed control"*, with a tail above `ℓ = 1996` taken from CAMB's unlensed `TT` scaled
at the join.
- **The grid is `0.8 … 1.2`, and `A_L = 0.00` is in the file as the unlensed input for reference.**
  It is **not** a grid point, and including it would both distort a monotone spline across the
  `0.0 → 0.8` gap and move the centre. The grid is taken from the config's own `ALENS` list.
- **The lensing potential is a different cosmology from the arm**: `H0 = 67.410309`, `Ω_m = 0.309826`,
  `n_s = 0.954248`, against the construction's `68.6` and `0.2973`. So this response is a ΛCDM
  stand-in for the lensing operator and **not the construction's own lensing**, which is a declared
  limit on every number below and not a defect of the bank.

**④ `τ` IS NOT A CANDIDATE AT ALL IN THIS METRIC, AND IT IS A DERIVATION RATHER THAN A JUDGEMENT.**
Above the reionisation bump, `τ` enters `TT` as the single factor `e^{−2τ}` on all scales. This
harness already marginalises one overall amplitude analytically at every evaluation. So `τ` is
**exactly** the amplitude that is already free — measured before registering: refitting the one
amplitude after an `e^{−2Δτ}` rescaling returns a residual `χ²` of order `10^{−26}` and recovers
`A = e^{+2Δτ}` to six decimals, at `Δτ = 0.01, 0.02, 0.05`. ⇒ **`τ` cannot absorb anything the
amplitude is not already absorbing, so it needs no bank** — and Ⓔ⑤ asserts that rather than
asserting a preference.

---

## THE ARMS, AS COMPARISONS WITH REACHABLE NEGATIVES

**Ⓐ① THE BANK IS WHAT IT IS REPORTED TO BE, AND THE REFERENCE ENTRY IS EXCLUDED.** `ℓ_A`, `r_s`, `D_M`
identical across the grid; the grid read from the config's `ALENS` and equal to `0.8 … 1.2` with
centre `1.0`; the `A_L = 0` entry present and **not** in the interpolation grid; the response a few
parts in a thousand, oscillating, changing sign near `ℓ ≈ 1600`.
*Negative: any acoustic quantity moves, or the sign change is absent ⇒ the bank is not the
peak-phase-like direction the order describes and the screen is measuring something else.*

**Ⓑ② THE REFERENT IS ESTABLISHED, NOT ASSUMED.** The corpus's silence on `A_L` is asserted by
locating the two phrase sites and showing neither supplies a value; the `TT`-only choice is asserted
against the metric this harness actually uses.
*Negative: the corpus does carry an `A_L` somewhere I did not find ⇒ it becomes the primary referent
and Planck's becomes the secondary.*

**Ⓒ③ THE SCREEN, RUN FIRST, ON `r7804`'s MEASURE.** `corr(A_L direction, post-tilt residual)` on all
three windows, and the share of the signature the direction removes, beside `Y_He`'s `53.5/32.3/10.5`,
`ω_b`'s `3.3/5.7/20.0` and `N_eff`'s `0.1/0.2/1.9`.
*Both branches registered. Small overlap ⇒ refused on SHAPE, back to the `ω_b`/`N_eff` pattern and
not `Y_He`'s. Large overlap ⇒ `A_L` is the second candidate the screen admits, and with the widest
room of the four it would be the best chance of CLOSING the row — which is the outcome that would
make this revision the one that terminates `PO-24`.*

**Ⓓ④ THE FIT, RUN IF THE SCREEN LEAVES ROOM, AS THE ORDER SAYS.** Tilt + `A_L` free together, twelve
starts: surviving displacement, absorbed share, and the `A_L` wanted, judged against the `TT`+lowE
constraint, the joint one, and absolutely.
*Negative: the displacement does not survive ⇒ `PO-24`'s clause IS met here and the row closes.*

**Ⓔ⑤ `τ` NEEDS NO BANK, AND THE REASON IS AN EXACT DEGENERACY RATHER THAN AN ESTIMATE.** The
`e^{−2τ}` rescaling is shown to be absorbed by the harness's own amplitude to machine precision on
every window, with the recovered amplitude equal to `e^{+2Δτ}`.
*Negative: the residual after refitting the amplitude is not at machine zero ⇒ `τ` has `TT` shape
this harness does not already free, and it DOES need a bank.*

**Ⓕ⑥ `ω_m` IS THE ONE THAT STILL NEEDS ONE, AND THE REASON IS NAMED BEFORE IT IS ASSERTED.** It is
the only remaining candidate that moves the **acoustic scale** — every parameter banked so far
leaves `ℓ_A`, `r_s` and `D_M` untouched, which is asserted from the three banks themselves. So no
argument from the existing banks covers it, and the screen cannot stand in for one.
*Negative: `ω_m`'s effect in the fitted window is also exhausted by the tilt and the amplitude
⇒ it needs no bank either, and the inherited route closes completely here.*

**Ⓖ⑦ NO PRINTED NUMBER DEPENDS ON WHICH START WINS**, bounded by the last decimal each printed
quantity is set in type — `r7804`'s form, not an absolute epsilon.

**Ⓗ⑧ THE FIT IS INSIDE THE BANK**, not at its edge, on every window.
*Negative: at an edge ⇒ that row is an extrapolation, reported as a bound with its direction
established, exactly as `r7806`'s Ⓗ⑧ required when it fired.*

---

**ARM COUNT: 8** — Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥ Ⓖ⑦ Ⓗ⑧. Asserted at the end of the receipt.
**Failed arms are reported AS failed. No criterion here is rewritten after measurement.**
**Figures the paper prints from this receipt are pinned in it, as inline comparisons.**
**I am never a subject.**
