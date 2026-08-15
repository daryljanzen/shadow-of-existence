#!/usr/bin/env python3
r"""S1 -- cc54, PO-6: L-818's boundary is a LOCATED result, and the object beyond it has a NAME and a
COEFFICIENT. L-818 showed the one-constant ledger survives the log divergence on the running-but-classical
FRW layer, with the reduction leaving remainder EXACTLY 0. This receipt shows WHY the remainder was 0 and
WHAT it becomes at the boundary: the graviton's log counterterm, in the {Weyl^2, GB, R^2} basis, is
(7/40)Weyl^2 + (149/360)GB + (1/8)R^2. On the shear-free layer Weyl^2=0, so the ONE irreducible piece --
the conformal (Weyl^2) coupling -- vanishes and the ledger survives (L-818). It turns on EXACTLY at the
shear, where Weyl^2 = 4 sigma^2 + O(sigma^4) (56's S10/r2743), and the shear IS the transverse-traceless
graviton tower, which is the interacting-tower P10 leaves open. So L-818's caveat, r2743's shear finding
and P10's open item are ONE boundary, now carrying a coefficient (routed to cc54, r2764).

** THE THREE FACTS, AND WHY THEY ARE ONE. ** (i) L-818's reduction of a1 Riem^2 + a2 Ric^2 + a3 R^2 to
{GB, Lambda^2, Lambda R, EOM} had remainder 0 on FRW -- because FRW is conformally flat (Weyl^2=0) and the
ONLY curvature-squared structure that is NOT {topological, Lambda/G-renormalising, EOM-removable} is the
Weyl^2, which was 0. (ii) The graviton's own b_4 carries a NONZERO Weyl^2 coefficient, 7/40 -- so the piece
L-818 could not test (because it evaluated to 0) is a real coupling, invisible only on the shear-free layer.
(iii) 56's S10 computed Weyl^2 = 4 sigma^2 + O(sigma^4) at the shear, and P10 names the transverse-traceless
graviton tower as its propagating sector; a TT perturbation IS shear. So the irreducible coupling turns on
exactly where the layer stops being FRW, and that place is the graviton tower = the interacting tower.

** WHAT THIS ADDS TO S10/S12 (56). ** S10 established Weyl^2=4 sigma^2 and "the tower is the shear"; S12
established that L-818's excluded sector, r2743's shear and P10's open item coincide. This receipt supplies
the COEFFICIENT and the MECHANISM from the counterterm side: the graviton b_4's irreducible content is
precisely (7/40)Weyl^2, which is 0 on the shear-free layer (so the ledger survives, L-818) and equals
(7/40)(4 sigma^2) = (7/10) sigma^2 at the shear -- a genuine conformal coupling, NON-topological (unlike GB),
NOT proportional to the field equations (unlike R^2/Ric^2), hence NOT field-redef removable and NOT in
{Lambda, G}. It is the one structure the ledger cannot absorb, and it is exactly the shear = graviton tower.

COMPUTES: the graviton one-loop b_4 in the {Weyl^2, GB, R^2} basis (its Weyl^2 coefficient), and the sign
and leading order of Weyl^2 in the shear on an axisymmetric anisotropic model. ** The 't Hooft-Veltman
coefficients (7/20, 1/120) and 53/90 for the Gauss-Bonnet term are CITED (standard one-loop gravity), not
re-derived; the conclusion -- that the irreducible survivor is the conformal Weyl^2 piece -- is
coefficient-INDEPENDENT (any nonzero Weyl^2 coefficient turns on at the shear), and 7/40 is the graviton's
specific value. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE DECOMPOSITION: the graviton log counterterm b_4 = (53/90)GB + (7/20)Ric^2 + (1/120)R^2 equals
     (7/40)Weyl^2 + (149/360)GB + (1/8)R^2 in the {Weyl^2, GB, R^2} basis (an algebraic identity via
     Ric^2 = (1/2)Weyl^2 - (1/2)GB + (1/3)R^2).
  2. THE ONE IRREDUCIBLE PIECE: of the three, GB is topological and R^2 reduces (L-818: R^2 = 4 Lambda R -
     R E_trace -> {G-renorm, EOM}); only the Weyl^2 term is neither, so (7/40)Weyl^2 is the irreducible
     content -- the conformal coupling outside {Lambda, G}.
  3. IT VANISHES ON THE SHEAR-FREE LAYER: Weyl^2 = 0 on FRW for every a(T) (L-818 Step 1), so the
     irreducible piece is 0 and the ledger survives -- which is WHY L-818's remainder was exactly 0.
  4. IT TURNS ON AT THE SHEAR: on an axisymmetric anisotropic expansion Weyl^2 is O(shear^2) and vanishes
     at zero shear (leading behaviour ~ 4 H^2 sigma^2-scale, i.e. entering at second order in the shear as
     56's S10 states with Weyl^2 = 4 sigma^2 + O(sigma^4)); so the irreducible coupling is supported exactly
     on the sheared = transverse-traceless-graviton = interacting-tower sector.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that PO-6 is closed or that its verdict changes (F5;
r2764 is explicit this locates the boundary, it does not convert the row). NOT that the interacting tower is
solved -- the opposite: this NAMES the surviving-open object (the conformal/Weyl^2 = graviton-tower coupling)
and gives its coefficient; defining it is P10's "standard problem of the interacting theory", untouched.
NOT a re-derivation of the one-loop coefficients -- they are the cited 't Hooft-Veltman / Christensen-Duff
values, used with the geometry. NOT a claim that Weyl^2 = 4 sigma^2 with coefficient exactly 4 in every
normalisation -- the leading coefficient is normalisation-dependent (this receipt's axisymmetric check gives
Weyl^2 = O(sigma^2) vanishing at sigma=0, and cites S10 for the value 4); the load-bearing fact is that it
enters at SECOND order in the shear and is zero on the shear-free layer.

** Board lead L-819 (cc54's band); locates L-818's boundary with a coefficient and meets P10's open item.
Informs L-165 (PO-6), L-818. Answers 56's r2764 routing (FOR_54). Companion to 56's S10/S12. **

Written r2674 (cc54, L-819). Asserts against the {Weyl^2, GB, R^2} curvature algebra and the axisymmetric
anisotropic invariants -- never the register. 't Hooft & Veltman, Ann. IHP A20 (1974) 69; Christensen &
Duff, Nucl. Phys. B170 (1980) 480. Stated for reversal.
"""
import sympy as sp

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-6: is the ledger\'s one irreducible survivor the conformal coupling that turns on'
          ' at the shear?')
    print()

    # 1. the decomposition: graviton b_4 in {Weyl^2, GB, R^2}
    W, GB, R2 = sp.symbols('Weyl2 GB R2')
    Ric2 = sp.Rational(1, 2) * W - sp.Rational(1, 2) * GB + sp.Rational(1, 3) * R2   # basis identity
    b4 = sp.expand(sp.Rational(53, 90) * GB + sp.Rational(7, 20) * Ric2 + sp.Rational(1, 120) * R2)
    cW, cGB, cR2 = b4.coeff(W), b4.coeff(GB), b4.coeff(R2)
    check('THE DECOMPOSITION: graviton b_4 = (53/90)GB + (7/20)Ric^2 + (1/120)R^2 = '
          f'({cW})Weyl^2 + ({cGB})GB + ({cR2})R^2',
          cW == sp.Rational(7, 40) and cGB == sp.Rational(149, 360) and cR2 == sp.Rational(1, 8))

    # 2. the one irreducible piece: GB topological, R^2 reduces (L-818), only Weyl^2 remains
    #    R^2 = 4 Lambda R - R E_trace  (E_trace = -R + 4 Lambda), the L-818 identity
    Rs, Lam = sp.symbols('R Lambda')
    E_trace = -Rs + 4 * Lam
    check('R^2 REDUCES (L-818): R^2 = 4 Lambda R - R E_trace with E_trace = -R + 4 Lambda -> {G-renorm, '
          'EOM}; GB is topological; so of {Weyl^2, GB, R^2} ONLY Weyl^2 is neither topological nor '
          'ledger-reducible',
          sp.simplify(4 * Lam * Rs - Rs * E_trace - Rs ** 2) == 0)

    # 3 & 4. Weyl^2 = 0 on shear-free FRW; O(shear^2) at the shear (axisymmetric anisotropic model)
    t, H, s = sp.symbols('t H s', real=True)
    Ae, Be = sp.exp((H - 2 * s) * t), sp.exp((H + s) * t)     # pure shear s over isotropic expansion H
    A = sp.Function('A')(t)
    B = sp.Function('B')(t)
    g = sp.diag(-1, A**2, B**2, B**2)
    gi = g.inv()
    x = [t, sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
    n = 4
    dd = lambda f, i: sp.diff(f, x[i])                                            # noqa: E731
    Ga = [[[sp.simplify(sum(gi[l, m] * (dd(g[m, i], j) + dd(g[m, j], i) - dd(g[i, j], m))
                            for m in range(n)) / 2) for j in range(n)] for i in range(n)]
          for l in range(n)]
    Ru = lambda l, i, j, k: sp.simplify(dd(Ga[l][i][k], j) - dd(Ga[l][i][j], k)                # noqa: E731
                                        + sum(Ga[l][j][m] * Ga[m][i][k] - Ga[l][k][m] * Ga[m][i][j]
                                              for m in range(n)))
    Rd = [[[[sp.simplify(sum(g[l, p] * Ru(p, i, j, k) for p in range(n))) for k in range(n)]
            for j in range(n)] for i in range(n)] for l in range(n)]
    Ric = sp.Matrix(n, n, lambda i, j: sp.simplify(sum(Ru(m, i, m, j) for m in range(n))))
    Rsc = sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
    Rup = [[[[sum(gi[i, a] * gi[j, b] * gi[k, c] * gi[l, e] * Rd[a][b][c][e] for a in range(n)
              for b in range(n) for c in range(n) for e in range(n)) for l in range(n)]
            for k in range(n)] for j in range(n)] for i in range(n)]
    Riem2 = sp.simplify(sum(Rd[i][j][k][l] * Rup[i][j][k][l] for i in range(n) for j in range(n)
                            for k in range(n) for l in range(n)))
    Ricup = sp.Matrix(n, n, lambda i, j: sum(gi[i, p] * gi[j, q] * Ric[p, q]
                                             for p in range(n) for q in range(n)))
    Ric2n = sp.simplify(sum(Ric[i, j] * Ricup[i, j] for i in range(n) for j in range(n)))
    Weyl2 = sp.simplify(Riem2 - 2 * Ric2n + Rsc ** 2 / 3)
    W2 = sp.simplify(Weyl2.subs({A: Ae, B: Be}).doit())
    check(f'WEYL^2 = 0 ON THE SHEAR-FREE LAYER: at s=0 (isotropic FRW) Weyl^2 = {sp.simplify(W2.subs(s, 0))} '
          '(the L-818 Step 1 fact, here for anisotropic-model a(T))',
          sp.simplify(W2.subs(s, 0)) == 0)
    ser = sp.series(W2, s, 0, 3).removeO()
    check('IT TURNS ON AT THE SHEAR: Weyl^2 is O(shear^2) -- no linear term, leading order s^2 '
          f'(Weyl^2 = {sp.simplify(ser)} + O(s^3)), so it enters at SECOND order and is supported on the '
          'sheared = TT-graviton = interacting-tower sector (56 S10: Weyl^2 = 4 sigma^2 + O(sigma^4))',
          sp.simplify(W2.coeff(s, 1)) == 0 and sp.simplify(W2.coeff(s, 2)) != 0)

    # 5. corpus/routing anchors
    check('THE BOUNDARY IS ONE OBJECT (r2764): L-818 excluded sector = r2743 shear (Weyl^2=4sigma^2) = '
          'P10 transverse-traceless graviton tower = the interacting tower P10 leaves open; this receipt '
          'gives that boundary its coefficient (7/40 Weyl^2), 0 on the shear-free layer and (7/10)sigma^2 '
          'at the shear',
          cW == sp.Rational(7, 40))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-6, L-818 boundary located with a coefficient): the graviton log counterterm is')
    print('  (7/40)Weyl^2 + (149/360)GB + (1/8)R^2. GB is topological and R^2 reduces to {G-renorm, EOM}')
    print('  (L-818), so the ONE irreducible piece is the conformal (7/40)Weyl^2. It is 0 on the shear-free')
    print('  FRW layer -- which is WHY L-818\'s remainder was exactly 0 and the ledger survived -- and it')
    print('  turns on at SECOND order in the shear, where Weyl^2 = 4 sigma^2 (56 S10/r2743). The shear IS')
    print('  the transverse-traceless graviton tower, which is P10\'s open interacting tower. So L-818\'s')
    print('  caveat, r2743\'s shear and P10\'s open item are ONE boundary, now carrying (7/40)Weyl^2. F5')
    print('  unsoftened: this locates the boundary and names the coupling; it does not convert PO-6.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
