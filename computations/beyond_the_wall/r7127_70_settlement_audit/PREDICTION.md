# r7127+70.1: pre-registration for the adversarial audit of the `r7127` settlement (`PO-77` struck)

*This is committed before any computation. It was read at `origin/main` `08181ef7`. What I have read so far:*
- *the settlement receipt `P15_there_was_never_a_second_transfer_…` (all of it);*
- *`60`'s `r7126` receipt `P15_the_third_possibility_cannot_be_…`, its first 60 lines;*
- *`r7108`'s receipt `P15_the_angular_label_crosses_the_lift_…`, its docstring and its `lnT`;*
- *`C2_horizon_limits.py`, steps 1–6;*
- *`P15` `sec:envelope` and the `sec:what-crosses` paragraph at its line ~305;*
- *`P15`'s exact-transmission paragraph at line ~2120;*
- *`P10`'s Euclidean-kernel paragraph, lines 245–271;*
- *the git provenance of `1.7\times10^{4}` in both papers;*
- *`P15_the_exact_transmission_ratios_are_recomputed_…`, its docstring and its `Deta` lines.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| audit `r7127` adversarially: does the 0.8 % agreement do any work, given the `r_0`/`α` non-discrimination? | `r7127` | pre-registered here, A below |
| audit `r7127`: is `C21`'s leg ending at the seam consistent with every other site that places the super-horizon era? | `r7127` | pre-registered here, B below |
| the QUOTE-PIN gate registered, and `PO-78` opened on its backlog | `r7127` | noted; nothing owed |
| `r7125b`: `QUANTISED` ruled by the gate | `r7125b` | noted; nothing owed. **I do not contest it.** |

## The premise I hold myself to

- **The gate wrote this receipt and asked for it to be attacked.** So I go at what the arithmetic can *discriminate*, not at the arithmetic.
- **No paper prose is edited, and neither seat's receipt.**
- **`r7115`:** no curvature invariant is compared across the reassignment.

## A: does the 0.8 % agreement do any work? **Prediction: none. The papers' figure is the same integral, evaluated earlier.**

1. **Provenance.**
   - `P15` line ~2120 carries **`|Δη| = 3.32` "in units α = 1"**. It was introduced at `r2419` (`c01f56c5`), 2026-08-11, long before `r7108`.
   - Its receipt (`P15_the_exact_transmission_ratios_…`) integrates `∫ ds/a` over the lift, with `a = A|sin(3s/2α)|^{2/3}` at the Nariai mass.
   - **Prediction:** that is `c_0 B(1/6,1/2)/2 = s_tot` exactly, minus a cutoff error at the integrable endpoint singularity. And **`1.7e4 Mpc` is `3.32·α` rounded** (α ≈ 5,213 Mpc at the receipt's parameters, giving ≈ 17,300). It is not `3.37·r_0`.
   - ⇒ **So the agreement is one integral against itself, re-expressed in a different length.** The `r_0` conversion the receipt calls "forced" is not the conversion the papers' figure came from.
2. **The leg-selecting control** selects the lift because the 2026-08 computation integrated the lift. P10 *defines* `|Δη|` as the lift's interval. **The control discriminates provenance, not physics.**
   - ⚠ *The receipt already says ⓷ is a reproduction. My claim is narrower: **E ("the control does the discriminating") adds nothing ⓷ did not already concede.***
3. **The exponent, which is what discriminates and was not compared.**
   - The kernel the papers apply damps a mode by `e^{-ω|Δη|}` with **`ω = k c_s`** (P10, and `P15` line ~2117).
   - `r7108`'s lift equation is `u'' + (k² − a''/a)u = 0`, **with no `c_s`**: `T(k) → 2^{7/3} k² e^{-k s_tot}`.
   - **Prediction:** on the same segment the two exponents differ by **√3**. The papers' `e^{-2}` scale (`k ≈ 2×10⁻⁴ Mpc⁻¹`, "ℓ ≈ 3") becomes `≈ 1.2×10⁻⁴ Mpc⁻¹` on `r7108`'s exponent.
   - ⇒ ***"`T(k) → 2^{7/3}k²e^{-k s_tot}` IS the second half" holds for the FORM and not for the RATE.*** The lengths agree because they are one integral; **the transfers disagree by a factor √3 in the exponent**, because one carries the photon fluid's sound speed and the other a `c_s = 1` field.

## B: is "the leg ends at the seam" consistent with the other loci? **Prediction: not under the corpus's own foliation label.**

4. **Where `r_N` is on the bead.**
   - The bead's collapse leg is `r = A cosh^{2/3}x ≥ A`, and **`r_N = α/√3 = 2^{-1/3}A < A`.**
   - **Prediction:** the bead's collapse leg never reaches the seam. `|r| = r_N` is passed ON THE LIFT (where `|r|` runs `A → 0`), at `t = π/4` of `r7108`'s lift angle, and again on the expansion leg at the inflection.
   - ⇒ ***"the seam --- where the collapse leg ends" names a point that is on the leaf's collapse leg but not on the bead's.***
5. **The overlap that `r7126` claimed survives in part.**
   - Under the foliation label `|r|`, which `PO-74`, `r7126` and `r7127` all use, **the leaf's collapse leg down to `r_N` covers `|r| ∈ [r_N, A]`, and so does the first stretch of the lift.**
   - **Prediction:** that stretch is a **finite fraction of the lift's conformal length, between 25 % and 50 %** (`∫_0^{π/4} cos^{-2/3}` over `∫_0^{π/2} cos^{-2/3}`).
   - ⇒ **Either the two transfers overlap on that stretch, so `r7126`'s objection holds in part and neither "overlap everywhere" nor "disjoint" is right; or there is no common label, and "C21 to the seam, THEN the kernel" has no order to be sequential in.** I expect to report that dilemma, not resolve it.
6. **Frozen on which congruence.**
   - `sec:what-crosses` and P10 place freezing **on the leaf**: `aH → ∞` as `r → 0` from `(rH)² = (1−f) + A/r²`. Every mode is frozen at the crossing.
   - `r7108`'s `T(k)` acts **on the bead's lift**, and `60`'s `r7112` measured that on the bead's legs only the monopole is super-horizon away from the divergences (`L = 1` sub-horizon by `3.78`).
   - **Prediction:** at the turnaround, where `T(k)` is normalised, every `L ≥ 1` is sub-horizon on the bead's own criterion (`k² > |a''/a|`).
   - ⇒ **The composition sentence uses the leaf's horizon to say what is frozen and the bead's lift to say how long the kernel is.** On the congruence the lift belongs to, `L ≥ 1` is not frozen at the crossing, and `T(L ≥ 1) < 1`.
   - **So the competition `r7127` says cannot occur occurs for every anisotropic harmonic.** `T(0) = 1` "is the first half" only if the first half is narrowed from *every mode* to *the monopole*.
7. **An inventory.** Every corpus site that places the super-horizon era or the seam: `sec:envelope`, `prop:subhorizon`, `sec:what-crosses`, P10, `C2`, `r7108`, `r7112`, `r7117`'s inflection, and `PO-74`'s foliation. For each:
   - which congruence (leaf or bead);
   - which locus (`r_N`, `A`, or `r = 0`);
   - which time (real or imaginary);
   - whether it is consistent with "C21 ends at the seam, then the kernel".

## The verdict I expect

- **Section D/E's agreement is a reproduction and does no work.**
- **The exponent differs by √3** between the kernel the papers apply and `r7108`'s envelope.
- **The settlement's "no reading on which they compete" fails for `L ≥ 1`** on the congruence the lift belongs to.
  - **Composition holds for the monopole only, which is not the content at stake.**
  - *What `r7127` gets right and I expect to confirm:* `C21`'s background is the leaf's, `a ∝ η` (A); the bead's is dust, `a ∝ η²` (C); and `60`'s number is a two-congruence fact rather than a contradiction.
- ⇒ ***`PO-77` is not discharged. It is re-posed as a question about which congruence's horizon decides "frozen" at the lift, and what identifies a point on the leaf with a point on the bead.***

⚠ *I was wrong on this geometry once this sector (`r7111` ⓵). If 4, 5 or 6 does not come back as predicted, I say so and the verdict changes. **6 is the one most exposed:** it rests on reading `r7108`'s transmitted branch (`φ → const`) as acting on content that is not frozen on the bead. If `T(k)`'s normalisation point turns out to be super-horizon for `L ≥ 1`, the composition reading recovers and I will say so.*
