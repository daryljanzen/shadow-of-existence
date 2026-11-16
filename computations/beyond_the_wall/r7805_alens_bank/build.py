"""r7805 (69) order: PO-24's lensing-amplitude (A_L) response bank, in the layout of r6897_wb_response_lcdm.npz.

ACOUSTIC_two_arm.py computes UNLENSED spectra and has no lensing anywhere, so there is no A_L to expose as a
byte-identical switch.  A_L is a post-processing amplitude: it multiplies the lensing potential's power
C_L^phiphi before the lensing operator acts on the unlensed C_l.  This applies exactly that, on the instrument:
  - the unlensed input is the instrument's own control spectrum, r6897's banked centre (Dl__0.021966, LSTEP=8,
    LMAXL=2000, the refit background), splined onto every l;
  - above the instrument's last multipole (1996) it is extended with CAMB's unlensed TT at the same background,
    scaled to the instrument at the join, because the lensing operator needs inputs band-limited to l >= 2500;
  - C_L^phiphi is CAMB's at the same background (H0 67.410309, Om 0.309826, ombh2 0.021966, ns 0.954248, N_eff 3.0,
    massless neutrinos, As 2.1e-9 -- a STANDARD amplitude, not the instrument's normalisation, which carries none);
  - A_L in {0.8, 0.9, 1.0, 1.1, 1.2} scales it, and camb.correlations.lensed_cls applies it (curved sky,
    Challinor & Lewis 2005), TT only (lensed TT needs only unlensed TT and phiphi).
Checks, written before reading the bank: A_L = 0 returns the input; and the same pipeline run on CAMB's own unlensed
TT reproduces CAMB's own lensed/unlensed ratio, which bounds the operator's numerical error on this grid."""
import os, json, numpy as np, camb
from camb.correlations import lensed_cls
SP = '/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
R = np.load(os.path.join(SP, 'r6897_wb_response_lcdm.npz'), allow_pickle=True)
ls = R['ls__0.021966'].astype(int); Dl = R['Dl__0.021966'].astype(float)
H0, OM, OB, NS, AS = 67.410309, 0.309826, 0.021966, 0.954248, 2.1e-9
h = H0 / 100; ombh2 = OB; omch2 = OM * h * h - ombh2
LMAX = 4000
p = camb.CAMBparams(); p.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=0.0, nnu=3.0, num_massive_neutrinos=0, tau=0.0)
p.InitPower.set_params(As=AS, ns=NS); p.set_for_lmax(LMAX, lens_potential_accuracy=2)
res = camb.get_results(p)
cu = res.get_unlensed_scalar_cls(lmax=LMAX, CMB_unit='muK')      # Dl, columns TT EE BB TE
cl_l = res.get_lensed_scalar_cls(lmax=LMAX, CMB_unit='muK')
clpp = res.get_lens_potential_cls(lmax=LMAX)[:, 0]                # [L(L+1)]^2 C_L^phiphi / 2pi
L = np.arange(LMAX + 1)
# the instrument's spectrum on every l up to its last sample, CAMB's tail above, scaled at the join
from scipy.interpolate import CubicSpline
inst = CubicSpline(ls, Dl)(np.arange(ls[0], ls[-1] + 1))
tt = np.zeros(LMAX + 1); tt[ls[0]:ls[-1] + 1] = inst
scale = inst[-1] / cu[ls[-1], 0]
tt[ls[-1] + 1:] = cu[ls[-1] + 1:, 0] * scale
tt[:ls[0]] = cu[:ls[0], 0] * (inst[0] / cu[ls[0], 0])
def lens(tt_in, AL):
    c = np.zeros((LMAX + 1, 4)); c[:, 0] = tt_in
    return lensed_cls(c, AL * clpp, lmax=LMAX)[:, 0]
# ---- the two checks --------------------------------------------------------------------------------
id0 = lens(tt, 0.0); e0 = np.max(np.abs(id0[2:2001] / tt[2:2001] - 1))
mine = lens(cu[:, 0], 1.0); ratio_mine = mine / cu[:, 0]; ratio_camb = cl_l[:, 0] / cu[:, 0]
e1 = np.max(np.abs(ratio_mine[30:2001] - ratio_camb[30:2001]))
print(f'  check A_L=0 returns the input (l 2..2000): max |rel| = {e0:.2e}')
print(f'  check the operator against CAMB\'s own lensed/unlensed ratio (l 30..2000): max |diff| = {e1:.2e}')
assert e0 < 1e-6 and e1 < 2e-3, (e0, e1)
# ---- the bank, on the instrument's own l grid ------------------------------------------------------
W = {}; AL = [0.0, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]   # 1.3, 1.4 added at r7809 ②
for a in AL:
    out = lens(tt, a); key = f'{a:.2f}'
    W[f'ls__{key}'] = ls.astype(np.int32); W[f'Dl__{key}'] = out[ls]
    for k in ('lA', 'rs', 'DM'):
        W[f'{k}__{key}'] = np.float64(R[f'{k}__0.021966'])
    W[f'nsl__{key}'] = np.int32(R['nsl__0.021966'])
W['alens'] = np.array([a for a in AL if a > 0]); W['missing'] = np.array([], dtype=object)
NB = np.load(os.path.join(SP, 'r7801_neff_response_lcdm.npz'), allow_pickle=True)
cfg = json.loads(str(NB['config__3.00'])); cfg['DNEFF'] = None
cfg['ALENS'] = [a for a in AL if a > 0]
cfg['bank'] = {'what': 'r7805 A_L response: CAMB lensing operator (lensed_cls, TT) applied to the instrument\'s '
               'unlensed control (r6897 centre); A_L=0.00 is the unlensed input, kept for reference',
               'phiphi': {'H0': H0, 'Om': OM, 'ombh2': OB, 'ns': NS, 'As': AS, 'nnu': 3.0, 'mnu': 0.0,
                          'lens_potential_accuracy': 2, 'camb': camb.__version__},
               'tail_above_l': int(ls[-1]), 'tail': 'CAMB unlensed TT scaled to the instrument at the join',
               'checks': {'AL0_identity_max_rel': float(e0), 'operator_vs_camb_ratio_max_diff': float(e1)}}
W['config'] = json.dumps(cfg)
out = os.path.join(SP, 'r7805_alens_response_lcdm.npz'); np.savez_compressed(out, **W)
print(f'  {os.path.basename(out)}: A_L = {list(W["alens"])} (+ 0.00, the unlensed input)')
c = W['Dl__1.00']
for a in ('0.80', '1.20', '0.00'):
    r = W[f'Dl__{a}'] / c
    print(f'  A_L {a} / A_L 1.00 at l ~', [(l, round(float(r[abs(ls - l).argmin()]), 4)) for l in (200, 500, 800, 1100, 1400, 1700, 1990)])

# ---- how much does the near-top response lean on the tail above l = 1996? ---------------------------
# Re-run the A_L = 1.2 / 1.0 ratio with the tail tilted by (l/1996)^(+-0.5) -- a deliberately large change of
# shape above the join -- and report the largest shift in the ratio, by l band.  Reported, not asserted.
def ratio_with_tail(tilt):
    t2 = tt.copy(); hi = np.arange(ls[-1] + 1, LMAX + 1)
    t2[hi] = tt[hi] * (hi / ls[-1]) ** tilt
    return lens(t2, 1.2)[ls] / lens(t2, 1.0)[ls]
base = W['Dl__1.20'] / W['Dl__1.00']
for lo, hi_ in ((2, 1500), (1500, 1800), (1800, 1997)):
    m = (ls >= lo) & (ls < hi_)
    d = max(np.max(np.abs(ratio_with_tail(s)[m] - base[m])) for s in (-0.5, 0.5))
    print(f'  tail-shape sensitivity of A_L 1.2/1.0, l in [{lo}, {hi_}): max |shift| = {d:.1e}')
