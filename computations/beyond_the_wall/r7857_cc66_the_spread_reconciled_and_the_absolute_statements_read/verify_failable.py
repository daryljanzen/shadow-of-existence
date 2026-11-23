#!/usr/bin/env python3
r"""r7857+cc66.3 -- ** ARE THIS RECEIPT'S PINS FAILABLE?  PERTURB WHAT IT READS AND SEE. **

Seven perturbations, each applied IN PLACE to the thing the receipt actually reads, each restored
from a byte copy this script made itself (never from a version-control checkout -- that is the
`r7855` defect, where the committed copy predated a field the receipt read and the later passes died
before any arm and printed no failures at all).

⛔ ** AND IT RE-READS ITS OWN BASELINE AT THE END. **  A perturbation loop that crashes prints no
failures, which looks exactly like a receipt with no failable pins.  So the baseline is run first
AND last, both asserted green, and every restored file's sha256 is compared with the one taken
before the first edit.

Usage: python3 verify_failable.py
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), f'ROOT is wrong: {ROOT}'
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_spread_was_not_like_for_like_and_fourpi_moves_none_of_the_six_but_it_'
                    'breaks_a_closure_the_sweep_did_not_look_for.py')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
BK = os.path.join(HERE, '_bk')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run(path=None):
    p = subprocess.run([sys.executable, path or RCPT], cwd=ROOT, capture_output=True, text=True,
                       errors='replace')
    red = [ln.strip()[6:60] for ln in (p.stdout + p.stderr).splitlines()
           if ln.strip().startswith('FAIL  ')]
    return p.returncode, red, (p.stdout + p.stderr)


def jedit(path, fn):
    d = json.load(open(path))
    fn(d)
    json.dump(d, open(path, 'w'), indent=1)


def main():
    os.makedirs(BK, exist_ok=True)
    targets = {k: os.path.join(HERE, k) for k in
               ('spread_reconciled.json', 'oscillation_at_peaks.json', 'fourpi_audit_six.json',
                'fourpi_figure_probe.json', 'fourpi_audit_pairs.json')}
    targets['instrument'] = INST
    targets['receipt'] = RCPT
    before = {}
    for k, p in targets.items():
        shutil.copy2(p, os.path.join(BK, os.path.basename(p)))
        before[k] = sha(p)
    rc0, red0, _ = run()
    print(f"  baseline before any edit: rc={rc0}, {len(red0)} red")
    if rc0 != 0 or red0:
        print('  ⛔ REFUSED: the baseline is not green, so nothing below would mean anything.')
        return 2

    def restore(k):
        shutil.copy2(os.path.join(BK, os.path.basename(targets[k])), targets[k])
        assert sha(targets[k]) == before[k], f'{k} did not restore'

    res = {}

    def trial(name, k, mutate):
        mutate()
        rc, red, _ = run()
        restore(k)
        res[name] = (rc, red)
        print(f"  {name:34s} rc={rc}  reddened {len(red)}: {[r.split(' ')[0] for r in red]}")

    trial('a spread moved by 0.001', 'spread_reconciled.json',
          lambda: jedit(targets['spread_reconciled.json'],
                        lambda d: d[list(d)[0]].__setitem__('spread',
                                                             d[list(d)[0]]['spread'] + 0.001)))
    trial('the third peak moved 0.1 per cent', 'oscillation_at_peaks.json',
          lambda: jedit(targets['oscillation_at_peaks.json'],
                        lambda d: d['peak_812'].__setitem__('departure_per_cent', 2.435)))
    trial('one of the six given a FAIL', 'fourpi_audit_six.json',
          lambda: jedit(targets['fourpi_audit_six.json'],
                        lambda d: d[list(d)[0]].__setitem__('fails_doubled', ['invented'])))
    trial('one of the six made unreachable', 'fourpi_audit_six.json',
          lambda: jedit(targets['fourpi_audit_six.json'],
                        lambda d: d[list(d)[0]].__setitem__('arrays_doubled', 0)))
    trial('the figure bank at 65 keys', 'fourpi_figure_probe.json',
          lambda: jedit(targets['fourpi_figure_probe.json'], lambda d: d.__setitem__('keys', 65)))
    trial('the live bank reported touched', 'fourpi_figure_probe.json',
          lambda: jedit(targets['fourpi_figure_probe.json'],
                        lambda d: d.__setitem__('live_unchanged', False)))
    trial('one of the seven red arms dropped', 'fourpi_audit_pairs.json',
          lambda: jedit(targets['fourpi_audit_pairs.json'],
                        lambda d: [v.__setitem__('fails_doubled', v['fails_doubled'][:1])
                                   for v in d.values() if len(v['fails_doubled']) == 2][:1]))

    # ** AND THE GAP ITSELF CLOSED, which is the one perturbation that must NOT redden the
    #   implication arm -- `Ⓔ⑭` is written so that 60 adding `_FP_ACC` to `_dec` makes its
    #   antecedent false.  `Ⓔ⑮`, which records the gap as it stands, MUST redden. **
    src = open(INST).read()
    old = "                    _dec[j, _c] = (1.0 if _a == _b else 2.0) * np.sum(P * _Dl[_a] * _Dl[_b])"
    assert old in src, 'the decomposition line must be found by its own text before it is edited'
    open(INST, 'w').write(src.replace(
        old, old.replace('np.sum(P * _Dl[_a] * _Dl[_b])', 'np.sum(P * _Dl[_a] * _Dl[_b]) * _FP_ACC')))
    rc, red, _ = run()
    restore('instrument')
    res['60 closes the gap on `_dec`'] = (rc, red)
    print(f"  {'60 closes the gap on `_dec`':34s} rc={rc}  reddened {len(red)}: "
          f"{[r.split(' ')[0] for r in red]}")

    # ** and the invariance arm itself: hold the amplitude instead of fitting it, in a COPY of the
    #   receipt beside it (its ROOT is three directories up from its own file, so a copy elsewhere
    #   would read a different tree). **
    tmp = os.path.join(os.path.dirname(RCPT), '_r7857_failable_tmp.py')
    s = open(RCPT).read()
    assert "    A = float(m @ _FI @ _d / (m @ _FI @ m))" in s
    open(tmp, 'w').write(s.replace("    A = float(m @ _FI @ _d / (m @ _FI @ m))",
                                   "    A = 1.0"))
    try:
        rc, red, _ = run(tmp)
    finally:
        os.remove(tmp)
    assert not os.path.exists(tmp), 'the temporary copy must be gone'
    res['the amplitude HELD, not fitted'] = (rc, red)
    print(f"  {'the amplitude HELD, not fitted':34s} rc={rc}  reddened {len(red)}: "
          f"{[r.split(' ')[0] for r in red]}")

    rc1, red1, _ = run()
    print(f"  baseline re-read after every restore: rc={rc1}, {len(red1)} red")
    ok = (rc1 == 0 and not red1 and all(sha(p) == before[k] for k, p in targets.items())
          and all(v[0] != 0 and v[1] for n, v in res.items()))
    json.dump({n: dict(rc=v[0], reddened=v[1]) for n, v in res.items()},
              open(os.path.join(HERE, 'verify_failable.json'), 'w'), indent=1)
    shutil.rmtree(BK)
    print(f"\n  ⇒ {sum(1 for v in res.values() if v[1])} of {len(res)} perturbations reddened the "
          f"receipt, every file restored byte-for-byte, baseline green before and after: "
          f"{'OK' if ok else '⛔ NOT OK'}")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
