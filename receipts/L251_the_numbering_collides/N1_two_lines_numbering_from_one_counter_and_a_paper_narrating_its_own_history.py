#!/usr/bin/env python3
r"""N1 -- `L-251`: TWO FINDINGS FROM READING THE OBSERVER LINE'S OWN WORK, AND ONE OF THEM BITES A
TOOL BUILT ONE REVISION EARLIER.

** ⓵ A PAPER CARRIES ONE STATE, SO IT MAY NOT NARRATE ITS OWN HISTORY. **  r3111 found *"That refit
has since been performed"* in P15 while reading it for something else, and repaired it to *"is
performed here"*.  ** One found by hand is a sighting; the sweep finds five more. **
  ⇒ *** AND ONE OF THE SIX IS NOT A DEFECT, which is why the discriminator matters more than the
      list: p0 says a centrepiece is "stated at what it has since become rather than at what it was
      when first written (r1609)".  That DECLARES the tense on purpose and names the revision. ***
  ⇒ ** So a history phrase with a revision id beside it passes and one without fails -- declared,
    not inferred, the same pattern as `NOT-A-RECEIPT:` and `IN-FLIGHT:`. **

** ⓶ AND TWO LINES NUMBERING FROM ONE COUNTER COLLIDE. **  The corpus reserves `L-` id BANDS per
line because two nodes working offline cannot otherwise avoid choosing the same number.
** Revision numbers have no band and no gate, and are chosen the same way: look at the front, add
one. **
  ⇒ *** TWELVE HAVE ALREADY HAPPENED.  Eight in `r2502`--`r2832`, some 330 revisions; FOUR in
      `r3099`--`r3111`, which is thirteen.  2.4 per hundred then, 31 per hundred now. ***
  ⌗ *The cause is not carelessness.  It is two lines working fast at the same front, which is the
  arrangement.*

** ⛭⛭ AND IT BITES `quotepin`, BUILT ONE REVISION EARLIER. **  That tool reports *"this text left the
paper at rNNNN"*.  ** With two `r3108`s, that sentence names an ambiguous revision. **
  ⇒ *It already prints the commit SHA beside the number, which is unambiguous -- but that was luck
  rather than design, and it is asserted here so it cannot be removed silently.*

** ⚠ WHAT IS NOT DONE, DELIBERATELY. **
  · *The five history phrases are REPORTED, not rewritten.*  ** "has since been measured" becomes
    "is measured" only if the measurement is in the paper's current state, and knowing that is a
    READING of the paper. **  *Three of the four papers are ones the observer line has read end to
    end; this line has not.*
  · *The numbering is not banded.*  ** A gate over history detects a collision after the merge and
    cannot prevent one -- exactly `check_id_bands`'s position. **  *** The prevention is a BAND, and
    revision numbers are programme-wide by design, so banding them changes how the corpus numbers
    itself.  That is not a node's call. ***

Run:  python3 receipts/L251_the_numbering_collides/N1_...py

Written r3112 (`L-251`).  Stated for reversal.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_paper_tense as T                                     # noqa: E402
import check_revision_collisions as C                             # noqa: E402
from quotepin import pinned                                       # noqa: E402

fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


print(__doc__)
print('=' * 78)
print('PART 1 -- THE HISTORY PHRASES, AND THE ONE THAT IS DECLARED')
print('=' * 78)
found = T.sites()
declared = [s for s in found if s[2]]
undeclared = [s for s in found if not s[2]]
for n, p, d, _ in found:
    print(f'    {"DECLARED  " if d else "undeclared"}  {n:<26} [{p}]')
check('⓵ six history phrases stand in paper bodies', len(found) == 6)
check('⓵ᵇ ⛭ and exactly one DECLARES its tense with a revision id beside it -- so the discriminator '
      'separates a deliberate then/now from an undeclared drift', len(declared) == 1)
check('⓵ᶜ the declared one is p0\'s, which names r1609 in the sentence itself',
      declared and declared[0][0] == 'geometric_core_paper.tex' and 'r1609' in declared[0][3])
check('⓵ᵈ and the other five are the drift, across three papers', len(undeclared) == 5
      and len({s[0] for s in undeclared}) == 3)
# ** the phrase the observer line repaired must be GONE, or this sweep is measuring a stale tree **
cosmo = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
             errors='replace').read()
check('⓵ᵉ and r3111\'s own repair has landed -- "That refit has since been performed" is gone',
      'That refit has since been performed' not in cosmo)

print()
print('=' * 78)
print('PART 2 -- ⛭⛭ THE COLLISIONS, AND THE TEST THAT SEPARATES THEM FROM SPANS')
print('=' * 78)
bad = C.collisions()
print(f'    {len(bad)} revision id(s) claimed on divergent branches')
recent = [r for r in bad if int(r[1:]) >= 3099]
older = [r for r in bad if int(r[1:]) < 3099]
print(f'      {len(older)} in r2502-r2832 (~330 revisions)   {len(recent)} in r3099-r3111 (13)')
check('⓶ twelve revision ids are claimed by divergent branches', len(bad) == 12)
check('⓶ᵇ ⛔ and four of the twelve fall in the last thirteen revisions -- the rate is accelerating, '
      'not historical', len(recent) == 4 and len(older) == 8)
# ** the discriminator, and the CONTROL that shows it is doing work **
# a subject-text rule (this gate's first version) cannot tell a span from a collision
out = subprocess.run(['git', 'log', '--format=%h%x09%s'], cwd=ROOT,
                     capture_output=True, text=True).stdout
by = {}
for line in out.split('\n'):
    if '\t' not in line:
        continue
    sha, _, subj = line.partition('\t')
    m = C.BARE.match(subj.strip())
    if m:
        by.setdefault(m.group(1), []).append((sha, m.group(2).strip()))
subject_rule = {r for r, e in by.items() if len({w for _, w in e}) > 1}
print(f'    a SUBJECT-TEXT rule would flag {len(subject_rule)}; ancestry flags {len(bad)}')
check('⓶ᶜ ⛭ the subject rule over-flags -- this corpus works one revision across many commits '
      '(r2674 spans 28), and a chain is a SPAN, not a collision',
      len(subject_rule) > len(bad) and 'r2674' in subject_rule)
check('⓶ᵈ and ancestry is the distinction: a span is pairwise ancestor-related, a collision is two '
      'commits neither of which reaches the other', set(bad) < subject_rule)

print()
print('=' * 78)
print('PART 3 -- ⛭ IT BITES `quotepin`, WHICH IS WHY THIS IS NOT BOOKKEEPING')
print('=' * 78)
print('  *`quotepin` answers "when did this text leave the paper?" with a revision number.*')
print(f'  ** And `r3108` is claimed twice: **')
for sha, w in bad.get('r3108', []):
    print(f'      {sha}  {w[:72]}')
_, why = pinned('That refit has since been performed', cosmo, 'corpus/CR_cosmology.tex', hint=False)
print(f'    quotepin on the observer line\'s own find returns:')
print(f'      {why[:150]}')
check('⓷ quotepin names the revision for r3111\'s own find', 'r3108' in why)
check('⓷ᵇ ⛭ AND prints the commit SHA beside it, which is unambiguous where the revision number is '
      'not -- asserted here so it cannot be removed silently', 'commit ' in why)
qp = open(os.path.join(ROOT, 'corpus', 'quotepin.py'), encoding='utf-8', errors='replace').read()
check('⓷ᶜ and the SHA is in the message template rather than incidental to one path',
      'commit {sha[:12]}' in qp)

print()
print('=' * 78)
print('PART 4 -- BOTH GATES ARE GREEN AND BOTH ARE BASELINED BY NAME')
print('=' * 78)
check('⓸ check_paper_tense is green on the repaired tree', T.main() == 0)
check('⓸ᵇ check_revision_collisions is green', C.main() == 0)
check('⓸ᶜ and both name their known sites rather than counting them -- a count can be satisfied by '
      'fixing one and adding another', len(T.BASELINE) == 5 and len(C.BASELINE) == 12)

print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⌷ *** WHAT IS ROUTED RATHER THAN TAKEN: the five history phrases need a reading of papers')
print('      this line has not read end to end, and the numbering needs a BAND, which changes how')
print('      the corpus numbers itself and is not a node\'s call. ***')
print()
