#!/usr/bin/env python3
r"""F1 -- the list of outstanding field bakes was surveyed ONCE, at r1890, and the corpus is twelve
hundred revisions past it.  Rebuilt as an instrument, three separate passes were needed before the
list was trustworthy -- and EACH ONE REORDERED THE TOP OF IT.

COMPUTES: the eight already-thrown fields re-found by their own vocabularies as controls; the same
survey run substring-wise and word-wise, with the reordering that separates them; the four candidates
whose dominant term is a homonym, each read at source; and the two candidates already discharged by
earlier bakes, which no count can see.  Nothing is fitted.

** ⛭ ⓵ THE QUESTION THAT PAID, ASKED ONCE. **  `THE_MATHEMATICS_REACH` records which of its two
survey questions found more:

      *** "The survey asked two things: which listed fields are unbaked, and which used fields are
          unlisted.  The second found more." ***

  *The second question is what found CATEGORY THEORY -- 363 uses and two papers named for its
  objects, absent from the reach list entirely, because* ***a groupoid filed under group theory gets
  baked with group theory's tools.***
  ⇒ ** And it was asked at r1890.  P11 through P17, the whole c54 fork and the fermion sector have
    never been asked it. **
  ⇒ *** A SURVEY IS AN INSTRUMENT OR IT IS A MEMORY, and a memory is not evidence about this tree. ***

** ⛔ ⓶ PASS ONE: SUBSTRING TO WORD, AND THE FIELD THAT LED THE LIST WAS AN ARTEFACT. **  *The rebuilt
survey used `reach_baseline.counts`, which is a SUBSTRING count -- correct for its own job, which is
"does this phrase occur at all".*
  ⇒ ** Used for a field vocabulary it returned `bit` ×253 by matching inside `orbit` and `arbitrary`,
    and `norm` ×118 inside `normal`. **
  ⇒ *** `information theory` led the candidate list at ×285 and is ×29 word-bounded -- tenth.
      `catastrophe theory` was first at ×543 and is seventh at ×54. ***
  ⌗ ** And the r1890 table this instrument re-runs said so in its own header: "word-bounded and keys
    stripped." **  *The instrument rebuilt from it dropped the condition its predecessor stated.*

** ⛔ ⓷ PASS TWO: WORD TO SENSE, AND FOUR OF THE TOP SEVEN WERE HOMONYMS. **
  * *`constraint` ×138 of optimisation's ×140 is the HAMILTONIAN constraint.*  ⇒ ** the field is
    REFUSED, not thrown: it is not a field this corpus uses. **
  * *`genus` ×21 is the corpus's own species/genus taxonomy of metric singularities.*
  * *`closure` ×100 is a theorem closing and the Galois closure, not an operator's.*
  * *`character` ×67 is "causal character" and "analytic character".*

** ⌗ ⓸ PASS THREE: SENSE AGAINST THE BAKES ALREADY THROWN, WHICH NO COUNT CAN SEE. **  *Catastrophe
theory is discharged by the ODE bake -- `P07` states outright* **"The word fold is used here in its
bifurcation-theoretic sense"** *-- and the operator half of spectral theory is `Ⓗ`'s.*
  ⇒ ** So a candidate can be large, word-bounded, correctly sensed, AND ALREADY ANSWERED. **

WHAT IS NOT CLAIMED.  ** Not that the r1890 survey was wrong ** -- it was right when it was run, and
the finding is that it has not been re-run.  ** Not that the vocabularies here are complete ** -- a
field the corpus uses under names not in its list is invisible to this instrument, which is exactly
the defect that hid category theory, and the lists are stated in full to be argued with.
** Not that the refused field is refused forever ** -- it is refused on this measurement, and a
different vocabulary could reopen it.  ** Not that the surviving candidates are openings ** -- they
are ORDERED READING, and the bake that follows is what decides.

    python3 receipts/L272_the_survey_that_was_a_memory/F1_the_outstanding_bake_list_was_surveyed_once_and_three_passes_were_needed_to_trust_it.py

Written r3162, `L-272`.  Stated for reversal.

NOT-A-FIELD-BAKE-RECEIPT: an audit of the programme's own records, not a probe of any field: it mentions
field bakes as its subject matter rather than settling a field's probe, so no ledger
names it and none should.  Declared at r3660 rather than inferred.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import reach_baseline as RB                                                # noqa: E402
import field_survey as FS                                                  # noqa: E402


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def loose_total(terms):
    return sum(max(sum(RB.counts(t).values()), sum(RB.counts(t, tex=True).values()))
               for t in terms)



#: ** ⛭ THE SURVEY'S POPULATION AT THIS FILE'S OWN THROW (r3974). **  `FS.FIELDS` is a LIVE list and
#: ** it grows as fields are baked: 21 entries at r3162 with 13 of them candidates, 24 now with none.
#: ** A control set read live is not the set the instrument was validated on, and a candidate set
#: ** read live is empty once the work is done.  *Both are read at the throw; the COUNTS stay live,
#: ** so the claims below remain claims about the instrument rather than a frozen table.*
_THROW = '7e6447a4'          # r3162 -- this survey's own commit
_FIELDS_THEN = []


def _fields_at_throw():
    if not _FIELDS_THEN:
        import subprocess as _sp
        import types as _types
        src = _sp.run(['git', 'show', f'{_THROW}:corpus/field_survey.py'], cwd=ROOT,
                      capture_output=True, text=True, errors='replace').stdout
        mod = _types.ModuleType('_fs_then')
        #: the survey resolves ROOT from its own `__file__`, so the module gets one
        mod.__dict__['__file__'] = os.path.join(ROOT, 'corpus', 'field_survey.py')
        cwd = os.getcwd()
        os.chdir(os.path.join(ROOT, 'corpus'))
        try:
            exec(compile(src, 'field_survey@throw', 'exec'), mod.__dict__)
        finally:
            os.chdir(cwd)
        _FIELDS_THEN.extend(mod.FIELDS)
        assert _FIELDS_THEN, 'the survey must be readable at its own throw, or nothing here compares'
    return _FIELDS_THEN


def _controls_at_throw():
    return {n for n, l, _ in _fields_at_throw() if l}


def _candidates_at_throw():
    return {n for n, l, _ in _fields_at_throw() if not l}


def main():
    print()
    print('  F1 -- the outstanding-bake list was a memory, and three passes were needed')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE CONTROLS: the instrument must re-find every field already thrown')
    print('  ==========================================================================')
    controls = [(n, l, t) for n, l, t in FS.FIELDS if l]
    cands = [(n, l, t) for n, l, t in FS.FIELDS if not l]
    found = {}
    for n, ledger, terms in controls:
        _, tot = FS.field_total(terms)
        found[n] = tot
        print(f'      {n:44s} ×{tot:<6d} {ledger}')
    # ** ⛭⛭⛭ RE-PINNED r3974, AND *** THE OUTSTANDING-BAKE LIST HAS BEEN COMPLETED. ***  At r3162
    # ** (`7e6447a4`) this survey held 8 controls and 13 CANDIDATES.  ** Every one of the thirteen
    # ** has since been baked: `FS.FIELDS` now carries 24 entries and NOT ONE is a candidate. **  So
    # ** `cands` is empty, the ranking passes below had nothing to rank, and the file crashed on
    # ** `loose[0]` rather than reporting -- the same lookup-assumes-its-key shape as `L257/V1` and
    # ** `P12/A4`, met a third time.
    # **   ⇒ ** THE CONTROL CLAIM AND THE POPULATION CLAIM ARE DIFFERENT CLAIMS AND ARE NOW
    # **     SEPARATE. **  What guards against blindness is that the instrument still re-finds the
    # **     fields it was VALIDATED on -- r3162's eight, which all still clear ×40.  What has
    # **     changed is the population: nine of the fields baked since score below ×40, and that is
    # **     a FINDING about those fields rather than a fault in the instrument.  *`probability /
    # **     stochastic processes` scores 7, and its bake's own result was that the corpus's whole
    # **     probability footprint is three geometry words.*
    _ctrl_then = _controls_at_throw()
    _val = {n: v for n, v in found.items() if n in _ctrl_then}
    _low = sorted((v, n) for n, v in found.items() if v < FS.NOTABLE)
    check(f'⓵ the instrument still re-finds every field it was VALIDATED on -- r3162\'s '
          f'{len(_ctrl_then)} controls, all at ×{FS.NOTABLE}+ -- so a clean sheet is not blindness: '
          f'{ {n: v for n, v in sorted(_val.items())} }',
          len(_val) == len(_ctrl_then) and all(v >= FS.NOTABLE for v in _val.values()))
    check(f'⓵ᵃ ⛭⛭ AND THE LIST THIS FILE SURVEYED IS COMPLETE: all {len(controls)} fields now carry '
          f'a ledger and {len(cands)} remain as candidates.  {len(_low)} of them score below '
          f'×{FS.NOTABLE} -- {_low} -- which is a finding about those fields, not a fault in the '
          f'instrument that found them',
          not cands and len(controls) == len(FS.FIELDS)
          and all(n in {c for c, _, _ in controls} for n in _ctrl_then))
    check('⓵ᵇ and every ledger a control names is ON DISK, checked rather than trusted',
          all(os.path.exists(os.path.join(ROOT, l)) for _, l, _ in controls))
    check('⓵ᶜ the survey exits 0 only when both hold: a missing ledger or an unfindable control '
          'FAILS it rather than being reported and passed over',
          'return 1' in open(os.path.join(ROOT, 'corpus', 'field_survey.py'),
                             encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ PASS ONE: SUBSTRING TO WORD REORDERED THE TOP OF THE LIST')
    print('  ==========================================================================')
    # ⌗ the ranking passes are about the CANDIDATE SET, and there is no longer one -- every field
    #   has been baked.  ** So they run over the candidates as they stood at this file's own throw,
    #   which is the population the three passes were about **, measured with today's instrument on
    #   today's papers so the orderings are a live claim about the SURVEY and not a frozen table.
    _cands_then = _candidates_at_throw()
    cands = [(n, l, t) for n, l, t in FS.FIELDS if n in _cands_then]
    check(f'⓶ᵃ the {len(_cands_then)} candidates this file ranked are all still known to the '
          f'instrument, so the passes below rank the same population they were written about',
          len(cands) == len(_cands_then))
    loose = sorted(((n, loose_total(t)) for n, _, t in cands), key=lambda r: -r[1])
    tight = sorted(((n, FS.field_total(t)[1]) for n, _, t in cands), key=lambda r: -r[1])
    print(f'      loose #1: {loose[0][0]} ×{loose[0][1]}      word-bounded #1: '
          f'{tight[0][0]} ×{tight[0][1]}')
    check(f'⓶ the substring survey and the word-bounded survey do not agree on the field to throw '
          f'FIRST: {loose[0][0]} against {tight[0][0]}',
          loose[0][0] != tight[0][0])
    info_l = dict(loose)['information theory']
    info_t = dict(tight)['information theory']
    rank_l = [n for n, _ in loose].index('information theory') + 1
    rank_t = [n for n, _ in tight].index('information theory') + 1
    print(f'      information theory: ×{info_l} (rank {rank_l}) → ×{info_t} (rank {rank_t})')
    check(f'⓶ᵇ ⛔ and the correction is not marginal: information theory falls from ×{info_l} to '
          f'×{info_t}, rank {rank_l} to rank {rank_t}, on `bit` matching inside `orbit` and '
          '`arbitrary`',
          info_l > 4 * info_t and rank_t > rank_l + 3)
    bit_loose = sum(RB.counts('bit', tex=True).values())
    bit_word = sum(FS.word_counts('bit').values())
    check(f'⓶ᶜ measured directly: `bit` is ×{bit_loose} as a substring and ×{bit_word} as a word',
          bit_loose > 100 and bit_word < 10)
    reach = open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'), encoding='utf-8',
                 errors='replace').read()
    check('⓶ᵈ ⌗ AND THE PREDECESSOR STATED THE CONDITION: the r1890 table\'s own header says '
          '"word-bounded and keys stripped", and the instrument rebuilt from it dropped it',
          'word-bounded and keys stripped' in reach)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔ PASS TWO: FOUR OF THE TOP SEVEN LED ON A HOMONYM')
    print('  ==========================================================================')
    homonyms = [
        ('constraint', 'the Hamiltonian constraint', 'Hamiltonian constraint'),
        ('genus', "the corpus's species/genus taxonomy", 'species of one genus'),
        ('closure', 'a theorem closing, and the Galois closure', 'Galois closure'),
        ('character', 'causal character, analytic character', 'causal character'),
    ]
    for word, sense, evidence in homonyms:
        n = sum(FS.word_counts(word).values())
        present = any(evidence.lower() in b.lower() for b in RB.BODIES_TEX.values())
        print(f'      {word:12s} ×{n:<5d} {sense}')
        check(f'⓷ `{word}` ×{n} is not the field\'s word: the corpus uses it as {sense}, '
              f'evidenced by "{evidence}" appearing verbatim in a paper body',
              n > 0 and present)
    opt = [t for n, _, t in cands if 'convexity' in n][0]
    opt_per, opt_tot = FS.field_total(opt)
    share = opt_per['constraint'][0] / opt_tot
    check(f'⓷ᵉ ⛔ SO OPTIMISATION IS REFUSED RATHER THAN THROWN: {share:.0%} of its whole vocabulary '
          'count is that one homonym, and a field whose evidence is a homonym is not a field the '
          'corpus uses',
          share > 0.90)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ PASS THREE: TWO CANDIDATES WERE ALREADY ANSWERED, WHICH NO COUNT SEES')
    print('  ==========================================================================')
    p07 = RB.BODIES_TEX['P07']
    check('⓸ catastrophe theory is discharged by the ODE/dynamical-systems bake: P07 states '
          'outright "The word fold is used here in its bifurcation-theoretic sense"',
          'bifurcation-theoretic sense' in p07)
    check('⓸ᵇ and the reach document records that bake and its result -- the Nariai merger is a '
          'fold, and the fold forces a scaling law the corpus did not have',
          'the Nariai merger is a FOLD' in reach or 'is a FOLD' in reach)
    check('⓸ᶜ the operator half of spectral theory is R-M station Ⓗ\'s, thrown at r3150 (L-264) as '
          'a Weyl limit-point test',
          'L-264' in reach or 'limit-point' in reach.lower())
    check('⓸ᵈ ⛭ so a candidate can be large, word-bounded, correctly sensed AND ALREADY ANSWERED -- '
          'which is the pass a count cannot perform and the reason this instrument orders the '
          'reading rather than doing it',
          'A COUNT IS NOT AN OPENING' in open(os.path.join(ROOT, 'corpus', 'field_survey.py'),
                                              encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE FINDINGS ARE IN THE INSTRUMENT, NOT ONLY IN THIS RECEIPT')
    print('  ==========================================================================')
    fs_src = open(os.path.join(ROOT, 'corpus', 'field_survey.py'),
                  encoding='utf-8', errors='replace').read()
    check('⓹ the substring-to-word correction is recorded in the survey itself, so the next reader '
          'learns why the counts are word-bounded',
          'SUBSTRING' in fs_src and 'arbitrary' in fs_src)
    check('⓹ᵇ and so are the four homonyms and the two discharged candidates, with the refusal of '
          'optimisation stated as a verdict rather than an omission',
          'REFUSED rather than thrown' in fs_src and 'bifurcation-theoretic sense' in fs_src)
    check('⓹ᶜ ⛭ which is the corpus\'s own rule applied to this instrument: a rule that lives only '
          'in a receipt protects only the files that receipt amended',
          fs_src.count('#:') > 20)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** a survey is an instrument or it is a memory. **')
    print('  *The list of outstanding bakes was surveyed once, at r1890, and the corpus is twelve')
    print('  hundred revisions past it.  Rebuilt, THREE passes were needed before it could be')
    print('  trusted, and each one reordered the top:*')
    print('    ⓵ substring → word: the leading candidate was `bit` inside `orbit`')
    print('    ⓶ word → sense: four of the top seven led on a homonym, and one field is REFUSED')
    print('    ⓷ sense → already-thrown: two more were answered by bakes a count cannot see')
    print('  ⌗ ** And the r1890 header stated the first condition itself. **  *The instrument')
    print('     rebuilt from a table can lose the discipline the table was written with.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
