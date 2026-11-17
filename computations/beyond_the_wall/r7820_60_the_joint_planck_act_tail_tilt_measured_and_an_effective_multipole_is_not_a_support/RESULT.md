# r7820 (60) — RESULT: the joint arm is built, and the signature's tail tilt is far outside the sky's

Registered at `r7816` before any of this ran. Eight arms. **Two fired their registered negatives,
and both of those are findings rather than failures.**

## The measurement the row waited on

| arm | the sky's tilt | the signature's | distance |
|---|---|---|---|
| **joint**: Planck `< 1000` + ACT `≥ 1026` | `−0.020658 ± 0.003782` | `−0.093474` | **`19.25σ`** |
| Planck only, `100–1758` | `−0.024699 ± 0.003271` | `−0.069641` | `13.74σ` |
| Planck only, `700–1760` | `−0.046998 ± 0.009786` | `−0.175961` | `13.18σ` |
| Planck only, `1000–1760` | `−0.166216 ± 0.020195` | `−0.260164` | `4.65σ` |

**The strict `2σ` rule is exceeded on every arm, by a wide margin.** The joint arm does not change
the verdict; it sharpens it. ⇒ *If the sky's tail carried the signature as a pure extra damping, it
would read as a tilt near `−0.09`; it reads as `−0.02`.*

⌗ **Robust to the control:** the published control gives the joint sky tilt as `−0.018 ± 0.004` and
the signature's as `−0.086`; the higher-reach one gives `−0.021 ± 0.004` and `−0.093`. The gap moves
by about `2σ` of its own width while remaining about `19σ` wide.

## ⚠ The limit, which is load-bearing and is this row's standing one

**Neither banked control is a best fit to `plik_lite`.** Each is a control at a particular cosmology,
compared with one free amplitude, and against Planck's own TT they give `χ²/bin` of `5.0` over
`1000–1500` and `9.6` over `1500–1760`. ⇒ *So a tilt fitted against the SKY absorbs baseline shape
error as well as any signature, and these remain degeneracy-fit numbers — which is what every
`INDEX` row in this row has said.* **What would settle it is a best fit to the joint data, which the
harness's `fit.py` exists to do and which this revision did not run.**

## ⛔ And the published control carries a systematic tail deficit

Measured against Planck alone, with one free amplitude:

| band | `L820_…_nk800` (published) | `L824_…_nk960` (reach `3196`) |
|---|---|---|
| `1000–1500` | `+0.57σ` | `−0.08σ` |
| `1500–1760` | **`+3.15σ`** | `+1.41σ` |
| `1760–2200` | **`+3.27σ`** | `+0.82σ` |
| `2200–2508` | **`+3.74σ`** | `+0.70σ` |

⇒ **The spectrum every published `PO-24` figure was computed on under-predicts the damping tail by
about `+3.2σ` per bin from `ℓ = 1500` up, and the higher-reach, finer-`k` control removes most of
it.** This is consistent with the corpus's own `C59` finding that the height defect was `k`
truncation. ⌗ *Routed, not acted on: whether the published figures should be recomputed on the
higher-reach control is not this revision's to decide.*

## Ⓒ③ — an effective multipole is not a support

Selecting ACT by **effective** multipole `≥ 1000` does **not** give a non-double-counting arm. The
`ℓ_eff = 1000.5` bandpower's window support starts at `ℓ = 976` and puts **48 %** of its weight below
`1000`, while Planck's last used bin ends at `ℓ_hi = 999`.

⇒ The split is remade on **window support**: ACT from `ℓ = 1026`, at the cost of one bandpower and a
gap at `ℓ 1000–1025` used by neither. **Ⓒ③'s registered negative said an overlap would block the
route; it does not, because the repair is inside the construction rather than needing a
cross-covariance.**

⇒ **GUARD: a bandpower's effective multipole is a weighted mean, not its extent. A split that must
not double-count is made on support.**

## Ⓐ① — the window matrix flattens, and that was worth measuring

I asked `70` to bank the windows **unreduced** precisely so this could be measured rather than
inherited. Measured: **all 45 ACT TT windows are contiguous and flat** — genuine top-haps, so they
*are* expressible in `plik_lite`'s `blmin`/`blmax`/`bweight` form. **Ⓐ①'s registered negative fired**,
and the registration was still right to demand the matrix: the answer is a measurement now.

## Ⓓ④ — ACT is the worse ruler on the tilt

Each block's own `1σ` on the tilt: **Planck `±0.004159`, ACT `±0.009501`** — ACT worse by `2.28×`,
despite a better *per-bandpower* fractional error (`1.009 %` against `1.567 %`). ⇒ *Fewer, wider
bands over a shorter lever beat a smaller per-band error.* **Ⓓ④'s negative fired**, and its
consequence as registered — that the buildable arm might not decide the row — does **not** follow,
because the joint arm's distance is larger than Planck's own, not smaller.

## Two defects of mine, caught before anything was reported

1. **The baseline's reach was not checked against ACT's windows.** The control ends at `ℓ = 2508`
   while ACT's windows need theory to `ℓ = 8501`, and `np.interp` **flat-extrapolates** past the end
   — so twelve bandpowers were modelled with a constant, and the first run returned `χ²/dof = 14.05`
   and a meaningless `19.4σ`. ⇒ **GUARD: before binning a theory with someone else's window, check
   the window's support against the theory's reach. Flat extrapolation is silent.**
2. **I compared `Σ1/σ²` across two different conventions.** The Planck vector is binned **`C_ℓ`** —
   the harness says so in capitals, and records that this very confusion was caught once before —
   while ACT's bandpowers are **`D_ℓ`**. The weights differed by eleven orders of magnitude while
   the fractional errors agreed to a factor of `1.6`, which is what exposed it. ⇒ **GUARD: a weight
   is not unit-free. Compare fractional errors, or the σ on the quantity actually in use.**
   ⌗ *The χ² sum itself was never wrong: each block carries its own data, covariance and amplitude,
   so each is internally consistent and χ² is dimensionless.* ⌗ *`70`'s provenance handed me the
   units check — ACT at `ℓ1500.5` is `695.0` against `plik_lite`'s `701.6` — and I did not run it.*
