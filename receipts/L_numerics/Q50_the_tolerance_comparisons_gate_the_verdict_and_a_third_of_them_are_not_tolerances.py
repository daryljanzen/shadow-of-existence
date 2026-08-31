#!/usr/bin/env python3
r"""Q50 -- `Q5` CLOSED: THE CORPUS'S TOLERANCE COMPARISONS DO GATE ITS VERDICTS, AND THE QUESTION
     `Q5` ASKED HAD A FALSE PRESUPPOSITION.

** WHAT `Q5` LEFT OPEN, at r3616, in `NUMERICAL_ANALYSIS_LEDGER.md`: **

  > *"whether 688 `abs(...) < tol` assertions carry meaningful tolerances.  **That needs a mutation
  > harness, not a reading**, and building one is a larger instrument than a field bake should ship.
  > Recorded with the shape of the check it wants: mutate the asserted quantity by the tolerance and
  > require the assertion to fail."*

** THE HARNESS IS `scripts/tolerance_audit.py` AND IT DOES THREE AST REWRITES OF EVERY `abs(E) < T`
   SITE, EACH RUN FROM THE RECEIPT'S OWN DIRECTORY: **
  * ** MARGIN ** -- semantics-preserving; records $\lvert E\rvert/T$ at every site the run reaches.
  * ** MUTATE-UP ** -- `abs(E + 3T) < T`; the comparison goes False.  Catches the ASSERT shape.
  * ** MUTATE-DOWN ** -- `abs(E)*0 < T`; the comparison goes True.  Catches the GUARD shape, where
    the FAILURE lives on the `<` branch and an upward kick can only silence it.

*** THE ANSWER, over 269 receipt files carrying 1116 static sites. ***

  * ** FAITHFULNESS FIRST: the margin transform reproduces the baseline verdict on 269 of 269
    files. **  *Not a claim about synthetic controls -- the whole population, run twice.*
  * ** 245 files pass at baseline.  243 of them (99.2%) have at least one tolerance comparison that
    GATES THE EXIT: kick it and the receipt fails. **
  * ** The two that do not are both correct. **  *`P14_lambda_spectrum`'s `abs(lv) <= 4` is a
    DISPLAY FILTER choosing which rows to print; `L562/P1` skips with a printed reason -- its banked
    run logs are not on this tree -- and names `L-830` as the gated self-contained substitute.*
  ⇒ *** So `Q5` closes the way `Q1` did: as a CONFIRMATION.  The corpus's tolerance comparisons can
      fail, and this is the first time anything has shown that rather than assumed it. ***

⛔⛭⛭ *** AND THE MEASUREMENT REFUTES THE QUESTION'S PREMISE, which is worth more than the number. ***
  *`Q5` asked whether the tolerances are "loose enough to pass anything" -- a question that
  presupposes every `abs(E) < T` is an ACCURACY ASSERTION.  Measured over the 918 sites that
  actually execute, they are not one kind of thing:*

  |   $\lvert E\rvert/T$   |  sites  |  what that band is  |
  |---|---|---|
  | exactly 0        | 210 (22.9%) | ** EXACTNESS ** -- integer or symbolic arithmetic; the tolerance is a formality |
  | up to 1e-6       |  82 ( 8.9%) | ulp-level residue of an identity that is exact in $\mathbb{R}$ |
  | 1e-6 .. 0.1      | 422 (46.0%) | ** ACCURACY ** -- a real numerical claim with headroom |
  | 0.1 .. 1         | 150 (16.3%) | ** ACCURACY, LOAD-BEARING ** -- within one order of its own tolerance |
  | at or over 1     |  54 ( 5.9%) | ** PREDICATES ** -- `if abs(fv)<1e-12: "NULL" else "spacelike"`, degeneracy guards, real-root counters.  *Being OVER the tolerance is the informative outcome* |

  ⇒ ** A single "are the tolerances meaningful" verdict over 1116 sites would have been meaningless,
    because a third of them are not measuring accuracy at all.  Two of the five bands are working
    exactly as intended by being nowhere near their tolerance. **

⛔⛭⛭ *** THE HARNESS'S FIRST PASS REPORTED FOUR DEFECTS AND ALL FOUR WERE ITS OWN BLIND SPOTS. ***
  *Up-mutation alone left four files exiting 0.  **Read one at a time instead of counted:**
  `L265`'s `abs(lv) < 3/4` is a threshold predicate on an INTEGER parameter; `P14_lambda_spectrum`'s
  is a display filter; and `P15_which_coupling`'s two are GUARDS whose failure branch is the `<`
  side, which an upward kick can only silence.*
  ** A one-sided mutation cannot test a two-sided guard, and `abs(E) < T` is not always a tolerance.
  Publishing the four as corpus defects would have been the instrument reporting its own limits as
  the corpus's. **  ⇒ *The down-kick was built from those four, and it recovers two of them.*

⌗ ** AND THE HARNESS BROKE THE FILES IT WAS MEASURING, ONCE. **  *The margin preamble was first
prepended as TEXT, which displaced each module's docstring and set `__doc__` to `None`; eleven
receipts that print and split their own docstring died with `AttributeError`, and the harness
reported that as THEIR result.*  ** The baseline mode exists because of it: a verdict about a
mutated run is worth nothing without the un-mutated one beside it. **

** WHAT THIS RECEIPT ASSERTS, AND WHAT IT ONLY RECORDS. **
  *The full-population run is twenty minutes over four modes and cannot live inside a 300-second
  receipt.  **Its numbers are PRINTED as a record with the command that reproduces them.**  What is
  ASSERTED here is the harness's five controls, and the four invariants re-measured live on a
  ten-file subset chosen to contain every verdict class -- up-only, down-only, both, and neither.*
  ⌗ *§4 of the work order: if a line is a record, print it.*

COMPUTES: scope.
  * `SUBSET` -- ten receipts, one per verdict class, re-run live in all four modes.
  * `POP` -- the full-population figures, RECORDED not asserted:
    269 files / 1116 static sites / 245 baseline-passing / 243 gated / 918 executed sites.
    Reproduce: `python3 scripts/tolerance_audit.py --mode {baseline,margin,mutate,mutate-down}`
  * `MIN_SITES`, `MIN_FILES` are FLOORS, not pins -- the corpus grows and a receipt that fails
    whenever a receipt is added is a nuisance rather than a gate.
  * ** NOT CLAIMED: that any particular tolerance is the right one. **  *This measures whether a
    comparison gates the verdict and how much room it has, not whether its author chose well.*

Written r3714 by node 60, numerical-analysis v2 pass, probe `Q50`, closing `Q5`.
"""
import ast
import collections
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import tolerance_audit as TA                                            # noqa: E402

MIN_SITES, MIN_FILES = 1000, 250

POP = dict(files=269, static_sites=1116, baseline_pass=245, gated=243, ungated=2,
           executed_sites=918, margin_agrees=269,
           bands={'exactly 0': 210, 'up to 1e-6': 82, '1e-6 .. 0.1': 422,
                  '0.1 .. 1': 150, 'at or over 1': 54})

SUBSET = [
    ('P09_range_paper/V1_carter_chain.py', 'up'),
    ('P15_CR_cosmology/P15_which_coupling_carries_the_k_dependence.py', 'down'),
    ('P03_SdS_slicing/D2_hexagon_klein.py', 'both'),
    ('P03_SdS_slicing/alpha_alone.py', 'both'),
    ('P14_matter_sector_paper/P14_the_two_threes_are_not_related_as_covers.py', 'both'),
    ('P15_CR_cosmology/C40_the_pair_was_quoted_against_a_rounding.py', 'up'),
    ('P07_CR_framework/two_realisations.py', 'up'),
    ('P17_geometric_core_paper/P17_power_is_null.py', 'up'),
    ('P16_cosmogenesis_paper/P16_peak_temperature.py', 'up'),
    ('L562_the_pin_test/P1_the_pin_test_run_the_spacing_follows_the_pin_so_the_ratio_does_not.py',
     'neither'),
]

FAILS = []


def check(name, cond):
    ok = bool(cond)
    print(f"    [{'ok ' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def static_census():
    """count every `abs(E) < T` site by source shape, without running anything"""
    shapes, files, total = collections.Counter(), set(), 0
    for dp, _, fns in os.walk(os.path.join(ROOT, 'receipts')):
        for fn in sorted(fns):
            if not fn.endswith('.py') or fn.startswith('_tolaudit_'):
                continue
            p = os.path.join(dp, fn)
            try:
                tree = ast.parse(open(p, encoding='utf-8', errors='replace').read())
            except SyntaxError:
                continue
            for n in ast.walk(tree):
                if (isinstance(n, ast.Compare) and len(n.ops) == 1
                        and isinstance(n.ops[0], (ast.Lt, ast.LtE))
                        and isinstance(n.left, ast.Call)
                        and getattr(n.left.func, 'id', '') == 'abs' and len(n.left.args) == 1):
                    inner = n.left.args[0]
                    kind = ('abs(A-B)' if isinstance(inner, ast.BinOp)
                            and isinstance(inner.op, ast.Sub) else 'abs(X)')
                    rhs = 'literal' if isinstance(n.comparators[0], ast.Constant) else 'expr'
                    shapes[f'{kind} < {rhs}'] += 1
                    files.add(p)
                    total += 1
    return total, len(files), shapes


if __name__ == '__main__':
    print(__doc__)
    print('=' * 96)
    print('(A) THE HARNESS\'S OWN FIVE CONTROLS — run live, not quoted')
    print('=' * 96)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'tolerance_audit.py'),
                        '--selftest'], capture_output=True, text=True, timeout=180)
    print('    ' + '\n    '.join(r.stdout.strip().split('\n')[2:]))
    check('the five controls behave (assert / guard / unenforced / ulp / zero)', r.returncode == 0)

    print()
    print('=' * 96)
    print('(B) THE STATIC CENSUS — every `abs(E) < T` site in receipts/, by shape')
    print('=' * 96)
    total, nfiles, shapes = static_census()
    for k, v in shapes.most_common():
        print(f'    {k:<24} {v:>6}')
    print(f'    {"TOTAL":<24} {total:>6}   in {nfiles} files')
    check(f'at least {MIN_SITES} sites in at least {MIN_FILES} files  -> {total} in {nfiles}',
          total >= MIN_SITES and nfiles >= MIN_FILES)
    dom = shapes['abs(A-B) < literal'] / total
    check(f'`abs(A-B) < literal` is the dominant shape  -> {100*dom:.1f}%', dom > 0.6)

    print()
    print('=' * 96)
    print('(C) THE FOUR INVARIANTS, RE-MEASURED LIVE on a subset holding every verdict class')
    print('=' * 96)
    TA.sweep_debris(verbose=False)
    marg = os.path.join(TA.tempfile.gettempdir(), 'q50_margins.jsonl')
    open(marg, 'w').close()
    print(f"    {'receipt':<62} {'base':>6} {'marg':>6} {'up':>8} {'down':>8}")
    got = {}
    for rel, want in SUBSET:
        p = os.path.join(ROOT, 'receipts', rel)
        v = {m: TA.run_one(p, m, 240, marg)['verdict']
             for m in ('baseline', 'margin', 'mutate', 'mutate-down')}
        got[rel] = v
        print(f'    {rel.split("/")[-1][:60]:<62} {v["baseline"]:>6} {v["margin"]:>6} '
              f'{v["mutate"]:>8} {v["mutate-down"]:>8}')
    TA.sweep_debris(verbose=False)

    print()
    check('INVARIANT 1 — the margin transform is faithful: it reproduces every baseline verdict',
          all(v['margin'] == v['baseline'] for v in got.values()))
    check('INVARIANT 2 — every subset receipt passes at baseline',
          all(v['baseline'] == 'EXIT0' for v in got.values()))
    gated = {k: (v['mutate'] == 'NONZERO' or v['mutate-down'] == 'NONZERO')
             for k, v in got.items()}
    want_gated = {k for k, w in SUBSET if w != 'neither'}
    check('INVARIANT 3 — every receipt but the documented skip is GATED by a tolerance comparison',
          {k for k, g in gated.items() if g} == want_gated)

    dnly = 'P15_CR_cosmology/P15_which_coupling_carries_the_k_dependence.py'
    check('INVARIANT 4 — the GUARD-shaped receipt is caught by the DOWN kick and NOT by the UP one '
          '(delete mutate-down and this fires)',
          got[dnly]['mutate-down'] == 'NONZERO' and got[dnly]['mutate'] == 'EXIT0')

    print()
    print('=' * 96)
    print('(D) THE FULL-POPULATION RUN — A RECORD, NOT AN ASSERTION')
    print('=' * 96)
    print('    Reproduce with, in order:')
    print('      python3 scripts/tolerance_audit.py --mode baseline    --jobs 6 --timeout 180')
    print('      python3 scripts/tolerance_audit.py --mode margin      --jobs 6 --timeout 180')
    print('      python3 scripts/tolerance_audit.py --mode mutate      --jobs 6 --timeout 180')
    print('      python3 scripts/tolerance_audit.py --mode mutate-down --jobs 6 --timeout 180')
    print()
    for k, v in POP.items():
        if k != 'bands':
            print(f'      {k:<18} {v}')
    print()
    for k, v in POP['bands'].items():
        print(f'      |E|/T {k:<14} {v:>5}  ({100*v/POP["executed_sites"]:5.1f}% of executed)')
    print()
    print('    ⇒ 243 of 245 gated is 99.2%.  The two exceptions are a display filter and a')
    print('      documented data-dependent skip that names its gated substitute.')
    print('    ⇒ 210 sites sit at EXACTLY zero and 54 sit at or OVER their tolerance: neither')
    print('      band is measuring accuracy, and both are working as intended.')

    print()
    print('=' * 96)
    if FAILS:
        print(f'  {len(FAILS)} FAILED: ' + '; '.join(FAILS))
        raise SystemExit(1)
    print('  ALL PASS')
