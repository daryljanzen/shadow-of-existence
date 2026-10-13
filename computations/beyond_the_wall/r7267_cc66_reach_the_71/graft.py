#!/usr/bin/env python3
"""
`r7267` ① — THE LOADER THE `59` NEED, AND IT IS WHY THE GAP WAS CALLED `INPUTS`.

`r7261`'s backlog named, per row, the module AND FUNCTION nearest to computing the quantity
its holder only matches as a string, and classified `59` of them `INPUTS`: the function
already computes the right quantity, at the module's OWN inputs, and the row needs it at
different ones.  ** The obstruction is not the mathematics.  It is that every one of those
modules is a SCRIPT: it prints its own report at import, and several run minutes of sympy
to do it. **  So a holder cannot `import` the function it was told to use.

⇒ ** THIS GRAFTS THE FUNCTION INSTEAD OF IMPORTING THE MODULE. **  Given a module path and a
function name it parses the file, takes that `def` plus the TRANSITIVE CLOSURE of the
module-level names the `def` actually reads -- other `def`s, plain assignments, imports --
and executes only those, in a fresh namespace, in source order.  Nothing else in the file
runs: no print, no sweep, no assert at module scope.

⚠ ** AND THE CLOSURE IS COMPUTED OVER THE `AST`, NOT BY TEXT. **  A name is a dependency when
it appears as a `Load` inside the retained statement and is bound at module level and is not
shadowed by a parameter or a local binding of the same statement.  That last clause is the
one a regex gets wrong, and getting it wrong here would silently graft a module-level
constant over a local of the same name.

WHAT IS NOT CLAIMED.  ** Not that this is safe on arbitrary code ** -- it executes the
statements it retains, and it is pointed only at this corpus.  ** Not that a graft is
equivalent to the module ** -- a graft that needs a name bound inside the module's own loops
or `if __name__` block RAISES rather than guessing, and that refusal is tested below.
"""
import ast
import builtins
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
COMP = os.path.join(ROOT, 'computations')


class GraftError(RuntimeError):
    pass


def _bound_by(stmt):
    """the module-level names this top-level statement BINDS -- `x = ...`, a `def`, an import.

    ⚠ ** A SUBSCRIPT OR ATTRIBUTE TARGET IS NOT A BINDING AND MUST NOT BE READ AS ONE. **
    `g[0, 1] = 1` mutates `g`; it does not create it.  A first version of this file walked the
    target for any `ast.Name`, so it registered `g[2, 2] = g[3, 3] = 1` as the LAST binding of
    `g` and dropped `g = sp.zeros(4, 4)` -- the graft then raised `NameError: name 'g' is not
    defined` on a module that builds its metric by element assignment, which several in this
    corpus do.  *The mutators are returned separately by `_mutated_by` and retained WITH the
    binding, in source order, so the matrix is built the way the module builds it.*"""
    out = set()
    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        out.add(stmt.name)
    elif isinstance(stmt, (ast.Import, ast.ImportFrom)):
        for a in stmt.names:
            out.add((a.asname or a.name).split('.')[0])
    elif isinstance(stmt, (ast.Assign, ast.AnnAssign)):
        tgts = stmt.targets if isinstance(stmt, ast.Assign) else [stmt.target]
        for t in tgts:
            if isinstance(t, ast.Name):
                out.add(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                for n in ast.walk(t):
                    if isinstance(n, ast.Name):
                        out.add(n.id)
    return out


def _mutated_by(stmt):
    """the module-level names this statement MUTATES in place without binding them"""
    out = set()
    tgts = []
    if isinstance(stmt, ast.Assign):
        tgts = list(stmt.targets)
    elif isinstance(stmt, (ast.AnnAssign, ast.AugAssign)):
        tgts = [stmt.target]
    for t in tgts:
        while isinstance(t, (ast.Subscript, ast.Attribute)):
            t = t.value
        if isinstance(t, ast.Name) and t.id not in _bound_by(stmt):
            out.add(t.id)
    return out


def _reads(stmt):
    """every name this statement READS, minus the ones it binds inside itself.

    Parameters, comprehension targets, `with ... as`, `for` targets and local assignments all
    shadow a module-level name of the same spelling, so they are subtracted.  A function's own
    name is subtracted too, so recursion is not a dependency on itself."""
    shadow = set(_bound_by(stmt))
    for n in ast.walk(stmt):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = n.args
            for p in (list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)
                      + ([a.vararg] if a.vararg else []) + ([a.kwarg] if a.kwarg else [])):
                shadow.add(p.arg)
        elif isinstance(n, (ast.comprehension, ast.For, ast.AsyncFor)):
            for t in ast.walk(n.target):
                if isinstance(t, ast.Name):
                    shadow.add(t.id)
        elif isinstance(n, ast.withitem) and n.optional_vars is not None:
            for t in ast.walk(n.optional_vars):
                if isinstance(t, ast.Name):
                    shadow.add(t.id)
        elif isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            tgts = (n.targets if isinstance(n, ast.Assign)
                    else [n.target])
            for t in tgts:
                for x in ast.walk(t):
                    if isinstance(x, ast.Name):
                        shadow.add(x.id)
        elif isinstance(n, ast.ExceptHandler) and n.name:
            shadow.add(n.name)
    return {n.id for n in ast.walk(stmt)
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)} - shadow


_KEEP = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef,
         ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign, ast.AugAssign)


_MUTATORS = ('append', 'extend', 'insert', 'add', 'update', 'setdefault', 'pop',
             'popitem', 'clear', 'remove', 'discard', 'sort', '__setitem__')

def _is_empty_container(stmt):
    """TRUE iff this statement binds its target to an EMPTY container and nothing else.

    `ends = {}` is such a binding.  ** A NAME BOUND THIS WAY CARRIES NO VALUE OF ITS OWN:
    whatever the module puts in it is put there by some LATER statement, and if that statement
    is not graftable the graft hands back an empty container with nothing to say so. **"""
    if not isinstance(stmt, ast.Assign) or len(stmt.targets) != 1:
        return False
    if not isinstance(stmt.targets[0], ast.Name):
        return False
    v = stmt.value
    if isinstance(v, ast.Dict) and not v.keys:
        return True
    if isinstance(v, (ast.List, ast.Tuple)) and not v.elts:
        return True
    if isinstance(v, ast.Set) and not v.elts:
        return True
    if (isinstance(v, ast.Call) and isinstance(v.func, ast.Name)
            and v.func.id in ('dict', 'list', 'set', 'defaultdict', 'OrderedDict')
            and not v.args and not v.keywords):
        return True
    return False


def _mutates_elsewhere(stmt):
    """the names this statement mutates IN PLACE, however deeply nested inside it.

    Unlike `_mutated_by`, which reads one top-level assignment, this one looks inside a `for`,
    an `if` or a `with` -- the statement kinds the graft does NOT keep -- and reports every
    module-level name they fill: `x[k] = v`, `x.attr = v`, `x.append(v)`."""
    out = set()
    local = set()
    for n in ast.walk(stmt):
        if isinstance(n, (ast.comprehension, ast.For, ast.AsyncFor)):
            for t in ast.walk(n.target):
                if isinstance(t, ast.Name):
                    local.add(t.id)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = n.args
            for q in (list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)):
                local.add(q.arg)
    for n in ast.walk(stmt):
        tgts = []
        if isinstance(n, ast.Assign):
            tgts = list(n.targets)
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign)):
            tgts = [n.target]
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr in _MUTATORS:
            tgts = [n.func]
        for t in tgts:
            base = t
            depth = 0
            while isinstance(base, (ast.Subscript, ast.Attribute)):
                base = base.value
                depth += 1
            if depth and isinstance(base, ast.Name) and base.id not in local:
                out.add(base.id)
    return out


def graft(module, *names, extra=()):
    """execute the named top-level functions of `module` and nothing else.

    `module` is a path relative to `computations/`.  Returns the namespace.  `extra` names
    further module-level bindings to carry across (a symbol a caller needs to build inputs
    with).  Raises `GraftError` if a dependency is not bound by a graftable top-level
    statement -- rather than letting the name resolve to something it was not."""
    path = os.path.join(COMP, module)
    src = open(path, encoding='utf-8').read()
    tree = ast.parse(src, filename=path)

    # index the graftable top-level statements by every name each binds, keeping the LAST
    # binding in source order -- which is what a module import would have left in place --
    # and index the IN-PLACE MUTATORS of each name separately, because a name's value is its
    # binding plus every mutation of it the module performs at top level.
    by_name, mut_by_name, order = {}, {}, {}
    for i, st in enumerate(tree.body):
        if not isinstance(st, _KEEP):
            continue
        for nm in _bound_by(st):
            by_name[nm] = st
        for nm in _mutated_by(st):
            mut_by_name.setdefault(nm, []).append(st)
        order[id(st)] = i

    wanted = list(names) + list(extra)
    for nm in wanted:
        if nm not in by_name:
            raise GraftError(f'{module}: no graftable top-level binding of {nm!r}')

    keep, seen = {}, set()
    stack = [by_name[nm] for nm in wanted]
    for nm in wanted:
        stack.extend(mut_by_name.get(nm, ()))
    while stack:
        st = stack.pop()
        if id(st) in keep:
            continue
        keep[id(st)] = st
        for nm in sorted(_reads(st)):
            if nm in seen:
                continue
            seen.add(nm)
            if nm in by_name:
                stack.append(by_name[nm])
                stack.extend(mut_by_name.get(nm, ()))
            elif hasattr(builtins, nm):
                pass
            elif nm in ('__doc__', '__file__', '__name__'):
                pass
            else:
                raise GraftError(
                    f'{module}: {nm!r} is read by a grafted statement but is not bound by any '
                    f'graftable top-level statement -- refusing to guess')

    # ** THE EMPTY-CONTAINER REFUSAL. **  A kept statement can bind a name to an EMPTY
    # container -- `ends = {}` -- and leave the filling to a `for` loop, which is not a
    # graftable statement kind.  The graft then hands back an empty dict and NOTHING SAYS SO,
    # so a row taken through it is vacuous rather than wrong.  Refuse instead of guessing.
    kept_names = {nm for st in keep.values() for nm in _bound_by(st)}
    filled_outside = {}
    for st in tree.body:
        if id(st) in keep:
            continue
        for nm in _mutates_elsewhere(st):
            if nm in kept_names:
                filled_outside.setdefault(nm, []).append(getattr(st, 'lineno', 0))
    hollow = sorted(nm for nm in filled_outside
                    if nm in by_name and _is_empty_container(by_name[nm]))
    if hollow:
        where = '; '.join(f'{nm} filled at line(s) '
                          + ','.join(str(x) for x in filled_outside[nm]) for nm in hollow)
        raise GraftError(
            f'{module}: {hollow} is bound to an EMPTY container by a graftable statement and '
            f'filled by one that is not ({where}) -- the graft would hand back an empty '
            f'container with nothing to say so, so it refuses')

    body = [keep[k] for k in sorted(keep, key=lambda k: order[k])]
    mod = ast.Module(body=body, type_ignores=[])
    ast.fix_missing_locations(mod)
    g = {'__name__': f'_graft_{os.path.basename(module)[:-3]}',
         '__file__': path, '__doc__': None}
    exec(compile(mod, path, 'exec'), g)
    missing = [nm for nm in wanted if nm not in g]
    if missing:
        raise GraftError(f'{module}: graft produced no {missing}')
    g['_GRAFTED'] = tuple(sorted({nm for st in body for nm in _bound_by(st)}))
    g['_STATEMENTS'] = len(body)
    # names a non-graftable top-level statement also mutates, where the binding is NOT empty:
    # recorded rather than refused, because the binding does carry a value of its own.
    g['_MUTATED_OUTSIDE'] = tuple(sorted(nm for nm in filled_outside if nm not in hollow))
    g['_OF'] = len(tree.body)
    return g


def _selftest():
    print('  graft.py -- self test')
    g = graft('baryon_edge/L006w_the_d5_fourfold.py', 'twoM', extra=('r0',))
    print(f"    L006w: twoM grafted from {g['_STATEMENTS']} of {g['_OF']} top-level statements")
    assert str(g['twoM'](5)) == '-r_0**4 + r_0**2', g['twoM'](5)
    g2 = graft('baryon_edge/L129_the_invariants.py', 'close', 'det', 'inv_dim', 'chi_VVV',
               extra=('ID', 'CYC'))
    print(f"    L129: four functions from {g2['_STATEMENTS']} of {g2['_OF']}")
    assert callable(g2['close']) and callable(g2['inv_dim'])
    try:
        graft('baryon_edge/L129_the_invariants.py', 'no_such_function_here')
    except GraftError as e:
        print(f'    refusal on a missing name: OK')
    else:
        raise AssertionError('a missing name must raise')
    print('  OK')
    return 0


if __name__ == '__main__':
    sys.exit(_selftest())
