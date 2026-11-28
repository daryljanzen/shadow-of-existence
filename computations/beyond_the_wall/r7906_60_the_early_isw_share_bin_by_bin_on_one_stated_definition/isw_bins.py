# -*- coding: utf-8 -*-
"""r7906+60 — THE EARLY-ISW SHARE, BIN BY BIN, ON ONE STATED DEFINITION.

Order `r7903` (69) item ②, registered in `PREDICTION.md` and pushed before the first per-bin share
existed.

** THE DEFINITION, AT THE HEAD AS THE ORDER REQUIRES. **  For each plik_lite `TT` bin `b` lying
WHOLLY inside multipoles `100`–`207`:

        S_b(Σ)  =  (full_b − noISW_b) / full_b

where `full_b` and `noISW_b` are the instrument's UNLENSED `TT` `D_l` binned through the likelihood's
OWN `TT` binning — `score_ttteee._bin_one`, which interpolates onto every `l`, converts to `C_l` on
the instrument's convention and bin-weights — and `noISW` is the instrument's own `NOISW` switch on
the `_ISW * et * (dPhi/deta + dPsi/deta)` term.  Σ runs over `0`, `0.06`, `0.30`, `0.60` eV on the
CONTROL arm, whose centre is the reference's own parameters.

⛔ ** THIS REVISION COMPUTES NO SPECTRUM. **  `r7900` ran the instrument eight times at exactly these
sums on exactly this arm; what did not exist is the per-bin share.  So the measurement is a new
READING of an existing bank, which is what the registration says, and the arm identification does not
rest on the filenames: `r7900`'s saved `config` does not record the switch, so the switch-off arm is
established from the decomposition beside each spectrum — the four `isw` bilinear pairs identically
zero and the other six bit-identical.

⛭ ** AND THE BINS ARE NOT TYPED. **  Which bins lie wholly inside the band is read from the
likelihood's own `BIN_LO`/`BIN_HI`.

    python3 isw_bins.py
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7842 = os.path.join(BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness'
                          '_does_not_have')
R7900 = os.path.join(BTW, 'r7900_60_the_late_time_potential_decay_source_computed_directly_and_the'
                          '_support_it_is_integrated_over')
SRC = os.path.join(R7900, 'srcdec')
sys.path.insert(0, R7842)
import score_ttteee as SC                                                   # noqa: E402

SUMS = [('S000', 0.00), ('S006', 0.06), ('S030', 0.30), ('S060', 0.60)]
BAND = (100, 207)
SPAN_BAR = 0.10          #: Ⓘ⓵ against Ⓘ⓶/Ⓘ⓷ — the full range over the mean, at Σ = 0
FAILS, RAN = [], []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def tt(tag, off=False):
    with np.load(os.path.join(SRC, 'lcdm_%s%s_tt.npz' % (tag, '_noisw' if off else '')),
                 allow_pickle=True) as z:
        return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def dec(tag, off=False):
    with np.load(os.path.join(SRC, 'lcdm_%s%s.npz' % (tag, '_noisw' if off else '')),
                 allow_pickle=True) as z:
        return (np.asarray(z['ls'], float), np.asarray(z['Dl_pairs'], float),
                [str(x) for x in z['pairs']])


def r7900_fraction(don, doff, ls):
    """`r7900`'s OWN definition, IN ITS OWN ARITHMETIC ORDER — sums over the band, the difference
    summed rather than the summands differenced, and the ratio taken last.

    ⛭ The FIRST form of this control took MEANS instead, which is the same number mathematically and
    a differently rounded one in double precision: it reproduced the banked fractions to `2.776e-16`,
    about five units in the last place, and so FAILED a bar that says exactly zero.  The bar was
    right and the arithmetic was mine, so the arithmetic is matched rather than the bar widened.
    """
    inb = (ls >= BAND[0]) & (ls <= BAND[1])
    tt_ = float(don[inb].sum())
    dd_ = float((don - doff)[inb].sum())
    return dd_ / tt_


def main():
    print(__doc__)
    print('=' * 100)

    # ── Ⓒ⓷ / Ⓒ⓸ the bins, READ from the likelihood, and the grid that covers them ───────────────
    ix = np.where(SC.BLOCK == 0)[0]
    lo, hi = SC.BIN_LO[ix], SC.BIN_HI[ix]
    inside = [int(i) for i in range(len(ix)) if lo[i] >= BAND[0] and hi[i] <= BAND[1]]
    edges = [(int(lo[i]), int(hi[i])) for i in inside]
    gate('Ⓒ⓷ the band the order names is EXACTLY a whole number of the likelihood\'s own `TT` bins, '
         'read from its `BIN_LO`/`BIN_HI` rather than typed — no partial bin, because `207` is a '
         'bin\'s own top edge — and the binning used below is the likelihood\'s own code, not a '
         're-implementation',
         len(inside) >= 1 and edges[0][0] == BAND[0] and edges[-1][1] == BAND[1],
         '%d bin(s), indices %d..%d, from %d to %d'
         % (len(inside), inside[0], inside[-1], edges[0][0], edges[-1][1]))

    ls0, _ = tt('S000')
    gate('Ⓒ⓸ every one of those bins is FULLY COVERED by the banked `l` grid, so none is partly '
         'extrapolated: the grid\'s first point is the first bin\'s own low edge',
         float(ls0[0]) <= edges[0][0] and float(ls0[-1]) >= edges[-1][1],
         'grid %g to %g over %d point(s), stride %g'
         % (ls0[0], ls0[-1], ls0.size, float(np.median(np.diff(ls0)))))

    # ── Ⓒ⓶ the switch-off arm identified from the RUN, never from the filename ──────────────────
    _lsd, _p_on, PAIRS = dec('S000')
    ISW = [i for i, p in enumerate(PAIRS) if 'isw' in p]
    OTH = [i for i, p in enumerate(PAIRS) if 'isw' not in p]
    zero_ok, ident_ok = True, True
    for tag, _s in SUMS:
        _, pon, _ = dec(tag)
        _, poff, _ = dec(tag, True)
        zero_ok = zero_ok and bool(np.all(poff[:, ISW] == 0.0))
        ident_ok = ident_ok and bool(np.array_equal(pon[:, OTH], poff[:, OTH]))
    gate('Ⓒ⓶ the switch-off arm is identified from the RUN and not from its filename: in every '
         'off-arm decomposition the four `isw` bilinear pairs are IDENTICALLY ZERO and the other six '
         'are BIT-IDENTICAL to the on-arm\'s. ⌗ *`r7900`\'s saved `config` does not record the '
         'switch, so a file called `_noisw` is otherwise only a file called `_noisw`*',
         zero_ok and ident_ok and len(ISW) == 4,
         '%d isw pair(s) %s zeroed on every off arm: %s; the other %d bit-identical: %s'
         % (len(ISW), [PAIRS[i] for i in ISW], zero_ok, len(OTH), ident_ok))

    # ── Ⓒ⓵ r7900's OWN definition recomputed from the same files, reproduced at exactly zero ────
    #: ⛭ AND THE TWO FILE FAMILIES ARE THE SAME SPECTRUM, checked rather than assumed: the control
    #:   below reads what `r7900` read, the per-bin shares read the `_tt` saves, and if those two
    #:   differed at all the control would license a reading of a different spectrum.
    fam = True
    for tag, _s in SUMS:
        for off in (False, True):
            _l1, _d1 = tt(tag, off)
            with np.load(os.path.join(SRC, 'lcdm_%s%s.npz' % (tag, '_noisw' if off else '')),
                         allow_pickle=True) as _z:
                fam = (fam and np.array_equal(_l1, np.asarray(_z['ls'], float))
                       and np.array_equal(_d1, np.asarray(_z['Dl'], float)))
    gate('Ⓒ⓵ᵃ the two file families `r7900` wrote — the decomposition\'s own total and the separate '
         '`TT` save — are BIT-IDENTICAL at every sum and on both arms, so the control below and the '
         'per-bin shares above are read off the same spectrum and not off two that agree closely',
         bool(fam), 'identical on all %d point(s): %s' % (2 * len(SUMS), bool(fam)))

    prev = json.load(io.open(os.path.join(R7900, 'isw_band.json'), encoding='utf-8'))
    mine, theirs = [], []
    for tag, s in SUMS:
        lsa, da = tt(tag)
        _lsb, db = tt(tag, True)
        mine.append(r7900_fraction(da, db, lsa))
        theirs.append(float(prev['per_sum'][tag]['fraction']))
    worst = float(np.max(np.abs(np.asarray(mine) - np.asarray(theirs))))
    gate('Ⓒ⓵ `r7900`\'s OWN band definition — the flat mean over its stride-8 grid points inside the '
         'band — recomputed HERE from the same files reproduces its banked fractions at EXACTLY '
         'ZERO. ⌗ *That is the one comparison in which the two definitions must agree to the last '
         'bit, and it is what licenses everything read on the new definition from the same files*',
         worst == 0.0,
         'worst difference %.3e over %d sum(s): %s against %s'
         % (worst, len(SUMS), ['%.6f' % v for v in mine], ['%.6f' % v for v in theirs]))

    # ── the shares ──────────────────────────────────────────────────────────────────────────────
    shares, full_b, noisw_b = {}, {}, {}
    for tag, s in SUMS:
        lsa, da = tt(tag)
        lsb, db = tt(tag, True)
        fb = np.asarray(SC._bin_one(lsa, da, 'TT'), float)[inside]
        nb = np.asarray(SC._bin_one(lsb, db, 'TT'), float)[inside]
        assert np.all(np.isfinite(fb)) and np.all(np.isfinite(nb)), tag
        shares[tag] = list((fb - nb) / fb)
        full_b[tag], noisw_b[tag] = list(fb), list(nb)

    print('\nⒾ⓵  THE TWELVE SHARES, BIN BY BIN')
    print('     bin      l range   ' + '  '.join('Σ=%4.2f  ' % s for _, s in SUMS)
          + '   S(0.60)−S(0)')
    s0 = np.asarray(shares[SUMS[0][0]], float)
    s3 = np.asarray(shares[SUMS[-1][0]], float)
    for j, i in enumerate(inside):
        print('      %2d   %4d - %4d   ' % (i, edges[j][0], edges[j][1])
              + '  '.join('%9.6f' % shares[t][j] for t, _ in SUMS)
              + '    %+10.3e' % (s3[j] - s0[j]))

    span = float((s0.max() - s0.min()) / s0.mean())
    mono = bool(np.all(np.diff(s0) > 0) or np.all(np.diff(s0) < 0))
    resp = s3 - s0
    print('\n    span at Σ = 0: %.6f  (bar %.2f);  monotone in l: %s' % (span, SPAN_BAR, mono))
    print('    the Σ response runs %+.3e to %+.3e' % (resp.min(), resp.max()))

    # ── UNREGISTERED, AND SAID TO BE: two things the registered outcomes do not capture ─────────
    turn = [j for j in range(1, len(s0)) if s0[j] > s0[j - 1]]
    print('\nⓊ    UNREGISTERED — two facts the registered outcomes do not carry')
    if turn:
        j = turn[0]
        print('    ⓵ The share FALLS across the band after ONE step up: the only rise is bin %d over '
              'bin %d,' % (inside[j], inside[j - 1]))
        print('      by %.3e, and from there it declines in every one of the remaining %d step(s).'
              % (s0[j] - s0[j - 1], len(s0) - 1 - len(turn)))
        print('      ⌗ So `Ⓘ⓷` fires on a SINGLE turning point at the band\'s own low edge, which is '
              'a weaker')
        print('        statement than `not monotone` sounds: the share runs %.6f at the top against '
              '%.6f' % (s0[-1], s0[j]))
        print('        at the peak, a fall of %.4f per cent across the %d bins above it.'
              % (100.0 * (1.0 - s0[-1] / s0[j]), len(s0) - 1 - j))
    else:
        print('    ⓵ The share falls across the whole band with no turning point.')
    print('    ⓶ The Σ RESPONSE itself falls with `l`: %+.3e in the lowest bin against %+.3e in the '
          'highest,' % (resp[0], resp[-1]))
    print('      a factor of %.4f, and it declines in every step (%s).'
          % (resp[0] / resp[-1], 'monotone' if np.all(np.diff(resp) < 0) else 'NOT monotone'))
    print('      ⌗ *So the band-integrated rise `r7900` measured is carried disproportionately by '
          'the band\'s low edge.*')

    out = verdict(span, mono, resp)
    print('\n  OUTCOME  %s' % ' + '.join(out['outcomes']))
    print('  %s' % out['note'])

    # ── the comparison, registered and NOT READABLE ─────────────────────────────────────────────
    print('\nⓍ    THE COMPARISON WITH THE REFERENCE — NAMED AS WAITING, NOT READ')
    print('    `cc66`\'s CAMB side is its `⑲ ③` and has not landed, and the order says neither side')
    print('    reads the other until both are banked. So `Ⓧ⓵`/`Ⓧ⓶` are NOT READABLE here, no')
    print('    shortfall exists, and the order\'s "follow it to its term" is not begun — the three')
    print('    candidate terms it names are a decomposition OF a shortfall.')

    rec = dict(band=list(BAND), bins=inside, edges=[list(e) for e in edges],
               sums=[[t, s] for t, s in SUMS], shares=shares, full_binned=full_b,
               noisw_binned=noisw_b, span_at_zero=span, monotone_in_ell=mono,
               response=[float(v) for v in resp],
               r7900_definition_reproduced=dict(worst=worst, mine=[float(v) for v in mine],
                                                banked=[float(v) for v in theirs]),
               span_bar=SPAN_BAR, comparison_readable=False,
               unregistered=dict(rises_at=[int(inside[j]) for j in turn],
                                 fall_from_peak_frac=float(1.0 - s0[-1] / s0.max()),
                                 response_ratio_low_over_high=float(resp[0] / resp[-1]),
                                 response_monotone=bool(np.all(np.diff(resp) < 0))),
               ran=RAN, failed=FAILS, **out)
    io.open(os.path.join(HERE, 'isw_bins.json'), 'w', encoding='utf-8').write(
        json.dumps(rec, indent=1, ensure_ascii=False, sort_keys=True))
    print('\n  wrote isw_bins.json')
    print('  ran %d gate(s), %d failed%s' % (len(RAN), len(FAILS),
                                             (': ' + ', '.join(FAILS)) if FAILS else ''))
    return 1 if FAILS else 0


def verdict(span, mono, resp):
    """PURE. The registered outcome glyphs, from the registered bar and the measured numbers only."""
    outs = ['Ⓘ⓵' if span < SPAN_BAR else ('Ⓘ⓶' if mono else 'Ⓘ⓷')]
    pos = int(np.sum(resp > 0.0))
    neg = int(np.sum(resp < 0.0))
    zer = int(np.sum(resp == 0.0))
    if pos and neg:
        outs.append('Ⓚ⓶')
    elif pos or neg:
        outs.append('Ⓚ⓵')
    if zer:
        outs.append('Ⓚ⓷')
    return dict(outcomes=outs, n_positive=pos, n_negative=neg, n_zero=zer,
                note='the share is %s in l%s, and the Σ response is %s'
                     % ('FLAT' if span < SPAN_BAR else 'STRUCTURED',
                        ' and monotone' if mono else ' and not monotone',
                        'one sign in every bin' if not (pos and neg) else 'MIXED in sign'))


if __name__ == '__main__':
    sys.exit(main())
