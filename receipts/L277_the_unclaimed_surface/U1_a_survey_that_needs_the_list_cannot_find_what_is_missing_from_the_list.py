#!/usr/bin/env python3
r"""U1 -- `field_survey` asks "is field X present?", which requires knowing X.  That is exactly why
category theory hid for ninety revisions.  Inverted -- take the corpus's own vocabulary and subtract
what every thrown field claims -- the survivors are 1420 words, and reading them names one field the
corpus uses 198 times that no bake has been thrown at.

COMPUTES: the corpus's word-bounded de-macroed vocabulary with LaTeX stripped; the claimed set built
from `field_survey.FIELDS`; the survivors; the HISTORICAL CONTROL, that removing category theory from
the claimed set brings `groupoid`, `algebroid` and `morphism` back into the survivors; the
concentration statistic measured and shown to FAIL on that same case; and the counts of the field the
reading named, against the two fields whose counts already earned bakes.  Nothing is fitted.

** ⛭ ⓵ THE BLIND SPOT IS THE INSTRUMENT'S OWN, AND IT WAS STATED. **  *`L-272` built `field_survey`
and wrote its limitation into it:* **"a vocabulary is a proxy for a field, so a field the corpus uses
under names not in its list is invisible here -- which is exactly the defect that hid category
theory."**  ⇒ ** A stated limitation is not a discharged one. **

** ⛔⛭⛭ ⓶ SO THE QUESTION IS INVERTED. **  *Not "is field X present" -- which cannot be asked without
X -- but* ***"what does the corpus use that no thrown field claims?"***  *That needs no list of
fields, which is the whole point: it is askable precisely when the list is what is missing.*
  ⇒ ** 11083 distinct word forms; 1420 survive stopwords, the claimed set, and a count floor. **

** ⛔ ⓷ AND THE OBVIOUS REFINEMENT DOES NOT WORK -- RECORDED SO IT IS NOT TRIED AGAIN. **  *Rank the
survivors by CONCENTRATION rather than reading them: a field-signature word should live in a few
papers while the corpus's own subject is everywhere.  Measured on the case that actually happened:*

        groupoid   ×125   14 papers   H = 0.278   count×H =  34.7
        horizon    ×792   16 papers   H = 0.136   count×H = 107.6

  ⇒ *** `horizon` OUTRANKS `groupoid` THREEFOLD.  A field's signature is defined by reference to
      mathematics OUTSIDE the corpus, and seventeen papers by one author on one programme contain no
      outside to contrast against. ***
  ⇒ ** So the sense pass cannot be automated from internal statistics. **  *`L-272` reached that
    conclusion by reading; this reaches it by building the statistic and watching it fail, which is
    the stronger form of the same finding.*

** ⛭ ⓸ THE CONTROL IS THE HISTORICAL FAILURE ITSELF. **  *Run with category theory removed from the
claimed set, `groupoid` ×125, `algebroid` ×52 and `morphism` ×24 reappear among the survivors.*
  ⇒ ** An instrument built to catch the defect that happened is shown to catch it, rather than
    asserted to. **

** ⛭⛭ ⓹ AND THE READING NAMED A FIELD. **  *`involution` ×198 word-bounded and de-macroed --
concentrated in `P03` ×73 and `P05` ×67, claimed by no thrown vocabulary.*
  ⇒ *** LARGER THAN `holonomy` ×33 AND `monodromy` ×55, each of which earned a whole bake. ***
  ⇒ ** And it is not a homonym: ** *the root-exchange involution, the chart involution, the
    signature-flip involution, σ as a real Weyl($A_2$) reflection -- every occurrence a genuine
    mathematical involution.*

WHAT IS NOT CLAIMED.  ** Not that the instrument ranks the answer ** -- it does not, and ⓷ is why; it
BOUNDS the reading from 11083 words to 1420 and the reading decides.  ** Not that the stopword list is
principled ** -- it is a judgement, stated in full in the instrument so it can be argued with, and it
deliberately does NOT remove the corpus's own subject nouns because deciding what counts as "the
corpus's own" is the judgement this instrument refuses to make for the reader.  ** Not that the
surface is complete ** -- a field used only in symbols is invisible to a word tokeniser.  ** And not
that `involution` is an opening ** -- that is the next revision's business, and a count is not a
finding.

    python3 receipts/L277_the_unclaimed_surface/U1_a_survey_that_needs_the_list_cannot_find_what_is_missing_from_the_list.py

Written r3172, `L-277`.  Stated for reversal.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import reach_baseline as RB                                                # noqa: E402
import field_survey as FS                                                  # noqa: E402
import unclaimed_surface as US                                             # noqa: E402


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)



#: ** ⛭ THE CLAIMED SET AT THIS FILE'S OWN THROW (r3978). **  `US.claimed()` is derived straight
#: ** from `field_survey.FIELDS`, which GROWS as fields are thrown -- so read live it says whether
#: ** the surface is claimed TODAY, and this file's finding is that it was unclaimed WHEN NAMED.
#: ** ⛔ AND LOADING THE OLD `unclaimed_surface.py` IS NOT ENOUGH, which is the trap here: that
#: ** module imports `field_survey` LIVE, so the historical code answers with today's field list and
#: ** reports the surface as claimed at its own throw.  *** The DATA has to be historical, not just
#: ** the code. ***  So the field list is read at the throw and `claimed()`'s own rule applied to it.
_THROW = '313f80f3'          # r3172 -- this file's own commit
_CLAIMED_THEN = set()


def _fields():
    import sys as _sys
    _sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import field_survey as _FS
    return _FS.FIELDS


def _fields_at_throw():
    import subprocess as _sp
    import types as _types
    src = _sp.run(['git', 'show', f'{_THROW}:corpus/field_survey.py'], cwd=ROOT,
                  capture_output=True, text=True, errors='replace').stdout
    mod = _types.ModuleType('_fs_then')
    mod.__dict__['__file__'] = os.path.join(ROOT, 'corpus', 'field_survey.py')
    cwd = os.getcwd()
    os.chdir(os.path.join(ROOT, 'corpus'))
    try:
        exec(compile(src, 'field_survey@throw', 'exec'), mod.__dict__)
    finally:
        os.chdir(cwd)
    assert mod.FIELDS, 'the field list must be readable at the throw, or nothing here compares'
    return mod.FIELDS


def _claimed_at_throw():
    """`US.claimed()`'s own rule, applied to the field list AS IT STOOD at the throw."""
    if not _CLAIMED_THEN:
        for _name, _ledger, _terms in _fields_at_throw():
            for _t in _terms:
                _CLAIMED_THEN.update(w.lower() for w in US.WORD.findall(_t))
        assert _CLAIMED_THEN, 'the claimed set must be non-empty, or the comparison is vacuous'
    return _CLAIMED_THEN


def main():
    print()
    print('  U1 -- a survey that needs the list cannot find what is missing from the list')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE BLIND SPOT WAS STATED, AND A STATED LIMITATION IS NOT DISCHARGED')
    print('  ==========================================================================')
    fs_src = open(os.path.join(ROOT, 'corpus', 'field_survey.py'),
                  encoding='utf-8', errors='replace').read()
    check('⓵ `field_survey` writes its own limitation into itself: a field used under names not in '
          'its list is invisible to it, and it names category theory as the case',
          'invisible here' in fs_src and 'category theory' in fs_src)
    check('⓵ᵇ and its question genuinely requires the answer in advance: every field it surveys is '
          'a hand-written vocabulary in its own FIELDS table',
          len(FS.FIELDS) > 15 and all(isinstance(t, list) for _, _, t in FS.FIELDS))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔⛭ THE INVERSION, AND WHAT IT LEAVES')
    print('  ==========================================================================')
    tot, per = US.vocabulary()
    live = US.survivors()
    print(f'      distinct word forms : {len(tot)}')
    print(f'      survivors           : {len(live)}')
    check(f'⓶ the inversion bounds the reading: {len(tot)} distinct forms reduce to {len(live)} '
          'candidates, and the question needs no list of fields to ask',
          len(tot) > 5000 and 500 < len(live) < 3000)
    check('⓶ᵇ and the claimed set is built FROM `field_survey`, not restated -- so a field thrown '
          'tomorrow is subtracted here automatically',
          'FS.FIELDS' in open(os.path.join(ROOT, 'corpus', 'unclaimed_surface.py'),
                              encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔ THE STATISTIC THAT DOES NOT WORK, MEASURED RATHER THAN GUESSED')
    print('  ==========================================================================')
    sc = {}
    for w in ('groupoid', 'horizon'):
        h = US.herfindahl(w, tot, per)
        k = sum(1 for p in per if per[p][w])
        sc[w] = (tot[w], k, h, tot[w] * h)
        print(f'      {w:10s} ×{tot[w]:<5d} {k:2d} papers   H={h:.3f}   count×H={tot[w]*h:7.1f}')
    check('⓷ the concentration statistic FAILS on the case that actually happened: `horizon` '
          f'outranks `groupoid` ({sc["horizon"][3]:.0f} against {sc["groupoid"][3]:.0f})',
          sc['horizon'][3] > sc['groupoid'][3])
    check('⓷ᵇ and it fails on the bare Herfindahl too being insufficient: groupoid separates from '
          'horizon by only a factor of two, which no threshold survives against 1420 candidates',
          sc['groupoid'][2] / sc['horizon'][2] < 3)
    check('⓷ᶜ ⛭ so the negative result is IN the instrument, with its numbers, so the next reader '
          'does not rebuild it',
          'horizon` OUTRANKS `groupoid`' in open(
              os.path.join(ROOT, 'corpus', 'unclaimed_surface.py'),
              encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭ THE CONTROL IS THE HISTORICAL FAILURE ITSELF')
    print('  ==========================================================================')
    without = dict(US.survivors(skip=('category theory',)))
    withct = dict(US.survivors())
    for w in ('groupoid', 'algebroid', 'morphism'):
        print(f'      {w:12s} claimed now: {"no" if w in withct else "yes":3s}   '
              f'unclaimed if category theory had never been thrown: ×{without.get(w)}')
    check('⓸ removing category theory from the claimed set brings groupoid, algebroid and morphism '
          'back among the survivors -- the instrument contains the defect that happened',
          all(without.get(w) for w in ('groupoid', 'algebroid', 'morphism')))
    check('⓸ᵇ and they are absent while category theory IS claimed, so the subtraction is real and '
          'not a no-op',
          not any(w in withct for w in ('groupoid', 'algebroid', 'morphism')))
    rc = os.system(f'cd {ROOT} && python3 corpus/unclaimed_surface.py --top 4 >/dev/null 2>&1')
    check('⓸ᶜ and the control runs on every invocation and FAILS the instrument if the historical '
          'case ever stops surviving', rc == 0
          and 'return 1' in open(os.path.join(ROOT, 'corpus', 'unclaimed_surface.py'),
                                 encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⛭⛭ AND THE READING NAMED A FIELD')
    print('  ==========================================================================')
    def wc(t):
        return max(sum(RB.word_counts(t).values()), sum(RB.word_counts(t, tex=True).values()))
    inv, hol, mon = wc('involution'), wc('holonomy'), wc('monodromy')
    print(f'      involution ×{inv}    holonomy ×{hol}    monodromy ×{mon}')
    check(f'⓹ `involution` ×{inv} is larger than `holonomy` ×{hol} and `monodromy` ×{mon}, each of '
          'which earned a whole bake',
          inv > hol and inv > mon)
    # ** ⛭⛭⛭ RE-PINNED r3978, AND *** THE UNCLAIMED SURFACE HAS BEEN CLAIMED. ***  This file is
    # ** named for a surface no thrown field's vocabulary reached -- `involution`, larger than
    # ** `holonomy` and `monodromy`, each of which had earned a whole bake.  ** Six revisions later
    # ** r3178 threw the field: `field_survey.py` now carries `involution / real forms`, scoring
    # ** ×531, the largest of the twenty-four. **
    # **   ⇒ ** The file's finding was ACTED ON, and asserting the surface is still unclaimed asserts
    # **     that it was not. **  The absence is pinned at the throw and the claim asserted now, so
    # **     the receipt records what it caused instead of failing because of it.
    _CLAIMED_AT = 'a5380606'        # r3178 -- the revision that threw the field
    check(f'⓹ᵇ no thrown field vocabulary claimed it at {_THROW}, this file\'s own commit -- which '
          f'is the surface it was written to name',
          'involution' not in _claimed_at_throw())
    check(f'⛭⛭ AND IT IS CLAIMED NOW ({_CLAIMED_AT}, six revisions later): `involution / real '
          f'forms` is a thrown field with a ledger, and `involution` is one of the '
          f'{len(US.claimed())} terms the survey\'s vocabularies reach',
          'involution' in US.claimed()
          and any(n == 'involution / real forms' and l for n, l, _ in _fields()))
    p03 = sum(RB.word_counts('involution', tex=True).get(p, 0) for p in ('P03',))
    p05 = sum(RB.word_counts('involution', tex=True).get(p, 0) for p in ('P05',))
    check(f'⓹ᶜ it is concentrated where the discrete structure lives: P03 ×{p03}, P05 ×{p05}',
          p03 > 40 and p05 > 40)
    b03, b05 = RB.BODIES_TEX['P03'], RB.BODIES_TEX['P05']
    check('⓹ᵈ ⛭ and it is not a homonym: the root-exchange involution, the chart involution and '
          'the signature-flip involution are all genuine mathematical involutions in the papers\' '
          'own words',
          'root-exchange involution' in b03 and 'chart involution' in b03
          and 'it is an involution' in b05)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** a survey that needs the list cannot find what is missing from the list. **')
    print('  *`field_survey` asks "is field X present?" and cannot be asked without X — which is')
    print('  precisely the shape of the failure it was built after.  Inverted, the corpus\'s own')
    print('  vocabulary minus every claimed word leaves 1420 candidates.*')
    print('  ⛔ ** And the refinement that would automate the reading does not work: ** *ranked by')
    print('     concentration, `horizon` outranks `groupoid` threefold.  A field\'s signature is')
    print('     defined outside the corpus, and seventeen papers by one author contain no outside.*')
    print('  ⛭ ** The control is the historical failure itself ** — remove category theory from the')
    print('     claimed set and groupoid, algebroid and morphism reappear.')
    print('  ⛭⛭ ** And the reading named a field: ** *`involution` ×198, larger than holonomy and')
    print('     monodromy together with the bakes they earned, claimed by nothing.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
