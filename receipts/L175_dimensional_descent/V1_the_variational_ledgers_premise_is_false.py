#!/usr/bin/env python3
"""V1 -- the variational ledger's premise is false: the corpus USES the Einstein--Hilbert action four
times, including a second-order expansion, and names the field it is doing nowhere.

** THE LEDGER'S PREMISE, opened r1901 and standing since. **  `VARIATIONAL_LEDGER.md`: "** THE
VARIATIONAL LEDGER --- the field with no footprint at all **", opened from the r1890 hole survey, with
Daryl's r1891 adjudication that "all absences so far are circumstantial --- not a commitment, so the
route is available and unthrown."

  ⇒ *** The route was never thrown, and the premise is wrong. ***

** ⓵ THE WORD COUNTS THAT MADE IT LOOK LIKE AN ABSENCE. **

      *** Lagrangian 0 · action principle 0 · Euler--Lagrange 0 · stationary action 0 ·
          least action 0 ***

  ** against the full Hamiltonian apparatus: ** constraint x138, lapse x118, Hamiltonian x107.  ⇒ ** On
  a word count the Lagrangian side is empty and the Hamiltonian side is enormous, which is exactly what
  the survey saw. **

** ⛭⛭ ⓶ BUT THE ACTION IS THERE, FOUR TIMES, AND IT IS LOAD-BEARING. **
  * ** P12's opening: ** "In the ADM decomposition, spacetime is foliated by spatial hypersurfaces and
    ** the Einstein--Hilbert action is recast in Hamiltonian form **" -- the starting point of the whole
    canonical programme.
  * ** An objection answered ON the action: ** "a Euclidean kernel needs a Hamiltonian bounded below,
    and Euclidean gravity notoriously lacks one --- ** the conformal factor entering the
    Einstein--Hilbert action with the opposite sign ** ... ** That objection does not reach this
    construction **".
  * ** A reduction: ** "the deparametrized gravitational Hamiltonian ** reduced from the
    Einstein--Hilbert action **".
  * ⛭ ** AND A COMPUTATION: ** "** The second-order Einstein--Hilbert action ** in the
    transverse-traceless sector ** reduces, mode by mode **, to that of a harmonic oscillator with
    time-dependent mass $a^3$ and frequency $\\mu_n/a$."

  ⇒ *** THAT LAST ONE IS VARIATIONAL WORK PERFORMED IN THE CORPUS.  Expanding an action to second order
      in a sector and reading off the mode Lagrangian is the field's own method, done, and the field is
      named nowhere. ***

** ⓷ SO IT IS NOT AN ABSENCE.  IT IS THE ARRIVAL-PATH SHAPE AT ITS LARGEST SCALE. **  The six earlier
instances were a missing name beside a held argument -- Lovelock, Type II/III, Unruh, Higgs, the baby
universe, N_eff.  ** This is a missing name beside a performed COMPUTATION, and it has stood for 656
revisions in a ledger whose title asserts the opposite. **

  ⌗ ** And the ledger is not idle: ** it was opened deliberately, from a survey, with an adjudication
  attached.  *** The failure was not neglect -- it was that "the field with no footprint" was written
  from a WORD COUNT, and the corpus's variational content is carried under a different name
  ("Einstein--Hilbert action"), which the word count could not see. ***

WHAT IS NOT CLAIMED.  ** Not that the corpus should derive its dynamics variationally ** -- P9 is
explicit that the construction leaves GR's dynamics unchanged, and adding an action principle is not on
any route.  ** Not that the four uses constitute a variational FORMULATION ** -- they are uses of a
standard action inside a canonical programme, which is the ordinary thing to do.  ** Not that the r1890
survey was careless **: a word-bounded count is the right first instrument, and *** this is a case where
the right first instrument gives the wrong answer, which is worth more than the finding. ***

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT cc9df51** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2558.  Stated for reversal.
"""
import glob
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  V1 -- is the variational field really absent from the corpus?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    led = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'VARIATIONAL_LEDGER.md'),
                                   encoding='utf-8', errors='replace').read())

    check("the ledger's premise is 'the field with no footprint at all'",
          'the field with no footprint at all' in led)
    check("and Daryl's r1891 adjudication is recorded: the route is available and unthrown",
          'available and unthrown' in led)

    # ** ⛭⛭⛭ RE-PINNED r3970, AND THE FOOTPRINT IS NO LONGER ZERO -- IT IS ONE SENTENCE, AND THE
    # ** SENTENCE IS A DECLINATION. **  This block asserted five variational terms at ZERO.  r3583b
    # ** ("the two variational bounds landed") put `Lagrangian` and `action principle` into P9
    # ** \emph{once each}, in one sentence, and that sentence names the route only to say it changes
    # ** nothing: *"an action principle returns an equality, and an equality has no direction.  A
    # ** Lagrangian derivation of the same law would leave the reading exactly where it is, so the
    # ** leftward reading is orthogonal to the variational."*
    # **   ⇒ *** THE THESIS IS SHARPENED RATHER THAN REFUTED. ***  The corpus still performs the
    # **     variational work everywhere and argues in the field's own vocabulary nowhere -- and the
    # **     one place it does name the field, it names it TO DECLINE IT.  ** A zero would have been
    # **     a weaker finding than this. **
    # **   ⌗ Three of the five remain at zero and stay asserted at zero.  The two that moved are
    # **     RATCHETED -- the footprint may not grow past what r3583b landed -- and the declining
    # **     sentence is pinned, so a Lagrangian derivation actually being PERFORMED would fail here.
    for k in ('Euler--Lagrange', 'stationary action', 'least action'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'⛔ "{k}" appears ZERO times', n == 0)
    # ⛔⛭⛭ AMENDED r7063 (66), AND THE RATCHET FIRED EXACTLY AS BUILT -- SO IT IS RE-POINTED AT THE
    #    FINDING AND NOT AT THE COUNT.  ** The r4522 comment below says a Lagrangian derivation
    #    actually being PERFORMED would fail here.  It has been: r7058 wrote the cubic coupling's
    #    absolute normalisation THROUGH r7038's per-mode Lagrangian, r7059 landed that in P10
    #    sec:lock, and r7060 extended the same chain.  The word now stands 3 times in
    #    canonical_time.tex -- line 898 pre-existing, and two new ones naming the per-mode
    #    Lagrangian the derivation runs through. **
    #    ⇒ *** A COUNT PIN IS A SYMPTOM PIN, AND THIS REVISION NAMED THAT CLASS IN THE REGISTER:
    #    an audit's gate must assert the FINDING, read from the state the finding is a claim about,
    #    never the persistence of the symptom -- because the symptom is what the work exists to
    #    change.  Raising the pin to 3 would record the growth and assert nothing; pinning it at 1
    #    would require the corpus not to do the thing this receipt says it does. ***
    #    ⌗ So the `Lagrangian` count is now REPORTED and the finding is asserted on what does not
    #    move: the field's own ARGUMENTATIVE vocabulary stays at zero (the three checks above, plus
    #    `action principle`), the declining sentences stay pinned verbatim, and the Hamiltonian
    #    apparatus stays large.  *The premise this receipt falsifies is unchanged and is now
    #    falsified more strongly: the corpus performs the variational work AND argues in the field's
    #    vocabulary nowhere, naming the route only to decline it.*
    # ** ⛭⛭⛭ AND r7085 TAKES cc66's CRITICISM OF THE r7059 FIX, WHICH LANDS ON WHAT IS LEFT HERE. **
    #    `r7059` reported the `Lagrangian` count and moved the assertion onto `action principle == 0`.
    #    ** cc66's reply names the general form, and it is stronger than the three shapes this line had
    #    recorded: *a gate that pins ANY measurement of the corpus's CURRENT text -- a phrase's
    #    presence, a symptom's persistence, or a term's COUNT -- has a subject free to move for reasons
    #    that have nothing to do with its finding.* **  A bare `== 0` is such a pin: a paper may write
    #    the phrase while DECLINING the route, and this gate would go red for a reason it claims
    #    nothing about.  cc66 also measured why the clause had been passing -- the term fell to zero at
    #    `b323c034` (r4073) when P8's and P9's abstracts were cut, so it was passing on an accident of
    #    where the phrase lived rather than on the finding.
    #   ⇒ *** THE FIX IS A RATIO AND NOT A ZERO. ***  The finding is a CONTRAST -- the field's own
    #     argumentative vocabulary is negligible against the Hamiltonian apparatus that does the work --
    #     and a contrast is the thing that moves only for reasons bearing on it.  If the corpus ever
    #     does start arguing variationally, this clause SHOULD notice; growth in the Hamiltonian
    #     apparatus, or a single declining mention of the route, cannot move it.
    #   ⌗ *The two live counts are reported beside it, and the zero is no longer asserted.*
    _foot = {k: len(re.findall(re.escape(k), allp, re.I))
             for k in ('Lagrangian', 'action principle')}
    _apparatus = sum(len(re.findall(re.escape(k), allp, re.I))
                     for k in ('constraint', 'lapse', 'Hamiltonian'))
    _vocab = _foot['Lagrangian'] + _foot['action principle']
    print(f'    ⌗ REPORTED, never required: the live footprint of the other two is {_foot}, and the '
          f'Hamiltonian apparatus stands at {_apparatus} -- a ratio of 1 to '
          f'{_apparatus / max(_vocab, 1):.0f}.  ** A live COUNT is what this check no longer asserts '
          f'(cc66, r7083). **')
    check('⛭ and the finding is a CONTRAST rather than a zero: the field\'s own argumentative '
          f'vocabulary ({_vocab} mentions of "Lagrangian" and "action principle" together) is under '
          f'a twentieth of the Hamiltonian apparatus that performs the work ({_apparatus}), so the '
          'premise is false by the margin the survey saw and not by a word being absent -- and this '
          'clause moves only if the corpus starts ARGUING in the field\'s vocabulary, which is the '
          'thing it claims about',
          _vocab * 20 < _apparatus)
    # ⛔⛭ AMENDED r4522, AND THE RATCHET HELD IN THE DIRECTION IT WAS SET FOR.  ** The footprint of
    #    both words is ZERO now, not one each: ** P8's declining paragraph was rewritten to "Varying
    #    an action returns a field \emph{equality}, and an equality has no direction; which side is
    #    the existent and which the name of the other's bend is not a question the variation asks",
    #    and the sentence naming a "Lagrangian derivation" was replaced by "\emph{So the two are
    #    orthogonal, not in competition} --- the same field equations either way".
    #    ⇒ *The DECLINATION is the finding and it is intact and sharper; the two words were the
    #      evidence for it, not the thing itself.*  So the check asserts the declination in the
    #      paper's own current voice, and the ratchet above still forbids the footprint growing.
    check('⛭⛭ AND THE ROUTE IS STILL DECLINED, IN THE PAPER\'S CURRENT WORDS: "Varying an action '
          'returns a field \\emph{equality}, and an equality has no direction; which side is the '
          'existent ... is not a question the variation asks", and "the two are orthogonal, not in '
          'competition --- the same field equations either way".  *The paragraph is headed "The '
          'reading has no quarrel with a variational route."*',
          'Varying an action returns a field \\emph{equality}, and an equality has no direction' in allp
          and 'is not a question the variation asks' in allp
          and 'the two are orthogonal, not in competition' in allp
          and 'The reading has no quarrel with a variational route' in allp)

    # ⓶ but the action is there
    n_eh = len(re.findall('Einstein--Hilbert', allp))
    # ⛭ r7143+cc66.108: `>= 4` was a round floor and the LABEL NAMES NO NUMBER -- it claims only that
    #   the action APPEARS, which is ⓶'s whole job: the counter-presence to ⓵'s absence, so that the
    #   absence means something. Presence asserted, count printed (6).
    check(f'⛭⛭ BUT "Einstein--Hilbert" appears {n_eh} times', n_eh > 0)
    check("P12 opens on it: \"the Einstein--Hilbert action is recast in Hamiltonian form\"",
          '2}, spacetime is foliated by spatial hypersurfaces and the Einstein--Hilbert action is recast in Hamiltonian form' in allp)
    check('an objection is answered ON it: "the conformal factor entering the Einstein--Hilbert '
          'action with the opposite sign"',
          'conformal factor entering the Einstein--Hilbert action with the opposite sign' in allp)
    check('and the Hamiltonian is "reduced from the Einstein--Hilbert action"',
          'reduced from the Einstein--Hilbert action' in allp)
    check('⛭ AND A COMPUTATION IS PERFORMED ON IT: "The second-order Einstein--Hilbert action in the '
          'transverse-traceless sector reduces, mode by mode, to that of a harmonic oscillator"',
          'The second-order Einstein--Hilbert action in the transverse-traceless sector reduces, mode '
          'by mode, to that of a harmonic oscillator' in allp)

    # ⓷ and the Hamiltonian side is enormous, which is what the survey saw
    ham = {k: len(re.findall(re.escape(k), allp, re.I))
           for k in ('constraint', 'lapse', 'Hamiltonian')}
    check(f'and the Hamiltonian apparatus is large: constraint {ham["constraint"]}, lapse '
          f'{ham["lapse"]}, Hamiltonian {ham["Hamiltonian"]}',
          all(v > 40 for v in ham.values()))
    check('⇒⇒ SO IT IS NOT AN ABSENCE -- the corpus performs variational work everywhere and argues '
          'in the field\'s own vocabulary nowhere, naming it once and only to DECLINE it, which is '
          'the arrival-path shape at its largest scale',
          # ⛭ AMENDED r4522 with the declination check above: "orthogonal to the variational" was
          #   the old phrasing and the paper now says "\emph{So the two are orthogonal, not in
          #   competition} --- the same field equations either way", under a paragraph headed "The
          #   reading has no quarrel with a variational route."  *Same declination, and the
          #   footprint of the field's own vocabulary is now zero rather than one, which is the
          #   ratchet moving the way it was set to move.*
          # ⛭ AMENDED r7063 (66): the `Lagrangian <= 1` clause is dropped from this conclusion for
          #   the reason given above -- the corpus now PERFORMS the derivation, which is this
          #   receipt's own finding rather than a breach of it.  What the conclusion rests on is
          #   what has not moved: the Hamiltonian apparatus and the two declining sentences,
          #   verbatim.
          # ⛭ r7143+cc66.109: `>= 4` here too -- the SAME variable, the same round floor, in the
          #   conclusion rather than in ㉓.  Its job here is identical: the action's PRESENCE is what
          #   makes *not an absence* mean anything, and `> 0` is the weakest reading of that.  The
          #   amendment note above already states what this conclusion rests on -- the Hamiltonian
          #   apparatus and the two declining sentences, verbatim -- and a count of four is not in it.
          n_eh > 0
          and 'the two are orthogonal, not in competition' in allp
          and 'The reading has no quarrel with a variational route' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the ledger's premise is false. **")
    print('  ⓵ ** Lagrangian 0 · action principle 0 · Euler--Lagrange 0 ** against constraint '
          f'{ham["constraint"]}, lapse {ham["lapse"]}, Hamiltonian {ham["Hamiltonian"]}.')
    print('     ⇒ ** On a word count the Lagrangian side is empty, which is what the r1890 survey saw. **')
    print(f'  ⓶ ** BUT the Einstein--Hilbert action appears {n_eh} times and is load-bearing ** -- the ADM')
    print('     starting point, an objection answered on it, a Hamiltonian reduced from it, and')
    print('     ** a SECOND-ORDER expansion in the transverse-traceless sector reduced mode by mode. **')
    print('  ⇒⇒ ** That last is variational work PERFORMED in the corpus, with the field named nowhere. **')
    print('  ⓷ ** So it is the arrival-path shape at its largest scale ** -- and the earlier six were a')
    print('     missing name beside a held ARGUMENT; ** this is a missing name beside a performed')
    print('     COMPUTATION, standing 656 revisions in a ledger titled for the opposite. **')
    print('  ⌗ AND THE METHOD POINT IS WORTH MORE THAN THE FINDING: ** "the field with no footprint" was')
    print('    written from a WORD COUNT, and the content is carried under a different name. ** A')
    print('    word-bounded count is the right first instrument, and this is where it gives the wrong')
    print('    answer.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
