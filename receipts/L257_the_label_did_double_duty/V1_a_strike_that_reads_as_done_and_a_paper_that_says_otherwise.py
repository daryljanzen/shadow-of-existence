#!/usr/bin/env python3
"""V1 -- five qualifications in three papers had no verdict in the open ledger, and reading the first
of them turned up a struck register clause whose LABEL contradicts, in terms, the paper it protects.

** ⛭ ⓵ WHAT WAS UNVERDICTED. **  `check_open_ledger` fails when a qualification appears in a paper
and nobody records a reading of it -- *"a grep is not a list of what is owed; it is a list of places
to look, and the looking has to be written down or it does not count."*  ⇒ Five stood open: three in
`P07`, one in `P10`, one in `P14`.

** ⛔⛭⛭ ⓶ AND THE FIRST OF THEM IS A CONTRADICTION IN TERMS WITH A STRUCK ROW. **

  * `P07`'s frontier item: *"only the ultraviolet definition of the mode sums remains open here ...
    ** the shared character of the wall does not settle it ** ... the latter is a genuine open
    frontier of the programme's quantum sector, carried as such and to be worked."*
  * `PO-6`, ** STRUCK r3001 **, clause ③: *"** THE UV DEFINITION: MET, NOT OWED ** -- generic to
    every interacting QFT."*

  ⇒ *** Read at face value the row says the shared character DOES settle it and the paper says it
      does not, about the same object, with the strike 582 revisions later than the sentence. ***

** ⌗ ⓷ AND IT IS NOT A DISAGREEMENT -- THE LABEL IS DOING DOUBLE DUTY, which is worse than a
disagreement because nothing marks it. **  `kills/PO-6.md`'s actual argument is that ** CR's SPECIFIC
part ** is bounded to a one-dimensional counterterm basis by conformal flatness -- *"a generic problem
on unusually good terms"*.  ⇒ *** So "NOT OWED" means ** CR adds no burden of its own **, not that the
generic construction exists.  On that reading the strike and the paper agree exactly, and `P10` says
the same thing in the same words: "the standard problem of the interacting theory rather than a
residual freedom in the quantization". ***
  ⇒ ** A THREE-CLAUSE ROW STRUCK AS A WHOLE CARRIES ONE VERDICT WORD PER CLAUSE, and a clause whose
    honest verdict is "not ours" reads, in the strike's grammar, as "done". **

** ⓸ THE OTHER FOUR, AND ONE OF THEM CARRIES ITS OWN LIMIT. **  `P10`'s straddle-as-a-computed-fact
is `NAMED-UNBUILT` -- *and the same sentence says what does not turn on it*: "how the straddle falls
does not bear on the closure below, which is supplied fibre by fibre".  ⇒ ** Both halves are recorded,
because an owed item that is not load-bearing and an owed item that is are different debts. **

WHAT IS NOT CLAIMED.  ** Not that `PO-6`'s strike is wrong ** -- the reconciliation is that it is
right and its clause label is ambiguous; nothing is unstruck.  ** Not that the papers were edited **
-- no `.tex` file is touched by this revision; what is written is the ledger reading.  ** Not that
the `P14` verdict is a reading of `P14` ** -- it rests on this line's own `PO-14` work at r3099, the
grounds are given in the entry, and it is marked so it can be overturned in one step.  ** And not
that the ledger's WARN backlog is addressed ** -- six entries name sentences no longer in any paper,
which `--rebuild` would re-derive, and rebuilding is not this revision's business.

    python3 receipts/L257_the_label_did_double_duty/V1_a_strike_that_reads_as_done_and_a_paper_that_says_otherwise.py

Written r3130, `L-257`.  Stated for reversal.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = '74555e6d'          # r3128 -- before this revision's ledger entries
FIVE = {'114e4d9ede': ('CR_framework', 'NAMED-UNBUILT'),
        'dc0202b02d': ('CR_framework', 'NAMED-UNBUILT'),
        'fb2d798ceb': ('CR_framework', 'SELF-ANSWERED'),
        'f36eef9790': ('canonical_time', 'NAMED-UNBUILT'),
        '988eda39e1': ('matter_sector_paper', 'SCOPE-BY-DESIGN')}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  V1 -- five unverdicted qualifications, and a label doing double duty')
    print()
    spec = importlib.util.spec_from_file_location(
        '_ol', os.path.join(ROOT, 'corpus', 'check_open_ledger.py'))
    ol = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    spec.loader.exec_module(ol)

    # ============================================================ (1) they were unverdicted
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ FIVE QUALIFICATIONS WITH NO RECORDED READING')
    print('  ' + '=' * 74)
    was = git('show', f'{BEFORE}:corpus/open_ledger.txt')
    check(f'⓵ at {BEFORE} none of the five was in the ledger: '
          f'{[k for k in FIVE if k not in was]}', all(k not in was for k in FIVE))
    # ** ⛭⛭⛭ RE-PINNED r3962, AND ALL FOUR OF THIS FILE'S REMAINING FAILURES ARE ONE DIAGNOSIS:
    # ** *** THE CORPUS ACTED ON WHAT THIS RECEIPT FOUND. ***  Two of the five opens were CLOSED --
    # ** `f36eef9790` at r3803 ("the straddle is a computed fact: build 3 of 3 closed") and
    # ** `dc0202b02d` at r3811 ("five stale sentences closed, including one in P07's ABSTRACT") --
    # ** so the gate's scan no longer raises them and there is no row to carry a verdict.  A third,
    # ** `114e4d9ede`, was RECLASSIFIED NAMED-UNBUILT -> REGISTERED at r3872 on the ledger's own
    # ** criterion, its home being `PO-23`.
    #   ⇒ ** A claim leaving the scan because the paper settled it is a STRONGER outcome than the
    #     verdict this file pinned, and pinning the verdict made the stronger outcome read as a
    #     failure. **  What is asserted now is the invariant: *each of the five has a recorded
    #     reading*, which is a live verdict OR a closure -- and WHICH, measured, for each.
    #   ⌗ This is the same class as `C19` and `L560/P1`, met a third time in one pass (r3962): a
    #     receipt that argues for a change and pins the unchanged state fails when it succeeds.
    cur = ol.scan()
    led = ol.read_ledger()
    got = {k: next((v[1] for i, v in led.items() if i.startswith(k)), None) for k in FIVE}
    scanned = {k: any(i.startswith(k) for i in cur) for k in FIVE}
    closed = sorted(k for k in FIVE if not scanned[k])
    check(f'⓵ᵇ each of the five is EITHER still a qualification the papers hold, by the gate\'s own '
          f'scan, OR closed since -- and none is half in: {scanned}',
          all(scanned[k] == (got[k] is not None) for k in FIVE))
    # ⌗ the VALUES are not this file's thesis and pinning all three is what broke the old check --
    #   a verdict is a reviewed judgement and may be revised, as `114e4d9ede`'s was at r3872.  What
    #   is asserted is that each has one and none is UNVERDICTED; and then, separately and by name,
    #   the ONE row this file's argument turns on.
    check(f'⓵ᶜ the three the papers still hold each carry a recorded verdict and none is blank: '
          f'{ {k: got[k] for k in FIVE if scanned[k]} }',
          all(got[k] and got[k] != 'UNVERDICTED' for k in FIVE if scanned[k]))
    check('⓵ᶜᐟ ⛭ and the row this file is ABOUT -- P07\'s "only the ultraviolet definition of the '
          'mode sums remains open here" -- reads REGISTERED, reclassified from NAMED-UNBUILT at '
          'r3872 because it has a home, and the home is PO-23',
          got['114e4d9ede'] == 'REGISTERED'
          and 'PO-23' in next(v[2] for i, v in led.items() if i.startswith('114e4d9ede')))
    check(f'⛭ and the other {len(closed)} were CLOSED rather than left unread -- {closed} -- so the '
          f'scan no longer raises them at all: r3803 computed the straddle and r3811 closed five '
          f'stale sentences, both AFTER this file named them',
          closed == ['dc0202b02d', 'f36eef9790']
          and all(got[k] is None for k in closed))
    unv = [k for k, v in led.items() if v[1] == 'UNVERDICTED']
    check(f'⓵ᵈ and nothing is left UNVERDICTED: {len(unv)}', unv == [])

    # ============================================================ (2) the contradiction in terms
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ THE STRUCK CLAUSE AND THE PAPER, READ SIDE BY SIDE')
    print('  ' + '=' * 74)
    p7 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
              encoding='utf-8', errors='replace').read()
    prot = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read()
    kill = open(os.path.join(ROOT, 'kills', 'PO-6.md'), encoding='utf-8', errors='replace').read()
    check('⓶ P07 says the shared character of the wall does NOT settle it, and that the UV '
          'definition is "a genuine open frontier of the programme\'s quantum sector"',
          'the shared character of the wall does not settle it' in p7
          and 'a genuine open frontier of the programme' in p7)
    po6 = [l for l in prot.split('\n') if re.match(r'\|\s*~*\*\*PO-6\*\*', l)]
    # ** ⛭⛭⛭ AND HERE IS THE FINDING BEING ACTED ON, IN THE REGISTER ITSELF (re-pinned r3962). **
    # ** This file's whole argument is that clause ③ read "THE UV DEFINITION: MET, NOT OWED" while
    # ** P07 carried the item as a live frontier -- a label doing double duty.  *** r3809 SUPERSEDED
    # ** the clause and opened `PO-23`, and the register now demotes the old reading to past tense:
    # ** "⛔ THIS CLAUSE IS SUPERSEDED -- see PO-23, opened r3809.  *It read MET, NOT OWED*". ***
    #   ⇒ ** Both ends are pinned: the strike stands, and the clause that made it ambiguous no longer
    #     does.  Re-pinning only the old wording would have asserted the defect as though it were
    #     still live -- which is the mirror of the mistake this file was written to catch. **
    check('⓶ᵇ ⛔ PO-6 is STRUCK, and clause ③ is now marked SUPERSEDED with the item rehomed to '
          'PO-23 (r3809) -- the "MET, NOT OWED" reading this file flagged is stated in the PAST '
          'tense, as a reading the row once carried',
          len(po6) == 1 and po6[0].lstrip('| ').startswith('~~')
          and 'THIS CLAUSE IS SUPERSEDED' in po6[0] and 'PO-23, opened r3809' in po6[0]
          and '*It read MET, NOT OWED*' in po6[0]
          and 'THE UV DEFINITION: **MET, NOT OWED**' not in po6[0])
    # ** the ORDER matters: the strike is the later statement, so it is not superseded prose **
    sent = git('log', '-S', 'the shared character of the wall does not settle it', '--format=%h',
               '--', 'corpus/CR_framework.tex').split()
    strike = git('log', '-S', 'THE UV DEFINITION: **MET, NOT OWED**', '--format=%h',
                 '--', 'PROTECTED_OPEN.md').split()
    later = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor',
                            sent[-1], strike[-1]], capture_output=True).returncode == 0
    check(f'⓶ᶜ and the STRIKE is the later statement ({strike[-1]} after {sent[-1]}), so this is '
          'not old prose left behind a newer verdict -- the newer one is the ambiguous one', later)

    # ============================================================ (3) the reconciliation
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ AND IT IS A LABEL DOING DOUBLE DUTY, NOT A DISAGREEMENT')
    print('  ' + '=' * 74)
    check('⓷ the kill file\'s ARGUMENT is about CR\'s SPECIFIC part -- a counterterm basis "one-'
          'dimensional by conformal flatness" -- and calls the result "a generic problem on '
          'unusually good terms", which is "not ours", not "done"',
          'one-dimensional by conformal flatness' in kill
          and 'A generic problem on unusually good terms' in kill)
    p10 = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
               encoding='utf-8', errors='replace').read()
    # ** ⛭ RE-PINNED r3962 (moved prose).  P10 said "the standard problem of the interacting theory
    # ** rather than a residual freedom in the quantization"; it now makes the SAME distinction in
    # ** other words, and the distinction is the whole of what this check is for. **
    check('⓷ᵇ and P10 draws the same distinction in its own voice -- what remains open is "the '
          'ultraviolet definition of the tower sums---a different thing from a residual freedom in '
          'the quantization at the boundary, and not settled by being shared with every interacting '
          'field theory" -- so the two papers agree and it is the ROW\'s one-word label that reads '
          'otherwise',
          'ultraviolet definition of the tower sums---a different thing from a residual freedom in '
          'the quantization at the boundary' in re.sub(r'\s+', ' ', p10)
          and 'shared with every interacting field theory' in re.sub(r'\s+', ' ', p10))
    entry = next(v[2] for i, v in led.items() if i.startswith('114e4d9ede'))
    # ** ⛭ RE-PINNED r3962, AND THE OLD NOTE WAS RETIRED FOR BEING STALE -- BY NAME, IN THIS ROW. **
    # ** The entry used to reconcile via PO-6's clause ③ warrant ("MET, NOT OWED" / "CR ADDS NO
    # ** BURDEN OF ITS OWN").  r3871 marked that warrant SUPERSEDED and r3872 rewrote the note, which
    # ** says so in terms: *"the strike and this sentence agree", but `kills/PO-6.md` marks that
    # ** warrant SUPERSEDED r3871 ... the live row is PO-23*.
    #   ⇒ ** The reconciliation is still written into the ledger, which is what this check is for --
    #     it is written against the LIVE row instead of the retired warrant. **  Pinning the old
    #     warrant's words would have re-certified the very reconciliation the corpus withdrew.
    check('⓷ᶜ and the reconciliation is written into the ledger entry rather than left to be '
          'rediscovered -- now against the LIVE row PO-23, the entry recording that PO-6\'s clause '
          '③ warrant was superseded at r3871 and naming what replaced it',
          'PO-23' in entry and 'SUPERSEDED r3871' in entry
          and 'the live row is PO-23' in entry)
    check('⓷ᵈ ⌗ and nothing is unstruck: PO-6 stays struck, because the reconciliation is that the '
          'strike is RIGHT',
          po6[0].lstrip('| ').startswith('~~'))

    # ============================================================ (4) the owed-but-not-load-bearing
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ AN OWED ITEM THAT IS NOT LOAD-BEARING IS A DIFFERENT DEBT')
    print('  ' + '=' * 74)
    # ** ⛭⛭⛭ AND THIS ONE IS NOT A RE-PIN, BECAUSE THE ITEM IS NO LONGER OWED (r3962). **  This check
    # ** read that P10 "names the straddle-as-a-computed-fact as OPEN".  *** P10 now COMPUTES it: ***
    # ** "The straddle itself is now a computed fact\rcpt{P10_the_straddle_is_computed}: the spectrum
    # ** does occupy both sides of $\tfrac34$" -- $\operatorname{spec}\hat\Gamma=[\gamma,\infty)$ with
    # ** $\gamma\le\tfrac14<\tfrac34$ below and unboundedness above.
    #   ⇒ ** Re-pinning would have preserved a sentence that says the opposite of the paper. **  The
    #     debt-shaped half is REPLACED by the discharge; the load-bearing half -- that the closure does
    #     not turn on it -- is unchanged and still pinned, and it is the half PART 4 is actually about.
    #     *An owed item that is not load-bearing is a different debt; an item that has been PAID and is
    #     not load-bearing is not a debt at all, and the section keeps its point either way.*
    _p10 = re.sub(r'\s+', ' ', p10)
    check('⓸ P10 has since SETTLED the straddle -- "The straddle itself is now a computed fact" -- so '
          'the item PART 4 carried as owed-but-not-load-bearing is now paid',
          'The straddle itself is now a computed fact' in _p10
          and 'not the floor but the straddle itself as a computed fact' not in _p10)
    check('⓸ᵃ ⌗ and the half this section turns on is untouched: the closure "is supplied fibre by '
          'fibre and so cannot be broken by the size of the sub-threshold set" -- which is why the '
          'reading held while the item was open and holds now that it is closed',
          'supplied fibre by fibre and so cannot be broken by the size of the sub-threshold set'
          in _p10)
    # ** ⛔ AND THIS ONE DID NOT FAIL, IT CRASHED (repaired r3962). **  `next(...)` with no default
    # ** raised `StopIteration` when the `f36eef9790` row left the ledger at r3803 -- so PART 5 never
    # ** ran and the file exited on a traceback instead of a verdict.  *** A lookup that assumes its
    # ** key still exists turns a closed item into a crash, and a crash reports nothing. ***  The
    # ** entry is gone because the OPEN is gone: the straddle is computed, ⓸ above measures it in
    # ** P10's own words, and there is no ledger row left to record two halves of a live debt.
    e = next((v[2] for i, v in led.items() if i.startswith('f36eef9790')), None)
    check('⓸ᵇ and the ledger no longer carries a row for it AT ALL -- r3803 closed the item, so the '
          'entry that recorded "not load-bearing" and "fibre by fibre" was retired with the open it '
          'described, which is the ledger working rather than the record being lost',
          e is None and not any(i.startswith('f36eef9790') for i in cur))
    e14 = next(v[2] for i, v in led.items() if i.startswith('988eda39e1'))
    check('⓸ᶜ ⚠ and the P14 entry says in itself that it is a LEDGER verdict on another line\'s '
          'paper, resting on this line\'s own PO-14 work, so it can be overturned in one step',
          'LEDGER VERDICT ON A' in e14 and 'PO-14' in e14)

    # ============================================================ (5) the gate
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- THE GATE, AND WHAT IS STILL OWED IN IT')
    print('  ' + '=' * 74)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_open_ledger.py')],
                       capture_output=True, text=True, errors='replace', timeout=600)
    check(f'⓹ check_open_ledger exits {r.returncode}', r.returncode == 0)
    # ** ⛭ RE-PINNED r3962: THE WARN BACKLOG WAS PAID. **  This read `warns >= 1` and said so in
    # ** terms -- "reported, not repaired ... not this revision's business".  Six entries named
    # ** sentences no longer in any paper; the gate now reports ZERO.  *** A check that requires a
    # ** backlog to still exist fails when the backlog is cleared, which is the direction nobody
    # ** writes a test for. ***  Asserted as a RATCHET in the corpus's own idiom: the count may fall
    # ** to zero and stay there, and it fails if the backlog GROWS past what this file recorded.
    warns = r.stdout.count('[WARN]')
    #   ⌗ and the bound is the MEASURED value, not a slack one.  `min(warns, 6) == warns` would pass
    #     at anything up to six and so would notice nothing; ZERO is what the gate reports, so zero
    #     is what is asserted, and a single WARN returning is a finding worth stopping for.
    check(f'⓹ᵇ ⌗ {warns} WARN(s) remain -- entries naming sentences no longer in any paper.  This '
          f'file recorded SIX and routed them rather than rebuilding; the backlog is now PAID, and '
          f'a WARN reappearing means a paper moved out from under a ledger row again',
          warns == 0)
    # ** ⛔ AND THIS ONE COMPARED AGAINST `HEAD`, WHICH IS NOT WHAT IT MEANT (repaired r3962). **
    # ** "no .tex file is touched by THIS REVISION" is a claim about r3130's own diff.  Written as
    # ** `BEFORE..HEAD` it silently became a claim about *** every revision that would ever follow
    # ** ***, and the corpus has edited .tex files on hundreds of them since -- correctly.
    #   ⇒ ** A check pinned to `HEAD` is pinned to the present, and the present moves. **  That is
    #     the class `L259_the_distance_from_the_present/D1` is named for, met here in its purest
    #     form.  The range is now the revision's OWN, end to end, and it cannot drift again.
    AFTER = 'ae749cb6'          # r3130 -- this revision's own commit
    check(f'⓹ᶜ and no .tex file was touched by THIS revision ({BEFORE}..{AFTER}) -- the reading was '
          f'written in the ledger, not in the papers',
          not [f for f in git('diff', '--name-only', BEFORE, AFTER).split()
               if f.endswith('.tex') and not f.startswith('corpus/appendix_receipts')])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a three-clause row struck as a whole carries one verdict word per clause,')
    print('  and a clause whose honest verdict is "not ours" reads, in the strike\'s grammar, as')
    print('  "done". **  *`PO-6` ③ says "THE UV DEFINITION: MET, NOT OWED"; `P07` says the shared')
    print('  character of the wall does not settle it and carries the item as a frontier.*')
    print('  ⌗ ** They agree. **  The kill file\'s argument is that CR\'s SPECIFIC part is bounded to')
    print('     a one-dimensional counterterm basis -- "not ours", not "done" -- and `P10` says so')
    print('     in the same words.  *Nothing is unstruck; the reconciliation is written down.*')
    print('  ⛭ ** And an owed item that is not load-bearing is a different debt: ** the straddle is')
    print('     `NAMED-UNBUILT` and the paper says the closure below does not turn on it.  Both')
    print('     halves recorded, because recording one is how a debt gets mis-priced.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
