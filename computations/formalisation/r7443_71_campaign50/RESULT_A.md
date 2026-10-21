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

---

# `r7443+71.52` — RESULT, campaign 50, part B: row 53 `DONE`. ⌗ The essential image is built as Mathlib's `Functor.essImage` and proved equal to the solution class, with the fibre counts, dimensions and strata. ⌗ p `0.50` came true

*`probes/Row53Image.lean`: 8 theorems on `[propext, Classical.choice, Quot.sound]`, `13 s`, 380 lines, no error or
warning. The build was delegated and re-run by 71 (`PROBE_RUN_B.txt`).*

- ***SdS.***
  - The mass functor `Discrete ℝ ⥤ Prof` has as essential image exactly the differentiable solutions of
    `r f′ + f − 1 + Λr² = 0` on `r > 0`. `Prof` is the radial profiles, two of them isomorphic iff they are equal on
    `r > 0`.
  - The functor is full and faithful, so `Discrete ℝ ≌` its essential image.
  - Each solution has exactly one `M`. The class is an affine line of dimension 1.
- ***Type-D.*** The essential image equals an ***intrinsic*** quartic class, not the range restated:
  - degree ≤ 4, `r⁴` coefficient `−Λ/3`, no `r³`, opposite `r²` coefficients, a shared constant;
  - an equivalence onto it, and dimension 4, not 6.
- ***Strata*** on Mathlib's indefinite `so′(p,q)`: `so(4,1)` is 10, `so(2,1)×so(3)` is 6, `ℝ×so(3)` is 4, and `so(5,1)`
  is 15.

***Caveats.***
- The receipt ***names*** the functor and the categories but does not define them. Those here are 71's choices,
  stated in the file.
- Not built:
  - K1's action groupoid and its orbit space;
  - Step 3's identification of each stratum's isotropy with its isometry group. The receipt computes only the
    dimension arithmetic, and Step 4 already limits the claim.
- The Type-D class is the receipt's quartic shape, not the Kerr–NUT–(A)dS field equations.

---

# `r7443+71.53` — RESULT, campaign 50, part C: row 18 `DONE`. ⌗ The full `S₃` monodromy of the root cover is built as Mathlib's own `IsCoveringMap.monodromyPerm`, with no identification step needed. ⌗ p `0.25` came true. ⌗ Campaign 50: three of three ROW objects built; ROW `0`

*`probes/Row18Monodromy.lean`: 12 theorems on `[propext, Classical.choice, Quot.sound]`, `8 s`, 558 lines, no
error or warning. The build was delegated and re-run by 71 (`PROBE_RUN_C.txt`).*

***Topological, which is the ROW object.***
- `r ↦ (r − r³)/2` is a covering map over `{27M² ≠ 1}`. That uses a closed map, finite fibres, and the inverse
  function theorem at the simple roots.
- The fibre over `0` has three points.
- An explicit loop `γ` around a branch point lifts to a transposition. The reason is that `t ↦ conj Γ(1−t)` is
  another lift, and `Γ(½)` is not real, which a connected-component argument proves.
- The symmetry `M ↦ −M` gives a second transposition. The two distinct transpositions generate `Perm(fibre)`.
- So the monodromy is surjective and the monodromy group is `S₃`.

***Algebraic.***
- `X³ − X + 2`, the rational member `E = 0, M = 1`, is irreducible over ℚ with discriminant `−104`, which is not a
  square.
- Its Galois group is the full `S₃` (`galActionHom_bijective_of_prime_degree'`), abstractly isomorphic to the
  monodromy group.

***Scope and caveats.***
- The receipt's `E = 0` slice, with base point `M = 0`.
- ***Not built, and not needed for the object:***
  - the ***canonical*** identification of monodromy with the Galois group over `ℂ(M)` (Riemann existence);
  - the Galois group over `ℚ(M)`.

  Neither is in Mathlib. Searched: "Riemann existence", "Hilbert irreducib", `RatFunc`-with-`Gal`, and
  "monodromy" outside `Topology/Homotopy/Lifting.lean`.
- The receipt checks "three-sheeted, branched at the two Nariai values, monodromy S₃" only by string search of
  its source. Lean now proves them. No disagreement.

## Campaign 50, scored

| row | p | outcome |
|---|---|---|
| 18 | 0.25 | `DONE` |
| 53 | 0.50 | `DONE` |
| 86 | 0.45 | `DONE` |

The band was 500–2500 lines across the three probes: `558 + 380 + 344 = 1282`, ***IN BAND***.
