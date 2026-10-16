# `r7403` ⓮ — THE SCOPE CHANGE, AND IT BUYS A DEFECT CLASS RATHER THAN A BETTER RATE

*⓮ ordered the extension, the measurement, bands before reading, before/after in one commit, and
`P7` left excluded. Bands are in `REGISTRATION.md`, pushed before anything was built or read.*

## ⓮ ③ BEFORE AND AFTER, IN THE SAME COMMIT

| | keys | sites |
|---|---:|---:|
| **before** (`r7401`, prose only) | `390` | `329` |
| **after**, `where = PROSE` | **`390`** | **`329`** |
| **after**, `where = COMMENT` | **`48`** | **`42`** |
| **after**, total | `438` | `371` |

⛭ ***The `PROSE` half is unchanged to the key.*** *That is the attributability ⓮ ③ asked for: the
growth is the comment blocks and nothing else. Every row carries its `where`, so the split is readable
off the file rather than taken on trust, and the `390` verdicts already written are carried forward —
`read_baseline()` reads a `7`-column row as the pre-⓮ layout, because a migration that lost a person's
column would be worse than the blindness it fixes.*

## THE BANDS

- ⒜ **new KEYS `25`–`60` → `48`. HELD**, and the reasoning held with it: I predicted `<` `55` because
  the `55` counts MATCHES rather than sites, and `48` is what the collapse comes to.
- ⒝ **new SITES `20`–`50` → `42`. HELD.**
- ⒞ **open claims among the new sites `40`–`80` % → `47.6` % ± `7.7`pp. BAND HELD, ⛔ REASONING WRONG.**
  *I predicted comment blocks would be LESS noisy than prose because a `STATUS` block is written to
  record status. They are not: prose is `52.5` % ± `7.9`pp and comment blocks are `47.6` % ± `7.7`pp
  — **the same within error, and if anything noisier.*** ⌗ *Why, from the read: a canon note carries
  provenance, policy and instructions as well as status, and those fire the net as readily as prose
  does.*
- ⒟ ⛔ **kind `②`'s share of the open-claim subset: predicted LOWER than prose's `61.9` %, band
  `10`–`50` % → `60.0` % ± `11.0`pp. THE BAND IS REFUTED HIGH, AND THE DIRECTIONAL PREDICTION IS NOT
  SUPPORTED.** *`60.0` ± `11.0` against `61.9` ± `10.6` is **indistinguishable**, and a `1.9`-point
  margin inside an `11`-point error is not a win. My reason — that a stated limit is addressed to a
  reader and a comment block is not — is **not borne out**: the notes state limits to the next SEAT
  exactly as the papers state them to a reader.*

Kinds of the `20` open claims: **`①` `6`, `②` `12`, `③` `2`.** `22` of the `42` state no open claim.

## ⛭⛭ ⒠ WHAT THE SCOPE CHANGE ACTUALLY BUYS, AND IT IS NOT THE RATE

⒠ was registered unbanded: *"a comment block whose claim DISAGREES with the printed paper … would be a
defect class and not just keys."* **Two things came out of the read, and both are classes rather than
counts.**

### ⒠① THE CORPUS HAS ALREADY CAUGHT ONE OF EXACTLY THIS CLASS, AND ITS NOTE RECORDS IT

`P8`, site `09`, in its own words:

> *"⚠ THIS NOTE READ "the deepest open question the construction RAISES" until `r2376+c54.179`, and the
> stronger phrasing is what propagated: `OPEN_PROBLEMS_MAP`'s `A·1` quoted it, and a register row
> inherited it, **so a map and a row both carried the item as an OPEN DISCOVERY while `sec:open`
> carries it as an EXHIBITION OWED**"*

⇒ ***A comment block's wording propagated into a map AND a register row and disagreed with the printed
paper — the `r7399`/`r7401` class, found by this programme before, recorded in the source, and
invisible to every net until this scope change.*** *It is historical (corrected at `r2376`), which is
why it is evidence that the class is real rather than a live defect.*

### ⒠② AND A NEW FALSE CLASS THAT IS SPECIFIC TO COMMENT BLOCKS: THE INSTRUCTION NOT TO REPORT

Three of the `42` are canon notes **instructing the next seat NOT to report something as open**:

- `P10`: *"**DO NOT REPORT THE COUPLED SECTOR AS A RE**[SIDUAL]"*
- `P11`: *"**DO NOT REPORT THE NONLINEAR RESONANCE AS OPEN.**"*
- `P12`: *"**THE SMEARED CLOSURE IS A COROLLARY, NOT AN OPEN ITEM.**"*

⇒ ⛔ ***A net that reads those as open sites is reading an instruction NOT to report openness as a
report of openness.*** *They are correctly classified `NOT-AN-OPEN-CLAIM` here because the rule reads
the claim and not the marker — but a gate that counted markers would invert them, and the inversion is
worse than a false positive: it would re-open exactly what the note exists to keep closed.*

### ⒠③ AND A RESIDUAL IDENTIFIER CLASS THE GUARD DOES NOT REACH, BECAUSE IT IS NOT LaTeX

`STRIP` removes `\label{...}`, `\ref{...}`, `\rcpt{...}`. Comment blocks carry identifier-shaped text
that is **not** a LaTeX command and so survives it:

- `P11`: `[frontier sec 13]` — a cross-reference written in prose brackets
- `P13`: `SILVER_PLATTER_colour-frontier-arc.md` — a FILENAME

⇒ *Both are `NOT-AN-OPEN-CLAIM` under the rule, so they cost reading rather than correctness. **Named
rather than patched: widening `STRIP` to bracket references and filenames is a change to the guard,
and `r7403` ⓮ ordered a scope change, not a guard change.*** ⌗ *Priced at `2` of `42`.*

## THE BINDING CHECKS — four, each in the direction that fails if the extension is absent

| | case | expected | got |
|---|---|---|---|
| A | unchanged copy | green | **rc `0`** |
| B | ⛭ a new marker in a `%` COMMENT BLOCK | red | **rc `1`**, reported as `3 LAW-SIX/COMMENT` |
| C | a marker only inside an identifier, inside a comment | green | **rc `0`** |
| D | a new PROSE site still reds | red | **rc `1`** |

⌗ *B's failure text carries the `where` tag, so the growth is attributable in the gate's own output and
not only in the baseline file.* ⌗ **And one defect of my own, caught before pushing: widening the row
moved the verdict to index `4` and three consumers still read index `3`, which wrote `mechanism`
values into the verdict column on the first regen. Found by checking the verdict distribution after
the regen rather than by trusting the row count; the baseline was restored from `HEAD` and rebuilt.**

## ⛔ `P7` IS STILL EXCLUDED

⓮ ④. `P7`'s own `42` comment matches are the larger half of the `97`, so this order deliberately buys
the smaller number, and the `P7` question is a separate registration whenever `66` wants it.
