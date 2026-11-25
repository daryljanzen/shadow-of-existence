# -*- coding: utf-8 -*-
"""Ⓕ④ THE SHIFT TEST -- does the departure survive a change of the clock that labels multipoles?

Registered in `PREDICTION.md`'s ADDENDUM, which was committed and pushed before this ran.

** THE MODEL IS TWO PARAMETERS WITH SEPARATE PHYSICAL MEANINGS AND NOTHING ELSE: **

    r_inst(ell)  ~  A * r_camb(ell * (1 + eps))

`A` is the response's AMPLITUDE -- how much the sum moves the spectrum.  `eps` is a fractional
ell-STRETCH -- how much the sum moves the peak positions.  A fit with enough freedom to absorb
anything would decide nothing, which is why this is two numbers and not a spline.

** AND THE `eps` IT NEEDS IS CHECKED AGAINST AN INDEPENDENTLY MEASURED NUMBER. **  Each bank point
records its own `l_A`, so the instrument's sum-induced fractional peak shift is read off the bank;
CAMB's is read from its own derived `thetastar` at the same sums.  The DIFFERENCE of those two
fractional shifts is what an `eps` of registration may legitimately be, and it is a ratio of ratios,
so it does not turn on whose definition of `l_A` is used.

    NODE=60 python3 shift.py
"""
import json
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7871 = os.path.join(_BTW, 'r7871_cc66_cambs_sum_response_at_the_spectrum_level')
ON = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
OUT = os.path.join(_HERE, 'shift.json')

CC = json.load(open(os.path.join(R7871, 'sum_response.json')))
H0, OM, WB, NS = (float(CC['control'][k]) for k in ('H0', 'OM', 'WB', 'NS'))
TAU, A_S, LMAX = float(CC['tau']), float(CC['A_s']), int(CC['lmax_calc'])
SUMS = [0.30, 0.60]
TAGS = {0.0: 'S000', 0.30: 'S030', 0.60: 'S060'}
L_LO, L_HI = 100, 420
rec = dict(window=[L_LO, L_HI], sums=SUMS,
           control=dict(H0=H0, OM=OM, WB=WB, NS=NS, tau=TAU, A_s=A_S, lmax=LMAX))
print('=' * 100)
print('  Ⓕ④ THE SHIFT TEST over ell %d-%d' % (L_LO, L_HI))
print('=' * 100)


def camb_one(sum_ev):
    import camb
    om_m = OM * (H0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=H0, ombh2=WB, omch2=max(om_m - WB - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=A_S, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=1)
        return p
    p = build(0.0)
    p = build(p.omnuh2)
    r = camb.get_results(p)
    sp = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['unlensed_scalar'])['unlensed_scalar']
    der = r.get_derived_params()
    return sp, float(der['thetastar'])


CA, THETA = {}, {}
for s in [0.0] + SUMS:
    CA[s], THETA[s] = camb_one(s)
    print('    CAMB at Sum = %.2f eV: 100 theta* = %.6f' % (s, THETA[s]))

# ── the two independently measured fractional peak shifts ──────────────────────────────────────
def bank_lA(tag):
    with np.load(os.path.join(ON, 'lcdm_%s.npz' % tag), allow_pickle=True) as z:
        return float(z['l_A'])


lA = {s: bank_lA(TAGS[s]) for s in [0.0] + SUMS}
shift = {}
print('\n  the two sum-induced fractional peak shifts, each measured by its own side:')
print('%6s %16s %16s %16s %16s %14s' % ('Sum', 'instrument l_A', 'frac shift', 'CAMB 100th*',
                                        'frac shift', 'difference'))
for s in SUMS:
    f_inst = lA[s] / lA[0.0] - 1.0
    # ell scales as 1/theta*, so a fractional change in ell_A is -(fractional change in theta*)
    f_camb = -(THETA[s] / THETA[0.0] - 1.0)
    shift[s] = dict(l_A_instrument=lA[s], l_A_instrument_at_zero=lA[0.0],
                    frac_shift_instrument=f_inst,
                    theta_star_camb=THETA[s], theta_star_camb_at_zero=THETA[0.0],
                    frac_shift_camb=f_camb, difference=f_inst - f_camb)
    print('%6.2f %16.6f %16.3e %16.6f %16.3e %14.3e'
          % (s, lA[s], f_inst, THETA[s], f_camb, f_inst - f_camb))
rec['peak_shifts'] = {('%.2f' % k): v for k, v in shift.items()}
EPS_ALLOWED = {s: abs(shift[s]['difference']) for s in SUMS}
print('  ⇒ an eps of REGISTRATION may legitimately be up to %s'
      % ', '.join('%.3e at Sum %.2f' % (EPS_ALLOWED[s], s) for s in SUMS))


def bank_resp(tag0, tag, blk):
    with np.load(os.path.join(ON, 'lcdm_%s.npz' % tag0), allow_pickle=True) as z:
        ls = np.asarray(z['ls'], int)
        d0 = np.asarray(z['Dl' if blk == 'TT' else 'Dl_EE'], float)
    with np.load(os.path.join(ON, 'lcdm_%s.npz' % tag), allow_pickle=True) as z:
        ds = np.asarray(z['Dl' if blk == 'TT' else 'Dl_EE'], float)
    return ls, ds / d0 - 1.0


EPS = np.linspace(-0.08, 0.08, 3201)
print('\n%6s %6s %10s %12s %12s %12s %12s %10s' % ('block', 'Sum', 'best eps', 'best A',
                                                   'resid best', 'resid (1,0)', 'eps allowed',
                                                   'verdict'))
res = {}
for blk in ('TT', 'EE'):
    for s in SUMS:
        bl, r_i = bank_resp('S000', TAGS[s], blk)
        m = (bl >= L_LO) & (bl <= L_HI)
        x, y = bl[m].astype(float), r_i[m]
        lsc = np.arange(L_LO, L_HI + 1)
        cc = CA[s][lsc, 0 if blk == 'TT' else 1] / CA[0.0][lsc, 0 if blk == 'TT' else 1] - 1.0
        lo = np.arange(2, LMAX + 1)
        cc_full = (CA[s][lo, 0 if blk == 'TT' else 1]
                   / CA[0.0][lo, 0 if blk == 'TT' else 1] - 1.0)

        def resid(eps, aout=False):
            g = np.interp(x * (1.0 + eps), lo.astype(float), cc_full)
            den = float(g @ g)
            a = float(g @ y) / den if den > 0 else 0.0
            r = y - a * g
            return (float(np.sqrt(np.mean(r * r))), a) if aout else float(np.sqrt(np.mean(r * r)))

        rr = np.array([resid(e) for e in EPS])
        j = int(np.argmin(rr))
        best_eps = float(EPS[j])
        best_res, best_A = resid(best_eps, aout=True)
        res00, _a00 = resid(0.0, aout=True)
        # the 1,0 residual with A held at exactly 1 -- the raw pointwise difference
        raw = float(np.sqrt(np.mean((y - np.interp(x, lo.astype(float), cc_full)) ** 2)))
        nearm = rr <= best_res * 1.10
        near = EPS[nearm]
        deg = float(near.max() - near.min())
        allowed = EPS_ALLOWED[s]
        # ⛔ THE REGISTERED CLAUSE IS ABOUT A TRADE-OFF, NOT ABOUT THE WIDTH OF THE eps BAND.
        #   `PREDICTION.md`'s addendum says NOT SEPARABLE means *"`A` and `eps` trade off against
        #   each other across a wide range at comparable residual"*.  The first cut of this file
        #   tested the eps band's WIDTH alone, which is a PROXY for that clause and not the clause:
        #   a wide eps band with a STABLE `A` is an eps that is poorly pinned and an `A` that is
        #   well pinned, which is not a trade-off at all.  ⇒ So `A` is measured ACROSS that band,
        #   and the clause is applied as written.  *The proxy's verdict is kept and printed beside
        #   the clause's, because a criterion that misfires is worth more as a record than as a
        #   deletion.*
        A_near = np.array([resid(e, aout=True)[1] for e in near])
        A_lo, A_hi = float(A_near.min()), float(A_near.max())
        A_spread = A_hi - A_lo
        traded = bool(A_spread > 0.10)        # A moves by over ten per cent across the band
        v_proxy = ('NOT SEP' if (deg > 4.0 * allowed and best_res > 0.5 * raw)
                   else ('REGISTR' if (abs(best_eps) <= allowed and abs(best_A - 1.0) <= 0.10
                                       and best_res < 0.25 * raw) else 'AMPLITUDE'))
        if traded and best_res > 0.5 * raw:
            v = 'NOT SEP'
        elif abs(best_eps) <= allowed and abs(best_A - 1.0) <= 0.10 and best_res < 0.25 * raw:
            v = 'REGISTR'
        else:
            v = 'AMPLITUDE'
        res['%s|%.2f' % (blk, s)] = dict(best_eps=best_eps, best_A=best_A,
                                         resid_best=best_res, resid_at_zero_eps=res00,
                                         resid_raw_A_one_eps_zero=raw,
                                         eps_allowed=allowed,
                                         eps_within_allowed=bool(abs(best_eps) <= allowed),
                                         eps_over_allowed=abs(best_eps) / allowed,
                                         degeneracy_eps_width_at_10pc=deg,
                                         A_across_band=[A_lo, A_hi], A_spread=A_spread,
                                         A_and_eps_trade_off=traded,
                                         verdict_from_the_coded_proxy=v_proxy,
                                         n_multipoles=int(m.sum()), verdict=v)
        print('%6s %6.2f %10.2e %12.5f %12.3e %12.3e %12.3e %10s  A in [%.3f, %.3f] -> %s '
              '(proxy said %s)'
              % (blk, s, best_eps, best_A, best_res, raw, allowed, v, A_lo, A_hi,
                 'trade-off' if traded else 'A STABLE', v_proxy))
rec['fits'] = res

vs = set(v['verdict'] for v in res.values())
if vs == {'REGISTR'}:
    overall = ('A REGISTRATION DIFFERENCE in every block and sum: the departure is a peak-position '
               'difference, and r7872 located nothing')
elif 'AMPLITUDE' in vs:
    overall = ('AN AMPLITUDE DIFFERENCE in at least one block/sum: a departure the envelope test '
               'was too lenient to see -- ROUTED, not asserted over the seat that ruled it')
else:
    overall = 'NOT SEPARABLE on this stretch; no verdict is read through a degenerate fit'
rec['verdict'] = overall
print('\n  ⇒ %s' % overall)
json.dump(rec, open(OUT, 'w'), indent=1, sort_keys=True)
print('  wrote %s' % OUT)
