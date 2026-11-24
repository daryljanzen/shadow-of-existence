"""r7865+cc66: ARE THIS REVISION'S PINS FAILABLE?  Perturb the records, watch the receipt redden.

Each trial edits one of the two reduced records in place, runs the receipt, records which arm
labels reddened, and restores from a BYTE COPY the driver made itself -- then re-reads the baseline
and compares hashes, so a trial that failed to restore cannot pass as a clean run.

** EVERY TRIAL NAMES THE ARM IT IS FOR, and the driver prints a miss. **  At `r7861` a trial was
found to exercise a different arm than it was written for, and a driver that asks only whether
SOMETHING reddened cannot see that.

Run: python3 -I verify_failable.py
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_repaired_background_agrees_with_camb_at_the_ordered_setting_but_the_'
                    'ordered_neff_is_a_conflation_and_the_memo_fix_moves_the_limit_by_nothing.py')
assert os.path.isfile(RCPT), RCPT
BG = os.path.join(HERE, 'background_read.json')
EX = os.path.join(HERE, 'exact_memo_read.json')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run():
    p = subprocess.run([sys.executable, RCPT], capture_output=True, text=True)
    return p.returncode, [ln.strip()[6:24] for ln in p.stdout.splitlines()
                          if ln.strip().startswith('FAIL ')]


def edit(path, fn):
    d = json.load(open(path))
    fn(d)
    json.dump(d, open(path, 'w'), indent=1)


TRIALS = [
    ('Ⓐ① the CAMB leg made to disagree with theirs', BG,
     lambda d: d.__setitem__('worst_rel_vs_sixty_camb', 2.0e-05)),
    ('Ⓑ② the ordered ruler made to dip below', BG,
     lambda d: d['settings']['ordered_0.0293'].update(all_above=False, n_below=1)),
    ('Ⓒ③ the ordered worst gap pushed past its tolerance', BG,
     lambda d: d['settings']['ordered_0.0293'].__setitem__('worst_abs_gap', 6.0e-03)),
    ('Ⓓ④ the worst H point moved off the earliest z', BG,
     lambda d: d['settings']['ordered_0.0293'].__setitem__('H_worst_at_z', 1)),
    ('Ⓔ⑤ the density improvement dropped under three', BG,
     lambda d: d.__setitem__('rho_improvement_ordered', 2.0)),
    ('Ⓕ⑥ the order figure made to equal N_eff', BG,
     lambda d: d['order_figure'].__setitem__('massless_plus_integer', d['order_figure']['N_eff'])),
    ('Ⓕ⑦ the gap to three changed', BG,
     lambda d: d['order_figure'].__setitem__('gap_to_three', 0.0293)),
    ('Ⓕ⑧ the measured figure made uniformly above too', BG,
     lambda d: d['settings']['measured_0.044'].update(all_above=True, n_below=0)),
    ('Ⓖ⑩ the limit made to move on the published grid', EX,
     lambda d: d['grids']['published_20001'].update(exact=54.6, moved=0.6)),
    ('Ⓖ⑪ the fine-grid bound inflated', EX,
     lambda d: d['grids']['fine_400001'].__setitem__('moved', -0.4)),
    ('Ⓖ⑫ one re-derivation term made non-zero', EX,
     lambda d: d['rederive_worst'].__setitem__('chi2_bao', 1.0e-06)),
    ('Ⓖ⑬ a point moved outside the attributed residue', EX,
     lambda d: d.__setitem__('worst_move_in_total', 9.0e-03)),
    ('Ⓖ⑭ a re-run point put on the box boundary', EX,
     lambda d: d.__setitem__('all_interior', False)),
]


def main():
    copies = {p: p + '.bytecopy' for p in (BG, EX)}
    for p, c in copies.items():
        shutil.copy2(p, c)
    h0 = {p: sha(p) for p in copies}
    rc, red = run()
    print('  baseline before any edit: rc=%d, %d red' % (rc, len(red)), flush=True)
    if rc != 0:
        print('  ⛔ the baseline is not green -- nothing below would mean anything')
        return 1
    out, ok = {}, 0
    for name, path, fn in TRIALS:
        edit(path, fn)
        rc, red = run()
        for p, c in copies.items():
            shutil.copy2(c, p)
            assert sha(p) == h0[p], 'restore failed on %s' % name
        want = name.split()[0]
        hit = any(r.startswith(want) for r in red)
        ok += bool(rc != 0 and hit)
        out[name] = dict(rc=rc, reddened=red, intended_arm_reddened=hit)
        print('  %-54s rc=%d  reddened %d: %s  intended %s'
              % (name, rc, len(red), red, 'YES' if hit else '⛔ NO'), flush=True)
    rc, red = run()
    print('  baseline re-read after every restore: rc=%d, %d red' % (rc, len(red)))
    for c in copies.values():
        os.remove(c)
    json.dump(out, open(os.path.join(HERE, 'verify_failable.json'), 'w'),
              indent=1, ensure_ascii=False)
    print('\n  ⇒ %d of %d trials reddened the receipt AT THE ARM THEY WERE FOR, every file restored '
          'byte-for-byte, baseline green before and after: %s'
          % (ok, len(TRIALS), 'OK' if ok == len(TRIALS) and rc == 0 else '⛔ NOT OK'))
    return 0 if (ok == len(TRIALS) and rc == 0) else 1


if __name__ == '__main__':
    raise SystemExit(main())
