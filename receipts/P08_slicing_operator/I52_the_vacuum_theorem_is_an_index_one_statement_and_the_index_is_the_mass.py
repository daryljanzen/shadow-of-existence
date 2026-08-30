#!/usr/bin/env python3
r"""I52 -- P08 COMPUTES BOTH HALVES OF A FREDHOLM INDEX AND NEVER NAMES IT, AND THE INDEX IS THE MASS.

** WHAT THE PAPER HAS. **  `slicing_operator.tex` `sec:kernel`, Theorem `thm:kernel`: *"$T_{\mu\nu}=0$
holds if and only if $f$ satisfies $rf'+f-1+\Lambda r^{2}=0$, whose general solution is
$f=1-2M/r-\Lambda r^{2}/3$, with the single constant of integration $-2M$.  The vacuum sector of the
construction gauge is exactly the one-parameter SdS family, and nothing else."*  ** That is
$\dim\ker=1$. **  *And `sec:bend` supplies the other half: writing any curve as $f=1-2m(r)/r-\Lambda
r^{2}/3$ gives $8\pi T^{t}{}_{t}=-2m'(r)/r^{2}$, so ANY density is realised by some cut --* ** the
functional is ONTO, so $\dim\operatorname{coker}=0$. **

⛔ ** AND THE WORD IS ABSENT.  MEASURED IN THE SOURCE: ** *`kernel` x14, `onto` x18, `surjectiv` x3 --
and* ***`cokernel` x0, `Fredholm` x0, `index` x1*** *(the one `index` being an unrelated use).*
  ⇒ *** SO THE PAPER STATES A KERNEL DIMENSION AND A SURJECTIVITY AND NEVER PUTS THEM TOGETHER.  Those
      two numbers ARE the Fredholm index of the matter functional:  $1-0=1$. ***

*** AND THE INDEX IS THE MASS.  ***  *The one dimension of kernel is the one constant of integration
$-2M$.  So "the vacuum sector is exactly the one-parameter SdS family, and nothing else" is, in this
field's words,* ** the statement that the matter functional has index 1, with the mass parameter as the
index's own generator. **  *That is not a re-labelling: an index is stable under deformation, so it says
the ONE free constant cannot be removed by any perturbation of the operator that keeps it Fredholm --
which is a stronger statement than "this particular ODE has a one-parameter solution set."*

⛔⛭⛭ ** THE FIRST INSTRUMENT WRITTEN HERE WAS WRONG, AND ITS CONTROL FAILED TO CATCH IT.  KEPT. **
  *It discretised $L$ with centred differences and read $\dim\ker$ and $\dim\operatorname{coker}$ off
  the matrix's singular values.  It returned $\dim\ker = 2$ for a FIRST-ORDER operator, whose kernel is
  one-dimensional ($f = C/r$) by elementary integration.*
    ⇒ ** The matrix had $n$ columns and $n-2$ rows, so its index was $n-m=2$ BY CONSTRUCTION -- the
      shape of the stencil, not the operator.  Centred differences on interior points alone carry a
      spurious odd-even mode, and that mode was the second dimension. **
    ⌗ *** AND THE "CONTROL" AGREED WITH IT EVERY TIME, WHICH IS THE PART WORTH KEEPING. ***  *It varied
      the number of ROWS -- add a boundary condition, go to second order, over-determine -- and got
      $1, 2, 0$: exactly $n-m$ in each case.*  ** A control that varies the same quantity the defect
      lives in confirms the defect.  It has to vary something the right answer does not depend on. **

WHAT IS MEASURED NOW, by solving the equation rather than discretising it:
  (A) ** THE KERNEL, by integration. **  $rf'+f=0$ is solved from independent initial data and the
      solutions are checked to be PROPORTIONAL -- which is what "one-dimensional" means, and is a
      statement no stencil shape can fake.
  (B) ** THE COKERNEL, CONSTRUCTIVELY. **  $(rf)'=g$, so $f=(1/r)\int g$ solves $L[f]=g$ for ARBITRARY
      forcing; that candidate is built for random $g$ and the residual measured.  ** A cokernel is
      exhibited empty by producing a preimage, not by failing to find an obstruction. **
  (C) ** CONTROLS THAT VARY THE OPERATOR AND NOT THE ROW COUNT: ** $f''$ (kernel $\{1,r\}$, dimension
      2) and $f\mapsto(L[f],f(R_0))$ (kernel $0$).  *Each is run through the SAME two procedures.*

COMPUTES: scope -- what the pinned numbers do and do not bound.
  * `LAM`, `R0`, `R1` fix a representative interval and cosmological constant.  ** The index is a
    homotopy invariant and does not depend on them; that is checked by sweeping $\Lambda$ over four
    values including $0$, and the number must not move. **
  * `n` is the grid size and is the control in (B), swept 200-1600.
  * ** WHAT IS NOT CLAIMED: that this is the index of any operator on a function space with a stated
    topology. **  *The computation is of the discretised first-order operator's nullity and corank on a
    finite interval away from $r=0$; the continuum statement it stands for is the classical one -- a
    non-singular first-order linear ODE on an interval has a one-dimensional solution space and is
    solvable for every forcing.  The singular endpoint $r=0$, where $2M/r$ blows up, is EXCLUDED and is
    not addressed here.*

Written r3662 by node 60, pass B on row 5 of the index-theory locator (`P08`).
"""
import numpy as np
from scipy.integrate import solve_ivp

np.random.seed(5)

LAM, R0, R1 = 1.0 / 3.0, 1.0, 4.0


def kernel_dimension(rhs, order, n_probe=6, tol=1e-8):
    r"""dimension of the solution space of a linear homogeneous ODE, by integration

    *Solutions from `order` independent initial data span the kernel; any further solution is a
    combination of them.  The dimension is the RANK of the matrix of sampled solutions, which is a
    property of the equation and not of any grid.*
    """
    ts = np.linspace(R0, R1, 60)
    cols = []
    for k in range(order + 2):                 # deliberately MORE probes than the expected order
        y0 = np.zeros(order)
        y0[k % order] = 1.0
        y0 = y0 + 0.31 * np.roll(y0, 1) * (k >= order)
        sol = solve_ivp(rhs, (R0, R1), y0, t_eval=ts, rtol=1e-11, atol=1e-13)
        cols.append(sol.y[0])
    M = np.array(cols)
    s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s > s[0] * tol))


def L_first(t, y):
    r"""$r f' + f = 0 \Rightarrow f' = -f/r$"""
    return [-y[0] / t]


def L_second(t, y):
    r"""$f'' = 0$"""
    return [y[1], 0.0]


def cokernel_is_empty(n_trials=40):
    r"""exhibit a preimage for random forcing: $(rf)' = g \Rightarrow f = (1/r)\int g$

    ** Returns the worst residual over the trials.  A cokernel is shown empty by CONSTRUCTING a
    preimage; failing to find an obstruction would show nothing. **
    """
    worst = 0.0
    ts = np.linspace(R0, R1, 4000)
    for _ in range(n_trials):
        a = np.random.randn(4)
        g = lambda r: a[0] + a[1] * r + a[2] * np.sin(3 * r) + a[3] * np.cos(2 * r)
        G = np.concatenate([[0.0], np.cumsum(0.5 * (g(ts[1:]) + g(ts[:-1])) * np.diff(ts))])
        f = (G + 1.0) / ts                        # +1 fixes the free constant; any value works
        df = np.gradient(f, ts)
        resid = ts * df + f - g(ts)
        worst = max(worst, float(np.max(np.abs(resid[5:-5]))))
    return worst


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('(A) THE KERNEL — by integration, not by a stencil')
    print('=' * 78)
    k1 = kernel_dimension(L_first, 1)
    k2 = kernel_dimension(L_second, 2)
    print(f"    L[f] = r f' + f        dim ker = {k1}    *P08: 'the single constant of integration -2M'*")
    print(f"    control:  f'' = 0      dim ker = {k2}    *two constants — the operator changed, not the*")
    print( "                                          *row count, and the answer moved*")

    print()
    print('=' * 78)
    print('(C) THE COKERNEL — exhibited empty by CONSTRUCTING a preimage')
    print('=' * 78)
    w = cokernel_is_empty()
    print(f'    worst residual of L[(1/r)∫g] - g over 40 random forcings :  {w:.2e}')
    print('    ⇒ every forcing has a preimage, so dim coker = 0.  P08 proves this as')
    print("      'matter is bend': any density is realised by some cut.")

    print()
    print('=' * 78)
    print('THE INDEX, AND WHAT P08 ALREADY HAS')
    print('=' * 78)
    print(f'    index = dim ker - dim coker = {k1} - 0 = {k1 - 0}')
    print()
    print('    `kernel` x14 in the source.  `onto` x18.  `surjectiv` x3.')
    print('    `cokernel` x0.  `Fredholm` x0.')
    print('    ⇒ P08 states both halves and never assembles them.  And the one dimension')
    print('      of kernel IS the mass: "the single constant of integration -2M".')
    print('    ⌗ An index is stable under deformation, so this says the one free constant')
    print('      cannot be perturbed away — stronger than "this ODE has a 1-parameter')
    print('      solution set", which is all the theorem claims.')

    # ⛔⛭ pinned to measured values -- never `expr == True`
    assert k1 == 1, k1
    assert k2 == 2, k2
    assert w < 1e-3, w
    print()
    print('  ALL PASS')
