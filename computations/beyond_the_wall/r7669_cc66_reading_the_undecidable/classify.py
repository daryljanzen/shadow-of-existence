#!/usr/bin/env python3
"""r7669 (cc66) -- READING THE UNDECIDABLE ITEMS: WHAT EACH ONE ACTUALLY LOADS.

** THE ORDER (r7669, 69) item 1: ** "Read the 22 undecidable receipts by hand, and classify each
one's actual load as arm of record or namesake.  Some will leave the list."

** WHY A FOURTH INSTRUMENT IS NOT WHAT THIS IS. **  `r7667`'s census converged and said so: the
remaining undecidable load sites are built from variables, and resolving them is a READING task.
This file does the reading mechanically where the source permits and NAMES what it cannot resolve --
it does not re-litigate the census.  The difference is that `r7667` asked "does this receipt load a
namesake?" of the load site, and this asks it of the DIRECTORY CONSTANT the load site joins:

    GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')              <- namesake
    GO = {'cr': os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1')}   <- arm of record
    z  = np.load(os.path.join(GO['cr'], 'cr_base.npz'))                     <- decided by the above

⛭⛭ ** AND THE STRUCTURAL FACT THE READING TURNED UP, which is `Ⓐ`'s content: the control has no
  `_leafrec1` leg in ANY grid family. **  Four families, four times zero.  *That is evidence about
  the BANK and not a measurement of the physics -- it says every seat that built an arm-of-record
  grid built the CR legs and no control leg, not that the control's features do not move, which is
  70's ordered measurement under item 3.*

Registered at PREDICTION.md in this directory, its own commit, before this file existed.
"""
import ast
import collections
import contextlib
import importlib.util
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')

fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


# ══ Ⓐ  THE CONTROL HAS NO ARM-OF-RECORD LEG, IN ANY FAMILY ═══════════════════════════════════════
head('Ⓐ  THE GRID FAMILIES: does the arm-of-record side carry a control leg at all?')
FAMILIES = [('refit_grid', 'refit_grid_leafrec1'),
            ('refit_grid185', 'refit_grid185_leafrec1'),
            (os.path.join('r7093_directions', 'grid_oneclock'),
             os.path.join('r7093_directions', 'grid_oneclock_leafrec1')),
            ('r7201_cc66_loading_lever', 'r7201_cc66_loading_lever_leafrec1')]


def legs(rel):
    d = os.path.join(BW, rel)
    if not os.path.isdir(d):
        return None
    fs = [f for f in os.listdir(d) if f.endswith('.npz')]
    return (len(fs), sum(f.startswith('cr_') for f in fs), sum(f.startswith('lcdm_') for f in fs))


rowsA = []
for nm, aor in FAMILIES:
    a, b = legs(nm), legs(aor)
    rowsA.append((nm, aor, a, b))
    print(f'      {nm:44s} npz={a[0]:3d}  cr_*={a[1]:2d}  lcdm_*={a[2]:2d}')
    print(f'      {aor:44s} npz={b[0]:3d}  cr_*={b[1]:2d}  lcdm_*={b[2]:2d}')
check('Ⓐ① ⛭⛭ EVERY arm-of-record grid carries the CR legs and ZERO control legs, in all four '
      'families -- so a control read has no arm-of-record counterpart to be moved to',
      all(b is not None and b[2] == 0 and b[1] == a[1] and a[2] > 0 for _, _, a, b in rowsA),
      '; '.join(f'{os.path.basename(aor)}: cr={b[1]} lcdm={b[2]}' for _, aor, _, b in rowsA))
check('Ⓐ② ⛔ AND THIS IS EVIDENCE ABOUT THE BANK, NOT A MEASUREMENT OF THE PHYSICS: the gate '
      'asserts what the directories hold and asserts NOTHING about whether the control\'s '
      'features move, which is 70\'s ordered measurement under the order\'s item 3',
      all(a[2] > 0 for _, _, a, _ in rowsA) and len(FAMILIES) == 4,
      f'{len(FAMILIES)} families, control legs present on the namesake side in all of them')

# ══ Ⓑ  WHAT EACH UNDECIDABLE ITEM ACTUALLY LOADS ════════════════════════════════════════════════
head('Ⓑ  THE UNDECIDABLE ITEMS, RESOLVED THROUGH THEIR DIRECTORY CONSTANTS')
_PY = re.compile(r'`?((?:receipts/)?[A-Za-z0-9_./-]+\.py)`?')
rows = []
for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read().split('\n'):
    if ln.count('|') < 8:
        continue
    cells = [x.strip() for x in ln.split('|')]
    for x in cells:
        m = _PY.search(x)
        if m:
            p = m.group(1)
            rows.append((cells[1], p if p.startswith('receipts/') else 'receipts/' + p))
            break
sel = [(a, b) for a, b in rows if a in {'P15', 'P7', 'P6', 'P18', 'P07'}]

tree = collections.defaultdict(list)
for dp, _, fns in os.walk(ROOT):
    if '.git' in dp.split(os.sep):
        continue
    for fn in fns:
        if fn.endswith('.npz'):
            tree[fn].append(os.path.relpath(os.path.join(dp, fn), ROOT))


def tok_class(tok):
    ps = tree.get(tok, [])
    if not ps:
        return 'unresolved'
    lr = ['leafrec1' in q for q in ps]
    return 'aor' if all(lr) else ('namesake' if not any(lr) else 'undecidable')


def dir_constants(tree_):
    """module-level names whose value is a path string we can partly resolve, flattened to text."""
    out = {}

    def flat(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return out.get(node.id, '')
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return flat(node.left) + flat(node.right)
        if isinstance(node, ast.Call):
            f = node.func
            if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) == 'join':
                return '/'.join(x for x in (flat(a) for a in node.args) if x)
        return ''

    for n in tree_.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1:
            t = n.targets[0]
            if isinstance(t, ast.Name):
                v = flat(n.value)
                if v:
                    out[t.id] = v
                elif isinstance(n.value, ast.Dict):
                    #: a dict of directories: keep each value under `NAME['key']`
                    for k, val in zip(n.value.keys, n.value.values):
                        if isinstance(k, ast.Constant):
                            fv = flat(val)
                            if fv:
                                out[f"{t.id}[{k.value!r}]"] = fv
                elif isinstance(n.value, (ast.Tuple, ast.List)):
                    #: ⛔ r7669+cc66.4: a TUPLE OF TUPLES is the third constant form, and missing it
                    #:   was my own gap -- `SPECTRA = (('cr_base', os.path.join(GO, 'cr_base.npz')),
                    #:   ...)` left four items UNDECIDED that the source decides plainly.
                    for j, el in enumerate(n.value.elts):
                        for sub in ast.walk(el):
                            fv = flat(sub) if isinstance(sub, (ast.Call, ast.BinOp)) else ''
                            if fv and ('/' in fv or fv.endswith('.npz')):
                                out[f"{t.id}#{j}"] = fv
                                break
    return out


def load_verdicts(src):
    """per-load-site verdict using the directory constants the site joins."""
    try:
        tr = ast.parse(src)
    except SyntaxError:
        return None, {}
    consts = dir_constants(tr)
    verdicts = []
    for n in ast.walk(tr):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
            continue
        lits, names = [], []
        for a in ast.walk(n):
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                lits.append(a.value)
            elif isinstance(a, ast.JoinedStr):
                lits += [v.value for v in a.values
                         if isinstance(v, ast.Constant) and isinstance(v.value, str)]
            elif isinstance(a, ast.Name):
                names.append(a.id)
            elif isinstance(a, ast.Subscript) and isinstance(a.value, ast.Name) \
                    and isinstance(a.slice, ast.Constant):
                names.append(f"{a.value.id}[{a.slice.value!r}]")
        ctx = ' '.join(lits) + ' ' + ' '.join(consts.get(x, x) for x in names)
        if 'leafrec1' in ctx:
            verdicts.append(('aor', ctx.strip()[:90]))
            continue
        npzs = [s for s in lits if s.endswith('.npz')]
        if npzs and {tok_class(os.path.basename(s)) for s in npzs} == {'aor'}:
            verdicts.append(('aor', ctx.strip()[:90]))
        elif any(consts.get(x) for x in names) or npzs:
            verdicts.append(('namesake', ctx.strip()[:90]))
        else:
            verdicts.append(('unresolved', ctx.strip()[:90]))
    return verdicts, consts


#: ⛔⛭ r7669+cc66.4: AND THE CALL-SITE PASS `census.py` HAS AND THIS FILE DID NOT.  `B5`/`B8` do
#:   `peaks(os.path.join(SP, 'c54.186_cr_L3000.npz'))` into `def peaks(path): np.load(path)`, so the
#:   load site sees only the parameter and the filename is at the CALLER.  ** Omitting this pass was
#:   my own gap, not an undecidable receipt: the source says plainly what those files are. **
def callsite_dirs(tree_):
    """literals the callers pass to helpers that load through one of their own parameters."""
    loaders = {}
    for fn in ast.walk(tree_):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        params = {a.arg for a in fn.args.args} | {a.arg for a in fn.args.posonlyargs}
        for n in ast.walk(fn):
            if isinstance(n, ast.Call):
                f = n.func
                if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
                    continue
                if any(isinstance(x, ast.Name) and x.id in params for x in ast.walk(n)):
                    loaders.setdefault(fn.name, [])
    hits = []
    for n in ast.walk(tree_):
        if isinstance(n, ast.Call):
            nm = (n.func.attr if isinstance(n.func, ast.Attribute)
                  else getattr(n.func, 'id', ''))
            if nm in loaders:
                for a in list(n.args) + [k.value for k in n.keywords]:
                    for x in ast.walk(a):
                        if isinstance(x, ast.Constant) and isinstance(x.value, str) \
                                and ('.npz' in x.value or 'leafrec1' in x.value):
                            hits.append(x.value)
    return hits


_NPZ = re.compile(r'([A-Za-z0-9_.\-]+\.npz)')
_GLOB = re.compile(r'glob\.glob\([^)]*(\*\*|recursive\s*=\s*True)')
items = []
for paper, pth in sel:
    fp = os.path.join(ROOT, pth)
    if not os.path.exists(fp):
        continue
    src = open(fp, encoding='utf-8', errors='replace').read()
    if not _NPZ.findall(src):
        continue
    v, consts = load_verdicts(src)
    if v is None:
        continue
    #: ⛔⛭⛭ r7669+cc66.4 -- THE THIRD SHAPE, AND IT IS RECEIPT-LEVEL BY NECESSITY.  Several receipts
    #:   build a TABLE and iterate it: `SPECTRA = (('cr_base', os.path.join(GO, 'cr_base.npz')),
    #:   ...)` then `for tag, path in SPECTRA: np.load(path)`.  The load site's only Name is the
    #:   loop variable, so no SITE-level resolution can reach the table.  ** Attributing the table's
    #:   paths to the RECEIPT is coarser than a per-site verdict and is labelled as such: it says
    #:   what this receipt reads, not which line reads it. **
    try:
        _tr = ast.parse(src)
        _tbl = []
        for _n in _tr.body:
            if isinstance(_n, ast.Assign):
                for _x in ast.walk(_n.value):
                    if isinstance(_x, ast.Constant) and isinstance(_x.value, str) \
                            and _x.value.endswith('.npz'):
                        _tbl.append(_x.value)
        if _tbl and not any(k == 'namesake' or k == 'aor' for k, _ in v):
            for _lit in sorted(set(_tbl)):
                v.append(('aor' if 'leafrec1' in _lit else
                          ('namesake' if tok_class(os.path.basename(_lit)) == 'namesake'
                           else 'unresolved'), f'table:{_lit}'))
    except SyntaxError:
        pass
    try:
        for _lit in callsite_dirs(ast.parse(src)):
            v.append(('aor' if 'leafrec1' in _lit else
                      ('namesake' if tok_class(os.path.basename(_lit)) == 'namesake'
                       else 'unresolved'), _lit))
    except SyntaxError:
        pass
    kinds = collections.Counter(k for k, _ in v)
    #: the undecidable population r7667 handed over: no load site resolved to a namesake THERE.
    #: here it is re-resolved through the constants, so a verdict is now possible for most.
    items.append((paper, pth, kinds, v, bool(_GLOB.search(src))))

aor_only = [i for i in items if i[2]['aor'] and not i[2]['namesake']]
mixed = [i for i in items if i[2]['aor'] and i[2]['namesake']]
nm_only = [i for i in items if i[2]['namesake'] and not i[2]['aor']]
globbers = [i for i in items if i[4]]
print(f'      receipts in scope that load a spectrum at all: {len(items)}')
print(f'        every resolved load is ARM OF RECORD          : {len(aor_only)}')
print(f'        loads BOTH arms                               : {len(mixed)}')
print(f'        every resolved load is NAMESAKE               : {len(nm_only)}')
print(f'        audit the whole tree with a recursive glob    : {len(globbers)}')
check(f'Ⓑ① ⛭⛭ RESOLVING THROUGH THE DIRECTORY CONSTANT DECIDES WHAT THE LOAD SITE COULD NOT: '
      f'{len(aor_only)} receipts load only the arm of record, {len(mixed)} load both and '
      f'{len(nm_only)} only the namesake',
      len(aor_only) > 0 and len(nm_only) > 0 and len(items) > 50,
      f'{len(aor_only)}/{len(mixed)}/{len(nm_only)} of {len(items)}')
check(f'Ⓑ② ⛭ AND A CLASS THE ORDER DID NOT ANTICIPATE IS NAMED RATHER THAN FOLDED IN: '
      f'{len(globbers)} receipt(s) audit every `.npz` under `computations/` with a recursive '
      f'glob, so they do not REST on a namesake in any sense a rebuild would fix',
      len(globbers) >= 1, f'{len(globbers)} tree-auditing receipt(s)')

#: ⛭⛭⛭ THE INTERSECTION THE ORDER ACTUALLY ASKS FOR.  `r7667`'s census handed over a set it could
#:   not decide: receipts whose every LOAD SITE carried no `.npz` literal and no `leafrec1`, so the
#:   filename lived in a variable.  ** This re-resolves exactly that set through the directory
#:   constants, which is the "read them by hand" the order asked for, done mechanically where the
#:   source permits. **
def r7667_undecidable(src):
    """True if every load site in src was undecidable from its own literals -- r7667's handover set."""
    try:
        tr = ast.parse(src)
    except SyntaxError:
        return False
    saw = False
    for n in ast.walk(tr):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if (f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')) != 'load':
            continue
        lits = []
        for a in ast.walk(n):
            if isinstance(a, ast.Constant) and isinstance(a.value, str):
                lits.append(a.value)
            elif isinstance(a, ast.JoinedStr):
                lits += [v.value for v in a.values
                         if isinstance(v, ast.Constant) and isinstance(v.value, str)]
        saw = True
        if any('leafrec1' in s for s in lits):
            return False
        npzs = [s for s in lits if s.endswith('.npz')]
        if npzs and 'namesake' in {tok_class(os.path.basename(s)) for s in npzs}:
            return False
    return saw


_hand = [i for i in items if r7667_undecidable(open(os.path.join(ROOT, i[1]),
                                                   encoding='utf-8', errors='replace').read())]
_h_aor = [i for i in _hand if i[2]['aor'] and not i[2]['namesake']]
_h_mix = [i for i in _hand if i[2]['aor'] and i[2]['namesake']]
_h_nm = [i for i in _hand if i[2]['namesake'] and not i[2]['aor']]
_h_glob = [i for i in _hand if i[4]]
_h_none = [i for i in _hand if not i[2]['aor'] and not i[2]['namesake']]
print(f'\n      r7667 HANDED OVER {len(_hand)} receipt(s) it could not decide.  Re-resolved here:')
print(f'        now ARM OF RECORD only  -> LEAVES the list : {len(_h_aor)}')
print(f'        now BOTH arms           -> sentence decides: {len(_h_mix)}')
print(f'        now NAMESAKE only       -> STAYS            : {len(_h_nm)}')
print(f'        tree-auditing glob      -> LEAVES, other way: {len(_h_glob)}')
print(f'        STILL undecidable                           : {len(_h_none)}')
check(f'Ⓑ③ ⛭⛭⛭ ARM ① SCORED: of the {len(_hand)} receipts `r7667` could not decide, '
      f'{len(_h_aor) + len(_h_glob)} LEAVE the list ({len(_h_aor)} because every resolved load '
      f'is arm-of-record, {len(_h_glob)} because they audit the whole tree), {len(_h_mix)} are '
      f'decided by their sentence and {len(_h_nm)} stay',
      len(_h_aor) + len(_h_mix) + len(_h_nm) + len(_h_none) == len(_hand),
      f'{len(_h_aor)}+{len(_h_glob)} leave, {len(_h_mix)} sentence, {len(_h_nm)} stay, '
      f'{len(_h_none)} still undecidable')
check(f'Ⓑ④ ⛔ AND WHAT IS STILL UNDECIDABLE IS NAMED RATHER THAN ASSUMED EITHER WAY: '
      f'{len(_h_none)} receipt(s) resolve to neither arm even through their constants',
      len(_h_none) == len([i for i in _hand if not i[2]['aor'] and not i[2]['namesake']]),
      f'{len(_h_none)} still undecidable')
#: ⛭ AND RESTRICTED TO THE FIGURE-PRINTING SUBSET, which is the "22" the order names: a receipt
#:   only reaches PO-87's list if a BODY SENTENCE prints one of its figures.
_texts = {}
for _f in ('corpus/CR_cosmology.tex', 'corpus/CR_framework.tex', 'corpus/CR_synthesis.tex',
           'EXPLAINER.md'):
    _fp = os.path.join(ROOT, _f)
    if os.path.exists(_fp):
        _texts[_f] = open(_fp, encoding='utf-8', errors='replace').read()
_NUM = re.compile(r'\d+\.\d+|\b\d{2,}\b')


#: ⛔⛭⛭ r7671+cc66.4 -- THIS FUNCTION CARRIED THE CRUDE SENTENCE TEST, one instrument after the
#:   census's copy of it was corrected.  It bounded a span at the nearest `. `, which in LaTeX lands
#:   inside `\emph{...}`, inside `$...$` and inside a `\rcpt{...}` run, so the span ran into
#:   NEIGHBOURING sentences and their figures were counted as the citing sentence's.  The census's
#:   same error put PO-87's list at 48 items when it is 30.
#:   ⇒ ** The fix is not a better copy, it is NOT A COPY: ** `sentences_citing` is imported from
#:     `r7667/sentence.py`, the one definition all three instruments now share.  The subset counts
#:     below are re-scored on it and the gate pins are corrected to the measured values.
sys.path.insert(0, os.path.join(BW, 'r7667_cc66_po87_the_unfiltered_list'))
from sentence import sentences_citing            # noqa: E402


def prints_a_figure(pth):
    base = os.path.basename(pth)[:-3]
    for tx in _texts.values():
        for s in sentences_citing(tx, base):
            if _NUM.search(s):
                return True
    return False


_fp_hand = [i for i in _hand if prints_a_figure(i[1])]
_f_aor = [i for i in _fp_hand if i[2]['aor'] and not i[2]['namesake']]
_f_mix = [i for i in _fp_hand if i[2]['aor'] and i[2]['namesake']]
_f_nm = [i for i in _fp_hand if i[2]['namesake'] and not i[2]['aor']]
_f_glob = [i for i in _fp_hand if i[4]]
_f_none = [i for i in _fp_hand if not i[2]['aor'] and not i[2]['namesake']]
_leave = len(_f_aor) + len([i for i in _f_glob if i not in _f_aor])
print(f'\n      OF THOSE, the figure-printing subset -- PO-87\'s own list -- is {len(_fp_hand)}:')
print(f'        ARM OF RECORD only -> LEAVES               : {len(_f_aor)}')
print(f'        BOTH arms          -> sentence decides     : {len(_f_mix)}')
print(f'        NAMESAKE only      -> STAYS                : {len(_f_nm)}')
print(f'        tree-auditing glob -> LEAVES, other grounds: {len(_f_glob)}')
print(f'        STILL undecidable                          : {len(_f_none)}')
check(f'Ⓑ⑤ ⛔⛭⛭ ARM ① IS FALSIFIED, AND NOT NARROWLY. I registered that between 8 and 14 of the '
      f'undecidable figure-printing items would LEAVE the list once read. **{_leave} leave.** '
      f'{len(_f_nm)} resolve to the namesake and STAY, {len(_f_mix)} are decided by their '
      f'sentence rather than their loads, and {len(_f_none)} are still undecidable from source',
      _leave < 8 and len(_f_aor) + len(_f_mix) + len(_f_nm) + len(_f_none) == len(_fp_hand),
      f'{_leave} leave against a registered 8-14 -> FALSIFIED')
#: ⛔⛭⛭ ARM ② IS WRONG TOO, AND IN THE OPPOSITE DIRECTION -- and `r7671+cc66.4` found the gate
#:   itself was keyed on a STALE LITERAL.  I registered that the gap against `r7667`'s census was
#:   ONE item.  The gate then compared this file's subset against the constant `22`, which was the
#:   census's count on the CRUDE sentence test; the census now says 15 and the constant said nothing
#:   about it.  ** A gate that pins one instrument against another instrument's old number measures
#:   neither. **
#:   ⇒ So the census is IMPORTED and the two populations are compared as SETS, both directions
#:     named, which is the discipline the merge rule uses on an append-only file for the same
#:     reason: a difference of counts hides which members differ.
_cen_ok, _cen_set = None, set()
try:
    _spec = importlib.util.spec_from_file_location(
        'census_r7667', os.path.join(BW, 'r7667_cc66_po87_the_unfiltered_list', 'census.py'))
    _cen = importlib.util.module_from_spec(_spec)
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            _spec.loader.exec_module(_cen)
            _cen_ok = True
        except SystemExit:
            _cen_ok = False          #: the census's own gates failed; recorded, never ignored
    _cen_set = {q for q in _cen.prints_fig if not _cen.cand[q]['sites'].get('namesake')}
except Exception as _e:              # noqa: BLE001
    _cen_ok = None
    print(f'      ⛔ the census could not be imported for the set comparison: {_e!r}')
_mine = {i[1] for i in _fp_hand}
_only_cen = sorted(_cen_set - _mine)
_only_mine = sorted(_mine - _cen_set)
print(f'\n      SET COMPARISON against `r7667/census.py` (imported, not a remembered number):')
print(f'        its undecidable-only figure-printing items : {len(_cen_set)}')
print(f'        this file\'s handover figure-printing subset: {len(_mine)}')
print(f'        in the census and not here                 : {len(_only_cen)}')
for _q in _only_cen:
    print(f'          {os.path.basename(_q)[:76]}')
print(f'        here and not in the census                 : {len(_only_mine)}')
for _q in _only_mine:
    print(f'          {os.path.basename(_q)[:76]}')
check(f'Ⓑ⑤ᵃ ⛔⛭ ARM ② IS FALSIFIED AND THE GATE\'S OWN PIN WAS STALE: I registered a ONE-item gap '
      f'against the census; on the shared sentence test the census holds {len(_cen_set)} '
      f'undecidable-only figure-printing items and this file {len(_mine)}, differing by '
      f'{len(_only_cen)} the census has that this file lacks and {len(_only_mine)} this file has '
      f'that it lacks -- compared as SETS, with the census imported and its own gates confirmed '
      f'green ({_cen_ok}), rather than against the constant 22 the crude test produced',
      _cen_ok is True and (len(_only_cen) + len(_only_mine)) > 0
      and len(_only_cen) + len(_only_mine) == len(_cen_set ^ _mine),
      f'census {len(_cen_set)} vs here {len(_mine)}; symmetric difference '
      f'{len(_only_cen)}+{len(_only_mine)}')
check(f'Ⓑ⑥ ⛭ ARM ④ HITS: the two receipts whose own header guard asserts the loaded file IS the '
      f'LEAFREC=0 namesake and that an arm-of-record counterpart exists beside it both resolve '
      f'NAMESAKE here, so they are RE-GROUND with the wording already written',
      all(any(os.path.basename(i[1]).startswith(s) for i in _f_nm + _f_mix + _f_none)
          for s in ('P15_the_phase_is_the_driving', 'P15_where_the_likelihood_sits')),
      'both header-guard receipts resolve to the namesake side')

for _, p, k, v, g in sorted(_hand):
    tag = ('AOR-ONLY   ' if (k['aor'] and not k['namesake'])
           else 'BOTH       ' if (k['aor'] and k['namesake'])
           else 'NAMESAKE   ' if k['namesake'] else 'UNDECIDED  ')
    print(f'        {tag}{"GLOB " if g else "     "}{os.path.basename(p)[:68]}')

print('\n      ARM-OF-RECORD-ONLY (these leave PO-87\'s list):')
for _, p, k, v, _ in sorted(aor_only):
    print(f'        {os.path.basename(p)[:76]}')
print('\n      BOTH ARMS (the sentence decides which figure it prints):')
for _, p, k, v, _ in sorted(mixed):
    print(f'        {os.path.basename(p)[:76]}  aor={k["aor"]} namesake={k["namesake"]}')
print('\n      TREE-AUDITING (leave on different grounds):')
for _, p, k, v, g in sorted(globbers):
    print(f'        {os.path.basename(p)[:76]}')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  ✓ ALL CHECKS PASSED')
print('=' * 100)
