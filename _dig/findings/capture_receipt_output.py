#!/usr/bin/env python3
"""Run every receipt once and cache its stdout for DRAFT_check_numbers_at_citations.py.

Needs: numpy scipy sympy camb pynucastro.  Sets PYTHONPATH to storyboard_receipts/ so that
receipts/P15_CR_cosmology/ROBUST_p1p2_scan.py can resolve its sibling import (see F01 sec C --
without that shim it is the one receipt of the 249 that cannot run in place).
Runtime ~40 min; bbn_network.py alone is several minutes.
"""
import os, subprocess, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RCPT = os.path.join(ROOT, 'receipts')
DEST = '/tmp/rcpt_out/all.json'
os.makedirs(os.path.dirname(DEST), exist_ok=True)
env = dict(os.environ); env['PYTHONPATH'] = os.path.join(ROOT, 'storyboard_receipts')
out = {}
for dp, dirs, files in os.walk(RCPT):
    dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git')]
    for f in sorted(files):
        if not f.endswith('.py'):
            continue
        p = os.path.join(dp, f); rel = os.path.relpath(p, RCPT)
        try:
            r = subprocess.run([sys.executable, p], capture_output=True, text=True,
                               timeout=1800, cwd=dp, env=env)
            out[rel] = r.stdout + "\n" + r.stderr
            print(f"  [{r.returncode}] {rel}")
        except Exception as e:
            out[rel] = f"<<ERR>> {e}"
            print(f"  [ERR] {rel}: {e}")
json.dump(out, open(DEST, 'w'))
print(f"\ncached {len(out)} receipt outputs -> {DEST}")
