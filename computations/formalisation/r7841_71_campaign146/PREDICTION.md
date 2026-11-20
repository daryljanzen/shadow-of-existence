# `r7841+71.1` — CENSUS AND PRE-REGISTRATION: campaign 146, the exact statements the P14, P15 and P16 cold reads put into print, with the other exact statements landed since campaign 145. ⌗ `120` new Lean lines (band 70–200), p(F1–F3 all BUILT and landed) `0.75`

*The order is 69's `r7841`. It names three statements and asks for a census of any other exact statement landed
since campaign 145. Each is to be registered before any Lean, built, and landed beside its claim. The P15 row is to be
built only if it is more than arithmetic.*

*The probe will be the new standalone `probes/ColdReads.lean` (`cr_`), importing only Mathlib. Each landing is a plain
paragraph placed after its claim, in the form of campaigns 144 and 145.*

## The census

**What was read, at `628ad6c5f`.**
- `git diff 6cfab7d85 628ad6c5f -- corpus/*.tex`, the window since campaign 145's census. Apart from campaign 145's
  own landings, this adds only P14:745, the crest discriminant.
- Because two of the three named statements entered before `6cfab7d85`, through the r7833 and r7835 cold reads, the
  census also read `843b40b54..6cfab7d85` outside the Y10–Y17 sites. That is the window since campaign 144's landing.

### Cored rows: campaign 146

| Row | Paper:line | Claim | Formal core | Lines | p |
|---|---|---|---|---|---|
| F1 | P14:745 (named) | "the discriminant `(4−3r₀²)(3r₀²−1)²` vanishing" at the crest | under `2M = r₀ − r₀³`, `−4(−1)³ − 27(2M)² = (4−3r₀²)(3r₀²−1)²` as a polynomial identity. At `r₀ = 1/√3` it vanishes through the squared factor, and there `4 − 3r₀² = 3` | 20 | 0.97 |
| F2 | P16:579–580 (named) | "the throat and the collapse branch's extremum both lie outside the horizon radius, at `1.50` and `1.89 R_s`", for a progenitor at the Nariai mass | with `α > 0` and `2M = 2α/(3√3)`: the throat `α/√3` is `(3/2)·2M`. The extremum ratio `y = (2Mα²)^{1/3}/(2M)` satisfies `y³ = 27/4`, so `y = (3√3/2)^{2/3}`, with `1.889 < y < 1.891` and so `y > 1` | 60 | 0.85 |
| F3 | P16:582–585 (found by the census) | "`ρ = 1/6πGt²`, in which the progenitor mass cancels identically, and at one Planck time … exactly `ρ_Planck/6π`" | for marginally bound free fall with `r³ = (9/2)GMt²`, `M/((4/3)π r³) = 1/(6πGt²)` for all `M > 0`. With `t² = ħG/c⁵` and `ρ_Pl = c⁵/(ħG²)`, this is `ρ_Pl/(6π)` | 30 | 0.9 |

**The expected stop is F2** (p 0.85). The `1/3` power is bounded by cubing, as in campaign 145's `ns_cube`.

### Named, and not built: P15's `0.4835` row

The P15 sec:coherence statement is the deficit `1 − (0.4835/0.5)²` on the power, printed as 6.5 per cent against
3.3 per cent on the amplitude. Its whole content is `1 − x² = (1 − x)(1 + x)` at `x = 0.967`, together with the two
roundings. The squaring is the definition of the power. Nothing in it goes beyond arithmetic on one printed number,
and `0.4835` itself is the receipt's numerical integration. **So by 69's own criterion it is not built.** The census
records it as arithmetic only.

### Seen, and not chosen

- **P16, frozen modes.** "`|aH|` diverges as `1/x` … `c_s k/|aH| → 0` for every `k`". This is the same mechanism as
  P15's `cm_horizon_exit`, which is already built in `Cosmology.lean`. On P16's leg the `1/x` divergence rests on the
  numerical scale factor, so it has no new exact core.
- **The rest of the window has no formal core.** P18's neutrino thread, P7's and P16's η account, and P16's network
  figures are empirical, estimates or interpretive, and are covered by campaign 145's census of Y10–Y17.

## Landing

- **F1:** after P14:745.
- **F2 and F3:** one paragraph after the P16 sec:peak paragraph (P16:574–585).
- **P15:** no landing, since F-P15 is not built.

PDFs and served pages are rebuilt for P14 and P16.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
