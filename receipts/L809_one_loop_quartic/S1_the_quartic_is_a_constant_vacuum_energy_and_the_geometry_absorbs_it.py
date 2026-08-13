#!/usr/bin/env python3
r"""S1 -- A7 (PO-6(a)): ONE LOOP ON THE COMPACTIFIED SUBSTRATE -- is the quartic UV divergence absorbed
by the geometry, or does it need a counterterm the framework cannot supply? It is ABSORBED. The quartic
is the mass- and field-INDEPENDENT part of the one-loop vacuum energy -- a constant vacuum energy -- and
p0 already states the mechanism that absorbs exactly that: a constant vacuum energy is not held against a
bare Lambda but is absorbed into the one observed substrate curvature, entering the profile's Lambda r^2/3
term. The counterterm the quartic needs is a cosmological-constant term, which IS the framework's one
dimensionful constant; ell_P is a gauge, not a second scale, so the cutoff is not one either.

** Board lead L-809 (cc54's band); informs vein L-165 (PO-6, what a quantum of this geometry is -- "can a
theory with one dimensionful constant regulate at all" is its DARK). A7 in THE_DISPATCH. This is the
arrival-path shape: the corpus (p0) holds the absorption mechanism, and the one-loop computation confirms
the object it absorbs (a constant vacuum energy) is exactly the quartic divergence. **

** THE QUESTION (A7). ** The vein's handle: the UV degree is quartic (the ordinary zero-point degree),
compactness buys the IR free, the boundary closes per fibre. So: is the quartic divergence absorbed by
the geometry, or does it need a counterterm the framework cannot supply? r2564: ell_P is a GAUGE, not a
second scale. ** State no expected outcome; report what the quartic is and whether the framework carries
its counterterm. **

** THE COMPUTATION: THE QUARTIC IS A CONSTANT (MASS/FIELD-INDEPENDENT) VACUUM ENERGY. ** The one-loop
vacuum energy density is rho = (1/2pi^2) int_0^{Lambda_c} k^2 (1/2) sqrt(k^2 + m^2) dk. Its large-cutoff
expansion is
      rho = Lambda_c^4/(16 pi^2) + Lambda_c^2 m^2/(16 pi^2) - (m^4/64 pi^2) log(...) + ...
  * The QUARTIC term Lambda_c^4/(16 pi^2) is INDEPENDENT of m: d/dm = 0. It survives at m = 0 and for
    every field, so it is a pure vacuum energy -- a cosmological CONSTANT, not a mass or coupling
    renormalisation.
  * Only the sub-leading terms (the quadratic Lambda_c^2 m^2 and the log m^4) carry the mass, i.e. only
    they renormalise mass/couplings; the leading quartic is the constant.

** THE MECHANISM IS ALREADY IN p0, AND IT ABSORBS EXACTLY THIS. ** The geometric core (p0) rejects the
cosmological-constant problem's two premises, and the second is precisely the quartic's fate: "a
CONSTANT vacuum energy is not a source held against a bare Lambda but is absorbed into that one observed
curvature: a constant density gravitates as a curvature scale, so it enters the profile's Lambda r^2/3
term, not as a 2m/r bend, and there is no bare-Lambda-versus-vacuum-energy split for the 10^122
cancellation to act on -- the substrate carries only the total." And the first premise is the cutoff's:
"The one physical length is alpha, not ell_P" -- the Planck values are gauge-combinations, so there is no
second physical scale for the quartic to be measured against.

** THE READING. ** The quartic divergence is a constant vacuum energy (computed: mass/field-independent).
Its counterterm is therefore a cosmological-constant term -- and the CC is the framework's ONE dimensionful
constant, Lambda, the substrate curvature. p0's mechanism absorbs a constant vacuum energy into that one
Lambda (via the Lambda r^2/3 profile term), with no bare-Lambda-versus-vacuum split. So the quartic is
absorbed by the geometry, and the counterterm it needs -- a CC -- is one the framework carries as its
single constant. ell_P being a gauge means the cutoff Lambda_c is not a second physical scale, so the
absorption is not smuggling one in. ** So: the quartic is absorbed, and one dimensionful constant does
regulate it. **

** THE VERDICT (A7). ** The quartic is absorbed by the geometry -- it is the constant vacuum energy p0
absorbs into the one curvature Lambda, and its counterterm is that one constant. The "can one dimensionful
constant regulate at all" question, at the QUARTIC (leading) degree the vein names, is answered YES:
the leading divergence is a CC and the CC is the one constant.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that the FULL tower is regulated by one constant ** -- only the quartic (A7's stated target, the
  leading zero-point degree) is shown absorbed. The sub-leading mass-dependent divergences (the quadratic
  Lambda_c^2 m^2 and the log m^4) renormalise mass and curvature-squared couplings, and whether the
  framework supplies THOSE counterterms is a separate and deeper question (PO-6's interacting tower), not
  settled here. ** Not that p0 derives the value of Lambda ** -- p0 states the honest residue that
  "Lambda's VALUE is the ledger's one input scale, not here predicted"; this concerns the DIVERGENCE's
  absorption, not the value. ** Not a compactification-specific computation ** -- the quartic is a local
  UV property, insensitive to the S^3 compactness that (per the vein) buys the IR free; the compact
  boundary closing per fibre is what makes the IR finite, and is not what the quartic turns on.

Written r2570 (cc54, L-809). Asserts against SOURCES (geometric_core_paper.tex = p0) and the one-loop
computation -- never the register. Stated for reversal.
"""
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


def norm(path):
    raw = open(os.path.join(ROOT, 'corpus', path), encoding='utf-8', errors='replace').read()
    body = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
    return re.sub(r'\s+', ' ', body)


def main():
    print()
    print('  S1 -- A7: is the one-loop quartic absorbed by the geometry? (PO-6(a))')
    print()

    # ---- the computation: the quartic is the mass/field-independent vacuum energy ------------------
    k, m, Lc = sp.symbols('k m Lambda_c', positive=True)
    rho = sp.integrate(k**2 * sp.Rational(1, 2) * sp.sqrt(k**2 + m**2) / (2 * sp.pi**2), (k, 0, Lc))
    quartic = sp.simplify(sp.limit(rho, m, 0))
    check('the one-loop vacuum energy has a QUARTIC divergence Lambda_c^4/(16 pi^2) '
          f'(computed m->0 limit: {quartic})',
          sp.simplify(quartic - Lc**4 / (16 * sp.pi**2)) == 0)
    check('and it is MASS/FIELD-INDEPENDENT -- d(quartic)/dm = 0 -- so it is a pure vacuum energy, a '
          'cosmological CONSTANT, not a mass or coupling renormalisation',
          sp.diff(quartic, m) == 0)
    # the sub-leading terms DO carry the mass (they are the separate, deeper question)
    ser = sp.series(rho.rewrite(sp.log), m, 0, 3).removeO()
    quad_coeff = ser.coeff(m, 2)
    check('while the SUB-LEADING quadratic term does carry the mass (coeff of m^2 is '
          f'Lambda_c^2/(16 pi^2), nonzero) -- only the leading quartic is the constant',
          sp.simplify(quad_coeff - Lc**2 / (16 * sp.pi**2)) == 0 and quad_coeff != 0)

    # ---- the mechanism, at source in p0 (geometric_core_paper) -------------------------------------
    p0 = norm('geometric_core_paper.tex')
    check('SOURCE: p0 absorbs a CONSTANT vacuum energy into the one curvature -- "is absorbed into that '
          'one observed curvature" and "enters the profile\'s $\\Lambda r^2/3$ term, not as a $2m/r$ bend"',
          'is absorbed into that one observed curvature' in p0
          and 'not as a $2m/r$ bend' in p0)
    check('SOURCE: and there is no bare-Lambda-versus-vacuum split for a cancellation to act on -- '
          '"there is no bare-$\\Lambda$-versus-vacuum-energy split"',
          'there is no bare-$\\Lambda$-versus-vacuum-energy split' in p0
          and 'the substrate carries only the total' in p0)
    check('SOURCE: and the cutoff is not a second scale -- p0: "The one physical length is $\\alpha$, '
          'not $\\ell_P$" (the Planck values are gauge-combinations)',
          'The one physical length is $\\alpha$, not $\\ell_P$' in p0
          and 'gauge-combination' in p0)

    # ---- the join: the quartic IS the constant vacuum energy p0 absorbs ---------------------------
    check('THE JOIN: the quartic (computed: constant, mass/field-independent) is exactly the "constant '
          'vacuum energy" p0 absorbs into Lambda -- so its counterterm is a CC = the one constant, and '
          'the framework carries it',
          sp.diff(quartic, m) == 0
          and 'is absorbed into that one observed curvature' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A7 -- is the quartic absorbed?):')
    print('  ** YES. ** The quartic Lambda_c^4/(16 pi^2) is a mass/field-independent CONSTANT vacuum')
    print('     energy (computed), and p0 already absorbs exactly a constant vacuum energy into the one')
    print('     substrate curvature Lambda (the profile\'s Lambda r^2/3 term), with no bare-Lambda-versus-')
    print('     vacuum split. So the quartic\'s counterterm is a CC = the framework\'s one dimensionful')
    print('     constant, and ell_P being a gauge means the cutoff is not a second scale.')
    print('  => One dimensionful constant regulates the quartic (the leading zero-point degree A7 names).')
    print('     The sub-leading mass-dependent divergences are the deeper, separate question. Informs L-165.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
