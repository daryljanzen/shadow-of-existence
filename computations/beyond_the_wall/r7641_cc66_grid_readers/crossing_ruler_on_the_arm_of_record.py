#!/usr/bin/env python3
"""r7641 item 2: the crossing receipt's RADIATION-FREE RULER on the arm of record.

`P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_the_172_is_the_radiation_free_ruler`
is the last reader of 70's re-banked crossing set, and the only one still pointing at its namesake
files -- the ladders receipt beside it was already re-pointed and is green.

** AND THIS ONE IS THE CASE TO CHECK HARDEST, BECAUSE THE BANK AGREES WITH MY OWN TITLE. **  70's
`RESULT.md` says the re-banked ruler reads `171.55` where r7635's `LEAFSCALES=1` rebuild read `302.9`.
*The receipt's title is "the 172 IS the radiation-free ruler", and `171.55` keeps it while `302.9`
would have destroyed it -- the ruler would have collapsed onto the body's comb and the receipt's whole
distinction with it.*  ⇒ ** A bank that rescues a claim of mine is exactly the output this seat has
learned to distrust (`r7641+cc66.34`), so every figure below is measured here from the files, and the
namesake's published row has to reproduce first. **

    spectra/c54.178_cr.npz                        -> ..._leafrec1.npz   (the superseded config)
    spectra/r6784_cr_crossing_hier.npz            -> ..._leafrec1.npz
    spectra/r6784_cr_crossing_hier_noCRIC.npz     -> ..._leafrec1.npz
    spectra/r6784_cr_crossing_los.npz             -> ..._leafrec1.npz

`c54.178_lcdm` has NO sibling, which is the bank saying the control does not move -- asserted below
rather than assumed.

** THE CARRY IS CLASS 3. **  Every quantity here is a ruler length, a peak position, a height ratio or
a chi^2 of one spectrum against the bandpowers.  The one arm-against-control comparison -- the implied
`r_s` ratio -- is a ratio of two LENGTHS, not of comb-band powers, so the comb-offset map has nothing
to act on; measured below by recomputing the arm's side from its own file alone.

Nothing is edited by this file.  Figures are reported old -> new in `FOR_66.md`.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


SKY = np.array([220.6, 538.1, 809.8])


def load(name):
    z = np.load(os.path.join(SPEC, name + '.npz'), allow_pickle=True)
    return (np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A']),
            float(z['r_s']), float(np.atleast_1d(z['D_M'])[0]))


def peaks(ls, Dl, n=5):
    return [int(ls[i]) for i in range(1, len(Dl) - 1)
            if Dl[i] > Dl[i - 1] and Dl[i] > Dl[i + 1]][:n]


def heights(ls, Dl):
    idx = [i for i in range(1, len(Dl) - 1) if Dl[i] > Dl[i - 1] and Dl[i] > Dl[i + 1]][:3]
    return (float(Dl[idx[0]] / Dl[idx[1]]), float(Dl[idx[0]] / Dl[idx[2]])) if len(idx) > 2 \
        else (float('nan'), float('nan'))


def comb(p):
    return float(np.mean(np.diff(np.array(p, dtype=float))))


def band_chi2(ls, Dl):
    lc, _ = CS.bin_center_and_fac()
    mb = CS.bin_spectrum(ls, Dl)
    ok = np.isfinite(mb)
    F = np.linalg.inv(CS.COV_TT[np.ix_(ok, ok)])
    d, m = CS.X_DATA[ok], mb[ok]
    A = (m @ F @ d) / (m @ F @ m)
    r = d - A * m
    per = r * (F @ r)
    out = {}
    for lo, hi in [(32, 700), (700, 1000), (1000, 2000)]:
        s = (lc[ok] >= lo) & (lc[ok] <= hi)
        out[(lo, hi)] = (int(s.sum()), float(per[s].sum()))
    return out


RUNS = {'lcdm': 'c54.178_lcdm', 'pinned': 'c54.178_cr', 'crossing': 'r6784_cr_crossing_hier',
        'matched': 'r6784_cr_crossing_hier_noCRIC', 'los': 'r6784_cr_crossing_los'}
MOVES = ('pinned', 'crossing', 'matched', 'los')


def read(arm):
    out = {}
    for k, stem in RUNS.items():
        n = stem + ('_leafrec1' if arm == 'aor' and k in MOVES else '')
        ls, Dl, lA, rs, DM = load(n)
        p = peaks(ls, Dl)
        h = heights(ls, Dl)
        c, nb = CS.chi2_of(ls, Dl)[:2]
        out[k] = dict(file=n, ls=ls, Dl=Dl, lA=lA, rs=rs, DM=DM, pk=p, cb=comb(p),
                      p12=h[0], p13=h[1], chi2=float(c), nb=int(nb),
                      band=band_chi2(ls, Dl))
    return out


print(__doc__)
print(BAR)
print("  PART 1 -- THE CONTROL HAS NO SIBLING, WHICH IS THE BANK'S OWN STATEMENT")
print(BAR)
_ctl_sib = os.path.exists(os.path.join(SPEC, 'c54.178_lcdm_leafrec1.npz'))
print(f"    c54.178_lcdm_leafrec1.npz present: {_ctl_sib}")
for k in MOVES:
    print(f"    {RUNS[k] + '_leafrec1.npz':48s} present: "
          f"{os.path.exists(os.path.join(SPEC, RUNS[k] + '_leafrec1.npz'))}")
check("every CR-side run has an arm-of-record sibling and the CONTROL has none -- so the re-point is "
      "complete on one side and the bank says the other does not move",
      not _ctl_sib and all(os.path.exists(os.path.join(SPEC, RUNS[k] + '_leafrec1.npz'))
                           for k in MOVES),
      f"control sibling {_ctl_sib}, "
      f"{sum(os.path.exists(os.path.join(SPEC, RUNS[k] + '_leafrec1.npz')) for k in MOVES)} of 4 arms")

A = {a: read(a) for a in ('namesake', 'aor')}
print()
print(BAR)
print("  PART 2 -- THE LICENCE: THE NAMESAKE ROW THE RECEIPT PUBLISHES")
print(BAR)
for a in ('namesake', 'aor'):
    print(f"\n    --- {a} ---")
    print(f"      {'run':34s} {'l_A':>8s} {'r_s':>8s} {'peaks':>26s} {'P1/P2':>7s} {'P1/P3':>7s} "
          f"{'chi^2':>10s}")
    for k in ('lcdm', 'pinned', 'crossing', 'matched', 'los'):
        e = A[a][k]
        print(f"      {k + ' (' + e['file'] + ')':34s} {e['lA']:8.3f} {e['rs']:8.2f} "
              f"{'/'.join(str(x) for x in e['pk'][:4]):>26s} {e['p12']:7.3f} {e['p13']:7.3f} "
              f"{e['chi2']:10.1f}")
N, O = A['aor'], A['namesake']
_b700 = lambda e: e['band'][(700, 1000)][1] / e['band'][(700, 1000)][0]      # noqa: E731
check("⛔ THE LICENCE GATE: the namesake arm reproduces the receipt's own published row -- the "
      "crossing peaks 220/540/820/1132, P1/P2 2.273 and P1/P3 2.319, the 700-1000 band at 4.02 per "
      "bin, and the radiation-free ruler at 172.3",
      O['matched']['pk'][:4] == [220, 540, 820, 1132]
      and abs(O['matched']['p12'] - 2.273) < 5e-4 and abs(O['matched']['p13'] - 2.319) < 5e-4
      and abs(_b700(O['matched']) - 4.02) < 5e-3 and abs(O['matched']['lA'] - 172.324) < 5e-4,
      f"peaks {O['matched']['pk'][:4]}, {O['matched']['p12']:.3f}/{O['matched']['p13']:.3f}, "
      f"band {_b700(O['matched']):.2f}, ruler {O['matched']['lA']:.3f}")

print()
print(BAR)
print("  PART 3 -- ⛭⛭ THE RULER ON THE ARM OF RECORD, MEASURED AND NOT TAKEN FROM THE BANK'S NOTE")
print(BAR)
print(f"    the radiation-free ruler: namesake {O['matched']['lA']:.3f}, "
      f"arm of record {N['matched']['lA']:.3f}  -- a move of "
      f"{abs(N['matched']['lA'] / O['matched']['lA'] - 1) * 100:.2f} per cent")
print(f"    r_s: namesake {O['matched']['rs']:.3f}, arm of record {N['matched']['rs']:.3f}")
print(f"    and all four re-banked files carry the SAME ruler: "
      + ", ".join(f"{N[k]['lA']:.3f}" for k in ('crossing', 'matched', 'los')))
check("⛭⛭ THE RULER READS 171.554 ON THE ARM OF RECORD, against the namesake's 172.324 -- a move of "
      "0.45 per cent.  ⇒ ** So the receipt's title survives the re-point: 70's `LEAFSCALES=0` "
      "rebank keeps the ruler at 172 to the title's precision, where r7635's `LEAFSCALES=1` rebuild "
      "read 302.9 and would have collapsed it onto the body's comb **",
      abs(N['matched']['lA'] - 171.554) < 5e-3
      and abs(N['matched']['lA'] / O['matched']['lA'] - 1) < 0.01
      and round(N['matched']['lA']) == 172,
      f"{N['matched']['lA']:.3f} against {O['matched']['lA']:.3f}, rounding to "
      f"{round(N['matched']['lA'])}")
check("⌗ and the three crossing paths agree on it to the last recorded digit, which is what makes it "
      "the configuration's ruler rather than one path's",
      len({round(N[k]['lA'], 3) for k in ('crossing', 'matched', 'los')}) == 1,
      ", ".join(f"{N[k]['lA']:.3f}" for k in ('crossing', 'matched', 'los')))

print()
print(BAR)
print("  PART 4 -- THE FOUR PART-7 GATES, RE-ASKED ON THE ARM OF RECORD")
print(BAR)
IMP = {a: {k: np.pi * A[a][k]['DM'] / A[a][k]['cb'] for k in RUNS} for a in A}
print(f"    {'arm':>9} {'run':>9} {'r_s computed':>13} {'comb':>7} {'r_s implied':>12} {'ratio':>7}")
for a in ('namesake', 'aor'):
    for k in ('lcdm', 'pinned', 'matched'):
        print(f"    {a:>9} {k:>9} {A[a][k]['rs']:>13.2f} {A[a][k]['cb']:>7.1f} "
              f"{IMP[a][k]:>12.2f} {IMP[a][k] / A[a][k]['rs']:>7.3f}")
print(f"    the sky's comb: {(SKY[2] - SKY[0]) / 2:.1f}")
check("⓵ on the control the ruler and the comb still agree to better than 1 per cent -- the control "
      "does not move, so this is unchanged and asserted rather than skipped",
      abs(IMP['aor']['lcdm'] / A['aor']['lcdm']['rs'] - 1.0) < 0.01
      and A['aor']['lcdm']['file'] == 'c54.178_lcdm',
      f"{IMP['aor']['lcdm'] / A['aor']['lcdm']['rs']:.4f}")
check("⓶ and on the crossing configuration they still come apart by more than 40 per cent on the "
      "arm of record, which is the receipt's load-bearing claim",
      abs(IMP['aor']['matched'] / A['aor']['matched']['rs'] - 1.0) > 0.4,
      f"{abs(IMP['aor']['matched'] / A['aor']['matched']['rs'] - 1.0) * 100:.1f} per cent, against "
      f"the namesake's {abs(IMP['namesake']['matched'] / A['namesake']['matched']['rs'] - 1.0) * 100:.1f}")
check("⓷ and what the SPECTRUM carries is still the physical scale: its implied r_s is within 2 per "
      "cent of the control's",
      abs(IMP['aor']['matched'] / IMP['aor']['lcdm'] - 1.0) < 0.02,
      f"{abs(IMP['aor']['matched'] / IMP['aor']['lcdm'] - 1.0) * 100:.2f} per cent")
check("⓸ and the crossing spectrum's comb is still within 5 per cent of the sky's",
      abs(A['aor']['matched']['cb'] / ((SKY[2] - SKY[0]) / 2) - 1.0) < 0.05,
      f"{A['aor']['matched']['cb']:.1f} against {(SKY[2] - SKY[0]) / 2:.1f}, "
      f"{abs(A['aor']['matched']['cb'] / ((SKY[2] - SKY[0]) / 2) - 1.0) * 100:.1f} per cent")

print()
print(BAR)
print("  PART 5 -- THE CARRY, AND THE SECOND PEAK THAT THREE RECEIPTS NOW AGREE ON")
print(BAR)
_solo_rs, _solo_cb = (lambda e: (e[3], comb(peaks(e[0], e[1]))))(
    load('r6784_cr_crossing_hier_noCRIC_leafrec1'))
check("⛭ THE CARRY HAS NOTHING TO ACT ON: the arm's side of every comparison here is a ruler length, "
      "a comb spacing or a chi^2 of its OWN spectrum -- recomputed from that file alone it is "
      "bit-identical to the pipeline's.  ** And the one cross-arm ratio is a ratio of two LENGTHS, "
      "not of comb-band powers, so the comb-offset map has nothing to remove.  Class 3 **",
      _solo_rs == N['matched']['rs'] and _solo_cb == N['matched']['cb'],
      f"solo r_s {_solo_rs:.6f} / comb {_solo_cb:.6f} against pipeline "
      f"{N['matched']['rs']:.6f} / {N['matched']['cb']:.6f}")
#: ⛭⛭ ** AND A CROSS-CHECK THAT COSTS NOTHING AND IS WORTH MORE THAN A GATE. **  The arm of record's
#: SECOND peak lands at 532 here, where the namesake's is at 540.  `r7641+cc66.39` measured the same
#: 532 on `cc66_r185_verify_cr_leafrec1` with a different locator, and the ladders receipt prints it
#: on the re-banked continuum run.  ⇒ *Three receipts, three locators, three banks: the 532 is the arm
#: of record's spectrum and not any one reading of it.*
check("⛭⛭ AND THE SECOND PEAK AT 532 IS CONFIRMED BY A THIRD INDEPENDENT ROUTE: this receipt's own "
      "locator puts the arm of record's second peak at 532 against the namesake's 540, which is "
      "what `cc66.39` measured on the 185-bin verification spectrum and what the ladders receipt "
      "prints on the re-banked continuum run.  ⇒ ** Three receipts, three locators, three banks: "
      "the 532 is the spectrum's and not a locator artefact **",
      N['matched']['pk'][1] == 532 and O['matched']['pk'][1] == 540,
      f"arm of record {N['matched']['pk'][:4]}, namesake {O['matched']['pk'][:4]}")

print()
print(BAR)
print("  PART 6 -- ⛔⛭⛭ AND THE RECEIPT'S OTHER COMPARISON LOSES ITS SUBJECT, WHICH IS A FOURTH")
print("  KIND OF BLOCK AND NOT ONE OF THE THREE ALREADY CATALOGUED")
print(BAR)
#: ** THE RECEIPT'S HEADER DEFINES THE CROSSING CONFIGURATION AS: ** *"Same command as the banked
#: `c54.178_cr` with three knobs changed -- `CRH0 = 68.62`, `CROM = 0.2973`, `ZSTART = 3e7` -- and
#: nothing else."*  ⇒ *On the arm of record BOTH are re-run at the arm of record's own point, so all
#: three of those knobs now agree, and the only switch left between them is `LEAFSCALES`.*
#:   ⛔ ** WHICH IS WHY THE chi^2 MUST NOT BE READ AS AN IMPROVEMENT. **  The superseded
#:   configuration scores 51817.0 on the namesake and 923.9 on the arm of record -- a factor of 56.
#:   *That is not the construction getting better: it is a different background point.  Reported as
#:   a factor of 56 it would have been one of the worst numbers this seat could publish.*
_swa, _swb = {}, {}
for _n, _d in (('c54.178_cr_leafrec1', _swa),
               ('r6784_cr_crossing_hier_noCRIC_leafrec1', _swb)):
    _z = np.load(os.path.join(SPEC, _n + '.npz'), allow_pickle=True)
    _m = _z['manifest'].item()
    if isinstance(_m, (bytes, str)):
        import ast as _ast
        _m = _ast.literal_eval(_m if isinstance(_m, str) else _m.decode())
    _d.update(dict(t.split('=', 1) for t in _m['switches'].split() if '=' in t))
_diff = sorted(k for k in set(_swa) | set(_swb)
               if _swa.get(k, '(unset)') != _swb.get(k, '(unset)'))
print(f"    the superseded config and the crossing config, arm of record, token by token:")
for k in sorted(set(_swa) | set(_swb)):
    print(f"      {k:12s} {_swa.get(k, '(unset)'):14s} {_swb.get(k, '(unset)'):14s}"
          f"{'   <<< differs' if k in _diff else ''}")
_rel = float(np.max(np.abs(N['pinned']['Dl'] - N['matched']['Dl']))
             / np.max(np.abs(N['matched']['Dl'])))
print(f"    and their spectra differ by {_rel:.3e} of the peak")
check("⛔⛭⛭ THE 'AGAINST THE CONFIGURATION THIS REPLACES' COMPARISON HAS NO SUBJECT ON THE ARM OF "
      "RECORD: the receipt defines the crossing config as `c54.178_cr` with CRH0, CROM and ZSTART "
      "changed and nothing else, and on the arm of record BOTH are re-run at the arm of record's "
      "point -- so those three agree and the ONLY remaining switch is `LEAFSCALES`.  ⇒ ** The two "
      "sides of that comparison have converged into one configuration with one knob between them, "
      "which is a FOURTH kind of block: not a centre, not a missing run, not a paper-bound "
      "comparison, but a contrast whose two sides meet when both are moved to the same arm **",
      _diff == ['LEAFSCALES'] and _rel < 0.01,
      f"differing tokens {_diff}, spectra {_rel:.3e} of peak apart")
check("⛔ AND THE 56-FOLD chi^2 FALL IS THEREFORE NOT A RESULT: 51817.0 to 923.9 is the superseded "
      "configuration re-run at a DIFFERENT BACKGROUND POINT, not the construction improving.  ⇒ "
      "** Gated here so that no later reader can take the number out of the table without the "
      "reason attached **",
      O['pinned']['chi2'] / N['pinned']['chi2'] > 50
      and _diff == ['LEAFSCALES']
      and abs(O['pinned']['lA'] - 301.600) < 5e-3,
      f"{O['pinned']['chi2']:.1f} -> {N['pinned']['chi2']:.1f}, a factor "
      f"{O['pinned']['chi2'] / N['pinned']['chi2']:.0f}")

print()
print(BAR)
print("  PART 7 -- WHAT MOVES, OLD -> NEW")
print(BAR)
ROWS = [('radiation-free ruler', O['matched']['lA'], N['matched']['lA'], '.3f'),
        ('r_s computed', O['matched']['rs'], N['matched']['rs'], '.2f'),
        ('D_M', O['matched']['DM'], N['matched']['DM'], '.1f'),
        ('crossing comb', O['matched']['cb'], N['matched']['cb'], '.1f'),
        ('r_s implied by the comb', IMP['namesake']['matched'], IMP['aor']['matched'], '.2f'),
        ('implied/computed ratio', IMP['namesake']['matched'] / O['matched']['rs'],
         IMP['aor']['matched'] / N['matched']['rs'], '.3f'),
        ('P1/P2', O['matched']['p12'], N['matched']['p12'], '.3f'),
        ('P1/P3', O['matched']['p13'], N['matched']['p13'], '.3f'),
        ('chi^2, crossing', O['matched']['chi2'], N['matched']['chi2'], '.1f'),
        ('700-1000 band, per bin', _b700(O['matched']), _b700(N['matched']), '.2f'),
        ('second peak', O['matched']['pk'][1], N['matched']['pk'][1], 'd'),
        ('chi^2, superseded config', O['pinned']['chi2'], N['pinned']['chi2'], '.1f'),
        ('ruler, superseded config', O['pinned']['lA'], N['pinned']['lA'], '.3f')]
#: ⛔ *the last two rows are NOT a move of the same quantity -- see PART 6 -- and are printed with
#: that said rather than left in a table a reader would take at face value.*
print(f"    {'figure':>26} {'namesake':>12} {'arm of record':>14}   verdict")
for lab, o, n, f in ROWS:
    v = 'unchanged' if abs(n - o) < 1e-12 else (
        'MOVED' if abs(n - o) > 0.005 * max(1e-12, abs(o)) else 'moved (trace)')
    print(f"    {lab:>26} {format(o, f):>12} {format(n, f):>14}   {v}")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
