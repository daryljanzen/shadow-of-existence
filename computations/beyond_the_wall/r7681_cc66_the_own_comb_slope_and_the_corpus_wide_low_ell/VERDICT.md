# `r7681` (cc66) — THE EIGHT ARMS SCORED, AGAINST THE RUNS BANKED BESIDE THIS FILE

*Registered at `r7681+cc66.0` in its own commit before a line of the computation existed. Every number
below is read off one of the `run_*.txt` files here. **Four confirmed, four falsified, and three of the
four falsifications are about the difference between a quantity and its printed digit.***

| arm | registered | measured | |
|---|---|---|---|
| ① | the **own-comb** slope survives its null, the **shared-comb** one does not | own `+0.01034` against `+0.00328`; shared `+0.02690` against `+0.03088` | ✔ |
| ② | the own-comb slope is **larger** than `r7641`'s `+0.0103`, between `+0.012` and `+0.030` | **`+0.01034`** — inside `r7641`'s own `±0.0014` | ⛔ |
| ③ | **3–6** further sentences rest on the rise, central **4** | **4** (`l.1777`, `l.1778`, two clauses at `l.2791`); none in P7 or P18 | ✔ |
| ④ | the spread's drift is the **draw count**, not the window, seeding or covariance file | the draw count is the quantity, but **nothing changed**: two commits, zero in the likelihood module | ⛔ |
| ⑤ | the drift moves neither the quartet nor either window's admissibility | both hold | ✔ |
| ⑥ | **4–7** of the seven depths move, central **6**; the three at ℓ=6–8 move **least**, under one per cent | **5** move; ℓ=6–8 move `−0.18`, `−0.05`, `−0.01` per cent | ✔ |
| ⑦ | `D_C/r_0` within one per cent of `2.774`, ℓ₂ within half a multipole of `7.8` | `+0.285` and `+0.287` per cent — **but both printed digits move** | ✔ / ⛔ |
| ⑧ | the band-RMS read reproduces 70's figures and `2/6/4`, and `l.1857` needs a **claim** change | both exactly | ✔ |

## THE FOUR FALSIFICATIONS, AND THREE OF THEM ARE ONE MISTAKE

**⛔ ⑦ twice, and ⑥'s framing.** I registered the SIZE of each geometric move and then wrote gates
asserting the PRINTED digits would hold. They are different questions. The stretch moves `0.285` per
cent and prints `2.782` against `2.774`; `ℓ₂` moves `0.287` per cent and prints `7.9` against `7.8`.
⇒ **A sub-per-cent move crosses a printed rounding boundary whenever the digit sits near one, and
nothing about the size tells you whether it does.** Both over-assertions are left in the receipt with
the reason, because the lesson is cheap to state and was not: *a gate that conflates a quantity with
its printed form asserts whichever of the two its author happened to hope for.*

**⛔ ② is the same error from the other side.** I reasoned that every arm-of-record quantity in this
family came in larger, so the own-comb slope would too. **But the own-comb statistic is the one
constructed to be insensitive to what the repoint changed** — the arms' combs parting — so its near
invariance (`+0.01002 → +0.01034`, three per cent) is not a surprise to be explained but the property
the statistic exists for. *The arm was registered against the wrong reference class: "quantities in
this family" instead of "quantities this statistic is built not to see".*

**⛔ ④ names the right quantity and the wrong story.** I registered the draw count, reasoning from a
CHANGE in it. Measured: that receipt has two commits and `computations/planck_tt_likelihood/` has had
none since the first, so no input changed at all. **The draw count is the cause because `600` was
never enough**: the fourth peak's spread runs `2.033`–`2.219` over eight seeds there, so the published
`2.19` and the live `2.03` are one measurement at two draws. ⇒ *Converged at `NMC = 10000` it is
`2.094` with a seed scatter of `0.017`, giving `± 2.27` combined.* **The honest answer to "what
changed" is "nothing, and the number was never pinned."**

## THE FINDING NO ARM REGISTERED, AND IT IS THE BEST ONE HERE

**Two of my own guards could not fail, and both were found by being asked a question they had not been
asked before.**
1. **`P15_the_band_rms_ratio…`'s live reader pointed at `/tmp/n66/r7041/inj`** — another node's
   container scratch path. It returned `None` on every CI run the receipt has ever had, so every
   figure was scored against a hardcoded fallback table. Now repointed at 70's in-repository bank.
2. **`the_skys_own_fourth_peak…`'s `"the spread does not depend on the seed"` allows 12 per cent** —
   wide enough to hold any value from `1.86` to `2.28`. It passed while the quantity it protects was
   undetermined at the precision the paper prints it to.

⇒ *Both are `r7679`'s label lesson in new clothes: there, four green gates quoted a bank they had
stopped reading; here, a reader that never ran and a bound that could not bind. **The common shape is
an assertion whose truth does not depend on the measurement it is about.***

## ONE ROUTE WITHDRAWN

`r7679+cc66.6` recommended restating `l.2790`'s `1.4` as `1.5` on the `2.21` this container drew.
**On the determined `2.27` the clause reads `3.26/2.27 = 1.44`, which prints the `1.4` already in
place.** The recommendation is withdrawn in `FOR_69.md` and in the receipt, rather than left standing.

## THE RUNS THIS IS SCORED AGAINST

| file | receipt | verdict |
|---|---|---|
| `run_phase_systematic_own_comb.txt` | `the_phase_systematic…` | GATES: ALL PASS |
| `run_stretch_refit_point.txt` | `the_background_returns_the_larger_stretch…` | ALL CHECKS PASS |
| `run_depth_gap_refit_point.txt` | `the_low_multipole_depth_gap…` | ALL CHECKS PASSED |
| `run_band_rms_arm_of_record.txt` | `the_band_rms_ratio…` | PASS |
| `run_fourth_peak_converged.txt` | `the_skys_own_fourth_peak…` | GATES: ALL PASS |
| `spread_probe.py`, `conv_probe.py` | the seed and draw-count scans item 3 rests on | — |
