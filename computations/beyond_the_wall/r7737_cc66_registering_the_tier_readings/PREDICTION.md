# `r7737+cc66` REGISTRATION — **HOW TIER 1 AND TIER 2 WILL BE READ, WRITTEN BEFORE EITHER EXISTS**

Order `r7737` items ① and ③.  ⛭ *Nothing is computed in this revision: 70 holds both builds.  The
deliverable IS the registration, and it is written now precisely so that the reading cannot be chosen
once the arrays are in hand.*  Item ② fires when Tier 1 lands.

⛔ **Both tiers were requested by this seat at `r7735`, so I am registering the reading of arrays I
asked for.** That is the case where a registration matters most, and it is why the licences below are
numbers and why every one of them has a declared outcome in both directions.

---

# PART A — TIER 1: **THE DISTANCE MAP'S SHAPE AGAINST ITS NORMALISATION** (order item ①)

## A.0 WHAT TIER 1 IS, AND THE NOTATION

70 rebuilds the four combinations with the *other arm's* `x0(eta)` **array** in place of a scalar
multiple of the source arm's.  Write `T[S_A, x0](l,k) = \int S_A(k,eta_A) j_l(k x0(eta_A)) d eta_A`,
and let `x0_B~` be arm `B`'s map read onto arm `A`'s time grid by the interpolation 70 declares.  Then

| object | what it is | where it comes from |
|---|---|---|
| `T[S_A, x0_A]` | the diagonal | `r7729`, already held |
| `T[S_A, xs x0_A]` | **the NORMALISATION-only swap** — the present cross term, `xs = D_M(B)/D_M(A)` | `r7729`, already held |
| `T[S_A, x0_B~]` | **the FULL map swap** | **Tier 1, new** |

and the three templates, in `r7733`'s log-and-weight convention (`M = P Dlk^2`, binned, the fit's own
contribution weights, dead cells at weight `0`):

```
    t_norm  = log M[S_A, xs x0_A] - log M[S_A, x0_A]       (= r7733's t_ker, unchanged)
    t_map   = log M[S_A, x0_B~]   - log M[S_A, x0_A]
    t_shape = t_map - t_norm                               (zero iff the maps are proportional)
```

## A.1 ⛔ `S4` — THE REFUSAL, CHECKED BEFORE ANY STATISTIC IS FORMED

The hybrid built with `x0_B~ = x0_A` must return the diagonal **bit for bit** (`np.array_equal`), and
the recorded `xs` must still satisfy `xs(A->B) * xs(B->A) = 1` to `1e-12`.
⇒ **If either fails, NOTHING below is computed and the build goes back to 70.**  *This is the same
refusal shape as `r7721`'s gate `2c` and `r7733`'s bank closures: a verdict is not computed on an
object that has not identified itself.*

## A.2 `S1` — THE MAP'S OWN GEOMETRY, BEFORE ANY TEMPLATE

```
    F_shape = rms( x0_B~ - xs x0_A ) / rms( x0_B~ - x0_A )
```
over the time grid, on the support where the visibility is non-negligible — **and the support is
declared here as the `eta` range 70's own `SRCFIELD` saves, with no trimming of my own.**

* ⇒ **`F_shape <= 0.05`** licenses: *the two arms' maps are proportional to five per cent, so the
  present one-parameter cross term IS the map swap* — and `r7735`'s ③ **CLOSES** with the answer
  *normalisation*.
* ⇒ **`F_shape > 0.05`** licenses: the map carries shape the scalar cannot, and `A.3` decides.
* ⚠ **`F_shape` is a statement about the MAP, not about the template.**  It is reported first and
  separately for exactly that reason, and `A.3` is not skipped whatever it returns.

## A.3 `S2` — THE SPLIT IN TEMPLATE SPACE, WHICH IS WHAT THE VERDICT RESTS ON

In the fit's own weighted norm, at **both** registered binnings (`12` and `23` nodes per bin):
```
    R_shape = wrms(t_shape) / wrms(t_map)        R_norm = wrms(t_norm) / wrms(t_map)
```

| outcome | what it licenses |
|---|---|
| **`R_shape <= 0.20`** | the distance leg of the located step **is the NORMALISATION**; `r7735`'s ③ closes, and `r7733`'s `93.6` per cent stands as a statement about the distance ratio |
| **`R_shape >= 0.80`** | it **is the SHAPE**; the present cross term is then the wrong object for the multipole-structure claim, `r7733`'s `93.6` per cent is a statement about the normalisation only, and **`P15` owes a correction, which I will say plainly rather than soften** |
| **in between** | both terms contribute; ③ **narrows but does not close**, and the distance leg must be reported as two terms with their shares |

⚠ *Registered in advance: if the two binnings disagree across a boundary (one side of `0.20` or `0.80`
and the other not), **the disagreement IS the verdict** and neither reading is chosen — the same rule
`r7723` §3 set for the two nulls.*

## A.4 `S3` — THE MULTIPOLE STRUCTURE, WHICH IS THE CLAIM `P15` PRINTS

Using `r7733`'s own `structure.split()` and weights, unchanged and imported rather than reimplemented:
the `l`-structured rms fraction of `t_norm`, of `t_shape` and of `t_map`; then the fitted model's
`l`-structured variance apportioned among `t_norm`, `t_shape` and the sources' template.

* The figure to compare against is `r7733`'s **`93.6` per cent**, which `P15` prints.
* ⇒ **the normalisation's own share `>= 0.80` of what the whole distance leg carries** licenses: *`P15`'s
  sentence survives as printed.*
* ⇒ **below `0.80`** licenses: *the printed `93.6` per cent belongs to the distance leg as a whole and
  not to the normalisation, which is a correction to a printed sentence and is reported as one.*

## A.5 `S5` — THE INTERPOLATION, WHICH IS THE ONE PLACE TIER 1 CAN GO WRONG QUIETLY

70 chooses and declares how `x0_B` is read onto `eta_A`.  I will re-read the map under **a second
interpolation of my own, declared here as a cubic spline in `eta` with natural end conditions**, and
report how far `F_shape` and `R_shape` move.
* ⇒ **either moves by more than `0.05`** ⇒ the result is **interpolation-dependent** and is reported as
  that, not as a measurement, and the licences of `A.2`–`A.4` are suspended.
* ⌗ *This is registered because I asked 70 for the build and named this risk in the request; a risk
  named in a request and then not measured is a risk waved at.*

---

# PART B — TIER 2: **THE ACCEPTANCE LAW'S THREE-TERM EXCHANGE** (order item ③)

## B.0 WHAT TIER 2 IS

`G_l(k) = \int g j_l(k chi) d eta`, `W_l(k) = G_l^2 dk/k`,
`A_l = |\int W_l e^{2 i k rs*} dk| / \int W_l dk` — `P15` l.1823ff, three named terms: the visibility
`g`, the map `chi`, the comb period `rs*`.  70 supplies `G_l` on the four `(g, chi)` combinations with
`W_l`, `A_l` and each arm's `rs*`.

⇒ With `rs*` applied from either arm, the three terms give **`2^3 = 8`** settings.  The reading
registered here uses five: the control `(g_L, chi_L, rs_L)`, the three single-term swaps, and the full
swap.

## B.1 ⛔ `B0` — THE PRECONDITION, AND IT IS NOT A FORMALITY

**`A_l` is the comb's fractional amplitude. It is not the step.**  Before any term is credited with
carrying the located step's multipole structure, the located multipole must actually show in `log A_l`'s
own `l`-dependence.  Registered test: the step statistic `P15` already uses, read on `log A_l` across
the located transition's own window, against the surrogate null `r7721` registered.
* ⇒ **a transition at `p <= 0.01`** ⇒ `A_l` carries the step and `B.2` answers `PO-87`'s question.
* ⇒ **no transition** ⇒ **Tier 2 answers a DIFFERENT question than `PO-87`'s last step**, and I say so
  rather than reporting the term shares as if they were the answer.  *`PO-87` would then still be open
  and the next object would have to be named.*
⌗ *This is the session's recurring fault pre-empted: crediting a term measured on `A_l` with carrying a
step measured on the spectra would be a statement about one object read as a statement about another.*

## B.2 `B1` — THE THREE-TERM DECOMPOSITION, ADDITIVE OR NOT

Templates in log space against the control, weighted along `l` by the same contribution weights summed
over `k`:
```
    u_g   = log A_l(g_C, chi_L, rs_L) - log A_l(g_L, chi_L, rs_L)
    u_chi = log A_l(g_L, chi_C, rs_L) - log A_l(g_L, chi_L, rs_L)
    u_rs  = log A_l(g_L, chi_L, rs_C) - log A_l(g_L, chi_L, rs_L)
    v     = log A_l(g_C, chi_C, rs_C) - log A_l(g_L, chi_L, rs_L)      (the full swap)
```
Fit `v` on the three templates by weighted least squares with no intercept, exactly `four_cell.fit2`'s
shape extended to three columns.

* **`B1a` the interaction residual:** `wrms(v - (a_g u_g + a_chi u_chi + a_rs u_rs)) / wrms(v)`.
  ⇒ **`<= 0.20`** licenses *three independent terms* and `B1b`; **`> 0.20`** licenses only that the
  terms interact, and the shares are reported as a decomposition that does **not** close.
* **`B1b` the amplitudes:** each within **`0.10`** of unity for the additive reading to hold at unit
  weight.  Any amplitude outside that is reported as what it is — a term whose single swap does not
  predict its contribution in the full swap.
* **`B1c` the carrier:** the term with the largest `|a| * wrms(u)` is **the term that carries the
  retention**, reported **with the other two beside it** and with no claim that it is the only one.
  ⛔ *Registered: "largest" is not "only", and the licence is the ordering plus the three sizes, never
  a single name.*

## B.3 `B2` — THE MULTIPOLE STRUCTURE, TERM BY TERM — `PO-87`'s QUESTION AS WORDED

Of the `l`-structured variance of `v`, the share carried by each of `a_g u_g`, `a_chi u_chi`,
`a_rs u_rs` and their cross terms, by `r7733`'s `split()` and weights.
* ⇒ **one term above `0.60`** licenses: *that named term carries the located step's multipole
  structure*, which is `PO-87`'s last step **closed**.
* ⇒ **no term above `0.60`** licenses: the structure is shared, `PO-87` closes with a **two- or
  three-term** answer, and the shares are the answer rather than a name.
* ⚠ Conditional on `B0` passing.  If `B0` fails this section is **not** run.

## B.4 WHAT PART B DOES NOT CLAIM, REGISTERED NOW

* ⛔ Not that `A_l` is the step — that is `B0`, and it can fail.
* ⛔ Not that the three named terms exhaust the law — the factorisation `P15` states holds to
  `3e-15` for a *standing* oscillation, and whether the real source is standing to that accuracy on
  this arm is not tested by anything in Part B.
* ⛔ Not that Tier 2's `G_l` is the same object as `r7729`'s `Dlk` — `G_l` carries the visibility alone
  and `Dlk` the whole source.  Any comparison between them is a separate measurement and is not made
  here.
* ⛔ And **not** that Part A's answer transfers to Part B: `chi` appears in both, but `A.3`'s
  `t_shape`/`t_norm` split is on `Dlk` and `B.2`'s `u_chi` is on `A_l`.  *Two objects, two statements.*

---

# WHAT HAPPENS IF NEITHER TIER LANDS

⇒ Then `r7735`'s ③ stays open with the words it already has, this registration stays unspent, and
nothing here is quietly repurposed onto the four arrays I already hold — which cannot answer any of it,
for the structural reason `r7735` §1 established.
