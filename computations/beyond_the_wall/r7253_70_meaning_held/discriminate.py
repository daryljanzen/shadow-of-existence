#!/usr/bin/env python3
"""r7253+70.1, 66's reachable negative: can the MEANING-HELD gate tell a HELD finding from an UNREAD key?
Every UNADJUDICATED PAPER/SENTENCE key is stamped `held at <HEAD>` -- a key nobody read -- and run through the gate
with and without H5 (the held commit must have CHANGED the receipt)."""
import os, sys, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as Q
head = Q._git('rev-parse', 'HEAD').stdout.strip()
base = Q.read_baseline()
pop = [(k, v) for k, v in sorted(base.items()) if v[3] == Q.UNREAD and v[0] == 'PAPER' and v[1] == 'SENTENCE']
for prov, label in ((False, 'H1-H4'), (True, 'H1-H5')):
    fails = collections.Counter()
    for (rc, lit), v in pop:
        r = Q.held_check(rc, lit, v[0], v[1], f'held at {head[:12]}', provenance=prov)
        fails[r[:2] if r else 'PASS'] += 1
    n = fails['PASS']
    print(f'  {label}: {n} of {len(pop)} unread keys stamped at HEAD pass ({100 * n / len(pop):.1f}%)   {dict(fails)}')

# NOT PRE-REGISTERED, and the test that matters: the ADVERSARIAL stamp.  A verdict-writer who knows H5 stamps each
# unread key with its OWN receipt's last commit, which satisfies H5 by construction.
fails = collections.Counter()
for (rc, lit), v in pop:
    sha = Q._git('log', '-1', '--format=%H', '--', rc).stdout.strip()
    r = Q.held_check(rc, lit, v[0], v[1], f'held at {sha[:12]}')
    fails[r[:2] if r else 'PASS'] += 1
n = fails['PASS']
print(f'  ADVERSARIAL (each stamped at its receipt\'s last commit), H1-H5: {n} of {len(pop)} pass '
      f'({100 * n / len(pop):.1f}%)   {dict(fails)}')
