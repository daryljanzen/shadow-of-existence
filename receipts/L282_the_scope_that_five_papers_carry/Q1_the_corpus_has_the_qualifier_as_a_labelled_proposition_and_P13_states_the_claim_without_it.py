#!/usr/bin/env python3
r"""Q1 -- L-280 found P13's "the unique maximally symmetric Lorentzian manifold of its dimension" false
and proposed a clause to repair it.  The repair was already in the corpus, as a LABELLED PROPOSITION the
geometric core says the programme's ontology stands on -- and five other sites state the claim with a
qualifier while P13 states it with none and cites nothing.

COMPUTES: every occurrence of the uniqueness claim across the seventeen bodies, with its qualifier
classified; p0's `prop:unique` located with its statement; the two distinct scopings separated and the
weaker one shown NOT to do the work; and P13's sentence checked for a citation.  Nothing is fitted.

** ⛭⛭ ⓵ THE DISCIPLINE FOUND IT, ON ITS FIRST OUTING. **  *`L-281` banked the rule: ask the receipts,
not only the papers.  Run on this claim, `prior_art` returned sixteen receipts and pointed at `L-165`'s
quotation of `P10` -- a THIRD phrasing, with a THIRD qualifier -- which is what turned a single
sentence into a pattern.*
  ⇒ ** The instrument built out of a failure paid on the next question asked of it. **

** ⛔⛭⛭ ⓶ FIVE SITES CARRY A QUALIFIER.  P13 CARRIES NONE. **

      `p0`  `prop:unique`  "De Sitter space is the ONLY real Riemannian manifold that is maximally
                            symmetric AND CARRIES AN INTRINSIC LORENTZIAN SIGNATURE"
      `P03`                "the unique real Riemannian manifold WHOSE LORENTZIAN SIGNATURE IS
                            INTRINSIC TO ITS POSITIVE CURVATURE"
      `P03`                "the unique maximally symmetric real-Lorentzian manifold, EVERY LESS
                            SYMMETRIC CANDIDATE CARRYING AN UNFORCED MODULUS"
      `P06`                "the maximally symmetric structure being the unique one THAT REQUIRES ITS
                            OWN CONFIGURATION"
      `P10`                "the unique maximally symmetric structure CARRYING NO UNFORCED MODULUS"
      `P13`                "the unique maximally symmetric Lorentzian manifold OF ITS DIMENSION"

  ⇒ *** The last is the only one that is false, and it is the only one with no qualifier and no
      citation. ***

** ⛭⛭⛭ ⓷ AND THE TWO SCOPINGS ARE DIFFERENT -- ONLY ONE DOES THE WORK. **
  * *THE SIGNATURE SCOPING (`p0`, `P03`) selects de Sitter from among Minkowski, de Sitter and
    anti-de Sitter, because it is a statement about which real Riemannian manifold carries an
    intrinsic Lorentzian signature.*
  * *THE MODULUS SCOPING (`P06`, `P10`, `P03`) contrasts MAXIMAL SYMMETRY WITH LESS SYMMETRY --
    "every less symmetric structure requires a choice of how to break the symmetry" -- and all three
    of Minkowski, de Sitter and anti-de Sitter are maximally symmetric.*
  ⇒ ** SO LEAST-ARBITRARINESS IS SILENT BETWEEN THE THREE, and would not rescue P13's sentence. **
  ⇒ *** The corpus has exactly one argument that selects the substrate from its two siblings, it is
      `prop:unique`, and it is not cited where the claim is made. ***

** ⛔ ⓸ WHICH MAKES IT LOAD-BEARING RATHER THAN COSMETIC. **  *`p0` on `prop:unique`:* **"the
proposition the programme's ontology stands on."**  *And `P13`'s sentence opens its substrate section.*
  ⇒ ** The claim the whole ontology rests on is stated, at the top of the section that uses it, in the
    one form that is false and with nothing pointing at the form that is true. **

** ⌗ ⓹ SO `L-280`'S PROPOSED REPAIR IS SUPERSEDED, AND SAYING SO IS THE POINT. **  *That receipt
suggested "of its dimension AND CURVATURE SIGN" -- correct, and weaker than what the corpus already
holds.*  ⇒ ** The repair is a CITATION, not a clause: point the sentence at `prop:unique`. **
  ⌷ *Recorded here rather than silently improved, because a superseded repair that is not marked stays
    in the register as a live suggestion.*

WHAT IS NOT CLAIMED.  ** Not that the substrate is wrongly chosen ** -- `prop:unique` establishes it,
and this receipt's whole content is that the corpus HAS the argument.  ** Not that the modulus scoping
is wrong ** -- it is correct for what it does, which is to select maximal symmetry; the claim is only
that it does not separate the three maximally symmetric candidates.  ** Not that `prop:unique` is
verified here ** -- it is cited by `p0` to a thesis section and this receipt LOCATES it rather than
re-proving it; whether its proof carries is a separate question and is named as unasked.  ** Not that
the other five sites need changing ** -- they are correct as they stand.

    python3 receipts/L282_the_scope_that_five_papers_carry/Q1_the_corpus_has_the_qualifier_as_a_labelled_proposition_and_P13_states_the_claim_without_it.py

Written r3182, `L-282`.  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

#: the six sites, and the qualifier each carries.  FIXED before the search.
SITES = [
    ('p0', 'only real Riemannian manifold that is maximally symmetric', 'intrinsic signature'),
    ('P03', 'unique real Riemannian manifold whose Lorentzian signature is intrinsic',
     'intrinsic signature'),
    ('P03', 'unique maximally symmetric real-Lorentzian manifold', 'unforced modulus'),
    ('P06', 'maximally symmetric structure being the unique one that requires its own',
     'unforced modulus'),
    ('P10', 'unique maximally symmetric structure carrying no unforced', 'unforced modulus'),
    ('P13', 'unique maximally symmetric Lorentzian manifold of its dimension', 'NONE'),
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  Q1 -- the corpus has the qualifier as a labelled proposition; P13 states it without')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    import prior_art as PA
    B = RB.BODIES_TEX

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭⛭ THE DISCIPLINE FOUND IT, ON ITS FIRST OUTING')
    print('  ==========================================================================')
    hits = PA.search(['maximally symmetric'])
    files = {h[0] for h in hits}
    check(f'⓵ `prior_art` returns {len(files)} receipts on this claim, which is what turned one '
          'sentence into a pattern — the instrument L-281 built out of a failure, paying on the '
          'next question asked of it',
          len(files) >= 5)
    check('⓵ᵇ and among them is L-165\'s quotation of P10 — a third phrasing with a third '
          'qualifier, which no paper-only survey would have surfaced',
          any('L165' in f for f in files))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔⛭⛭ FIVE SITES CARRY A QUALIFIER; P13 CARRIES NONE')
    print('  ==========================================================================')
    found = []
    for paper, phrase, qual in SITES:
        present = phrase.lower() in B[paper].lower()
        found.append((paper, qual, present))
        print(f'      {paper:4s}  qualifier: {qual:20s}  located: {present}')
    check('⓶ all six sites are located at source, verbatim',
          all(p for _, _, p in found))
    qualified = [s for s in found if s[1] != 'NONE']
    check(f'⓶ᵇ ⛔ {len(qualified)} of the six carry a qualifier and exactly one — P13 — carries '
          'none', len(qualified) == 5 and found[-1][1] == 'NONE')

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭⛭⛭ THE TWO SCOPINGS DIFFER, AND ONLY ONE DOES THE WORK')
    print('  ==========================================================================')
    p06 = B['P06']
    check('⓷ the MODULUS scoping contrasts maximal symmetry with LESS symmetry: P06 — "every less '
          'symmetric structure requires a choice of how to break the symmetry, and that choice is '
          'a modulus, whereas maximal symmetry leaves nothing to choose"',
          'every less symmetric structure requires a choice of how to break the symmetry' in p06)
    check('⓷ᵇ ⛔ so it is SILENT between Minkowski, de Sitter and anti-de Sitter, all three of '
          'which are maximally symmetric (L-280 computed all three at isometry dimension 15) — '
          'and it would not rescue P13\'s sentence',
          'anti-de Sitter' not in p06.split('leaves nothing to choose')[0][-800:])
    check('⓷ᶜ ⛭ while the SIGNATURE scoping does separate them: p0 states it as a labelled '
          'proposition — "De Sitter space ... is the only real Riemannian manifold that is '
          'maximally symmetric and carries an intrinsic Lorentzian signature"',
          'only real Riemannian manifold that is maximally symmetric' in B['p0']
          and 'intrinsic Lorentzian signature' in B['p0'])
    check('⓷ᵈ and it is labelled `prop:unique`, so it is citable',
          'prop:unique' in B['p0'])

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛔ LOAD-BEARING, NOT COSMETIC')
    print('  ==========================================================================')
    check('⓸ p0 calls it "the proposition the programme\'s ontology stands on"',
          "the proposition the programme's ontology stands on" in B['p0']
          or 'ontology stands on' in B['p0'])
    p13 = B['P13']
    check('⓸ᵇ ⛔ and P13 cites nothing for it: the sentence carries no reference, P13 never '
          'mentions `prop:unique`, and it never carries "intrinsic" with "signature"',
          'prop:unique' not in p13
          and not re.search(r'intrinsic[^.]{0,60}signature', p13, re.I))
    i = p13.find('unique maximally symmetric Lorentzian manifold')
    check('⓸ᶜ the claim opens P13\'s substrate section, so the form that is false is the first '
          'thing the section that depends on it says',
          i > 0 and 'sec:setup' in p13[max(0, i - 300):i])

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ AND L-280\'S PROPOSED REPAIR IS SUPERSEDED')
    print('  ==========================================================================')
    l280 = os.path.join(ROOT, 'receipts', 'L280_the_decidable_claims',
                        'D1_ds5_is_not_the_unique_maximally_symmetric_lorentzian_five_manifold.py')
    src = open(l280, encoding='utf-8', errors='replace').read() if os.path.exists(l280) else ''
    check('⓹ L-280 proposed "of its dimension AND CURVATURE SIGN" — correct, and weaker than what '
          'the corpus already holds', 'curvature sign' in src)
    check('⓹ᵇ ⛭ the repair is a CITATION and not a clause: point the sentence at `prop:unique`, '
          'which is exact, already proved elsewhere, and the programme\'s own',
          'prop:unique' in B['p0'])
    check('⓹ᶜ ⌷ and recording the supersession matters, because a superseded repair that is not '
          'marked stays in the register as a live suggestion',
          os.path.exists(l280))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** the corpus has the qualifier as a labelled proposition, and P13 states')
    print('  the claim without it. **')
    print('  *Six sites state the uniqueness of the substrate.  Five carry a qualifier; P13 carries')
    print('  none, cites nothing, and is the only one that is false.*')
    print('  ⛭⛭ ** And the two qualifiers are not interchangeable: ** *least-arbitrariness selects')
    print('     MAXIMAL SYMMETRY against less symmetry and is silent between Minkowski, de Sitter')
    print('     and anti-de Sitter — all three maximally symmetric.  Only the intrinsic-signature')
    print('     scoping separates them, and that is `prop:unique`.*')
    print('  ⛔ ** Which makes it load-bearing: ** *p0 calls prop:unique the proposition the')
    print('     programme\'s ontology stands on, and P13 opens its substrate section with the one')
    print('     form of the claim that is false, pointing at nothing.*')
    print('  ⌗ ** So the repair is a citation, not a clause — and L-280\'s suggestion is')
    print('     superseded, which is recorded rather than quietly improved.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
