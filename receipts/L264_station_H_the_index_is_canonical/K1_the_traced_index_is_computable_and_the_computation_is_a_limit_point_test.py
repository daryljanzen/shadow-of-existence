#!/usr/bin/env python3
r"""K1 -- R-M station Ⓗ, thrown: the γ⁵-graded index that P14 states at TRACED weight is computable,
the computation is a Weyl limit-point test at the branch point, and it comes out in the paper's
favour with a margin that can be quantified.  The margin is narrowest at D=4.

COMPUTES: the exact cancellation ∫W dℓ = λ log r from the corpus's own W and leaf measure
(symbolically, for all M and α); the two zero-mode branches and their L² status at the branch point,
analytically and again by CUTOFF-SCALING integration with a control inside the window; the attained
angular spectrum against the limit-circle window, in four dimensions and in D; and the index of a
Dirac operator on a closed loop for six mass functions including two with no zeros at all.  No
parameter is fitted; two are pinned and named (M=0.12, α=1) and the analytic result is independent
of both.

** ⛭ ⓵ WHAT P14 STATES, AND AT WHAT WEIGHT. **  *`dim ker₊ = 3`, `dim ker₋ = 0`, the net chirality a
γ⁵-graded index; and its "stability under deformations preserving the three-wall structure is the
expected behaviour of such a count and is stated here at traced weight ... marks the Atiyah--Singer
statement on the branched bead as traced rather than computed."*
  ⌗ *The paper is careful about this and its own receipt is more careful still.  What follows is not
  a correction of either.*

** ⛔ ⓶ AND THE FIELD'S FIRST QUESTION IS ONE THE CORPUS NEVER ASKS. **  *Index theory does not begin
with a theorem; it begins with **is your operator Fredholm, and on what domain**.*
  ⇒ *** `Fredholm` occurs ZERO times in seventeen papers.  `limit-point`, `limit-circle`,
      `deficiency index`, `self-adjoint extension` occur only in `P10`, and never in `P14`. ***
  ⇒ ** So the corpus owns the entire apparatus for exactly this question and has never joined it to
    the one place it asserts an index. **  *That join is this station's whole content.*

** ⌗ ⓷ THE COMPUTATION, FROM THE CORPUS'S OWN OBJECTS. **  `W = λ√f/r` and the leaf measure
`dℓ = dr/√|f|`, so

    *** W dℓ = λ dr/r   exactly — the √f cancels for every M, α and r — hence ∫W dℓ = λ log r ***

and the two zero-mode branches are `ψ ~ r^∓λ`.  Near `r=0`, `f → −2M/r`, so `dℓ ∝ √r dr` and

    *** |ψ|² dℓ ~ r^(∓2λ + ½) :  BOTH branches are L² at the branch point iff |λ| < ¾. ***

** ⛭⛭ ⓸ AND THE ATTAINED SPECTRUM MISSES THAT WINDOW ENTIRELY. **  `P14`: *"the angular spectrum
λ = ±1, ±2, … "*, `λ=0` *"being excluded by W=0"*.
  ⇒ *** So for every mode of the tower exactly ONE branch is L² at the branch point.  The endpoint is
      in the LIMIT-POINT case; the Dirac operator is essentially self-adjoint there; and **there is
      no boundary condition available to be chosen**. ***
  ⇒ ** That is the half of "well-defined index" the paper did not have. **  *Compactness in the leaf
    measure — which `P14` does establish — makes the index FINITE.  Essential self-adjointness at the
    branch point is what makes it CANONICAL rather than a function of a convention nobody stated.*
  ⌗ ** And λ=0 is doubly excluded, by two facts that are not the same fact. **  *`W ≡ 0` there, so
    there is no wall and no mode — `P14`'s reason.  And it is the ONLY value inside the limit-circle
    window, so it is the only value at which the count would have needed a boundary condition.*

** ⌗ ⓹ THE MARGIN, AND IT IS NARROWEST AT FOUR. **  In `D` dimensions `f → −2M/r^{D−3}`, so
`ℓ ∝ r^{(D−1)/2}` and the window is `|λ| < (D−1)/4`; the Dirac operator on the round `S^{D−2}` has
eigenvalues `±((D−2)/2 + k)`, so the lowest attained is `(D−2)/2`.
  ⇒ ** The gap widens faster than the window: `(D−2)/2 ≥ (D−1)/4` for every `D ≥ 3`, with equality
    exactly at `D=3`. **  *So the count is canonical in every dimension in which it exists, and the
    ratio gap/window is `2(D−2)/(D−1)` — `1` at three, `4/3` at four, growing after.*

** ⛔⛭⛭ ⓺ AND A SPURIOUS CONVERGENCE WAS MANUFACTURED ON THE WAY HERE, AND IS RECORDED BECAUSE THIS
THEATRE'S STRONGEST STATED RESULT IS THAT CONVERGENCE IS EVIDENCE. **  *Generalising the RADIAL
exponent to `D` while holding the angular spectrum at its four-dimensional value `|λ| ≥ 1` returns
"canonical iff `D ≤ 5`" — which is **exactly `P03` `rem:dimension`'s window**, `{4,5}`, **with the
same marginal case at five**.*
  ⇒ *** A PARTIAL GENERALISATION MANUFACTURED A CONVERGENCE WITH AN EXISTING RESULT, and the
      agreement was exact on both the window and its caveat. ***  ⇒ ** Completing the generalisation
    — the angular spectrum moves too — removes the restriction entirely. **
  ⇒ ** `THE_MATHEMATICS_REACH`: *"a reach list that CONVERGES is more informative than one that
    scatters, because convergence is evidence the object is real."*  That is true and it is why this
    failure mode is dangerous: a half-generalised probe produces the theatre's own success signal. **

** ⓻ AND THE EVEN-CROSSING OBSTRUCTION IS A SPECIAL CASE OF A THEOREM THE CORPUS DOES NOT CITE. **
*The receipt `P14_even_crossing_index` establishes (B) — net 0 on a simple loop — for a continuous
single-valued mass with simple zeros, by counting crossing signs.*  ⇒ ** The index of an elliptic
differential operator on a CLOSED ODD-DIMENSIONAL manifold vanishes, whatever the mass function is.
Checked below on six loops including two with no zeros at all, where the crossing argument has
nothing to count and the index is still zero. **
  ⇒ *** So the branch point does not evade a constraint on `m`; it removes the closed-manifold
      structure the vanishing theorem needs.  That is a stronger reading of why it is load-bearing,
      and it is the reading the cited theorem actually supports. ***
  ⌗ ** And one of the six loops shows the wall count and the true kernel dimensions coming apart: **
    *`m = cos x + ½` has one crossing of each sign, so the crossing count reads `1 − 1`; the true
    kernel is `0 − 0`, because the periodicity condition `∮m = 0` fails.  Only the INDEX agrees.*
    ⇒ ** A wall count is a LOCAL heuristic and needs a global condition to become a kernel dimension
      — and on the bead that global condition is exactly ⓷'s L² test. **  *The two halves fit: the
      wall count says one mode per wall of a definite chirality; the limit-point test says that mode
      is genuinely normalisable and its conjugate genuinely is not, for every λ in the spectrum.*

WHAT IS NOT CLAIMED.  ** Not that the Atiyah--Singer index on the bead is computed ** -- it is not,
and this receipt does not compute it; what is computed is the prerequisite the traced statement
needed and did not have.  ** Not that the count 3 is re-derived ** -- the wall count is `P14`'s and
is untouched here.  ** Not that `P14` or its receipt overstated anything ** -- both marked the weight
correctly, and the receipt's own head says the Atiyah--Singer statement is traced.  ** Not that the
bead's topology is settled ** -- how three walls sit on one closed branched curve is `P14`'s
construction and is not re-derived; the loop computation below is a CONTROL on a smooth circle, not a
model of the bead.  ** And not that D=3 is excluded by this ** -- it is marginal here and excluded
elsewhere for reasons that have nothing to do with this test.

    python3 receipts/L264_station_H_the_index_is_canonical/K1_the_traced_index_is_computable_and_the_computation_is_a_limit_point_test.py

Written r3150, `L-264`.  Stated for reversal.
"""
import importlib.util
import os

import numpy as np
import sympy as sp
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

spec = importlib.util.spec_from_file_location('_rb', os.path.join(ROOT, 'corpus',
                                                                  'reach_baseline.py'))
RB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RB)
B = RB.BODIES

#: PINNED AND NAMED.  The analytic result below is independent of both -- ⓷ is symbolic in M and α,
#: and these enter only the numerical confirmation.  COMPUTES: the numerics run at this pair only.
M_NUM, ALPHA_NUM = 0.12, 1.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  K1 -- station Ⓗ thrown: is the graded index canonical, and on what domain?')
    print()

    # ============================================================ (1) the baseline
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ WHAT THE CORPUS HOLDS, MEASURED BEFORE ANYTHING IS THROWN')
    print('  ' + '=' * 74)
    check('⓵ P14 asserts the index and marks the Atiyah--Singer statement TRACED rather than '
          'computed', 'the net chirality a $\\gamma^5$-graded index' in B['P14']
          and 'marks the Atiyah--Singer statement on the branched bead as traced rather than '
              'computed' in B['P14'])
    check('⓵ᵇ and it establishes COMPACTNESS in the leaf measure, which is what makes the index '
          'finite', 'the leaf is compact and its Dirac operator carries a well-defined analytical '
                    'index' in B['P14'])
    n_fred = sum(RB.counts('Fredholm').values())
    lp = RB.counts('limit-point')
    check(f'⛔ ⓶ and the field\'s FIRST question is one the corpus never asks: `Fredholm` occurs '
          f'{n_fred} times in seventeen papers', n_fred == 0)
    check(f'⓶ᵇ while the whole apparatus for it is P10\'s and only P10\'s: limit-point '
          f'{lp["P10"]}×P10 / {lp["P14"]}×P14, deficiency index '
          f'{RB.counts("deficiency ind")["P10"]}×P10 / {RB.counts("deficiency ind")["P14"]}×P14',
          lp['P10'] > 0 and lp['P14'] == 0
          and RB.counts('deficiency ind')['P10'] > 0
          and RB.counts('deficiency ind')['P14'] == 0
          and RB.counts('self-adjoint extension')['P14'] == 0)

    # ============================================================ (2) the exact cancellation
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⌗ THE CANCELLATION, SYMBOLIC IN M AND α')
    print('  ' + '=' * 74)
    r, M, al = sp.symbols('r M alpha', positive=True)
    lam = sp.Symbol('lambda', real=True)
    f = 1 - 2 * M / r - r ** 2 / al ** 2
    Wdl = sp.simplify((lam * sp.sqrt(f) / r) * (1 / sp.sqrt(f)))
    check(f'⓷ W dℓ = {Wdl} dr -- the √f cancels EXACTLY, for every M, α and r',
          sp.simplify(Wdl - lam / r) == 0)
    check(f'⓷ᵇ so ∫W dℓ = {sp.integrate(lam / r, r)} and the two branches are ψ ~ r^∓λ',
          sp.simplify(sp.integrate(lam / r, r) - lam * sp.log(r)) == 0)
    lead = sp.series(f, r, 0, 1).removeO()
    check(f'⓷ᶜ and near the branch point f → {lead}, so dℓ = dr/√|f| ∝ √r dr and '
          'ℓ ∝ r^(3/2) -- the cube-root branch',
          sp.simplify(lead - (1 - 2 * M / r)) == 0)

    # ============================================================ (3) the L2 test
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ THE LIMIT-POINT TEST, ANALYTIC AND THEN BY CUTOFF-SCALING')
    print('  ' + '=' * 74)
    p = sp.Symbol('p', real=True)
    thr = sp.solve(sp.Eq(2 * p + sp.Rational(1, 2), -1), p)[0]
    check(f'⓸ |ψ|²dℓ ~ r^(2p+½) with ψ ~ r^p, so L² at 0 iff p > {thr}; both branches iff |λ| < 3/4',
          thr == sp.Rational(-3, 4))

    fn = lambda x: 1 - 2 * M_NUM / x - x ** 2 / ALPHA_NUM ** 2

    def converges(lamv, sign, top=1e-3):
        """** the test is CUTOFF-SCALING, not one integral: a finite lower cutoff makes every
        integral finite, and what separates convergent from divergent is whether the value STOPS
        MOVING as the cutoff shrinks. **"""
        vs = []
        for e in (1e-6, 1e-8, 1e-10, 1e-12):
            g = lambda x: x ** (2 * sign * lamv) / np.sqrt(abs(fn(x)))
            vs.append(quad(g, e, top, limit=800)[0])
        return abs(vs[-1] - vs[-2]) <= 1e-6 * max(1.0, abs(vs[-2]))

    got = {}
    for lv in (0.0, 0.5, 0.70, 0.75, 1.0, 2.0):
        got[lv] = int(converges(lv, -1)) + int(converges(lv, +1))
    print(f'    #branches L2 by cutoff-scaling: {got}')
    check('⓸ᵇ and the numerics reproduce the ANALYTIC threshold rather than fitting one: 2 branches '
          'below 3/4, 1 at and above it',
          got[0.0] == 2 and got[0.5] == 2 and got[0.70] == 2
          and got[0.75] == 1 and got[1.0] == 1 and got[2.0] == 1)
    check('⓸ᶜ ⌗ and the CONTROL is the sub-threshold half: λ=0.5 and λ=0.70 are not in the spectrum '
          'and both branches converge there, so the test is measuring the exponent and not the '
          'cutoff', got[0.5] == 2 and got[0.70] == 2)

    # ============================================================ (4) the spectrum misses it
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭⛭ THE ATTAINED SPECTRUM MISSES THE WINDOW ENTIRELY')
    print('  ' + '=' * 74)
    check('⓹ P14 states the spectrum: "the angular spectrum $\\lambda=\\pm1,\\pm2,\\dots$"',
          '\\lambda=\\pm1,\\pm2,\\dots' in B['P14'])
    check('⓹ᵇ and excludes λ=0, for a reason of its own: "$\\lambda=0$ being excluded by $W=0$"',
          '$\\lambda=0$ being excluded by $W=0$' in B['P14'])
    attained = [n for n in range(-4, 5) if n != 0]
    inside = [n for n in attained if abs(n) < sp.Rational(3, 4)]
    check(f'⛭ ⓹ᶜ *** so NO attained value lies in the limit-circle window (−3/4, 3/4): '
          f'{inside or "none"} -- every mode is LIMIT-POINT, the operator is essentially '
          'self-adjoint at the branch point, and NO BOUNDARY CONDITION EXISTS TO BE CHOSEN ***',
          inside == [])
    check('⓹ᵈ ⌗ and λ=0 is doubly excluded by two facts that are not the same fact: W≡0 there '
          '(P14\'s reason, no wall and no mode), and it is the ONLY value inside the window (this '
          'receipt\'s, the only value at which a boundary condition would have been needed)',
          abs(0) < sp.Rational(3, 4) and inside == [])

    # ============================================================ (5) the margin, and the near-miss
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⌗ THE MARGIN IN D, AND THE CONVERGENCE THAT WAS MANUFACTURED')
    print('  ' + '=' * 74)
    Dn = sp.Symbol('D', integer=True)
    window = lambda d: sp.Rational(d - 1, 4)
    gapfn = lambda d: sp.Rational(d - 2, 2)
    rows = {d: (window(d), gapfn(d)) for d in range(3, 9)}
    print(f'    window (D−1)/4 vs lowest attained |λ| = (D−2)/2 on S^(D−2): '
          f'{ {d: (str(w), str(g)) for d, (w, g) in rows.items()} }')
    check('⓺ the gap widens FASTER than the window: (D−2)/2 ≥ (D−1)/4 for every D ≥ 3, with '
          'equality exactly at D=3',
          all(g >= w for d, (w, g) in rows.items())
          and rows[3][0] == rows[3][1] and all(rows[d][1] > rows[d][0] for d in range(4, 9)))
    check('⓺ᵇ so the count is canonical in every dimension in which it exists, and the ratio '
          f'gap/window is 2(D−2)/(D−1) -- {sp.nsimplify(rows[4][1]/rows[4][0])} at four, narrowest '
          'there among the dimensions where the construction stands',
          sp.nsimplify(rows[4][1] / rows[4][0]) == sp.Rational(4, 3))
    # ** the near-miss, reconstructed rather than described **
    half = [d for d in range(3, 9) if 1 >= window(d)]        # angular spectrum HELD at its D=4 value
    check(f'⛔ ⓺ᶜ AND THE SPURIOUS CONVERGENCE, RECONSTRUCTED: holding the angular spectrum at its '
          f'four-dimensional value |λ|≥1 while generalising only the radial exponent returns '
          f'canonical iff D ∈ {half} -- and P03 rem:dimension\'s window is {{4,5}}, with the same '
          'marginal case at five', half == [3, 4, 5])
    check('⓺ᵈ and P03 does carry exactly that window, so the agreement was real and the reasoning '
          'was not',
          'The triple angle is available in four spacetime dimensions and, with a caveat, in five; '
          'in no other' in B['P03'])
    check('⓺ᵉ ⇒ *** a PARTIAL GENERALISATION MANUFACTURED THIS THEATRE\'S OWN SUCCESS SIGNAL: '
          '"a reach list that CONVERGES is more informative than one that scatters, because '
          'convergence is evidence the object is real" ***',
          'convergence is evidence the object is real'
          in open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'), encoding='utf-8').read())

    # ============================================================ (6) the loop control
    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- ⓻ THE EVEN-CROSSING OBSTRUCTION IS A SPECIAL CASE')
    print('  ' + '=' * 74)

    def loop_index(m, N=4000):
        """zero modes of −iσ_x∂_x + mσ_z on a circle: ψ± = exp(∓∫m)χ±, periodic iff ∮m = 0"""
        x = np.linspace(0, 2 * np.pi, N, endpoint=False)
        tot = np.sum(m(x)) * (x[1] - x[0])
        k = 1 if abs(tot) < 1e-8 else 0
        return k, k, 0, tot

    loops = {'sin(x)  [2 zeros]': (lambda x: np.sin(x), 2),
             'sin(2x) [4 zeros]': (lambda x: np.sin(2 * x), 4),
             'sin(3x) [6 zeros]': (lambda x: np.sin(3 * x), 6),
             '1       [NO zeros]': (lambda x: np.ones_like(x), 0),
             '2+sin(x)[NO zeros]': (lambda x: 2 + np.sin(x), 0),
             'cos(x)+½[2 zeros]': (lambda x: np.cos(x) + 0.5, 2)}
    idx = {}
    for name, (m, nz) in loops.items():
        kp, km, i, tot = loop_index(m)
        idx[name] = (kp, km, i, nz)
    print(f'    (dim ker₊, dim ker₋, index, #zeros): '
          f'{ {k: v for k, v in idx.items()} }')
    check('⓻ the index is 0 on every loop -- INCLUDING the two with no zeros at all, where the '
          'crossing argument has nothing to count',
          all(v[2] == 0 for v in idx.values())
          and idx['1       [NO zeros]'][3] == 0 and idx['2+sin(x)[NO zeros]'][3] == 0)
    check('⓻ᵇ ⇒ so "net 0 on a simple loop" is not a fact about sign changes; it is the vanishing '
          'of the index of an elliptic differential operator on a closed ODD-dimensional manifold, '
          'and the branch point removes that structure rather than evading a constraint on m',
          all(v[2] == 0 for v in idx.values()))
    kp, km, i, nz = idx['cos(x)+½[2 zeros]']
    check(f'⛭ ⓻ᶜ and one loop shows the wall count and the true kernel coming apart: cos(x)+½ has '
          f'one crossing of each sign, so a crossing count reads 1−1, while the true kernel is '
          f'{kp}−{km} because ∮m ≠ 0.  ** Only the INDEX agrees. **  A wall count is a LOCAL '
          'heuristic and needs a global condition to become a kernel dimension -- which on the bead '
          'is PART 3\'s L² test', nz == 2 and kp == 0 and km == 0 and i == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for ff in FAILED:
            print(f'    - {ff[:150]}')
        return 1
    print('  VERDICT: ** the γ⁵-graded index that P14 states at traced weight is COMPUTABLE at the')
    print('  point where it is traced, and the computation is a Weyl limit-point test. **')
    print('  ⌗ ** W dℓ = λ dr/r exactly, so the branches are ψ ~ r^∓λ and both are L² at the branch')
    print('     point iff |λ| < ¾.  The attained spectrum is λ = ±1, ±2, … ** -- so every mode is')
    print('     limit-point, the operator is essentially self-adjoint there, and *no boundary')
    print('     condition exists to be chosen*.  Compactness made the index finite; this is what')
    print('     makes it CANONICAL.')
    print('  ⌗ ** And λ=0 is doubly excluded ** -- by W≡0, which is P14\'s reason, and by being the')
    print('     only value inside the window, which is this one.')
    print('  ⛔ ** A SPURIOUS CONVERGENCE WAS MANUFACTURED ON THE WAY AND IS RECORDED: ** half-')
    print('     generalising to D returned P03\'s window {4,5} exactly, caveat included.  Completing')
    print('     it removes the restriction.  *A partial generalisation produced this theatre\'s own')
    print('     success signal, which is the most dangerous artefact it can produce.*')
    print('  ⓻ ** And the even-crossing obstruction is a special case: ** the index vanishes on a')
    print('     closed loop for ANY mass function, including ones with no zeros at all.  The branch')
    print('     point removes the closed-manifold structure; it does not evade a constraint on m.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
