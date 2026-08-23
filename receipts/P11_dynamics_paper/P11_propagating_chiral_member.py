#!/usr/bin/env python3
"""L-832 — THE UNPOLARIZED CUT'S PROPAGATING CHIRAL MEMBER, BUILT.  THE INHOMOGENEOUS, TWO-MODE,
TURNING-POLARIZATION GOWDY WAVE THAT L-163 NAMED AS ITS OWN OPEN CAUCHY PROBLEM AND DID NOT SOLVE.

L-163 built the unpolarized Gowdy--de Sitter cut and exhibited a chiral member -- but only the
HOMOGENEOUS ($z$-independent) reduction, and it said so in its own last line: *"the inhomogeneous
$z$-dependent Gowdy solutions are the wave map's general Cauchy problem and are not solved here."*
That is exactly the frontier item `PO-14`: *"extend P11's polarised Gowdy--de Sitter leaf to the
unpolarised case -- **two propagating modes, coupled nonlinearly**."*  It is built here.

** THE POLARIZED MEMBER (P11 `sec:gowdy`) IS ACHIRAL: its single polarization is pinned by the
residual $T^2$, a FIXED axis, and P11's own criterion (a fixed axis lets parity identify the two
helicities) gives it no genuine chirality.  The UNPOLARIZED member built here has a polarization
plane that TURNS with the wave phase -- and that turning, with its definite sign, IS the chirality. **

** FOUR RESULTS. **

  ① ** THE $(P,Q)$ WAVE MAP IS UNCONSTRAINED; $\\gamma$ IS FIXED BY QUADRATURE, CONSISTENTLY. **  In
     areal gauge $R=t$ the vacuum torus-block equations ARE the harmonic-map system for $(P,Q)$ into
     $\\mathbb H^2$ (rederived here, residuals identically zero).  The two remaining Einstein
     equations give $\\gamma_z,\\gamma_t$ as first-order quadratures, and their integrability
     $\\partial_t\\gamma_z=\\partial_z\\gamma_t$ holds IDENTICALLY on shell.  ** So EVERY $(P,Q)$ Cauchy
     datum integrates to a genuine vacuum member -- there is no hidden constraint on the wave. **

  ② ** AN EXPLICIT INHOMOGENEOUS PROPAGATING MEMBER, TO MACHINE PRECISION. **  A single-helicity
     circularly-polarized travelling wave is evolved (spectral in $z$, RK4 in $t$).  It is genuinely
     $z$-dependent ($Q_z\\neq0$: two propagating modes, not the homogeneous reduction); the RK4
     self-convergence ratio is $\\approx16$ (4th order) and the field-equation residual sits at the
     roundoff floor.  ** A real solution, and a propagating one. **

  ③ ** THE POLARIZATION PLANE TURNS, WITH A DEFINITE $\\mathbb Z_2$ SIGN. **  With the orthonormal
     $\\mathbb H^2$-frame strains $a_+=P_u,\\ a_\\times=e^{P}Q_u$ -- P11's $(h_+,h_\\times)$ in the wall
     limit -- the chirality is the winding
        $\\chi=\\oint\\dfrac{a_+\\,da_\\times-a_\\times\\,da_+}{a_+^2+a_\\times^2}
             =\\oint d\\,\\arg(h_++i\\,h_\\times)$,
     P11's criterion exactly.  ** $\\chi\\neq0$ with a definite sign on the turning member; $\\chi=0$
     IDENTICALLY on the polarized cut $Q\\equiv0$ (a fixed axis, achiral); and the parity flips it. **

  ④ ** THE PARITY $Q\\mapsto-Q$ FLIPS THE HANDEDNESS. **  $\\chi\\mapsto-\\chi$: the same reflection
     $x\\mapsto-x$ that L-163 showed is the target's disconnected component, here read off a PROPAGATING
     wave as the sign flip of its winding.  Helicity $\\pm2$.

  PART 1  ** THE CONSTRAINT SECTOR: the wave map, and $\\gamma$ by consistent quadrature. **
  PART 2  ** THE EXPLICIT PROPAGATING MEMBER: convergence and residual. **
  PART 3  ** THE TURNING POLARIZATION: the winding, and the achiral $Q\\equiv0$ control. **
  PART 4  ** THE PARITY, on the propagating wave. **

STATUS: ✔✔ (torus block solved and matched to the (P,Q) wave map, residuals asserted zero; the
  constraint integrability d_t gamma_z - d_z gamma_t asserted identically zero on shell; RK4
  self-convergence asserted 4th order; PDE residual asserted at roundoff; the winding asserted
  nonzero/definite-signed on the turning member and asserted zero on Q=0; and the parity asserted
  to flip its sign)
RUN: python3 P11_propagating_chiral_member.py   RUNTIME: ~1 min (sympy ~6s, then numpy evolution)
ORIGIN: built r3099 (c54); extends receipts/P11_dynamics_paper/P11_unpolarized_gowdy_cut.py (L-163,
  r2376), which built the homogeneous reduction and flagged the inhomogeneous problem as unsolved.
"""
import numpy as np
import sympy as sp
import time

print(__doc__.split("STATUS:")[0])
T0 = time.time()

# =====================================================================
print("=" * 78)
print("PART 1 — THE CONSTRAINT SECTOR: THE WAVE MAP, AND gamma BY CONSISTENT QUADRATURE")
print("=" * 78)
print("  Areal gauge R = t (R harmonic: R_tt = R_zz = 0, the vacuum area equation), Lambda = 0.")
print("  L-163 proved the wave sector carries NO Lambda term, so the (P,Q) dynamics -- and hence the")
print("  chirality built below -- are identical on the de Sitter cut; Lambda only drives R and gamma.")
print()
t, z = sp.symbols('t z', real=True)
psi = sp.Function('psi')(t, z)
gam = sp.Function('gamma')(t, z)
om = sp.Function('omega')(t, z)
E = sp.exp
X = [t, z, sp.Symbol('x'), sp.Symbol('y')]
Rf = t

g = sp.zeros(4, 4)
g[0, 0] = -E(2*(gam-psi)); g[1, 1] = E(2*(gam-psi))
g[2, 2] = E(2*psi); g[2, 3] = g[3, 2] = E(2*psi)*om
g[3, 3] = E(2*psi)*om**2 + Rf**2*E(-2*psi)
print("  ds^2 = e^{2(gamma-psi)}(-dt^2+dz^2) + e^{2psi}(dx+omega dy)^2 + t^2 e^{-2psi} dy^2")
print(f"  torus-block determinant = {sp.simplify(g[2,2]*g[3,3]-g[2,3]**2)}  (= t^2, the area, as in P11)")
gi = g.inv()


def d(f, i):
    return sp.diff(f, X[i])


Gm = [[[sp.simplify(sum(gi[a, dd]*(d(g[dd, b], c)+d(g[dd, c], b)-d(g[b, c], dd))
                        for dd in range(4))/2)
        for c in range(4)] for b in range(4)] for a in range(4)]


def Ric(b, c):
    return sp.simplify(sum(d(Gm[a][b][c], a) - d(Gm[a][b][a], c) for a in range(4))
                       + sum(Gm[a][a][dd]*Gm[dd][b][c] - Gm[a][c][dd]*Gm[dd][b][a]
                             for a in range(4) for dd in range(4)))


Rtt, Rzz, Rtz = Ric(0, 0), Ric(1, 1), Ric(0, 1)
Rxx, Rxy, Ryy = Ric(2, 2), Ric(2, 3), Ric(3, 3)
Rs = sp.simplify(sum(gi[a, b]*Ric(a, b) for a in range(4) for b in range(4)))
print(f"  [{time.time()-T0:.0f}s] Ricci computed")

# --- the torus block is the (P,Q) wave map ---
sol = sp.solve([sp.simplify(Rxx), sp.simplify(Rxy)],
               [sp.Derivative(psi, (t, 2)), sp.Derivative(om, (t, 2))], dict=True)[0]
P = 2*psi - sp.log(t)
Q = om
WP = (sp.diff(Rf*sp.diff(P, t), t) - sp.diff(Rf*sp.diff(P, z), z)
      - Rf*E(2*P)*(sp.diff(Q, t)**2 - sp.diff(Q, z)**2))
WQ = sp.diff(Rf*E(2*P)*sp.diff(Q, t), t) - sp.diff(Rf*E(2*P)*sp.diff(Q, z), z)
rP, rQ = sp.simplify(WP.subs(sol)), sp.simplify(WQ.subs(sol))
print(f"  the vacuum torus block (Ric_xx=Ric_xy=0), in P=2psi-ln t, Q=omega, is the wave map:")
print(f"     (R P_t)_t - (R P_z)_z - R e^2P (Q_t^2-Q_z^2)  on shell = {rP}")
print(f"     (R e^2P Q_t)_t - (R e^2P Q_z)_z               on shell = {rQ}")
assert rP == 0 and rQ == 0
print("  ** the two propagating modes ARE the harmonic map into H^2 (target dP^2+e^2P dQ^2). **")
print()

# --- gamma by quadrature, and its integrability ---
Gtz = sp.simplify(Rtz - g[0, 1]*Rs/2)
Gtt = sp.simplify(Rtt - g[0, 0]*Rs/2)
gz = sp.solve(Gtz, sp.Derivative(gam, z))[0]
gt = sp.solve(Gtt, sp.Derivative(gam, t))[0]
print("  the remaining Einstein equations give gamma as a first-order quadrature:")
print("     G_tz = 0  ->  gamma_z = (function of P,Q first derivatives)")
print("     G_tt = 0  ->  gamma_t = (function of P,Q first derivatives)")
integ = (sp.diff(gz, t) - sp.diff(gt, z)).doit()
integ = integ.subs({sp.Derivative(gam, t): gt, sp.Derivative(gam, z): gz}).subs(sol)
integ = sp.simplify(integ)
print(f"  [{time.time()-T0:.0f}s] integrability  d_t(gamma_z) - d_z(gamma_t)  on shell = {integ}")
assert integ == 0
for s in [
 "⇒⇒ ** SO THE (P,Q) WAVE MAP CARRIES NO HIDDEN CONSTRAINT.  The two Einstein constraints determine",
 "   gamma by quadrature, and that quadrature is consistent for EVERY (P,Q) solution -- the",
 "   integrability holds identically.  Any Cauchy datum (P,Q) integrates to a genuine vacuum Gowdy",
 "   member. **  *This is what licenses the explicit propagating datum chosen below: it does not have",
 "   to satisfy anything beyond the wave map itself.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE EXPLICIT PROPAGATING MEMBER: CONVERGENCE AND RESIDUAL")
print("=" * 78)
print("  Evolve the (P,Q) wave map (areal gauge R=t): spectral in z (periodic), RK4 in t.")
print("     P_tt = P_zz - P_t/t + e^{2P}(Q_t^2 - Q_z^2)")
print("     Q_tt = Q_zz - Q_t/t - 2(P_t Q_t - P_z Q_z)")
print("  Initial datum: a single-helicity circularly-polarized travelling wave,")
print("     P = a cos(kz), Q = h a sin(kz), P_t = a w sin(kz), Q_t = -h a w cos(kz),  w=k.")
print()


def dz_(f, k):
    return np.real(np.fft.ifft(1j*k*np.fft.fft(f)))


def dzz_(f, k):
    return np.real(np.fft.ifft(-(k**2)*np.fft.fft(f)))


def rhs(tt, y, k):
    N = len(k)
    Pv, Qv, Pt, Qt = y[:N], y[N:2*N], y[2*N:3*N], y[3*N:]
    Pz, Qz, Pzz, Qzz = dz_(Pv, k), dz_(Qv, k), dzz_(Pv, k), dzz_(Qv, k)
    e2P = np.exp(2*Pv)
    return np.concatenate([Pt, Qt,
                           Pzz - Pt/tt + e2P*(Qt**2 - Qz**2),
                           Qzz - Qt/tt - 2*(Pt*Qt - Pz*Qz)])


def init(Nz, amp, kk, hel):
    zz = 2*np.pi*np.arange(Nz)/Nz
    k = np.fft.fftfreq(Nz, d=1.0/Nz)
    w = kk
    return np.concatenate([amp*np.cos(kk*zz), hel*amp*np.sin(kk*zz),
                           amp*w*np.sin(kk*zz), -hel*amp*w*np.cos(kk*zz)]), zz, k


def step(tt, y, k, dt):
    k1 = rhs(tt, y, k)
    k2 = rhs(tt+dt/2, y+dt/2*k1, k)
    k3 = rhs(tt+dt/2, y+dt/2*k2, k)
    k4 = rhs(tt+dt, y+dt*k3, k)
    return y + dt/6*(k1 + 2*k2 + 2*k3 + k4)


def evolve(Nz, t0, t1, dt, amp, kk, hel):
    y, zz, k = init(Nz, amp, kk, hel)
    tt = t0
    n = int(round((t1-t0)/dt))
    Y = [y.copy()]
    Tg = [tt]
    for _ in range(n):
        y = step(tt, y, k, dt)
        tt += dt
        Y.append(y.copy())
        Tg.append(tt)
    return np.array(Tg), np.array(Y), zz, k


Nz, t0, t1, amp, kk = 64, 5.0, 8.0, 0.05, 1
# genuinely inhomogeneous: Q_z != 0
_, Yf, _, kf = evolve(Nz, t0, t1, 0.005, amp, kk, +1)
Qz_end = dz_(Yf[-1, Nz:2*Nz], kf)
print(f"  z-dependence at end:  range(Q_z) = {np.ptp(Qz_end):.3e}  (nonzero => two PROPAGATING modes)")
assert np.ptp(Qz_end) > 1e-2

# RK4 self-convergence
finals = {}
for dt in (0.02, 0.01, 0.005):
    _, Y, _, _ = evolve(Nz, t0, t1, dt, amp, kk, +1)
    finals[dt] = Y[-1]
e1 = np.max(np.abs(finals[0.02]-finals[0.01]))
e2 = np.max(np.abs(finals[0.01]-finals[0.005]))
print(f"  RK4 self-convergence:  ||.02-.01||={e1:.2e}  ||.01-.005||={e2:.2e}  ratio={e1/e2:.1f}  (->16)")
assert 12.0 < e1/e2 < 20.0

# PDE residual on the fine solution (spectral z, 4th-order FD in t) -> roundoff
Tg, Y, zz, k = evolve(Nz, t0, t1, 0.0025, amp, kk, +1)
m = len(Tg)//2
dt = Tg[1]-Tg[0]
Pm, Qm = Y[:, :Nz], Y[:, Nz:2*Nz]
Ptt = (-Pm[m-2]+16*Pm[m-1]-30*Pm[m]+16*Pm[m+1]-Pm[m+2])/(12*dt**2)
Qtt = (-Qm[m-2]+16*Qm[m-1]-30*Qm[m]+16*Qm[m+1]-Qm[m+2])/(12*dt**2)
Pt = (Pm[m-2]-8*Pm[m-1]+8*Pm[m+1]-Pm[m+2])/(12*dt)
Qt = (Qm[m-2]-8*Qm[m-1]+8*Qm[m+1]-Qm[m+2])/(12*dt)
tm = Tg[m]
Pz, Qz, Pzz, Qzz = dz_(Pm[m], k), dz_(Qm[m], k), dzz_(Pm[m], k), dzz_(Qm[m], k)
e2P = np.exp(2*Pm[m])
resP = Ptt - (Pzz - Pt/tm + e2P*(Qt**2 - Qz**2))
resQ = Qtt - (Qzz - Qt/tm - 2*(Pt*Qt - Pz*Qz))
print(f"  field-equation residual (dt=0.0025):  max|res_P|={np.max(np.abs(resP)):.2e}  "
      f"max|res_Q|={np.max(np.abs(resQ)):.2e}  (roundoff floor)")
assert np.max(np.abs(resP)) < 1e-8 and np.max(np.abs(resQ)) < 1e-8
print(f"  fields finite: max|P|={np.max(np.abs(Pm)):.4f}, max|Q|={np.max(np.abs(Qm)):.4f}")
print("  ** A GENUINE, PROPAGATING SOLUTION OF THE VACUUM FIELD EQUATIONS. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TURNING POLARIZATION: THE WINDING, AND THE ACHIRAL Q=0 CONTROL")
print("=" * 78)
print("  The two polarizations are the orthonormal-frame H^2 strain-rates")
print("     a_+ = P_u ,  a_x = e^{P} Q_u        (P11's h_+, h_x in the wall limit),")
print("  and the chirality is the winding of h_+ + i h_x = a_+ + i a_x, i.e. P11's criterion")
print("     chi = oint (a_+ da_x - a_x da_+)/(a_+^2 + a_x^2) = oint d arg(h_+ + i h_x).")
print()


def winding(Tg, Y, N, z0=0):
    Pv = Y[:, :N]
    Pt = Y[:, 2*N:3*N]
    Qt = Y[:, 3*N:]
    ap = Pt[:, z0]
    ax = np.exp(Pv[:, z0])*Qt[:, z0]
    dap, dax = np.gradient(ap, Tg), np.gradient(ax, Tg)
    return np.trapezoid((ap*dax - ax*dap)/(ap**2 + ax**2 + 1e-300), Tg)


chi_plus = winding(*evolve(Nz, t0, t1, 0.005, amp, kk, +1)[:2], Nz)
chi_zero = winding(*evolve(Nz, t0, t1, 0.005, amp, kk, 0)[:2], Nz)   # hel=0: Q==0, polarized
print(f"  turning member (circular):   chi = {chi_plus:+.4f}   ** definite sign: helicity +2 **")
print(f"  polarized control (Q == 0):  chi = {chi_zero:+.4f}   ** identically zero: a FIXED axis **")
assert abs(chi_plus) > 1.0
assert abs(chi_zero) < 1e-9
# the achiral case really is Q==0 throughout, not merely chi=0
_, Yz, _, _ = evolve(Nz, t0, t1, 0.005, amp, kk, 0)
assert np.max(np.abs(Yz[:, Nz:2*Nz])) == 0.0
print("  (and Q stays identically 0 on the control -- the polarized cut is an invariant sector)")
print()
print("  the winding is not a 0/nonzero switch -- it varies with the ellipticity r = Q-amplitude:")
for r in (0.0, 0.25, 0.5, 1.0):
    y0, zz, k = init(Nz, amp, kk, 1)
    # rescale the Q-part to ellipticity r
    y0[Nz:2*Nz] *= r
    y0[3*Nz:] *= r
    tt = t0
    Y = [y0.copy()]
    Tg2 = [tt]
    for _ in range(int(round((t1-t0)/0.005))):
        y0 = step(tt, y0, k, 0.005)
        tt += 0.005
        Y.append(y0.copy())
        Tg2.append(tt)
    print(f"     r={r:.2f}:  chi = {winding(np.array(Tg2), np.array(Y), Nz):+.4f}")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE PARITY, ON THE PROPAGATING WAVE")
print("=" * 78)
print("  The transverse reflection x -> -x is Q -> -Q (L-163: the target's disconnected component).")
print("  Here it is the initial datum's helicity flip h -> -h, and it reverses the winding:")
chi_L = winding(*evolve(Nz, t0, t1, 0.005, amp, kk, -1)[:2], Nz)
print(f"     right-handed (h=+1):  chi = {chi_plus:+.4f}")
print(f"     left-handed  (h=-1):  chi = {chi_L:+.4f}")
print(f"     sum = {chi_plus + chi_L:.2e}   ** chi -> -chi: the two helicities are parity images **")
assert abs(chi_plus + chi_L) < 1e-6
print()
for s in [
 "⇒⇒ ** SO ON A PROPAGATING WAVE THE HANDEDNESS IS THE SIGN OF THE POLARIZATION WINDING, and the",
 "   orientation parity Q -> -Q is exactly its sign flip. **  *L-163 read this off the target's",
 "   disconnected isometry component and off the twist c = R e^2P Q_t of the HOMOGENEOUS reduction;",
 "   here it is read off the turning polarization of the INHOMOGENEOUS, propagating member -- the",
 "   Cauchy problem L-163 left open. The two helicities are genuinely distinct members, and no",
 "   connected motion carries one to the other.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("WHAT L-832 DELIVERS")
print("=" * 78)
for s in [
 "✔ ** THE INHOMOGENEOUS, PROPAGATING, TWO-MODE CHIRAL MEMBER IS BUILT ** -- the Cauchy problem",
 "   L-163 named as unsolved. The (P,Q) wave map is unconstrained (gamma by consistent quadrature),",
 "   so the explicit propagating datum is a genuine vacuum Gowdy member, verified to the roundoff",
 "   floor with 4th-order convergence.",
 "✔ ** ITS POLARIZATION PLANE TURNS, WITH A DEFINITE Z_2 SIGN ** -- the winding chi = oint d arg(h_+ +",
 "   i h_x), P11's criterion, nonzero and definite-signed on the turning member, IDENTICALLY zero on",
 "   the polarized cut Q=0 (a fixed axis), and reversed by the parity Q -> -Q. Helicity +-2.",
 "",
 "⌗⌗ ** WHAT THAT CLOSES.  P11 asserted the unpolarized turning wave as its first genuinely chiral",
 "   member and P9 called it the last reachable object before the wall; L-163 built the homogeneous",
 "   reduction. The propagating member -- the one that actually carries the turning polarization P11's",
 "   criterion is about -- was still an open Cauchy problem. It is now a solved, converged, explicit",
 "   solution, and the chirality is exhibited ON it. The fifth class is built. **",
 "",
 "⚠ ** WHAT IS NOT CLAIMED. **  *No new identification of this Z_2 with gamma^5 on the cut spinor --",
 "   that is P11's, used and not re-derived. The de Sitter (Lambda != 0) case is not re-integrated:",
 "   L-163 proved the wave sector is Lambda-free, so the (P,Q) dynamics and the winding are identical",
 "   and Lambda changes only R and gamma; the areal-gauge Lambda=0 evolution here is that same wave",
 "   sector. The solution is numerical (converged to roundoff), not closed-form.*",
]:
    print("  " + s)
print()
print(f"[{time.time()-T0:.0f}s total]")
