"""r7863+cc66: ARE THIS REVISION'S PINS FAILABLE?  Perturb the record, watch the receipt redden.

A green receipt proves nothing unless its arms would go red on a wrong number.  Each trial edits
`cuts_and_node.json` in place, runs the receipt, records which arm labels reddened, and restores the
file from a BYTE COPY the driver made itself -- then re-reads the baseline at the end and compares
hashes, so a trial that failed to restore cannot be mistaken for a clean run.

⌗ *At `r7861` one trial was found to exercise no arm it was supposed to -- the TE perturbation moved
a field a different arm read -- so here every trial names the arm it is FOR and the driver prints
what actually reddened, which is the only way the mismatch becomes visible.*

Run: python3 -I verify_failable.py
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# THREE dirnames: this file sits two directories below the repository root, and writing two
# here is the FOURTH instance of that defect in this seat's work today -- the assertion is
# what caught every one of them instantly, which is why it is the standing answer and care
# is not.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_both_ell_cuts_cost_little_and_the_low_end_costs_less_than_the_top_so_'
                    'sixtys_asymmetry_does_not_reproduce_and_the_reference_is_one_branch_to_'
                    'point_six_eV.py')
assert os.path.isfile(RCPT), RCPT
TARGET = os.path.join(HERE, 'cuts_and_node.json')
BACKUP = TARGET + '.bytecopy'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run():
    p = subprocess.run([sys.executable, RCPT], capture_output=True, text=True)
    red = [ln.strip()[6:24] for ln in p.stdout.splitlines() if ln.strip().startswith('FAIL ')]
    return p.returncode, red


def edit(fn):
    d = json.load(open(TARGET))
    fn(d)
    json.dump(d, open(TARGET, 'w'), indent=1)


TRIALS = [
    ('Ⓐ② a leg made to TIGHTEN its limit',
     lambda d: d['cuts']['rd_min|bot1800'].__setitem__('move_meV', -0.9)),
    ('Ⓑ④ the top-1800 cost pushed past its bound',
     lambda d: d['cuts']['rd_min|top1800'].__setitem__('move_meV', 6.5)),
    ('Ⓒ⑥ the first ratio raised above ten',
     lambda d: d['bot_over_top'].__setitem__('rd_min|1800', 12.0)),
    ('Ⓒ⑦ the second ratio raised above ten',
     lambda d: d['bot_over_top'].__setitem__('rd_min|1500', 11.0)),
    ('Ⓒ⑧ the one ratio above one brought below it',
     lambda d: d['bot_over_top'].__setitem__('rd_camb|1800', 0.9)),
    ('Ⓓ⑩ the calibrated arm made to move MORE than the minimised',
     lambda d: d['cuts']['rd_camb|top1500'].__setitem__('move_meV', 9.9)),
    ('Ⓔ⑫ a cold start made to land lower',
     lambda d: d['node']['rd_min'].__setitem__('any_cold_lower', True)),
    ('Ⓔ⑬ a step made to exceed the three-times-mean bound',
     lambda d: d['node']['rd_camb'].__setitem__('max_within_bound', False)),
    ('Ⓕ⑭ the calibrated landing point moved outside its interval',
     lambda d: d['node']['rd_camb'].__setitem__('H0_at_060', 67.9)),
    ('Ⓖ⑮ the minimised landing point moved onto the other pipeline\'s value',
     lambda d: d['node']['rd_min'].__setitem__('H0_at_060', 65.70)),
    ('Ⓗ⑰ the covered-bin figure changed',
     lambda d: [c.__setitem__('removed', [c['removed'][0], 555, c['removed'][2]])
                for c in d['cuts'].values()]),
]


def main():
    shutil.copy2(TARGET, BACKUP)
    h0 = sha(TARGET)
    rc, red = run()
    print('  baseline before any edit: rc=%d, %d red' % (rc, len(red)), flush=True)
    if rc != 0:
        print('  ⛔ the baseline is not green -- nothing below would mean anything')
        return 1
    out, ok = {}, 0
    for name, fn in TRIALS:
        edit(fn)
        rc, red = run()
        shutil.copy2(BACKUP, TARGET)
        assert sha(TARGET) == h0, 'restore failed on %s' % name
        want = name.split()[0]
        hit = any(r.startswith(want) for r in red)
        ok += bool(rc != 0 and hit)
        out[name] = dict(rc=rc, reddened=red, intended_arm_reddened=hit)
        print('  %-62s rc=%d  reddened %d: %s  intended arm %s'
              % (name, rc, len(red), red, 'YES' if hit else '⛔ NO'), flush=True)
    rc, red = run()
    print('  baseline re-read after every restore: rc=%d, %d red' % (rc, len(red)))
    os.remove(BACKUP)
    json.dump(out, open(os.path.join(HERE, 'verify_failable.json'), 'w'),
              indent=1, ensure_ascii=False)
    print('\n  ⇒ %d of %d trials reddened the receipt AT THE ARM THEY WERE FOR, every file restored '
          'byte-for-byte, baseline green before and after: %s'
          % (ok, len(TRIALS), 'OK' if ok == len(TRIALS) and rc == 0 else '⛔ NOT OK'))
    return 0 if (ok == len(TRIALS) and rc == 0) else 1


if __name__ == '__main__':
    raise SystemExit(main())
