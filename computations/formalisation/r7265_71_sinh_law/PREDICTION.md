# `r7265+71.1` — PRE-REGISTRATION: the `sinh^{2/3}` law against Physlib's `FirstOrderFriedmann`, the path-scoped CI job, and the run record

*Committed and pushed before the Physlib project is created, before Physlib is fetched or built, and before
the workflow file is written. The order is `FOR_71.md` §`r7265`.*

## ① The law

*The statement, fixed now.* The flat Λ + dust scale factor, with `A > 0`, `Λ > 0`, `c > 0`, `G > 0` and
`t > 0`, is

    a(t) = A · sinh^{2/3}( (3/2) · √(Λ/3) · c · t ),
    ρ(t) = (Λ c² / (8πG)) · A³ / a(t)³          (pressureless: ρ ∝ a⁻³).

**L1:** `FirstOrderFriedmann a ρ 0 Λ G c t` — Physlib's own definition at `b0e7ca1c`, imported, not copied.

**L2 (secondary):** `SecondOrderFriedmann a ρ 0 Λ G c t` (`p = 0`), same `a` and `ρ`.

| claim | L1 | L2 |
|---|---|---|
| **states** — the theorem statement elaborates against Physlib's definitions | **0.95** | 0.95 |
| **compiles** — `lake build` accepts the file, proofs included or `sorry` | **0.9** | 0.9 |
| **proves** — no `sorryAx` in `#print axioms` | **0.75** | **0.5** |

*If a proof needs a lemma that `mathlib` does not have, the lemma is named in the result, and no `sorry` stands
in for it.* The derivative of `sinh^{2/3}` on `t > 0` (a real power of a positive function) is where I expect
the work to be. `Real.rpow`'s `HasDerivAt` lemmas exist, so I expect the work to be bookkeeping, not a missing
lemma.

### ⛔ The reachable negative, and where I think its inference does not go through — stated BEFORE the run

*The order: if L1 proves with no new foundation and no `sorry`, then "statement discipline" was the wrong frame,
and the 82 per cent is a fact about the geometric receipts specifically.*

**My prediction: L1 proves (0.75).** *And I pre-register now that, if it does, I will argue the negative does
not fire on its own terms.* The reason:

- `FirstOrderFriedmann` is itself the Einstein equations reduced to a scale factor. In Physlib the metric it is
  the reduction of is `def FLRW : Type := sorry`. *So L1 is the coordinate shadow of a geometric theorem* ("the
  FLRW metric with this `a`, with dust and Λ, solves Einstein's equations"), and that theorem is not statable
  there.
- That is the I20 pattern again, inside another project's library. **A proof of L1 would confirm the frame,
  not overturn it: the shadow proves and the theorem it stands for still cannot be stated.**
- The result will say which of the two readings the run supports. If my argument is wrong, I will say so.

| quantity | central | band |
|---|---|---|
| Physlib, its pinned mathlib (`d13f23b`) and toolchain (`v4.34.1`) fetched and built far enough to import `Physlib.Cosmology.FLRW.Basic` | **yes, 0.8** | — |
| Physlib modules built from source (Physlib ships no cache I expect `lake` to fetch) | **~40** | 10–150 |

## ② The path-scoped CI job

*A separate workflow file, so `gates.yml` is not touched:* `.github/workflows/formalisation.yml`. It triggers on
`push` and `pull_request` with `paths: computations/formalisation/lean*/**`. It installs `elan`, runs
`lake exe cache get`, builds, and runs `check_no_sorry.py`, timing each step into the log.

| runner time on the first push | central | band |
|---|---|---|
| whole job, mathlib project only | **6 min** | 3–15 min |
| … of which `lake exe cache get` | **3 min** | 1–8 min |

*The placement is decided from the measured number after the first push, as ratified. If the job exceeds 15
minutes, it moves to a schedule and stays out of the per-push path.*

## ③ The run record

The raw `lake build` output, `check_no_sorry.py`'s full stdout, `lean --version`, and the mathlib (and Physlib)
SHAs, committed as `RUN_RECORD.txt` beside each `RESULT.md`. *Re-run for `r7263`'s project, so its record is a
run and not a reconstruction.* No prediction: it is a record.
