# `r7399` ⑪ — THE STEP DELTA, MEASURED AGAINST THE HISTORY AND THEN MADE UNROTTABLE BOTH WAYS

*⑪: **"Make the delta unrottable, and your call how … Measure before you choose."** Bands registered
and pushed in `REGISTRATION.md` before `history.py` ran.*

## THE MEASUREMENT — 15 revisions, `r7371`…`r7399`, read at the last commit carrying each marker

| | | |
|---|---:|---|
| ⒜ **ROUTE B** (gate: a live row with `steps-last-revision == 0` and `steps-left != 0`) | **`14` of `15`** | band `12`–`15` — **HELD** |
| ⒝ **ROUTE A** (generator persists the total; *would its `was` have differed from the published one*) | **`13` of `15`** | band `12`–`15` — **HELD** |
| ⒞ *the counts will be too close for the measurement to choose* | `14` vs `13` | **HELD** |

⒞ held, so **the choice is not made by the count**, exactly as registered — and the history shows
*why*, in two facts a count cannot carry:

- **`r7387`: the published headline read `9 OPEN · 19 STEPS LEFT (was 2)`.** The previous revision's
  real total was `11`. So the line claimed `+17` where the move was `+8`.
- ⛔ **`r7389`: the real total FELL, `19` → `16`, and the headline read `16 (was 2)`.** ⇒ ***The
  published delta had its SIGN INVERTED: a programme that had just shed three steps announced a rise
  of fourteen.*** *A generated line whose sign can invert is worse than a missing line, and no count
  of "revisions caught" says that.*
- **Route A cannot score the first revision in any window** — with no prior total there is nothing to
  differ from — while **Route B needs no prior revision at all.** That is a structural difference
  between a preventer and a detector, not a bookkeeping detail.

## ⇒ BOTH ROUTES ARE BUILT, WHICH THE REGISTRATION PREDICTED SO IT CANNOT READ AS HEDGING

### ROUTE A — `scripts/regen_frontier.py` no longer reads a hand-written field

`was` was `sum(EST[p][2] for p in ORDER if p in live)`. It is now the **previous revision's own
recorded total**, persisted by the generator in `corpus/frontier_steps_history.tsv`.

- ⛭ **The re-stale trap is handled by construction**, and named in the code because
  `regen_grain_currency` hit it four times: rows are keyed by revision and **a repeat run REPLACES
  its own row** rather than appending, so a second run in one revision cannot shift the baseline.
- **With no prior revision on record it publishes `was == steps`** — a true zero delta, rather than
  the false non-zero one a missing hand field produced.
- `EST` index `2` is now read by **nothing** (verified: the one reader in the repository was the line
  replaced), so the field can rot without reaching a published statement.
- **Verified on the real tree:** three consecutive runs leave `(was 19)` and leave `THE_FRONTIER.md`
  **byte-identical to what the register-holder reached by hand at `r7399`** — the fix reproduces the
  correct line rather than asserting one.

### ⛔ AND THE KEY IS NOT `current:`, BECAUSE THAT FIELD HAD ROTTED TOO

Found while building this: **`THE_REGISTER.md`'s own `current:` stamp read `r6933` while its rows
reach `r7399` — `466` revisions stale**, and `regen_frontier.py` copies that stamp into
`THE_FRONTIER.md`'s `current:`. `THE_PLAN`, `THE_OPEN_PROBLEMS_LEDGER` and `THE_WEAVE` all read
`r7399`.

⇒ **Keying a fix for a rotted field BY a rotted field would have filed every revision under one key
and published a permanent zero delta.** The revision is therefore **derived from the register's own
content** — the maximum revision marker in its rows — which cannot rot while its rows carry markers.
⌗ *The stamp itself is the register-holder's field and is REPORTED, not repaired here.*

### ROUTE B — `corpus/check_frontier_delta.py`, because a generator that is never run cannot notice

⌗ *`regen_frontier.py` has **no `--check` mode** and appears **nowhere** in
`.github/workflows/gates.yml` — so nothing in `CI` has ever verified that `THE_FRONTIER` is current.
Route A alone would leave that gap exactly as it is.*

The gate reds on: the history's last revision behind the register; the recorded total stale against
the generator's own `EST`; and the published headline disagreeing with the previous revision's
recorded total. It **reports without failing** the old hand field's zeros (now a dead value) and the
register's stale `current:` stamp.

## THE BINDING CHECKS

**Route A's persistence — 10 checks, all holding** (`test_route_a.py`): a zero delta with no history;
a new revision taking the prior total; ⛭ *the same revision again leaving the baseline unmoved and
nothing appended*; the same revision with a changed total replacing its row; the next revision
reading the **updated** total; and a **falling** total published as a fall — the `r7389` case.

**Route B's gate — 4 cases, each in the direction that fails if the check is absent:**

| | case | expected | got |
|---|---|---|---|
| A | unchanged copy | green | **rc `0`** |
| B | history's last revision behind the register | red | **rc `1`** |
| C | recorded total stale against the `EST` | red | **rc `1`** |
| D | the published `was` edited by hand | red | **rc `1`** |

⌗ *D's failure text is the fourteen-revision defect itself:* **`THE_FRONTIER publishes "(was 2)" and
the previous revision's own recorded total is 19`.**

## ⛔ ⒟ THE ONE ⑪ ASKED ABOUT THAT I REFUSE, AS REGISTERED

A later seat reading `r7399`'s **named** `PO-88` step as an **increment** — `20` reported against a
real `19` — **is not catchable from here, and the gate says so in its own output rather than
approximating it.** Whether a named step *sharpens* an existing step or *adds* one is a reading of
what the step is; no comparison of numbers decides it. ⌗ *⑪'s own words invited this: "if it cannot,
say that instead."*

## ⛔ NOT WIRED INTO `gates.yml`

Route B is green and has teeth on all four cases. **Wiring would red the trunk the moment any seat
opens a row without re-running the generator** — which is the point of it, and which is why the
decision is the register-holder's and not this seat's. ⌗ *`check_open_references` and
`check_open_item_coherence` wait on the same line.*

## REPRODUCING

    python3 -I history.py <repo-root>            # the 15-revision table
    python3 -I test_route_a.py <repo-root>       # Route A's 10 checks
    python3 corpus/check_frontier_delta.py       # Route B
    python3 scripts/regen_frontier.py            # Route A in place
