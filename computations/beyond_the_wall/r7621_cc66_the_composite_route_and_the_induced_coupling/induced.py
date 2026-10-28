#!/usr/bin/env python3
"""r7621+cc66 -- B59's LAST route: does a COMPOSITE/INDUCED coupling come out a number?

Registered in PREDICTION.md in this directory before a line of this file existed.

A Sakharov-style induced coupling is 1/g^2 = c * N * log(Lambda/mu): a species count N, an
ultraviolet cutoff Lambda, an infrared scale mu.  r7619 landed Lambda = 1/beta as the scale the
construction supplies.  The order names the reachable negative as "mu is free".

** THIS FILE REGISTERS, AND THEN MEASURES, A DIFFERENT AND STRONGER NEGATIVE. **  The face is
COMPACT, so there is no infrared infinity: the Dirac spectrum is gapped at 5/2alpha, and that gap is
an infrared scale the construction fixes.  Every slot of the formula is then filled -- and the
mechanism still fails, because

    Lambda / mu  =  [1/(2 pi alpha)] / [5/(2 alpha)]  =  1/(5 pi)  <  1

so the cutoff lies BELOW the gap and NOTHING lies between them to integrate out.  A loop of a field
with no modes under the cutoff induces nothing.  Both readings are run, because only their agreement
makes the conclusion independent of the identification I am the one making.
"""
import math
import os
import re
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')
CHECKS = []


def check(name, ok, detail=''):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f'   ->  {detail}' if detail else ''), flush=True)


def head(t):
    print('\n' + '=' * 78 + f'\n {t}\n' + '=' * 78)


def reads(fn, needle):
    txt = re.sub(r'\s+', ' ', open(os.path.join(CORPUS, fn), encoding='utf-8',
                                  errors='replace').read())
    return re.sub(r'\s+', ' ', needle) in txt


# =============================================================================================
head('Ⓐ  THE THREE DATA THE FORMULA NEEDS -- WHICH OF THEM THE PAPERS SUPPLY')
# =============================================================================================
LEAST = r'the least eigenvalue is $5/2\alpha$'
PERIOD = r'a Euclidean continuation of period $\beta=2\pi\alpha$'

check(f'the face\'s spectral GAP is the paper\'s own figure -- READ: "{LEAST}"',
      reads('boundary_paper.tex', LEAST), 'found in boundary_paper.tex')
check(f'and the thermal period, from which r7619\'s Lambda is built -- READ: "{PERIOD}"',
      reads('boundary_paper.tex', PERIOD), 'found in boundary_paper.tex')

al = sp.Symbol('alpha', positive=True)
beta = 2 * sp.pi * al
LAMBDA = 1 / beta                      # r7619: the scale the construction supplies
GAP = sp.Rational(5, 2) / al           # P13: the face's least Dirac eigenvalue

print("""
  ⇒ So of the three data 1/g^2 = c N log(Lambda/mu) needs, the construction supplies Lambda
    (r7619) and -- on the reading this row argues for -- mu, because a COMPACT face has a GAP
    and a gap is an infrared scale.  ** The order expects mu to be the free one.  This file
    tests that reading too, but it tests the favourable one first. **""")


# =============================================================================================
head('Ⓑ  THE INSTRUMENT: HOW MANY FACE MODES LIE UNDER A CUTOFF -- AND IT MUST BE ABLE TO COUNT')
# =============================================================================================
def spinor_rank(n):
    """2^floor(n/2), the rank of the spinor bundle in n dimensions."""
    return 2 ** (n // 2)


def multiplicity(n, k):
    """the multiplicity of the Dirac eigenvalue +(n/2+k)/alpha on the round n-sphere."""
    return spinor_rank(n) * math.comb(k + n - 1, k)


def modes_below(cut_over_alpha, n=5, kmax=200):
    """how many Dirac modes (with multiplicity) have |lambda| <= cut/alpha on the round n-sphere.

    ⌗ The cutoff arrives as a PURE NUMBER times 1/alpha and the eigenvalues are (n/2+k)/alpha, so
    alpha cancels and nothing here depends on the face's radius having a value.  Both signs of the
    eigenvalue are counted, since a loop integrates over both.
    """
    tot = 0
    for k in range(kmax):
        if sp.Rational(n, 2) + k <= cut_over_alpha:
            tot += 2 * multiplicity(n, k)
        else:
            break
    return tot


check('the spinor rank is COMPUTED from the dimension and agrees with the Clifford construction '
      'at r7619, which found the chirality-4 by building the algebra',
      spinor_rank(5) == 4 and spinor_rank(6) == 8,
      f'rank(5) = {spinor_rank(5)}, rank(6) = {spinor_rank(6)}')
check('and the multiplicities are the ones r7615 and r7619 used, recomputed here rather than '
      'carried: 4 at the lowest level, 20 at the next',
      multiplicity(5, 0) == 4 and multiplicity(5, 1) == 20,
      f'm_0 = {multiplicity(5, 0)}, m_1 = {multiplicity(5, 1)}')

_big = modes_below(20.0)
_small = modes_below(3.0)
check('** CONTROL, AND THE GUARD r7615 COST ME: the counter CAN return non-zero, and it RISES with '
      'the cutoff -- so a zero from it later is a measurement and not an instrument that cannot '
      'count **', _big > _small > 0,
      f'cut = 3/alpha -> {_small} modes;  cut = 20/alpha -> {_big} modes')
check('CONTROL: and it returns ZERO below the gap, which is the arithmetic the whole row turns on, '
      'checked here on a cutoff chosen for the test rather than on the construction\'s',
      modes_below(2.0) == 0, f'cut = 2/alpha (below 5/2) -> {modes_below(2.0)} modes')


# =============================================================================================
head("Ⓒ  THE FAVOURABLE READING: mu = THE GAP, EVERY SLOT FILLED -- AND THE WINDOW IS INVERTED")
# =============================================================================================
ratio = sp.simplify(LAMBDA / GAP)
check('** THE WINDOW IS INVERTED, EXACTLY: Lambda/mu = 1/(5 pi), computed from the two symbolic '
      'scales and not asserted -- the construction\'s cutoff lies BELOW its own infrared scale by a '
      'factor of 5 pi **', sp.simplify(ratio - 1 / (5 * sp.pi)) == 0 and ratio < 1,
      f'Lambda/mu = {ratio} = {float(ratio):.6f}, and 5 pi = {float(5 * sp.pi):.4f}')
check('so the logarithm the induced coupling needs comes out NEGATIVE, which would make 1/g^2 '
      'negative and g^2 negative -- unphysical, and computed rather than described',
      sp.log(ratio) < 0, f'log(Lambda/mu) = {sp.simplify(sp.log(ratio))} = {float(sp.log(ratio)):.6f}')

_cut_number = sp.nsimplify(sp.simplify(LAMBDA * al))        # Lambda in units of 1/alpha
_n_under = modes_below(float(_cut_number))
check('** AND THE DECISIVE FORM, WHICH IS A COUNT AND NOT A SIGN: the number of face Dirac modes '
      "under the construction's own cutoff is ZERO.  A loop of a field with no modes below the "
      'cutoff induces NOTHING, so the mechanism does not engage on this geometry at all **',
      _n_under == 0,
      f'Lambda = {_cut_number} / alpha = {float(_cut_number):.6f} / alpha, against a least '
      f'eigenvalue of 2.5 / alpha  ->  {_n_under} modes')


# =============================================================================================
head("Ⓓ  CONTROL: A MODEL WHERE THE INDUCED COUPLING *IS* FIXED -- WHAT THE ORDER ASKS FOR BY NAME")
# =============================================================================================
# the textbook one-loop form: 1/g^2 = N/(12 pi^2) * log(Lambda/mu)
N_sym, L_sym, mu_sym = sp.symbols('N Lambda mu', positive=True)
inv_g2 = N_sym / (12 * sp.pi ** 2) * sp.log(L_sym / mu_sym)

_fixed = inv_g2.subs({N_sym: 4, L_sym: 100, mu_sym: 1})
_fixed2 = inv_g2.subs({N_sym: 4, L_sym: 1000, mu_sym: 1})
# ⌗ The mode count stays OUT of this check's name and is carried by the measured detail instead.
#   My first version of this line asserted "with 1255 modes under that cutoff" -- a figure I wrote
#   from nothing; the counter returns 666,333,360.  The assertion was sound and the PROSE was false
#   by five orders of magnitude, which is the stale-figure fault 69 corrected at r7613 and again on
#   r7615's check count.  A name may describe what is measured; it may not quote a number the run
#   has not produced.
check('CONTROL: with a window the right way up the coupling IS a number -- N = 4, Lambda/mu = 100 '
      'gives a positive 1/g^2 with a large population under the cutoff, so the formula and the '
      'counter both engage', float(_fixed) > 0 and modes_below(100.0) > 1000,
      f'1/g^2 = {float(_fixed):.6f} > 0, modes under 100/alpha = {modes_below(100.0)}')
check('** and it MOVES with the cutoff, so the coefficient is genuinely a function of the data and '
      '"no window, no coupling" is a measurement rather than a form of words **',
      float(_fixed2) > float(_fixed),
      f'Lambda/mu = 100 -> {float(_fixed):.6f};  Lambda/mu = 1000 -> {float(_fixed2):.6f}')
check("CONTROL: and the same expression on the construction's OWN ratio returns NEGATIVE, so the "
      'two cases are distinguished by the instrument and not by my description of them',
      float(inv_g2.subs({N_sym: 4, L_sym: 1, mu_sym: 5 * sp.pi})) < 0,
      f"on Lambda/mu = 1/(5 pi): 1/g^2 = "
      f"{float(inv_g2.subs({N_sym: 4, L_sym: 1, mu_sym: 5 * sp.pi})):.6f}")


# =============================================================================================
head("Ⓔ  THE ORDER'S OWN READING, RUN SO THE VERDICT DOES NOT REST ON MY IDENTIFICATION")
# =============================================================================================
d_inv_g2 = sp.simplify(sp.diff(inv_g2, mu_sym))
check("** ON THE ORDER'S READING -- mu FREE, the scale at which the coupling is quoted -- the "
      'answer is also no, and for the reason the order gives: 1/g^2 depends on mu, its derivative '
      'being non-zero everywhere, so a free mu is a free coupling **',
      d_inv_g2 != 0 and sp.simplify(d_inv_g2 + N_sym / (12 * sp.pi ** 2 * mu_sym)) == 0,
      f'd(1/g^2)/d(mu) = {d_inv_g2}, non-zero for all mu > 0')
check('⇒ so BOTH readings give no fixed coupling, by DIFFERENT mechanisms -- the order\'s because '
      'mu is free, mine because with mu fixed by the gap there is no window and nothing under the '
      'cutoff.  The conclusion does not depend on which reading is right',
      _n_under == 0 and d_inv_g2 != 0, 'mu free -> free coupling; mu = gap -> zero modes')


# =============================================================================================
head('Ⓕ  WHAT THE CONSTRUCTION DOES FIX, SO THE NEGATIVE IS NOT OVERSTATED')
# =============================================================================================
check('the SPECIES COUNT is not the missing datum: the face\'s spinor bundle has rank 4, a discrete '
      'fact of dimension five and not a choice, and the lowest level carries 4 states -- so N is '
      'available even though the window is not',
      spinor_rank(5) == 4 and multiplicity(5, 0) == 4,
      f'N = {spinor_rank(5)} from the rank, {multiplicity(5, 0)} states at the lowest level')


# =============================================================================================
head('Ⓖ  THE VERDICT -- INSIDE THE ASSERT, WHERE IT CAN FAIL')
# =============================================================================================
check('** ⑴ THE INDUCED-COUPLING ROUTE DOES NOT ENGAGE ON THIS FACE, AND THE REASON IS NOT THE ONE '
      "THE ORDER NAMED: the species count IS fixed (4) and the infrared scale IS fixed (the gap, "
      '5/2alpha), so the missing datum is neither -- it is that the cutoff the construction '
      'supplies lies BELOW the gap, Lambda/mu = 1/(5 pi), leaving ZERO modes to integrate out **',
      _n_under == 0 and ratio < 1 and spinor_rank(5) == 4,
      f'N = 4 fixed, mu = 5/2alpha fixed, Lambda/mu = 1/(5 pi) < 1, modes under cutoff = {_n_under}')
check("** ⑵ AND IT FAILS ON THE ORDER'S READING TOO, so the answer is robust to the one "
      'identification this row makes: with mu free the coupling is free, which is the negative the '
      'order named.  Pre-registered outcome 2, reached by BOTH routes, and whether "no modes under '
      'the cutoff" CLOSES the route or merely fails to engage it here is 69\'s to rule on **',
      d_inv_g2 != 0 and _n_under == 0,
      'outcome 2 on both readings; the close-or-not-engage distinction is routed, not collapsed')

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print('\n' + '=' * 78 + '\n ' + ('ALL CHECKS PASS' if not bad else 'FAILURES ABOVE') + '\n' + '=' * 78)
assert not bad, f'{len(bad)} check(s) failed: {bad}'
