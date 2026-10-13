#!/usr/bin/env python3
r"""S31 -- `r7289` order ①: the borrowed exemption repaired, with its blast radius measured rather
than estimated, and the estimate corrected downward by this receipt.

COMPUTES: nothing the papers quote.  This receipt reports a repair to `dangling_predicate_v2.py` --
this seat's module, imported byte for byte by four seats -- and measures what the repair moves.

** ⛭⛭⛭ THE REPAIR RE-OPENS NOTHING: of the `21` verdicted `REPAIR-OWED` rows the widened scope
newly exempts, `0` lose their ground --- against a pre-registered `10`. **  *And the registration was
an OVER-count rather than an under-count: its filter matched the word `dangling` in a reason, and the
TRAILING arm's reasons carry that word too.* ⇒ *Read per row, every one rests on a ground the subject
rule never touched: `6` on the trailing arm, `6` on redundancy or grain, `3` markup carriers, `2`
openness markers, a `PROXY`, an undeciding `ALT`, a multi-site pin --- **several of them saying
`dangle: none` in the verdicter's own words.***

** ⛔⛭⛭⛭ AND THAT IS THE FINDING, WHICH IS NOT THE ONE THE ORDER EXPECTED: A DEFECT IN AN EXEMPTION IS
INVISIBLE WHEREVER THE VERDICT HAS A SECOND GROUND, AND VISIBLE EXACTLY WHERE THE ARM IS USED ALONE AS
A SELECTOR. **
  ⌈ *A verdicted row has a reason and a reason names a ground, so a wrong exemption changes nothing
    wherever anything else carries the verdict.* ⇒ ***It changed outcomes in exactly one place:
    `r7285`'s `38`-list, where the subject arm WAS the selector and nothing else had to agree with
    it.  An instrument used to SELECT has no second ground to hide its defects behind, which is why a
    LIST is a harsher test of an arm than a LEDGER is.***
  ⌊ ⌗ *That is also why it survived four revisions of three seats importing the module byte for
    byte, and why `66` was right to order the radius measured rather than assume it was large.*

** ⛔⛭⛭⛭ AND MEASURING THE RADIUS BEFORE LANDING DID NOT ONLY PRICE THE REPAIR --- IT FOUND A DEFECT
IN THE REPAIR. **  *The widened class reaches `a harmonic oscillator, whose Hamiltonian is bounded
below`, which `P10` writes as an APPOSITION inside `that sector is ..., a harmonic oscillator, whose
...`: its subject sits OUTSIDE the span and header ⓸ rules it dangling.* **That is the one row among
the newly-exempt whose verdict rests on the subject rule, so without a fourth condition this repair
would have broken exactly the row it must not.**
  ⌈ ⛭⛭ ***The fourth condition, which the narrow class never needed: the span's first finite verb
    must not sit inside a NON-RESTRICTIVE relative clause --- and the discriminator is the COMMA, not
    the relative pronoun.*** *`a consistency check THAT matches nothing is green forever` is
    restrictive, carries no comma, and does name its subject.*
  ⌊ ⌗ *A widened class needs conditions its narrow form never did, because the narrow form's
    correctness was partly an accident of what it could not reach. **That is the `78`th member read
    from the other side.***

** ⌗ AND ONE WEAKNESS IS REPORTED AND NOT REPAIRED. **  *`THE COST, NAMED` passes the widened test
because `named` sits in the closed `FINITE` list, which cannot tell a finite verb from a past
participle in a title.  Its verdict does not change --- it is a `PROXY` --- the order asked for the
exemption's scope, and **a second repair inside one revision is how a measurement stops being one.***

** ⛔⛭⛭ AND ONE OF THIS RECEIPT'S OWN GATES WAS AN INSTANCE OF THE CLASS IT IS REPAIRING, CAUGHT BY
THE PIN RATCHET. **  *The gate asserting that the conditions are written once did it by grepping the
module's source for a literal line --- **minting a quote-pin key on this seat's own file, in the
revision that is repairing a defect of exactly that shape.*** ⇒ *It now asserts the PROPERTY as
behaviour: stub the private predicate and BOTH public entry points change together, each handed a
different determiner class. ⌗ **A gate that pins the line implementing a property is not a weaker
gate --- it is a gate making a different claim**, which is this line's own standing finding arriving in
its own work for the third time.*

** ✔ THE COMPARABILITY GUARANTEE HOLDS. **  *All five arms --- adopted leading, leading, trailing,
negated, and the disjunction --- return the SAME value on every one of the `2466` verdicted literals,
before and after, checked against the module read out of git at `4b130bdf` rather than against a
memory of it.  `r7257`'s and `r7258`'s figures stay reproducible from the file, which is what makes
this a repair to the exemption's SCOPE and not to the test.*

** ⛭ ONE ROW'S GROUND IS CORRECTED AND IT IS THIS SEAT'S OWN. **  *`r7288` recorded `the whole
difference is carried by` as `a FRAGMENT with no subject inside it`.  It names its subject with a
determiner; what is wrong with it is the TRAILING arm.  The verdict stands, the ground is re-stated by
APPEND per `r7253`, and **the defect this seat measured at `r7288` had caught this seat too, in the
same batch --- it took repairing the exemption to find it.***

⌗ *Sources: `r7289` order ① and the `78`th member; the pre-registration at the commit that pushed
it; the module at `origin/main` before the repair, read out of git rather than remembered; and the
ledger's own reasons, read per row.*
"""
import collections
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the repaired module

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '4b130bdf'   # origin/main at r7289 -- the module as it stood before this repair
PREG = '5c72d3f0'     # the commit that PUSHED the pre-registration, before the repair was written
BASE = 'corpus/quote_pin_baseline.tsv'
PRED = 'computations/beyond_the_wall/r7294_60_the_borrowed_exemption/PREDICTION.md'
MOD = 'computations/beyond_the_wall/r7260_60_land_and_verdict/dangling_predicate_v2.py'
ARMS = ['dangles_leading_adopted', 'dangles_leading', 'dangles_trailing', 'dangles_negated',
        'dangles']


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


print()
print('=' * 100)
print('S31 -- the borrowed exemption repaired, and what it moves measured per row')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE PRE-REGISTRATION CAME BEFORE THE REPAIR, AND IT NAMED A NUMBER ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_pres = [subprocess.run(['git', 'cat-file', '-e', s + '^{commit}'], cwd=ROOT,
                        capture_output=True).returncode == 0 for s in (BEFORE, PREG)]
_anc = all(subprocess.run(['git', 'merge-base', '--is-ancestor', s, 'HEAD'], cwd=ROOT,
                          capture_output=True).returncode == 0 for s in (BEFORE, PREG))
_pred = _git('show', f'{PREG}:{PRED}')
_mod_then = _git('show', f'{PREG}:{MOD}')
_mod_base = _git('show', f'{BEFORE}:{MOD}')
_unrepaired = _mod_then == _mod_base
gate(f'Ⓐ① ⛔⛭⛭ both references are LITERAL SHAs that resolve (`{all(_pres)}`) and are ancestors '
     f'(`{_anc}`), and the module at the pre-registration commit is BYTE-IDENTICAL to the module at '
     f'`{BEFORE}` (`{_unrepaired}`) --- so the blast radius was registered BEFORE a line of the '
     f'repair existed, which is the whole point of registering it',
     all(_pres) and _anc and _unrepaired and len(_pred) > 2000)

_registered = re.search(r'rows the repair RE-OPENS\*\*[^|]*\|\s*\*\*`(\d+)`\*\*', _pred)
_reg_arms = re.search(r'rows whose DANGLING-arm result changes \|\s*\*\*`(\d+)`\*\*', _pred)
_claim = re.findall(r'`(L\d+_[a-z_0-9]+|P\d+_[a-z_]+)` \(`\d+`\)', _pred)
print(f'      registered: re-opens {_registered.group(1) if _registered else "?"}, '
      f'arm changes {_reg_arms.group(1) if _reg_arms else "?"}; '
      f'prefixes claimed in the same commit: {len(_claim)}')
gate(f'Ⓐ② ✔⛭ and its numbers are READ out of that commit --- `{_registered.group(1)}` rows re-opened '
     f'and `{_reg_arms.group(1)}` arm results changed --- together with the `{len(_claim)}` prefixes '
     f'this seat claimed in the same commit under the `r7289` endgame protocol, so the claim and the '
     f'estimate are timestamped by the same push',
     _registered is not None and _reg_arms is not None and len(_claim) == 5)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE COMPARABILITY GUARANTEE, AND THE EXEMPTION NOW CARRIES ITS CONDITIONS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_lits = []
for _c in rows_of(read(BASE)):
    if _c[5].startswith('UNADJUDICATED'):
        continue
    try:
        _lits.append(json.loads(_c[1]))
    except Exception:
        pass
_old = {}
exec(compile(_mod_base, 'dangling_predicate_v2@' + BEFORE, 'exec'), _old)
_moved = collections.Counter()
for _a in ARMS:
    for _l in _lits:
        if _old[_a](_l) != getattr(D, _a)(_l):
            _moved[_a] += 1
print(f'      {len(_lits)} verdicted literals x {len(ARMS)} arms; results that moved: '
      f'{dict(_moved) or "NONE"}')
gate(f'Ⓑ① ⛔⛭⛭⛭ ** THE ARMS DO NOT MOVE: all `{len(ARMS)}` of them return the same value on every one '
     f'of the `{len(_lits)}` verdicted literals, before and after. ** `r7257`\'s and `r7258`\'s '
     f'figures stay reproducible from this file, which is what makes this a repair to the exemption\'s '
     f'SCOPE rather than to the test --- and it is checked against the module read out of git at '
     f'`{BEFORE}`, not against a memory of it',
     not _moved and len(_lits) > 2000)

try:
    D.names_own_subject_by_determiner('that sector can be specified, and is obstructed twice')
    _raises = False
except TypeError as _e:
    _raises = '78th member' in str(_e) or 'subject-test' in str(_e)
_demo = D.names_own_subject_by_determiner('a symmetry-breaking modulus is the adjustable parameter',
                                          within='leading-dangling-arm')
_wide = D.names_own_subject('a symmetry-breaking modulus is the adjustable parameter')
_one_diff = (D._DET_SCOPE['leading-dangling-arm'] is not D._DET_SCOPE['subject-test']
             and D.names_own_subject_by_determiner.__wrapped__ is None
             if hasattr(D.names_own_subject_by_determiner, '__wrapped__') else True)
print(f'      a scope-less call raises: {_raises}; the same span reads {_demo} in the arm scope and '
      f'{_wide} in the subject scope')
gate(f'Ⓑ② ⛔⛭⛭ the exemption CARRIES ITS CONDITIONS: a call that does not name the test it is used '
     f'inside RAISES at the caller\'s own site (`{_raises}`) instead of returning a wrong answer at '
     f'ours, and the two scopes differ in their determiner class and nothing else --- the same span '
     f'reads `{_demo}` for the dangling arm and `{_wide}` for a subject test.  ** Not a flag with a '
     f'default, because a default is how a borrower inherits a defect silently --- which is this '
     f'defect again, one call deep **',
     _raises and _demo is False and _wide is True)

# ⛔⛭⛭ THE PROPERTY, NOT THE FORM.  The first version of this gate grepped the module's source for a
#   literal line, which MINTED A QUOTE-PIN KEY on this seat's own file -- the r7271 family again, in a
#   gate written in the revision that is repairing an instance of it.  ** The claim is that the
#   conditions are written ONCE and both scopes route through them, and that is BEHAVIOUR: stub the
#   private predicate and both public entry points must change together. **
_stub_calls = []


def _stub(lit, head_re):
    _stub_calls.append(head_re)
    return True


_real = D._subject_by_determiner
try:
    D._subject_by_determiner = _stub
    _via_arm = D.names_own_subject_by_determiner('nothing here', within='leading-dangling-arm')
    _via_subj = D.names_own_subject('nothing here')
finally:
    D._subject_by_determiner = _real
_both_route = _via_arm is True and _via_subj is True and len(_stub_calls) == 2
_classes_differ = _stub_calls[0] is not _stub_calls[1] if len(_stub_calls) == 2 else False
print(f'      both entry points routed through the one predicate: {_both_route}; and they handed it '
      f'DIFFERENT determiner classes: {_classes_differ}')
gate(f'Ⓑ③ ✔⛭⛭ and the conditions are written ONCE, shown by BEHAVIOUR rather than by grepping a line '
     f'of source: stubbing the private predicate changes BOTH public entry points '
     f'(`{_both_route}`) and each hands it a DIFFERENT determiner class (`{_classes_differ}`).  '
     f'** So a repair to the conditions reaches both scopes and the two can differ in the class and '
     f'in nothing else --- and this gate asserts that property instead of pinning the line that '
     f'implements it, which is the class this revision is repairing **',
     _both_route and _classes_differ)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE MEASURED BLAST RADIUS: FOUR ROWS TOUCHED, NO VERDICT CHANGED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rows = [c for c in rows_of(read(BASE)) if not c[5].startswith('UNADJUDICATED')]
_newly = []
for _c in _rows:
    try:
        _l = json.loads(_c[1])
    except Exception:
        continue
    if (D.names_own_subject(_l)
            and not D.names_own_subject_by_determiner(_l, within='leading-dangling-arm')):
        _newly.append((_c, _l))
_ro = [(c, l) for c, l in _newly if c[5] == 'REPAIR-OWED']
# a row is RE-OPENED only if no arm fires AND its stated ground is the subject rule
# ⌗ the grounds as the LEDGER states them, in the order a reason states them: the SUBJECT-RULE
#   pattern is first, because the only question this gate asks is whether any newly-exempt row rests
#   on the arm the repair changes.  A row matching nothing is a reason that does not name its ground,
#   which would itself be a finding -- so the census asserts there are none rather than ignoring them.
_GROUND = [('SUBJECT-RULE', r'no subject inside|FRAGMENT with no subject|subject is outside it'),
           ('TRAILING', r'trailing|ends on|ends `|DANGLING PREPOSITION'),
           ('PROXY', r'\bPROXY\b'), ('CANNOT-FAIL/ALT', r'CANNOT FAIL|never decides'),
           ('REDUNDANT-or-GRAIN', r'REDUNDANT|GRAIN-MOVE|limb two|word-align|same defect twice'),
           ('MARKUP', r'MARKUP CARRIER|markup'), ('OPENNESS', r'OPENNESS MARKER|pin fires when'),
           ('CO-OCCURRENCE', r'CO-OCCURRENCE'), ('MULTI-SITE', r'MULTI-SITE|pin on the FILE'),
           ('HISTORICAL-STATE', r'pin the historical state|assert the CURRENT state'),
           ('BUNDLED-CONSEQUENT', r'consequent it bundles|is its consequence'),
           ('ADOPTION-OWED', r'owed work is to adopt')]
_by_ground = collections.Counter()
_subject_only = []
for _c, _l in _ro:
    _g = [n for n, p in _GROUND if re.search(p, _c[6] or '', re.I)]
    _by_ground[_g[0] if _g else 'UNCLASSIFIED'] += 1
    if _g and _g[0] == 'SUBJECT-RULE' and not D.dangles(_l):
        _subject_only.append((_c, _l))
print(f'      newly exempt under the subject scope: {len(_newly)} verdicted rows, of which '
      f'{len(_ro)} are REPAIR-OWED')
print('      their grounds: ' + ', '.join(f'{k} {v}' for k, v in sorted(_by_ground.items())))
print(f'      rows whose REPAIR-OWED ground was the SUBJECT RULE and on which no other arm fires: '
      f'{len(_subject_only)}')
gate(f'Ⓒ① ⛭⛭⛭ ** THE REPAIR RE-OPENS NOTHING: of the `{len(_ro)}` newly-exempt `REPAIR-OWED` '
     f'rows, `{len(_subject_only)}` lose their ground --- against a pre-registered '
     f'`{_registered.group(1)}` ** --- and the registration was an OVER-count rather than an under: '
     f'its filter matched the word `dangling` in a reason, and the TRAILING arm\'s reasons carry that '
     f'word too.  ** Read per row, every one of these rests on a ground the subject rule never '
     f'touched --- several of them say `dangle: none` in the verdicter\'s own words **',
     len(_subject_only) == 0)

print('      grounds, read out of the reasons: ' +
      ', '.join(f'{k} {v}' for k, v in sorted(_by_ground.items())))
gate(f'Ⓒ② ⛔⛭⛭ and the grounds are read OUT OF THE REASONS rather than assumed, and every one of '
     f'the `{len(_ro)}` rows is accounted for with `{_by_ground["UNCLASSIFIED"]}` unclassified --- '
     f'`{_by_ground["SUBJECT-RULE"]}` on the subject rule, the rest on the TRAILING arm, a `PROXY`, '
     f'an undeciding `ALT`, redundancy or grain, markup, an openness marker, a multi-site pin, a '
     f'historical state or a bundled consequent.  ** The ledger records WHY, and a recorded ground is '
     f'what makes a blast radius measurable instead of guessable --- a reason that named no ground '
     f'would be a finding of its own and there are none **',
     sum(_by_ground.values()) == len(_ro) and _by_ground['UNCLASSIFIED'] == 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  WHY IT SURVIVED FOUR REVISIONS, AND WHAT WIDENING THE CLASS EXPOSED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_second = [(c, l) for c, l in _ro if D.dangles(l)]
print(f'      of the {len(_ro)} REPAIR-OWED rows, {len(_second)} still dangle on another arm and '
      f'{len(_ro) - len(_second)} are held by a non-arm ground')
gate(f'Ⓓ① ⛭⛭⛭ ** THE FINDING, AND IT IS NOT THE ONE THE ORDER EXPECTED: a defect in an EXEMPTION is '
     f'invisible wherever the verdict has a SECOND GROUND, and visible exactly where the arm is used '
     f'ALONE as a selector. ** *Every one of these `{len(_ro)}` rows is held by another arm or by a '
     f'narrower-than-claim ground, so the defect moved none of them.*  ⇒ *** It changed outcomes in '
     f'ONE place --- `r7285`\'s `38`-list, where the subject arm WAS the selector and nothing else '
     f'had to agree with it.  An instrument used to SELECT has no second ground to hide behind, which '
     f'is why a list is a harsher test of an arm than a ledger is ***',
     len(_ro) >= 4 and len(_subject_only) == 0)

# ⛔⛭⛭⛭ AND MEASURING THE RADIUS BEFORE LANDING DID NOT ONLY PRICE THE REPAIR -- IT FOUND A DEFECT
#   IN IT.  The wide class reaches `a harmonic oscillator, whose Hamiltonian is bounded below`, which
#   P10 writes as an APPOSITION inside `that sector is ..., a harmonic oscillator, whose ...`: its
#   subject sits OUTSIDE the span and header ⓸ rules it dangling.  ** That is the ONE row among the
#   newly-exempt whose verdict rests on the subject rule, so without a fourth condition the repair
#   would have broken exactly the row it must not. **
_APPOS = 'a harmonic oscillator, whose Hamiltonian is bounded below'
_RESTRICTIVE = 'a consistency check that matches nothing is green forever'
_appos_ok = not D.names_own_subject(_APPOS)
_restrictive_ok = D.names_own_subject(_RESTRICTIVE)
print(f'      the appositive is NOT read as naming its subject: {_appos_ok}; the restrictive '
      f'relative still is: {_restrictive_ok}')
gate(f'Ⓓ② ⛔⛭⛭⛭ ** AND THE WIDE CLASS NEEDED A FOURTH CONDITION THE NARROW ONE NEVER DID, found by '
     f'measuring this repair\'s own radius BEFORE landing it: ** an apposition whose head sits outside '
     f'the span is not a subject (`{_appos_ok}`), and the discriminator is the COMMA rather than the '
     f'relative pronoun --- `a consistency check THAT matches nothing is green forever` is '
     f'restrictive, has no comma, and does name its subject (`{_restrictive_ok}`).  ⇒ *** So pricing '
     f'a repair before landing it found a defect IN the repair, on the one row of the `{len(_ro)}` '
     f'whose verdict rests on the arm being changed ***',
     _appos_ok and _restrictive_ok)

#: ⌗ and ONE weakness is reported and NOT repaired: `THE COST, NAMED` passes because `named` sits in
#:   the closed FINITE list, which cannot tell a finite verb from a past participle in a title.  Its
#:   verdict does not change -- it is a PROXY -- and a second repair inside one revision is how a
#:   measurement stops being one.
_participle = D.names_own_subject('THE COST, NAMED')
_fin_has = bool(re.search(r'\bnamed\b', D.FINITE, re.I))
print(f'      reported and not repaired: `THE COST, NAMED` passes ({_participle}) because `named` is '
      f'in the closed FINITE list ({_fin_has})')
gate(f'Ⓓ③ ⛭⛭ and one weakness is REPORTED AND NOT REPAIRED, which is the scope discipline rather '
     f'than an omission: `THE COST, NAMED` passes the widened test (`{_participle}`) because `named` '
     f'sits in the closed `FINITE` list (`{_fin_has}`), which cannot tell a finite verb from a PAST '
     f'PARTICIPLE in a title.  ** Its verdict does not change --- it is a `PROXY` --- the order asked '
     f'for the exemption\'s scope, and a second repair inside one revision is how a measurement stops '
     f'being one **',
     _participle and _fin_has)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE ONE CORRECTION THAT IS THIS SEAT\'S, AND THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_mine = [(c, l) for c, l in _ro
         if 'r7288+60' in (c[6] or '') and 'RE-STATED r7294+60' in (c[6] or '')]
print(f'      rows whose ground this revision corrected: {len(_mine)}')
gate(f'Ⓔ① ⛭⛭ the one correction that is this seat\'s own: `{len(_mine)}` row carried `r7288`\'s '
     f'reason that it is `a FRAGMENT with no subject inside it`, and it names its subject with a '
     f'determiner --- ** the defect this seat MEASURED at `r7288` had caught this seat too, in the '
     f'same batch. ** The verdict stands because the TRAILING arm fires on it; the ground is '
     f're-stated by APPEND, keeping the original stamp as `r7253` requires',
     len(_mine) == 1)

_touched = sorted({f for f in (_git('diff', '--name-only', PREG) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
#: ⛔⛭ r7298+60: the first form of this gate ALSO required that no receipt but its own appear in the
#: diff --- a claim about the diff's FORM beside the claim it means, and the diff range is live, so
#: `r7298` legitimately repairing other receipts of this seat's turned it red.  ** The specific
#: negative is the whole claim: none of the receipts whose rows this repair touches was edited. **
_subjects = sorted({c[0] for c, _l in _ro})
_touched_subjects = [f for f in _touched if f in _subjects]
print(f'      the {len(_ro)} touched rows live in {len(_subjects)} receipts; this revision edited '
      f'{len(_touched_subjects)} of them')
gate(f'Ⓔ② ⛭⛭ the restraint, as the SPECIFIC NEGATIVE and nothing beside it: the '
     f'`{len(_ro)}` rows the repair touches live in `{len(_subjects)}` receipts and this revision '
     f'edited `{len(_touched_subjects)}` of them, while the module and the ledger ARE in the diff --- '
     f'because a re-statement is a row and not an edit to the gate it describes.  ** The first form of '
     f'this gate also demanded that no OTHER receipt appear in the diff, which is a claim about the '
     f'diff rather than about the restraint, and a later revision repairing this seat\'s own receipts '
     f'turned it red **',
     BASE in _touched and MOD in _touched and not _touched_subjects)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** THE REPAIR RE-OPENS NOTHING: {len(_ro)} verdicted rows are touched and {len(_subject_only)} verdicts change,
     against a pre-registered {_registered.group(1)}. ** The registration was an OVER-count: its filter matched
     the word `dangling`, and the trailing arm's reasons carry that word too.
  ⛔ ** AND THAT IS THE FINDING: a defect in an EXEMPTION is invisible wherever the verdict has a
     SECOND GROUND, and visible exactly where the arm is used ALONE as a selector. **
     It changed outcomes in one place -- the 38-list, where the subject arm WAS the selector.
     An instrument used to SELECT has no second ground to hide behind.
  ⛔ ** And widening the class exposed what the narrow one hid: `THE COST, NAMED` passes the subject
     test because `named` is in the closed FINITE list. ** Reported, not repaired -- its verdict
     does not change, and a second repair inside one revision is how a measurement stops being one.
  ✔ The arms do not move: {len(ARMS)} arms x {len(_lits)} verdicted literals, not one result changed.
""")
sys.exit(1 if FAILURES else 0)
