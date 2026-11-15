# `r7797+cc66.2` — RESULT: items ① and ③ of `r7797`, as one receipt

**8 of 8 gates**, `rc=0`
(`receipts/P15_CR_cosmology/P15_the_low_multipole_depths_on_the_one_rate_at_every_l_from_2_to_8_and_the_cross_validation_becomes_3_0_and_the_reversal_is_the_ladders.py`).
Every registered row held on the first run. The runtime is gate ⑦'s CAMB transfer; the other seven
are a bank read and five paper parses.

## ① Every multipole, ℓ = 2 through 8

| ℓ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| **(L)**, arm A, distances' point | 0.4848 | 0.4407 | 0.3536 | 0.6569 | 0.9087 | 0.9828 | 0.9992 |
| **one rate** | 0.4898 | 0.4351 | 0.3594 | 0.6677 | 0.9120 | 0.9856 | 0.9973 |
| move, per cent | +1.031 | **−1.271** | +1.640 | +1.644 | +0.363 | +0.285 | **−0.190** |

Rounded: **`0.485 0.441 0.354 0.657 0.909 0.983 0.999`** → **`0.490 0.435 0.359 0.668 0.912 0.986 0.997`**.

⛭ **`P15` already prints all seven**, at `sec:scope` — *"the deficits are 0.485, 0.441, 0.354, 0.657,
0.909, 0.983 and 0.999 of the flat expectation at ℓ=2 through 8"* — and arm A under (L) at the
distances' point reproduces **all seven to the digit**. The `r7783` receipt pinned four of them;
this one pins the whole run, which is what the order asked for.

**The sign alternates.** ℓ = 2, 4, 5, 6, 7 rise; the **octopole falls**, and so does ℓ = 8. So the
move is not a rescaling of the curve — `r7779`'s finding, now at all seven.

### The two things the order asked to have pinned do not move

**Minimum at ℓ = 4 under both clocks. Recovery at ℓ = 8 under both clocks** (first ℓ ≥ 5 reaching
0.99 — the `r7779` bank's own definition, not one chosen here). So every **shape** claim `P15` makes
survives the clock unchanged, at all five sites that state the ℓ = 4 minimum; only the depths move.

## The cross-validation: 2.9 → 3.0, at five sites, and the companion clause survives

| | arm A vs arm B **decoupled**, distances' point | above ℓ = 5 |
|---|---|---|
| (L) | **2.9129 %** → the paper's `2.9` | 0.2971 % |
| one rate | **3.0328 %** → `3.0` | 0.3653 % |

**Named by build, not by the prose:** arm B's **frozen** build at the same point gives **6.1934 %**,
so the decoupled build is a measurement. Both maxima fall at **ℓ = 4**, where the dip bottoms — the
deepest point is the hardest to cross-validate, which is a property of the ratio, not a defect.

⛭ **The clause *"to 2.9 per cent at every multipole"* appears at five sites and all five become 3.0.
The companion clause *"to under one per cent above ℓ = 5"* SURVIVES UNCHANGED** (0.2971 → 0.3653 %),
so it needs no edit. **That is the part of this result that saves work.**

## ⛭⛭ And the move takes P15 *into* agreement with its companions — gate ⑤

The order said the depths *"sit in P7 and P18"*. They do, **differently**, and neither needs the
cross-validation figure changed:

- **P7** (`CR_framework`) prints the **quartet** `0.485, 0.441, 0.354, 0.657` *and* says the transfers
  are *"cross-validated between two independent transfers to **three per cent**"* — already three.
- **P18** (`CR_synthesis`) prints the **ℓ = 4 minimum** (*"bottoming at ℓ=4 and not at the
  quadrupole"*) and *"the two transfers agreeing to **three per cent** at every multipole"* — and
  **no depths at all**.

**So only P15's five `2.9`s move, and after they move the three papers agree.** P7 needs its quartet
moved; **P18 needs nothing.**

## ⑥ The abstract

It states the figures in a different **order** and to a different **precision** — two decimals at
ℓ = 4, three at ℓ = 2,3 — so it is parsed on its own terms: `0.35`, `0.485`, `0.441` → **`0.36`,
`0.490`, `0.435`**.

## ③ The mechanism, carried in as a check — gate ⑦

The `r7783` ladder computation is run from source and reproduces inside this receipt:

**Moving `r₀` alone, at fixed transfer, gives the measured sign at 5 of 5 multipoles** (ℓ = 2…6), the
**ℓ = 3 reversal included**; and the **`L = 2` floor term alone carries that sign at 4 of 4**
(ℓ = 2…5).

| ℓ | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| measured move (one rate / (L) − 1), per cent | +1.451 | **−1.524** | +1.351 | +2.015 | +0.744 |
| $-\partial\ln(\text{depth})/\partial\ln r_0$ | −1.4940 | **+2.1727** | −3.8724 | −2.8292 | −0.7551 |
| sign agrees | ✔ | **✔** | ✔ | ✔ | ✔ |

**The mechanism in one sentence:** the depth is the `L = 2`-floored Riemann sum (step dL = 1) of the
very integral it is divided by; the ladder `k_L = √(L(L+2))/r₀` carries **no projection distance**, so
the distance enters only through `Δ_ℓ`'s `j_ℓ(kχ)` and moving it acts the way moving `r₀` does; and
because the ladder is floored hard at `L = 2`, each multipole's response follows that one mode — **so
the ℓ = 3 reversal is commensurability between the floor and the ℓ = 3 kernel.** Not in the dynamics,
not in the clock.

## The blob licence, named rather than relied on silently

The distances-point arm B pair is **blob-confounded**: its two legs came off different instrument
versions. `r7779` established by **normalised-AST equality** that the newer blob *is* the same program
with `SPLITCLOCK` unset, and that every rate object the dynamics read is bit-identical
(max |old − new| = 0.0e+00 over 9 objects). That licence is inherited here. ④'s one-rate column is
the only row that needs it.

## Paper pins are disjunctions wherever 69's rewrite is the success condition

①, ②, ⑤ and ⑥ test that the sentence prints **one of the two sets this receipt measures**, and report
**which**. A pin on the current wording would go red on the very rewrite this receipt is for —
`check_quote_pins`'s own named failure mode.

## Not claimed

No likelihood, no significance, no new instrument run, and no claim that the one-rate depths fit the
sky better or worse. The `Δ(−2 ln L) = +1.7` scoring `sec:largescale` prints is untouched. Whether the
depths should be reprinted is 69's. Gate ⑧ asserts that scope against this file's own AST.
