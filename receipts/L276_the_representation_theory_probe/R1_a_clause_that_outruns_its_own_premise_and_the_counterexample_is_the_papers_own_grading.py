#!/usr/bin/env python3
r"""R1 -- the representation-theory PROBE (not a bake: the field is partly discharged, Ⓕ having been
struck as already held in P13).  P14 closes an argument with "no character count on a finite group can
produce three."  In context that is right.  Read unqualified it is false, and the counterexample is
P14's own triality grading, three paragraphs away.

COMPUTES: the fibre count of every one-dimensional character of Z_2, Z_3, Z_4 and Z_6 by enumeration;
that the premise the sentence sets up (a character into {+-1}) does bound the blocks at two; that
dropping the premise admits three; and that the corpus's own triality class is exactly such a
character.  Also re-verifies the su(3) real-form obstruction the same paper states.  Nothing is fitted.

** ⌗ ⓵ WHY A PROBE AND NOT A BAKE. **  *`L-272`'s re-survey put representation theory fourth of four
and marked it "partly discharged, wants a targeted probe": station Ⓕ -- the two real forms of
$SO(6,\mathbb{C})$ -- was STRUCK at r3148 as already held in `P13`, and `P13`/`P14` do their own
representation theory throughout.*  ⇒ ** So the field is thrown at one sentence, not at the corpus. **

** ⛭ ⓶ AND THE SENTENCE IS RIGHT WHERE IT STANDS. **  `P14`, closing the two-bits argument:

      *"A grading by a one-dimensional character is a function to $\{\pm1\}$ and its blocks are its
       fibres, so it has at most two, and no character count on a finite group can produce three."*

  *The premise is stated: a function to $\{\pm1\}$.  Given it, "at most two" is exact, and the
  conclusion the paragraph needs -- that the two bits reproduce the lepton content's names and not its
  gauging -- follows.*  ⇒ ** Nothing in the argument is wrong. **

** ⛔ ⓷ BUT THE FINAL CLAUSE DROPS THE PREMISE, AND THE COUNTEREXAMPLE IS IN THE SAME PAPER. **
*A one-dimensional character of a finite group is a homomorphism to $\mathbb{C}^\times$; its image is a
finite cyclic group $\mu_n$ and its fibres number exactly $n$.  Enumerated below: $Z_3$'s non-trivial
characters have **three** fibres, and $Z_6$'s have $1, 6, 3, 2, 3, 6$.*
  ⇒ ** So a character count on a finite group produces three whenever the character is valued in
    $\mu_3$ -- and $Z_6 \subset D_6 = \mathrm{Aut}(A_2)$ is the corpus's own skeleton group. **
  ⇒ *** AND `P14` USES SUCH A GRADING AS ITS OWN CENTRAL ONE: "the triality class is what separates
      the two, a coloured constituent carrying a non-zero class and a lepton the zero one."  Triality
      is the centre $Z_3$ of $SU(3)$, and it takes three values. ***

** ⌗ ⓸ SO WHAT IS OWED IS FOUR WORDS, NOT AN ARGUMENT. **  *The clause needs its premise carried --
"no count by a $\{\pm1\}$-valued character can produce three" -- and then it is exact and the paragraph
is unchanged.*
  ⇒ ** This is the corpus's own registered class: a gloss that outruns the computation beneath it. **
    *`OWED` 621 recorded the same shape at receipt grain -- a summary sentence drifting from the table
    two lines above it, carrying a receipt's authority.  Here it is at paper grain, and the drift is
    from a premise stated in the same sentence.*

WHAT IS NOT CLAIMED.  ** Not that the argument fails ** -- the paragraph's conclusion is correct and
this receipt verifies its premise-bounded form.  ** Not that anything downstream is affected ** -- the
$2+1+1$ decomposition, the refusal to derive $SU(2)_L$, and the orbit reading are untouched.
** Not that triality is being confused with the lepton grading in the paper ** -- it is not; the point
is only that the paper contains a three-valued character grading and the unqualified clause denies such
a thing exists.  ** Not that the field bit anywhere else ** -- it did not, and the probe's scope was
one sentence by design.  ** And the su(3) obstruction is re-verified and STANDS: ** *a real rank-three
bundle's metric holonomy sits in $SO(3)$, of dimension three, and $\mathfrak{su}(3)$ has dimension
eight -- no room, exactly as `P14` and `P07` say.*

    python3 receipts/L276_the_representation_theory_probe/R1_a_clause_that_outruns_its_own_premise_and_the_counterexample_is_the_papers_own_grading.py

Written r3170, `L-276`.  Stated for reversal.
"""
import os
import sys
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def fibres(n, k):
    """the number of fibres of chi_k : Z_n -> C*, chi_k(j) = omega_n^{kj}"""
    return len({(k * j) % n for j in range(n)})



def _flat_at(rev):
    """`matter_sector_paper.tex` at a revision, flattened the way `p14` is."""
    import re as _re
    import subprocess as _sp
    return _re.sub(r'\s+', ' ', _sp.run(
        ['git', 'show', f'{rev}:corpus/matter_sector_paper.tex'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)


def main():
    print()
    print('  R1 -- a clause that outruns its own premise, and the counterexample is in the paper')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    p14 = RB.BODIES_TEX['P14']

    print('  ' + '=' * 74)
    print('  PART 1 -- ⌗ WHY A PROBE: THE FIELD IS PARTLY DISCHARGED ALREADY')
    print('  ==========================================================================')
    reach = open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'),
                 encoding='utf-8', errors='replace').read()
    check('⓵ station Ⓕ — the two real forms of SO(6,C), the reach list\'s representation-theory '
          'entry — was STRUCK r3148 as already held in P13',
          'STRUCK r3148' in reach and 'real forms' in reach)
    check('⓵ᵇ and the re-survey marked the field "partly discharged" and wanting a targeted probe '
          'rather than a full bake — so the field is thrown at one sentence by design',
          'partly discharged' in reach and 'probe' in reach.lower())

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛭ THE SENTENCE, AND IT IS RIGHT WHERE IT STANDS')
    print('  ==========================================================================')
    check('⓶ P14 sets its premise explicitly: "A grading by a one-dimensional character is a '
          'function to $\\{\\pm1\\}$"',
          'is a function to' in p14 and 'pm1' in p14.replace('\\', ''))
    check('⓶ᵇ and given that premise the bound is exact: a character into {±1} has at most two '
          'fibres', max(fibres(2, k) for k in range(2)) == 2)
    check('⓶ᶜ so the paragraph\'s own conclusion stands — the two bits reproduce the lepton '
          'content\'s names and not its gauging, and P14 says so',
          'names and not its gauging' in p14)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔ THE FINAL CLAUSE DROPS THE PREMISE')
    print('  ==========================================================================')
    # ** ⛭⛭⛭ RE-PINNED r3978, AND THE DEFECT THIS FILE FOUND HAS BEEN REPAIRED IN THE PAPER. **
    # ** P14 read "no character count on a finite group can produce three" -- unqualified, and false
    # ** as stated, since a $\mathbb{Z}_3$ character has three fibres.  *** r3315 ("the two landings
    # ** 54 routed: P14's dropped premise") carried the premise back into the clause. ***
    # **   ⇒ ** So the defective wording is pinned WHERE IT STOOD and the repair asserted here. **
    _p14_then = _flat_at('2ed352c1~1')
    check('⓷ the clause as written was unqualified at 2ed352c1~1: "no character count on a finite '
          'group can produce three" -- false as stated, which is this file\'s finding',
          'no character count on a finite group can produce three' in _p14_then)
    print('      G      k   fibres of χ_k')
    for n in (2, 3, 4, 6):
        for k in range(n):
            print(f'      Z_{n}    {k}   {fibres(n, k)}')
    check('⓷ᵇ ⛔ but a one-dimensional character\'s fibres number |image|, so Z_3\'s non-trivial '
          'characters have exactly THREE',
          fibres(3, 1) == 3 and fibres(3, 2) == 3)
    check('⓷ᶜ and this is not an exotic group: Z_6 ⊂ D_6 = Aut(A_2) is the corpus\'s own skeleton '
          f'group, and its characters have {sorted({fibres(6, k) for k in range(6)})} fibres — '
          'three among them',
          3 in {fibres(6, k) for k in range(6)})

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛔⛭ AND THE COUNTEREXAMPLE IS THE PAPER\'S OWN CENTRAL GRADING')
    print('  ==========================================================================')
    check('⓸ P14 grades by triality: "the triality class is what separates the two, a coloured '
          'constituent carrying a non-zero class and a lepton the zero one"',
          'triality class is what separates the two' in p14)
    check('⓸ᵇ ⛭ and triality is the centre Z_3 of SU(3) — a one-dimensional character taking '
          'THREE values, which is exactly what the unqualified clause denies exists',
          fibres(3, 1) == 3 and 'triality' in p14.lower())
    check('⓸ᶜ so the clause and its counterexample are in the same paper, and the counterexample '
          'is not incidental — it is the grading the quark/lepton distinction rests on',
          'a coloured constituent carrying a non-zero class' in p14)

    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ WHAT IS OWED IS FOUR WORDS, AND THE CLASS IS REGISTERED')
    print('  ==========================================================================')
    owed = open(os.path.join(ROOT, 'OWED.md'), encoding='utf-8', errors='replace').read()
    # ** the repair is ASSERTED as a predicate: the qualified form is true and the text lacks it **
    qualified_true = max(fibres(2, k) for k in range(2)) == 2
    unqualified_false = any(fibres(n, k) == 3 for n in (3, 6) for k in range(n))
    text_lacks_qualifier = ('no character count on a finite group can produce three' in p14
                            and 'valued character' not in p14)
    # ** ⛭⛭ AND THE PAPER'S REPAIR SAYS MORE THAN THE ONE THIS FILE PROPOSED. **  It suggested "no
    # ** count by a {±1}-valued character can produce three".  P14 now reads *"A grading by a
    # ** one-dimensional character is a function to $\{\pm1\}$ and its blocks are its fibres, so it
    # ** has at most two, and no \emph{two-valued} character count can produce three"*, and then
    # ** names the premise outright: *"The restriction is the premise and not a general fact: a
    # ** $\mathbb{Z}_3$ character takes three values, and this paper uses one---the centre"*.
    # **   ⇒ ** The arithmetic this file computed is unchanged and still asserted; what moved is that
    # **     the paper now carries the qualifier AND says why it is a premise. **  *A receipt that
    # **     proposes a repair and pins the unrepaired text fails when the repair lands -- and the
    # **     landing is what it was for.*
    check('⓹ the repair carried the premise into the clause: the qualified form is TRUE (a two-'
          'valued character has at most two fibres) and the unqualified form is FALSE (a '
          '$\\mathbb{Z}_3$ character has three), and P14 now carries the QUALIFIED one -- "no '
          '\\emph{two-valued} character count can produce three"',
          qualified_true and unqualified_false
          # ⌗ `p14` is the DE-MACROED view (`BODIES_TEX`), where `\emph{}` is stripped -- so the
          #   pin is the de-macroed form.  *Pinning the raw `\emph{two-valued}` here would match
          #   nowhere and read as the repair not having landed.*
          and 'no two-valued character count can produce three' in p14
          and 'no character count on a finite group can produce three' not in p14)
    check('⓹ᵃ ⛭ and it names the restriction as a premise rather than leaving it implicit: "The '
          'restriction is the premise and not a general fact: a $\\mathbb{Z}_3$ character takes '
          'three values, and this paper uses one---the centre"',
          'The restriction is the premise and not a general fact' in p14
          and '$Z_3$ character takes three values' in p14)
    check('⓹ᵇ ⛭ and the class is the corpus\'s own: OWED 621 recorded a gloss drifting from the '
          'computation beneath it — "a receipt\'s prose is not its result" — at receipt grain; '
          'this is the same shape at PAPER grain',
          "a receipt's prose is not its result" in owed or 'prose is not its result' in owed)

    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- ⌗ AND THE OTHER BIG REPRESENTATION-THEORY CLAIM IS RE-VERIFIED AND STANDS')
    print('  ==========================================================================')
    dim_so3, dim_su3 = 3, 8
    print(f'      a real rank-3 bundle with metric connection: Hol ⊆ SO(3), dim so(3) = {dim_so3}')
    print(f'      su(3) has dim = {dim_su3}')
    check('⓺ the su(3) real-form obstruction P14 and P07 state is exact: a real bundle\'s '
          'complexification carries a parallel conjugation, its holonomy commutes with that '
          f'conjugation and lands in the real form so(3) of dimension {dim_so3}, with no room for '
          f'{dim_su3}', dim_su3 > dim_so3)
    check('⓺ᵇ and the paper states it in those words: "a real bundle\'s complexification carries a '
          'parallel conjugation, so its holonomy commutes with that conjugation and lands in the '
          'real form"',
          'parallel conjugation' in p14 and 'lands in the real form' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** one clause outruns its own premise, and the counterexample is the')
    print('  paper\'s own grading. **')
    print('  ⛭ *The sentence sets its premise — a character into {±1} — and given it, "at most')
    print('     two" is exact and the paragraph\'s conclusion stands.*')
    print('  ⛔ ** The final clause drops the premise. **  *A one-dimensional character\'s fibres')
    print('     number |image|, so a μ_3-valued character has three — and Z_6 ⊂ D_6 = Aut(A_2) is')
    print('     the corpus\'s own skeleton group.*')
    print('  ⛔⛭ ** And P14 grades by triality three paragraphs later ** *— the centre Z_3 of')
    print('     SU(3), three values — which is exactly what the unqualified clause denies.*')
    print('  ⌗ ** What is owed is four words, not an argument **, *and the class is registered:')
    print('     OWED 621\'s "a receipt\'s prose is not its result", one grain up.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
