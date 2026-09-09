#!/usr/bin/env python3
r"""
P10 — ** THE TENSOR TOWER'S SPECTRAL $\zeta(0)$ IS $10$, AND THE NO-FREE-CONSTANT CLAIM THEREFORE
NEEDS THE SCOPING `sec:frontier` ALREADY APPLIES LOCALLY. **  `CR_synthesis` `sec:ledger` turned the
claim into a prediction about a computable number --- *"that coefficient vanishes"* --- and on the
free static tower the coefficient does not vanish, on either reading of which spectral quantity
carries it: $\zeta(0)=10$ and $\operatorname{Res}_{s=-1}\zeta(s)=\tfrac{39}{4}$.

** THE SPECTRUM IS THE CORPUS'S, NOT THIS RECEIPT'S. **  `P10` `sec:lock` fixes it: Laplace
eigenvalues $\mu_n^2=n(n+2)-2$ for $n\ge2$, degeneracy $2(n-1)(n+3)$ (ten at the floor, derived there
from Peter--Weyl on the parallelizable $S^3=SU(2)$), frequency $\omega_n=\mu_n/a$, shell $2n^3$,
quartic divergence.  In $m=n+1\ge3$ that is $\mu^2=m^2-3$, $d=2(m^2-4)$ --- *the standard
transverse-traceless three-sphere form, so the corpus's own derivation and the textbook harmonic
analysis are the same numbers.*

** AND $\zeta(0)$ IS EXACT RATHER THAN NUMERICAL. **  Writing $(m^2-4)(m^2-3)^{-s/2}
= m^{2-s}\sum_j c_j(s)m^{-2j}$, at $s=0$ one has $c_j(0)=1,-4,0,0,\dots$ --- the series TERMINATES,
because $(1-4x)(1-3x)^0$ is a polynomial.  So
$$\zeta(0)=2\big[(\zeta_R(-2)-1-2^2)-4(\zeta_R(0)-1-1)\big]=2[-5+10]=10$$
is a finite exact identity carrying no truncation error, not an asymptotic estimate.

** ⛭ ONE PLACE THE CORPUS'S WORDING NEEDS CARE, AND THE VERDICT SURVIVES IT. **  `sec:ledger` says
the ambiguity's coefficient is "that function at zero".  For a functional DETERMINANT that is right:
$\zeta'(0)\to\zeta'(0)+\zeta(0)\ln\lambda$.  But the sums `sec:ledger` points at are the zero-point
sums $E=\tfrac12\sum_n d_n\omega_n=\tfrac12\zeta(-1)$ --- the ones it says diverge quartically --- and
THEIR log-scale coefficient is $\operatorname{Res}_{s=-1}\zeta$, a different number.
  ⇒ *Both are computed, so the verdict does not turn on which object the sentence meant.  Both are
    non-zero, so it does not need to.*  ⌗ The sentence should say which; that is a wording repair and
    not a change of content.

** ⌈ THE TOWER'S OR THE SCHEME'S -- THE QUESTION THIS LINE WAS TOLD TO ASK OF ITS OWN NUMBER. **  A
regularization result can be a property of the coding rather than of the construction; this line has
just spent two days finding such numbers, its own factor of $2.4$ among them.  Here the answer is
** the tower's **, and it is shown rather than asserted:
  · the log coefficient $\tfrac{39}{4}$ is reproduced by a HARD CUTOFF with no zeta function anywhere
    --- $\sum_{m=3}^{M}d_m\mu_m$ minus its exact polynomial part has $d/d\ln M \to 9.7498\ldots$
    against $39/4=9.75$, converging monotonically;
  · the same $\tfrac{39}{4}$ is the $1/m$ coefficient of the summand's own large-$m$ expansion;
  · $\zeta(0)$ and the residue are heat-kernel coefficients --- fixed by the spectrum's asymptotics,
    which is exactly what no choice of regulator can move.  *Schemes disagree about the FINITE part;
    they agree about the log coefficient, and that agreement is what is measured above.*
  ⌗ ** What WOULD tell them apart, stated so the discriminator is on the record: ** a number that is
    the scheme's changes when the regulator changes.  The cutoff and the zeta agree here to four
    digits and converging, so this one does not.

** ⛭ AND THE TIME-DEPENDENCE DOES NOT MOVE IT. **  $\omega_n=\mu_n/a(T)$ gives
$\zeta(s)=a^{s}Z(s)$ with $Z$ carrying no $a$, so $\zeta(0)=Z(0)$: ** the coefficient is independent
of the scale factor and does not evolve with the layer. **  *That is a partial answer to the first of
the two complications, not a dismissal of it: it says the leading coefficient does not evolve, not
that the regularization commutes with the evolution.*

** SCOPE -- WHAT THIS IS AND IS NOT, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** FREE and STATIC. **  The tower's couplings to the scale-factor sector are not in it, and the
    instantaneous spectrum is used.  `sec:lock` is explicit that the interacting tower is the open
    object; a free sum is a first step and this receipt is that step and no more.
  · ** TRANSVERSE-TRACELESS ONLY, and that is forced rather than chosen. **  Deparametrization solves
    the constraint, so the physical content IS the TT tower --- there are no ghost or conformal
    towers to cancel against, which is what makes a single number the whole answer.
  · ** It does not touch essential self-adjointness of the coupled system **, which `sec:lock` carries
    separately and which is nonperturbative.
  · ** It does not overturn the geometric ledger. **  What is measured is that the QUANTUM sector's
    mode sums spend one constant.  $c$, $G$, $\hbar$ as unit gauges over $\Lambda$ are untouched.

*** => THE READING. ***  `sec:ledger` offers the alternative itself: *"if it does not, the mode sums
spend one dimensionless constant and the claim needs the scoping sec:frontier already applies
locally."*  On the free static tower it does not, so that scoping is owed --- and the claim's own
sentence, unscoped where it names the quantum sector, is the thing to repair.
  ⌗ *What would overturn this is a coupled or non-adiabatic computation returning zero.  Nothing here
    forbids it; what this rules out is the claim holding TRIVIALLY, on the most favourable case the
    construction offers --- physical modes only, no ghosts, constraints already solved.*

Written r4568.  Stated for reversal.
"""
import os
import subprocess
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'ZETA_the_tensor_towers_spectral_zeta.py')
FAILED = []
M_, S_, X_ = sp.symbols('m s x', positive=True)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def paper(name):
    return ' '.join(open(os.path.join(ROOT, 'corpus', name), encoding='utf-8',
                         errors='replace').read().split())


def main():
    print()
    print('  P10 -- the tower\'s spectral zeta(0), and what it does to the ledger claim')
    print()

    # ============================================================ (1) the spectrum is the paper's
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE SPECTRUM IS READ OFF THE PAPER, NOT SUPPLIED HERE')
    print('  ' + '=' * 74)
    p10 = paper('canonical_time.tex')
    check('⓵ P10 sec:lock states the Laplace eigenvalues mu_n^2 = n(n+2)-2 with n >= 2',
          'Laplace eigenvalues $\\mu_n^2=n(n+2)-2$, $n\\ge 2$' in p10)
    check('⓵ᵇ and the degeneracy 2(n-1)(n+3), ten at the floor -- a Peter-Weyl component count '
          'rather than a scaling',
          'the degeneracy is $2(n-1)(n+3)$' in p10 and 'ten at the floor' in p10)
    check('⓵ᶜ and the tower is time-dependent oscillators with frequency mu_n/a, one per tensor '
          'harmonic -- so the object is a countable system, not a field theory',
          'tower of time-dependent oscillators' in p10 and 'one per tensor harmonic' in p10)

    n = sp.Symbol('n', positive=True)
    mu2_m = sp.simplify((n * (n + 2) - 2).subs(n, M_ - 1))
    deg_m = sp.simplify((2 * (n - 1) * (n + 3)).subs(n, M_ - 1))
    check(f'⓵ᵈ in m = n+1 the paper\'s spectrum is mu^2 = {mu2_m}, d = {sp.factor(deg_m)} -- the '
          f'standard transverse-traceless S^3 form, so the corpus\'s own derivation and the textbook '
          f'harmonic analysis agree',
          sp.simplify(mu2_m - (M_ ** 2 - 3)) == 0
          and sp.simplify(deg_m - 2 * (M_ ** 2 - 4)) == 0)
    check('⓵ᵉ and the floor carries the paper\'s stated ten',
          deg_m.subs(M_, 3) == 10 and mu2_m.subs(M_, 3) == 6)

    # ============================================================ (2) zeta(0), exactly
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- *** zeta(0) = 10, AND IT IS EXACT ***')
    print('  ' + '=' * 74)
    f = (1 - 4 * X_) * (1 - 3 * X_) ** (-S_ / 2)
    ser = sp.expand(sp.series(f, X_, 0, 5).removeO())
    c = [sp.simplify(ser.coeff(X_, j)) for j in range(5)]
    c0 = [sp.simplify(cj.subs(S_, 0)) for cj in c]
    check(f'⓶ the asymptotic expansion TERMINATES at s=0 -- c_j(0) = {c0} -- so the continuation '
          f'has no remainder there and zeta(0) is a finite exact identity, not an estimate',
          c0[0] == 1 and c0[1] == -4 and all(x == 0 for x in c0[2:]))
    tail = lambda z: sp.zeta(z) - 1 - sp.Integer(2) ** (-z)
    z0 = sp.simplify(2 * (c0[0] * tail(sp.Integer(-2)) + c0[1] * tail(sp.Integer(0))))
    check(f'⓶ᵇ *** zeta(0) = 2[(zeta_R(-2) - 5) - 4(zeta_R(0) - 2)] = {z0}, WHICH IS NOT ZERO ***',
          z0 == 10)

    # ============================================================ (3) the other reading
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ AND THE OTHER READING OF "THE COEFFICIENT" IS ALSO NON-ZERO')
    print('  ' + '=' * 74)
    res = sp.simplify(2 * c[2].subs(S_, -1))
    asym = sp.expand(sp.series(2 * (M_ ** 2 - 4) * sp.sqrt(M_ ** 2 - 3), M_, sp.oo, 4).removeO())
    check(f'⓷ the zero-point sum E = (1/2) sum d_n omega_n = (1/2) zeta(-1) has its log-scale set by '
          f'Res_{{s=-1}} zeta = 2 c_2(-1) = {res} -- a DIFFERENT number from zeta(0), and the sums '
          f'sec:ledger points at are these',
          res == sp.Rational(39, 4))
    check(f'⓷ᵇ and the same 39/4 is the 1/m coefficient of the summand\'s own large-m expansion '
          f'({sp.nsimplify(asym)}) -- reached with no zeta function in the route',
          sp.simplify(asym.coeff(M_, -1)) == sp.Rational(39, 4))
    check('⓷ᶜ *** so on EITHER reading the coefficient fails to vanish, and the verdict does not '
          'turn on which object sec:ledger\'s sentence meant ***',
          z0 != 0 and res != 0)

    # ============================================================ (4) the tower's, not the scheme's
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌈ THE TOWER\'S OR THE SCHEME\'S: A CUTOFF WITH NO ZETA IN IT')
    print('  ' + '=' * 74)
    import mpmath as mp
    mp.mp.dps = 30

    def rem(M):
        tot = mp.fsum(2 * (m * m - 4) * mp.sqrt(m * m - 3) for m in range(3, M + 1))
        S3 = mp.mpf(M) ** 2 * (M + 1) ** 2 / 4 - 9
        S1 = mp.mpf(M) * (M + 1) / 2 - 3
        return tot - (2 * S3 - 11 * S1)

    pts = [(M, rem(M)) for M in (1000, 2000, 4000, 8000)]
    slopes = [float((pts[i][1] - pts[i - 1][1]) / mp.log(mp.mpf(pts[i][0]) / pts[i - 1][0]))
              for i in range(1, len(pts))]
    for (M0, _), (M1, _), sl in zip(pts, pts[1:], slopes):
        print(f'      cutoff {M0:>5} -> {M1:<5}   d(sum)/d(ln M) = {sl:.6f}      (39/4 = 9.75)')
    check(f'⓸ a HARD CUTOFF -- no zeta function anywhere in it -- returns the same log coefficient: '
          f'the slope is {slopes[-1]:.4f} against 39/4 = 9.75 and is still rising toward it',
          abs(slopes[-1] - 9.75) < 0.01)
    check('⓸ᵇ and it approaches monotonically from below rather than straddling, which is what an '
          'asymptotic series does and a coincidence does not',
          all(slopes[i] > slopes[i - 1] for i in range(1, len(slopes)))
          and all(s < 9.75 for s in slopes))
    # ⛭ the cross-scheme claim is TESTED and not asserted: the cutoff slope is compared against the
    #   number the ZETA route produced, so the check fails if the two regulators ever disagree.
    gap = abs(slopes[-1] - float(res))
    check(f'⓸ᶜ ⇒ THE NUMBER IS THE TOWER\'S, NOT THE SCHEME\'S: the cutoff\'s slope and the zeta\'s '
          f'residue -- computed by routes sharing no machinery -- agree to {gap:.4f}, and the gap is '
          f'the cutoff\'s own 1/ln M convergence rather than a disagreement.  *A scheme artefact is '
          f'exactly what moves when the regulator moves, and this does not.*',
          gap < 0.01)

    # ============================================================ (5) time-dependence
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⛭ THE SCALE FACTOR DOES NOT MOVE IT EITHER')
    print('  ' + '=' * 74)
    a = sp.Symbol('a', positive=True)
    # zeta(s) = sum d (mu/a)^{-s} = a^s Z(s);  at s=0 the prefactor is 1
    check('⓹ omega_n = mu_n/a(T) gives zeta(s) = a^s Z(s), so zeta(0) = Z(0) is INDEPENDENT of the '
          'scale factor -- the coefficient does not evolve with the layer, which answers part of the '
          'time-dependence complication without pretending to answer all of it',
          sp.simplify((a ** S_).subs(S_, 0)) == 1)

    # ============================================================ (6) the claim it bears on
    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- ⛔ WHAT THIS DOES TO THE LEDGER CLAIM')
    print('  ' + '=' * 74)
    syn = paper('CR_synthesis.tex')
    check('⓺ CR_synthesis sec:ledger makes the prediction in its own words -- the coefficient '
          'vanishes -- and names the consequence if it does not',
          'makes a prediction about a computable number' in syn
          and 'that coefficient vanishes' in syn
          and 'the mode sums spend one dimensionless constant' in syn)
    check('⓺ᵇ and it names the repair itself: the claim needs the scoping sec:frontier already '
          'applies locally',
          'needs the scoping' in syn)
    check('⓺ᶜ *** THE MEASURED COEFFICIENT IS NON-ZERO, SO THE SCOPING IS OWED. *** The free static '
          'tower spends one dimensionless constant.',
          z0 != 0)

    # ============================================================ (6b) what the log costs
    print()
    print('  ' + '=' * 74)
    print('  PART 6b -- ⛔⛭ AND THE PAPER ALREADY NAMES THE COUNTERTERM A NON-ZERO LOG NEEDS')
    print('  ' + '=' * 74)
    check('⓺ᵈ P10 sec:lock disposes of the LEADING quartic term itself: it is field-independent, so '
          'it is a constant vacuum energy whose counterterm is a cosmological-constant term -- "the '
          'framework\'s single dimensionful constant, absorbed into the one observed curvature"',
          'the counterterm a constant vacuum energy requires is a cosmological-constant term' in p10)
    check('⓺ᵉ *** but it says the SUCCESSORS are different in kind: "only the quadratic and '
          'logarithmic successors carry the mass", the logarithmic one going "with curvature-squared '
          'invariants, and a curvature-squared coupling is NOT AN ENTRY IN THIS FRAMEWORK\'S '
          'LEDGER" ***',
          'quadratic and logarithmic successors' in p10
          and 'a curvature-squared coupling is not an entry in this framework' in p10)
    check('⓺ᶠ ⇒ SO THE MEASUREMENT LANDS ON A COUNTERTERM THE LEDGER LACKS, NOT MERELY ON AN '
          'UNSCOPED SENTENCE.  The 39/4 is the coefficient of exactly the logarithmic successor the '
          'paper singles out; the quartic leader it had already absorbed into Lambda, and this is '
          'the next term along, which it says it cannot absorb the same way.',
          res != 0)

    # ============================================================ (7) the computation runs
    print()
    print('  ' + '=' * 74)
    print('  PART 7 -- the computation is a file that runs, not a quotation')
    print('  ' + '=' * 74)
    r = subprocess.run([sys.executable, COMP], capture_output=True, text=True, errors='replace')
    check('⓻ the computation exits 0 and reports both numbers',
          r.returncode == 0 and 'zeta(0) = 10' in r.stdout and '39/4' in r.stdout)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** zeta(0) = 10 AND Res_{s=-1} = 39/4.  THE COEFFICIENT DOES NOT VANISH. ***')
    print('    ⛔ And the paper names the cost itself: the quartic leader it absorbs into Lambda,')
    print('       but the LOGARITHMIC successor goes with curvature-squared invariants and "a')
    print('       curvature-squared coupling is not an entry in this framework\'s ledger".')
    print('    On the free static tower -- physical TT modes only, no ghosts, constraints already')
    print('    solved, which is the most favourable case the construction offers -- the mode sums')
    print('    spend one dimensionless constant, and sec:ledger\'s claim needs the scoping its own')
    print('    sentence names.  ⌗ FREE and STATIC: the coupled and non-adiabatic tower is not')
    print('    computed here and could still return zero; what is excluded is the claim holding')
    print('    trivially.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
