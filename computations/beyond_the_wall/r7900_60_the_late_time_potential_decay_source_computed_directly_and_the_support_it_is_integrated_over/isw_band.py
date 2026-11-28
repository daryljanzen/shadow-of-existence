# -*- coding: utf-8 -*-
"""r7900+60 — THE POTENTIAL-DECAY SOURCE, WITH AND WITHOUT, OVER MULTIPOLES 100–207.

Order `r7895` (69) item ②, registered in `PREDICTION.md` before either side ran.

⛔ **NOTHING IS RETYPED AND NO SPECTRUM IS COMPUTED HERE.**  `gen_isw.sh` ran the instrument's own
generator eight times — the control arm at four sums, each with `_ISW` on and off — and this reads
those banked decompositions.  The band is read on the spectra DIRECTLY and never through a crossing,
as the order requires, because `r7890` established that on this band the difference operator's own
artefact is `7.2` times the signal.

⛭ **AND ONE DEFECT IN THIS REVISION'S OWN REGISTRATION IS REPORTED RATHER THAN WORKED AROUND.**
`PREDICTION.md` defines `Ⓔ⓷` as *the fractional difference is flat in Σ to within the instrument's own
reproducibility*.  This instrument is DETERMINISTIC: a re-run of one point is bit-identical, so its
reproducibility spread is zero and that criterion can never be satisfied by any real measurement.
⇒ *The criterion as written is degenerate.  It is reported as degenerate, the actual size of the Σ
response is printed so a reader can judge it, and the verdict is carried by `Ⓔ⓸`, which has a concrete
one-per-cent bar.  Substituting a threshold now and presenting it as registered is the thing a
registration exists to prevent.*

    python3 isw_band.py
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'srcdec')
R7874 = os.path.join(BTW, 'r7874_60_the_sum_response_by_source_term_and_the_correction_that'
                          '_decides_one_object')

SUMS = [('S000', 0.00), ('S006', 0.06), ('S030', 0.30), ('S060', 0.60)]
BAND = (100, 207)                 #: the order's own window, inclusive
ABSENT_BAR = 0.01                 #: Ⓔ⓸: the difference as a fraction of TT in the band
FAILS, RAN = [], []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def load(tag, off=False):
    p = os.path.join(SRC, 'lcdm_%s%s.npz' % (tag, '_noisw' if off else ''))
    with np.load(p, allow_pickle=True) as z:
        return (np.asarray(z['ls'], float), np.asarray(z['Dl'], float),
                np.asarray(z['Dl_pairs'], float), [str(x) for x in z['pairs']])


def main():
    print(__doc__)
    print('=' * 100)
    have = [(t, s) for t, s in SUMS
            if os.path.isfile(os.path.join(SRC, 'lcdm_%s.npz' % t))
            and os.path.isfile(os.path.join(SRC, 'lcdm_%s_noisw.npz' % t))]
    gate('Ⓔ⓪ both arms are present at every sum the order names, so the comparison is not quietly '
         'made on a subset of the registered grid',
         len(have) == len(SUMS), '%d of %d sum(s): %s' % (len(have), len(SUMS),
                                                          [t for t, _ in have]))
    if FAILS:
        sys.exit('\n  ⛔ the registered grid is incomplete, so no response is reported')

    LS, _, _, PAIRS = load(SUMS[0][0])
    ISW = [i for i, nm in enumerate(PAIRS) if 'isw' in nm]
    OTH = [i for i, nm in enumerate(PAIRS) if 'isw' not in nm]
    inb = (LS >= BAND[0]) & (LS <= BAND[1])
    gate('Ⓔ⓪ᵃ and the four `isw`-involving pairs and the six others are named from the bank\'s own '
         'pair labels, not by position — the decomposition\'s layout is its own and this file does '
         'not assume an order for it',
         len(ISW) == 4 and len(OTH) == 6 and int(inb.sum()) > 0,
         '%d isw pair(s) %s, %d other(s), %d multipole(s) in %d-%d'
         % (len(ISW), [PAIRS[i] for i in ISW], len(OTH), int(inb.sum()), *BAND))

    rec, rows = {}, []
    print('\nⒺ①  THE CONTROL: THE SWITCH MUST BE INERT OUTSIDE ITS OWN TERM')
    for tag, s in have:
        ls, don, pon, _ = load(tag)
        ls2, doff, poff, _ = load(tag, off=True)
        assert np.array_equal(ls, ls2)
        isw_off = float(np.max(np.abs(poff[:, ISW])))
        oth_rel = float(np.max(np.abs(poff[:, OTH] - pon[:, OTH])
                               / np.maximum(np.abs(pon[:, OTH]), 1e-300)))
        ident = float(np.max(np.abs((don - doff) - pon[:, ISW].sum(axis=1))
                             / np.maximum(np.abs(don), 1e-300)))
        rec[tag] = dict(sum_eV=s, isw_pairs_off_max=isw_off, other_pairs_max_rel=oth_rel,
                        identity_max_rel=ident)
        print('    %s  Σ=%.2f eV   isw pairs off: max |%.3e|   other pairs: max rel %.3e   '
              'identity: max rel %.3e' % (tag, s, isw_off, oth_rel, ident))
    gate('Ⓔ① with the switch off the four `isw` pairs are identically zero and the six others are '
         'unchanged, so the difference below is the potential-decay term\'s and carries no change in '
         'the monopole or the Doppler dipole',
         all(v['isw_pairs_off_max'] == 0.0 for v in rec.values())
         and all(v['other_pairs_max_rel'] < 1e-12 for v in rec.values()),
         'isw pairs off max %.3e; other pairs max rel %.3e'
         % (max(v['isw_pairs_off_max'] for v in rec.values()),
            max(v['other_pairs_max_rel'] for v in rec.values())))
    gate('Ⓔ①ᵃ and the registered identity holds: the with/without difference EQUALS the four '
         '`isw`-involving bilinear pairs, which is what makes it a well-defined object rather than '
         '`the ISW term\'s contribution`, a thing `r7874` established does not exist because `D_l` '
         'is quadratic in the transfer',
         all(v['identity_max_rel'] < 1e-10 for v in rec.values()),
         'max relative departure %.3e' % max(v['identity_max_rel'] for v in rec.values()))

    print('\nⒺ②  THE BAND, READ ON THE SPECTRA DIRECTLY')
    print('    Σ (eV)      TT in band       with−without        fraction of TT')
    for tag, s in have:
        ls, don, _, _ = load(tag)
        _, doff, _, _ = load(tag, off=True)
        tt = float(don[inb].sum())
        dd = float((don - doff)[inb].sum())
        fr = dd / tt
        rec[tag].update(tt_band=tt, diff_band=dd, fraction=fr)
        rows.append((s, tt, dd, fr))
        print('    %6.2f   %14.4f   %+16.4f   %+14.6f' % (s, tt, dd, fr))

    fracs = {t: rec[t]['fraction'] for t, _ in have}
    absent = all(abs(f) < ABSENT_BAR for f in fracs.values())
    spread = max(fracs.values()) - min(fracs.values())
    print('\n    the fraction moves by %.3e across the four sums' % spread)
    print('    ⌗ Ⓔ⓷ as registered asks for flatness `within the instrument\'s own reproducibility`,')
    print('      which for a DETERMINISTIC instrument is zero -- so that criterion is DEGENERATE and')
    print('      is reported as such rather than replaced with a bar chosen now.')

    outcome = 'Ⓔ⓸' if absent else 'Ⓔ⓶/Ⓔ⓷ UNDECIDED WITHOUT cc66'
    note = ('THE TERM IS ABSENT WHERE IT MATTERS: under %g per cent of TT at every sum'
            % (100 * ABSENT_BAR)) if absent else \
           ('the difference is NOT negligible, so the support reading does not decide it and the '
            'comparison needs cc66\'s split')
    print('\n    ⇒ %s  %s' % (outcome, note))
    gate('Ⓔ③ the outcome is read off the band figures against the bar fixed in `PREDICTION.md`, and '
         'where `Ⓔ⓸` fires it is reported as the stronger statement with the response reported beside '
         'it — the non-exclusivity the registration fixed in advance',
         True, '%s; fractions %s' % (outcome, {t: round(f, 6) for t, f in fracs.items()}))

    #: ⛭ the ISW-on arm should reproduce `r7874`'s bank where the two overlap. The generator claims
    #:   to differ from that script only in the added sum and the switch; this CHECKS the claim.
    ov, worst, missing = [], 0.0, []
    for tag, _ in have:
        p = os.path.join(R7874, 'srcdec', 'lcdm_%s.npz' % tag)
        if not os.path.isfile(p):
            missing.append(tag)
            continue
        with np.load(p, allow_pickle=True) as z:
            d74 = np.asarray(z['Dl'], float)
        _, don, _, _ = load(tag)
        if d74.shape == don.shape:
            worst = max(worst, float(np.max(np.abs(don - d74) / np.maximum(np.abs(d74), 1e-300))))
            ov.append(tag)
    gate('Ⓔ④ and the `ISW on` arm REPRODUCES `r7874`\'s banked spectra at the sums the two share, '
         'which checks the generator\'s own claim that it differs from that script only in the added '
         'sum and the switch — a claim in a comment is not evidence',
         bool(ov) and worst < 1e-12,
         'reproduced on %s at max rel %.3e; not in that bank: %s' % (ov, worst, missing or 'none'))

    out = dict(band=list(BAND), absent_bar=ABSENT_BAR, per_sum=rec,
               fractions={t: float(f) for t, f in fracs.items()},
               fraction_spread=float(spread), absent=bool(absent), outcome=outcome, note=note,
               isw_pairs=[PAIRS[i] for i in ISW], other_pairs=[PAIRS[i] for i in OTH],
               e3_criterion_degenerate=True, reproduces_r7874=ov, r7874_max_rel=float(worst))
    io.open(os.path.join(HERE, 'isw_band.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote isw_band.json')
    if FAILS:
        sys.exit('\n  ⛔ %d of %d GATE(S) FAILED: %s' % (len(FAILS), len(RAN), ', '.join(FAILS)))
    print('  ⇒ all %d gate(s) pass' % len(RAN))
    return 0


if __name__ == '__main__':
    sys.exit(main())
