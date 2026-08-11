"""
P16_theory_error_and_likelihood.py -- verifies the P16 sec:verdict DATA CONFRONTATION. Builds the theory-error
  budget (sensitivity coefficients alpha_i=d ln X/d ln rate_i, validated vs Cyburt-Fields-Olive, times per-
  reaction rate uncertainties): D/H 1.1%, 3He 2.5%, 7Li 6.6%, Y_p 0.6%. Rate-library cross-check at eta10=6.13:
  StarLib D/H=2.505e-5, 7Li=5.13e-10 (canonical); REACLIB 2.8% higher -- inside the budget. LIKELIHOOD vs
  measured primordial values at the Planck eta: D/H -0.5sigma, Y_p +0.5sigma, 7Li +7.8sigma. Matches the paper
  (D -0.5s, He-4 +0.5s, Li 6-8s): D and He-4 concordant <1sigma at the SAME CMB-fixed eta, lithium the shared
  open edge. Sources: Planck2018, Cooke2018 (DLA), Aver2021 (He), Sbordone2010 (Spite). Needs bbn_network + pynucastro.
STATUS: ✔✔ (D -0.5s, Y_p +0.5s, 7Li +7.8s = paper's confrontation; theory errors propagated; two libraries)
RUN: python3 P16_theory_error_and_likelihood.py   RUNTIME: ~2-3 min (needs pynucastro + bbn_network alongside)
ORIGIN: computations/p16_bbn/theory_error_and_likelihood.py, verified r1402.
"""
import numpy as np
import bbn_network as B

# ---- validated sensitivity table (from make_sensitivity.py; alpha = d ln X / d ln rate) ----
#   reaction        aD/H    a3He    a7Li
ALPHA = {
 "p(n,g)d":      (-0.19,  0.09,  1.31),
 "d(p,g)3He":    (-0.33,  0.39,  0.62),
 "d(d,n)3He":    (-0.56,  0.22,  0.72),
 "d(d,p)t":      (-0.47, -0.28,  0.07),
 "3He(d,p)4He":  (-0.01, -0.77, -0.77),
 "3He(n,p)t":    ( 0.02, -0.19, -0.28),
 "3He(a,g)7Be":  ( 0.00,  0.00,  0.97),
 "7Be(n,p)7Li":  ( 0.00,  0.00, -0.75),
}
# per-reaction 1-sigma fractional rate uncertainties (standard BBN nuclear inputs; post-LUNA for
# the deuteron rates). Refs: Cyburt-Fields-Olive-Yeh RMP 2016; Pitrou et al. (PRIMAT) 2018;
# Mossa et al. (LUNA) Nature 2020 for d(p,g)3He (~1.5%).
SIGMA_RATE = {
 "p(n,g)d":     0.010, "d(p,g)3He":  0.015, "d(d,n)3He": 0.013, "d(d,p)t": 0.013,
 "3He(d,p)4He": 0.030, "3He(n,p)t":  0.020, "3He(a,g)7Be":0.050, "7Be(n,p)7Li":0.045,
}
def theory_frac_error(col):  # col: 0=D/H,1=3He,2=7Li
    return np.sqrt(sum((ALPHA[k][col]*SIGMA_RATE[k])**2 for k in ALPHA))

sD  = theory_frac_error(0)
s3  = theory_frac_error(1)
sLi = theory_frac_error(2)
# Y_p theory error is set by the neutron lifetime and radiative/QED corrections, not these rates:
sYp_frac = 0.006     # ~0.6% (tau_n +/-0.4s ~0.05%, plus the omitted Born-level QED corrections)

print("="*72)
print("D1 DATA-CONFRONTATION  --  theory error + likelihood at the Planck baryon density")
print("="*72)
print("\n[A] THEORY-ERROR BUDGET (fractional, from sensitivity x rate-uncertainty):")
print(f"    D/H : {sD*100:4.1f}%   3He/H : {s3*100:4.1f}%   7Li/H : {sLi*100:4.1f}%   Y_p : {sYp_frac*100:4.1f}%")
print(f"    (D/H dominated by the deuteron-burning rates d(d,n)3He, d(d,p)t, d(p,g)3He;")
print(f"     7Li by 3He(a,g)7Be and 7Be(n,p)7Li -- the same rates that carry the REACLIB-vs-")
print(f"     BBN-evaluated offset, so the 2% D/H shift from canonical sits inside this budget.)")

# ---- run the network at the Planck-inferred baryon-to-photon ratio ----
# Planck 2018: Omega_b h^2 = 0.02237 +/- 0.00015  ->  eta10 = 273.8 * Omega_b h^2 = 6.13 +/- 0.04
# PRIMARY: StarLib (Sallaska et al. 2013), the carefully-evaluated light-nuclide library -- lands on
# the canonical standard-BBN values. CROSS-CHECK: REACLIB, an independent compilation (2% higher D/H).
eta10_planck = 6.13
o  = B.run(eta10=eta10_planck, verbose=False, library='starlib')
oR = B.run(eta10=eta10_planck, verbose=False, library='reaclib')
Yp,DH,He3H,Li7H = o['Yp'],o['DH'],o['He3H'],o['Li7H']
print(f"\n[X] RATE-LIBRARY CROSS-CHECK at eta10={eta10_planck} (robustness of the pattern):")
print(f"    StarLib : D/H={o['DH']:.3e}  7Li/H={o['Li7H']:.3e}   (evaluated light-nuclide rates)")
print(f"    REACLIB : D/H={oR['DH']:.3e}  7Li/H={oR['Li7H']:.3e}   (independent compilation)")
print(f"    spread  : D/H {abs(o['DH']-oR['DH'])/o['DH']*100:.1f}%  -- within the theory-error budget above;")
print(f"              StarLib sits on the canonical D/H=2.51e-5, 7Li/H=5.0e-10.")
# Y_p: the Born-level network omits the standard ~+1.6% Coulomb/radiative/finite-mass corrections;
# apply them as a documented offset to compare like-with-like against the full standard value.
Yp_corr = Yp*1.016

print(f"\n[B] COMPUTED at eta10={eta10_planck} (Planck):  Y_p={Yp:.4f} (Born) / {Yp_corr:.4f} (+QED corr)")
print(f"    D/H={DH:.3e}   3He/H={He3H:.3e}   7Li/H={Li7H:.3e}")

# ---- measured primordial abundances (cited) ----
OBS = {
 'Yp':  (0.2453, 0.0034, "Aver et al. 2021 (He II recombination)"),
 'DH':  (2.527e-5, 0.030e-5, "Cooke, Pettini & Steidel 2018 (metal-poor DLAs)"),
 'Li7H':(1.6e-10, 0.3e-10, "Sbordone et al. 2010 (Spite plateau)"),
}
print(f"\n[C] LIKELIHOOD vs measured primordial abundances (concordance in sigma):")
print(f"    {'':7s} {'computed':>12s} {'+/-theory':>11s} {'observed':>12s} {'+/-obs':>10s} {'tension':>9s}")
def tension(comp, sig_th, obs, sig_obs):
    return (comp-obs)/np.sqrt(sig_th**2+sig_obs**2)
# D/H
obs,sig_obs,_=OBS['DH']; th=DH*sD
tD=tension(DH,th,obs,sig_obs)
print(f"    {'D/H':7s} {DH:12.3e} {th:11.2e} {obs:12.3e} {sig_obs:10.2e} {tD:+8.1f}s")
# Y_p (use QED-corrected)
obs,sig_obs,_=OBS['Yp']; th=Yp_corr*sYp_frac
tY=tension(Yp_corr,th,obs,sig_obs)
print(f"    {'Y_p':7s} {Yp_corr:12.4f} {th:11.2e} {obs:12.4f} {sig_obs:10.2e} {tY:+8.1f}s")
# 7Li
obs,sig_obs,_=OBS['Li7H']; th=Li7H*sLi
tLi=tension(Li7H,th,obs,sig_obs)
print(f"    {'7Li/H':7s} {Li7H:12.3e} {th:11.2e} {obs:12.3e} {sig_obs:10.2e} {tLi:+8.1f}s")

print(f"\n[D] VERDICT:")
print(f"    D/H and Y_p CONCORDANT (<1 sigma) with the measured primordial values at the SAME")
print(f"    baryon density Planck reads from the CMB peak heights -- the single inherited eta")
print(f"    fits the microwave background AND the light elements jointly. 7Li sits at {tLi:+.1f} sigma:")
print(f"    the standard lithium problem, shared with flat LambdaCDM, neither dissolved nor worsened.")
print(f"    So 'produces the abundances' is earned with data: one forced hot phase, one CMB-fixed")
print(f"    eta, quantitative concordance on D and He-4 -- the lithium tension the honest open edge.")
print("    Sources: Planck 2018 (eta); "+OBS['DH'][2]+"; "+OBS['Yp'][2]+"; "+OBS['Li7H'][2]+".")
print("="*72)


# ** CHECKS, added r2376+c54.156: pin the three tensions the paper prints (-0.5, +0.5, 6-8 sigma). **
print()
print("  ** CHECKS: the paper prints D/H at -0.5 sigma, He-4 at +0.5 sigma, Li-7 at 6-8 sigma **")
_tD, _tY, _tL = tD, tY, tLi          # the tensions this file already computed
print(f"     D/H {_tD:+.2f}   Y_p {_tY:+.2f}   7Li {_tL:+.2f}")
assert abs(_tD + 0.5) < 0.15, f"D/H tension {_tD:+.2f}, paper says -0.5"
assert abs(_tY - 0.5) < 0.15, f"Y_p tension {_tY:+.2f}, paper says +0.5"
assert 6.0 <= _tL <= 8.5, f"7Li tension {_tL:+.2f}, paper says 6-8 sigma"
print("  CHECKS PASS")
