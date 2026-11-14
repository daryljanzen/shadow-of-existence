# `r7779+cc66` item ① — THE LOW-ℓ DEPTHS **DO** MOVE ON THE ONE RATE: FOUR TIMES THEIR OWN RULER, AND THE SIGN ALTERNATES

**9 of 10 rows hold. The one red is `R3`, and `R3`'s red IS the result** — the registered direction
was wrong by a factor of four, which is why the sharp threshold was registered rather than a safe
one. `rc=1` from `low_ell_depths.py` is that registered miss, not a defect.

## The answer to the order, in one line

The order asked whether the low-multipole depths move when the projection goes on the one rate.
**They do — by up to $1.976\,\%$ at $\ell=5$, where the projection distance that carries them moves
only $0.4984\,\%$.** And the move is not a rescaling: **the sign alternates**, $\ell=2$ down,
$\ell=3$ **up**, $\ell=4$ down, $\ell=5$ down, dying away by $\ell=7$–$8$.

*So the three figures of `r7767` and this one answer four different ways:*

| figure | how it responds to the rate |
|---|---|
| the damping signature $r_D/r_s$ | **cannot** move — the projection cancels identically |
| the fitted acoustic comb | moves **nine times less** than its ruler ($-0.055$ vs $-0.498\,\%$) |
| $\ell_A$ | moves **exactly with** its ruler ($-0.498\,\%$) |
| **the low-$\ell$ depths** | move **four times more** than their ruler, **with alternating sign** |

## The depths, clock against clock

Every pair below sits inside a **single** `.npz`, so one instrument blob and one producer run, with
every `config` field equal but `SPLITCLOCK` (`R0`). Banked to 4 decimals, so the grain is
$\approx 0.014\,\%$ — the moves are $70$–$140\times$ it.

| pair | $\ell=2$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| arm A, distances' point | $-1.021$ | $+1.287$ | $-1.614$ | $-1.617$ | $-0.362$ | $-0.284$ | $+0.191$ |
| arm A, refit point | $-1.112$ | $+1.240$ | $-1.636$ | $-1.688$ | $-0.450$ | $-0.284$ | $+0.040$ |
| arm B frozen, refit point | $-1.430$ | $+1.547$ | $-1.333$ | $-1.976$ | $-0.738$ | $-0.102$ | $+0.271$ |
| arm B decoupled, refit point | $-1.077$ | $+1.549$ | $-1.457$ | $-1.557$ | $-0.408$ | $-0.041$ | $-0.030$ |

*(percent, $({\rm L}) / {\rm one\ rate} - 1$)*

**The recovery multipole does not move** (`R4`): first $\ell \ge 5$ with depth $\ge 0.99$ is $\ell=8$
under **both** clocks in **all four** pairs. *So the clock reshapes the deficit without moving where
it closes.*

## It is the PROJECTION, not the dynamics (`R8`, post-hoc)

Arm A carries **CAMB's leaf-rate dynamics in both rows**, so its pair moves the *projection clock
alone*:

| | $\ell=2$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| projection only (arm A, refit) | $1.112$ | $1.240$ | $1.636$ | $1.688$ | $0.450$ | $0.284$ | $0.040$ |
| projection + dynamics (arm B frozen, refit) | $1.430$ | $1.547$ | $1.333$ | $1.976$ | $0.738$ | $0.102$ | $0.271$ |

**The projection clock alone moves $\ell=5$ by $1.688\,\%$ — already $3.4\times$ its own distance —
and is $85\,\%$ of the full move.** ⛔ The remainder is **not** a clean dynamics measurement: arm A
and arm B are different dynamics codes, so it bounds the dynamics share rather than isolating it.

## The amplification, and what is NOT explained (`R9`)

$|{\rm d}\log{\rm depth} / {\rm d}\log D_M|$ against the depth's own logarithmic slope in $\ell$:

| | $\ell=2$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| amplification | $2.87$ | $-3.10$ | $2.67$ | $3.96$ | $1.48$ | $0.20$ | $-0.54$ |
| $d\log{\rm depth}/d\log\ell$ | $-0.19$ | $-0.62$ | $1.24$ | $2.33$ | $1.13$ | $0.30$ | $0.11$ |

The depth is more clock-sensitive than its ruler at every $\ell \le 5$. ⛔ **I am not asserting a
mechanism.** A sampling-slope argument would want the amplification to follow that slope; it does so
in rough magnitude at $\ell = 4,5$ and **not at all** at $\ell = 2,3$, where the slope is negative
throughout while the amplification reverses sign at $\ell=3$ alone. **The $\ell=3$ sign reversal is
reported as unexplained.**

## Two corrections I owe

### My `r7767` reply was too strong

I said item 3 *"needs a run the bank cannot stand in for"*. **With the switch named, no run is
needed.** Four clock-only pairs were already banked (`R0`), at *both* parameter points. What was
true is narrower: the pair I had looked at differed by parameter point, and I could not identify the
switch. **No new instrument run was launched for this item** (`R7`).

### The pair the order names was the one confounded pair — and it is licensed anyway

`distances__armB_*__L` carries blob `c66bfff27…`; the one-clock leg at that same point is banked
separately at blob `5936a51b8…` (`R1`). So that pair differs by instrument *version* as well as by
clock. **`R2′` settles it rather than guessing:** normalise both blobs' ASTs for `SPLITCLOCK` unset —
rename `_Hdyn → Hc_of`, reduce every `IfExp` and `If` on `_SPLITL` to its false branch, drop the
`_SPLITL`/`_Hdyn` bindings, reduce `(A or _SPLITL)` to `A` — and **the two normalised trees are
identical**: with the switch unset the newer blob *is the same program*. An independent runtime arm
agrees — every rate object the dynamics read is **bit-identical** (max $0\cdot10^{0}$ over nine
objects), `_Hdyn is Hc_of`, `Jac_of` never defined. On that licence the confounded pair reproduces
**both** verdicts of the four clean ones ($1.933\,\%$, recovery unmoved) — `R6`.

*`R2` as first written could not have passed:* it asked that every differing executable line name a
split token, which fails any rename regardless of inertness — the **removed** lines `Hc=Hc_of(e)`
and `return out` name no split token because they are the lines being replaced. **The claim was
right; my test for it was wrong.**

## One thing for 69 that is not part of the order

`R5′`: the receipt's own frozen/decoupled standard is $3\,\%$. At the **refit** point these banks sit
at $3.39\,\%$ under (L) and $3.51\,\%$ under the one rate — **above the standard under both clocks**.
The registered condition (*the one rate exceeds 3 % where (L) does not*) is therefore **not** met, so
the clock does not break the cross-validation; but the $3\,\%$ figure was established at the
receipt's own point and build, and does not hold at this one. The one rate is worse than (L) by
$0.12$ percentage points, $4\times$ the bank's grain on that ratio — real, and small.

## Failability

`R0`/`R1` move under any edit to a bank's `config`. `R2′` goes red the moment a `SPLITCLOCK` change
touches the unconditional path — it is the row that would catch exactly that. `R3`/`R4`/`R6`/`R8`/`R9`
move under any change to the banked depth arrays; `R5′` under either refit-point build.
