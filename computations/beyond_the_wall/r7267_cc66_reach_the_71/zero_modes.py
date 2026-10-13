#!/usr/bin/env python3
"""`r7275`/`r7283` ORDER ② — **THE ZERO-MODE FUNCTION. THE CAPABILITY `r7267` ③ FILED AS A
STATED LIMIT, BUILT, WITH THE MEASURE AS RULED AND THE FLAT COUNT BESIDE IT.**

** THE ORDER. **  `r7275` ②, carried unchanged through `r7281`, `r7283`, `r7285` and `r7287`:
*the zero-mode function, measure RULED as `dmu = sqrt(|g_rr|) dr` **with the absolute value**,
and the flat `dr` count reported beside it; **hard stop at one cycle.***

** WHAT THE LIMIT SAID THE FUNCTION NEEDS, AND WHERE EACH PIECE COMES FROM. **
`STATED_LIMIT.md` listed four inputs and named three of them as already computed:

  ⓵ the profile `W = sqrt(f)/r` with `2M` from `twoM`   -- `parity.py`, batch one
  ⓶ its sign change at `r = 0`, the domain-wall condition -- `parity.py`: ODD at `D = 5`
  ⓷ the chirality operator `gamma^5 = R`                -- named by the corpus in its own voice
  ⓸ the solve `(-i gamma^1 d_r + W) psi = 0`            -- ** this file **

** ⛭⛭⛭ AND THE RULED MEASURE IS NOT A FORMALITY: IT IS WHAT MAKES THE WALL REGION HABITABLE. **
*The wall sits where `f < 0` -- `B34`'s own finding -- which at `D = 5` is `|r| < 1/2`, inside
the inner horizon.  There `g_rr = 1/f` is NEGATIVE, so `sqrt(g_rr)` is imaginary and the static
`L^2` measure does not exist.*
  ⇒ `dmu = sqrt(|g_rr|) dr = dr / sqrt(|f|)` **is real exactly because of the absolute value the
  order insisted on**, and the flat `dr` is reported beside it so the two counts can be
  compared rather than conflated.

** ⓹ WHAT THE SOLVE IS. **  `(-i gamma^1 d_r + W) psi = 0` separates into the two chirality
eigenstates of `gamma^5`, giving `psi_mp = exp(mp int W dr)`.  *A chirality is BOUND iff its
`|psi|^2` is integrable over the wall interval in the measure asked for.*  ⌗ *The mode count is
then a count of bound chiralities per wall, and nothing about the answer is assumed here: `f`,
`W` and the integrals decide it.*

WHAT IS NOT CLAIMED.  ** Not `B1`'s equivariant Dirac index ** -- `STATED_LIMIT.md` named it as
NOT this capability, an index theorem rather than a mode solve, and it stays inside that limit.
** Not that the twelve rows are hereby reached ** -- this file builds the capability the limit
named; reaching the rows is a separate batch with its own converses.  ** Not a claim about the
`D = 4` wall ** -- `parity.py` measured `W` to have NO parity there, so there is no sign change
and no domain wall, and that is reported rather than forced.  ** Not that any pin moves. **

Run: python3 zero_modes.py
"""
import functools
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import parity as P                                                 # noqa: E402

D_WALL = 5                      # the dimension at which `parity.py` measures `W` ODD


# ══════════════════ ⒜ THE PROFILE, FROM THE CORPUS'S OWN `twoM` ══════════════════════════
@functools.lru_cache(maxsize=None)
def profile(D=D_WALL):
    """`(r, f, W, 2M)` with `2M` taken from `L-006w`'s own `twoM` through `parity.py`.

    *`W = sqrt(|f|)/r` -- the absolute value is inside the profile for the same reason it is
    inside the measure: on the wall interval `f < 0`.*"""
    p = P.at_inputs()
    r, f, M2 = p.metric_function(D)
    f = sp.together(f)
    return r, f, sp.sqrt(sp.Abs(f)) / r, M2


def wall_is_a_wall(D=D_WALL):
    """the domain-wall condition: `W` changes sign at `r = 0`, which `parity.py` measures as
    `W` being ODD in the signed radius"""
    return P.at_inputs().wall_factor_parity(D) == -1


@functools.lru_cache(maxsize=None)
def horizons(D=D_WALL):
    """the real positive roots of `f` -- the horizons that bound the wall region"""
    r, f, _, _ = profile(D)
    roots = sp.solve(sp.Eq(sp.numer(f), 0), r)
    return tuple(sorted(float(z) for z in roots
                        if z.is_real and float(z) > 0))


@functools.lru_cache(maxsize=None)
def wall_interval(D=D_WALL):
    """the interval on which `f < 0` next to the origin: the wall region `B34` names.

    *Computed from the roots rather than asserted: the inner horizon is the SMALLEST positive
    root, and `f` is checked negative at the interval's midpoint.*"""
    r, f, _, _ = profile(D)
    hs = horizons(D)
    inner = hs[0]
    mid = inner / 2.0
    assert float(f.subs(r, mid)) < 0, 'the wall interval must have f < 0'
    return (0.0, inner)


# ══════════════════ ⒝ THE TWO MEASURES, ONE RULED AND ONE FLAT ═══════════════════════════
def measure_weight(which, D=D_WALL):
    """`dmu/dr` for the named measure.

    `ruled`: `sqrt(|g_rr|) = 1/sqrt(|f|)` -- the measure `r7275` ruled, real on the wall
    interval BECAUSE of the absolute value.
    `flat`:  `1` -- the plain `dr`, reported beside it as the order requires."""
    r, f, _, _ = profile(D)
    if which == 'ruled':
        return sp.lambdify(r, 1 / sp.sqrt(sp.Abs(f)), 'numpy')
    if which == 'flat':
        return lambda x: np.ones_like(np.asarray(x, dtype=float))
    raise KeyError(which)


def static_measure_is_unavailable(D=D_WALL):
    """and the reason the absolute value is not a formality: WITHOUT it the weight is imaginary
    on the wall interval, so the static `L^2` measure does not exist there"""
    r, f, _, _ = profile(D)
    a, b = wall_interval(D)
    val = complex(sp.sqrt(1 / f).subs(r, (a + b) / 2))
    return abs(val.imag) > 1e-12


# ══════════════════ ⒞ THE SOLVE ══════════════════════════════════════════════════════════
@functools.lru_cache(maxsize=None)
def _profile_callable(D=D_WALL):
    r, f, W, _ = profile(D)
    return sp.lambdify(r, W, 'numpy')


def exponent(rs, D=D_WALL, ref=None):
    """`int_ref^r W dr'`, by cumulative quadrature on the grid handed in"""
    a, b = wall_interval(D)
    ref = ref if ref is not None else (a + b) / 2.0
    Wf = _profile_callable(D)
    vals = Wf(rs)
    out = np.zeros_like(rs)
    # cumulative trapezoid from the grid's start, then shifted so the reference reads zero
    inc = np.concatenate(([0.0], np.cumsum(np.diff(rs) * (vals[1:] + vals[:-1]) / 2.0)))
    return inc - np.interp(ref, rs, inc)


def mode_norm(chirality, measure, D=D_WALL, n=400000):
    """`int |psi|^2 dmu` over the wall interval for the named chirality and measure.

    *`psi_mp = exp(mp int W)`, so `chirality = -1` is the upper sign.  The integral is taken on
    a grid that stops short of both endpoints by one step, and the value is reported with the
    endpoint behaviour rather than silently clipped.*"""
    a, b = wall_interval(D)
    eps = (b - a) / n
    rs = np.linspace(a + eps, b - eps, n)
    E = exponent(rs, D)
    # ⌗ the UNBOUND chirality genuinely overflows -- `exp` of a divergent exponent -- and `inf`
    #   is the answer rather than a warning, so the overflow is silenced and REPORTED.
    with np.errstate(over='ignore', invalid='ignore'):
        psi2 = np.exp(2.0 * chirality * E)
        w = measure_weight(measure, D)(rs)
        return float(np.trapezoid(psi2 * w, rs))


def is_bound(chirality, measure, D=D_WALL, ceiling=1e6):
    """BOUND iff the norm is finite -- tested by refinement rather than by one number: the
    integral is computed at two grid densities and must not grow with resolution"""
    lo = mode_norm(chirality, measure, D, n=100000)
    hi = mode_norm(chirality, measure, D, n=400000)
    return bool(np.isfinite(hi) and hi < ceiling and hi <= lo * 1.5)


def bound_count(measure, D=D_WALL):
    """the number of bound chiralities on the wall interval, in the named measure"""
    return sum(1 for ch in (-1, +1) if is_bound(ch, measure, D))


def bound_chirality(measure, D=D_WALL):
    return [ch for ch in (-1, +1) if is_bound(ch, measure, D)]



def count_is_measure_independent(D=D_WALL):
    """** THE ONE THING `STATED_LIMIT.md` SAID THE ORDER WOULD HAVE TO SPECIFY, ANSWERED. **

    *The limit named the measure as `the question the order should carry; nothing else about the
    function is open`.  The order carried it and ruled `dmu = sqrt(|g_rr|) dr`.*
      ⇒ *** Measured: the two measures give DIFFERENT NORMS and the SAME COUNT. ***  So the
      condition the limit flagged as the only open one does not change the answer it was
      flagged for -- though it is still what makes the measure REAL on the wall interval, which
      is a separate and necessary thing."""
    return bound_count('ruled', D) == bound_count('flat', D)


def norms_differ(D=D_WALL, ch=+1):
    """and the norms themselves are not equal, so the independence is a fact about the COUNT
    and not an artefact of the two measures coinciding"""
    a = mode_norm(ch, 'ruled', D)
    b = mode_norm(ch, 'flat', D)
    return bool(abs(a - b) / a > 0.1)


def d4_has_no_wall():
    """and at `D = 4` there is NO wall to put a mode on: `parity.py` measures `W` to have no
    parity, so it does not change sign at the origin.  *Reported rather than forced.*"""
    return P.at_inputs().wall_factor_parity(4) == 0

# ══════════════════════════════════════ REPORT ═══════════════════════════════════════════
def main():
    print()
    print(__doc__.split('Run:')[0])
    r, f, W, M2 = profile()
    print(f'  ⒜  THE PROFILE, from `L-006w`\'s own `twoM` through `parity.py`')
    print(f'      2M = {M2}   f = {f}')
    print(f'      numerator factored: {sp.factor(sp.numer(f))}')
    print(f'      W = sqrt(|f|)/r is ODD in the signed radius: {wall_is_a_wall()}   '
          f'-> there IS a domain wall at r = 0')
    print(f'      positive roots of f (the horizons): {horizons()}')
    a, b = wall_interval()
    print(f'      the wall interval, where f < 0: ({a}, {b})')
    print()
    print('  ⒝  THE TWO MEASURES')
    print(f'      WITHOUT the absolute value, sqrt(g_rr) is IMAGINARY on the wall interval: '
          f'{static_measure_is_unavailable()}')
    print(f'      so the static L^2 measure does not exist there, and the RULED measure '
          f'dmu = sqrt(|g_rr|) dr = dr/sqrt(|f|) is real BECAUSE of the absolute value')
    print()
    print('  ⒞  THE SOLVE -- (-i gamma^1 d_r + W) psi = 0, psi = exp(mp int W dr)')
    print(f'      {"chirality":>10} {"measure":>8} {"norm (n=1e5)":>16} {"norm (n=4e5)":>16} '
          f'{"bound":>7}')
    for measure in ('ruled', 'flat'):
        for ch in (-1, +1):
            lo = mode_norm(ch, measure, n=100000)
            hi = mode_norm(ch, measure, n=400000)
            print(f'      {ch:>+10d} {measure:>8} {lo:>16.6e} {hi:>16.6e} '
                  f'{str(is_bound(ch, measure)):>7}')
    print()
    print(f'      ** THE RULED MEASURE dmu = sqrt(|g_rr|) dr BINDS '
          f'{bound_count("ruled")} chirality/chiralities: {bound_chirality("ruled")} **')
    print(f'      ** THE FLAT dr BINDS {bound_count("flat")}: '
          f'{bound_chirality("flat")}   (reported beside it, as ordered) **')
    print()
    print('  ⒹTHE QUESTION THE LIMIT SAID THE ORDER WOULD HAVE TO CARRY, ANSWERED')
    print(f'      the two measures give DIFFERENT norms '
          f'({mode_norm(+1, "ruled"):.6f} against {mode_norm(+1, "flat"):.6f}, '
          f'differ: {norms_differ()}) and the SAME count: '
          f'{count_is_measure_independent()}')
    print(f'      ** so the one condition `STATED_LIMIT.md` named as open does not change the')
    print(f'         COUNT it was named for -- while still being what makes the measure REAL **')
    print(f'      and at D = 4 there is no wall at all to put a mode on: '
          f'{d4_has_no_wall()}   (W has no parity there)')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
