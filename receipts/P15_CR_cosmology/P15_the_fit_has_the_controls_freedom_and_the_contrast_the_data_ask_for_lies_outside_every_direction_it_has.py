"""
P15_the_fit_has_the_controls_freedom_and_the_contrast_the_data_ask_for_lies_outside_every_direction_it_has.py

** THE REFIT'S OWN ANATOMY, WHICH THE PAPER REPORTED AS A RATIO AND NEVER AS A GEOMETRY.  `sec:refit-
bound` states that the refit closes about a third of the gap and leaves the rest.  WHAT it leaves was
never measured: how many directions the fit actually has, whether this arm has fewer than the control,
and whether what survives is a direction the model could move at all.  All three are measured here. **

** AND IT SETTLES THE READING THE SECTION WAS MISSING.  The leftover is not a parameter deficiency --
this arm has the control's freedom, direction for direction -- and it is not noise.  It is a uniform
ACOUSTIC CONTRAST, which no declared parameter supplies on EITHER arm, and which the data ask this arm
to lower by 6.4 per cent.  The control is asked for nothing.  That is the same quantity, and very
nearly the same size, as the standing arm/control contrast excess the section already carries. **

** COMPUTES: on the banked six-parameter refit grid `computations/beyond_the_wall/refit_grid185/` --
185 plik_lite TT bins over ell 100-1996, base and two-sided steps in H0, Omega_m, omega_b and n_s on
each arm, the amplitude in closed form -- (1) the singular values and effective rank of the whitened
response of the five independent directions, per arm; (2) each parameter's response decomposed on an
amplitude, an acoustic-SHIFT and an acoustic-CONTRAST template of the base spectrum, and the
singular-value ratio of the resulting 4x2 (shift, contrast) matrix; (3) the residual chi2 at the exact
linearised GLS minimum, which is by construction unreachable by any linear move of the five, against
n - 5; (4) the drop a free contrast template would buy, and its fitted coefficient with its error; and
(5) the residual's sign-change count in ell order against correlated plik_lite noise with the same five
directions projected out.  NOT a run of the transfer: every spectrum here is a BANKED one and no
numerical setting of the integrator is touched.  NOT a convergence question: that is swept and closed
elsewhere in this sector.  NOT an attribution of the contrast to a mechanism, which is PO-70's. **

ORIGIN: node 70's `computations/beyond_the_wall/r7091_70_fit_rigidity/rigidity.py` and
  `contrast_size.py`, pre-registered at `PREDICTION.md` beside them.  Those scripts print; this one
  asserts, and the construction is rebuilt here from the banked grid rather than imported, so the
  figures the paper quotes rest on a receipt that recomputes them.

  ** TWO OF THAT PRE-REGISTRATION'S FOUR PREDICTIONS MISSED, AND THE MISSES ARE WHY THIS RECEIPT
  ASSERTS WHAT IT ASSERTS.  A CR-ONLY shift/contrast coupling was predicted and is NOT there -- both
  arms read alike, so the coupling is a property of the parameter basis and not of this arm's clock
  Jacobian -- and a CR arm one effective rank lower was predicted and is not there either.  So the
  equality of the two arms' freedom is asserted here as the finding it is, rather than noted as a
  shortfall of a guess. **

WHAT IS COMPUTED, and what each assertion is for.
  1. ** THE RANK IS 4 STIFF PLUS 1 SOFT ON BOTH ARMS, with the same degenerate direction. **  H0 and
     Omega_m have |cos| = 0.99 on both arms: the familiar geometric degeneracy, not an artefact here.
     Asserted so that "this arm has fewer directions" cannot be read into the ratio.
  2. ** THE CONTRAST RESPONSE IS SMALL ON BOTH ARMS. **  The 4x2 (shift, contrast) singular-value
     ratio is 0.04 on the control and 0.036 on this arm.  Both read "collinear" against the
     pre-registered 0.1 -- so the right statement is that the declared parameters move the acoustic
     SHIFT and barely move the CONTRAST, on either background.
  3. ** THE REACH SEPARATES THE ARMS AND NOTHING ELSE HERE DOES. **  At the exact GLS minimum the
     control leaves 186.0 against n - 5 = 180 (+0.3 sigma: the fit reaches the data) and this arm
     leaves 278.8 (+5.2 sigma).  About a hundred in chi2 lies outside every direction the model has.
  4. ** AND THE MISSING DIRECTION IS A UNIFORM CONTRAST. **  Freeing one contrast template removes
     56.4 of this arm's residual (20 per cent) against 0.8 on the control, at a coefficient
     c = -0.0636 +- 0.0085 (-7.5 sigma) against the control's -0.0075 +- 0.0083 (-0.9 sigma).  An
     ell-MODULATED contrast buys 4.5 and a modulated shift 0.4, so the request is uniform rather than
     a drift.
  5. ** THE RESIDUAL IS NOT NOISE ON THIS ARM AND IS NOISE ON THE CONTROL. **  54 sign changes against
     noise's 88 +- 10, on 2000 correlated draws with the five directions removed; the control's 87.

WHAT IS NOT CLAIMED.
  * ** Nothing here says CR's physics sets the contrast lower. **  What is established is that the
    quantity the data ask to move is outside the span of the declared parameters, so no
    re-parametrisation reaches it and the change has to come from what SETS the contrast.  Which
    assignment that is, is `PO-70`'s and the rate rulings', not this receipt's.
  * ** The lensing operator is the registered refit's own fallback **, CAMB at the control's
    parameters, and is identical on both arms by construction, so it cannot carry an arm difference.
  * ** The onset pin is not in this grid. **  Every CR run in it sets ZSTART=3e7, so the solved onset
    is overridden there.  That is asserted below as a FACT about the grid, because it bounds what this
    receipt is about: these are the directions of the grid's model, and if the reported spectrum uses
    the solved onset they are not that spectrum's directions.
  * The Monte Carlo is 2000 draws at a fixed seed; the sign-change count is asserted as a wide
    inequality against the noise mean, not at a p-value this receipt would have to calibrate.

STATUS: OK (ranks, the two singular-value ratios, the two reaches, the contrast drop and its
coefficient with its sigma, the modulated alternatives, the crossing counts, and the grid's own
ZSTART, all asserted).

rc=0 on success.  Run: python3 P15_the_fit_has_the_controls_freedom_and_the_contrast_the_data_ask_for_lies_outside_every_direction_it_has.py
"""
import glob
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                            # noqa: E402

GRID = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)       # the registered refit's own step sizes
NMC = 2000
rng = np.random.default_rng(7091)

_fails = []


def check(label, ok):
    print(f"   {'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        _fails.append(label)


print(__doc__.split('rc=0')[0])

# ---------------------------------------------------------------- the lensing operator, the refit's own
_lr = os.path.join(SPEC, 'cc66_lens_ratio.npz')
if os.path.exists(_lr):
    _z = np.load(_lr)
    LG, RATIO = np.asarray(_z['lg'], float), np.asarray(_z['ratio'], float)
    LENSSRC = 'banked cc66_lens_ratio.npz'
else:
    import camb
    _p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                         mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    _cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
    _le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
    LG = np.arange(len(_le), dtype=float)
    RATIO = np.ones_like(_le)
    RATIO[_un > 0] = _le[_un > 0] / _un[_un > 0]
    LENSSRC = "CAMB at the control's parameters (the registered refit's own fallback)"


def binned(ls, Dl):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO))


def load(tag):
    z = np.load(os.path.join(GRID, f'{tag}.npz'))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


def build(arm):
    """Every response scaled by the base's closed-form amplitude, so a whitened column is in the
    DATA's sigma.  (Omitting that is the one trap here: the banked spectra are in arbitrary units.)"""
    ls, Dl, lA = load(f'{arm}_base')
    m0 = binned(ls, Dl)
    ok = np.isfinite(m0)
    C = CS.COV_TT[np.ix_(ok, ok)]
    L = np.linalg.cholesky(C)
    g = {}
    for k in STEP:
        lp, Dp, _ = load(f'{arm}_{k}p')
        lm, Dm, _ = load(f'{arm}_{k}m')
        g[k] = (binned(lp, Dp)[ok] - binned(lm, Dm)[ok]) / (2 * STEP[k])
    dD = np.gradient(Dl, ls)
    shift = binned(ls, -ls * dD)[ok]                                 # a stretch in ell
    env = np.array([Dl[(ls >= l - 0.5 * lA) & (ls <= l + 0.5 * lA)].mean() for l in ls])
    contrast = binned(ls, Dl - env)[ok]                              # the oscillatory part about it
    d = CS.X_DATA[ok]
    Fi = np.linalg.inv(C)
    A0 = float((m0[ok] @ Fi @ d) / (m0[ok] @ Fi @ m0[ok]))
    return dict(m0=A0 * m0[ok], ok=ok, C=C, L=L, d=d, lA=lA, A0=A0,
                g={k: A0 * v for k, v in g.items()},
                bins=0.5 * (CS.BIN_LO + CS.BIN_HI)[ok],
                shift=A0 * shift, contrast=A0 * contrast)


def W(B, v):
    return scipy.linalg.solve_triangular(B['L'], v, lower=True)


def crossings(s):
    sg = np.sign(s)
    return int(np.sum(sg[1:] != sg[:-1]))


# ================================================================ ⓪ THE GRID'S OWN ONSET SETTING
print('=' * 96)
print(' ⓪  THE GRID IS READ BEFORE IT IS USED: which onset every CR run in it was computed at.')
print('=' * 96)
_meta = sorted(glob.glob(os.path.join(GRID, '*.json')) + glob.glob(os.path.join(GRID, '*.sh'))
               + glob.glob(os.path.join(GRID, '*.log')) + glob.glob(os.path.join(GRID, '*.py')))
_txt = ''.join(open(f, encoding='utf-8', errors='replace').read() for f in _meta)
_zs = 'ZSTART=3e7' in _txt or "ZSTART', '3e7" in _txt or 'ZSTART=3.0e7' in _txt
print(f"   grid files carrying the run configuration: {len(_meta)}")
print(f"   ** ZSTART=3e7 appears in the grid's own configuration: {_zs} ** -- so the solved onset")
print("      (Z_START = None, solved for the pinned acoustic scale) is OVERRIDDEN in this grid, and")
print("      the directions measured below are the directions of the grid's model.")
check('⓪ the grid states its own onset, and it is the fixed 3e7 rather than the solved pin', _zs)

OUT = {}
for arm, name in (('lcdm', 'CONTROL'), ('cr', 'CR, crossing')):
    B = build(arm)
    n = int(B['ok'].sum())
    cols = ['A'] + list(STEP)
    print()
    print('=' * 96)
    print(f'  {name}   {n} bins, lensing: {LENSSRC},  l_A at base {B["lA"]:.3f}')
    print('=' * 96)

    # ------------------------------------------------------------ ① the rank
    Jw = np.column_stack([W(B, c) for c in
                          [B['m0'] * 0.02] + [B['g'][k] * STEP[k] for k in STEP]])
    S = np.linalg.svd(Jw, compute_uv=False)
    rank1 = int(np.sum(S ** 2 > 1))
    print('  ①  whitened singular values, one receipt-step per parameter (amplitude at 2 %):')
    print('        ' + '  '.join(f'{s:8.2f}' for s in S))
    print(f'        effective rank {rank1} at dchi2 > 1 per step;  '
          f'{int(np.sum(S > 0.01 * S[0]))} above 1 % of the largest')
    nrm = Jw / np.linalg.norm(Jw, axis=0)
    cs = abs(float(nrm[:, cols.index('H0')] @ nrm[:, cols.index('OM')]))
    print(f'        |cos| between the H0 and Omega_m responses: {cs:.3f}  (the geometric degeneracy)')

    # ------------------------------------------------------------ ② the shift / contrast decomposition
    T = np.column_stack([W(B, B['m0']), W(B, B['shift']), W(B, B['contrast'])])
    co = {}
    for k in STEP:
        co[k], *_ = np.linalg.lstsq(T, W(B, B['g'][k] * STEP[k]), rcond=None)
    M = np.array([[co[k][1], co[k][2]] for k in STEP]) * np.array(
        [np.linalg.norm(T[:, 1]), np.linalg.norm(T[:, 2])])
    s2 = np.linalg.svd(M, compute_uv=False)
    ratio = float(s2[1] / s2[0])
    print('  ②  each parameter on (shift, contrast), whitened and the templates put on one scale:')
    for i, k in enumerate(STEP):
        print(f'        {k:3s}  shift {M[i, 0]:+.3e}   contrast {M[i, 1]:+.3e}   '
              f'contrast/shift {M[i, 1] / M[i, 0]:+.3f}')
    print(f'        the 4x2 matrix: sv {s2[0]:.3f}, {s2[1]:.3f}  ->  ratio {ratio:.3f}')

    # ------------------------------------------------------------ ③ the reach, at the exact GLS minimum
    dw = W(B, B['d'])
    Q, _ = np.linalg.qr(Jw)
    rw = dw - Q @ (Q.T @ dw)
    tot = float(rw @ rw)
    sig = (tot - (n - 5)) / np.sqrt(2 * (n - 5))
    print(f'  ③  residual chi2 at the linearised GLS minimum {tot:.1f} -- unreachable by any linear')
    print(f'        move of the five by construction -- against n - 5 = {n - 5}  ({sig:+.1f} sigma)')

    # ------------------------------------------------------------ ④ what a free contrast would buy
    drops = {}
    for lab, tmpl in (('contrast, uniform', B['contrast']),
                      ('contrast x (ell - mid)', B['contrast'] * (B['bins'] - B['bins'].mean())
                       / np.ptp(B['bins'])),
                      ('shift x (ell - mid)', B['shift'] * (B['bins'] - B['bins'].mean())
                       / np.ptp(B['bins']))):
        tw = W(B, tmpl)
        tw = tw - Q @ (Q.T @ tw)
        drops[lab] = float((tw @ rw) ** 2 / (tw @ tw))
        print(f'        + {lab:24s} free would remove dchi2 {drops[lab]:7.1f}  '
              f'({100 * drops[lab] / tot:4.1f} % of the residual)')
    # the coefficient itself, fitted jointly with the five so it is not credited their freedom
    Jc = np.column_stack([Jw, W(B, B['contrast'])])
    y = dw - W(B, B['m0'])
    xc, *_ = np.linalg.lstsq(Jc, y, rcond=None)
    err = np.sqrt(np.diag(np.linalg.inv(Jc.T @ Jc)))
    cval, cerr = float(xc[-1]), float(err[-1])
    print(f'        ** the contrast scaled by (1 + c):  c = {cval:+.4f} +- {cerr:.4f}  '
          f'({cval / cerr:+.1f} sigma) **')

    # ------------------------------------------------------------ ⑤ the residual's shape against noise
    r = B['L'] @ rw
    s = np.sqrt(np.diag(B['C']))
    obs = crossings(r / s)
    P = np.identity(n) - Q @ Q.T
    sim = np.array([crossings((B['L'] @ (P @ rng.standard_normal(n))) / s) for _ in range(NMC)],
                   float)
    print(f'  ⑤  sign changes in ell order: data {obs}   noise {sim.mean():.1f} +- {sim.std():.1f}'
          f'   ({(obs - sim.mean()) / sim.std():+.2f} sigma over {NMC} correlated draws)')

    OUT[arm] = dict(rank=rank1, cs=cs, ratio=ratio, tot=tot, sig=sig, drops=drops,
                    c=cval, cerr=cerr, cross=obs, nmean=sim.mean(), nsd=sim.std())

# ================================================================ THE ASSERTIONS
print()
print('=' * 96)
print('  THE ASSERTIONS')
print('=' * 96)
L, R = OUT['lcdm'], OUT['cr']

print(' ① the freedom, and it is EQUAL -- which is the finding, the pre-registration having predicted'
      ' one fewer on this arm')
check('① the control has 4 stiff directions at dchi2 > 1 per step', L['rank'] == 4)
check('① and this arm has the same 4, not fewer', R['rank'] == 4)
check('① H0 and Omega_m are degenerate to |cos| > 0.98 on BOTH arms, so the degeneracy is the '
      'familiar geometric one and not this arm\'s', min(L['cs'], R['cs']) > 0.98)

print(' ② the contrast response is small on BOTH arms -- so no declared parameter supplies a contrast,'
      ' on either background')
check('② the control\'s 4x2 (shift, contrast) sv-ratio is 0.040 to three decimals',
      abs(L['ratio'] - 0.040) < 0.0015)
check('② this arm\'s is 0.036 to three decimals', abs(R['ratio'] - 0.036) < 0.0015)
check('② both sit under the 0.1 pre-registered as "collinear", so the coupling is NOT CR-specific',
      max(L['ratio'], R['ratio']) < 0.1)

print(' ③ the reach, which is the one place the two arms part')
check('③ the control leaves 186.0 at the GLS minimum', abs(L['tot'] - 186.0) < 1.0)
check('③ and that is within 1 sigma of n - 5 = 180: the control reaches the data', abs(L['sig']) < 1.0)
check('③ this arm leaves 278.8', abs(R['tot'] - 278.8) < 1.5)
check('③ at +5.2 sigma over n - 5, so about a hundred in chi2 is outside every direction it has',
      abs(R['sig'] - 5.2) < 0.2)

print(' ④ and the missing direction is a UNIFORM contrast, at a size the data name')
check('④ a free uniform contrast removes 56.4 of this arm\'s residual',
      abs(R['drops']['contrast, uniform'] - 56.4) < 1.5)
check('④ against 0.8 on the control, so the control asks for no contrast',
      L['drops']['contrast, uniform'] < 2.0)
check('④ the fitted coefficient is c = -0.064 +- 0.009 on this arm',
      abs(R['c'] + 0.0636) < 0.003 and abs(R['cerr'] - 0.0085) < 0.002)
check('④ which is -7.5 sigma', abs(R['c'] / R['cerr'] + 7.5) < 0.5)
check('④ and -0.9 sigma on the control, which is nothing',
      abs(L['c'] / L['cerr']) < 1.5)
check('④ an ell-MODULATED contrast buys under a tenth of what the uniform one does, so the request '
      'is uniform rather than a drift',
      R['drops']['contrast x (ell - mid)'] < 0.1 * R['drops']['contrast, uniform'])
check('④ and a modulated shift buys less still', R['drops']['shift x (ell - mid)']
      < R['drops']['contrast x (ell - mid)'])

print(' ⑤ the residual is not noise on this arm, and is noise on the control')
check('⑤ this arm crosses zero 54 times', R['cross'] == 54)
check('⑤ against a noise mean of 88 +- 10, so it is more than 3 sigma short of noise',
      abs(R['nmean'] - 88) < 4 and (R['nmean'] - R['cross']) > 3 * R['nsd'])
check('⑤ while the control crosses 87, inside one sigma of its own noise',
      abs(L['cross'] - L['nmean']) < L['nsd'])

print(' ⛭ AND THE ONE INFERENCE THE PAPER TAKES FROM THIS, asserted as an inequality rather than '
      'narrated')
# ⌗ ** THE FIRST WRITING OF THIS CHECK ASSERTED A FACTOR OF TWENTY AND THE MEASURED RATIO IS EIGHT
#   (7.5 against 0.9).  The check caught it; the reasoning that wrote it did not. **  It is kept at the
#   size the numbers support, which is the whole point of putting the inference in an assertion: the
#   two arms are separated by this quantity being SIGNIFICANT on one and absent on the other, and the
#   strength of that separation is a measured eight-fold rather than a remembered one.
check('⛭ the request is decisive on this arm and absent on the control: past 7 sigma against under 1',
      abs(R['c'] / R['cerr']) > 7.0 and abs(L['c'] / L['cerr']) < 1.0)
check('⛭ and the two differ eight-fold in significance and more than five-fold in size',
      abs(R['c'] / R['cerr']) > 8 * abs(L['c'] / L['cerr']) and abs(R['c']) > 5 * abs(L['c']))

print()
if _fails:
    print(f'FAIL ({len(_fails)}): ' + '; '.join(_fails))
    sys.exit(1)
print('ALL CHECKS PASS')
sys.exit(0)
