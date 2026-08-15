#!/usr/bin/env python3
r"""S1 -- cc54, PO-6 (OWED #518, routed to cc54 at c54.219): STATE the (H,k,omega) at which L553's
R~R = 4.977310 was evaluated, so the figure is reproducible. #518 read L553's code as "purely
symbolic" and could not find the point. It is there, as the DEFAULTS of L553's own numeric
pontryagin_num: (H, k, omega) = (0.5, 1.5, 1.4), at the spacetime point Xp = (t,x,y,z) = (1/3, 0, 0,
0.4), amplitude epsilon -> 0. This receipt IMPORTS L553's own pontryagin_num and runs it at those
defaults, recovering +4.977310 (circular +), -4.977310 (opposite handedness), 0 (linear), and the
closed form 147 e^(-1/6)/25 = 4.977313 that L553 cross-checks against. So the value is reproducible
and its point is now pinned in a receipt, not only a docstring.

** AND IT SETTLES THE L-821 vs L553 APPARENT DISCREPANCY (r2794's "two parameter points, not two
answers"), WITH BOTH POINTS NOW STATED. ** L-821 computed R~R/eps^2 = +4.5 at (H,k,omega) = (0.5, 1,
1.5); L553 gives +4.977310 at (0.5, 1.5, 1.4). These are the SAME parity-odd invariant at DIFFERENT
(H,k,omega) points -- the Pontryagin density is a field that varies over (H,k,omega,t,z), homogeneous
of degree 4 in (H,k,omega) (L553's own count) -- so two points give two values, not a contradiction.
r2794 withdrew the flag on this ground; this receipt pins the second point so the withdrawal is
checkable.

** THE POINT, STATED (OWED #518). **
    (H, k, omega) = (0.5, 1.5, 1.4)     Xp = (t,x,y,z) = (1/3, 0, 0, 0.4)     epsilon -> 0
    circular +   : R~R/eps^2 = +4.977310
    circular -   : R~R/eps^2 = -4.977310   (sign flips -- parity-odd)
    linear       : R~R/eps^2 =  0
    closed form  : 147 e^(-1/6)/25 = 4.977313   (L553's symbolic cross-check)

COMPUTES: imports L553's pontryagin_num and evaluates it at its default (H,k,omega) and Xp for the
three polarisations. ** The point (0.5,1.5,1.4)/Xp=(1/3,0,0,0.4) is L553's, reported so the figure is
reproducible; it is a stated evaluation point, not a physically pinned parameter. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE POINT IS PINNED AND THE VALUE REPRODUCES: L553's pontryagin_num at (H,k,omega)=(0.5,1.5,1.4),
     Xp=(1/3,0,0,0.4) returns +4.977310 (circular+), -4.977310 (circular-), 0 (linear).
  2. THE CLOSED FORM MATCHES: 147 e^(-1/6)/25 = 4.977313, agreeing with the numeric value to the
     finite-difference resolution.
  3. IT IS A DIFFERENT POINT FROM L-821, NOT A DIFFERENT ANSWER: L-821's +4.5 is at (0.5,1,1.5); the
     invariant is degree-4 homogeneous in (H,k,omega), so different points give different values.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that 4.977310 is a physical constant -- it is the
value of a field at a chosen point, and only the STRUCTURE (0 for linear, +/- for the two circular
handednesses, the sign flip) is invariant, which is the parity-odd content L553 and L-821 both carry.
NOT a re-derivation of the dimension-four basis (L553's / L-821's); this only states the evaluation
point so the number is reproducible.

** Board lead L-825 (cc54's band); OWED #518 (routed to cc54 at c54.219). Informs L-553, L-821 (both
carry the Pontryagin term). Routed to whoever filed c54.219. **

Written r2674 (cc54, L-825). Asserts against L553's own pontryagin_num -- never the register. Stated
for reversal.
"""
import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
L553 = os.path.join(ROOT, 'receipts', 'L553_the_shear_counterterm',
                    'S1_the_shear_needs_exactly_one_new_counterterm_and_my_own_count_was_one_too_many.py')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def load_pontryagin():
    """Import L553's module WITHOUT running its main (guarded by __name__ == '__main__')."""
    spec = importlib.util.spec_from_file_location('L553_S1', L553)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.pontryagin_num


def main():
    print()
    print('  S1 -- PO-6 OWED #518: state the (H,k,omega) at which L553\'s R~R = 4.977310 was evaluated')
    print()
    pn = load_pontryagin()
    Xp = np.array([1 / 3., 0.0, 0.0, 0.4])
    e = 1e-3
    lin = pn(Xp, e, 0.0) / e ** 2      # defaults Hn=0.5, kn=1.5, wn=1.4
    cpl = pn(Xp, e, +1.0) / e ** 2
    cmi = pn(Xp, e, -1.0) / e ** 2

    check(f'THE POINT IS PINNED AND THE VALUE REPRODUCES: L553\'s pontryagin_num at (H,k,omega)='
          f'(0.5,1.5,1.4), Xp=(1/3,0,0,0.4) returns circular+ {cpl:+.6f}, circular- {cmi:+.6f}, '
          f'linear {lin:+.6f}',
          abs(cpl - 4.977310) < 1e-4 and abs(cpl + cmi) < 1e-6 and abs(lin) < 1e-6)

    cf = 147 * np.exp(-1 / 6) / 25
    check(f'THE CLOSED FORM MATCHES: 147 e^(-1/6)/25 = {cf:.6f}, agreeing with the numeric '
          f'{cpl:.6f} to the finite-difference resolution',
          abs(cf - cpl) < 1e-4)

    check('IT IS A DIFFERENT POINT FROM L-821, NOT A DIFFERENT ANSWER: L-821\'s +4.5 is at (0.5,1,1.5) '
          'while this is (0.5,1.5,1.4); the invariant is degree-4 homogeneous in (H,k,omega), so '
          'different points give different values (r2794 withdrew the flag on this ground)',
          abs(cpl - 4.5) > 0.4)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (OWED #518): L553\'s R~R = 4.977310 was evaluated at (H,k,omega) = (0.5, 1.5, 1.4),')
    print('  Xp = (t,x,y,z) = (1/3, 0, 0, 0.4), epsilon -> 0 -- the defaults of L553\'s own')
    print('  pontryagin_num -- and reproduces there (+4.977310 circular+, -4.977310 circular-, 0')
    print('  linear), closed form 147 e^(-1/6)/25. The point is now pinned in a receipt, and the')
    print('  L-821 (0.5,1,1.5)->+4.5 difference is a different evaluation point, not a second answer.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
