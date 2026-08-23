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
    cur = ol.scan()
    check('⓵ᵇ and all five are qualifications the papers actually hold, by the gate\'s own scan',
          all(any(i.startswith(k) for i in cur) for k in FIVE))
    led = ol.read_ledger()
    got = {k: next((v[1] for i, v in led.items() if i.startswith(k)), None) for k in FIVE}
    check(f'⓵ᶜ and each now carries the verdict recorded here: {got}',
          all(got[k] == FIVE[k][1] for k in FIVE))
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
    check('⓶ᵇ ⛔ and PO-6 is STRUCK with clause ③ reading "THE UV DEFINITION: **MET, NOT OWED**"',
          len(po6) == 1 and po6[0].lstrip('| ').startswith('~~')
          and 'THE UV DEFINITION: **MET, NOT OWED**' in po6[0])
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
    check('⓷ᵇ and P10 says the same thing in the same words -- "the standard problem of the '
          'interacting theory rather than a residual freedom in the quantization" -- so the two '
          'papers agree and it is the ROW\'s one-word label that reads otherwise',
          'the standard problem of the interacting theory rather than a residual freedom' in p10)
    entry = next(v[2] for i, v in led.items() if i.startswith('114e4d9ede'))
    check('⓷ᶜ and the reconciliation is written into the ledger entry rather than left to be '
          'rediscovered -- which is the whole point of the ledger',
          'MET, NOT OWED' in entry and 'CR ADDS NO BURDEN OF ITS OWN' in entry)
    check('⓷ᵈ ⌗ and nothing is unstruck: PO-6 stays struck, because the reconciliation is that the '
          'strike is RIGHT',
          po6[0].lstrip('| ').startswith('~~'))

    # ============================================================ (4) the owed-but-not-load-bearing
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ AN OWED ITEM THAT IS NOT LOAD-BEARING IS A DIFFERENT DEBT')
    print('  ' + '=' * 74)
    check('⓸ P10 names the straddle-as-a-computed-fact as open AND says in the same sentence what '
          'does not turn on it -- "supplied fibre by fibre and so cannot be broken by the size of '
          'the sub-threshold set"',
          'not the floor but the straddle itself as a computed fact' in p10
          and 'supplied fibre by fibre' in p10)
    e = next(v[2] for i, v in led.items() if i.startswith('f36eef9790'))
    check('⓸ᵇ and the entry records BOTH halves', 'not load-bearing' in e and 'fibre by fibre' in e)
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
    warns = r.stdout.count('[WARN]')
    check(f'⓹ᵇ ⌗ and {warns} WARN(s) remain -- ledger entries naming sentences no longer in any '
          'paper.  *Reported, not repaired: `--rebuild` re-derives them and that is not this '
          'revision\'s business.*  A gate that passed silently over these would be worse.',
          warns >= 1 and 'run --rebuild to re-derive' in r.stdout)
    check('⓹ᶜ and no .tex file is touched by this revision -- the reading is written in the '
          'ledger, not in the papers',
          not [f for f in git('diff', '--name-only', BEFORE, 'HEAD').split()
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
