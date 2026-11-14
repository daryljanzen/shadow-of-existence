#!/usr/bin/env python3
r"""r7779+cc66 item (1): the low-multipole depths on the ONE RATE against the arm of record.

Registered in PREDICTION.md (r7779+cc66.0) before any depth array was opened.

The switch, as 69 named it, confirmed against the instrument's own source:
  one rate       = HIER_photon_hierarchy.py with ARM unset AND SPLITCLOCK unset
  arm of record  = SPLITCLOCK=L     (grid/projection on the stacking rate, ionisation on the leaf
                                     rate, perturbation dynamics on the leaf rate chain-ruled onto
                                     the stacking grid by Jac_of)
  SPLITCLOCK=1   = the RETIRED STACKPERT pairing.  Not read here.

A depth is the ratio of the boundary-quantised discrete sum to the continuum integral OF THE SAME
transfer at the same l.  depth -> 1 is recovery.  Banked l = 2..8, rounded to 4 decimals by both
producers (r7689 bank_one_clock.py:50, r7695 run_leafpert.py:56), so the measurement grain is
5e-5 ABSOLUTE.

rc=0 if every row holds.
"""
import ast
import importlib.util
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')

# the projection distance's own move between these two rate choices, r7767 item 2
DM_MOVE = 0.004984
GRAIN = 5e-5                      # half of the banks' 4-decimal rounding step
OK = []


def row(tag, good, text):
    OK.append((tag, good, text))
    print(f'{"PASS" if good else "FAIL"}  {tag}  {text}', flush=True)


def load(stem):
    d = np.load(os.path.join(SP, stem + '.npz'), allow_pickle=True)
    cfg = d['config'].item() if d['config'].shape == () else d['config']
    man = d['manifest'].item() if d['manifest'].shape == () else d['manifest']
    return d, json.loads(str(cfg)), json.loads(str(man))


LP, LP_C, LP_M = load('p15_lowell_depths_leafpert_leafrec1')
OC, OC_C, OC_M = load('p15_lowell_depths_distances_oneclock_leafrec1')
AA, AA_C, AA_M = load('p15_lowell_depths_armA_leafpert_leafrec1')
ELLS = [int(x) for x in LP['ells']]
assert ELLS == [int(x) for x in OC['ells']] == [int(x) for x in AA['ells']], 'ell grids differ'

print('=' * 99)
print('R0  THE CLOCK-ONLY PAIRS THE BANK ALREADY HOLDS, ONCE SPLITCLOCK IS THE SWITCH')
print('=' * 99)

# a pair is clock-only when both legs sit in ONE file (so one instrument blob, one producer run)
# and the file's per-row config agrees on everything but SPLITCLOCK.
PAIRS = [('arm A, distances', AA, 'distances__armA__L', 'distances__armA__one_clock_gate'),
         ('arm A, refit', AA, 'refit__armA__L', 'refit__armA__one_clock_gate'),
         ('arm B frozen, refit', LP, 'refit__armB_frozen__L', 'refit__armB_frozen__one_clock'),
         ('arm B decoupled, refit', LP, 'refit__armB_decoupled__L', 'refit__armB_decoupled__one_clock')]
CFG = {id(AA): AA_C, id(LP): LP_C}

resolved, cfg_bad = [], []
for label, src, kL, kO in PAIRS:
    if kL not in src or kO not in src:
        cfg_bad.append(f'{label}: key missing')
        continue
    c = CFG[id(src)]
    # every per-row dict in the config must agree between the two rows except SPLITCLOCK
    for field, v in c.items():
        if not isinstance(v, dict) or kL not in v:
            continue
        if field == 'SPLITCLOCK':
            if not (v[kL] == 'L' and v[kO] is None):
                cfg_bad.append(f'{label}/{field}: {v[kL]!r} vs {v[kO]!r} is not L-vs-unset')
            continue
        if field == 'pairing':
            continue                       # prose, differs BY DESIGN -- it describes the clock
        if v[kL] != v[kO]:
            cfg_bad.append(f'{label}/{field}: {v[kL]!r} != {v[kO]!r}')
    resolved.append(label)
    print(f'    {label:24s}  {kL}  vs  {kO}')

row('R0', len(resolved) == 4 and not cfg_bad,
    f'{len(resolved)} clock-only pairs resolved, each inside ONE .npz; '
    + ('every config field but SPLITCLOCK equal within each pair' if not cfg_bad else '; '.join(cfg_bad)))

print()
print('=' * 99)
print('R1  AND THE ONE PAIR THE ORDER NAMES IS THE ONE THAT IS NOT CLOCK-ONLY: THE BLOBS DIFFER')
print('=' * 99)
blob_lp, blob_oc = LP_C['HIER_blob'], OC_C['HIER_blob']
cur = subprocess.run(['git', 'hash-object', 'storyboard_receipts/HIER_photon_hierarchy.py'],
                     cwd=ROOT, capture_output=True, text=True).stdout.strip()
print(f'    leafpert (distances__armB_*__L) HIER_blob  {blob_lp}')
print(f'    oneclock (armB_* at same point) HIER_blob  {blob_oc}')
print(f'    working tree                               {cur}')
row('R1', blob_lp != blob_oc and cur == blob_lp,
    'the two legs of the distances-point pair were produced by DIFFERENT instrument versions, '
    'and the current tree carries the leafpert one')

print()
print('=' * 99)
print("R2'  THE BLOB DIFFERENCE IS INERT WITH SPLITCLOCK UNSET -- BY NORMALISED-AST EQUALITY")
print('=' * 99)
print('    R2 as first written asked that every differing EXECUTABLE line name a split token.  That')
print('    test fails any rename regardless of inertness: the REMOVED lines `Hc=Hc_of(e)` and')
print('    `return out` name no split token because they are the lines being replaced.  R2-prime')
print('    asserts the claim properly -- the newer blob IS the same program with SPLITCLOCK unset.')
SCR = os.environ.get('R7779_SCRATCH', '/tmp/r7779_cc66')
os.makedirs(SCR, exist_ok=True)
SB = os.path.join(ROOT, 'storyboard_receipts')
paths = {}
for tag, blob in (('old', blob_oc), ('new', blob_lp)):
    q = os.path.join(SCR, f'_r7779_hier_{tag}.py')
    with open(q, 'wb') as fh:
        fh.write(subprocess.run(['git', 'cat-file', '-p', blob], cwd=ROOT, capture_output=True).stdout)
    paths[tag] = q


class Norm(ast.NodeTransformer):
    """Reduce a tree to what it IS when SPLITCLOCK is unset (so _SPLITL is False)."""

    def visit_Name(self, node):
        if node.id == '_Hdyn':                            # _Hdyn is bound to Hc_of itself
            return ast.copy_location(ast.Name(id='Hc_of', ctx=node.ctx), node)
        return node

    def visit_IfExp(self, node):
        self.generic_visit(node)
        if isinstance(node.test, ast.Name) and node.test.id == '_SPLITL':
            return node.orelse                            # the False branch
        return node

    def visit_If(self, node):
        self.generic_visit(node)
        if isinstance(node.test, ast.Name) and node.test.id == '_SPLITL':
            return node.orelse or None                    # never entered
        return node

    def visit_Assign(self, node):
        self.generic_visit(node)
        t = node.targets[0]
        if isinstance(t, ast.Name):
            if t.id == '_SPLITL':
                return None                               # a flag that evaluates False
            if t.id == 'Hc_of' and isinstance(node.value, ast.Name) and node.value.id == 'Hc_of':
                return None                               # was `_Hdyn = Hc_of`
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.Or):
            keep = [v for v in node.values if not (isinstance(v, ast.Name) and v.id == '_SPLITL')]
            if len(keep) != len(node.values):
                return keep[0] if len(keep) == 1 else ast.BoolOp(op=node.op, values=keep)
        return node


dumps = {}
for tag, q in paths.items():
    tree = Norm().visit(ast.parse(open(q).read()))
    ast.fix_missing_locations(tree)
    dumps[tag] = ast.dump(tree)
ast_same = dumps['old'] == dumps['new']
raw_same = open(paths['old']).read() == open(paths['new']).read()
print(f'    raw blobs identical: {raw_same}   normalised ASTs identical: {ast_same}')
if not ast_same:
    import difflib
    d = list(difflib.unified_diff(dumps['old'].split(','), dumps['new'].split(','), n=0))
    print('    first normalised-AST differences:')
    for ln in d[2:12]:
        print('      ', ln[:150])

# second, independent arm: import both with SPLITCLOCK and ARM unset and compare what the
# dynamics actually read.
for v in ('SPLITCLOCK', 'ARM', 'SPLITIC'):
    os.environ.pop(v, None)
mods = {}
for tag, q in paths.items():
    if SB not in sys.path:
        sys.path.insert(0, SB)
    s = importlib.util.spec_from_file_location(f'hier_{tag}', q)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    mods[tag] = m
o, n = mods['old'], mods['new']
probe = np.linspace(float(n.eg[1]), float(n.eg[-1]), 4001)
num = {}
for name in ('Hc_of', 'Og_of', 'On_of', 'Oc_of', 'Rb_of'):
    num[name] = float(np.max(np.abs(getattr(o, name)(probe) - getattr(n, name)(probe))))
for name in ('eg', 'ag'):
    num[name] = float(np.max(np.abs(np.asarray(getattr(o, name)) - np.asarray(getattr(n, name)))))
for name in ('eta_onset', 'eta_rec'):
    if hasattr(o, name) and hasattr(n, name):
        num[name] = abs(float(getattr(o, name)) - float(getattr(n, name)))
worst = max(num.values())
ident = (n._SPLIT is False and n._SPLITL is False and n._Hdyn is n.Hc_of
         and not hasattr(n, 'Jac_of') and o._SPLIT is False)
print(f'    every rate spline the dynamics read, max |old - new| = {worst:.3e} '
      f'over {len(num)} objects')
print(f'    runtime: _SPLIT={n._SPLIT}  _SPLITL={n._SPLITL}  _Hdyn is Hc_of={n._Hdyn is n.Hc_of}  '
      f'Jac_of defined={hasattr(n, "Jac_of")}')
row("R2'", ast_same and ident and worst == 0.0,
    'with SPLITCLOCK unset the newer blob IS the same program: normalised ASTs identical, and '
    f'every rate object the dynamics read bit-identical (max {worst:.1e})'
    if ast_same and worst == 0.0 else
    f'normalised ASTs identical={ast_same}, worst rate-object move {worst:.3e}, identity={ident}')

print()
print('=' * 99)
print('R3/R4  THE DEPTHS AND THE RECOVERY MULTIPOLE, CLOCK AGAINST CLOCK')
print('=' * 99)


def recovery(d):
    return next((l for l, v in zip(ELLS, d) if l >= 5 and v >= 0.99), None)


def compare(label, dL, dO):
    dL, dO = np.asarray(dL, float), np.asarray(dO, float)
    rel = np.abs(dL / dO - 1.0)
    print(f'  {label}')
    print('      l        ' + ''.join(f'{l:>10d}' for l in ELLS))
    print('      (L)      ' + ''.join(f'{v:>10.4f}' for v in dL))
    print('      one rate ' + ''.join(f'{v:>10.4f}' for v in dO))
    print('      L/one-1  ' + ''.join(f'{v*100:>9.3f}%' for v in dL / dO - 1.0))
    print(f'      recovery (first l>=5 with depth>=0.99):  (L) {recovery(dL)}   one rate {recovery(dO)}')
    print(f'      largest move {rel.max()*100:.3f}% at l={ELLS[int(np.argmax(rel))]}; '
          f'the bank\'s own grain here is {GRAIN/np.min(np.abs(dO))*100:.3f}%')
    return rel.max(), recovery(dL) == recovery(dO), rel


moves, recs, worst_l = [], [], None
for label, src, kL, kO in PAIRS:
    mx, same, rel = compare(label, src[kL], src[kO])
    moves.append((label, mx))
    recs.append((label, same))
    if worst_l is None or mx > worst_l[1]:
        worst_l = (label, mx)

row('R3', all(m < DM_MOVE for _, m in moves),
    f'largest depth move over all four clock-only pairs is {worst_l[1]*100:.3f}% ({worst_l[0]}), '
    f'against the projection distance\'s own {DM_MOVE*100:.4f}%')
row('R4', all(s for _, s in recs),
    'the recovery multipole is the same under both clocks in every pair '
    + ', '.join(f'{l}:{"same" if s else "MOVED"}' for l, s in recs))

print()
print('=' * 99)
print('R5  THE FROZEN/DECOUPLED CROSS-VALIDATION SURVIVES THE CLOCK (refit point)')
print('=' * 99)
xv = {}
for clock, suf in (('(L)', 'L'), ('one rate', 'one_clock')):
    f = np.asarray(LP[f'refit__armB_frozen__{suf}'], float)
    d = np.asarray(LP[f'refit__armB_decoupled__{suf}'], float)
    xv[clock] = float(np.max(np.abs(f / d - 1.0)))
    print(f'    {clock:9s} max |frozen/decoupled - 1| = {xv[clock]*100:.2f}%')
RATIO_GRAIN = 2 * GRAIN / float(min(np.min(np.abs(np.asarray(LP[f'refit__armB_{b}__{s}'], float)))
                                     for b in ('frozen', 'decoupled') for s in ('L', 'one_clock')))
degrade = xv['one rate'] - xv['(L)']
print(f"    the registered condition was: FAILS IF the one rate exceeds 3% WHERE (L) DOES NOT.")
print(f"    (L) {xv['(L)']*100:.2f}% and one rate {xv['one rate']*100:.2f}% BOTH exceed 3%, so the")
print(f"    clock does not break the cross-validation -- but the cross-validation is not at 3% here.")
print(f"    one rate is worse than (L) by {degrade*100:.2f} percentage points, against a bank grain")
print(f"    of {RATIO_GRAIN*100:.3f} pp on this ratio -- a real but small degradation, {degrade/RATIO_GRAIN:.1f}x the grain.")
row("R5'", not (xv['one rate'] > 0.03 and xv['(L)'] <= 0.03),
    "the registered condition is NOT met: both clocks sit at 3.4-3.5%, so the one rate does not "
    "break the frozen/decoupled agreement. REPORTED SEPARATELY FOR 69: the receipt's 3% standard "
    f"was set at its own point and build; at the refit point these banks are at "
    f"{xv['(L)']*100:.2f}% / {xv['one rate']*100:.2f}%, above it under BOTH clocks")

print()
print('=' * 99)
print("R6  THE DISTANCES-POINT PAIR -- READ ONLY ON R2-PRIME")
print('=' * 99)
r2 = dict((t, g) for t, g, _ in OK)["R2'"]
if not r2:
    row('R6', False, 'WITHDRAWN: R2-prime is red, so the distances-point pair is confounded and is not read')
else:
    dmoves, dsame = [], []
    for build in ('frozen', 'decoupled'):
        mx, same, _ = compare(f'arm B {build}, distances (R2-prime licensed)',
                              LP[f'distances__armB_{build}__L'], OC[f'armB_{build}'])
        dmoves.append((build, mx))
        dsame.append(same)
    # R6 registered "the SAME VERDICT as R3 and R4" -- not "below the threshold".  R3's verdict is
    # that the threshold is exceeded; R4's is that the recovery multipole holds.  So R6 is green
    # exactly when the distances point reproduces BOTH of those, red if it diverges from either.
    verdicts = dict((t, g) for t, g, _ in OK)
    same_as_r3 = all((m >= DM_MOVE) == (not verdicts['R3']) for _, m in dmoves)
    same_as_r4 = all(dsame) == verdicts['R4']
    row('R6', same_as_r3 and same_as_r4,
        f'the distances point reproduces BOTH verdicts: the move exceeds the threshold there too '
        f'({max(m for _, m in dmoves)*100:.3f}%, R3 red at the refit point as well) and the recovery '
        f'multipole is unmoved in both builds (R4 green) -- so the blob-confounded pair, once '
        f'R2-prime licenses it, says exactly what the four clock-only pairs say')

print()
print('=' * 99)
print('R8  POST-HOC, NOT PREDICTED: the move is PROJECTION-dominated')
print('=' * 99)
print('    Arm A carries CAMB leaf-rate dynamics in BOTH rows, so its pair moves the PROJECTION')
print('    CLOCK ONLY.  Arm B moves projection AND dynamics.  So arm A measures the projection')
print('    share cleanly; the remainder is NOT a clean dynamics measurement, because arm A and')
print('    arm B are different dynamics codes (CAMB vs HIER).  Stated as a bound, not a split.')
aA = np.abs(np.asarray(AA['refit__armA__L'], float) / np.asarray(AA['refit__armA__one_clock_gate'], float) - 1)
aB = np.abs(np.asarray(LP['refit__armB_frozen__L'], float) / np.asarray(LP['refit__armB_frozen__one_clock'], float) - 1)
print('      l                 ' + ''.join(f'{l:>10d}' for l in ELLS))
print('      projection only  ' + ''.join(f'{v*100:>9.3f}%' for v in aA))
print('      proj + dynamics  ' + ''.join(f'{v*100:>9.3f}%' for v in aB))
share = float(aA[ELLS.index(5)] / aB[ELLS.index(5)])
print(f'    at l=5, the projection clock alone accounts for {share*100:.0f}% of the full move')
row('R8', aA[ELLS.index(5)] > DM_MOVE and share > 0.5,
    f'the projection clock ALONE moves the l=5 depth by {aA[ELLS.index(5)]*100:.3f}% -- already '
    f'{aA[ELLS.index(5)]/DM_MOVE:.1f}x its own distance -- and is {share*100:.0f}% of the full move')

print()
print('=' * 99)
print('R9  THE AMPLIFICATION, PER MULTIPOLE -- and the one thing it does NOT explain')
print('=' * 99)
dO = np.asarray(LP['refit__armB_frozen__one_clock'], float)
dL = np.asarray(LP['refit__armB_frozen__L'], float)
amp = (dL / dO - 1.0) / (-DM_MOVE)
ll = np.asarray(ELLS, float)
slope = np.gradient(np.log(dO), np.log(ll))
print('      l                 ' + ''.join(f'{l:>10d}' for l in ELLS))
print('      amplification    ' + ''.join(f'{v:>10.2f}' for v in amp))
print('      dlog(depth)/dlogl' + ''.join(f'{v:>10.2f}' for v in slope))
hot = [i for i, l in enumerate(ELLS) if l <= 5]
print('    The depth is MORE clock-sensitive than the ruler that projects it at every l <= 5.')
print('    ⛔ NOT EXPLAINED HERE: the SIGN reverses at l=3 (the depth rises where l=2 and l=4 fall)')
print('       while the depth\'s logarithmic slope does NOT change sign there.  So a single')
print('       sampling-slope argument does not account for the pattern, and I am not asserting one.')
row('R9', all(abs(amp[i]) > 1.0 for i in hot),
    'the amplification |d log depth / d log D_M| exceeds 1 at every l <= 5 ('
    + ', '.join(f'l={ELLS[i]}:{abs(amp[i]):.2f}' for i in hot)
    + '); the l=3 sign reversal is reported as UNEXPLAINED')

print()
print('=' * 99)
print('R7  SCOPE')
print('=' * 99)
row('R7', True, 'no new instrument run is claimed here; every row reads banked arrays and the two blobs')

print()
print('=' * 99)
bad = [t for t, g, _ in OK if not g]
print(f'{len(OK) - len(bad)} of {len(OK)} rows hold' + (f'; RED: {bad}' if bad else ''))
print('=' * 99)
json.dump({t: g for t, g, _ in OK}, open(os.path.join(HERE, 'rows.json'), 'w'), indent=1)
raise SystemExit(1 if bad else 0)
