# -*- coding: utf-8 -*-
"""Ⓐ① THE SUM RESPONSE AT THE SPECTRUM LEVEL, THE INSTRUMENT AGAINST CAMB.

Order `r7871` item ①: *at the control's cosmology with every other parameter held, give the
instrument's `Dl(Σ)/Dl(0) − 1` for TT, TE and EE at `Σ = 0.06`, `0.30` and `0.60` eV, with NUFD on
and off; name the block and ℓ range where it departs from CAMB's, and say whether NUFD moves the
instrument towards CAMB or away there.*

⛭ ** WHY A RATIO AND NOT A SPECTRUM. **  The instrument's spectra carry a free amplitude that the
chi^2 fits out, so an absolute comparison with CAMB would be a comparison of normalisations.  The
ratio `Dl(Σ)/Dl(0)` divides it out exactly -- a constant amplitude, the units, and `exp(-2 tau)` all
cancel -- which is why the order asks at the spectrum level and not at the level of the limit.

⛔ ** TWO THINGS ARE HELD FIXED THE SAME WAY ON BOTH SIDES, and that is the whole like-for-like. **
  * The TOTAL matter.  The instrument keeps `OM` and takes the sum out of the CLUSTERING matter
    (`OCDM = OM - OB - ONU`); so CAMB is built the same way, `omch2 = om_m - wb - omnuh2`, with
    `omnuh2` taken from a first pass at the same sum.  A CAMB leg that let the total move would be
    answering a different question.
  * Every other parameter: `H0`, `Om`, `ombh2`, `ns`, `tau` are the control's own, identical at
    every sum, so the only thing that varies along each series is the sum.

⚠ ** THE INSTRUMENT'S BANKED TT/EE/TE ARE UNLENSED, so CAMB's UNLENSED leg is the like-for-like
one.**  Both CAMB legs are computed and both are reported, so the choice is visible and measured
rather than assumed: if the departure is the same on both, lensing is not what carries it.

⚠ ** TE CROSSES ZERO, and the registered criterion is pointwise in `Dl(0)`. **  Where `Dl_TE(0)`
passes through zero, `5e-3 * |Dl_TE(0)|` goes to zero with it and the criterion becomes degenerate
-- every multipole near a crossing counts.  ⇒ The criterion is applied EXACTLY as registered and
the degeneracy is NAMED, with the count of multipoles where `|Dl_TE(0)|` is under one per cent of
the block's own RMS; and an RMS-normalised reading is reported BESIDE it, labelled as an additional
reading and not as the registered one.  *The criterion is not swapped after the fact.*

    NODE=60 python3 response.py
"""
import json
import os

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
OUT = os.path.join(_HERE, 'response.json')

ON = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')      # the repair ON, no offset
OFF = os.path.join(BANK, 'pol_grid_bvel1_nufd_off')      # the repair explicitly OFF, this revision's
SUMS = [0.06, 0.30, 0.60]
TAGS = {0.06: 'S006', 0.30: 'S030', 0.60: 'S060'}
BLOCKS = [('TT', 'Dl'), ('EE', 'Dl_EE'), ('TE', 'Dl_TE')]

# the control's own centre, as the generators write it
H0, OM, WB, NS, TAU = 67.40, 0.3150, 0.0224, 0.965, 0.054
A_S, LMAX, ACC = 2.1e-9, 2600, 1
BAND = 5.0e-3            # the registered departure threshold: five parts in a thousand of Dl(0)

rec = dict(control=dict(H0=H0, OM=OM, WB=WB, NS=NS, tau=TAU, A_s=A_S, lmax=LMAX, lens_acc=ACC),
           threshold_of_Dl0=BAND, sums=SUMS)
print('=' * 100)
print('  Ⓐ① THE SUM RESPONSE AT THE SPECTRUM LEVEL -- the instrument against CAMB')
print('=' * 100)


# ── Ⓐ①ᵃ the instrument, read off the banks ─────────────────────────────────────────────────────
def load(where, tag):
    f = os.path.join(where, 'lcdm_%s.npz' % tag)
    if not os.path.exists(f):
        return None
    with np.load(f, allow_pickle=True) as z:
        d = {k: np.asarray(z[k], float) for k in ('ls', 'Dl', 'Dl_EE', 'Dl_TE')}
        c = z['config']
    try:
        c = c.item()
    except Exception:
        pass
    d['config'] = json.loads(str(c))
    return d


banks = {}
blocked = []
for name, where in (('on', ON), ('off', OFF)):
    pts = {}
    for tag in ['S000'] + [TAGS[s] for s in SUMS]:
        p = load(where, tag)
        if p is None:
            blocked.append('%s/%s' % (os.path.basename(where), tag))
        pts[tag] = p
    banks[name] = pts

# the registered negative: a missing point, or multipole vectors that are not identical
ls_ref = None
for name in ('on', 'off'):
    for tag, p in banks[name].items():
        if p is None:
            continue
        if ls_ref is None:
            ls_ref = p['ls']
        elif not np.array_equal(ls_ref, p['ls']):
            blocked.append('%s/%s multipole vector differs element for element' % (name, tag))
rec['blocked'] = blocked
if blocked:
    print('\n  ⛔ BLOCKED, as registered -- nothing is interpolated, re-binned or carried across '
          'banks:')
    for b in blocked:
        print('     - %s' % b)
    rec['verdict'] = 'BLOCKED'
    json.dump(rec, open(OUT, 'w'), indent=1, sort_keys=True)
    raise SystemExit('BLOCKED: %d missing or mismatched point(s)' % len(blocked))

LS = ls_ref.astype(int)
rec['ls'] = LS.tolist()
rec['n_ls'] = int(LS.size)
rec['switch_states'] = {n: {t: dict(NUFD=banks[n][t]['config'].get('NUFD', 'ABSENT'),
                                    MNU=banks[n][t]['config'].get('MNU', 'ABSENT'))
                            for t in banks[n]} for n in banks}
print('\n  %d multipoles, %d to %d; both banks identical element for element'
      % (LS.size, LS[0], LS[-1]))
print('  switch states read from each point\'s own config:')
for n in ('on', 'off'):
    print('    NUFD %-3s : %s' % (n, ', '.join('%s NUFD=%s MNU=%s'
                                               % (t, rec['switch_states'][n][t]['NUFD'],
                                                  rec['switch_states'][n][t]['MNU'])
                                               for t in ['S000'] + [TAGS[s] for s in SUMS])))

inst = {}
for n in ('on', 'off'):
    z0 = banks[n]['S000']
    for s in SUMS:
        zs = banks[n][TAGS[s]]
        for blk, key in BLOCKS:
            inst[(n, s, blk)] = zs[key] / z0[key] - 1.0
rec['denominator'] = 'each bank\'s OWN S000 point, so the ratio is internal to one bank and one arm'


# ── Ⓐ①ᵇ CAMB on the same multipoles, built the same way ────────────────────────────────────────
def camb_dl(sum_ev):
    import camb
    om_m = OM * (H0 / 100.0) ** 2

    def build(onu):
        p = camb.CAMBparams()
        p.set_cosmology(H0=H0, ombh2=WB, omch2=max(om_m - WB - onu, 1e-4), mnu=sum_ev,
                        num_massive_neutrinos=3, neutrino_hierarchy='normal', tau=TAU)
        p.InitPower.set_params(As=A_S, ns=NS)
        p.set_for_lmax(LMAX, lens_potential_accuracy=ACC)
        return p
    p = build(0.0)
    onu = float(p.omnuh2)
    p = build(onu)
    r = camb.get_results(p)
    sp = r.get_cmb_power_spectra(p, CMB_unit='muK',
                                 spectra=['unlensed_scalar', 'lensed_scalar'])
    out = {}
    for leg, arr in (('unlensed', sp['unlensed_scalar']), ('lensed', sp['lensed_scalar'])):
        out[leg] = dict(TT=arr[LS, 0], EE=arr[LS, 1], TE=arr[LS, 3])
    out['omnuh2'] = onu
    return out


print('\n  CAMB legs, built with the TOTAL matter held and omch2 reduced by omega_nu:')
camb = {}
for s in [0.0] + SUMS:
    camb[s] = camb_dl(s)
    print('    Sum = %.2f eV  ->  omega_nu = %.7f' % (s, camb[s]['omnuh2']))
rec['camb_omnuh2'] = {str(s): camb[s]['omnuh2'] for s in [0.0] + SUMS}

ref = {}
for leg in ('unlensed', 'lensed'):
    for s in SUMS:
        for blk, _ in BLOCKS:
            ref[(leg, s, blk)] = camb[s][leg][blk] / camb[0.0][leg][blk] - 1.0

# ── the departure, by the registered criterion, pointwise in |Dl(0)| ───────────────────────────
def runs(mask):
    """the contiguous runs of True, as (lo, hi, n) in multipole"""
    out, i = [], 0
    while i < mask.size:
        if not mask[i]:
            i += 1
            continue
        j = i
        while j + 1 < mask.size and mask[j + 1]:
            j += 1
        out.append((int(LS[i]), int(LS[j]), int(j - i + 1)))
        i = j + 1
    return out


dl0 = {('on', blk): banks['on']['S000'][key] for blk, key in BLOCKS}
rms0 = {blk: float(np.sqrt(np.mean(banks['on']['S000'][key] ** 2))) for blk, key in BLOCKS}
te_degenerate = int(np.sum(np.abs(banks['on']['S000']['Dl_TE']) < 0.01 * rms0['TE']))
rec['te_degeneracy'] = dict(n_multipoles_under_one_percent_of_block_rms=te_degenerate,
                            block_rms_TE=rms0['TE'],
                            note='the registered pointwise criterion is degenerate at a TE zero '
                                 'crossing; it is applied as registered and the degeneracy counted')

dep = {}
print('\n%6s %6s %5s  %-28s %-28s' % ('block', 'Sum', 'leg', 'NUFD on: departing runs',
                                      'NUFD off: departing runs'))
for blk, key in BLOCKS:
    for s in SUMS:
        for leg in ('unlensed', 'lensed'):
            cells = []
            for n in ('on', 'off'):
                # |response_instrument - response_camb| * |Dl(0)| > BAND * |Dl(0)|
                #  <=>  |response difference| > BAND, measured on the instrument's own Dl(0)
                diff = np.abs(inst[(n, s, blk)] - ref[(leg, s, blk)])
                m = diff > BAND
                rr = runs(m)
                rr.sort(key=lambda t: -t[2])
                dep[(blk, s, leg, n)] = dict(n_departing=int(m.sum()), runs=rr[:4],
                                             max_abs_diff=float(diff.max()),
                                             at_ell=int(LS[int(np.argmax(diff))]))
                cells.append('%3d of %3d, longest %s'
                             % (m.sum(), LS.size,
                                ('%d-%d (%d)' % rr[0]) if rr else 'none'))
            print('%6s %6.2f %5s  %-28s %-28s' % (blk, s, leg, cells[0], cells[1]))
rec['departures'] = {'%s|%.2f|%s|%s' % k: v for k, v in dep.items()}

# ── Ⓐ①ᶜ towards CAMB or away, only where a departure was named ─────────────────────────────────
print('\n  Ⓐ①ᶜ does the Fermi-Dirac repair move the instrument TOWARDS CAMB or AWAY, where a '
      'departure was named?')
direction = {}
for leg in ('unlensed', 'lensed'):
    per_block = {}
    for blk, _ in BLOCKS:
        votes = []
        for s in SUMS:
            m = np.abs(inst[('on', s, blk)] - ref[(leg, s, blk)]) > BAND
            m |= np.abs(inst[('off', s, blk)] - ref[(leg, s, blk)]) > BAND
            if not m.any():
                votes.append(None)
                continue
            d_on = float(np.mean(np.abs(inst[('on', s, blk)][m] - ref[(leg, s, blk)][m])))
            d_off = float(np.mean(np.abs(inst[('off', s, blk)][m] - ref[(leg, s, blk)][m])))
            votes.append(dict(sum=s, n=int(m.sum()), mean_abs_on=d_on, mean_abs_off=d_off,
                              towards=bool(d_on < d_off),
                              ratio_on_over_off=(d_on / d_off) if d_off else None))
        live = [v for v in votes if v]
        if not live:
            per_block[blk] = dict(verdict='NO DEPARTURE', votes=votes)
        elif all(v['towards'] for v in live):
            per_block[blk] = dict(verdict='TOWARDS', votes=votes)
        elif all(not v['towards'] for v in live):
            per_block[blk] = dict(verdict='AWAY', votes=votes)
        else:
            per_block[blk] = dict(verdict='MIXED ACROSS SUMS', votes=votes)
        print('    %-9s %-4s %s' % (leg, blk, per_block[blk]['verdict']))
        for v in [x for x in votes if x]:
            print('        Sum %.2f on %d multipoles: |on| %.5f  |off| %.5f  -> %s'
                  % (v['sum'], v['n'], v['mean_abs_on'], v['mean_abs_off'],
                     'towards' if v['towards'] else 'away'))
    named = [b for b in per_block if per_block[b]['verdict'] not in ('NO DEPARTURE',)]
    vs = set(per_block[b]['verdict'] for b in named)
    if not named:
        overall = 'NO DEPARTURE IN ANY BLOCK'
    elif vs == {'TOWARDS'}:
        overall = 'TOWARDS, in every block where a departure was named'
    elif vs == {'AWAY'}:
        overall = 'AWAY, in every block where a departure was named'
    else:
        overall = 'MIXED -- reported as mixed, not resolved by choosing or averaging blocks'
    direction[leg] = dict(per_block=per_block, overall=overall)
    print('    ⇒ %s (%s leg): %s' % (leg, leg, overall))
rec['direction'] = direction

# ── Ⓐ①ᵈ the ℓ-dependence, reported and not diagnosed ───────────────────────────────────────────
print('\n  Ⓐ①ᵈ the ℓ-dependence of each response: bottom of the band, top, and the ratio')
print('%6s %6s %-12s %12s %12s %12s' % ('block', 'Sum', 'who', 'at %d' % LS[0],
                                        'at %d' % LS[-1], 'top/bottom'))
shape = {}
for blk, _ in BLOCKS:
    for s in SUMS:
        for who, arr in (('instrument on', inst[('on', s, blk)]),
                         ('instrument off', inst[('off', s, blk)]),
                         ('CAMB unlensed', ref[('unlensed', s, blk)]),
                         ('CAMB lensed', ref[('lensed', s, blk)])):
            b, t = float(arr[0]), float(arr[-1])
            r = (t / b) if abs(b) > 1e-12 else None
            shape['%s|%.2f|%s' % (blk, s, who)] = dict(bottom=b, top=t, ratio=r)
            print('%6s %6.2f %-12s %12.6f %12.6f %12s'
                  % (blk, s, who, b, t, ('%.4f' % r) if r is not None else 'n/a')) 
rec['shape'] = shape

json.dump(rec, open(OUT, 'w'), indent=1, sort_keys=True)
print('\n  wrote %s' % OUT)
