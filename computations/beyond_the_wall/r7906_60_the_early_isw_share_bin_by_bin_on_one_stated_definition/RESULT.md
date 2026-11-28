# r7906 (60) — THE EARLY-ISW SHARE IS STRUCTURED ACROSS THE BAND, FALLING BY A QUARTER FROM ITS LOW EDGE, AND THE Σ RESPONSE FALLS WITH IT BY A FACTOR OF FOUR

Order `r7903` (69) item ②. Registered in `PREDICTION.md` and **pushed** before the first per-bin
share existed. **Outcome `Ⓘ⓷ + Ⓚ⓵`.**

## The definition, and what was and was not computed

`S_b(Σ) = (full_b − noISW_b) / full_b`, on the instrument's **unlensed** `TT` binned through the
likelihood's **own** `TT` binning, at Σ = `0`, `0.06`, `0.30`, `0.60` eV on the control arm, whose
centre is the reference's own parameters.

⛭ **The band the order names is EXACTLY twelve of the likelihood's own `TT` bins** — indices `14`
through `25`, edges `100`–`108` up to `199`–`207`, with `207` a bin's own top edge — read from
`score_ttteee`'s `BIN_LO`/`BIN_HI` rather than typed. No partial bin exists and none had to be
dropped.

⛔ **No spectrum was computed.** `r7900` ran the instrument eight times at exactly these sums on
exactly this arm; what did not exist is the per-bin share. The measurement is a new reading of an
existing bank, and the registration said so before it was made.

## The twelve shares

| bin | `ℓ` | Σ = `0` | `0.06` | `0.30` | `0.60` | `S(0.60) − S(0)` |
|---|---|---|---|---|---|---|
| `14` | `100`–`108` | `0.438702` | `0.439786` | `0.447351` | `0.460550` | `+2.1848e-02` |
| `15` | `109`–`117` | `0.440062` | `0.441004` | `0.447470` | `0.458837` | `+1.8775e-02` |
| `16` | `118`–`126` | `0.435825` | `0.436644` | `0.442180` | `0.452006` | `+1.6181e-02` |
| `17` | `127`–`135` | `0.427468` | `0.428182` | `0.432937` | `0.441477` | `+1.4009e-02` |
| `18` | `136`–`144` | `0.416217` | `0.416841` | `0.420945` | `0.428413` | `+1.2195e-02` |
| `19` | `145`–`153` | `0.403049` | `0.403598` | `0.407159` | `0.413730` | `+1.0680e-02` |
| `20` | `154`–`162` | `0.388720` | `0.389205` | `0.392312` | `0.398131` | `+9.4106e-03` |
| `21` | `163`–`171` | `0.373795` | `0.374227` | `0.376952` | `0.382136` | `+8.3406e-03` |
| `22` | `172`–`180` | `0.358687` | `0.359072` | `0.361476` | `0.366119` | `+7.4325e-03` |
| `23` | `181`–`189` | `0.343677` | `0.344023` | `0.346153` | `0.350334` | `+6.6566e-03` |
| `24` | `190`–`198` | `0.328979` | `0.329290` | `0.331185` | `0.334965` | `+5.9853e-03` |
| `25` | `199`–`207` | `0.314713` | `0.314993` | `0.316682` | `0.320110` | `+5.3975e-03` |

## What it says

**① `Ⓘ⓷`: STRUCTURED, and not monotone.** The span at Σ = `0` is `0.3221030244` of the mean, against
a registered bar of `0.10`. ⛭ *The STRONG expectation — that `Ⓘ⓵`, flat in `ℓ`, would be refuted —
is **met**, on the grounds the registration gave: `r7900` measured most of the with-and-without
difference as interference with the acoustic monopole, and `100`–`207` is the rise toward the first
peak.*

**② `Ⓚ⓵`: the Σ response is POSITIVE in all twelve bins**, `12` positive, `0` negative, `0` zero. The
WEAK expectation holds, and it was right to be weak — a band sum rising does not force every bin to
rise, and here the per-bin check is what establishes it rather than the band figure.

**③ UNREGISTERED, and the two facts the outcome glyphs do not carry.**

- **`Ⓘ⓷` fires on a SINGLE turning point at the band's own low edge.** The only rise is bin `15`
  over bin `14`, by `1.360e-03`; from there the share declines in every one of the remaining `10`
  steps, from `0.440062` at the peak to `0.314713` at the top — a fall of `28.4844` per cent across
  the `10` bins above it. ⌗ *So "not monotone" is a weaker statement here than it sounds: the shape
  is a monotone decline with one step up at the edge, not a band without an order.*
- **The Σ RESPONSE falls with `ℓ` too, monotonically, by a factor of `4.04783900227215`** —
  `+2.1848e-02` in the lowest bin against `+5.3975e-03` in the highest. ⇒ *The band-integrated rise
  `r7900` measured is carried disproportionately by the band's low edge.*

## The control that licenses the rest

`Ⓒ⓵` **`r7900`'s own band definition, recomputed here from the same files in its own arithmetic
order, reproduces its banked fractions at EXACTLY ZERO** — `0.3812497286698585`,
`0.38180361645716626`, `0.38546214867806106`, `0.39221513157332405`.

⛔ **The FIRST form of that control FAILED, and the bar was right.** It took means where `r7900` took
sums — the same number mathematically, a differently rounded one in double precision — and reproduced
the fractions to `2.776e-16`, about five units in the last place, against a bar that says exactly
zero. *The arithmetic was mine, so the arithmetic was matched rather than the bar widened.*

`Ⓒ⓵ᵃ` The two file families `r7900` wrote — the decomposition's own total and the separate `TT` save
— are **bit-identical** at every sum on both arms, so the control and the shares are read off one
spectrum. `Ⓒ⓶` The switch-off arm is identified from the **run**: the four `isw` bilinear pairs
identically zero and the other six bit-identical, at every sum. ⌗ *`r7900`'s saved `config` does not
record the switch, so a file called `_noisw` is otherwise only a file called `_noisw`.* `Ⓒ⓸` Every
bin is fully covered by the banked grid, which starts at `ℓ = 100`, the first bin's own low edge.

## What is not claimed

- **NO COMPARISON, AND NO SHORTFALL.** `cc66`'s CAMB side is its `⑲ ③` and has not landed; the order
  says neither side reads the other until both are banked. `Ⓧ⓵`/`Ⓧ⓶` are registered here and
  reported **NOT READABLE**.
- ⛔ **And the order's "follow it to its term" is NOT begun.** The three candidate terms it names —
  the potential's decay rate after recombination, the visibility's tail, the radiation fraction in
  the potential — are a decomposition **of a shortfall**, and no shortfall exists until both sides
  are banked. Picking among them on one side's numbers would be answering a question nothing has
  asked yet.
- ⚠ **The share is not "the ISW's contribution to the band".** `r7874` established that `D_ℓ` is
  quadratic in the transfer, so a with-and-without difference equals the four `isw`-involving
  bilinear pairs — at Σ = `0`, `r7900` measured the cross pair at `24.2` per cent of the band
  against the self pair's `8.5`. One label, two objects, and only the difference is measured.
- **No mechanism and no limit.** A share is not a mechanism; `r7888`'s `193.545` meV is untouched.
- **Nothing about the late ISW**, which `69` closed as a fork at `r7903`.
