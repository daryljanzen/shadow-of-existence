# `r7263+71.2` — RESULT: the first compiled statements in this project, and the one measurement before the `sinh^{2/3}` offer

*Read against `PREDICTION.md` in this directory, pushed at `r7263+71.1` before any Lean project existed, before
`mathlib`'s cache was fetched, and before `FirstOrderFriedmann` was read. The pre-registration is not revised.*

## ⛭ The milestone

***The first file this project has compiled is `computations/formalisation/lean/ShadowFormal/Nariai.lean`, the
horizon cubic's Nariai member. It built on its first attempt.***

| | |
|---|---|
| toolchain | `Lean (version 4.35.0-rc4, x86_64-unknown-linux-gnu, commit c29b6dda4f7c20e3eeaa717c4e565663c5cfa364, Release)`, installed by `elan` through this container's network policy |
| `mathlib4` | `4e6064a4a3a617a3ba6739b50152b02e4d6ad3ea` — the commit measured at `r7259+71.5`, pinned in `lakefile.toml` and `lake-manifest.json` |
| cache | `lake exe cache get` — `Already decompressed 9024 file(s)`, `cache exit=0` |
| build | `lake build` — `Build completed successfully (9043 jobs).` |

*The only warning is advisory: `imports Mathlib … designed for use with the module system; consider adding
module`.*

## The instrument, and why its green can fail

`computations/formalisation/lean/check_no_sorry.py`, run to completion here. Its verdict line:

```
VERDICT: ALL 14 THEOREMS COMPILE AND REST ON NO sorryAx -- the control's sorry was seen, so this reading can fail
```

- **What it does.** A theorem that type-checks is not yet evidence, because `sorry` type-checks too. So the
  checker reads `#print axioms` for every theorem (`Axioms.lean`). It reports `PROVED` only when a theorem's
  axioms are a subset of `{propext, Classical.choice, Quot.sound}`, and `STATED` when it rests on `sorryAx`.
- **Gate zero.** `controls/SorryControl.lean` proves `(1 : ℝ) = 2` by `sorry`. The checker must report it
  `STATED` before anything else prints, and it did: `control shadow_control_sorry -> STATED`. *A checker that
  cannot see a sorry it was handed is the "green on the work that broke it" class this project exists for.*

## ① The Nariai cubic — 4 of 4 compile, 4 of 4 proved

| # | theorem | compiles | proved | predicted proved |
|---|---|---|---|---|
| N1 | `discr_horizon : (horizon m).discr = 4 − 27 m²` | ✔ | ✔ | 0.9 |
| N2 | `discr_horizon_eq_zero_iff : … = 0 ↔ m = mN ∨ m = −mN`, with `mN = 2/(3√3)` | ✔ | ✔ | 0.8 |
| N3 | `nariai_factorisation : X³ − X + C mN = (X − C(1/√3))² (X + C(2/√3))` | ✔ | ✔ | 0.8 |
| N4 | `nariai_double_root : rootMultiplicity (1/√3) … = 2` | ✔ | ✔ | 0.6 |

| quantity | central | band | measured |
|---|---|---|---|
| statements that compile | 4 | 3–4 | **4** ✔ |
| proved with no `sorryAx` | 3 | 2–4 | **4** ✔, above central |
| cache fetched | yes, 0.75 | — | **yes** ✔ |

*N2 is the corpus's sentence "the Nariai member is the discriminant's zero", now a theorem about mathlib's own
`Cubic.discr`. The file says in its header what it does not state: that the merged root is a horizon, that the
collapse selects this member, that `α` is the throat. Those are readings of the algebra, and none is claimed.*

## ② I20 stated as what it computes — the identity SEPARATES, and two of its checks are one proposition

*`ShadowFormal/I20.lean`. The geometric theorem I20 is filed under is written in the module docstring, with the
five missing layers named, and is not stated, because nothing can state it. Each of the ten checks is a
theorem whose docstring says which part of that theorem it does not reach.*

| I20 check | Lean theorem | form of its proof | predicted |
|---|---|---|---|
| ① `L_ξ g = 2(a′/a) g` | `lie_eta_component` | `HasDerivAt.pow`, then `field_simp`: **the one with content** | content ✔ |
| ② not exact Killing | `not_killing_witness` | **needs a witness** (`a = exp`, `η = 0`) that the receipt's `!= 0` never supplied | witness ✔ |
| ③ `ξ·p = −C` | `charge_on_asserted_input` | `field_simp` **on the asserted input `p^η = C/a²`** | trivial ✔ |
| ④ `ω = C/a` | `omega_eq` | `field_simp` | trivial ✔ |
| ⑤ `a·ω = C` | `a_omega_const` | `field_simp` | trivial ✔ |
| ⑥ `1+z = a_obs/a_em` | `one_plus_z` | `field_simp` — **no integration occurs** | trivial ✔ |
| ⑦ `ln(1+z) = … = ∫H dt` | `log_ratio` | **`Real.log_div`, and `H` appears nowhere in the statement** *(read at source: `Real.log (a_obs / a_em) = Real.log a_obs - Real.log a_em`)* | trivial ✔ |
| ⑧ control: momentum ∝ `1/a` | `control_momentum` | **its proof is `a_omega_const` — the same proposition as ⑤** | trivial ✔ |
| ⑨ control: `a·E` not constant | `control_massive_witness` | **needs a witness** (`a = exp`, `C = m = 1`) | witness ✔ |
| ⑩ control: massless limit | `control_massless` | `Real.sqrt_sq_eq_abs`, `abs_of_pos`, `field_simp` | witness ✘ — *trivial* |

| quantity | central | band | measured |
|---|---|---|---|
| trivial on the asserted input or one library lemma | 6 | 4–8 | **7** ✔ (③④⑤⑥⑦⑧⑩) |
| need a witness the receipt never supplied | 3 | 2–4 | **2** ✔ (②⑨) |
| carry content as computed | 1 | 1–2 | **1** ✔ (①) |

- **A finding the Python could not show: two of I20's ten checks are one proposition.** ⑧'s Lean proof is
  ⑤'s theorem. The receipt files one statement under two titles, one of them "CONTROL".

⛔ **The reachable negative: it did NOT fire, and the price of that is stated rather than hidden.** ① separates
from the geometry. Its Lean form is a statement about `deriv` of the metric's components, with no Lie derivative
in it, and the claim that the expression *is* `𝓛_ξ g` is layer 2, written as a comment.

***The separation is not free.*** The receipt's own formula has three terms. Two vanish because `ξ` is constant
and because `g` does not depend on `x`. Those two facts are properties of the coordinate chart, which cannot be
stated without layer 1, so **`lie_eta_component` keeps only the surviving term, and its docstring says so.** So
the 82 per cent stands as a gap between two claims, as `r7259+71.5` reported it. It is a gap that can be written
down exactly, and here it is.

## ③ Physlib's `FirstOrderFriedmann` — NON-STUB, as predicted (0.75)

*Read at source in `Physlib` `b0e7ca1c`, `Physlib/Cosmology/FLRW/Basic.lean`.*

```lean
def FirstOrderFriedmann (a ρ : Time → ℝ) (k Λ G c : ℝ) (t : Time) : Prop :=
    ((∂ₜ a t / a t)^2
      = ((8 * Real.pi * G) / 3) * ρ t - k * c^2 / (a t)^2 + Λ * c ^2/ 3)
```

Each of its dependencies traced, to `mathlib` or to a `sorry`:

| name | defined at | reaches `sorry`? |
|---|---|---|
| `Time` | `Physlib/SpaceAndTime/Time/Basic.lean` l.33 — `structure Time where val : ℝ` | no — the file has 0 `sorry` |
| `∂ₜ` | `Physlib/SpaceAndTime/Time/Derivatives.lean` l.79 — `scoped notation "∂ₜ" => deriv` | no — it is `mathlib`'s `deriv` |
| `Real.pi` | `mathlib` | no |
| `FLRW` | l.101 — `@[sorryful] def FLRW : Type := sorry` | **yes, and it is not referenced:** `FirstOrderFriedmann` sits in `namespace FLRW.FriedmannEquation`, which is a namespace and not a use of the type |

*And Physlib already proves solutions against it with no `sorry`: `Cosmology/FLRW/Solutions.lean` has 0
`sorry` and proves `deSitterScaleFactor_firstOrderFriedmann` and the flat power laws.* ⇒ **The `sinh^{2/3}` law
is statable against `FirstOrderFriedmann` as it stands.** The offer is one result, not a foundations project. It
is not started here, because it is not ordered.

## What is in the tree

`computations/formalisation/lean/` — `lakefile.toml`, `lean-toolchain`, `lake-manifest.json`,
`ShadowFormal.lean`, `ShadowFormal/Nariai.lean`, `ShadowFormal/I20.lean`, `Axioms.lean`,
`controls/SorryControl.lean`, `check_no_sorry.py`. `.lake/` is ignored.

**To reproduce:** with `elan` installed, `lake exe cache get && python3 check_no_sorry.py` from that directory.
*CI has no Lean toolchain, so this is not a CI gate yet. Wiring it would mean `elan` and the mathlib cache in a
workflow job. That is this seat's gate to design, and it is offered rather than done, because it adds minutes
to every push.*
