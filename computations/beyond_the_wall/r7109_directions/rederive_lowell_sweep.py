#!/usr/bin/env python3
"""r7109 ⓷ -- ** THE PRODUCER FOR `spectra/cc66_lowell_sweep.npz`, WRITTEN INTO THE REPOSITORY. **

`70`'s provenance audit lists this bank as load-bearing for a registered receipt and a published
figure with **no producer in the repository**, and offers two ways to close it: re-derive, or write
the producer in.  ** This does both: it re-derives every banked key, and it IS the producer. **

⛭ ** THE ENGINE IS NOT DUPLICATED HERE -- IT IS READ OUT OF THE RECEIPT THAT OWNS IT. **
`P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling` carries the arm-B harness
(`_RUN`, `armB`, `r0_of`, the two backgrounds).  *Copying that text into this file would create a
second engine that can drift from the first silently, which is the defect class this corpus keeps
naming.*  So the receipt's source is parsed and exactly those definitions are exec'd -- nothing else
runs, because the receipt computes at import.

⚠ ** THE CONFIGURATIONS ARE READ OFF THE BANKED KEYS' OWN NAMES, not out of my memory of them. **
Each key spells its own variant, background and knobs; this file maps the name to the environment
and says so in one table.  *The two command lines the receipt prints in its PART 5 are the
specification; this is that specification made executable.*

** IDEMPOTENT AND RESUMABLE. **  Each configuration's result is appended to the JSON as it lands, so
a container reclaim costs at most the in-flight configuration.  The DECOUPLED variant is ~9 minutes
a configuration, which is why this is a launcher and not a receipt body.

Run:  python3 rederive_lowell_sweep.py [--out /tmp/n66/lowell_rederive.json]
"""
import argparse
import ast
import json
import os
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
BANK = os.path.join(SPEC, 'cc66_lowell_sweep.npz')

# ** the banked keys' own names, mapped to the environment each one spells. **  `armB` pops every
#   knob before applying these, so an ABSENT key here means the module's own default -- which is
#   what `FROZEN_control_default_cut_z_53_5_KLO_0_1` says in its name.
FROZEN = dict(ZEND=0, NTAU=150000, KLO=0.1, NLOW=480)
CASES = [
    ('FROZEN_control_KLO_0_1', 'CTL', FROZEN),
    ('FROZEN_control_KLO_0_02', 'CTL', dict(FROZEN, KLO=0.02)),
    ('FROZEN_adjudicated_KLO_0_1', 'ADJ', FROZEN),
    ('FROZEN_control_NTAU_300000', 'CTL', dict(FROZEN, NTAU=300000)),
    # the module's DEFAULT cut: ZEND omitted, which is what "default_cut_z_53_5" names
    ('FROZEN_control_default_cut_z_53_5_KLO_0_1', 'CTL', dict(NTAU=150000, KLO=0.1, NLOW=480)),
    ('DECOUPLED_control_KLO_0_1_NS3_60000', 'CTL',
     dict(NTAU=150000, ZDEC=200, NS3=60000, KLO=0.1, NLOW=480)),
    ('DECOUPLED_adjudicated_KLO_0_1_NS3_60000', 'ADJ',
     dict(NTAU=150000, ZDEC=200, NS3=60000, KLO=0.1, NLOW=480)),
    ('DECOUPLED_control_NS3_30000', 'CTL',
     dict(NTAU=150000, ZDEC=200, NS3=30000, KLO=0.1, NLOW=480)),
]


def engine():
    """the receipt's own arm-B harness, read out of its source rather than copied into this file"""
    tree = ast.parse(open(RECEIPT, encoding='utf-8').read())
    want_assign = {'_RUN', 'C', 'NS', 'CTL', 'ADJ', 'R0'}
    want_func = {'r0_of', 'armB'}
    keep = []
    for n in tree.body:
        if isinstance(n, ast.Assign):
            names = set()
            for t in n.targets:
                if isinstance(t, ast.Name):
                    names.add(t.id)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    names |= {e.id for e in t.elts if isinstance(e, ast.Name)}
            if names & want_assign:
                keep.append(n)
        elif isinstance(n, ast.FunctionDef) and n.name in want_func:
            keep.append(n)
    ns = {'os': os, 'sys': sys, 'subprocess': subprocess, 'np': np,
          'HIER_DIR': os.path.join(ROOT, 'storyboard_receipts')}
    exec(compile(ast.Module(body=keep, type_ignores=[]), '<engine>', 'exec'), ns)
    missing = {k for k in want_assign | want_func} - set(ns)
    if missing:
        raise SystemExit(f"the receipt no longer defines {sorted(missing)} -- the engine has moved")
    return ns


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='/tmp/n66/lowell_rederive.json')
    a = ap.parse_args(argv)
    ns = engine()
    bg = {'CTL': ns['CTL'], 'ADJ': ns['ADJ']}
    SW = np.load(BANK)
    out = {}
    if os.path.exists(a.out):
        out = json.load(open(a.out))
        print(f"  resuming: {len(out)} of {len(CASES)} already done")
    for key, which, env in CASES:
        if key in out:
            print(f"  skip {key} (done)")
            continue
        t0 = time.time()
        v, meta = ns['armB'](bg[which], **env)
        if v is None:
            print(f"  FAILED {key}: {meta}")
            out[key] = {'error': str(meta)}
        else:
            b = np.asarray(SW[key], float)
            v = np.asarray(v, float)
            n = min(len(b), len(v))
            out[key] = {'live': [float(x) for x in v[:n]],
                        'bank': [float(x) for x in b[:n]],
                        'secs': round(time.time() - t0, 1), 'meta': str(meta)[:200]}
            worst = float(np.max(np.abs(v[:n] - b[:n])))
            rnd = float(np.max(np.abs(np.round(v[:n], 4) - b[:n])))
            out[key]['worst_abs'] = worst
            out[key]['worst_after_rounding_to_4dp'] = rnd
            print(f"  done {key} in {out[key]['secs']}s   worst |live-bank| = {worst:.3e}   "
                  f"after rounding live to 4 dp = {rnd:.3e}")
        json.dump(out, open(a.out, 'w'), indent=1)
    print(f"\n  wrote {a.out}  ({len([k for k in out if 'live' in k or 'live' in out[k]])} of "
          f"{len(CASES)} configurations)")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
