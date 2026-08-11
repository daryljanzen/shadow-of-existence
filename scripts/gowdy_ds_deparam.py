import sympy as sp
t,z,Lam=sp.symbols('t z Lambda',real=True)
# fields and their z-gradients as independent symbols for functional derivatives
psi,R,gam=sp.symbols('psi R gamma',real=True)
psiz,Rz,gamz=sp.symbols('psi_z R_z gamma_z',real=True)
Ppsi,Pgam,PR=sp.symbols('P_psi P_gamma P_R',real=True)

# Hamiltonian density from r162
Hd = Ppsi**2/(8*R) + 2*R*psiz**2 - sp.Rational(1,2)*Pgam*PR - 2*Rz*gamz + 2*Lam*R*sp.exp(2*(gam-psi))

# Hamilton velocities  q_t = dH/dp_q   (canonical pairs: (psi,Ppsi),(R,PR),(gamma,Pgam))
psi_t = sp.diff(Hd,Ppsi)
R_t   = sp.diff(Hd,PR)
gam_t = sp.diff(Hd,Pgam)
print("psi_t =",psi_t,"  R_t =",R_t,"  gam_t =",gam_t)
# matches momentum defs?  Ppsi=4R psi_t -> psi_t=Ppsi/4R ; PR=-2 gam_t ; Pgam=-2 R_t
print("check defs:  Ppsi-4R*psi_t =",sp.simplify(Ppsi-4*R*psi_t),
      "| PR+2*gam_t =",sp.simplify(PR+2*gam_t),"| Pgam+2*R_t =",sp.simplify(Pgam+2*R_t))

# Hamilton momenta  p_t = -(dHd/dq - d/dz dHd/dq_z).  Here d/dz acts on z-gradient pieces.
# Build functional derivative; the only q_z dependence: psiz (in 2R psiz^2), Rz & gamz (in -2 Rz gamz).
# delta/delta psi:
dHd_dpsi  = sp.diff(Hd,psi);   dHd_dpsiz = sp.diff(Hd,psiz)
dHd_dR    = sp.diff(Hd,R);     dHd_dRz   = sp.diff(Hd,Rz)
dHd_dgam  = sp.diff(Hd,gam);   dHd_dgamz = sp.diff(Hd,gamz)
print("\ndHd/dpsi_z =",dHd_dpsiz,"  dHd/dR_z =",dHd_dRz,"  dHd/dgam_z =",dHd_dgamz)
print("(so the d/dz pieces become: -(4R psi_z)_z for psi ; -(-2 gam_z)_z for R ; -(-2 R_z)_z for gamma)")

# Now reconstruct the time-evolution of the momenta in terms of the original t,z functions
# and check WAVE/AREA/gamma-eq.  Use functions of (t,z):
tt,zz=sp.symbols('t z',real=True)
PSI=sp.Function('psi')(tt,zz); GAM=sp.Function('gamma')(tt,zz); RR=sp.Function('R')(tt,zz)
sub={psi:PSI,R:RR,gam:GAM,psiz:sp.diff(PSI,zz),Rz:sp.diff(RR,zz),gamz:sp.diff(GAM,zz),
     Ppsi:4*RR*sp.diff(PSI,tt),Pgam:-2*sp.diff(RR,tt),PR:-2*sp.diff(GAM,tt)}

# p_psi_t = -(dHd/dpsi - d/dz dHd/dpsiz);  also p_psi=4R psi_t so p_psi_t = d/dt(4R psi_t)
lhs_ppsi = sp.diff(4*RR*sp.diff(PSI,tt),tt)
rhs_ppsi = -( dHd_dpsi.subs(sub) - sp.diff(dHd_dpsiz.subs(sub),zz) )
WAVE = sp.diff(RR*sp.diff(PSI,tt),tt)-sp.diff(RR*sp.diff(PSI,zz),zz)-Lam*RR*sp.exp(2*(GAM-PSI))
print("\nHAMILTON psi-eqn  (lhs-rhs)/4 - WAVE =", sp.simplify((lhs_ppsi-rhs_ppsi)/4 - WAVE))

# p_gamma_t : p_gamma=-2 R_t -> lhs=-2 R_tt ; rhs=-(dHd/dgam - d/dz dHd/dgamz)
lhs_pgam = sp.diff(-2*sp.diff(RR,tt),tt)
rhs_pgam = -( dHd_dgam.subs(sub) - sp.diff(dHd_dgamz.subs(sub),zz) )
AREA = sp.diff(RR,tt,tt)-sp.diff(RR,zz,zz)-2*Lam*RR*sp.exp(2*(GAM-PSI))
print("HAMILTON gamma-eqn -> AREA :  (lhs-rhs)/(-2) - AREA =", sp.simplify((lhs_pgam-rhs_pgam)/(-2) - AREA))

# p_R_t : p_R=-2 gam_t -> lhs=-2 gam_tt ; rhs=-(dHd/dR - d/dz dHd/dRz)
lhs_pR = sp.diff(-2*sp.diff(GAM,tt),tt)
rhs_pR = -( dHd_dR.subs(sub) - sp.diff(dHd_dRz.subs(sub),zz) )
gameq = sp.diff(GAM,tt,tt)-sp.diff(GAM,zz,zz)+sp.diff(PSI,tt)**2-sp.diff(PSI,zz)**2-Lam*sp.exp(2*(GAM-PSI))
print("HAMILTON R-eqn -> gamma-eq:  (lhs-rhs)/(-2) - gammaeq =", sp.simplify((lhs_pR-rhs_pR)/(-2) - gameq))
