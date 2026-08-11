"""UNC — QUANTIFYING WHAT WE DO NOT KNOW.  The prediction with an error budget.
Corrections folded in first:
  * the recombination WIDTH scales with the rate (A.22) -- so the thickness contributes ~nothing to
    the RATIO and the signature is carried by r_D essentially alone;
  * the l_D anchor affects only the ABSOLUTE r_D and cancels in the ratio -- it carries NO uncertainty
    into the prediction;
  * z_rec is now COMPUTED on the set rate through the Peebles equation (PEEB, r1956), which
    tightened its spread from the +/-1% guess this receipt originally carried to +/-0.11%.
    *** UPDATED r2052: the receipt had been left at the pre-PEEB budget while P15 carried the
    post-PEEB number, so the cited receipt did not reproduce the cited value. ***
ORIGIN: storyboard_receipts/UNC_error_budget.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458
def predict(H0=73.0, Om=0.3066, ombh2=0.0224, z_rec=1089.9, lstar=301.6):
    OL=1-Om; a_rec=1/(1+z_rec)
    Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rbf=lambda a: Rb_rec*(a/a_rec)
    H=lambda a: H0*np.sqrt(Om/a**3+OL)
    g=lambda a: (Rbf(a)**2/(1+Rbf(a))+8/9)/(6*(1+Rbf(a)))
    rs=lambda zs: quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1/(1+zs), a_rec, limit=250)[0]
    DM=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=250)[0]
    zs=brentq(lambda z: np.pi*DM/rs(z)-lstar, 1500., 60000.)
    I=quad(lambda a: g(a)/H(a), 1/(1+zs), a_rec, limit=250)[0]
    # LambdaCDM reference at ITS own best fit, same z_rec convention
    Oml=0.307; H0l=67.4; Orl=Oml/(1+3403.6)
    Hl=lambda a: H0l*np.sqrt(Orl/a**4+Oml/a**3+1-Oml)
    Il=quad(lambda a: g(a)/Hl(a), 1e-9, a_rec, limit=250)[0]
    rsl=quad(lambda a: c/(a**2*Hl(a)*np.sqrt(3*(1+Rbf(a)))), 1e-9, a_rec, limit=250)[0]
    return (np.sqrt(I/Il))/(rs(zs)/rsl), zs, rs(zs)
r0,zs0,rs0 = predict()
print("="*80); print("UNC — THE PREDICTION AND ITS ERROR BUDGET"); print("="*80)
print(f"\n  CENTRAL:  theta_D/theta_* ratio = {r0:.4f}  ({100*(r0-1):+.2f}%)   z_onset={zs0:.0f}  r_s={rs0:.2f}")
print(f"  (thickness now excluded -- A.22 showed it cancels; this is r_D alone)\n")
print(f"  {'source':30s} {'range':>22s} {'d(ratio)':>10s} {'% of central':>13s}")
print("  "+"-"*80)
budget=[]
for lab, kw, lo, hi in [
    ("H0 (SH0ES 73.0 +/- 1.0)","H0",72.0,74.0),
    ("Om (BAO fit, +/- 0.006)","Om",0.3006,0.3126),
    ("omega_b (BBN, +/- 0.0005)","ombh2",0.0219,0.0229),
    ("z_rec (Peebles, +/-0.11%)","z_rec",1088.7,1091.1),
    ("l_* (Planck, +/-0.1)","lstar",301.5,301.7)]:
    a=predict(**{kw:lo})[0]; b=predict(**{kw:hi})[0]
    d=abs(b-a)/2
    budget.append((lab,d))
    print(f"  {lab:30s} {f'{lo}..{hi}':>22s} {d:>10.5f} {100*d/(r0-1):>12.1f}%")
tot=np.sqrt(sum(d**2 for _,d in budget))
print("  "+"-"*80)
print(f"  {'QUADRATURE TOTAL':30s} {'':>22s} {tot:>10.5f} {100*tot/(r0-1):>12.1f}%")
print(f"\n  *** theta_D/theta_* = {100*(r0-1):+.2f}% +/- {100*tot:.2f}%  ***")
print(f"  i.e. a {100*(r0-1)/ (100*tot):.1f}-sigma effect against its own parameter uncertainty")

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# Print-only receipt.  P15 sec:refit-bound sets theta_D/theta_* = +13.96% +/- 0.89% in a
# displayed equation citing this receipt, and says the seam falls at z ~ 6.8e3 and that the
# budget is "dominated by the measurement of H0 itself".  Every one of those is pinned here.
assert abs(100 * (r0 - 1) - 13.96) < 0.02, f"theta_D/theta_* = {100*(r0-1)}%, the paper's displayed equation says +13.96%"
assert abs(100 * tot - 0.89) < 0.02, f"quadrature total = {100*tot}%, the paper's displayed equation says 0.89%"
assert abs(r0 - 1.1396) < 0.0005, f"central ratio = {r0}, receipt prints 1.1396"
assert abs(zs0 - 6761.0) < 2.0, f"z_onset = {zs0}, receipt prints 6761"
assert 6.7e3 < zs0 < 6.9e3, "the paper says the seam falls at z ~ 6.8e3"
assert abs(rs0 - 135.46) < 0.05, f"r_s = {rs0}, receipt prints 135.46"
# the significance the receipt closes on, and the paper's "an error budget dominated by H0"
assert abs((r0 - 1) / tot - 15.67) < 0.10, f"significance = {(r0-1)/tot}, receipt prints 15.7-sigma"
assert (r0 - 1) / tot > 10.0, "the signature must remain many-sigma against its own parameter spread"
_labels = [lab for lab, d in budget]
assert len(budget) == 5 and _labels[0].startswith("H0"), "the five budget lines must all be present, H0 first"
_dH0 = budget[0][1]
assert abs(_dH0 - 0.00781) < 0.0002, f"H0 contribution = {_dH0}, receipt prints 0.00781"
assert _dH0 > 1.5 * max(d for lab, d in budget[1:]), "H0 must DOMINATE the budget, as the paper states"
# the two contributions the paper says do not enter: z_rec and l_* are each sub-percent of central
for _lab, _d in budget[3:]:
    assert 100 * _d / (r0 - 1) < 1.0, f"{_lab} now carries {100*_d/(r0-1)}% of the central value"
print(f"\n  [assertions r2376+c54.160] +13.96% +/- 0.89%, z_onset 6761, r_s 135.46, 15.7-sigma, H0-dominated: pinned.")
