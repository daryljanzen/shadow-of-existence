# `r7345+cc66.4` — THE DECLARATION, frozen before scoring: one container rule, three stated exclusions, written from half `A` only, to be scored ONCE on held-out half `B`

*`r7345` ⒞: **"Hold out a population and test the container rule ONCE: declare it on one half, score it
once on the other. That converts four fits into one test and it is the single thing not yet done."** This
file is the declaration. **It is committed before the score is computed, and the score goes in a separate
file.** If the rule fails on `B`, the hop is abandoned with its measurement, per ⒞.*

## ① THE POPULATION, THE SPLIT, AND WHY THIS SPLIT AND NOT THE OBVIOUS ONE

**Population: the `117` hop-minted keys whose HAND LABELS are frozen in commit `7db5db61c`** —
`READING.md`'s three class lists, `keep82.tsv` and `want14.txt`, all pushed **before `r7345` was written**.
*The labels therefore cannot be revised to fit a rule declared after them; git history is the
pre-registration.*

**Split: `int(sha256(receipt + '\t' + literal).hexdigest()[0], 16) % 2`** — `0` → declaration half `A`
(`58`), `1` → held-out half `B` (`59`). *Deterministic, computable by anyone, and chosen before either half
was tabulated.*

⛔ **THE WEAKNESS, STATED FIRST RATHER THAN DISCOVERED LATER.** *I have read all `117` by hand, so this is
**not** a hold-out of my knowledge — it is a hold-out of the RULE's specification against labels that were
frozen earlier. The stronger test does not exist: the hop's population is corpus-wide and I have read it
whole, so there is no unread population of hop keys to score on.* ⇒ **What this test can refute is a rule
fitted to `A`'s residue; what it cannot refute is my hand labelling. I am not claiming the stronger thing.**

⌗ *The merged tree now mints `121`, and the `4` keys beyond the `117` — three in `60`'s new `S48` — are
**excluded from the test** because their labels would be written after seeing the rule. They are reported
as an unlabelled addendum instead.*

## ② THE RULE, DECLARED FROM HALF `A` ONLY

**A hop-minted key is KEPT unless exactly one of three stated exclusions fires.** Each is a conjunction of
container and form, as `r7345` ⒜ requires, and each is computed from the **narrow** trace — the object that
decides key-hood, available per this phase's `CORRECTION.md`.

**`E1` SOURCE-READ** — *the container reads another receipt's source as text.* All four must hold:
- the narrow trace's file kinds are **exactly** `{py}`;
- the trace shows a text read: `splitlines(`, `split('\n')`, `readlines(`, `open(`, `cat-file`,
  `git('show'`, `git('grep'`;
- the trace shows **no** import mechanism: not `ModuleType`, `exec_module`, `spec_from_file_location`,
  `importlib`;
- the container's own first trace segment does **not** use a `.py` path only as a dict **key**
  (`[... '.py']`).

**`E2` OWN STAMP** — *the literal is an authorship marker in a ledger or register.* Both must hold:
- the narrow trace's kinds include `tsv` or `md`;
- the literal **contains** `r\d{4,5}\+(\d{2}|cc\d{2})(\.\d+)?`, **or** is exactly `+\d+`, **or** is exactly
  `cc\d+`.

*A bare revision id with no seat suffix — `r7329`, `r7150`, `L-552` — is a cross-reference and is KEPT.
That line is `66`'s ⒜ ruling and it is why the seat suffix is required.*

**`E3` DELIMITER** — *the literal is table formatting.* The literal, stripped, consists only of characters
drawn from `-`, `|`, `=`, `_` and whitespace.

**Everything else is KEPT.** *There is no fourth class and no residual catch-all: that is what makes this a
test rather than a fifth narrowing.*

## ③ THE BAR, WHICH IS `66`'s ⒟ AND NOT A PERCENTAGE

Scored on held-out `B`, the rule **passes** only if both hold:

1. **ZERO genuine keys forgone** — no key the frozen labels call a pin is excluded by `E1`–`E3`;
2. **every imprecise key in `B` individually NAMED and excluded** by one of `E1`–`E3` — a key the frozen
   labels call a non-pin that the rule keeps is a named miss, and the rule fails if any exists.

⇒ ⛔ ***Both halves of the bar, or the hop is abandoned with its measurement and the invisible pins become a
stated limit.*** *`r7345` ⒞ says that outcome is acceptable, and I am not going to argue with it after the
fact if it is the one that comes up.*
