#!/usr/bin/env python3
r"""r7857 item ② -- ** WHICH OF THE SIX WOULD `FOURPI` MOVE, MEASURED RATHER THAN REASONED. **

Each receipt is run TWICE in its own process: once as it stands, once with every instrument TT `Dl`
the bank hands it doubled (`fourpi_child.py`, which states why doubling IS the regenerated bank).
What is reported per receipt: its exit code both ways, the labels of any check that changes verdict,
and every printed number that moves, with the ratio it moved by.

⛔ ** THE POSITIVE CONTROL IS THE WHOLE RELIABILITY OF THIS SWEEP. **  A probe that patches a key no
receipt reads would report `nothing moves` for every receipt and look like a clean result.  So a
patched run that doubled ZERO arrays is REFUSED as vacuous, per receipt, and the audit exits
non-zero rather than printing a reassuring table.  (`60`'s own sweep failed exactly this way first.)

Usage: python3 fourpi_audit.py [--mode tt|all] [--out <json>] [receipt.py ...]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
# ⛔ ** `ROOT` IS ASSERTED AND NOT COUNTED ON: two `dirname` calls instead of three is exactly
#   how `60`'s own sweep came out empty and looked clean (`r7858` ⓷).  I reproduced that defect
#   here on the first run of this file, which is why the assertion is here rather than trusted. **
assert os.path.isdir(RCPT), f'the receipts directory must be under ROOT -- {RCPT} is not a directory'
CHILD = os.path.join(HERE, 'fourpi_child.py')

# ** THE SIX 60's SWEEP ROUTED TO THIS SEAT, in the order `r7857` ② names them. **
SIX = ['P15_the_model_difference_is_an_acoustic_contrast_difference_and_it_is_not_one_skys_luck.py',
       'P15_the_monopole_zero_point_is_not_the_channel_and_the_two_residuals_point_opposite_ways.py',
       'P15_the_no_fit_confrontation_is_three_per_bin_and_its_residual_carries_a_nine_sigma_'
       'modulation_at_the_combs_own_period_which_binning_at_that_period_cancels.py',
       'P15_the_period_difference_null_is_not_significant_because_the_control_has_no_measurable_'
       'period_and_the_offset_is_exactly_a_phase_drift_at_fixed_ell_A.py',
       'P15_the_projection_read_recombination_at_the_wrong_conformal_time_and_one_clock_moves_it_72_'
       'per_cent.py',
       'P15_the_two_channels_compose_multiplicatively_and_the_pair_is_flat_where_the_excess_grows.py']

NUM = re.compile(r'[-+]?\d+\.\d+(?:[eE][-+]?\d+)?|[-+]?\d+(?:[eE][-+]?\d+)?')
# ⛔ both shapes this sector's receipts print: `FAIL  <label>` and `[FAIL] <label>`.  The
#   first version of this line knew only the first, and reported `0 FAIL` for a receipt whose
#   log it had just printed with two `[FAIL]` lines in it.
FAILLINE = re.compile(r'^\s*(?:⛔ ?)?(?:FAIL|\[FAIL\])\s+(.*)$')


def run(cmd, env=None, timeout=3600):
    t = time.time()
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, errors='replace',
                       env={**os.environ, **(env or {})}, timeout=timeout)
    return p.stdout + p.stderr, p.returncode, time.time() - t


def fails(txt):
    return [m.group(1).strip() for ln in txt.splitlines() for m in [FAILLINE.match(ln)] if m]


def moved(base, pat):
    """every printed number that moves, line-aligned; the trailer lines are the child's own"""
    b = [ln for ln in base.splitlines()]
    q = [ln for ln in pat.splitlines() if not ln.startswith('__FOURPI_')]
    out, n = [], min(len(b), len(q))
    for i in range(n):
        if b[i] == q[i]:
            continue
        xb, xq = NUM.findall(b[i]), NUM.findall(q[i])
        if len(xb) != len(xq):
            out.append((b[i].strip()[:150], q[i].strip()[:150], None))
            continue
        for u, v in zip(xb, xq):
            fu, fv = float(u), float(v)
            if abs(fv - fu) > 1e-9 * max(1.0, abs(fu)):
                out.append((b[i].strip()[:150], q[i].strip()[:150],
                            (fv / fu) if fu != 0 else None))
                break
    return out, (len(b), len(q))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', default='tt', choices=('tt', 'all'))
    ap.add_argument('--out', default=os.path.join(HERE, 'fourpi_audit.json'))
    ap.add_argument('receipts', nargs='*')
    a = ap.parse_args()
    names = a.receipts or SIX
    rec, vac = {}, []
    for nm in names:
        p = (nm if os.path.isabs(nm) else
             (os.path.abspath(nm) if os.path.exists(nm) else os.path.join(RCPT, nm)))
        if not os.path.exists(p):
            print(f'  ⛔ REFUSED: {nm} is not a file.  Nothing is run and nothing is asserted.')
            return 2
        short = os.path.basename(p)[4:60]
        print('=' * 104)
        print(f'  {os.path.basename(p)}')
        print('=' * 104)
        b, rb, tb = run([sys.executable, p])
        q, rq, tq = run([sys.executable, CHILD, p], env={'MODE': a.mode})
        hits = re.search(r'__FOURPI_HITS__ (\d+) (\[.*\])', q)
        nh = int(hits.group(1)) if hits else 0
        op = re.search(r'__FOURPI_OPENED__ (\d+) ', q)
        no = int(op.group(1)) if op else 0
        mv, (lb, lq) = moved(b, q)
        fb, fq = fails(b), fails(q)
        rec[os.path.basename(p)] = dict(rc_base=rb, rc_doubled=rq, arrays_doubled=nh,
                                        archives_opened=no,
                                        which=hits.group(2) if hits else '', lines=(lb, lq),
                                        fails_base=fb, fails_doubled=fq, moved=mv,
                                        secs=(round(tb, 1), round(tq, 1)))
        print(f'    base rc={rb} ({tb:.0f} s)   doubled rc={rq} ({tq:.0f} s)   '
              f'npz opened: {no}   arrays doubled: {nh}')
        if nh == 0 and no > 0:
            vac.append(os.path.basename(p))
            print('    ⛔ VACUOUS: this receipt opens archives and the patch reached NONE of them.  '
                  'Nothing is asserted about it.')
            continue
        if nh == 0:
            print('    ⌗ READS NO BANK AT ALL: there is no instrument spectrum in this receipt\'s '
                  'run to double, so `FOURPI` cannot reach it AT RUN TIME.  What it STATES is read '
                  'by hand below, because a figure stated as a literal is not protected by being '
                  'unreachable.')
            continue
        print(f'    checks that change verdict: base {len(fb)} FAIL -> doubled {len(fq)} FAIL')
        for lbl in fq:
            print(f'        ⛔ {lbl[:140]}')
        if not mv:
            print('    ⇒ ** INVARIANT: not one printed number moves. **')
        else:
            print(f'    ⇒ {len(mv)} printed line(s) move:')
            for u, v, r in mv[:14]:
                print(f'        - {u}')
                print(f'        + {v}' + (f'    [x{r:.6g}]' if r else '    [shape]'))
    print('=' * 104)
    json.dump(rec, open(a.out, 'w'), indent=1)
    print(f'  written -> {os.path.relpath(a.out, ROOT)}')
    if vac:
        print(f'  ⛔ REFUSED: the probe doubled nothing in {len(vac)} receipt(s): {vac}.  A sweep '
              f'whose patch does not reach its subject reports a clean result for the wrong reason.')
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
