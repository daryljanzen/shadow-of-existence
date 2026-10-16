#!/usr/bin/env python3
"""r7406 (60) -- THE SIGNATURE OF THE DEFECT IS THE SIGNATURE OF THE REPAIR.  Four arms, all registered
in `PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ exact 0, ⒝ 1 of 3 (1-2),
⒞ 4 (0-30), ⒟ 15 (2-120).

⛭ `r7402`'s FORM 4 keyed on a clause holding BOTH provenances.  `r7368` ②'s carve-out REQUIRES the
repaired form to hold both -- the historical claim at a pin, the live state reported beside it -- so that
signature cannot tell a defect from its own cure, and FORM 4's precision here is `1` of `3`.
  ⇒ FORM 5 keys on the thing the defect actually is: ** ONE ASSERTED QUANTITY BUILT FROM BOTH **, which
    is what `S37`'s counter was -- a pinned population looked up in a live map, so the number asserted is
    neither historical nor current.  Per NAME, never unioned over the clause.

⛭⛭ The provenance machinery is `r7402`'s and is IMPORTED, not retyped: `_writers`, `_mixes`, `_targets`,
`seat_receipts` and the two read patterns all come from that computation, so a figure here is comparable
to the one it corrects.

    python3 -I cost.py
"""
import argparse
import ast
import importlib.util
import os
import re
import sys
import time
from collections import Counter

FRAME = 'b4e4715d'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R7402 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7402_60_the_gate_that_counted_the_repairs_it_ordered', 'cost.py')

_spec = importlib.util.spec_from_file_location('r7402_cost', R7402)
C = importlib.util.module_from_spec(_spec)
sys.modules['r7402_cost'] = C
_spec.loader.exec_module(C)

# FORM 4's own three hits, named so ⒝ is scored against the record and not against a memory
FORM4_HITS = [
    ('receipts/L555_merge_duplication/M1_a_merge_duplicated_four_protected_rows_and_no_gate_saw_it.py', 322),
    ('receipts/L_probability/S37_the_ground_disqualified_seventeen_of_its_authors_own_calls_and_sixteen_'
     'of_them_are_repairs.py', 197),
    ('receipts/L_probability/S47_the_cheap_tail_closes_whole_and_nine_of_its_fourteen_rows_are_repairs_'
     'of_a_claim_the_tail_itself_made.py', 341),
]


# ⛔⛭ FORM 6 -- FORM 5 WITH THE SOURCE CLASSIFIER CORRECTED, because FORM 5's three hits are ONE
#   ARTEFACT: `r7402`'s live-read pattern includes `__file__`, and every receipt binds
#   `ROOT = os.path.dirname(os.path.abspath(__file__))`, so EVERY name within two hops of `ROOT`
#   inherits LIVE -- which is every name that reads anything at all.  ** A PATH ROOT IS NOT A READ. **
#   ⇒ The sixth instance in this phase of the same family: the detector's UNIT was wrong, here its
#     source classification rather than its target shape, its hop count or its guard.
#   ⌗ `r7402`'s pattern is NOT edited: its recorded output must keep standing.  The corrected pattern
#     is applied in THIS process only, and both figures are reported.
_LIVE_FIXED = re.compile(r'\bopen\s*\(|\bread\s*\(|\bread_text\s*\(|'
                         r'subprocess\.(run|check_output)|\bls-files\b|\blive_')


def census_live_names(tree, src):
    """the names an INSTRUMENT RUN writes -- `r7402`'s `_CENSUS_READ`, applied per target"""
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and n.value is not None:
            if C._CENSUS_READ.search(ast.get_source_segment(src, n.value) or ''):
                out.update(C._targets(n))
        elif isinstance(n, ast.For):
            if C._CENSUS_READ.search(ast.get_source_segment(src, n.iter) or ''):
                out.update(C._targets(n))
    return out


def inputs_closure(nm, inputs, depth=2):
    seen, front, got = set(), {nm}, set()
    for _ in range(depth + 1):
        nxt = set()
        for x in front:
            if x in seen:
                continue
            seen.add(x)
            got.add(x)
            nxt |= inputs.get(x, set())
        front = nxt - seen
        if not front:
            break
    return got


def form5(only=None):
    """a clause is flagged iff ONE name its CONDITION asserts was built, within two hops of its own
    writing statements, from BOTH a pinned source and a census-live source -- and the comparison is not
    merely directional (`r7368` ②'s carve-out).  Returns (hits, carveouts, form3_hits)."""
    hits, carve, form3 = [], [], []
    for f, src in C.seat_receipts():
        if only and f not in only:
            continue
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        kinds, inputs = C._writers(tree, src)
        censusy = census_live_names(tree, src)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in C.ASSERTERS):
                continue
            claim = n.args[C.ASSERTERS[n.func.id]:]
            if not claim:
                continue
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            directional = bool(cmps) and all(isinstance(op, C._DIRECTIONAL)
                                             for cp in cmps for op in cp.ops)
            mixed = [nm for nm in names if {'PINNED', 'LIVE'} <= C._mixes(nm, kinds, inputs)]
            if mixed:
                form3.append((f, n.lineno, sorted(mixed), directional))
            sharp = [nm for nm in mixed
                     if inputs_closure(nm, inputs) & censusy
                     and 'PINNED' in C._mixes(nm, kinds, inputs)]
            if not sharp:
                continue
            if directional:
                carve.append((f, n.lineno, sorted(sharp)))
                continue
            hits.append((f, n.lineno, sorted(sharp)))
    return hits, carve, form3


def carve_population():
    """⒟: clauses whose condition asserts a name with a LIVE source as a DIRECTION or a CEILING only --
    the carve-out's own population, counted as a denominator and never read"""
    out = []
    for f, src in C.seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        kinds, inputs = C._writers(tree, src)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in C.ASSERTERS):
                continue
            claim = n.args[C.ASSERTERS[n.func.id]:]
            if not claim:
                continue
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            if not cmps or not all(isinstance(op, C._DIRECTIONAL) for cp in cmps for op in cp.ops):
                continue
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            if any('LIVE' in C._mixes(nm, kinds, inputs) for nm in names):
                out.append((f, n.lineno))
    return out


# ⛔⛭⛭ FORM 7 -- THE UNIT IS A BINDING IN A SCOPE, NOT A NAME IN A FILE.  FORM 6's two remaining hits
#   are a second artefact of the same kind: `src`'s two-hop closure picks up a one-letter `r` bound to a
#   live read somewhere else in the module, because a name-level map identifies every `r` in the file.
#   ⇒ The seventh form, and the seventh different reason: the provenance of a quantity is a property of
#     the BINDING that produced it, so each function's statements are read in their own scope and a name
#     resolves to the innermost scope that binds it.
#   ⌗ Written here rather than by patching `r7402`: the unit differs, so this is a different instrument
#     and not a correction of that one, and both figures stand side by side.
def _scopes(tree):
    """[(scope node, parent scope node or None)] -- the module and every function, nested ones included"""
    out = [(tree, None)]
    def rec(node, parent):
        for n in ast.iter_child_nodes(node):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                out.append((n, parent))
                rec(n, n)
            else:
                rec(n, parent)
    rec(tree, tree)
    return out


def _own_statements(scope):
    """every statement of `scope` EXCLUDING nested function bodies, which are their own scopes"""
    acc = []
    def rec(node):
        for n in ast.iter_child_nodes(node):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                continue
            acc.append(n)
            rec(n)
    rec(scope)
    return acc


def _scope_writers(scope, src, live_pat):
    """(kinds, inputs) for the bindings this scope makes, by the same rules as `r7402`'s `_writers`
    (the `for` iterable, the guard of a write inside it) but confined to this scope's own statements"""
    kinds, inputs = {}, {}

    def add(nm, seg, eaten):
        pin = bool(C._PIN_READ.search(seg)) or bool(C._SHA.search(seg))
        live = bool(live_pat.search(seg)) and not pin
        kinds.setdefault(nm, set()).add('PINNED' if pin else ('LIVE' if live else ''))
        inputs.setdefault(nm, set()).update(eaten - {nm})

    stmts = _own_statements(scope)
    guards = {}
    for n in stmts:
        if isinstance(n, ast.If):
            g = {x.id for x in ast.walk(n.test) if isinstance(x, ast.Name)}
            gs = ast.get_source_segment(src, n.test) or ''
            for inner in n.body + n.orelse:
                for q in ast.walk(inner):
                    g0, s0 = guards.get(id(q), (set(), ''))
                    guards[id(q)] = (g0 | g, s0 + gs)
    for n in stmts:
        if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and n.value is not None:
            seg = ast.get_source_segment(src, n.value) or ''
            eaten = {x.id for x in ast.walk(n.value) if isinstance(x, ast.Name)}
            g, gs = guards.get(id(n), (set(), ''))
            for nm in C._targets(n):
                add(nm, seg + gs, eaten | g)
        elif isinstance(n, ast.For):
            seg = ast.get_source_segment(src, n.iter) or ''
            eaten = {x.id for x in ast.walk(n.iter) if isinstance(x, ast.Name)}
            for nm in C._targets(n):
                add(nm, seg, eaten)
    return kinds, inputs


def form7():
    """FORM 5's discriminator with the scope-aware unit and the corrected classifier"""
    hits, carve, bare = [], [], []
    for f, src in C.seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        scopes = _scopes(tree)
        tables = {id(sc): _scope_writers(sc, src, _LIVE_FIXED) for sc, _ in scopes}
        parent = {id(sc): p for sc, p in scopes}
        owner = {}
        for sc, _ in scopes:
            for n in _own_statements(sc):
                owner[id(n)] = sc

        def resolve(nm, sc):
            seen = set()
            while sc is not None and id(sc) not in seen:
                seen.add(id(sc))
                k, i = tables[id(sc)]
                if nm in k:
                    return k, i
                sc = parent.get(id(sc))
            return {}, {}

        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in C.ASSERTERS):
                continue
            claim = n.args[C.ASSERTERS[n.func.id]:]
            if not claim:
                continue
            sc = owner.get(id(n), tree)
            k_all, i_all = tables[id(sc)]
            censusy = set()
            for s2, _ in scopes:
                kk, ii = tables[id(s2)]
                for st in _own_statements(s2):
                    if isinstance(st, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and st.value is not None:
                        if C._CENSUS_READ.search(ast.get_source_segment(src, st.value) or ''):
                            censusy.update(C._targets(st))
                    elif isinstance(st, ast.For):
                        if C._CENSUS_READ.search(ast.get_source_segment(src, st.iter) or ''):
                            censusy.update(C._targets(st))
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            directional = bool(cmps) and all(isinstance(op, C._DIRECTIONAL)
                                             for cp in cmps for op in cp.ops)
            mixed, sharp = [], []
            for nm in names:
                kk, ii = resolve(nm, sc)
                if not kk:
                    continue
                prov = C._mixes(nm, kk, ii)
                if {'PINNED', 'LIVE'} <= prov:
                    mixed.append(nm)
                    if inputs_closure(nm, ii) & censusy:
                        sharp.append(nm)
            if mixed:
                bare.append((f, n.lineno, sorted(mixed), directional))
            if sharp:
                (carve if directional else hits).append((f, n.lineno, sorted(sharp)))
    return hits, carve, bare


def with_fixed_classifier(fn):
    """run `fn` with the corrected live-read pattern in place, then restore it"""
    was = C._LIVE_READ
    C._LIVE_READ = _LIVE_FIXED
    try:
        return fn()
    finally:
        C._LIVE_READ = was


def main():
    argparse.ArgumentParser().parse_args()
    print(f'# r7406 (60) -- the discriminator, at FRAME {FRAME}')
    print(f'# provenance machinery imported from r7402, over {len(C.seat_receipts())} receipt(s) '
          f'carrying a +60 stamp')

    t0 = time.time()
    hits, carve, form3 = form5()
    t_f5 = time.time() - t0
    print()
    print(f'# ⒜ FORM 5 over this seat\'s receipts: {len(hits)}   (point prediction 0)   [{t_f5:.1f}s]')
    for h in sorted(hits):
        print(f'#     {h[0].split("/")[-1][:58]}:{h[1]}  {",".join(h[2])}')
    print(f'#    and {len(carve)} more carried only as a DIRECTION or a CEILING, which r7368 ②\'s '
          f'carve-out makes sound:')
    for h in sorted(carve)[:8]:
        print(f'#       {h[0].split("/")[-1][:58]}:{h[1]}  {",".join(h[2])}')

    print()
    print('# ⒝ FORM 5 against FORM 4\'s own three hits   (band 1-2, central 1)')
    only = {f for f, _ in FORM4_HITS}
    h2, c2, _ = form5(only=only)
    kept = [(f, l) for f, l, _ in h2 if (f, l) in [(a, b) for a, b in FORM4_HITS]]
    for f, l in FORM4_HITS:
        verdict = 'KEPT' if (f, l) in [(x[0], x[1]) for x in h2] else 'DROPPED'
        print(f'#     {verdict:7}  {f.split("/")[-1][:58]}:{l}')
    print(f'#    kept {len(kept)} of {len(FORM4_HITS)}')

    print()
    print(f'# ⒞ FORM 3\'s bare shape: {len(form3)} clause(s); FORM 5 keeps '
          f'{len(hits) + len(carve)} of them before the carve-out and {len(hits)} after   '
          f'(band 0-30, central 4)')
    print(f'#    ⇒ the bare shape over-states the discriminated class by '
          f'{len(form3) / max(1, len(hits) + len(carve)):.0f}x before the carve-out')

    t0 = time.time()
    cp = carve_population()
    t_cp = time.time() - t0
    print()
    print(f'# ⒟ the carve-out\'s own population -- a live name asserted ONLY as a direction or a '
          f'ceiling: {len(cp)}   (band 2-120, central 15)   [{t_cp:.1f}s]')
    print(f'#    by receipt: {Counter(f.split("/")[-1][:28] for f, _ in cp).most_common(6)}')

    print()
    h6, c6, f36 = with_fixed_classifier(form5)
    print(f'# ⛔⛭ FORM 6 -- the same discriminator with `__file__` OUT of the live-read pattern, '
          f'because a path root is not a read: {len(h6)} hit(s), {len(c6)} carved out, '
          f'{len(f36)} on the bare shape')
    for h in sorted(h6):
        print(f'#     {h[0].split("/")[-1][:58]}:{h[1]}  {",".join(h[2])}')
    print('#    ⇒ FORM 5\'s hits were ONE artefact: every receipt binds its ROOT from `__file__`, so')
    print('#      every name within two hops of ROOT inherited LIVE.  The detector\'s UNIT was wrong')
    print('#      for the sixth time in this phase -- here its SOURCE CLASSIFICATION.')

    print()
    t0 = time.time()
    h7, c7, b7 = form7()
    print(f'# ⛔⛭⛭ FORM 7 -- the unit is a BINDING IN A SCOPE, not a name in a file: {len(h7)} hit(s), '
          f'{len(c7)} carved out, {len(b7)} on the bare shape   [{time.time() - t0:.1f}s]')
    for h in sorted(h7):
        print(f'#     {h[0].split("/")[-1][:58]}:{h[1]}  {",".join(h[2])}')
    print('#    ⇒ FORM 6\'s two were a SECOND artefact of the same kind: `src`\'s closure picked up a')
    print('#      one-letter `r` bound to a live read elsewhere in the module, because a name-level map')
    print('#      identifies every `r` in the file.  Seven forms, seven different reasons.')

    print()
    print('# every FORM 3 hit, for the record: receipt, line, the mixing names, directional')
    for x in sorted(form3):
        print('\t'.join((x[0], str(x[1]), ','.join(x[2]), str(x[3]))))


if __name__ == '__main__':
    main()
