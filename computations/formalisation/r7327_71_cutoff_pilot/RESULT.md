# `r7327+71.5` — RESULT: all three steps land in the order's sequence. The cutoff lemma comes in at `63` lines (band 50–130) and closes B's near-the-point caveat once, as a theorem. ⛭ The `S²` pilot lands: row 45, the SdS Kretschmann scalar, at `149` lines for the instance (band 100–220, stop `250`), plus a `44`-line coordinate recipe every reopened row reuses. ⌗ The split adds about `24` new lines, and all `131` axiom lines are identical across it. ***The reopening is no longer a reading. The second seat can be started.***

*Scored against `PREDICTION.md` in this directory (pushed at `r7327+71.1`, before row 45's receipt was opened and
before any Lean). It is not revised. ***All `131` `#print axioms` lines rest on `[propext, Classical.choice,
Quot.sound]`, and there is no `sorryAx`.*** Unit: `git diff --stat` insertions, one commit per step.*

## ⛔ The stop, scored first

| condition | measured |
|---|---|
| the pilot over `250` | ***no*** — `149` (the instance), `193` with the recipe |

***The pilot did not fail, so the expected failure point did not arise.*** I named it in advance: the profile's
`θ`-dependence through E5. What actually took the iterations was something else:
- mathlib's combinators return function-algebra forms (`k ∘ (fun f => f i)`, `f − g`, `F⁻¹`), which do not match
  pointwise lambdas until stated with `show`;
- `field_simp` closes many table goals by itself, so `field_simp; ring` inside a `try` silently reverts them;
- `field_simp` cannot clear `3r − Λr³ − 6M` (`3r·f(r)`) unless the contraction is closed with `F` kept abstract and
  `f` substituted afterwards.

***None of the three is about `θ`.*** *The angular profile entered the table only through one combination,
`Q = (4F₀S₀² + 2S₀S₂ − S₁²)/(4S₀²)`. With `S = sin²θ`, it is `F₀ − 1` by plain algebra: `cos θ` cancels with no trig
identity.*

## The steps

| step | predicted | measured | |
|---|---|---|---|
| ① cutoff lemma (`exists_global_profile`, `exists_global_family`) | 80 (50–130) | ***63*** | in |
| ② the pilot, row 45 (`sds_kretschmann`) | 150 (100–220) | ***149*** | in |
| ② the coordinate recipe (`co_d1`, `co_d2`, `pr_d1`, `pr_d2`), reusable | — (inside ② in the model) | ***44*** | ② in all is `193`, still in |
| ③ the split | ≤ 40 new lines; no axiom line changes | ***≈ 24 new*** (661 inserted, 637 moved); ***131 axiom lines identical*** | in |
| ③ an instance file builds in under 2 minutes | — | ***6.5 s for row 79; 4m16 for E3 + row 52*** | ***half right*** |

***The build-time line, said plainly:*** importing `ShadowEngine` costs about `6` seconds. An instance file then
builds in its own proof time: seconds for a connection or Einstein-component row, minutes for a row with a `256`-case
component table (E3, row 45). *I registered "under `2` minutes" without separating the two. It holds for the second
seat's rows (Einstein components and foliations) and fails for mine (the Kretschmann tables).*

## The probabilities

| quantity | p | outcome |
|---|---|---|
| the cutoff lemma lands in `50`–`130` | 0.7 | ***yes*** |
| the pilot lands at all | 0.85 | ***yes*** |
| the pilot lands in `100`–`220` | 0.6 | ***yes*** |
| the stop fires | 0.1 | ***no*** |
| the split adds `≤ 40` new lines and changes no axiom line | 0.8 | ***yes*** |

## What the pilot proves

```
theorem sds_kretschmann (M Λ : ℝ) (p : Fin 4 → ℝ)
    (eF : F =ᶠ[𝓝 (p 1)] fun s => 1 - 2 * M * s⁻¹ - Λ / 3 * s ^ 2) (eP : P =ᶠ[𝓝 (p 1)] fun s => s ^ 2)
    (eS : S =ᶠ[𝓝 (p 2)] fun s => Real.sin s ^ 2) :
    riem2C (g at p) (THE connection's curvature on basis fields at p) = 48 * M ^ 2 / p 1 ^ 6 + 8 * Λ ^ 2 / 3
```

- `F`, `P` and `S` are smooth and nowhere zero, which is what `diag4` needs. `exists_global_profile` shows that such
  profiles exist at every point with `r ≠ 0`, `f(r) ≠ 0` and `sin θ ≠ 0`.
- `r ≠ 0`, `f(r) ≠ 0` and `sin θ ≠ 0` are not hypotheses. They follow from `P`, `F` and `S` being nowhere zero.
- ***The intermediate general result*** (the table `kR`) holds for ANY static metric `diag(−F, 1/F, r², r²S)`, with `F` and `S`
  arbitrary.
  It is `K = F″² + 4F′²/r² + 4(F − 1)²/r⁴` once `S = sin²θ`, so rows 17, 81, 93 and 110 (Nariai, SdS) start from it.

## Beside the score

1. ***`CANDIDATES.md` is corrected*** by an appended note (`r7327` ④.4): the 18 rows and 6 halves are candidates
   again. The exclusions of 35, 83 (dimension) and 65, 66, 67 (global on `S³`) stand.
2. ***`SEAT_BRIEF.md`*** in this directory is the second seat's starting page: its rows, the interface, the recipe as
   row 45 ran it, the two traps above, and the price.
3. ***The split changed the file layout.*** `CurvatureProbe.lean` is now `ShadowEngine.lean`, a second `lean_lib` in
   `lakefile.toml`, plus `probes/CurvatureInstances.lean`. The default target (`ShadowFormal`) and CI's
   `check_no_sorry` are untouched.
4. *Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
