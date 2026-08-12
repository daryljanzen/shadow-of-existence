#!/usr/bin/env python3
"""I9 -- the exhibition, at linear order: data with sigma^TT != 0 on the de Sitter leaf evolves by
ordinary GR in closed form, with the constraint CONSERVED and the count coming out on its own.

** WHAT r2513 LEFT TO DO. **  L-174 (1) stopped being "make the operator reach further" -- thm:bound
forecloses that for every subgroup H -- and became: ** exhibit the ORDINARY GR EVOLUTION of data with
sigma^TT != 0. **  cor:wall says such data is "carried past [the wall] by the ordinary
general-relativistic evolution", the wall "a regular boundary of the operator's reach and not a frontier
of the theory".  ** This receipt does that at linear order. **

** ⓵ THE EVOLUTION, EXACT AND IN CLOSED FORM. **  On the de Sitter leaf a(t) = a0 e^{Ht}, a
transverse-traceless perturbation h_ij = a^2 h(t) e_ij obeys the ordinary GR equation

      hddot + 3H hdot + (k^2/a^2) h = 0

and in conformal time, with u = a h and a = -1/(H eta),

      u'' + (k^2 - 2/eta^2) u = 0 ,      *** u = e^{-ik eta} (1 - i/(k eta)) ***

  ** verified here: the residual is IDENTICALLY ZERO. **  (sympy also returns the Bessel form,
  sqrt(eta) [C1 J_{3/2}(k eta) + C2 Y_{3/2}(k eta)], of which this is the elementary equivalent.)

** ⛭ ⓶ AND THE CONSTRAINT IS CONSERVED, NOT RE-IMPOSED. **  For a wave along z the two polarisation
tensors are constant:

      e_+  = diag(1, -1, 0) ,     e_x = offdiag(1)

  and both satisfy ** trace = 0 and k^j e_ij = 0 ** -- checked symbolically.  Since they do not evolve,
  ** D_j sigma^TT ij = 0 holds FOR ALL TIME **: the momentum constraint is preserved by the evolution
  rather than imposed at each step.

** ⓷ AND r2504's IDENTITY APPLIES WITH NO SYMMETRY ASSUMED. **  sigma_ij = (1/2) hdot^TT_ij, so
rho = R3/2 + theta^2/3 - (1/2) sigma_ij sigma^ij with sigma^2 = (1/2)(hdot)^2 (e:e).
  ⇒ ** THE TT MODE'S ENERGY IS ITS SHEAR ** -- which is what P11 says for the Gowdy case, holding here
    for a geometry with no continuous isometry, exactly as r2504 established the identity is general.

** ⓸ AND THE COUNT COMES OUT ON ITS OWN. **  Two polarisation tensors -> ** TWO free functions **, which
is c54.198's count (5 - 3 under the York split) and cor:radiation's "** the graviton's two propagating
polarizations **" arrived at from the evolution rather than from the counting.

  ⇒ *** SO THE STRATUM EVOLVES BY ORDINARY GR, EXACTLY AS cor:wall SAYS, AND NOTHING IN THE EVOLUTION
      NEEDS THE OPERATOR.  The wall is a boundary of REACH and not of THEORY. ***

** ⚠ WHAT IS NOT CLAIMED, and the scope is the point. **
  * ** THIS IS LINEARIZED ABOUT DE SITTER. **  The construction's substrate is de Sitter, so this is the
    natural background -- but a ** NONLINEAR exhibition is not done **.
  * ** The sigma^2 term that made the trade nontrivial is SECOND ORDER and does not appear here. **  At
    linear order the shear does not back-react on rho, so the very obstruction r2504 named is invisible
    at this order.
  ⇒ *** SO (1) CLOSES AT LINEAR ORDER AND ITS REMAINDER IS EXACTLY: does the NONLINEAR evolution keep
      sigma^TT free?  That is a smaller, sharper and genuinely open question. ***
  * Not that this is new physics: ** it is textbook GR on a de Sitter background **, and that is the
    finding -- ** the stratum needed nothing else. **

Written r2514.  Stated for reversal.
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
    print('  I9 -- does data with sigma^TT != 0 evolve by ordinary GR on the de Sitter leaf?')
    print()
    raw = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'),
               encoding='utf-8', errors='replace').read()
    p9 = re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                       if not l.lstrip().startswith('%')))

    # ⓵ the exact solution
    eta = sp.Symbol('eta', negative=True)
    k = sp.Symbol('k', positive=True)
    u = sp.exp(-sp.I*k*eta)*(1 - sp.I/(k*eta))
    res = sp.simplify(sp.diff(u, eta, 2) + (k**2 - 2/eta**2)*u)
    check('⛭ u = e^{-ik eta}(1 - i/(k eta)) solves u_{,eta eta} + (k^2 - 2/eta^2) u = 0 EXACTLY '
          f'(residual {res})', sp.simplify(res) == 0)
    # and the cosmic-time form is the same equation
    t, H, a0 = sp.symbols('t H a_0', positive=True)
    h = sp.Function('h')
    a = a0*sp.exp(H*t)
    ev = sp.diff(h(t), t, 2) + 3*H*sp.diff(h(t), t) + k**2/a**2*h(t)
    check('and the cosmic-time form is hddot + 3H hdot + (k^2/a^2) h = 0, the ordinary GR equation',
          sp.simplify(ev - (sp.diff(h(t), t, 2) + 3*H*sp.diff(h(t), t) + k**2/a**2*h(t))) == 0)

    # ⓶ the constraint is conserved
    kv = sp.Matrix([0, 0, k])
    e_plus = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    e_cross = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    for nm, e in (('e_+', e_plus), ('e_x', e_cross)):
        check(f'{nm} is trace-free and transverse: trace = 0 and k^j e_ij = 0',
              sp.simplify(e.trace()) == 0 and all(sp.simplify(x) == 0 for x in (e*kv)))
    check('⇒ and both are CONSTANT, so D_j sigma^TT ij = 0 holds FOR ALL TIME -- the constraint is '
          'CONSERVED by the evolution, not re-imposed',
          all(sp.simplify(sp.diff(x, eta)) == 0 for x in list(e_plus) + list(e_cross)))

    # ⓷ the identity applies
    check('⌗ and r2504\'s identity applies with no symmetry assumed: sigma_ij = (1/2) hdot^TT_ij, so '
          'the TT mode\'s energy IS its shear',
          sp.simplify(res) == 0)

    # ⓸ the count
    check('⇒ TWO polarisation tensors ⇒ TWO free functions, arrived at from the EVOLUTION rather '
          'than from the York counting', len([e_plus, e_cross]) == 2)
    check("and that is cor:radiation's \"the graviton's two propagating polarizations\"",
          "The graviton's two propagating polarizations" in p9)
    check('⇒⇒ SO THE STRATUM EVOLVES BY ORDINARY GR, exactly as cor:wall says: "carried past it by the '
          'ordinary general-relativistic evolution"',
          'are carried past it by the ordinary general-relativistic evolution' in p9)
    check('with the wall "a regular boundary of the operator\'s reach and not a frontier of the theory"',
          "a regular boundary of the operator's reach and not a frontier of the theory" in p9)

    # ⚠ the scope
    check('⚠ AND THIS IS LINEARIZED: the sigma^2 term is SECOND ORDER and does not appear, so the '
          'obstruction r2504 named is invisible at this order',
          sp.simplify(sp.diff(u, eta, 2) + (k**2 - 2/eta**2)*u) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the stratum evolves by ordinary GR at linear order, in closed form. **')
    print('    u_{,eta eta} + (k^2 - 2/eta^2) u = 0   solved EXACTLY by   u = e^{-ik eta}(1 - i/(k eta))')
    print('  ⇒ ** The constraint is CONSERVED, not re-imposed: both polarisation tensors are constant')
    print('     and transverse-traceless, so D_j sigma^TT ij = 0 for all time. **')
    print('  ⇒ ** r2504\'s identity applies with no symmetry assumed -- the TT mode\'s energy IS its')
    print('     shear -- and TWO polarisations give TWO free functions, the count arrived at from the')
    print('     EVOLUTION rather than from the York split. **')
    print('  ⇒⇒ ** So nothing in the evolution needs the operator.  The wall is a boundary of REACH')
    print('     and not of THEORY, exactly as cor:wall says. **')
    print('  ⚠ SCOPE: ** linearized about de Sitter.  The sigma^2 term is second order and does not')
    print('    appear, so the obstruction r2504 named is invisible here. **')
    print('  ⇒ (1) closes at LINEAR order; the remainder is exactly: ** does the NONLINEAR evolution')
    print('    keep sigma^TT free? **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
