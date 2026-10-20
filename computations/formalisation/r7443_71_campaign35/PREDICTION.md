# `r7443+71.15` — PRE-REGISTRATION: campaign 35, library-gap row 64 (the descent is free at the order the section works at). ⌗ `330` lines (band 180–700), ⛔ stop `1000`. ⌗ p `0.50`

*Under `r7443` ②, step 4, next in `PRICING.md`'s order. The receipt is
`P10_the_descent_is_free_at_the_order_the_section_works_at_and_the_kernel_rotates_rather_than_failing.py`. No Lean
was written before this registration.*

## ① The piece: `probes/Row64Descent.lean`

The receipt's computed checks are sections A–D as `PRICING.md` lists them.
- ***A.*** The rank of `(f₁, f₂, f₃)` is `2` on a four-point spectrum and `1` on a one-point spectrum, with
  exhibited nullspaces. The phase is absent from `⟨ψ|diag(1,4)|ψ⟩` and present in `⟨ψ|σ_x|ψ⟩`.
- ***B.*** On closed FRW `α cosh(T/α)`: `R = 4Λ`, `Ric² = 4Λ²`, `Riem² = 8Λ²/3`, and `λ₀ = λ₁ = Λ`. On the
  deformation:
  - `R = 4Λ + εν/a⁴`;
  - the four dimension-six invariants are `(64, 16, 32/3, 4)Λ³`;
  - the first-order shifts are `(3/4)(ν/a⁴)` times order zero over `Λ`;
  - the ranks by order are `1, 1, 2`.
- ***C.*** `L = 15/4`, the convention kernel's rank `2` and kernel dimension `1`, the anomaly-dependent kernel entry,
  and its ratio and divergence as `ε → 0`.
- ***D.*** The rank survives an extra `A₆` factor.

Each check is built as the receipt computes it: ranks by an exhibited minor plus an exhibited kernel, and limits as
`Tendsto`.

***Caveats, registered.***
- ***Imported:***
  - the TT weights;
  - the closed-FRW formulas for `λ₀`, `λ₁` and `Riem²` in the receipt's typed form. Where cheap, they are tied to
    the engine; where not, that is said;
  - the forms of `f₁`, `f₂` and `f₃`.
- The paper-text check is a pin.

***Failable:*** BUILT, BUILT IN PART (per section), or REPORTED. p `0.50`.

***Census if BUILT:*** row 64 → `DONE`, its imports named, `decl` filled in the same push.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
