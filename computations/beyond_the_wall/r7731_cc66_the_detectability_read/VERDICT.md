# `r7731+cc66` VERDICT — **BOTH CONTRIBUTE. The fourth cell, on all four readings, with power `1.000`.**

The registered test, run on 70's `(ℓ, k)` arrays. **13 gates, 0 failures**, under
`PREDICTION_detectability.md` amendments 1–6. Outputs in `read_output.txt`, `four_cell_output.txt`,
`plain_null_output.txt`.

---

## ① ⛭ THE PRECONDITION THE PSEUDO-SPECTRA COULD NOT MEET

On the pseudo-spectra the two-amplitude fit was an **exact algebraic identity** — residual ratio
`2.6e-15` — so there was nothing to detect and no null could change that.

| | |
|---|---|
| rms of `full − (t_ker + t_src)` | **`1.9521`** |
| rms of the signal itself | **`4.2057`** |
| ⇒ ratio | **`0.4642`** — ⛔ *unbinned and equal-weight; see ⑤'s correction, the model's own is `0.0444`* |

⇒ **On the real computation the fit is NOT an identity.** The detectability question can be asked here,
and this is the first object on which it could be.

## ② THE FOUR-CELL VERDICT — **BOTH CONTRIBUTE**, on `2 × 2` readings

| null × binning | `a_ker` | its 99 % null interval | `a_src` | its 99 % null interval | cell |
|---|---|---|---|---|---|
| normalised, 120 bins | **`+1.0076`** | `±0.030` | **`+1.0035`** | `±0.26` | **BOTH** |
| normalised, 63 bins | `+1.0195` | `±0.117` | `+1.0045` | `±0.28` | **BOTH** |
| plain, 120 bins | `+1.0076` | `±0.050` | `+1.0035` | `±0.14` | **BOTH** |
| plain, 63 bins | `+1.0195` | `±0.119` | `+1.0045` | `±0.26` | **BOTH** |

⇒ **Both amplitudes land within `2 %` of unity and both exclude zero by a wide margin, on every
reading.** §3's rule — *both null constructions reported, a disagreement between them IS the verdict* —
does not fire: there is no disagreement.

⛭ **This is the FOURTH CELL**, registered in advance in §1 with the note that the order's three names —
*creates*, *fails to cancel*, *neither* — **do not partition the outcome space**. ⇒ The answer to
*"creates or fails to cancel"* is that **the question's premise is wrong: both mechanisms contribute, at
unit amplitude.** ⌗ *And it matches what the collapsed route measured at `r7713` (`+1.045`, `+1.061`)
without being able to separate them.*

## ③ THE POWER REQUIREMENT, MET

| | pure-kernel injection | pure-source injection |
|---|---|---|
| 120 bins | **`1.000`** | **`1.000`** |
| 63 bins | **`1.000`** | **`1.000`** |

against the registered `0.95` at `α = 0.01`. ⇒ **"Neither, by the instrument" is not in play**: the test
recovers a planted signal of either kind every time.

## ④ THE CONDITIONING — the degeneracy is broken, and worse collapsed than on the pseudo-spectra

| the same statistic, the same four arrays | corr | cond | VIF |
|---|---|---|---|
| **COLLAPSED** | **`−0.9937`** | `17.77` | **`79.47×`** |
| un-collapsed, 120 bins | **`+0.0215`** | `1.02` | **`1.00×`** |
| un-collapsed, 63 bins | `+0.0043` | `1.00` | `1.00×` |
| *registered threshold* | *`≤ 0.70`* | | *`≤ 2.0`* |

⇒ The collapsed baseline is **worse here than on the pseudo-spectra** (`−0.9937` against `−0.9518`), so
the break is a property of the plane and not of the statistic. `f_sep` is **`0.979`/`0.980`** against
`0.8595` on the pseudo-spectra: **almost none of the kernel swap is reproducible by a source rescaling.**

## ⑤ ⛔ TWO LIMITS I AM NOT GLOSSING

- ⚠ **The two-amplitude model is INCOMPLETE, not merely imperfect.** `46 %` of the plane's signal rms
  lies in **neither template** (①). ⇒ Licensed: *both contribute at unit amplitude*. **NOT** licensed:
  *the swap is exhausted by these two mechanisms.*
  > ⛔⛔ **CORRECTED AT `r7733+cc66`, AND THE CORRECTION IS THIS BULLET'S OWN FIGURE.** The `0.4642`
  > of ① is measured on the **unbinned** plane, counting **every cell equally**, at **unit**
  > coefficients. The model is fitted **binned**, in the **contribution weights**, at the **fitted**
  > coefficients — and there the ratio is **`0.0444`** (primary) and **`0.0429`** (secondary); the
  > unbinned contribution-weighted figure is `0.2344`. ⇒ **The licence above holds in DIRECTION — the
  > swap is still not exhausted by these two — and this bullet's "INCOMPLETE, not merely imperfect"
  > OVERSTATES the model's own incompleteness by about a factor of ten.** On the object the amplitudes
  > come from, the two templates carry the signal to within about four per cent in rms: *imperfect,
  > not incomplete.* ⌗ *A statement about one object read as a statement about another, in this seat's
  > own verdict. The corrected figures are gated in
  > `receipts/P15_CR_cosmology/P15_both_mechanisms_contribute_at_unit_amplitude_and_the_located_step_is_the_kernels_because_the_source_template_is_flat_in_ell.py`;
  > the text above is left standing, with its error named, rather than rewritten.*
- ⚠ **`a_src` is the less determined of the two** — its null interval is about **ten times wider** than
  `a_ker`'s on the normalised null (`±0.26` against `±0.030`). Both still exclude zero by ~`4×` their own
  interval, but the kernel amplitude is the better measured, and a reader should not take the two as
  equally pinned.

## ⑥ The controls, since the verdict rests on them

| | |
|---|---|
| the convention `ℓ(ℓ+1) Σ_k P·Dlk² = Dl`, **recomputed not cited** | departure exactly **`0`** |
| §2c, the grid move, **my arithmetic** | **`1.9627e-06`** against the registered `1e-3` |
| the premise: `P` depends on the source arm alone | exactly **`0`** |
| cells negative | **`0`** — `P > 0` at all `1450` nodes, `Dlk² ≥ 0` |
| cells exactly zero | `62 191` of `1 012 100` (`6.1 %`), masked at weight `0` |
| bins dead at **every** `ℓ` | **`0`** of `120`, **`0`** of `63` |

⌗ *70's C3 records the same `1.9627e-06` on the same comparison. **That agreement is a cross-check, not a
substitution** — §2c was run here as this seat's own arithmetic, which is what the order confirmed it
should be.* ⌗ *And 70's `XS` is part of the **cross-term definition** — the distance ratio entering the
Bessel argument — **not** a post-hoc rescaling of the arrays. Reading it as a rescaling would have been
wrong, and it was checked against 70's own code rather than guessed.*

---

## ⑦ ⛔ THE PROCESS RECORD, WHICH IS NOT CLEAN

- **Gate A5a FIRED, and I restated it.** That is the shape of a seat talking past its own refusal, so the
  defence had to be in the registration's text rather than my judgement — §A5.4 names the closing failure
  as *"the same way it failed on the pseudo-spectra"*, and measured, **`0` bins are dead at every `ℓ`** and
  **`0` cells are negative**. ⛭ **Registered while still blind to the verdict**, because the script refused
  before computing it. *Had any bin been dead at every `ℓ`, the route would be closed.*
- **I met only HALF of my own §3 on the first pass.** It registers **two** null constructions; `four_cell.py`
  called the surrogate with `normalise=True` only. ⇒ The plain null was run afterwards and is reported
  above. ⌗ *Caught by re-reading §3 against what the script did, **not** by the result — and the result
  would not have changed, which is exactly why it had to be caught some other way.*
- ⌗ *The word "secondary" carries two independent axes in this registration — §3's secondary **null** and
  amendment 5's secondary **binning**. They are not the same thing and are reported separately above.*
