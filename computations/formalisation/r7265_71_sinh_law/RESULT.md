# `r7265+71.2` — RESULT: the `sinh^{2/3}` law PROVES against Physlib's Friedmann equations, both of them; the run records; and the Lean CI job

*Read against `PREDICTION.md` in this directory, pushed at `r7265+71.1` before the Physlib project existed. The
pre-registration is not revised. The raw run is `RUN_RECORD.txt` beside this file: toolchain, every dependency
revision, the full `lake build` output and the checker's full stdout. It was written by
`computations/formalisation/record_run.sh` from a clean rebuild of the project's own build products.*

## ① The law — states, compiles and PROVES, for L1 and for L2

*`computations/formalisation/lean-physlib/ShadowPhys/SinhLaw.lean`, imports `Physlib.Cosmology.FLRW.Basic` at
`b0e7ca1c` — Physlib's own definitions, not copies. Toolchain `v4.34.1` and `mathlib` `d13f23b`, both Physlib's
pins.*

```
a(t) = A · sinh^{2/3}((3/2) · √(Λ/3) · c · t),     ρ(t) = (Λ c² / 8πG) · A³ / a(t)³,
for A, Λ, G, c > 0 and t > 0.
```

| theorem | states | compiles | proves | predicted proves |
|---|---|---|---|---|
| **L1** `firstOrderFriedmann_scale : FirstOrderFriedmann (scale A Λ c) (density A Λ G c) 0 Λ G c t` | ✔ | ✔ | ✔ | 0.75 |
| **L2** `secondOrderFriedmann_scale : SecondOrderFriedmann (scale A Λ c) (density A Λ G c) (fun _ => 0) Λ G c t` | ✔ | ✔ | ✔ | **0.5** |
| `deriv_scale`, `deriv_deriv_scale` (the two derivatives, through Physlib's `Time.deriv_eq_of_hasDerivAt`) | ✔ | ✔ | ✔ | — |

**Checker verdict** (`lean/check_no_sorry.py lean-physlib`, run here, quoted from `RUN_RECORD.txt`):
`VERDICT: ALL 4 THEOREMS COMPILE AND REST ON NO sorryAx -- the control's sorry was seen, so this reading can fail`.
*Gate zero passed: the project carries its own planted `sorry`, and it read `STATED`.*

- **No `mathlib` lemma was missing.** The proof used `HasDerivAt.rpow_const`, `Real.rpow_sub_one`,
  `Real.rpow_mul`, `Real.cosh_sq` and `HasDerivAt.congr_of_eventuallyEq`. L1 built on its first attempt; L2
  needed two tactic fixes (`Pi.div_apply`, and a rewrite order), and neither was a missing fact.
- **What the theorems hold for:** `t > 0`. At `t = 0` the scale factor vanishes and the density is
  unbounded, so the branch point is outside the statement. That is the hypothesis, said where it is used.
- **Physlib built from source: 11 modules** (band 10–150, central 40). *`lake` compiled exactly the import
  closure of `Physlib.Cosmology.FLRW.Basic`, and mathlib came from its cache.*

## ⛔ The reachable negative: its CONDITION fires, and the pre-registered argument says its CONCLUSION does not

*The order: "if the `sinh^{2/3}` law PROVES in `mathlib` plus `Physlib` as they stand, with no new foundation and
no `sorry`, then STATEMENT DISCIPLINE was the wrong frame … and the 82 per cent is a fact about the GEOMETRIC
receipts specifically rather than about the corpus."*

***The condition is met, exactly as written: L1 and L2 both prove, with no new foundation and no `sorry`.*** *So
the letter of the negative fires, and this result says so first.*

***Pinned at `+71.1`, before the run: if it proves, this seat would argue the conclusion does not follow.*** The
argument, now with the run behind it:

1. **`FirstOrderFriedmann` is already a coordinate shadow.** It is Einstein's equations reduced to a scale
   factor. The metric it reduces is, in this same Physlib commit, `def FLRW : Type := sorry`, and Physlib's
   header says the curvature of the FLRW metric is "not available yet". *Read at source:
   `Physlib/Cosmology/FLRW/Basic.lean` l.101 and `Solutions.lean`'s overview.*
2. **So what proved is the shadow, and the theorem it stands for still cannot be stated:** "the flat FLRW metric
   with this `a` solves Einstein's equations with Λ and dust". *That sentence is written in `SinhLaw.lean`'s
   header as what is not stated. It is the I20 pattern again: a true identity filed under a theorem nothing can
   state, here inside another project's library rather than this corpus.*
3. **The half of the negative's conclusion that the run does support:** proving is cheap where the claim is the
   shadow. *Both seats expected that, since the law is in the 79 per cent algebraic slice.* **The half it does
   not support:** that the 82 per cent is "about the geometric receipts specifically" in a way that excuses the
   algebra. *Physlib's own solutions — de Sitter, the power laws, and now this one — are all shadows of the same
   unstated statement. The gap is not a property of this corpus's receipts; it is where the libraries stop.*

*Adjudication is the gate's. What this seat claims is narrower: the run does not distinguish "proving was the
right frame" from "statement discipline is the right frame and this was its cheap case", because the statement
that would distinguish them is the one that cannot be written.*

## ② The Lean CI job — WRITTEN, path-scoped, and its runner time is measured on this push

*Two workflow files, so `gates.yml` is untouched and each project is gated only by pushes that touch it:*

| file | triggers on | steps, each timed into the log |
|---|---|---|
| `.github/workflows/formalisation-mathlib.yml` | `computations/formalisation/lean/**` | elan · `lake exe cache get` · `check_no_sorry.py lean` |
| `.github/workflows/formalisation-physlib.yml` | `computations/formalisation/lean-physlib/**`, `lean/check_no_sorry.py` | elan · `lake exe cache get` · `check_no_sorry.py lean-physlib` |

*The runner times are the first push's own `TIMING` lines and are reported in the reply that follows them. The
placement rule pre-registered at `+71.1` ② stands: over 15 minutes, the job moves to a schedule.*

## ③ The run records — committed

| record | of | wall of the clean rebuild | verdict |
|---|---|---|---|
| `r7263_71_first_statements/RUN_RECORD.txt` | `lean/` (mathlib `4e6064a4`, Lean `4.35.0-rc4`) | 36 s | `ALL 14 THEOREMS COMPILE AND REST ON NO sorryAx` |
| `r7265_71_sinh_law/RUN_RECORD.txt` | `lean-physlib/` (Physlib `b0e7ca1c`, mathlib `d13f23b`, Lean `4.34.1`) | 11 s | `ALL 4 THEOREMS COMPILE AND REST ON NO sorryAx` |

⚠ ***And one thing I broke and repaired while making them, reported because it nearly cost a day.*** *The first
draft of `record_run.sh` ran `lake clean` to force a real rebuild. That invalidated mathlib's cached build here
and started a from-source rebuild of mathlib. I stopped it, restored the cache (`Decompressed 7894
already-cached file(s)`), and changed the script to remove only the project's own `.lake/build`. That change is
commented in the script. No result depends on the aborted run.*
