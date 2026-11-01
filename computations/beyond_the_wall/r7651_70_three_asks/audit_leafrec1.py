"""r7651+70 ②: `r7101_70_three_grid_audit/audit.py` run UNCHANGED except that its GRIDS resolve PER ARM -- the
control from the namesake grid, the arm from the `_leafrec1` sibling (which carries `cr_*` legs only).  The
resolver is a per-run directory of links built here, so the imported `rigidity.py` and its `--grid` subprocess
driver see exactly the same resolution.  The audit's own RECEIPT literals are the namesake's: on the arm of
record its `cr` rows print `** DIFFERS **` by construction (old -> new is reported, not a failure).
Usage:  python3 audit_leafrec1.py      (prints; audit_leafrec1_log.txt beside it is this output)"""
import ast
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
AUDIT = os.path.join(BW, 'r7101_70_three_grid_audit', 'audit.py')
PAIRS = (('banked', 'refit_grid185', 'refit_grid185_leafrec1'),
         ('licensed', 'r7095_directions/grid_licensed', 'r7095_directions/grid_licensed_leafrec1'),
         ('forbidden', 'r7093_directions/grid_oneclock', 'r7093_directions/grid_oneclock_leafrec1'))
TMP = tempfile.mkdtemp(prefix='r7651_grids_')
RESOLVED = []
print('the per-arm resolution (control <- namesake, arm <- sibling):')
for nm, ctl, arm in PAIRS:
    d = os.path.join(TMP, nm)
    os.makedirs(d)
    for src, pre in ((ctl, 'lcdm_'), (arm, 'cr_')):
        for f in sorted(os.listdir(os.path.join(BW, src))):
            if f.startswith(pre):
                os.symlink(os.path.join(BW, src, f), os.path.join(d, f))
    print(f'  {nm:9s} lcdm_* <- {ctl}/   cr_* <- {arm}/   ({len(os.listdir(d))} files)')
    RESOLVED.append((nm, d))
tree = ast.parse(open(AUDIT).read())
for n in tree.body:
    if isinstance(n, ast.Assign) and any(getattr(t, 'id', '') == 'GRIDS' for t in n.targets):
        n.value = ast.Name(id='RESOLVED', ctx=ast.Load())
ns = {'__file__': AUDIT, '__name__': '__main__', 'RESOLVED': tuple(RESOLVED)}
sys.path.insert(0, os.path.dirname(AUDIT))
exec(compile(ast.fix_missing_locations(tree), AUDIT, 'exec'), ns)
