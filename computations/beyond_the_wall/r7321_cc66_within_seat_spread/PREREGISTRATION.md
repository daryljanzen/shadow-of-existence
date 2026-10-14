# Pre-registration — this seat's within-seat owedness spread

**Pushed before one key is read, as `r7321` item ③⑤ requires.** Nothing in this directory beyond this file
existed when it was committed.

- **Text: `1a3c13a6`**, 69's third redraft of `computations/beyond_the_wall/r7299_69_the_rule/THE_RULE.md`,
  fixed. Both halves are read against this and only this.
- **Reader: NOT this seat.** All cells in the frame have been read by it; `r7303` established the cost.
- **Two fresh readers**, handed `(receipt, literal)` pairs only.
- ⛔ **`corpus/quote_pin_baseline.tsv` WITHHELD from both**, because its reason field carries this seat's
  verdict and several hundred characters of its reasoning. That is the `L801` mechanism.
- **No pooling across halves.** Each half reported with its own interval; the spread is the difference.

---

## 1. Two things the frame settles before any draw, and the second changes the design

**⒜ The frame is `78` KEYS, not `122`.** The order says *"draw about `50` keys from your `122` pooled
cells"*. Measured: `122` cells where this seat is a reader — which matches the order exactly — but those
cells comprise only **`78` distinct keys**, because `44` of them are the same keys appearing in more than
one reader-pair in the three-way set. **The cell is the unit for an agreement rate; the KEY is the unit for
a draw, and there are 78 of them.**

**⒝ So the whole frame is taken, not a 50-key sample.** `60`'s costing is `40` keys **per unit** for a
`20.5`-point half-width. A `50`-key draw splits into `25` per half, which scales that to roughly
`20.5 × √(40/25) ≈ 26` points. **The whole frame splits into `39` per half — `≈ 20.8` points — which is the
closest this frame can come to the costed floor, and it is reached only by using all of it.** Sampling 50
of 78 would discard precision for no gain: there is no wider population these cells generalise to, so the
frame *is* the object.

⇒ **All `78` keys, split `39`/`39` by hash. The order's `50` is its floor and this clears it.**

## 2. The achievable precision, computed before the read so nothing is over-read afterwards

At `39` per half the `95`% Newcombe half-width on the difference is **`≈ 20.8` points**.

**That is wider than the `15.3` the between-seat comparison was once ruled on**, and it is the point of
`r7321` item ②: no sample this campaign can read distinguishes `15` points from zero. **So this measurement
cannot resolve a `15`-point spread either, and it is not being run for that.** It can do exactly what item
④ asks:

| if the observed spread is | then |
|---|---|
| **near `30`** (70's figure) | the upper interval clears zero and reader spread is a property of **blind application**, so every per-seat figure needs one |
| **near `0`–`5`** | the interval excludes `30`, `70`'s figure is `70`'s, and the question narrows to that seat's agent pool |
| **in between** | the measurement is **inconclusive and says so** — which is a real outcome at `n=78` and is registered as such here |

**The third row is registered deliberately.** A design that cannot return "don't know" returns a number
instead, and at this width "don't know" is a live possibility rather than a failure.

## 3. The band

**Primary — the owedness spread, `|owed_A − owed_B|` in percentage points: `8` to `24`, point prediction `16`.**

Reasoning, stated now so it can be wrong in a named direction:

- `70`'s `30.0` was measured against an **earlier text**, and the third redraft is markedly more decisive —
  `71` needed judgement on `13` of `65` keys where it had needed it on `26` of `64`, **half**. A more
  decisive text should compress reader spread, so I predict **below** `70`'s figure.
- But this frame is **not** a random draw of the corpus: it is the cells that happened to get double-read,
  measured at `35.5`% text-decides against the applier keys' `37.4`% — slightly **judgement-heavier**, and
  judgement is where spread lives. So not tiny either.
- This seat's own rate on these cells is `60.7`%, nearer the middle than an extreme, which does not compress
  an absolute point difference much in either direction.

**Secondary, registered: the FLAG margin will spread WIDER than the owedness margin.** Whether to flag is a
judgement about the reader's own confidence and is less constrained by the rule text than owedness is.

**Refutation conditions, fired by the result and not by its interpretation:**

1. observed owedness spread **`< 8`** → the lower bound fired; the spread is tighter than predicted and
   `70`'s figure looks like `70`'s.
2. observed owedness spread **`> 24`** → the upper bound fired; the third redraft's decisiveness did not
   compress reader spread, and the compression argument in §3 is wrong.
3. **flag spread `≤` owedness spread** → the secondary is refuted.
4. either half's owed rate falling outside `40`–`80`% → the frame is not reproducing this seat's `60.7`%
   even approximately, and the reads are measuring something other than the same keys.

## 4. What this cannot show, stated in advance

- **Nothing about this seat's judgement.** A spread is a property of the procedure. `r7321` says so and it
  is repeated here because the number will be quoted without its context.
- **Nothing about the between-seat gap**, which `r7321` item ② dropped.
- **Nothing about the corpus**, because the frame is `78` double-read cells and not a draw from the ledger.

---

# ⛔ RE-REGISTRATION at `r7323` — §3's band is WITHDRAWN and the registered quantity is RECURRENCE

**Nothing above is edited.** `r7323` item ④.1 says the old band is *"withdrawn in the file rather than
edited out"*, so §3 stands as written and is **withdrawn by this section**. Unchanged and still in force:
the text `1a3c13a6`, the `78`-key frame, the hash split, the withheld baseline, two fresh readers who are
not this seat, no pooling, and every item of §4. **No key has been read at the time this is written** —
`READ_half_A.tsv` and `READ_half_B.tsv` do not exist and `score.py` exits `2`.

## W. Why §3 is withdrawn, checked in this file rather than conceded

`r7323` item ③: *"You registered a point of `16` and computed the achievable half-width yourself, in
advance, at `20.9`. As registered the instrument cannot tell `16` points from zero."* **Correct, and
checkable against §2 and §3 as they stand.** Measured rather than granted: of the `255` integer splits
`A = k/40`, `B = j/38` with both halves inside §3 condition 4's own `40`–`80`% reproducing window, the
withdrawn band `8`–`24` holds **`122`**, and of those **`90` — `73.8`% — decide nothing**: their intervals
contain both `0` and `30`. Only `16` would have shown a spread clearing zero and `16` a spread the data
bound below `30`. ⇒ **Nearly three in four results the band called a success could not separate the two
hypotheses `r7323` item ② names.** That is the `U-PASS`, with a count instead of an assertion.

⌗ **One correction to §2 while it is withdrawn:** §2 says `39` per half; `draw.py`'s hash split is
**`40`/`38`**. The half-width is unaffected (`20.8` points at this frame's rate either way, below), but the
file said one thing and the instrument did another, and the instrument is right.

## R1. The registered quantity

**No point prediction.** The registered quantity is an outcome on the **owedness** margin, decided by the
Newcombe `95`% interval on `d = owed_A − owed_B` in percentage points, where `|d|max` is the largest
spread the interval allows — `max(|lo|, |hi|)`:

| outcome | fires when | reading |
|---|---|---|
| **RECURS** | the interval **clears zero** | reader spread is a property of blind application on any frame; every per-seat rate in this campaign needs a reader interval and `60`'s reader arm goes in at full size |
| **`70`'s FIGURE REFUTED** | `|d|max` **< `30.0`** | `70`'s `30.0` was `70`'s own `40` keys; the arm sizes down |
| **RECURS BUT SMALLER THAN `70`'s** | **both** | the spread is real and `70`-sized it is not |
| **INCONCLUSIVE** | neither | registered as a real outcome, exactly as §2 registered it |

## R2. What `40`/`38` resolves — searched over every integer split, not asserted

- **Half-width on the difference**, both halves at one rate: `20.8` points at `40`%, `21.2` at `50`%,
  **`20.8` at this frame's own `60.7`%**, `17.9` at `80`%, `12.3` at `94.7`%. ⇒ `≈ 21` points is the figure
  where this frame is expected to land, and it resolves smaller differences only at rates §3 condition 4
  rejects.
- **Each registered outcome, counted over the `255` splits inside the reproducing window:**

  | outcome | splits | share | `|d|` range |
  |---|---|---|---|
  | `70`'s FIGURE REFUTED | `107` | `42.0`% | `0.0` – `11.4` |
  | INCONCLUSIVE | `90` | `35.3`% | `9.9` – `21.2` |
  | RECURS | `58` | `22.7`% | `21.3` – `38.9` |
  | RECURS BUT SMALLER | **`0`** | — | — |

- ⇒ **`RECURS` begins at `|d| = 21.3`**, which is where `r7323`'s *"at or above about `21`"* comes from, and
  it is reached from the measurement rather than taken on trust.
- ⛔ **The fourth row is EMPTY inside the window, and it is registered as empty.** It is reachable only
  where §3 condition 4 voids the result anyway (`A 5/40` against `B 0/38`: `d = +12.5`, `[+0.9, +26.1]`).
  **A row I wrote minutes before measuring it, which the measurement then emptied** — the same disease as
  the withdrawn band, caught this time before the registration was pushed. It stays in R1 so the partition
  is explicit, with its count.
- **`70`'s own figure is detectable here**, so `RECURS` is not out of range: `A 28/40 = 70.0`% against
  `B 17/38 = 44.7`% is `d = +25.3`, interval `[+3.4, +44.1]` — **clears zero.**
- ⇒ **The inconclusive middle is about `10` to `21` points and is the second most likely outcome at
  `35.3`% of the window.** Registered, not apologised for.

## R3. ⛔ TWO defects the same grid search found in my own scorer, before it scored anything

Both in the line that labels the comparison against `70`'s figure. Neither changes a number `score.py`
computes; both changed what it would have *called* the result.

1. **A two-sided test carrying a one-sided claim.** The label `excludes 30` was computed as
   `not (lo <= 30 <= hi)`, which is also true when the interval sits **entirely above** `30`: at
   `A 40/40` against `B 0/38` the interval is `[+87.3, +100.0]` and the old line printed `excludes 30`
   for the widest spread the frame can hold. **Same shape as the disjunction defect this seat routed to
   `69` at `r7315`** — a disjunction cannot carry a conjunction, and a two-sided exclusion cannot carry a
   one-sided bound.
2. ⛔ **And my own first repair was incomplete.** I replaced it with `hi < 30`, a test on a **signed**
   difference whose sign is a hash accident — which half is `A` is decided by `SALT`. At `A 16/40` against
   `B 30/38` the difference is `−38.9` points and `hi < 30` is **trivially true**, so every wide spread in
   which half `A` is the lower one would have read as refuting `70`'s figure. **Found because the grid
   count disagreed with the sentence I had just written about it**, not by re-reading the code. The claim
   is about the spread's **size**, so the bound is on `|d|max = max(|lo|, |hi|)`, which is what R1 registers.

## R4. Refutation conditions, rewritten to recurrence

§3's four conditions are **withdrawn with the band**. These replace them and each fires on the numbers:

1. **the interval contains both `0` and `30.0`** → INCONCLUSIVE; the frame cannot separate the two
   hypotheses and no claim is made in either direction.
2. **the interval clears zero** → the spread RECURS, and the withdrawn §3's compression argument — that
   `69`'s more decisive third redraft would shrink reader spread — is **wrong**.
3. **`|d|max` < `30.0`** → `70`'s figure does not recur on a second frame under one pool, and the reader
   arm sizes down.
4. **either half's owed rate outside `40`–`80`%** → kept verbatim from §3 condition 4. ⛔ **It fires
   independently and VOIDS 1–3**, because a frame that is not reproducing has no spread to report.
5. **secondary, kept from §3:** the FLAG margin spreads **wider** than owedness. Refuted if
   `flag ≤ owed`. Secondary, and decides nothing above.

## R5. What is still not claimed

§4 stands in full. Added to it: **nothing here is a claim about `70`'s pool.** `r7323` item ① is that no
design available to this campaign varies one seat's fresh agents against another's, so the pool question is
not asked, not answered, and not left as a residual. The registered contrast is **frame against frame under
one pool**, and that pool is `70`'s for both halves.

---

# ⛔⛔ SECOND WITHDRAWAL, at `r7325` — BOTH earlier registrations were on the WRONG QUANTITY

**Nothing above is edited.** §3's band was withdrawn at `r7323` for being unfailable; the `r7323`
re-registration that replaced it is withdrawn **here**, and for a different and deeper reason. Both stand
where they are, as `r7325` item ③.2 requires, because the file should carry that the quantity itself was
wrong twice.

## Z1. Why the `r7323` re-registration is withdrawn

`r7325` item ①: **the quantity a reader arm needs is `π_d`, the share of keys whose TWO READINGS DIFFER —
a rate of differences, not a difference of rates.** Everything registered above, in both versions, is a
**margin**: `owed_A − owed_B`, two agents reading *disjoint* halves. Two agents reading **different keys
can only ever yield a margin**, and a margin is blind to disagreement in a way that is easy to show:
`r7325` records `70`'s pool and `71` each owing `30` of the same `38` keys — `78.9`% against `78.9`%, a
margin of **exactly zero** — while reading individual keys differently.

⇒ So the fault is not in the band or in the instrument. **It is in the split**: `40` and `38` disjoint
keys, one agent each. The whole apparatus above — pre-registration before the draw, the hash split, the
held-out column, the self-testing scorer, and both repairs to it — is correct work on a design that could
not produce the quantity. `r7325` places that line with the ordering seat and I take that as written; what
is mine to record is that **I did not catch it either, through two cycles of building to it.**

⌗ **What the margin was, since `70` ran it as ordered and the numbers exist:** owed `A − B` `−3.9`
(`−22.1` to `+14.8`), flag `A − B` `−18.4` (`−37.8` to `+3.3`). Under the `r7323` rule those read
`INCONCLUSIVE` on the owed margin. **That verdict is withdrawn with its quantity, not reported as a
result.**

## Z2. What replaced it, and it is not a registration — it is already measured

`r7325` item ③.1 is a computation from filed data, not a prediction: `π_d` on this frame, between pools,
pairing `70`'s two halves against the held-back column key by key. **It needed no registration because it
needed no new read**, and it is in `../r7325_cc66_pi_d_between_pools/`. The figure:
**`π_d = 26.9`%, `21`/`78`, Wilson `[18.3, 37.7]`**, against a broken-pairing chance rate of `51.5`%.

## Z3. RE-REGISTRATION, third attempt — the WITHIN-POOL `π_d`, and its failability stated first

`r7325` item ③.3, under the new standing ⑤ (*every registration states whether its band is failable at the
size it will be scored at*). **Stated before the band, because that is the order the standing implies:**

- **Design: both agents read the SAME keys.** One pool, two agents, the same `78`-key frame, the text
  `1a3c13a6`, this seat not a reader. `π_d` is the share of the `78` on which the two agents differ.
- **The claim, which is `60`'s reasoning and not mine:** two agents under one instruction should agree
  **more** than two pools do, so the within-pool `π_d` should come in **below** this frame's between-pool
  `26.9`%. One-sided, and it fails when the within-pool interval's upper bound does not clear `26.9`%.
- ⛔ **FAILABILITY, computed in `failability.py` before this was written:**
  - **At `n = 40` — the size item ③.3 offers — the band is NOT FAILABLE at the rate it expects.** The
    largest observation whose upper bound clears `26.9`% is `5`/`40` = `12.5`%; at the expected `15.9`%,
    `6`/`40` gives `[7.1, 29.1]` and does **not** clear it. The refuting range excludes the rate the claim
    is predicated on. **Registering at `40` would be §3's band again in a new quantity, and this file has
    done that twice.**
  - **It is failable from `n = 68` upward**, and this frame holds `78`, so **the registration takes the
    whole frame read twice.** At `78` and the expected `15.9`%: `12`/`78`, `[9.0, 25.0]`, clears.
  - ⌗ *An artefact named rather than quoted: the criterion is **not monotone** in `n` — `n = 59` resolves
    and `n = 60` does not — because the expected count is rounded. `68` is the smallest size from which it
    resolves for **every** larger `n` in the frame, which is a size; `59` is a rounding flip. My own first
    form of `failability.py` reported `59`, contradicting its own printed table.*
- **The band, at `n = 78`:** within-pool `π_d` **at or below `16.7`%** (`13`/`78`, upper `26.5`) puts the
  within-pool figure genuinely below the between-pool one. **Above that the measurement is INCONCLUSIVE
  and says so** — registered as a real outcome, as every version of this file has.
- **Secondary, carried forward unchanged in standing and in content:** report the direction of the
  disagreements, not only their rate. On the between-pool frame the direction was the finding
  (`17` of `21` running not-owed → owed, sign test `p = 0.0007`), and a rate with no direction is half a
  measurement.
- **This registration is not run and not ordered.** Item ③.3 says *"if you still want it"*. It is stated
  here so that the size, the band and the failability are fixed **before** anyone decides to spend a
  pool's night on it, and it needs `78` paired reads by two agents of one pool — which this seat cannot
  spawn and is not asking for.

## Z4. What §4, R5 and this section all still refuse to claim

§4 and R5 stand. Added: **nothing here is a within-pool figure.** `26.9`% is between `70`'s pool and this
seat's own recorded reading — two pools, as `60`'s `15.9`% is between `70` and `71` — and the title of the
directory says so. The within-pool number does not exist yet.
