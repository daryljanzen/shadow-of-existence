#!/usr/bin/env python3
"""r7650 (60) -- for each ABSENT figure, RUN the receipt that does compute it, so a MIS-CITATION is
proved by a run and not by a grep.  *A wrong address is only a finding if the right one exists.*"""
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

CAND = {
    '0.958': ['P15_the_phase_moves_with_the_datum_and_only_the_spacing_does_not',
              'C22_the_end_to_end_number'],
    '298.0': ['P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_the_172_is_the_'
              'radiation_free_ruler',
              'P15_the_likelihood_pair_is_another_instruments_and_the_crossing_run_needed_a_'
              'missing_knob'],
    '12.5': ['P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_'
             'position_not_amplitude'],
    '0.75': ['P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_'
             'position_not_amplitude'],
}
JOBS = sorted({n for v in CAND.values() for n in v})


def one(name):
    if name not in G.FILES:
        return name, 'NO-SUCH-RECEIPT', ''
    env = dict(os.environ, NODE='60')
    for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[k] = '1'
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, G.FILES[name]],
                           cwd=os.path.dirname(G.FILES[name]) or ROOT,
                           capture_output=True, text=True, timeout=900, env=env)
        txt, st = (r.stdout or '') + (r.stderr or ''), f'rc={r.returncode}'
    except subprocess.TimeoutExpired as e:
        txt = (e.stdout or b'').decode('utf-8', 'replace') if isinstance(e.stdout, bytes) else (e.stdout or '')
        st = 'UNRUN'
    print(f"  {st:<6} {time.time() - t0:>7.1f}s  {name[:66]}", flush=True)
    return name, st, txt


print(f"running {len(JOBS)} candidate computing receipt(s)")
with ThreadPoolExecutor(max_workers=3) as ex:
    got = {n: (st, txt) for n, st, txt in ex.map(one, JOBS)}

print("\n  figure   PRINTED BY                                                      state")
proof = {}
for fig, names in sorted(CAND.items()):
    for n in names:
        st, txt = got.get(n, ('MISSING', ''))
        hit = fig in txt
        print(f"  {fig:>7}  {('✓ ' if hit else '  ') + n[:60]:<64} {st}")
        if hit:
            proof.setdefault(fig, []).append(n)
json.dump(proof, open(os.path.join(HERE, 'miscitations.json'), 'w'), indent=1)
print(f"\n  proved by a run: {sorted(proof)}")
