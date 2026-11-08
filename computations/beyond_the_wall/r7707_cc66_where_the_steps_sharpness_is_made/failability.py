#!/usr/bin/env python3
"""`r7707+cc66` FAILABILITY -- every pin in the inserted block, perturbed, with the NAMED check red.

The block's own source and the host's `_locate` are READ OUT OF THE RECEIPT, never copied, so a leg
that passes is a statement about the text in the tree.  Upstream names the block reuses (`_FB`, `_ST`)
are rebuilt here as mutable objects; the banks the block loads itself are perturbed by pointing `SP` at
a scratch directory of doctored copies.

⛔ The harness's own control runs FIRST and must be green: without it a leg's red is not evidence.
⛔ A leg reporting `0` FAIL is a leg that found NOTHING -- `r7705`'s leg A perturbed TOWARDS its gate
   and said so, and `r7703`'s leg B is why that is read correctly the first time.
"""
import json
import os
import shutil
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SPEC0 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_a_source_with_no_physics_reproduces_the_contrast_and_'
                    'the_two_clocks_part_company_at_the_visibility.py')
SRC_BANKS = ('r6911_source_lcdm_leafrec1.npz', 'r6911_source_cr_leafrec1.npz', 'r6911_source_lcdm.npz')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC                                                        # noqa: E402
import own_comb_kinds as OCK                                                 # noqa: E402


def _lines():
    return open(RCPT, encoding='utf-8').read().split('\n')


def slices():
    """(the host's `_locate`, the `r7707` block) sliced out of the receipt by their own markers"""
    src = _lines()
    a = next(i for i, l in enumerate(src) if l.startswith('def _locate(fn):'))
    b = next(i for i, l in enumerate(src) if i > a and l.startswith('# the seven bands, both sides'))
    c = next(i for i, l in enumerate(src) if l.startswith('_SRCB, _SRCM = {}, {}'))
    while not src[c].startswith('# ===='):
        c -= 1
    d = next(i for i, l in enumerate(src) if i > c and l.startswith('print("=" * 100)'))
    return '\n'.join(src[a:b]), a + 1, '\n'.join(src[c:d]), c + 1, d


def fine_banks():
    out = {}
    for t, n in (('lcdm', 'r6941_fine_lcdm'), ('cr', 'r6941_fine_cr_leafrec1')):
        z = np.load(os.path.join(SPEC0, n + '.npz'), allow_pickle=True)
        out[t] = (z['ls'].astype(float) / float(z['l_A']), np.asarray(z['Dl'], float).copy())
    return out


def scratch_spec(tmp, edits=None):
    """a `SP` the block can load, with the source banks it loads optionally doctored"""
    os.makedirs(tmp, exist_ok=True)
    edits = edits or {}
    for fn in SRC_BANKS:
        src = os.path.join(SPEC0, fn)
        if fn not in edits:
            shutil.copy(src, os.path.join(tmp, fn))
            continue
        z = np.load(src, allow_pickle=True)
        d = {k: np.asarray(z[k]).copy() for k in z.files}
        edits[fn](d)
        np.savez(os.path.join(tmp, fn), **d)
    return tmp


def run(name, must_redden, edits=None, up=None):
    with tempfile.TemporaryDirectory() as tmp:
        spec = scratch_spec(os.path.join(tmp, 'spec'), edits)
        loc, la, blk, ba, bb = slices()
        red, lab = [], []

        def check(nm, cond, got=None):
            lab.append(nm)
            if not cond:
                red.append(nm)

        FB = fine_banks()
        ns = dict(np=np, os=os, json=json, sys=sys, SP=spec, check=check, OCK=OCK, OC=OC, _FB=FB)
        exec(compile(loc, f'{RCPT}:{la}', 'exec'), ns)
        ns['_ST'] = OCK.own_state(FB, 'mean', 1.0)
        if up is not None:
            up(ns)
        exec(compile(blk, f'{RCPT}:{ba}-{bb}', 'exec'), ns)
        hit = [l for l in red if must_redden in l]
        ok = bool(hit) if must_redden else not red
        print(f"  {'OK  ' if ok else 'FAIL'}  {name}")
        if must_redden:
            print(f"          must redden ....... {must_redden!r}")
        print(f"          checks run / red .. {len(lab)} / {len(red)}"
              + ("   ⛔ NOTHING REDDENED -- the leg found nothing" if must_redden and not red else ""))
        for l in red:
            print(f"          red: {l[:100]}")
        return ok


def main():
    loc, la, blk, ba, bb = slices()
    print(f"\n  under test: {os.path.relpath(RCPT, ROOT)}")
    print(f"    the host's `_locate` at line {la}; the `r7707` block at lines {ba}-{bb}, "
          f"{len(blk.splitlines())} lines, {blk.count('check(')} gates\n")

    ok = [run("0  THE CONTROL: the block unperturbed, through this harness", None)]
    if not ok[0]:
        print("  ⛔ the harness does not reproduce the green run; no leg below is evidence")
        return 1
    print()

    def ed_dm(d):
        d['D_M'] = np.asarray(float(d['D_M']) * 1.02)
    ok.append(run("A  a source bank's D_M scaled by 1.02 (the abscissa identity)",
                  'ONE VARIABLE ONLY UNDER', {'r6911_source_cr_leafrec1.npz': ed_dm}))

    def ed_lift(d):
        d['S_i'] = np.asarray(d['S_i'], float) + 3.0        # lift S_i clear of zero
    ok.append(run("B  S_i lifted by +3 so its envelope no longer crosses zero",
                  'FREQUENCY-MATCHED OBJECT', {'r6911_source_cr_leafrec1.npz': ed_lift}))

    def ed_k(d):
        d['k'] = np.asarray(d['k'], float) * 1.06           # stretch the source abscissa
    ok.append(run("C  the source k grid stretched 6 per cent (breaks the comb match to D_l)",
                  'FREQUENCY-MATCHED OBJECT', {'r6911_source_cr_leafrec1.npz': ed_k}))

    def ed_cfg(d):
        c = json.loads(str(d['config'].item()))
        c.pop('STACKPERT', None)
        d['config'] = np.array(json.dumps(c), dtype=object)
    ok.append(run("D  STACKPERT struck from a source bank's own config",
                  'the source banks are the declared ones', {'r6911_source_cr_leafrec1.npz': ed_cfg}))

    def ed_alt(d):
        d['S_i'] = np.asarray(d['S_i'], float) * 1.001      # namesake no longer byte-identical
    ok.append(run("E  the control's NAMESAKE bank made to differ in S_i (the inertness claim)",
                  'the source banks are the declared ones', {'r6911_source_lcdm.npz': ed_alt}))

    def up_flat(ns):
        ns['_ST']['oa'] = np.interp(ns['_ST']['ua'], ns['_ST']['xc'], ns['_ST']['oc'])
    ok.append(run("F  the arm's spectrum residual replaced by the control's (the step removed)",
                  'the step is in the arm/control ratio', up=up_flat))

    def up_rise(ns):
        _s = 1.0 + 0.9 * (ns['_ST']['ua'] - ns['_ST']['ua'].min()) / np.ptp(ns['_ST']['ua'])
        ns['_ST']['oa'] = ns['_ST']['oa'] * _s
        _t = 1.0 + 0.9 * (ns['_ST']['xc'] - ns['_ST']['xc'].min()) / np.ptp(ns['_ST']['xc'])
        ns['_ST']['oc'] = ns['_ST']['oc'] * _t
    ok.append(run("G  both arms' own band RMS made to RISE (the locator's domain claim)",
                  "NEITHER ARM'S OWN PROJECTED SPECTRUM", up=up_rise))

    def ed_step(d):
        x = np.asarray(d['k'], float) * float(d['r_s']) / np.pi
        d['S_i'] = np.asarray(d['S_i'], float) * np.where(x > 1.783, 1.035, 1.0)
    ok.append(run("H  a step of the SPECTRA's size injected into the arm's source",
                  'NOT IN THE SOURCE-SIDE RATIO', {'r6911_source_cr_leafrec1.npz': ed_step}))

    def up_ramp(ns):
        _u = (ns['_ST']['ua'] - 0.85) / (3.0 - 0.85)
        ns['_ST']['oa'] = ns['_ST']['oa'] * (1.0 + 0.30 * np.clip(_u, 0, 1))
    ok.append(run("I  the spectra ratio replaced by a broad monotone ramp (the translation control)",
                  'WHICH OF THE TWO IS A LOCATION', up=up_ramp))

    print(f"\n  the control is green and {sum(ok[1:])} of {len(ok) - 1} legs reddened their named check")
    if not all(ok):
        return 1
    print("  ✓ EVERY PIN IN THE BLOCK IS FAILABLE")
    return 0


if __name__ == '__main__':
    sys.exit(main())
