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
as ⟐ **owed** in `OWED` 609 and is in `P13` in the paper's own words: the enumeration; $\\su(3)$
compact of dimension eight needs a maximal compact of at least that; $\\so(4,2)$ and $\\so(3,3)$
excluded on dimension; $\\so(5,1)$'s $\\so(5)$ too small because $\\su(3)$'s smallest faithful real
representation is six-dimensional.
  ⌗ ** THE COUNT IN THAT SENTENCE WAS FOUR WHEN THIS WAS WRITTEN AND IS FIVE NOW ** -- the involution
    bake corrected it at r3329, naming $\\SO^{*}(6)\\cong\\SU(3,1)$ as the omitted form, and the
    "unique real form" clause went at r3414.  *The STATION is untouched by either: what `P13` holds
    is the enumeration and the exclusions, and it holds MORE of them than it did.*  Both superseded
    wordings are pinned at the commits where they stood (`⓵ᵉ`), so this audit's own history stays
    checkable rather than becoming a memory.

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

#: ** ⛭ THE BASELINE AT THIS AUDIT'S OWN THROW (r3972), mirroring `reach_baseline.bodies()` exactly.
#: ** An audit's baseline is a fact about the corpus BEFORE the stations were thrown; read from the
#: ** live papers it asserts that nobody acted on them.
_AT_BUILD = '21504860'          # r3148 -- this audit's own throw
_AT_BUILD_CACHE = {}


def _at_build_counts(term):
    """`RB.counts(term)` as it read at this audit's own throw commit."""
    import re as _re
    import subprocess as _sp
    if not _AT_BUILD_CACHE:
        for _tex, _key in RB.TEX2P.items():
            _raw = _sp.run(['git', 'show', f'{_AT_BUILD}:corpus/{_tex}'], cwd=ROOT,
                           capture_output=True, text=True, errors='replace').stdout
            _b = '\n'.join(l for l in _raw.split('\n') if not l.lstrip().startswith('%'))
            _j = _b.find('\\begin{thebibliography}')
            _AT_BUILD_CACHE[_key] = _re.sub(r'\s+', ' ', _b[:_j] if _j > 0 else _b)
        assert len(_AT_BUILD_CACHE) == len(RB.TEX2P), (
            'every paper must be readable at the throw commit, or the baseline is partial',
            sorted(set(RB.TEX2P.values()) - set(_AT_BUILD_CACHE)))
    return {k: len(_re.findall(_re.escape(term), v, _re.I))
            for k, v in _AT_BUILD_CACHE.items()}

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
        # ⛭⛭ RE-PINNED r3544 (node 60).  ** THE STATION IS STILL HELD; ITS WORDING MOVED TWICE. **
        #   The r3148 quote was P13's own and is P13's no longer: the involution bake corrected the
        #   count FOUR -> FIVE at r3329 and the "unique real form" sentence went at r3414.  ** A
        #   station whose quote has been superseded reads exactly like a station that was never
        #   held, and the difference is the whole point of this audit. **  So both halves are now
        #   asserted, in the corpus's own r2376+c54.226 shape: the historical wording pinned at the
        #   commit where it stood, the CURRENT wording asserted against the live paper.
        'Ⓕ the real forms of SO(6,C)': (
            'P13', 'real forms of the one complex group $\\SO(6,\\mathbb{C})$'),
    }
    for station, (paper, quote) in HELD.items():
        check(f'⓵ {station} -- held in {paper}: "{quote[:66]}..."', quote in B[paper])
    p13 = B['P13']
    # ** and Ⓕ's supporting argument, not just its conclusion -- as P13 CARRIES IT NOW **
    check('⓵ᵈ and Ⓕ is held with its ARGUMENT and not only its conclusion: FIVE real forms with '
          'SO*(6) = SU(3,1) named, so(4,2) and so(3,3) excluded on dimension, and so(5,1)\'s so(5) '
          'too small for a subalgebra whose smallest faithful real representation is six-dimensional',
          all(t in p13 for t in ('\\emph{five} real forms', '\\SO^{*}(6)', '\\SU(3,1)',
                                 '\\so(4,2)', '\\so(3,3)',
                                 'smallest faithful real representation is six-dimensional')))
    # and the SUPERSEDED wording, pinned where it stood, so the audit's own history stays checkable
    FOUR_AT = 'aa32d936'      # r3329^ -- the last tree in which P13 said "four real forms"
    UNIQ_AT = '2f0ebd6f'      # r3414^ -- the last tree carrying "the compact form is the unique..."
    old13 = lambda sha: subprocess.run(['git', '-C', ROOT, 'show', f'{sha}^:corpus/boundary_paper.tex'],
                                       capture_output=True, text=True, errors='replace').stdout
    was_four, was_uniq = old13(FOUR_AT), old13(UNIQ_AT)
    check(f'⓵ᵉ ⛭ and the r3148 wording is pinned, not lost: "four real forms" stood at {FOUR_AT}^ '
          f'(r3329, where the involution bake corrected it to five) and the "unique real form" '
          f'sentence at {UNIQ_AT}^ (r3414) -- and BOTH are gone from the live paper',
          bool(was_four) and 'four real forms' in was_four
          and bool(was_uniq) and 'the compact form is the unique real form' in was_uniq
          and 'four real forms' not in p13
          and 'the compact form is the unique real form' not in p13)

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
    # ⛭⛭ REWRITTEN r3544 (node 60).  ** THE ABSENCE THIS CHECK RECORDED IS GONE, AND THAT IS THE
    #   STATION BEING WORKED RATHER THAN THIS RECEIPT BREAKING. **  At r3148 `Atiyah sequence` was
    #   x0 across seventeen bodies and Ⓖ's baseline was that absence.  P12 now states the grading
    #   IS the Atiyah sequence (x2, entered at 6c47575d, r3253) and p0 carries `exact sequence` x1.
    #   ⇒ *** A check that keeps asserting an absence after the absence has been filled reports the
    #   station as owed for as long as nobody re-runs it -- which is the SAME failure this receipt
    #   was written to name, arriving in the receipt that names it. ***  So it now asserts the
    #   baseline where it stood AND the present, in opposite directions.
    AS_AT = '3803c725'        # r3251 -- where P12 FIRST carried the Atiyah sequence.  ⌗ r3253 was
    #   the first candidate and it is NOT the introduction: `git log -S` lists every commit that
    #   changes a count, and r3253 took P12 from one occurrence to two.  ** The first commit a
    #   -S search returns is the most RECENT change, not the origin. **  Checked at both parents.
    p12_was = subprocess.run(['git', '-C', ROOT, 'show', f'{AS_AT}^:corpus/algebroid_paper.tex'],
                             capture_output=True, text=True, errors='replace').stdout
    check('⓷ Ⓖ\'s baseline STOOD as the theatre states -- algebroid and anchor in quantity, and no '
          f'Atiyah sequence anywhere -- and is pinned at {AS_AT}^ (r3251) rather than recalled',
          g['algebroid'] > 100 and g['anchor'] > 20 and g['Chevalley'] == 0
          and bool(p12_was) and 'Atiyah sequence' not in p12_was)
    check('⓷ᵃ ⛭ AND IT IS NO LONGER THE BASELINE: P12 now names the Atiyah sequence and p0 an exact '
          'sequence, so Ⓖ has been WORKED since this audit and the station is not owed as it was',
          g['Atiyah sequence'] > 0 and g['exact sequence'] > 0
          and RB.counts('Atiyah sequence')['P12'] > 0)
    h = {t: sum(RB.counts(t).values()) for t in
         ('Fredholm', 'limit-point', 'deficiency ind', 'Atiyah--Singer', 'graded index',
          'traced rather than computed')}
    print(f'    Ⓗ the graded index : {h}')
    # ** ⛭⛭⛭ RE-PINNED r3972, THE SAME WAY Ⓖ'S HALF ABOVE ALREADY WAS. **  The Ⓗ baseline was
    # ** `Fredholm` at ZERO -- index theory's first question asked nowhere -- and r3722 closed it:
    # ** "index theory's half of the shortfall closed: six clauses landed", putting a Fredholm index
    # ** of 1 into P08 with its stability consequence drawn.  ** So this audit row records a station
    # ** ANSWERED rather than a station owed, which is the same disposition ⓷ᵃ takes for Ⓖ. **
    # **   ⇒ *An audit that can only report absences reports a failure the moment its own findings
    # **     are acted on -- and both of the stations it called owed have now been paid.*
    _fred_then = sum(_at_build_counts('Fredholm').values())
    check(f'⓷ᵇ ⛔ Ⓗ was genuinely owed and its baseline was SHARPER than the theatre stated: the '
          f'corpus asserted a graded index and cited Atiyah--Singer, and `Fredholm` occurred '
          f'{_fred_then} times in seventeen papers at {_AT_BUILD}, this audit\'s own throw',
          _fred_then == 0 and h['graded index'] > 0 and h['Atiyah--Singer'] > 0
          and h['traced rather than computed'] > 0)
    check(f'⛭⛭ ⓷ᵇ¹ AND IT HAS SINCE BEEN PAID: `Fredholm` occurs {h["Fredholm"]} time(s) now, landed '
          f'at r3722 -- P08 states "a Fredholm index of $1$, generated by the constant of '
          f'integration $-2M$" and draws the stability consequence rather than stopping at the word',
          h['Fredholm'] >= 1
          and 'a Fredholm index of $1$, generated by the constant of integration $-2M$'
          in RB.BODIES['P08'])
    # ** r3249 (node 57): THE GAP THIS CHECK RECORDED IS NOW CLOSED, and the check is rewritten to
    #    say so rather than to keep asserting the absence.  Station Ⓗ made the join (L-264, r3150),
    #    57's L-265 corrected its verdict to LIMIT-CIRCLE at r3205, and P14 now carries that
    #    statement with a self-adjoint extension named as owed (OWED 622).  What the audit FOUND --
    #    that the apparatus was P10's alone and unjoined -- is what made the station worth throwing. **
    # ⛔⛭⛭ CORRECTED r3544 (node 60).  ** THE r3249 AMENDMENT WAS BUILT ON A CLAIM THE CORPUS THEN
    #   WITHDREW. **  It asserted that "P14 states the branch point limit-circle", and at r3339 the
    #   corpus reversed that in its own words -- *"I was wrong: LIMIT-POINT stands, and the corpus
    #   had decided it twice before I touched it"* -- and removed the sentence from P14.  So this
    #   check has been red ever since, and reading its red as "the join was lost" would have been
    #   exactly backwards: ** the join was never P14's to make, and the paper is RIGHT to have
    #   dropped it. **  What survives, and is checked, is that the apparatus lives in P10 and is a
    #   THRESHOLD statement rather than a verdict, and that P14 carries its index at traced weight.
    L_AT = '614466b4'         # r3339 -- where P14's limit-circle sentence was withdrawn
    p14_was = subprocess.run(['git', '-C', ROOT, 'show', f'{L_AT}^:corpus/matter_sector_paper.tex'],
                             capture_output=True, text=True, errors='replace').stdout
    check('⓷ᶜ ⌗ the machinery EXISTS in the corpus as P10\'s deficiency-index apparatus, and it is '
          'a THRESHOLD statement -- gamma = 3/4 separating limit-point from limit-circle, so whether '
          'a boundary condition must be chosen at all is decided rather than assumed',
          RB.counts('deficiency ind')['P10'] > 0
          and RB.counts('limit-circle')['P10'] > 0
          and RB.counts('limit-point')['P10'] > 0)
    check(f'⓷ᵉ ⛔ and the JOIN TO P14 IS NOT MADE, because the corpus WITHDREW it: P14 carried the '
          f'branch-point limit-circle at {L_AT}^ and r3339 removed it ("LIMIT-POINT stands"), so '
          f'P14 today carries neither term and marks its Atiyah--Singer statement as TRACED',
          bool(p14_was) and 'limit-circle' in p14_was
          and RB.counts('limit-circle')['P14'] == 0
          and RB.counts('limit-point')['P14'] == 0
          and 'traced' in B['P14'] and 'Atiyah--Singer' in B['P14'])
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
    print('  words -- the FIVE real forms of SO(6,C) enumerated, SO*(6) = SU(3,1) named, and so(4,2),')
    print('  so(3,3) and so(5,1) each excluded by an argument the paper gives.*')
    print('  ⌗ *Re-pinned r3544: P13 said FOUR when this was written and has said five since')
    print('     r3329, and this audit now reads the paper rather than its memory of it.*')
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
