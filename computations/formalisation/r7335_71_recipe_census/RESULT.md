# `r7335+71.4` — RESULT: ***YES, `ShadowEngine` takes the two-variable recipe***, restated for ANY coordinate pair `(i, j)` and third coordinate `l`, at `106` lines (band 50–120). No existing axiom line changes. ⌗ The row that needs it is the closed `S³` slicing: `a(t)² sin²χ sin²θ` is `h(t, χ)·k(θ)`. ⌗ The census: `14` rows to DONE and row 17 to a half, so DONE `24 → 38`, halves `5 → 6`, reopenable `18 → 3`. I predicted `39` and `5`, and named row 17 as the one that would be argued

*Scored against `PREDICTION.md` in this directory (pushed at `r7335+71.1`, before `70`'s recipe, RESULT or
instance files were opened). It is not revised.*

## ③ The decision, in one line

> ***`ShadowEngine` takes it: `tw_d1`/`tw_d2`/`twp_d1`/`twp_d2` in section `TwoVarRecipe`, general in `i`, `j`, `l`.
> `70`'s `tv_*` copy in `SecondSeatLTB.lean` stays where it is, under its own names, and still builds.***

| registered condition | outcome |
|---|---|
| 1. a row still open needs it | ***yes.*** The closed-slicing halves (rows 0, 2, 3, 4, 5) have `g_φφ = a(t)² sin²χ sin²θ` in `(t, χ, θ, φ)`. That is `h(y⁰, y¹)·k(y²)`, which `pr_d*` does not cover: it multiplies two one-coordinate profiles, not three. |
| 2. its clean form is general | ***no, as offered, so restated.*** `70`'s form is fixed at `(0, 1)` and coordinate `2`, through `pr01`. The engine's form takes `prP i j` and a free `l`. Each proof is `70`'s, with `pr01` replaced by `prP i j`. |
| 3. nothing that exists changes | ***yes.*** See the build below. |

***So it moved in the re-stated form the registration provided for.*** *The new names (`prP`, `eTV`, `d1H`, `d2H`,
`tw_*`, `twp_*`) were chosen to avoid `70`'s (`pr01`, `e01`, `d1h`, `d2h`, `tv_*`, `tvp_*`). This is the `cT`
collision from `70`'s friction (ii), avoided before it happened.*

## The build

| check | measured |
|---|---|
| `lake build ShadowEngine` | ***exit 0, `1m43s`*** (registered: under `3` minutes, p `0.85`) |
| engine `#print axioms` lines | ***`125`***: the `121` before, each still `[propext, Classical.choice, Quot.sound]`, and `4` new ones the same |
| the five files importing the engine, rebuilt against it | ***all exit 0, `33` axiom lines all standard*** (`PROBE_RUN_DOWNSTREAM.txt`): `CurvatureInstances` `307 s`; `70`'s four files `5`–`14 s`, `SecondSeatLTB` included |

## The predictions, scored

| quantity | prediction | measured | |
|---|---|---|---|
| the answer | YES (p `0.7`) | ***YES*** | as predicted |
| the row that needs it | the closed-slicing halves (p `0.6`) | ***the closed-slicing halves*** | as predicted |
| lines added to the engine | `80` (50–120) | ***`106`*** | in, above central |
| existing axiom lines changed | `0` (p `0.9`) | ***`0`*** | as predicted |
| `ShadowEngine` under `3` minutes | p `0.85` | ***`1m43s`*** | yes |
| rows moved to DONE | `15` | ***`14` + `1` half*** | off by row 17, the one named in advance |
| DONE after | `39` | ***`38`*** | |
| halves after | `5` | ***`6`*** | |
| reopenable after | `3` | ***`3`*** | exact |
| all fifteen move whole | p `0.8` | ***no:*** row 17 is a half | |

***Why `106` and not `80`.*** I priced `70`'s `100` lines less its row-13 specifics.
- There were no row-13 specifics inside the recipe. The coefficients `cLT` come after it.
- Generality added the `i`, `j`, `l` arguments to every statement and a `prP_split` in place of `pr01_split`.
- ***The model's error:*** I assumed the offered `100` included instance code. It did not.

## ④ The census

- ***Moved to DONE (`14`):*** 45, 93, 81, 28, 104, 110 (by 71) and 47, 102, 94, 48, 49, 51, 54, 13 (by 70).
- ***To DONE (chartable half) (`1`):*** 17.
  - Its RESULT built `K = 72/α⁴` on `dS₂ × S²`.
  - The receipt's own computation, SdS's `K` AT the horizon point, needs a chart through the horizon or a limit.
  - That half is named in the row.
- ***Kept DONE whole, with the caveat in the row:***
  - 110, real invariants only. The receipt's own `Ψ₂` is real, and the dual parts are a library gap, written in
    the row.
  - 104, the 3D flatness via the flat 4D static metric.
- ***The convention, written once at the foot of `ROWS.tsv`:***
  - a DONE row names the closing seat, the revision, the RESULT and the theorems;
  - the form is the same whichever seat closed it;
  - only 71 edits the file, and other seats route their changes to it.
- `CANDIDATES.md` gets an appended note. `SEAT_BRIEF.md` gets `70`'s three frictions and the two new tools,
  appended and credited.

## Beside the score

1. ***Still open on the reopened block:***
   - rows 59, 62 and 72;
   - the closed-slicing halves of 0, 2, 3, 4 and 5;
   - row 79's static-leaf half.

   Nothing is started: `r7335` ⑤ orders nothing new.
2. *Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
