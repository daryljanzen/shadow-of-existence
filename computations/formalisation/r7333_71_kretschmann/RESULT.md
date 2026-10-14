# `r7333+71.5` — RESULT: all six Kretschmann rows land, at `391` lines against `610` registered, and the stop never fires. ⌗ The general lemma came in OVER its band: `144` against `40`. It took in the second table I had priced separately for Nariai (`130`): one table, with the area profile `P` left free, carries both SdS and `dS₂ × S²`. ⛭ After it, the rows are cheap: `16`–`68` each, mean `41`. ⛔ Two rows needed a reading that I name below: row 17's point lies on a horizon, where the static chart fails. Row 110 is built through a cubic contraction I wrote in the instance file. That is a new contraction, as registered risk 1 said it might be

*Scored against `PREDICTION.md` in this directory (pushed at `r7333+71.1`, before any of the six receipts was
opened). It is not revised. ***All `23` `#print axioms` lines in the instance file rest on `[propext,
Classical.choice, Quot.sound]`, with no `sorryAx`. That covers the `10` lines that were there before, which are
unchanged, and the `13` new ones*** (`PROBE_RUN_KRETSCHMANN.txt`). `sds_kretschmann` is untouched. No `ShadowEngine` proof
body was opened. Unit: `git diff --stat` insertions.*

## ⛔ The stop, scored first

| condition | measured |
|---|---|
| one instance over `200` | ***no*** — the largest row is `68` |
| two in a row over `170` | ***no*** |

## The pieces

| order | row | what was built | predicted | measured | band `60`–`170` |
|---|---|---|---|---|---|
| 0 | — | `kG` (the general table), `RK` (THE connection's curvature, named once), `static_table`, `sin2_facts`, `static_ric`, `static_riem2` | **40** (25–80) | ***144*** | ***over*** |
| 1 | 93 | `sds_derivs`, `sds_contractions` (Ricci `= Λg`, `R = 4Λ`, `R_abR^ab = 4Λ²`), `row93_weyl_split` | **70** | ***68*** | in |
| 2 | 81 | `row81_separator` | **60** | ***16*** | under |
| 3 | 28 | `row28_curves` | **50** | ***33*** | under |
| 4 | 17 | `nariai_curvature` | **130** | ***33*** | under |
| 5 | 104 | `row104_flat_slice`, `row104_nariai_root` (and `nariai_curvature`, counted at 17) | **80** | ***36*** | under |
| 6 | 110 | `weylB`, `weyl3C`, `wT`, `row110_petrov` | **180** | ***61*** | in |
| | | ***the section's closing line*** | | ***2*** | |
| | | ***total*** | ***`610`*** | ***`393`*** (`391` attributed) | |

***Why the lemma is over, and why the total is under.***
- I registered the lemma as `kR` lifted to any `F` with `P = r²` fixed. I priced the Nariai rows as a SECOND table
  at `130`. Before writing either, I generated the table with `P` free, and it has the same `24` nonzero entries.
  So I built that one instead.
  - It costs `49` lines of proof, row 45's own proof shape. Building it took `12` minutes.
  - It made the Nariai table unnecessary: row 17 is `33` lines, not `130`.
  - Lemma plus row 17 registered `170`; they measured `177`.
- The lemma also carries the Ricci contraction (`static_ric`) and a general `K` (`static_riem2`). The registered
  `40` did not include them. Every row after it reads its numbers off those two.
- ***So "over" here names the driver: I widened the lemma's scope, and the widening is what the rows saved.***
  - The registered model priced the general step too cheaply and the rows too dearly.
  - Its total was too high by `217`.

## What each row proves, and the caveats beside the score

*Every theorem is stated for profiles `F`, `P`, `S` that are smooth and nowhere zero and equal to the named
functions NEAR THE POINT. This is the convention, and `exists_global_profile` proves such profiles exist.*

- ***Row 93 (`row93_weyl_split`).*** For SdS with `Λ = 3/α²`, under THE connection:
  - `C_abcd C^abcd = 48M²/r⁶` (`weyl2C`, the engine's contraction);
  - `K − C² = 24/α⁴`, the `Λ`-only part.

  *The receipt's ratio at the forced mass is arithmetic on these two values, and it is not restated.*
- ***Row 81 (`row81_separator`).*** SdS is Einstein:
  - `R_ab = (3/α²) g_ab` component by component;
  - `R_ab R^ab = 36/α⁴`, which is mass-free;
  - `K = 48M²/r⁶ + 24/α⁴`, with `∂_M = 96M/r⁶`.

  *The `M`-derivative is taken of the closed form at fixed `r`, not across a family of metrics.*
- ***Row 28 (`row28_curves`).*** Schwarzschild, `Λ = 0`.
  - On the cycloid `r = M(1 + cos z)`: `K = 48/(M⁴(1 + cos z)⁶)`, which carries `M`.
  - On the bead: `K = 12/(α⁴ sinh⁴(3s/2α))`. On the receipt's own small-`s` form: `K = 64/(27 s⁴)`. Both are free of `M`.

  *The bead is stated as `r³ = 2Mα² sinh²(3s/2α)`. For `r > 0` this is equivalent to the receipt's
  `r = (2Mα²)^{1/3} sinh^{2/3}(3s/2α)`, and it keeps `rpow` out of the proof.*
- ***Row 17 (`nariai_curvature`).*** ⛔ ***The receipt does not do what its one-line stand-in suggested.***
  - It evaluates SdS's `K` at the Nariai values `M = α/3√3`, `r = α/√3`, and gets `72/α⁴`.
  - At that point `f(r) = 0`, a double root. So `F` cannot be nowhere zero near the point, and the static chart
    does not reach it. It is the same degeneracy the chart clause excluded, but at the point itself rather than
    away from it.
  - ***What is built*** is `K = 8Λ² = 72/α⁴` on the Nariai geometry itself, `dS₂ × S²`. That is
    `−(1 − Λx²)dt² + dx²/(1 − Λx²) + Λ⁻¹dΩ²`, with `Ricci = Λg`. It is mass-free at every point of it.
  - Separately, `sds_kretschmann` gives the SdS value at every point off the horizon.
  - ***Not built:*** the limit of SdS's `K` as `r → r_N`, and the identification of `dS₂ × S²` as SdS's
    near-horizon limit. *The number matches. The two statements are not the receipt's single substitution.*
- ***Row 104*** takes the receipt's three checks in turn.
  - ***Check ① (`row104_flat_slice`):*** every Riemann component of `−dt² + dr² + r²dΩ²` is `0` under THE connection.
    - *The engine is 4D. The receipt's claim is that the 3-metric `dr² + r²dΩ²` is flat. That is the same
      statement, because the 3-metric is a totally geodesic leaf of a static product. The 3D form is not stated
      directly.*
    - *The receipt does not check that SdS's constant-`τ` slice has this metric, and neither do I. That is
      foliation work, on `70`'s side of the split.*
  - ***Check ② (`row104_nariai_root`):*** at `M = ρ/3`, `Λ = 1/ρ²`:
    - `f(ρ) = f′(ρ) = 0`;
    - `f″(ρ) = −2Λ`;
    - `2/ρ² = 2Λ`;
    - `−2/f″ = 1/Λ`.

    This is calculus on `f` and needs no connection.
  - ***Check ③*** is `nariai_curvature`: both radii² equal `1/Λ`, as `Ricci = Λg`. The receipt's third check, the
    SdS `K`, is row 45's `sds_kretschmann`.
- ***Row 110 (`row110_petrov`).*** For SdS, for every `M` and `Λ`:
  - `C² = 48M²/r⁶`;
  - `C_ab^cd C_cd^ef C_ef^ab = 96M³/r⁹`;
  - so `(C²)³ = 12(C³)²`, which is `I³ = 27J²` with `I = C²/16`, `J = −C³/96`.

  The caveats, said plainly:
  1. ***Registered risk 1 came true in part.*** The engine has no cubic contraction.
     - I wrote the Weyl tensor as a bivector map (`weylB`, the 4D trace-removal formula) and `weyl3C` in the
       instance file: `12` lines, outside the engine.
     - That `weylB`'s square trace equals the engine's `weyl2C` was checked symbolically (sympy, generic
       `F`, `P`), not in Lean. The theorem uses `weyl2C` for `C²` and `weylB` only for `C³`.
  2. ***This is the REAL part of the Petrov condition only.***
     - In general `I` and `J` are complex. Their imaginary parts (`C·*C` and the dual cubic) need the Levi-Civita
       volume form, which is a library gap in `ROWS.tsv`.
     - For a static metric they vanish by time-reversal parity. That is argued, not proved.
     - The receipt itself computes `I` and `J` from `Ψ₂ = −M/r³` and never from the metric.
  3. The dictionary `I = C²/16`, `J = −C³/96` for real `Ψ₂` is stated in the docstring and not proved.

## The probabilities

| quantity | p | outcome |
|---|---|---|
| the general lemma lands in `25`–`80` | 0.7 | ***no*** — `144`, for the reason above |
| rows 93, 81, 28 each land under `100` | 0.65 | ***yes*** — `68`, `16`, `33` |
| all six land without the stop firing | 0.5 | ***yes*** |
| row 110 is built (not reported as needing a new contraction) | 0.5 | ***built, WITH a new contraction*** written in the instance file. *Scored as "yes, built"; the contraction is named above so it can be scored otherwise* |
| the mean of the landed rows is under `110` | 0.6 | ***yes*** — `41.2` |

## Beside the score

1. ***Build time.***
   - The whole instance file now builds in `5m31s` wall time (`15m16s` CPU), against `5m14s` before.
   - `static_table`, at `256` cases with `P` free, is the slow part: `12` minutes wall time when elaborated alone in a
     scratch file.
   - The rows built against it in about a minute in total.
2. ***Commits.***
   - `+71.2` adds `146` lines: the `144` attributed to the lemma plus the section's two closing lines.
   - `+71.3` adds `186` lines, rows 93, 81, 28, 17 and 104. `+71.4` adds `61` lines, row 110.
   - The intermediate states are prefixes of the final file. They were built as part of the full run, not one by one.
3. ***CI.*** On PR #422, "the runner-read sweep, on what this push deleted or renamed" is red. It is red on main's
   own head (`53b0944`) too, and this branch deletes or renames nothing. I commented once on the PR.
4. ***The registration's table promised a second table for 17 and 104.*** None was needed. Risk 2 ("17 and 104 may
   share less") did not arise: they share `nariai_curvature`.
5. *Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
