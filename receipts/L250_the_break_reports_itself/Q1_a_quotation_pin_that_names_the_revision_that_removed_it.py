#!/usr/bin/env python3
r"""Q1 -- `L-250`: A QUOTATION PIN THAT DIAGNOSES ITS OWN BREAK, TESTED ON SEVEN BREAKS WHOSE
ANSWERS ARE ALREADY KNOWN.

** THE PROPOSAL IS THE OBSERVER LINE'S (r3107) AND IT IS THE RIGHT SHAPE. **  `L-249` left a gate
owed and said why it could not be built: *"pins a live register" is not mechanically separable from
"checks a live register"*, and a gate needs that distinction.  57's answer:

  *"a check that pins a quotation could be required to carry the commit it was pinned at, so a break
  reports 'this text left the paper at rNNNN' instead of 'FAIL.'  That doesn't distinguish pinning
  from checking -- it just makes the break self-diagnosing."*

  ⇒ ** Exactly right, and it needs no distinction at all.  `corpus/quotepin.py` is the build. **

** ⌗ THE TEST IS THE POINT: it is run on breaks whose answers were established BEFORE the tool
existed. **  *Seven quotations, each one a pin this session or the observer line's already repaired
by hand, each with a revision found by reading `git log` directly.  ** If the helper is worth having
it must return those same revisions without being told them. ***

** ⚠ AND THE CONTROL IS THE HALF THAT MATTERS.  A tool that names a removing commit for EVERY absent
string is worse than no tool: it would send a reader hunting a removal that never happened. **
  ⇒ *** NEVER-THERE and GONE are different findings, and the helper must separate them. ***

** ⌷ WHAT IT DELIBERATELY DOES NOT DO. **  *Decide what the replacement MEANS.  It names the commit
and that commit's subject; whether the new wording strengthens, weakens or relocates the claim is a
reading.*  ⇒ ** A helper that guessed would be `L-249`'s own error in a new place -- a tool asserting
what a person must judge -- so the nearest-added-line is printed as a CANDIDATE and never returned as
a verdict. **

Run:  python3 receipts/L250_the_break_reports_itself/Q1_...py

Written r3108 (`L-250`).  Stated for reversal.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
from quotepin import pinned, removing_commit, candidate_replacement   # noqa: E402

fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


def read(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()


print(__doc__)

# ** every one of these was found by hand, BEFORE the helper existed -- by this line at r3105 or by
# ** the observer line at r3106/r3107.  They are the answers the tool is graded against. **
KNOWN = [
    ('is not settled by this reading and is not claimed here', 'corpus/CR_framework.tex', 'r3059',
     'handed back to 57 at r3105; re-pinned by them at r3107'),
    ('the mechanism of the crossing, not its unitarity', 'corpus/CR_framework.tex', 'r3096',
     'the same pair'),
    ('a closure on a protected item is Daryl', 'PROTECTED_OPEN.md', 'r2826',
     'C1 -- closure authority moved from a PERSON to a MECHANISM'),
    ('IS AN ARGUMENT, NOT A COMPUTATION', 'kills/PO-7.md', 'r2993',
     'L805/S1 -- the pin broke because the receipt reproduced the thing'),
    ('r2674 pointer', 'kills/PO-7.md', 'r2993', 'L811/S1 -- the same rewrite'),
    ('cut is four and **says nothing about the substrate**', 'BOARD.md', 'r2832h',
     'N1 -- BOARD pruned, the wording lives in the arc'),
    ('is part of what this paragraph leaves open at its end', 'corpus/canonical_time.tex', 'r2970',
     'S4 -- P10 strengthened; the observer line re-pinned it'),
]

print('=' * 78)
print('PART 1 -- SEVEN BREAKS WITH KNOWN ANSWERS, GRADED')
print('=' * 78)
print(f'    {"expected":>9}  {"returned":>9}   file                              why it broke')
for quote, path, want, why in KNOWN:
    ok, msg = pinned(quote, read(path), path, hint=False)
    got = msg.split(' at ')[1].split(' --')[0] if (not ok and ' at ' in msg) else 'PRESENT'
    print(f'    {want:>9}  {got:>9}   {path:<32}  {why[:44]}')
    check(f'⓵ {path.split("/")[-1][:26]:<26} names {want}', got == want)

print()
print('=' * 78)
print('PART 2 -- ⛭⛭ THE CONTROL: NEVER-THERE MUST NOT REPORT A REMOVAL')
print('=' * 78)
NEVER = [
    ('the horizon is a perfectly ordinary Tuesday', 'corpus/CR_framework.tex'),
    ('lim sup of the quixotic bifurcation', 'PROTECTED_OPEN.md'),
]
for quote, path in NEVER:
    ok, msg = pinned(quote, read(path), path, hint=False)
    sha, _ = removing_commit(quote, path)
    print(f'    {path:<32}  "{quote[:40]}"')
    check('⓶ a string that was never in the file is reported NEVER-THERE, not as a removal',
          not ok and sha is None and 'may never have been in this file' in msg)
# ** and the reason that matters, stated as its own check rather than left to the reader **
check('⓶ᵇ ⛭ so the tool separates GONE from NEVER-THERE -- a tool that named a commit for every '
      'absent string would send a reader hunting a removal that did not happen',
      all(removing_commit(q, p)[0] is None for q, p in NEVER)
      and all(removing_commit(q, p)[0] is not None for q, p, _, _ in KNOWN))

print()
print('=' * 78)
print('PART 3 -- A PIN TO THE WRONG COMMIT IS REPORTED AS SUCH')
print('=' * 78)
print('  *A pin carries a commit the text is claimed to have stood at.  ** If the text was not there')
print('   either, the PIN is wrong and not only the paper -- and saying "the text left at rNNNN"')
print('   would be misleading. ***')
q, path = KNOWN[0][0], KNOWN[0][1]
good_at = subprocess.run(['git', 'rev-parse', '5e30d0e9^'], cwd=ROOT,
                         capture_output=True, text=True).stdout.strip()
# ** a WRONG pin is one naming a commit where the text is not there.  The repo's root commit is
# ** r2419's consolidation, which already CARRIES this sentence -- so "the earliest commit" is not a
# ** wrong pin, and using it would have tested nothing.  *Caught by the control failing.*
#   ⇒ HEAD is unambiguously after the removal, so a pin to it is wrong by construction.
bad_at = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                        capture_output=True, text=True).stdout.strip()
_, msg_good = pinned(q, read(path), path, at=good_at, hint=False)
_, msg_bad = pinned(q, read(path), path, at=bad_at, hint=False)
print(f'    pinned at {good_at[:12]} (r3059^, where it stood) -> reports WAS present')
print(f'    pinned at {bad_at[:12]} (HEAD, after the removal)  -> reports the PIN is wrong')
check('⓷ a correct pin is confirmed against the commit it names', 'and it WAS present' in msg_good)
check('⓷ᵇ ⛔ and an incorrect one says so -- "the PIN is wrong, not only the paper"',
      'the PIN is wrong' in msg_bad)

print()
print('=' * 78)
print('PART 4 -- ⌷ THE HINT IS A HINT, AND IS NOT ALLOWED TO BECOME A VERDICT')
print('=' * 78)
q, path, _, _ = KNOWN[0]
sha, _subj = removing_commit(q, path)
cands = candidate_replacement(sha, path, q)
print(f'    nearest added line by word overlap at {sha[:12]}:')
for c in cands:
    print(f'      "{c[:96]}"')
if not cands:
    print('      (none scored above the floor -- which is also a correct outcome)')
check('⓸ the hint is returned separately from the verdict, so a caller cannot mistake it for one -- '
      '`pinned()` returns (ok, message) and the candidate is only ever text inside the message',
      isinstance(pinned(q, read(path), path), tuple)
      and isinstance(pinned(q, read(path), path)[0], bool))
_, msg_h = pinned(q, read(path), path, hint=True)
check('⓸ᵇ and where a hint is shown it is LABELLED a hint in the message itself',
      'not a verdict' in msg_h or not cands)
check('⓸ᶜ ⌗ and the helper never claims to know what the replacement MEANS -- no word in its output '
      'asserts strengthened, weakened or relocated',
      not any(w in msg_h.lower() for w in ('strengthen', 'weaken', 'relocat', 'equivalent')))

print()
print('=' * 78)
print('PART 5 -- IT IS AVAILABLE TO RECEIPTS, AND COSTS ONE IMPORT')
print('=' * 78)
print('    from quotepin import pinned')
print("    ok, why = pinned(SENTENCE, tex, 'corpus/CR_framework.tex')")
print("    check('P7 states ...' if ok else why, ok)")
print()
print('  ⇒ ** A red run then reads "this text left corpus/CR_framework.tex at r3059 -- <subject>"')
print('     rather than "FAIL", and the next reader starts at the commit instead of at a search. **')
check('⓹ the helper lives in `corpus/` where every receipt can reach it',
      os.path.exists(os.path.join(ROOT, 'corpus', 'quotepin.py')))

print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⚠ ** WHAT IS STILL OWED, and it is what `L-249` said: no gate REQUIRES this. **  *A receipt')
print('     may still pin a quotation the old way, and nothing stops it.  Requiring the helper needs')
print('     the same pinning-versus-checking distinction that could not be made -- so what this adds')
print('     is a better failure, not an enforced practice.*')
print()
