# -*- coding: utf-8 -*-
"""r7886+60 — THE LENSING GRID'S CLOSURES, AND THEY ARE REFUSALS.

Order `r7885` (69) item ①. Run this on the runner AFTER `launch.sh`, before anything is pushed to a
`refs/ci` ref. It exits nonzero and prints what failed; a grid that does not pass is not a grid.

    python3 verify_grid.py <RUNNER_OUT_DIR> [--ref <COMMITTED_BANK_DIR>] [--json OUT]

⛔ **THE RUNNER MUST WRITE TO ITS OWN DIRECTORY, NOT THE COMMITTED BANK.** Six of the ten are
already banked in the checkout, and `launch.sh` skips a point whose output exists — so pointing
`PPOUT` at the committed bank would skip those six and leave `Ⓒ⓸` with nothing to compare. Point
`PPOUT` at a fresh directory (`$RUNNER_TEMP/pp_out`), let all ten recompute, and this script
compares them against the checkout's six.

THE CLOSURES, each registered in `PREDICTION.md` before any of this was written:
    Ⓒ⓵ COMPLETE      all ten points present and parseable; five sums on each of the two arms.
    Ⓒ⓶ PROVENANCE    every point carries the seven switches and its own sum, read OFF THE POINT.
    Ⓒ⓷ SHAPE         9 bandpowers over 36 multipoles, every value finite and positive.
    Ⓒ⓸ CROSS-MACHINE the six banked here, compared bandpower by bandpower, in three registered
                     states: `<= 1e-10` ACCEPT; `<= 1e-6` ACCEPT WITH THE MISS REPORTED; worse
                     REFUSE, the discrepancy being the finding.
    Ⓒ⓹ NO DRIFT      `points.json`'s per-arm environment still agrees with `r7884`'s generator,
                     so the frozen list cannot silently diverge from the landed command.
"""
import argparse
import io
import json
import math
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
GEN = os.path.join(_BTW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector',
                   'gen_phiphi_nuhier.sh')
FAILS = []


def gate(name, ok, got=None):
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name)
    return ok


def load(d):
    out = {}
    for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if f.endswith('.json'):
            try:
                out[f[:-5]] = json.load(io.open(os.path.join(d, f), encoding='utf-8'))
            except Exception as exc:                                        # noqa: BLE001
                out[f[:-5]] = {'__unreadable__': str(exc)}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--ref', default=None)
    ap.add_argument('--json', dest='js', default=None)
    a = ap.parse_args()

    spec = json.load(io.open(os.path.join(_HERE, 'points.json'), encoding='utf-8'))
    ref_dir = a.ref or os.path.join(_BTW, 'bank', spec['out_dir_name'])
    print(__doc__)
    print('=' * 100)
    print('  runner output : %s' % a.out)
    print('  reference     : %s' % ref_dir)

    got = load(a.out)
    ref = load(ref_dir)
    want = {'%s_%s' % (p['arm'], p['tag']): p for p in spec['points']}
    rec = {'out': a.out, 'ref': ref_dir, 'n_got': len(got), 'n_ref': len(ref)}

    # ── Ⓒ⓵ COMPLETE ─────────────────────────────────────────────────────────────────────────────
    missing = sorted(set(want) - set(got))
    unreadable = sorted(k for k, v in got.items() if '__unreadable__' in v)
    bysum = {}
    for k, p in want.items():
        if k in got and '__unreadable__' not in got[k]:
            bysum.setdefault(p['arm'], set()).add(round(float(got[k].get('mnu', -1)), 6))
    five = {0.06, 0.15, 0.3, 0.45, 0.6}
    gate('Ⓒ⓵ COMPLETE -- all ten points present and parseable, five sums on each of the two arms',
         not missing and not unreadable
         and bysum.get('lcdm') == bysum.get('cr') == five,
         'missing %s; unreadable %s; sums %s'
         % (missing or 'none', unreadable or 'none',
            {k: sorted(v) for k, v in sorted(bysum.items())}))

    # ── Ⓒ⓶ PROVENANCE ───────────────────────────────────────────────────────────────────────────
    need = spec['provenance_required']
    bad = []
    seen2 = 0
    for k in sorted(want):
        d = got.get(k)
        if not d or '__unreadable__' in d:
            continue
        seen2 += 1
        sw = d.get('switches', {})
        for key, val in sorted(need.items()):
            if str(sw.get(key)) != str(val):
                bad.append('%s records %s=%r, not %r' % (k, key, sw.get(key), val))
        if abs(float(d.get('mnu', -1)) - want[k]['mnu']) > 5e-07:
            bad.append('%s records mnu=%r, not %s' % (k, d.get('mnu'), want[k]['mnu']))
    gate('Ⓒ⓶ PROVENANCE -- every point carries the seven switches and its own sum, read OFF THE '
         'POINT and not off the generator that was meant to set them',
         not bad, '; '.join(bad[:4]) if bad
         else '%d point(s) EXAMINED x %d key(s)' % (seen2, len(need)))

    # ── Ⓒ⓷ SHAPE ────────────────────────────────────────────────────────────────────────────────
    nb, nl = spec['shape_required']['bandpowers'], spec['shape_required']['multipoles']
    bad3 = []
    seen3 = 0
    for k in sorted(want):
        d = got.get(k)
        if not d or '__unreadable__' in d:
            continue
        seen3 += 1
        bp, ls = d.get('bandpowers', []), d.get('ls', [])
        if len(bp) != nb or len(ls) != nl:
            bad3.append('%s is %d bandpower(s) over %d multipole(s)' % (k, len(bp), len(ls)))
            continue
        if not all(math.isfinite(v) and v > 0 for v in bp):
            bad3.append('%s has a non-finite or non-positive bandpower' % k)
    gate('Ⓒ⓷ SHAPE -- %d bandpowers over %d multipoles, every value finite and positive' % (nb, nl),
         not bad3, '; '.join(bad3[:4]) if bad3 else '%d point(s) EXAMINED' % seen3)

    # ── Ⓒ⓸ THE CROSS-MACHINE CONTROL ────────────────────────────────────────────────────────────
    shared = sorted(set(got) & set(ref) & set(want))
    worst, worst_at = 0.0, None
    for k in shared:
        g, r = got[k], ref[k]
        if '__unreadable__' in g or '__unreadable__' in r:
            continue
        gb, rb = g.get('bandpowers', []), r.get('bandpowers', [])
        if len(gb) != len(rb):
            worst, worst_at = float('inf'), '%s: %d against %d bandpowers' % (k, len(gb), len(rb))
            break
        for i, (x, y) in enumerate(zip(gb, rb)):
            den = max(abs(x), abs(y), 1e-300)
            d = abs(x - y) / den
            if d > worst:
                worst, worst_at = d, '%s band %d' % (k, i)
    rec['cross_machine'] = {'compared': len(shared), 'worst_rel': worst, 'worst_at': worst_at}
    accept, report = spec['cross_machine']['bar_accept'], spec['cross_machine']['bar_report']
    if not shared:
        state = 'NO OVERLAP -- nothing to control against'
    elif worst <= accept:
        state = 'Ⓒ⓸ᵃ ACCEPTED: the runner reproduces this container'
    elif worst <= report:
        state = 'Ⓒ⓸ᵇ ACCEPTED WITH THE MISS REPORTED'
    else:
        state = 'Ⓒ⓸ᶜ REFUSED: the discrepancy IS the finding and NO LIMIT IS READ'
    rec['cross_machine']['state'] = state
    gate('Ⓒ⓸ THE CROSS-MACHINE CONTROL -- the points banked in the checkout, compared bandpower by '
         'bandpower against the runner\'s own, against bars registered BEFORE these numbers existed',
         bool(shared) and worst <= report,
         '%d point(s) compared, worst relative %.3e at %s => %s'
         % (len(shared), worst, worst_at, state))
    if accept < worst <= report:
        print('  ⚠ Ⓒ⓸ᵇ: the miss is %.3e, worse than the %.0e accept bar and inside the %.0e '
              'report bar.\n     ** THIS FIGURE MUST BE PRINTED BESIDE THE LIMIT. **  A limit is '
              'read at a chi-squared\n     threshold of 2.71 and bandpowers agreeing to this cannot '
              'move a crossing of it.' % (worst, accept, report))

    # ── Ⓒ⓹ NO DRIFT ─────────────────────────────────────────────────────────────────────────────
    gsrc = io.open(GEN, encoding='utf-8').read() if os.path.exists(GEN) else ''
    drift = []
    for nm, key in (('CR_H0', 'CRH0'), ('CR_OM', 'CROM'), ('CR_WB', 'WBH2'), ('CR_NS', 'NS')):
        m = re.search(r'\b%s=([0-9.]+)' % nm, gsrc)
        v = {p['tag']: p['env'].get(key) for p in spec['points'] if p['arm'] == 'cr'}
        if not m or set(v.values()) != {m.group(1)}:
            drift.append('cr %s: generator %s, points.json %s'
                         % (key, m.group(1) if m else '(absent)', sorted(set(v.values()))))
    for nm, key in (('LC_H0', 'LH0'), ('LC_OM', 'LOM'), ('LC_WB', 'WBH2'), ('LC_NS', 'NS')):
        m = re.search(r'\b%s=([0-9.]+)' % nm, gsrc)
        v = {p['tag']: p['env'].get(key) for p in spec['points'] if p['arm'] == 'lcdm'}
        if not m or set(v.values()) != {m.group(1)}:
            drift.append('lcdm %s: generator %s, points.json %s'
                         % (key, m.group(1) if m else '(absent)', sorted(set(v.values()))))
    gate('Ⓒ⓹ NO DRIFT -- `points.json`\'s per-arm cosmology still agrees with `r7884`\'s landed '
         'generator, so the frozen list cannot diverge from the command it was read off',
         bool(gsrc) and not drift, '; '.join(drift[:3]) if drift else 'both arms, four numbers each')

    rec['failed'] = FAILS
    if a.js:
        json.dump(rec, io.open(a.js, 'w', encoding='utf-8'), indent=1, sort_keys=True, default=float)
    print('\n' + '=' * 100)
    print('  %d closure(s) failed' % len(FAILS))
    for f in FAILS:
        print('    FAILED: %s' % f)
    print('=' * 100)
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
