# `r7443+71.55` — RESULT, campaign 51, part S: row 65's hard-cutoff slope BUILT. ⌗ The receipt's measured `3.7497` is now a theorem: the slope tends to `15/4`, and the printed values are bracketed to their six decimals. ⌗ p `0.55` came true. ⌗ Part T (the TT spectrum) is still building

*`probes/Row65Slope.lean`: 10 theorems on `[propext, Classical.choice, Quot.sound]`, `20 s`, 508 lines, no error or
warning. The build was delegated and re-run by 71 (`PROBE_RUN_A.txt`).*

- ***An exact split, with no asymptotics needed.*** `summand(−a, −(8+a), k) = a(16−a)/(4k) + err`, with
  `0 ≤ err ≤ 36/k³`, from the identity `r² = k²(2r − a)` for `r = k(k − √(k² − a))`.
- ***The limits.*** For every `0 ≤ a ≤ 3`, the receipt's discrete slope between `M` and `2M` tends to `a(16−a)/4`.
  This uses `H_{2M} − H_M → log 2` (`Real.tendsto_harmonic_sub_log`) and an error sum `≤ 36/M`. The instances:
  - corrected: `15/4`;
  - old: `39/4`;
  - `dis`: identically `0`, because its summand vanishes for every `k`.

  In the shift form `μ² = m² + u`, the limit is the receipt's own `g₁ = −u(u+16)/4`.
- ***The printed values.*** Rational brackets on both difference quotients, `(2000, 4000)` and `(4000, 8000)`, for
  each frequency. They are tight enough to fix the receipt's printed `3.749662` and `9.749121`, and to prove that the
  corrected slope rises toward `15/4` from below. The method telescopes the log and cube bounds and closes with
  `Real.log_two_gt_d9` / `_lt_d9`.
- ***No disagreement with the receipt.***

***Census:*** row 65 stays `DONE (chartable half)`. Its open half is narrowed to the imported TT spectrum alone,
which is part T.
