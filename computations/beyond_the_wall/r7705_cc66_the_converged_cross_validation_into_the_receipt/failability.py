#!/usr/bin/env python3
"""`r7705+cc66` FAILABILITY -- every pin in the inserted block, perturbed, with the NAMED check
watched go red.

The block's own source is READ OUT OF THE RECEIPT, never copied, so a leg that passes is a statement
about the text that is in the tree.  Upstream names the block reuses (`_LAZ`, `_LBZ`, `_LE`, `_ARMA`,
`_LDEC`, `_LFRO`, `_LAC`) are rebuilt here from the same banks, as dicts, so a leg can perturb them;
the two banks the block loads itself are perturbed by pointing `SPEC` at a scratch directory of
doctored copies.

⛔ A leg that reports 0 FAIL is a leg that found NOTHING -- `r7703`'s leg B is why that is said here.
Each leg therefore names the check it must redden and the run is only green if that check is among the
ones that failed."""
import json
import os
import shutil
import sys
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SPEC0 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
CVN = 'p15_lowell_depths_leafpert_convergence_leafrec1.npz'
FCN = 'p15_lowell_depths_frozen_converged_leafrec1.npz'


def block_source():
    """The inserted block, sliced out of the receipt by its own markers."""
    src = open(RCPT, encoding='utf-8').read().split('\n')
    a = next(i for i, l in enumerate(src) if l.startswith('_CVP = os.path.join(SPEC,'))
    while not src[a].startswith('# ===='):
        a -= 1
    b = next(i for i, l in enumerate(src) if i > a and l.startswith('# ===='))
    return '\n'.join(src[a:b]), a + 1, b


def banks(spec):
    """_LAZ / _LBZ as mutable dicts carrying .item()-able configs, plus the derived rows."""
    out = {}
    for nm, fn in (('_LAZ', 'p15_lowell_depths_armA_leafpert_leafrec1.npz'),
                   ('_LBZ', 'p15_lowell_depths_leafpert_leafrec1.npz')):
        z = np.load(os.path.join(spec, fn), allow_pickle=True)
        out[nm] = {k: (np.array(str(z[k].item()), dtype=object) if k in ('config', 'manifest')
                       else np.asarray(z[k]).copy()) for k in z.files}
    E = list(np.asarray(out['_LAZ']['ells'], int))
    out['_LE'] = E
    out['_ARMA'] = {l: float(np.asarray(out['_LAZ']['distances__armA__L'], float)[E.index(l)]) for l in range(2, 9)}
    out['_LDEC'] = {l: float(np.asarray(out['_LBZ']['distances__armB_decoupled__L'], float)[E.index(l)])
                    for l in range(2, 9)}
    out['_LFRO'] = {l: float(np.asarray(out['_LBZ']['distances__armB_frozen__L'], float)[E.index(l)])
                    for l in range(2, 9)}
    out['_LAC'] = json.loads(str(out['_LAZ']['config'].item()))
    return out


def scratch_spec(tmp, edit_cv=None, edit_fc=None):
    """A SPEC the block can load, with the two banks it loads optionally doctored."""
    os.makedirs(tmp, exist_ok=True)
    for fn, ed in ((CVN, edit_cv), (FCN, edit_fc)):
        src = os.path.join(SPEC0, fn)
        if ed is None:
            shutil.copy(src, os.path.join(tmp, fn))
            continue
        z = np.load(src, allow_pickle=True)
        d = {k: np.asarray(z[k]).copy() for k in z.files}
        ed(d)
        np.savez(os.path.join(tmp, fn), **d)
    return tmp


def run_leg(name, must_redden, edit_cv=None, edit_fc=None, edit_up=None):
    with tempfile.TemporaryDirectory() as tmp:
        spec = scratch_spec(os.path.join(tmp, 'spec'), edit_cv, edit_fc)
        src, a, b = block_source()
        failed, labels = [], []

        def check(label, ok, got=None):
            labels.append(label)
            if not ok:
                failed.append(label)

        ns = dict(banks(SPEC0), np=np, os=os, json=json, SPEC=spec, check=check)
        if edit_up is not None:
            edit_up(ns)
        exec(compile(src, f'{RCPT}:{a}-{b}', 'exec'), ns)
        hit = [l for l in failed if must_redden in l]
        ok = bool(hit)
        print(f"  {'OK  ' if ok else 'FAIL'}  {name}")
        print(f"          must redden ....... {must_redden!r}")
        print(f"          checks run / red .. {len(labels)} / {len(failed)}"
              + ("   ⛔ NOTHING REDDENED -- the leg found nothing" if not failed else ""))
        for l in failed:
            print(f"          red: {l[:104]}")
        return ok


def bump(key, l_index, factor):
    def ed(d):
        d[key] = np.asarray(d[key], float).copy()
        d[key][l_index] = round(float(d[key][l_index]) * factor, 4)
    return ed


def setrow(key, src_key):
    def ed(d):
        d[key] = np.asarray(d[src_key], float).copy()
    return ed


def main():
    src, a, b = block_source()
    print(f"\n  the block under test: {os.path.relpath(RCPT, ROOT)} lines {a}-{b - 1}, "
          f"{len(src.splitlines())} lines, {src.count('check(')} gates\n")
    ells = list(np.asarray(np.load(os.path.join(SPEC0, CVN), allow_pickle=True)['ells'], int))
    i4, i3 = ells.index(4), ells.index(3)
    legs = []

    # A  the arm A bound (70's pin): move arm A (L) at l = 4 so the 3.2 per cent is breached.
    #    ⛔ THE DIRECTION IS THE WHOLE LEG.  Written first as `/= 1.04` this reported 0 FAIL, because
    #    converged FROZEN sits 3.17 per cent BELOW arm A at l = 4, so shrinking arm A shrinks the
    #    departure to +0.7 per cent and the bound holds.  *The harness was telling me I had perturbed
    #    towards the gate, not away from it -- which is what a leg reporting nothing always means.*
    def up_a(ns):
        ns['_ARMA'][4] *= 1.04
        ns['_LAZ']['distances__armA__L'] = np.asarray(ns['_LAZ']['distances__armA__L'], float).copy()
        ns['_LAZ']['distances__armA__L'][ns['_LE'].index(4)] *= 1.04
    legs.append(('A  arm A (L) at l = 4 scaled by 1.04 (AWAY from the gate)', 'WITHIN 3.2 PER CENT OF ARM A',
                 {}, dict(edit_up=up_a)))

    # B  the DECOUPLED bound (70's pin): move the refit DECOUPLED row at l = 3 past 1.9 per cent
    def up_b(ns):
        ns['_LBZ']['refit__armB_decoupled__L'] = np.asarray(ns['_LBZ']['refit__armB_decoupled__L'], float).copy()
        ns['_LBZ']['refit__armB_decoupled__L'][ns['_LE'].index(3)] /= 1.03
    legs.append(('B  refit DECOUPLED (L) at l = 3 scaled by 1/1.03', '1.9 PER CENT OF', {}, dict(edit_up=up_b)))

    # C  the NS3 900 departure (70's pin): make the banked FROZEN row already converged
    def up_c(ns):
        ns['_LFRO'][4] = 0.3424
    legs.append(('C  banked NS3 900 FROZEN at l = 4 set to the converged value', 'NS3 900 FROZEN ROW WAS NOT',
                 {}, dict(edit_up=up_c)))

    # D  the ntau_x2 claim (cc66): give FROZEN one last-place step under the doubled grid
    legs.append(('D  FROZEN ntau_x2 at l = 4 bumped one last place', 'DOUBLED OPACITY GRID MOVES NEITHER',
                 {}, dict(edit_cv=bump('distances__armB_frozen__L__ntau_x2', i4, 1.0 + 1e-4 / 0.3317))))

    # E  THE CONTROL ITSELF (cc66): the dead-knob world -- FROZEN does not move under ns3_half either
    legs.append(('E  FROZEN ns3_half set equal to the FROZEN reference (the dead-knob world)',
                 'ONE KNOB DISCRIMINATES', {},
                 dict(edit_cv=setrow('distances__armB_frozen__L__ns3_half', 'distances__armB_frozen__L__ntau_x2'))))

    # F  the resolution claim (cc66): store a value finer than four decimals
    def ed_f(d):
        d['distances__armB_decoupled__L__klo_0_02'] = np.asarray(
            d['distances__armB_decoupled__L__klo_0_02'], float).copy()
        d['distances__armB_decoupled__L__klo_0_02'][i4] += 1e-6
    legs.append(('F  one convergence row stored to six decimals', 'STORED TO FOUR DECIMALS', {},
                 dict(edit_cv=ed_f)))

    # G  the klo_0_02 bound (70's pin, restated): push the continuum move past 0.4 per cent
    legs.append(('G  DECOUPLED klo_0_02 at l = 3 scaled by 1.01', 'FIVE-FOLD DEEPER CONTINUUM', {},
                 dict(edit_cv=bump('distances__armB_decoupled__L__klo_0_02', i3, 1.01))))

    # H  the pairing assertion (cc66): strike the refit row's SPLITCLOCK from the hierarchy bank
    def up_h(ns):
        c = json.loads(str(ns['_LBZ']['config'].item()))
        c['SPLITCLOCK']['refit__armB_decoupled__L'] = None
        ns['_LBZ']['config'] = np.array(json.dumps(c), dtype=object)
    legs.append(('H  hierarchy bank\'s refit SPLITCLOCK struck to null', 'SO DOES THE HIERARCHY BANK', {},
                 dict(edit_up=up_h)))

    # I  the 2400-vs-h^2 convergence (70's pin): move the 2400 rung off its limit
    legs.append(('I  converged FROZEN NS3 2400 at l = 4 scaled by 1.01', 'NS3 2400 sits within 0.4 per cent',
                 {}, dict(edit_fc=bump('distances__armB_frozen__L__NS3_2400', i4, 1.01))))

    # 0  THE HARNESS'S OWN CONTROL: unperturbed, nothing may redden.  ⛔ Without this a leg's "red" is
    #    not evidence -- a harness that reddens everything reddens the named check too.
    with tempfile.TemporaryDirectory() as tmp:
        spec = scratch_spec(os.path.join(tmp, 'spec'))
        red0, lab0 = [], []

        def chk0(label, ok, got=None):
            lab0.append(label)
            if not ok:
                red0.append(label)
        ns0 = dict(banks(SPEC0), np=np, os=os, json=json, SPEC=spec, check=chk0)
        exec(compile(src, RCPT, 'exec'), ns0)
        ctl = not red0
        print(f"  {'OK  ' if ctl else 'FAIL'}  0  THE CONTROL: the block unperturbed, through this harness")
        print(f"          checks run / red .. {len(lab0)} / {len(red0)}")
        for l in red0:
            print(f"          red: {l[:104]}")
    if not ctl:
        print("  \u26d4 the harness itself does not reproduce the green run; no leg below is evidence")
        sys.exit(1)
    print()

    print("  LEGS -- each perturbs ONE thing and names the check it must redden\n")
    oks = [ctl] + [run_leg(nm, tgt, **kw) for nm, tgt, _, kw in legs]
    print(f"\n  the control is green and {sum(oks) - 1} of {len(oks) - 1} legs reddened their named check")
    if not all(oks):
        sys.exit(1)
    print("  ✓ EVERY PIN IN THE BLOCK IS FAILABLE")


if __name__ == '__main__':
    main()
