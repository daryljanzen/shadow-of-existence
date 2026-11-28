# r7898 — REGISTER BEFORE THE SCAN: are `193.545` meV and the reference's limit the same quantity?

Order `r7895` (69) item ①, `Ⓡ⓶`. ⌗ *Committed and pushed before any substituted limit is read.*

`r7888` read this instrument's calibrated limit at `193.545` meV on `70`'s ten lensing points.
`cc66`'s reference gives `30.560` meV calibrated and `54.000` meV ruler-minimised. The order's
hypothesis `Ⓡ⓶` is that the two are **not the same quantity** — that some part of the disagreement is
definitional rather than physical. The order requires the definitions stated point for point first,
then the instrument run on the reference's definition **one difference at a time**, with the limit
read after each.

## ⒜ WHAT EACH NUMBER IS, STATED BEFORE THE SCAN

Both sides are read through **the same likelihood module**, `score_ttteee.py`, which this seat built
at `r7842`. That is not an assumption: `cc66`'s reference modules import it (`import score_ttteee as
SC`) and use its `chi2_of`, `bin_three`, `BLOCK` and `BIN_LO`. So the following are **shared, not
differences**:

| | both sides |
|---|---|
| likelihood | `plik_lite`, binned `TT`+`TE`+`EE` |
| bins | `555` bandpowers, `185` per block, multipoles `100`–`1996` |
| covariance | restricted to covered bins **on the covariance and re-inverted**, which marginalises over uncomputed multipoles rather than conditioning on them |
| amplitude | ONE amplitude across all three blocks, closed form `A = (m F d)/(m F m)` |
| positivity | guard applied to `TT` and `EE` only, because `TE` changes sign three times inside reach |
| interpolation | spectrum interpolated in multipole BEFORE binning |

What differs is the **model** scored and the **ruler** the sum is read against:

| | this seat's `193.545` meV | `cc66`'s `30.560` / `54.000` meV |
|---|---|---|
| spectra | this instrument, hierarchy ON, envelope CLOSED | `CAMB` |
| ruler | this instrument's own `r_d`, derived at `r7862` (`147.0734` Mpc at `z_drag = 1061.185`) | calibrated: the reference's `rdrag`; minimised: `r_d` minimised |
| parameters | four profiled at every sum (`H0`, `OM`, `WB`, `NS`) | calibrated holds `omega_b` and `n_s`; minimised frees them |
| column read | calibrated; the minimised column is **unreadable** (`310.148` meV, non-monotonic above its minimum) | both columns readable |
| grid | `70`'s ten lensing points, run `46016816497` | `cc66`'s own grid |

## ⒝ WHAT THE RECORD HAS ALREADY SETTLED, AND IS NOT RE-RUN

⛭ Three of the five axes the order names are already measured. Re-running them would spend compute
to reproduce a known number, and the order's own instruction is to find what has NOT been measured.

| axis | already measured | by |
|---|---|---|
| likelihood, bins, covariance | **identical by construction** — one module, imported by both | `r7842`, read at source here |
| parameters held or profiled | freeing `omega_b` and `n_s` moves the reference `54.28` → `54.000` meV, **half a per cent** | `cc66`'s `r7853+cc66.12` |
| envelope closure | moves this seat's calibrated crossing `+0.00008` meV | `r7888` |
| ruler | substituting the reference's own ruler moved this seat's calibrated limit `146.13` → `89.91` meV | this seat's `r7862` |

⛔ **The ruler figure is the one that is STALE, and that is what this revision measures.** `r7862`
measured it **before** the hierarchy landed and before the envelope was closed. The current calibrated
column is `193.545` meV, not `146.13`. So the question the order asks is live on exactly one axis: how
much of the gap does the ruler substitution carry **on the current column**?

## ⒞ THE SCAN

One substitution at a time, each applied to the current calibrated column and to nothing else, with
the limit read after each:

1. **the ruler** — read the sum against the reference's own `rdrag` in place of this instrument's `r_d`
2. **the parameters** — hold `omega_b` and `n_s` as the reference's calibrated arm does
3. **the two together** — to see whether they compose or interfere, which neither alone can show

## ⒟ THE REPRODUCTION TOLERANCE, FIXED NOW

**`0.001` meV.** It is an order of magnitude above the largest move any measured no-op produces on
this column — `r7888`'s closure at `+0.00008` meV — and it is not chosen from the scan's numbers
because the scan has not run. A substitution moving the limit by more than `0.001` meV is a
definitional difference by the order's own criterion.

⌗ *This tolerance is deliberately tight, so almost any real substitution will clear it. That makes
the bare `Ⓡ⓶` test weak on its own, which is why the SHARE of the gap each substitution closes is
registered below as the quantity that decides the outcome. A test that everything passes decides
nothing.*

Gap, defined now: `193.545` meV against the arm each substitution makes the like-for-like partner —
`30.560` meV when the parameters are held, `54.000` meV when they are free.

    closed(s) = ( 193.545 − limit(s) ) / ( 193.545 − partner(s) )

## ⒠ THE OUTCOMES, FIXED BEFORE ANY SUBSTITUTED LIMIT IS READ

| | outcome | criterion |
|---|---|---|
| `Ⓡ⓵` | **DEFINITIONAL, AND ONE AXIS CARRIES IT** | some single substitution closes `≥ 0.5` of the gap |
| `Ⓡ⓶` | **DEFINITIONAL BUT SPREAD** | none alone closes `≥ 0.5`, the two together close `≥ 0.5` |
| `Ⓡ⓷` | **PARTLY DEFINITIONAL** | every substitution clears `0.001` meV but together they close `< 0.5` |
| `Ⓡ⓸` | **REFUTED — THE SAME QUANTITY** | no substitution moves the limit by more than `0.001` meV |

`Ⓡ⓸` is reachable and is the outcome the order explicitly asks to be said if it fires: *"If the
definitions already match point for point, `Ⓡ⓶` is refuted and you say so."* Given ⒝ it is the least
likely, and it is kept because a registered outcome that cannot fire is not a registration.

`Ⓡ⓵` and `Ⓡ⓶` are exclusive. `Ⓡ⓷` is exclusive with both. `Ⓡ⓸` is exclusive with all three.

⚠ **Declared in advance, so it cannot be presented as a surprise:** a substitution may move the limit
the WRONG WAY, *away* from the reference, making `closed(s)` negative. `r7888` found both physics
repairs moved the limit away from the reference, so this is a live possibility and not a remote one. A
negative share is **reported, not clipped**, and if every share is negative the outcome is `Ⓡ⓷` with
the sign stated in the headline, because a definitional difference that widens the gap is still a
definitional difference.

⚠ **And the minimised column is expected to stay unreadable.** `r7888` established it is
non-monotonic above its minimum, so a crossing on it is not a limit. If a substitution makes it
readable that is reported as a finding in its own right; if it does not, no limit is read from it and
no share is computed against `54.000` meV through it.

## ⒡ THE CONTROL, AND IT GATES EVERYTHING

Reading the limit with **no substitution at all**, through the same code path the substituted arms
use, must reproduce `193.545` meV to within the reproduction tolerance of `0.001` meV.

⛔ **If the control misses, no share is computed and no outcome is declared**, because every share is
measured from that number and a share measured from the wrong origin is not a weaker result but a
meaningless one. This is the same gate `r7896` used and the same reason.

## ⒢ THE REGISTERED EXPECTATION

**`Ⓡ⓵`, with the ruler.** The grounds are stated as what they are: `r7862` measured the ruler
substitution carrying `146.13` → `89.91` meV, which is `0.49` of that column's gap to `30.560` — just
under this registration's own bar, on a column that has since moved. So the expectation is an
extrapolation from one stale measurement across a changed column, and it is registered as the weaker
kind of ground. If the hierarchy has changed how the ruler enters, this expectation fails, and that
failure is the more informative result.

⌗ **What this revision does not touch.** It names no mechanism. It reads no new grid and dispatches no
runner job. It does not re-measure the three axes ⒝ records as settled, and if any of them is
re-opened by what the scan finds, that is said rather than quietly folded in. Item ② of the order, the
late-ISW term computed directly, is a separate revision and is not begun here.
