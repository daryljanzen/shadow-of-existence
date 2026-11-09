# `r7721+cc66.2` — PRE-REGISTRATION: can the two-dimensional `(l, k)` integrand separate the kernel swap from the source swap?

⛔ **REGISTERED BEFORE ANY OF IT IS COMPUTED.**  This file is in its own commit, pushed, and not a line
of the measurement exists when it lands.  Nothing below is a result.  Every number printed here was
read off the BANKED INSTRUMENT (grid sizes, `l` ranges, `l_A`, `k` endpoints) or is a THRESHOLD fixed
in advance; no statistic of the measurement itself has been evaluated.

---

## 0.  Why this registration exists, and the one thing it is not allowed to do

`r7719` closed the one-dimensional route geometrically: after the `k`-sum, the kernel and source
templates sit at correlation **−0.9200**, condition number **5.03**, VIF **6.51×**.  Two nearly
anti-parallel templates cannot be told apart by any amount of precision on the collapsed spectrum, and
that single fact also explains `r7713`'s sign reversal.  I then named the build — *stop collapsing the
`k`-sum* — and wrote, in the same breath:

> ⚠ **I am NOT claiming the two-dimensional build will resolve it.**  Its separability is measurable and
> is **not measured here**, and asserting it would be the very fault this revision spent its length
> catching.

That caveat is the whole point of this registration, and this file is bound by it.  The measurement
registered below has **two admissible outcomes, registered as equals**: the `(l, k)` build separates
the two swaps, or it does not.  The thresholds in §4 are fixed now, in advance, so that the verdict is
not chosen after the number is seen.

---

## 1.  ⛔ THE PREMISE I NAMED IS FALSE ON THE BANKED INSTRUMENT, AND I FOUND THAT OUT HERE

The order's words, which are my own words relayed back:

> In the two-dimensional integrand, the source swap is a rescaling along `k` at every `l`, and the
> kernel swap is not.

Checked against the instrument before registering anything on top of it.  **The two source arms do not
share a `k` grid:**

| | `lcdm` source | `cr` source |
|---|---|---|
| `n_k` | **2547** | **1452** |
| `k_min` | 8.599466822427623e-4 | 5.503183515799346e-4 |
| `k_max` | 2.8664889408092076e-1 | 2.8290023347379184e-1 |

So on the banked instrument the source swap changes **the quadrature grid, the number of nodes, and
the range at both ends**, not only the amplitude at each node.  The sentence names the amplitude part
and is silent about the grid part.

⛔ **This is the recurring fault in embryo, and this is the ELEVENTH instance** — a statement about one
object (the continuum integrand, where `S^2(k)` genuinely multiplies pointwise) read as a statement
about another (the banked discretisation, where the swap also moves the nodes).  It is the first
instance caught **at registration time**, before a line of the computation existed, which is exactly
what registering before computing is for.  The previous ten were caught after the computation ran, and
one of them only by a gate.

⇒ The measurement therefore has to be defined on a **common grid**, and the move to that grid is itself
an instrument change that must be controlled rather than assumed harmless.  §2 does that.

---

## 2.  The object, and the two grid decisions, both fixed now

For a combination (source `S`, kernel `K`), the quantity the existing instrument forms per `l` and
then throws away is

```
M^{S,K}(l, k) = G_l^K(k)^2 · (dk / k) · S^2(k),     with    y^{S,K}(l) = sum_k M^{S,K}(l, k)
```

and `y` is exactly the banked spectrum.  The build is: **keep `M`, do not sum it.**

### 2a.  The common `k` grid `K*` — registered a priori

`K*` = the **`cr` arm's own nodes** (the coarser grid, 1452 points) restricted to the overlap of the two
arms' ranges, `[8.599466822427623e-4, 2.8290023347379184e-1]` ⇒ **1450 nodes**.  The coarser arm is
chosen so that **no arm is interpolated up**; inventing nodes the data never had, in the direction the
statistic reads, is how a separability signal gets manufactured.

- `S^2` is carried to `K*` by linear interpolation in `log k` of `log S^2`.
- `G_l^K` is **recomputed directly at the `K*` nodes**, never interpolated.  `G` is an integral over the
  banked visibility and is cheap to evaluate exactly at any `k`; interpolating it would mean
  interpolating the very object whose `(l, k)` structure is being measured.

### 2b.  The common `l` reading — BOTH forms, and they must agree

The kernels have different `l_A` (301.54271387763947 vs 302.9430505935752, ratio **1.0046439083137786**),
so their dense `l` lists differ: `lcdm` 242…934 (693 values), `cr` 243…939 (697).  `spherical_jn` takes
an integer order, so a non-integer `l` is not available and one of the two readings must interpolate.
Neither is privileged, so **both are registered and the verdict must hold under both** — the same
agreement discipline `r7713` and `r7717` ran under:

- **(A) same integer `l`, no interpolation at all.**  The shared integer range is **243…934, 692
  values**.  The price is that the two kernels are then read at `q` differing by **0.464 %**.
- **(B) common `q`**, with the `cr`-kernel array interpolated in `q` at fixed `k` onto the `lcdm`
  `q`-grid.  The price is an interpolation **along the direction the step statistic reads**, which can
  only make the field smoother — i.e. it can only flatter the separability.

⇒ Registered now: if (A) and (B) disagree on the §4 verdict, **the verdict is NOT RESOLVED**, and the
disagreement is the result.  Reading whichever of the two is kinder is not available.

### 2c.  ⛔ The control on the grid change — the number that decides whether any of this transfers

`sum_k M` on `K*` must reproduce the **banked** `y(l)`.  Tolerance registered at **1e-3 relative, at
every `l`** — deliberately *not* `1e-12`.  `K*` is a different quadrature, so the agreement is a
numerical-convergence statement, not an identity, and demanding an identity would guarantee a red that
means nothing.  If the collapse on `K*` departs from the banked `y` by more than 1e-3 relative at any
`l`, then **the common-grid object is not the banked object** and nothing read off it transfers to
P15's printed claims.  That is a refusal, not a caveat: the script computes no statistic downstream.

---

## 3.  The gates, in the order the script will run them, with no later re-ordering

**Gate 0 — CONTROL, before anything.**  Recompute `M^{lcdm,lcdm}` for the first block of `l` on the
*banked* `k` grid and require `sum_k M` to match the banked `y` to **≤ 1e-12 relative** — the same
tolerance `r7715`'s CI control already runs under, through the same code path.  Fail ⇒ exit, compute
nothing.

**Gate 1 — THE PREMISE, AS A CONTROL AND NOT AS A RESULT.**  On `K*`, require
`M^{cr,K} / M^{lcdm,K} = rho(k) := S^2_cr(k) / S^2_lcdm(k)` to **≤ 1e-12** at every `(l, k)`, for each
kernel separately, **and** the two kernels' `rho` to agree to the same tolerance.  This is expected to
pass *by construction* once the grid is common — it is registered as a control precisely so that it
cannot later be reported as a finding.  Its one real content: passing it establishes that the kernel
difference `Delta_ker` is **independent of the source**, which is what halves the price in §5.
Failing it means the framing in §2 is wrong and the revision stops there and says so.

**Gate 2 — HOW MUCH OF THE KERNEL SWAP A SOURCE SWAP CAN MIMIC.**  In log space,
`Delta_ker(l, k) = log M^{S,cr} − log M^{S,lcdm} = log(G^2_cr / G^2_lcdm)` (source-free by Gate 1).
Split it into the part a source swap could have produced and the part it could not:

```
Delta_ker(l, k) = a(k) (x) 1_l  +  R(l, k),        a(k) = mean over l of Delta_ker(., k)
f_mimic = ||a (x) 1_l||_F / ||Delta_ker||_F        f_sep = ||R||_F / ||Delta_ker||_F
```

Report `f_mimic`, `f_sep`, the leading singular value's share of `||R||_F`, and how many singular
components hold 90 % of it.  ⚠ `f_sep` is reported but is **NOT the verdict**: a Frobenius fraction has
no units of resolvability, and reading one as if it did would be instance twelve.

**Gate 3 — THE VERDICT: CONDITIONING, AGAINST THE 1D NUMBERS THAT CLOSED THE ROUTE.**  Build the two
*two-dimensional* templates, mean-removed and flattened,

```
t_ker(l, k) = log( M^{S,cr} / M^{S,lcdm} )      (kernel swap, source fixed)
t_src(l, k) = log( M^{cr,K} / M^{lcdm,K} )      (source swap, kernel fixed)
```

and report **correlation, condition number of the 2×2 design, and VIF**, under reading (A) and reading
(B) separately, beside the 1D values **−0.9200 / 5.03 / 6.51×** that closed the collapsed route.

**Gate 4 — THE INTERPOLATION'S OWN SIZE.**  Report how much reading (B)'s `q`-interpolation moves
`f_sep` and the Gate-3 correlation. If that movement is comparable to the separation Gate 3 claims,
the claim is the interpolation's and not the instrument's, and the verdict is NOT RESOLVED.

---

## 4.  ⛔ THE THRESHOLD, FIXED NOW

> **The two-dimensional build resolves what the one-dimensional collapse could not if and only if, under
> BOTH readings (A) and (B), `|correlation| <= 0.70` AND `VIF <= 2.0`.**

0.70 is not a round number chosen for looking like one: at `|corr| = 0.70` the VIF is
`1 / (1 − 0.49) = 1.96`, so the two halves of the threshold are the same statement and neither can be
satisfied alone.  Against the 1D route's −0.9200 and 6.51× this demands the degeneracy be **broken, not
merely dented**.

⇒ **Registered in advance: anything above that is NOT resolution**, however suggestive `f_sep` looks, and
I commit here to printing the correlation and the VIF whichever side of the line they fall on, and to
reporting a failure as the result rather than as a reason to look for a third reading.

---

## 5.  The price, and the one thing it does not buy

- **No extra Bessel evaluations.**  `M(l, ·)` is *already formed* inside the existing per-`l` loop and
  destroyed by `np.sum` on the next line.  Keeping it costs a write, not a computation.
- **Recomputation is unavoidable** because only the collapse is banked.  By Gate 1 the measurement needs
  **two kernel arrays, not four combinations** — ~half the `r7713` grid, so **≈ 2.1 CPU-hours**,
  ≈ 35 min wall in the four-way `dense-ell` matrix already standing from `r7715`, inside its 330-minute
  timeout.
- **Storage: 16.12 MB** for the two arrays on `K*` (`692…697 l × 1450 k × 8 B`).  ⇒ The arrays are **NOT
  committed**; the committed artefacts are the derived rank statistics and the gate verdicts, and
  regeneration is scripted and idempotent in blocks, as `r7713`'s own restart losses taught.
- Checkpointing per block of `l`, not per array: a checkpoint interval longer than the interval between
  container restarts is not a checkpoint.

⛔ **What the price does not buy — registered so it cannot be blurred afterwards.**  Good conditioning is
**necessary and not sufficient**.  A separating component must also survive the noise of a real
measurement, and that is a *detectability* question needing a per-`(l, k)` noise model which this
instrument does not have.  ⇒ **Item 2 returns a CONDITIONING result, never a detectability result**, and
a passing Gate 3 licenses the sentence *"the degeneracy that closed the collapsed route is broken in the
`(l, k)` plane"* and **not** the sentence *"the two swaps can be told apart in the data."*

---

# ⛔ AMENDMENT 1 — the registered per-cell log-space form is **NOT COMPUTABLE** on `K*`, and this is why

**Made before any statistic of the measurement was computed, in its own commit, and it does NOT touch the
threshold.** §4 stands exactly as written. What changes is *where the measurement is defined*, forced by a
property of the instrument that was measured, not by any result.

## What went wrong

§3's Gates 2 and 3 are written in log space: `Delta_ker = log(G^2_cr / G^2_lcdm)`. On `K*` that is `log 0`
over a large part of the plane. `j_l(k x0)` **underflows to exactly zero below its turning point**
`k ~ l / x0`, and the dead region grows with `l`:

| | cells with `M <= 0`, of 1450 |
|---|---|
| `l = 243` (bottom of the shared window) | **11** |
| `l = 589` | **86** |
| `l = 934` (top) | **181** |

and the `|G|` distribution inside block 0 runs down through `8.3e-148` to `1.6e-276` to exact `0` — the
exponential tail of the Bessel function, not an oscillation zero.

⇒ ⛔ **The registration asked for a logarithm of a quantity that is exactly zero on up to 12 % of the
plane.** Nothing in §2 or §3 noticed, because the premise check in §1 was about the *grid* and this is
about the *integrand*.

## The first replacement I considered, and why it is NOT used

Collapse to `B` log-spaced `k`-bands instead of to one, with `B = 1` reproducing the closed 1D route as a
control. Band sums are positive, so the logs come back. **Measured, it fails at once:** the lowest bands
sit entirely inside the dead region for *every* `l` in the window, so

| `B` | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 |
|---|---|---|---|---|---|---|---|---|
| non-positive band cells | **0** | 4 | 8 | 20 | 42 | 84 | 169 | 345 |

⇒ Only `B = 1` is admissible on the full range, and `B = 1` **is** the collapsed route. Banding buys
nothing here, and recording that is the point of writing it down rather than quietly trying the next idea.

## The amendment, and the two measurements that license it

The dead set is not scattered: it is a **contiguous low-`k` prefix**, and **above it there is no zero at
all** — measured at both ends of the window (`l = 243`: first non-zero node `0`, zeros above it `0`;
`l = 934`: first non-zero node `119` for `lcdm` and `117` for `cr`, zeros above it `0` for both).

⇒ **The measurement is restricted to the COMMON LIVE SUPPORT**: the nodes of `K*` at or above the largest
dead prefix over the shared `l` range and both kernels. At the binding `l` that is node `119`,
`k >= 2.4126e-2`, so **1331 of 1450 nodes**. The restriction is then determined **from the assembled array
itself**, not from these three `l`, and gated:

- **Gate 1a (NEW).** At every `l` and for both kernels the dead set must be a contiguous prefix of `K*`.
- **Gate 1b (NEW).** Above the common prefix there must be **no** zero, for either kernel, at any `l`.

If either fails, the per-cell form is still not computable and the measurement reports that, rather than
masking cell by cell — a per-cell mask makes the array ragged and the rank framing in §3 does not survive it.

⛭ **And the restriction carries its own sharp control, for free.** The dropped cells are *exactly* zero, so
dropping them **cannot change `sum_k M` at all**. ⇒ Gate 2c is re-run on the restricted support and must
return **the same** departure from the banked spectrum as on full `K*` (measured there: `4.9367e-05`
against the registered `1e-3`). A restriction that moves that number has dropped something that was not zero.

## ⛔ What is NOT amended

The threshold in §4 — `|correlation| <= 0.70` **and** `VIF <= 2.0`, under both readings — is **unchanged**,
and the 1D comparison values `−0.9200 / 5.03 / 6.51x` are unchanged. ⚠ *An amendment made after seeing a
numerical obstruction is legitimate; an amendment that also moved the line the verdict is read against
would not be, and would be indistinguishable from choosing the verdict. The line is where it was.*

## The price, re-measured rather than re-estimated

§5 estimated ~2.1 CPU-hours. **Measured: `1.51` s per `l` on `K*`** ⇒ the two kernel arrays over 692 shared
`l` come to **≈ 35 min in one process**, inside this container's recycle interval only because the blocks
are checkpointed. ⇒ The registered price was **conservative by about three and a half times.**
