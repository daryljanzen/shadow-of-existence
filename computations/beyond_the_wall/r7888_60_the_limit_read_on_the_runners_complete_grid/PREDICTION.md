---
kind: PREDICTION
revision: r7888+60
order: r7885 (69) item ②
status: REGISTERED BEFORE THE LIMIT READ
---

# r7888 — REGISTERED BEFORE ANY LIMIT NUMBER IS SEEN

Order `r7885` (69) item ②: *"When the points land on the ref, read the control's limits on the closed
envelope as registered, against `cc66`'s `54.00` meV (ruler minimised) and `30.56` meV
(calibrated)."* They have landed. `refs/ci/r7884_phiphi` is at `133e612fe` and carries all ten
points, from `70`'s run `46016816497` at `46f824c2feba`.

⛔ **This file is committed and pushed BEFORE `limits_nuhier.py` is run on that grid.** The fork it
decides was registered at `r7884` and is NOT re-opened here. What this file fixes is the two things
`r7884` could not: **which grid the limit is read on**, and **what cross-machine state permits the
read at all.**

## ⓵ THE GRID THE LIMIT IS READ ON IS THE RUNNER'S TEN, NOT THIS CONTAINER'S EIGHT

This checkout has banked eight of the ten points itself. **The limit is read on the ref's ten**, for
the reason the order gives — the runner is where the grid was commissioned to be computed — and
because eight is not a grid.

⛔ **And the two sets are NOT mixed.** Filling this container's two missing points from the ref would
produce a ten-point grid whose points came from two machines with nothing in the record saying which
came from where. *That is the silent conflation this programme has a class for.* So:

- `r7884`'s `limits_nuhier.py` is **imported whole and not retyped**, and only its `NEW_PP` source
  directory is redirected to the ref's extracted points before its assembly runs. The assembly, the
  five plumbing gates, the carried nodes and both envelope reads are untouched.
- This container's eight points stay where they are and are used **only** as the cross-machine
  control. They are not an input to the limit.
- ⌗ *The two still-unbanked local points are redundant either way, since `70`'s runners produced the
  grid of record. They are being allowed to finish rather than being spent on.*

## ⓶ THE CROSS-MACHINE STATE THAT PERMITS THE READ — AND IT IS ALREADY MEASURED

`r7886` registered three states for this control **before any runner number existed**, and the
measurement has now been made on the eight points the two machines share:

| state | bar | verdict | measured |
|---|---|---|---|
| `Ⓒ⓸ᵃ` | `≤ 1e-10` | ACCEPT | — |
| `Ⓒ⓸ᵇ` | `≤ 1e-6` | **ACCEPT WITH THE MISS REPORTED** | ⬅ **`2.121e-09`, at `cr_S015` band `8`** |
| `Ⓒ⓸ᶜ` | worse | REFUSE; the discrepancy is the finding and no limit is read | — |

**So the read proceeds, and the miss is reported rather than passed.** The agreement is `2.121e-09`
— nine orders below the report bar and far below anything that could move a limit — but it is **not
zero**, and the record says so because the registered state says to.

⛔ **This is the case the accept/report split was registered for, and it is worth stating plainly.**
`70`'s own gate carries a single `1e-6` refuse bar, under which `2.121e-09` passes **silently**.
`70`'s gate also compared only the two points banked at the time it ran, both `lcdm`, and recorded
`0.0` for both. The miss is on a `cr` point — the arm with the non-standard background — which that
gate never compared. ⇒ *A one-sided bar would have reported exact agreement on this grid. It is not
exact. Nothing about the limit changes; what changes is whether the record is true.*

## ⓷ THE FORK IS `r7884`'s AND IS NOT RE-OPENED

Read on the **CALIBRATED** profile against `r7870`'s **SEPARATING** rung, `185.958 meV`, minimum at
`0.06`. ⛔ *Not `185.92 meV`, which is the control's limit of record but the wrong comparison here.*

| registered | minimum at | consequence |
|---|---|---|
| `Ⓝ⓵′` | `0.06` or above | every profile point from the minimum upward is supported by nodes `r7882` solved, plus the exactly-carried zero node. **The limit is READ.** |
| `Ⓝ⓶′` | `0.0` | supported by the exactly-carried zero node and its neighbours. **The limit is READ**, with the support stated. |
| `Ⓝ⓷′` | `0.03` | ⛔ that point's interpolation leans on a carried NEGATIVE node, which is not like for like. **NO LIMIT IS READ**; the grid is reported as needing the negative nodes re-solved, which the hierarchy cannot do. **That is the finding, not a patch.** |

## ⓸ WHAT MAKES THIS REVISION REFUSE

- **Any of the five plumbing gates `Ⓛ⓵`–`Ⓛ⓹` failing.** The module raises before either envelope read
  and no number is printed. A limit read through unverified plumbing is not a limit.
- **The assembled grid not being the one the model holds** (`Ⓛ⓸`).
- **The ref's points not being the runner's** — if the recorded run or commit does not match
  `46016816497` at `46f824c2feba`, the grid is not the one the order pointed at.
- **The minimum landing at `0.03`** — then `Ⓝ⓷′` fires and no limit is read.

## ⓹ WHAT THIS REVISION WILL NOT CLAIM WHATEVER THE NUMBER IS

⛔ **The limit is NOT joint, and will not be called joint.** `r7882`'s validation stands on **one
fitter**. `cc66`'s second fit on the validation legs is order `r7885` item ③ and **has not returned**.
69's own ruling is that *the limit is joint only when both fitters agree.* So whatever number this
read produces is **this seat's single-fitter reading**, to be stated as such, and item ④'s arm of
record waits on `cc66` and not on this.
