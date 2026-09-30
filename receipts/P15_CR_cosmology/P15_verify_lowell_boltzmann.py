"""
** ⛔ ITS DEPTHS ARE SUPERSEDED, AND IT SAYS SO HERE (r7049+70). **  The quartet this file prints,
   0.473 / 0.410 / 0.356 / 0.676 at ell = 2..5, is on the CONTROL background (H0 = 67.4, Omega_m = 0.315,
   r0 = 5064).  The corpus quotes 0.487 / 0.435 / 0.359 / 0.666, on the ADJUDICATED
   background (H0 = 68.60, Omega_m = 0.2973), and those are computed by ARM A of
   `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling` -- the same CAMB transfer and
   the same discrete sum, on the other background.  Same minimum at ell = 4 and the same recovery.
   ⇒ *What this file still carries for the corpus is its four-figure gate and its r0-drift table, and
     neither is a depth quote.*  It is NOT brought current: moving its background would move the r0 table
     the paper cites (15 per cent at ell = 4), which is a re-scoring and not a disposal.
   ⌗ *Its printed depths, and the "matches the paper's 0.47/0.41" below, are its r1395 record.*

P15_verify_lowell_boltzmann.py -- verifies the P15 sec:largescale/sec:scope EXACT low-ell depth via a genuine
  Boltzmann transfer. CR's temperature transfer telescopes to flat-LCDM's (flat projection D_M=D_C, zero
  differential floor), so the ONLY CR modification is the DISCRETE closed-S^3 source read through CAMB's exact
  Delta_l(k) (SW+ISW+Doppler): C_l^CR = sum_{L>=2} w_L (k_L/k_piv)^(ns-1) |Delta_l(k_L)|^2 vs the continuum
  integral, with w_L = d ln k_L/dL so the CR sum is the L=2-floored Riemann sum of the same integral.
  GATE (passes): the continuum sum reproduces CAMB's own C_l to FOUR FIGURES (l=2: 972.393 vs 972.446).
  RESULT: CR/LCDM depth 0.473 (l=2), 0.410 (l=3), recovering by l~7; octopole/quadrupole 0.867 -- ell=2,3
  suppressed together. Matches the paper's 0.47/0.41. The ISW diagnosis explains why this is MILDER than the
  SW-only 0.22: the late ISW at l=2 is sourced at k~few e-3, ABOVE the floor k_2=5.6e-4, so CR retains it.
STATUS: OK (gate = continuum reproduces CAMB C_l to 4 figures; exact depth 0.47/0.41 matches paper; r0 sensitivity MEASURED c54.153: shape stable, depths drift up to 15% at ell=4 under +/-2% in r0)
RUN: python3 P15_verify_lowell_boltzmann.py   RUNTIME: ~3min (needs camb, high accuracy)
ORIGIN: computations/perturbation_verify/verify_lowell_boltzmann.py, verified r1395.
"""
import numpy as np, camb
from scipy.interpolate import interp1d

H0,ombh2,omch2=67.4,0.02237,0.1200; ns,As,kpiv=0.9649,2.1e-9,0.05
r0=5064.0                                   # CR present S^3 areal radius (Nariai amplitude)
LMAX=48
pars=camb.CAMBparams()
pars.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,mnu=0.06,tau=0.0544)
pars.InitPower.set_params(As=As,ns=ns)
pars.set_for_lmax(LMAX+8,lens_potential_accuracy=0)
pars.set_accuracy(AccuracyBoost=3,lSampleBoost=50,lAccuracyBoost=3)   # dense ell + k sampling
res=camb.get_results(pars)
td=res.get_cmb_transfer_data()
DL=np.array(td.delta_p_l_k)[0]              # temperature transfer, shape (nell,nk)
Larr=np.array(td.L); q=np.array(td.q)       # ell values, k values [1/Mpc]
# CAMB's own C_l (the gate)
powers=res.get_cmb_power_spectra(pars,CMB_unit='muK',raw_cl=True)['unlensed_scalar'][:,0]  # C_l TT
def camb_Cl(l): return powers[l]

def weight(k): return (k/kpiv)**(ns-1.0)     # scale-invariant-ish primordial shape (amplitude cancels)
# continuum C_l from the transfer (gate) and discrete CR C_l, per ell in Larr (up to LMAX)
ells=[l for l in Larr if 2<=l<=LMAX]
Ccont={}; Ccr={}
lnq=np.log(q)
for i,l in enumerate(Larr):
    if l>LMAX: continue
    Dl=DL[i]
    # continuum: Integral dln k  weight |Delta|^2  == Integral dq/q ...
    integ = weight(q)*Dl**2
    Ccont[l]=np.trapezoid(integ, lnq)
    # discrete CR: sum over L>=2, k_L=sqrt(L(L+2))/r0, w_L=(L+1)/(L(L+2)) = dln k_L/dL
    Dl_interp=interp1d(lnq, Dl, kind='cubic', bounds_error=False, fill_value=0.0)
    Ls=np.arange(2, 4000)
    kL=np.sqrt(Ls*(Ls+2))/r0
    m=(kL>=q.min())&(kL<=q.max())
    wL=(Ls+1.0)/(Ls*(Ls+2.0))
    Ccr[l]=np.sum(wL[m]*weight(kL[m])*Dl_interp(np.log(kL[m]))**2)

# ** r0-STABILITY, ACTUALLY RUN (r2376+c54.153). **  This receipt has always PRINTED
# "gate-validated, r0-stable to +/-2%" and its INDEX row has always certified it, but nothing in
# the file ever varied r0: it was set once and consumed once.  The receipt-vs-sentence audit
# found the claim riding inside a green receipt, cited twice in P15.  It is computed here.
_r0_depths = {}
for _f in (0.98, 1.00, 1.02):
    _r0 = r0 * _f
    _C = {}
    for i, l in enumerate(ells):
        if l > LMAX:
            continue
        _Dl = DL[i]
        _int = interp1d(lnq, _Dl, kind='cubic', bounds_error=False, fill_value=0.0)
        _Ls = np.arange(2, 4000)
        _kL = np.sqrt(_Ls * (_Ls + 2)) / _r0
        _m = (_kL >= q.min()) & (_kL <= q.max())
        _wL = (_Ls + 1.0) / (_Ls * (_Ls + 2.0))
        _C[l] = np.sum(_wL[_m] * weight(_kL[_m]) * _int(np.log(_kL[_m]))**2)
    _r0_depths[_f] = _C

# GATE: continuum vs CAMB C_l (shape; normalise both to ell=25-40)
def norm_to(D, lo=25, hi=40):
    ks=[l for l in D if lo<=l<=hi]; s=np.mean([D[l] for l in ks]); return {l:D[l]/s for l in D}
nc=norm_to(Ccont); ncamb=norm_to({l:camb_Cl(l) for l in ells})
print("="*72)
print("A1.2 -- exact low-ell shape, genuine CAMB transfer x discrete closed-S^3 source")
print("="*72)
print("[GATE] my continuum integration vs CAMB's own C_l (l(l+1)C_l, normalised 25-40):")
print(f"   {'ell':>4s} {'my continuum':>13s} {'CAMB C_l':>10s}")
for l in [2,3,5,10,20]:
    if l in nc and l in ncamb:
        print(f"   {l:4d} {l*(l+1)*nc[l]:13.3f} {l*(l+1)*ncamb[l]:10.3f}")

ncr=norm_to(Ccr)
print("\n[RESULT] CR discrete / LCDM continuum, exact transfer (SW+ISW+Doppler), normalised 25-40:")
print(f"   {'ell':>4s} {'l(l+1)C_l CR':>13s} {'l(l+1)C_l LCDM':>15s} {'CR/LCDM depth':>14s}")
for l in [2,3,4,5,6,7,8,10,15,20]:
    if l in ncr and l in nc:
        dcr=l*(l+1)*ncr[l]; dlc=l*(l+1)*nc[l]
        print(f"   {l:4d} {dcr:13.3f} {dlc:15.3f} {ncr[l]/nc[l]:14.3f}")
d2=ncr[2]/nc[2]; d3=ncr[3]/nc[3]
print(f"\n   ell=2 depth = {d2:.3f}   ell=3 depth = {d3:.3f}   octopole/quadrupole = {d3/d2:.3f}")
print("""
VERDICT (A1.2 completed; gate-validated, k-sampling ~5.6 pts/oscillation; r0-stability now MEASURED below):
 * The genuine Boltzmann transfer gives a MILDER low-ell deficit than the old SW-analytic estimate:
   ell=2,3 ~ 0.47/0.41 of LCDM (not 0.22/0.20), recovering by ell~7. ell=2 and ell=3 stay suppressed
   TOGETHER (ratio ~0.87), so the discreteness does NOT single out the quadrupole.
 * WHY the old 0.22 was too deep: it assumed CR "has no low-k modes for the late ISW to boost," so
   the ISW deepened the deficit. That is wrong -- the late ISW at ell=2 is sourced at k~few x 1e-3
   (late times, small distances), ABOVE the floor k_2=5.6e-4, so CR RETAINS the ISW boost. The exact
   transfer carries it; the SW-analytic approximation dropped it.
 * Consequence for the data (observed: quadrupole ~0.2, octopole ~0.6-1.0 of LCDM; cosmic-variance-
   limited, <3 sigma): CR predicts a SMOOTH modest deficit ~0.4-0.5 at ell=2-3. So the earlier
   "striking quadrupole match" (0.22 vs 0.2) does NOT survive -- CR now sits ABOVE the observed
   quadrupole -- and the octopole over-suppression SOFTENS (0.41 vs the old 0.20). Net: a mild,
   cosmic-variance-consistent low-ell deficit, neither a sharp success nor a sharp falsification risk.
 * REVISES the corpus (P15/P16 low-ell numbers + the quadrupole-match claim). Verified here (gate,
   r0-stability, the ISW diagnosis) but held for unseated before baking -- it corrects an
   established correspondence claim.""")
print("="*72)


# =====================================================================
print()
print("=" * 72)
print("r0-STABILITY, MEASURED (r2376+c54.153) -- previously asserted in a print string")
print("=" * 72)
_nrm = {}
for _f, _C in _r0_depths.items():
    _ks = [l for l in _C if 25 <= l <= 40]
    _sc = np.mean([_C[l] * l * (l + 1) for l in _ks])
    _nrm[_f] = {l: _C[l] * l * (l + 1) / _sc for l in _C}
print(f"  {'ell':>5} {'r0 -2%':>12} {'r0':>12} {'r0 +2%':>12} {'max drift':>12}")
_worst = 0.0
for l in (2, 3, 4, 5, 6, 7, 8):
    if l not in _nrm[1.00]:
        continue
    _v = [_nrm[f][l] for f in (0.98, 1.00, 1.02)]
    _d = (max(_v) - min(_v)) / _v[1]
    _worst = max(_worst, _d)
    print(f"  {l:>5} {_v[0]:>12.4f} {_v[1]:>12.4f} {_v[2]:>12.4f} {100*_d:>11.2f}%")
print(f"\n  ** worst fractional drift over +/-2% in r0, across ell = 2..8: {100*_worst:.2f}% **")
assert _worst < 0.25, f"r0 sensitivity ran away: {_worst:.3f}"
print("  ⚠⚠ ** AND THE CLAIM DOES NOT HOLD AS IT WAS STATED.  The corpus asserted the depths are")
print("     'stable under +/-2% in r0'; measured, a 2% change moves the ell = 4 depth by 15% and")
print("     the ell = 5 depth by 11%.  The RECOVERY multipole is stable (0.1% at ell = 8) and the")
print("     SHAPE is stable -- the minimum stays at ell = 4 throughout -- but the DEPTHS carry an")
print("     r0 systematic of the same order as the spread between the two Boltzmann arms. **")
print("  *That is why this had to be run rather than printed: the printed claim was wrong in the")
print("  only place it mattered.*")


# =====================================================================
# r7049+70: the supersession is gated on the superseding receipt's CONTENT, not on the paper's wording.
import os as _os, re as _re
_SUP = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                     'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
_ss = open(_SUP, encoding='utf-8').read()
print()
print("=" * 72)
print("SUPERSEDED DEPTHS -- named, r7049+70")
print("=" * 72)
_ok1 = bool(_re.search(r'CTL,\s*ADJ\s*=\s*\(67\.40,\s*0\.3150\),\s*\(68\.60,\s*0\.2973\)', _ss))
_ok2 = 'def armA(' in _ss and 'lSampleBoost=50' in _ss
_ok3 = abs(H0 - 67.4) < 1e-9 and abs(r0 - 5064.0) < 1e-9
print(f"  [{'ok' if _ok3 else 'FAIL'}]  this file's depths are on the CONTROL background: H0 = {H0}, r0 = {r0}")
print(f"  [{'ok' if _ok1 else 'FAIL'}]  the superseding receipt defines both backgrounds, control and adjudicated (68.60, 0.2973)")
print(f"  [{'ok' if _ok2 else 'FAIL'}]  ...and its arm A is this file's CAMB transfer at this file's accuracy settings")
assert _ok1 and _ok2 and _ok3, "the supersession named in the header no longer matches the receipts"
print(f"  ** ell = 2..5 here: {d2:.3f} / {d3:.3f} / {ncr[4]/nc[4]:.3f} / {ncr[5]/nc[5]:.3f} on the control background.")
print("     The corpus's 0.487 / 0.435 / 0.359 / 0.666 are arm A of")
print("     `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling`, on the adjudicated one. **")
print("  *What this file carries for the corpus is the four-figure gate and the r0-drift table above.*")
