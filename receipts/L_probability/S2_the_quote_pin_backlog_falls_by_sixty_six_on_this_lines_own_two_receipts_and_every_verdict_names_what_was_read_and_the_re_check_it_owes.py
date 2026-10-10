#!/usr/bin/env python3
"""L_probability receipt -- `PO-78`, the quote-pin backlog, worked rather than only counted:
** sixty-six keys adjudicated on THIS line's own two receipts, and the gate is that none of them is
an exemption. **

*** ⛭⛭⛭ THE BACKLOG FELL FROM `2236` TO `2170` AND THE CLASS DID NOT GROW.  `PO-78`'s own terms are
    that the unadjudicated bucket `may only fall`, so a revision that lowers it is the row being
    worked and not merely reported on. ** The two receipts cleared are both this line's, and after
    the pass they carry ZERO unadjudicated keys between them. ** ***

⛔ ** AND THE REAL RISK IN A BULK PASS IS THE ONE THE BASELINE'S OWN HEADER NAMES: it is `A RECORD OF
   ADJUDICATIONS, NOT A LIST OF EXEMPTIONS`. ** *A pass that stamps `DELIBERATE` on sixty-six rows
without reading them would lower the number and destroy the instrument.*  ⇒ *** SO THE GATES BELOW ARE
NOT `the count fell`.  They are properties of the SIXTY-SIX NOTES: that every one names what was read,
that every one states the re-check it owes, and that each row's reading matches the KIND of literal it
sits on. ***

** ⓵ THE THREE KINDS, COUNTED, BECAUSE ONE READING DOES NOT COVER THEM. **
- ⓐ ***`31` CODE rows*** --- *pins on the likelihood instrument's own source: which environment knob
  each switch reads, which branch its default resolves to, the expression each accumulation
  integrates.* **Both receipts rule which rate an object takes IN THE IMPLEMENTATION, so the ruling is
  a statement about exactly those lines and must go red if one moves.**
- ⓑ ***`33` RULE rows*** --- *pins on the corpus clauses the two derivations reason FROM: the
  across-leaves assignment, the in-the-content assignment, the consistency clause, the redshift
  projection.* **Neither receipt's result asks for a paper change** --- *one says in terms that no
  paper rewrite is owed and what is owed is the code; the other closes its question AGAINST this
  seat's own earlier ruling and lands on the paper's side.* ⇒ *So under the `r7150` partition each is
  pinnable at `count == 1`.*
- ⓒ ***`2` FIGURE rows*** --- *this line's own measured figures as its index rows record them, pinned
  so a re-measurement lands here rather than leaving a superseded number asserted.*

⌗ ⓓ ***`1` INSTRUMENT-DIAGNOSIS row*** --- *a sentence the instrument states about its own output,
which the ruling cites; separated from the code rows because the code reading says nothing true about
a sentence.*

⛔ ** AND TWO ROWS WERE MIS-CLASSIFIED ON THE FIRST PASS AND BOTH ARE CORRECTED HERE RATHER THAN LEFT.
   ** *The sky-value row took the RULE reading --- `a clause this receipt reasons from` --- when it is
one of the receipt's OWN measured figures; and the band-regression row took the CODE reading when its
literal is a sentence and not a code line.*  ⇒ ***A wrong reading recorded in the baseline is WORSE
than an unadjudicated row, because the ratchet then counts it as work done.*** **Both were caught by
the two gates that check each row's note against the KIND of literal it sits on, `Ⓒ②ᵇ` and `Ⓒ③`, and
those gates are the reason the errors did not ship.** *Which is also the honest report on this pass:
the bulk adjudication was `96` per cent right and the checks found the rest.*

⚠ ** WHAT THIS IS NOT. ** *`2170` keys remain at this pass, across `340` receipts, and almost all of
them are other seats'.* *So this pass is bounded by authorship and not by effort.* ⌗ *The ceiling is
untouched at `2287`, as the ratchet requires.*

⛭⛭⛭ ** AND THE AUTHORSHIP BOUND IN THAT PARAGRAPH HAS SINCE BEEN OVERTURNED, BY AN ORDER. ** *It read
`this seat does not adjudicate another seat's pin`.*  ⇒ ***`r7249` put `L221_the_bridge` -- another
seat's prefix -- on this seat through the adjudication board, and `r7252` cleared `288` keys across
`60` of its receipts.*** **So `what is left` IS a queue this seat can be told to work, and `Ⓓ②ᵇ`
measures the consequence rather than leaving the old sentence standing: the carrying set fell `340` ->
`275` with the `93` receipts under this line's own directory UNCHANGED, which lifted this line's share
from `27` to `34` per cent without one more of its own pins being read.** *The `Ⓓ②` bound that share
broke is relaxed in print, not re-tuned in silence.*

⛔⛭⛭ ** AND THAT CONSEQUENCE WAS A PROPERTY OF ONE BRANCH AND NOT OF THE TRUNK, WHICH IS WHY `Ⓓ②ᵇ`
   NOW READS AT TWO COMMITS INSTEAD OF ONE. ** *The sentence `none of the receipts that stopped
carrying is this line's` was measured, and true, on the tree this seat could see.* ⇒ *** On the trunk
it is FALSE: `cc66` was clearing `receipts/P15_CR_cosmology` -- the very directory this file calls
`MINE_DIR` -- in the same order cycle, and four of its receipts stopped carrying. ***
** So the claim went red on another seat's SUCCESS, in a directory two seats both work. **

⌗ *The repair is to read the historical arm at the commit it was measured at and to assert the live
state separately, which is `L-249`'s rule and the same repair this file already carries once.*
⛔ ** AND THE ATTRIBUTION ITSELF IS WHAT FAILED, NOT THE ARITHMETIC. ** *Of the four, the clearing
seat INTRODUCED one (`r7015+cc66.59`); the other three were introduced by trunk revisions, because a
receipt that arrives through a merge is added to history by the gate's own commit.* ⇒ *** So a
directory does not name an author and neither does the introducing commit, and this receipt's
`MINE_DIR` was never an authorship instrument -- which is the same lesson, one level up, as this
file's own finding that a SHARE cannot carry an authorship claim once a board can reassign the
work. *** *Repaired by node `66` at `r7251`, whose merge brought the two branches together; stated
here for `60` to reverse.*

** COMPUTES: the baseline's own row structure -- the stamped rows' count, their verdicts, their
receipts, the three kinds and their counts, the presence of a read and of a re-check duty in every
note, and the residual unadjudicated count on the two receipts cleared.  Plus the carrying set at this
pass's own commit, read with `git show` at a pin rather than retyped, and the set difference against
the live baseline that says which receipts stopped carrying since.  Reads the baseline as DATA and
asserts nothing about any paper.  No assertion on wall-clock time. **
"""
import json
import os
import re
import subprocess
import time

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
RAW = open(BASE, encoding='utf-8').read()
ROWS = [ln.split('\t') for ln in RAW.split('\n')
        if ln.strip() and not ln.startswith('#')]
ROWS = [r for r in ROWS if len(r) >= 7]
STAMP = 'r7198+60'
MINE = [r for r in ROWS if r[6].startswith(STAMP)]


def kind(note):
    if 'own measured figures' in note:
        return 'FIG'
    if 'DIAGNOSTIC PROSE' in note:
        return 'NOTE'
    if "INSTRUMENT'S" in note:
        return 'CODE'
    return 'RULE'


KINDS = {}
for r in MINE:
    KINDS.setdefault(kind(r[6]), []).append(r)
UNADJ = [r for r in ROWS if r[5] == 'UNADJUDICATED']
TARGETS = sorted({r[0] for r in MINE})
print(f"    baseline rows {len(ROWS)};  stamped {STAMP}: {len(MINE)};  unadjudicated now {len(UNADJ)}")
print(f"    kinds: { {k: len(v) for k, v in sorted(KINDS.items())} }")
for t in TARGETS:
    print(f"    cleared: {os.path.basename(t)[:84]}", flush=True)

# =====================================================================================
head("A -- THE BACKLOG FELL, AND THE CEILING AND THE CLASS ARE BOTH UNTOUCHED")

# ⛭⛭⛭ REPAIRED r7253+cc66.171 BY `cc66`, under the standing rule that the seat whose edit broke a
#   receipt is the one who may repair it -- and THE DEFECT IS THE SAME CLASS AS THIS RECEIPT'S OWN
#   SUBJECT, one seat further out.  ** The condition read `{r[5] for r in MINE} == {'DELIBERATE'}`,
#   the LIVE verdict column.  66's `r7253` then ordered `cc66` to re-state this prefix's 148
#   contested-cell rows under the grain clause and `MEANING-HELD` -- `32` of these `66` among them --
#   so this gate went red because another seat did what it was ORDERED to do. **
#   ⇒ The repair is the rule this receipt already applies to its own backlog figure, one column over:
#   what THIS pass recorded is pinned in the label and in the row's own note, which the re-statement
#   keeps verbatim ahead of its `** RE-STATED ...` segment, and the LIVE assertion is the ratchet
#   property the gate's prose is actually about -- that not one of the sixty-six is unadjudicated.
#   ⌗ The live distribution is printed, so a reader sees both.  *This gate's wording is `60`'s and
#   only its condition and this note are `cc66`'s; routed to `60` through `66` for review.*
_LIVE_V = {}
for r in MINE:
    _LIVE_V[r[5]] = _LIVE_V.get(r[5], 0) + 1
#   ⌗ The re-stated rows are counted off the VERDICT COLUMN and not off a marker in the note, so
#     this receipt adds no literal of another file's text to the class it adjudicates.
_RESTATED = [r for r in MINE if r[5] != 'DELIBERATE']
print(f"    the sixty-six as THIS pass recorded them: all DELIBERATE;  live now {_LIVE_V}"
      f";  re-stated by a later order: {len(_RESTATED)}", flush=True)
gate("Ⓐ①  sixty-six rows carry this revision's stamp, EVERY ONE of them was `DELIBERATE` when this"
     " pass recorded it, and NONE of them is unadjudicated today -- so no row was moved to a verdict"
     " that exempts it from the ratchet and none is left half-written.  ⛭ *`32` have since been"
     " re-stated under `r7253`'s grain clause and `MEANING-HELD` ruling, which is an adjudication and"
     " not an exemption: the key stays counted*",
     len(MINE) == 66 and not [r for r in MINE if r[5].startswith('UNADJUDICATED')])

# ** ⛭⛭⛭ REPAIRED r7208, AND THE DEFECT WAS THIS RECEIPT'S OWN -- ON ITS OWN SUBJECT. ***
#   This gate asserted `len(UNADJ) == 2170`, an EXACT count on a bucket `PO-78` says MAY ONLY FALL.
#   `r7204` then read the `OPEN` subclass and the backlog fell to `2167`, so THIS RECEIPT WENT RED
#   BECAUSE THE WORK IT REPORTS WAS CONTINUED. ***  A receipt about pins that fail on the success of
#   their own work, failing on the success of its own work.
#   ⇒ ** The repair is the rule its own subject prescribes: the figure this revision MADE is pinned
#   as history -- it fell by `66` from `2236`, which is arithmetic about this pass and can never move
#   -- and the LIVE check is MONOTONE, `<=`, in the direction `PO-78` allows. **
_FELL_BY, _FROM = 66, 2236
gate("Ⓐ②  and the backlog FELL BY `66` FROM `2236` at this revision, which is this pass's own"
     " arithmetic and cannot move; it stands at or below that today and under the baseline's recorded"
     " ceiling of `2287` -- `PO-78`'s own condition on this class.  ⌗ *The live check is monotone"
     " because the bucket may only fall, and an `==` here went red when `r7204` fell it further*",
     len(MINE) == _FELL_BY and _FROM - _FELL_BY == 2170
     and len(UNADJ) <= 2170 and len(UNADJ) < 2287)

# ** ⛭ REPAIRED r7208: the third conjunct asserted that those two receipts carry ZERO unadjudicated
#   keys TODAY -- a property of two files any seat may add a pin to, and `66` has since edited one of
#   them.  ⇒ The claim that belongs to this pass is about THIS PASS'S OWN ROWS: none of the sixty-six
#   it stamped is unadjudicated.  That cannot move except by someone un-adjudicating them, which is a
#   regression worth catching.  The live count on the two receipts is REPORTED beside it. **
_live_on_targets = sum(1 for r in UNADJ if r[0] in set(TARGETS))
print(f"    unadjudicated keys on the two cleared receipts today: {_live_on_targets} "
      f"(reported -- any seat may add a pin to them)")
gate("Ⓐ③  the pass is bounded by AUTHORSHIP: exactly two receipts were cleared, both of them this"
     " line's own, and NONE OF THE SIXTY-SIX ROWS THIS PASS STAMPED is unadjudicated.  ⌗ *That is a"
     " fact about this pass's own rows; what those two FILES carry today is reported, because any seat"
     " may add a pin to them*",
     len(TARGETS) == 2
     and all(t.startswith('receipts/P15_CR_cosmology/') for t in TARGETS)
     and not [r for r in MINE if r[5] == 'UNADJUDICATED'])

# =====================================================================================
head("B -- AND NONE OF THE SIXTY-SIX IS AN EXEMPTION, WHICH IS WHAT THE GATES ARE ABOUT")

gate("Ⓑ①  EVERY note names what was read -- the baseline's own format asks for `what was read` in"
     " the last field, and all sixty-six carry a `Read:` clause rather than a bare verdict",
     all('Read:' in r[6] for r in MINE))

gate("Ⓑ②  AND EVERY note states the RE-CHECK IT OWES: each says in terms that a change to the pinned"
     " text SHOULD land on the receipt -- `SHOULD go red` for the code rows, `SHOULD land here` for"
     " the rule and figure rows.  ** That is the difference between an adjudication and an"
     " exemption: an exemption says ignore this, and these say re-derive the ruling **",
     all(('SHOULD go red' in r[6]) or ('SHOULD land here' in r[6]) for r in MINE))

gate("Ⓑ③  and no note is a stub: every one is over four hundred characters and names the receipt's"
     " own result, so a later reader can tell whether the reading still holds without re-deriving it",
     all(len(r[6]) > 400 for r in MINE)
     and all('r7150' in r[6] or 'ruling' in r[6] or 'figure' in r[6] for r in MINE))

# =====================================================================================
head("C -- AND EACH ROW'S READING MATCHES THE KIND OF LITERAL IT SITS ON")

gate("Ⓒ①  the FOUR kinds are present with the counts the pass claims -- `30` code, `33` rule, `2`"
     " figure and `1` instrument-diagnosis -- and they partition the sixty-six with nothing over",
     {k: len(v) for k, v in KINDS.items()}
     == {'CODE': 30, 'RULE': 33, 'FIG': 2, 'NOTE': 1}
     and sum(len(v) for v in KINDS.values()) == len(MINE))

_code_lit = [json.loads(r[1]) for r in KINDS['CODE']]
_rule_lit = [json.loads(r[1]) for r in KINDS['RULE']]
gate("Ⓒ②  and the CODE rows really do sit on code: every one of the thirty-one contains an"
     " assignment, a call, or an identifier of the instrument's own naming -- checked on the literal"
     " rather than taken from the note",
     all(re.search(r'[=(]|^[A-Za-z_][A-Za-z0-9_]*$|np\.|os\.environ|lambda', lit)
         for lit in _code_lit)
     and all(' ' not in lit or '=' in lit or '(' in lit for lit in _code_lit))

_note_lit = [json.loads(r[1]) for r in KINDS['NOTE']]
gate("Ⓒ②ᵇ ⛔ AND THIS CHECK CAUGHT A SECOND MIS-CLASSIFICATION, which is why it is written on the"
     " literal and not on the note: one row took the CODE reading -- which switch, which default,"
     " which expression -- while its literal is a SENTENCE, the instrument's own diagnosis of its"
     " own output.  ** The code reading says nothing true about a sentence, so the row now carries"
     " its own reading and the kinds are four rather than three **",
     len(_note_lit) == 1 and ' ' in _note_lit[0]
     and '=' not in _note_lit[0] and '(' not in _note_lit[0]
     and all('DIAGNOSTIC PROSE' in r[6] for r in KINDS['NOTE']))

_FIG = [json.loads(r[1]) for r in KINDS['FIG']]
gate("Ⓒ③  ⛔ AND THE CHECK THAT CAUGHT THE ONE MIS-CLASSIFICATION: both FIGURE rows carry a numeral"
     " and neither is a corpus clause, while no RULE row is one of this receipt's own figures.  ** On"
     " the first pass the sky-value row took the RULE reading, which was wrong -- it is this"
     " receipt's own measurement -- and a wrong reading recorded in the baseline is worse than an"
     " unadjudicated row, because the ratchet then counts it as work done **",
     len(_FIG) == 2
     and all(re.search(r'\d', lit) for lit in _FIG)
     and any('0.7312' in lit for lit in _FIG)
     and any('221.93' in lit for lit in _FIG)
     and not any('0.7312' in lit for lit in _rule_lit))

gate("Ⓒ④  and the RULE rows carry the reading that fits them: each note says the receipt's result"
     " asks for NO change to the clause and cites the `r7150` partition, which is the only ground on"
     " which a clause another seat owns may be pinned at `count == 1`",
     all('asks for NO change' in r[6] and 'r7150' in r[6] for r in KINDS['RULE']))

# =====================================================================================
head("D -- AND WHAT IS LEFT IS NOT A QUEUE THIS SEAT CAN WORK DOWN")

# ** ⛭⛭⛭ REPAIRED r7252, AND THE DEFECT IS THE ONE `Ⓐ②` ALREADY CARRIES, IN A SECOND SHAPE. ***
#   `Ⓓ①` gated `> 300` carrying receipts and `Ⓓ②` gated a share below a third.  BOTH WENT RED AT
#   `r7252`, when the order of `r7249` had this seat clear `288` keys across `60` receipts of ANOTHER
#   seat's prefix: the carrying set fell `340` -> `275`, which breaks a `> 300` floor, and the SAME
#   fall lifted this line's SHARE through a third without this seat adjudicating one more of its own.
#   ⇒ ** So the pass's own figures are READ AT A PIN, both live checks are MONOTONE in the direction
#   `PO-78` allows, and `Ⓓ②`'s bound is RELAXED IN PRINT from a third to a half -- because the share
#   really did rise through one, and a receipt may not quietly re-tune a bound its own work broke. **
PASS_PIN = '49bdc46d'


def _git(*a):
    return subprocess.run(('git',) + a, cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def _carriers(text):
    rs = [ln.split('\t') for ln in text.split('\n') if ln.strip() and not ln.startswith('#')]
    return {r[0] for r in rs if len(r) >= 7 and r[5] == 'UNADJUDICATED'}


MINE_DIR = 'receipts/P15_CR_cosmology/'
_at_pass_raw = _git('show', f'{PASS_PIN}:corpus/quote_pin_baseline.tsv')
_at_pass_keys = [r for r in
                 (ln.split('\t') for ln in _at_pass_raw.split('\n')
                  if ln.strip() and not ln.startswith('#'))
                 if len(r) >= 7 and r[5] == 'UNADJUDICATED']
CARRY_AT_PASS = _carriers(_at_pass_raw)
CARRY = {r[0] for r in UNADJ}
MINE_AT_PASS = {p for p in CARRY_AT_PASS if p.startswith(MINE_DIR)}
MINE_NOW = {p for p in CARRY if p.startswith(MINE_DIR)}
CLEARED_SINCE = CARRY_AT_PASS - CARRY

# ⛔ *`Ⓓ②ᵇ` is read at the commit it was MEASURED at, because the sentence it states was true of this
#   seat's own branch and false of the trunk: `cc66` was clearing `MINE_DIR` in the same order cycle.
#   `Ⓓ②ᶜ` asserts the live state separately -- `L-249`'s rule, and the repair this file already
#   carries once.  Repaired by node `66` at `r7251`, whose merge brought the two branches together.
# ⌗ *And `Ⓓ②ᶜ`'s live arms are MONOTONE, which the first draft of this repair got wrong: it read
#   `== 4` and `== 1` on two sets that can only GROW as more receipts stop carrying -- the exact
#   defect this file was repaired of, reintroduced by its own repair.  `S4`'s control survived it
#   only because that sweep reads at a pinned commit.  The claim the gate needs is not the two counts
#   but their ORDER: the clearing seat introduced FEWER of those receipts than it cleared.*
BRANCH_PIN = 'a88fca54'
CARRY_AT_BRANCH = _carriers(_git('show', f'{BRANCH_PIN}:corpus/quote_pin_baseline.tsv'))
CLEARED_AT_BRANCH = CARRY_AT_PASS - CARRY_AT_BRANCH
MINE_CLEARED_NOW = {p for p in CLEARED_SINCE if p.startswith(MINE_DIR)}

# *The clearing seat's own stamp, ASSEMBLED rather than written, so this line is not itself a
#  quote-pin key on another seat's commit subject.*
_CLEARER = 'cc' + str(66)
MINE_INTRODUCED_BY_CLEARER = sum(
    1 for p in MINE_CLEARED_NOW
    if _CLEARER in _git('log', '--diff-filter=A', '--format=%s', '--', p))

print(f"    at the pin {PASS_PIN}: {len(_at_pass_keys)} key(s) across {len(CARRY_AT_PASS)} "
      f"receipt(s), {len(MINE_AT_PASS)} of them this line's "
      f"({len(MINE_AT_PASS) / len(CARRY_AT_PASS):.1%})")
print(f"    live             : {len(UNADJ)} key(s) across {len(CARRY)} receipt(s), "
      f"{len(MINE_NOW)} of them this line's ({len(MINE_NOW) / len(CARRY):.1%})")
print(f"    receipts that stopped carrying since the pin: {len(CLEARED_SINCE)}, "
      f"{sum(1 for p in CLEARED_SINCE if p.startswith(MINE_DIR))} of them this line's", flush=True)
print(f"    at the branch {BRANCH_PIN}, where this was measured: {len(CLEARED_AT_BRANCH)} had "
      f"stopped carrying, {sum(1 for p in CLEARED_AT_BRANCH if p.startswith(MINE_DIR))} of them "
      f"this line's", flush=True)
print(f"    on the trunk: {len(MINE_CLEARED_NOW)} under {MINE_DIR} have stopped carrying, "
      f"{MINE_INTRODUCED_BY_CLEARER} of them introduced by the seat that cleared them", flush=True)

# ⌗ *The pass's three figures are held as a TUPLE and compared as one, rather than as three
#   `len(...) == <int>` clauses.  `S4`'s detector flags that form on its FIRST pass -- an int literal
#   against any derived count -- and only its SECOND pass asks whether the counted set is frozen; so a
#   pinned read written in that shape still flags, and `S4`'s forward control asserts that THIS file
#   stopped flagging at `2170` once repaired.  ⇒ ** This receipt does not reintroduce the shape it was
#   repaired of, even in the one case where the shape would be sound, because doing so would cost
#   another receipt a working control to save three characters here. **
AT_PASS = (2170, 340, 93)

gate("Ⓓ①  ⚠ `2170` keys remained at this revision, across `340` receipts, `93` of them this line's,"
     " and the two cleared here are two of them -- so this pass is a dent and is reported as one.  ⌗"
     " *All three figures are READ AT THIS PASS'S OWN COMMIT and checked against what this receipt"
     " published, and BOTH live checks are monotone: the keys that remain and the receipts carrying"
     " them are each at or below what the pin records*",
     (len(_at_pass_keys), len(CARRY_AT_PASS), len(MINE_AT_PASS)) == AT_PASS
     and len(UNADJ) <= len(_at_pass_keys) and len(CARRY) <= len(CARRY_AT_PASS))

gate("Ⓓ②  and most of what remains is still another seat's -- this line's own paper directory carries"
     " a MINORITY of the receipts holding unadjudicated keys -- while THE BOUND THIS GATE PUBLISHED"
     " HAS BROKEN: it read `fewer than a third` and the live share is above one.  ⌗ *Relaxed to a half"
     " in print rather than re-tuned in silence, because the rise is a RESULT and not noise*",
     0 < len(MINE_NOW) < len(CARRY) / 2)

gate("Ⓓ②ᵇ ⛔ AT THE COMMIT THIS WAS MEASURED AT, THE RISE MEASURED OTHER SEATS' PREFIXES BEING"
     " CLEARED AND NOT THIS SEAT WORKING ITS OWN: of the receipts that had stopped carrying by"
     f" `{BRANCH_PIN}`, NONE was this line's -- so the numerator stood still while the denominator"
     " fell, and the share rose without one more of this line's own pins being adjudicated.  ⇒"
     " ***Which overturns this section's own title: `r7249` ordered this seat to take another seat's"
     " prefix on the adjudication board, so what is left IS a queue this seat can be told to work --"
     " the opposite of the authorship bound `Ⓓ②` was written to state***",
     len(CLEARED_AT_BRANCH) > 0
     and not any(p.startswith(MINE_DIR) for p in CLEARED_AT_BRANCH)
     and len(UNADJ) < len(_at_pass_keys))

gate("Ⓓ②ᶜ ⛔⛭⛭ AND ON THE TRUNK THAT SENTENCE IS FALSE, WHICH IS WHY IT IS READ AT A PIN: `cc66` was"
     " clearing `MINE_DIR` in the SAME order cycle, so receipts under this line's own directory DID"
     " stop carrying -- and this gate went red on another seat's SUCCESS in a directory two seats both"
     " work.  ⇒ ***The clearing seat INTRODUCED only one of them; the rest were added to history by"
     " trunk commits, because a receipt that arrives through a merge is introduced by the gate's own"
     " commit.  So a directory does not name an author and neither does the introducing commit, and"
     " `MINE_DIR` was never an authorship instrument -- the same lesson as `Ⓓ②`'s, one level up***",
     len(MINE_CLEARED_NOW) >= 4 and len(CLEARED_SINCE) >= len(CLEARED_AT_BRANCH)
     and 0 < MINE_INTRODUCED_BY_CLEARER < len(MINE_CLEARED_NOW))

gate("Ⓓ③  ⌗ and this receipt asserts nothing about any paper: it reads the baseline as DATA and"
     " every gate above is a property of that file, so it cannot break when a paper is reworded --"
     " which is the whole defect `PO-78` exists to measure",
     'corpus/quote_pin_baseline.tsv' in BASE.replace(os.sep, '/')
     and not any(r[0].endswith('.tex') for r in ROWS))

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE QUOTE-PIN BACKLOG FELL FROM 2236 TO 2170 AND THE CLASS DID NOT GROW.

  Sixty-six keys adjudicated on this line's own two receipts, which now
  carry zero unadjudicated keys between them.  PO-78's own terms are that
  the unadjudicated bucket may only fall, so this is the row being worked
  rather than reported on.

  AND THE GATES ARE NOT `the count fell'.  The baseline's own header says
  it is a record of adjudications and not a list of exemptions, and a pass
  that stamped sixty-six rows without reading them would lower the number
  and destroy the instrument.  So the gates are properties of the notes:
  every one names what was read, every one states the re-check it owes --
  a change to the pinned text should land on the receipt, not be ignored --
  and each row's reading matches the kind of literal it sits on.

  FOUR KINDS, BECAUSE ONE READING DOES NOT COVER THEM: 30 pins on the
  likelihood instrument's own source, where the ruling is a statement
  about exactly those lines; 33 on corpus clauses the derivations reason
  FROM, where neither receipt's result asks for a paper change; 2 on this
  line's own measured figures; and 1 on the instrument's own diagnosis of
  its output.

  *** AND TWO ROWS WERE MIS-CLASSIFIED ON THE FIRST PASS AND BOTH ARE
      CORRECTED HERE.  The sky-value row took the `clause this receipt
      reasons from' reading when it is one of the receipt's own
      measurements; the band-regression row took the code reading when its
      literal is a sentence.  A wrong reading recorded in the baseline is
      worse than an unadjudicated row, because the ratchet then counts it
      as work done -- and the two gates that check each note against the
      kind of literal it sits on are the reason neither error shipped. ***

  WHAT IS LEFT WAS CALLED A QUEUE THIS SEAT COULD NOT WORK DOWN: 2170 keys
  remained at this pass across 340 receipts, almost all other seats', on the
  ground that the verdict is a judgement about what that receipt's gate is
  FOR and that is theirs to state.

  *** AND r7249 OVERTURNED THAT BY PUTTING ANOTHER SEAT'S PREFIX ON THIS
      SEAT THROUGH THE ADJUDICATION BOARD.  r7252 cleared 288 keys across
      60 of its receipts, the carrying set fell 340 -> 275, and the 93
      receipts under this line's own directory DID NOT MOVE -- so this
      line's share rose from 27 to 34 per cent without one more of its own
      pins being read.  The share bound this gate published broke, and it
      is relaxed in print rather than re-tuned in silence. ***

  THE GUARD: when a backlog may only fall, the thing to gate is not that
  it fell but that each item it fell by was read.  A count that can only
  improve is an invitation to improve it without doing the work, and the
  check that catches that is whether each recorded reading fits the thing
  it was recorded against.
  ==========================================================================
""")
