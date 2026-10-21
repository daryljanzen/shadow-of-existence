# `r7443+71.51` — RESULT, campaign 50, part A: row 86 `DONE`. ⌗ The `Z₃` action on the quadric's loci is built as the receipt defines it, and every computed check is proved. ⌗ Rows 18 and 53 are still building; their scores go in part B

*Scored against `PREDICTION.md` (pushed at `r7443+71.50` before any Lean), not revised. `probes/Row86Action.lean`:
11 theorems on `[propext, Classical.choice, Quot.sound]`, `10 s`, 344 lines, no error or warning. The build was
delegated and re-run by 71 (`PROBE_RUN_A.txt`). Row 86's registered p of `0.45` came true.*

***Built.***
- ***The space and the action.*** The space is `ℂ × ℝ × ℝ`. `X₀` is complex so that the axis pair `±iα` exists, as
  the receipt's "imaginary and NOT absent" requires. `Z₃` acts as the 120° rotation of `(X₁, X₂)`: a faithful
  `MulAction (Multiplicative (ZMod 3))` of order 3. It preserves the quadric `X₀² = X₁² + X₂² − α²`.
- ***The loci.*** The walls lie on the throat; each wall is antipodal to its hinge; walls and hinges are cycled; the
  throat is stable; the axis is fixed.
- ***Fixed points and orbits.*** The fixed points are exactly the axis, and every other orbit has three points. For
  `α ≠ 0` the throat has no fixed point, and the walls form one free orbit.
- ***Branches.*** There is one branch iff the point is on the throat, over ℂ. The axis pair is distinct and fixed.
- ***The singlet question.*** Every computed check of the receipt's Parts 1–4 is proved (`singlet_obstructed`).
  Stronger than the receipt states: no point is both one-branch and `Z₃`-fixed.

***Caveats.***
- The receipt's `R` is ***quoted*** from P7, not defined. It is modelled as the branch flip `X₀ ↦ −X₀`, whose fixed
  set on the quadric is the whole throat. So P7's "sole fixed point" and the "three times over" multiplicity, which
  rests on P14R28's three-vantage reading, are not reproduced. They are P7's content, not this receipt's
  computation.
- ***A receipt claim true only as a locus:*** "not hinge-free" holds of the throat as a whole. A generic `Z₃`-orbit
  on the throat contains no wall.
