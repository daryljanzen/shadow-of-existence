# `r7687` (cc66) — VERDICT

Scored against `PREDICTION.md`, committed and pushed (`r7687+cc66.0`, `551739049`) before any
computation. **Four confirmed, one split, one discharged beyond its registration — and two claims of
mine from `r7685` withdrawn, which is the round's real event.**

## ⛔⛔ FIRST, THE TWO WITHDRAWALS, BECAUSE THEY WERE NOT ARMS AND MATTER MORE THAN THE ARMS

69 had **accepted** my `r7685` build finding as the content of the `\S`\ref{sec:scope}` sentence and was
about to land it. Item 3 sent me into `P15_the_low_multipole_depth_gap_closes…`; reading it first
showed it already gates the clause I had declared false.

1. **"Neither the freeze nor the towers is doing the work" is NOT falsified at ℓ = 4.** That receipt
   defines the clause as the **invariance of the conclusion** — minimum at ℓ = 4, recovery by ℓ = 8 —
   and on the distances bank both builds return `(4, 8)`. ⌗ *Its own `r7675`/`r7677` note names my
   error in words: "a namesake MEASUREMENT promoted to a bound on an intermediate quantity the claim
   never mentions." **I reproduced, in a finding 69 accepted, the defect the file I was sent to edit
   exists to prevent.***
2. **"The octopole is the clock" cannot be measured from these banks.** The ℓ = 3 excess is invariant
   to the **tower treatment** (spread `0.67` against a residual of `5.54`), which rules the towers
   **out** and does not rule the clock **in**. Both LEAFREC banks are `SPLITCLOCK`; the only one-clock
   bank carries **no point record at all**.

⌗ **And `4.90%` was not even a new quantity:** that receipt already computes `_agree = max|decoupled/
frozen − 1|` and prints it — `5.3%` at the refit point, **`5.2%`** on the distances bank. Mine was the
same diagnostic with a different normaliser, re-measured without noticing the receipt reports it.

## ① THE WORST PHASE COSTS NOTHING — ✔ CONFIRMED

Already scanned at all 24 phases and both amplitudes; only the fitted slope per phase was kept, so
**`0.54`/`0.51` was computed all along and never printed** (shared: `1.50`/`1.09`). *A measured
quantity a file keeps and never prints is as unciteable as one it never measured — the fourth shape of
this round's defect.*

## ② THE CARRIER CLAUSE INVERTS — ✔ CONFIRMED, and both halves of it

| | own comb | shared comb |
|---|---|---|
| null at the real phase | `+0.00328` | `+0.03088` |
| …one comb for both arms | **`+0.03088`** | *is the shared* |
| …envelope flattened | **`−0.00003`** | leaves most |

`+0.03088` under one comb **is the shared form's own value to five decimals.** ⇒ *On the shared comb
the envelope carries the null and one comb removes it; on the own comb the comb difference carries all
of it and the envelope carries none.* **My draft marked both clauses "holds".**

## ③ THE EFFECTIVE COUNTS — ⚠ SPLIT: confirmed on one, FALSIFIED on the other

I registered that both would be wrong **"in the upward direction"**. Only one is.

| | own comb | shared comb | registered | scored |
|---|---|---|---|---|
| slope effective count | `174.2` / `67.5` | `9.4` / `17.7` | above | ✔ **confirmed** |
| band `N_eff` of 7 | `1.94` / `2.27` | `3.77` / `3.45` | "differs", **upward** | ⛔ **falsified: it is DOWNWARD** |

⇒ *And the two together say something I had not expected: the own-comb null is **smaller in amplitude
and more coherent across bands** — fewer independent band modes, far less of it. I guessed "upward" for
both because I was reasoning from one quantity's formula and carried its direction to the other.*

⌗ **`174.2` is also not a count of modes, and I nearly sent it as one.** `n_slope = 7(s/\sigma)^2` is a
signal-to-systematic ratio shaped like a count: at `9.4`/`17.7` it reads as "nine to eighteen modes";
**above the band count it cannot** — it says the systematic is under this diagnostic's resolution.
*Routed as a ratio with that stated. This is the first time this round that check ran before the
sentence left rather than after.*

## ④ THE COST — ✔ DISCHARGED, in the opposite direction from registered

Registered: **under `+20%`** and under `540 s`. Measured alone, before and after: **`287 s → 105 s`, a
`2.7×` SPEEDUP while adding four figures.** ⌗ *`retained_own` does `C = C or retention_combs(banks)`
and the twelve settings never change the banks, so the scan refitted the same four combs twelve times
per phase — **528 times** — for identical results. Passing `C` is exactly equivalent.* **The receipt is
now cheaper than before the order.** Item 3 cost nothing measurable: `377 s → 377 s`.

**FAILABILITY, per commitment ⑦ — each assertion perturbed separately, not the computation once:**
all four of item 1's assertions gave **exactly one failure each, the matching one.** Item 3's eight
assertions: perturbing the decoupled row broke **all seven that should break** — the five value pins,
the invariance gate and the cannot-say gate — and left "the bank is present" passing, which is right.

### ⛔⛔ AND MY OWN VERIFICATION HARNESS GAVE THREE FALSE NEGATIVES BEFORE IT GAVE A RESULT

All three printed the **same observable, `0 FAILs`**, for three unrelated reasons, and only one of
those reasons would have meant "the pins are not failable":

| attempt | did the perturbation apply? | `0 FAILs` meant |
|---|---|---|
| first | **no** — my anchor wrote `_DZ["…"]`, the file has `_DZ['…']` | **nothing was tested** |
| second, leg A | yes | *(after fixing the token: **7 FAILs**)* |
| second, leg B | yes | **my off-by-one** — index 3 is ℓ = 5, not ℓ = 4, and no assertion reads the ℓ = 5 spread |

…and between the first and second, a fourth: **I grepped for `[FAIL]` while this receipt prints
`FAIL`**, so leg A's seven real failures were invisible and reported as zero.

⇒ ***A verification that reports one number cannot distinguish its own failure modes from its
result.*** The fixes were to assert the patch applied, diff the file before running, and read the
receipt's own token — but the general lesson is the same one this round keeps producing, one level up:
**`r7685` was an assertion that could not fail; this was a check whose PASS carried no information.**
⌗ *Marking the verdict's claim **pending** rather than asserting it is the only reason this was caught
instead of published.* ⌗ *And the "cannot say" gate's
metadata conjunct was checked to discriminate: `'config' not in files` is true only for the one-clock
bank — so if 70 ever banks a point for it the gate goes **red**, which is correct, because that is
exactly when the clock could be tested.*

## ⑤ EVERY ROW ENUMERATED — ✔ CONFIRMED, and the extra one is a new kind

Ten claims: five sound on the own comb, two convention-neutral, four misattributed (69's), **and one
that belongs to no measurement at all.** Row 6b — *"and the rest is that drift"* — reads the null's
**response to a chosen amplitude** as the drift's **share of the real signal**, which the cited
receipt's own NOT CLAIMED forbids in plain words. ⇒ *69's four are "this figure belongs to the other
statistic". This one belongs to no statistic.*

## ⑥ ITEM 3's FIVE PINS — ✔ CONFIRMED to the digit

`+5.54`, `+2.33`, `+0.57`, `−4.90`, `−0.67`, each two-sided at the printed precision, all exact.

## WHAT THIS ROUND ACTUALLY TAUGHT ME

**Three times in two revisions I produced a correct number and attached it to a claim it could not
support** — a sensitivity read as a decomposition, a per-multipole diagnostic read as a verdict on a
conclusion-level claim, and tower-invariance read as clock-causation. `r7679`, `r7681` and `r7685` were
all about figures going **stale, loose or unfalsifiable**, so every check I had built was aimed at
*whether the number is sound* and none at *whether the claim is the number's to make.*

⇒ **Commitment ⑧, and the one structural thing I did about it:** item 3 carries a gate that asserts
**what the bank cannot say**. Every other check in these receipts asserts something true; that one
asserts the boundary of what the data licenses, and it expires itself the moment the data that would
license the claim arrives. *A commitment I can forget; a gate I cannot.*
