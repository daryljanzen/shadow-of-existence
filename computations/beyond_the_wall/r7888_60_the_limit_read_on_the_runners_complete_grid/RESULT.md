---
kind: RESULT
revision: r7888+60
order: r7885 (69) item ②
---

# r7888 — THE LIMIT IS READ, AND THE REPAIR MOVES IT **AWAY** FROM THE REFERENCE

Order `r7885` (69) item ②, on the grid `70`'s runners produced. `refs/ci/r7884_phiphi` at `133e612fe`
carries all ten points from run `46016816497`. **Branch `Ⓝ⓵′` fired as registered** — the calibrated
profile's minimum sits at `0.060` eV with **no dips above it** — so the limit is readable and is read.

## ⛭⛭⛭ THE NUMBER, AND WHAT IT IS AGAINST

| | calibrated limit | against the reference's `30.56` meV |
|---|---|---|
| the reference (`cc66`/CAMB) | **`30.56` meV** | — |
| `r7870` separating rung, **no** hierarchy, no closure | `185.95834` meV | `6.085` × |
| `r7870` separating rung, **no** hierarchy, envelope **CLOSED** | `185.95842` meV | `6.085` × |
| **this revision — hierarchy ON, envelope CLOSED** | **`193.545` meV** | **`6.333` ×** |

**The move is `+7.587` meV, `+4.08` per cent — and it is the WRONG WAY.** The gap to the reference
goes `155.398` → `162.985` meV, widening by `4.88` per cent of the gap that was already there.

## ⛔ AND THE MOVE IS THE HIERARCHY'S, NOT THE ENVELOPE CLOSURE'S — DECOMPOSED, NOT ASSUMED

This revision's number carries **two** changes against `r7870`'s `185.958`: the hierarchy, and closing
the envelope under cross-seeding. ⇒ *A `+7.587` meV move reported without separating them would be
attributing to the repair whatever the closure did, which is the mistake `r7878` was made to avoid.*

**The control exists and was already banked:** `r7870`'s own record carries the closed envelope on
the same rung with the hierarchy OFF.

- `raw_calibrated` = `185.95834` meV, `env_calibrated` = `185.95842` meV.
- **Closure moves the calibrated crossing by `+0.00008` meV.** It is a no-op there, and it has to be:
  that profile is already `monotonic_above_min = True`, so cross-seeding has nothing to repair.

**So the whole `+7.587` meV belongs to the hierarchy.** ⌗ *On the MINIMISED column closure is the
opposite — `181.436` → `287.772` meV on the same rung — because that column is NOT monotonic above
its minimum. Which is exactly why the limit is read on the calibrated column and the minimised one is
an envelope crossing and never a limit.*

## ⛔ WHAT THIS MEANS FOR THE ARC, STATED AS A NEGATIVE RESULT

`69` set the expectation at `r7885`'s channel section: the Fermi–Dirac background repair moved the
calibrated limit `81.94` → `185.96` meV, **away** from `30.56`, and *"a repair that brings the
background into agreement should not double the disagreement in the limit."* The named candidate for
the exposed compensation was **how the perturbations carry the neutrinos** — the clustering matter
losing `ω_ν` at all times, with no free-streaming scale.

**The hierarchy supplies precisely that missing physics, and the limit moved further away again.**

- It is not a failure of the hierarchy to *work*: `r7882` validated it jointly, verdict `Ⓐ`, TT and EE
  within `0.03` of one at both sums on one fitter, converged in both numerical parameters.
- ⇒ *So the candidate `69` named is not the compensation, or is not all of it.* A repair that is
  correct on its own terms and moves the limit the wrong way says the disagreement is not sitting
  where either of us put it.
- ⛔ **This is reported as the finding and NOT patched.** No parameter is tuned toward `30.56`, and no
  reading is chosen to make the move smaller.

## ⛔ WHAT IS NOT CLAIMED

- **The limit is NOT joint.** `r7882`'s validation stands on **one fitter**. `cc66`'s second fit on the
  validation legs is order `r7885` item ③ and has not returned. `69`'s own ruling: *the limit is joint
  only when both fitters agree.* So `193.545` meV is **this seat's single-fitter reading** and item
  ④'s arm of record waits on `cc66`, not on this.
- **A crossing on the minimised column is never a limit** — `310.148` meV here, non-monotonic above
  the minimum, and `r7870` had already measured that column unreadable on this rung.
- **The closed envelope is a lower envelope over the basins REACHED**, not a proved global minimum.
- **`193.545` meV is not offered as the control's limit of record.** It is the limit on the jointly
  validated sector, read on one fitter, on the grid the order pointed at.

## THE GRID, AND THE CROSS-MACHINE CONTROL

Read on `70`'s ten points, **not** on this checkout's own. ⛔ *The two were never mixed: filling either
from the other would make a grid whose points came from two machines with nothing recording which
came from where.* This container's eight points served only as the control:

- All five of `r7886`'s closures **pass** on the runner's grid — complete, provenanced on seven
  switches, `9` bandpowers over `36` multipoles, the frozen list undrifted.
- **The cross-machine agreement is `2.121e-09`**, at `cr_S015` band `8`, in the registered state
  `Ⓒ⓸ᵇ` — **accept with the miss reported.** ⛭ *Read on `8` shared points when the limit was read, and
  since completed on all `10`: this container finished its own tenth point afterwards, and the worst
  disagreement over the full grid is **unchanged at `2.121e-09`**, so the two points added agree
  better than the worst already found. `PREDICTION.md` is left as registered, on eight, because it
  was registered before the read; this is the same control carried to completion, not a re-choice.*
  ⇒ *So the entire ten-point grid has now been computed INDEPENDENTLY TWICE — once on `70`'s runners,
  once in this container — and the two agree to `2` parts in `10⁹` at the worst band. That is a fact
  about the instrument's reproducibility and not about the limit, and it is the strongest form the
  registered control can take.* ⌗ *Nine orders below anything that could move a limit.
  But it is not zero, and `70`'s single `1e-6` refuse bar would have passed it silently; `70`'s gate
  also compared only the two `lcdm` points banked when it ran and recorded `0.0` for both. The miss
  is on a `cr` point, the non-standard-background arm, which that gate never compared.*
- All five plumbing gates `Ⓛ⓵`–`Ⓛ⓹` pass **before** either envelope read, as the module enforces:
  `22` carried points with the switch absent and each at the sum its own tag names, of which exactly
  `4` negative; `10` re-solved at the gated grid; the model holding the assembled grids.

## ⛔ THREE DEFECTS IN `r7884`'s LIMIT MODULE, AND ONE CAUSE: IT LANDED **REGISTERED AND UNRUN**

`r7884` landed `limits_nuhier.py` with both envelope reads in it and its gates ahead of any number,
deliberately unrun. **Every part of it that had never executed was wrong.**

⓵ **`Ⓛ⓵` could not pass on the carry set the module itself defines.** It demanded `MNU == 0.00` of
every carried tag, while `CARRY_TAGS` deliberately includes the two negative nodes at `-0.06` and
`-0.12` — carried *precisely because* the hierarchy has no reading below zero. ⇒ *The clause the
argument reasons from is not "every carried sum is zero" but "every carried point is the point its tag
claims".* It now reads each tag's own named sum and **counts** the negatives, because the registered
fork `Ⓝ⓷′` turns on whether the minimum leans on them. Measured: `22` carried, switch absent on all,
exactly `4` negative.

⓶ **`Ⓛ⓷` read its own wording.** It asked `'def closed_envelope' not in src` of its own source — and
its own assertion contains that string, so the test was false for **every file that carried it**. It
also asked `'import envelope_closed as EC' in src`, which its own text made trivially **true**. One
half could never pass; the other could never fail. ⇒ *Now read off the PARSE TREE, so the gate cannot
be satisfied or defeated by the question being written down.*

⓷ **A `KeyError` after both reads had completed.** The reporting line asked for a `limit_meV` key that
`closed_envelope` has never returned; the key is `crossing_meV`. The whole read was spent and then
thrown away.

⛔ **The gates were fixed to assert the clause they reason from, not to pass.** Both were REFUSING,
which is exactly the situation where repairing a gate is suspect, so the teeth are checked in the
receipt on faulted inputs rather than asserted here. ⌗ *And the lesson is the one that generalises:
registering a gate is not running it. An unrun gate is a claim about a measurement nobody made.*

## TWO MORE, FOUND THE SAME WAY

⓸ **`git archive` resolves its tree at the current directory's path inside the repository**, so run
from a subdirectory it archived nothing and this revision extracted **zero** points. The gates caught
it and refused rather than reading a limit off an empty grid — but the extraction is now checked for
itself, because a silently empty source is the same shape as a gate counting what is not there. ⌗ *And
the repository root is now ASKED FOR rather than counted up with `dirname`, which got it wrong by one
level and produced the same empty archive a second time.*

⓹ **The result was landing in another revision's directory.** `limits_nuhier.py` writes its record
beside itself, so a read driven from here left its output in `r7884`'s folder, where the next reader
would take it for `r7884`'s own — and the file sitting there was from the run that **refused at the
gates**, naming the since-fixed `Ⓛ⓵`. ⇒ *Committing it would have filed a stale refusal as this
revision's result.* The driver now keeps its own copy, named for the grid it was read on, and only on
a run that got through the gates.
