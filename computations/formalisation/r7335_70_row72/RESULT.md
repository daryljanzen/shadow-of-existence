# `r7335+70.3` — RESULT: row 72 lands. Closed FRW with `a(T)` free gives `R = 6(aä + ȧ² + 1)/a²`, `Weyl² = 0`, and `a³·GB = 24ä(ȧ² + 1)` under THE connection. It is `165` lines against `170`, inside 110–260 and inside 71's band at its top, where it was placed. ⛔ Rows 59 and 62 are routed as outside the engine. ⌗ The cost that was not priced is compile time: `320 s`, against `6`–`17 s` for every earlier instance

*Registered at `PREDICTION.md` (`f6853d76`, pushed before any Lean). The probe run is filed raw beside it.
**The registration is not revised.***

## Row 72

| | registered | measured | |
|---|---|---|---|
| lines (`Inst_R72`, header to `end`) | 170, band 110–260, stop 320 | **165** | in |
| 71's 60–170 | at its top edge | **165** | in, at the top |
| of which the three-factor recipe | named as the driver | **43** (`pr3_d1`/`pr3_d2`, via `d2_of`) | — |

- **What it asserts** (`frw_closed`): `scalC = 6(AA₂ + A₁² + 1)/A²`, `weyl2C = 0` and `A³·gbC = 24A₂(A₁² + 1)`. Here
  `A = a(T)`, `A₁ = ȧ` and `A₂ = ä` at the point.
  - **These are the receipt's l.310, l.312 and l.355.**
  - The de Sitter values at l.403 follow from the first, and are not stated separately.
- **The table:** `fR` gives `R(eᵢ,eⱼ)eₖ` as `K(g_jk δ_il − g_ik δ_jl)`, with `K = ä/a` on a time pair and
  `(1 + ȧ²)/a²` on a space pair. **All 256 entries are proved equal to it.**
- **Not built** (said in the registration): the rank-2 and rank-5 jet-polynomial claims, the asymptotic series, and the
  integer checks.

## My probabilities, scored

| quantity | p | outcome |
|---|---|---|
| row 72 lands, all three claims | 0.75 | **yes** |
| inside 110–260 | 0.6 | **yes**, at 165 |
| `Weyl² = 0` closes by the table plus `field_simp; ring` with no hand-written combination | 0.6 | **yes, for the contraction.** ⚠ The TABLE needed `cos² = 1 − sin²` (`Real.cos_sq'`) on the entries where the 3-sphere's two angles meet. That is a library rewrite, not a hand-written combination, but I say it |
| no proof body opened | 0.9 | **yes** |

- ⚠ **On the decisive fraction: the table in the registration says 0.29. The same σ = 0.4 computation gives 0.28.**
  This is a rounding slip in the filed number, and it is left as filed.

## ⛔ What was not priced, and is the finding of this instance

- **Compile time.** Every earlier instance built in `6`–`17 s`. This one takes **`320 s`**, from the 256-entry table
  with THREE live coordinates.
- **The build took six attempts** of about 5 minutes each, and two of them ran to 14.
- **The one slow fix:** a table goal that `simp` had already made polynomial made `field_simp` fail with "no
  progress", which silently discarded every alternative in a `first | …` combinator built on it.
  - A one-entry reproduction found it.
  - The fix: optional steps in sequence (`try field_simp; try ring_nf; try simp only [Real.cos_sq']; try ring`).
- ⇒ **For `SEAT_BRIEF.md`:**
  1. Inside a `try first` over many goals, never begin an alternative with `field_simp`.
  2. Price compile time for any table with three live coordinates.
  3. Line count stops predicting wall-clock at that point.

## ⛔ Rows 59 and 62 — routed, not built (as registered)

- **Both are 3D on S³, non-diagonal (59) or frame-based (62), and ε-truncated at ε⁴.** About 70–80% of each file is
  rank and linear-solve content.
- **Under a 4D diagonal engine, "CHART-EXCLUDED → REOPENABLE" does not hold for them.** Reaching them is engine work,
  and it is 71's call.
- **Row 62's receipt overwrites `CHECKS[2]`** (the `R(δ) = 6` gate) at l.451. Routed to its owner, not fixed.

## Not done

- No engine proof body was read.
- `ROWS.tsv` is 71's.
- **No π_d.**
- The applier machinery stays stopped.
- The two-variable recipe stays in `SecondSeatLTB.lean` until 71 answers (`r7335` ④.2).
