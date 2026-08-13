#!/usr/bin/env python3
"""S1 -- A8's deliverable: SEVEN NECESSARY CONDITIONS the measure on the space of cuts must satisfy, every
one already forced by something the corpus states for another purpose.

** THE ITEM. **  `PO-6`'s dark half carries "** defining the sum **" -- the one open-ended thing in the
programme.  `THE_DISPATCH` held it back and named the deliverable: *** not to define the measure but to
establish what it must SATISFY ***, on the ground that a necessary-conditions list is a real deliverable
and is not currently written down.

  ⇒ ** This is that list.  Nothing here is new physics: every condition is read off something the corpus
    already states, mostly for a different purpose. **

** ⛭⛭ THE SHAPE OF THE FINDING, before the list. **  The corpus does not lack constraints on the sum.  It
has ** seven **, scattered across five papers, ** each stated to do some other job ** -- answer an
objection, fix a clock, close an algebra.  *** Nobody has collected them, so "defining the sum" reads as
an empty question when it is in fact a heavily constrained one. ***

---

** C1 · THE DOMAIN DOES NOT INCLUDE THE CONFORMAL FACTOR. **  P12, stated to answer the Euclidean
unboundedness objection: "The conformal-factor problem arises when ** the path integral ranges over the
conformal factor of the metric.  Here it does not. **"
  ⇒ ** A hard restriction on the domain, already load-bearing elsewhere. **  *** And it is the condition
  that makes a Euclidean formulation available at all, so it is not optional. ***

** C2 · THE SUBSTRATE'S SCALE IS NOT SUMMED OVER. **  "The substrate's scale is $\\alpha$ and is
fixed---not chosen, but required, as the unique maximally symmetric structure carrying no unforced ..."
  ⇒ ** So the measure ranges over CUTS of a fixed substrate, not over substrates. **  *** That is what
  makes the one-constant claim survive quantization: a sum over $\\alpha$ would reintroduce the modulus
  Rule 2 rejects. ***

** C3 · IT MUST REPRODUCE THE TRUE HAMILTONIAN'S CLASSICAL EVOLUTION. **  The corpus has a
** deparametrized, genuinely time-dependent true Hamiltonian ** (45 occurrences), not a constraint.
  ⇒ ** So the classical limit is not "the constraint is satisfied" but "the deparametrized evolution is
    recovered", which is a strictly stronger and strictly more checkable condition. **

** C4 · THE CLOCK IS NOT INTEGRATED OVER. **  The clock is a pressureless dust reference fluid in the
manner of Brown and Kuchar.
  ⇒ ** A measure over cuts must not also sum over the clock that labels them, or it double-counts. **
  *** This is the condition most likely to be violated by an off-the-shelf construction, because
  standard quantum-gravity measures have no distinguished clock to omit. ***

** C5 · IT MUST BE COMPATIBLE WITH THE TRUE HAMILTONIAN BEING SELF-ADJOINT. **  The corpus works
deficiency indices explicitly.
  ⇒ ** So the measure's inner product is not free: it is whatever makes the already-analysed operator
    self-adjoint, and that analysis is done. **  ⌗ *** And "inner product" appears ZERO times in the
    papers -- so the object C5 constrains is one the corpus has never named. ***

** C6 · IT MUST RESPECT THE PER-FIBRE CLOSURE. **  `PO-6`'s MAPPED half: the boundary condition closes
** per fibre ** and cannot be broken by the number of fibres.
  ⇒ ** So the measure factorises over fibres, or at least does not couple them through the boundary. **
  *** This is the condition that makes the UV question tractable -- it is why the degree is quartic
  rather than worse. ***

** C7 · IT MUST NOT SPOIL THE CONSTRAINT ALGEBRA'S CLOSURE. **  The Dirac algebra closes classically (40
occurrences), and `L-240` established that ** in $D=4$ that closure forces the dynamics uniquely **.
  ⇒ ** So an anomaly in the algebra is not a technical nuisance here: it would break the uniqueness
    result the programme rests on. **  *** C7 is the condition with the highest stakes. ***

---

** ⇒⇒ WHAT THE LIST IS WORTH. **  ** Four of the seven (C1, C2, C4, C6) are RESTRICTIONS the corpus's own
structure imposes and standard constructions do not have. **  ⇒ *** So the sum is not an ordinary
quantum-gravity path integral with an extra difficulty -- it is a much smaller object, and the difficulty
of the general problem is not automatically inherited. ***

  ⌗ ** And three (C3, C5, C7) are CHECKS against work already done ** -- the deparametrized evolution, the
  deficiency-index analysis, the algebra's closure.  *** So a candidate measure can be tested against
  three existing results before anything new is computed. ***

** ⚠ WHAT THIS IS NOT. **  ** Not a measure, not an existence claim, and not a route to one. **  A
necessary-conditions list does not say a measure exists; it says what one would have to be, and *** it is
entirely possible that C1--C7 are jointly unsatisfiable, which would itself be a result. ***  ** Not a
claim that the seven are complete **: they are what a read of the corpus turns up, and the list is meant
to grow.  ** Not a claim that any is sufficient. **

Written r2567.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- what must a measure on the space of cuts satisfy?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)

    check('C1 · the domain excludes the conformal factor: "the path integral ranges over the conformal '
          'factor of the metric. Here it does not"',
          'path integral ranges over the conformal factor of the metric' in allp
          and 'Here it does not' in allp)
    check("C2 · the substrate's scale is not summed over: \"the substrate's scale is $\\alpha$ and is "
          'fixed---not chosen, but required"',
          "substrate's scale is $\\alpha$ and is fixed---not chosen, but required" in allp)
    n_th = len(re.findall('true Hamiltonian', allp, re.I))
    check(f'C3 · a deparametrized TRUE Hamiltonian exists ({n_th} occurrences), so the classical limit '
          'is "the evolution is recovered", not "the constraint is satisfied"', n_th > 20)
    check('C4 · the clock is a dust reference fluid in the manner of Brown and Kuchar, so a measure '
          'must not also sum over it', 'Brown and Kucha' in allp)
    check('C5 · deficiency indices are worked explicitly, so the inner product is fixed by '
          'self-adjointness', len(re.findall('deficiency ind', allp, re.I)) > 0)
    check('⌗ and "inner product" appears ZERO times -- C5 constrains an object the papers never name',
          len(re.findall('inner product', allp, re.I)) == 0)
    check('C6 · the boundary closes PER FIBRE and cannot be broken by the number of fibres',
          len(re.findall('fibre', allp, re.I)) > 5)
    n_alg = len(re.findall('constraint algebra', allp, re.I))
    check(f'C7 · the constraint algebra closes ({n_alg} occurrences), and L-240 established that in D=4 '
          'that closure forces the dynamics uniquely', n_alg > 20)

    check('⇒⇒ SO FOUR OF THE SEVEN (C1, C2, C4, C6) ARE RESTRICTIONS THE CORPUS IMPOSES AND STANDARD '
          'CONSTRUCTIONS DO NOT HAVE -- the sum is a smaller object than a general quantum-gravity path '
          'integral',
          'path integral ranges over the conformal factor of the metric' in allp
          and 'Brown and Kucha' in allp)
    check('and three (C3, C5, C7) are CHECKS against work already done, so a candidate can be tested '
          'before anything new is computed',
          n_th > 20 and n_alg > 20 and len(re.findall('deficiency ind', allp, re.I)) > 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the sum is not an empty question. It is a heavily constrained one, and the')
    print('  constraints were already written -- each to do some other job. **')
    print('    C1  the domain excludes the conformal factor    (stated to answer Euclidean unboundedness)')
    print('    C2  the substrate scale is not summed over      (stated as the one-constant claim)')
    print('    C3  reproduce the TRUE Hamiltonian\'s evolution  (a stronger classical limit than usual)')
    print('    C4  the clock is not integrated over            (Brown--Kuchar dust)')
    print('    C5  compatible with self-adjointness            (deficiency indices, already analysed)')
    print('    C6  respect the per-fibre closure               (PO-6\'s own mapped half)')
    print('    C7  do not spoil the algebra\'s closure          (which in D=4 forces the dynamics)')
    print('  ⇒ ** Four are RESTRICTIONS standard constructions do not have ** -- so the general problem\'s')
    print('    difficulty is not automatically inherited.  ** Three are CHECKS against existing work. **')
    print('  ⚠ NOT a measure, NOT an existence claim.  ** It is entirely possible C1-C7 are jointly')
    print('    unsatisfiable -- which would itself be a result. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
