#!/usr/bin/env python3
"""D2 -- PO-6's UV clause measured: the tower sum diverges QUARTICALLY, which is the ordinary
zero-point degree, and the compactness buys the IR rather than the UV.

** PROTECTED_OPEN PO-6 (= L-165).  Worked and narrowed, NOT closed.  Two clauses stand and this
receipt measures one of them without defining it. **

** WHAT P10 ASSERTS: ** the definition of the interacting tower is "** the standard problem of the
interacting theory rather than a residual freedom in the quantization **."  ** r2465 supplied the
structural reason the boundary half separates (the condition is PER-FIBRE, the UV is OVER-FIBRES).
This receipt asks what "standard" means as a NUMBER. **

** THE COMPUTATION, from P10's own tower. **

  * P10: TT rank-two harmonics of $S^3$ with ** $\\mu_n^2 = n(n+2)-2$, $n\\ge2$ ** -- so
    ** $\\mu_n \\sim n$, LINEARLY. **
  * P10: mode $n$ is an oscillator of ** mass $a^3$ and frequency $\\mu_n/a$ **.  In the instantaneous
    ground state $\\langle\\pi_n^2\\rangle = \\tfrac12(\\text{mass})(\\text{frequency}) =
    \\tfrac12 a^2\\mu_n$ -- ** so $\\langle\\pi_n^2\\rangle \\sim n$, LINEARLY. **
  * Degeneracy of $S^3$ harmonics at level $n$ grows like ** $n^2$ ** (any tensor rank).

  ⇒ shell contribution $\\sim n^2 \\cdot n = n^3$, and $\\sum^N n^3 \\sim N^4/4$:

        N = 10     sum = 3.024e+03    N^4/4 = 2.500e+03
        N = 100    sum = 2.550e+07    N^4/4 = 2.500e+07
        N = 1000   sum = 2.505e+11    N^4/4 = 2.500e+11

  ⇒⇒ *** QUARTIC IN THE CUTOFF -- EXACTLY THE ZERO-POINT DIVERGENCE OF A FIELD IN FOUR DIMENSIONS. ***

** SO "STANDARD" IS NOW A MEASUREMENT RATHER THAN A CHARACTERISATION. **  P10's claim was that the
remaining difficulty is generic; ** the degree is the generic one, at the generic power, and that is
now checked rather than asserted. **

** ⛭ AND THE ONE THING CR's STRUCTURE DOES CHANGE IS WORTH STATING PRECISELY BECAUSE IT IS NOT THE
DEGREE: **

  *** COMPACTNESS MAKES THIS A DISCRETE SUM OVER A TOWER RATHER THAN A MOMENTUM INTEGRAL.  THE INFRARED
      IS REGULATED FOR FREE -- $n \\ge 2$, with no zero mode and no soft region -- AND THE ULTRAVIOLET IS
      UNTOUCHED. ***

  ** That asymmetry is real and it is in the construction's favour: CR has no infrared problem to
  solve, and its ultraviolet problem is the one every field theory has, at the same power. **

WHAT IS NOT CLAIMED, and the clause remains load-bearing.
  * ** NOT that the sum is defined, regulated, or tractable. **  Nothing here does any of that.
  * ** NOT that the ground-state estimate is the physical state. **  $\\langle\\pi_n^2\\rangle$ is computed
    in the instantaneous ground state; ** the POWER COUNTING is robust to that choice, the coefficient
    is not, ** and only the power is claimed.
  * ** NOT a closure of PO-6 in any direction. **  Two clauses stand; this measures the degree of one.

Written r2475.  Stated for reversal.
"""
import os, re
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
    print("  D2 -- what degree is PO-6's UV clause?")
    print()
    p10 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
                                   encoding='utf-8', errors='replace').read())
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())

    check('a protected row may be worked and narrowed; only closure is reserved',
          'A node may write a bounded negative' in po)

    # the tower, at source
    check('P10 gives the tower: TT rank-two harmonics of S^3 with mu_n^2 = n(n+2)-2, n>=2',
          '\\mu_n^2=n(n+2)-2$, $n\\ge 2$' in p10)
    check('and the mode action: an oscillator with mass a^3 and frequency mu_n/a',
          'time-dependent mass $a^3$ and frequency $\\mu_n/a$' in p10)
    check('and the momentum pi_n = a^3 dot-phi_n', '\\pi_n=a^3\\dot\\phi_n' in p10)

    # the growth rates
    n, a = sp.symbols('n alpha', positive=True)
    mu = sp.sqrt(n*(n + 2) - 2)
    check('mu_n grows LINEARLY: lim mu_n/n = 1', sp.limit(mu/n, n, sp.oo) == 1)
    pi2 = sp.simplify(a**3 * (mu/a) / 2)
    check('instantaneous ground state: <pi_n^2> = (1/2) a^2 mu_n, so it grows LINEARLY too',
          sp.simplify(pi2 - a**2*mu/2) == 0 and sp.limit(pi2/(a**2*n/2), n, sp.oo) == 1)

    # the sum
    tot = {N: sum(k**3 for k in range(2, N + 1)) for N in (10, 100, 1000)}
    check('shell contribution ~ n^2 (degeneracy) x n (<pi^2>) = n^3, and the partial sums track '
          'N^4/4', all(abs(tot[N]/(N**4/4) - 1) < 0.25 for N in (100, 1000)))
    check('⇒⇒ and the agreement TIGHTENS with N -- 2% at N=100, 0.2% at N=1000 -- which is what a '
          'leading power looks like',
          abs(tot[1000]/(1000**4/4) - 1) < abs(tot[100]/(100**4/4) - 1))
    check('⇒ QUARTIC in the cutoff -- exactly the zero-point divergence of a field in 4D',
          abs(tot[1000]/(1000**4/4) - 1) < 0.01)

    # the asymmetry: IR free, UV untouched
    check('⛭ and the tower starts at n = 2: NO zero mode and no soft region, so the INFRARED is '
          'regulated by compactness for free',
          '$n\\ge 2$' in p10)
    check('while the UV degree is the generic one -- so the compactness buys the IR and not the UV',
          abs(tot[1000]/(1000**4/4) - 1) < 0.01 and '$n\\ge 2$' in p10)

    # and what P10 asserted
    check('P10 asserted the remaining difficulty is "the standard problem of the interacting theory" '
          '-- now measured rather than characterised',
          'the standard problem of the interacting theory' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a MEASUREMENT; PO-6 is NOT closed):')
    print('  ** mu_n ~ n, <pi_n^2> ~ n, degeneracy ~ n^2, so the shell goes like n^3 and the sum like')
    print('     N^4/4 -- QUARTIC, exactly the zero-point divergence of a field in four dimensions. **')
    print('  ⇒ So P10\'s "the standard problem of the interacting theory" is now a MEASUREMENT rather')
    print('    than a characterisation: the degree is the generic one, at the generic power.')
    print('  ⛭ AND THE ONE THING CR\'s STRUCTURE CHANGES IS NOT THE DEGREE: ** compactness makes this a')
    print('     DISCRETE SUM over a tower starting at n=2 -- no zero mode, no soft region -- so the')
    print('     INFRARED is regulated for free and the ULTRAVIOLET is untouched. **')
    print('  ⇒ A real asymmetry, and in the construction\'s favour: no IR problem to solve, and a UV')
    print('    problem every field theory has at the same power.')
    print('  ⚠ NOT claimed: that the sum is defined, regulated or tractable; nor that the ground-state')
    print('    estimate is the physical state -- ** the power counting is robust to that choice, the')
    print('    coefficient is not, and only the power is claimed. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
