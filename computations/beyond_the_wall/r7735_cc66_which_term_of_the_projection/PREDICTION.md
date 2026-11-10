# `r7735+cc66` REGISTRATION — **WHICH NAMED TERM OF THE ACCEPTANCE CARRIES THE LOCATED STEP'S MULTIPOLE STRUCTURE**

Order `r7735` item ①, registered before a line of the computation exists.  ⛭ *The order asks for the
projection's contribution to be split into the acceptance law's named terms.  **Reading 70's builder
before registering a split showed that the object `r7731` called "the projection's contribution" has
exactly ONE term in the arrays I hold, and it is not any of the law's.**  That is §1, it is a CODE
READING and not a measurement, and it is what the rest of this registration is built on.*

---

## ① THE PREMISE — A CODE READING, STATED AS ONE, AND NOT MEASURED HERE

`computations/beyond_the_wall/r7729_70_dlk_build/project4.py` builds the four combinations at its
lines 139–146:

```
srcs = {'cr':   dict(S=C['S'][:, sel], eta=C['eta'], x0=C['x0'], D_M=C['D_M'], ns=C['ns']),
        'lcdm': dict(S=S_l,            eta=L['eta'], x0=L['x0'], D_M=L['D_M'], ns=L['ns'])}
for s, kr in COMBOS:
    src = srcs[s]
    combos[f'S_{s}__K_{kr}'] = dict(S=src['S'], eta=src['eta'], x0=src['x0'], k=kg,
                                    xs=A[kr]['D_M'] / src['D_M'], ...)
```

and the transfer is `np.trapezoid(S * spherical_jn(l, k * (xs * x0)), ee, axis=0)`.

⇒ *** THE SOURCE INDEX CARRIES `S`, THE `eta` GRID, THE DISTANCE MAP `x0(eta)` AND THE TILT `n_s`.
THE KERNEL INDEX CARRIES ONE SCALAR: `xs = D_M(kernel arm) / D_M(source arm)`. ***

70's own registration says so in words — *"`SRCXS`'s definition of **the same source through the
other arm's distance**"* (`r7729_70_dlk_build/PREDICTION.md` l.20).  And the blob's own `meta` carries
the four values:

| combination | `xs` |
|---|---|
| `S_lcdm__K_lcdm`, `S_cr__K_cr` | `1.0` |
| `S_lcdm__K_cr` | `1.0128706132848382` |
| `S_cr__K_lcdm` | `0.9872929344419445` |

⛔ **TWO CONSEQUENCES, BOTH ABOUT NAMES, AND THE SECOND IS ALREADY IN PRINT.**

1. **`r7731`'s "kernel difference" is the arms' DISTANCE RATIO and nothing else** — a one-parameter
   object.  There is no second term in it to split off, so the order's split cannot be performed on
   these four arrays *at all*, and not because they are too coarse.
2. **`r7731`'s "source difference" is not a source difference.**  It swaps the source field, the
   `eta` grid, **the distance map `x0(eta)`** and the tilt, together.  So the acceptance law's own
   named mechanism — the visibility's extent in `chi` — sits in the leg called "the source", while the
   leg called "the projection" moves that extent by `|xs - 1| = 1.287` per cent.

## ② WHAT THE LAW'S NAMED TERMS ARE, IN `P15`'s OWN WORDS

`corpus/CR_cosmology.tex` l.1823ff states the law with no fitted coefficient:

> `Delta_l(k) = cos(k rs*) k^((1-n_s)/2) G_l(k)` with `G_l(k) = \int g j_l(k chi) d eta`,
> `W_l(k) = G_l(k)^2 dk/k`, and `A_l = |\int W_l e^{2 i k rs*} dk| / \int W_l dk`,
> *"built from the window the kernel reads and the comb's period, both of them the background's own"*.

So the named terms are exactly three, and the paper reads the law physically through the first:

| term | what the paper measures of it |
|---|---|
| **`g`**, the visibility weight in `eta`, and its extent in `chi` | *"this arm's visibility is the `15.5` per cent wider in `chi`"*, which is *"why it retains more"* |
| **`chi(eta)`**, the distance map the Bessel argument reads | its endpoint is `D_M`; the acceptance it induces spans `4.43` of acoustic phase against `5.14`, `13.73` per cent narrower |
| **`rs*`**, the comb's period | *"accumulating the same sound horizon to `0.36` per cent"* |

⇒ **The kernel index of §1 touches none of these.**  It multiplies the source arm's own `chi(eta)` by
a scalar, which moves the extent in `chi` by `1.287` per cent where the arms differ by `15.5`.

## ③ WHAT IS REGISTERED AS MEASURABLE ON THE FOUR ARRAYS I HOLD

⛔ **The premise of §1 is NOT measurable here** — confirming it would mean rebuilding the transfers,
which needs the fields.  It is a reading, and it is labelled one.  What the arrays can carry is the
premise's *consequences*, and these are registered now, blind to all three:

**M1 — IS THE KERNEL TEMPLATE A SHIFT IN WAVENUMBER?**  Scaling `chi` by `xs` is the same as scaling
`k` by `xs` inside the Bessel factor, so if the source were smooth in `k` over `1.287` per cent the
cross term would be the diagonal transfer read at `xs k`.  Measure, on the primary binning's live
cells and in the fit's own contribution weights,
```
    t_shift(l,k)  =  2 [ log|Dlk(S_lcdm,K_lcdm)|(l, xs k)  -  log|Dlk(S_lcdm,K_lcdm)|(l, k) ]
    M1  =  wrms( t_ker - t_shift ) / wrms( t_ker )
```
with the shifted read taken by **cubic spline in `log k` per `l` row**, declared here, and cells whose
shifted node falls outside the ladder dropped and counted.
  * ⇒ **`M1 <= 0.10`** licenses: *the projection's contribution IS the distance acting through the
    multipole-wavenumber mapping, to ten per cent*, and with it §4's conclusion.
  * ⇒ **`M1 > 0.10`** means the cross term carries something a pure rescaling does not, and §4 has to
    be re-derived rather than reported.
  * ⚠ The comb's own period in `k` is of order the shift, so this is **not** expected to be tiny by
    construction; a small `M1` would be a finding and a large one is a live outcome.

**M2 — THE TWO CROSS TERMS ARE EXACT INVERSES, AND THE RESIDUAL MEASURES IT.**  Two closures, both
exact arithmetic on what is banked:
  * `xs(S_lcdm,K_cr) * xs(S_cr,K_lcdm) == 1` to machine precision — the signature of a one-parameter
    family;
  * and the algebraic identity, which needs no new run:
    `obs - (t_ker + t_src)  ==  -( t_ker^{S_lcdm} + t_ker^{S_cr} )`,
    where `t_ker^{S_cr} = lb[S_cr,K_lcdm] - lb[S_cr,K_cr]`.
    ⇒ So `r7733`'s already-measured residual of `0.0444` **is** the departure of the two source arms'
    kernel templates from exact antisymmetry.  Registered: the identity holds to `1e-12` relative, and
    the antisymmetry is reported as that same `0.0444` rather than as a second measurement.

**M3 — THE ARITHMETIC THE CONCLUSION TURNS ON.**  `|xs - 1|` against the arms' measured `chi`-extent
difference: `1.287` per cent against `15.5`, a factor to be computed and printed, not estimated.

## ④ THE PRICE, AND WHAT IT NEEDS FROM 70 — order item ②

**It cannot be read off the four arrays I hold.**  §1 is the reason, and it is structural.  The split
needs combinations these four do not contain, in two tiers:

**TIER 1 — the distance MAP, not its endpoint.**  Rebuild the four combinations with the *other arm's*
`x0(eta)` array in place of a scalar multiple of the source arm's:
`transfer(S_A, eta_A, x0_B, ...)` with `xs = 1`.  ⇒ This separates **the map's shape** from **the
distance normalisation**, which is the whole of what §1 says the present cross term conflates.
  * **Cost: the same order as `r7729`'s projection step and no new solves.**  `SRCFIELD` already saves
    `x0` per arm (`r7729_70_dlk_build/PREDICTION.md` l.12), so the fields on the runner, or one re-run
    of `launch.sh`, carry everything Tier 1 needs: `4 x 698 x 1450` quadratures, as before.
  * ⚠ The two arms' `eta` grids and `x0` arrays differ in length, so the hybrid needs `x0_B` read onto
    `eta_A` — an interpolation 70 must choose and declare, and the choice is 70's, not mine.

**TIER 2 — the visibility `g`, which is what the law is actually about.**  `G_l(k) = \int g j_l(k chi)
d eta` on the four `(g, chi)` combinations, with `W_l` and `A_l` per combination and each arm's `rs*`.
  * ⛔ **`g(eta)` is NOT in `SRCFIELD`** — it saves `S`, `ee`, `x0`, `kb`, `P`.  So Tier 2 needs one
    more output line in the instrument, which is 70's to add.
  * ⌗ *`G_l` is cheaper per cell than `Dlk`: `g` is a function of `eta` alone, so there is no `k`
    dependence in the integrand beyond the Bessel factor.*

⇒ **Tier 1 answers "map shape or normalisation".  Tier 2 answers the order's question as asked —
which named term.**  Routed to 70 in `FOR_66.md`, not held for 69.

## ⑤ WHAT WOULD FALSIFY EACH CLAIM

| claim | what reds it |
|---|---|
| §1's premise | any line of `project4.py` taking `eta`, `x0` or `S` from the kernel arm; the reading is against lines 139–146 and the quoted `transfer` |
| M1's licence | `M1 > 0.10`, in which case the conclusion is withdrawn and re-derived |
| M2's closures | `xs * xs' != 1`, or the identity failing above `1e-12` |
| §4's Tier 1 price | `x0` absent from the saves, which `r7729`'s own registration would then contradict |

## ⑥ WHAT THIS DOES NOT CLAIM

* ⛔ **It does not withdraw `r7731`'s verdict.**  Both amplitudes are still within two per cent of
  unity and both still exclude their nulls.  What §1 changes is **what the two legs are called**.
* ⛔ **It does not say the landed `P15` sentence is false.**  Its figures are this seat's and they
  stand.  It says the sentence's two NAMES — *"exchanging the two arms' projections"* and
  *"exchanging their sources"* — describe wider and narrower objects than the ones measured, and the
  precise names are *"the ratio of the arms' distances to last scattering"* and *"the arms' sources
  together with their distance maps"*.  Whether that is worth a rewording is 69's call, and the
  measurement is put to 69 rather than acted on.
* ⛔ **It does not claim the one-parameter cross term is WRONG.**  It is `SRCXS`'s registered
  definition and `r7731` already recorded that it is a definition and not a post-hoc rescaling.  What
  is new is that a definition with one parameter cannot carry a split into three named terms.
* It makes no claim about `A_l` on any arm, which needs Tier 2.
