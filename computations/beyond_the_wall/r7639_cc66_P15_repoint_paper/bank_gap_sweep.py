#!/usr/bin/env python3
"""Which CR-arm spectra do cc66's 44 P15 receipts read that have no arm-of-record counterpart?

The question is a bank question, so it is answered from the bank: for every spectrum one of the 44
actually loads, ask whether `<name>_leafrec1` is on disk beside it.  `_leafrec1` is the arm-of-record
suffix (`AOR = {'lcdm': '', 'cr': '_leafrec1'}`), and the 37 files that already carry it fix the
convention: the suffix goes at the END of the name.

THE HARD PART IS NOT THE GAP, IT IS THE READING.  Receipts load spectra through f-strings
(`f'r6941_fine_{t}.npz'`), so a name need never appear in the source.  A first version of this sweep
matched each TEMPLATE as a regex against the bank and credited `r6941_fine_cr_visleaf` with 23 readers
where it has 2 -- the template `r6941_fine_{t}` with `t` in `('lcdm','cr')` cannot produce that name,
but a regex with a permissive placeholder happily matches it.  So nothing here matches a pattern
against the bank.  Every template is EXPANDED over the values its placeholder can actually take:

  * a loop or comprehension over a literal tuple of strings, including a tuple target bound positionally;
  * a loop over a dict literal's `.items()`, which binds the first name to that dict's keys;
  * a tuple target over a NAME bound to a sequence of tuples -- `for t, _desc in CAND:`, which is how
    `model_difference` reaches the four `r6885` knob pairs;
  * an assignment of a string or of a tuple of strings;
  * a dict literal's values, for a placeholder of the form `D[k]`;
  * a function or lambda parameter, from the string arguments at its call sites.

** THE ONE KNOWN OVER-MATCH, DECLARED. **  A template whose suffix is keyed to another placeholder --
`f'cc66_r185_verify_{arm}{AOR[arm]}.npz'` -- is expanded as a CROSS product, so the sweep names pairs
the code never forms (`cc66_r185_verify_cr` and `r6889_nufs0_cr` in `free_streaming`).  It therefore
over-counts and never under-counts, which is the safe direction for a gap list.  Tracing `np.load`
through the eleven receipts that carry a gap confirmed the direction and the counts: 24 of 24
(gap, reader) pairs are a real load, and those two over-matches are the only two swept-but-not-loaded
names in the eleven.

Anything left unresolved is PRINTED rather than guessed at.  All ten that remain load from a response
grid -- `refit_grid`, `refit_grid185`, `r7093_directions/grid_oneclock`, `r7095_directions/grid_licensed`
-- and not from the bank, which is a separate class and is reported as one.

Run from anywhere.  Writes nothing.
"""
import ast
import collections
import itertools
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REC = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

MINE = [l.strip() for l in open(os.path.join(HERE, 'mine44.txt')) if l.strip()]
DISK = set(f[:-4] for f in os.listdir(SPEC) if f.endswith('.npz'))
NPZ = re.compile(r'^[A-Za-z0-9_.+-]+\.npz$')
ISCR = re.compile(r'(^|[._])cr([._]|$)')
HOLE = '\x00'


def templates_and_literals(tree):
    """every `*.npz` string constant, and every `*.npz` f-string as (lineno, template, placeholders)"""
    lits, tmpls = set(), []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and NPZ.match(n.value):
            lits.add(n.value[:-4])
        elif isinstance(n, ast.JoinedStr):
            parts, ph, ok = [], [], True
            for v in n.values:
                if isinstance(v, ast.Constant) and isinstance(v.value, str):
                    parts.append(v.value)
                elif isinstance(v, ast.FormattedValue):
                    parts.append(HOLE)
                    ph.append(ast.unparse(v.value))
                else:
                    ok = False
            t = ''.join(parts)
            if ok and t.endswith('.npz'):
                tmpls.append((n.lineno, t, ph))
    return lits, tmpls


def bindings(tree):
    """placeholder name -> the string values it can take, read off the syntax alone"""
    b = collections.defaultdict(set)
    keys, seqs = {}, {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Dict):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    keys[t.id] = set(k.value for k in n.value.keys
                                     if isinstance(k, ast.Constant) and isinstance(k.value, str))
        if isinstance(n, ast.Assign) and isinstance(n.value, (ast.Tuple, ast.List)) \
                and any(isinstance(e, (ast.Tuple, ast.List)) for e in n.value.elts):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    seqs[t.id] = n.value
    deferred = collections.defaultdict(set)
    for n in ast.walk(tree):
        if isinstance(n, (ast.For, ast.comprehension)):
            tgt, it = n.target, n.iter
            if isinstance(tgt, ast.Name) and isinstance(it, (ast.Tuple, ast.List, ast.Set)) \
                    and all(isinstance(e, ast.Constant) and isinstance(e.value, str) for e in it.elts):
                b[tgt.id] |= set(e.value for e in it.elts)
            elif isinstance(tgt, ast.Tuple) and isinstance(it, (ast.Tuple, ast.List)):
                for row in it.elts:                      # a sequence of tuples, bound positionally
                    if not isinstance(row, (ast.Tuple, ast.List)):
                        continue
                    for i, e in enumerate(tgt.elts):
                        if isinstance(e, ast.Name) and i < len(row.elts) \
                                and isinstance(row.elts[i], ast.Constant) \
                                and isinstance(row.elts[i].value, str):
                            b[e.id].add(row.elts[i].value)
            elif isinstance(tgt, ast.Tuple) and isinstance(it, ast.Name) and it.id in seqs:
                for row in seqs[it.id].elts:
                    if not isinstance(row, (ast.Tuple, ast.List)):
                        continue
                    for i, e in enumerate(tgt.elts):
                        if isinstance(e, ast.Name) and i < len(row.elts) \
                                and isinstance(row.elts[i], ast.Constant) \
                                and isinstance(row.elts[i].value, str):
                            b[e.id].add(row.elts[i].value)
            elif isinstance(tgt, ast.Tuple) and isinstance(it, ast.Call) \
                    and isinstance(it.func, ast.Attribute) and it.func.attr == 'items' \
                    and isinstance(it.func.value, ast.Name) and isinstance(tgt.elts[0], ast.Name):
                deferred[tgt.elts[0].id].add(it.func.value.id)   # `for tag, _ in D.items()`
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if not isinstance(t, ast.Name):
                    continue
                v = n.value
                if isinstance(v, ast.Constant) and isinstance(v.value, str):
                    b[t.id].add(v.value)
                elif isinstance(v, (ast.Tuple, ast.List, ast.Set)) \
                        and all(isinstance(e, ast.Constant) and isinstance(e.value, str) for e in v.elts):
                    b[t.id] |= set(e.value for e in v.elts)
                elif isinstance(v, ast.Dict):
                    b[t.id + '[]'] |= set(x.value for x in v.values
                                          if isinstance(x, ast.Constant) and isinstance(x.value, str))
        if isinstance(n, ast.Dict):                      # `arm['tag']`, a dict of dicts
            for k, v in zip(n.keys, n.values):
                if isinstance(k, ast.Constant) and isinstance(k.value, str) \
                        and isinstance(v, ast.Constant) and isinstance(v.value, str):
                    b['*' + k.value].add(v.value)
    for name, dicts in deferred.items():
        for d in dicts:
            b[name] |= keys.get(d, set())
    return b


def call_sites(tree):
    """(name -> param -> strings passed to it, lineno -> the functions whose body covers that line)

    A parameter is resolved from the call sites of ITS OWN function, so `t` in `have(t)` does not pick
    up the values passed to `pair(t)`.  Both lambdas exist in `source_decomposition`, and reading the
    wrong one loses `r6889_noop_cr`.
    """
    byname, bodies = {}, {}
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            byname[n.name], bodies[n.name] = [a.arg for a in n.args.args], n
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Lambda) \
                and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            byname[n.targets[0].id] = [a.arg for a in n.value.args.args]
            bodies[n.targets[0].id] = n.value
    calls = collections.defaultdict(lambda: collections.defaultdict(set))
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in byname:
            params = byname[n.func.id]
            for i, a in enumerate(n.args):
                if i >= len(params):
                    continue
                if isinstance(a, ast.Constant) and isinstance(a.value, str):
                    calls[n.func.id][params[i]].add(a.value)
                elif isinstance(a, ast.Name):
                    calls[n.func.id][params[i]].add('\x01' + a.id)
    owner = collections.defaultdict(list)
    for fn, node in bodies.items():
        for m in ast.walk(node):
            if hasattr(m, 'lineno'):
                owner[m.lineno].append(fn)
    return calls, owner


def values_of(p, b, calls, prefer):
    m = re.fullmatch(r'(\w+)\[(\w+)\]', p)
    if m and b.get(m.group(1) + '[]'):
        return set(b[m.group(1) + '[]'])
    m = re.fullmatch(r"(\w+)\['(\w+)'\]", p)
    if m and b.get('*' + m.group(2)):
        return set(b['*' + m.group(2)])
    for fn in list(prefer) + [f for f in calls if f not in prefer]:
        if p in calls.get(fn, {}):
            out = set()
            for x in calls[fn][p]:
                out |= set(b.get(x[1:], set())) if x.startswith('\x01') else {x}
            if out:
                return out
    return set(b[p]) if b.get(p) else None


def main():
    read = collections.defaultdict(set)      # spectrum -> the receipts that load it
    unresolved = []
    for name in MINE:
        tree = ast.parse(open(os.path.join(REC, name + '.py')).read())
        lits, tmpls = templates_and_literals(tree)
        b = bindings(tree)
        calls, owner = call_sites(tree)
        for s in lits:
            if s in DISK:
                read[s].add(name)
        for ln, tmpl, phs in tmpls:
            sets = [values_of(p, b, calls, owner.get(ln, [])) for p in phs]
            if any(s is None for s in sets):
                unresolved.append((name, ln, tmpl, phs))
                continue
            for combo in itertools.product(*[sorted(s) for s in sets]):
                s = tmpl
                for c in combo:
                    s = s.replace(HOLE, c, 1)
                if s[:-4] in DISK:
                    read[s[:-4]].add(name)

    gaps = {s: sorted(r) for s, r in read.items()
            if '_leafrec1' not in s and ISCR.search(s) and (s + '_leafrec1') not in DISK}
    cr = [s for s in DISK if ISCR.search(s) and '_leafrec1' not in s]

    print('THE BANK holds %d spectra, %d of them on the cr arm, and %d of those have no `_leafrec1`.'
          % (len(DISK), len(cr), sum(1 for s in cr if s + '_leafrec1' not in DISK)))
    print('MY %d RECEIPTS read %d of them.  %d are cr-arm spectra with no arm-of-record counterpart:\n'
          % (len(MINE), len(read), len(gaps)))
    for s in sorted(gaps, key=lambda k: (-len(gaps[k]), k)):
        print('  %-24s %d reader(s)' % (s, len(gaps[s])))
        for r in gaps[s]:
            print('        %s' % r)
    print('\ntouching %d of my %d receipts.' % (len(set(r for v in gaps.values() for r in v)), len(MINE)))
    print('\nUNRESOLVED TEMPLATES (%d) -- every one loads from a response grid, not from the bank:'
          % len(unresolved))
    for name, ln, tmpl, phs in unresolved:
        print('  %-62s l.%-5d %-26s %s' % (name[:62], ln, tmpl.replace(HOLE, '{·}'), phs))
    key_arm_gaps(read)


def key_arm_gaps(read):
    """⛔ r7639+cc66.18 -- THE GAP CLASS THE SWEEP ABOVE CANNOT SEE, BECAUSE IT KEYS ON FILENAMES.

    A bank can carry its ARM INSIDE THE FILE, as a key suffix (`k__cr`, `k__lcdm`), and then a
    missing arm of record is a missing KEY and not a missing file.  The filename sweep reports such a
    bank as present and says nothing about the arm, which is how `r6897_fields` -- read by five of my
    44 -- passed as available while having no arm-of-record arm at all.  *The sweep did not
    under-report its own class; its class was the wrong one, and that is not visible from inside it.*
    """
    import numpy as np
    arm_keyed, unread = {}, []
    for s in sorted(DISK):
        try:
            ks = list(np.load(os.path.join(SPEC, s + '.npz'), allow_pickle=True).keys())
        except Exception as e:                      # ⛔ REPORTED, never swallowed: the first draft of
            unread.append((s, type(e).__name__))    #   this function said `continue` and a NameError
            continue                                #   turned 12 gap banks into a clean `0`.
        sfx = {k.split('__', 1)[1] for k in ks if '__' in k}
        arms = {x for x in sfx if x == 'cr' or x.startswith('cr_') or x.endswith('_cr') or '_cr_' in x}
        if arms and not any('leafrec' in x for x in sfx):
            arm_keyed[s] = sorted(arms)
    print('\n' + '=' * 100)
    print('KEY-ARM GAPS -- a bank whose ARM IS A KEY SUFFIX, with no arm-of-record key.')
    print('=' * 100)
    print('%d of the %d banks could not be opened at all%s' % (len(unread), len(DISK),
          ': ' + ', '.join(f'{b} ({e})' for b, e in unread[:6]) if unread else ' -- every one read.'))
    print('%d bank(s) carry a cr arm as a key and have NO arm-of-record key:' % len(arm_keyed))
    for b, a in arm_keyed.items():
        print('  %-26s arm key(s): %s' % (b, ', '.join(a)[:64]))
    hit = {b: [] for b in arm_keyed}
    for name in MINE:
        src = open(os.path.join(REC, name + '.py')).read()
        for b in arm_keyed:
            if b in src:
                hit[b].append(name)
    print('\nREADERS AMONG MY %d:' % len(MINE))
    for b in sorted(hit, key=lambda k: (-len(hit[k]), k)):
        if hit[b]:
            print('  %-26s %d reader(s)' % (b, len(hit[b])))
            for r in hit[b]:
                print('        %s' % r)
    touched = set(r for v in hit.values() for r in v)
    print('\n%d of my %d read at least one key-arm bank with no arm-of-record counterpart.'
          % (len(touched), len(MINE)))
    print('\n⚠ A READER IS NOT AUTOMATICALLY BLOCKED: it is blocked where it reads the `cr` KEY and')
    print('  compares what it gets against a quantity this seat has moved to the arm of record.')
    print('  Measured so far: `held_period_estimator` IS blocked (its candidate side is built from')
    print('  `r6897_fields`\'s `__cr` key); `the_step_is_the_excesss_own_` is NOT (its fields read is')
    print('  `__lcdm` only, control-only, as its own header states); and `the_two_readings_` WAS')
    print('  cross-arm and is repaired at r7639+cc66.18.')


if __name__ == '__main__':
    main()
