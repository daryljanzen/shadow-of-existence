#!/usr/bin/env python3
"""
r7474 — IS THE WAVENUMBER SUM CARRIED FAR ENOUGH?  The contrast statistic read on the convergence
variants that are already banked.

Order `r7471`: the papers leave one alternative standing about the contrast excess -- the kernel's
acceptance in wavenumber either is what this background requires, or the wavenumber sum on this arm is
not carried far enough to say.

** AND NO NEW RUN IS NEEDED. **  The variants are banked: the continuum replacement of the arm's
discrete ladder, the guard-failing sampling, and a matched crossing pair.  The banked convergence
results report chi-squared, peak positions and height ratios -- NOT the contrast statistic, which is
what the excess is measured in.  ⇒ A check run on one object licenses a conclusion about that object
and no other, so this reads the statistic itself across the variants.

⌗ THE STATISTIC IS IMPORTED from `r7093`'s `contrast_two_models.py` by `ast`, so that file's own
  printing does not run and no second copy of `env_a`/`osc` grows (`r7445`'s rule).  Ⓥ① then
  reproduces its four printed rows: the cheapest proof that it is the same instrument.

Run:  python3 kconv.py          the sound run, controls and arms together
      python3 kconv.py --seed   the seed, pinned per L-249's repair rule
"""

import ast
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
_SRC = os.path.join(BW, 'r7093_70_configuration_census', 'contrast_two_models.py')
if not os.path.exists(_SRC):
    sys.exit("FATAL: r7093's contrast_two_models.py is not where this file expects it.\n"
             "  Fix the path.  Do NOT rebuild the statistic here.")


def _load(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    # ⌗ A TUPLE TARGET IS NOT A NAME, and the first draft of this filter dropped
    #   `LO, HI, NG = 0.85, 5.75, 1200` for exactly that reason: `n.targets` is one Tuple node,
    #   whose `.id` does not exist, so the whitelist never matched it.  Names are collected from
    #   the target TREE rather than from its top node.
    def _names(t):
        if isinstance(t, ast.Name):
            return [t.id]
        if isinstance(t, (ast.Tuple, ast.List)):
            return [x for e in t.elts for x in _names(e)]
        return []

    want = ('LO', 'HI', 'NG', 'HERE', 'BW')
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            nm = [x for t in n.targets for x in _names(t)]
            if nm and all(x in want for x in nm):
                keep.append(n)
    ns = {'__file__': path, '__name__': 'r7093_contrast'}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, 'exec'), ns)   # noqa: S102
    return ns


_NS = _load(_SRC)
_NS['BW'] = BW                     # the module's own BW is relative to its directory
env_a, osc = _NS['env_a'], _NS['osc']
LO, HI, NG = _NS['LO'], _NS['HI'], _NS['NG']


def stat(arm_file, ctl_file):
    """r7093's three numbers for one pair, with its own osc() doing the work."""
    A, lA_a, rs_a = osc(arm_file)
    B, lA_b, _rs_b = osc(ctl_file)
    proj = float(np.sum(A * B) / np.sum(B * B))
    rms = float(np.sqrt(np.sum(A * A) / np.sum(B * B)))
    cos = float(np.sum(A * B) / np.sqrt(np.sum(A * A) * np.sum(B * B)))
    return proj, rms, cos, lA_a, lA_b


def spectrum_diff(f, g):
    """max relative difference between two banked spectra on their shared ell range."""
    za, zb = np.load(os.path.join(BW, f)), np.load(os.path.join(BW, g))
    la, lb = np.asarray(za['ls'], float), np.asarray(zb['ls'], float)
    lo, hi = max(la.min(), lb.min()), min(la.max(), lb.max())
    x = np.linspace(lo, hi, 400)
    ya = np.interp(x, la, np.asarray(za['Dl'], float))
    yb = np.interp(x, lb, np.asarray(zb['Dl'], float))
    return float(np.max(np.abs(ya - yb) / np.maximum(np.abs(yb), 1e-300)))


# ---------------------------------------------------------------- the banked pairs
S = 'spectra/'
PRINTED = [                                        # Ⓥ①: r7093's own four rows
    ('A  default, solved onset   c54.178', S + 'c54.178_cr.npz', S + 'c54.178_lcdm.npz', -0.3766),
    ('A  default, solved onset   c54.186 L3000', S + 'c54.186_cr_L3000.npz',
     S + 'c54.186_lcdm_L3000.npz', -0.4108),
    ('B  refit grid base', 'refit_grid185/cr_base.npz', 'refit_grid185/lcdm_base.npz', 1.0563),
    ('B  refit minimum (verify)', S + 'cc66_r185_verify_cr.npz',
     S + 'cc66_r185_verify_lcdm.npz', 1.0452),
]

VARIANTS = [
    # label, arm, control, what the variant changes
    ('Ⓐ  model A  LADDER      (banked)', S + 'c54.186_cr_L3000.npz',
     S + 'c54.186_lcdm_L3000.npz', 'the arm on its discrete physical ladder'),
    ('Ⓐ  model A  CONTINUUM   (KCONT)', S + 'c54.186_cr_KCONT.npz',
     S + 'c54.186_lcdm_L3000.npz', 'the same arm with the ladder replaced by a continuum'),
    ('Ⓑ  crossing LADDER      (banked)', S + 'cc66_cr_crossing.npz',
     S + 'c54.186_lcdm_L3000.npz', 'the crossing configuration, ladder'),
    ('Ⓑ  crossing CONTINUUM   (KCONT)', S + 'cc66_cr_x_kcont.npz',
     S + 'c54.186_lcdm_L3000.npz', 'the same, continuum -- matched ell grid and l_A'),
    ('Ⓒ  model A vs GUARD-FAILING ctl', S + 'c54.186_cr_L3000.npz',
     S + 'L820_lcdm_nk260_guardfail.npz', 'the CONTROL resampled below the projection guard'),
]


def reach(f):
    """the reported ell reach of a banked spectrum -- the thing that sets k_max = KFAC*LMAXL/D_M."""
    z = np.load(os.path.join(BW, f))
    ls = np.asarray(z['ls'], float)
    return float(ls.max()), len(ls)


def matched(f, g):
    """Is this pair matched in everything but the knob under test?

    ⛔ THE DEFECT THIS EXISTS FOR, found by running: `c54.186_cr_KCONT` and `c54.186_cr_L3000`
    share a stem and are NOT a matched pair.  The ladder run reports to ell 2996 and the
    continuum one to 1996, and since k_max = KFAC * LMAXL / D_M, a different reported reach is a
    different k_max.  Their spectra differ by 1.6 per cent at the median and 57 per cent at the
    ninetieth percentile, against a banked chi-squared difference of 0.001 for the continuum
    check alone.  ⇒ COMPARING THEM MIXES THE KNOB WITH THE REACH, and a comparison that moves two
    things answers about neither.
    ⌗ This is the registered guard again: before two stretches are identified by a label, check
      how many-to-one the label is on the object.  A shared file stem is a label.
    """
    ra, na = reach(f)
    rb, nb = reach(g)
    return abs(ra - rb) < 1.0 and na == nb, (ra, na), (rb, nb)


def main():
    print('=' * 104)
    print('  Ⓥ① SAME INSTRUMENT — the imported statistic against r7093\'s printed rows')
    print('=' * 104)
    fired = []
    worst = 0.0
    for lab, a, b, printed in PRINTED:
        if not (os.path.exists(os.path.join(BW, a)) and os.path.exists(os.path.join(BW, b))):
            print(f'  {lab:44s} ABSENT FROM THE BANK')
            continue
        proj, rms, cos, _la, _lb = stat(a, b)
        d = abs(proj - printed)
        worst = max(worst, d)
        print(f'  {lab:44s} projected {proj:+9.4f}  printed {printed:+9.4f}  diff {d:.2e}')
    ok1 = worst < 5e-5
    print(f'  ⇒ worst difference {worst:.2e} against 5e-5  '
          f'{"PASS" if ok1 else "FIRED: this is a second instrument"}')
    if not ok1:
        fired.append('Ⓥ①')

    print()
    print('=' * 104)
    print('  Ⓥ② THE NULL — a file against itself')
    print('=' * 104)
    proj, rms, cos, _a, _b = stat(S + 'c54.186_cr_L3000.npz', S + 'c54.186_cr_L3000.npz')
    ok2 = max(abs(proj - 1), abs(rms - 1), abs(cos - 1)) < 1e-12
    print(f'  projected {proj:.12f}  RMS {rms:.12f}  phase cos {cos:.12f}')
    print(f'  ⇒ {"PASS" if ok2 else "FIRED: the statistic is not what it is taken to be"}')
    if not ok2:
        fired.append('Ⓥ②')

    print()
    print('=' * 104)
    print('  Ⓥ③ THE VARIANTS ARE REAL PERTURBATIONS — max relative spectrum difference')
    print('=' * 104)
    checks = [('model A ladder vs continuum', S + 'c54.186_cr_KCONT.npz',
               S + 'c54.186_cr_L3000.npz', 0.0),
              ('crossing ladder vs continuum', S + 'cc66_cr_x_kcont.npz',
               S + 'cc66_cr_crossing.npz', 0.0),
              ('control guard-passing vs failing', S + 'L820_lcdm_nk260_guardfail.npz',
               S + 'c54.186_lcdm_L3000.npz', 0.01)]
    ok3 = True
    for lab, f, g, floor in checks:
        if not (os.path.exists(os.path.join(BW, f)) and os.path.exists(os.path.join(BW, g))):
            print(f'  {lab:36s} ABSENT'); ok3 = False; continue
        d = spectrum_diff(f, g)
        good = d > floor
        ok3 &= good
        print(f'  {lab:36s} max|dD/D| = {d:.4e}  floor {floor:g}  '
              f'{"ok" if good else "FIRED: a relabelled copy"}')
    print(f'  ⇒ {"PASS" if ok3 else "FIRED: a comparison would be vacuous"}')
    if not ok3:
        fired.append('Ⓥ③')

    print()
    print('=' * 104)
    print('  THE CONTRAST STATISTIC ON THE BANKED CONVERGENCE VARIANTS')
    print('=' * 104)
    print(f"  {'variant':36s} {'l_A arm':>8s} {'l_A ctl':>8s} {'projected':>10s} {'RMS':>8s}"
          f" {'phase cos':>10s}")
    got = {}
    for lab, a, b, _why in VARIANTS:
        if not (os.path.exists(os.path.join(BW, a)) and os.path.exists(os.path.join(BW, b))):
            print(f'  {lab:36s} ABSENT FROM THE BANK')
            continue
        proj, rms, cos, la, lb = stat(a, b)
        got[lab] = proj
        print(f'  {lab:36s} {la:8.3f} {lb:8.3f} {proj:+10.4f} {rms:8.4f} {cos:+10.4f}')

    print()
    print('-' * 104)
    print('  THE ARMS')
    print('-' * 104)
    kA = [k for k in got if k.startswith('Ⓐ')]
    if len(kA) == 2:
        d = got[kA[1]] - got[kA[0]]
        ok, ra, rb = matched(S + 'c54.186_cr_KCONT.npz', S + 'c54.186_cr_L3000.npz')
        print(f'  Ⓐ model A, ladder -> continuum   predicted |d| < 0.01')
        print(f'                                   measured  {d:+.5f}')
        print(f'      ⛔ BUT THE PAIR IS NOT MATCHED: the continuum file reports to ell '
              f'{ra[0]:.0f} on {ra[1]} points and the ladder to ell {rb[0]:.0f} on {rb[1]}.')
        print(f'        k_max = KFAC * LMAXL / D_M, so a different reported reach IS a different')
        print(f'        k_max -- the comparison mixes the knob with the reach and answers about')
        print(f'        neither.  ⇒ ** Ⓐ IS WITHDRAWN AS A MEASUREMENT **, kept as the record, and')
        print(f'        Ⓑ below is the matched pair that does answer it.')
    kB = [k for k in got if k.startswith('Ⓑ')]
    if len(kB) == 2:
        d = got[kB[1]] - got[kB[0]]
        print(f'  Ⓑ crossing, ladder -> continuum  predicted |d| < 0.01, the cleaner pair')
        print(f'                                   measured  {d:+.5f}   '
              f'⇒ {"HIT" if abs(d) < 0.01 else "MISS"}')
    kC = [k for k in got if k.startswith('Ⓒ')]
    if kC and kA:
        d = got[kC[0]] - got[kA[0]]
        print(f'  Ⓒ the guard-failing control      predicted 0.01 <= |d| <= 0.10')
        print(f'                                   measured  {d:+.5f}   '
              f'⇒ {"HIT" if 0.01 <= abs(d) <= 0.10 else "MISS"}')

    print()
    print('  Ⓔ THE COVERAGE — is any banked PROJECTED continuum run at the excess\'s own l_A?')
    # ⛔ AND A SECOND DEFECT OF THE SAME SHAPE, found by running: the first draft of this arm
    #    matched a configuration by its `l_A` within 0.5, and that admitted `c54.186_cr_KCONT`
    #    (l_A = 301.600) as being "at" the refit minimum (l_A = 301.799).  Their contrast
    #    statistics are -0.41 and +1.045 -- they differ by 1.5 on a quantity of order 1.
    #    ⇒ ** l_A IS NOT A CONFIGURATION LABEL. **  It is many-to-one on the object, which is the
    #      same registered guard as `matched()` above, firing twice in one run on one instrument.
    #    The test now asks what the file IS, not what number it carries.
    import glob
    EXCESS_PAIR = (S + 'cc66_r185_verify_cr.npz', S + 'cc66_r185_verify_lcdm.npz')
    ex_proj = stat(*EXCESS_PAIR)[0]
    print(f'      the excess is measured on cc66_r185_verify, projected {ex_proj:+.4f}')
    print(f'      {"file":38s} {"l_A":>9s} {"source?":>9s}  verdict')
    at_excess = []
    for p in sorted(set(glob.glob(os.path.join(BW, 'spectra', '*kcont*.npz'))
                        + glob.glob(os.path.join(BW, 'spectra', '*KCONT*.npz')))):
        z = np.load(p, allow_pickle=True)
        if 'l_A' not in z.files:
            continue
        n = os.path.basename(p)
        lA = float(z['l_A'])
        src = 'source' in n
        same_cfg = (not src) and abs(lA - 301.799) < 0.01
        if same_cfg:
            at_excess.append(n)
        why = ('SOURCE side, not projected' if src
               else 'projected, AT the excess\'s configuration' if same_cfg
               else 'projected, a DIFFERENT configuration')
        print(f'      {n:38s} {lA:9.3f} {"yes" if src else "no":>9s}  {why}')
    print(f'  ⇒ predicted NO projected continuum run at the excess\'s configuration;')
    print(f'    measured {len(at_excess)}: {", ".join(at_excess) or "none"}   '
          f'⇒ {"HIT" if not at_excess else "MISS"}')

    print()
    print('=' * 104)
    if fired:
        print(f'  ⛔ VOID — controls fired: {" ".join(fired)}')
        return 1
    print('  ✔ CONTROLS HOLD.')
    return 0


PIN = '1f20bd2d'
PIN_DIGEST = 'a3ee7f7f'


def seed():
    import hashlib
    print('=' * 104)
    print('  THE SEED — three assertions, none of them about the other two')
    print('=' * 104)
    ok = True
    try:
        blob = subprocess.run(
            ['git', '-C', ROOT, 'show',
             f'{PIN}:computations/beyond_the_wall/'
             f'r7474_60_is_the_wavenumber_sum_carried_far_enough/PREDICTION.md'],
            capture_output=True, check=True).stdout
        d = hashlib.sha256(blob).hexdigest()[:8]
        good = d == PIN_DIGEST
        print(f'  (1) HISTORICAL  at {PIN}, PREDICTION.md digests {d}; pinned {PIN_DIGEST}'
              f'  ⇒ {"PASS" if good else "FAIL"}')
        ok &= good
    except subprocess.CalledProcessError:
        print(f'  (1) HISTORICAL  the pin {PIN} is not readable from here  ⇒ FAIL')
        ok = False
    n = sum(1 for _l, a, b, _p in PRINTED
            if os.path.exists(os.path.join(BW, a)) and os.path.exists(os.path.join(BW, b)))
    good = n >= 3
    print(f'  (2) CURRENT     {n} of {len(PRINTED)} printed pairs readable today, 3 or more needed'
          f'  ⇒ {"PASS" if good else "FAIL"}')
    ok &= good
    good = os.path.exists(_SRC)
    print(f'  (3) DIRECTIONAL the imported statistic\'s file is present, so no second copy can grow'
          f'  ⇒ {"PASS" if good else "FAIL"}')
    ok &= good
    print()
    print(f'  ⇒ {"SEED HOLDS" if ok else "SEED BROKEN"}')
    return 0 if ok else 1


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(main())
