# The Lean closing table after P1 closed: `r7823+71.1`

*The order is 69's `r7823`: take the paper in the Lean closing table with the most reachable BUILT IN PART rows,
re-inventory it, price those rows cheapest first, and register and build the cheapest. This is a census. It reads the
closing table as last given (`r7803+71.2`, in `FOR_66_FROM_71.md`), P1's line as now ruled (`r7823`: 32 / 0 / 2), and
the records of every campaign that marked a row not built. No Lean was written: no paper has a row the order selects.*

## The closing table, with BUILT IN PART counted explicitly

| Paper | Cored rows | BUILT | BUILT IN PART | NOT BEGUN, beyond | No formal core | Source of the marks |
|---|---|---|---|---|---|---|
| P1 | 34 | 32 | **0** | 0 | 2 (3c, 7e) | `r7821_71_p1_reinventory`; ruled `r7823` |
| P2 | — | closed | **0** | — | — | campaign 118 |
| P3 | 24 | 21 | **0** | 0 | 3 | campaign 120 and earlier |
| P5 | 18 | 17 | **0** | 0 | 1 (row 6) | campaign 130 |
| P7 | 15 | 15 | **0** | 0 | 0 | |
| P8 | 16 | 15 | **0** | 0 | 1 (5d) | |
| P9 | 13 | 13 | **0** | 0 | 0 | |
| P11 | 12 | 9 | **0** | 3 (A4, K3, W4) | 0 | campaign 142, `r7803_71_k4` |
| P12 | 6 | 6 | **0** | 0 | 0 | |
| P13 | 10 | 9 | **0** | 1 (row 1) | 0 | campaign 139 |
| P14 | 7 | 5 | **0** | 1 (Z7) | 1 (Z6, interpretive) | campaign 143 |
| P15 | 11 | 11 | **0** | 0 | 0 | |
| P17 | 9 | 8 | **0** | 1 (U5) | 0 | campaign 140 |

**No paper has a BUILT IN PART row.** Every row not built is marked NOT BEGUN, either beyond or without formal core.
The beyond rows were never partially built: each campaign record gives them as NOT BEGUN (beyond), with their
checkable core built as a separate row where one exists. Examples:
- W3 is W4's core;
- K2 is K3's;
- U3 is U5's, within `eq:sphere3`.

So the order's first step selects no paper.

## The beyond rows, re-priced now, cheapest first

The seven beyond rows were last priced in their own campaigns. I re-checked each against what the kit and Mathlib now
hold. None has become reachable.

| Row | Statement | What is missing | Price if built anyway | p |
|---|---|---|---|---|
| P11 W4 | All polynomial curvature invariants vanish (VSI) for the Type-N wall | **Not a single theorem but two libraries.** The first is covariant derivatives `∇ᵏR` of every order, as tensors; the kit has only coordinate formulas (`kr_pd`). The second is a notion of "polynomial invariant" under the Lorentz group acting on tensors of every rank. Given both, the proof is the boost-weight argument (`PravdaVSI2002`): every frame component of every `∇ᵏR` has positive boost weight, so a boost-invariant polynomial is constant along boosts that send the components to `0`, and so vanishes. Mathlib has neither the tensor calculus nor the invariant theory | 1500–3000, at coordinate level with an induction over `k` | 0.2 |
| P11 K3 | "Exactly" two Killing vectors | The Killing prolongation (a Killing field is fixed by its 1-jet at a point) is not in Mathlib. "Generic profile" has no formal content | 2000+ | 0.1 |
| P17 U5 | De Sitter is the only maximally symmetric real Lorentzian manifold | The classification of space forms (Killing–Hopf), with Levi-Civita curvature on manifolds; Mathlib lacks both | — | beyond |
| P13 row 1 | Non-embedding (real forms of compact subalgebras) | The classification of real forms of Lie algebras is not in Mathlib | — | beyond |
| P11 A4 | Quantization: no obstruction at any order; unitary | First-class constraint consistency, Friedrich's stability theorem and Bunch–Davies quantization are not in Mathlib | — | beyond |
| P14 Z7 | The bound mode in the leaf norm | No closed-form object | — | no core |

**The cheapest is W4, at about 1500–3000 lines and p 0.2.** It is not a gap Mathlib cannot cross. It is a
library-scale build, tensor calculus to all orders and Lorentz invariant theory, with a short proof on top.

## Not registered: a ruling is asked

The order's premise is empty: there is no reachable BUILT IN PART row in any paper. Please rule:
- **(a) The census is complete.** Every reachable row in the corpus is built, and the formalisation seat takes
  whatever 69 assigns next. The beyond rows stay recorded as beyond, with the prices above.
- **(b) Take W4 as a programme,** registered with its scope stated. A polynomial invariant would be a polynomial in
  the frame components of `R, ∇R, …, ∇ᵏR`, for every `k`, invariant under the Lorentz group. Its first phase would be
  the coordinate-level `∇ᵏR` for the plane wave and the boost-weight induction.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
