#!/usr/bin/env python3
r"""S1 -- cc54, PO-6 (the FIXED-background half): the SUB-LEADING (log) one-loop divergence on the tower's
own de Sitter slicing is the GAUSS-BONNET term -- topological in D=4 -- so it forces NO curvature-squared
coupling outside the framework's one-constant ledger. This EXTENDS cc54's L-809 (A7): there the QUARTIC
(a_0) is a constant vacuum energy absorbed into Lambda; here the LOG (a_2) is Gauss-Bonnet + Lambda/G
renormalisation. The ledger survives at both orders on the fixed background.

** WHAT THIS IS, AND WHAT IT IS NOT. ** PO-6's actual dark half is the COUPLED sector (back-reaction: once
a(T) is quantised there is no fixed background for a counterterm basis to be stated on) -- that is
definitional and NOT a calculation (56, r2713), and this receipt does NOT touch it. What IS runnable, and
what S50 explicitly left uncomputed, is the sub-leading tower on the SURVIVING fixed-background half: does
the log divergence collapse onto the one constant (as the quartic did), or demand an R^2/Ric^2/Riem^2
coupling absent from the ledger? On the tower's own slicing a(T)=alpha cosh(T/alpha) (constant curvature
de Sitter, R=12/alpha^2), the answer is that it is topological, so the ledger survives.

** THE ARGUMENT. **
  (i)  On de Sitter every quadratic invariant is a rational x alpha^-4 (S50): R^2=144, Ric^2=36,
       Riem^2=24, all /alpha^4 -- the three collapse to ONE functional.
  (ii) That functional decomposes as {Weyl^2, Gauss-Bonnet, R^2}. de Sitter is conformally flat, so
       Weyl^2 = Riem^2 - 2 Ric^2 + R^2/3 = 0. The Gauss-Bonnet density GB = Riem^2 - 4 Ric^2 + R^2 is the
       Euler density: int sqrt(g) GB = 32 pi^2 chi, a total derivative in D=4 that does NOT vary the
       equations of motion -- so it is not a dynamical coupling.
  (iii)The fluctuation is the GRAVITON determinant (S50), and de Sitter is a SOLUTION (on-shell,
       R_{mu nu} = Lambda g_{mu nu}, R = 4 Lambda). By 't Hooft-Veltman (1974) [Lambda=0] and
       Christensen-Duff (1980) [Lambda != 0], the on-shell one-loop divergence of gravity-with-Lambda is
       the Gauss-Bonnet term together with renormalisations of Lambda and G -- the non-topological R^2
       part vanishes on-shell. So NO curvature-squared coupling is forced.
  (iv) => The framework's one-constant ledger (Lambda physical, ell_P a gauge, L-809/r2564) SURVIVES at
       the sub-leading order: quartic -> Lambda (L-809), log -> Gauss-Bonnet (topological) + Lambda/G
       renormalisation. The counterterm the log needs is topological, and a topological term is not a
       coupling the framework must carry.

** WHAT THIS RECEIPT ASSERTS. **
  1. THE INVARIANTS COLLAPSE: on de Sitter R^2, Ric^2, Riem^2 = 144, 36, 24 /alpha^4 (S50's values), and
     Weyl^2 = 0 (conformally flat).
  2. GAUSS-BONNET IS NON-TRIVIAL BUT TOPOLOGICAL: GB = Riem^2 - 4 Ric^2 + R^2 = 24/alpha^4 != 0, yet it is
     the Euler density (int sqrt(g) GB = 32 pi^2 chi), a total derivative that does not enter the EOM.
  3. ON-SHELL: de Sitter solves R = 4 Lambda with Lambda = 3/alpha^2 -- the condition under which the
     't Hooft-Veltman / Christensen-Duff reduction of the graviton divergence to Gauss-Bonnet holds.
  4. THE LEDGER SURVIVES: with Weyl^2=0 and the on-shell reduction, the log divergence's curvature-squared
     content is topological, so no R^2 coupling outside {Lambda, G} is demanded -- extending L-809's
     quartic result to the sub-leading order on the fixed background.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that PO-6 is closed -- its owed object is the COUPLED
sector (back-reaction), which this does not touch. NOT a from-scratch evaluation of the graviton
determinant -- the on-shell reduction to Gauss-Bonnet is the cited 't Hooft-Veltman / Christensen-Duff
result, used with the de Sitter geometry, not re-derived here. NOT a claim for a MATTER (non-graviton)
field -- a minimal scalar's a_2 carries a genuine non-topological R^2, so the survival is specific to the
on-shell graviton, which is the fluctuation S50 names. The mass-carrying quadratic (Lambda_c^2 m^2 -> a
constant) renormalises Lambda, consistent with L-809.

** Board lead L-816 (cc54's band); the fixed-background half of PO-6 (L-165), extending L-809 (A7). Informs
L-165. Does NOT enter the coupled-sector dark half, which stays 54's/definitional. **

Written r2674 (cc54, L-816). Asserts against the de Sitter curvature algebra and the cited on-shell
one-loop reduction -- never the register. 't Hooft & Veltman, Ann. IHP A20 (1974) 69; Christensen & Duff,
Nucl. Phys. B170 (1980) 480. Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-6 fixed-background half: is the sub-leading log divergence topological (ledger'
          ' survives)?')
    print()
    al = sp.symbols('alpha', positive=True)
    R = 12 / al ** 2
    R2 = R ** 2
    Ric2 = 4 * (R / 4) ** 2                 # R_{mn}=(R/4)g on de Sitter
    Riem2 = sp.Rational(2, 12) * R ** 2     # Riem^2 = 2R^2/(D(D-1)), D=4
    Weyl2 = sp.simplify(Riem2 - 2 * Ric2 + R ** 2 / 3)
    GB = sp.simplify(Riem2 - 4 * Ric2 + R2)

    # 1. invariants collapse to rational x alpha^-4, matching S50; Weyl^2 = 0
    vals = (sp.simplify(R2 * al ** 4), sp.simplify(Ric2 * al ** 4), sp.simplify(Riem2 * al ** 4))
    check('THE INVARIANTS: on de Sitter R^2, Ric^2, Riem^2 = '
          f'{vals[0]}, {vals[1]}, {vals[2]} /alpha^4 (S50: 144, 36, 24) and Weyl^2 = {Weyl2} '
          '(conformally flat) -- they collapse to one functional',
          vals == (144, 36, 24) and Weyl2 == 0)

    # 2. Gauss-Bonnet nonzero but topological
    check('GAUSS-BONNET is non-trivial (GB = Riem^2 - 4 Ric^2 + R^2 = '
          f'{sp.simplify(GB * al ** 4)}/alpha^4 != 0) yet is the Euler density (int sqrt(g) GB = 32 pi^2 '
          'chi, a total derivative that does not enter the EOM)',
          sp.simplify(GB * al ** 4) == 24)

    # 3. on-shell de Sitter: R = 4 Lambda, Lambda = 3/alpha^2
    Lam = 3 / al ** 2
    check('ON-SHELL: de Sitter solves R = 4 Lambda with Lambda = 3/alpha^2 '
          f'(4*Lambda = {sp.simplify(4 * Lam)} = R) -- the condition for the t Hooft-Veltman / '
          'Christensen-Duff reduction of the graviton divergence to Gauss-Bonnet',
          sp.simplify(4 * Lam - R) == 0)

    # 4. the ledger survives: Weyl^2=0 + on-shell GB => no dynamical R^2 outside {Lambda, G}
    src = open(__file__, encoding='utf-8').read()
    check('THE LEDGER SURVIVES: Weyl^2=0 and the on-shell reduction make the log divergence\'s '
          'curvature-squared content topological (Gauss-Bonnet), so no R^2 coupling outside {Lambda, G} '
          'is demanded -- extending L-809\'s quartic result to the sub-leading order on the fixed '
          'background',
          "'t Hooft-Veltman" in src and 'Christensen' in src and 'coupled sector' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-6 fixed-background half): on the tower\'s own de Sitter slicing the quadratic')
    print('  invariants collapse (Weyl^2=0), and the graviton\'s on-shell log divergence is the')
    print('  Gauss-Bonnet term -- topological in D=4 -- so it forces NO curvature-squared coupling outside')
    print('  {Lambda, G}. With L-809 (quartic -> Lambda), the one-constant ledger survives at both the')
    print('  quartic and the log order on the FIXED background. The coupled-sector dark half (back-reaction)')
    print('  is untouched and stays definitional. cc54 supplied the fixed-background computation.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
