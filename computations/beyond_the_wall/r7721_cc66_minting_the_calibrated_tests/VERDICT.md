# `r7721+cc66.2` VERDICT — the `(ℓ, k)` separability measurement

**10 of 10 gates, 0 failures.** Read exactly as registered in `PREDICTION_separability.md`, under all four
of its amendments. Output in `separability_output.txt`.

---

## ⛭ THE RESULT, AND ITS OWN BASELINE BESIDE IT

| the SAME statistic, the SAME four banked spectra | correlation | cond | VIF |
|---|---|---|---|
| **COLLAPSED** — `Σ_k` taken, the route `r7719` closed | **`−0.9518`** | `6.36` | **`10.63×`** |
| **UN-COLLAPSED (A)** — same integer `ℓ`, **no interpolation** | **`+0.0031`** | `1.00` | **`1.00×`** |
| **UN-COLLAPSED (B)** — common `q`, `cr` kernel interpolated | `−0.0008` | `1.00` | `1.00×` |
| *registered threshold* | *`≤ 0.70`* | | *`≤ 2.0`* |

⇒ **The degeneracy that closed the collapsed route is not merely dented in the `(ℓ, k)` plane; it is
gone.** `10.63×` variance inflation becomes `1.00×`, and both `ℓ` readings agree — the registered
condition for a verdict to exist at all.

⛭ **And it is NOT an artefact of the statistic.** Gate 3b feeds the *same* statistic the *collapsed* object
built from the *same* four spectra, and it still returns `−0.9518 / 10.63×`. ⇒ The near-orthogonality is a
property of the plane, and **un-collapsing the `k`-sum is what removed the degeneracy.** ⌗ *The `−0.9200`
from the real spectra stays in the record as that object's figure and no longer does work it cannot do —
it was never a measurement of this object.*

---

## ⚠ WHAT THE SEPARATING STRUCTURE LOOKS LIKE, AND WHY IT IS NOT GOOD NEWS ON ITS OWN

| | |
|---|---|
| `f_mimic` | `0.5111` — half of the kernel swap is reproducible by *some* source rescaling |
| `f_sep` | `0.8595` — the part that is not |
| leading singular component of the residual | `0.6294` of its norm |
| components holding 90 % of it | ⛔ **`142`** |

⇒ **The separating structure is NOT low-rank.** Ninety per cent of it is spread over `142` modes, so there
is no single clean direction to measure: a template fit that exploits this needs essentially the whole
plane, not one well-chosen summary statistic. ⌗ *That is the practical cost of the result, and it is the
part a reader is most likely to skip.*

---

## ⛔ WHAT THIS DOES **NOT** SAY — registered in advance, in §5, and not softened now

> Good conditioning is **NECESSARY AND NOT SUFFICIENT.** Item 2 returns a **CONDITIONING** result, never a
> **detectability** result, because the per-`(ℓ, k)` noise model a detectability claim needs **does not
> exist on this instrument.**

⇒ Licensed: *"the degeneracy that closed the collapsed route is broken in the `(ℓ, k)` plane."*
⇒ **NOT licensed:** *"the two swaps can be told apart in the data."* The second needs a noise model and
`142` modes' worth of it.

---

## The controls, since the verdict rests on them

| | |
|---|---|
| the banked combination through the banked code path | `0.000e+00`, byte-identical, against `1e-12` |
| the premise — the source swap IS a column rescaling | departure `2.098e-13`, **`0`** non-finite cells |
| the grid change — the collapse reproduces the banked spectrum | **`4.1800e-05`** against the registered `1e-3` |
| nothing dropped, so the collapse cannot move | difference **exactly `0`** |
| the dead set is a contiguous prefix at every `ℓ` | prefix runs `0` at `ℓ=243` to `119` at `ℓ=934` |
| no zero above each `ℓ`'s own prefix | `0` |
| the interpolation does not carry the verdict | it moves `\|corr\|` by `0.0023` against `0.6969` to the line |

`34211` dead cells are **masked at weight `0`, not dropped** — the fix amendment 3 forced.

---

## ⛔ THE RECORD THIS REVISION LEAVES, WHICH IS NOT FLATTERING

The registration needed **four amendments**, and **one gate failure refused an earlier run that had
already printed this same verdict as a clean PASS off an integrand with 94 % of its low-`ℓ` support
deleted.** Five instances of the recurring fault, all in one revision:

| | what was read as what |
|---|---|
| §1, at registration | the continuum integrand's pointwise rescaling read as the banked grid's |
| amendment 1 | representability (`G != 0`) read as contribution |
| amendment 2 | an unweighted plane read as the object that carries the integral |
| amendment 3 | the dead prefix at the top of the window read as the prefix at every `ℓ` |
| the price | the cost at the bottom of the window read as the cost over it |

⌗ *Three were caught before a statistic existed, which is what registering before computing is for. One was
caught by a gate — the first time in this revision. And one was a confident **correction** of a conservative
estimate into a wrong one, which is the instance worth remembering: a correction is a claim and takes the
same check as the thing it corrects.*

⚠ **Declared: amendment 4's control was added AFTER the verdict was first seen**, and amendment 3 was
written after I had seen a number. The threshold was fixed before any computation and is untouched in all
four amendments, so nothing I saw could move the line — but the ordering protection is partly spent and the
result should be weighted accordingly.
