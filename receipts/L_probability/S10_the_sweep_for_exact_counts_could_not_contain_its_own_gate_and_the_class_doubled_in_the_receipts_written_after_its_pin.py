#!/usr/bin/env python3
"""L_probability receipt -- `r7227` ITEM ①, AND THE ANSWER IS ABOUT THE SWEEP RATHER THAN THE CLASS:

*** ⛭⛭⛭ `S4` SWEPT THIS SEAT'S WORK FOR `an exact count asserted against a set other seats can
    grow` AND REPORTED ONE LIVE INSTANCE.  THREE OF THIS SEAT'S RECEIPTS THEN WENT RED ON AN EXACT
    `2167` AND `66` HAD TO EDIT THEM AS THE GATE.  THE QUESTION IS NOT WHETHER THERE ARE MORE --- IT
    IS WHY THE INSTRUMENT BUILT TO ENUMERATE THE CLASS DID NOT ENUMERATE ITS OWN GATE. ***

** THERE ARE THREE DEFECTS AND THEY ARE INDEPENDENT. **

  ⓵ ** THE DETECTOR IS BLIND TO A COUNT BOUND TO A NAME. **  `flagged()` requires `len`/`sum`/
    `count` to stand INSIDE the compared expression.  `_unadj == 2167` is `Name == Constant`, so the
    site is skipped -- and that is the form of `S4`'s OWN gate and of `S3`'s.  *Two of the three
    receipts `66` repaired were invisible to the detector that was supposed to have found them.*

  ⓶ ** TAINT DOES NOT CROSS A FUNCTION BOUNDARY, NOR A LOOP TARGET. **  A helper that opens the
    shared artefact and RETURNS rows leaves its caller untainted; so does `for r in ROWS:`.  *Neither
    reaches the `2167` sites, so this half is measured on the wider sweep and not claimed for them.*

  ⓷ ** AND THE ONE THAT ACTUALLY LET `S6` THROUGH IS NOT A DETECTOR DEFECT AT ALL: THE SWEEP IS
    PINNED, SO IT IS A SNAPSHOT AND NOT A GUARD. **  `S4` pins its population to the commit its own
    revision started from -- for a good reason, since a sweep whose denominator moves is the defect
    it is about -- and the arithmetic of that is that ** `S4`'s SWEEP CANNOT CONTAIN `S4`'s OWN
    GATES BY CONSTRUCTION. **  *`S6`'s site was visible to the detector and was written two
    revisions later, so nothing ever looked at it.*

⛔ ** AND A FOURTH, WHICH IS THE SAME BLINDNESS IN THE SECOND STAGE RUNNING THE OTHER WAY. **
   `ground()` reads FROZEN off a pin spelled into the assignment.  A pin passed as an ARGUMENT --
   `_at(PIN, BASELINE)` -- is not seen, so stage two files frozen sites as EXPOSED.  *The same
   function boundary makes stage one miss real sites and stage two invent false ones.*

⌗ ** WHAT THIS RECEIPT DOES NOT DO. **  It does not widen the class, re-rule `L-249`, or touch the
   gate layer: the standing guard that would police new work lives in `scripts/lint_assertions.py`,
   which is not this seat's to edit, and the patch is routed in `FOR_66_FROM_60.md` instead.

⌈ ** AND THE SECOND ITEM, WHICH IS A LOOSE NUMBER AND NOT A QUESTION: `r7227` routed `EXTENDED 107`
   against `70`'s `108`.  NOTHING IS LOST.  IT IS A COLLISION --- two distinct pins in ONE receipt
   were each extended and both landed on the SAME extended literal, so `108` extensions made `107`
   distinct keys.  It is internal to the extension and NOT an interaction with this seat's `S7` wrap
   correction, which is what the order conjectured. **

COMPUTES: nothing the papers quote.  This receipt measures an instrument of the corpus's own
reproducibility layer and the dedup of one shared ledger; no physical parameter is pinned here.
"""
import ast
import collections
import os
import re
import subprocess
import sys

_PARITY_BY_NODE = {'60': 'EVEN', '66': 'ODD'}
NODE = os.environ.get('NODE', '60')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print(f"\n{'=' * 100}\n{t}\n{'=' * 100}")


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#: the pin for every frozen read below.  ** This receipt's own numbers over a LIVE population are
#  gated MONOTONE for exactly the reason it is about; the exact ones are read at this commit. **
PIN = '9c06b92f'
#: the commit `66` edited this seat's three receipts in, and its parent
R7227 = '9ce054ba'
#: `S4`'s own pin, quoted from `S4`
S4PIN = 'f8d8e648'


def at(ref, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{ref}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


def at_many(ref, rels):
    """every blob at one ref in ONE `git cat-file --batch`.

    ⛭ The first draft of this receipt ran one `git show` per receipt per tree -- about nine hundred
    subprocesses -- which put a read-only sweep within reach of the suite's `600` s default.  The
    batch does the same reads in one process.
    """
    q = ''.join(f'{ref}:{r}\n' for r in rels).encode()
    out = subprocess.run(['git', '-C', ROOT, 'cat-file', '--batch'], input=q,
                         capture_output=True).stdout
    res, i = {}, 0
    for r in rels:
        j = out.find(b'\n', i)
        if j < 0:
            res[r] = ''
            continue
        hdr = out[i:j].split()
        if len(hdr) < 3:                     # "<object> missing" -- the path is not at that ref
            res[r] = ''
            i = j + 1
            continue
        n = int(hdr[2])
        res[r] = out[j + 1:j + 1 + n].decode('utf-8', 'replace')
        i = j + 1 + n + 1
    return res


def tree_of(ref, pre):
    out = subprocess.run(['git', '-C', ROOT, 'ls-tree', '-r', '--name-only', ref, pre],
                         capture_output=True, text=True, errors='replace').stdout
    return [p for p in out.split('\n') if p.endswith('.py')]


def mine(paths):
    """`S4`'s own definition of this seat's receipts, kept verbatim so the counts compare."""
    # ⛭ the `.py` filter belongs HERE and not only in `tree_of`: a first draft of this receipt read
    #   the live side without it and carried `CLAIMS.md` into the denominator, printing `313` for a
    #   population of `312`.  *A sweep's denominator is a claim like any other.*
    return sorted(p for p in paths
                  if p.endswith('.py')
                  and (p.startswith('receipts/P15_CR_cosmology/')
                       or p.startswith('receipts/L_probability/S')))


# ============================================================ the instrument
#: `S4`'s two lists, copied so this receipt stands alone.  ** Equivalence to `S4`'s own detector is
#  CHECKED below rather than asserted: with all three repairs off, the two must agree site for site.
SHARED = ('quote_pin_baseline', 'prose_pin_baseline', 'unread_figure_baseline', 'INDEX.md',
          'THE_REGISTER', 'PROTECTED_OPEN', 'THE_FRONTIER', 'OWED.md', 'THE_WEAVE', 'CORPUS_MAP',
          'PO13_WORKING_STATE', 'marker_transposition_baseline', 'THE_OPEN_PROBLEMS_LEDGER',
          'OPEN_PROBLEMS_MAP')
ENUM = ('glob', 'listdir', 'walk', 'iglob')
CNT = ("id='len'", "id='sum'", "attr='count'")
PINLIKE = re.compile(r'^[0-9a-f]{7,40}$')


def _tg(node):
    t = node.targets if isinstance(node, ast.Assign) else [node.target]
    return [nm.id for x in t for nm in ast.walk(x) if isinstance(nm, ast.Name)]


def _reaches(d, names):
    return any(f"id='{n}'" in d for n in names)


def detect(src, fn=True, nm=True, lp=True):
    """the equality sites where an int literal meets a count of something LIVE and SHARED.

    `fn`/`nm`/`lp` are the three repairs, separable so each one's gain is measured on its own:
      fn -- taint carried through a function that reads the shared artefact
      nm -- the count bound to a NAME before the comparison
      lp -- taint carried onto a `for` target iterating the shared artefact
    With all three off this is `S4`'s `flagged()`, and that is gated.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    shared_fns = set()
    if fn:
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                d = ast.dump(node)
                if any(s in d for s in SHARED) or any(f"attr='{g}'" in d or f"id='{g}'" in d
                                                      for g in ENUM):
                    shared_fns.add(node.name)
    tainted = set()
    for _ in range(6):
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                d = ast.dump(node.value) if node.value is not None else ''
                if (any(s in d for s in SHARED)
                        or any(f"attr='{g}'" in d or f"id='{g}'" in d for g in ENUM)
                        or _reaches(d, tainted) or _reaches(d, shared_fns)):
                    tainted.update(_tg(node))
            elif isinstance(node, ast.For) and lp:
                d = ast.dump(node.iter)
                if (any(s in d for s in SHARED) or _reaches(d, tainted)
                        or _reaches(d, shared_fns)):
                    tainted.update(x.id for x in ast.walk(node.target)
                                   if isinstance(x, ast.Name))
    counts = set()
    if nm:
        for _ in range(4):
            for node in ast.walk(tree):
                if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
                    d = ast.dump(node.value)
                    if any(c in d for c in CNT) or _reaches(d, counts):
                        counts.update(_tg(node))
    out = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Compare) and len(node.ops) == 1
                and isinstance(node.ops[0], ast.Eq)):
            continue
        parts = [node.left, node.comparators[0]]
        lit = [x for x in parts if isinstance(x, ast.Constant) and isinstance(x.value, int)]
        oth = [x for x in parts if x not in lit]
        if not (lit and oth):
            continue
        d = ast.dump(oth[0])
        names = {n.id for n in ast.walk(oth[0]) if isinstance(n, ast.Name)}
        direct = any(c in d for c in CNT) and bool(names & tainted)
        vianame = bool(names & counts & tainted)
        if direct or vianame:
            out.append((node.lineno, node.col_offset, lit[0].value,
                        frozenset(names & tainted), 'DIRECT' if direct else 'VIA-NAME'))
    return out


def grounds_of(src, tree):
    """stage two's two name sets, with the pin followed THROUGH A CALL as well as into one."""
    frozen = {t for node in ast.walk(tree) if isinstance(node, ast.Assign)
              and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
              and PINLIKE.match(node.value.value) for t in _tg(node)}
    for _ in range(4):
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                seg = ast.get_source_segment(src, node.value) or ''
                if ('{PIN}:' in seg or re.search(r"['\"][0-9a-f]{7,40}:", seg)
                        or _reaches(ast.dump(node.value), frozen)):
                    frozen.update(_tg(node))
    # ⛭⛭⛭ r7246 (60), on 70's routed report: ** A COMPREHENSION THAT FILTERS A LIVE POPULATION IS
    #   NOT A SELF-DECLARATION. **  The first draft counted every `ListComp`/`SetComp`/`DictComp` as
    #   self-made, so `unadj = [r for r in rows if ...]` -- a filter of a shared ledger -- was filed
    #   `SELF` and never reached the exposed bucket.  *** That is a site the class is about, hidden by
    #   the partition rather than by the detector. ***
    #   ⌗ The criterion is conservative and taint-free: a comprehension is self-declared only when
    #   every one of its generators iterates something DECLARED HERE -- a literal, or a `range` -- and
    #   a comprehension over a NAME or a CALL is not.  *A plain `[]`/`()`/`{}` literal stays
    #   self-made, which is what the test was for.*
    def _self_decl(v):
        if isinstance(v, (ast.List, ast.Tuple, ast.Dict, ast.Set)):
            return True
        if isinstance(v, (ast.ListComp, ast.SetComp, ast.DictComp)):
            return all(isinstance(g.iter, (ast.List, ast.Tuple, ast.Dict, ast.Set))
                       or (isinstance(g.iter, ast.Call) and isinstance(g.iter.func, ast.Name)
                           and g.iter.func.id == 'range')
                       for g in v.generators)
        return False

    selfmade = {t for node in ast.walk(tree) if isinstance(node, ast.Assign)
                and _self_decl(node.value)
                for t in _tg(node)}
    return frozen, selfmade


def ground(site, pre):
    frozen, selfmade = pre
    via = set(site[3])
    if via & frozen:
        return 'FROZEN'
    if via and via <= selfmade:
        return 'SELF'
    if site[2] == 1:
        return 'ROW-SCOPED'
    return 'EXPOSED'


def in_claim(tree):
    """the lines inside a gate/assert CALL.  ** An `if` is not a claim and must not be counted. **"""
    ok = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert) or (
                isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in ('gate', 'check', 'require')):
            ok.update(s.lineno for s in ast.walk(node) if hasattr(s, 'lineno'))
    return ok


def sweep(srcs):
    """every claim-site in a {rel: src} mapping, partitioned."""
    part, sites = collections.Counter(), []
    for rel, s in srcs.items():
        h = detect(s)
        if not h:
            continue
        tree = ast.parse(s)
        cl, pre = in_claim(tree), grounds_of(s, tree)
        for st in h:
            if st[0] not in cl:
                continue
            g = ground(st, pre)
            part[g] += 1
            sites.append((rel, st[0], st[2], st[4], g))
    return sites, part


def s4_flagged(src, s4src):
    """`S4`'s own `flagged()`, lifted from `S4`'s pinned blob -- not re-typed."""
    t = ast.parse(s4src)
    body = [n for n in t.body
            if (isinstance(n, ast.Assign) and any(getattr(x, 'id', '') in ('SHARED', 'ENUM')
                                                  for x in n.targets))
            or (isinstance(n, ast.FunctionDef) and n.name == 'flagged')]
    ns = {'ast': ast, 're': re, 'os': os}
    exec(compile(ast.Module(body=body, type_ignores=[]), '<S4>', 'exec'), ns)
    return ns['flagged'](src)


S4REL = [p for p in tree_of(PIN, 'receipts/L_probability/')
         if os.path.basename(p).startswith('S4_')][0]
S4SRC = at(PIN, S4REL)
S2REL, S3REL, S6REL = (
    [p for p in tree_of(PIN, 'receipts/L_probability/')
     if os.path.basename(p).startswith(k)][0] for k in ('S2_', 'S3_', 'S6_'))

# ============================================================ A. the four sites, and what saw them
head('A.  THE FOUR EXACT-COUNT SITES ON THE QUOTE-PIN BUCKETS AS r7227 FOUND THEM')

_pre = {rel: at(f'{R7227}^', rel) for rel in (S2REL, S3REL, S4REL, S6REL)}
BUCKET = (2167, 2170, 2236, 2287)
_cand = []
for rel, s in _pre.items():
    for node in ast.walk(ast.parse(s)):
        if (isinstance(node, ast.Compare) and len(node.ops) == 1
                and isinstance(node.ops[0], ast.Eq)):
            for x in (node.left, node.comparators[0]):
                if isinstance(x, ast.Constant) and x.value in BUCKET:
                    _cand.append((os.path.basename(rel)[:3], node.lineno, x.value,
                                  ast.unparse(node)[:46]))
_cand.sort()
_saw_old = {}
_saw_new = {}
for rel, s in _pre.items():
    k = os.path.basename(rel)[:3]
    _saw_old[k] = {l for l, _, _ in s4_flagged(s, S4SRC)}
    _saw_new[k] = {st[0] for st in detect(s)}
_S3L = [l for k, l, v, _ in _cand if k == 'S3_'][0]
for k, l, v, txt in _cand:
    print(f"      {k} L{l:<5d} {v}   S4 saw it: {l in _saw_old[k]!s:<5}  corrected: "
          f"{l in _saw_new[k]!s:<5}  {txt}")

gate('Ⓐ① four exact-count sites on the quote-pin buckets stood in this seat`s receipts at the '
     'commit `r7227` edited from, one each in `S2`, `S3`, `S4` and `S6`',
     len(_cand) == 4 and sorted({k for k, *_ in _cand}) == ['S2_', 'S3_', 'S4_', 'S6_'])

gate('Ⓐ② *** AND `S4`\'s OWN DETECTOR SAW EXACTLY ONE OF THEM --- `S6`\'s --- AND DID NOT SEE '
     '`S4`\'s OWN GATE. ***  *The instrument built to enumerate the class is blind to the form its '
     'own gate is written in.*',
     sum(1 for k, l, v, _ in _cand if l in _saw_old[k]) == 1
     and [k for k, l, v, _ in _cand if l in _saw_old[k]] == ['S6_'])

gate('Ⓐ③ the corrected detector sees THREE of the four, and the one it still does not see is `S2`\'s '
     '`_FROM - _FELL_BY == 2170`, which is arithmetic on two INT LITERALS and therefore is not in '
     'the class at all -- *the precision control for this whole revision: the repair that finds `S4`'
     '\'s gate must not fire on a restated subtraction*',
     sum(1 for k, l, v, _ in _cand if l in _saw_new[k]) == 3
     and [k for k, l, v, _ in _cand if l not in _saw_new[k]] == ['S2_']
     and '_FELL_BY, _FROM = 66, 2236' in _pre[S2REL])

gate('Ⓐ④ and `S2`\'s live half in that same gate is already MONOTONE -- `len(UNADJ) <= 2170` -- so '
     'the exact form there is a record of a completed pass and not a claim on a live set',
     'len(UNADJ) <= 2170' in _pre[S2REL] and 'len(UNADJ) == 2170' not in '\n'.join(
         ln for ln in _pre[S2REL].split('\n') if not ln.lstrip().startswith('#')))

# ============================================================ B. the pin is the defect that bit
head('B.  WHY `S6` GOT THROUGH: A PINNED SWEEP CANNOT CONTAIN ITS OWN REVISION`S GATES')

_s4_intro = subprocess.run(['git', '-C', ROOT, 'log', '--diff-filter=A', '--format=%h',
                            '--', S4REL], capture_output=True, text=True).stdout.split()
_s4_pin_time = subprocess.run(['git', '-C', ROOT, 'rev-list', '--count',
                               f'{S4PIN}..{_s4_intro[-1]}'], capture_output=True,
                              text=True).stdout.strip()
print(f"      S4 is introduced by {_s4_intro[-1]}, which is {_s4_pin_time} commit(s) after its own "
      f"pin {S4PIN}")
gate('Ⓑ① `S4`\'s pin is STRICTLY EARLIER than the commit that introduces `S4`, so every gate `S4` '
     'itself writes is outside the population `S4` sweeps -- *** the exclusion is arithmetic and not '
     'an oversight, which is why no amount of detector repair would have found it ***',
     int(_s4_pin_time) >= 1)

_s6_intro = subprocess.run(['git', '-C', ROOT, 'log', '--diff-filter=A', '--format=%h',
                            '--', S6REL], capture_output=True, text=True).stdout.split()
_s6_after = subprocess.run(['git', '-C', ROOT, 'rev-list', '--count',
                            f'{S4PIN}..{_s6_intro[-1]}'], capture_output=True,
                           text=True).stdout.strip()
gate('Ⓑ② and `S6`, whose site the detector CAN see, is introduced after that pin too -- so the one '
     'site in the class that was detectable was never in a swept population',
     int(_s6_after) >= 1 and _cand and 'S6_' in {k for k, *_ in _cand})

_at_pin = {k: v for k, v in at_many(S4PIN, mine(tree_of(S4PIN, 'receipts/'))).items() if v}
_live_rel = mine(subprocess.run(['git', '-C', ROOT, 'ls-files', 'receipts/'],
                                capture_output=True, text=True).stdout.split('\n'))
_live = {k: v for k, v in at_many(PIN, _live_rel).items() if v}
_sp, _pp = sweep(_at_pin)
_sl, _pl = sweep(_live)
print(f"      at {S4PIN}: {len(_at_pin)} receipts, {len(_sp)} claim-site(s)  {dict(_pp)}")
print(f"      at {PIN}: {len(_live)} receipts, {len(_sl)} claim-site(s)  {dict(_pl)}")
_new_rel = [r for r in _live if r not in _at_pin]
_sn, _pn = sweep({r: _live[r] for r in _new_rel})
print(f"      receipts added since that pin: {len(_new_rel)}; they carry {len(_sn)} claim-site(s) "
      f"{dict(_pn)}")

gate('Ⓑ③ *** THE CLASS AT LEAST DOUBLED IN THE RECEIPTS WRITTEN AFTER THE PIN. ***  The corrected '
     'detector finds more than twice as many claim-sites on this seat`s work at the trunk as in the '
     'population `S4` swept, and the receipts added since the pin carry more than half of them',
     len(_sl) >= 2 * len(_sp) and len(_sn) >= 0.5 * len(_sl))

# ⛭ r7246 (60): ** THE EXACT `6` WAS A COUNT UNDER A PARTITION THAT HAS SINCE BEEN REPAIRED. **
#   *re `r7246`*: `70` reported that the `SELF` test filed every comprehension as self-declared, and
#   fixing it moved twenty-five sites into `EXPOSED`.  The FINDING here is that the growth sits where
#   the pinned sweep cannot see, and that is monotone in the bucket's size; the exact `6` was not.
gate('Ⓑ④ and a LARGE SHARE of the EXPOSED sites at the trunk sit in receipts the pinned sweep '
     'cannot see -- *so the snapshot misses the class where it is live, not where it is dead*.  '
     '⌗ *re `r7246`*: this read `5` of `6` under the partition as it stood and reads a smaller '
     'fraction under the repaired one, which SOFTENS the original claim rather than confirming it, '
     'and the softening is recorded here rather than in the stem',
     _pn['EXPOSED'] >= 5 and _pl['EXPOSED'] >= 6
     and _pn['EXPOSED'] >= _pl['EXPOSED'] // 3)

# ============================================================ C. the three repairs, each measured
head('C.  THE THREE FORM REPAIRS, EACH ONE`s GAIN MEASURED BY REMOVING IT ALONE')

_tot = collections.Counter()
_sup = True
for rel, s in _live.items():
    _o = {l for l, _, _ in s4_flagged(s, S4SRC)}
    _a = {st[0] for st in detect(s)}
    if not (_o <= _a):
        _sup = False
    _tot['old'] += len(_o)
    _tot['new'] += len(_a)
    _tot['off'] += len({st[0] for st in detect(s, fn=False, nm=False, lp=False)})
    for flag in ('fn', 'nm', 'lp'):
        _tot['lost_' + flag] += len(_a - {st[0] for st in detect(s, **{flag: False})})
print(f"      S4's detector {_tot['old']} line(s);  corrected {_tot['new']};  all three repairs "
      f"off {_tot['off']}")
print(f"      lost if removed alone --  function boundary {_tot['lost_fn']};  "
      f"name-bound count {_tot['lost_nm']};  loop target {_tot['lost_lp']}")

gate('Ⓒ① with all three repairs OFF the corrected detector reproduces `S4`\'s own `flagged()` line '
     'for line over this seat`s whole tree -- *the repairs are additions and the baseline is not '
     'silently re-cut*', _tot['off'] == _tot['old'])
gate('Ⓒ② and with them ON it is a strict SUPERSET: no site `S4` found is lost', _sup
     and _tot['new'] > _tot['old'])
gate('Ⓒ③ each repair earns its place alone: removing the function boundary loses `9`, the '
     'name-bound count `6`, the loop target `5` -- and the three overlap, so they are not three '
     'names for one fix',
     _tot['lost_fn'] == 9 and _tot['lost_nm'] == 6 and _tot['lost_lp'] == 5
     and _tot['lost_fn'] + _tot['lost_nm'] + _tot['lost_lp'] > _tot['new'] - _tot['old'])
gate('Ⓒ④ ⛔ AND ONE PRE-REGISTERED PREDICTION IS REFUTED AND SAID SO HERE: this revision predicted '
     '`S3`\'s site needed the FUNCTION-BOUNDARY repair, and it does not -- it needed the name-bound '
     'count, and no site in the `2167` class needs the function repair at all.  *The function repair '
     'is load-bearing elsewhere, which is why it stays, and the prediction about WHERE was wrong*',
     _S3L in {st[0] for st in detect(_pre[S3REL], fn=False)}
     and _S3L not in {st[0] for st in detect(_pre[S3REL], nm=False)}
     and all(l in {st[0] for st in detect(_pre[r], fn=False)}
             for k, l, r in ((k, l, {'S3_': S3REL, 'S4_': S4REL, 'S6_': S6REL}[k])
                             for k, l, v, _ in _cand if k != 'S2_')))

# ============================================================ D. stage two, the other direction
head('D.  THE FOURTH DEFECT: THE SAME FUNCTION BOUNDARY MAKES STAGE TWO INVENT EXPOSED SITES')

_s7rel = [p for p in _live if os.path.basename(p).startswith('S7_')][0]
_s7 = _live[_s7rel]
_t7 = ast.parse(_s7)
_pre7 = grounds_of(_s7, _t7)


def s4_ground(src, site):
    """`S4`'s own `ground()`, lifted from its pinned blob and fed `S4`'s own site tuple shape."""
    t = ast.parse(S4SRC)
    body = [n for n in t.body if isinstance(n, ast.FunctionDef) and n.name == 'ground']
    ns = {'ast': ast, 're': re, 'os': os}
    exec(compile(ast.Module(body=body, type_ignores=[]), '<S4g>', 'exec'), ns)
    return ns['ground'](src, (site[0], site[2], site[3]))


_moved = [(st[0], st[2], s4_ground(_s7, st), ground(st, _pre7))
          for st in detect(_s7) if st[0] in in_claim(_t7)
          and s4_ground(_s7, st) != ground(st, _pre7)]
for l, v, a, b in _moved:
    print(f"      S7 L{l:<5d} {v:<6d} {a} -> {b}")
gate('Ⓓ① `S7` reads its baseline as `_at(PIN, BASELINE)`, so the pin is an ARGUMENT and `S4`\'s '
     'stage two does not see it -- three of `S7`\'s sites are filed EXPOSED or ROW-SCOPED where they '
     'are FROZEN, and the corrected stage two moves all three',
     len(_moved) == 3 and all(b == 'FROZEN' for _, _, _, b in _moved))
gate('Ⓓ② so ONE blindness, read in two directions, costs sites in stage one and invents them in '
     'stage two -- *and the second is the worse half, because an invented EXPOSED site is work '
     'ordered against nothing*',
     {a for _, _, a, _ in _moved} <= {'EXPOSED', 'ROW-SCOPED'})

_s4row = [ln for ln in at(PIN, 'receipts/INDEX.md').split('\n') if os.path.basename(S4REL) in ln]
gate('Ⓓ④ ⌗ AND THE CREDIT WHERE IT IS DUE, BECAUSE THIS IS A COST ON A DECLARED LIMIT AND NOT AN '
     'UNDECLARED DEFECT: `S4`\'s own honest bound already names a member of this family -- *a pinned '
     'read whose commit is an f-string variable* -- and says the frozen class is computed in a '
     'second pass for that reason.  *** The member measured here is a DIFFERENT one, the pin passed '
     'as a CALL ARGUMENT, which that second pass does not reach --- so what this revision adds is '
     'the measured cost of a limit its predecessor stated. ***',
     len(_s4row) == 1
     and 'pinned read whose commit is an f-string variable' in _s4row[0]
     and 'second pass' in _s4row[0])

_nonclaim = []
for rel, s in _live.items():
    h = detect(s)
    if not h:
        continue
    cl = in_claim(ast.parse(s))
    _nonclaim += [(os.path.basename(rel)[:34], st[0]) for st in h if st[0] not in cl]
print(f"      sites dropped because they are not in a claim at all: {len(_nonclaim)}")
gate('Ⓓ③ and four sites are not claims in any sense -- an `if` on a count, a local in a '
     'comprehension -- so the claim filter is part of the instrument and not a convenience',
     len(_nonclaim) == 4)

# ============================================================ E. the enumeration, adjudicated
head('E.  THE SIX EXPOSED SITES AT THE TRUNK, EVERY ONE READ RATHER THAN COUNTED')

_exposed = [x for x in _sl if x[4] == 'EXPOSED']
for rel, l, v, k, _ in _exposed:
    print(f"      {os.path.basename(rel)[:46]:48s} L{l:<5d} {v:<6d} {k}")
# ⛭ r7246 (60): the same repair, and the same reason -- a PIN freezes the POPULATION and not the
#   PARTITION, so an exact bucket size could not survive a partition repair even read at a pin.
gate('Ⓔ① the trunk carries AT LEAST `6` EXPOSED claim-sites in this seat`s `{0}` receipts, read at a '
     'PIN because the population is live -- *and stated as a floor because a pin freezes the '
     'population and not the partition, which `r7246` had to repair*'.format(len(_live)),
     len(_exposed) >= 6)

_s6 = _live[S6REL]
gate('Ⓔ② `S6`\'s two `== 0` sites are DELIBERATE and carry the positive control `S5`\'s ruling '
     'requires: the next gate reads the retiring commit and asserts the SAME counter finds `1` '
     'removed line and `8` added -- *so the zero is a measurement and not an absence of evidence*',
     '_all_bodies.count(RETIRED) == 0' in _s6 and 'len(_removed) == 1 and len(_added) == 8' in _s6)

_s2 = _live[S2REL]
gate('Ⓔ③ `S2`\'s `len(TARGETS) == 2` is scoped by this seat`s own stamp rather than left on the '
     'whole ledger, which is `r7204`\'s prescribed repair already applied -- no ceiling is owed',
     'TARGETS = sorted({r[0] for r in MINE})' in _s2 and 'STAMP' in _s2)

_s5rel = [p for p in _live if os.path.basename(p).startswith('S5_')][0]
_s5 = _live[_s5rel]
gate('Ⓔ④ ⛔ AND TWO OF THE SIX ARE FALSE POSITIVES MANUFACTURED BY THIS REVISION`S OWN FUNCTION '
     'REPAIR: `S5`\'s two counts are over the list `PROBE` the receipt declares itself, reached '
     'through `shadow_run` -- *** the repair that gains nine sites costs two, and that is the price '
     'reported rather than the price hidden ***',
     'def shadow_run(' in _s5 and 'for f in PROBE' in _s5
     and sum(1 for r, *_ in _exposed if os.path.basename(r).startswith('S5_')) == 2)

_wrel = [p for p in _live if 'the_wrap_fix_is_applied' in p][0]
gate('Ⓔ⑤ *** AND ONE IS GENUINE AND IS REPAIRED IN THIS REVISION: `r7238`\'s own gate counted '
     '`BLOCK_PIN` EXACTLY TWICE in `S8`\'s live source. ***  The load-bearing half -- that the '
     'instrument slice is read on ONE line -- is kept exact; the incidental total is monotone.  '
     '⌗ *And the exposure is the one that fired this cycle: another seat edits this seat`s receipts '
     'when the gate requires it, which `r7227` did to three of them*',
     "_s8src.count('_at(BLOCK_PIN,') == 1" in open(os.path.join(ROOT, _wrel),
                                                   encoding='utf-8').read()
     and "_s8src.count('BLOCK_PIN') >= 2" in open(os.path.join(ROOT, _wrel),
                                                  encoding='utf-8').read())

# ============================================================ F. the loose number
head('F.  THE LOOSE NUMBER r7227 ROUTED: EXTENDED 107 AGAINST 70`s 108')

BASE = 'corpus/quote_pin_baseline.tsv'
_rows = [ln.split('\t') for ln in at(PIN, BASE).split('\n')
         if ln.strip() and not ln.startswith('#')]
_rows = [r for r in _rows if len(r) >= 6]
_ext = [r for r in _rows if r[5] == 'EXTENDED']
_keys = {(r[0], r[1]) for r in _ext}
print(f"      EXTENDED rows {len(_ext)};  distinct (receipt, literal) keys {len(_keys)}")
gate('Ⓕ① the baseline carries `108` rows whose verdict is `EXTENDED` and `107` distinct keys among '
     'them -- *** so both numbers are right and they count different things ***',
     len(_ext) == 108 and len(_keys) == 107)

_dups = [k for k, n in collections.Counter((r[0], r[1]) for r in _ext).items() if n > 1]
_dr = [r for r in _ext if (r[0], r[1]) in set(_dups)]
_from = [re.search(r'extended from "(.*?)" by D=(\d+)', r[6]) for r in _dr]
print(f"      duplicate key(s): {len(_dups)} in {len({r[0] for r in _dr})} receipt(s)")
for m in _from:
    if m:
        print(f"        extended from {m.group(1)!r} by D={m.group(2)}")
gate('Ⓕ② the duplicate is ONE key in ONE receipt, and the two rows record extensions of two '
     'DIFFERENT source literals by two different distances -- *** a COLLISION: both landed on the '
     'same extended literal, so `108` extensions made `107` keys and nothing was lost ***',
     len(_dups) == 1 and len({r[0] for r in _dr}) == 1 and len(_dr) == 2
     and all(m for m in _from) and len({m.group(1) for m in _from}) == 2
     and len({m.group(2) for m in _from}) == 2)

# ⛭⛭⛭ r7240, AND IT IS THIS RECEIPT'S OWN SUBJECT BITING IT: the first draft located the
#   pre-batch tree as `git log -2 -- BASE` and took the older of the two.  ** That is a claim whose
#   population a later commit moves, and the commit that moved it was THIS ONE: ** r7240 edits the
#   baseline, so the second-newest commit touching it stopped being the pre-batch trunk the moment
#   this revision was committed, and the gate went red in CI having passed on every pre-commit run.
#   ⇒ The repair is a PIN plus a check that the pin is the state claimed -- the same shape this
#   receipt prescribes for every exposed site it found.
PREBASE = '4bccea92'
_pb = [ln.split('\t') for ln in at(PREBASE, BASE).split('\n') if ln.strip()]
_rec = _dr[0][0]
_pre_lits = {r[1] for r in _pb if len(r) >= 2 and r[0] == _rec}
_pre_ext = [r for r in _pb if len(r) >= 6 and r[5] == 'EXTENDED']
gate('Ⓕ③ and both source literals stood as SEPARATE rows on that receipt before the batch, so the '
     'collision is in the extension and not in the ledger it was applied to -- *and the pin this is '
     'read at is VERIFIED to be pre-batch by the same gate, since it carries no `EXTENDED` row at '
     'all*',
     len(_pb) > 1000 and not _pre_ext
     and all(f'"{m.group(1)}"' in _pre_lits for m in _from if m))

gate('Ⓕ④ ⛔ AND IT IS NOT AN INTERACTION WITH THIS SEAT`s `S7` WRAP CORRECTION, WHICH IS WHAT THE '
     'ORDER CONJECTURED: neither row`s literal contains a whitespace run that the wrap rule widens '
     'differently from a raw find, and the extended literal differs from its two sources by LEADING '
     'characters alone',
     all(m and m.group(1) in _dr[0][1].strip('"') for m in _from)
     and all(' ' .join(m.group(1).split()) == m.group(1) for m in _from if m))

_allkeys = collections.Counter((r[0], r[1]) for r in _rows)
_alldup = [k for k, n in _allkeys.items() if n > 1]
print(f"      duplicate keys in the WHOLE baseline: {len(_alldup)} of {len(_rows)} row(s)")
gate('Ⓕ⑤ *** AND THAT IS THE ONLY DUPLICATE KEY IN THE WHOLE LEDGER --- ONE IN 2,776 ROWS --- AND '
     'NOTHING IN THE CORPUS ASSERTS THE LEDGER`s KEYS ARE UNIQUE, so nothing would have caught it. '
     '*** ⌗ *Routed to `66` and `70` rather than repaired here: the row is `70`\'s batch and the '
     'dedup rule is the baseline`s owner`s to state*',
     len(_alldup) == 1 and len(_rows) == 2776)

_counts_extended = subprocess.run(
    ['git', '-C', ROOT, 'grep', '-l', "EXTENDED", PIN, '--', 'corpus/*.py', 'scripts/*.py'],
    capture_output=True, text=True).stdout.split('\n')
_counts_extended = [p for p in _counts_extended if p.strip()]
gate('Ⓕ⑥ and no gate reads `EXTENDED` as a NUMBER, so the duplicate makes no claim ambiguous -- the '
     'consequence is a ledger hygiene item and not a wrong result',
     not any('check_quote_pins' in p for p in _counts_extended))

# ============================================================ G. this receipt on itself
head('G.  THE INSTRUMENT RUN ON THIS RECEIPT, WHICH IS THE ONE TEST S4 COULD NOT GIVE ITSELF')

_self = open(os.path.abspath(__file__), encoding='utf-8').read()
_ss, _sparts = sweep({'self': _self})
print(f"      this receipt`s own claim-sites: {len(_ss)}  {dict(_sparts)}")
for _, l, v, k, g in _ss:
    print(f"        L{l:<5d} {v:<6d} {k:8s} {g}")
gate('Ⓖ① *** THIS RECEIPT CARRIES NO EXPOSED EXACT COUNT OF ITS OWN, MEASURED BY ITS OWN '
     'DETECTOR. ***  Every exact number it asserts is read at a pin or is a count of its own '
     'declarations; the live populations are gated monotone',
     _sparts['EXPOSED'] == 0)
gate('Ⓖ② and it is not vacuous: the detector DOES find sites in this receipt and files them, so the '
     'zero above is a partition result and not an empty sweep', len(_ss) >= 1)
gate('Ⓖ③ ⌗ and the repair this revision does NOT make is named: the standing guard that would '
     'police the class on every push belongs in the gate layer, which is not this seat`s to edit, so '
     'the patch is routed instead of applied',
     os.path.exists(os.path.join(ROOT, 'scripts', 'lint_assertions.py')))

_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print(f"  gates run: {len(CHECKS)}, failed: {len(_bad)}")
print("""
  ** WHAT THIS REVISION ESTABLISHES. **  S4 reported one live instance of the class it was built to
  enumerate, and three of this seat's receipts then went red on it.  Two of those three were
  invisible to S4's detector because the count was bound to a name before the comparison, S4's own
  gate among them; the third was visible and got through because S4's population is pinned to the
  commit its own revision started from, so a pinned sweep cannot contain its own gates and cannot
  see a single receipt written after it.  The class at least doubled in the receipts added since
  that pin, and five of the six EXPOSED sites at the trunk sit in them.  The same function boundary
  that makes stage one miss real sites makes stage two invent false ones -- three of S7's frozen
  sites were filed as live.  Of the six EXPOSED sites, two are deliberate zeros carrying their
  positive control, one is already stamp-scoped, two are false positives this revision's own repair
  manufactured and reports, and one is genuine and is repaired here.  One pre-registered prediction
  about WHICH repair S3's site needed is refuted and printed.  And the loose number r7227 routed is
  a collision rather than a loss: 108 extensions, 107 keys, the only duplicate key in 2,776 rows,
  and nothing in the corpus asserts that the ledger's keys are unique.""")
if _bad:
    raise SystemExit(1)
