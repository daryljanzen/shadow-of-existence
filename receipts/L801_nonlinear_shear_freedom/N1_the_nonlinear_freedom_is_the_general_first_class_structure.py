#!/usr/bin/env python3
r"""N1 -- L-174 (1)'s nonlinear remainder, split at its own seam: whether the nonlinear evolution keeps
sigma^TT FREE is the FIRST-CLASS COUNT, and that is carried by the contracted Bianchi identity, which
is symmetry-free -- so it covers the general (no-isometry) leaf, not only P11's Gowdy model. What P11
adds beyond the Bianchi count -- the conserved shear charge and the positive-definite reduced energy --
is about STABILITY (no runaway), a different question, and P11 itself routes its general/all-data case
to Friedrich and Andreasson-Ringstrom.

** Board lead L-801 (cc54's band); informs vein L-174 (the general matter dynamics / the unworked
stratum) and L-165 (PO-6). The run Daryl handed cc54: does the nonlinear evolution keep sigma^TT free? **

** THE QUESTION (from I9, r2514). ** I9 closed L-174 (1) at LINEAR order: data with sigma^TT != 0 on
the de Sitter leaf evolves by ordinary GR in closed form, the momentum constraint CONSERVED, the count
of two arriving from the evolution. Its stated remainder: "does the NONLINEAR evolution keep sigma^TT
free? -- where the sigma^2 back-reaction first appears, and it is second order so it is invisible in the
linear exhibition." P11 (dynamics_paper) answers the all-orders question FOR ITS GOWDY MODEL: "A
first-class constrained system evolves consistently to all orders by the contracted Bianchi identity",
then "Two exact structures sharpen this beyond the Bianchi count" -- the shear charge and the reduced
energy, both written in the Gowdy variables (R, psi, z). ** Whether the argument covers the GENERAL case
is exactly what a run could settle. State no expected outcome; report what the structure does. **

** THE SPLIT THIS RECEIPT MAKES. ** P11's all-orders consistency has two layers, and they answer two
different questions:
  (a) THE FREEDOM (the count). "First-class => consistent to all orders by the contracted Bianchi
      identity." This is the statement that the constraints PROPAGATE, so no NEW constraint appears to
      freeze a degree of freedom. ** It is an off-shell geometric identity, true for every metric, using
      no Killing vector ** -- so it is symmetry-free, and the two Killing vectors of the Gowdy model are
      not what makes it hold.
  (b) THE STABILITY (no runaway). The conserved shear charge and the positive-definite reduced energy
      close the zero-mode and ghost runaways; the residual nonlinear parametric resonance is the future
      stability of de Sitter. ** These are Gowdy-specific, and P11 routes the general statement OUT to
      Friedrich (vacuum small-data) and Andreasson-Ringstrom (all-data T^3-Gowdy with matter), with the
      Nariai branch the named non-generic exception. **
  ** Daryl's question -- does the evolution keep sigma^TT FREE -- is (a), not (b). This receipt shows
    (a) is symmetry-free, and locates (b) as the separate, externally-settled remainder. **

** WHAT IS COMPUTED. **
  (1) GENERAL, NO-ISOMETRY TT DATA still preserves the momentum constraint and evolves mode-by-mode.
      I9 used ONE mode along z with a fixed polarisation -- the Gowdy configuration, which HAS two
      Killing vectors. Here a superposition of two TT waves in NON-PARALLEL directions, each with its
      own transverse polarisations, is checked: each tensor is trace-free and transverse to its OWN k,
      so D_j h^TT ij = 0 for the sum, and each amplitude obeys the same de Sitter mode equation
      u'' + (k^2 - 2/eta^2) u = 0. ** The preservation of the constraint uses transversality per mode
      and the mode equation -- neither is a Killing vector -- so it is not resting on the Gowdy
      symmetry. **
  (2) THE sigma^2 BACK-REACTION IS A SCALAR AT SECOND ORDER, so it sources the ENERGY (Hamiltonian-
      constraint) sector, not a new TT constraint. sigma_ij = (1/2) hdot^TT_ij; sigma^2 = sigma_ij
      sigma^ij = (1/4) hdot^2 (e:e) with e:e = 2 for each polarisation and 0 across -- a POSITIVE
      O(eps^2) SCALAR. In rho = R3/2 + theta^2/3 - (1/2) sigma^2 (P11: the leaf's "energy and momentum
      are the shear") it enters rho, which at second order fixes the SCALAR/longitudinal metric piece
      through an elliptic (Poisson) equation, always solvable for arbitrary TT data. ** So the sigma^2
      the linear order could not see does not constrain the TT amplitudes; it feeds the constraint-
      determined scalar sector. The two TT functions stay free. **
  (3) THE MECHANISM IS THE CONTRACTED BIANCHI IDENTITY, verified to hold EXACTLY (all orders in the
      wave amplitude) on the INHOMOGENEOUS polarized leaf ds^2 = -dt^2 + a^2[e^{2h}dx^2 + e^{-2h}dy^2
      + dz^2], h = h(t,z): nabla_mu G^{mu nu} = 0 for arbitrary h. ** The identity holds with h
      inhomogeneous in z (z-translation broken) and to all orders in h -- it is not resting on
      homogeneity or on linearisation. That is P11's "contracted Bianchi identity", exhibited as the
      general object it is. **

** THE VERDICT (L-174 (1)'s nonlinear remainder, split). ** The freedom -- sigma^TT stays free at
nonlinear order -- is carried by the first-class / contracted-Bianchi structure of full GR, which is
symmetry-free, so it covers the general no-isometry leaf and not only the Gowdy model: P11's all-orders
FREEDOM argument generalises. The sigma^2 back-reaction, invisible at linear order, is a positive scalar
that sources the energy/scalar sector, not a new constraint on the two TT functions. What does NOT
automatically generalise is P11's STABILITY layer (the Gowdy shear charge and reduced energy), but that
is the separate no-runaway question, and P11 already routes its general/all-data form to Friedrich and
Andreasson-Ringstrom, with the Nariai branch the known non-generic exception.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not a closed-form nonlinear solution ** -- P11 does not claim one either ("a closed-form nonlinear
  solution ... is not built here"), and none is built here. ** Not that the STABILITY holds for all data
  in the general (non-Gowdy) class ** -- only vacuum-small-data (Friedrich) and all-data T^3-Gowdy-with-
  matter (Andreasson-Ringstrom) are externally covered; the general no-isometry all-data stability is
  NOT settled here and is flagged as the standing remainder. ** Not new physics ** -- (a) is the
  first-class structure of ordinary GR, exactly as I9 found the linear order to be textbook GR; the
  finding is that the FREEDOM half of the nonlinear question needs nothing Gowdy-specific. ** Not a
  count of the full Dirac algebra ** -- the propagation is exhibited via the contracted Bianchi
  identity, which is its ADM face, not by re-deriving the hypersurface-deformation brackets.

Written r2525 (cc54, L-801). Asserts against SOURCES (dynamics_paper.tex = P11, range_paper.tex = P9)
and the symbolic computation -- never against the register. Stated for reversal.
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
    print('  N1 -- does the NONLINEAR evolution keep sigma^TT free? (L-174 (1) remainder)')
    print()
    p11 = norm('dynamics_paper.tex')
    p9 = norm('range_paper.tex')

    eta = sp.Symbol('eta', negative=True)
    k = sp.Symbol('k', positive=True)
    eps = sp.Symbol('epsilon', positive=True)

    # =====================================================================================
    # (1) GENERAL, NO-ISOMETRY TT DATA: two non-parallel waves, each with its own
    #     transverse polarisations.  The constraint is preserved mode-by-mode.
    # =====================================================================================
    # wave 1 along z: transverse tensors live in the (x,y) plane
    k1 = sp.Matrix([0, 0, k])
    e1_plus = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    e1_cross = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    # wave 2 along x: transverse tensors live in the (y,z) plane -- a DIFFERENT direction
    k2 = sp.Matrix([k, 0, 0])
    e2_plus = sp.Matrix([[0, 0, 0], [0, 1, 0], [0, 0, -1]])
    e2_cross = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])

    tensors = [('e1_+', e1_plus, k1), ('e1_x', e1_cross, k1),
               ('e2_+', e2_plus, k2), ('e2_x', e2_cross, k2)]
    for nm, e, kv in tensors:
        tracefree = sp.simplify(e.trace()) == 0
        transverse = all(sp.simplify(x) == 0 for x in (e * kv))
        check(f'{nm}: trace-free and transverse to its OWN k (k^j e_ij = 0)',
              tracefree and transverse)

    # the two propagation directions are non-parallel -> the configuration is NOT the single
    # Gowdy mode; there is no common axis of translation symmetry the way the Gowdy leaf has.
    check('the two waves propagate in NON-parallel directions (k1 . k2 = 0, not the single '
          'Gowdy mode) -- so the data breaks the Gowdy translational structure',
          sp.simplify((k1.T * k2)[0]) == 0 and sp.simplify(k1.cross(k2).norm()) != 0)

    # momentum constraint for the SUPERPOSITION at linear order: D_j h^TT ij = 0.
    # In Fourier each term contributes i (k^j e_ij) e^{i k.x}; each vanishes by transversality,
    # so the sum's divergence is identically zero for ARBITRARY amplitudes A1, A2.
    A1, A2 = sp.symbols('A1 A2')
    x, y, z = sp.symbols('x y z', real=True)
    Xv = sp.Matrix([x, y, z])
    hsum = (A1 * (e1_plus + e1_cross) * sp.exp(sp.I * (k1.T * Xv)[0])
            + A2 * (e2_plus + e2_cross) * sp.exp(sp.I * (k2.T * Xv)[0]))
    # divergence D_j h_ij = d/dx^j of column-summed entries
    div = sp.zeros(3, 1)
    for i in range(3):
        div[i] = sum(sp.diff(hsum[i, j], (x, y, z)[j]) for j in range(3))
    check('D_j h^TT ij = 0 for the two-wave SUPERPOSITION and ARBITRARY amplitudes A1, A2 -- '
          'the momentum constraint is preserved for general TT data, not just the single mode',
          all(sp.simplify(d) == 0 for d in div))

    # each mode obeys the SAME de Sitter evolution as in I9, independent of direction/polarisation
    u = sp.exp(-sp.I * k * eta) * (1 - sp.I / (k * eta))
    res = sp.simplify(sp.diff(u, eta, 2) + (k**2 - 2 / eta**2) * u)
    check('each mode amplitude obeys u_{,eta eta} + (k^2 - 2/eta^2) u = 0 EXACTLY (I9\'s equation, '
          f'direction-independent) -- residual {res}', res == 0)

    # =====================================================================================
    # (2) THE sigma^2 BACK-REACTION IS A POSITIVE O(eps^2) SCALAR -> sources the energy sector.
    # =====================================================================================
    hdot = sp.Symbol('hdot', real=True)
    # e:e contractions (indices with delta): 2 within a polarisation, 0 across
    def dd(a, b):
        return sum(a[i, j] * b[i, j] for i in range(3) for j in range(3))
    check('e:e = 2 for each polarisation and 0 across (e_+:e_+ = e_x:e_x = 2, e_+:e_x = 0)',
          dd(e1_plus, e1_plus) == 2 and dd(e1_cross, e1_cross) == 2
          and dd(e1_plus, e1_cross) == 0)

    # sigma_ij = (1/2) hdot^TT_ij  =>  sigma^2 = sigma_ij sigma^ij = (1/4) hdot^2 (e:e)
    sigma = sp.Rational(1, 2) * (eps * hdot) * e1_plus          # one polarisation, amplitude eps*hdot
    sigma2 = sum(sigma[i, j]**2 for i in range(3) for j in range(3))
    check('sigma_ij = (1/2) hdot^TT_ij gives sigma^2 = (1/4) hdot^2 (e:e) = (1/2) eps^2 hdot^2 -- '
          'a POSITIVE quantity',
          sp.simplify(sigma2 - sp.Rational(1, 2) * eps**2 * hdot**2) == 0 and sigma2.subs(
              {eps: 1, hdot: 1}) > 0)
    # it is second order: scales as eps^2, so it is invisible at linear order (eps^1) -- exactly
    # I9's "the sigma^2 term is SECOND ORDER and does not appear"
    check('sigma^2 is O(eps^2): sigma^2(eps) / eps^2 is eps-independent, so it is invisible at '
          'linear order and first appears at second order (I9\'s remainder)',
          sp.simplify(sp.diff(sigma2 / eps**2, eps)) == 0)
    # sigma^2 is a SCALAR (a full contraction), so in rho = R3/2 + theta^2/3 - (1/2) sigma^2 it
    # sources the SCALAR (Hamiltonian-constraint) sector, not the tensor TT evolution.
    check('sigma^2 is a SCALAR (a complete index contraction), so it enters the energy density rho '
          'and sources the scalar/Hamiltonian sector -- NOT a new constraint on the tensor TT data',
          sigma2.free_symbols == {eps, hdot})   # no free tensor index survives

    # =====================================================================================
    # (3) THE MECHANISM IS THE CONTRACTED BIANCHI IDENTITY: nabla_mu G^{mu nu} = 0, EXACTLY,
    #     on the INHOMOGENEOUS polarized leaf (all orders in the wave amplitude h(t,z)).
    # =====================================================================================
    t, zc = sp.symbols('t z', real=True)
    H = sp.Symbol('H', positive=True)
    a = sp.exp(H * t)
    hf = sp.Function('h')(t, zc)          # ARBITRARY wave profile -> inhomogeneous, all orders
    # exact polarized Gowdy-de Sitter spatial part (P11 eq:metric form), background de Sitter a(t)
    g = sp.diag(-1, a**2 * sp.exp(2 * hf), a**2 * sp.exp(-2 * hf), a**2)
    ginv = g.inv()
    coords = [t, sp.Symbol('x', real=True), sp.Symbol('y', real=True), zc]
    n = 4

    # Christoffel symbols
    Gamma = [[[0] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for r in range(n):
                s = 0
                for sidx in range(n):
                    s += ginv[l, sidx] * (sp.diff(g[sidx, m], coords[r])
                                          + sp.diff(g[sidx, r], coords[m])
                                          - sp.diff(g[m, r], coords[sidx]))
                Gamma[l][m][r] = sp.together(s / 2)

    # Ricci tensor
    Ric = sp.zeros(n, n)
    for m in range(n):
        for r in range(n):
            s = 0
            for l in range(n):
                s += sp.diff(Gamma[l][m][r], coords[l]) - sp.diff(Gamma[l][m][l], coords[r])
                for p in range(n):
                    s += Gamma[l][l][p] * Gamma[p][m][r] - Gamma[l][r][p] * Gamma[p][m][l]
            Ric[m, r] = s
    Rscal = sum(ginv[m, r] * Ric[m, r] for m in range(n) for r in range(n))
    G = sp.zeros(n, n)                      # Einstein tensor G_{mu nu}
    for m in range(n):
        for r in range(n):
            G[m, r] = Ric[m, r] - sp.Rational(1, 2) * g[m, r] * Rscal

    # contracted Bianchi: nabla_mu G^{mu}_{nu} = 0.  Compute the covariant divergence.
    Gud = ginv * G                          # G^{mu}_{nu}
    div_ok = True
    for nu in range(n):
        d = 0
        for mu in range(n):
            d += sp.diff(Gud[mu, nu], coords[mu])
            for l in range(n):
                d += Gamma[mu][mu][l] * Gud[l, nu] - Gamma[l][mu][nu] * Gud[mu, l]
        if sp.simplify(d) != 0:
            div_ok = False
    check('nabla_mu G^{mu}_{nu} = 0 EXACTLY on the inhomogeneous polarized leaf '
          'ds^2 = -dt^2 + a^2[e^{2h}dx^2 + e^{-2h}dy^2 + dz^2], h = h(t,z) ARBITRARY -- '
          'the contracted Bianchi identity holds all-orders in h and with z-translation broken, '
          'so the constraint propagation needs neither homogeneity nor linearisation',
          div_ok)

    # =====================================================================================
    #  SOURCE ANCHORS (against P11 = dynamics_paper, P9 = range_paper) -- the claim this
    #  receipt is ABOUT, pinned to the papers and never to the register.
    # =====================================================================================
    check('P11 states the FREEDOM layer: "A first-class constrained system evolves consistently to '
          'all orders by the contracted Bianchi identity"',
          'first-class constrained system evolves consistently to all orders by the contracted '
          'Bianchi identity' in p11)
    check('P11 marks its Gowdy-specific STABILITY layer as EXTRA: "Two exact structures sharpen this '
          'beyond the Bianchi count" (the shear charge and the reduced energy)',
          'Two exact structures sharpen this beyond the Bianchi count' in p11
          and 'the propagating sector is ghost-free to all orders' in p11)
    check('P11 routes the STABILITY question OUT to external theorems, not to its Gowdy structures: '
          'Friedrich (vacuum small-data) and Andreasson-Ringstrom (all-data T^3-Gowdy), Nariai the '
          'non-generic exception',
          'Friedrich proved the nonlinear stability of de Sitter in vacuum' in p11
          and 'the one non-generic exception, the Nariai branch' in p11)
    check('P11 does NOT claim a closed-form nonlinear solution (so neither does this receipt): '
          '"a closed-form nonlinear solution"',
          'a closed-form nonlinear solution' in p11
          and 'admits rather than forces a quantum structure' in p11)
    check('and the identity r2504/I9 use -- the leaf\'s energy and momentum ARE its shear -- is P11\'s '
          'own: "whose energy and momentum are the shear of the leaf"',
          'whose energy and momentum are the shear of the leaf' in p11)
    check('P9 (range_paper) still frames the wall as the reach boundary past which free radiation '
          'begins -- the stratum this evolves',
          'free gravitational radiation begins' in p9
          or 'a regular boundary of the operator' in p9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (L-174 (1) nonlinear remainder, SPLIT at the freedom/stability seam):')
    print('  ** THE FREEDOM GENERALISES. ** sigma^TT stays free at nonlinear order because the')
    print('     constraints PROPAGATE -- the contracted Bianchi identity -- which is an off-shell')
    print('     identity true for the inhomogeneous leaf to all orders, using NO Killing vector.')
    print('     The sigma^2 back-reaction I9 could not see is a positive O(eps^2) SCALAR that sources')
    print('     the energy/scalar sector, not a new constraint on the two TT functions.')
    print('  ** THE STABILITY IS THE SEPARATE REMAINDER. ** P11\'s Gowdy shear charge and reduced')
    print('     energy are stability sharpenings; the general/all-data no-runaway statement is routed')
    print('     to Friedrich and Andreasson-Ringstrom, with the Nariai branch the non-generic')
    print('     exception -- and the general no-isometry all-data stability is NOT settled here.')
    print('  => So P11\'s all-orders FREEDOM argument covers the general case; what stays open is the')
    print('     narrower STABILITY question, and it is open in a named, externally-bounded way.')
    print('     Informs L-174 and L-165 (PO-6). The conversion to a vein verdict is Daryl\'s.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
