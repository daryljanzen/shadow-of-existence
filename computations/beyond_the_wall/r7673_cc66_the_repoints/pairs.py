#!/usr/bin/env python3
"""
`r7673` (cc66) -- ** WHAT THE `_leafrec1` SUFFIX ACTUALLY NAMES, READ OFF THE BANKS' OWN RESOLVED
CONFIGURATION RATHER THAN OFF THEIR FILENAMES. **

*** THE FINDING, IN TWO PARTS.  ⑴ FOR FOUR OF THE NINETEEN PAIRS, `LEAFREC` IS NOT WHAT MOVES: IT IS
`true` ON BOTH SIDES, RECORDED AS SUCH IN EACH FILE'S OWN `config`, AND WHAT THE TWIN CHANGES IS THE
REFIT POINT.  ⑵ AND FOR FIVE MORE THE ARM OF RECORD IS NOT IN A FILE AT ALL BUT IN KEYS THE NAMESAKE
DOES NOT HAVE, SO A PATH-ONLY REPOINT READS THE NAMESAKE'S NUMBERS AND REPORTS NO CHANGE.  ⛔ NOT
ONE OF THE NINETEEN IS INERT ON BOTH CHANNELS. ***

⌗⌗ ** AND THE FIRST VERSION OF THIS INSTRUMENT GOT ⑵ EXACTLY BACKWARDS, in this same revision. **
It measured the shared channel only, found five pairs with every shared array bit-identical, and
called them `INERT` -- which went into a route to `69` saying an item left PO-87's list because its
figure `cannot move`.  *The opposite is true: those five carry the arm of record in `..._leafrec1`
keys, and one of them is the very bank a receipt in print declares it is BLOCKED on.*  ⇒ `moved.py`,
in this same directory and this same revision, had already measured both channels, because
`r7673+cc66.2` made this error and `.3` corrected it twenty minutes later.  ** The lesson is not to
be careful: it is that a fix belongs in the shared definition, not in the instrument that needed it
-- `_moved` below now carries it, and gate ⑤ asserts the note saying so is still in this file. **

Built r7673+cc66 (node 66, code seat), answering `r7673` ⓶.

===================================================================================================
** WHY THIS IS ASKED BEFORE A RECEIPT IS EDITED, AND IT IS r7645's TRAP ONE LEVEL DEEPER **
===================================================================================================

`r7645+cc66.68` named the trap this corpus keeps setting: *an arm-of-record twin is a SUPERSET of its
namesake*, so a repoint that changes only a filename can read the same numbers and report no change.
Its remedy was to name the arm key once in a constant and GATE it.

** That remedy is sound and it does not reach this case.**  Here the twin's NAME is the thing that
lies: the directory and the file say `_leafrec1`, and for five of the nineteen pairs `LEAFREC` is
already `true` on the NAMESAKE side -- written into its own `config` by the instrument that made it.
*What those twins change is `CRH0 68.60 -> 68.570730`, `CROM 0.2973 -> 0.291246`, with `WBH2` and `NS`
made explicit: the REFIT POINT, which is the arm of record's other half.*

⇒ ** So "repointed onto the arm of record" is two claims, not one, and the suffix names only one of
them -- in these five cases the one that did not move. **  A repoint is still right where the arm of
record is that point; what is wrong is to report the move as the recombination switch's.

⌗ ** AND THE SISTER RECEIPT ALREADY HAD THE OTHER HALF OF THIS WRITTEN DOWN. **
`P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were...` carries, at its own
`AOR` table: *"All three siblings sit at the SAME point -- CRH0 68.57073, CROM 0.291246, WBH2
0.021643, NS 1.015066 -- so the three readings stay comparable with each other.  `refit_grid185_
leafrec1_distances/` is a DIFFERENT point (68.60 / 0.2973) and is deliberately NOT used here:
pairing it with `grid_oneclock_leafrec1` would compare two backgrounds, which is the error `cc66.72`
found."*  ** That note says the point is part of what the twin carries.  It is the third time in one
revision that the trap was documented in the tree before this seat walked into it. **

===================================================================================================
** THE FOUR CLASSES, AND EACH IS A DIFFERENT ANSWER TO "SHOULD THIS LEG REPOINT" **
===================================================================================================

  `INERT`       neither channel moves: every shared array bit-identical AND no arm-of-record key
                inside the twin.  A repoint is a true no-op and a figure read off such legs cannot
                move.  ⛔ *Nothing in this table is in this class.*
  `RE-KEY`      every shared array bit-identical, and the arm of record lives in keys the namesake
                does not have (`..._cr_leafrec1`).  ** So the repoint is a KEY change, not a path
                change, and a path-only repoint reads the namesake's numbers silently. **
  `POINT-ONLY`  arrays move, and `LEAFREC` is identical on both sides.  The move is the refit point.
                Legitimate, but it must not be reported as the recombination switch's.
  `LEAFREC+`    arrays move AND `LEAFREC` differs between the two recorded configurations.
  `UNRECORDED`  the namesake carries no `config` and no `switches` key, so its configuration cannot
                be read from the file.  ⛔ NOT reported as either -- an absence is not a reading.

rc=0 on success.  Run: python3 pairs.py
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
fail = []

# the repoint table, taken from r7671's SPLIT.md: every distinct spectrum it marks
# "[arm-of-record sibling banked]", with the items that read it
PAIRS = [
    ('r6919_injected_cr',  'spectra/r6919_injected_cr.npz',
     'spectra/r6919_injected_cr_leafrec1.npz', ['01', '24']),
    ('r6919_geometry',     'spectra/r6919_geometry.npz',
     'spectra/r6919_geometry_leafrec1.npz', ['01']),
    ('r6911_noop',         'spectra/r6911_noop.npz',
     'spectra/r6911_noop_leafrec1.npz', ['01', '05']),
    ('r6911_source_cr',    'spectra/r6911_source_cr.npz',
     'spectra/r6911_source_cr_leafrec1.npz', ['01']),
    ('r6893_switch_screen_cr', 'spectra/r6893_switch_screen_cr.npz',
     'spectra/r6893_switch_screen_cr_leafrec1.npz', ['01', '05', '09']),
    ('r6915_noop',         'spectra/r6915_noop.npz',
     'spectra/r6915_noop_leafrec1.npz', ['09']),
    ('r6897_fields',       'spectra/r6897_fields.npz',
     'spectra/r6897_fields_leafrec1.npz', ['18']),
    ('r6897_noop',         'spectra/r6897_noop.npz',
     'spectra/r6897_noop_leafrec1.npz', ['18']),
    ('r6885_los_cr',       'spectra/r6885_los_cr.npz',
     'spectra/r6885_los_cr_leafrec1.npz', ['17']),
    ('r6885_losdp0_cr',    'spectra/r6885_losdp0_cr.npz',
     'spectra/r6885_losdp0_cr_leafrec1.npz', ['17']),
    ('r6885_lossw0_cr',    'spectra/r6885_lossw0_cr.npz',
     'spectra/r6885_lossw0_cr_leafrec1.npz', ['17']),
    ('c54.178_cr',         'spectra/c54.178_cr.npz',
     'spectra/c54.178_cr_leafrec1.npz', ['30']),
    ('c54.177_cr',         'spectra/c54.177_cr.npz',
     'spectra/c54.177_cr_leafrec1.npz', ['30']),
    ('banked/cr_base',     'refit_grid185/cr_base.npz',
     'refit_grid185_leafrec1/cr_base.npz', ['08', '14']),
    ('licensed/cr_base',   'r7095_directions/grid_licensed/cr_base.npz',
     'r7095_directions/grid_licensed_leafrec1/cr_base.npz', ['08', '14', '20']),
    ('oneclock/cr_base',   'r7093_directions/grid_oneclock/cr_base.npz',
     'r7093_directions/grid_oneclock_leafrec1/cr_base.npz', ['08', '14', '20', '25', '27']),
    ('lever/cr_nodrive',   'r7201_cc66_loading_lever/cr_nodrive.npz',
     'r7201_cc66_loading_lever_leafrec1/cr_nodrive.npz', ['20', '25', '27']),
    ('lever/cr_rb0.5',     'r7201_cc66_loading_lever/cr_rb0.5.npz',
     'r7201_cc66_loading_lever_leafrec1/cr_rb0.5.npz', ['20']),
    ('lever/cr_rb1.5',     'r7201_cc66_loading_lever/cr_rb1.5.npz',
     'r7201_cc66_loading_lever_leafrec1/cr_rb1.5.npz', ['20']),
]
# the point the arm of record's banks sit at, from the sister receipt's own AOR note -- quoted here
# rather than re-derived, so a disagreement is attributable
AOR_POINT = {'CRH0': '68.570730', 'CROM': '0.291246', 'WBH2': '0.021643', 'NS': '1.015066'}


def _load(rel):
    p = os.path.join(BW, rel)
    if not os.path.exists(p):
        return None
    return np.load(p, allow_pickle=True)


def _cfg(z):
    """the instrument's OWN resolved configuration, read off the file -- never off its name"""
    if z is None:
        return None
    if 'config' in z.files:
        try:
            return json.loads(str(z['config']))
        except (ValueError, TypeError):
            return None
    return None


def _switches(z):
    if z is None or 'switches' not in z.files:
        return None
    return {k: v for k, v in (t.split('=', 1) for t in str(z['switches']).split() if '=' in t)}


def _leafrec(cfg, sw):
    """`LEAFREC` as the file records it, or None when the file records nothing"""
    if cfg is not None and 'LEAFREC' in cfg:
        return bool(cfg['LEAFREC'])
    if sw is not None and 'LEAFREC' in sw:
        return bool(int(sw['LEAFREC']))
    return None


SUF = '_leafrec1'


def _ne(x, y):
    x, y = np.asarray(x), np.asarray(y)
    return x.shape != y.shape or not bool(np.all(x == y))


def _moved(a, b):
    """BOTH channels, which is `moved.py`'s own definition in this directory.

    ⛔⛔ A twin is a SUPERSET of its namesake, so the shared half can be bit-identical BY DESIGN
    while the arm of record lives in keys the namesake does not have.  `r7673+cc66.2` measured the
    shared channel alone and reported six pairs bit-identical; `.3` corrected it twenty minutes
    later.  ** Measuring only the shared channel here would have made the same error in a second
    instrument in the same revision, and it did, until this function was fixed. **
    """
    sh = sorted(set(a.files) & set(b.files))
    mv = [k for k in sh if _ne(a[k], b[k])]
    rekey = sorted(k for k in b.files
                   if k.endswith(SUF) and k[:-len(SUF)] in b.files
                   and _ne(b[k], b[k[:-len(SUF)]]))
    return sh, mv, rekey


print(__doc__.split("rc=0")[0])
print("=" * 100)
print("  ① EVERY PAIR, CLASSIFIED FROM ITS OWN RECORDED CONFIGURATION")
print("=" * 100)
print(f"  {'leg':>24} {'class':>11} {'LFR n/t':>10} {'shrd':>5} {'mvd':>4} {'rekey':>6}  where LEAFREC was read")
print("  " + "-" * 98)

CLASS = {}
WHAT = {}
CDIFF = {}
REKEY = {}
for nm, a, b, items in PAIRS:
    za, zb = _load(a), _load(b)
    if za is None or zb is None:
        fail.append(f"{nm}: {'namesake' if za is None else 'twin'} absent from this checkout")
        continue
    ca, cb = _cfg(za), _cfg(zb)
    sa, sb = _switches(za), _switches(zb)
    la, lb = _leafrec(ca, sa), _leafrec(cb, sb)
    sh, mv, rk = _moved(za, zb)
    arrmv = [k for k in mv if k not in ('config', 'switches', 'manifest')]

    if not arrmv and not rk:
        cls = 'INERT'
    elif not arrmv and rk:
        cls = 'RE-KEY'
    elif la is None:
        cls = 'UNRECORDED'
    elif la == lb:
        cls = 'POINT-ONLY'
    else:
        cls = 'LEAFREC+'
    CLASS[nm] = cls
    REKEY[nm] = rk

    # what the twin changes, from the switches both sides record
    # ⛔ READ THE RESOLVED `config` AND THE `switches` STRING SEPARATELY, AND PRINT BOTH.  The
    #    switches string is the command line and OMITS anything left at its default; the `config`
    #    is what the instrument resolved and RECORDS the default it took.  So `LEAFREC` can be
    #    absent from a namesake's switches and `true` in its own config -- which is the whole
    #    reason this instrument classifies off `config` and never off the command line or the name.
    what = []
    if sa and sb:
        for k in sorted(set(sa) | set(sb)):
            if k == 'SAVE' or sa.get(k) == sb.get(k):
                continue
            what.append(f"{k} {sa.get(k, '(default)')}->{sb.get(k, '(default)')}")
    if ca and cb:
        cdiff = sorted(k for k in set(ca) | set(cb)
                       if k != 'instrument_blob' and ca.get(k) != cb.get(k))
        cnote = ('config: ' + ','.join(cdiff)) if cdiff else 'config IDENTICAL on both sides'
    else:
        cdiff = None
        cnote = 'namesake records no `config` key -- LEAFREC read off its switches string instead'
    WHAT[nm] = what
    CDIFF[nm] = cnote
    ln = {True: '1', False: '0', None: '-'}
    print(f"  {nm:>24} {cls:>11} {ln[la]:>4} /{ln[lb]:>4} {len(sh):>5} {len(arrmv):>4} "
          f"{len(rk):>6}  {cnote[:42]}")

if len(CLASS) != len(PAIRS):
    fail.append(f"{len(PAIRS) - len(CLASS)} of {len(PAIRS)} pairs were not classified")
else:
    print(f"\n  all {len(PAIRS)} pairs classified, each from its own file's `config` or `switches`")

# =====================================================================
print()
print("=" * 100)
print("  ② THE CLASSES PARTITION THE TABLE, AND THE TWO THAT CHANGE AN ANSWER ARE NAMED WHOLE")
print("=" * 100)
BY = {}
for nm, c in CLASS.items():
    BY.setdefault(c, []).append(nm)
for c in ('INERT', 'RE-KEY', 'POINT-ONLY', 'LEAFREC+', 'UNRECORDED'):
    got = sorted(BY.get(c, []))
    print(f"  {c:>11}  {len(got):>2}   {', '.join(got) if got else '(none)'}")
tot = sum(len(v) for v in BY.values())
if tot != len(PAIRS):
    fail.append(f"the classes hold {tot} legs against the table's {len(PAIRS)}")
else:
    print(f"\n  {tot} of {len(PAIRS)}: the four classes partition the table with nothing double-counted")

# ⛔ the claim that makes this worth a gate: the POINT-ONLY class is not empty
if not BY.get('POINT-ONLY'):
    fail.append("the POINT-ONLY class is empty -- this instrument's whole finding fails, and the "
                "suffix would then name exactly what moves")
else:
    print(f"\n  ⛔ ** {len(BY['POINT-ONLY'])} leg(s) are POINT-ONLY: `LEAFREC` is recorded identical on")
    print("     both sides and the arrays move anyway. **  For these the `_leafrec1` name is a")
    print("     misnomer and the move is the refit point:")
    for nm in sorted(BY['POINT-ONLY']):
        print(f"       {nm:>22}  switches: {'; '.join(WHAT[nm])[:66]}")
        print(f"       {'':>22}  resolved {CDIFF[nm]}")
    print("\n     ⌗ ** AND THE TWO COLUMNS DISAGREE ON `LEAFREC` FOR THE THREE LEVER LEGS, WHICH IS")
    print("        ITSELF THE READING. **  Their switches STRING omits `LEAFREC` on the namesake")
    print("        side, because a command line omits what it leaves at its default; their resolved")
    print("        `config` carries `LEAFREC: true` on BOTH sides, because that is the default the")
    print("        instrument took.  *A switches-string read would have called these `LEAFREC+` and")
    print("        reported the refit point's move as the recombination switch's.*")

if not BY.get('RE-KEY'):
    fail.append("the RE-KEY class is empty -- r7645's trap would then not be live in this table, "
                "and this instrument's second channel would be asserting nothing")
else:
    print(f"\n  ⛔⛔ ** {len(BY['RE-KEY'])} leg(s) are RE-KEY: every SHARED array is bit-identical and the arm")
    print("     of record is in keys the namesake does not have. **  A path-only repoint of these")
    print("     reads the namesake's numbers and reports no change -- `r7645+cc66.68`'s trap exactly,")
    print("     live in this table.  ⇒ ** For these the KEY has to move, not the path. **")
    _items = {n: it for n, _, _, it in PAIRS}
    for nm in sorted(BY['RE-KEY']):
        _k = REKEY[nm]
        print(f"       {nm:>22}  item(s) {', '.join(_items[nm]):<14} {len(_k)} arm-of-record key(s), "
              f"e.g. {', '.join(_k[:3])}")
if BY.get('INERT'):
    print(f"\n  ⌗ {len(BY['INERT'])} leg(s) are INERT on BOTH channels: {', '.join(sorted(BY['INERT']))}")
    print("     *A repoint of those is a true no-op and a figure read off them alone cannot move.*")
else:
    print("\n  ⌗ ** NO leg in this table is INERT on both channels. **  Every one of the nineteen")
    print("     carries the arm of record somewhere -- in a moved array, or in a key the namesake")
    print("     does not have.  *The class is kept and printed empty rather than dropped, because")
    print("     `INERT` is the verdict a reader would otherwise infer from `moved = 0`.*")

# =====================================================================
print()
print("=" * 100)
print("  ③ THE TWO TWINS THAT ARE ONE COMPUTATION BANKED TWICE")
print("=" * 100)
A = _load('refit_grid185_leafrec1/cr_base.npz')
B = _load('r7095_directions/grid_licensed_leafrec1/cr_base.npz')
if A is None or B is None:
    fail.append("the banked/licensed arm-of-record pair is not in this checkout")
else:
    sh, mv, _rk = _moved(A, B)
    print(f"  refit_grid185_leafrec1/cr_base.npz against "
          f"r7095_directions/grid_licensed_leafrec1/cr_base.npz")
    print(f"    shared keys {len(sh)}; differing {mv}")
    print(f"    `switches` character-identical: {str(A['switches']) == str(B['switches'])}")
    print(f"    `config` character-identical  : {str(A['config']) == str(B['config'])}")
    ma, mb = json.loads(str(A['manifest'])), json.loads(str(B['manifest']))
    md = sorted(k for k in set(ma) | set(mb) if ma.get(k) != mb.get(k))
    print(f"    `manifest` differs in: {md}")
    if mv != ['manifest']:
        fail.append(f"the two arm-of-record bases differ in {mv}, not in `manifest` alone -- "
                    f"the identity this gate rests on does not hold")
    if str(A['switches']) != str(B['switches']) or str(A['config']) != str(B['config']):
        fail.append("the two arm-of-record bases do not record the same configuration")
    if md != ['file', 'held', 'namesake']:
        fail.append(f"the manifests differ in {md}, not in the three path/bookkeeping keys alone")
    else:
        print("\n  ⛔ ** SO ON THE ARM OF RECORD THE `banked` AND `licensed` CONFIGURATIONS ARE ONE")
        print("     COMPUTATION, BANKED TWICE UNDER TWO NAMES -- every shared array identical and")
        print("     the resolved `config` character-identical, differing only in which namesake each")
        print("     manifest records. **")
        print("     *And that is not an accident of the banking: `licensed` MEANS the leaf-rate")
        print("      distance, which is what `LEAFREC=1` does -- its namesake already carries")
        print("      `LEAFREC=1` in its own switches.  So the arm of record IS the licensed")
        print("      configuration, and a receipt whose table contrasts the two has no contrast left")
        print("      on it.*")

# =====================================================================
print()
print("=" * 100)
print("  ③ᵇ AND IT IS NOT ONE LEG: ALL NINE OF THE TWO GRIDS' CR LEGS ARE THE SAME COMPUTATION")
print("=" * 100)
print("  *`reach()` in the sister receipt reads the WHOLE grid -- the base and the eight derivative")
print("   legs -- so the identity matters on all nine or it does not matter at all.*")
_A, _B = 'refit_grid185_leafrec1', os.path.join('r7095_directions', 'grid_licensed_leafrec1')
_la = sorted(f for f in os.listdir(os.path.join(BW, _A)) if f.endswith('.npz'))
_lb = sorted(f for f in os.listdir(os.path.join(BW, _B)) if f.endswith('.npz'))
_both = sorted(set(_la) & set(_lb))
_bad = []
for _f in _both:
    _za, _zb = _load(os.path.join(_A, _f)), _load(os.path.join(_B, _f))
    _sh, _mv, _rkx = _moved(_za, _zb)
    if _mv != ['manifest']:
        _bad.append((_f, _mv))
print(f"  legs in {_A}: {len(_la)}   in {_B}: {len(_lb)}   shared by name: {len(_both)}")
print(f"  of the {len(_both)} shared legs, {len(_both) - len(_bad)} differ in `manifest` ALONE "
      f"-- every other array identical")
if len(_both) != 9:
    fail.append(f"the two grids share {len(_both)} legs by name, not the nine a grid read needs")
if _bad:
    fail.append(f"{len(_bad)} leg(s) differ in more than `manifest`: {_bad[:3]} -- the nine-leg "
                f"identity this gate rests on does not hold")
else:
    print(f"  ⛔⛔ ** SO ALL NINE LEGS ARE ONE COMPUTATION, AND THE CONSEQUENCE IS A LIVE ONE. **")
    print("     `P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were...` is")
    print("     cited at `CR_cosmology.tex` l.1981 and resolves BOTH `banked` and `licensed` to")
    print("     these two directories through its own `AOR` table.  Its PART B headline computes")
    print("     `_mv = V[banked,cr].chi2 - V[licensed,cr].chi2` and gates `abs(_mv)/_gap < 5e-4`.")
    print("     ⇒ ** On the arm of record that difference is IDENTICALLY ZERO, so the gate passes")
    print("     because the two readings are the same nine files -- not because the rebuild moves")
    print("     nothing. **  Its printed clause, `on a rebuild that changed the spectrum by six and")
    print("     a half per cent`, states a contrast the arm of record does not carry.")
    print("     ⌗ *Routed, not repaired here: that receipt is not on PO-87's list and the banks are")
    print("      70's.  And this is not a banking mistake -- `licensed` MEANS the leaf-rate")
    print("      distance, so setting `LEAFREC=1` on the baseline NECESSARILY merges the two.  The")
    print("      arm of record cannot carry a banked-against-licensed contrast, because that")
    print("      contrast IS the flag.*")
    print("     ⚠ *One step of this is INFERRED and not read: `refit_grid185/cr_base.npz` carries no")
    print("      `switches` and no `config` key, so that the two NAMESAKES differ in `LEAFREC` alone")
    print("      cannot be read off the files.  What is READ here is that their twins are identical")
    print("      and that `grid_licensed`'s namesake already records `LEAFREC=1`.*")

# =====================================================================
print()
print("=" * 100)
print("  ④ THE REFIT POINT IS THE ARM OF RECORD'S OTHER HALF, AND EVERY MOVING TWIN SITS AT IT")
print("=" * 100)
print("  *Quoted from the sister receipt's own `AOR` note rather than re-derived: CRH0 68.570730,")
print("   CROM 0.291246, WBH2 0.021643, NS 1.015066.*")
atp = []
for nm, a, b, items in PAIRS:
    zb = _load(b)
    sb = _switches(zb)
    if sb is None or 'CRH0' not in sb:
        continue
    ok = all(sb.get(k) == v for k, v in AOR_POINT.items())
    atp.append((nm, ok, {k: sb.get(k) for k in AOR_POINT}))
for nm, ok, pt in atp:
    print(f"    {'[ok]' if ok else '[  ]'} {nm:>22}  CRH0={pt['CRH0']} CROM={pt['CROM']} "
          f"WBH2={pt['WBH2']} NS={pt['NS']}")
off = [nm for nm, ok, _ in atp if not ok]
if off:
    fail.append(f"{len(off)} twin(s) do not sit at the arm of record's point: {off} -- pairing them "
                f"with each other compares two backgrounds, which is cc66.72's error")
elif not atp:
    fail.append("no twin records a point at all -- gate ④ asserted nothing")
else:
    print(f"\n  all {len(atp)} twins that record a point sit at the SAME one, so legs repointed")
    print("  together stay comparable with each other -- the condition cc66.72's error broke")

# =====================================================================
print()
print("=" * 100)
print("  ⑤ SCOPE, GATED RATHER THAN ASSERTED IN PROSE ALONE")
print("=" * 100)
_me = open(os.path.abspath(__file__), encoding='utf-8').read()
for want, label in (
        ('is a SUPERSET of its namesake',
         'this states r7645+cc66.68\'s trap, which it extends rather than replaces'),
        ('an absence is not a reading',
         'an UNRECORDED namesake is not reported as either class'),
        ('A repoint is still right where the arm of record is that point',
         'a POINT-ONLY move is not called illegitimate, only mis-named'),
        ('Measuring only the shared channel here would have made the same error',
         'the second channel is measured, and the instrument records that it was added '
         'after the first version got this wrong')):
    if want not in _me:
        fail.append(f"this instrument's own text no longer carries: {label}")
    else:
        print(f"    [ok]  ⑤ {label}")

print()
print("=" * 100)
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  GATES: ALL PASS.")
print("  ⛭ The `_leafrec1` suffix names ONE of the two things the arm of record changes, and for")
print(f"     {len(BY.get('POINT-ONLY', []))} of the {len(PAIRS)} legs in the repoint table it names the one that did not move.")
print(f"  ⛔⛔ AND {len(BY.get('RE-KEY', []))} legs are RE-KEY: the shared half is bit-identical and the arm of record")
print("     is in keys the namesake does not have, so a PATH-ONLY repoint of those reads the")
print("     namesake's numbers and reports no change.  For them the KEY has to move.")
print(f"  ⌗ And {len(BY.get('INERT', []))} legs are inert on both channels.")
print("=" * 100)
sys.exit(0)
