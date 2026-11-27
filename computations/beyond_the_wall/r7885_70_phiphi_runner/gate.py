#!/usr/bin/env python3
"""r7885+70: the provenance gate for 60's lensing grid built on GitHub runners.  A REFUSAL, NOT A WARNING.

The expected configuration of every point is READ FROM 60's GENERATOR, `gen_phiphi_nuhier.sh`, and not
retyped here: the point list (arms x positive sum nodes), each arm's background numbers, and the switch
assignments on each arm's `env` line.  A banked point passes only if the record it wrote -- its own
`switches`, `arm`, `tag`, `mnu`, `etaref` -- matches what the generator was meant to set for it.

  gate.py --list                      print the generator's points, one `<arm> <tag>` per line
  gate.py --check <dir> <arm> <tag>   gate one point; exit 1 on any mismatch
  gate.py --manifest <dir>            gate every point found in <dir>, write <dir>/MANIFEST.json;
                                      exit 1 unless all of the generator's points pass

⌗ THE CROSS-MACHINE CONTROL.  Where the repository already banks a point (60's container ran it), the
  runner's bandpowers are compared with the banked ones.  A relative difference above `XMACH_BAR` is a
  refusal; the value is reported either way, as dlk's C1 was.
"""
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(HERE, '..', 'r7884_60_the_controls_limits_on_the_jointly_validated_sector',
                   'gen_phiphi_nuhier.sh')
BANKED = os.path.join(HERE, '..', 'bank', 'phiphi_grid_eta4000_bvel1_primnorm1_nuhier')
XMACH_BAR = 1e-6
NBANDS = 9
ETAREF = 4000.0


def parse_generator():
    src = open(GEN).read()
    num = dict(re.findall(r'\b((?:CR|LC)_(?:H0|OM|WB|NS))=([0-9.]+)', src))
    nodes = re.findall(r'"([0-9.]+) (S\d+)"', src)
    arms = re.search(r'for arm in ([a-z ]+); do', src).group(1).split()
    envs = re.findall(r'env (BVEL=1[^\n]*?)\\\n\s*(MNU="\$mnu"[^\n]*?)\\', src)
    if len(envs) != 2 or not nodes or not arms:
        sys.exit('GATE: the generator no longer parses as r7884 wrote it -- refusing rather than guessing')
    per_arm = {}
    for (l1, l2), arm in zip(envs, ['cr', 'lcdm']):        # the `if [ "$arm" = cr ]` branch comes first
        per_arm[arm] = dict(re.findall(r'(\w+)="?([^"\s]*)"?', l1 + ' ' + l2))
    pre = {'cr': 'CR', 'lcdm': 'LC'}
    points = []
    for arm in arms:
        for mnu, tag in nodes:
            sub = {'$h0': num[f'{pre[arm]}_H0'], '$om': num[f'{pre[arm]}_OM'],
                   '$wb': num[f'{pre[arm]}_WB'], '$ns': num[f'{pre[arm]}_NS'], '$mnu': mnu,
                   '$arm': arm, '$tag': tag}
            sw = {k: sub.get(v, v) for k, v in per_arm[arm].items()}
            points.append((arm, tag, float(mnu), sw))
    return points


RECORDED = ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'MNU', 'HIER', 'BVEL', 'NUFD', 'PRIMNORM',
            'NUHIER', 'NQ', 'LMAXNU', 'QMAXNU', 'LMAXL', 'LSTEP', 'LEAFGEOM', 'LEAFSCALES', 'ZSTART')


def check(d, arm, tag, points):
    exp = [p for p in points if p[0] == arm and p[1] == tag]
    if not exp:
        return dict(ok=False, why=f'{arm} {tag} is not a point of the generator')
    _, _, mnu, sw = exp[0]
    path = os.path.join(d, f'{arm}_{tag}.json')
    if not os.path.isfile(path):
        return dict(ok=False, why='no record written')
    rec = json.load(open(path))
    why = []
    if rec.get('placeholder'):
        why.append('a seeding placeholder, not a point')
    if rec.get('arm') != arm or rec.get('tag') != tag:
        why.append(f"record names {rec.get('arm')} {rec.get('tag')}")
    if rec.get('mnu') != mnu:
        why.append(f"mnu {rec.get('mnu')} != {mnu}")
    if rec.get('etaref') != ETAREF:
        why.append(f"etaref {rec.get('etaref')} != {ETAREF}")
    want = {k: v for k, v in sw.items() if k in RECORDED}
    got = rec.get('switches', {})
    for k in sorted(set(want) | set(got)):
        if want.get(k) != got.get(k):
            why.append(f'switch {k}: recorded {got.get(k)!r}, generator sets {want.get(k)!r}')
    bp = rec.get('bandpowers') or []
    if len(bp) != NBANDS or not all(isinstance(x, float) and math.isfinite(x) for x in bp):
        why.append(f'bandpowers: {len(bp)} values, not {NBANDS} finite ones')
    out = dict(ok=not why, why='; '.join(why) or None)
    banked = os.path.join(BANKED, f'{arm}_{tag}.json')
    if os.path.isfile(banked) and len(bp) == NBANDS:
        ref = json.load(open(banked)).get('bandpowers') or []
        if len(ref) == NBANDS:
            rel = max(abs(a - b) / max(abs(b), 1e-300) for a, b in zip(bp, ref))
            out['xmach_rel'] = rel
            if rel > XMACH_BAR:
                out['ok'] = False
                out['why'] = '; '.join(filter(None, [out['why'],
                                                     f'cross-machine: {rel:.2e} > {XMACH_BAR:g} against the banked point']))
    return out


def main(argv):
    points = parse_generator()
    if argv[:1] == ['--list']:
        for arm, tag, _, _ in points:
            print(arm, tag)
        return 0
    if argv[:1] == ['--check'] and len(argv) == 4:
        r = check(argv[1], argv[2], argv[3], points)
        print(f"  GATE {argv[2]} {argv[3]}: {'PASS' if r['ok'] else 'REFUSE -- ' + r['why']}"
              + (f"   (cross-machine against the banked point: {r['xmach_rel']:.2e})" if 'xmach_rel' in r else ''))
        return 0 if r['ok'] else 1
    if argv[:1] == ['--manifest'] and len(argv) == 2:
        d = argv[1]
        man = {}
        for arm, tag, _, _ in points:
            r = check(d, arm, tag, points)
            tp = os.path.join(d, f'{arm}_{tag}.timing.json')
            if os.path.isfile(tp):
                r['timing'] = json.load(open(tp))
            man[f'{arm}_{tag}'] = r
            print(f"  {arm:4s} {tag}: {'PASS  ' if r['ok'] else 'REFUSE'}"
                  f"  wall {r.get('timing', {}).get('wall_s', '-')!s:>6} s"
                  + (f"  xmach {r['xmach_rel']:.2e}" if 'xmach_rel' in r else '')
                  + ('' if r['ok'] else f"  ({r['why']})"))
        json.dump(man, open(os.path.join(d, 'MANIFEST.json'), 'w'), indent=1, sort_keys=True)
        npass = sum(r['ok'] for r in man.values())
        print(f'  {npass} of {len(man)} points pass')
        return 0 if npass == len(man) else 1
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
