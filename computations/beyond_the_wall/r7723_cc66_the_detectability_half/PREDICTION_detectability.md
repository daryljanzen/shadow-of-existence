# `r7723+cc66.2` — PRE-REGISTRATION: does the two-amplitude fit on the `(ℓ, k)` plane distinguish "the projection creates it" from "the projection fails to cancel it"?

⛔ **REGISTERED BEFORE ANY STATISTIC EXISTS**, in its own commit. Every number below is either a property
of the banked instrument, measured here, or a threshold fixed in advance. ⛭ The order's instruction was
**"price it first"**, so §4 comes before anything is run — and §5 is the result of having done so.

---

## 1. ⛔ THE THREE OUTCOMES, NAMED IN ADVANCE — and the order's three names do NOT partition the space

The order asks me to name what counts as *"creates"*, *"fails to cancel"* and *"neither"*. ⛭ **I am taking
these from the order file's own earlier wording and not from my paraphrase of it** — `r7705`'s item reads:
*"what result would count as 'the projection creates it', what would count as 'the projection fails to
cancel it', and what would count as neither."* ⇒ So the subject is **the projection**: the kernel swap is
*"the projection creates it"*, the source swap is *"the projection fails to cancel it"*. ⌗ *Checked rather
than assumed, because getting that mapping backwards would invert every verdict below.*

The test fits, on the plane,

```
Delta_obs(l, k)  =  a_ker · t_ker(l, k)  +  a_src · t_src(l, k)  +  e(l, k)
```

and the null of §3 supplies the joint sampling distribution of `(a_ker, a_src)`. With `I_ker` and `I_src`
the two **99 % null intervals**, the outcome is read off a 2×2 and **nothing else**:

| `a_ker` excludes 0 | `a_src` excludes 0 | REGISTERED VERDICT |
|---|---|---|
| ✔ | ✘ | **"the projection CREATES it"** |
| ✘ | ✔ | **"the projection FAILS TO CANCEL it"** |
| ✘ | ✘ | **"NEITHER"** — the plane does not decide |
| ✔ | ✔ | ⛔ **"BOTH CONTRIBUTE"** — see below |

⚠ **The order's three names do not cover the fourth cell, and I am not forcing it into "neither".** Both
amplitudes significant is a distinct, physically meaningful outcome — it is in fact what the collapsed route
measured (`+1.045` kernel, `+1.061` source at `r7713`), consistent with exact log-additivity. ⇒ Registered as
its own verdict, reported under that name, and **not** reported as either of the first two nor as "neither".

**Also fixed now, so it cannot be chosen later:** the amplitudes are reported with their null intervals
whatever the verdict, and a verdict is only read when the §2 power requirement is met. If power fails,
**"NEITHER" is forced by the instrument** and is reported with that reason attached rather than as a finding
about the physics.

## 2. The power requirement, fixed in advance

Inject a known pure-kernel signal (`a_ker = 1, a_src = 0`) and a known pure-source signal
(`a_ker = 0, a_src = 1`) into null draws and recover them. ⛔ **The test is read only if it recovers each at
power ≥ 0.95 at α = 0.01.** Below that the instrument cannot tell the two apart at this amplitude and the
verdict is "neither, by the instrument", with the measured power printed.

## 3. The null — two constructions, BOTH registered, because one of them is only partly honest

The order requires a null that **"carries the plane's own structure"** and **"preserves correlation along
both `ℓ` and `k`"**, since the separating structure is spread over `142` modes.

- **SECONDARY: plain 2D phase randomisation.** `rfft2` the field, randomise phases, keep the amplitude
  spectrum, `irfft2`. This preserves the **2D autocovariance exactly**, in both directions and across them.
- ⛭ **PRIMARY: row-and-column-normalised 2D phase randomisation.** Divide the field by its per-`ℓ` and
  per-`k` standard deviations, randomise phases, then restore both.

⇒ ⛔ **Why the plain form is not enough, measured here before it was chosen:** the field is **not
stationary**, and phase randomisation flattens it.

| | per-`ℓ` variance, max/min | per-`k` variance, max/min |
|---|---|---|
| the field | **`6.1`** | **`24.9`** |
| a plain phase-randomised surrogate of it | `2.9` | **`5.09`** |

The autocovariance is preserved by construction; what is **not** preserved is **where the variance lives** —
flattened about fivefold along `k`. ⇒ A null that is smoother than the data where the data is quiet rejects
too easily, so the normalised form is the primary and **both are reported; a disagreement between them IS
the verdict**, by the same rule the separability measurement ran under.

⌗ *One objection I expected to be fatal and measured instead: the support is a ragged triangle, not a
rectangle, so a 2D FFT needs the dead region filled. Filling it with zero puts **`2.8 %`** of the
surrogate's variance in cells the data has no value for — small, and registered as a reported diagnostic
rather than a refusal. The measurement is what demoted it.*

## 4. ⛭ THE PRICE, MEASURED FIRST AS THE ORDER REQUIRED

| | |
|---|---|
| one 2D phase-randomised surrogate, `692 × 1450` | **`0.046` s** |
| memory per surrogate | `8.0` MB |
| `2000` draws | **`2` min** |
| `10⁴` draws | `0.1` h |
| `10⁶` draws | `13` h |

⇒ **The null is cheap.** `10⁴` draws — enough for a 99 % interval and a power curve — costs about six
minutes. ⌗ *Measured over 5 draws on the real array, not extrapolated from one. The cost is flat in the
draw index, unlike the `ℓ`-dependent Bessel cost whose flat extrapolation I got wrong last revision.*

---

## 5. ⛔⛔ AND YET THE TEST CANNOT BE RUN ON THIS INSTRUMENT — TWO INDEPENDENT REASONS, BOTH MEASURED

The order's item 3 asks me to say so if no honest null can be built from what the instrument holds. **It is
worse than that: there is no object to apply a null to.**

### ⒜ On the pseudo-spectra, where the plane exists at `692 ℓ`, the two-amplitude fit is an EXACT ALGEBRAIC IDENTITY

`M^{S,K}(l,k) = G_l^K(k)² (dk/k) S²(k)` factorises, so

```
log M^{cr,cr} − log M^{lcdm,lcdm}  ≡  t_ker  +  t_src        exactly, cell by cell
```

Measured over the `969189` live cells:

| | |
|---|---|
| max \|residual\| of `full_swap − (t_ker + t_src)` | **`2.06e-13`** |
| rms residual | **`1.41e-14`** |
| rms of the signal itself, for scale | **`5.4089`** |

⇒ **`a_ker = a_src = 1` with zero residual, to machine precision.** There is nothing to detect, no noise for
a null to model, and the fit returns the answer it was built from. ⛔ **A detectability test on the
pseudo-spectrum plane is a tautology, and no null makes it otherwise.**

### ⒝ The only `k`-resolved REAL object the instrument holds sits ENTIRELY BELOW the window the transition is in

`Dlk_samp__fixed` in both arms' accept banks is a genuine `(ℓ, k)`-resolved object from the full
computation — ⌗ *and I nearly reported that no such object existed at all. It is there.* But:

| | `lcdm` arm | `cr` arm |
|---|---|---|
| sampled `ℓ` | `20, 46, 73, 99, 125, 151, 178, 204` | `20, 46, 73, 99, 126, 152, 179, 205` |
| that is `q = ℓ/l_A` | **`0.066` … `0.677`** | **`0.066` … `0.677`** |
| `k` nodes | `2547` | `1452` |

⛔ **The discriminant's window is `q ∈ [0.80, 3.10]`. Every sampled `ℓ` is BELOW `q = 0.68`** — the
`k`-resolved real object does not reach the band the located transition lives in, at any `ℓ`. Three further
obstructions on top: the arms share only **`4` of `8`** sampled `ℓ`, their `k` grids differ again
(`2547` vs `1452`), and the row sums do **not** reproduce the banked spectra (`−4.13e-02` against
`9.12e-02` at the first sampled `ℓ`), so what the array even is would have to be established before
anything rested on it.

⇒ **Verdict on item 3: no honest null can be built, because the object the null would be for does not
exist.** The price is cheap and the construction is registered; what is missing is the plane itself, for the
real computation, in the window that matters.

## 6. What would supply one

**An instrument change, not an analysis change.** Specifically, a re-run of the full computation that
**retains the `(ℓ, k)` integrand** rather than collapsing it, over `q ∈ [0.80, 3.10]`, for both arms, on a
**shared `k` grid**, at enough `ℓ` to carry the `142`-mode structure the separability measurement found.

⌗ *Two things that make this cheaper than it sounds, and one that does not:* the `(ℓ, k)` array is already
formed inside the existing per-`ℓ` loop and destroyed by the collapse on the next line, so retaining it costs
a write and not a computation; and `Dlk_samp` shows the retention has been done before, at 8 multipoles, so
the mechanism exists. ⚠ **But it is the FULL computation, not the pseudo-spectrum one**, and its per-`ℓ`
cost is not the `1.5`–`4` s this seat has measured. ⇒ **That price is not mine to quote and I am not
quoting it.**

⚠ **Until that exists, nothing from the separability result goes into `P15`** — which is the order's own
instruction, and this registration does not weaken it.
