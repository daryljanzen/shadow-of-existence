# `r7365+71.2` — the census at the campaign's edge, the survival rate over the whole run, and a re-run of every DONE row from what is committed. ⌗ DONE `51`, chartable halves `6`, ENGINE-REACHABLE `0`, REOPENABLE `0` rows plus one half (79), generic-metric `2`, no-connection `32`, real end `20`. ⌗ Survival `14` of `21` (`0.67`), unchanged since `r7351`, because campaigns 7–13 registered no new pre-opening readings. ⌗ Re-run: `50` of `57` DONE rows re-run clean from HEAD, `0` fail, and `7` cite no declaration and are claims until named. ⌗ Of `r7325`'s `24` reopenable units, `20` are DONE, so the second seat should be priced against `≈ 3`, not `24`

*Answers `FOR_71.md` §`r7355` ②–③ and §`r7365` ②–③. Campaign 13 closed the last halves the block named, so this is
taken at the campaign's edge, as ② asks.*

## ① The census, in the standing state's form

| status | rows | which |
|---|---|---|
| ***DONE*** | ***`51`*** | |
| ***DONE (chartable half)*** | ***`6`*** | 7, 17, 35, 59, 79, 108 |
| ENGINE-REACHABLE | `0` | |
| REOPENABLE | `0` rows, plus one half | row 79's half: SdS's static `S²` leaves, by the near-point convention |
| GENERIC-METRIC IDENTITY | `2` | 20, 62. Both are REPORTED as not pointwise identities |
| NO-CONNECTION, NOT DONE | `32` | |
| ***the real end*** | ***`20`*** | `17` library gaps, plus `3` global `S³` (65, 66, 67) |
| **total** | **`111`** | |

*Source: `r7325_71_inventory/ROWS.tsv` at this commit, counted by its status column. The register's copy is
`r7345`'s: DONE `43` plus `7` halves.*

***The six open halves, each with its obstruction named:***
- ***79:*** SdS's `S²` leaves. Reachable by the near-point convention. ***One small campaign.***
- ***17:*** the Kretschmann scalar AT the Nariai horizon point `r_N`, where `f = 0` and the static chart fails.
  Reachable in a horizon-crossing chart such as Eddington–Finkelstein: non-diagonal but nondegenerate at `f = 0`,
  which is the non-diagonal engine's case. ***One campaign.***
- ***35:*** Tangherlini–de Sitter for every `D`. The engine is over `Fin n`, but a table indexed by coordinate class
  rather than by number is owed. ***Engineering, one to two campaigns.***
- ***7:*** the receipt's count claims (Killing vectors buy a count, the shear count is the gap). Not a pointwise
  identity.
- ***59:*** the `S³` harmonics, integrals and ranks. GLOBAL on `S³`, in the real-end class.
- ***108:*** a nonexistence argument (no static spherically symmetric hypersurface of `dS₅` induces SdS at
  `M ≠ 0`). Not a pointwise curvature claim.

## ② `r7325`'s `24`-unit reopening: where it stands — what the second seat is priced against

`r7325+71.3` named `24` reopenable row-units. Their status now, read mechanically from `ROWS.tsv` then and now:

| now | units |
|---|---|
| ***DONE*** | ***`20`*** (0, 2, 3, 4, 5, 13, 28, 45, 47, 48, 49, 51, 54, 72, 81, 93, 94, 102, 104, 110) |
| DONE (chartable half) | `2` (17, 59) |
| reclassified GENERIC-METRIC | `1` (62: a jet-space rank, not a pointwise identity) |
| untouched | `1` (79's half) |

- ***Still reachable:*** about ***`3` units*** (79, 17 and 35 above). That is two to four campaigns of this seat's
  measured size.
- ***My reading for the decision, not a ruling:*** a second formalisation seat priced against the `24`-unit reopening
  would be priced against work that is `20/24` done. The remainder is about `3` units, which this seat can carry in
  its current cadence.
- ***The cutoff caveat is closed once for all of them:*** `exists_global_profile` (engine) builds the global profile
  the near-point convention assumes.

## ③ The pre-opening survival rate, over the whole run

| block | readings registered before opening | survived | expected (per-row p) |
|---|---|---|---|
| `r7327`–`r7339` (measured at `r7341`) | 12 | 9 | — (priced after) |
| campaign 5 (`r7341`) | 3 | 2 | 1.9 |
| campaign 6 (`r7351`) | 6 | 3 | 3.6 |
| campaigns 7–13 (`r7353`) | ***0*** | — | — |
| ***whole run*** | ***21*** | ***14*** | |

- ***Rate: `14` of `21`, `0.67`***, against `9` of `12` (`0.75`) when the register last carried it.
- ***Why it has not moved since `r7351`:*** campaigns 7 to 13 opened rows already read (58, 6, 19, 83), or read their
  receipts before registering, so no reading was made blind.
  - This is a property of where the line is: the rows left are rows I have opened.
  - It is not a gap in the scoring.
- ***Is the per-row forward price holding?*** Over the two priced campaigns, expected `5.5` and observed `5`.
  - ***It holds within one row, with a slight optimism.***
  - The `7` misses of the whole run share ONE shape: the stand-in names an object or a construction, and the receipt
    evaluates it on a different metric, chart or point, or proves the construction fails.
  - A per-row `p` that discounts stand-ins naming a construction, as campaign 5's did, is what kept the forward
    price within a row.
- ***For the second seat:*** the remaining reachable units (79, 17, 35) have all been opened. A new seat would make
  readings only on rows it opens fresh, and the line has none left that are reachable.

## ④ Every campaign's result re-run from what is committed (`r7365` ③)

***The instrument:*** `computations/formalisation/rerun_census.py`, committed at `r7365+71.1` BEFORE its measurement.
- ***Its selector, the population, is stated in the script and is mechanical.*** Every `theorem`/`lemma` that a DONE
  row's text cites by name (rule 1), or that sits in the section the source names for that row (rule 2). That
  section is `section Inst_R<row>`, or `section SweepB<k>` where a committed run record's header reads
  "B<k> (row <row>)".
- ***Its measurement:*** each file holding a selected declaration is rebuilt at HEAD with `#print axioms` appended
  for every selected name. The probe copies are temporary, so no committed file is touched.
- ***The record:*** `RERUN_CENSUS.txt` beside this file.

***The result:***

| | count |
|---|---|
| DONE rows (whole or chartable half) | `57` |
| ***re-run CLEAN from HEAD*** (every cited declaration's axiom line inside `[propext, Classical.choice, Quot.sound]`) | ***`50`*** |
| not clean | ***`0`*** |
| ***unresolved*** — the row's text names no declaration at HEAD | ***`7`***: 29, 41, 42, 43, 77, 92 ("discharged before B, r7297 C1–C5 and earlier") and 74 ("discharged by the engine, E3/E4") |

- `297` axiom lines in all, across `17` files (`ShadowEngine.lean` and `16` probes, `70`'s four `SecondSeat*` files
  among them). All are CLEAN. Exit `0` and zero error lines on every file.

***The finding about the records, which is what `cc66`'s rule is for:***
1. ***Seven DONE rows are claims, not re-runnable facts, until their census text names the theorems.***
   - Their theorems exist, but the census points at a cycle ("C1–C5") and not at a declaration.
   - The repair is to name them in the row's text, after which this script checks them. That is a census-text change
     in its own push, with the re-run beside it. It is not done here, so this measurement stays clean.
2. ***The pre-`r7327` run records name a file that no longer exists at HEAD.***
   - `probes/CurvatureProbe.lean` was split into `ShadowEngine.lean` and `probes/CurvatureInstances.lean` at
     `r7327+71.4`.
   - Those records re-run only at their own commit. Their theorems re-run at HEAD through this script.
3. ***Run records state wall times of one machine.*** Following `60`'s rule, `RERUN_CENSUS.txt` PRINTS the toolchain
   and the wall times and asserts nothing of them.
   - What is pinned is `lean/lean-toolchain` (`v4.35.0-rc4`) and `lean/lake-manifest.json` (mathlib
     `4e6064a4…`), both committed.
   - The compile-time figures in earlier RESULT files are measurements of this container class, not re-runnable
     facts. They are said to be that here.
4. ***Generated tables*** (`NonDiag.lean`'s `D1L`/`D2L`/`GamL`/`RicL`, `FRWk.lean`'s `fRk`) came from sympy scripts that
   are not committed. ***This does not affect re-running:*** every entry is CHECKED by Lean against the metric, so the
   proof is self-certifying without the generator. The generator is the selector of nothing.

*The record's header gives the tree commit as `b4eb552ae`. The run started from that tree, before
`rerun_census.py` was committed at `b30f3211c`. No Lean file differs between the two.*

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
