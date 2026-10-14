# `r7317+71.6` — PRE-REGISTRATION: the `4D` curvature engine, as `r7317` ② orders. THE Levi-Civita connection's curvature, in closed form, for ANY diagonal metric on `ℝ⁴` whose coefficients depend on every coordinate, plus the contractions, behind an interface a second seat can use without opening a proof. ⌗ Predicted `150` lines (band 80–350), stop at `400`, and the comparison `r7317` ③ asks for is registered here before any of it is built

*Written after B's RESULT (`../r7315_71_sweep/RESULT.md`) and before any Lean for this item. **What B already built is
named, and it is not counted here.** Unit: Lean lines that build, as `git diff --stat` insertions, as in B.*

## What exists, and the one gap

- From `B13`, `lcGam_diag4` gives the Christoffel form of any diagonal `ℝ⁴` metric. It already allows coefficients in
  every coordinate.
- From `B15`, `curv_T` gives the curvature in closed form, but only when the coefficients depend on `t` alone.
- ***The gap:*** the curvature when the coefficients depend on several coordinates. Its closed form needs the second
  partials `∂ᵢ∂ⱼ cₖ` and the symmetry of second derivatives (`ContDiffAt.isSymmSndFDerivAt`, already used in `B12`).
- That gap is what B stopped on: row 2's open slicing in a horospherical chart, Gowdy-dS in `(t, z)`, and the
  foliation rows.

## The item

| piece | what | predicted lines |
|---|---|---|
| E1 | `curvD`: THE connection's `R(u,v)w` on constant fields equals an explicit formula in `cₖ(p)`, `∂ⱼcₖ(p)`, `∂ᵢ∂ⱼcₖ(p)` | 90 |
| E2 | the contractions as definitions: `ricC`, `scalC`, `ric2C`, `riem2C` exist from B; add `weyl2C`, `gbC`, `einsteinC` | 15 |
| E3 | ***acceptance instance 1:*** row 2's `k = −1`, open FRW `−dt² + a(t)²(dw² + e^{2w}(dx² + dy²))`, `Weyl² = 0` for a free `a` | 30 |
| E4 | ***acceptance instance 2:*** row 74, the Gowdy-dS background in `(t, z)` (`C5`'s family), `G_ab` against its wave and constraint equations | 30 |
| total | | ***150*** (band 80–350) |

***E3 and E4 complete rows 2 and 74 of B's list.*** *They are counted in the engine, not as B discharges, and each is
also reported as its own marginal cost so the per-instance rate can be read.*

## ⛭ What the engine exposes — `r7317` ②'s question

***A second seat should need these five things and nothing else. In particular, not `lcConn`, `kosz`,
`curv_model`, `lcGam` or `koszK`.***
1. **The input:** `c : Fin 4 → (Fin 4 → ℝ) → ℝ`, with `∀ i p, c i p ≠ 0` and `∀ i, ContDiff ℝ ∞ (c i)`. Profiles that
   vanish somewhere are handled by B's convention: equal to the named one near the point, and the caveat carried.
2. **One theorem, `curvD`**, stating THE connection's curvature on basis fields as an explicit formula. The
   statement is the API; its proof is not read.
3. **The contractions** as definitions over a Riemann array and the diagonal `g`: `scalC`, `ric2C`, `riem2C`,
   `weyl2C`, `gbC`, `einsteinC`.
4. ***The recipe***, the same three lines every instance in B ended with:
   - state `cₖ(p)`, `∂ⱼcₖ(p)` and `∂ᵢ∂ⱼcₖ(p)` for the named metric as `simp` facts (usually from `HasFDerivAt`);
   - `simp [Fin.sum_univ_four, …]`;
   - `field_simp; ring`.
5. **`boxD`** for scalar fields (from `B13`), and the pp-wave engine (`B11`/`B12`) for the one non-diagonal family.

*Out of scope, and named so nobody assumes otherwise:*
- **non-diagonal metrics in general;**
- **the generic-metric identities** (rows 7, 58, 20, 6, 19, 71). Those are index algebra over an arbitrary `g`
  (contracted Bianchi, `C² = E₄ + 2(Ric² − R²/3)`), not curvature computations. They are a different item, and this
  one does not price them.

## ⛔ Stop rule and symmetric negative, scored first

| outcome | read |
|---|---|
| E1–E4 build in `≤ 400` | the engine lands |
| E1 alone exceeds `250`, or a symmetric-second-derivative step needs a `mathlib` port over `100` | ***STOP.*** *The engine is reported not worth its cost, and the instances go out as separate work, per `r7317` ③* |
| ⛭ symmetric negative: E1–E4 in `< 60` | *then `curv_T` was already the engine, and "the engine" was never a separate item. That is reported as what it is* |

## ⌗ The comparison `r7317` ③ asks for, registered before the build

| route | lines, on this seat's numbers |
|---|---|
| ***separately:*** the 8 engine-needing rows at `CANDIDATES.md`'s predictions (2, 74, 75, 79, 47, 102, 94, 52) | `2,550` |
| ***separately, as B actually ran:*** each instance building its own curvature, about `150` + `60` | `≈ 1,700` |
| ***engine first:*** `150` + the remaining 6 at about `60` each | ***`≈ 510`*** |

***If the engine's measured cost plus the measured E3/E4 marginals implies a route above `≈ 1,700`, the engine loses,
and I will say so.***

## My probabilities

| quantity | p |
|---|---|
| E1–E4 land `≤ 400` | 0.75 |
| within `2×` the central `150` | 0.65 |
| symmetric negative (`< 60`) | 0.10 |
| E3 and E4 each `≤ 60` marginal, once E1 exists | 0.6 |

## Not done here

- No Lean is written for this item until it is ordered.
- B's remaining 18 candidates stay "statable, connection carried as a hypothesis" until then.
- Nothing in the quote-pin stride.
