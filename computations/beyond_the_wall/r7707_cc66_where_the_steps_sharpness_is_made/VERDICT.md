# `r7707+cc66` — VERDICT: THE STEP IS IN THE CONTRAST AND IN NOTHING ELSE

69's question: the law carries the step's size and not its sharpness — **where is the sharpness made?**

## THE ANSWER, AS A LOCALISATION

**The sharp transition is in neither arm's own projected spectrum and not in the source-side ratio. It
exists only in the contrast between the two projected spectra.**

| reading | half | lo | hi | step | step / own sd | corr(Ra,Rc) | Ra hi/lo | Rc hi/lo |
|---|---|---|---|---|---|---|---|---|
| **spectra ratio** | 0.175 | `+0.0309` | `+0.0551` | `+0.0242` | **`2.91`** | `0.999524` | `0.687` | `0.671` |
| | 0.250 | `+0.0316` | `+0.0558` | `+0.0242` | **`4.56`** | `0.999367` | `0.730` | `0.713` |
| | 0.350 | `+0.0306` | `+0.0561` | `+0.0255` | **`9.49`** | `0.999014` | `0.802` | `0.783` |
| **source ratio** | 0.175 | `−0.0068` | `−0.0043` | `+0.0025` | `0.40` | `0.999813` | `0.854` | `0.852` |
| | 0.250 | `−0.0068` | `−0.0044` | `+0.0024` | `0.65` | `0.999892` | `0.887` | `0.884` |
| | 0.350 | `−0.0072` | `−0.0054` | `+0.0018` | `0.88` | `0.999955` | `1.019` | `1.017` |

**⓵ In the spectra's contrast: yes.** From `+0.031` to `+0.056` across `q = 1.783`, a factor of
`1.77`–`1.83` at `2.9` to `9.5` times the plateaus' own scatter. *That is the "about 1.8" the step
paragraph prints, reproduced on the slide rather than on the seven bands.*

**⓶ In either arm's own spectrum: no.** Both arms' own band RMS **falls** across the range
(`hi/lo` `0.67`–`0.80` at every smoothing) and the two track each other at a correlation above `0.999`.
Their own curves are the comb's beat, swinging by a factor of two to five; the step is a **two per cent
relative difference** between them. ⛔ **The rising-step locator is out of its domain on all six of those
curves, and its numbers there are not reported** — the first form of the slide ran it anyway and got a
negative 25–75 width and a `NaN` under translation, which is the instrument saying it had been asked a
question it cannot answer. *Those numbers are in `where_the_sharpness_is.json` and in no gate.*

**⓷ In the source-side ratio: no, and the exclusion has a size.** Its own low-to-high change is `+0.002`,
**under one standard deviation of its own scatter at every smoothing**, while a step of the spectra's size
would have shown there at **`3.8` to `11.8` sd**. The two arms' η-integrated sources carry the same
relative comb amplitude to under one per cent, and the ratio sits near zero and slightly **negative**
throughout rather than stepping up. ⚠ *So a step of the measured size is EXCLUDED in the source; a tenth
of it is neither excluded nor resolved, and that is said rather than rounded to zero.*

**⓸ The translation control decides which of the two is a location.** Translating the read interval by
`+0.15` and `+0.30` in `q` moves the spectra ratio's half-rise by the same amount to within `0.004`
(`1.7830 → 1.6329 → 1.4868`) and does not move the source ratio's at all (`1.3014 → 1.2286 → 1.6212`,
residuals `0.077` and `0.620`). *`r7703`'s withdrawal is why this is the primary evidence for every "no
transition here" and not a footnote.*

## ⚠ MY REGISTERED PREDICTION IS FALSIFIED

I predicted the step would be **in** each arm, because P15 calls it "very largely shared". Measured, the
arms are shared at `0.999` and **the step is in the remainder.** ⛔ *"Very largely shared" and "the step is
in each arm's own spectrum" are different statements, and I read one as the other.* Same fault as reading a
null's response at a chosen amplitude as a decomposition: a statement about one object taken as a statement
about another.

## ⛭ AND THE REGISTERED TENSION RESOLVES WITHOUT ANYTHING SHARPENING

The registration named it in advance: a linear projection of finite width cannot sharpen, and `r7703`
measured the law's own window at some seven times the step — so a step absent in the source and present in
the spectrum looked like it needed the projection to do something it cannot.

**It does not.** The step is a `+0.024` change in a **ratio** between curves that each swing by a factor of
two to five and track each other at `0.999`. ⇒ **The ratio does not sharpen a broad feature; it exposes a
small one.** "The projection only broadens" constrains each arm's spectrum and says nothing about a two per
cent difference between them.

## ⛔ WHAT IS NOT CLAIMED

- **No attribution**, registered in advance and unchanged: attribution needs a build that removes the
  sharpness and leaves the rest, the step is largely shared between the arms, and no build removes it.
- **Not "the projection makes it".** What is established is where the transition **first appears** in the
  readings available: in the contrast of the projected spectra, and in neither the source contrast nor
  either arm alone. Whether the projection creates the two per cent difference or merely fails to cancel
  something the source contrast hides below its own scatter **cannot be separated here**, and the source
  ratio's scatter is the reason: it excludes a step of the measured size, not a tenth of one.
- **No new printed figure is proposed.** `1.77`–`1.83` is the "about `1.8`" already in print.

## THE REGISTERED PRECONDITION FIRED

`S_i`'s running envelope crosses zero **twelve** times on both arms, `min|e|` down to `8e-6`, so `(y−e)/e`
is meaningless there; `S_i**2`'s never crosses. ⇒ And the square is the **frequency-matched** object, not
merely the safe one: `cos²` has half the period of `cos`, `D_ℓ` is itself quadratic in the transfer, and
`S_i**2` fits the same comb period as `D_ℓ` (`1.0070`/`1.0008` against `0.9935`/`0.9893`), while `S_i`'s
fitted `1.10`–`1.13` is an **artefact of `fit_period`'s `0.90`–`1.20` grid**, which cannot reach a period of
two at all.

## THE PRICE

| | |
|---|---|
| baseline, three reps | `2227` / `1990` / `2020` ms, `46` PASS |
| with the block | **`3140` ms, `53` PASS, `0` FAIL** |
| added | **`+1.06` s**, against a registered `10` s |

So the block lives in the host receipt with no INDEX row owed, on the same rule as `r7703`.

## FAILABILITY

Nine legs over a green control, the block's source and the host's `_locate` read **out of the receipt**.
Legs F and I redden three checks each, reported rather than tuned away. **Leg H is the one that matters**:
it injects a step of the measured size into the arm's own source and watches the source-exclusion gate go
red — which is what makes "would have shown at `3.8` to `11.8` sd" a measurement rather than an arithmetic
remark about a standard deviation.
