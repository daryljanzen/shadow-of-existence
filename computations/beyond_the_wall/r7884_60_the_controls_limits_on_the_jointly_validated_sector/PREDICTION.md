---
kind: PREDICTION
revision: r7884
node: 60
order: r7879 item ③
---
# r7884+60 — THE CONTROL'S LIMITS ON THE JOINTLY VALIDATED SECTOR, READ ON THE CLOSED ENVELOPE

⛔ **COMMITTED AND PUSHED BEFORE ANY MEASUREMENT OF THIS REVISION RAN.** Nothing below has been
measured. Every number quoted from an earlier revision is cited as that revision's.

`r7879` item ③: *"Then the control's limits on the validated sector, read on the closed envelope."*
`r7882` validated that sector — verdict `Ⓐ`, `A` within `0.03` of one in TT **and** EE at `0.30` and
`0.60 eV`, with both convergence gates met. `r7879`'s own condition for a limit was *"only then"*.

---

## FOUR STRUCTURAL READS, ESTABLISHED BEFORE ANY GRID IS RUN

⌗ *Declared as reads of the existing record and machinery, not as results of this revision. Each is
checkable from the files named.*

**⓵ THE LIMIT IS READ BY SCANNING UPWARD FROM THE PROFILE'S MINIMUM.** `r7864`'s `profile` takes
`i0 = argmin` of the profile total and then looks only at `k > i0` for the first node where
`Δχ² ≥ 2.71`, interpolating the crossing between that node and the one before it. ⇒ **So nodes below
the minimum are used ONLY to locate the minimum**, and a node below it never enters the crossing.

**⓶ THE GRID IS 32 POINTS PER BANK, AND SIXTEEN OF THEM ARE AT ZERO SUM.** `r7870`'s generator runs,
per arm, eight sum nodes — `−0.12`, `−0.06`, `0.00`, `0.06`, `0.15`, `0.30`, `0.45`, `0.60` — **plus
eight parameter-offset directions (`H0±`, `OM±`, `WB±`, `NS±`) every one of which is at `MNU = 0.00`.**
Two arms, so 32 points.

**⓷ THE HIERARCHY REFUSES A ZERO SUM, BY DESIGN AND CORRECTLY.** The switch requires `NUFD=1` and
`MNU != 0` and raises otherwise. `NUFD` is itself gated on a non-zero mass, so at zero sum the
species is exactly massless, `w_ν` is exactly `1/3`, and there is no massive species for a massive
species' hierarchy to describe. ⇒ **So the sixteen offset legs and the zero node CANNOT carry the
hierarchy — not for want of compute, but because there is nothing there for it to do.**

**⓸ AND THAT MAKES THEM CARRIABLE EXACTLY, WHICH IS A DIFFERENT CLAIM FROM "CLOSE ENOUGH".** At zero
sum the hierarchy-on and hierarchy-off spectra are the SAME spectrum, so the sixteen offset legs and
the zero node are carried from the landed bank **without approximation**. This is the argument
`r7876`'s and `r7882`'s own generators already make for their zero legs, and `r7870` made for the arm
of record: *"the carried points' own configs record no offset at all, which the precondition below
checks rather than assumes."* ⛔ **The same precondition is required here: each carried point's own
recorded config must show the switch absent AND the sum zero, checked and not asserted.**

⇒ **Only the FIVE POSITIVE sum nodes per arm need re-solving: ten points.**

---

## ⚠ THE ONE THING THAT IS NOT CARRIABLE, NAMED AS THE FORK IT IS

**The two NEGATIVE sum nodes cannot be carried exactly and cannot be run.** A negative sum is not a
mass: the hierarchy's per-node energy `ε_j = √(q_j² + y(a)²)` has no reading at `y² < 0`, and no
inertness argument applies, because the landed fluid closure DOES produce a spectrum there and the
hierarchy produces none. So at `−0.12` and `−0.06` the profile can only carry the landed closure's
points, which is **not like for like**.

By read ⓵ those two nodes enter the limit only through where the minimum sits. So:

| | what the profile's minimum turns out to be | what follows |
|---|---|---|
| **Ⓝ⓵** | the minimum sits at a **positive** sum node | the crossing is read entirely on nodes the hierarchy supplies, the two negative nodes are **not used by the crossing at all**, and the limit is READ — with the carried negative nodes reported beside it as carried and not like for like |
| **Ⓝ⓶** | the minimum sits at the **zero** node | the crossing is read upward from a node that is exactly carriable by ⓸, so the limit is still READ, and the two negative nodes are still unused by the crossing |
| **Ⓝ⓷** | the minimum sits at a **negative** node | ⛔ **NO LIMIT IS READ.** The crossing would then depend on a node the hierarchy cannot supply, and carrying the landed closure there would make the profile mix two closures across the very interval the limit is measured on. **That is reported as the finding and the grid is reported as insufficient for this sector, not patched.** |

⛔ **`Ⓝ⓷` IS REACHABLE AND IS NOT A FORMALITY.** `r7870`'s corrected read put the limit at
`185.92 meV`, so its minimum sat below `0.15 eV`; it is a measurement, not a guarantee, that this
sector's minimum does not sit at or below zero. **The hierarchy lowers `A` at every sum** — `r7882`
measured all four amplitudes BELOW one — and a closure that changes the fit at positive sums can
move where the minimum falls.

⌗ **This fork is this seat's to decide and it is decided here, before the measurement:** the limit is
read under `Ⓝ⓵` or `Ⓝ⓶` and refused under `Ⓝ⓷`. It is routed to `69` with both branches stated
because it bears on what the order asked for, not because the decision is being deferred.

---

## WHAT IS MEASURED, AND THE GATES ON IT

| | gate | criterion | why |
|---|---|---|---|
| **Ⓛ⓵** | **the carried points are carriable** | every carried point's own recorded config shows the hierarchy switch ABSENT and its sum exactly `0.00`, and the two negative nodes are marked carried-and-not-like-for-like in the record | by read ⓸ this is what makes the carry exact rather than an approximation, and `r7870` was bitten once by a carried point that was not what it was taken for |
| **Ⓛ⓶** | **the new points are the hierarchy's** | every re-solved point's own recorded config shows the switch ON, its sum the node it stands for, and the grid `12` nodes at cut `20` with cutoff `12` — the grid `r7882`'s gates fixed | a bank labelled by its directory name is not evidence about what produced it; `r7882` learned to read this off the leg |
| **Ⓛ⓷** | **the machinery is the one of record** | `r7864`'s `Ruler`, `attach` and `profile` IMPORTED, not retyped, and the threshold left at its `Δχ² = 2.71` | so a difference from `r7870`'s number is the SPECTRA and not the method — `r7870`'s own words for the same requirement |
| **Ⓛ⓸** | **the envelope is the closed cross-seeded one** | the profile is read on `r7870`'s closed envelope, and the record states which envelope file it read | `r7879` said "on the closed envelope"; reading it on a one-basin envelope would answer a different question |

⛔ **`Ⓛ⓵`, `Ⓛ⓶` AND `Ⓛ⓷` RUN BEFORE ANY LIMIT NUMBER IS READ.** A limit read through unverified
plumbing is not a limit, and this line has already spent one whole grid on the wrong reading of a
re-point.

---

## THE COST, DECLARED AS A RISK AND NOT AS A RESULT

`r7864` put a CMB point at *"about 35 minutes per CMB point on four cores"*. **`r7882` measured this
box's own figure at the same resolution: `3945` and `3956` seconds a leg with the hierarchy on, four
legs in parallel.** Ten points at that rate is of order **eleven core-hours**, and the lensing grid
is a second generator whose scope is not yet read.

⌗ **So the cost is the same shape of risk `r7882` carried, and the same discipline applies:** if the
ten points do not fit in one revision, **the measured cost is reported and the item splits**, with
the grid landing first and the limit read following on it. ⛔ *Not quietly dropped, and not run at a
resolution the banked grids cannot be compared against.*

---

## ⚠ THE DEPENDENCY THIS REVISION CARRIES, STATED BEFORE IT STARTS

`r7879` requires the validation *"read on both fitters"*. **`r7882` is ONE fitter.** `cc66`'s second
fit reads `r7882`'s banked legs, and `r7882`'s own registration says that if that fit disagrees
beyond its own reproduction tolerance, **the disagreement IS the finding and no limit is read through
either fitter.**

⛔ **SO A LIMIT READ HERE IS CONDITIONAL ON A VALIDATION THAT IS NOT YET JOINT, AND SAYS SO.**
`r7882`'s reply recommends `cc66`'s fit land first and asks `69` to rule. Absent that ruling this
revision proceeds and **carries the dependency explicitly rather than reading a limit as if the
joint condition were already met** — which is the one thing that would make this number worse than
no number.

---

## REACHABLE NEGATIVES, NAMED

- **`Ⓝ⓷` can fire** and no limit is read at all.
- **The profile can DIP** above its minimum, which `r7864`'s discipline reports as NO limit rather
  than as a limit with a caveat — `r7870`'s minimised profile returned `None` for exactly that reason.
- **`Ⓛ⓵` can fail**: a carried point whose config does not show what it is taken for, which is the
  defect `r7870` was bitten by.
- **The limit can fail to MOVE** from `r7870`'s `185.92 meV`, which would say the sector's closure
  does not reach the limit — a result about the limit's sensitivity, reported as one.
- **And the limit can move a long way**, which is the outcome the order expects and is the one that
  most needs the plumbing gates above to have run first.
