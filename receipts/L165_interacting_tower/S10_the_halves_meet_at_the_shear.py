#!/usr/bin/env python3
"""S10 -- `PO-6`'s two halves MEET AT THE SHEAR, and the second-order entry says which processes can
break the degeneracy: none at one graviton, and the tower IS the shear.

** WHERE THIS ARRIVES. **  c54.215 established the counterterm degeneracy is CONFORMAL FLATNESS
(verified at r2736: $\\mathrm{Weyl}^2=0$ for $k=+1,0,-1$ and a FREE $a(T)$), and named the real limit as
the shear, $4\\sigma^2+O(\\sigma^4)$.  *** Nobody had run what that means for the ROW. ***

** ⓵ THE DEFICIT'S FORM, AND THE FAMILY IT IS COMPUTED ON, WHICH THIS RECEIPT USED TO NAME WRONG
(repaired r7346, on `r7341` ①). **  The polynomial below is `L549/Q1`'s, computed there symbolically
from a NAMED metric, and the family is READ OUT OF `Q1`'s OWN FILE here rather than retyped:

      *** g = diag(-1, e^{2t}, e^{2(t + sigma t)}, e^{2(t - sigma t)})   -- Q1's PLANAR
          Bianchi I family, rates (1, 1+sigma, 1-sigma), shear eigenvalues (0, sigma, -sigma)
          ** NOT axisymmetric: all three rates differ.  The AXISYMMETRIC family is the one this
          receipt used to name, (-2 sigma, sigma, sigma), rates (H-2 sigma, H+sigma, H+sigma) --
          and that is the whole distinction the repair turns on (corrected r7350 on `r7349` ③). **

          sigma_ab sigma^ab = 2 sigma^2
          C^2 = sigma^2 (4 + 16 sigma^2 / 3) = 4 sigma^2 + O(sigma^4)
          C^2(0) = 0 · C^2(1/10) = 76/1875 · C^2(1/2) = 4/3 ***

  ⇒ ** Leading coefficient 4, entering at SECOND order, vanishing identically at $\\sigma=0$. **

⛔ ** WHAT WAS WRONG, AND IT WAS NOT THAT NO METRIC WAS NAMED. **  This receipt named
$\\mathrm{diag}(-2\\sigma,\\sigma,\\sigma)$ with the invariant $6\\sigma^2$ -- a DIFFERENT family --
and asserted `Q1`'s polynomial beside it.  *** On the family it named, the same routines give
$12\\sigma^2(2\\sigma-1)^2 = 12\\sigma^2 - 48\\sigma^3 + 48\\sigma^4$, which is where `71`'s reported
$-48H\\sigma^3$ term comes from: `71` did not supply an arbitrary family, it used THIS ONE. ***  And
the guard that could not catch it was this receipt's own: it checked that the triple is TRACE-FREE,
which is true of every traceless triple.  ⇒ ** The control below computes the other family too, so
the referent is now load-bearing: swap the family back and ⓵ goes red. **
  ⌗ *And the evenness in $\\sigma$ is a SYMMETRY of `Q1`'s family and of no other: on
  $(0,\\sigma,-\\sigma)$ the relabelling $y\\leftrightarrow z$ carries $g(\\sigma)$ to $g(-\\sigma)$
  exactly, and on the family this receipt named not one of the six permutations does.*

** ⛭⛭ ⓶ AND P10 SAYS WHAT THE TOWER IS, IN ITS OWN WORDS. **  "the ** TRANSVERSE-TRACELESS graviton
modes form a discrete tower ** that deparametrizes to a unitary evolution in cosmic time" -- and again,
"the closed-$S^3$ layer's propagating sector---** the transverse-traceless graviton tower **, advanced
unitarily in cosmic time".

  ⇒⇒ *** THE TOWER IS THE SHEAR.  Transverse-traceless perturbation IS shear. ***

** ⛭ ⓷ SO `PO-6`'s TWO DECLARED HALVES ARE NOT INDEPENDENT -- THEY MEET AT THE SHEAR. **
  * ** the counterterm half ** ends where conformal flatness ends, which is at the shear;
  * ** the interacting-tower half ** quantises the transverse-traceless modes, which ARE the shear.
  ⇒ *** The row declares two halves (r2684) and the corpus supplies one object under both.  That is a
      convergence, not a coincidence, and it was invisible while the counterterm half was stated as
      "maximal symmetry" and the tower half as "back-reaction". ***

** ⓸ AND THE SECOND-ORDER ENTRY HAS A PHYSICAL READING. **  *** $C^2$ entering at $\\sigma^2$ means the
degeneracy SURVIVES TO FIRST ORDER in the graviton amplitude: a one-graviton process cannot break the
one-dimensional counterterm basis, and a two-graviton process can.  ** That is a statement about which
diagrams the basis is safe against, and it is the kind of thing a counterterm question wants. ** ***

WHAT IS NOT CLAIMED.  ** Not that the basis is computed at second order ** -- *** what is established is
where it must break and at what order, not what the second-order basis contains. ***  ** Not that the
$4\\sigma^2$ coefficient is re-derived from the metric ** -- cc54 computed it; its STRUCTURE is checked
here (vanishing at $\\sigma=0$, quadratic leading term) and the identification with the tower is read
from P10.  ** Not that the two halves are thereby one problem ** -- they meet at an object; they are
still asked about different things (a basis, and a spectrum).

** COMPUTES: the shear eigenvalues read out of `L549/Q1`'s own metric assignment, $\\mathrm{Weyl}^2$
and $\\sigma_{ab}\\sigma^{ab}$ for that family and for the one this receipt used to name, both with
`Q1`'s own curvature routines, and the structure of $C^2(\\sigma)$ at three amplitudes.  *** The shear
amplitude is the corpus's own object -- P10's transverse-traceless tower; nothing is imported except
`Q1`'s derivation of the polynomial this receipt reasons FROM, which is the repair. *** **

Written r2743.  Repaired r7346 on `r7341` ①.  Stated for reversal.
"""
import ast
import importlib.util
import io
import itertools
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


#: ** ⛭⛭ MARKERS ARE APPARATUS, NOT PROSE, AND A PIN INTO PROSE MUST NOT SEE THEM (r3962). **
#: ** This file failed because r3558's marker pass inserted `\ldg{variational}` INTO THE MIDDLE of a
#: ** sentence it quotes: "the transverse-traceless\ldg{variational} graviton modes form a discrete
#: ** tower ...".  *** The paper's words did not change.  A bake landing split the quotation. ***
#: **   ⇒ ** That is the fourth repair kind seen from the other side: `R1` was a receipt COUNTING
#: **     its own bake's landings, and this is a receipt QUOTING across one. **  A bake that lands
#: **     markers correctly should never be able to falsify a receipt about the sentence it marks,
#: **     so the markers are stripped here rather than the quotation being cut into fragments --
#: **     fragments would only move the fragility to wherever the NEXT marker lands.
MARKER = re.compile(r'\\(?:ldg|rcpt)\{[A-Za-z0-9_]+\}')


#: ** ⛭ THE REPAIR (r7346, on `r7341` ①): THE FAMILY IS READ OUT OF `Q1`'s OWN FILE. **
#: This receipt asserted `Q1`'s polynomial while NAMING a different family -- `71`'s
#: `diag(-2 sigma, sigma, sigma)`, invariant `6 sigma^2` -- and the only guard on the naming was that
#: the triple is trace-free, which every traceless triple satisfies.  *** A formula whose referent no
#: condition can reach is not a checkable claim: that is the defect, and naming the right family in
#: the prose would leave it exactly as unreachable. ***
#:   ⇒ ** So the triple is EXTRACTED from `L549/Q1`'s own metric assignment and the polynomial is
#:     DERIVED from it with `Q1`'s own curvature routines, and the family this receipt used to name is
#:     computed beside it as a control.  Swap the family back and ⓵ goes red. **
Q1_PATH = os.path.join(ROOT, 'receipts', 'L549_coupled_counterterms',
                       'Q1_the_degeneracy_is_conformal_flatness_not_maximal_symmetry_so_no_scale'
                       '_factor_can_break_it.py')


def q1_module():
    """`L549/Q1` itself.  Its top level is imports and definitions, so importing runs no check."""
    spec = importlib.util.spec_from_file_location('L549_Q1', Q1_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def q1_family(t, sig, _name='gB'):
    """the metric READ OUT of `Q1`'s own assignment, and the shear eigenvalues derived from it"""
    tree = ast.parse(io.open(Q1_PATH, encoding='utf-8').read())
    node = [n for n in ast.walk(tree) if isinstance(n, ast.Assign)
            and any(isinstance(x, ast.Name) and x.id == _name for x in n.targets)]
    if len(node) != 1:
        raise AssertionError(f'{_name} is assigned {len(node)} times in Q1')
    g = eval(ast.unparse(node[0].value), {'sp': sp, '__builtins__': {}}, {'t': t, 'sig': sig})
    return g, tuple(sp.simplify(sp.diff(sp.log(g[i, i]) / 2, t).coeff(sig)) for i in (1, 2, 3))


def bianchi(triple, t, sig):
    """the SAME construction for any trace-free triple -- the control differs only in the triple"""
    return sp.diag(-1, *[sp.exp(2 * (t + c * sig * t)) for c in triple])


def weyl(g, mod, x):
    Rs, ric2, riem2 = mod.invariants(g, x)
    return sp.simplify(sp.expand(mod.weyl_sq(Rs, ric2, riem2)))


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return MARKER.sub('', b[:j] if j > 0 else b)


def main():
    print()
    print("  S10 -- what does the shear deficit mean for PO-6's row?")
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    s = sp.symbols('sigma', real=True)
    t = sp.Symbol('t', real=True)
    x = [t] + list(sp.symbols('x y z', real=True))
    mod = q1_module()

    # ⓵ the family, read out of Q1's own file, and the polynomial derived from it
    gQ, triple = q1_family(t, s)
    inv = sp.simplify(sum((c*s)**2 for c in triple))
    check(f'⓵ the family is READ OUT of `L549/Q1`\'s own metric assignment -- shear eigenvalues '
          f'{tuple(sp.sstr(c*s) for c in triple)} over an isotropic expansion -- and it is trace-free',
          sp.simplify(sum(triple)) == 0 and len([c for c in triple if c != 0]) == 2)
    check(f'and ITS shear invariant is $2\\sigma^2$: $\\sigma_{{ab}}\\sigma^{{ab}}={sp.sstr(inv)}$ -- '
          f'NOT the $6\\sigma^2$ of the family this receipt used to name',
          sp.simplify(inv - 2*s**2) == 0)
    C2 = weyl(gQ, mod, x)
    check(f'⛭ and `Q1`\'s polynomial is what THAT metric gives, derived here with `Q1`\'s own '
          f'curvature routines rather than retyped: $C^2={sp.sstr(sp.factor(C2))}$',
          sp.simplify(C2 - s**2*(4 + sp.Rational(16, 3)*s**2)) == 0)
    check('and $C^2$ vanishes identically at $\\sigma=0$ -- the degeneracy is exact on any shear-free '
          'background', sp.simplify(C2.subs(s, 0)) == 0)
    check('and its leading term is $4\\sigma^2$ -- entering at SECOND order, not first',
          sp.expand(C2).as_poly(s).all_coeffs()[-3] == 4
          and sp.expand(C2).as_poly(s).all_coeffs()[-2] == 0)
    check('while being NON-zero away from zero, so the check is not vacuous: '
          f'$C^2(1/10)={sp.nsimplify(C2.subs(s, sp.Rational(1,10)))}$, '
          f'$C^2(1/2)={sp.nsimplify(C2.subs(s, sp.Rational(1,2)))}$',
          C2.subs(s, sp.Rational(1, 10)) == sp.Rational(76, 1875)
          and C2.subs(s, sp.Rational(1, 2)) == sp.Rational(4, 3))

    # ⓵ CONTROL -- the family this receipt used to name, through the SAME construction
    #: ** The old guard was that the triple is trace-free, and $(-2,1,1)$ is trace-free too, so it
    #: could not fail.  *** This one can: the polynomial is FALSE on the family that was named. *** **
    C2o = weyl(bianchi((-2, 1, 1), t, s), mod, x)
    check(f'⛔ CONTROL -- and the family this receipt USED TO NAME, diag$(-2\\sigma,\\sigma,\\sigma)$, '
          f'gives ${sp.sstr(sp.factor(C2o))}$ through the same construction, which is NOT `Q1`\'s '
          f'polynomial: the referent is load-bearing',
          sp.simplify(C2o - 12*s**2*(2*s - 1)**2) == 0
          and sp.simplify(C2o - C2) != 0)
    check('and it carries the odd term `71` reported as the contradiction, $-48H\\sigma^3$ at $H=1$, '
          'so the contradiction was correct ABOUT THE FAMILY THIS RECEIPT NAMED',
          sp.expand(C2o).coeff(s, 3) == -48 and sp.expand(C2).coeff(s, 3) == 0)
    check('while the evenness is a SYMMETRY of `Q1`\'s family and of no other: $y\\leftrightarrow z$ '
          'carries $g(\\sigma)$ to $g(-\\sigma)$ there, and not one of the six permutations does on '
          'the family that was named',
          sp.simplify(gQ.subs(s, -s) - sp.diag(gQ[0, 0], gQ[1, 1], gQ[3, 3], gQ[2, 2]))
          == sp.zeros(4, 4)
          and not any(sp.simplify(bianchi((-2, 1, 1), t, s).subs(s, -s) - bianchi(perm, t, s))
                      == sp.zeros(4, 4)
                      for perm in itertools.permutations((-2, 1, 1))))

    # ⓶ P10 identifies the tower
    check('⛭⛭ ⓶ and P10 names the tower: "the transverse-traceless graviton modes form a discrete '
          'tower that deparametrizes to a unitary evolution in cosmic time"',
          'transverse-traceless graviton modes form a discrete tower' in p10)
    check('and again as the propagating sector: "the transverse-traceless graviton tower, advanced '
          'unitarily in cosmic time"',
          'transverse-traceless graviton tower' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-6's two halves MEET AT THE SHEAR. **")
    print('  ⓵ ** The deficit, on L549/Q1\'s OWN family and derived from its metric here: ** shear')
    print('     eigenvalues (0, σ, −σ), σ_abσ^ab = 2σ², C² = σ²(4 + 16σ²/3) = 4σ² + O(σ⁴).')
    print('     ⛔ ** And on the family this receipt used to name, diag(−2σ,σ,σ), the same routines')
    print("       give 12σ²(2σ−1)² — 71's −48Hσ³ exactly. ** The referent is now load-bearing.")
    print('  ⛭⛭ ⓶ ** And P10 says what the tower IS: ** "the TRANSVERSE-TRACELESS graviton modes form')
    print('     a discrete tower".  *** Transverse-traceless perturbation IS shear.  THE TOWER IS THE')
    print('     SHEAR. ***')
    print('  ⛭ ⓷ ** So the two declared halves are not independent: ** the counterterm half ends where')
    print('     conformal flatness ends — at the shear; the tower half quantises the')
    print('     transverse-traceless modes — which are the shear.')
    print('     ⇒ *** A convergence, invisible while one half read "maximal symmetry" and the other')
    print('       read "back-reaction". ***')
    print('  ⓸ ** And the second-order entry has a physical reading: ** the degeneracy SURVIVES TO')
    print('     FIRST ORDER in the graviton amplitude.  ** A one-graviton process cannot break the')
    print('     one-dimensional basis; a two-graviton process can. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
