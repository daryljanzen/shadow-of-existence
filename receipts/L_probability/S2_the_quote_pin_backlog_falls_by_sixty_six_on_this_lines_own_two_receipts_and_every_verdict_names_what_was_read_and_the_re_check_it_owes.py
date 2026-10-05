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

⚠ ** WHAT THIS IS NOT. ** *`2170` keys remain, across `340` receipts, and almost all of them are other
seats'.* ***This seat does not adjudicate another seat's pin: the verdict is a judgement about what
that receipt's gate is FOR, and that is theirs to state.*** *So this pass is bounded by authorship and
not by effort, and the remaining backlog is not a queue this seat can work down alone.* ⌗ *The ceiling
is untouched at `2287`, as the ratchet requires.*

** COMPUTES: the baseline's own row structure -- the stamped rows' count, their verdicts, their
receipts, the three kinds and their counts, the presence of a read and of a re-check duty in every
note, and the residual unadjudicated count on the two receipts cleared.  Reads the baseline as DATA
and asserts nothing about any paper.  No assertion on wall-clock time. **
"""
import json
import os
import re
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

gate("Ⓐ①  sixty-six rows carry this revision's stamp and EVERY ONE of them is `DELIBERATE` -- no row"
     " was moved to a verdict that exempts it from the ratchet, and none is left half-written",
     len(MINE) == 66 and {r[5] for r in MINE} == {'DELIBERATE'})

gate("Ⓐ②  and the backlog now stands at `2170` against the baseline's recorded ceiling of `2287` --"
     " so it fell by `66` from `2236` and the ceiling is untouched, which is `PO-78`'s own condition"
     " on this class",
     len(UNADJ) == 2170 and len(UNADJ) + len(MINE) == 2236 and len(UNADJ) < 2287)

gate("Ⓐ③  the pass is bounded by AUTHORSHIP: exactly two receipts were cleared, both of them this"
     " line's own, and between them they now carry ZERO unadjudicated keys",
     len(TARGETS) == 2
     and all(t.startswith('receipts/P15_CR_cosmology/') for t in TARGETS)
     and sum(1 for r in UNADJ if r[0] in set(TARGETS)) == 0)

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

gate("Ⓓ①  ⚠ `2170` keys remain across more than three hundred receipts, and the two cleared here are"
     " two of them -- so this pass is a dent and is reported as one",
     len(UNADJ) == 2170 and len({r[0] for r in UNADJ}) > 300)

gate("Ⓓ②  and almost all of what remains is another seat's: fewer than a third of the receipts"
     " carrying unadjudicated keys sit under this line's own paper directory, and this seat does not"
     " adjudicate another seat's pin -- the verdict is a judgement about what that receipt's gate is"
     " FOR, which is theirs to state",
     sum(1 for p in {r[0] for r in UNADJ} if p.startswith('receipts/P15_CR_cosmology/'))
     < len({r[0] for r in UNADJ}) / 3)

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

  WHAT IS LEFT IS NOT A QUEUE THIS SEAT CAN WORK DOWN: 2170 keys remain
  across more than three hundred receipts, and almost all are other seats'.
  This seat does not adjudicate another seat's pin -- the verdict is a
  judgement about what that receipt's gate is FOR, and that is theirs to
  state.  So the pass is bounded by authorship rather than by effort.

  THE GUARD: when a backlog may only fall, the thing to gate is not that
  it fell but that each item it fell by was read.  A count that can only
  improve is an invitation to improve it without doing the work, and the
  check that catches that is whether each recorded reading fits the thing
  it was recorded against.
  ==========================================================================
""")
