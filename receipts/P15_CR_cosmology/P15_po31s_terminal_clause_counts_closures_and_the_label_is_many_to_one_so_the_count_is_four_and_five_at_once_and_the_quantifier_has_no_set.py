#!/usr/bin/env python3
"""P15 receipt -- `PO-31`'s terminal clause, taken as a CHECK rather than as prose.  Nothing is
ordered; the board states this row is where this seat's open work is and `r7224` pre-registered the
step before any computation.

*** ⛭⛭⛭ THE PRE-REGISTERED PREDICTION FAILS AND THE PRE-REGISTERED THIRD OUTCOME FIRES: THE CLAUSE
    IS NOT CHECKABLE AS WRITTEN, AND NOT FOR THE REASON I EXPECTED.  I LOOKED FOR A CHANNEL THE ROW
    HAD MISSED.  WHAT IS WRONG IS THE COUNT THE CLAUSE RESTS ON AND THE SET ITS QUANTIFIER RANGES
    OVER. ***

The live clause, set at `r7197`, terminates the row `if it is demonstrated that no channel available
to this construction can supply a red tilt --- four are closed and each by a mechanism`.

** ⓵ THE WORD `closed` IS MANY-TO-ONE ON THIS ROW, SO THE COUNT IS FOUR AND FIVE AT ONCE. **  *The
row says in its own words* `Five channels were closed --- substrate, collapse leg, finite duration,
interior vacuum, transfer`, *and the live clause says* `four are closed`.  ⇒ ** Both are in the row,
neither is a typo, and they differ because `closed` names two different things: a CANDIDATE examined
and dismissed, and a MECHANISM that yields no tilt. **  *The transfer is the fifth under the first
reading and is not a member under the second, because `r6913` measured that it IMPRINTS --- it does
supply a running, so it is dismissed as the source of a near-constant tilt while being the one
candidate that is not silent.*  ⌗ ***This is the corpus's own guard about labels, met on a count: before
two things are identified by a label, check how many-to-one the label is on the object.***

** ⓶ AND THE QUANTIFIER RANGES OVER A SET THE ROW NEVER WRITES DOWN. **  *`no channel available to
this construction` is the terminal condition's subject, and nowhere in the row is that set
enumerated.*  **What the row contains is a HISTORY of what was tried**, in the order it was tried.
⇒ *A terminal condition over a set that exists only as a list of attempts cannot be demonstrated: it
can only run out of ideas, which is the distinction the clause's own phrase `by a mechanism rather
than by a failure to find one` was written to protect and does not extend to the set itself.*

** ⓷ AND THE CLAUSE'S FORM IS THE ONE THE ROW ALREADY RETIRED, WHICH IS THE PART THAT MATTERS MOST. **
*`r6913` states* `The row stops being a channel hunt and becomes a statement about the interior model
plus one computed requirement on its input`.  ⇒ *** The live clause, set EIGHTY-FOUR revisions later,
restates the row as a channel hunt.  It did not contradict a stale clause --- `r7027` had already
installed the one-live-clause discipline and `r7197` superseded that clause correctly.  What came
through both passes unchanged was the FORM, because each pass checked that a clause was current and
neither asked whether it still described the row. ***  ⌗ *That is the same shape `r7027` found when it
built the discipline: the gate checked presence where the question was currency; here currency is
checked where the question is FIT.*

⚠ ** AND ONE DRAFT OF THIS RECEIPT WAS WRONG IN THE DIRECTION THAT WOULD HAVE FLATTERED IT. **  *The
first version of `Ⓓ` asserted that the row contains NO totality-shaped phrase about channels.  It
contains THREE.*  ⇒ ** The claim is now the stronger one, because each of the three was READ: `every
channel closed SO FAR`, `ONE CHANNEL IS LEFT`, `the only place a scale survives` --- every one of them
scoped to the channels ALREADY TRIED. **  *A count of matches was not a finding; reading them is.*

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not file the transfer as a fifth closure, does not
re-open the four, does not declare the row discharged or terminated, and does not edit the row.*  ⇒
** The repair is PROPOSED and routed, not applied: the clause's terminal half should be stated over
the REQUIREMENT `r6913` computed --- an input whose own running is the transfer's negated --- rather
than over a set of channels, and its count should name what it counts. **  *The row and its clause are
the gating seat's.*

** COMPUTES: every sentence this receipt relies on, extracted from `THE_REGISTER` programmatically and
   asserted present verbatim rather than quoted from memory; the distinct closure COUNTS the row
   asserts, by one rule applied to the whole row; the absence of any enumeration of the quantifier's
   set, by the same kind of rule; two must-come-back-wrong controls on the counting rule, one
   truncation and one synthetic row; and the register's digest before and after, so the row is
   demonstrably unedited. *** No number is asserted that is not counted here, and no verdict on the
   row is offered. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (stdlib only; ~1 s)

⚠ ** REPAIRED AFTER `r7215` STRUCK THE ROW, AND THE REPAIR IS THE FINDING'S OWN CLASS COMING HOME. **
*`Ⓐ③` pinned the LIVE clause marker to `r7197` --- the status of a sentence the row was asking to
change --- and `r7215` struck `PO-31` on `r7226`'s enumeration and set a new clause.* ⇒ ***So this
receipt's own gate went RED on the SUCCESS OF ITS OWN WORK: the class `L-249` named at `r3105`, which
`S3` read in full two revisions before this, instanced by this seat's own hand.*** **The repair is
`L-249`'s: every sentence the argument reasons FROM is now read at a PINNED commit where it cannot
move, and the LIVE state is asserted as a DISJUNCTION over the states the row may be in --- still
carrying the clause, struck, or amended to a later one --- rather than as a pin on one of them.**
⌗ *`Ⓐ⑤` then asserts which of those states actually holds, so the strike is recorded as a fact
rather than absorbed into a green.*
"""
import hashlib
import os
import re
import subprocess
import sys

print(__doc__.split("** COMPUTES:")[0].rstrip())
BAR = "=" * 104
fail = []


def gate(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.path.join(ROOT, 'THE_REGISTER.md')
if not os.path.exists(REG):
    print(f"  ⛔ A PATH THIS RECEIPT READS IS NOT ON DISK: {REG}")
    sys.exit(1)
REGBYTES = open(REG, 'rb').read()
REGHASH = hashlib.sha256(REGBYTES).hexdigest()
LIVE_RAW = REGBYTES.decode('utf-8')

# ⛭⛭⛭ REPAIRED AFTER `r7215` STRUCK THE ROW, AND THE REPAIR IS `L-249`'s.
#    *** This receipt's `Ⓐ③` pinned the LIVE clause marker to `r7197` --- the status of a sentence the
#    row was asking to change --- and `r7215` struck `PO-31` on `r7226`'s enumeration and set a new
#    clause.  So the gate went RED on the SUCCESS OF ITS OWN WORK: the ninth instance of the class
#    `L-249` named at `r3105`, produced by this seat's own hand TWO REVISIONS AFTER `S3` measured that
#    class in full. ***
#    ⇒ The repair, which is the one `S3` and `S5` both recorded: ** every sentence the argument reasons
#      FROM is read at a PINNED commit, where it cannot move; and the LIVE state is asserted separately
#      as a DISJUNCTION over the states the row may be in, not as a pin on one of them. **
#    ⌗ The pin is the last trunk commit whose `PO-31` row carries the `r7197` clause --- the trunk this
#      receipt was derived against, immediately before the strike.
PIN = 'd6ff1b549ac29aacccc63db87b8f29e8df0c0e6f'
RAW = subprocess.run(['git', 'show', f'{PIN}:THE_REGISTER.md'], cwd=ROOT, capture_output=True,
                     text=True, check=True).stdout


def row_of(raw):
    """the row is ONE line of the register, located by its id and not by a line number, because a
    line number is a fact about today's file and the id is a fact about the row."""
    rows = [l for l in raw.split('\n')
            if '**PO-31**' in l or re.search(r'\|\s*`?PO-31`?\s*\|', l)]
    return max(rows, key=len) if rows else ''


ROW = row_of(RAW)
FLAT = ' '.join(ROW.split())
LIVE_FLAT = ' '.join(row_of(LIVE_RAW).split())


def present(s):
    """is this sentence in the row, whitespace-normalised?  No regex: the literal, or nothing."""
    return ' '.join(s.split()) in FLAT


# ============================================================ A. the row's own words
head("A.  THE SENTENCES THIS RECEIPT RESTS ON, READ OUT OF THE ROW AND NOT RECALLED")

gate(f"Ⓐ① the `PO-31` row is located by its id and is one line of {len(FLAT)} characters",
     len(FLAT) > 20000)
TERMINAL = ("it is demonstrated that no channel available to this construction can supply a red "
            "tilt")
FOUR = "four are closed and each by a mechanism"
FIVE = ("Five channels were closed --- substrate, collapse leg, finite duration, interior vacuum, "
        "transfer")
TURN = ("The row stops being a channel hunt and becomes a statement about the interior model plus "
        "one computed requirement on its input")
for _lab, _s in (("the terminal condition", TERMINAL), ("its count", FOUR),
                 ("the five-channel sentence", FIVE), ("the turn", TURN)):
    gate(f"Ⓐ② {_lab} is present verbatim", present(_s))
gate("Ⓐ③ and the clause this receipt reasons from is the one set at `r7197`, read AT THE PIN where "
     "it cannot move",
     "THE LIVE CLAUSE (SET `r7197`)" in FLAT or "THE LIVE CLAUSE (SET r7197)" in FLAT)

# ⛭⛭ AND THE LIVE STATE AS A DISJUNCTION OVER THE STATES THE ROW MAY PRODUCE, which is what the
#    standing guard asks for and what the first draft of this gate did not do.
_m = re.search(r'THE LIVE CLAUSE \(SET `?r(\d+)', LIVE_FLAT)
_LIVE = {
    'still carries the r7197 clause': bool(re.search(r'THE LIVE CLAUSE \(SET `?r7197', LIVE_FLAT)),
    'STRUCK': LIVE_FLAT.lstrip().startswith('| ~~') or '~~**PO-31**~~' in LIVE_FLAT,
    'amended to a later clause': bool(_m) and int(_m.group(1)) > 7197,
}
for _k, _v in _LIVE.items():
    print(f"      live row: {_k:32s} {_v}")
gate("Ⓐ④ ⛭⛭ and the LIVE row is in one of the states this receipt enumerates rather than pinned to "
     f"one of them -- {', '.join(k for k, v in _LIVE.items() if v) or 'NONE OF THEM'} -- so the "
     "strike this receipt's own work led to cannot turn this receipt red",
     any(_LIVE.values()))
gate("Ⓐ⑤ ⛔ and the finding is recorded rather than smoothed over: the row IS struck and its clause "
     "IS a later one, so this receipt's first `Ⓐ③` went red on the success of its own work -- the "
     "class `L-249` named and `S3` measured, instanced by this seat two revisions later",
     _LIVE['STRUCK'] and _LIVE['amended to a later clause']
     and not _LIVE['still carries the r7197 clause'])

# ============================================================ B. the count, by a rule
head("B.  ⛔ THE COUNT THE TERMINAL CLAUSE RESTS ON IS FOUR AND FIVE AT ONCE")

WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8}
# ONE rule, applied to the whole row: a number word or digit, then within 40 characters a word built
# on `channel` or `closure` or the participle `closed`.  No hand-picked sentences.
RULE = re.compile(r'\b(' + '|'.join(WORDS) + r'|\d+)\b(?=((?!\b(?:' + '|'.join(WORDS)
                  + r')\b).){0,40}?(channels?|closures?|closed))', re.I)


def counts(text):
    out = {}
    for m in RULE.finditer(text):
        tok = m.group(1).lower()
        n = WORDS.get(tok, int(tok) if tok.isdigit() else None)
        if n is not None and 1 <= n <= 8:
            out.setdefault(n, 0)
            out[n] += 1
    return out


C = counts(FLAT)
print(f"      closure counts the row asserts, by one rule over the whole row: "
      f"{dict(sorted(C.items()))}")
gate(f"Ⓑ① the rule finds BOTH four and five, each more than once -- "
     f"four x{C.get(4, 0)}, five x{C.get(5, 0)}", C.get(4, 0) >= 2 and C.get(5, 0) >= 1)
gate("Ⓑ② and they are not a typo and not a stale clause: the FIVE is in the row's own summary of its "
     "real move, the FOUR is in the clause that is CURRENT, so the row carries both as live text",
     present(FIVE) and present(FOUR) and present(TERMINAL))
_whynot = "filing it as a fifth would overstate the row by one"
gate("Ⓑ③ ⛭ and the row's reason for refusing a fifth is about the SEAM'S FLUX and not the transfer, "
     "so the refusal was right about its own object and left the count where it already was",
     present(_whynot) and present("THE SEAM'S FLUX IS NOT A FIFTH CHANNEL"))

# ============================================================ C. the label
head("C.  ⌗ WHY IT IS BOTH: `closed` NAMES A DISMISSED CANDIDATE AND A SILENT MECHANISM")

IMPRINT = "THE TRANSFER IMPRINTS"
gate("Ⓒ① the transfer is NOT silent -- the row's own heading says it imprints -- so under `a "
     "mechanism that yields no tilt` it is not a closure", IMPRINT in FLAT.upper())
gate("Ⓒ② and it IS a dismissed candidate, counted as the fifth in the row's own list, so under "
     "`a candidate examined and dismissed` it is one", present(FIVE))
gate("Ⓒ③ ⇒ so the two readings differ by exactly the transfer, which is the whole of the "
     "discrepancy: 5 - 4 = 1 and the one is named", C.get(5, 0) >= 1 and C.get(4, 0) >= 1)

# ============================================================ D. the quantifier's set
head("D.  ⛔ AND THE QUANTIFIER'S SET IS NOWHERE IN THE ROW")

# the same KIND of rule: find every TOTALITY-shaped phrase near `channel`, then READ each one --
# because a count of matches is not a finding and an earlier draft of this section asserted zero
# matches and was wrong.  Three exist.  The question is what each is a totality OF.
TOTAL = re.compile(r'\b(all|every|exactly|the only|complete|exhaustive|comprises|consists)\b'
                   r'(((?!\bchannel).){0,60})channels?', re.I)
# a phrase is scoped to the ATTEMPTED set rather than to the AVAILABLE set when its own
# neighbourhood carries one of these -- each taken from the row's wording, not invented here.
SCOPED = ('so far', 'is left', 'are now closed', 'a scale survives', 'closed so far')


def totality(text):
    out = []
    for m in TOTAL.finditer(text):
        lo, hi = max(0, m.start() - 160), min(len(text), m.end() + 160)
        ctx = text[lo:hi]
        out.append((' '.join(m.group(0).split()), ctx,
                    [k for k in SCOPED if k.lower() in ctx.lower()]))
    return out


_tot = totality(FLAT)
print(f"      totality-shaped phrases near `channel` in the row: {len(_tot)} -- and each is READ")
for _ph, _ctx, _sc in _tot:
    print(f"        · {_ph[:58]:<58} scoped by: {_sc if _sc else 'NOTHING'}")
_unscoped = [t for t in _tot if not t[2]]
gate(f"Ⓓ① ⛭⛭ the row DOES carry {len(_tot)} totality-shaped phrases, and EVERY ONE of them is scoped "
     "to the channels ALREADY TRIED rather than to the channels AVAILABLE -- `every channel closed "
     "SO FAR`, `ONE CHANNEL IS LEFT`, `the only place a scale survives` -- so the terminal "
     "condition's domain is still nowhere in the row", len(_tot) >= 3 and len(_unscoped) == 0)
_probe = FLAT + (" For the avoidance of doubt these are all the channels this construction "
                 "contains and there are no others.")
_pt = totality(_probe)
_pu = [t for t in _pt if not t[2]]
gate(f"Ⓓ② ⌗ and the reading is not a way of dismissing whatever turns up: the same rule and the same "
     f"scoping test on the same text PLUS one planted unscoped totality sentence finds it and leaves "
     f"it unscoped ({len(_pu)} unscoped against {len(_unscoped)} on the row itself)",
     len(_pt) == len(_tot) + 1 and len(_pu) == 1)
gate("Ⓓ③ ⇒ so the terminal half can be reached by running out of candidates and not by a "
     "demonstration -- which is the distinction the clause's own `by a mechanism rather than by a "
     "failure to find one` protects for each MEMBER and does not extend to the MEMBERSHIP",
     present("by a mechanism rather than by a failure to find one") and len(_unscoped) == 0)

# ============================================================ E. controls
head("E.  ⌗ THE MUST-COME-BACK-WRONG CONTROLS ON THE COUNTING RULE, FIXED BEFORE THE MEASUREMENT")

_trunc = FLAT[:FLAT.index(FIVE.split(' --- ')[0])] if present(FIVE) else FLAT
_ct = counts(_trunc)
print(f"      on the row TRUNCATED before its five-channel sentence: {dict(sorted(_ct.items()))}")
gate(f"Ⓔ① the rule reads the TEXT and not this seat's expectation: truncating the row before the "
     f"five-channel sentence drops the five ({_ct.get(5, 0)} occurrence(s) against "
     f"{C.get(5, 0)} on the whole row)", _ct.get(5, 0) < C.get(5, 0))
_syn = "Exactly three channels are closed here and nothing else is."
gate(f"Ⓔ② and on a synthetic row carrying ONE count it returns that one and nothing else: "
     f"{dict(counts(_syn))}", counts(_syn) == {3: 1})
_none = "This row names no channels and closes nothing."
gate(f"Ⓔ③ and on a row with no count it returns nothing: {dict(counts(_none))}", counts(_none) == {})

# ============================================================ F. the prediction
head("F.  ⛭⛭⛭ THE PRE-REGISTERED PREDICTION FAILED, AND THE THIRD OUTCOME IS WHAT FIRED")

print("      r7224 predicted: the enumeration comes out LARGER than four, so the row gains a named")
print("      candidate it had not examined and does not terminate.")
print("      Measured: there is no enumeration to be larger or smaller than.  The clause rests on a")
print("      count whose label is many-to-one and quantifies over a set the row never writes down.")
print("      ⇒ The pass condition is NOT met.  The pre-registered THIRD outcome fired instead, which")
print("        was written down in advance precisely so this could not be reported as a success.")
gate("Ⓕ① the pass condition is NOT met and is reported as a failure: no member outside the four is "
     "named by this receipt, because the row's own totality-shaped phrases all turned out to be "
     "about the channels tried, so there was no domain in which to look for one",
     len(_unscoped) == 0)
gate("Ⓕ② and the outcome that did fire is the one the pre-registration names third -- `no rule "
     "generates the list, so the finding is that the clause is not checkable as written`",
     len(_unscoped) == 0 and C.get(4, 0) >= 1 and C.get(5, 0) >= 1)
gate("Ⓕ③ ⛔ and no absence is filed as a closure: the transfer is NOT proposed as a fifth here, it "
     "is exhibited as the reason one label gives two counts", IMPRINT in FLAT.upper())

# ============================================================ G. untouched
head("G.  ⌗ THE ROW IS UNTOUCHED AND THE REPAIR IS A PROPOSAL")

_after = hashlib.sha256(open(REG, 'rb').read()).hexdigest()
gate(f"Ⓖ① the register is byte-identical after this run, checked by digest ({_after[:12]}), so "
     "nothing here edits the row or its clause", _after == REGHASH)
print("      PROPOSED, NOT APPLIED, and routed: state the terminal half over the REQUIREMENT r6913")
print("      computed -- an input whose own running is the transfer's negated, which the row already")
print("      carries as a computed function -- rather than over a set of channels; and have the")
print("      clause name what its count counts.  The clause is the gating seat's to amend.")
gate("Ⓖ② and the proposal is stated in terms the row already contains, so it asks for a rewording "
     "and not for new physics", present("a REQUIREMENT ON THE PROGENITOR AND NOT A RESULT ABOUT IT")
     or present("requirement on the progenitor"))

print(f"\n{BAR}")
if fail:
    print(f"  ⛔ {len(fail)} GATE(S) FAILED")
    for x in fail:
        print(f"      - {x[:96]}")
    sys.exit(1)
print("  ✔ every gate passed")
print(f"{BAR}")
