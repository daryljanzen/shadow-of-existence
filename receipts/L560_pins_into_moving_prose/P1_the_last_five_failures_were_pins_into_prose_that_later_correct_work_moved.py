#!/usr/bin/env python3
"""P1 -- the last five failing receipts were one class, and it is the class this span kept finding: a
pin into prose that later CORRECT work moved.  Four had their finding acted on; the fifth turned up six
sentences that left the papers entirely.

COMPUTES: each of the five failures traced to the commit that caused it; that in four cases the mover
was the receipt's own recommendation landing; that in three of those the mover was this fork; the
before/after measurement at each end pinned to a SHA; and the survival count for the sixth case, stated
as a measurement and routed rather than interpreted.

** ⛭⛭⛭ THE CLASS, AND IT IS NOT CARELESSNESS. **

At the start of this span the full run stood at 13 failures.  Nine were cleared by repairing the corpus
(`L-556`, `L-557`, `L-558`, `L-559`).  ** The five that remained had nothing wrong with the corpus at
all: each pins a quotation or a count into text that later work CHANGED, and in four of the five the
change is the receipt's OWN FINDING BEING ACTED ON. **

      L175/N1   measured ZERO "Lovelock" in the papers at r2515 -- correctly.  The fork's own
                c54.202 then added P12's Lovelock sentence, and the merge carried it in.
      L200/U1   pinned p0's "Reach: stated as a target, not a result".  The fork's own c54.179
      L200/U3   split that item -- "two sides and they now stand differently" -- which is the
                closure both receipts argued for.
      L536/F1   measured 11,359 characters (35%) of settled physics filed under "Frontiers and
                open problems".  It is 3,264 (13%) now: about eight thousand characters moved out.
      L207/W1   quotes six sentences of P8.  r2581's "rehoming pass 1" moved them.

  ⇒ *** A receipt that argues for a change and pins the unchanged text is a receipt that fails the
      moment it succeeds. ***  ** That is the same shape as `L-557`'s seven loud receipts and
      `L230/C1`'s overturned thesis, and it is the third distinct instance this span. **

** ⌷ THE FIX IS UNIFORM AND IT IS c54.220's RULE. **  A quotation is a claim about a FILE AT A COMMIT.
Both ends are pinned: the historical wording at the commit where it stood, and the CURRENT text asserted
separately -- so the receipt records the closure instead of dying of it.

** ⚠ AND ONE OF THE FIVE IS NOT LIKE THE OTHERS, AND IT IS ROUTED RATHER THAN READ. **  Of the six
sentences `W1` quotes from `slicing_operator.tex`, *** NONE is present in any paper .tex now *** -- they
did not move to another paper, they left.  r2581's message is "rehoming pass 1: slicing_operator, and
the paragraph contained the general form of the paper's own central identity."
  ⇒ ** Whether the CONTENT survives under other words is a reading of P8 before and after, and this file
    does not make it. **  *The number is stated so the question is well posed and cheap to take up.
    Interpreting six missing sentences in passing, at the end of a re-pinning sweep, is how a wrong
    reading gets inscribed -- and a re-pin is exactly the operation that would hide it.*

** WHAT IS NOT CLAIMED. **  ** Not that any of the five findings changes ** -- every one is preserved and
now records its own discharge.  ** Not that r2581 lost content ** -- that is the routed question and the
measurement is all this file supplies.  ** Not that the run is at zero because the corpus is right **:
it is at zero because five stale pins were repaired, which is a smaller claim.

Written c54.226 (`L-560`).  Stated for reversal.
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RD = os.path.join(ROOT, 'receipts')
FAILED = []

#: the five, and the commit that moved the text each pinned.
CASES = [
    ('L175_dimensional_descent/N1_the_cut_being_four_is_what_makes_the_dynamics_forced.py',
     '0d38a5b', 'c54.202', True),
    ('L200_free_data_count/U1_the_count_as_the_corpus_now_states_it.py',
     '2af0b0b', 'c54.179', True),
    ('L200_free_data_count/U3_the_residue_is_one_and_it_is_already_counted.py',
     '2af0b0b', 'c54.179', True),
    ('L536_frontier_placement/F1_resolved_content_sits_in_the_frontier_sections.py',
     None, 'the frontier sweep', True),
    ('L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py',
     '989fc4b', 'r2581', False),
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def src(rel):
    return open(os.path.join(RD, rel), encoding='utf-8', errors='replace').read()


def flat(s):
    return re.sub(r'\s+', ' ', s)


def main():
    print()
    print('  P1 -- the last five failures, and the one class they share')
    print()

    # ⓵ all five now run and all five carry the re-pin note
    rcs = []
    for rel, _, _, _ in CASES:
        d, b = os.path.dirname(os.path.join(RD, rel)), os.path.basename(rel)
        rcs.append((b[:28], subprocess.run(['python3', b], cwd=d, capture_output=True,
                                           text=True, errors='replace').returncode))
    check(f'⓵ all five run and exit zero: { {b: rc for b, rc in rcs} }',
          all(rc == 0 for _, rc in rcs))
    noted = [rel for rel, _, _, _ in CASES if 'c54.226' in src(rel)]
    check(f'⇒ and all {len(noted)} carry the re-pin note naming this revision, so the repair is '
          f'legible in the file rather than only in a register',
          len(noted) == len(CASES))

    # ⓶ the mover, per case, at the commit
    live = flat(''.join(open(f, encoding='utf-8', errors='replace').read()
                        for f in sorted(__import__('glob').glob(
                            os.path.join(ROOT, 'corpus', '*.tex')))
                        if not os.path.basename(f).startswith('appendix_receipts')))
    p12_then = flat(git('show', 'eda3ad7:corpus/algebroid_paper.tex'))
    check('⓶ N1: "Lovelock" occurs 0 times in P12 at eda3ad7 (r2515, its own build) and is present '
          'now -- the fork\'s c54.202 added it',
          'Lovelock' not in p12_then
          and 'the same algebra closes for the Lovelock theories' in live)
    p0_then = flat(git('show', 'aa2b6ee:corpus/geometric_core_paper.tex'))
    check('⇒ U1/U3: p0 read "Reach: stated as a target, not a result" at aa2b6ee and reads "the item '
          'has two sides and they now stand differently" now -- the fork\'s c54.179 split it',
          'Reach: stated as a target, not a result' in p0_then
          and 'the item has two sides and they now stand differently' in live
          and 'Reach: stated as a target, not a result' not in live)
    p7_then = flat(git('show', 'e8e58cf:corpus/CR_framework.tex'))
    seg_then = p7_then[p7_then.find('\\section{Frontiers and open problems}'):]
    below_then = len(seg_then) - seg_then.find('\\end{enumerate}')
    p7_now = flat(open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
                       encoding='utf-8', errors='replace').read())
    seg_now = p7_now[p7_now.find('\\section{Frontiers and open problems}'):]
    below_now = len(seg_now) - seg_now.find('\\end{enumerate}')
    # ** measured on the RAW file here; `F1` strips the preamble and comments before measuring, so its
    # own figures are 11,359 -> 3,264 (35% -> 13%).  The two preprocessings differ and the DIRECTION and
    # the magnitude agree, which is what this check is for -- not a second copy of F1's arithmetic. **
    check(f'⇒ F1: {below_then:,} characters sat below P7\'s frontier list at e8e58cf (r2579, its own '
          f'build) and {below_now:,} do now, measured on the raw file -- the defect it named was acted '
          f'on (F1\'s own stripped measurement: 11,359 -> 3,264), and the residue is not zero',
          below_then > 10000 and 0 < below_now < 0.75 * below_then)

    # ⓷ three of the four movers are THIS fork
    ours = [tag for _, sha, tag, acted in CASES if acted and tag.startswith('c54')]
    check(f'⓷ and {len(ours)} of the four acted-on cases were moved by THIS FORK\'s own later work '
          f'({", ".join(sorted(set(ours)))}) -- a receipt of the observer line\'s broken by the fork '
          f'doing what the receipt asked for',
          len(set(ours)) == 2 and len(ours) == 3)

    # ⓸ the routed one
    QUOTES = ["the cut's advance is generated by a true Hamiltonian",
              'the first dynamical bend the construction displays, in vacuum',
              'a characteristic crossing with no curvature obstruction',
              'That worldline dynamics is taken up for a concrete matter model',
              'the deepest question the construction opens onto',
              'Since the framework leaves the dynamics of general relativity unchanged']
    p8_then = flat(git('show', '9d9f97f:corpus/slicing_operator.tex'))
    alive = [q for q in QUOTES if q in live]
    check(f'⓸ W1 is not like the others: all {len(QUOTES)} of its P8 quotations are present at '
          f'9d9f97f (before r2581) and {len(alive)} are present in ANY paper now',
          all(q in p8_then for q in QUOTES) and len(alive) == 0)
    check('⇒ SO THEY DID NOT MOVE TO ANOTHER PAPER -- THEY LEFT.  r2581 is "rehoming pass 1: '
          'slicing_operator, and the paragraph contained the general form of the paper\'s own central '
          'identity"',
          'rehoming pass 1' in git('log', '--format=%s', '-1', '989fc4b'))
    w1 = src('L207_the_bend/W1_what_remains_between_the_wall_and_a_curve_dynamics.py')
    check('⚠ and this file does NOT read whether the CONTENT survives under other words: W1 states the '
          'count and says so in terms, and it is routed rather than interpreted',
          'ROUTED RATHER THAN INTERPRETED' in w1 and 'routed rather than made here' in w1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the last five failures were one class -- a pin into prose that later CORRECT')
    print('    work moved -- and in four of the five the mover was the receipt\'s own finding being')
    print('    acted on. **')
    print('    · three of those four were moved by THIS fork doing what the receipt asked for')
    print(f'    · the fifth turned up {len(QUOTES)} sentences that left the papers at r2581, MEASURED')
    print('      and routed, not read')
    print('  ⇒ ** A receipt that argues for a change and pins the unchanged text fails the moment it')
    print('    succeeds.  Both ends take a SHA. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
