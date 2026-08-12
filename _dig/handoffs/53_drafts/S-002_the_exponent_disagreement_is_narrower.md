---
name: s-002-exponent
kind: FINDING (draft, uncommitted)
current: r2428 / c54.178
job: Correct a mislabelled quantity in the acoustic fold's own arc, and the receipt narrative that inherited it. Two instruments disagree on the CR acoustic phase exponent — but by −0.97 vs −0.62, not −2 vs −0.62, and the fold's mechanism is confirmed by its own data rather than falsified by them.
sources: [chat]
---

# S-002 · THE FOLD'S EXPONENT IS −0.97, NOT −2 — AND ITS MECHANISM REQUIRES −1

**Two corrections, one in each line. Neither changes a verdict; both change what the disagreement
between the two instruments *is*.**

---

## ① THE FOLD'S ARC MISLABELS ITS OWN QUANTITY

`ACOUSTIC_LIVE_ARC.md` L-108 (and again in the handoff shipped from it) reads:

> *"Φ′ carries −k²Φ/(3ℋ), so an unsupported potential relaxes on 3ℋ/k² — and **Q₁·k² is constant
> across the whole range (0.120 → 0.124)**."*

⛔ **`Q₁·k²` is not constant. It spans a factor of 3.94.** The numbers 0.120–0.124 are the values of
**k²·Δη₁** — the *timescale* relation, computed correctly in the fold's own working and belonging to
a different quantity. **The label was carried onto the wrong object and then propagated into a
handoff document.**

*This is the corpus's own law about hand-transcription, earned again: a number written into prose
from an adjacent calculation has no way to fail.*

## ② AND THE MECHANISM NEVER REQUIRED −2

The fold's stated mechanism is that the potential relaxes on **τ = 3ℋ/k²**, so the first turnover
arrives at Δη₁ ∼ τ ∼ 1/k². But **Q is an accumulated sound phase, not a time**:

$$Q_1 \;=\; \frac{k}{\pi}\int c_s\,\mathrm d\eta \;\sim\; \frac{k\,c_s\,\Delta\eta_1}{\pi} \;\sim\; k\cdot k^{-2} \;=\; k^{-1}.$$

⇒ **A 3ℋ/k² relaxation requires Q ∼ k⁻¹.** What is constant under it is `k²·Δη₁`, and equivalently
**`k·Q₁`** — never `k²·Q₁`.

## ③ WHAT THE FOLD'S OWN NUMBERS GIVE

Fitting the Q₁ values recorded in L-108 and L-114 — two independently-run k sets, nothing new
computed:

| data | fit | rms residual (ln Q) |
|---|---|---|
| **fold, L-108 set** (5 pts) | **Q ∼ k^−0.969** | 0.051 |
| **fold, L-114 set** (6 pts) | **Q ∼ k^−0.968** | 0.046 |
| **receipt's CR column** (7 pts) | **Q ∼ k^−0.622** | 0.064 |

*The two fold sets agree to 0.001 in the exponent, which is the fold's own internal reproducibility.*

And the collapse test, which is the receipt's own instrument turned on the fold's data:

| power *p* | spread of `Q·k^p` (max/min) |
|---|---|
| `Q·k²` | **3.94** |
| `Q·k^0.62` | 1.60 |
| **`Q·k^1.00`** | **1.15** |
| `Q·k^0.97` | 1.13 |

⇒ **`k·Q₁` is constant to 15% across the band — 0.0200 to 0.0230.** *The fold's mechanism is
**confirmed** by the fold's own data, at the exponent the mechanism actually predicts.*

---

## ⇒ WHAT THIS DOES TO THE RECEIPT

`receipts/P15_CR_cosmology/P15_the_driving_shift_by_subtraction.py`, PART 4, states:

> *"The acoustic fold reports Q₁k² constant — an exponent of −2 — which its mechanism (a seam
> transient relaxing on 3ℋ/k²) requires. This instrument does not see that exponent."*

**The receipt quotes the fold accurately. The fold was wrong about itself.** Two consequences:

**(a) The disagreement is real but much narrower: −0.97 against −0.62, not −2 against −0.62.**
Whether that gap is instrumental or physical is a live question; a factor of 1.6 in exponent is not
a factor of 3.2.

**(b) The clause *"which its mechanism requires"* should go, and the sentence turned around.** The
3ℋ/k² mechanism requires −1; the fold measures −0.97; **so the fold's mechanism is not what the
disagreement is between.** What is left is two instruments giving −0.97 and −0.62 for the same
physical quantity, which is a question about the instruments and worth exactly the attention the
receipt already gives it.

⌗ *The receipt's numerical gate is unaffected — it tests `-1.2 < slope < -0.3` and −0.622 passes,
as would −0.97. **The defect is in the narrative, not the check**, which is the class the corpus
already names: a verdict written in prose beside a check that cannot see it.*

---

## ⌗ WHAT IS GENUINELY SHARED, AND IT IS THE LARGER PART

*Recorded so the correction is not mistaken for a dispute.* **Two instruments, built independently,
agree on all of this:**

| | receipt (c54.169) | fold (r2381) |
|---|---|---|
| ΛCDM's acoustic phase is **flat in k** | 0.791 → 0.774, **2.1%** | 0.868 → 0.846, **2.5%** |
| CR's **varies strongly** over the same band | **3.9×** | **3.7×** |
| the direction | falls with k | falls with k |
| the reason offered | *"no radiation era to cross, so the shift is not acquired at crossing"* | *"the modes never cross the sound horizon inside the L1 foliation"* |

**The phenomenon is independently reproduced, the explanation independently arrived at, and the
disagreement is confined to one exponent.**

## ⚠ AND ONE THING THE RECEIPT HAS THAT THE FOLD DOES NOT — this is the fold's defect, not the receipt's

**The receipt calibrates its undriven column and the fold never did.** The receipt measures
Q_undriven = 0.9968–1.0003 on both arms and reads everything against it; the fold used its
`PHIPOIS` datum as an undriven reference **without ever checking that it returns Q = 1**.

⌗ *And the receipt's first recorded correction is precisely the fold's method:* **"Q was first read
on Θ̂ = Θ₀ + Ψ; DR switches the couplings into the fluid but not Ψ's own evolution, so the undriven
column carried a non-oscillating piece and calibrated at 0.0003."** **The fold reads Q on
Θ̂ = Θ₀ + Ψ throughout.**

⇒ ***The exponent gap may be exactly this, and it is checkable at low cost: re-read the fold's Q on
Θ₀ = δ_γ/4 alone and refit.*** *That is the next move, and it is the fold's to make. Stated as a
named unrun question rather than a conclusion — the fold's own calibration failure is a live reason
to prefer the receipt's number, and this note does not claim otherwise.*

---

# ⛭ ADDENDUM — the named unrun question, RUN. The variable is not the explanation.

*Stated above as the next move; done in the same session rather than left as a debt.*

Read the **same runs** both ways in one process, so nothing can differ but the variable. ✔ **CONTROL:
the Θ̂ column reproduces L-114 to 0.0004.**

| | k=0.0376 | 0.0563 | 0.0774 | 0.0988 | 0.1208 | 0.1427 | fit | rms |
|---|---|---|---|---|---|---|---|---|
| **Θ̂ = Θ₀+Ψ** *(the fold's variable)* | 0.588 | 0.364 | 0.259 | 0.211 | 0.182 | 0.161 | **k^−0.966** | 0.046 |
| **Θ₀ = δ_γ/4** *(the receipt's variable)* | 1.546 | 0.325 | 0.234 | 0.191 | 0.165 | 0.146 | k^−1.619 | **0.306** |
| Θ₀, lowest-k point dropped | — | 0.325 | 0.234 | 0.191 | 0.165 | 0.146 | **k^−0.854** | 0.023 |

*The receipt's `kη > 1` exclusion removes nothing here, exactly as the receipt says it will on the CR
arm — its modes are already sub-horizon at the onset.*

⛔ **SO THE VARIABLE IS NOT THE EXPLANATION.** Switching to Θ₀ moves the fold from −0.966 to −0.854
(dropping an outlier the fit cannot carry) — **toward the receipt's −0.62 but nowhere near it**, and
on the full set it makes the fold's own power law *worse*, rms 0.046 → 0.306.

⌗ *Every figure in this table is machine-printed by `S002_theta0_refit.py`, and the two in the last
row were re-run rather than carried across by hand — which, in a note whose subject is a
hand-carried number, is the minimum.*

⇒ **The most obvious candidate is eliminated and the disagreement stands at ≈ −0.9 against −0.62.**
Named, unrun, and now genuinely the next thing: *the two instruments differ in what "undriven" means
— the receipt flips one multiplicative switch in the couplings; the fold slaves Φ₀ to a Poisson
datum. Those are different references and only one of them is calibrated. **The fold's is not, and
that is where I would look next.***

---

# ⛭⛭⛭ SECOND ADDENDUM — THE DISAGREEMENT LARGELY DISSOLVES, AND THE CORPUS HAD THE INSTRUMENT

*Found by re-running `ACOUSTIC_two_arm.py QSCAN=1` on the current (c54.178) instrument, after `S-011`'s
scan flagged that the receipt behind this note was pinned at c54.169.*

**First: the pin holds.** The driven CR column still fits **k^−0.63** on the rebuilt instrument, so
nothing in the receipt's headline moved. *`S-011`'s flag was a question, and this is its answer: not
stale in this figure.*

**But the c54.170 split — which post-dates the receipt this note corrects — changes what the
disagreement IS.** `P15_which_coupling_carries_the_k_dependence.py` switches the two couplings
independently, and reproduced here:

| configuration | Q range | variation | **fitted exponent** |
|---|---|---|---|
| undriven *(calibration)* | 0.9980 – 1.0002 | 1.00× | k^+0.00 |
| **continuity only** *(the 4Φ′ — the DECAY channel)* | 0.1091 – 0.1767 | 1.62× | **k^−0.18** |
| **Euler only** *(the k²Ψ — the GRADIENT)* | 0.0640 – 0.5577 | 8.71× | **k^−1.04** |
| **driven** *(both)* | 0.1167 – 0.4635 | 3.97× | **k^−0.63** |

⇒ ***THE FOLD'S −0.968 SITS ON THE EULER COLUMN (−1.04), NOT ON THE DRIVEN COLUMN (−0.63).***

**So the two lines were never measuring the same object, and both numbers are right:**

- **The corpus is right about the mechanism.** The fold attributes its k-dependence to a seam
  transient relaxing on 3ℋ/k² — *a statement about how the potential DECAYS* — and decay feeds the
  fluid through the continuity coupling. **That channel is nearly flat: k^−0.18.** The receipt's own
  framing is exact: *"the k-dependence lives in the potential's gradient, not in its decay."*
- **And the fold's number is not wrong.** −0.968 ± 0.001 against Euler-only's −1.04 is 7%. **The fold
  measured the gradient coupling and attributed it to decay.**

⌗ **Which also explains the reading-variable clue this note's first addendum could not use.** The
fold reads Q on **Θ̂ = Θ₀ + Ψ**; the receipt reads it on **Θ₀**. Θ̂ absorbs the potential's own value,
which is the thing the continuity channel feeds — **so a Θ̂-read is the one that would suppress the
continuity contribution and leave the Euler behaviour standing.** *That is a hypothesis with an
obvious test, named rather than assumed:* **run `QSCAN=1` with Q read on Θ̂ instead of Θ₀ and see
whether the driven column moves from −0.63 toward −1.** *If it does, the two instruments are
reconciled completely and the residue is a documented choice of variable rather than a discrepancy.*

⇒ **NET, and this supersedes this note's opening framing:** *the "disagreement between instruments"
is largely an artefact of comparing a two-coupling number with a one-coupling number.* **What
survives as a real correction to the fold is its MECHANISM, not its exponent** — and the corpus
already had the instrument that shows it, built one revision after the receipt this note corrects.
