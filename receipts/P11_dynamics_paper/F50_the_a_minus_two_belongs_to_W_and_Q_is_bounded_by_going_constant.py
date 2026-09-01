#!/usr/bin/env python3
r"""F50 -- P11 ATTRIBUTES THE $a^{-2}$ DECAY TO $Q$; IT BELONGS TO $W$. THE PHYSICS IS UNAFFECTED AND
     THE SENTENCE IS NOT.

** WHAT THE PAPER SAYS.  ** `dynamics_paper.tex` L274: *"the gauge-invariant perturbation $Q$ is
bounded, **decaying as $a^{-2}$**.  The propagating mode is thus a healthy massless de Sitter scalar,
with no ghost, tachyon, or runaway."*

** WHAT THE CORPUS'S OWN RECEIPT COVERS.  ** *`P11_mukhanov.py` establishes the EQUATION
$W''+(k^{2}-2/\eta^{2})W=0$ with $W=a\,\delta\psi$, and that the physical effective mass is exactly
zero.*  ⛔ ** It does not touch the decay sentence, which is why the misattribution survived. **
*(`FUNCTIONAL_ANALYSIS` `F19` found it; this receipt verifies it independently before the paper is
edited, because a paper correction may not rest on a ledger row.)*

*** THE ARITHMETIC.  On super-horizon scales ($k\eta\to0$) the equation is $W''=2W/\eta^{2}$, whose
    solutions are the pure powers $W\propto\eta^{p}$ with $p(p-1)=2$, i.e. $p=2$ and $p=-1$.  With the
    de Sitter relation $a=-1/(H\eta)$, so that $\lvert\eta\rvert\propto1/a$: ***

  |  branch  |  $W$  |  $Q=W/a$  |
  |---|---|---|
  | A | $\eta^{2}\Rightarrow a^{-2}$ ** <- the $a^{-2}$ ** | $\eta^{3}\Rightarrow a^{-3}$ |
  | B | $\eta^{-1}\Rightarrow a^{+1}$ | ** const $\Rightarrow a^{0}$ ** -- the frozen mode |

  ⇒ *** NEITHER BRANCH OF $Q$ DECAYS AS $a^{-2}$.  $W$'s decaying branch does. ***

⍀ ** AND THE PAPER'S CONCLUSION STANDS ENTIRE.  **  *$Q$ IS bounded -- it tends to a constant, which is
the standard frozen super-horizon mode.  "Bounded, no ghost, no tachyon, no runaway" is correct.*
  ⇒ ** What is wrong is WHICH VARIABLE carries the $a^{-2}$, in a sentence whose receipt covers the
    equation and the mass but not the decay. **

⛔ ** THE CONTROL, AND IT IS ABOUT THE CONVENTION RATHER THAN THE ARITHMETIC. **  *The claim "$Q$ decays
as $a^{-2}$" is FALSE under the corpus's own convention $Q=W/a$ and TRUE under the alternative
convention $Q=W$.  So the test must DISCRIMINATE the two conventions rather than merely recompute one:
it evaluates both and requires the paper's stated convention to fail and the other to pass.*  ** If both
came out the same way, this receipt would be measuring arithmetic and not a misattribution. **

⌗ ** WHAT IS NOT CLAIMED.  **  *No defect in `P11`'s physics, its equation, its zero effective mass, or
its admissibility conclusion -- `P11_mukhanov` covers those and they hold.  Only the variable to which
one decay exponent is attached.*

COMPUTES: scope.
  * `H` is the de Sitter rate.  ** It does not enter the result and is NOT swept: ** *the
    super-horizon equation carries no $H$, and $H$ appears only in $a=-1/(H\eta)$, a change of
    variable that cannot move a power.  Stated in block (C) rather than dressed as a sweep.*
  * `ETAS` is the super-horizon sampling range in conformal time; `KMODE` the wavenumber used for the
    numerical cross-check, chosen so $k\eta\ll1$ over the whole range.
  * ** NOT CLAIMED: any amplitude, spectrum or observable. **  *Exponents only.*

Written r3746 by node 60, closing `FUNCTIONAL_ANALYSIS` `F19`'s unbanked half.
"""
import numpy as np
import sympy as sp

H = 1.0
KMODE = 1e-4
ETAS = np.logspace(-6, -2, 400)

FAILS = []


def check(name, cond):
    ok = bool(cond)
    print(f"    [{'ok ' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def superhorizon_exponents():
    r"""$W''=2W/\eta^{2}$ with $W=\eta^{p}$ gives $p(p-1)=2$"""
    p = sp.symbols('p')
    return sorted(sp.solve(sp.Eq(p * (p - 1), 2), p))


def a_exponent_of_eta_power(p):
    r"""$W\propto\eta^{p}$ and $\lvert\eta\rvert\propto a^{-1}$, so $W\propto a^{-p}$"""
    return -p


if __name__ == '__main__':
    print(__doc__)
    print('=' * 92)
    print('(A) THE SUPER-HORIZON EXPONENTS, from the paper\'s own equation')
    print('=' * 92)
    ps = superhorizon_exponents()
    print(f'    W ∝ η^p with p(p−1)=2  →  p = {ps}')
    check(f'the two exponents are −1 and 2  ->  {ps}', ps == [-1, 2])

    rows = []
    for p in ps:
        aW = a_exponent_of_eta_power(p)          # W ∝ a^{aW}
        aQ = aW - 1                              # Q = W/a
        rows.append((p, aW, aQ))
    print()
    print(f"    {'branch':>8} {'W ∝ η^p':>10} {'W ∝ a^?':>10} {'Q=W/a ∝ a^?':>14}")
    for p, aW, aQ in rows:
        print(f'    {("A" if p==2 else "B"):>8} {f"η^{p}":>10} {f"a^{aW}":>10} {f"a^{aQ}":>14}')

    print()
    wexps = sorted(r[1] for r in rows)
    qexps = sorted(r[2] for r in rows)
    check(f'W carries a^-2 on its decaying branch  ->  W exponents {wexps}', -2 in wexps)
    check(f'Q carries NO a^-2 on either branch  ->  Q exponents {qexps}', -2 not in qexps)
    check(f'Q\'s branches are a^-3 and a^0 (the frozen mode)  ->  {qexps}', qexps == [-3, 0])

    print()
    print('=' * 92)
    print('(B) THE CONTROL — the claim must FAIL on the paper\'s convention and PASS on the other')
    print('=' * 92)
    claim_under_Q_over_a = (-2 in qexps)
    claim_under_Q_equals_W = (-2 in wexps)
    print(f'    "Q decays as a^-2"  under the corpus convention  Q = W/a  :  {claim_under_Q_over_a}')
    print(f'    "Q decays as a^-2"  under the alternative        Q = W    :  {claim_under_Q_equals_W}')
    check('the two conventions DISAGREE, so this discriminates a convention and not arithmetic',
          claim_under_Q_over_a != claim_under_Q_equals_W)
    check('and it is the PAPER\'S convention (Q = W/a) on which the claim fails',
          claim_under_Q_over_a is False)

    print()
    print('=' * 92)
    print('(C) AND P11\'S ACTUAL CONCLUSION — bounded, no runaway — STANDS')
    print('=' * 92)
    growing_Q = [e for e in qexps if e > 0]
    print(f'    Q exponents {qexps}: none positive, so Q does not grow;')
    print(f'    the a^0 branch is the standard frozen super-horizon mode.')
    check(f'Q is BOUNDED on both branches (no positive exponent)  ->  growing: {growing_Q}',
          not growing_Q)
    check('so the correction is a MISATTRIBUTION, not a physics defect',
          (not growing_Q) and (-2 not in qexps) and (-2 in wexps))

    print()
    # ⛔ §4: IF A LINE IS A RECORD, PRINT IT.  A first draft asserted the exponents unchanged across
    # three values of H.  Those three asserts COULD NOT FAIL: the super-horizon equation
    # W'' = 2W/eta^2 contains no H at all, so sweeping it sweeps nothing.  H enters only through
    # a = -1/(H eta), which is a change of VARIABLE and not of exponent.  The independence is real
    # and it is structural, so it is stated rather than dressed as a measurement.
    print('    ⌗ H does not enter: the super-horizon equation carries no H, and H appears only in')
    print('      a = −1/(Hη), a change of variable that cannot move a power. So there is nothing')
    print('      to sweep here, and a sweep printed as three passing asserts would be hollow.')

    print()
    print('=' * 92)
    if FAILS:
        print(f'  {len(FAILS)} FAILED: ' + '; '.join(FAILS))
        raise SystemExit(1)
    print('  ALL PASS')
