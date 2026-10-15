# `r7395` ⑨ ⒞ — THE RATCHETING VOCABULARY, PRICED THEN BUILT

*⑨ ⒞ orders the vocabulary baseline seeded with the law's six **plus the `19` measured expressions**,
*"a new expression at a site being a new key"*, and ⛔ *"price it before wiring it --- the
adjudication backlog is the number that decides, not the runtime."* Bands in `REGISTRATION.md`,
pushed before `price.py` ran.*

## ⑨ ⒞ THE PRICE

| | |
|---|---:|
| **SITES** `(paper, normalised sentence)` | **`329`** |
| **KEYS** `(paper, sentence, expression)` | **`390`** |
| keys / sites | `1.185` |
| of those sites, reached by the law's six alone | `214` |
| ⇒ **added by the `19` harvested expressions** | **`115` sites, `150` keys** |
| all `25` seeded expressions fire in the corpus outside `P7` | `25` of `25` |

⌗ **Two independent implementations agree on both numbers** — `price.py` and the gate's own
`population()`, written separately, return `329`/`390`.

## THE BANDS, SCORED

- ⒜ **sites `380`–`900` → `329`. ⛔ REFUTED LOW.** *The band was deliberately wide because I could
  not predict it, and it was still wrong — in the direction that makes the arm cheaper.*
- ⒝ **keys/sites `1.05`–`1.35`× → `1.185`. HELD.**
- ⒞ **"the two largest among the `19` will be `what would` and `has not been`" → ⛔ REFUTED, and the
  refutation is the useful part.** The top two are **`\bowed\b` (`24`)** and **`conjectur` (`18`)`**;
  `what would` is joint third at `16` and `has not been` is `5`.
  ⇒ ⛭ ***The harvested expressions that fire most are the PROGRAMME's own vocabulary, not ordinary
  English.*** *My reason for the band was that ordinary constructions would flood the net. They do
  not. `owed` is this programme's own word for an outstanding obligation and `conjectur` marks a
  conjecture — both are about unfinishedness by construction. **So the widened net is less noisy than
  I predicted, which is the opposite of `.47`'s `70`-per-cent finding and had to be measured to be
  known.***
- ⒟ **a commitment rather than a prediction, and honoured:** the ratchet costs `0` human readings to
  install at any size, so the `390` is **the chat seat's reading queue and not a reason to refuse the
  arm** — and the gate is **not wired**, at this size or any other, on this seat's authority.

| n | expression | source | | n | expression | source |
|---:|---|---|---|---:|---|---|
| 127 | `open` | LAW-SIX | | 6 | `not built` | HARVEST-69 |
| 70 | `remains` | LAW-SIX | | 5 | `has not been` | HARVEST-69 |
| 27 | `frontier` | LAW-SIX | | 5 | `not fixed by` | HARVEST-69 |
| 24 | `\bowed\b` | HARVEST-69 | | 5 | `would settle` | HARVEST-69 |
| 18 | `conjectur` | HARVEST-69 | | 5 | `undetermined` | HARVEST-69 |
| 16 | `not settled` | HARVEST-69 | | 5 | `is not fixed` | HARVEST-69 |
| 16 | `what would` | HARVEST-69 | | 4 | `we do not claim` | HARVEST-69 |
| 14 | `not claimed` | HARVEST-69 | | 4 | `not computed` | HARVEST-69 |
| 12 | `not yet` | LAW-SIX | | 3 | `we have not` | HARVEST-69 |
| 12 | `is not settled` | HARVEST-69 | | 3 | `deferred` | LAW-SIX |
| | | | | 2 each | `is missing`, `have not been`, `unresolved`, `remain to be` | HARVEST-69 |
| | | | | 1 | `incomplete` | LAW-SIX |

## WHAT WAS BUILT

**`corpus/open_vocabulary.tsv` — the net as DATA, not code.** `25` rows: the law's six as `LAW`, the
`19` as `SEEDED`. `status` is a person's column; a reading turns a `SEEDED` expression into
`ADMITTED` or **`NOT-AN-OPEN`, and `NOT-AN-OPEN` leaves the net.** ⌗ *That is ⒞'s other direction —
"joins the vocabulary or is recorded as not-an-open" — and it is mechanical, not advisory.*

**`corpus/open_reference_baseline.tsv` — `390` rows, every one `UNREAD`,** keyed
`(paper, sentence, expression)` with `section`, `source` and `mechanism` beside it. `--regen` writes
`UNREAD` for a new key and never changes an existing verdict.

**`corpus/check_open_references.py`** reds on one thing: a key not in the baseline. ⛭ **And the
`\command{...}` guard is STATED on every run, as ⑨ asks** — *"the guard is a property your arm has and
`69`'s net lacks, and the gate should state that rather than inherit it silently"* — with
`r7391+cc66.50`'s `13` of `257` printed beside it, and the heading-fusion correction beside that.

## THE BINDING CHECKS — six, each in the direction that fails if the mechanism is absent

| | case | expected | got |
|---|---|---|---|
| A | unchanged tree | green | **rc `0`** |
| B | a new open-language sentence in its own paragraph | red | **rc `1`** |
| C | a new open claim FUSED to a `\paragraph{...}` heading | red | **rc `1`** |
| D | a marker present ONLY inside `\S\ref{sec:open-probe}` | green | **rc `0`** |
| E | ⛭ **a NEW EXPRESSION admitted to the vocabulary** — ⒞'s own case | red | **rc `1`**, `762` new keys |
| F | an expression read `NOT-AN-OPEN` (`conjectur`) | green, keys retired | **rc `0`**, `18` keys reported gone |

⌗ *E is the measurement that shows ⒞'s key is really the triple: admitting one expression created
`762` new keys at sentences that already had rows. **A sentence key alone would have stayed green
through it.*** ⌗ *Run end-to-end against a copied corpus tree, not by patching the module.*

## ⛔ STILL NOT WIRED, AND ⒟ SAID SO BEFORE THE NUMBER WAS KNOWN

Gate runtime is seconds. The number that decides is the `390`-key reading queue, and that decision is
the register-holder's. ⌗ *`r7271` ⒟: the human is the intended bottleneck. Wiring is one line in
`gates.yml`.*

## REPRODUCING

    python3 -I price.py <repo-root>                      # 329 sites / 390 keys
    python3 corpus/check_open_references.py              # the gate
    python3 corpus/check_open_references.py --regen      # rewrite the baseline

⌗ **Gate runtime `1.553` s**, measured — up from `0.417` s at `.51` because the net is `25`
patterns rather than one. ⌗ *`r7383` Ⓔ asked for three cheap arms rather than one complete one.*
