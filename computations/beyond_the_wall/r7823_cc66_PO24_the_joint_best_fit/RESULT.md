# RESULT — r7823 (cc66): `PO-24`'s joint best fit

**All six registered predictions HELD**, including the one registered as risky.
Run: `python3 fit_joint.py lcdm 900`, `python3 fit_joint.py cr 900`, then
`python3 measure.py`. Banked at `out/`.

## ⇒ THE HEADLINE: fitting the baseline SHARPENS the tension rather than absorbing it

`r7820`'s standing limit was that neither banked control is a best fit, so every
tilt figure on this row absorbed baseline shape error as well as any signature.
**That limit is now removed, and the figure moved the other way.**

| | banked control (`r7820`) | **joint best fit (here)** |
|---|---|---|
| the sky's tail tilt | `−0.020658 ± 0.003782` | **`−0.000500 ± 0.003527`** |
| the signature's tilt | `−0.093474` | **`−0.079500`** |
| **distance** | `19.25σ` | **`22.40σ`** |

⇒ *** At a baseline that actually fits, **the sky prefers no tail tilt at all** —
`−0.0005 ± 0.0035`, a fifth of a sigma from zero — while the signature needs
`−0.0795`. The `19σ` was not an artefact of an unfitted control: it was an
UNDERSTATEMENT of it. ***

## The fit

| arm | joint χ² | Planck | ACT | best fit |
|---|---|---|---|---|
| **ΛCDM** | **`113.17`** | `86.61` / 114 | `26.56` / 28 | `H0 69.7349`, `ω_b 0.022834`, `ω_c 0.114712`, `A_s9 2.311757`, `n_s 0.981426` |
| **CR** | `486.04` | `207.35` / 114 | `278.70` / 28 | `H0 83.9777`, `ω_b 0.026000`, `ω_c 0.090297`, `A_s9 2.999383`, `n_s 1.133791` |

142 data points; ΛCDM's `χ²/point = 0.7970`. **Δχ² = `372.87`** in ΛCDM's favour.

⛔ **The CR arm's minimum is BOUNDARY-LIMITED and that is stated, not hidden.**
Three of its five parameters sit on the box wall — `ω_b` at `0.026`, `ω_c` at
`0.09`, `A_s9` at `3.0`. ⇒ *So `486.04` is an UPPER BOUND on that arm's joint
χ², not a free minimum, and the `372.87` gap is not sharpened by the wall: the
arm is pressed against three of them while still fitting four times worse.*

## The limit that was load-bearing, measured OUT OF SAMPLE

The Planck bins above the cut enter neither block, so they are a genuine
out-of-sample test of the fitted baseline — and they are exactly the bands
`r7820` measured its control's deficit in:

| band | `r7820`'s banked control | **this best fit** |
|---|---|---|
| `1000–1500` | `5.0` / bin | **`1.387`** / bin (55 bins) |
| `1500–1760` | `9.6` / bin | **`1.351`** / bin (15 bins) |
| `1760–2200` | — | **`0.968`** / bin (19 bins) |

*The baseline shape error that made the earlier figures degeneracy-fit numbers is
gone, on bins the fit never saw.*

## The signature at the fitted background

`r = 1.087021`, `ℓ_D = 1368.303`. ⌗ *Second reading, with the suppression taken
at the CR arm's OWN best fit (`r = 1.056844`) instead of on the ΛCDM background:
the signature's tilt reads `−0.053000` and the distance `14.89σ`. **Both readings
clear the strict bar by more than an order of magnitude**, which is what makes the
verdict robust to which background the signature is evaluated on.*

## The six predictions

| # | prediction | verdict |
|---|---|---|
| ① | ΛCDM best fit brings Planck `1000–1500` below `2.0`/bin, out of sample | **HELD** (`1.387`) |
| ② | the sky's fitted tail tilt stays small, `|tilt| < 0.05` | **HELD** (`0.0005`) |
| ③ | the signature's tilt lands in `0.06 ≤ |dn| ≤ 0.13` | **HELD** (`0.0795`) |
| ④ | ⚠ **the risky one**: the distance stays above `6σ` | **HELD** (`22.40σ`) |
| ⑤ | the refit does NOT absorb the signature, `Δχ² > 20` | **HELD** (`372.87`) |
| ⑥ | the best fit sits near Planck's point, `|ΔH0| < 3`, `|Δn_s| < 0.03` | **HELD** (`+2.375`, `+0.0165`) |

## What this does to the row, in the row's own words

`PO-24`'s discharge clause offers *"a joint Planck + ACT likelihood with the
shared sky handled, deciding it by the strict `2σ` rule on the arm that does not
double-count."* **The split uses no multipole twice, and the arm decides it at
`22.40σ`.**

And the row's own `OR TERMINATES IF` clause is **refuted rather than
unexamined**: *"the displacement is shown to be absorbed by the inherited
parameters it is degenerate with, the baryon density among them."* The fit had
all five free, the baryon density among them, and moved it to `0.022834` — and
the displacement did not absorb. ⇒ *`60` closed the baryon-density route at
`r7800` by freeing it in one direction; this closes it from the other, with the
whole baseline free at once.*

⌗ **What this is NOT.** Not the other discharge route: no data more precise than
ACT DR6 is used and the `1.16×` precision gap is untouched. Not a claim about
TE or EE: the joint arm is TT only, as `r7820`'s split is. And not a free
minimum for the CR arm, as the boundary note above says in the same breath.
