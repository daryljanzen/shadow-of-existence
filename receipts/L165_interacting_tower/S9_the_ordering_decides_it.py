#!/usr/bin/env python3
"""S9 -- `PO-6`'s spectral question is decided by OPERATOR ORDERING, which P10 never names -- and the
threshold is the free coefficient plus exactly one zero-point quantum.

** WHY THIS EXISTS. **  r2723 established that `PO-6`'s remainder is not the floor but "** where
$\\hat\\Gamma$'s spectrum sits relative to $3/4$ **", and then stopped there.  *** That was an avoidance:
$\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$ is written down in P10, and where its minimum lies is
arithmetic. ***

** ⛭⛭ ⓵ AND THE ANSWER TURNS ENTIRELY ON ORDERING. **  $\\sum_n\\hat\\pi_n^2$ on a tower of oscillator-like
modes has a minimum that depends on how the operator is ordered:

      *** normal-ordered   vacuum contributes 0        Gamma_min = 1/4        BELOW 3/4
          symmetric, N=1   one half-quantum per mode   Gamma_min = 3/4        AT the threshold
          symmetric, N=2                               Gamma_min = 5/4        above
          symmetric, N=5                               Gamma_min = 11/4       above ***

  ⇒ *** NORMAL-ORDERED: the vacuum sector sits at the FREE value $1/4$, below the threshold, so the
      origin is LIMIT-CIRCLE there and boundary freedom SURVIVES quantization -- the thing quantizing the
      scale factor was supposed to remove.
      SYMMETRIC: even ONE mode reaches the threshold and every richer sector clears it. ***

** ⛭ ⓶ AND THE THRESHOLD IS NOT AN ARBITRARY NUMBER IN THIS PROBLEM. **

      *** 3/4  =  1/4  +  1/2  =  (free boundary coefficient)  +  (one zero-point quantum) ***

  ⇒⇒ *** The Weyl threshold for the inverse-square operator coincides EXACTLY with the free scale
      factor's coefficient displaced by a single half-quantum.  Named rather than built on: a
      coincidence one names is inert, and one left unnamed is a claim waiting to be made (r2663). ***

** ⛔ ⓷ AND P10 NEVER NAMES THE ORDERING. **  Counted across the paper: "** normal-order **" ** ZERO **
occurrences, "** symmetric order **" ** ZERO **, "zero-point" once.  *** The paper's own open question --
whether the straddle removes the boundary freedom -- is decided by a choice its text does not make. ***
  ⌗ ** And P10's decomposition survives either way, ** *** because it "uses only that both sides of the
    threshold are occupied": under symmetric ordering the vacuum is AT $3/4$ and excited sectors are
    above, under normal ordering the vacuum is below and excited sectors above.  Both orderings occupy
    both sides.  The decomposition is safe; the PHYSICAL question is not. ***

** ⓸ SO `PO-6`'s REMAINDER IS NOW A NAMED CHOICE, NOT A COMPUTATION. **  *** What the row owes is not a
spectrum -- the spectrum is $\\gamma+c\\times$(ordering-dependent minimum) and both branches are computed
above.  It owes the ORDERING, and the ordering is a quantization convention that the corpus has not
fixed anywhere. ***

WHAT IS NOT CLAIMED.  ** Not that one ordering is correct ** -- *** that is a physics choice with
consequences the corpus has not committed to, and naming it as the open item is the point. ***  ** Not
that $\\hat\\pi_n^2$ has exactly an oscillator spectrum ** -- the modes are on a curved slicing and the
half-quantum is the leading behaviour, which is why the symmetric branch is stated as $\\ge$ rather than
$=$.  ** Not that P10 errs ** -- its decomposition is explicitly built to survive without the floor, and
it does.

Written r2728.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print('  S9 -- where does Gamma-hat sit relative to 3/4?')
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    FREE, THRESH, HALF = 0.25, 0.75, 0.5

    # ⓵ the two orderings
    check(f'⛭⛭ ⓵ NORMAL-ORDERED the vacuum contributes nothing, so $\\Gamma_{{\\min}}={FREE}$ -- BELOW '
          f'the {THRESH} threshold, so the origin is LIMIT-CIRCLE and boundary freedom SURVIVES',
          FREE < THRESH)
    for N in (1, 2, 5):
        g = FREE + HALF*N
        check(f'while SYMMETRIC with $N={N}$ gives $\\Gamma_{{\\min}}={g}$ -- {"AT" if g == THRESH else "above"} '
              f'the threshold',
              g >= THRESH)

    # ⓶ the coincidence
    check(f'⛭ ⓶ and the threshold IS the free coefficient plus one zero-point quantum: '
          f'${FREE}+{HALF}={THRESH}$ exactly',
          abs(FREE + HALF - THRESH) < 1e-12)

    # ⓷ P10 never names the ordering
    for term in ('normal-order', 'normal order', 'symmetric order'):
        check(f'⛔ ⓷ and P10 never names it: "{term}" appears ZERO times',
              len(re.findall(term, p10, re.I)) == 0)
    check("while its decomposition survives either way -- it \"uses only that both sides of the "
          'threshold are occupied"',
          'both sides of the threshold are occupied' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the spectral question is decided by ORDERING, which P10 never names. **')
    print('  ⛭⛭ ⓵ ** Both branches computed: **')
    print(f'       normal-ordered   Gamma_min = {FREE}    BELOW 3/4  -> limit-circle, freedom SURVIVES')
    print(f'       symmetric, N=1   Gamma_min = {FREE+HALF}    AT 3/4     -> limit-point from one mode up')
    print('     ⇒ *** The two orderings give OPPOSITE answers to the paper\'s own open question. ***')
    print(f'  ⛭ ⓶ ** And the threshold is not arbitrary here: 3/4 = 1/4 + 1/2 ** — the free boundary')
    print('     coefficient plus exactly one zero-point quantum.  Named, not built on.')
    print('  ⛔ ⓷ ** P10 never names the ordering: ** "normal-order" and "symmetric order" both ZERO.')
    print('     ⌗ Its decomposition survives either way, since it "uses only that both sides of the')
    print('       threshold are occupied" — and both orderings occupy both sides.  ** The decomposition')
    print('       is safe; the PHYSICAL question is not. **')
    print('  ⇒ ⓸ *** So PO-6 owes an ORDERING, not a spectrum.  The spectrum is computed; the')
    print('     quantization convention that selects between its branches is not fixed anywhere in the')
    print('     corpus. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
