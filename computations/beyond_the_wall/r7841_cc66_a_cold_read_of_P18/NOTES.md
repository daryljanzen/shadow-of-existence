# NOTES — r7841+cc66.1

## Method, as registered before reading

Ten sections read **in order, end to end, before touching anything**, which the order
requires and which paid: §4.6's cluster only reads as *superseded* once §4.7's handover is
in view, and §10's count only reads as *sourced to a retired document* once §1's "nothing
here is new" has set up what the register is for.

Then three passes, each over the whole paper rather than section by section: every printed
figure against the companion that owns it; every companion's result as that companion **now**
states it; and the internal identities recomputed.

## ⛔ Guards this revision earned, in the order the instruments found them

### ⓵ A membership test is not a pin — and it failed three different ways in my own receipt

The perturbation sweep came back **15 of 19** on the first cut. Four silences, three of them
real, and all three were `in` tests:

1. **`'ten at the floor' in P18`** — the phrase occurs **twice in the flattened paper**, the
   second split across a line break. `grep`, `sed` and a line-wise count all see **one**.
   `in` is satisfied by either, so changing one site reddened nothing.
   *⇒ Pin the COUNT, require the sites to agree, and parse the word.*
2. **`fig in P18 and fig in P14`** for the lepton-number scale — P14 carries that figure
   **twice**, so moving one site reddened nothing.
   *⇒ Parse each figure out of its OWN sentence in each paper and compare as numbers.*
3. **⛔ The worst.** Four arms asserted the Virgo bound figures `1.70`, `2.35`, `1.85` and
   `6.4` were *"printed identically in P18 and in JanzenSlicing"* — and **P18 does not print
   that ratio at all.** Its `1.70` is the acoustic damping exponent on the power. The arms
   passed on unrelated digits that happen to appear in both files, and a reader would have
   taken them for a cross-check.
   *⇒ Deleted. What replaced them is a computation: P18's `24°–26°` IS the angular span of
   the `7` Mpc infall edge it prints in the same sentence, at the `15.8` Mpc the `r7831`
   computation projects from.*

**The general form:** `'phrase' in FLAT` is satisfied by *any* occurrence anywhere, so it
pins no site and cannot tell a figure in its role from the same digits elsewhere. It is the
same family as r7839's tautological arm (two sides sharing an input). **An assertion whose
truth does not depend on the site you mean is not a check of that site.**

### ⓶ A relational pin passes when both sides drift together

`check_figures_pinned` flagged **19** figures this revision prints beside its own citation.
It was right, and structurally so: every arm compared one *parsed* reading against another
— which is exactly what the order asks — so rewriting P15 **and** P18 to one wrong cluster
left `Ⓑ⑧` green. *⇒ Pin the figures against their own values **as well**, not instead.*

And a tolerance has to be inside half the last printed digit: `abs(d - 0.63) < 0.02` holds
`0.63` no tighter than `0.6`, so the gate counted it unpinned. Correctly.

### ⓷ A gate's own detector shapes how the check must be WRITTEN, not only what it must say

The first cut of those pins held the figures in tuples and compared `TUPLE[i]` in a loop.
All nineteen still read UNPINNED **while the receipt ran green** — the gate substitutes a
named *scalar* constant but not a tuple element. It was right to: a loop over a tuple is
harder for a **reader** to check too. *⇒ Written unrolled, every figure inline.*

### ⓸ The quote-pin operator is a reading instrument, and its report was ACTED ON

Fourteen spans changed before a single baseline row was written:

- **`([a-z]+) papers` matched the first of SEVENTEEN occurrences of `" papers"` in P18.** It
  happened to be the abstract's, by luck and not by pinning.
- **A substring ALT**: `'out\nto ...' in text or 'to ...' in text` — the second arm is a
  substring of the first, so the first could never decide. One arm now, on text flattened
  once.
- **Eleven dangling spans** — opening on a predicate, verb, preposition or relative pronoun
  with the subject outside — widened to the clause naming their subject.
- **One span longer than its claim**, shortened to its minimal carrier *after* checking the
  shorter form occurs exactly once, so shortening does not convert a pin on the claim into a
  pin on the file.
- **One pattern evaluated twice** in one condition, which the operator reads as a disjunction
  of two arms. Read once.

### ⓹ `check_paper_pins_present`: a bracket-class pattern with no backslash reads ABSENT

Its `hit` matches a literal as a regex **only if the literal contains a backslash**;
otherwise it does a plain `in` test, which no pattern satisfies. Two of my 35 PAPER pins
read absent from every paper for this reason alone. *⇒ `\s` instead of a literal space —
which a wrapped paper sentence needs anyway.*

### ⓺ P18 had no declared receipt home

`corpus/receipt_home.txt` declares P1–P17. **P18 is the one paper it never covered**, and
P18's two pre-existing receipts sit in thematic directories (`L550_third_mechanism`,
`L_probability`) rather than a paper one. So `receipts/P18_CR_synthesis` was a stray.
Declared as `P18  P18_CR_synthesis`, matching `P15_CR_cosmology` and its siblings, in the
same commit as the directory — the gate's own stated remedy. The two thematic homes are
untouched: the gate matches only paper-prefixed directory names. **Flagged to 69 as a
structural decision, reversible.**

## Repeated mistakes, logged because they are repeats

- **Backslash collapsing, for the third time.** `python3 -c "...\\times..."` inside double
  quotes collapses to `\times`, and in a non-raw string `\t` is a TAB — so the search found
  nothing. Fixed by writing the probe to a file with a **quoted** heredoc.
  *⇒ Any Python that handles LaTeX goes in a file via `<<'EOF'`, never `-c` in double quotes.*
- **An f-string expression cannot contain a backslash** (pre-3.12). Precompute the value.
- **A patch anchor spanning lines needs real newlines**, not `\n` inside a raw string. Three
  failed patches before I indexed by content rather than by offset.

## The sweep, as run

Control green from the receipt's own directory, then each source figure moved by one digit
and restored via `git checkout`. **32 of 33 bite.** The one silence is a probe of mine aimed
at P14's discriminant, where the arm asserts about P18 and does not claim to pin P14 — so
passing was correct. Three cases first returned SKIP because the literal straddles a line
break in the raw file; each bites under a whitespace-tolerant match.

## What this revision does NOT settle

- The §10 count cluster beyond the receipts figure. **No live source, no stated counting
  convention** — the live tree has `263` spine environments against the retired document's
  `196`, and without knowing which the sentence counts, "some two hundred" is neither
  confirmed nor refuted. Reported, not fixed, per the order's own test.
- Whether the rewritten sentences are the **right** sentences. No gate checks a reading.
  Both are quoted whole in the channel for reversal.
- P18's Virgo profile figures (`1.9`, `7`, `1.2` Mpc, "under a fifth") rest on their external
  citations. P18 is their **sole corpus carrier**, so no companion can be compared against —
  stated rather than papered over with an `in` test that would pass on any digits.
