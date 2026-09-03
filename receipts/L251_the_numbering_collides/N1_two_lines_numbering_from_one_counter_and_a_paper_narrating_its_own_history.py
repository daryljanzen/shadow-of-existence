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
    ⛭⛭ ** WITHDRAWN r3128 (`L-256`), against this receipt. **  *Three more collisions arrived in the
      sixteen revisions after this was written -- `r3103`, `r3104`, and `r3112`, which is this
      receipt's own revision.*  ⇒ *** A finding that routes its own remedy and then recurs is not
      waiting for a decision; it is accumulating cost while one is not made.  The band is PARITY:
      this line takes the EVEN half, `check_revision_collisions` enforces it on this line's own
      unmerged commits BEFORE the merge, and the other line adopting the ODD half is a request that
      has been made and is not presumed answered. ***  ⌷ *`r3127` is skipped, and the skip is the
      first instance of the rule.*

Run:  python3 receipts/L251_the_numbering_collides/N1_...py

Written r3112 (`L-251`); PART 2 re-pinned and the band taken r3128 (`L-256`).  Stated for reversal.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
# ** ⛭⛭ NODE IS SET HERE, BEFORE THE IMPORT, AND THAT IS NOT A CONVENIENCE (r3962). **  The gate
# ** reads `NODE` AT IMPORT TIME and *refuses to default* when it is unset -- r3679's rule, written
# ** after an unset NODE silently certified the EVEN half on odd-banded trees and passed 21
# ** collisions.  ** The refusal is right.  What was wrong is this file inheriting the answer from
# ** whoever happened to run it: ** unset in a plain shell, `ci` under `sweep_gates.sh`, and the
# ** receipt's verdict changed with the caller.
#   ⇒ *** A RECEIPT THAT ASSERTS `C.PARITY == 0` IS MAKING A CLAIM ABOUT A NAMED LINE'S BAND, so it
#       must NAME the line rather than read it out of the environment. ***  `60` is this line, it is
#       on the even half by declaration, and the assertion below now says so out loud instead of
#       depending on it.  *A check whose result depends on the caller's environment is not a check
#       of the corpus; it is a check of the caller.*
os.environ.setdefault('NODE', '60')
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

def _fires_on_new():
    """** SEEDED: take the three post-r3112 collisions OUT of the baseline; the gate must name them
    and exit 1. **  *A detection gate is only shown to work by being shown a defect it has not been
    told about -- "the gate is green" shows nothing at all.*
    """
    import contextlib
    import io
    keep = set(C.BASELINE)
    try:
        C.BASELINE.difference_update({'r3103', 'r3104', 'r3112'})
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = C.main()
        out = buf.getvalue()
    finally:
        C.BASELINE.clear()
        C.BASELINE.update(keep)
    named = all(f'[FAIL] {r}' in out for r in ('r3103', 'r3104', 'r3112'))
    # ** and the restore is VERIFIED, not trusted to the `finally` -- c54.213 **
    return rc == 1 and named and C.BASELINE == keep


print()
print('=' * 78)
print('PART 2 -- ⛭⛭ THE COLLISIONS, AND THE TEST THAT SEPARATES THEM FROM SPANS')
print('=' * 78)
bad = C.collisions()
print(f'    {len(bad)} revision id(s) claimed on divergent branches')
recent = [r for r in bad if int(r[1:]) >= 3099]
older = [r for r in bad if int(r[1:]) < 3099]
print(f'      {len(older)} in r2502-r2832 (~330 revisions)   {len(recent)} in r3099-r3111 (13)')
# ⛔⛭⛭ AMENDED r3128 (`L-256`).  ** THESE TWO CHECKS PINNED A DEFECT COUNT TO THE MOMENT IT WAS
# ** MEASURED, AND THE COUNT ROSE -- so they went red for the reason the finding PREDICTED. **
#   *The finding is "two lines numbering from one counter collide, and the rate is accelerating".
#   Three more arrived in the sixteen revisions after it was written, and the receipt reporting the
#   acceleration failed because the acceleration continued.*
#   ⇒ *** r3105's rule, one level up: a check that pins a LIVE register punishes the finding it
#       defends.  A DEFECT COUNT is the same object -- so the historical claim is read at the SHA
#       where it was made, and the present is a separate claim in the direction that can only be
#       good news: the count has not FALLEN below what was found. ***
AT = '5af2a1da54'          # r3112, where the twelve were counted
import tempfile as _tf                                                     # noqa: E402
import shutil as _sh                                                       # noqa: E402
_wt = _tf.mkdtemp()
subprocess.run(['git', 'worktree', 'add', '--detach', _wt, AT], cwd=ROOT,
               capture_output=True, text=True)
try:
    at_bad = C.collisions(root=_wt)
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', _wt], cwd=ROOT, capture_output=True)
    _sh.rmtree(_wt, ignore_errors=True)
at_recent = [r for r in at_bad if int(r[1:]) >= 3099]
print(f'    AT {AT} (r3112, where this was written): {len(at_bad)} collisions, '
      f'{len(at_recent)} of them in r3099-r3111')
check(f'⓶ twelve revision ids were claimed by divergent branches AT r3112 -- read at the SHA, '
      f'measured {len(at_bad)}', len(at_bad) == 12)
check(f'⓶ᵇ ⛔ and four of the twelve fell in the last thirteen revisions -- measured '
      f'{len(at_recent)} at that SHA, a rate of {len(at_recent) / 13 * 100:.0f} per hundred against '
      f'{len(at_bad) - len(at_recent)} across the ~330 before it',
      len(at_recent) == 4 and len(at_bad) - len(at_recent) == 8)
check(f'⛔ ⓶ᶜ *** AND THE PRESENT, IN THE ONLY DIRECTION THAT IS NEWS: the count has NOT fallen. '
      f'{len(bad)} now against {len(at_bad)} then -- {len(bad) - len(at_bad)} more arrived in the '
      f'revisions since, which is the acceleration this finding reported CONTINUING, and it is why '
      f'r3128 stops routing the band and takes it. ***', len(bad) >= len(at_bad))
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
# ⛭⛭ AMENDED r3128 (`L-256`): ** "THE GATE IS GREEN" IS A CLAIM ABOUT THE FUTURE, and it is the
# ** one thing a detection gate is built NOT to promise. **  *This went red when three new
# collisions arrived -- that is the gate WORKING.  What a receipt can assert is that the gate FIRES
# on a collision outside its baseline, and that its baseline names rather than counts.*
check('⓸ᵇ check_revision_collisions FIRES on a collision outside its baseline: with the three that '
      'arrived after r3112 removed from BASELINE, it reports them by name and exits 1',
      _fires_on_new())
check('⓸ᶜ ⌗ and it is green as the tree stands, with those three now baselined BY NAME',
      C.main() == 0)
check('⓸ᵈ and both gates name their known sites rather than counting them -- a count can be '
      f'satisfied by fixing one and adding another.  {len(T.BASELINE)} tense sites, '
      f'{len(C.BASELINE)} collisions, {len(C.BAND_GRANDFATHERED)} band exception',
      len(T.BASELINE) == 5 and len(C.BASELINE) == 15 and len(C.BAND_GRANDFATHERED) == 1)

print()
print('=' * 78)
print('PART 5 -- ⛭⛭ THE BAND, TAKEN RATHER THAN ROUTED')
print('=' * 78)
print('  *r3112 wrote that banding revision numbers "is not a node\'s call" and routed it.  Three')
print('   more collisions arrived in the sixteen revisions that followed, and one of them is r3112')
print('   itself -- the revision that reported the problem.*')
check('⓹ the band is PARITY and this line takes the even half -- the cheapest band that keeps the '
      'chronological reading a range-band would destroy',
      C.PARITY == 0 and 'THE BAND IS PARITY' in
      open(os.path.join(ROOT, 'corpus', 'check_revision_collisions.py'),
           encoding='utf-8', errors='replace').read())
_v = C.band_violations()
check(f'⓹ᵇ and it is PREVENTION: it reads this line\'s own unmerged commits, which are the only '
      f'ones whose numbers can still be changed -- {len(_v) if _v is not None else "no upstream"} '
      'out of band', _v == [])
# ⛔⛭⛭ AMENDED r3142 (`L-261`): ** THIS CHECK ASSERTED THAT A QUESTION WAS STILL OPEN, and it broke
# ** WHEN THE QUESTION WAS ANSWERED. **  *It required the gate to say the odd half "is a REQUEST, not
#   an assumption"; node 57 accepted the band and now runs `PARITY = 1`, so the gate records the
#   ANSWER and the check went red on the settlement it asked for.*
#   ⇒ *** THE SAME CLASS AS PINNING A LIVE REGISTER, with "still open" as the thing that moves.  A
#       check on the state of a request punishes the request being granted -- and this is the third
#       site of it in one turn (`L-258`, `L-259`, `L-260`), each time in a different disguise. ***
#   ⇒ ** What must hold is not that the half is still unheld but the property the request was FOR:
#     that the gate cannot describe itself as prevention on a half it does not have.  That is a
#     property of the gate and it SURVIVES the answer, which is what the old form did not. **
_gate_src = open(os.path.join(ROOT, 'corpus', 'check_revision_collisions.py'),
                 encoding='utf-8', errors='replace').read()
check('⓹ᶜ ⌗ and the gate cannot describe itself as prevention on a half it does not hold: with '
      '`OTHER_HALF` unset it prints "THE BAND IS A PROPOSAL, NOT A PREVENTION" instead',
      'THE BAND IS A PROPOSAL, NOT A PREVENTION' in _gate_src
      and 'if OTHER_HALF is None:' in _gate_src)
check('⓹ᶜ¹ ⛭ and the other half IS held now, carried as a fact in the other line\'s own words '
      'rather than presumed', C.OTHER_HALF is not None and 'PARITY = 1' in C.OTHER_HALF)
check('⓹ᵈ and the one grandfathered id is named, not dated -- a cutoff silently absorbs everything '
      f'behind it: {sorted(C.BAND_GRANDFATHERED)}',
      C.BAND_GRANDFATHERED == {'r3125'})

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
print('      this line has not read end to end. ***')
print('  ⛭⛭ *** AND THE NUMBERING IS NO LONGER AMONG THEM.  r3112 routed the band as "not a')
print('      node\'s call"; three more collisions arrived in the sixteen revisions after, one of')
print('      them r3112 itself.  A finding that routes its own remedy and then recurs is not')
print('      waiting for a decision -- it is accumulating cost while one is not made.  The band')
print('      is PARITY, this line takes the EVEN half, and the gate enforces it BEFORE the merge.')
print('      The other line adopting the ODD half is a request, made and not presumed answered. ***')
print()
