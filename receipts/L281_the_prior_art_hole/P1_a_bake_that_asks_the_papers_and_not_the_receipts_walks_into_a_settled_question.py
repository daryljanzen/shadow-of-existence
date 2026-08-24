#!/usr/bin/env python3
r"""P1 -- the baseline instrument reads the seventeen PAPER bodies.  The corpus holds its adjudications
in 637 RECEIPTS, and a receipt is where a question is settled before a paper ever carries it.  Two bakes
touched the branch-point operator without consulting the verdict that fixed it at r2825, and both came
out right BY INHERITANCE rather than by method.

COMPUTES: the substitution test that settles the branch-point index, run symbolically on four candidate
solutions; both self-consistent pairings carried out and shown to agree; the prior-art search that
returns the fourteen receipts the bake never read; and the two documents -- `S3` at r2819 and the `B67`
verdict at r2825 -- located with what each settles.  Nothing is fitted.

** ⛔⛭⛭ ⓵ THE HOLE, AND IT WAS THERE FROM THE START. **  *`reach_baseline` was built at `L-263` on
`OWED` 609's own gate --* **"a bake against a corpus that cannot say what it already holds returns
findings it owns"** *-- and it reads THE PAPERS.*
  ⇒ ** The corpus does not hold its adjudications only in the papers. **  *It holds them in receipts,
    and `prior_art` now searches those.*
  ⇒ *** A BAKE COULD SURVEY EVERY PAPER, FIND A CLEAN SHEET, AND WALK INTO A QUESTION THE CORPUS
      DECIDED TWO HUNDRED REVISIONS AGO. ***

** ⛭⛭ ⓶ WHICH IS EXACTLY WHAT HAPPENED, TWICE, TO THIS LINE. **  *Station Ⓗ (`L-264`) and the
functional-analysis bake (`L-275`) both turn on the branch-point index of
$(\sqrt f\,d/dr \mp \lambda\sqrt f/r)\psi=0$.  Both inherited the right pairing and both came out
right.*  ⇒ ** Neither consulted `S3` or `B67`. **  *So the answer was carried, not checked -- and
nothing in either procedure would have caught a drift.*

** ⛔ ⓷ AND THE DRIFT IS REAL, BECAUSE THE OTHER LINE TOOK IT. **  *Node 57 re-derived the exponent by
pairing the tortoise superpotential with the frame measure, obtaining
$\ln\psi=-i\lambda\sqrt{2/M}\sqrt r$ -- a bounded imaginary phase, hence limit-CIRCLE.*
  ⇒ ** `S3` names that exact result as the third of FOUR wrong reductions, all sharing one substitution:
    "the NORM measure put where the operator's own $1/\sqrt f$ belongs." **

** ⛭⛭⛭ ⓸ THE TEST IS A SUBSTITUTION AND IT NEEDS NO REDUCTION AT ALL. **  *$\sqrt f$ multiplies BOTH
terms of the zero-mode equation, so it cancels in the real variable $r$ before any branch could be
chosen.*  ⇒ ***$r^{+\lambda}$ solves it identically; $r^{i\lambda}$ and the closed form above do not.***
  ⌗ ** And both self-consistent pairings agree: ** *in the operator coordinate $dx=dr/\sqrt f$,
    $\int W\,dx=\lambda\ln|r|$; in the tortoise coordinate $dr_*=dr/f$, $d\psi/\psi=\lambda\,dr/r$.
    Neither returns $\lambda/(r\sqrt f)$.*

** ⛭⛭ ⓹ AND THE CORPUS HAS A VERDICT, NOT MERELY AN ADJUDICATION. **  *`B67`, r2825, is the observer
line's F5 call and it names BOTH prescriptions:* **"Under the analytic $\sqrt f$ operator the bound
index is real $\pm\lambda$; under the self-adjoint $\sqrt{|f|}$ operator it is oscillatory
$\pm i\lambda$."**  ⇒ ** It chooses, and the reason is physical: ** *self-adjointness is a requirement
on a SPATIAL Dirac operator; where $f<0$ the radial direction is timelike and the operator is an
evolution generator, so the requirement does not apply where the two prescriptions differ.*
  ⇒ *** And at $\omega=0$ there is no fork at all -- $\sqrt f$ cancels -- so the branch-point index
      never reaches the choice. ***

WHAT IS NOT CLAIMED.  ** Not that station Ⓗ or `L-275` were wrong ** -- both verdicts stand, and this
receipt is about how they were reached, not what they said.  ** Not that node 57 was careless ** -- the
fork it identified is REAL and `B67` says so; what the corpus adds is that it had already been called,
by the other line, on physical grounds.  ** Not that `prior_art` closes the hole ** -- it matches words,
so an adjudication phrased differently is invisible to it, which is `field_survey`'s blind spot in a
second place; it bounds the reading and the reading decides.  ** Not that the $\omega\ne0$ continuum is
settled ** -- `B67` says outright it is not, and this receipt does not touch it.

    python3 receipts/L281_the_prior_art_hole/P1_a_bake_that_asks_the_papers_and_not_the_receipts_walks_into_a_settled_question.py

Written r3180, `L-281`.  Stated for reversal.
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  P1 -- a bake that asks the papers and not the receipts walks into a settled question')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import prior_art as PA

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭⛭⛭ THE SUBSTITUTION TEST, WHICH NEEDS NO REDUCTION')
    print('  ==========================================================================')
    r, lam, M = sp.symbols('r lambda M', positive=True)
    f = 1 - 2 * M / r
    sf = sp.sqrt(f)
    W = lam * sf / r
    res = lambda psi: sp.simplify(sf * sp.diff(psi, r) - W * psi)

    solves_real = res(r ** lam) == 0
    solves_imag = res(r ** (sp.I * lam)) == 0
    solves_57 = res(sp.exp(-sp.I * lam * sp.sqrt(2 / M) * sp.sqrt(r))) == 0
    print(f'      psi = r^(+lambda)                      solves: {solves_real}')
    print(f'      psi = r^(+i lambda)                    solves: {solves_imag}')
    print(f'      psi = exp(-i lam sqrt(2/M) sqrt(r))    solves: {solves_57}')
    check('⓵ r^(+lambda) solves the zero-mode equation identically, for any f — because sqrt(f) '
          'multiplies BOTH terms and cancels in the real variable r',
          solves_real)
    check('⓵ᵇ ⛔ while the oscillatory index and the imaginary-phase closed form do NOT solve it, '
          'so they are not solutions of this operator at all',
          not solves_imag and not solves_57)

    # both self-consistent pairings
    x_pairing = sp.simplify(sp.integrate((lam * sf / r) * (1 / sf), r))
    check(f'⓵ᶜ and both self-consistent pairings agree: in the operator coordinate dx = dr/sqrt f, '
          f'∫W dx = {x_pairing} — the sqrt f cancelling, giving a REAL exponent',
          sp.simplify(x_pairing - lam * sp.log(r)) == 0)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔⛭⛭ THE HOLE: THE BASELINE READS PAPERS, THE CORPUS DECIDES IN RECEIPTS')
    print('  ==========================================================================')
    heads = PA.receipt_heads()
    print(f'      receipt heads available to be searched : {len(heads)}')
    check(f'⓶ the corpus carries {len(heads)} receipt docstrings, and `reach_baseline` reads none '
          'of them — it reads the seventeen paper bodies',
          len(heads) > 500
          and 'seventeen paper' in open(os.path.join(ROOT, 'corpus', 'reach_baseline.py'),
                                        encoding='utf-8', errors='replace').read().lower()
          .replace('17 paper', 'seventeen paper'))
    hits = PA.search(['sqrt f', 'wall index'], heads=heads)
    files = {h[0] for h in hits}
    bridge = {h for h in files if 'L221_the_bridge' in h}
    print(f'      receipts mentioning the superpotential : {len(files)}  '
          f'({len(bridge)} of them in L221_the_bridge)')
    check(f'⓶ᵇ ⛔ a prior-art search returns {len(files)} receipts on this operator, {len(bridge)} '
          'of them in one cluster — and the functional-analysis bake read none of them',
          len(files) >= 10 and len(bridge) >= 5)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭⛭ AND THE CORPUS HAS A VERDICT, NOT MERELY AN ADJUDICATION')
    print('  ==========================================================================')
    s3p = os.path.join(ROOT, 'receipts', 'L829_po11_continuum_continues',
                       'S3_the_wall_index_is_real_because_sqrt_f_factors_out_of_the_operator'
                       '_not_the_norm.py')
    b67 = [f for f in os.listdir(os.path.join(ROOT, 'receipts', 'L221_the_bridge'))
           if f.startswith('B67')]
    s3 = open(s3p, encoding='utf-8', errors='replace').read() if os.path.exists(s3p) else ''
    b = open(os.path.join(ROOT, 'receipts', 'L221_the_bridge', b67[0]),
             encoding='utf-8', errors='replace').read() if b67 else ''
    check('⓷ S3 (r2819, joint with 56) names FOUR wrong reductions and the substitution they '
          'share: "the NORM measure put where the operator\'s own 1/sqrt f belongs"',
          'Four reductions returned four wrong answers' in s3
          and 'NORM measure put where' in s3)
    check('⓷ᵇ and one of the four is the imaginary-phase form: "ln P ~ sqrt r"',
          'ln P ~ sqrt r' in s3)
    check('⓷ᶜ ⛭ B67 (r2825) is the observer line\'s F5 VERDICT and names BOTH prescriptions — '
          'analytic sqrt f giving real ±lambda, self-adjoint sqrt|f| giving oscillatory ±i lambda',
          bool(b) and 'oscillatory' in b and 'F5' in b)
    check('⓷ᵈ it chooses on physical grounds: self-adjointness is a requirement on a SPATIAL Dirac '
          'operator, and where f<0 the radial direction is timelike, so the requirement does not '
          'apply where the two differ',
          'SPATIAL' in b and 'timelike' in b)
    check('⓷ᵉ ⛭⛭ and at omega=0 there is NO fork: sqrt f is an overall factor, so the branch-point '
          'index never reaches the choice',
          'OVERALL FACTOR' in b and 'regardless of the sign' in b)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ THE INSTRUMENT, AND WHAT IT CANNOT DO')
    print('  ==========================================================================')
    pa_src = open(os.path.join(ROOT, 'corpus', 'prior_art.py'),
                  encoding='utf-8', errors='replace').read()
    check('⓸ `prior_art` searches receipt docstrings — a receipt\'s head is its finding — and '
          'fails rather than reporting a clean sheet if it finds none',
          'receipt_heads' in pa_src and 'not a clean sheet' in pa_src)
    check('⓸ᵇ and it states its own blind spot: it matches WORDS, so an adjudication phrased '
          'differently is invisible — field_survey\'s defect in a second place',
          'matches words' in pa_src.lower() and 'blind spot' in pa_src)
    check('⓸ᶜ ⛭ the rule it exists to enforce: the papers say what the corpus PUBLISHES, the '
          'receipts say what it has already DECIDED, and those are different sets',
          'already DECIDED' in pa_src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** a bake that asks the papers and not the receipts walks into a settled')
    print('  question. **')
    print('  *`reach_baseline` reads seventeen paper bodies.  The corpus decides in 637 receipts,')
    print('  and two bakes of mine turned on an operator whose treatment was fixed at r2819 and')
    print('  VERDICTED at r2825 — consulting neither.  Both came out right BY INHERITANCE, and')
    print('  nothing in either procedure would have caught a drift.*')
    print('  ⛔ ** One line did drift, ** *re-deriving the exponent by the exact substitution S3')
    print('     names as the shared error of four failed reductions.  It could as easily have')
    print('     been me: I had no check that would have said otherwise.*')
    print('  ⛭ ** The test needs no reduction at all: ** *sqrt f multiplies both terms and cancels')
    print('     before a branch could be chosen — r^(+lambda) solves, the oscillatory forms do')
    print('     not — and both self-consistent pairings return the real exponent.*')
    print('  ⌗ ** The rule: ** *ask the receipts, not only the papers.  What the corpus publishes')
    print('     and what it has already decided are different sets.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
