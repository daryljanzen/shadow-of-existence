"""PEEB — THE PEEBLES IONISATION HISTORY ON THE SET RATE.
ZREC used Saha only: right shift, wrong absolute (1283 vs CAMB's 1090), because Saha has no
departure from equilibrium.  Peebles adds it -- and the departure is itself H-dependent, which is
exactly why it must be integrated on the construction's own rate rather than inherited.
Standard effective three-level hydrogen atom (Peebles 1968; Seager et al. fits)."""
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
Mpc=3.0856775814913673e22; G=6.67430e-11; mp=1.67262192e-27
kB=1.380649e-23; hbar=1.054571817e-34; cc=2.99792458e8; me=9.1093837e-31
sigT=6.6524587e-29; T0=2.7255
eV=1.602176634e-19; B1=13.598*eV; E21=10.198*eV; lam_a=121.5682e-9
def nH0(ombh2):
    rho_c=3*(100e3/Mpc)**2/(8*np.pi*G)
    return 0.76*ombh2*rho_c/mp                      # hydrogen only
def alphaB(T):                                       # case-B recombination, Seager fit [m^3/s]
    t=T/1e4
    return 1e-19*4.309*t**-0.6166/(1+0.6703*t**0.5300)
def betaB(T):
    # case-B: photoionisation from n=2, binding B1/4 = 3.4 eV.  ONE exponential, not two.
    return alphaB(T)*(me*kB*T/(2*np.pi*hbar**2))**1.5*np.exp(-B1/(4*kB*T))
def peebles(H_of_z, ombh2=0.0224, z_hi=2000., z_lo=600.):
    n0=nH0(ombh2)
    def rhs(z,y):
        xe=min(max(y[0],1e-12),1.0)
        T=T0*(1+z); nH=n0*(1+z)**3
        a=alphaB(T); b=betaB(T)
        # Peebles C factor
        K=lam_a**3/(8*np.pi*H_of_z(z))
        L2s=8.227
        C=(1+K*L2s*nH*(1-xe))/(1+K*(L2s+b)*nH*(1-xe))
        dxdt = -C*(a*xe**2*nH - b*(1-xe)*np.exp(-E21/(kB*T)))
        return [dxdt/(-(1+z)*H_of_z(z))]             # dx/dz
    # start in Saha equilibrium
    T=T0*(1+z_hi); nb=n0*(1+z_hi)**3
    r=(me*kB*T/(2*np.pi*hbar**2))**1.5*np.exp(-B1/(kB*T))/nb
    x0=(-r+np.sqrt(r**2+4*r))/2
    sol=solve_ivp(rhs,[z_hi,z_lo],[x0],method='LSODA',rtol=1e-6,atol=1e-10,dense_output=True)
    return sol, n0
print("="*80); print("PEEB — RECOMBINATION INTEGRATED ON EACH RATE"); print("="*80)
def H_CR(z): return 73.0*1e3/Mpc*np.sqrt(0.3066*(1+z)**3+1-0.3066)
def H_L(z):  return 67.4*1e3/Mpc*np.sqrt(0.307/(1+3403.6)*(1+z)**4+0.307*(1+z)**3+0.693)
out={}
for lab,Hf in [("LambdaCDM",H_L),("CR",H_CR)]:
    sol,n0=peebles(Hf)
    zg=np.linspace(700.,1950.,1200)
    xg=np.clip(sol.sol(zg)[0],0,1)
    ig=xg*n0*(1+zg)**3*sigT*cc/((1+zg)*np.array([Hf(z) for z in zg]))
    taug=np.concatenate([[0.],np.cumsum(0.5*(ig[1:]+ig[:-1])*np.diff(zg))])
    xe=lambda z: float(np.interp(z,zg,xg))
    tau=lambda z: float(np.interp(z,zg,taug))
    print(f"  {lab:10s}  x_e: 1200={xe(1200):.4f}  1100={xe(1100):.4f}  1000={xe(1000):.5f}  900={xe(900):.5f}")
    for zt in [1000,1050,1100,1150,1200,1400]:
        print(f"       tau({zt}) = {tau(zt):.3f}")
    try:
        zr=brentq(lambda z: tau(z)-1.0, 750., 1950.); out[lab]=zr
        print(f"       -> z(tau=1) = {zr:.1f}")
    except Exception as e:
        print("       bracket:", e); out[lab]=float('nan')
print(f"""
  *** LambdaCDM: {out['LambdaCDM']:.1f}   (CAMB's full treatment: 1089.9 -- agreement to {100*abs(out['LambdaCDM']-1089.9)/1089.9:.1f}%) ***
  *** CR:        {out['CR']:.1f} ***
      shift = {out['CR']-out['LambdaCDM']:+.1f}  ({100*(out['CR']/out['LambdaCDM']-1):+.3f}%)
  Saha-only (ZREC) gave a shift of -0.32%; the full Peebles integration gives {100*(out['CR']/out['LambdaCDM']-1):+.3f}%.
""")

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# Print-only receipt.  P15 sec:refit-bound cites it for exactly two numbers: the recombination
# redshift "moves by only -0.11%" on this construction's own rate, and "the same integration
# returns z_*=1091 on the radiation-included rate, against the 1090 of the standard treatment,
# which is the check that the ionisation history is being handled correctly."  Both pinned, so
# a change in the Peebles integration breaks the gate rather than the paper's sentence.
assert 'LambdaCDM' in out and 'CR' in out, "one of the two rates failed to bracket tau=1"
assert np.isfinite(out['LambdaCDM']) and np.isfinite(out['CR'])
assert abs(out['LambdaCDM'] - 1091.08) < 0.30, f"LCDM z(tau=1) = {out['LambdaCDM']}, receipt prints 1091.1"
assert abs(out['CR'] - 1089.92) < 0.30, f"CR z(tau=1) = {out['CR']}, receipt prints 1089.9"
# the validation against CAMB's full treatment (1089.9): agreement to 0.1%, the paper's "1091 vs 1090"
assert 100 * abs(out['LambdaCDM'] - 1089.9) / 1089.9 < 0.15, "the LCDM arm no longer reproduces CAMB to 0.1%"
# the shift itself -- the figure the paper quotes as -0.11%
_pct = 100 * (out['CR'] / out['LambdaCDM'] - 1)
assert abs(_pct - (-0.107)) < 0.005, f"shift = {_pct}%, paper says -0.11%"
assert _pct < 0.0, "the CR rate must recombine EARLIER, not later"
# and the point of the receipt: Peebles shrinks the Saha-only ZREC shift of -0.32% by ~3x
assert abs(_pct) < 0.32 / 2.0, f"the Peebles shift {_pct}% no longer sits well inside the Saha-only -0.32%"
print(f"  [assertions r2376+c54.160] 1091.08 / 1089.92, shift -0.107% (paper -0.11%): pinned.")
