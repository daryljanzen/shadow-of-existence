#!/usr/bin/env python3
"""sweep_vacuous_pins.py -- ** PO-60 ⓶ᵃ: THE VACUOUS GREEN, SWEPT ACROSS EVERY RECEIPT. **

Built r6931+70.3 by node 70.  NOT wired into CI: the order asks for a detector seeded BOTH WAYS
before any wiring, and `--seed` below is that seeding.

** THE CLASS. **  A check pinned to a BARE NUMBER -- `'8.2' in p15`, `p15.count('1.082')` --
that matches the document somewhere OTHER than the sentence the check is about.  Five were found
inside PO-59's 83 by accident (C16 '1.082', and the '8.2' conjunct in C24, C25, C28 and L557 ⓹).
*A literal short enough to recur is not a pin, it is a coincidence with a passing exit code*, and
the class grows as the corpus does.

** WHAT THIS MEASURES, AND IT IS STRUCTURAL, NOT A GUESS AT INTENT. **  For every presence test
whose needle is a bare number (TeX punctuation removed: `$`, `\\%`, braces) and whose haystack is
a LIVE document -- a corpus paper or a root register -- every site the needle matches is located,
digit-bounded so '8.2' does not match '18.2', and the check's OWN context is looked for beside it:
any other string literal of the same check condition (>= 12 characters, or a number of >= 4
significant digits) and any quotation in its label, within 400 characters of the site.

    ANCHORED     some site sits beside the check's own context -- the pin reads its sentence
    DISTINCTIVE  one site, and the number has >= 4 significant digits -- a coincidence is not
                 credible (302.2, 301.76), so it is not flagged
    FLAGGED      it matches, and no site sits beside the check's context:
                   VACUOUS  -- there is context and none of it is near any site
                   UNIQUE   -- one site, a short number, and the check carries no context to test
    ABSENT       the needle is not in the document (the receipt is red, or the branch is unused)

  and, COUNTED BUT NOT JUDGED:
    HISTORICAL   the haystack is the document at a FIXED commit (`git show`, `_at(...)`, `_then`)
                 -- that text cannot move, so a pin into it cannot drift
    SOURCE       the haystack is another receipt's source.  ⚠ ** Judged by hand at r6931+70.3 and
                 EXCLUDED from the automatic verdict: 6 flagged, 1 true (C28 ⓶, repaired), 5
                 false -- a receipt's source repeats its own figure in docstring, table and assert,
                 so co-location against the checking receipt's context is the wrong test there. **
    OUTPUT       stdout, a register row selected in code, literal data -- not a document

** THE MEASUREMENT (r6931+70.3), precision first because the order asks for that one. **
  * HEAD before repair: 5 flagged literals in 4 checks (C22 ⓷, C27 ⓷, C36 ⓵, C41 ⓶), ALL TRUE on
    reading each site -- all four were held up by the control arm's "8.2%" or by the
    counterfactual "a ratio of $1.082$".  After repair: 0.
  * ALL 20 judged live-document pins at head were read by hand, ANCHORED and DISTINCTIVE included:
    15 read their own sentence and are not flagged, 5 are the flagged ones.  ** 0 false positives
    and 0 misses on that population. **
  * RECALL on the known class, by running this on the tree PO-59 started from (`31f3276`): all five
    known instances are flagged, plus the four above, which were already vacuous there.
  ⚠ ** WHAT IT CANNOT SEE: ** a needle built at run time (an f-string or a variable), a regex pin,
    a haystack whose file is not named in the assignment it comes from, and a distinctive number
    that sits alone in the WRONG sentence.  Those are recall limits, stated rather than estimated.

Usage:
    python3 scripts/sweep_vacuous_pins.py            # sweep, summary, flagged listed, exit 1 if any
    python3 scripts/sweep_vacuous_pins.py --json     # every pin with its verdict
    python3 scripts/sweep_vacuous_pins.py --seed     # the both-ways seeding; exit 0 iff it discriminates
    python3 scripts/sweep_vacuous_pins.py --root DIR # sweep another checkout (e.g. a worktree)
"""
import argparse
import ast
import collections
import glob
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WIN = 400
FLAGGED = ('VACUOUS', 'UNIQUE')

_NUM = re.compile(r'^[-+−]?\d[\d.,]*$')
_FILE = r"['\"]([A-Za-z0-9_.]+\.(?:tex|md|py|txt))['\"]"
_HIST = re.compile(r"'show'|git\(|_at\(|_then|_before|BEFORE|\bPRE\b")


def _core(s):
    c = s.replace('\\\\', '\\').replace('\\%', '').replace('%', '').replace('$', '')
    for t in ('\\,', '{', '}', '~', '\\times', '\\pm'):
        c = c.replace(t, '')
    return c.strip()


def bare_number(s):
    c = _core(s)
    return bool(_NUM.match(c)) and len(c) <= 8


def sigdigits(s):
    return len(re.sub(r'[^0-9]', '', s).lstrip('0'))


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\\\\', '\\'))


class Sweep:
    def __init__(self, root):
        self.root = root
        self._docs = {}

    def locate(self, name):
        for cand in (os.path.join(self.root, 'corpus', name), os.path.join(self.root, name)):
            if os.path.exists(cand):
                return cand
        g = glob.glob(os.path.join(self.root, '**', name), recursive=True)
        return g[0] if g else None

    def doc(self, name):
        if name not in self._docs:
            p = self.locate(name)
            t = None
            if p is not None:
                t = open(p, encoding='utf-8', errors='replace').read()
                if name.endswith('.tex'):
                    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
                t = re.sub(r'\s+', ' ', t)
            self._docs[name] = t
        return self._docs[name]

    @staticmethod
    def files_for(name, module_src, hsrc):
        hits = set(re.findall(_FILE, hsrc))
        for m in re.finditer(r'(?m)^\s*' + re.escape(name) + r'\s*=\s*(.+)$', module_src):
            rhs = m.group(1)
            hits |= set(re.findall(_FILE, rhs))
            for v in re.findall(r'\b([A-Z_][A-Z0-9_]*)\b', rhs):
                for m2 in re.finditer(r'(?m)^\s*' + re.escape(v) + r'\s*=\s*(.+)$', module_src):
                    hits |= set(re.findall(_FILE, m2.group(1)))
        return sorted(hits)

    def scan(self, path):
        text = open(path, encoding='utf-8', errors='replace').read()
        try:
            tree = ast.parse(text)
        except SyntaxError:
            return []
        parent = {}
        for n in ast.walk(tree):
            if isinstance(n, ast.Call) and len(n.args) >= 2:
                for sub in ast.walk(n.args[1]):
                    parent.setdefault(id(sub), n)
        out = []
        for n in ast.walk(tree):
            needle = hay = None
            if isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], ast.In) \
                    and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str):
                needle, hay = n.left.value, n.comparators[0]
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr == 'count' and n.args and isinstance(n.args[0], ast.Constant) \
                    and isinstance(n.args[0].value, str):
                needle, hay = n.args[0].value, n.func.value
            if needle is None or not bare_number(needle):
                continue
            chk = parent.get(id(n))
            cond = chk.args[1] if chk is not None else n
            label = chk.args[0] if chk is not None else None
            hsrc = ast.get_source_segment(text, hay) or ''
            name = re.split(r'[\[(]', hsrc)[0].strip()
            rec = dict(file=os.path.relpath(path, self.root), line=n.lineno, needle=needle,
                       hay=hsrc[:60])
            rhs = ' '.join(re.findall(r'(?m)^\s*' + re.escape(name) + r'\s*=\s*(.+)$', text)) + hsrc
            files = self.files_for(name, text, hsrc) if re.fullmatch(r'[A-Za-z_]\w*', name) \
                else sorted(set(re.findall(r'([A-Za-z0-9_.]+\.(?:tex|md|py|txt))', hsrc)))
            rec['docs'] = files
            if _HIST.search(rhs + ' ' + name):
                rec['verdict'] = 'HISTORICAL'
            elif not files:
                rec['verdict'] = 'OUTPUT'
            elif all(f.endswith('.py') for f in files):
                rec['verdict'] = 'SOURCE'
            else:
                rec.update(self.judge(needle, [f for f in files if not f.endswith('.py')],
                                      cond, label, text))
            out.append(rec)
        return out

    def judge(self, needle, files, cond, label, text):
        ctx = []
        for n in ast.walk(cond):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value != needle:
                if len(n.value) >= 12 and not bare_number(n.value):
                    ctx.append(n.value)
                elif bare_number(n.value) and sigdigits(n.value) >= 4:
                    ctx.append(n.value)
        if label is not None:
            ctx += re.findall(r'"([^"]{12,})"', ast.get_source_segment(text, label) or '')
        ctx = [norm(c) for c in ctx]
        nd, sites, anchored = norm(needle), 0, False
        for f in files:
            d = self.doc(f)
            if d is None:
                continue
            for m in re.finditer(re.escape(nd), d):
                a, b = m.start(), m.end()
                if (a > 0 and d[a - 1].isdigit()) or (b < len(d) and d[b].isdigit()):
                    continue
                sites += 1
                w = d[max(0, a - WIN): b + WIN]
                if any(c[:40] in w for c in ctx):
                    anchored = True
        if sites == 0:
            v = 'ABSENT'
        elif anchored:
            v = 'ANCHORED'
        elif sites == 1 and sigdigits(needle) >= 4:
            v = 'DISTINCTIVE'
        elif not ctx and sites == 1:
            v = 'UNIQUE'
        else:
            v = 'VACUOUS'
        return dict(verdict=v, sites=sites, nctx=len(ctx))

    def run(self):
        res = []
        for f in sorted(glob.glob(os.path.join(self.root, 'receipts', '**', '*.py'), recursive=True)):
            res.extend(self.scan(f))
        return res


# ------------------------------------------------------------------------------------ seeding
_SEED_TEX = r"""
\section{Seed}
The observable is then $\theta_{D}/\theta_{*}$ larger by $0.9\%$ at the common endpoint.
The polarisation source pulls both arms: the control by $8.2\%$ and this arm by $10.9\%$.
And $\ell_{*}=302.2$ against the measured $301.76$ on the adjudicated background.
"""
_SEED_RECEIPT = r'''
import os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
p15 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'seed_paper.tex')).read())
def check(label, cond): pass
# PLANTED: the corrected sentence is gone; '8.2' survives only as the control's pull
check('the corrected sentence: "larger by 8.2%"', '8.2' in p15)
# PLANTED, count form, same defect
check('the figure is carried', p15.count('8.2') >= 1)
# LEGITIMATE: a short number anchored by its own sentence
check('the endpoint: "larger by 0.9%"', 'at the common endpoint' in p15 and '0.9' in p15)
# LEGITIMATE: a distinctive number at one site
check('the angle', '301.76' in p15)
# LEGITIMATE: a pin into a fixed commit cannot drift
p15_then = p15
check('then', '8.2' in p15_then)
'''


def seed():
    """Both ways: the two planted pins must be FLAGGED and the three legitimate ones must not."""
    tmp = tempfile.mkdtemp(prefix='po60a_seed_')
    try:
        os.makedirs(os.path.join(tmp, 'corpus'))
        os.makedirs(os.path.join(tmp, 'receipts', 'SEED'))
        open(os.path.join(tmp, 'corpus', 'seed_paper.tex'), 'w').write(_SEED_TEX)
        open(os.path.join(tmp, 'receipts', 'SEED', 'S1_seed.py'), 'w').write(_SEED_RECEIPT)
        got = {(r['line'], r['needle']): r['verdict'] for r in Sweep(tmp).run()}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    want_flag = [k for k in got if k[1] == '8.2' and got[k] != 'HISTORICAL']
    ok_planted = len(want_flag) == 2 and all(got[k] in FLAGGED for k in want_flag)
    ok_legit = (got.get(next((k for k in got if k[1] == '0.9'), None)) == 'ANCHORED'
                and got.get(next((k for k in got if k[1] == '301.76'), None)) == 'DISTINCTIVE'
                and sum(1 for k, v in got.items() if v == 'HISTORICAL') == 1)
    for k in sorted(got):
        print(f'    line {k[0]:>2}  {k[1]!r:9}  {got[k]}')
    print(f'  planted pins flagged       : {ok_planted}')
    print(f'  legitimate pins let through: {ok_legit}')
    return 0 if ok_planted and ok_legit else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(HERE))
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        print('\n  sweep_vacuous_pins --seed: does it catch a planted instance AND let a legitimate one through?\n')
        return seed()
    res = Sweep(a.root).run()
    if a.json:
        json.dump(res, sys.stdout, indent=1)
        return 0
    c = collections.Counter(r['verdict'] for r in res)
    print(f'\n  VACUOUS-PIN SWEEP -- {len(res)} bare-numeric presence pins in '
          f'{len({r["file"] for r in res})} receipt(s)')
    for k in ('ANCHORED', 'DISTINCTIVE', 'VACUOUS', 'UNIQUE', 'ABSENT', 'HISTORICAL', 'SOURCE',
              'OUTPUT'):
        print(f'    {k:12} {c.get(k, 0)}')
    bad = [r for r in res if r.get('verdict') in FLAGGED]
    for r in bad:
        print(f'  ⛔ {r["verdict"]:8} {r["file"]}:{r["line"]}  {r["needle"]!r} in {r["hay"]}  '
              f'({r["sites"]} site(s), none beside the check\'s own context)')
    print()
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
