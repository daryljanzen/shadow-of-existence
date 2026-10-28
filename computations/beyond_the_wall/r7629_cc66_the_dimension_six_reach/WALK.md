# `r7629+cc66` — the walk: `PO-89` ⒜ is out of reach, but the threshold is not vacuous

## What the order asked, and the one place I changed the question

Three steps: size the dimension-six term on each observable, set each against current precision, and
either fire the exit or name the observable that could fix the value.

⚠ **The order asks for the suppression as "a power of the curvature against the cutoff", and `Λ` is
exactly what `r7627` established the construction does not fix.** So *"the term lies below current
precision"* is not a computable statement — it is a statement about an assumed cutoff. A row that
picked a Planckian `Λ`, found `10⁻²⁷` and declared victory would be reporting its own choice.

⇒ **So the deliverable is a threshold.** For each observable, the `Λ*` at which the term would *reach*
that observable's measured precision, with the exit reported as the inequality `Λ > Λ*`.

```
delta  =  c · (E/Λ)^(d−4)          Λ*  =  E · (c/sigma)^(1/(d−4))          c = 6023/20160
```

## The result

| observable | `E` (GeV) | `σ` | **`Λ*`** |
|---|---|---|---|
| the rate `H₀` | `1.44e−42` | `1.0e−2` | `7.9e−42` GeV |
| **the acoustic scale** | `2.6e−10` | `2.9e−4` | **`8.345 eV`** |
| the tilt `n_s` | `2.6e−10` | `4.4e−3` | `2.14 eV` |
| the tensor amplitude | `2.6e−10` | `3.2e−2` | `0.7944 eV` |

**The acoustic scale binds**, because it couples a recombination-era energy to the tightest fractional
precision of the four. And against candidate cutoffs:

| cutoff | orders above `Λ*` | the term is |
|---|---|---|
| Planck | `+27.2` | hidden |
| GUT | `+24.1` | hidden |
| weak | `+10.1` | hidden |
| `1 GeV` | `+8.1` | hidden |
| **`1 eV`** | **`−0.9`** | **visible, at ~70× the acoustic precision** |
| CMB temperature | `−4.6` | visible |

⇒ **The exit fires for `Λ` above a few eV** — an atomic scale or higher — and at `1 GeV` and above the
margin is `8` orders of magnitude or more, with **no** observable within ten times its precision. The
order's named reachable negative is missed at every cutoff from `1 GeV` up.

## ⚠ But the threshold is not vacuous, and that is the part worth reporting

**A `1 eV` cutoff does not hide the term.** It sits `0.9` orders *below* the binding `Λ*`, and there the
dimension-six correction would stand at about **70 times** the acoustic scale's measured precision. So
the exit is a real condition, not a formality: it requires `Λ ≳ 8 eV`.

⌗ **An earlier draft of this row claimed the exit failed "only for a cutoff below the CMB temperature,
which is not a cutoff any construction could mean."** That was **false**, and the arithmetic in my own
table said so: `Λ*` is `4.6` orders of magnitude *above* the CMB temperature, and `1 eV` lies between
them. The correction is printed in the computation's own output rather than quietly dropped, because
the margin **is** the result. *This is the fourth time in two rows that my prose overran what my
numbers showed, and the first time I caught it from the table rather than from a gate.*

## The controls

1. **The order's named control — a dimension-four quantity the same estimate sizes correctly.** The
   estimator takes the operator dimension as a **parameter**, so this is its own bookkeeping being
   checked rather than a sentence about it: at `d = 4` it returns an *unsuppressed* correction
   (exponent `0`), which is why the dimension-four terms are the ones these observables actually
   measure; at `d = 6` exactly two powers of `E/Λ`.
2. **A real dimension-six case with a known cutoff**, so the `(E/Λ)²` form is validated where the
   answer is independent: the Fermi four-fermion operator at the muon mass, `(m_μ/m_W)² = 1.7e−6` —
   the right order for a weak-scale dimension-six operator.
3. **The three parts reproduce the stated total**: `−⅓·197131/6720 + 367/48 + 389/160 = 6023/20160`
   exactly, so the coefficient is carried and not retyped.
4. **Every measured precision quoted with its observable and how it is quoted**, and the conclusion
   reported in orders of magnitude so a factor of a few in any of them cannot move it.
5. **Candidate cutoffs carried explicitly**, so "far below" is measured against something.

## What this row does not claim

- **It does not supply a cutoff.** Every line is conditional on `Λ`, and the exit is an inequality.
- The **tensor amplitude** enters as an *exclusion* (`r < 0.032`), not a measurement, so its threshold
  is the weakest of the four and is reported apart rather than averaged in with three measured ones.
- The **tilt's characteristic energy** is the least well defined of the four — a property of the
  primordial spectrum, and which energy the construction reads it at is a reading. It is carried at
  the recombination scale and is not the binding observable either way.
- **`6023/20160` is an obstruction to covariance, not an invariant's coefficient.** The carrier is not
  covariant from inside, so "the dimension-six term" here means the magnitude whose non-covariant
  split between the reduction and the truncation is itself `PO-89`'s stated limit — which is exactly
  why ⒜ is the whole of the exit.
