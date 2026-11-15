# `r7803+71.1` — PRE-REGISTRATION: **K4, P11's Petrov type I (`prop:twoKV`): a vacuum-Λ point of the polarized Gowdy–de Sitter form where the Weyl tensor is type I**. ⌗ `450` new lines (band 350–600) plus a short verbatim copy, p(BUILT) `0.55`

*Registered before any Lean, per r7803. The probe is `probes/Dynamics.lean`, appended in `dy_`. Its six copied
blocks stay byte-identical. Two more verbatim blocks are added from `probes/Range.lean`, in a reopened
`ShadowProbe.RangeProbe` namespace: `ij_tbl`, and `ij_blk` through `ij_tr3`. Mathlib only.*

## What the claim is, and what is formalised
`prop:twoKV` says the metric `eq:metric` "with a generic profile `ψ(t, z)`" has a Weyl tensor "separately, of Petrov
type I". The paper gives no closed-form inhomogeneous solution with `Λ > 0`; it says so ("no closed-form nonlinear
solution").

**Type I is a pointwise condition on the 2-jet of the metric**: `I³ ≠ 27J²`, with `I, J` built from the Weyl tensor,
which needs only second derivatives. So the formal content registered is a point and a jet:
- an explicit metric of `eq:metric`'s form (`γ = ψ = ½ log B`, `R = √(BC)`), namely
  `g = diag(−1, 1, B, C)` on `(t, z, x, y)` with `B = 1 + 2t + 5t² + z²` and `C = 1 + 2z − t² − 3z²`;
- whose 2-jet at the origin satisfies the Einstein–Λ equations `R_ab = Λg_ab` (`Λ = 3`) there;
- which depends on `z` (it is not the homogeneous Bianchi I member);
- and whose Weyl tensor at the origin is Petrov type I.

The jet was found by solving the field equations at the origin (sympy). They are linear in the second-order
coefficients, with one consistency condition `p₁p₂ = q₁q₂`. One free parameter was set to keep the three electric
eigenvalues distinct.

| Row | Statement | Lines | p | Note |
|---|---|---|---|---|
| K4a | The Christoffel table of `diag(−1, 1, B, C)`, and its full Riemann table at the origin. Eight nonzero `R_abab`: `R_txtx = −4`, `R_tyty = 1`, `R_zxzx = −1`, `R_zyzy = 4` and their symmetric partners, all others `0`. Hence `R_ab = 3g_ab` there | 200–320 | 0.6 | **The expected stop**: 256 Riemann components through the copied `kr_` kit, with the derivatives of the rational Christoffels at the origin |
| K4b | At the origin the Weyl operator is `ij_tbl u`, its dual traces vanish, and `I = 7`, `J = 3`: `I³ = 343 ≠ 243 = 27J²`, **type I**. The electric eigenvalues are `(1, −3, 2)`, distinct | 100–200 | 0.75 | Through the copied `ij_tr2`, `ij_tr3`, `ij_tr_dual` |

**The fallback:** K4a alone (the jet is vacuum at the point), with K4b's type-I step left NOT BEGUN. That would be
marked BUILT IN PART.

**Not formalised:**
- that an exact solution of the full Gowdy–de Sitter system realises this 2-jet. That is a Cauchy-problem statement,
  which the paper asserts (`sec:gowdy`: every Cauchy datum integrates);
- the word "generic". Type I is an open condition, but its density is not formalised.

**After K4,** per r7803: the closing table of the formalisation's standing, paper by paper.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
