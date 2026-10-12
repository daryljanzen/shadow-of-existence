#!/usr/bin/env python3
r"""S23 -- the `r7265` order's four items, worked; and the one shape that runs through all of them.

** WHAT `r7265` ORDERED. **  *** ① the absence guard whose COUNTER has no control, one site, taken
after five cycles on the owed list.  ② the fourth dangling arm as a PART-OF-SPEECH test, the closed
list kept byte-for-byte and the cell reported both ways.  ③ `N1`'s two rows and the count.  ④ `P16`'s
monodromy sign where it is a contradiction, the magnitudes left. ***

** ⛔⛭⛭⛭ AND THE SHAPE THAT RUNS THROUGH ALL FOUR, WHICH IS THIS REVISION'S RESULT. **  *Every item
was MIS-DESCRIBED -- three of them by the order, one by this line's own reply for five cycles -- and
in each case the instrument that would have caught it had stored a SNAPSHOT OF A RULE INSTEAD OF THE
RULE.*
  ⇒ *** A gate that stores the state a rule had reached, rather than the rule, goes red the day the
      rule's reach changes -- and the change is usually THE WORK SUCCEEDING. ***
  ⌗ ** FIVE INSTANCES IN THIS ONE REVISION, each named in section Ⓕ: ** *`S19`'s five routed
    remainders (asserted as still owed, discharged by the routing working); `S21`'s and `S22`'s
    reference commit (`merge-base HEAD origin/main`, which collapses onto `HEAD` the moment the work
    merges); `S22`'s revision selector (`git log --grep`, which searches the BODY, so a later commit
    MENTIONING this revision pulled its files in); and `P03`'s ownership clause (a list of the two
    prefixes the ownership rule had reached at `r7222`, which an ORDER widened).*
  ⛔ ** AND A SIXTH, WHICH IS THIS RECEIPT'S OWN GATE AGAINST THE SHAPE. **  *`Ⓕ①` asked whether
    both repaired receipts carried `BEFORE = '` -- the identifier MY repair happened to choose.  `66`
    repaired the same defect independently in the same cycle, one turn further, and the trunk's
    spelling (`BASE_SHA`, `REV_TIP`) came in at the merge: the gate went red ON THE WORK SUCCEEDING,
    which is the sentence above reaching the instrument that wrote it.*
  ⇒ *** It is rewritten to the property -- a constant bound to a literal sha that RESOLVES and is an
      ANCESTOR of `HEAD` -- which both spellings satisfy and no moving ref does. ***
  ⛔ ** AND THEN THE OTHER TWO WENT THE SAME WAY, WHICH IS WHY IT IS THE SECTION AND NOT THE GATE. **
    *`r7267` repaired all three subjects on the trunk, and `Ⓕ②` and `Ⓕ③` failed on the merge for the
    same reason `Ⓕ①` did: `Ⓕ②` asked for the ABSENCE of `--grep`, so it called the trunk's better
    selector -- the range's start named by the pre-registration's subject -- the defect; `Ⓕ③` asked
    for the parity predicate THIS SEAT wrote, which `66` reversed with a reason that holds.*
  ⇒⇒ *** SO THE RULE IS ABOUT THE WHOLE CLASS: a gate that asserts a REPAIR LANDED has as its subject
      a thing another seat may legitimately rewrite, so it must assert the repair's PROPERTY and
      never its form.  The three properties are in `r7268`'s receipt, with a control each. ***

** ⛭⛭ ① `one site` WAS NEVER MEASURED, AND IT IS RIGHT BY ACCIDENT. **  *Five cuts of the instrument
on one tree: `65`, `20`, `8`, `7`, `4` receipts.  The number is a function of where the instrument
draws TWO boundaries -- what counts as a FOREIGN HAYSTACK and what counts as a POSITIVE CONTROL --
and `r7246`'s proxy (`any non-zero counter assertion anywhere in the file`) defined neither.*
  ⇒ *** `78` sites, `72` controlled, `6` bare -- and `one site` is right read as ONE SITE THIS SEAT
      MAY REPAIR, which is what five cycles of the reply have meant without saying it. ***
  ⌗ *The fifth cut is the one that matters: a NON-EMPTINESS guard is the STRONGEST control of the
    three forms -- `bool(hay)` excludes the empty read directly where an `in` excludes it only by
    implying it -- and the first four cuts counted every one of them as absent.*

** ⛭⛭ ② ONE DISTRIBUTIONAL AXIS WAS NOT ENOUGH, AND THE ARM REFUTED ITS OWN FIRST CUT. **  *Verbs are
an OPEN class and determiners a CLOSED one, so the arm tests the open class by its distribution
against the closed one -- the only list it carries is the one that can be finished.*
  ⛔ *But a low determiner-BEFORE ratio says `not a noun`, which is not `a verb`: the first run's
    widening carried formula heads, three adverbs, a negator, a subordinator and two numerals.*
  ⇒ *** So the arm carries a SECOND axis -- a verb is also often FOLLOWED by a determiner -- and a
      word is verb-like only on both.  The two tests are NOT NESTED: the closed list catches spans
      opening on a FUNCTION WORD and this arm catches spans opening on a TRANSITIVE VERB. ***
  ✔ *The order's threshold was fixed before the arm existed, at `4` keys wider.  Measured `12` raw;
    read by hand with the reason published per key, `8` true and `4` the arm's own false positives.*
    ** So the negative does not fire -- by `5` and not by `9`, and that is the number. **

** ⛭ ③ `N1` IS SEVEN EDITS AND NOT THREE. **  *The count is stated in FOUR places, and the fifth edit
is a dependency the order does not name: the body's statement of the Weyl-squared coefficient ended
`which the frontier table records`, a pointer the row's removal would have broken silently.*
  ✔ *And the paper's own rule is satisfied rather than bypassed -- `an item that leaves a list by
    reclassification rather than by being worked has not been closed` -- because both were worked.*

** ⛭ ④ THE SIGN IS WRONG IN THREE PLACES AND NOT TWO. **  *A census of every signed form, after
repairing the two the order names, found a third writing the off-diagonal for both sectors with its
imaginary unit and no sign.  The two MAGNITUDES are left exactly as the order rules.*

⛔ *Sources: `r7265`'s four items; `PREDICTION.md`, pushed before any item was worked; the instrument
and its five cuts in `find_bare_absence.py`; the arm and its calibration in `pos_arm.py`; the hand
reading in `WIDENING_HAND.tsv`; `P18` and `P16` at a literal reference commit and after; and
`L-249`'s rule at `r3105`, which is what every one of the snapshot gates needed.*
"""

import hashlib
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7266_60_the_arm_and_the_guard')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))
sys.path.insert(0, WORK)

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED arms, byte-for-byte
import pos_arm as POS                      # noqa: E402  the fourth arm this revision builds

CHECKS = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


# ⛔⛭⛭ THE REFERENCE COMMIT IS A LITERAL SHA.  *`r7262`'s and `r7264`'s receipts pinned
#   `merge-base HEAD origin/main`, which collapses onto `HEAD` the moment the work merges, and one of
#   them went red on `main` for exactly that.  **A historical pin computed against a moving ref is not
#   a historical pin**, and this receipt does not repeat it.
BEFORE = '4b8be176'      # r7266's pre-registration, before any of the four items was worked


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True).stdout


def at_before(rel):
    r = subprocess.run(['git', 'show', f'{BEFORE}:{rel}'], cwd=ROOT,
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def flat(t):
    return re.sub(r'\s+', ' ', t or '')


def run(rel, *args):
    return subprocess.run([sys.executable, os.path.join(ROOT, rel)] + list(args),
                          cwd=ROOT, capture_output=True, text=True, timeout=1800)


P18, P16 = 'corpus/CR_synthesis.tex', 'corpus/cosmogenesis_paper.tex'
p18, p18b = flat(read(P18)), flat(at_before(P18))
p16, p16b = flat(read(P16)), flat(at_before(P16))

print()
print('=' * 100)
print('S23 -- the r7265 order, four items, and the six gates that stored a snapshot of a rule')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE REFERENCE COMMIT, ASSERTED BEFORE ANYTHING IS READ THROUGH IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res = _git('cat-file', '-t', BEFORE).strip() == 'commit'
_anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'],
                      cwd=ROOT, capture_output=True, text=True).returncode == 0
gate(f'Ⓐ① ⛔⛭⛭ the reference is a LITERAL SHA, it resolves, it is an ancestor of `HEAD`, and both '
     f'papers come back from it DIFFERING from the working tree.  ** Without the literal the pin '
     f'collapses onto `HEAD` on merge and every gate below compares a tree with itself -- which is '
     f'what put a receipt of this line RED ON `main` this cycle **',
     _res and _anc and p18b and p16b and p18b != p18 and p16b != p16)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  ① THE OWED ITEM WAS NEVER MEASURED, AND THE NUMBER IS THE INSTRUMENT\'S ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_bare = run('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/find_bare_absence.py')
_m = re.search(r'absence-guard sites: (\d+) \((\d+) controlled[^,]*, (\d+) BARE\)', _bare.stdout)
gate('Ⓑ① ⛭ the instrument RUNS here rather than being cited, and reports its three counts',
     _bare.returncode == 0 and _m is not None)
_tot, _ctl, _bar = (int(_m.group(1)), int(_m.group(2)), int(_m.group(3))) if _m else (0, 0, 0)
gate(f'Ⓑ② ⛔ `{_tot}` absence-guard sites on PAPER haystacks, `{_ctl}` controlled on the same '
     f'haystack, `{_bar}` BARE --- against an owed item that has read `one site` in every reply '
     f'since `r7246`',
     _tot >= 70 and _ctl >= 70 and _bar == _tot - _ctl)

_rec = read('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/bare_absence.txt')
# ⛭ *the published table is PARSED rather than quoted phrase by phrase: five rows, each a cut with a
#   receipt count, and the counts must DESCEND -- which is the claim.*
_CUT = re.compile(r'^\s+\d\s{3,}(\S.*?)\s{2,}(\d+)\s', re.M)
_cuts = [(m.group(1).strip(), int(m.group(2))) for m in _CUT.finditer(_rec)]
gate(f'Ⓑ③ ⛔⛭⛭⛭ AND THE FIVE CUTS ARE PUBLISHED AS A TABLE WITH THEIR COUNTS, so `the figure was '
     f'never measured` is checkable rather than asserted --- `{[c for _, c in _cuts]}` receipts on '
     f'ONE tree, differing only in where the instrument drew its two boundaries, and **the counts '
     f'DESCEND at every cut**',
     len(_cuts) == 5 and [c for _, c in _cuts] == sorted((c for _, c in _cuts), reverse=True)
     and _cuts[0][1] == 65 and _cuts[-1][1] == 4)

gate('Ⓑ④ ⛭⛭ and the FIFTH cut is the one that matters, which is stated as the reason and not as a '
     'step: a non-emptiness guard excludes the empty read DIRECTLY where an `in` excludes it only by '
     'implying it, so it is the STRONGEST of the three control forms and the first four cuts counted '
     'every one of them as absent',
     'STRONGEST control' in _rec and 'bool(hay)' in _rec)

_K_COUNTER = ("READ OFF A PAPER SHOWN TO BE PRESENT: the file is non-empty and still carries its own")
_n1 = ('receipts/L251_the_numbering_collides/'
       'N1_two_lines_numbering_from_one_counter_and_a_paper_narrating_its_own_history.py')
gate('Ⓑ⑤ ✔ the ONE site this seat may repair is repaired, and the counter is the file\'s own '
     'identity rather than another sentence --- so the gate can tell `the phrase is gone` from `the '
     'paper is gone`, which is the whole class',
     _K_COUNTER in read(_n1) and _K_COUNTER not in (at_before(_n1) or ''))

_n1run = run(_n1)
gate(f'Ⓑ⑥ ✔ and the repaired receipt RUNS (exit `{_n1run.returncode}`), asserted by running it',
     _n1run.returncode == 0)

gate('Ⓑ⑦ ⌗ and the `6` that remain are in `3` receipts whose introducing commits carry NO revision '
     'id, under an ownership ruling this line routed at `r7258` and that was never ratified --- so '
     'they are named and not touched',
     'UNATTRIBUTED' in _rec and 'never ratified' in _rec)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  ② THE ARM, ITS TWO AXES, AND THE ORDER\'S THRESHOLD ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_ADOPTED = 'computations/beyond_the_wall/r7260_60_land_and_verdict/dangling_predicate_v2.py'
_h_now = hashlib.sha256(read(_ADOPTED).encode()).hexdigest()
_h_then = hashlib.sha256((at_before(_ADOPTED) or '').encode()).hexdigest()
gate(f'Ⓒ① ⛭⛭ THE BURDEN IS DISCHARGED BY HASH AND NOT BY INTENTION: the adopted word list is '
     f'BYTE-FOR-BYTE what it was, so `r7257`\'s and `r7258`\'s figures stay reproducible from it '
     f'(`{_h_now[:16]}`)',
     _h_now == _h_then)

_arm = run('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/pos_arm.py')
_a1 = re.search(r'axis ONE.*?verbs ([\d.]+) vs nouns ([\d.]+)', _arm.stdout)
_a2 = re.search(r'axis TWO.*?verbs ([\d.]+) vs nouns ([\d.]+)', _arm.stdout)
gate('Ⓒ② ⛭ the arm RUNS here and reports BOTH axes with their calibrations, on control sets drawn '
     'from the corpus rather than hand-picked --- known verbs on one side, words following a '
     'determiner on the other',
     _arm.returncode == 0 and _a1 and _a2
     and float(_a1.group(2)) > float(_a1.group(1))        # nouns above verbs on axis one
     and float(_a2.group(1)) > float(_a2.group(2)))       # verbs above nouns on axis two

def _num(pat):
    m = re.search(pat + r'[^\n:]*:\s*(\d+)', _arm.stdout)
    return int(m.group(1)) if m else None


_pop = (_num(r'the THREE ADOPTED ARMS flag'), _num(r'the PART-OF-SPEECH arm flags'),
        _num(r'part-of-speech ONLY'), _num(r'closed-list ONLY'))
gate(f'Ⓒ③ ⛔⛭⛭ AND THE TWO TESTS ARE NOT NESTED, which is the finding and not a caveat: on the SAME '
     f'`163` keys the adopted arms flag `{_pop[0]}` and this one `{_pop[1]}`, with `{_pop[2]}` the '
     f'closed list misses and `{_pop[3]}` the other way.  ** The closed list catches a FUNCTION-WORD '
     f'head and this arm a TRANSITIVE-VERB head; the class is the union **',
     all(x is not None for x in _pop) and _pop[2] > 0 and _pop[3] > 0)

_hand = read('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/WIDENING_HAND.tsv')
_rows = [l.split('\t') for l in _hand.split('\n') if l and not l.startswith('#')]
_true = [r for r in _rows if r[0] == 'TRUE']
_false = [r for r in _rows if r[0] == 'FALSE']
gate(f'Ⓒ④ ⛭⛭ the widening is read BY HAND with the reason published per key, so the count can be '
     f'disputed without redoing the pass: `{len(_true)}` true and `{len(_false)}` the arm\'s own '
     f'false positives, every row carrying its why',
     len(_true) + len(_false) == len(_rows) and len(_rows) >= 12
     and all(len(r) >= 4 and len(r[3]) > 30 for r in _rows))

gate(f'Ⓒ⑤ ✔⛔ AND THE ORDER\'S REACHABLE NEGATIVE DOES NOT FIRE, BY `{len(_true) - 3}` AND NOT BY '
     f'`{_pop[2] - 3}`: the threshold was `4` keys wider than the closed '
     f'list, fixed in the pushed pre-registration before the arm existed, and the honest count is '
     f'the HAND one.  *Reported at the tighter number, because the raw `12` includes four the arm '
     f'itself gets wrong*',
     len(_true) >= 4
     and 'must flag at least `4` keys the closed' in
     read('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/PREDICTION.md'))

gate('Ⓒ⑥ ⛔⛭ and THREE of the eight are negated predicate fragments the ADOPTED NEGATOR ARM MISSES, '
     'because it strips the `not` and then tests the remainder against the same closed list --- so '
     'the closed list\'s shortfall reaches inside an arm built to extend it',
     sum(1 for r in _true if r[2] == 'not') == 3
     and not D.dangles('not a debt') and POS.dangles_pos('not a debt'))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  ③ `N1` IS SEVEN EDITS, AND THE FIFTH WAS A POINTER THAT WOULD HAVE BROKEN SILENTLY ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_ROW_A = 'the mode sums beyond the free static case &'
_ROW_B = 'the Weyl-squared coefficient at second order in the shear &'
gate('Ⓓ① ⛔ both rows stood in the open table at the reference commit and are gone now --- asserted '
     'as a before-and-after on the rows themselves',
     _ROW_A in p18b and _ROW_B in p18b and _ROW_A not in p18 and _ROW_B not in p18)

_COUNTS = ['Seven items stand open', 'Seven open items stand against roughly',
           '\\subsection{The seven, with what would discharge each}',
           'lists the seven open items in full']
gate(f'Ⓓ② ⛭⛭ and the count is stated in FOUR places, not one --- all four carried and all four '
     f'moved, which is why the order\'s `two edits and the count` is `{4 + 2 + 1}` edits in one unit',
     all(c in p18 for c in _COUNTS)
     and all(c.replace('Seven', 'Nine').replace('seven', 'nine') in p18b for c in _COUNTS))

_PTR_OLD = 'on the physical-mode count---which the frontier table records'
_PTR_NEW = 'on the physical-mode count, \\emph{stated and reversible on its scoping}'
gate('Ⓓ③ ⛔⛭⛭ AND THE FIFTH EDIT IS THE ONE THE ORDER DOES NOT NAME: the body pointed AT the row it '
     'was about to lose, and the row\'s own caveat is carried into the body so nothing is lost with '
     'it.  ** A pointer into a table is a pin into a thing that moves **',
     _PTR_OLD in p18b and _PTR_OLD not in p18 and _PTR_NEW in p18)

_RULE = ('an item that leaves a list by reclassification rather than by being worked has not been '
         'closed')
gate('Ⓓ④ ✔⛭ and the paper\'s OWN rule is satisfied rather than bypassed --- it is still there, and '
     'both items left by having been WORKED: the mode sums by the construction\'s own regulator with '
     'the counterterm computed, the Weyl-squared coefficient by being stated with its value',
     _RULE in p18 and _RULE in p18b
     and 'ultraviolet definition of the mode sums} is settled beyond the free static case' in p18)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  ④ THE SIGN IS WRONG IN THREE PLACES, AND THE MAGNITUDES ARE LEFT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_signed = re.findall(r'\$-[24]\\pi i/\\rho\$', p16)
_unsigned = re.findall(r'[^-]\$[24]\\pi i/\\rho\$', p16)
_unsigned_b = re.findall(r'[^-]\$[24]\\pi i/\\rho\$', p16b)
gate(f'Ⓔ① ⛔⛭ EVERY signed occurrence now carries the minus --- `{len(_signed)}` of them --- and '
     f'`{len(_unsigned_b)}` stood unsigned at the reference commit against `{len(_unsigned)}` now, '
     f'which is `{len(_unsigned_b) // 2}` SITES at two forms each.  ** The order names TWO sites; a '
     f'census of every signed form found a THIRD **',
     len(_signed) == 8 and len(_unsigned) == 0 and len(_unsigned_b) == 6)

gate('Ⓔ② ✔ and the two MAGNITUDES are left exactly as the order rules them --- not a contradiction, '
     'so not touched',
     p16.count('$4\\pi/\\rho$') == p16b.count('$4\\pi/\\rho$') == 1
     and p16.count('$2\\pi/\\rho$') == p16b.count('$2\\pi/\\rho$') == 1)

gate('Ⓔ③ ✔⛭ and the one form that was always right is untouched: the off-diagonal written as '
     '`$2\\pi ip$` with `p = -1/\\rho`, which is the minus carried in the variable instead of the '
     'sign --- a census that flagged it would have been the wrong census',
     '$2\\pi ip$' in p16 and '$2\\pi ip$' in p16b)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE SNAPSHOT GATES, EACH WITH ITS SNAPSHOT GONE AND ITS RULE IN PLACE -- AND THE '
      'SIXTH IS Ⓕ① ITSELF ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_S21 = ('receipts/L_probability/S21_a_pre_registered_negative_can_fire_without_reaching_the_claim_it_'
        'was_written_to_test_and_mine_did_while_the_order_was_wrong_about_both_defects_in_opposite_'
        'directions.py')
_S22 = ('receipts/L_probability/S22_the_sentence_over_reached_and_the_receipt_cited_on_it_under_'
        'reached_so_the_rcpt_convention_was_violated_at_a_site_where_nothing_could_fail.py')
_P03 = ('receipts/P03_SdS_slicing/P03_the_enclosed_mass_is_monotone_so_the_turnaround_ratio_cannot_'
        'fall_below_one_and_the_contested_direction_is_two_different_quantities.py')
_s21, _s22, _p03 = read(_S21), read(_S22), read(_P03)
# ⛔⛭⛭⛭ THE SIXTH INSTANCE OF THIS REVISION'S OWN SHAPE, AND THE GATE THAT CARRIED IT IS THIS
#   ONE.  *Ⓕ①'s first form asked whether both repaired receipts carried `BEFORE = '` -- THE IDENTIFIER
#   THIS SEAT'S REPAIR HAPPENED TO CHOOSE.  `66` repaired the same defect independently in the same
#   cycle and carried it one turn further -- `BASE_SHA..REV_TIP`, a RANGE where mine pinned a point,
#   because a base-to-working-tree diff on a merged trunk is every file four seats changed since --
#   and the trunk's spelling came into this branch at the merge.*
#   ⇒ *** So the gate written to catch a stored snapshot of a rule had stored one itself, and it went
#       red on the merge.  THE SNAPSHOT WAS THE VARIABLE'S NAME, and the change that broke it was the
#       work succeeding, which is this revision's result reaching its own instrument. ***
#   ⌗ *Rewritten to the PROPERTY, which is name-agnostic: a module constant bound to a literal hex
#     sha that RESOLVES to a commit and is an ANCESTOR of `HEAD`.  Both repairs satisfy it under two
#     different spellings; a base computed from a moving ref satisfies neither half, and the gate
#     carries a control for each half rather than trusting the regex.*
_SHA_PIN = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*'([0-9a-f]{8,40})'", re.M)
_MOVING = "'merge-base', 'HEAD', 'origin/main'"


def sha_pins(src):
    """every module constant bound to a literal sha that RESOLVES to a commit in this history and is
    an ancestor of HEAD -- a historical pin read by what it IS and not by what it is called."""
    out = []
    for _m in _SHA_PIN.finditer(src):
        _h = _m.group(2)
        if subprocess.run(['git', 'cat-file', '-e', _h + '^{commit}'], cwd=ROOT,
                          capture_output=True).returncode == 0 \
                and subprocess.run(['git', 'merge-base', '--is-ancestor', _h, 'HEAD'],
                                   cwd=ROOT, capture_output=True).returncode == 0:
            out.append(_m.group(1))
    return out


_CTRL_MOVING = "BASE = subprocess.run(['git', 'merge-base', 'HEAD', 'origin/main'])\n"
_CTRL_GONE = "BEFORE = 'deadbeefdeadbeef'\n"
_p21, _p22 = sha_pins(_s21), sha_pins(_s22)
gate(f'Ⓕ① ⛔⛭⛭⛭ the REFERENCE-COMMIT snapshot is gone from both receipts that carried it, and it '
     f'is tested as the PROPERTY rather than as a spelling: neither computes `merge-base HEAD '
     f'origin/main`, and each binds a constant to a literal sha that resolves and is an ancestor of '
     f'`HEAD` --- `{", ".join(_p21) or "none"}` in one and `{", ".join(_p22) or "none"}` in the '
     f'other, TWO SPELLINGS OF ONE PROPERTY.  ** This gate\'s first form asked for the NAME and went '
     f'red when `66`\'s own repair of the same defect replaced mine: the sixth instance of this '
     f'revision\'s shape was this gate **',
     _MOVING not in _s21 and _MOVING not in _s22 and _p21 and _p22
     and _MOVING in _CTRL_MOVING and not sha_pins(_CTRL_MOVING)
     and not sha_pins(_CTRL_GONE))

# ⛔⛭⛭⛭ AND Ⓕ② STORED A FORM TOO, AND THE TRUNK'S OWN REPAIR BROKE IT.  *It asked that
#   neither receipt pass `--grep` to `git log` at all -- the shape MY repair took.  `66` repaired
#   `S22`'s far end and selected the range's START by the pre-registration's SUBJECT, which is better
#   than a bare sha because it says WHAT the start is; the gate called that the defect.*
#   ⇒ *** The rule is not `no --grep`.  It is that a selector must not be satisfiable by a later
#       commit that merely MENTIONS the revision -- so the test is a CENSUS of each selector the two
#       receipts actually use: unique, and matched in the SUBJECT rather than only in a body. ***
_GREPPAT = re.compile(r"'--grep=([^']+)'")


def grep_census(pat):
    """(matches, matches whose SUBJECT does not carry the pattern) -- the second number is the
    defect's own signature, a commit that merely MENTIONS the revision in its message body."""
    _out = subprocess.run(['git', 'log', '--format=%H%x00%s%x00%b%x01', '--grep=' + pat],
                          cwd=ROOT, capture_output=True, text=True).stdout
    _tot = _body = 0
    for _blk in _out.split('\x01'):
        if _blk.count('\x00') >= 2:
            _, _subj, _bod = _blk.split('\x00', 2)
            _tot += 1
            if pat not in _subj and pat in _bod:
                _body += 1
    return _tot, _body


_pats = _GREPPAT.findall(_s21) + _GREPPAT.findall(_s22)
# ⌗ a selector ASSEMBLED AT RUNTIME cannot be censused from the source at all, so it would pass this
#   gate by being invisible to it.  Both kinds are counted and the non-literal kind must be empty.
_built = [_p for _p in _pats if '{' in _p or '}' in _p]
_cens = {_p: grep_census(_p) for _p in _pats if _p not in _built}
_CTRL_PAT = 'r7266'                      # a revision id MENTIONED in bodies as well as in subjects
_ctot, _cbody = grep_census(_CTRL_PAT)
for _p, (_t, _b) in sorted(_cens.items()):
    print(f'      selector `{_p[:52]}`: {_t} match(es), {_b} body-only')
gate(f'Ⓕ② ⛔⛭⛭⛭ the REVISION SELECTOR is sound, tested as the RULE and not as the absence of '
     f'`--grep`: each of the `{len(_cens)}` literal selector(s) the two receipts use matches exactly '
     f'once and '
     f'in the SUBJECT, so no later commit that merely mentions the revision can satisfy it --- and '
     f'the census is CONTROLLED on the same haystack, `{_CTRL_PAT}` giving `{_ctot}` matches of '
     f'which `{_cbody}` are body-only.  ** This gate first asked for the absence of `--grep` '
     f'itself, which called the trunk\'s better selector the defect **',
     all(_t == 1 and _b == 0 for _t, _b in _cens.values()) and not _built
     and _ctot > 1 and _cbody >= 1)

# ⛔⛭⛭⛭ AND SO DID Ⓕ③, AND HERE THE TRUNK WAS RIGHT AND THIS SEAT WAS WRONG.  *It
#   asserted the ownership clause had become a REVISION-PARITY rule -- the repair this seat made --
#   and `66` reversed it with a reason that holds: parity owns every receipt an even revision ever
#   introduced, which RETIRES the restraint claim instead of bounding it.  **Accepted.**  The
#   authorised crossings are carried by name instead, and this gate is rewritten to the property
#   both repairs have to share.*
#   ⇒ *** The property: the predicate must own the receipt THE GATE IS IN.  `P03`'s own path is
#       outside both prefixes, this branch MODIFIED it, and `P03` nevertheless reports ZERO
#       unauthorised crossings --- which cannot be true unless ownership is read by something better
#       than the prefix pair.  No spelling of either repair appears in this gate. ***
_P03_PFX = ('receipts/P15_CR_cosmology/', 'receipts/L_probability/S')
_p03_unowned_by_prefix = not _P03.startswith(_P03_PFX)
# ⌗ against `origin/main` and not `origin/main...HEAD`, so an edit still in the working tree counts:
#   on the branch the restraint's own evidence is uncommitted, which is `66`'s point about the far end.
_p03_touched_here = _P03 in _git('diff', '--name-only', 'origin/main').split('\n')
_r03 = run(_P03)
_p03_zero = '0 UNAUTHORISED modified unowned receipt(s)' in _r03.stdout
gate(f'Ⓕ③ ⛔⛭⛭⛭ and the OWNERSHIP clause is sound, tested as the PROPERTY: the receipt '
     f'the gate lives in is outside both prefixes (`{_p03_unowned_by_prefix}`) and this branch '
     f'MODIFIED it (`{_p03_touched_here}`), and it still reports ZERO unauthorised crossings --- '
     f'which no prefix pair can give.  ** This gate first asserted the parity rule this seat wrote, '
     f'which `66` reversed for retiring the claim rather than bounding it; accepted, and the '
     f'property is what both repairs must share **',
     _p03_unowned_by_prefix and _p03_touched_here and _p03_zero
     and _r03.returncode == 0)

for _nm, _rel in (('S21', _S21), ('S22', _S22), ('P03', _P03)):
    _r = _r03 if _rel is _P03 else run(_rel)      # P03 already ran for Ⓕ③; a trace is not a timing
    gate(f'Ⓕ④{_nm} ✔ and `{_nm}` RUNS GREEN after its repair (exit `{_r.returncode}`), asserted by '
         f'running it here rather than by citing it',
         _r.returncode == 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓖ  THE BANDS, THE STANDING RULES, AND THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PRED = read('computations/beyond_the_wall/r7266_60_the_arm_and_the_guard/PREDICTION.md')
_ROWRE = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROWRE.finditer(_PRED)]
gate(f'Ⓖ① ⛭ the bands are PARSED out of the pushed pre-registration --- `{len(_bands)}` rows',
     len(_bands) == 5 and all(lo <= c <= hi for _, c, lo, hi in _bands))

_MEAS = [_bar, _pop[2], _pop[3], 0, 3]
# ⛭⛭ *The bands are SCORED and the scoring is what is asserted: a band breaking is a FINDING, so a
#   gate that failed on a break would make a broken band unreportable.  The gate below asserts WHICH
#   bands broke, which is falsifiable in both directions.*
_broke = []
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m2 = _MEAS[_i]
    _in = _lo <= _m2 <= _hi
    if not _in:
        _broke.append(_i)
    print(f'      {"✔" if _in and _m2 == _c else "⌗" if _in else "⛔"} {_name.strip()[:62]:62} '
          f'pre-registered {_c} in {_lo}-{_hi}, measured {_m2}'
          + ('' if _in else '   BREAKS'))
gate(f'Ⓖ② ⛭⛭ the five bands are scored and `{len(_broke)}` BREAK, at indices `{_broke}` --- '
     f'asserted as a SET, so a break is reportable rather than a gate failure and a band that broke '
     f'silently would turn this red',
     _broke == [0, 2])

gate(f'Ⓖ③ ⛔⛭⛭ AND THE FIRST BAND BREAKS ABOVE ITS CEILING --- `1` central in `0`–`5`, measured '
     f'`{_bar}` --- which is the reachable negative I set against myself FIRING: the item had been '
     f'on the owed list for five cycles describing a number nobody had measured',
     _bar > 5)

# ⛭⛭ *ONE regex and not a list of eight literals.  **A list of narration phrases is eight quote-pin
#   keys**, each needing a verdict and each describing nothing once the phrase is absent -- so the
#   check is written as the pattern it is, which keys once and says the same thing.*
# ⛔⛭⛭⛭ AND THE REGEX THAT REPLACED THE LIST WAS BROADER THAN THE LIST, WHICH IS THIS REVISION'S OWN
#   FINDING COMMITTED BY ITS OWN AUTHOR IN THE ACT OF AVOIDING A PIN.
#   *The first cut allowed a bare `was stated`, and it matched `the conclusion this chain reaches was
#   stated as a conjecture in the original derivation` -- a true sentence about the SOURCE
#   literature's history and no narration about a repair at all.  The eight-literal list it replaced
#   carried `was formerly stated` and did not match it.*
#     ⇒ *** So a pattern is not a cheaper list; it is a WIDER one, and the widening has to be checked
#         exactly as the narrowing does.  Caught by running it, not by reading it. ***
_NARRATION = re.compile(r'(?:formerly|previously)\s+stated|an earlier (?:revision|version)'
                        r'|corrected from|used to say', re.I)
_CONTROL = 'was formerly stated as a conjecture'
gate('Ⓖ④ ⛭⛭ the one-state rule, in the only form a gate can check: no narration pattern matches '
     'either repaired paper --- and the pattern is CONTROLLED, firing on a sentence written here '
     'that the papers do not contain.  *One pattern rather than eight literals, because a list of '
     'phrases a paper must not contain is a list of pins describing nothing; and narrowed after the '
     'first cut matched a true sentence about the source literature*',
     not _NARRATION.search(p18) and not _NARRATION.search(p16)
     and _NARRATION.search(_CONTROL) and _CONTROL not in p18 and _CONTROL not in p16)

_log = _git('log', '--no-merges', '--format=%H\t%s', BEFORE + '..HEAD').split('\n')
_own = [l.split('\t')[0] for l in _log if '\t' in l and 'r7266' in l.split('\t', 1)[1]]
_changed = sorted({f for sh in _own for f in
                   _git('diff-tree', '--no-commit-id', '--name-only', '-r', sh).split()})
_tex = [f for f in _changed if f.startswith('corpus/') and f.endswith('.tex')
        and not f.startswith('corpus/appendix_')]
gate(f'Ⓖ⑤ ⛭⛭ and the restraint is measured from the `{len(_own)}` commits whose SUBJECT names this '
     f'revision --- `{len(_changed)}` files --- and the only papers among them are the two the order '
     f'names: {sorted(os.path.basename(f) for f in _tex)}',
     sorted(_tex) == sorted([P16, P18]))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = [l for l, ok in CHECKS if not ok]
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print()
print('  ⛔ ** EVERY ONE OF THE FOUR ITEMS WAS MIS-DESCRIBED, and in each case the instrument that')
print('     would have caught it stored a SNAPSHOT OF A RULE instead of the rule: ** six instances')
print('     in one revision, from a routed backlog to a reference commit to a list of prefixes.')
print('  ⓵ ** `one site` was never measured ** -- five cuts gave 65, 20, 8, 7, 4 receipts, and it is')
print('     right only read as `one site this seat may repair`.')
print('  ⓶ ** One distributional axis was not enough ** -- the arm refuted its own first cut, and the')
print('     two tests are not nested: a function-word head against a transitive-verb head.')
print('  ⓷ ** N1 is seven edits ** -- the count is in four places and the body pointed at the row.')
print('  ⓸ ** The sign is wrong in three places ** -- a census found the one the order did not have.')
print()

if _fail:
    raise SystemExit(1)
