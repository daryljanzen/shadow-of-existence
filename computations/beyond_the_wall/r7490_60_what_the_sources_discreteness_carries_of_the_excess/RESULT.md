# r7490 — THE EXCESS IS `99.3` PER CENT AMPLITUDE ON THE ARM'S OWN SPECTRUM, AND THE DISCRETENESS CARRIES `13.7` PER CENT OF IT ONCE THE TWO PARTS ARE READ APART

**COMPUTES:** nothing. No run; the four banked spectra are re-read with the imported statistic.

**THE ORDER** (`r7489` ①): *"say what part of the `0.045` excess the discreteness carries once
amplitude and phase are read separately, since the two moves cancel in the projected statistic and
need not cancel in the likelihood's own metric."*

**THE RULING IT CARRIES, taken as given:** the closed `S³` source spectrum is discrete by degree,
one mode per `L`, and the ladder reaches `k_max D_M ≃ 4000` at one mode per degree — **so the ladder
IS that spectrum and the continuum is the check**, which makes `r7480`'s two component moves the
measured effect of the source's **discreteness**.

---

## ⌈ ① THE IDENTITY THE WHOLE DECOMPOSITION RESTS ON, AND IT IS EXACT

> `proj = S_AB/S_BB`, `rms = √(S_AA/S_BB)`, `cos = S_AB/√(S_AA·S_BB)`
> ⇒ `rms × cos = S_AB/S_BB = proj` — **the algebra of the three sums and nothing else.**

| spectrum | `proj` | `rms × cos` | difference |
|---|---|---|---|
| **LADDER** (the arm) | `+1.045204` | `+1.045204` | `0.000e+00` |
| **CONTINUUM** `4.0` pts | `+1.045163` | `+1.045163` | `0.000e+00` |
| **CONTINUUM** `8.0` pts | `+1.045163` | `+1.045163` | `0.000e+00` |
| CONTROL vs itself | `+1.000000` | `+1.000000` | `0.000e+00` |

⌗ **Checked against the sums, not against the printed decimals** — five decimals could agree by
rounding, and `Ⓐ` was registered as falsifiable to machine precision precisely so that this is a
test rather than a restatement.

⇒ **So the excess splits exactly:** `proj − 1 = (rms − 1) + rms·(cos − 1)`.

---

## ⌈ ② THE DECOMPOSITION — THE EXCESS IS ALMOST ALL AMPLITUDE ON THE ARM'S OWN SPECTRUM

| spectrum | excess | **amplitude** | **phase** | phase share |
|---|---|---|---|---|
| **LADDER** (the arm) | `+0.04520` | **`+0.04552`** | `−0.00032` | **`0.71` %** |
| **CONTINUUM** `4.0` pts | `+0.04516` | `+0.04986` | `−0.00470` | `10.41` % |
| **CONTINUUM** `8.0` pts | `+0.04516` | `+0.04986` | `−0.00470` | `10.41` % |

> ⚑ **On the spectrum the ruling says is the arm's, the `0.045` excess is `99.3` per cent
> amplitude**: `+0.04552` of amplitude against `−0.00032` of phase, a ratio of `143` to one.

⌗ **And the continuum is not a small perturbation of that split**: its phase part is `14.7` times
larger while its amplitude part grows by `9.5` per cent of itself. *The two spectra agree on the
excess to four decimals and disagree on what the excess is made of.*

---

## ⌈ ③ THE ANSWER: WHAT THE DISCRETENESS CARRIES

| the move, ladder → continuum | value | as a share of the `0.045` excess |
|---|---|---|
| the **amplitude** part | `+0.00434` | `9.65` % |
| the **phase** part | `−0.00438` | `9.73` % |
| **their sum — the projected statistic** | `−0.00004` | **`0.09` %** |

**They are opposite in sign and their magnitudes agree to `0.9` per cent.**

> ⚑ **THE DISCRETENESS CARRIES `13.7` PER CENT OF THE `0.045` EXCESS IN QUADRATURE (`+0.00617`),
> AND `19.4` PER CENT IF THE TWO ARE SIMPLY ADDED (`0.00872`), AGAINST `0.09` PER CENT IN THE
> PROJECTED STATISTIC.**
>
> ⇒ **The projected number is a product of two factors that move oppositely, and reading it alone
> hides a tenth of the excess.**

### ⌊ THE METRIC IS NAMED AND ITS ARBITRARINESS IS STATED

**This seat has no data covariance.** What is used is the metric the statistic itself induces — the
two additive parts as components of one residual over the same `q` window — so the size is their
quadrature sum, with the `L1` sum printed beside it as the other obvious choice. ⛔ **A real
likelihood weights per-`ℓ` residuals by a covariance this does not have and would give a different
number. The figure is reported as what the decomposition gives in the statistic's own metric, not as
a likelihood result.**

---

## ⌈ ④ TWO THINGS THE BAND TABLE SHOWS THAT NO SCALAR DOES

| `q` band (index) | ladder `rms` | cont `rms` | **ladder corr** | **cont corr** |
|---|---|---|---|---|
| `[0, 200)` | `1.01533` | `1.01846` | `0.99985` | `0.99909` |
| `[200, 400)` | `1.05707` | `1.05290` | `0.99996` | `0.99792` |
| `[400, 600)` | `1.05048` | `1.07584` | `0.99997` | `0.99737` |
| `[600, 800)` | `1.06275` | `1.04236` | `0.99984` | `0.99270` |
| `[800, 1000)` | `1.06880` | `1.07639` | `0.99999` | `0.99440` |
| `[1000, 1200)` | `1.06633` | `1.07280` | `0.99990` | **`0.98505`** |

**⒜ The discreteness's phase effect is concentrated at high `q`.** The ladder's correlation with the
control is `≥ 0.9998` in **every** band; the continuum's falls monotonically to `0.985` in the top
one. ⇒ **So `13.7` per cent is an UPPER reading for a likelihood**: the phase half of it lives where
the damping tail gives a likelihood least weight, and a real covariance would discount it more than
it discounts the amplitude half. *That is a direction and not a number, and it is said because the
metric caveat would otherwise read as neutral when it is not.*

**⒝ The two moves agree to `0.9` per cent and this file does not know why.** A cancellation that
close is either a coincidence of this configuration or a structure of the statistic, and nothing
here distinguishes them. ⌗ **No mechanism is offered** — the corpus has paid for invented ones
before. What can be said is that it is **not** forced by the identity: the identity makes the
projected number the product, not the two factors' moves equal and opposite.

---

## ⌈ ⑤ THE ARMS — digest `744e5b6c`, pinned `9962d71c`, registered before the arithmetic

| arm | registered | measured | |
|---|---|---|---|
| **Ⓐ** `proj == rms × cos` | to machine precision | `0.000e+00` on all four | **HIT** |
| **Ⓑ** the ladder excess is almost all amplitude | `>100×` | `143×` | **HIT** |
| **Ⓒ** the continuum phase part grows, amplitude barely | `>5×`, `<10%` | `14.7×`, `9.5%` | **HIT** |
| **Ⓔ** `10`–`20` per cent in a metric that does not cancel | a **band**, before the arithmetic | `13.7` % | **HIT** |
| **Ⓕ** opposite and near-equal within `10` per cent | both | `0.9` %, opposite | **HIT** |

**Five hits.** ⌗ `Ⓔ` was registered as a **band before the metric was applied**, because a number
produced after choosing the metric is not a prediction — and the band was `10`–`20` where the answer
landed at `13.7`.

## ⌈ ⑥ THE CONTROLS — four, all held

- **Ⓥ① the imported statistic — PASS.** `r7093`'s predicate by `ast`, its own four printed rows
  reproduced to `2.97e-05` **before** any number of this revision's is read; the window is the
  statistic's own `q ∈ [0.85, 5.75]`.
- **Ⓥ② the identity checked on all four spectra — PASS**, against the sums rather than the decimals.
- **Ⓥ③ the metric named and its arbitrariness stated — PASS**, and `④⒜` says which way a real
  covariance would move it.
- **Ⓥ④ the per-band residual printed — PASS**, which is where `④` came from.

---

**Nothing is applied to the register. `PO-87` carries the discreteness effect as a property of the
construction, per the ruling; what share of the excess it carries in the likelihood's own metric
needs that covariance, and this says so rather than supplying a number dressed as one.
Supplied, not applied.**
