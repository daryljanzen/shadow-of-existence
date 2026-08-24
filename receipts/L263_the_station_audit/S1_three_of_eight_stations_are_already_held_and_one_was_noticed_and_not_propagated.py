#!/usr/bin/env python3
"""S1 -- the R-M theatre's eight stations, audited against the papers before any field is thrown.
THREE are already held.  Two were known (Ⓑ, Ⓓ); the third (Ⓕ) is one the theatre's own frontmatter
complained about, in writing, six hundred and eighty revisions before the list still carried it.

COMPUTES: each station's claim located in the paper that holds it, quoted from the paper body with
comments and bibliography stripped; the frontmatter's own record of the Ⓕ bookkeeping failure and the
span over which it persisted; the three genuinely-owed stations' baselines measured rather than
recalled; and a seeded check that the baseline instrument reads bodies and not comment headers.
No parameter is pinned.

** ⛭ ⓵ THE INSTRUCTION AND ITS REASON. **  `OWED` 609, Daryl r3122: *"exhaust both lists ... Strike
Ⓑ and Ⓓ before starting so the bakes do not re-find them."*  And the gate on the whole item:
*"a bake against a corpus that cannot say what it already holds returns findings it owns"* -- with
`L-203`'s audit, which found two stations already held, cited as *"the failure demonstrated rather
than feared."*

** ⛔⛭⛭ ⓶ AND THERE ARE THREE, NOT TWO. **  Ⓕ -- *the real forms of $SO(6,\\mathbb{C})$* -- is carried
as ⟐ **owed** in `OWED` 609 and is in `P13` in the paper's own words: four real forms; $\\su(3)$
compact of dimension eight needs a maximal compact of at least that; $\\so(4,2)$ and $\\so(3,3)$
excluded on dimension; $\\so(5,1)$'s $\\so(5)$ too small because $\\su(3)$'s smallest faithful real
representation is six-dimensional; *the compact form is the unique real form that admits $\\su(3)$ at
all*.

** ⛔ ⓷ AND THE FAILURE WAS NOTICED, IN WRITING, AND DID NOT PROPAGATE. **  `THE_MATHEMATICS_REACH`'s
own frontmatter says of Ⓕ: *"this frontmatter carried Ⓕ as owed for forty-eight revisions after its
own ① block recorded the answer."*
  ⇒ *** So the document diagnosed the exact bookkeeping error, about the exact station, wrote the
      diagnosis into its own head -- and the downstream list still carried Ⓕ as owed at r3122. ***
  ⇒ ** A NOTICE WRITTEN WHERE THE ERROR HAPPENED DOES NOT REACH THE LIST THAT REPEATS IT.  The
    frontmatter corrected itself; nothing carried the correction to `OWED`. **

** ⌗ ⓸ SO THE GATE IS AN INSTRUMENT, NOT A WAIT. **  609 blocks the theatres on the P11--P17 read
*"by readiness, not dependency"*.  ⇒ *Readiness means "the corpus can say what it already holds",
and that is a MEASUREMENT.*  `corpus/reach_baseline.py` performs it: the paper bodies, comments and
bibliography stripped, surveyed for a bake's terms before the bake asserts anything.
  ⌗ ** And it earned itself immediately: ** *`equivariant index` ×7 read as a hole in the theatre's
    own prose and is `P13` using the Atiyah--Hirzebruch obstruction; `permutation representation` ×1
    read as an opening and is `P14` citing the discrete-flavour literature.*  ⇒ ** A count is not a
    verdict, and the instrument's job is to make a reader LOOK. **

WHAT IS NOT CLAIMED.  ** Not that the three remaining stations are hollow ** -- Ⓖ and Ⓗ are measured
below and both have real baselines: `Atiyah sequence` ×0 against `algebroid` ×128, and `Fredholm` ×0
corpus-wide against an index the corpus asserts.  ** Not that the read is unnecessary ** -- the three
unread papers are `P15`, `P16`, `p0`, and every claim here is measured against all seventeen bodies,
so a bake that lands in one of the three is still a bake against a paper this line has not read.
** Not that `L-203`'s station verdicts are wrong ** -- they are right; what was wrong is the list
downstream of them.  ** And not that Ⓕ was work wasted ** -- it was done, by node 55 at `F13`, and
landed in `P13`; only the bookkeeping failed.

    python3 receipts/L263_the_station_audit/S1_three_of_eight_stations_are_already_held_and_one_was_noticed_and_not_propagated.py

Written r3148, `L-263`.  Stated for reversal.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

spec = importlib.util.spec_from_file_location('_rb', os.path.join(ROOT, 'corpus',
                                                                  'reach_baseline.py'))
RB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RB)
B = RB.BODIES


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- eight stations, audited against the papers')
    print()

    # ============================================================ (1) the three that are held
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔ THREE STATIONS ARE ALREADY HELD IN THE PAPERS')
    print('  ' + '=' * 74)
    HELD = {
        'Ⓑ the forced triple angle / at which D': (
            'P03', 'The triple angle is available in four spacetime dimensions and, with a caveat, '
                   'in five; in no other'),
        'Ⓓ Galois of the energy family': (
            'P05', 'the \\emph{Galois group} of the horizon cubic over the field '
                   '$\\mathbb{C}(2M)$ of the mass parameter'),
        'Ⓕ the real forms of SO(6,C)': (
            'P13', 'the compact form is the unique real form of $\\SO(6,\\mathbb{C})$ that admits '
                   '$\\su(3)$ at all'),
    }
    for station, (paper, quote) in HELD.items():
        check(f'⓵ {station} -- held in {paper}: "{quote[:66]}..."', quote in B[paper])
    # ** and Ⓕ's supporting argument, not just its conclusion **
    p13 = B['P13']
    check('⓵ᵈ and Ⓕ is held with its ARGUMENT and not only its conclusion: four real forms, the '
          'dimension-eight requirement, so(4,2) and so(3,3) excluded, and so(5,1)\'s so(5) too small '
          'for a subalgebra whose smallest faithful real representation is six-dimensional',
          all(s in p13 for s in ('four real forms', '\\so(4,2)', '\\so(3,3)',
                                 'smallest faithful real representation is six-dimensional')))

    # ============================================================ (2) Ⓕ was noticed and not carried
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND Ⓕ WAS DIAGNOSED IN WRITING, WHERE IT HAPPENED')
    print('  ' + '=' * 74)
    reach = open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'), encoding='utf-8').read()
    NOTICE = 'carried Ⓕ as owed for forty-eight revisions after its own ① block recorded the answer'
    check(f'⓶ the theatre\'s own frontmatter says it: "{NOTICE[:60]}..."', NOTICE in reach)
    # ⛔⛭⛭ AMENDED r3156 (`L-268`).  ** THESE TWO CHECKS READ THE LIVE `OWED.md` FOR A CLAIM ABOUT
    # ** THE STATE THIS RECEIPT'S OWN REVISION CHANGED. **  *r3148 struck Ⓕ in `OWED` 609 -- that is
    #   what the receipt is FOR -- and the checks then asserted that `OWED` still carried it.*
    #   ⇒ *** So they were false at the moment they were committed, and no care about the past
    #       protects against it: the state was changed by the same revision that asserted it. ***
    #   ⇒ ** The fifth disguise of `L-258`'s class, and the tightest: the earlier four were broken by
    #     time, by another line's settlement, or by a distance from HEAD.  This one is broken by the
    #     receipt's own edit, in its own revision. **
    #   ⇒ ** The claim is about the state BEFORE the strike, so it is read at the PARENT commit; and
    #     the present is asserted in the opposite direction, which is the direction that says the
    #     repair landed. **
    PARENT = '3eb48621'          # the tree as it stood before r3148 struck the three stations
    owed_was = subprocess.run(['git', '-C', ROOT, 'show', f'{PARENT}:OWED.md'],
                              capture_output=True, text=True, errors='replace').stdout
    owed_now = open(os.path.join(ROOT, 'OWED.md'), encoding='utf-8').read()
    RX = r'Ⓕ the two real forms of \$SO\(6,\\mathbb\{C\}\)\$ ⟐ \*\*owed\*\*'
    was = re.search(RX, owed_was)
    check(f'⓶ᵇ ⛔ and at {PARENT} -- before this revision struck it -- `OWED` 609 still carried Ⓕ as '
          '⟐ owed, downstream of that notice', was is not None)
    check('⓶ᶜ *** so a notice written where the error happened did not reach the list that repeats '
          'it -- the frontmatter corrected itself and nothing carried the correction ***',
          NOTICE in reach and was is not None)
    check('⓶ᵉ ⛭ and it is struck NOW, which is this receipt landing rather than this receipt '
          'breaking: the live row says STRUCK r3148 and no longer says owed',
          re.search(RX, owed_now) is None and 'STRUCK r3148' in owed_now)
    # the span, measured rather than recalled
    walked = subprocess.run(['git', '-C', ROOT, 'log', '--format=%s', '-S', NOTICE,
                             '--', 'THE_MATHEMATICS_REACH.md'], capture_output=True,
                            text=True, errors='replace').stdout.split('\n')
    walked = [w for w in walked if w.strip()]
    print(f'    the notice enters the file at: {walked[-1][:70] if walked else "?"}')
    check('⓶ᵈ and the notice is a commit in this history, so the span is a fact and not a memory',
          len(walked) >= 1)

    # ============================================================ (3) the three genuinely owed
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THE REMAINING STATIONS, WITH BASELINES MEASURED')
    print('  ' + '=' * 74)
    g = {t: sum(RB.counts(t).values()) for t in
         ('Atiyah sequence', 'exact sequence', 'Chevalley', 'algebroid', 'anchor')}
    print(f'    Ⓖ Lie algebroids : {g}')
    check('⓷ Ⓖ is genuinely owed and its baseline is the one the theatre states: the corpus holds '
          'algebroid and anchor in quantity and carries NO Atiyah sequence, no exact sequence and '
          'no Chevalley--Eilenberg anywhere',
          g['algebroid'] > 100 and g['anchor'] > 20
          and g['Atiyah sequence'] == 0 and g['exact sequence'] == 0 and g['Chevalley'] == 0)
    h = {t: sum(RB.counts(t).values()) for t in
         ('Fredholm', 'limit-point', 'deficiency ind', 'Atiyah--Singer', 'graded index',
          'traced rather than computed')}
    print(f'    Ⓗ the graded index : {h}')
    check('⓷ᵇ ⛔ Ⓗ is genuinely owed and its baseline is SHARPER than the theatre states: the '
          'corpus asserts a graded index and cites Atiyah--Singer, and the word `Fredholm` does not '
          'occur in seventeen papers',
          h['Fredholm'] == 0 and h['graded index'] > 0 and h['Atiyah--Singer'] > 0
          and h['traced rather than computed'] > 0)
    # ** r3249 (node 57): THE GAP THIS CHECK RECORDED IS NOW CLOSED, and the check is rewritten to
    #    say so rather than to keep asserting the absence.  Station Ⓗ made the join (L-264, r3150),
    #    57's L-265 corrected its verdict to LIMIT-CIRCLE at r3205, and P14 now carries that
    #    statement with a self-adjoint extension named as owed (OWED 622).  What the audit FOUND --
    #    that the apparatus was P10's alone and unjoined -- is what made the station worth throwing. **
    check('⓷ᶜ ⌗ the machinery EXISTS in the corpus as P10\'s deficiency-index apparatus, and the '
          'join to P14 -- which carries the index -- IS NOW MADE: P14 states the branch point '
          'limit-circle and names the extension as owed',
          RB.counts('deficiency ind')['P10'] > 0
          and RB.counts('limit-circle')['P14'] > 0)
    check('⓷ᵈ and Ⓒ is not owed as a station -- the theatre records it as BIT and `L-203`/`M1` '
          'carries the finding',
          os.path.exists(os.path.join(ROOT, 'receipts', 'L203_reach_stations',
                                      'M1_the_equianharmonic_group_is_not_the_monodromy_group.py')))

    # ============================================================ (4) the instrument
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE GATE IS A MEASUREMENT, SO IT IS AN INSTRUMENT')
    print('  ' + '=' * 74)
    check('⓸ the instrument reads BODIES: `%` comment headers are stripped, so a term that lives '
          'only in a paper\'s working notes is not counted as held',
          all(not any(l.lstrip().startswith('%') for l in b.split('\\n')) for b in B.values()))
    # SEEDED: a phrase that exists ONLY in P14's comment header must not be found
    raw14 = open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
                 encoding='utf-8', errors='replace').read()
    only_comment = 'THE RECEIPT WAS MORE HONEST THAN THE PAPER'
    check(f'⓸ᵇ SEEDED: "{only_comment}" is in P14\'s comment header and NOT in its body -- the '
          'instrument finds 0',
          only_comment in raw14 and sum(RB.counts(only_comment).values()) == 0)
    check('⓸ᶜ and it earned itself on this very audit: `equivariant index` ×7 reads as a hole in '
          'the theatre\'s prose and is P13 using the Atiyah--Hirzebruch obstruction',
          sum(RB.counts('equivariant index').values()) == 7
          and 'Atiyah--Hirzebruch index obstruction' in B['P13'])
    check('⓸ᵈ and `permutation representation` ×1 reads as an opening and is P14 citing the '
          'discrete-flavour literature, not an index statement',
          sum(RB.counts('permutation representation').values()) == 1
          and 'three-object permutation representation' in B['P14']
          and 'democracy matrix' in B['P14'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** three of the eight R-M stations are already held in the papers, not two. **')
    print('  *Ⓑ in P03\'s `rem:dimension`, Ⓓ in P05\'s `rem:galois`, and Ⓕ in P13 in the paper\'s own')
    print('  words -- the compact form the unique real form admitting su(3).*')
    print('  ⛔ ** And Ⓕ was diagnosed in writing, where it happened. **  *The theatre\'s frontmatter')
    print('     says it carried Ⓕ as owed for forty-eight revisions after recording the answer; the')
    print('     list downstream still carried it.*  ⇒ *** A notice written where the error happened')
    print('     does not reach the list that repeats it. ***')
    print('  ⌗ ** So the readiness gate is a MEASUREMENT and can be an instrument instead of a')
    print('     wait: ** `corpus/reach_baseline.py` surveys the paper bodies before a bake asserts.')
    print('     *It earned itself twice on this audit alone.*')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
