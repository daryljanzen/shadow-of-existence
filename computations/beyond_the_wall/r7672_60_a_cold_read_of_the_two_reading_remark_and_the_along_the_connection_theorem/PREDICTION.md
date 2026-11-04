# `r7672` — a cold read of the two-reading remark and the along-the-connection theorem

**Registered before any bank is taken.**  Order `r7671` asks a cold read of the along-the-connection
remark's **new sentences**, on a named tree, in three directions: against `AlongConnection.lean`;
against P1's own text (Section 1's `Δτ`, the proof's *"These are not coordinate differences
accumulated along some path"*, and `cor:threefold`(iv)); and **whether any sentence of P1 still
reads `Δτ` in a way the remark does not account for.**

## The objects

**Seven claims**, fixed here: ① `Δτ` read along the connection is the adapted frame's temporal leg,
`Δτ = ∫N|dt|` with `N` the lapse, the geodesic running along that frame's time direction because it
stays at one value of the invariant spatial coordinate; ② on a Killing horizon it is `∫|χ|dλ` along
the Killing parameter, as in `lem:killing`; ③ its integrand is invariant and it is not a coordinate
difference; ④ `τ(q) − τ(p)` assigned by an arbitrary temporal function stays non-invariant, as
Section 1 and `cor:threefold`(iv) say; ⑤ the theorem is machine-checked **on any manifold** —
along a `C¹` curve, with `g = h − N²dt²` and `N ≥ 0`, (a) and (b) give `Δτ = 0`
(`ac_metric_singularity_along`); ⑥ where `N > 0` along the curve, (a) and (b) force `p = q`
(`ac_lapse_pos_forces_point`), so metrically coincident distinct events need the adapted lapse to
vanish; ⑦ as it does on a generator of the Rindler horizon, where `p ≠ q` (`ac_witness`).

**And ⑧, the order's third question**, scored separately: the residue of P1 sentences reading `Δτ`
that the remark does not account for.

## The arms

- **⓵ Every cited name must resolve** in `AlongConnection.lean`.  **Registered prediction: all
  resolve.**
- **⓶ `ac_metric_singularity_along` must have the hypotheses the sentence states and `Δτ` as an
  INTEGRAL**, not an endpoint difference.  **Registered prediction: the splitting, `N ≥ 0`, (a) and
  (b) are its hypotheses and nothing further, and its `Δτ` is an integral along the curve.**
- **⓷ `ac_lapse_pos_forces_point` must conclude `p = q`** from `N > 0` with (a) and (b).
  **Registered prediction: it does, with the conclusion stated on the curve's endpoints or on the
  curve being constant.**
- **⓸ `ac_witness` must exhibit BOTH halves** — a Rindler-horizon generator with `p ≠ q` and a
  vanishing adapted lapse.  **Registered prediction: both.**
- **⓹ "machine-checked on any manifold"** must be true of the file's own ambient instances.
  **Registered prediction: the general `MSpacetime E N`, no dimension assumed, no finite
  dimensionality.**
- **⓺ ⑧ is registered as a COMPARISON, not a count.**  `r7670` corrected this seat for registering
  an expected verdict instead of the comparison that decides it, so: the instrument enumerates
  **every** sentence of P1 that mentions the temporal separation, classifies each as accounted-for
  or not by markers drawn from the remark's own text, and reports the residue **whatever its
  size**.  My reading before measuring, recorded so it can be scored but not used as the
  instrument: the one still unaccounted is the proof's *"These are not coordinate differences
  accumulated along some path between `p` and `q`"*, because the remark answers its *coordinate*
  half — "it is not a coordinate difference" — and not its *accumulation* half, while itself now
  saying `Δτ` is "the temporal leg **accumulated along** it".  The collision is sharper than it was
  at `r7670`, since the remark has adopted the very word.
- **⓻ The guard, three families.**  Every verdict a function of its readings; a flip family;
  anchored markers only, in the two forms `r7670` fixed — a word boundary or an escaped control
  sequence — with the scanner refusing anything else and recording each hit's context.  **If any
  probe does not flip, every verdict is withdrawn.**

## What would falsify the reading

A claim scored from the prose rather than the Lean, or from the order's account of the repair
rather than the paper's sentences; a cited name taken on trust; a residue asserted rather than
computed; a verdict on a tree other than the one `runs/TREE.txt` names; a guard probe that does not
flip.
