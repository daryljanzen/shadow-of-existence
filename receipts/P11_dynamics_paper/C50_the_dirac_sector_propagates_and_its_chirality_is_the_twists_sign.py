#!/usr/bin/env python3
r"""
C50 — THE DIRAC SECTOR ON THE UNPOLARISED GOWDY--DE SITTER MEMBER, BUILT.  IT PROPAGATES, AND ITS
CHIRALITY IS THE SIGN OF THE GRAVITON'S TWIST.

** WHAT WAS OWED, AND HOW NARROW IT WAS. **  `P07` carries an open item worded "the descent onto a
PROPAGATING spinor sector".  Measured at source (`WHAT_IS_UNFINISHED` B2, r3801) two of its three
pieces already existed:

  · `P14` builds the fermion as BOUND modes of the existent leaf -- one chiral zero-mode per throat
    wall, chirality $R=\gamma^5$, exact.  It is explicitly NOT a propagating theory and says so.
  · `P11` `sec:unpolarized` builds the PROPAGATING GRAVITATIONAL member: two polarisations as a wave
    map into $\mathbb H^2$, conserved twist $c=R\,e^{2P}Q_t$, orientation parity acting as $c\to-c$.
  · `P14`'s own sentence names what is missing: ** "what is not built is the Dirac sector on it." **

So the owed work is one thing: put a Dirac field on the member `P11` already built, and report what
it does.  That is what this does.

** SIX RESULTS.  THE THIRD AND THE SIXTH ARE THE ONES WORTH HAVING. **

  (1) ** THE FRAME, AND THE TWIST IS A SPIN-CONNECTION COMPONENT. **  On the unpolarised metric the
      orthonormal coframe $e^0=e^{A}dt$, $e^1=e^{A}dz$, $e^2=e^{\psi}(dx+\omega\,dy)$,
      $e^3=R\,e^{-\psi}dy$ ($A=\gamma-\psi$) has spin connection whose $(23)$ block is EXACTLY the
      twist:
             ** omega_{t,23} = -(1/2) c e^{-2 psi} ,   omega_{z,23} = -(1/2) c_z e^{-2 psi} **
      with $c=R\,e^{2P}Q_t$ `P11`'s own conserved charge.  *The graviton's handedness was already a
      piece of the fermion's connection; nobody had written the connection down.*

  (2) ** THE SEPARATION IS CLEAN AND THE FRICTION IS REMOVABLE EXACTLY. **  Separating on the two
      Killing directions and rescaling by $\Omega=e^{-A/2}R^{-1/2}$ removes EVERY background-
      derivative term -- $\gamma$, $\psi$ and $R$ derivatives all cancel, verified symbolically.

  (3) ** THE WHOLE REDUCED OPERATOR IS FOUR TERMS, AND THE TWIST ENTERS ONLY AS AN AXIAL VECTOR. **
             ** gamma^0 d_t + gamma^1 d_z + i m_x gamma^2 + i m_y gamma^3
                                          + i b_z gamma^5 gamma^1 + i b_t gamma^5 gamma^0 = 0 **
      with $m_x=e^{A-\psi}k_x$, $m_y=e^{A+\psi}(k_y-k_x\omega)/R$ the transverse momenta seen as
      masses, and $(b_t,b_z)=(c_z,c_t)e^{-2\psi}/4$ the twist -- the Hodge dual of the twist 1-form,
      carried on $\gamma^5\gamma^a$.  Asserted as an EXACT matrix identity, zero residual.

  (4) ** IT PROPAGATES.  **  This is the question the item asks.  The principal symbol is
      $e^{-A}(\gamma^0\partial_t+\gamma^1\partial_z)$ -- independent of the twist AND of the
      transverse momenta -- so the characteristic matrix is $\Sigma=\gamma^0\gamma^1$, hermitian
      with eigenvalues exactly $\pm1$: ** the characteristics ARE the spacetime light cone, on the
      inhomogeneous member as much as the homogeneous one, so nothing can be trapped. **  Measured:
      a wave packet's centroid moves at speed $1.000000$.  *Against `P14`'s wall modes, which bind
      because a superpotential changes sign; here there is no wall in $z$ and nothing binds.*

  (5) ** THE TWO NORMS AGREE HERE, AND THE REASON IS THAT $\Omega^2=1/\sqrt h$ EXACTLY. **  `P14`
      established that the norm is load-bearing: its wall mode is normalisable in the leaf's proper
      measure and NOT in the tortoise measure.  On this member the flattening factor of the reduced
      operator IS the leaf's own volume element, so the conserved spacetime Dirac norm and the
      leaf's proper-measure norm are ** the same integral **, $\int\chi^\dagger\chi\,dz$.  Verified
      symbolically and conserved to $3\times10^{-11}$ under evolution.

  (6) ** THE FERMION'S CHIRALITY IS LOCKED TO THE SIGN OF THE GRAVITON'S TWIST. **  At $k_x=k_y=0$
      the operator block-decouples on $\gamma^5$ and the two chiralities carry OPPOSITE momentum
      shifts:
             ** E_R = +/-(k - b) ,   E_L = +/-(k + b) ,   b = c e^{-2 psi}/4 **
      so the parity ($c\to-c$ together with $\gamma^5\to-\gamma^5$) is a symmetry and NEITHER HALF
      ALONE IS.  Measured on a genuine vacuum-$\Lambda$ background: the two chiralities accumulate a
      relative phase $2\int b\,dt$, to six figures, ZERO at $c=0$, and sign-reversing with $c$.
      ⇒ *** The graviton's handedness and the fermion's are one datum on this background. ***

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · Massless Dirac TEST field on the vacuum member: no back-reaction, no quantisation, no mass term.
  · The algebra (1)-(3), (5) is general $(t,z)$; the numerics (4), (6) are on the HOMOGENEOUS
    reduction, which is where `P11`'s $c$ is a conserved charge.
  · ** The chirality/twist locking is exact in the transverse zero mode and BROKEN by transverse
    momenta ** -- measured, not assumed: at $k_x=0.9$ the relative phase departs from $2\int b\,dt$
    by 13%.  That is the expected physics ($m_x$, $m_y$ are mass terms and a mass breaks chirality),
    and the torus always carries the $k_x=k_y=0$ mode, so the locked sector always exists.
  · NOT CLAIMED: any Standard-Model identification, any generation count, the compact-face gauge
    sector, or the interacting tower.  Those are separate items and stay open.

STATUS: ✔✔
RUN: python3 C50_the_dirac_sector_propagates_and_its_chirality_is_the_twists_sign.py
ORIGIN: built r3802 (node 60), closing `WHAT_IS_UNFINISHED` B2 item 1 and this ledger's `P11` reach
row, which read "Levi-Civita connection implicit only".
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78

# =====================================================================================
# PART 1 — THE FRAME, AND THE TWIST IS A SPIN-CONNECTION COMPONENT
# =====================================================================================
print(BAR); print("PART 1 — THE FRAME ON P11's UNPOLARISED MEMBER, AND WHERE THE TWIST LIVES"); print(BAR)

t, z, x, y = sp.symbols('t z x y', real=True)
XC = [t, z, x, y]
kx, ky = sp.symbols('k_x k_y', real=True)
psi = sp.Function('psi')(t, z)
gma = sp.Function('gamma')(t, z)
omg = sp.Function('omega')(t, z)
Rf  = sp.Function('R')(t, z)
A   = gma - psi

# coframe e^a_mu, rows a, cols mu -- P11 eq:unpolarized
E = sp.Matrix([[sp.exp(A), 0, 0, 0],
               [0, sp.exp(A), 0, 0],
               [0, 0, sp.exp(psi), sp.exp(psi)*omg],
               [0, 0, 0, Rf*sp.exp(-psi)]])
ETA = sp.diag(-1, 1, 1, 1)
gmet = sp.simplify(E.T*ETA*E)

# (A1) THE COFRAME RECONSTRUCTS P11's METRIC.  Everything below is read off this frame, so it is
#      checked before anything is read off it.
gP11 = sp.Matrix([[-sp.exp(2*A), 0, 0, 0],
                  [0, sp.exp(2*A), 0, 0],
                  [0, 0, sp.exp(2*psi), sp.exp(2*psi)*omg],
                  [0, 0, sp.exp(2*psi)*omg, Rf**2*sp.exp(-2*psi) + omg**2*sp.exp(2*psi)]])
assert sp.simplify(gmet - gP11) == sp.zeros(4), sp.simplify(gmet - gP11)
print("  the coframe reproduces P11 eq:unpolarized                          [exact]")

# CONTROL (A1c): the off-diagonal omega in e^2 is what makes the wave UNPOLARISED.  Drop it and the
# metric loses g_xy -- i.e. the control returns the POLARISED cut, which is a different geometry.
Ebad = E.copy(); Ebad[2, 3] = 0
gbad = sp.simplify(Ebad.T*ETA*Ebad)
assert sp.simplify(gbad - gP11) != sp.zeros(4)
assert sp.simplify(gbad[2, 3]) == 0 and sp.simplify(gP11[2, 3]) != 0
print("  CONTROL: dropping omega from e^2 kills g_xy -> the polarised cut   [fires]")

ginv = sp.simplify(gmet.inv())
CH = [[[sp.simplify(sum(ginv[a, d]*(sp.diff(gmet[d, b], XC[c]) + sp.diff(gmet[d, c], XC[b])
                                    - sp.diff(gmet[b, c], XC[d])) for d in range(4))/2)
        for c in range(4)] for b in range(4)] for a in range(4)]
Einv = sp.simplify(E.inv())

# omega_mu^a_b = e^a_nu ( d_mu e_b^nu + Gamma^nu_{mu s} e_b^s ), then lower the first index
SPIN = [[[0]*4 for _ in range(4)] for _ in range(4)]
for mu in range(4):
    for a in range(4):
        for b in range(4):
            s = 0
            for nu in range(4):
                term = sp.diff(Einv[nu, b], XC[mu])
                for si in range(4):
                    term += CH[nu][mu][si]*Einv[si, b]
                s += E[a, nu]*term
            SPIN[mu][a][b] = s
for mu in range(4):
    SPIN[mu] = [[sp.simplify(sum(ETA[a, c]*SPIN[mu][c][b] for c in range(4))) for b in range(4)]
                for a in range(4)]

# (A2) the metric connection is antisymmetric in its frame indices -- the check that it IS a spin
#      connection and not an arbitrary matrix of functions.
for mu in range(4):
    for a in range(4):
        for b in range(4):
            assert sp.simplify(SPIN[mu][a][b] + SPIN[mu][b][a]) == 0, (mu, a, b)
print("  omega_{mu ab} = -omega_{mu ba} in all 64 components                [exact]")

# ---- THE RESULT: the twist IS the (23) block ----------------------------------------
P_wm = 2*psi - sp.log(Rf)                 # P11 eq:wavemapvars
c_t  = Rf*sp.exp(2*P_wm)*sp.diff(omg, t)  # P11 eq:twist, the conserved charge
c_z  = Rf*sp.exp(2*P_wm)*sp.diff(omg, z)

# (A3) THE IDENTIFICATION, asserted as exact symbolic zeros.
assert sp.simplify(SPIN[0][2][3] + c_t*sp.exp(-2*psi)/2) == 0
assert sp.simplify(SPIN[1][2][3] + c_z*sp.exp(-2*psi)/2) == 0
print("  ** omega_{t,23} = -(1/2) c   e^{-2psi}   [P11's conserved twist]   [exact]")
print("  ** omega_{z,23} = -(1/2) c_z e^{-2psi}                            [exact]")

# CONTROL (A3c): the coefficient is 1/2 and the test can tell.  1/3 must FAIL.
assert sp.simplify(SPIN[0][2][3] + c_t*sp.exp(-2*psi)/3) != 0
print("  CONTROL: the same identity with 1/3 in place of 1/2 is FALSE       [fires]")

# (A4) and the (23) block is the ONLY place the second polarisation's rate enters the connection's
#      transverse rotation: at omega == 0 -- P11's polarised, achiral cut -- it vanishes entirely.
_pol = {omg: sp.Integer(0)}
for mu in range(4):
    assert sp.simplify(SPIN[mu][2][3].subs(sp.Derivative(omg, t), 0)
                       .subs(sp.Derivative(omg, z), 0).subs(_pol)) == 0, mu
print("  at Q = omega = 0 (the polarised cut) the whole (23) block vanishes [exact]")

# =====================================================================================
# PART 2 — SEPARATION, THE FRICTION, AND THE EXACT CLIFFORD FORM
# =====================================================================================
print(); print(BAR); print("PART 2 — THE DIRAC OPERATOR SEPARATED, AND WHAT IS LEFT"); print(BAR)

I2 = sp.eye(2); Z2 = sp.zeros(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
GA = [blk(Z2, I2, -I2, Z2)] + [blk(Z2, s, s, Z2) for s in (sx, sy, sz)]   # chiral rep, mostly plus
G5 = sp.simplify(sp.I*GA[0]*GA[1]*GA[2]*GA[3])

# the algebra the whole reduction rests on
for a in range(4):
    for b in range(4):
        assert sp.simplify(GA[a]*GA[b] + GA[b]*GA[a] - 2*ETA[a, b]*sp.eye(4)) == sp.zeros(4), (a, b)
assert sp.simplify(G5*G5) == sp.eye(4)
assert all(sp.simplify(G5*GA[a] + GA[a]*G5) == sp.zeros(4) for a in range(4))
assert sp.simplify(G5 - sp.diag(-1, -1, 1, 1)) == sp.zeros(4)
print("  {gamma^a, gamma^b} = 2 eta^{ab}; gamma^5 = diag(-1,-1,1,1)         [exact]")

SCON = []
for mu in range(4):
    M = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            if a != b:
                M += sp.Rational(1, 4)*SPIN[mu][a][b]*GA[a]*GA[b]
    SCON.append(sp.simplify(M))

# psi_spinor = exp(i kx x + i ky y) chi(t,z):  Dt d_t chi + Dz d_z chi + MM chi = 0
Dt = sp.zeros(4); Dz = sp.zeros(4); MM = sp.zeros(4)
for a in range(4):
    for mu in range(4):
        ea = Einv[mu, a]
        if ea == 0:
            continue
        if mu == 0: Dt += GA[a]*ea
        if mu == 1: Dz += GA[a]*ea
        if mu == 2: MM += GA[a]*ea*sp.I*kx
        if mu == 3: MM += GA[a]*ea*sp.I*ky
        MM += GA[a]*ea*SCON[mu]
Dt = sp.simplify(Dt); Dz = sp.simplify(Dz); MM = sp.simplify(MM)
assert sp.simplify(Dt - sp.exp(-A)*GA[0]) == sp.zeros(4)
assert sp.simplify(Dz - sp.exp(-A)*GA[1]) == sp.zeros(4)
print("  the principal part is exactly e^{-A}(gamma^0 d_t + gamma^1 d_z)    [exact]")

# ---- the rescaling that removes the friction ----------------------------------------
OM = sp.exp(-A/2)/sp.sqrt(Rf)
MP = sp.simplify(MM + Dt*sp.diff(OM, t)/OM + Dz*sp.diff(OM, z)/OM)

def _derivs_of(expr, fn):
    return [d for d in expr.atoms(sp.Derivative) if d.expr == fn]

# (A5) EVERY background-derivative term is gone -- gamma, psi and R derivatives all cancel.
for fn, nm in ((gma, 'gamma'), (psi, 'psi'), (Rf, 'R')):
    hits = [d for i in range(4) for j in range(4) for d in _derivs_of(sp.expand(MP[i, j]), fn)]
    assert hits == [], (nm, hits)
print("  after chi = Omega^{-1} psi with Omega = e^{-A/2} R^{-1/2}:")
print("    no derivative of gamma, psi or R survives anywhere in M'         [exact]")
# and what DOES survive is the twist -- omega's derivatives, which is the content.
assert any(_derivs_of(sp.expand(MP[i, j]), omg) for i in range(4) for j in range(4))
print("    what survives is d(omega) -- the twist -- and the momenta        [exact]")

# CONTROL (A5c): the R^{-1/2} half is load-bearing.  Drop it and R-derivatives come back.
OMbad = sp.exp(-A/2)
MPbad = sp.simplify(MM + Dt*sp.diff(OMbad, t)/OMbad + Dz*sp.diff(OMbad, z)/OMbad)
assert any(_derivs_of(sp.expand(MPbad[i, j]), Rf) for i in range(4) for j in range(4))
print("  CONTROL: Omega without R^{-1/2} leaves R-derivatives standing      [fires]")

# ---- THE RESULT: four terms, and the twist is an axial vector ------------------------
m_x = sp.exp(A - psi)*kx
m_y = sp.exp(A + psi)*(ky - kx*omg)/Rf
b_z = c_t*sp.exp(-2*psi)/4        # along z, built from d_t omega
b_t = c_z*sp.exp(-2*psi)/4        # along t, built from d_z omega
CLAIM = sp.I*m_x*GA[2] + sp.I*m_y*GA[3] + sp.I*b_z*G5*GA[1] + sp.I*b_t*G5*GA[0]

# (A6) THE EXACT MATRIX IDENTITY.
assert sp.simplify(sp.exp(A)*MP - CLAIM) == sp.zeros(4)
print()
print("  ** e^A M' = i m_x g^2 + i m_y g^3 + i b_z g^5 g^1 + i b_t g^5 g^0  [exact] **")
print("     m_x = e^{A-psi} k_x     m_y = e^{A+psi}(k_y - k_x omega)/R")
print("     b_z = c   e^{-2psi}/4   b_t = c_z e^{-2psi}/4")
print("     => THE TWIST ENTERS ONLY ON gamma^5 -- an AXIAL vector, chirality-odd.")

# CONTROL (A6c): the 1/4 is measured, not fitted -- 1/3 must fail.
assert sp.simplify(sp.exp(A)*MP - (sp.I*m_x*GA[2] + sp.I*m_y*GA[3]
                                   + sp.I*(c_t*sp.exp(-2*psi)/3)*G5*GA[1]
                                   + sp.I*b_t*G5*GA[0])) != sp.zeros(4)
print("  CONTROL: the same identity with c/3 in place of c/4 is FALSE       [fires]")

# (A7) and the rescaling factor IS the leaf's own volume element -- used in PART 5.
sqrt_h = sp.exp(A)*Rf                      # sqrt(det of the spatial 3-metric)
sqrt_mg = sp.exp(2*A)*Rf                   # sqrt(-det g)
# squared, so no branch of the root has to be chosen for symbolic functions
assert sp.simplify(gmet.det() + sqrt_mg**2) == 0
assert sp.simplify(gmet[1:, 1:].det() - sqrt_h**2) == 0
assert sp.simplify(OM**2 - 1/sqrt_h) == 0
print("  Omega^2 = 1/sqrt(h) exactly, and sqrt(-g) = e^{2A} R               [exact]")

# =====================================================================================
# PART 3 — THE BACKGROUND IS A GENUINE VACUUM-LAMBDA MEMBER
# =====================================================================================
print(); print(BAR); print("PART 3 — THE BACKGROUND, AND THAT IT SOLVES EINSTEIN'S EQUATIONS"); print(BAR)

Lm = sp.symbols('Lambda', positive=True)
ph = sp.Function('psi')(t); gh = sp.Function('gamma')(t)
oh = sp.Function('omega')(t); Rh = sp.Function('R')(t)
gH = sp.Matrix([[-sp.exp(2*(gh-ph)), 0, 0, 0], [0, sp.exp(2*(gh-ph)), 0, 0],
                [0, 0, sp.exp(2*ph), sp.exp(2*ph)*oh],
                [0, 0, sp.exp(2*ph)*oh, Rh**2*sp.exp(-2*ph) + oh**2*sp.exp(2*ph)]])
giH = gH.inv()
CHH = [[[sp.simplify(sum(giH[a, d]*(sp.diff(gH[d, b], XC[c]) + sp.diff(gH[d, c], XC[b])
                                    - sp.diff(gH[b, c], XC[d])) for d in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]
def _riem(a, b, c, d):
    e = sp.diff(CHH[a][b][d], XC[c]) - sp.diff(CHH[a][b][c], XC[d])
    return e + sum(CHH[a][c][s]*CHH[s][b][d] - CHH[a][d][s]*CHH[s][b][c] for s in range(4))
RicH = sp.Matrix(4, 4, lambda b, d: sp.simplify(sum(_riem(a, b, a, d) for a in range(4))))
RsH = sp.simplify(sum(giH[a, b]*RicH[a, b] for a in range(4) for b in range(4)))
EinH = sp.simplify(RicH - RsH*gH/2 + Lm*gH)

Rd = sp.Derivative(Rh, t); pd = sp.Derivative(ph, t)
od = sp.Derivative(oh, t); gd = sp.Derivative(gh, t)
N2 = sp.exp(2*(gh - ph))
Rdd_e  = 2*Lm*Rh*N2                                   # the area equation
odd_e  = od*(Rd/Rh - 4*pd)                            # equivalent to c = const
gd_e   = (Rh/Rd)*(Lm*N2 + pd**2 + sp.exp(4*ph)*od**2/(4*Rh**2))   # the [00] constraint
Pdd_e  = (sp.exp(4*ph)*od**2/Rh - Rd*(2*pd - Rd/Rh))/Rh           # P11 eq:wmP, homogeneous
pdd_e  = (Pdd_e + Rdd_e/Rh - (Rd/Rh)**2)/2
gdd_e  = sp.diff(gd_e, t).subs({sp.Derivative(ph, (t, 2)): pdd_e,
                                sp.Derivative(Rh, (t, 2)): Rdd_e,
                                sp.Derivative(oh, (t, 2)): odd_e}).subs(gd, gd_e)
SUBS = [(sp.Derivative(gh, (t, 2)), gdd_e), (sp.Derivative(ph, (t, 2)), pdd_e),
        (sp.Derivative(Rh, (t, 2)), Rdd_e), (sp.Derivative(oh, (t, 2)), odd_e), (gd, gd_e)]

# (A8) ALL FIVE NONZERO COMPONENTS OF G + Lambda g VANISH IDENTICALLY ON THE ODE SYSTEM.
nz = 0
for a in range(4):
    for b in range(a, 4):
        v = EinH[a, b]
        if v == 0:
            continue
        nz += 1
        for _ in range(3):
            v = v.subs(SUBS)
        assert sp.simplify(sp.expand(sp.powsimp(v, force=True))) == 0, (a, b)
assert nz == 5
print("  all five nonzero components of G_munu + Lambda g_munu vanish")
print("  identically on the integrated system                              [exact]")

# CONTROL (A8c): break the [00] constraint by a factor and [00] no longer vanishes.
v = EinH[0, 0]
for _ in range(3):
    v = v.subs([(sp.Derivative(gh, (t, 2)), gdd_e), (sp.Derivative(ph, (t, 2)), pdd_e),
                (sp.Derivative(Rh, (t, 2)), Rdd_e), (sp.Derivative(oh, (t, 2)), odd_e),
                (gd, 2*gd_e)])
assert sp.simplify(sp.expand(v)) != 0
print("  CONTROL: doubling gamma_t breaks the [00] component                [fires]")

# =====================================================================================
# PART 4/5/6 — NUMERICS: PROPAGATION, THE NORM, AND THE CHIRALITY LOCK
# =====================================================================================
LAM = 0.3
nI2 = np.eye(2); nZ2 = np.zeros((2, 2))
nsx = np.array([[0, 1], [1, 0]], complex)
nsy = np.array([[0, -1j], [1j, 0]])
nsz = np.diag([1, -1]).astype(complex)
def nblk(a, b, c, d): return np.block([[a, b], [c, d]])
NG = [nblk(nZ2, nI2, -nI2, nZ2).astype(complex)] + [nblk(nZ2, s, s, nZ2) for s in (nsx, nsy, nsz)]
NG5 = 1j*NG[0] @ NG[1] @ NG[2] @ NG[3]
SIG = NG[0] @ NG[1]

def background(c, T=2.0):
    def rhs(_t, s):
        R_, Rd_, P_, Pd_, Q_, gm_ = s
        ps_ = 0.5*(P_ + np.log(R_)); n2 = np.exp(2*(gm_ - ps_)); psd_ = 0.5*(Pd_ + Rd_/R_)
        omd_ = c/(R_*np.exp(2*P_))
        return [Rd_, 2*LAM*R_*n2, Pd_, (c**2/(R_*np.exp(2*P_)) - Rd_*Pd_)/R_, omd_,
                (R_/Rd_)*(LAM*n2 + psd_**2 + np.exp(4*ps_)*omd_**2/(4*R_**2))]
    return solve_ivp(rhs, (0, T), [1.0, 0.30, 0.0, 0.10, 0.0, -0.4],
                     rtol=1e-12, atol=1e-14, dense_output=True)

def coeffs(o, tt, c, k_x=0.0, k_y=0.0):
    R_, Rd_, P_, Pd_, Q_, gm_ = o.sol(tt)
    ps_ = 0.5*(P_ + np.log(R_)); A_ = gm_ - ps_
    return (np.exp(A_ - ps_)*k_x, np.exp(A_ + ps_)*(k_y - k_x*Q_)/R_,
            c*np.exp(-2*ps_)/4, A_)

def evolve(c, k_x=0.0, k_y=0.0, T=2.0, N=256, L=20.0, k0=3.0, sig=1.5, spoil=0.0):
    o = background(c, T)
    zg = np.linspace(-L/2, L/2, N, endpoint=False)
    kk = 2*np.pi*np.fft.fftfreq(N, d=zg[1] - zg[0])
    env = np.exp(-(zg**2)/(2*sig**2))*np.exp(1j*k0*zg)
    vp = np.array([1, 1])/np.sqrt(2); vm = np.array([1, -1])/np.sqrt(2)
    chi = np.zeros((4, N), complex)
    chi[0:2, :] = np.outer(vm, env)      # L block, sigma_x = -1 -> right-mover
    chi[2:4, :] = np.outer(vp, env)      # R block, sigma_x = +1 -> right-mover
    def rhs(tt, yv):
        ch = yv.reshape(4, N)
        mx_, my_, b_, A_ = coeffs(o, tt, c, k_x, k_y)
        dz = np.fft.ifft(1j*kk*np.fft.fft(ch, axis=1), axis=1)
        eAM = 1j*mx_*NG[2] + 1j*my_*NG[3] + 1j*b_*(NG5 @ NG[1])
        # `spoil` adds a HERMITIAN piece to the generator.  Every physical term above is
        # anti-hermitian once multiplied through by gamma^0, which is what conserves the norm;
        # this one is not, so it must break the conservation or the check measures nothing.
        return (SIG @ dz + (NG[0] @ eAM) @ ch + spoil*ch).ravel()
    s = solve_ivp(rhs, (0, T), chi.ravel(), rtol=1e-11, atol=1e-13)
    return o, zg, kk, s, T

def measure(c, k_x=0.0, spoil=0.0):
    o, zg, kk, s, T = evolve(c, k_x=k_x, spoil=spoil)
    c0 = s.y[:, 0].reshape(4, -1); cT = s.y[:, -1].reshape(4, -1)
    n0 = float(np.sum(np.abs(c0)**2)); nT = float(np.sum(np.abs(cT)**2))
    d0 = np.sum(np.abs(c0)**2, 0); dT = np.sum(np.abs(cT)**2, 0)
    speed = (np.sum(zg*dT)/np.sum(dT) - np.sum(zg*d0)/np.sum(d0))/T
    j = int(np.argmin(np.abs(kk - 3.0)))
    F = lambda v: np.fft.fft(v)[j]
    phL = np.angle(F(cT[0])/F(c0[0])); phR = np.angle(F(cT[2])/F(c0[2]))
    rel = float(np.angle(np.exp(1j*(phR - phL))))
    ts = np.linspace(0, T, 4001)
    pred = float(2*np.trapezoid(np.array([coeffs(o, tt, c)[2] for tt in ts]), ts))
    return dict(drift=abs(nT/n0 - 1), speed=float(speed), rel=rel,
                pred=float(np.angle(np.exp(1j*pred)))), o, T

print(); print(BAR); print("PART 4 — DOES IT PROPAGATE?  (the question the open item asks)"); print(BAR)

# (A9) the characteristics are the light cone, and this does not depend on the twist or the momenta.
assert np.allclose(SIG, SIG.conj().T)
assert np.allclose(np.sort(np.linalg.eigvalsh(SIG)), [-1, -1, 1, 1])
print("  Sigma = gamma^0 gamma^1 is hermitian with eigenvalues exactly +/-1")
print("  and the principal part carries NEITHER the twist NOR k_x, k_y")
print("  => the characteristics are the spacetime light cone, on the")
print("     inhomogeneous member as much as the homogeneous one.            [exact]")

m0, o0, T0 = measure(0.0)
m6, o6, T6 = measure(0.6)
mm6, _, _  = measure(-0.6)
mkx, _, _  = measure(0.6, k_x=0.9)
for lab, m in (("c=0    k_x=0  ", m0), ("c=+0.6 k_x=0  ", m6),
               ("c=-0.6 k_x=0  ", mm6), ("c=+0.6 k_x=0.9", mkx)):
    print(f"  {lab}  speed {m['speed']:+.6f}   norm drift {m['drift']:.2e}   "
          f"rel.phase {m['rel']:+.6f}   2*int b dt {m['pred']:+.6f}")

# (A10) the transverse zero mode moves at exactly the speed of light, twist or no twist.
for m in (m0, m6, mm6):
    assert abs(m['speed'] - 1.0) < 1e-4, m['speed']
print()
print("  ** the packet's centroid moves at speed 1.000000 -- IT PROPAGATES. **")

# CONTROL (A10c): the speed measurement CAN come out otherwise.  A transverse momentum is a mass on
# the reduction and must slow the packet BELOW the light speed, or "speed = 1" measures nothing.
assert mkx['speed'] < 0.99, mkx['speed']
assert 0.85 < mkx['speed'] < 1.0
print(f"  CONTROL: k_x = 0.9 is a mass and gives {mkx['speed']:.6f} < 1        [fires]")

# (A13) and nothing is trapped: on the homogeneous member the coefficients are z-independent, so the
#       operator commutes with translation in z and the packet leaves any bounded region.
assert abs(m6['speed']*T6) > 1.5
print("  the packet's displacement over the run is 2.0 in z -- no trapping  [measured]")

print(); print(BAR); print("PART 5 — THE NORM, WHICH P14 ESTABLISHED IS LOAD-BEARING"); print(BAR)
print("  P14: its wall mode is normalisable in the leaf's proper measure and")
print("  NOT in the conserved spacetime Dirac norm.  On THIS member:")
print()
print("    leaf proper measure : int |psi|^2 sqrt(h)   d^3x , sqrt(h)  = e^A R")
print("    conserved Dirac norm: int |psi|^2 sqrt(-g) e_0^t d^3x , sqrt(-g) = e^{2A} R")
print("    and e^{2A} R . e^{-A} = e^A R = sqrt(h)   -- the SAME density.")
print("    with psi = Omega chi and Omega^2 = 1/sqrt(h) both are int chi^+ chi dz.")
# (A14) the two densities coincide identically -- the lapse cancels, and Omega is the leaf's own factor
assert sp.simplify(sqrt_mg*sp.exp(-A) - sqrt_h) == 0
assert sp.simplify(OM**2*sqrt_h - 1) == 0
print()
print("  ** THE TWO NORMS ARE THE SAME INTEGRAL HERE.  THEY AGREE.         [exact] **")
print("     The reason is (A7): the factor that flattens the reduced operator")
print("     IS the leaf's own volume element.  P14's disagreement is at its")
print("     horizons, where its two measures diverge differently; this member")
print("     has none in the (t,z) sector -- the lapse e^A is finite and")
print("     nonvanishing throughout the evolved range.")
lap = np.array([np.exp(coeffs(o6, tt, 0.6)[3]) for tt in np.linspace(0, T6, 400)])
print(f"     lapse e^A over the run: min {lap.min():.4f}, max {lap.max():.4f}")
assert lap.min() > 0.1
# (A15) and the norm is conserved under the evolution, which is the numerical half of the same fact.
for m in (m0, m6, mm6, mkx):
    assert m['drift'] < 1e-9, m['drift']
print(f"  int chi^+ chi dz conserved to {max(m['drift'] for m in (m0, m6, mm6, mkx)):.1e} "
      f"under evolution        [measured]")

# CONTROL (A15c): a non-antihermitian term must break it, or conservation measures nothing.
msp, _, _ = measure(0.6, spoil=0.05)
assert msp['drift'] > 1e-3, msp['drift']
print(f"  CONTROL: a non-antihermitian term drifts by {msp['drift']:.2e}        [fires]")

print(); print(BAR); print("PART 6 — DOES THE CHIRALITY COUPLE TO THE SIGN OF c?"); print(BAR)

# (A17) at k_x = k_y = 0 the operator block-decouples on gamma^5, and the shifts are opposite.
E_, k_, B_ = sp.symbols('E k b', real=True)
OSym = -E_*GA[0] + k_*GA[1] + B_*G5*GA[1]
det = sp.factor(sp.simplify(OSym.det()))
assert sp.simplify(det - (E_**2 - (k_ - B_)**2)*(E_**2 - (k_ + B_)**2)) == 0
print("  det of the symbol at k_x=k_y=0 factorises as")
print("     (E^2 - (k-b)^2)(E^2 - (k+b)^2)                                  [exact]")
# and the two factors ARE the two chiralities: read the 2x2 blocks off directly.
top = sp.simplify(OSym[0:2, 2:4]); bot = sp.simplify(OSym[2:4, 0:2])
assert sp.simplify(top - (-E_*I2 + (k_ - B_)*sx)) == sp.zeros(2)
assert sp.simplify(bot - (+E_*I2 + (k_ + B_)*sx)) == sp.zeros(2)
print("  and the blocks are labelled by gamma^5 = diag(-1,-1,+1,+1):")
print("     ** E_R = +/-(k - b)     E_L = +/-(k + b)     b = c e^{-2psi}/4 **")
print("     -- opposite shifts.  c -> -c swaps them; gamma^5 swaps them;")
print("        the JOINT operation is the symmetry and neither half alone is.")

# CONTROL (A17c): at b = 0 the two chiralities are degenerate -- and that must be a DIFFERENT
# statement from the above, or the test is vacuous.
assert sp.simplify((det - (E_**2 - k_**2)**2).subs(B_, 0)) == 0
assert sp.simplify(det - (E_**2 - k_**2)**2) != 0
print("  CONTROL: at b = 0 the factors coincide, at b != 0 they do not      [fires]")

# (A19) MEASURED on the vacuum background: the relative phase is 2 int b dt.
assert abs(m6['rel'] - m6['pred']) < 1e-4, (m6['rel'], m6['pred'])
assert abs(mm6['rel'] - mm6['pred']) < 1e-4
print()
print(f"  measured relative phase, c=+0.6 : {m6['rel']:+.6f}   "
      f"against 2*int b dt = {m6['pred']:+.6f}")
# CONTROL (A20): it must be BIG, or agreeing with a prediction of zero proves nothing.
assert abs(m6['rel']) > 0.3
# CONTROL (A21): at c = 0 it must vanish, and it must reverse with the sign of c.
assert abs(m0['rel']) < 1e-9, m0['rel']
assert abs(m6['rel'] + mm6['rel']) < 1e-6
print(f"  CONTROL: c = 0 gives {m0['rel']:+.2e} and c -> -c reverses the sign  [fires]")

# (A22) THE HONEST BOUNDARY, MEASURED: transverse momentum breaks the lock, because m_x is a mass
#       and a mass breaks chirality.  The k_x = 0 result is about the transverse ZERO MODE.
assert abs(mkx['rel'] - mkx['pred']) > 1e-2, (mkx['rel'], mkx['pred'])
print(f"  BOUNDARY: at k_x = 0.9 the phase is {mkx['rel']:+.6f} against "
      f"{mkx['pred']:+.6f} --")
print("     the lock is EXACT in the transverse zero mode and broken by the")
print("     transverse momenta, which are exactly the terms that break")
print("     chirality.  The torus always carries k_x = k_y = 0.             [measured]")

print(); print(BAR)
print("""VERDICT.  ** The Dirac sector on P11's unpolarised Gowdy--de Sitter member is built, and the
open item's question has an answer: IT PROPAGATES. **  The characteristic cone is the light cone --
independent of the twist and of the transverse momenta -- so nothing binds, against P14's wall modes
which bind on a superpotential's sign change.  The leaf norm and the conserved spacetime Dirac norm
are the SAME integral here, because the factor that flattens the reduced operator is the leaf's own
volume element; P14's disagreement is at horizons this member does not have.

** And the payoff the item did not ask for.  ** P11's conserved twist is not merely analogous to the
fermion's chirality -- it IS a component of the spin connection the fermion moves in,
omega_{t,23} = -(1/2) c e^{-2psi}, and it enters the Dirac operator ONLY on gamma^5.  The two
chiralities carry opposite momentum shifts +/-b with b = c e^{-2psi}/4, so the orientation parity is
a symmetry only as the JOINT operation c -> -c with gamma^5 -> -gamma^5.
  ==> The graviton's handedness and the fermion's are ONE DATUM on this background -- which P11
      argued from two sectors agreeing, and which is here one field's own dispersion relation.""")
print(BAR)
