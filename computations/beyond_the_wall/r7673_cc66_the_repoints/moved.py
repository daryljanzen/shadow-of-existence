#!/usr/bin/env python3
"""r7673 (cc66) -- WHICH REPOINTS CAN MOVE A FIGURE AT ALL, measured before any receipt is run.

** THE ORDER (r7673, 69) item 2: ** "Repoint each receipt, run it, and route every printed figure
that moves, with its sentence.  Figures that do not move need only the receipt change."

⛭⛭ ** THE CHEAPEST THING TO KNOW FIRST, AND IT IS NOT A RECEIPT RUN. **  A repoint can only move a
figure if the arm-of-record twin DIFFERS from the namesake.  That is a comparison of two `.npz`
files and it costs nothing, where running the receipt costs minutes.  ⇒ So the pass is ordered by
this file: the paths whose twin is BIT-IDENTICAL are repointed as bookkeeping and cannot move a
figure, and only the rest need a run and a reading.

⛔ ** AND IT CHECKS 70's MEASUREMENT RATHER THAN RESTING ON IT. **  `r7669+70.1` reports that
LEAFREC does not touch the control.  Every control key here is compared, and the ONE class that
does move in a control file is named rather than waved through: a CROSS-ARM SWAP product
(`Dl_swap`, `xswap`, `Dl__viswap`) is the arm's own source or visibility substituted into the
control's leg, so it involves the CR arm by construction and moving is what it must do.  A control
key outside that class moving would put every control figure in print in question.

Registered at PREDICTION.md in this directory, in its own commit, before this file existed.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SP = os.path.join(BW, 'spectra')
fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


#: the paths r7671's REBUILD table named, plus 70's seven twins, as (relative dir, basename)
TARGETS = [
    ('spectra', 'r6919_injected_cr.npz'), ('spectra', 'r6919_injected_lcdm.npz'),
    ('spectra', 'r6919_geometry.npz'), ('spectra', 'r6919_noop.npz'),
    ('spectra', 'r6911_source_cr.npz'), ('spectra', 'r6911_source_lcdm.npz'),
    ('spectra', 'r6911_source_cr_kcont.npz'), ('spectra', 'r6911_noop.npz'),
    ('spectra', 'r6915_noop.npz'), ('spectra', 'r6915_pairs_cr.npz'),
    ('spectra', 'r6893_switch_screen_cr.npz'),
    ('spectra', 'r6897_fields.npz'), ('spectra', 'r6897_noop.npz'),
    ('spectra', 'r6885_los_cr.npz'), ('spectra', 'r6885_losdp0_cr.npz'),
    ('spectra', 'r6885_lossw0_cr.npz'), ('spectra', 'r6885_dp0_cr.npz'),
    ('spectra', 'r6889_nufs0_cr.npz'), ('spectra', 'r6959_eta_cr.npz'),
    ('spectra', 'cc66_r185_verify_cr.npz'),
    ('spectra', 'r7041_accept_digest.npz'), ('spectra', 'r7041_accept_Al.npz'),
    ('spectra', 'r7041_accept_sample.npz'), ('spectra', 'r7041_accept_nk_slices.npz'),
    ('refit_grid185', 'cr_base.npz'),
    (os.path.join('r7095_directions', 'grid_licensed'), 'cr_base.npz'),
    (os.path.join('r7093_directions', 'grid_oneclock'), 'cr_base.npz'),
    ('r7201_cc66_loading_lever', 'cr_nodrive.npz'),
    ('r7201_cc66_loading_lever', 'cr_rb0.5.npz'),
    ('r7201_cc66_loading_lever', 'cr_rb1.5.npz'),
]
#: the cross-arm substitution products: the arm's own source or visibility put into the other leg
SWAP = ('swap', 'viswap', 'xswap')


def twin_of(d, b):
    """the arm-of-record form, by filename OR by directory -- the distinction census cut 1 missed"""
    for cand in (os.path.join(BW, d, b.replace('.npz', '_leafrec1.npz')),
                 os.path.join(BW, d + '_leafrec1', b)):
        if os.path.exists(cand):
            return cand
    return None


head('Ⓐ  WHICH TWINS DIFFER FROM THEIR NAMESAKE, AND WHAT MOVED IN THEM')
rows, missing = [], []
for d, b in TARGETS:
    nsk = os.path.join(BW, d, b)
    twin = twin_of(d, b)
    if not os.path.exists(nsk) or twin is None:
        missing.append(os.path.join(d, b) + ('  (no namesake)' if not os.path.exists(nsk)
                                             else '  (no twin)'))
        continue
    A = np.load(nsk, allow_pickle=True)
    B = np.load(twin, allow_pickle=True)
    shared = sorted(set(A.files) & set(B.files))

    def _ne(x, y):
        try:
            return not np.array_equal(x, y)
        except Exception:                                      # noqa: BLE001
            return True

    #: ⛔⛭⛭⛭ r7673+cc66.3 -- THE FIRST FORM OF THIS COMPARED ONLY SHARED KEYS AND CALLED SIX PAIRS
    #:   BIT-IDENTICAL.  THEY ARE NOT.  Since `r7643`+70's RE-KEY, a twin keeps the NAMESAKE's
    #:   values under the original keys and carries the arm-of-record values under `*_leafrec1`
    #:   SUFFIXED keys beside them:
    #:
    #:       r6919_geometry_leafrec1.npz:  l_A__cr          <- still the NAMESAKE's
    #:                                     l_A__cr_leafrec1 <- the arm of record's
    #:
    #:   ** So comparing shared keys measures exactly the half that cannot move, and every one of
    #:   the six "identical" pairs moves 1 to 15 quantities under its suffixed keys. **
    #:   ⇒ And the consequence for the order is larger than the count: ** A REPOINT THAT MOVES ONLY
    #:     THE FILENAME READS THE SAME NUMBERS. **  For these files the KEY has to move too, which
    #:     is what `P15_the_contrast_excess…`'s own comment says in the tree -- *"the sibling's
    #:     `__cr` is the NAMESAKE's since r7643+70's re-key"* -- and this file did not read it.
    #:   ⌗ *Tenth instance of keying on something cheaper than the question, and the first I pushed
    #:     a headline on before catching: `r7673+cc66.2` said six repoints could not move a figure.*
    diff = [k for k in shared if _ne(A[k], B[k])]
    rekey = [k for k in B.files
             if k.endswith('_leafrec1') and k[:-len('_leafrec1')] in B.files
             and _ne(B[k], B[k[:-len('_leafrec1')]])]
    #: ⛔⛭⛭ THE FIRST FORM OF THIS CLASSIFIED A KEY AS CONTROL-SIDE BY ITS OWN NAME, and that is
    #:   the wrong question one more time.  `r6919_injected_lcdm.npz` is a CONTROL leg and its one
    #:   moving key is `Dl__viswap` -- no `lcdm` anywhere in the key -- so a name test counted a
    #:   control file's moving key as CR-side and the swap class came out EMPTY.  ** The gate then
    #:   read "0 control keys moved" when two control files had moved a key each. **
    #:   ⇒ A key is control-side when THE FILE is a control leg or the key names one.  *Caught
    #:     because a scratch measurement taken before this file disagreed with the gate it wrote;
    #:     that disagreement is the only reason it did not ship saying something false.*
    _is_ctl_file = 'lcdm' in b.lower() or 'control' in b.lower()
    ctl = [k for k in diff if _is_ctl_file or 'lcdm' in k.lower()]
    ctl_swap = [k for k in ctl if any(s in k.lower() for s in SWAP)]
    ctl_bad = [k for k in ctl if k not in ctl_swap]
    rows.append((os.path.join(d, b), len(shared), diff, ctl_swap, ctl_bad,
                 sorted(set(B.files) - set(A.files)), rekey))

print(f'      targets: {len(TARGETS)};  comparable pairs: {len(rows)};  not comparable: {len(missing)}')
for q in missing:
    print(f'        {q}')
print()
print(f'      {"path":58s} {"shared":>6} {"moved":>6} {"rekey":>6}  markers')
for p, ns, diff, cs, cb, extra, rk in rows:
    print(f'      {p:58s} {ns:6d} {len(diff):6d} {len(rk):6d}  {[x for x in extra if x in ("config", "manifest")]}')

#: a pair is INERT only if NEITHER channel moved: no shared key differs AND no re-keyed
#: `*_leafrec1` key differs from its unsuffixed base.
identical = [r for r in rows if not r[2] and not r[6]]
moved = [r for r in rows if r[2] or r[6]]
print()
print(f'      BIT-IDENTICAL across the switch (a repoint cannot move a figure): {len(identical)}')
for p, *_ in identical:
    print(f'        {p}')
print(f'      genuinely moved                                                 : {len(moved)}')
#: ⛔⛭⛭⛭ Ⓐ① AS FIRST WRITTEN ASSERTED THAT SOME PAIRS ARE INERT, AND NONE IS.  The claim came from
#:   comparing shared keys only, which measures the half the re-key leaves alone.  Scored on both
#:   channels: ** every one of the 30 pairs moves something, and the class that matters is the one
#:   that moves ONLY through the re-key -- there a repoint of the FILENAME ALONE IS A SILENT NO-OP. **
_silent = [r for r in rows if not r[2] and r[6]]
_direct = [r for r in rows if r[2]]
print()
print(f'      move through a SHARED key (a filename repoint suffices)   : {len(_direct)}')
print(f'      move ONLY through the re-key (filename repoint is SILENT) : {len(_silent)}')
for p, ns, diff, cs, cb, extra, rk in _silent:
    print(f'        {p:52s} {len(rk)} re-keyed quantit(ies)')
check(f'Ⓐ① ⛔⛭⛭⛭ NO PAIR IS INERT, AND THE FIRST FORM OF THIS GATE SAID SIX WERE: all {len(moved)} '
      f'of the {len(rows)} pairs move a quantity.  {len(_direct)} move through a SHARED key, where '
      f'repointing the filename is enough; {len(_silent)} move ONLY through `r7643`+70\'s RE-KEY, '
      f'where the twin keeps the namesake values under the original keys and ** a repoint of the '
      f'filename alone reads the same numbers and is a SILENT no-op **',
      len(identical) == 0 and len(_silent) > 0 and len(_direct) + len(_silent) == len(rows),
      f'{len(_direct)} shared-key, {len(_silent)} re-key-only, 0 inert, of {len(rows)}')

#: ⛭⛭ 70's MEASUREMENT, CHECKED HERE ON EVERY PAIR RATHER THAN TAKEN ON REPORT
bad = [(p, cb) for p, ns, diff, cs, cb, extra, rk in rows if cb]
swaps = [(p, cs) for p, ns, diff, cs, cb, extra, rk in rows if cs]
print()
print(f'      control keys that moved and are CROSS-ARM SWAP products: {len(swaps)} file(s)')
for p, cs in swaps:
    print(f'        {p}: {cs}')
print(f'      control keys that moved and are NOT swap products      : {len(bad)} file(s)')
for p, cb in bad:
    print(f'        ⛔ {p}: {cb}')
check(f'Ⓐ② ⛭⛭⛭ 70\'s MEASUREMENT IS CHECKED ON EVERY PAIR, NOT RESTED ON: across '
      f'{len(rows)} pairs, the ONLY control keys that move are cross-arm SWAP products '
      f'({len(swaps)} file(s)) -- the arm\'s own source or visibility substituted into the '
      f'control\'s leg, which involves the CR arm by construction.  {len(bad)} control key(s) '
      f'moved outside that class.  ⇒ A control key moving outside it would put every control '
      f'figure in print in question, which is why this is a gate and not a remark',
      not bad, f'{len(swaps)} swap-product file(s), {len(bad)} outside the class')

#: ⛭ and the arm-of-record marker, which is how a twin declares itself
nomark = [p for p, ns, diff, cs, cb, extra, rk in rows if 'manifest' not in extra]
print()
print(f'      twins carrying no `manifest` marker: {len(nomark)}')
for p in nomark:
    print(f'        {p}')
check(f'Ⓐ③ EVERY arm-of-record twin DECLARES ITSELF with a `manifest` key the namesake lacks -- '
      f'which is the test the namesake-pinning receipts\' own header guards use -- and '
      f'{len(nomark)} of {len(rows)} do not',
      not nomark, f'{len(rows) - len(nomark)} of {len(rows)} carry a manifest')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)
