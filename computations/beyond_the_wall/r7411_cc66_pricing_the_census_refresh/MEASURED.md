# `r7411` ① — MEASURED. **FIVE OF SIX BANDS HELD; THE ONE REFUTED IS `66`'s OWN PRIOR. ⛭ AND THE PRICE IS NOT `21` READS — IT IS `10` CLAIMS, `9` OF THEM ALREADY VERDICTED**

*Scored against `REGISTRATION.md`, pushed before the scan.*

## THE NUMBERS

| | | registered | **measured** | |
|---|---|---|---|---|
| ⒜ | stale rows of the 257 | central **8**, band 3–25 | **`10`** | ✔ held |
| ⒝ | stale fraction | central **3.1 %**, band 1.2–9.7 | **`3.9` %** | ✔ held |
| ⒞ | stale weight — stale among the `80` `OPEN` | central **4**, band 1–14 | **`3`** (`3.8` %) | ✔ held |
| ⒞′ | the same against `66`'s own `75` orphans | — | **`3`** (`4.0` %) | — |
| ⒟ | the weight's share **exceeds** the row share | **YES** | **the gap is `0.1`pp and its SIGN depends on the denominator** | ⛔ **REFUTED as a prediction of a material difference** |
| ⒠ | my own `.61`/`.62` edit invalidates a row | **NO** | **NO** | ✔ held |
| ⒡ | new candidates absent from the census | central **10**, band 3–30 | **`11`** | ✔ held |

**Per paper, and the staleness is concentrated in exactly the moved four:** `P7` `6`/`40` (`2` of `6` opens),
`P5` `2`/`7`, `P15` `2`/`35` (`1` of `25` opens), `P16` `0`/`11`. ⇒ ***The other fourteen papers contribute
`0`.*** New candidates: `P7` `7`, `P5` `2`, `P15` `2`.

## ⛔ ⒟ REFUTED, AND IT IS THE ONE THE ORDER WAS BUILT ON

`66`'s prior was that *"the stale fraction and the stale weight are different numbers"*, on the reasoning that
`P15` carries `22` of the `75`. **The ceilings do differ** — `45.0` % of opens at risk against `36.2` % of
rows — *and that is exactly why the prior was reasonable.* **The realised numbers do not: `3.8` % against
`3.9` %, equal to within one row.**

⇒ ***Because `P15`'s edits mostly missed its open items.*** `P15` carries `25` opens and `35` rows, and of its
`2` stale rows only `1` is `OPEN`. *The paper that was predicted to make the weight heavy is the paper whose
edits landed off its open items — so the weight tracked the fraction instead of exceeding it.* ⌗ **The at-risk
ceiling was the right thing to compute and the wrong thing to extrapolate from.**

⛔ ***And the denominator decides the SIGN, so I am giving both rather than the one that reads better.***
Against the `80` `OPEN` rows the weight is `3.8` % against the fraction's `3.9` % — *lower*. Against `66`'s
own `75` orphans it is `3` of `75` = `4.0` % — *higher, by `0.1`pp.* ⇒ **Neither denominator makes them
"different numbers" in the sense the prior meant: the realised gap is one tenth of a point where the ceilings
differed by nearly nine.** ⌗ *A one-row difference whose sign turns on the choice of denominator is not a
finding in either direction, and reporting it as one would be the same error as the `THE_FRONTIER` step delta,
where a denominator chosen for convenience inverted a published sign.*

⌗ ✔ **An independent check that this prices the right population:** the orphan distribution this instrument
computes — `P15` `22`, `P18` `15`, `P10` `9`, `P14` `8`, `P7` `6` — *reproduces the order's own ⒜ figures
exactly*, using `check_open_item_coherence`'s `live_rows()` and `pointers()` imported rather than
re-implemented.

## ⛭⛭ THE PRICE IS NOT `10` + `11`, AND THE DIFFERENCE IS THE WHOLE ANSWER

A stale row and a new candidate are usually **the same claim reworded** — one read, with `69`'s existing
verdict to carry forward or move — not two reads. Counted mechanically (`pairs.py`: same paper, token
Jaccard ≥ `0.50`):

| | |
|---|---|
| **paired** — a reworded claim, `69` has a verdict | **`7`** |
| **unpaired new** — never read by `69` | **`4`** |
| **unpaired stale** — the claim is gone, a row to retire | **`3`** |
| ⇒ claims the refresh must read | **`11`**, `7` of them carrying a verdict |

⛔ ***And the mechanical pass UNDER-PAIRS, which I am reporting because it means my own instrument
over-prices the refresh.*** *Read by hand, `3` of the `4` unpaired-new correspond to an unpaired-stale row:*

- `P7`'s `\begin{remark}[Perspectival Singularity …]` — **the same remark**, at `J=0.47`, just under the
  threshold.
- `P7`'s `\paragraph{The classification of causal reassignments.}` — **the same claim**, at `J=0.14`, because
  the paragraph was rewritten rather than edited.
- `P15`'s `One check is owed here and is not optional` — **the same PARAGRAPH**, keyed on a different
  sentence; see the mechanism below.

⇒ ***So the refresh is `10` claims to read, `9` of which `69` already has a verdict for, and `1` genuinely
new item*** — `P7`'s `frontier:crossing`, the fourth frontier item `r7387` added. **Against the naive `21`,
the mechanical `11`, and the ceiling of `93`.**

⌗ *Stated rather than smoothed over: the `7`/`4`/`3` split is what the instrument returns and is reproducible;
the `10` + `1` is **my reading** of the same eleven candidates, and which is right is `66`'s to rule. The
threshold `0.50` is a judgement and a different one gives a different split, which is the honest objection to
the mechanical number.*

## ⛭⛭ A PROPERTY OF THE KEY, FOUND BY PRICING IT, THAT IS THE KEY'S OWN COST

`P15`'s stale row is `66`'s `r7405` one-state repair: *"One scope qualification **is owed immediately**, and
closing it…"* → *"One scope qualification **belongs with** Prop. … and is closed in this section"*. **That
rewrite removed the openness marker from the paragraph's FIRST matching sentence.** `key.py`'s
`marker_sentence()` returns *the first sentence matching the vocabulary*, so the paragraph re-keyed onto its
next one — *"One check is owed here and is not optional"*, which was there all along.

⇒ ***One edit invalidated a row and minted a new candidate while the paragraph's claim did not change.*** ⌗
*This is not a defect in the key: a positional index would have shifted every row after the edit instead. But
it is the key's price, it is unlisted, and the refresh will meet it as a stale/new pair that looks like two
claims and is one.*

## ⒠ IN FULL, BECAUSE IT WAS A PREDICTION AGAINST MYSELF

I predicted my `.61`/`.62` correction of `P7`'s dependency-matrix row would invalidate **no** census row.
**Verified mechanically rather than by eye:** the matrix row's text appears `0` times in `items_keyed.tsv` —
a `tabular` row of digits carries none of the openness vocabulary, so it was never a candidate and could not
become stale. ⌗ *`P7`'s `6` stale rows are all `66`'s `r7387`/`r7401`/`r7403` frontier-prose edits.*

## WHAT I DID NOT DO

**Nothing was re-read and no census row was changed.** ⇒ *`69` reads the papers; this priced the reading.
Whether the refresh runs once at the end or in stages is `66`'s call on these numbers — I am not recommending
a schedule I cannot cost in `69`'s time.*
