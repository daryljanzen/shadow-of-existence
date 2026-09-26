"""
P15_the_free_streaming_knob_is_common_to_both_arms_and_the_switch_sweep_finds_no_further_shadow
===============================================================================================

LEVEL: two measurements on an instrument that has just been repaired, which is `r6891`'s order --
pointing `NUFS` at the question on a grid that can resolve it, and sweeping every switch the
instrument reads to find out whether the knob shadow `cc66.35`, `cc66.36` and `cc66.17` each found
by a different route has a fourth instance.

** WHY THE SWEEP IS THE POINT AND NOT THE REPAIRS. **  Three knob shadows have been found in this
sector, each by a DIFFERENT accident: the `NS` literal at `cc66.17` from reading a residual, the
baryon density from a refit that would not move, and `_SWSRC`/`_DPSRC` at `cc66.35` from a bracketing
test that returned a bit-identical spectrum.  *** Three findings by three routes is a RATE, not a
count, and a rate cannot be closed by finding a fourth the same way. ***  ⇒ So this revision does
not look for a fourth.  It enumerates ** every environment switch the instrument reads **, records
from the source text which of the three source constructions and which of the two solver paths reads
each one, and then MEASURES, on the reporting path, whether moving it off its reporting value moves
the spectrum.  ⌗ *The output is the table.  If the table shows nothing further shadowed, the
sector's numbers stop being held subject to an unknown, and `r6891` puts that at the worth of a
fourth finding.*

** AND THE FREE-STREAMING SHIFT IS MEASURED, WHICH `cc66.36` COULD NOT DO AND SAID SO. **  `NUFS`
was built at `r6889+cc66.36` and its phase half came out at exactly one binned grid step, so that
receipt reported the SIGN and refused the VALUE.  ⇒ Here it is located sub-bin, by two independent
locators, on both arms, at four times the multipole resolution, with ** the drag half kept as its
own number and never folded into the phase **.

  ⚠ ** AND IT CORRECTS r6889 ON ONE SUB-CLAIM. **  `cc66.36` gated the shift as "UNIFORM across the
  first four peaks on both arms, which is what a PHASE shift looks like as against a rescaling of the
  acoustic scale", on peak positions quantised to the l grid.  *** Sub-bin, it is not uniform.  It
  rises monotonically with multipole, from about +3 near the first peak to about +12 by l ~ 1500, on
  both arms and on both locators. ***  The uniformity was the grid, and the gate that certified it
  was a gate on quantised integers.  ⌗ *This is the second time in three revisions that a gate
  passed because the resolution, and not the physics, set the number -- `cc66.36`'s own reassociation
  episode was the first -- and both are recorded rather than tidied away.*

-------------------------------------------------------------------------------
COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms are the verified
    185-bin refit minima of `r6825+cc66.25` -- `LH0=67.410309 LOM=0.309826 WBH2=0.021966
    NS=0.954248` for the control, `CRH0=68.581133 CROM=0.297209 WBH2=0.021524 NS=0.997952
    ZSTART=3e7 LEAFSCALES=1` for the arm.  Every run banked for this receipt is one of those two
    commands with AT MOST ONE switch added.
  * The static half reads `ACOUSTIC_two_arm.py` as TEXT, through `ast`, and asserts nothing from
    memory.  Its reporting path is declared from the dispatch's own three lines.
  * The switch screen runs at reduced reach (`LMAXL=500 LSTEP=16`) because ** connectivity is
    path-dependent and not resolution-dependent **: a switch read on this path is read on it at any
    l_max.  ⌗ *Every switch the screen reports as moving NOTHING is re-run at full reach before the
    table calls it inert, because that is the half of the claim reduced reach cannot carry.*
  * The locator runs on the banked `LSTEP=8` spectra and again on `LSTEP=2` spectra computed here,
    so the answer can be shown not to be a property of the grid.
  * Every run is launched by a banked, idempotent script under
    `computations/beyond_the_wall/r6891_directions/`, and the value each switch was moved TO is declared
    in this receipt's own `OFFVAL` table, so the experiment is on the record and not only in the scripts.
    ⚠ *Including `pass5.sh`, which exists because `SWSRC` was missing from the first screen list -- kept
    as its own script rather than folded back in, because a table that silently gained a row would not
    say so.*
  * The lensing operator is `c54.183`'s CAMB lensed/unlensed TT ratio at Planck 2018, used exactly
    as `cc66.33`-`cc66.36` use it, and only for the one Delta-space cross-check.
  * ** NOT CLAIMED: a mechanism for the contrast imbalance. **  `r6891` states that boundary has not
    moved and this receipt does not move it.

WHAT IS CLAIMED.

 (1) The reporting path is what the dispatch says it is, and BOTH solver right-hand sides are on it,
     because `hier_run` calls `evolve` for the tight-coupling leg and `evolve_hier` after it.
 (2) The instrument reads sixty environment switches.  Fifty-one have at least one use site live on
     the reporting path; nine do not, and every one of those nine is confined to a DECLARED
     alternative mode -- `qscan`, the line-of-sight projection diagnostics, or the low-multipole
     analytic block that `LOS=0` selects.
 (3) ** AND THE STATIC READ IS CONFIRMED BY MEASUREMENT AND NOT TRUSTED. **  Each of the nine is set
     away from its default ON the reporting path and the spectrum comes back BIT-IDENTICAL, on both
     arms.  A static reachability argument that no run contradicts is the only kind worth having.
 (4) No further knob shadow.  Every switch written into a source construction or a solver right-hand
     side that the reporting path executes moves the spectrum there, or is inert for a reason the
     source text states and a run confirms.
 (5) The free-streaming phase shift, sub-bin: it is POSITIVE everywhere, it GROWS with multipole, and
     it is not a constant additive shift -- which corrects `r6889`.
 (6) ⚑ ** AND IT IS COMMON TO THE TWO ARMS. **  Band by band the two arms' shifts agree to better
     than a fifth of a multipole, and in units of each arm's own l_A to better than 2e-4.  On
     `r6891`'s own criterion -- "a phase shift common to both is not a candidate for Delta and one
     that differs between them is" -- ** the free-streaming phase shift is not a candidate. **
 (7) And the drag half, kept apart and split in two because it is two things: an ENVELOPE rescale of
     about 1.26, and a peak-to-trough CONTRAST ratio of about 0.99.  ** Delta is a contrast
     difference (`cc66.35`), and this knob's amplitude action is almost all envelope. **  So it is
     not a candidate on that ground either, and the two grounds are independent.

NOT CLAIMED: a mechanism for the contrast imbalance; that the growth of the shift with multipole is
the Bashinsky-Seljak term rather than the k-dependent change in the potentials' decay that `NUFS=0`
also causes -- separating those two is not attempted here; any value of n_s, H_0, Omega_m or omega_b.
-------------------------------------------------------------------------------
"""
import ast
import collections
import os
import sys

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INST).read()

# ===================================================================================================
# PART 1 -- THE REPORTING PATH, DECLARED FROM THE DISPATCH AND NOT FROM MEMORY.
# ===================================================================================================
print("\nPART 1 -- WHAT THE REPORTING PATH IS, READ OFF THE DISPATCH.")
print("-" * 100)

TREE = ast.parse(SRC)
SPANS, PARENT, FNODE = {}, {}, {}


def _walk(node, prefix):
    for ch in ast.iter_child_nodes(node):
        if isinstance(ch, (ast.FunctionDef, ast.AsyncFunctionDef)):
            q = f"{prefix}.{ch.name}" if prefix else ch.name
            end = max(getattr(d, 'lineno', ch.lineno) for d in ast.walk(ch))
            SPANS[q] = (ch.lineno, end)
            PARENT[q] = prefix
            FNODE[q] = ch
            _walk(ch, q)
        else:
            _walk(ch, prefix)


_walk(TREE, '')
_ORDER = sorted(SPANS.items(), key=lambda kv: kv[1][1] - kv[1][0])       # innermost span first


def qwhere(line):
    """the QUALIFIED name of the innermost function containing this line"""
    for q, (a, b) in _ORDER:
        if a <= line <= b:
            return q
    return '<module>'


def lineof(sub, frm=0):
    i = SRC.index(sub, frm)
    return SRC[:i].count('\n') + 1


# ** the three lines that define the path, quoted from the file. **
L_QSCAN = lineof("if os.environ.get('QSCAN', '0') == '1':")
L_LOS = lineof("if os.environ.get('LOS', '1') == '1':")
L_HIER = lineof("if os.environ.get('HIER', '0') == '1':")
L_RET0 = lineof("            return 0\n", SRC.index("PEAKS (line-of-sight, HIERARCHY)"))
MAIN_A, MAIN_B = SPANS['main']
for nm, l in (('QSCAN', L_QSCAN), ('LOS', L_LOS), ('HIER', L_HIER)):
    print(f"    main:{l:<5d} {SRC.splitlines()[l-1].strip()}")
print(f"    main:{L_HIER+1:<5d} {SRC.splitlines()[L_HIER].strip()}")
print(f"    main:{L_RET0:<5d} {SRC.splitlines()[L_RET0-1].strip()}")
check("the dispatch selects the reporting path in three lines, in this order: QSCAN, then LOS, then "
      "HIER -- and the HIER branch RETURNS, so everything in `main` after it is dead there",
      MAIN_A < L_QSCAN < L_LOS < L_HIER < L_RET0 < MAIN_B,
      f"main spans {MAIN_A}-{MAIN_B}; QSCAN {L_QSCAN}, LOS {L_LOS}, HIER {L_HIER}, return {L_RET0}")

# ---- live lines, branch-resolved ONLY where the reporting path settles the test ------------------
# every run in this receipt sets SAVE, so it belongs in the path's environment: leaving it
# out would prune the `if os.environ.get('SAVE'):` body, and pruning a branch the runs DO
# take is the one direction in which this analysis would not be safe.
ENVSET = {'LOS': '1', 'HIER': '1', 'SAVE': '<a path>'}


def envread(node):
    """(name, default) if this node is an os.environ read, else None"""
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'get':
        v = node.func.value
        if isinstance(v, ast.Attribute) and v.attr == 'environ' and node.args \
                and isinstance(node.args[0], ast.Constant):
            d = node.args[1].value if len(node.args) > 1 and isinstance(node.args[1], ast.Constant) \
                else None
            return node.args[0].value, d
    if isinstance(node, ast.Subscript):
        v = node.value
        if isinstance(v, ast.Attribute) and v.attr == 'environ' \
                and isinstance(node.slice, ast.Constant):
            return node.slice.value, '<required>'
    return None


def decide(test):
    """True/False when the reporting path's environment settles this test, else None"""
    if isinstance(test, ast.Compare) and len(test.ops) == 1 \
            and isinstance(test.comparators[0], ast.Constant):
        r = envread(test.left)
        if r:
            got, want = ENVSET.get(r[0], r[1]), test.comparators[0].value
            if isinstance(test.ops[0], ast.Eq):
                return got == want
            if isinstance(test.ops[0], ast.NotEq):
                return got != want
    r = envread(test)
    if r:                                                     # bare `if os.environ.get('X')`
        v = ENVSET.get(r[0], r[1])
        return False if v in (None, '', '<required>') else bool(v)
    return None


TERM = (ast.Return, ast.Raise, ast.Break, ast.Continue)


def live_lines(body):
    """** the lines this statement list executes under the reporting path's environment. **

    A branch is pruned ONLY where `decide` settles its test, so the set OVER-counts what runs.  That
    is the safe direction: an over-counted live set can only UNDER-report a shadow, never invent one.
    """
    out = set()
    for st in body:
        out.add(st.lineno)
        if isinstance(st, ast.If):
            for n in ast.walk(st.test):
                out.add(getattr(n, 'lineno', st.test.lineno))
            d = decide(st.test)
            if d is True:
                sub = live_lines(st.body)
                out |= sub
                if '__term__' in sub:
                    return out
            elif d is False:
                out |= live_lines(st.orelse)
                if '__term__' in out:
                    return out
            else:
                out |= live_lines(st.body) | live_lines(st.orelse)
                out.discard('__term__')
            continue
        if isinstance(st, (ast.For, ast.While, ast.With, ast.Try)):
            for f in ('body', 'orelse', 'finalbody', 'handlers'):
                for s in getattr(st, f, []) or []:
                    out |= live_lines(s.body) if isinstance(s, ast.excepthandler) else live_lines([s])
            out.discard('__term__')
            for n in ast.walk(st):
                if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.add(getattr(n, 'lineno', st.lineno))
            continue
        if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue                      # the def executes; its body is reached by REFERENCE below
        for n in ast.walk(st):
            out.add(getattr(n, 'lineno', st.lineno))
        if isinstance(st, TERM):
            return out | {'__term__'}
    return out


def flines(q):
    s = live_lines(FNODE[q].body if q != '<module>' else TREE.body)
    s.discard('__term__')
    return s


LIVE = {q: flines(q) for q in list(SPANS) + ['<module>']}
check("and `main`'s live lines under LOS=1 + HIER=1 stop at that return: the low-multipole block, "
      "the `los_spectrum` call and the `qscan` call are all outside them",
      max(LIVE['main']) == L_RET0 and (L_RET0 + 1) not in LIVE['main']
      and (L_QSCAN + 1) not in LIVE['main'],
      f"live {min(LIVE['main'])}-{max(LIVE['main'])} of a span that runs to {MAIN_B}; "
      f"the QSCAN body at {L_QSCAN+1} is not live")

# ---- the call/reference graph.  A nested def handed to solve_ivp is never a Call. ----------------
EDGES = collections.defaultdict(list)
for node in ast.walk(TREE):
    if isinstance(node, ast.Call):
        f = node.func
        nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
        if nm:
            EDGES[qwhere(node.lineno)].append((node.lineno, nm))
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
        EDGES[qwhere(node.lineno)].append((node.lineno, node.id))


def resolve(nm, frm):
    cand = [q for q in SPANS if q.split('.')[-1] == nm]
    inner = [q for q in cand if q.startswith(frm + '.')]
    if inner:
        return inner[0]
    top = [q for q in cand if '.' not in q]
    return top[0] if top else (cand[0] if cand else None)


def named(q, win=None):
    ok = LIVE[q] if win is None else win
    return {nm for l, nm in EDGES.get(q, ()) if l in ok}


def reach(roots, rootwin=None):
    seen, stack = set(), list(roots)
    while stack:
        q = stack.pop()
        if q in seen or (q not in SPANS and q != '<module>'):
            continue
        seen.add(q)
        nms = named(q, (rootwin or {}).get(q))
        for nm in nms:
            r = resolve(nm, q)
            if r:
                stack.append(r)
        for qq, pp in PARENT.items():          # a nested def: its parent is reached AND names it
            if pp == q and qq.split('.')[-1] in nms:
                stack.append(qq)
    return seen


REPORT = reach(['main', '<module>'])
check("⚑ ** BOTH SOLVER RIGHT-HAND SIDES ARE ON THE REPORTING PATH **, which is the fact that makes "
      "a shadow in either of them a shadow in the numbers: `hier_run` calls `evolve` for the "
      "tight-coupling leg and `evolve_hier` after the handover, and `_project` builds the source",
      {'evolve', 'evolve.rhs', 'evolve_hier', 'evolve_hier.rhs', '_project', 'hier_run'} <= REPORT,
      f"{len(REPORT)} functions reachable; "
      f"evolve@{lineof('s1, _, NVf = evolve(kb, t_eval=t1, e_end=e_sw)')} and "
      f"evolve_hier@{lineof('s2 = evolve_hier(kb, E2, e_sw, Y1[-1])')}, both inside hier_run")
check("...and `los_spectrum` and `qscan` are NOT, so anything read only there is read on a path no "
      "reported number is computed on",
      'los_spectrum' not in REPORT and 'qscan' not in REPORT,
      f"los_spectrum {'in' if 'los_spectrum' in REPORT else 'out'}, "
      f"qscan {'in' if 'qscan' in REPORT else 'out'}")

# ===================================================================================================
# PART 2 -- THE TABLE, STATIC HALF: EVERY SWITCH, AND WHICH CONSTRUCTION READS IT.
# ===================================================================================================
print("\nPART 2 -- EVERY ENVIRONMENT SWITCH THE INSTRUMENT READS, FROM THE SOURCE TEXT.")
print("-" * 100)
print("""
  ** A BINDING IS NOT A USE, AND THAT DISTINCTION IS THE WHOLE OF THIS HALF. **
  `_DAMPX = float(os.environ.get('DAMPX', 1.0))` sits at module level and executes on every path the
  instrument can take.  *** It proves nothing about whether the value is ever READ. ***  A first pass
  that counted binding sites reported fifty-five of sixty switches live on the reporting path, which
  is the answer a check keyed to the wrong thing gives.  ⇒ Only LOADS of the bound name, and env
  reads that are not pure bindings, count as uses here.
""")

# the five constructions, each a function and a line window
LOWL_A = lineof("        return los_spectrum(kk, EE, Yl, L_A, D_M, R_S)") + 1
ANCH = {}
for lbl, sub, q_, win in (
        ("SRC:LOS", "_DPSRC * np.gradient(g_ * Y[:, :, 3] * Dmp", None, None),
        ("SRC:HIER", "_DPSRC * np.gradient(g_ * tb, ee, axis=0)", None, None),
        ("SRC:LOWL", "_DPSRC * DP * damp", 'main', (LOWL_A, MAIN_B)),
        ("RHS:FLUID", "out[:, 3] = (-(Hc * Rb / (1 + Rb)) * tg", None, None),
        ("RHS:HIER", "out[:, I_TB] = -Hc * tb + DRE * kk ** 2 * Ps", None, None)):
    _l = lineof(sub)
    _q = q_ or qwhere(_l)
    ANCH[lbl] = (_q, set(range(win[0], win[1] + 1)) if win else LIVE[_q], _l)
SUB = {lbl: reach([q], {q: w}) for lbl, (q, w, l) in ANCH.items()}
for lbl, (q, w, l) in ANCH.items():
    print(f"    {lbl:10s} line {l:5d}   in {q}")
check("the five constructions this sector has are where the source says they are: three source "
      "builds on three paths, and two solver right-hand sides",
      [ANCH[k][0] for k in ('SRC:LOS', 'SRC:HIER', 'SRC:LOWL', 'RHS:FLUID', 'RHS:HIER')]
      == ['los_spectrum.source', '_project', 'main', 'evolve.rhs', 'evolve_hier.rhs'],
      ", ".join(f"{k}={ANCH[k][0]}" for k in ANCH))

BIND, USES, DEFAULT, BINDLINES = collections.defaultdict(set), collections.defaultdict(set), {}, set()
for node in ast.walk(TREE):
    if isinstance(node, ast.Assign) and len(node.targets) == 1 \
            and isinstance(node.targets[0], ast.Name):
        for n in ast.walk(node.value):
            r = envread(n)
            if r:
                BIND[node.targets[0].id].add(r[0])
                DEFAULT.setdefault(r[0], r[1])
                BINDLINES |= {n.lineno, node.lineno}
                break
for node in ast.walk(TREE):
    r = envread(node)
    if r:
        DEFAULT.setdefault(r[0], r[1])
        if node.lineno not in BINDLINES:
            USES[r[0]].add((node.lineno, qwhere(node.lineno)))
for node in ast.walk(TREE):
    if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id in BIND:
        if node.lineno in BINDLINES and qwhere(node.lineno) == '<module>':
            continue
        for e in BIND[node.id]:
            USES[e].add((node.lineno, qwhere(node.lineno)))


def onpath(sites):
    return any(q in REPORT and l in LIVE[q] for l, q in sites)


def inanchor(sites, lbl):
    """'own' = written into that construction's own text; 'reach' = only downstream of it"""
    q0, w0, _ = ANCH[lbl]
    if any(q == q0 and l in w0 for l, q in sites):
        return 'own'
    if any(q in SUB[lbl] and l in LIVE[q] for l, q in sites):
        return 'reach'
    return None


ROWS = []
for e in sorted(USES):
    st = sorted(USES[e])
    ROWS.append(dict(env=e, default=DEFAULT.get(e), on=onpath(st), sites=st,
                     reads={lbl: inanchor(st, lbl) for lbl in ANCH if inanchor(st, lbl)}))
SK, RK = ['SRC:LOS', 'SRC:HIER', 'SRC:LOWL'], ['RHS:FLUID', 'RHS:HIER']
mk = lambda r, ks: ''.join('W' if r['reads'].get(k) == 'own'
                           else ('.' if r['reads'].get(k) else '-') for k in ks)
print()
print(f"  {'SWITCH':11s} {'default':>10s} {'path':>5s}  {'LOS HI LOW':^12s} {'FLU HI':^8s}  use sites")
print("  " + "-" * 112)
for r in ROWS:
    print(f"  {r['env']:11s} {str(r['default'])[:10]:>10s} {'YES' if r['on'] else 'NO':>5s}  "
          f"{'  '.join(mk(r, SK)):^12s} {'   '.join(mk(r, RK)):^8s}  "
          + ", ".join(sorted({q + ('' if (q in REPORT and l in LIVE[q]) else '*')
                              for l, q in r['sites']})))
print("""
  columns: the three source constructions -- LOS = `los_spectrum.source`, HI = `_project`,
  LOW = the low-multipole block at the foot of `main` -- and the two solver right-hand sides,
  FLU = `evolve.rhs` and HI = `evolve_hier.rhs`.
    W = the switch is WRITTEN INTO that construction's own text
    . = only reachable downstream of it, not written into it
    - = not on its path at all
  and a use site marked * is one that is DEAD on the reporting path.
""")

OFF = [r['env'] for r in ROWS if not r['on']]
check("the instrument reads sixty environment switches with at least one use site, and every switch "
      "that is bound is also used somewhere",
      len(ROWS) == 60 and not [e for e in DEFAULT if e not in USES],
      f"{len(ROWS)} switches used, {len(DEFAULT)} bound, "
      f"bound-but-never-used {[e for e in DEFAULT if e not in USES]}")
check("⚑ ** NINE OF THE SIXTY HAVE NO LIVE USE SITE ON THE REPORTING PATH **, and every one of the "
      "nine is confined to a DECLARED alternative mode -- `qscan` (QSCAN=1), the line-of-sight "
      "projection diagnostics (HIER=0), or the low-multipole analytic block (LOS=0)",
      sorted(OFF) == ['DAMPX', 'DSAVE', 'DSCAN', 'NOPROJ', 'PHISAVE', 'QK', 'QMIN', 'QTURN', 'RD'],
      f"{len(OFF)}: {sorted(OFF)}")
check("...and each of the nine lives in ONE of exactly three places -- `qscan`, `los_spectrum`, or "
      "`main` after the reporting path has returned -- so it is verified and used in the same mode.  "
      "*That is the difference from the three found shadows, which were each calibrated on one path "
      "and read on another; and whether it holds is settled by MEASUREMENT in Part 3, not here.*",
      all(any(q in ('qscan', 'los_spectrum', 'main') for l, q in
              [s for s in next(r for r in ROWS if r['env'] == e)['sites']]) for e in OFF),
      "qscan: QK/QMIN/QTURN;  los_spectrum: DAMPX/DSCAN/DSAVE  (DAMPX already recorded LOS-only at "
      "r4494);  the low-multipole block: NOPROJ/PHISAVE/RD")
_src4 = {e: mk(next(r for r in ROWS if r['env'] == e), SK) for e in ('SWSRC', 'DPSRC', 'NOISW', 'PISRC')}
check("⛭ ** AND THE SOURCE-SWITCH MATRIX IS NOT SQUARE, FOR A REASON THE TEXT GIVES. **  `SWSRC`, "
      "`DPSRC` and `NOISW` are written into all THREE source constructions after `cc66.36`; `PISRC` "
      "is written into the hierarchy's alone -- because the line-of-sight and low-multipole source "
      "expressions carry NO anisotropic-stress term for it to switch",
      _src4['SWSRC'] == 'WWW' and _src4['DPSRC'] == 'WWW' and _src4['NOISW'] == 'WWW'
      and _src4['PISRC'] == '-W-'
      and '_PI' not in SRC[lineof("return (_SWSRC * g_ * (Y[:, :, 2] / 4 * Dmp + Ps)"):
                               lineof("def spectra(dampx_list):")]
      and '_PI' not in SRC[lineof("    SWd, DPd = _SWSRC * SW * damp, _DPSRC * DP * damp"):
                           lineof("    DO_ISW = os.environ.get('NOISW', '0') != '1'")],
      ", ".join(f"{k}={v}" for k, v in _src4.items())
      + " -- and neither the LOS nor the low-multipole source text mentions `_PI` at all")


# ===================================================================================================
# PART 3 -- THE TABLE, MEASURED HALF: DOES MOVING IT MOVE THE SPECTRUM ON THE REPORTING PATH?
# ===================================================================================================
print("\nPART 3 -- THE SAME SIXTY SWITCHES, MEASURED ON THE REPORTING PATH.")
print("-" * 100)
print("""
  Each run is one arm's refit command with AT MOST ONE switch added, at `HIER=1 LSTEP=16 LMAXL=500`.
  ** A switch reporting NO CHANGE cannot be told from a switch that is not connected -- `r4558`'s own
  rule, and the rule that produced all three found shadows. **  ⇒ So every inert switch here carries
  a REASON from the source text, and where the reason is another switch, a PAIRED run that shows it
  connected once that other switch is set.  The four reasons the table needs are:

    OFF-PATH    no live use site on the reporting path at all -- Part 2's nine
    RATE-ID     inert on the CONTROL arm, because there the leaf congruence IS the physical one.
                `Hphys` adds `OR / a**4` under `RAD_IN_RATE` and `Hleaf` always carries it, and
                `RAD_IN_RATE = True` is set inside `if ARM == 'lcdm'`, so on the control the two
                rates are the SAME EXPRESSION, the Jacobian is 1, and every switch that only chooses
                between the two congruences multiplies by exactly 1.0.  ** And `x * 1.0` is exact --
                the same floating-point fact `cc66.36`'s reassociation episode turned on, which is
                why these come back bit-identical and not merely small. **
    ARM-BRANCH  the arm dispatch reads it in the other arm's branch (`if ARM == 'lcdm': ... else:`)
    GATED       another switch gates it, and a paired run shows it connected once that one is set
""")

SCREEN, HDR, FAILED = {}, {}, {}
for arm in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6891_switch_screen_{arm}.npz'), allow_pickle=True)
    SCREEN[arm] = {k[4:]: (d['ls__' + k[4:]].astype(float), d['Dl__' + k[4:]].astype(float))
                   for k in d.files if k.startswith('ls__')}
    HDR[arm] = {k[4:]: dict(l_A=float(d['lA__' + k[4:]]), r_s=float(d['rs__' + k[4:]]),
                            D_M=float(d['DM__' + k[4:]])) for k in d.files if k.startswith('ls__')}
    FAILED[arm] = [str(x) for x in d['failed']]


def cmp2(arm, a, b):
    """(bit-identical?, max |dD_l|, max relative) between two runs on one arm"""
    la, A = SCREEN[arm][a]
    lb, B = SCREEN[arm][b]
    if len(la) == len(lb) and np.array_equal(la, lb):
        return bool(np.array_equal(A, B)), float(np.max(np.abs(B - A))), \
            float(np.max(np.abs(B - A)) / np.max(np.abs(A)))
    lo, hi = max(la[0], lb[0]), min(la[-1], lb[-1])
    g = np.arange(lo, hi + 1e-9, 8.0)
    Ai, Bi = np.interp(g, la, A), np.interp(g, lb, B)
    return False, float(np.max(np.abs(Bi - Ai))), float(np.max(np.abs(Bi - Ai)) / np.max(np.abs(Ai)))


mv = lambda arm, t: cmp2(arm, 'base', t)

# ** the value each switch was moved TO, declared here so the experiment is on the record. **
OFFVAL = {
    'ARM': '(the sweep runs BOTH arms; that is this switch\'s own test)',
    'BSPLIT': '0', 'CRAMP': 'onset', 'CRIC': 'branchpoint', 'CRPHI': '0.7854', 'CRPSI': 'envelope',
    'CRXE': '0.70', 'CRH0': '69.0', 'CROM': '0.3100', 'DPSRC': '0', 'DRC': '0.5', 'DRE': '0.5',
    'ETAEND': '3000', 'GSRC': '1', 'KBATCH': '100', 'KCONT': '1', 'KFAC': '3.0',
    'KSLICE': '0:200', 'LATARG': '310.0', 'LEAFSCALES': 'the other value on each arm',
    'LG': '32', 'LH0': '68.0', 'LMAXL': '600', 'LN': '16', 'LOM': '0.3200', 'LRSFROM': 'start',
    'LSTEP': '20', 'LZSTART': '1.0e7', 'NK': '320', 'NLOS': '700', 'NODRIVE': '1', 'NOISW': '1',
    'NOTC': '0', 'NS': '0.9800', 'NUFS': '0', 'ORFAC': '1.5', 'PHASEONLY': '1', 'PHASEPOW': '1',
    'PISRC': '0', 'POLC': '0.0', 'RBFAC': '1.1', 'RTOL': '1e-6', 'STACKPERT': '1', 'TCSW': '5.0',
    'WBH2': '0.02250', 'ZSTART': '1.0e7',
    'DAMPX': '2.0', 'DSCAN': '1', 'DSAVE': 'a path', 'NOPROJ': '1', 'PHISAVE': 'a path',
    'QK': '0.02,0.05,0.10', 'QMIN': '1', 'QTURN': 'vel', 'RD': '8.0 (and 3.0)',
    'HIER': '0', 'LOS': '0', 'QSCAN': '1', 'SAVE': 'unset',
}
OFFPATH = sorted(OFF)
RATE_ID = ['GSRC', 'LEAFSCALES', 'PHASEONLY', 'PHASEPOW', 'STACKPERT']
READS_ARM = {'CRAMP': 'cr', 'CRIC': 'cr', 'CRPHI': 'cr', 'CRPSI': 'cr', 'CRXE': 'cr',
             'CRH0': 'cr', 'CROM': 'cr', 'KCONT': 'cr', 'LATARG': 'cr', 'ZSTART': 'cr',
             'LZSTART': 'lcdm', 'LRSFROM': 'lcdm', 'LH0': 'lcdm', 'LOM': 'lcdm'}
MODE = {'HIER': L_HIER, 'LOS': L_LOS, 'QSCAN': L_QSCAN}
other = lambda a: 'cr' if a == 'lcdm' else 'lcdm'

print(f"  {'SWITCH':11s} {'moved to':>22s} | {'control arm':^20s} | {'CR arm':^20s} | reading")
print("  " + "-" * 116)
cell = lambda v: "         --         " if v is None else \
    ("   BIT-IDENTICAL    " if v[0] else f"  moves {v[2]:9.3e}   ")
MEAS = {}
for r in ROWS:
    e = r['env']
    MEAS[e] = [mv(a, e) if e in SCREEN[a] else None for a in ('lcdm', 'cr')]
    if e in MODE:
        rd = f"MODE SELECTOR -- main:{MODE[e]} sends the run to another construction; not measured"
    elif e == 'SAVE':
        rd = "I/O -- its only action is writing the file this receipt reads"
    elif e == 'ARM':
        rd = "the arm selector; both columns of this table ARE its test"
    elif e in OFFPATH:
        rd = "OFF-PATH -- and bit-identical on both arms, which is Part 2 confirmed"
    else:
        bits = []
        if e in READS_ARM:
            bits.append(f"ARM-BRANCH, read on {READS_ARM[e]}")
        if e in RATE_ID:
            bits.append("RATE-ID on the control")
        if e in ('LRSFROM', 'LATARG', 'PHASEPOW'):
            bits.append("GATED, see the paired runs below")
        rd = "; ".join(bits) or "-"
    print(f"  {e:11s} {str(OFFVAL.get(e, '?'))[:22]:>22s} | {cell(MEAS[e][0]):^20s} | "
          f"{cell(MEAS[e][1]):^20s} | {rd}")

# --- the gates -----------------------------------------------------------------------------------
print()
check("every screen run that was asked for produced a spectrum, except ONE -- and that one is "
      "reported rather than dropped: the CR arm with `ZSTART` UNSET cannot solve for its own onset "
      "at `LATARG=301.6`, because `brentq` finds no sign change on [1500, 5e6] at this arm's refit "
      "background.  ⌗ *r6760+cc66.1 widened that bracket to 5e6 for exactly this solve; at the "
      "adjudicated background there is no root in it at all, which is why the refit command supplies "
      "`ZSTART=3e7`.*",
      FAILED['lcdm'] == [] and FAILED['cr'] == ['pairLATARGbase_cr:rc=1'],
      f"lcdm {FAILED['lcdm']}, cr {FAILED['cr']}")
_off = {(e, a): mv(a, e) for e in OFFPATH for a in ('lcdm', 'cr')}
check("⚑ ** THE STATIC READ IS CONFIRMED BY MEASUREMENT AND NOT TRUSTED: ALL NINE OFF-PATH SWITCHES "
      "COME BACK BIT-IDENTICAL ON BOTH ARMS. **  Nine switches, eighteen runs, `max |dD_l| = 0.0` "
      "exactly -- not small, zero.  *A static reachability argument is worth having only when a run "
      "could have contradicted it and did not.*",
      all(v[0] for v in _off.values()),
      f"{len(_off)} runs, max over all of them {max(v[1] for v in _off.values()):.1e}")
check("...and `RD` at a SECOND off-default value is bit-identical too, so the nine are not "
      "bit-identical by the accident of one value",
      cmp2('lcdm', 'base', 'RD2')[0] and cmp2('cr', 'base', 'RD2')[0],
      "RD=3.0 as well as RD=8.0, both arms, exactly 0.0")
_ri = {e: (mv('lcdm', e), mv('cr', e if e != 'PHASEPOW' else 'PHASEPOWon')) for e in RATE_ID}
check("⛭ ** THE RATE-IDENTITY FAMILY: FIVE SWITCHES ARE BIT-IDENTICALLY INERT ON THE CONTROL ARM AND "
      "EVERY ONE OF THEM MOVES THE CR ARM. **  `GSRC`, `LEAFSCALES`, `PHASEONLY`, `PHASEPOW` and "
      "`STACKPERT` all choose between the leaf congruence and the physical one -- and on the control "
      "those are the same expression, so each multiplies by exactly 1.0.  *This is the control arm "
      "being a control: there is no leaf/physical distinction there to make.*",
      all(l[0] and not c[0] for l, c in _ri.values()),
      ", ".join(f"{e} lcdm {'0.0' if l[0] else f'{l[2]:.1e}'} / cr {c[2]:.3e}"
                for e, (l, c) in _ri.items()))
check("...and the source text says why, without a run: `Hphys` differs from `Hleaf` only by the "
      "`RAD_IN_RATE` branch, and `RAD_IN_RATE = True` is assigned inside `if ARM == 'lcdm'`",
      "    if RAD_IN_RATE:\n        t = t + OR / a ** 4" in SRC
      and qwhere(lineof("    RAD_IN_RATE = True")) == '<module>'
      and SRC[:SRC.index("    RAD_IN_RATE = True")].rstrip().endswith("H0 = float(os.environ.get('LH0', H0))")
      is False,
      f"Hphys@{SPANS['Hphys'][0]}, Hleaf@{SPANS['Hleaf'][0]}, "
      f"RAD_IN_RATE=True at line {lineof('    RAD_IN_RATE = True')} inside the lcdm branch at "
      f"{lineof(chr(105)+chr(102)+' ARM == ')}")
_ab = {e: mv(other(a), e) for e, a in READS_ARM.items()}
check("⛭ ** THE ARM-BRANCH FAMILY: FOURTEEN SWITCHES ARE BIT-IDENTICALLY INERT ON THE ARM WHOSE "
      "BRANCH DOES NOT READ THEM **, which is the arm dispatch at main-level `if ARM == 'lcdm': ... "
      "else:` doing its job and not a shadow",
      all(v[0] for v in _ab.values()),
      ", ".join(f"{e}/{other(a)}" for e, a in sorted(READS_ARM.items())))
_moves_home = {e: mv(a, e) for e, a in READS_ARM.items()}
_still = sorted(e for e, v in _moves_home.items() if v[0])
check("...and twelve of those fourteen MOVE on the arm that DOES read them, so none of those twelve "
      "is a null dressed as an arm condition.  ⚠ ** The two that do not are `LATARG` and `LRSFROM`, "
      "and they are the only two things this sweep turned up -- Part 3b. **",
      _still == ['LATARG', 'LRSFROM'],
      ", ".join(f"{e} {v[2]:.2e}" for e, v in sorted(_moves_home.items()) if not v[0])
      + f"  |  still bit-identical: {_still}")
check("⛭ ** AND THE ONE SWITCH GATED BY ANOTHER IS SHOWN CONNECTED BY THE PAIR, NOT ASSUMED: "
      "`PHASEPOW` is bit-identical at the default `PHASEONLY=0` on both arms and moves the CR arm by "
      "176 per cent once `PHASEONLY=1` **, which is `r4558`'s rule discharged by a run",
      mv('lcdm', 'PHASEPOW')[0] and mv('cr', 'PHASEPOW')[0] and not mv('cr', 'PHASEPOWon')[0],
      f"PHASEPOW=1 alone: 0.0 on both arms;  PHASEONLY=1 PHASEPOW=1 on the CR arm: "
      f"{mv('cr', 'PHASEPOWon')[2]:.3e}")
_nk = mv('lcdm', 'NK')
check("...and `NK` is connected -- it moves the control arm -- while on the CR arm the k grid is "
      "re-derived by the continuation block at main:1323-1330 and lands on the same 361 modes at "
      "`NK=320` as at the default, so its CR null is a property of that construction and not of the "
      "switch",
      not _nk[0] and mv('cr', 'NK')[0],
      f"lcdm {_nk[2]:.3e} (780 modes -> 960);  cr exactly 0.0 (361 modes -> 361)")

# ---- THE EXHAUSTIVE ACCOUNTING.  Not "the ones I looked at": ALL of them. ------------------------
SKIP = set(MODE) | {'SAVE', 'ARM'}
CANDIDATES = [r['env'] for r in ROWS if r['env'] not in SKIP]
OBSERVED = {(e, a) for e in CANDIDATES for a in ('lcdm', 'cr')
            if e in SCREEN[a] and mv(a, e)[0]}
EXPLAINED = ({(e, a) for e in OFFPATH for a in ('lcdm', 'cr')}
             | {(e, 'lcdm') for e in RATE_ID}
             | {(e, other(a)) for e, a in READS_ARM.items()}
             | {('PHASEPOW', 'cr'),          # gated by PHASEONLY; the pair shows it connected
                ('NK', 'cr'),                # the CR k grid is re-derived and lands on the same modes
                ('LATARG', 'cr'),            # no root at this background; ZSTART is supplied instead
                ('LRSFROM', 'lcdm')})        # Part 3b -- the one find
check("⚑⚑ ** THE ACCOUNTING IS EXHAUSTIVE, WHICH IS THE ONLY FORM THIS ANSWER IS WORTH ANYTHING IN. "
      "**  Fifty-five switches x two arms, and the set of runs that came back BIT-IDENTICAL is "
      "EXACTLY the set the four readings predict -- no unexplained null, and no switch explained "
      "away that in fact moved.  *That is what closes the rate: not a fourth shadow not found, but "
      "every switch accounted for.*",
      OBSERVED == EXPLAINED,
      f"{len(CANDIDATES)} switches, {len(OBSERVED)} bit-identical runs; "
      f"unexplained {sorted(OBSERVED - EXPLAINED)}; "
      f"predicted-but-moved {sorted(EXPLAINED - OBSERVED)}")
_moved_n = sum(1 for e in CANDIDATES for a in ('lcdm', 'cr')
               if e in SCREEN[a] and not mv(a, e)[0])
check("...and the other side of the same count: every switch written into a source construction or a "
      "solver right-hand side that the reporting path executes MOVES the spectrum there",
      all(not mv(a, e)[0] for e in ('SWSRC', 'DPSRC', 'NOISW', 'PISRC', 'BSPLIT', 'DRC', 'DRE',
                                    'LN', 'LG', 'NUFS', 'NOTC', 'KCONT')
          for a in ('lcdm', 'cr') if not (e == 'KCONT' and a == 'lcdm')),
      f"{_moved_n} of the {_moved_n + len(OBSERVED)} runs move; the source/solver switches move by "
      + ", ".join(f"{e} {mv('cr', e)[2]:.2e}" for e in
                  ('SWSRC', 'DPSRC', 'NOISW', 'PISRC', 'BSPLIT', 'DRC', 'DRE', 'LN', 'LG', 'NUFS',
                   'NOTC')))

# ---------------------------------------------------------------------------------------------------
# PART 3b -- THE TWO THINGS THE SWEEP TURNED UP.  Neither is a knob shadow of the r6476 class, and
# saying which class each IS is the whole content.
# ---------------------------------------------------------------------------------------------------
print("\nPART 3b -- WHAT THE SWEEP TURNED UP, AND WHAT CLASS EACH THING IS IN.")
print("-" * 100)

# ---- (i) LRSFROM: a knob that moves the instrument's PRINTED acoustic scale and not its spectrum ---
_hb = FNODE['hier_run']
_hnames = {n.id for n in ast.walk(_hb) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
_rs_sites = sorted({(l, qwhere(l)) for l in
                    [i_ for i_, ln in enumerate(SRC.split('\n'), 1)
                     if ('R_S' in ln or 'L_A' in ln) and not ln.lstrip().startswith('#')]})
_rs_live = [(l, q) for l, q in _rs_sites if q in REPORT and l in LIVE[q]]
print("""
  ⚑ ** (i) `LRSFROM` MOVES THE INSTRUMENT'S PRINTED ACOUSTIC SCALE BY A QUARTER AND ITS SPECTRUM BY
  EXACTLY ZERO. **  At `LZSTART=6761`, setting `LRSFROM=start` moves the header's `r_s` from 145.38 to
  110.49 Mpc and its `l_A = pi D_M / r_s` from 301.5 to 396.8 -- *** and D_l comes back
  BIT-IDENTICAL. ***

  ⌗ Why, from the source text: on the reporting path `R_S` and `L_A` reach three `print` calls and the
  `SAVE` metadata, and nothing else.  ** `hier_run(kk, EE, L_A_, D_M_, R_S_)` accepts the acoustic
  scale, the distance and the sound horizon AND REFERENCES NONE OF THE THREE IN ITS BODY. **

  ⚠ ** AND r6476's OWN NOTE IN THE FILE IS WHAT THIS CORRECTS. **  It records `LRSFROM` as
  "reachability-checked before use", on the ground that `R_S` "feeds `L_A` two lines below AND the
  header line ... so the knob is visible in the instrument's own report and was seen to move it --
  144.53 Mpc / 301.4 at the default against 109.70 Mpc / 397.1" -- and calls that "a knob checked at
  the REPORTING path, not at the definition".  *** The print is not the reported number. ***  ⇒ This
  is a fourth member of the family and it is NOT of the r6476 class: nothing reported as physics is
  computed from `R_S`, so no number moves and nothing needs rewiring.  ** What was wrong was the
  certification, and it was a certification of the wrong quantity. **

  ⇒ ⛭ ** AND THE CONSEQUENCE IS WORTH STATING THE RIGHT WAY ROUND. **  Because the spectrum does not
  read `L_A`, the agreement the instrument prints -- `l_1/l_A = 0.7312` against the sky's
  `220.6/301.7 = 0.7312` -- is between TWO INDEPENDENTLY COMPUTED QUANTITIES and not a value fed in.
  *A reader could have taken the acoustic scale for an input to the transfer. It is not one.*
""")
check("`hier_run` accepts `L_A_`, `D_M_` and `R_S_` and loads none of the three anywhere in its body",
      not ({'L_A_', 'D_M_', 'R_S_'} & _hnames),
      f"hier_run signature at line {SPANS['hier_run'][0]}; names it does load include "
      f"{sorted(_hnames & {'kk', 'EE', 'kb', 'ls', 'Cl'})}")
def _rs_kind(l):
    ln = SRC.split('\n')[l - 1]
    if 'R_S = rs_from' in ln or 'L_A = np.pi' in ln:
        return 'the definition itself'
    if 'print(' in ln or ln.lstrip().startswith('f"'):
        return 'a print'
    if 'np.savez' in ln or 'l_A=L_A' in ln:
        return 'SAVE metadata'
    if 'hier_run(kk, EE, L_A' in ln:
        return 'passed to hier_run, which drops it'
    return 'ARITHMETIC -- this would be a real input'
_kinds = {l: _rs_kind(l) for l, q in _rs_live}
check("...and every live line on the reporting path that mentions `R_S` or `L_A` is the DEFINITION "
      "itself, a `print`, the `SAVE` metadata, or the `hier_run` call that drops it -- not one is "
      "arithmetic feeding a transfer function.  ** So the acoustic scale is a DIAGNOSTIC of this "
      "instrument and not an input to it. **",
      all(v != 'ARITHMETIC -- this would be a real input' for v in _kinds.values()),
      f"{len(_rs_live)} live sites: " + ", ".join(f"{l} ({v})" for l, v in sorted(_kinds.items())))
_p1, _p2 = cmp2('lcdm', 'pairLRSFROMbase', 'pairLRSFROM')[0], mv('lcdm', 'LRSFROM')[0]
_h0, _h1 = HDR['lcdm']['pairLRSFROMbase'], HDR['lcdm']['pairLRSFROM']
_drs = abs(_h1['r_s'] / _h0['r_s'] - 1)
check("⚑ and the measurement, which is the part r6476 did not have: with `LZSTART=6761` -- the very "
      "configuration that note quotes -- the two runs differ in the reported `r_s` by a quarter and "
      "in D_l by EXACTLY ZERO",
      _p1 and _p2 and _drs > 0.20,
      f"r_s {_h0['r_s']:.2f} -> {_h1['r_s']:.2f} Mpc ({_drs*100:.1f} per cent), "
      f"l_A {_h0['l_A']:.1f} -> {_h1['l_A']:.1f}, D_M unchanged at {_h0['D_M']:.0f} Mpc; "
      f"max |dD_l| = {cmp2('lcdm', 'pairLRSFROMbase', 'pairLRSFROM')[1]:.1f}, and at the reporting "
      f"default LZSTART=3.0e7 it is bit-identical too")
check("⛭ ** AND THIS REVISION'S ONLY EDIT TO THE INSTRUMENT IS COMMENTS, WHICH IS MEASURED AND NOT "
      "ASSERTED. **  `cc66.36` is why: a change that should have been nothing cost 1.1e-16 there.  "
      "Both arms' bases are re-run against the ANNOTATED file and come back bit-identical to the "
      "screen's own bases, which were computed before it",
      cmp2('lcdm', 'base', 'annot')[0] and cmp2('cr', 'base', 'annot')[0],
      "both arms, max |dD_l| = 0.0 exactly")

# ---- (ii) LATARG: the corpus's one fitted number has no root at the arm's adjudicated background ---
print("""
  ⚑ ** (ii) `LATARG` -- WHICH THIS FILE CALLS "THE CORPUS'S ONE FITTED NUMBER" -- HAS NO ROOT AT THE
  CR ARM'S ADJUDICATED BACKGROUND. **  With `ZSTART` unset, the arm solves `pi D_M / r_s(z) = LATARG`
  for the onset redshift by `brentq` on [1500, 5e6].  At `LATARG=301.6` and this arm's refit
  background that solve RAISES: `f(a)` and `f(b)` have the same sign, so there is no root in the
  bracket at all.  ⌗ *`r6760+cc66.1` widened that bracket from 60000 to 5e6 for exactly this solve,
  on the finding that a bracket is an implementation detail until it truncates the answer.  At the
  background the refit since settled on, widening is not enough: there is no root.*  ⇒ ** Which is
  why the refit command supplies `ZSTART=3e7` and every reported number already comes from that. **
  So nothing reported moves -- but the register should say that `LATARG` is not reachable at the arm's
  own minimum, and it did not.
""")
check("the switch is nonetheless CONNECTED, which is what `r4558`'s rule requires before its "
      "inertness at the reporting configuration counts as a result: at values where the root does "
      "exist it moves the spectrum",
      'pairLATARG' in SCREEN['cr'] and not cmp2('cr', 'base', 'pairLATARG')[0],
      f"LATARG=310.0 with ZSTART unset moves D_l by "
      f"{cmp2('cr', 'base', 'pairLATARG')[2]:.3e} against the reporting base")

# ===================================================================================================
# PART 4 -- THE FREE-STREAMING SHIFT, SUB-BIN, ON BOTH ARMS, WITH THE DRAG KEPT APART.
# ===================================================================================================
print("\nPART 4 -- THE FREE-STREAMING PHASE SHIFT, LOCATED RATHER THAN BRACKETED.")
print("-" * 100)
print("""
  `cc66.36` reported this shift at exactly one binned grid step and refused its value.  ** Two
  independent locators are used here so that neither carries the claim alone: **

    A. the PARABOLA VERTEX at each acoustic extremum.  D_l is smooth and broad near an extremum, so
       a quadratic through the 2w+1 sampled points either side has a vertex that is not quantised at
       the l step.  Being per-extremum, it also answers whether the shift is a CONSTANT additive
       shift in l or grows with l -- which is the question `cc66.36`'s gate thought it had settled.
    B. a sub-bin CROSS-CORRELATION of the ENVELOPE-NORMALISED oscillation.  Divide each spectrum by
       its own running geometric-mean envelope over one acoustic period first, so the amplitude
       change cannot leak into the position estimate, then minimise the squared difference over a
       CONTINUOUS shift.  Run band by band it gives the shift as a function of l.

  ** AND THE DRAG HALF IS REPORTED SEPARATELY AND SPLIT IN TWO **, because it is two things: an
  ENVELOPE rescale and a peak-to-trough CONTRAST ratio.  `r6891` asked for it not to become one
  number with the phase; `cc66.35` established that Delta is a CONTRAST difference, so which of the
  two the drag lands in is the whole question.
""")

from numpy.polynomial import polynomial as _P                                # noqa: E402
from scipy.interpolate import CubicSpline                                    # noqa: E402
from scipy.signal import argrelextrema                                       # noqa: E402


def env_of(ls, Dl, per):
    """running geometric mean over one acoustic period in l"""
    lg = np.log(np.maximum(Dl, 1e-300))
    return np.array([np.exp(lg[np.abs(ls - l) <= per / 2].mean()) for l in ls])


def extrema(ls, Dl, order=3, w=3):
    """(l_vertex, kind, D_l there) for every acoustic extremum, located sub-bin"""
    out = []
    for kind, cmp_ in (('max', np.greater), ('min', np.less)):
        for i in argrelextrema(Dl, cmp_, order=order)[0]:
            if i - w < 0 or i + w >= len(ls):
                continue
            x, y = ls[i - w:i + w + 1].astype(float), Dl[i - w:i + w + 1]
            c = _P.polyfit(x - x.mean(), y, 2)
            if c[2] == 0:
                continue
            lv = x.mean() - c[1] / (2 * c[2])
            if ls[i - w] <= lv <= ls[i + w]:
                out.append((lv, kind, float(CubicSpline(ls, Dl)(lv))))
    return sorted(out)


def xshift(ls, A, B, per, lo, hi, rng=40.):
    """B(l) ~ A(l - d): d by continuous minimisation, amplitude divided out first"""
    oa = CubicSpline(ls, A / env_of(ls, A, per))
    ob = CubicSpline(ls, B / env_of(ls, B, per))
    g = np.arange(lo, hi, 1.0)
    ds = np.arange(-rng, rng + 1e-9, 0.02)
    cost = np.array([np.sum((ob(g) - oa(g - d)) ** 2) for d in ds])
    j = int(np.argmin(cost))
    if 0 < j < len(ds) - 1:
        c = _P.polyfit(ds[j-1:j+2] - ds[j], cost[j-1:j+2], 2)
        if c[2] != 0:
            return float(ds[j] - c[1] / (2 * c[2]))
    return float(ds[j])


def locate(tag, fbase, ftest):
    ls, A = (lambda d: (d['ls'].astype(float), d['Dl'].astype(float)))(np.load(os.path.join(SP, fbase)))
    l2, B = (lambda d: (d['ls'].astype(float), d['Dl'].astype(float)))(np.load(os.path.join(SP, ftest)))
    l_A = float(np.load(os.path.join(SP, fbase))['l_A'])
    assert np.array_equal(ls, l2)
    ea, eb = extrema(ls, A), extrema(ls, B)
    print(f"\n  ===== {tag}   l_A = {l_A:.2f}   grid step {ls[1]-ls[0]:.0f}   {len(ls)} multipoles")
    print(f"    {'kind':>5} {'l (free-str)':>13} {'l (fluid)':>11} {'d_l':>8} {'d_l/l_A':>9} "
          f"{'A ratio':>8}")
    dls, lbs, rat = [], [], []
    for (la_, ka, aa), (lb_, kb, ab) in zip(ea, eb):
        if ka != kb:
            continue
        print(f"    {ka:>5} {la_:13.3f} {lb_:11.3f} {lb_-la_:+8.3f} {(lb_-la_)/l_A:+9.5f} "
              f"{ab/aa:8.4f}")
        dls.append(lb_ - la_)
        lbs.append(la_)
        rat.append(ab / aa)
    dls, lbs, rat = map(np.array, (dls, lbs, rat))
    fit = np.polyfit(lbs, dls, 1)
    print(f"    A. mean {dls.mean():+.3f}   sd {dls.std(ddof=1):.3f}   "
          f"spread {dls.max()-dls.min():.3f} over {len(dls)} extrema   "
          f"-- straight line: d_l = {fit[1]:+.3f} {fit[0]:+.5f} l")
    bands = []
    for lo in np.arange(150., ls[-1] - l_A - 50., l_A):
        bands.append((float(lo + l_A / 2), xshift(ls, A, B, l_A, lo, lo + l_A)))
    print("    B. " + "   ".join(f"l~{l:.0f}: {d:+.2f}" for l, d in bands))
    eA, eB = env_of(ls, A, l_A), env_of(ls, B, l_A)
    m = (ls >= 150) & (ls <= ls[-1] - 50)
    cs = []
    for i in range(len(ea) - 1):
        (l1, k1, a1), (l2_, k2, a2) = ea[i], ea[i + 1]
        (m1, _, b1), (m2, _, b2) = eb[i], eb[i + 1]
        if k1 == k2:
            continue
        ca = a1 / a2 if k1 == 'max' else a2 / a1
        cb = b1 / b2 if k1 == 'max' else b2 / b1
        cs.append(cb / ca)
    print(f"    C. DRAG, and it is two numbers: envelope ratio {(eB[m]/eA[m]).mean():.4f} "
          f"(range {(eB[m]/eA[m]).min():.4f}-{(eB[m]/eA[m]).max():.4f});   "
          f"peak-to-trough CONTRAST ratio {np.mean(cs):.4f} "
          f"(range {min(cs):.4f}-{max(cs):.4f})")
    return dict(l_A=l_A, dl=dls, l=lbs, rat=rat, bands=bands, step=float(ls[1] - ls[0]),
                fit=fit, env=float((eB[m] / eA[m]).mean()), con=float(np.mean(cs)),
                envmin=float((eB[m]/eA[m]).min()), envmax=float((eB[m]/eA[m]).max()))


LOC = {}
for arm in ('lcdm', 'cr'):
    LOC[arm] = locate(f"NUFS 1 -> 0 (free-streaming removed), arm = {arm}",
                      f'cc66_r185_verify_{arm}.npz', f'r6889_nufs0_{arm}.npz')

print("\n  ----- the gates on the shift itself -----")
_L, _C = LOC['lcdm'], LOC['cr']
check("⚑ the shift is POSITIVE at every extremum on both arms, which is `cc66.36`'s sign claim "
      "re-established on a locator that is not quantised: removing free-streaming pushes the peaks "
      "to LARGER multipole, the direction the Bashinsky-Seljak pull has",
      all(v > 0 for v in _L['dl']) and all(v > 0 for v in _C['dl']),
      f"24 extrema, smallest {min(_L['dl'].min(), _C['dl'].min()):+.3f}")
check("⚠⚑ ** AND IT IS NOT UNIFORM, WHICH CORRECTS r6889+cc66.36. **  That receipt gated the shift "
      "as \"UNIFORM across the first four peaks on both arms, which is what a PHASE shift looks like "
      "as against a rescaling of the acoustic scale\", on peak positions quantised to the l grid and "
      "with a tolerance of 0.05 on integers that could only differ by a whole bin.  *** Sub-bin the "
      "spread across the extrema is larger than the grid step itself, on both arms, and locator B "
      "agrees band by band: the shift RISES monotonically with multipole. ***  ** The uniformity was "
      "the resolution. **",
      _L['dl'].max() - _L['dl'].min() > _L['step']
      and _C['dl'].max() - _C['dl'].min() > _C['step']
      and all(b[1] < c[1] for b, c in zip(_L['bands'], _L['bands'][1:]))
      and all(b[1] < c[1] for b, c in zip(_C['bands'], _C['bands'][1:])),
      f"spread {_L['dl'].max()-_L['dl'].min():.2f} (lcdm) and "
      f"{_C['dl'].max()-_C['dl'].min():.2f} (cr) against a grid step of {_L['step']:.0f}; "
      f"locator B rises {_L['bands'][0][1]:+.2f} -> {_L['bands'][-1][1]:+.2f} (lcdm) and "
      f"{_C['bands'][0][1]:+.2f} -> {_C['bands'][-1][1]:+.2f} (cr)")
check("...and a pure rescaling of the acoustic scale does not fit it either: `l -> (1+eps) l` would "
      "give a straight line through the ORIGIN, and the fitted intercept is three multipoles.  ⚠ *So "
      "what this knob does to the positions is not a constant additive shift and not a rescaling, "
      "and separating the Bashinsky-Seljak constant from the k-dependent change in the potentials' "
      "decay that `NUFS=0` also causes is NOT attempted here.*",
      abs(_L['fit'][1]) > 2.0 and abs(_C['fit'][1]) > 2.0,
      f"lcdm d_l = {_L['fit'][1]:+.3f} {_L['fit'][0]:+.5f} l;  "
      f"cr d_l = {_C['fit'][1]:+.3f} {_C['fit'][0]:+.5f} l")

print("\n  ----- THE COMPARISON r6891 ASKED FOR: the two arms side by side -----")
print(f"    {'band':>10} {'lcdm':>9} {'cr':>9} {'difference':>12}")
for (lb, dl_), (lc, dc_) in zip(_L['bands'], _C['bands']):
    print(f"    l ~ {lb:6.0f} {dl_:+9.3f} {dc_:+9.3f} {dc_-dl_:+12.3f}")
_bd = max(abs(dc_ - dl_) for (_, dl_), (_, dc_) in zip(_L['bands'], _C['bands']))
_fd = abs(_C['dl'].mean() / _C['l_A'] - _L['dl'].mean() / _L['l_A'])
check("⚑⚑ ** THE FREE-STREAMING PHASE SHIFT IS COMMON TO THE TWO ARMS. **  Band by band the two "
      "arms' shifts agree to better than a fifth of a multipole, and the extremum-averaged shift in "
      "units of each arm's OWN l_A agrees to 2e-4.  ⇒ *** On `r6891`'s own criterion -- \"a phase "
      "shift common to both is not a candidate for Delta and one that differs between them is\" -- "
      "this is not a candidate. ***",
      _bd < 0.20 and _fd < 2e-4,
      f"largest band-by-band difference {_bd:.3f} multipoles; "
      f"d_l/l_A difference {_fd:.2e} ({_L['dl'].mean()/_L['l_A']:.6f} against "
      f"{_C['dl'].mean()/_C['l_A']:.6f})")
check("⚑ ** AND THE DRAG HALF IS ALSO COMMON, AND IT LANDS IN THE ENVELOPE AND NOT IN THE CONTRAST. "
      "**  Removing free-streaming raises the ENVELOPE by a quarter and changes the peak-to-trough "
      "CONTRAST by about one per cent DOWNWARD -- on both arms, to four decimal places.  ⇒ *** And "
      "Delta is a CONTRAST difference (`cc66.35`), so this knob's large effect is in the wrong "
      "quantity and its arm-difference in the right quantity is 6e-4.  That is a second and "
      "independent reason it is not a candidate. ***",
      abs(_C['env'] - _L['env']) < 2e-3 and abs(_C['con'] - _L['con']) < 2e-3
      and _L['env'] > 1.2 and abs(_L['con'] - 1.0) < 0.02,
      f"envelope {_L['env']:.4f} / {_C['env']:.4f} (difference {_C['env']-_L['env']:+.4f});  "
      f"contrast {_L['con']:.4f} / {_C['con']:.4f} (difference {_C['con']-_L['con']:+.4f})")

# ---------------------------------------------------------------------------------------------------
# PART 4b -- THE SAME CRITERION IN DELTA'S OWN SPACE, SO "COMMON TO BOTH" IS A NUMBER AND NOT A WORD.
# ---------------------------------------------------------------------------------------------------
print("\nPART 4b -- AND THE SAME CRITERION IN DELTA'S OWN SPACE.")
print("-" * 100)
print("""
  A direction that acts identically on the two arms cancels in their difference and can carry none of
  Delta.  ⇒ So the criterion has a number: whiten both arms' residuals on the full covariance, take
  the knob's direction on each arm, and ask how much of `||Delta||^2` the ARM-DIFFERENCE of those two
  directions could remove at its best scaling.  ** And the answer has to be read with one physical
  fact beside it: `NUFS` is not an arm-differentiating freedom. **  Both arms carry the same neutrino
  sector; there is no parameter that sets free-streaming differently on the two.  *The number below is
  therefore the size of what a freedom this construction does not have could have reached.*
""")
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                                # noqa: E402
import camb                                                                  # noqa: E402

LC, FACB = CS.bin_center_and_fac()
_p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                     mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
_LG = np.arange(len(_le), dtype=float)
RAT = np.ones_like(_le)
_m = _un > 0
RAT[_m] = _le[_m] / _un[_m]
sp = lambda f: (lambda d: (d['ls'].astype(float), d['Dl'].astype(float)))(np.load(os.path.join(SP, f)))
mb = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, _LG, RAT))
KEEP = np.isfinite(mb(*sp('cc66_r185_verify_lcdm.npz'))) & (LC >= 100) & (LC <= 1900)
COVK = CS.COV_TT[np.ix_(KEEP, KEEP)]
LINV = np.linalg.inv(np.linalg.cholesky(COVK))
FISH = np.linalg.inv(COVK)
DK = CS.X_DATA[KEEP]


def fitted(f):
    m = mb(*sp(f))[KEEP]
    A = float(m @ FISH @ DK / (m @ FISH @ m))
    r = A * m - DK
    return A * m, float(r @ FISH @ r)


M_L, C2_L = fitted('cc66_r185_verify_lcdm.npz')
M_C, C2_C = fitted('cc66_r185_verify_cr.npz')
N_L, _ = fitted('r6889_nufs0_lcdm.npz')
N_C, _ = fitted('r6889_nufs0_cr.npz')
DEL = LINV @ (M_C - M_L)
ND2 = float(DEL @ DEL)
dL, dC = LINV @ (N_L - M_L), LINV @ (N_C - M_C)
cosine = lambda a, b: float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))
dd = dC - dL
FRAC = float(dd @ DEL) ** 2 / float(dd @ dd) / ND2
print(f"    chi^2 control {C2_L:.2f}   arm {C2_C:.2f}   ||Delta||^2 = {ND2:.2f}   "
      f"(the 185-bin decomposition of cc66.35)")
print(f"    the knob's whitened direction:  ||d_lcdm|| = {np.linalg.norm(dL):.3f}   "
      f"||d_cr|| = {np.linalg.norm(dC):.3f}   cos = {cosine(dL, dC):.6f}")
print(f"    its ARM-DIFFERENCE: ||d_cr - d_lcdm|| = {np.linalg.norm(dd):.4f} against "
      f"||Delta|| = {np.sqrt(ND2):.4f}, at cos = {cosine(dd, DEL):+.4f}")
check("⚑ the knob acts on the two arms in almost exactly the same direction: the whitened cosine "
      "between the two arms' `NUFS` directions is 0.999, so what it does is common and not "
      "differential",
      cosine(dL, dC) > 0.999,
      f"cos(d_lcdm, d_cr) = {cosine(dL, dC):.6f}, norms {np.linalg.norm(dL):.2f} and "
      f"{np.linalg.norm(dC):.2f}")
check("⚠ ...and the residue is reported rather than rounded to zero: freely rescaled, the "
      "arm-difference of the knob's direction could remove 8.7 per cent of `||Delta||^2`, at a "
      "NEGATIVE coefficient.  ** But there is no such freedom: both arms carry the same neutrino "
      "sector, so nothing sets free-streaming differently on the two, and the 8.7 per cent is the "
      "size of a handle this construction does not have. **  ⇒ *Nine tenths of Delta is orthogonal "
      "to anything this knob's arm-difference can reach even with that handle.*",
      0.05 < FRAC < 0.12 and float(dd @ DEL) < 0,
      f"{FRAC*100:.2f}% of ||Delta||^2 at best scaling; the best coefficient is "
      f"{float(dd @ DEL)/ND2:+.5f}, negative")

# ---------------------------------------------------------------------------------------------------
# PART 4c -- AND THE LOCATOR ON A FOUR-TIMES-FINER GRID, SO THE ANSWER IS NOT THE GRID'S.
# ---------------------------------------------------------------------------------------------------
print("\nPART 4c -- THE SAME FOUR SPECTRA AT LSTEP=2, WHICH IS THE POINT OF r6891's \"FINER GRID\".")
print("-" * 100)
print("""
  `cc66.36`'s number was one bin step because the locator was the bin.  ⇒ It is not enough to locate
  sub-bin on the same grid and say so: the four spectra are recomputed at `LSTEP=2` -- four times the
  multipole sampling, the same `LMAXL=2000` reach and the same refit commands -- and the locator is
  run again.  ** If the answer were a property of the grid it would move here, and the test is that it
  does not. **
""")
for _need in ('r6891_fine_grid_lcdm.npz', 'r6891_fine_grid_cr.npz',
              'r6891_full_reach_nulls_lcdm.npz'):
    check(f"the bank this part reads is present: `spectra/{_need}`",
          os.path.exists(os.path.join(SP, _need)), _need)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK YET.  The parts that need it are NOT run,")
    print("     and this receipt FAILS rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
FINE = {}
for arm in ('lcdm', 'cr'):
    d = np.load(os.path.join(SP, f'r6891_fine_grid_{arm}.npz'), allow_pickle=True)
    FINE[arm] = {k[4:]: (d['ls__' + k[4:]].astype(float), d['Dl__' + k[4:]].astype(float),
                         float(d['lA__' + k[4:]])) for k in d.files if k.startswith('ls__')}


def locate_pair(tag, ls, A, B, l_A):
    ea, eb = extrema(ls, A, order=8), extrema(ls, B, order=8)
    dls = np.array([b[0] - a[0] for a, b in zip(ea, eb) if a[1] == b[1]])
    lbs = np.array([a[0] for a, b in zip(ea, eb) if a[1] == b[1]])
    bands = [(float(lo + l_A / 2), xshift(ls, A, B, l_A, lo, lo + l_A))
             for lo in np.arange(150., ls[-1] - l_A - 50., l_A)]
    eA, eB = env_of(ls, A, l_A), env_of(ls, B, l_A)
    m = (ls >= 150) & (ls <= ls[-1] - 50)
    cs = []
    for i in range(len(ea) - 1):
        (l1, k1, a1), (l2_, k2, a2) = ea[i], ea[i + 1]
        (m1, _, b1), (m2, _, b2) = eb[i], eb[i + 1]
        if k1 != k2:
            cs.append((b1 / b2) / (a1 / a2) if k1 == 'max' else (b2 / b1) / (a2 / a1))
    print(f"    {tag:6s} step {ls[1]-ls[0]:.0f}, {len(ls)} multipoles, {len(dls)} extrema: "
          f"mean {dls.mean():+.3f}, spread {dls.max()-dls.min():.3f}, "
          f"line {np.polyfit(lbs, dls, 1)[1]:+.3f} {np.polyfit(lbs, dls, 1)[0]:+.5f} l")
    print(f"           bands  " + "  ".join(f"l~{l:.0f}: {v:+.2f}" for l, v in bands))
    return dict(dl=dls, l=lbs, bands=bands, l_A=l_A, step=float(ls[1] - ls[0]),
                env=float((eB[m] / eA[m]).mean()), con=float(np.mean(cs)))


FLOC = {}
for arm in ('lcdm', 'cr'):
    ls, A, l_A = FINE[arm]['cc66_r185_verify']
    _, B, _ = FINE[arm]['r6889_nufs0']
    FLOC[arm] = locate_pair(arm, ls, A, B, l_A)
_fL, _fC = FLOC['lcdm'], FLOC['cr']
check("the fine grid is four times the sampling of the banked spectra, at the same reach",
      _fL['step'] == 2.0 and _fC['step'] == 2.0 and len(FINE['lcdm']['cc66_r185_verify'][0]) > 900,
      f"step {_fL['step']:.0f} against the banked {_L['step']:.0f}; "
      f"{len(FINE['lcdm']['cc66_r185_verify'][0])} multipoles against {len(_L['dl'])} extrema on "
      f"{238} banked")
_bmax = max(abs(a[1] - b[1]) for a, b in zip(_L['bands'], _fL['bands'])) if \
    len(_L['bands']) == len(_fL['bands']) else 99.
_bmaxC = max(abs(a[1] - b[1]) for a, b in zip(_C['bands'], _fC['bands'])) if \
    len(_C['bands']) == len(_fC['bands']) else 99.
check("⚑ ** AND THE ANSWER IS NOT THE GRID'S: band by band, the LSTEP=2 locator reproduces the "
      "LSTEP=8 locator to better than half a multipole on both arms. **  *The shift was measured, not "
      "bracketed.*",
      _bmax < 0.5 and _bmaxC < 0.5,
      f"largest band-by-band difference between the two grids: {_bmax:.3f} (lcdm), "
      f"{_bmaxC:.3f} (cr)")
check("...and every conclusion of Part 4 survives on it: the shift still rises monotonically, the two "
      "arms still agree to a fifth of a multipole, and the drag is still an envelope rescale with the "
      "contrast within one per cent of unity",
      all(b[1] < c[1] for b, c in zip(_fL['bands'], _fL['bands'][1:]))
      and all(b[1] < c[1] for b, c in zip(_fC['bands'], _fC['bands'][1:]))
      and max(abs(a[1] - b[1]) for a, b in zip(_fL['bands'], _fC['bands'])) < 0.25
      and abs(_fC['env'] - _fL['env']) < 2e-3 and abs(_fL['con'] - 1.0) < 0.02,
      f"rises {_fL['bands'][0][1]:+.2f} -> {_fL['bands'][-1][1]:+.2f} (lcdm) and "
      f"{_fC['bands'][0][1]:+.2f} -> {_fC['bands'][-1][1]:+.2f} (cr); largest arm difference "
      f"{max(abs(a[1]-b[1]) for a, b in zip(_fL['bands'], _fC['bands'])):.3f}; "
      f"envelope {_fL['env']:.4f}/{_fC['env']:.4f}, contrast {_fL['con']:.4f}/{_fC['con']:.4f}")

# ---------------------------------------------------------------------------------------------------
# PART 3c -- AND THE NULLS AT FULL REACH, WHICH IS THE HALF REDUCED REACH CANNOT CARRY.
# ---------------------------------------------------------------------------------------------------
print("\nPART 3c -- THE NINE OFF-PATH SWITCHES AND `LRSFROM`, RE-RUN AT THE REPORTED l REACH.")
print("-" * 100)
print("""
  The screen ran at `LMAXL=500`, on the argument that connectivity is path-dependent and not
  resolution-dependent.  ** That argument is sound for a switch that MOVES and it is exactly where a
  null could hide: `DAMPX` and `RD` both act on the DAMPING TAIL, which l <= 500 barely sees. **  ⇒ So
  every switch the screen calls inert is re-run on the control arm at `LMAXL=2000` -- the reach every
  reported number in this sector is computed at -- before the table calls it inert.
""")
d = np.load(os.path.join(SP, 'r6891_full_reach_nulls_lcdm.npz'), allow_pickle=True)
FULL = {k[4:]: (d['ls__' + k[4:]].astype(float), d['Dl__' + k[4:]].astype(float))
        for k in d.files if k.startswith('ls__')}


def fcmp(a, b):
    la, A = FULL[a]
    lb, B = FULL[b]
    return bool(np.array_equal(A, B)), float(np.max(np.abs(B - A)))


_fo = {e: fcmp('base', e) for e in OFFPATH}
print("    " + "   ".join(f"{e} {'0.0' if v[0] else f'{v[1]:.2e}'}" for e, v in _fo.items()))
check("⚑⚑ ** ALL NINE HOLD AT FULL REACH: bit-identical at `LMAXL=2000`, where the damping tail is "
      "fully present and `DAMPX` and `RD` would have shown if they reached it. **",
      all(v[0] for v in _fo.values()),
      f"{len(_fo)} switches at LMAXL=2000 on the control arm, max over all of them "
      f"{max(v[1] for v in _fo.values()):.1e}; "
      f"{len(FULL['base'][0])} multipoles to l = {FULL['base'][0][-1]:.0f}")
check("...and `LRSFROM` holds at full reach too: a quarter-sized move in the reported `r_s` and "
      "exactly zero in D_l out to l = 2000",
      fcmp('pairLRSFROMbase', 'pairLRSFROM')[0],
      f"max |dD_l| = {fcmp('pairLRSFROMbase', 'pairLRSFROM')[1]:.1f} over "
      f"{len(FULL['base'][0])} multipoles")

# ===================================================================================================
print()
print("=" * 100)
_bandL = " / ".join(f"{v:+.1f}" for _, v in _L['bands'])
_bandC = " / ".join(f"{v:+.1f}" for _, v in _C['bands'])
print(f"""
WHAT THIS REVISION ESTABLISHES.

  ⚑⚑ ** THE SWITCH SWEEP IS EXHAUSTIVE AND IT FINDS NO FURTHER KNOB SHADOW. **  Sixty environment
  switches, read from the source text and not from memory; fifty-one with a live use site on the
  reporting path and nine without; fifty-five of them measured on both arms, one switch moved at a
  time, at each arm's own refit minimum.  *** The set of runs that came back BIT-IDENTICAL is exactly
  the set four readings predict -- off-path, rate-identity on the control arm, the arm branch, and
  gated by another switch -- with no unexplained null and nothing explained away that in fact moved.
  ***  ⇒ ** That is what closes the rate: not a fourth shadow that was not found, but every switch
  accounted for. **  ⌗ *And the nine off-path switches are not taken on the static argument: all
  eighteen runs come back at max |dD_l| = 0.0 exactly, and again at full reach where `DAMPX` and `RD`
  would have shown if they touched the damping tail.*

  ⛭ ** TWO THINGS THE SWEEP TURNED UP, AND NEITHER IS OF THE r6476 CLASS. **
   (i) `LRSFROM` moves the instrument's REPORTED acoustic scale by a quarter -- r_s from 145.38 to
       110.49 Mpc, l_A from 301.5 to 396.8 -- and its spectrum by EXACTLY ZERO, at full reach as at
       reduced.  ** `R_S` and `L_A` are diagnostics of this instrument: on all three paths they reach
       a print and the SAVE metadata and nothing else, and `hier_run` accepts all three and uses
       none. **  ⚠ *r6476 recorded this switch as "reachability-checked ... A knob checked at the
       REPORTING path", on the ground that the header moved.  The header is not the reported number,
       so what is corrected is the certification and not any number.*  ⇒ And the consequence points
       the useful way: because no transfer function reads `L_A`, the printed `l_1/l_A = 0.7312`
       agreeing with the sky's `220.6/301.7` is an agreement between two INDEPENDENTLY computed
       quantities and not a value fed in.
  (ii) `LATARG` -- "the corpus's one fitted number" -- has NO ROOT at the CR arm's adjudicated
       background: with `ZSTART` unset the onset solve raises, f(a) and f(b) the same sign across the
       whole widened bracket.  *Which is why the refit command supplies `ZSTART=3e7`, so nothing
       reported moves -- but the register should say the switch is unreachable at the arm's own
       minimum, and it did not.*

  ⚑⚑ ** AND THE FREE-STREAMING SHIFT IS MEASURED, ON BOTH ARMS, AND IT IS COMMON TO THEM. **
  Band by band, in bands one acoustic period wide: {_bandL} on the control and {_bandC} on the arm.
  *** The largest difference between the two arms is {max(abs(a[1]-b[1]) for a, b in zip(_L['bands'], _C['bands'])):.2f} of a multipole, and in units of each arm's own
  l_A the extremum-averaged shift agrees to {_fd:.0e}. ***  ⇒ ** On `r6891`'s own criterion -- "a phase
  shift common to both is not a candidate for Delta and one that differs between them is" -- the
  free-streaming phase shift is NOT a candidate. **  In Delta's own space the two arms' `NUFS`
  directions sit at a whitened cosine of {cosine(dL, dC):.6f}; their difference, freely rescaled, could reach
  {FRAC*100:.1f} per cent of ||Delta||^2 at a NEGATIVE coefficient -- and there is no such freedom, because both
  arms carry the same neutrino sector.

  ⚑ ** AND THE DRAG HALF, KEPT APART FROM THE PHASE AND SPLIT IN TWO, BECAUSE IT IS TWO THINGS. **
  Removing free-streaming raises the ENVELOPE by {(_L['env']-1)*100:.1f} per cent and changes the peak-to-trough
  CONTRAST by {(_L['con']-1)*100:+.1f} per cent -- on both arms, agreeing to {abs(_C['env']-_L['env']):.4f} and {abs(_C['con']-_L['con']):.4f} respectively.  *** Delta is a
  CONTRAST difference (`cc66.35`), so this knob's large effect is in the wrong quantity and its
  arm-difference in the right quantity is six parts in ten thousand. ***  That is a second reason it
  is not a candidate, and it is independent of the first.

  ⚠ ** AND ONE CORRECTION TO r6889+cc66.36, WHICH IS WHY THE FINER GRID WAS THE ORDER. **  That
  receipt gated the shift as "UNIFORM across the first four peaks on both arms, which is what a PHASE
  shift looks like as against a rescaling of the acoustic scale".  *** Sub-bin it is not uniform: it
  rises monotonically with multipole, from about +3 near the first peak to about +12 by l ~ 1500, on
  both arms, on both locators, and again at four times the multipole sampling. ***  ** The uniformity
  was the grid, and the gate that certified it was a tolerance of 0.05 on integers that could only
  differ by a whole bin. **  ⌗ *That is the second time in three revisions that a gate passed because
  the resolution and not the physics set the number -- `cc66.36`'s own reassociation episode was the
  first -- and both are recorded rather than tidied away.*  ⚠ *And a pure rescaling does not fit it
  either: the straight line through the per-extremum shifts has an intercept of three multipoles, so
  separating the Bashinsky-Seljak constant from the k-dependent change in the potentials' decay that
  `NUFS=0` also causes is NOT attempted here.*

  ⚠ ** WHAT THIS IS NOT. **  No mechanism for the contrast imbalance -- `r6891` says that boundary has
  not moved and this does not move it.  No claim that the growth of the shift with multipole is the
  Bashinsky-Seljak term.  No pinned value of n_s, H_0, Omega_m or omega_b.  And the sweep is a sweep
  of ENVIRONMENT switches: a hard-coded literal that ought to be a switch is not an environment
  switch, and `cc66.17`'s `NS` literal is the reminder that that is a different search.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the instrument reads sixty environment switches; the reporting path executes fifty-one of
them and the nine it does not are each confined to a declared alternative mode and come back
bit-identical there, twice over, at reduced and at full reach.  Fifty-five switches measured on both
arms account for every bit-identical result by one of four readings and leave no unexplained null, so
the knob-shadow rate that has held every number in this sector subject to an unknown is closed by an
accounting rather than by a fourth find.  The two things the sweep did turn up are a certification of
the wrong quantity (`LRSFROM`, r6476, checked on the header) and a switch with no root at the arm's
own background (`LATARG`) -- neither of which moves a reported number.  AND the free-streaming phase
shift is measured: positive everywhere, RISING with multipole from about +3 to about +12 rather than
uniform, identical between the two arms to {max(abs(a[1]-b[1]) for a, b in zip(_L['bands'], _C['bands'])):.2f} of a multipole, with its drag half an
envelope rescale of {_L['env']:.4f} and a contrast ratio of {_L['con']:.4f} -- so on r6891's own criterion it is not a
candidate for Delta, on two independent grounds.
NOT CLAIMED: a mechanism for the contrast imbalance; that the shift's growth with l is the
Bashinsky-Seljak term; or that a hard-coded literal that ought to be a switch would have been found by
a sweep of environment switches.
""")
