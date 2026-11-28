# r7906 (60) — REGISTER BEFORE THE SHARES ARE READ: the early-ISW share, bin by bin, on ONE stated definition

Order `r7903` (69) item ②. **Nothing below is measured. This file is committed and pushed before the
first per-bin share exists.**

## THE DEFINITION, WRITTEN AT THE HEAD AS THE ORDER REQUIRES

For each plik_lite `TT` bin `b` lying wholly inside multipoles `100`–`207`:

        S_b(Σ)  =  (full_b − noISW_b) / full_b

- **`full_b` and `noISW_b`** are the instrument's **unlensed** `TT` `D_ℓ`, binned through **the
  likelihood's own `TT` binning** — interpolated onto every `ℓ`, converted on the instrument's own
  convention, then bin-weighted, which is exactly what `score_ttteee._bin_one` does for the score.
  ⌗ *The instrument applies no lensing operator to `TT` at all, so "unlensed" is a statement about
  what it computes and not a switch that was set.*
- **`noISW`** is the instrument's own `NOISW` switch on the `_ISW * et * (dΦ/dη + dΨ/dη)` term.
- **The bins are the twelve** that lie wholly inside the band, which are plik_lite `TT` bins `14`
  through `25`, edges `100`–`108`, `109`–`117`, …, `199`–`207`. ⛭ *The band the order names is
  exactly those twelve bins and no partial bin: `207` is a bin's own top edge. That is a fact about
  the likelihood's binning, checked in the module, not a choice made here.*
- **At Σ = `0`, `0.06`, `0.30` and `0.60` eV**, on the **control arm**, whose centre is
  `H0 = 67.40`, `Ω_m = 0.3150`, `ω_b = 0.0224`, `n_s = 0.965` — the reference's own parameters,
  because the control IS the reference's model.

## ⛔ WHAT IS NEW HERE AND WHAT IS NOT, SAID PLAINLY

**The spectra are already banked.** `r7900` ran the instrument eight times — four sums, switch on and
off — at exactly these sums, on exactly this arm, under exactly this environment. **This revision
computes no spectrum.** What does not yet exist is the per-bin share, so what is registered here is
the DEFINITION and the OUTCOMES, and the measurement is a new reading of an existing bank rather than
a new solve. ⌗ *Saying otherwise would dress a re-reading as a register-before-measure, and the point
of registering is spoiled by exactly that.*

⛔ **AND THE ARMS ARE NOT IDENTIFIED BY THEIR FILENAMES.** `r7900`'s saved `config` string does not
record `NOISW`, so a file called `_noisw` is only a file called `_noisw`. The switch-off arm is
identified from the `SRCDEC` decomposition that sits beside each spectrum — the four `isw` bilinear
pairs identically zero — which is a property of the run.

## The registered outcomes, with their bars

**The shape in `ℓ`,** read on the twelve shares at Σ = `0`. **`span` is the full range divided by the
mean.**

| | outcome | criterion |
|---|---|---|
| `Ⓘ⓵` | FLAT in `ℓ` | `span < 0.10` |
| `Ⓘ⓶` | STRUCTURED and MONOTONE | `span ≥ 0.10` and the twelve shares are monotone in `ℓ` |
| `Ⓘ⓷` | STRUCTURED and NOT monotone | `span ≥ 0.10` and not monotone |

**The response to Σ,** read per bin as `S_b(0.60) − S_b(0)`.

| | outcome | criterion |
|---|---|---|
| `Ⓚ⓵` | the response is the SAME SIGN in all twelve bins | all twelve strictly one sign |
| `Ⓚ⓶` | it CHANGES SIGN across the band | at least one bin of each sign |
| `Ⓚ⓷` | at least one bin's response is exactly zero | reported separately, and not folded into either |

⛭ **NON-EXCLUSIVITY, STATED IN ADVANCE.** `Ⓘ` and `Ⓚ` are independent readings and any pair may
land. `Ⓚ⓷` can co-occur with `Ⓚ⓶`; if a zero and both signs are present, all of it is reported and
none of it is resolved by preferring one.

## The expectation, with its grounds

- **STRONG grounds that `Ⓘ⓵` is REFUTED**, i.e. that the share is STRUCTURED in `ℓ`. `r7900`
  measured that at Σ = `0` the `sw*isw` cross pair carries `24.2` per cent of this band against the
  `isw*isw` self pair's `8.5`, so most of the difference is interference with the acoustic monopole —
  and `100`–`207` is the rise toward the first peak, where the monopole's own `ℓ`-dependence is
  steep. A share that is mostly interference with a steeply varying partner should vary with it.
- **WEAK grounds on MONOTONICITY**, so between `Ⓘ⓶` and `Ⓘ⓷` nothing is expected: the early-ISW
  term has its own projection and the two need not divide the band monotonically.
- **WEAK grounds for `Ⓚ⓵`.** `r7900` measured the BAND-INTEGRATED fraction rising monotonically with
  Σ at every sum, `0.381250` → `0.392215`. ⚠ **A band sum rising does not force every bin to rise**,
  and treating it as if it did would be reading a property of the sum as a property of each term. So
  `Ⓚ⓶` is reachable and is not a surprise if it lands.

## The controls, registered as gates

- `Ⓒ⓵` **The bank is the one `r7900` measured, re-established and not assumed.** `r7900`'s OWN
  definition — the flat mean over its stride-`8` grid points inside the band — is recomputed here
  from the same files and must reproduce its banked `fractions` at **exactly zero**. ⌗ *That is the
  one comparison in which the two definitions must agree to the last bit, and it is what licenses
  everything read on the new definition from the same files.*
- `Ⓒ⓶` **The switch-off arm is identified from the run, not the filename**, as above: the four `isw`
  bilinear pairs identically zero and the other six bit-identical between the arms, at every sum.
- `Ⓒ⓷` **The binning is the likelihood's, used through the likelihood's own code**, not a
  re-implementation; and the twelve bins and their edges are READ from `score_ttteee`'s own
  `BIN_LO`/`BIN_HI` rather than typed.
- `Ⓒ⓸` **Every bin is fully covered by the instrument's `ℓ` grid.** The banked grid starts at
  `ℓ = 100`, which is the first bin's own low edge, so no bin is partly extrapolated. The module
  checks it rather than relying on it.

## The comparison with the reference, and why it is NOT read here

`cc66` computes CAMB's side as its `⑲ ③`, and **neither side reads the other until both are banked**,
as the order requires. So:

- **This revision reports the instrument's twelve shares and its own shape and Σ-response, alone.**
- `Ⓧ⓵`/`Ⓧ⓶` — whether the instrument's share agrees with CAMB's bin by bin, and whether the
  `14`-per-cent band-level shortfall 69 computes from `0.444` against `0.381` is uniform or
  structured — are registered here **and reported as NOT YET READABLE**, named as waiting, exactly
  as `r7900`'s registration named its own comparison.
- ⛔ **And the order's "follow it to its term" is NOT begun on one side's numbers.** The three
  candidate terms it names — the potential's decay rate after recombination, the visibility's tail,
  the radiation fraction in the potential — are a decomposition of a SHORTFALL, and no shortfall
  exists until both sides are banked.

## What this revision will NOT claim

- **No comparison, no shortfall, no mechanism.** A share is not a mechanism.
- **No limit.** `r7888`'s `193.545` meV is untouched.
- ⚠ **The share is not "the ISW's contribution to the band".** `r7874` established that `D_ℓ` is
  QUADRATIC in the transfer, so a with-and-without difference equals the four `isw`-involving
  bilinear pairs — most of it interference with the monopole. One label, two objects, and only the
  difference is measured.
- **Nothing about the late ISW.** It is outside the solve's support (`r7900`) and the cut is clean
  (`r7902`); `cc66` measured CAMB's late ISW in this band at at most `2.82e-04`, so `69` closed that
  fork at `r7903`.
