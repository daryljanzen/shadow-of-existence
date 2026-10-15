# `r7385` ⑨ ⒜ + ⒞ — THE REFERENCE ARM, PRICED AND THEN BUILT AS A RATCHET

*⑨ ⒜ authorises **"the mechanical reference arm — the law's own test, your `(paper, marker sentence)`
key, reporting candidate rows and quoting the law, never ruling"**; ⒞ authorises the **ratcheting
baseline** in the quote-pin ledger's shape. `r7383` Ⓔ orders the price first. Bands registered in
`REGISTRATION.md` and pushed before `price.py` ran.*

## ⛔ THE PRICE, AND IT DECIDES THE DESIGN

| mechanism | in the sentence | in its paragraph | band | verdict |
|---|---:|---:|---|---|
| `\ref{frontier:...}` | **`0`** | **`0`** | exactly `0` | **HELD** |
| `\cite{JanzenCRframework}` | `7` | **`41`** | `15`–`60` | **HELD** |
| `\rcpt{...}` | `13` | **`64`** | `120`–`200` | ⛔ **REFUTED LOW** |

Of the `221` sites priced: **`131` carry none of the three** in their paragraph, `49` carry only a
receipt key.

- ⒜ **HELD exactly, and it is the result the whole arm turns on.** `P7` §frontiers carries four
  labelled items (`frontier:scalar`, `frontier:sm`, `frontier:quantum`, `frontier:crossing`); all
  `5` occurrences of `ref{frontier:` in the corpus are inside `corpus/CR_framework.tex` itself.
  **The eighteen papers compile separately, so a `\ref` cannot cross a document boundary.** ⇒ ⛔ ***The
  law's literal test discharges `0` of `221`, and an arm that reds on "no reference" would red on its
  entire population*** — which is `r7383+cc66.48`'s `99`-per-cent artefact arriving by a second
  route, and `r7383` Ⓔ says refuse it.
- ⒞ **refuted low: `64`, not `120`–`200`.** Receipt keys are dense in the corpus but *not* in
  law-word paragraphs. ⌗ *The band was a guess about density and the measurement says the density is
  not where the guess put it.*

## ⇒ WHAT WAS BUILT INSTEAD: `corpus/check_open_references.py`, A RATCHET AND NOT A VERDICT

**It rules nothing and reds on one thing: a candidate site that is not in the baseline.** The backlog
is frozen; it may not GROW. Its failure text quotes `P7` §frontiers' law verbatim, as `r7383` ⑦
requires, and states that the gate is *not* calling the site a false-open.

- **The key is `(paper, normalised marker sentence)`** — `r7371+cc66.46`, and
  `prose_pin_baseline`'s own rule one level up: *a reworded expression is a NEW site and must be read
  again.*
- **`verdict` is a person's column.** `--regen` writes `UNREAD` for a new key and never changes an
  existing verdict. Permitted: `UNREAD`, `REFERENCED`, `FALSE-OPEN`, `NOT-AN-OPEN`, `OWED`.
- **`mechanism` is reported, never treated as a discharge.** `124` none, `49` `rcpt`, `26` `cite-P7`,
  `15` both.
- **Cost: `0` human readings to install.** The `214` sit as `UNREAD` and do not fail. The worklist
  comes down only by a person reading a site.

## ⛔ TWO DEFECTS IN THIS SEAT'S OWN NET, FOUND WHILE BINDING-TESTING THE GATE

The population moved from `221` to **`214`**, and the delta is named rather than adopted:
**`221` − `11` + `4` = `214`.**

1. ⒜ **A SECTIONING COMMAND CARRIES NO TERMINAL PUNCTUATION**, so the sentence split fuses it with
   the prose after it and the `HEAD` exclusion then vetoes that prose. **`4` prose open claims were
   invisible for exactly that reason**, among them `P3`'s `\paragraph{Open.} One thing is open, and
   \S\ref{sec:lap} states its obstruction exactly` — ⛭ *the plainest instance in the corpus of the
   claim the law targets, and the arm could not see it.* ⇒ the heading is now REMOVED from the run
   rather than used as a veto; a heading's own words are still never a claim.
   ⌗ *Found by accident: the first binding test injected its probe on the line after a `\section{...}`
   and the gate stayed green. **The botched test found a real defect.***
2. ⒝ **AN IDENTIFIER IS NOT PROSE.** `\label{rem:phase-open}`, `\S\ref{sec:open}` and a receipt key
   carry the law's words as machine names. **`11` of the original `221` were reached ONLY that way.**
   ⇒ *This is `r7391+cc66.50`'s finding — `13` of `69`'s `257` census rows reached only through a
   LaTeX identifier, `3` of them classed `OPEN` — applied to this instrument before it could repeat
   it.* Formatting that wraps PROSE (`\emph`, `\textit`) is deliberately not stripped.

⌗ **`price.py` is left at its registered `221` and not retrofitted.** The pricing is a historical
measurement with pre-registered bands; silently re-running it on a corrected population would make
the bands unfalsifiable. The two numbers and the arithmetic between them are the report.

## THE BINDING CHECKS, all four run

| | case | expected | got |
|---|---|---|---|
| A | unchanged tree | green | **rc `0`** |
| B | a new open-language sentence in its own paragraph | red | **rc `1`** |
| C | a new open claim FUSED to a `\paragraph{...}` heading | red | **rc `1`** |
| D | a law word present ONLY inside `\S\ref{sec:open-probe}` | green | **rc `0`** |

⌗ *C and D are the two corrections above, each tested in the direction that would fail if the fix
were absent. Run end-to-end against a copied corpus tree, not by patching the module.*

## ⛔ NOT WIRED INTO `gates.yml`, AND THE REASON IS NOT TIMIDITY

Wiring spends every seat's `CI` time and can red the trunk. `check_open_item_coherence.py` from ⑦ was
left unwired on the same ground, pending the `79` open-item dispositions. **This gate is green on the
current tree and has teeth on all four binding cases — wiring it is one line in `gates.yml` and it is
`66`'s to authorise.** ⌗ *`r7271` ⒟: the human is the intended bottleneck.*

## REPRODUCING

    python3 -I price.py <repo-root>                      # the pricing, 221 sites
    python3 corpus/check_open_references.py              # the gate
    python3 corpus/check_open_references.py --regen      # rewrite the baseline

⌗ **Gate runtime `0.417` s**, measured. ⌗ *`r7383` Ⓔ asked for three cheap arms rather than
one complete one; this is the cheapest of the three and the only one with teeth so far.*
