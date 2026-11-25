# -*- coding: utf-8 -*-
"""Ⓐ⓪ THE ENVELOPE RULING, APPLIED TO THIS LINE'S OWN LANDED HEADLINE FIRST.

Order `r7873` relays `cc66`'s finding that CAMB's sum response at fixed parameters is an
OSCILLATION -- a peak shift -- whose ENVELOPE is what is monotone in the sum, and rules: *"Read your
ratios against that envelope, not against point values."*

⛔ ** THAT RULING LANDS ON `r7872`'s OWN HEADLINE, so it is spent here before anything new is
measured. **  `r7872` reported the instrument's TT response at `ell = 100` as `1.77x` CAMB's, which
is a ratio of POINT VALUES.  If CAMB's response oscillates with an envelope as large as that gap,
the factor was reading the oscillation and not a departure.  Both outcomes are registered in
`PREDICTION.md` and this file decides between them.

** THE DEFINITION IS cc66's, AND IT IS REPRODUCED BEFORE IT IS USED. **  `envelope` is the largest
absolute excursion of the response over the band; this file recomputes `cc66`'s own whole-band
numbers from its own control, tau, `A_s`, `lmax` and CAMB leg, and reports the agreement.  *A second
seat re-implementing a definition and then comparing against its own version is how two numbers get
called the same thing.*

⚠ ** AND ONE THING cc66's NUMBER CANNOT BE USED FOR WITHOUT SAYING SO. **  `cc66` computed on the
LENSED leg; the instrument's banked TT/EE/TE are UNLENSED, which is why `r7872` compared against the
unlensed one.  The envelope is leg-dependent, so an unlensed departure read against a lensed
envelope mixes two objects.  ⇒ Both legs' envelopes are reported, whole-band and local, and the
VERDICT is taken on the like-for-like (unlensed) one with the lensed one printed beside it.

    NODE=60 python3 envelope.py
"""
import json
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7871 = os.path.join(_BTW, 'r7871_cc66_cambs_sum_response_at_the_spectrum_level')
ON = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
OUT = os.path.join(_HERE, 'envelope.json')

CC = json.load(open(os.path.join(R7871, 'sum_response.json')))
H0 = float(CC['control']['H0'])
OM = float(CC['control']['OM'])
WB = float(CC['control']['WB'])
NS = float(CC['control']['NS'])
TAU = float(CC['tau'])
A_S = float(CC['A_s'])
LMAX = int(CC['lmax_calc'])
L_LO, L_HI = int(CC['l_lo']), int(CC['l_hi'])
SUMS = [float(s) for s in CC['sums']]
rec = dict(read_from=os.path.basename(R7871),
           control=dict(H0=H0, OM=OM, WB=WB, NS=NS, tau=TAU, A_s=A_S, lmax=LMAX),
           band=[L_LO, L_HI], sums=SUMS)
print('=' * 100)
print('  Ⓐ⓪ THE ENVELOPE RULING, SPENT ON THIS LINE\'S OWN HEADLINE FIRST')
print('=' * 100)
print('  cc66\'s control read from its record: H0 %.2f, Om %.4f, ombh2 %.4f, ns %.3f, tau %.3f, '
      'A_s %.3g, lmax %d' % (H0, OM, WB, NS, TAU, A_S, LMAX))


def camb_legs(sum_ev):
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
    sp = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['unlensed_scalar', 'lensed_scalar'])
    ls = np.arange(L_LO, L_HI + 1)
    out = {}
    for leg, arr in (('unlensed', sp['unlensed_scalar']), ('lensed', sp['lensed_scalar'])):
        out[leg] = dict(TT=arr[ls, 0], EE=arr[ls, 1], TE=arr[ls, 3])
    return ls, out


LS, legs = {}, {}
for s in [0.0] + SUMS:
    LS, legs[s] = camb_legs(s)
    print('    CAMB at Sum = %.2f eV: both legs on %d multipoles' % (s, LS.size))


def osc(r):
    """cc66's own summary of a response array: the envelope is the largest absolute excursion"""
    r = np.asarray(r, float)
    return dict(envelope=float(max(abs(float(r.max())), abs(float(r.min())))),
                max=float(r.max()), min=float(r.min()),
                sign_changes=int(np.sum(np.diff(np.sign(r)) != 0)),
                frac_positive=float(np.mean(r > 0)))


# ── the definition, reproduced on cc66's own leg and band ──────────────────────────────────────
print('\n  cc66\'s whole-band numbers, RECOMPUTED here on its own LENSED leg (its definition, not '
      'a second one):')
print('%6s %6s %14s %14s %10s %10s' % ('block', 'Sum', 'envelope here', 'cc66\'s', 'rel diff',
                                       'sign chg'))
repro = {}
worst = 0.0
for s in SUMS:
    for blk in ('TT', 'EE'):
        r = legs[s]['lensed'][blk] / legs[0.0]['lensed'][blk] - 1.0
        here = osc(r)
        theirs = CC['oscillation'][('%g' % s)][blk]
        rel = abs(here['envelope'] - theirs['envelope']) / abs(theirs['envelope'])
        worst = max(worst, rel)
        repro['%s|%.2f' % (blk, s)] = dict(here=here, cc66=theirs, rel_diff=rel)
        print('%6s %6.2f %14.8f %14.8f %10.2e %5d/%-4d'
              % (blk, s, here['envelope'], theirs['envelope'], rel,
                 here['sign_changes'], theirs['sign_changes']))
rec['reproduction'] = dict(rows=repro, worst_rel_diff=worst,
                           holds=bool(worst < 1e-6))
print('  ⇒ worst relative difference %.2e -- %s' % (worst,
      'the definition is reproduced, so it IS cc66\'s' if worst < 1e-6
      else '⛔ NOT reproduced: the envelope used below would be a second definition'))

# ── the envelopes that matter: both legs, whole band and local ─────────────────────────────────
WINDOWS = {'whole 100-1996': (L_LO, L_HI), 'local 100-420': (100, 420), 'the run 100-212': (100, 212)}
print('\n%6s %6s %-9s %-16s %14s' % ('block', 'Sum', 'leg', 'window', 'envelope'))
env = {}
for blk in ('TT', 'EE'):
    for s in SUMS:
        for leg in ('unlensed', 'lensed'):
            r = legs[s][leg][blk] / legs[0.0][leg][blk] - 1.0
            for wn, (a, b) in WINDOWS.items():
                m = (LS >= a) & (LS <= b)
                e = osc(r[m])
                env['%s|%.2f|%s|%s' % (blk, s, leg, wn)] = e
                print('%6s %6.2f %-9s %-16s %14.8f' % (blk, s, leg, wn, e['envelope']))
rec['envelopes'] = env

# ── the instrument's departure over the run, measured on its own grid ──────────────────────────
def bank(tag):
    with np.load(os.path.join(ON, 'lcdm_%s.npz' % tag), allow_pickle=True) as z:
        return (np.asarray(z['ls'], int), np.asarray(z['Dl'], float),
                np.asarray(z['Dl_EE'], float))


tags = {0.06: 'S006', 0.30: 'S030', 0.60: 'S060'}
bl, b0_tt, b0_ee = bank('S000')
print('\n  the instrument\'s departure over the run it was located in, on its own %d-multipole '
      'grid:' % bl.size)
print('%6s %6s %16s %16s %16s %10s' % ('block', 'Sum', 'max|dep| 100-212', 'env unlensed',
                                       'env lensed', 'verdict'))
dep = {}
for blk, b0 in (('TT', b0_tt), ('EE', b0_ee)):
    for s in SUMS:
        _, s_tt, s_ee = bank(tags[s])
        r_inst = (s_tt if blk == 'TT' else s_ee) / b0 - 1.0
        for wn, (a, b) in (('the run 100-212', (100, 212)), ('local 100-420', (100, 420))):
            mi = (bl >= a) & (bl <= b)
            mc = np.isin(LS, bl[mi])
            r_c_un = (legs[s]['unlensed'][blk] / legs[0.0]['unlensed'][blk] - 1.0)[mc]
            r_c_le = (legs[s]['lensed'][blk] / legs[0.0]['lensed'][blk] - 1.0)[mc]
            d_un = float(np.max(np.abs(r_inst[mi] - r_c_un)))
            d_le = float(np.max(np.abs(r_inst[mi] - r_c_le)))
            e_un = env['%s|%.2f|unlensed|%s' % (blk, s, wn)]['envelope']
            e_le = env['%s|%.2f|lensed|%s' % (blk, s, wn)]['envelope']
            v = 'SURVIVES' if d_un > e_un else 'INSIDE'
            dep['%s|%.2f|%s' % (blk, s, wn)] = dict(
                max_departure_vs_unlensed=d_un, max_departure_vs_lensed=d_le,
                envelope_unlensed=e_un, envelope_lensed=e_le,
                ratio_to_unlensed_envelope=d_un / e_un, ratio_to_lensed_envelope=d_le / e_le,
                verdict_on_like_for_like=v,
                verdict_on_cc66_leg=('SURVIVES' if d_le > e_le else 'INSIDE'))
            if wn == 'the run 100-212':
                print('%6s %6.2f %16.8f %16.8f %16.8f %10s' % (blk, s, d_un, e_un, e_le, v))
rec['departure'] = dep

# ── r7872's own figure, re-read ────────────────────────────────────────────────────────────────
i100 = int(np.where(bl == 100)[0][0])
_, s60_tt, _ = bank('S060')
r_inst_100 = float(s60_tt[i100] / b0_tt[i100] - 1.0)
c100_un = float((legs[0.60]['unlensed']['TT'] / legs[0.0]['unlensed']['TT'] - 1.0)[LS == 100][0])
c100_le = float((legs[0.60]['lensed']['TT'] / legs[0.0]['lensed']['TT'] - 1.0)[LS == 100][0])
e_un_run = env['TT|0.60|unlensed|the run 100-212']['envelope']
e_le_run = env['TT|0.60|lensed|the run 100-212']['envelope']
gap = r_inst_100 - c100_un
rec['r7872_headline'] = dict(instrument_at_100=r_inst_100, camb_unlensed_at_100=c100_un,
                             camb_lensed_at_100=c100_le,
                             point_ratio=r_inst_100 / c100_un,
                             gap_at_100=gap,
                             envelope_over_the_run_unlensed=e_un_run,
                             envelope_over_the_run_lensed=e_le_run,
                             gap_over_envelope_unlensed=gap / e_un_run,
                             gap_over_envelope_lensed=gap / e_le_run,
                             survives_on_like_for_like=bool(abs(gap) > e_un_run),
                             survives_on_cc66_leg=bool(abs(gap) > e_le_run))
print('\n  r7872\'s headline, re-read under the ruling:')
print('     instrument %.6f at ell 100; CAMB unlensed %.6f, lensed %.6f'
      % (r_inst_100, c100_un, c100_le))
print('     the POINT ratio r7872 reported: %.3fx' % (r_inst_100 / c100_un))
print('     the GAP: %.6f, against the envelope over 100-212 -- unlensed %.6f (%.2fx), '
      'lensed %.6f (%.2fx)' % (gap, e_un_run, gap / e_un_run, e_le_run, gap / e_le_run))
print('  ⇒ %s' % ('THE DEPARTURE SURVIVES the envelope ruling on the like-for-like leg'
                  if abs(gap) > e_un_run else
                  '⛔ THE DEPARTURE IS INSIDE THE ENVELOPE on the like-for-like leg: r7872\'s '
                  'factor was a point-value comparison of a quantity that oscillates'))

json.dump(rec, open(OUT, 'w'), indent=1, sort_keys=True)
print('\n  wrote %s' % OUT)
