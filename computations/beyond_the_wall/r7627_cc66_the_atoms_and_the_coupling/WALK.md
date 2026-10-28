# `r7627+cc66` — the walk: what the atoms form, and why the near-misses are not evidence

## The shape of the answer

The order asked three things. The answers, in order:

**1. Enumerate the dimensionless numbers the atoms form.** Under the rule frozen in `PREDICTION.md`
— products of integer powers with `Σ|exponent| ≤ D`, deduplicated **by value and not by spelling** —
the `15` frozen atoms give

| `D` | `N` distinct values |
|---|---|
| 1 | `30` |
| 2 | `374` |
| 3 | `2481` |
| 4 | **`11049`** |

**2. What a mechanism needs.** A **reference scale** at which the coupling is quoted, and a
**matching condition** saying that some particular number *is* the coupling there.

**3. Whether the construction supplies it.** No, on both counts, and for a reason underneath both.

## ⛭ THE RESULT THAT MATTERS, AND IT IS THE CONTROL AND NOT THE HIT

The order's named negative was *"a number formed from the data lands near the measured strong
coupling."* **One does.** The closest is

```
0.117893   =  (β/α)⁻¹ · 60 · 81⁻¹        against  α_s(M_Z) = 0.1180 ± 0.0009      −0.09%
```

a tenth of a per cent from the measured value, inside its experimental error. **Quoted alone it would
look like a find.** It is not one, and the row's own control says so:

| target | window | observed | **expected by chance** | ratio |
|---|---|---|---|---|
| `α_s(M_Z)` | ±1% | `12` | **`13.26`** | **`0.91`** |
| `α_s(M_Z)` | ±5% | `71` | `66.45` | `1.07` |
| `1/g²(M_Z)` | ±1% | `12` | **`13.73`** | **`0.87`** |
| `1/g²(M_Z)` | ±5% | `77` | `69.05` | `1.12` |

⇒ **The atoms hit `α_s` no better than they hit a number drawn at random from the same two decades
— slightly worse, in the tight window.** `4000` random targets set the expectation. So the finding is
not "a number comes close": it is that **coming close carries no information at this density**, and a
row reporting the `−0.09%` without the `13.26` would have reported noise as a result.

⌗ *This is the `r7615` lesson inverted. There the fault was a test that could not fail; here it is a
test that could not help but succeed. The guard is the same guard: say in advance what the test would
have to show, and count the ways it could succeed by accident.*

## And the reason underneath, which is dimensional rather than numerical

The enumeration could have come back with `0.9` or with `1.4` and it would not have mattered, because
**a gauge coupling is an action normalisation and the atoms are geometry.**

The toy control is what makes this precise rather than rhetorical. Kaluza–Klein on a circle:

```
1/g₄²  =  2πR / g₅²  =  12.566371        [determinate]
```

and what makes it determinate is **not** the geometry. It is `g₅²` — an independent **dimensionful**
datum, the five-dimensional action's own normalisation. Strip it and keep only `R`, and `1/g₄²` is not
a number at all. ⇒ **The construction's data are lengths, integers and spectral ratios, with no
independent dimensionful coupling for a gauge field.** So no monomial in these atoms is a coupling
*whatever its value*, which is exactly why question ② came back uninformative instead of coming back
empty.

## The three failures, each with its own measurement

- **No absolute scale.** `α` is symbolic end to end — `r7615`, `r7619` and `r7621` all declare it so —
  and every atom is dimensionless or a ratio of the two lengths. A coupling is quoted *at an energy*;
  a set of pure ratios names no energy.
- **No running interval, even on the construction's own scales.** `r7621` measured `Λ = 1/(2πα)`
  *below* the gap `5/(2α)`, with zero modes between: `Λ/μ = 1/(5π) = 0.063662 < 1`.
- **No matching condition.** Nothing in the data picks *which* of the `11049` numbers, or where.

## What was checked that could have gone the other way

- **The enumeration can miss**: targets at `10⁻³⁰` and `10³⁰` return **`0`** hits each. A counter that
  cannot miss counts nothing.
- **The positive control**: `β/α = 2π` is in the set and determinate, so "no coupling comes out" is not
  the machinery failing to produce numbers.
- **Dedup by value, not spelling.** Counting spellings would have inflated `N` and *flattered* the
  chance-hit control — the direction that favours a hit. It is counted the other way on purpose.

## ⌗ The cost of the first attempt, recorded because it was mine

The first enumerator swept the full exponent grid, `(2D+1)^15 = 9^15 ≈ 2×10¹⁴` products at `D = 4`. It
did not finish and had to be killed. The monomials with `Σ|e| ≤ 4` number `11049`; the grid containing
them is ten orders of magnitude larger. **The fix was to recurse over the support** — which atoms carry
a nonzero exponent — rather than over the grid. The reason sits in the function's own docstring.

## Where this row is open, and it is the atom list

Whether "the integers" is **closed** is a reading of what the construction posits, not a computation.
`27` and `81` are derived group orders; `5` is a dimension; `20` and `60` are multiplicities at `k = 1`
and `k = 2` and the sequence continues. ⇒ **The enumeration is bounded by my choice of `D` and by my
choice of where the multiplicity list stops, and neither bound is the construction's.** Two things make
that honest rather than fatal: the chance-hit ratio is flat in `D` by construction (both counts scale
with `N`), and the dimensional argument does not depend on the list's length at all — adding atoms adds
geometry, and geometry is the thing that cannot be an action normalisation.
