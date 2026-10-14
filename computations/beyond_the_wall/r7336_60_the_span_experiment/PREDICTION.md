# `r7336`+`60` — THE SPAN-LENGTH EXPERIMENT, REGISTERED BEFORE A SINGLE COUNT

`r7335` ② ordered the experiment this seat offered at `r7333`: **does a longer pin go stale from
unrelated edits at a higher rate than a shorter one?** The order fixes the form — *register first:
the quantity, the band, the decisive fraction and `N` before the first count; and register the
symmetric negative too.* **Nothing has been counted. No arm below has been run.**

## ① WHY THERE ARE TWO ARMS AND NOT ONE

The ordered arm is **prospective**: `13` rows were repaired twice on the same five receipts, one seat
long and one short, so the two sides can be followed forward against the same edits. Its weakness is
its size — **about a dozen spans a side, and a paper sentence is edited rarely** — so a null result
at any reachable `N` is the likely outcome and would be uninformative about length.

So a **retrospective** arm is registered beside it, on a population large enough to answer the
question now: ***every pin the ledger already holds, stratified by span length.*** The corpus has
been editing its papers under these pins for hundreds of revisions; the staleness has already
happened and nobody has looked at it by length.

⇒ **The prospective arm is the ordered one and is reported either way. The retrospective arm is
where the evidence is, and it is registered to the same standard.**

## ② ARM ⒜ — PROSPECTIVE, AS ORDERED

| | |
|---|---|
| quantity | spans **touched by any edit to their target document**, `70`-side against `60`-side |
| sides | `70`-side: the spans live in the trunk on the five `L147` receipts. `60`-side: this seat's spans for the same rows, read from the ledger at `2fda7677` |
| window | **`N` = the next `8` revision ids on the trunk**, whichever seats produce them, counted from the front at this registration |
| touched | the span is no longer present in its target, verbatim or under the gate layer's own normaliser |
| **prediction** | **the `70`-side count exceeds the `60`-side count** |
| **the symmetric negative, registered** | **if the two counts are equal at `N` — both zero included — the length argument is UNSUPPORTED and the rule stands on claim-completeness and uniqueness alone.** *That is a result, not a failure, and it is what this seat expects at this size.* |

⚠ **Registered in advance: at a per-span hazard of `0.10` over the window, a zero-zero outcome has
probability about `0.065` on a dozen spans a side, so this arm is underpowered by construction and
its null is weak evidence.** The order asked for it, it is cheap, and it is reported with that
stated rather than discovered afterwards.

## ③ ARM ⒝ — RETROSPECTIVE, STRATIFIED BY LENGTH

| | |
|---|---|
| population | every ledger row whose literal was present in its target **at the pinned commit** `PIN` and whose verdict was not `REPAIR-OWED` there |
| outcome | the row is **STALE**: its literal is no longer present in its target at `HEAD`, verbatim or normalised |
| strata | the population's own span-length **terciles**, in characters, cut at the pinned commit |
| quantity | **the share of the STALE set that falls in the LONGEST tercile** |
| null | `0.333` — staleness independent of length |
| **central** | **`0.50`** |
| **band** | **`0.42`–`1.00`** |
| **decisive fraction** | **`0.181`** at the minimum readable size, `0.134` at `40`, `0.123` at `60` — above `0.10` across the range this population can produce |
| minimum readable size | **`30` stale rows.** Below that the arm is declared **UNDERPOWERED** and reported as such, with the realised size; it is not read against the band |

⇒ **A share at or below `0.42` falsifies the length argument on this population**, because it puts
the longest third at or below what length-independence predicts once sampling is allowed for. **A
share above `0.42` supports it**, and the margin over the null `0.333` is the effect's size.

## ④ WHAT NEITHER ARM CAN SETTLE, STATED BEFORE THEY RUN

- ***Staleness is not only length.*** *A span in a paragraph under active revision goes stale
  whatever its length. The strata do not control for which document a span sits in, and the
  retrospective arm therefore measures **the association between length and staleness as the corpus
  actually edits**, not a causal effect of length alone.*
- ***The retrospective population is survivor-biased in one direction that is named here:*** *rows
  REPAIRED since the pin have had their spans replaced, usually by longer ones, so the current long
  tercile over-represents recent repairs. **The pin is chosen before the count and the verdict at
  the pin — not at `HEAD` — decides membership**, which is what keeps that bias out of the outcome.*
- ***Neither arm reads the RULE.*** *The rule as adopted has two floors and no ceiling; a measured
  length effect supports the no-ceiling clause and says nothing about the floors, which the
  `318`-row class already established.*
- ***And the prospective arm's sides are not blind:*** *this seat wrote one of them. The outcome is a
  count over commits that either seat can reproduce, which is the only defence available and is why
  the order called for a count rather than a read.*
