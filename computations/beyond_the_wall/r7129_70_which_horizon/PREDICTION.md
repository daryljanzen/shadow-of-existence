# r7129+70.1: pre-registration for `PO-77` ⓵, which horizon decides "frozen" at the lift, and a check of the row against my findings

*This is committed before any computation. It was read at `origin/main` `4ab40876`. What I have read so far:*
- *`r7129`'s order, and the `PO-77` row in `THE_FRONTIER`;*
- *`prop:subhorizon` and its argument (`P15` ~l.290);*
- *`sec:envelope`;*
- *the `sec:what-crosses` freezing sentence;*
- *P10's kernel paragraph;*
- *`C2_horizon_limits.py`;*
- *`P15_the_locus_is_wrong_in_six_places_…`, lines 100–140;*
- *the corpus's definition of "the comoving turnaround": `1 − f = 0`, `r = −(2Mα²)^{1/3}`, from `P07_cube_root_two…` and `I11_I1…`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| `PO-77` ⓵: which congruence's horizon the corpus's freezing argument is about; if it is the leaf's, what carrying the leaf onto the lift would require | `r7129` | pre-registered here |
| check the `PO-77` row against my five findings; say if it overstates or softens any | `r7129` | pre-registered here, R below. **Two of my own statements need correcting, and the row inherited one of them.** |
| `PO-77` ⓪ and ⓶ | `r7129` | `60`'s; nothing of mine |

## R: the row, and two corrections of my own, stated before I compute

- **R1. The row is faithful to the five findings** as I wrote them. One wording point: *"on the bead's own collapse leg `aH` RISES from zero at the turnaround"* reads the leg outward from the turnaround. In the leg's own direction of travel (contracting), `aH` **falls** to zero as the leg approaches the turnaround, and the paper's sentence speaks in that direction.
- **R2. ⛔ My own error, which the row carries.** I wrote that the paper's `1.96` (at `|r| = 0.1α`) and `19.6` (at `10⁻³α`) place its freezing on the lift, "in the `|r|` range the bead covers ONLY on the lift".
  - **That is true of the bead's contracting side only.** The expansion leg (`r > 0`) covers `|r| < A` too.
  - **And those two numbers do not discriminate the sign:**
    - **Prediction:** the positive-`r` value is `√(2M/r + r²/α²)` = `1.9645` and `19.62`; the negative-`r` value is `√|2M/r + r²/α²|` = `1.9593` and `19.61`. All round to the paper's `1.96` and `19.6`.
    - **66's verification got `1.964`, which is the positive-`r` value.**
  - **The one number in the sentence that would discriminate is `0.13` "at the comoving turnaround".**
    - The corpus defines that point as `1 − f = 0`, where `√|1 − f|` is **exactly zero**.
    - **Prediction:** `0.13` is not reproducible from the stated law at the stated locus. Wherever it can be reproduced (`|r|` within ~1.5 % of `A`), it is on the **signed-negative** branch only, because on `r > 0` the minimum of `√(1 − f)` is `1.0` at `r_N`.
- **R3. ⛔ And my inventory missed a fourth seam.** `P15` names *"the two unit-speed loci `r = −2α/√3` and `r = +α/√3`"*. **`|−2α/√3| = 1.155α > A`, so the bead's collapse leg DOES pass a seam: the back seam.** My audit's ⓻ ("the bead's collapse leg reaches none of them") is true of the three referents I listed and false of the corpus's own list. **Finding ⓹ (`r_N` is not on the bead's collapse leg) stands.**

## ⓵: which horizon, and what carrying the leaf onto the lift would require

1. **Every COMPUTED freezing census in the corpus is on a real-time branch with no Euclidean segment.**
   - `C2` and `P15_the_locus_is_wrong…` both evaluate `(rH)² = 2M/r + r²/α² [+ A_r/r²]` at **positive** `r`, which is positive-definite: no turnaround, no lift.
   - `prop:subhorizon` says *"on either rate"*, and its argument is *"because `2M/r` diverges"*. That is the same census, real-time, `r > 0`.
   - The `sec:what-crosses` sentence writes `√|1−f|`. Only its unreproducible `0.13` would put it on the bead's signed contracting side.
   - **Prediction:** the corpus's freezing argument, wherever it is computed, is the **leaf's** (or the bead's expansion leg run backwards). **It is not the bead's contracting side.**
2. **Can the leaf be carried onto the lift?**
   - The leaf's rate on the contracting (signed-negative) side is `g(x) = A_r/x² − 2M/x + x²/α²` with `x = |r|`. A Euclidean segment exists iff `g < 0` somewhere.
   - **Prediction:** the threshold is a double root, at `x³ = M/2` (α = 1), giving `A_r* = (3M/2)(M/2)^{1/3}`.
   - In the corpus's own datum language: **the leaf has a lift only if `ρ_r/ρ_m` at the seam is below ≈ 0.595. The corpus's datum (`C2`: `ρ_r/ρ_m ≈ 2` at the seam, `A_r = 4Mr_s`) is about 3.4× above it.**
   - ⇒ ***At the corpus's own radiation datum the leaf has no lift at all.***
     - Carrying the leaf onto the lift would require the radiation term to fall below that threshold on the stretch, i.e. the leaf becoming the bead there.
     - **Or** a different object: the bead with radiation, which no file constructs.
3. **The answer I expect to ⓵:** the two halves of the composition sentence are true on two congruences that cannot both hold on one segment.
   - **On the leaf:** every mode freezes in real time as `r → 0`, and there is no kernel, because there is no lift.
   - **On the bead:** there is a kernel, and on its contracting side anisotropic modes are inside the horizon at the turnaround (`aH = 0` there, exactly).
   - ⇒ **"Frozen, so the kernel has nothing to act on" uses the leaf's census for a segment only the bead has.**
   - ***It is not a matter of choosing which horizon decides at the lift: the leaf, at the corpus's datum, does not reach a lift to decide anything at.***

⚠ *This is the third pass on this geometry, and two of my own statements are corrected above before computing. If the threshold in 2 comes out above the datum, so that the leaf does have a lift, the verdict in 3 is wrong, and I will say so plainly.*
