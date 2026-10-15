#!/usr/bin/env python3
"""S49 -- `r7341` ①'s ORDERED REPAIR, AND THE CLASS IT BELONGS TO MEASURED OVER THE WHOLE BLOCK.
The order says `L165/S10` NAMES NO METRIC.  *** It names a different one, and that is a sharper
defect: a reader who supplied nothing would have had nothing to check, while a reader who took the
receipt at its word got a contradiction -- which is exactly what happened. ***

** WHAT WAS ORDERED. **  `r7341` ①: *`S10` asserts `C^2 = sigma^2(4 + 16 sigma^2/3)` and names no
metric, so any reader supplies a family and gets a different answer.  The repair is one line, because
`L549/Q1` computes the same polynomial symbolically from a named metric and passes: `S10` names Q1's
family or cites Q1.  Do not re-derive it.*

** ⛔ Ⓐ WHAT WAS ACTUALLY WRONG. **  `S10` named `diag(-2 sigma, sigma, sigma)` with the invariant
`6 sigma^2` -- `71`'s family -- and asserted `Q1`'s polynomial beside it.  Computed below with `Q1`'s
OWN curvature routines, so the polynomial is not re-derived by a second implementation:

      *** Q1's family         (0, sigma, -sigma)   sigma_ab sigma^ab = 2 sigma^2
                              Weyl^2 = 4 sigma^2 (4 sigma^2 + 3)/3 = sigma^2 (4 + 16 sigma^2/3)
          the family NAMED    (-2 sigma, sigma, sigma)  sigma_ab sigma^ab = 6 sigma^2
                              Weyl^2 = 12 sigma^2 (2 sigma - 1)^2 = 12 sigma^2 - 48 sigma^3 + 48 sigma^4 ***

  ⇒⇒ *** `71` DID NOT SUPPLY AN ARBITRARY FAMILY.  IT USED THE ONE `S10` HANDED IT, and the
      `-48 H sigma^3` term it reported as the contradiction is that family's, exactly. ***  The
      contradiction was withdrawn at `r7341` because the polynomial belongs to `Q1`'s family; what is
      added here is that it was CORRECT about the family the receipt named.

** Ⓑ AND THE GUARD THAT COULD NOT CATCH IT WAS THE RECEIPT'S OWN. **  `S10` checked that its triple
is TRACE-FREE.  *** Every traceless triple is, `Q1`'s included, so the condition's truth is invariant
under the very swap that produced the collision: it could not fail. ***  ⌗ *This is the fifth
cannot-fail label this seat has found in this phase, and the first where the label is not merely
uninformative but names the WRONG OBJECT while staying true.*

** Ⓒ THE REPAIR, AND IT IS MEASURED BY MUTATION RATHER THAN DESCRIBED. **  The triple is now
EXTRACTED from `Q1`'s own metric assignment and the polynomial DERIVED from it with `Q1`'s routines,
with the named family computed beside it through the same construction as a control.

      *** before: the family entered NO condition at all -- there was nothing to mutate
          after:  swapping the family back turns 8 of the 9 conditions of ⓵ red ***

  ⌗ ** Naming the right family in the PROSE would have left the count at `0`. **  That is why the
    repair is not the one line the order describes, and the difference is the phase's own thesis.

** Ⓓ THE ARM, SCORED AS REGISTERED. **  Receipts of `r7338`'s block carrying an UNREFERENCED CLOSED
FORM: central `4` of the block's `43` gates, band `2`-`7`, two-sided, decisive `0.124`.

      *** 10 of 43  --  OUTSIDE THE BAND, HIGH ***

  ** The population is the WHOLE block and not the `19` receipts that had owed rows **, because
  `S10`'s two ledger rows are both `DELIBERATE`: the instrument the phase is priced on could never
  have reached this receipt.  ⌗ *Of the `43`: `14` write a closed form by hand; of those `2` DERIVE
  it and `2` TIE it in code.*

** Ⓔ AND THE EXCESS IS THE OVER-INCLUSION THE REGISTRATION DECLARED IN ADVANCE, WHICH IS WHY THE
REFINEMENT IS REGISTERED FOR THE NEXT REVISION AND NOT SCORED HERE. **  The registered arbiter asks
whether the MODULE derives the form; the defect is a property of the CONDITION.  Refined -- a form is
unreferenced when no condition it enters holds any other operand the module DERIVED -- the same `43`
give `7`; adjudicated receipt by receipt, `5`.  *** Registered `10`, refined `7`, adjudicated `5`
against a central of `4`: the arm fails high by three and the three are the declared over-inclusion. ***

** Ⓖ AND THE RETROSPECTIVE SPAN ARM IS READ FAR ENOUGH TO SAY WHY IT IS NOT COUNTED. **  `r7336`
registered it on the `2482` rows whose verdict at `23cecc99` was not `REPAIR-OWED`.  *** Only `41` of
them have left the ledger since, and `33` of the `41` -- `0.80` -- are in receipts THIS SEAT repaired
in the three strides: on this population the outcome is a stride effect. ***  ⛔ ** And the outcome
measure cannot be approximated from the text. **  The instrument extracts a receipt's literals from its
SYNTAX TREE, so a span the receipt carries across source lines is not in its text verbatim: read that
way the population looks `567` stale while the ledger still carries `545` of them.  ⇒ *** That
artefact puts `0.7072` of the set in the longest tercile -- INSIDE the band `0.42`--`1.00` -- so a seat
that approximated the measure would have reported the arm PASSING on an extraction effect. ***

** COMPUTES: ** `Weyl^2` and `sigma_ab sigma^ab` for the two families from their metrics via `Q1`'s
own routines; the mutation counts `0` and `8`; the arm `10` of `43` with its decisive fraction; the
refined `7` and the adjudicated `5`; and the span arm's population `2482`, its `41` departures, the
`33` of them in this seat's own stride, and the artefact's `567`/`545`/`0.7072`.  No paper quantity.

** WHAT IS NOT CLAIMED. **  ** Not that the polynomial is re-derived ** -- `Q1`'s routines compute it,
and the order's instruction not to re-derive is honoured.  ** Not that the other four members are
repaired ** -- they are named with the one line each would need, and the order asked for one receipt.
** Not that the adjudication is an arm ** -- it is this seat's reading of its own mechanical count and
is reported as that.  ** And not that the refined arbiter is sound ** -- it is registered for the next
revision so that it can fail somewhere its author did not already know the answer.

Written r7346 on `r7341` ①.  Stated for reversal.
"""
import ast
import contextlib
import importlib.util
import io
import json as _json
import os
import subprocess

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

#: the pins.  ** Every historical claim is read at the commit it is a claim ABOUT (`r7335` ④), and
#: what the trunk holds LIVE is asserted separately and allowed to be smaller. **
BEFORE = '28edd3c6'             # the pre-repair S10, and the commit the census population is cut at
REG = '1e470a50'                # this revision's registration commit
WORK = '3d97814c'               # this revision's last repair commit
SPAN_PIN = '23cecc99'           # `r7336`'s span experiment cut its population here
S10 = os.path.join('receipts', 'L165_interacting_tower', 'S10_the_halves_meet_at_the_shear.py')
COST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7346_60_the_wrong_referent',
                    'cost.py')


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    print()
    print('  S49 -- the ordered repair was a WRONG referent, and the class measured over the block')
    print()
    s = sp.Symbol('sigma', real=True)
    t = sp.Symbol('t', real=True)
    x = [t] + list(sp.symbols('x y z', real=True))
    s10 = load(os.path.join(ROOT, S10), 'L165_S10')
    q1 = s10.q1_module()

    # ── Ⓐ the two families, each from its own metric, with Q1's own routines ──────────────────────
    gQ, triple = s10.q1_family(t, s)
    C2 = s10.weyl(gQ, q1, x)
    C2o = s10.weyl(s10.bianchi((-2, 1, 1), t, s), q1, x)
    check(f'Ⓐ① `Q1`\'s family is {tuple(sp.sstr(c*s) for c in triple)} with '
          f'$\\sigma_{{ab}}\\sigma^{{ab}}={sp.sstr(sp.simplify(sum((c*s)**2 for c in triple)))}$, and '
          f'ITS $\\mathrm{{Weyl}}^2$ is the polynomial `S10` asserts',
          sp.simplify(sum((c*s)**2 for c in triple) - 2*s**2) == 0
          and sp.simplify(C2 - s**2*(4 + sp.Rational(16, 3)*s**2)) == 0)
    check(f'Ⓐ② and the family `S10` NAMED, diag$(-2\\sigma,\\sigma,\\sigma)$ with $6\\sigma^2$, gives '
          f'${sp.sstr(sp.factor(C2o))}$ instead -- so the polynomial is FALSE on it',
          sp.simplify(sum((c*s)**2 for c in (-2, 1, 1)) - 6*s**2) == 0
          and sp.simplify(C2o - 12*s**2*(2*s - 1)**2) == 0
          and sp.simplify(C2o - s**2*(4 + sp.Rational(16, 3)*s**2)) != 0)
    check('Ⓐ③ ⛭ and it carries `71`\'s reported $-48H\\sigma^3$ exactly, so the contradiction was '
          'CORRECT about the family the receipt named and wrong only about whose family it was',
          sp.expand(C2o).coeff(s, 3) == -48 and sp.expand(C2).coeff(s, 3) == 0)
    check('Ⓐ④ while the reconciliation `r7341` states holds: leading coefficients $4$ and $12$ at '
          '$H=1$, a factor of three, which is the ratio of the two shear invariants',
          sp.simplify(sp.series(C2o, s, 0, 3).removeO()/sp.series(C2, s, 0, 3).removeO()) == 3
          and sp.simplify(sum((c*s)**2 for c in (-2, 1, 1))/sum((c*s)**2 for c in triple)) == 3)

    # ── Ⓑ the guard that could not fail, read on the PRE-REPAIR source ───────────────────────────
    #: ** Asserted rather than described: the old condition's truth is the SAME for both triples. **
    old_src = git('show', f'{BEFORE}:{S10}')
    old_tree = ast.parse(old_src)
    old_conds = [ast.unparse(n.args[1]) for n in ast.walk(old_tree)
                 if isinstance(n, ast.Call) and getattr(n.func, 'id', '') == 'check'
                 and len(n.args) >= 2]
    family_conds = [c for c in old_conds if '-2 * s' in c or '-2*s' in c]
    check(f'Ⓑ① the pre-repair gate had exactly one condition mentioning the triple at all, of its '
          f'{len(old_conds)}, and it is the trace-free one: `{family_conds[0] if family_conds else ""}`',
          len(family_conds) == 1)
    check('Ⓑ② ⛔ and its truth is invariant under the swap that produced the collision -- trace-free '
          'holds for `Q1`\'s triple too -- so the condition COULD NOT FAIL',
          bool(eval(family_conds[0], {'sp': sp}, {'s': s}))
          and sp.simplify(sum(c*s for c in triple)) == 0)
    check('Ⓑ③ and the pre-repair module built no metric and called no curvature routine, so the '
          'polynomial was typed rather than derived',
          not any(getattr(n.func, 'attr', getattr(n.func, 'id', '')) in
                  ('diag', 'Matrix', 'invariants', 'weyl_sq')
                  for n in ast.walk(old_tree) if isinstance(n, ast.Call)))

    # ── Ⓒ the repair, measured by mutation ───────────────────────────────────────────────────────
    #: The mutation is applied to the LIVE module in process: `q1_family` is replaced by the family
    #: the receipt used to name, and `S10`'s own checks are re-run.  ** Nothing is written to disk. **
    buf = io.StringIO()
    s10.FAILED.clear()
    with contextlib.redirect_stdout(buf):
        rc_honest = s10.main()
    honest = list(s10.FAILED)
    s10.FAILED.clear()
    _real = s10.q1_family
    s10.q1_family = lambda _t, _sig, _name='gB': (s10.bianchi((-2, 1, 1), _t, _sig), (-2, 1, 1))
    try:
        with contextlib.redirect_stdout(buf):
            rc_mut = s10.main()
        mutant = list(s10.FAILED)
    finally:
        s10.q1_family = _real
        s10.FAILED.clear()
    check(f'Ⓒ① the repaired `S10` runs green on this tree: {len(honest)} failure(s), exit '
          f'{rc_honest}', rc_honest == 0 and not honest)
    check(f'Ⓒ② ⛭ and swapping the family back turns {len(mutant)} of its conditions red, exit '
          f'{rc_mut} -- the referent is load-bearing', rc_mut == 1 and len(mutant) == 8)
    check('Ⓒ③ while the pre-repair gate had NOTHING to mutate: the family entered no condition whose '
          'truth depends on it, so the same swap was invisible -- 0 against 8',
          len(family_conds) == 1 and len(mutant) == 8)

    # ── Ⓓ the arm, scored as registered ──────────────────────────────────────────────────────────
    cost = load(COST, 'r7346_cost')
    got, band, inside, dec = cost.scored()
    check(f'Ⓓ① the arm is scored as registered: {got} of {cost.RESULT["A_SPACE"]} against band '
          f'{band[0]}-{band[1]}, central {cost.A_CENTRAL} -- ⛔ OUTSIDE, HIGH', got == 10
          and inside is False and band == (2, 7) and cost.A_CENTRAL == 4)
    check(f'Ⓓ② and the band could have failed at the size it is scored at: decisive {dec:.3f}, '
          f'two-sided', abs(dec - cost.decisive(43, 4, (2, 7))) < 1e-12 and dec >= 0.10)
    check('Ⓓ③ the three conditions counted over the same 43: 14 write a closed form by hand, of '
          'those 2 DERIVE it and 2 TIE it in code',
          (cost.RESULT['HANDWRITTEN'], cost.RESULT['DERIVES'], cost.RESULT['TIED_IN_CODE'])
          == (14, 2, 2))
    #: ** The population is asserted from the tree at the pin, not from this file. **
    check(f'Ⓓ④ and the population is the WHOLE block read at {BEFORE} -- every `.py` gate under the '
          f'four prefixes -- and not the 19 receipts that had owed rows',
          len(cost.population(BEFORE)) == 43 and len(cost.PREFIXES) == 4)
    _ledger = [l.split('\t') for l in
               git('show', f'{BEFORE}:corpus/quote_pin_baseline.tsv').split('\n')
               if l.startswith('receipts/')]
    _s10_rows = [r for r in _ledger if r[0] == S10]
    check(f'Ⓓ⑤ ⛭ and the reason an owed-row arm could not have found this receipt: both of `S10`\'s '
          f'{len(_s10_rows)} ledger rows are DELIBERATE and neither is owed',
          len(_s10_rows) == 2 and all(r[5] == 'DELIBERATE' for r in _s10_rows))

    # ── Ⓔ the refinement, post-hoc, registered for the next revision ─────────────────────────────
    _mem = cost.census(BEFORE)[0]
    _ref = {p: cost.unreferenced_refined(p, BEFORE) for p in _mem}
    check(f'Ⓔ① the refined arbiter reads {sum(1 for v in _ref.values() if v)} of the same 43, and '
          f'the adjudication {cost.RESULT["ADJUDICATED"]}',
          sum(1 for v in _ref.values() if v) == cost.RESULT['REFINED_MEMBERS'] == 7
          and cost.RESULT['ADJUDICATED'] == 5)
    check('Ⓔ② and every member of the refined set is adjudicated by name in the registration, with '
          'the two that are NOT the class given their reason',
          {k for k, _ in cost.RESULT['ADJUDICATION']} ==
          {'L165/S10', 'L165/S5', 'L204/P13', 'L204/P7', 'L211/A3', 'L204/P5', 'L204/P8'}
          and sum(1 for _, v in cost.RESULT['ADJUDICATION'] if v.startswith('not the class')) == 2)
    check('Ⓔ③ ⛭ and the repair moves `S10` OUT of the refined set on this tree, read by the same '
          'arbiter -- which is how the repair is asserted rather than described',
          not cost.unreferenced_refined(S10, 'HEAD'))

    # ── Ⓖ the retrospective span arm, NOT counted, and the reason is measured ────────────────────
    #: ** `r7337` ④③ and `r7339` ⑥ both say whenever convenient.  It does not ride this revision, and
    #: the reason is not idleness: on THIS population the arm's outcome is a stride effect, and a
    #: text-presence reading of its outcome measure is an EXTRACTION ARTEFACT that would have reported
    #: the arm PASSING. **  The design is `r7336_60_the_span_experiment/design.py`, unchanged here.
    #: ⚠ ** BOTH SIDES ARE READ AT A PIN, and the LIVE companion is stated monotone. **  A count of
    #: what has left the ledger is a count that only grows, so an equality on it read live would go
    #: red the next time any seat retires a row -- which is the fail-on-success class this phase has
    #: already cost this seat three repairs.
    _pin = [l.split('\t') for l in
            git('show', f'{SPAN_PIN}:corpus/quote_pin_baseline.tsv').split('\n')
            if l.startswith('receipts/')]
    _live = [l.split('\t') for l in
             git('show', f'{BEFORE}:corpus/quote_pin_baseline.tsv').split('\n')
             if l.startswith('receipts/')]
    _now = [l.split('\t') for l in
            git('show', 'HEAD:corpus/quote_pin_baseline.tsv').split('\n')
            if l.startswith('receipts/')]
    _pop = [(r[0], r[1], len(r[1]) - 2) for r in _pin if r[5] != 'REPAIR-OWED']
    _livek = {(r[0], r[1]) for r in _live}
    _gone = [r for r in _pop if (r[0], r[1]) not in _livek]
    _mine = {r[0] for r in _live if any(t in r[6] for t in ('r7332+60', 'r7336+60', 'r7338+60'))}
    _gone_mine = [r for r in _gone if r[0] in _mine]
    check(f'Ⓖ① the arm\'s population, cut at {SPAN_PIN} as the design fixes it: {len(_pop)} rows '
          f'whose verdict there was not REPAIR-OWED, of which {len(_gone)} have left the ledger since',
          len(_pop) == 2482 and len(_gone) == 41)
    check(f'Ⓖ② ⚠ and {len(_gone_mine)} of those {len(_gone)} -- '
          f'{len(_gone_mine)/len(_gone):.2f} -- are in receipts THIS SEAT repaired in the three '
          f'strides, so on this population the outcome is a stride effect and not a length effect',
          len(_gone_mine) == 33 and len(_gone_mine)/len(_gone) >= 0.75)
    #: ** AND THE OUTCOME MEASURE CANNOT BE APPROXIMATED FROM THE TEXT. **  The instrument extracts a
    #: receipt's literals from its SYNTAX TREE, so a span the receipt carries across source lines is
    #: not in its text verbatim.  *** Read that way the population looks `567` stale -- while the
    #: ledger, which is the instrument's own record of what it reports, STILL CARRIES 545 of them. ***
    _naive, _texts = [], {}
    for _path, _lit, _n in _pop:
        try:
            _s = _json.loads(_lit)
        except ValueError:
            _s = _lit[1:-1]
        if _path not in _texts:
            _texts[_path] = git('show', f'{BEFORE}:{_path}') or None
        _src = _texts[_path]
        if _src is None or _s not in _src:
            _naive.append((_path, _lit, _n))
    _still = [r for r in _naive if (r[0], r[1]) in _livek]
    _lens = sorted(r[2] for r in _pop)
    _t1, _t2 = _lens[len(_lens)//3], _lens[2*len(_lens)//3]
    _long = [r for r in _naive if r[2] > _t2]
    check(f'Ⓖ③ ⛔ a text-presence reading calls {len(_naive)} of the {len(_pop)} stale, and the live '
          f'ledger still carries {len(_still)} of them -- {len(_still)/len(_naive):.2f} -- so the '
          f'reading contradicts the instrument\'s own record rather than measuring it',
          len(_naive) == 567 and len(_still) == 545)
    check(f'Ⓖ④ ⛭ and that artefact would have reported the arm PASSING: the share of the text-read '
          f'set in the longest tercile (> {_t2} chars) is {len(_long)/len(_naive):.4f}, INSIDE the '
          f'band `0.42`--`1.00` registered at `r7336` -- a length effect that is entirely extraction',
          abs(len(_long)/len(_naive) - 0.7072) < 5e-4 and 0.42 <= len(_long)/len(_naive) <= 1.00)
    _now_gone = [r for r in _pop if (r[0], r[1]) not in {(q[0], q[1]) for q in _now}]
    check(f'Ⓖ⑤ and the LIVE companion is stated monotone, as a count of what has left the ledger '
          f'only grows: {len(_now_gone)} gone on this tree, against the {len(_gone)} read at the pin',
          len(_now_gone) >= len(_gone))

    # ── Ⓕ restraint: this revision's own commits, merges excluded ────────────────────────────────
    _own = [c for c in git('rev-list', '--no-merges', f'{REG}~1..{WORK}').split('\n') if c]
    _touched = sorted({f for c in _own
                       for f in git('show', '--no-merges', '--name-only', '--format=', c).split('\n')
                       if f.startswith('receipts/')})
    check(f'Ⓕ① this revision\'s own commits to the repair, merges excluded: {len(_own)}, and the '
          f'only receipt touched in them is the one that was ordered',
          len(_own) == 2 and _touched == [S10])
    check('Ⓕ② and nothing of `70`\'s, `cc66`\'s or the do-not-edit set is in the range',
          not any(f.startswith(('receipts/L256', 'receipts/L257', 'receipts/L259',
                                'receipts/L_numerics')) for f in _touched))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** THE ORDERED DEFECT WAS A WRONG REFERENT AND NOT A MISSING ONE. **')
    print('  Ⓐ ** `S10` named `71`\'s family and asserted `Q1`\'s polynomial beside it: ** 2σ² against')
    print('     6σ², σ²(4 + 16σ²/3) against 12σ²(2σ−1)².  *** So `71` used the family the receipt')
    print('     HANDED it, and its −48Hσ³ was correct about THAT family. ***')
    print('  Ⓑ ** And the guard could not fail: ** trace-free is true of every traceless triple.')
    print('  Ⓒ ** The repair, by mutation: ** 0 conditions to mutate before, 8 of 9 red after.')
    print('     ⇒ *** Naming the right family in the prose would have left the count at 0. ***')
    print('  Ⓓ ⛔ ** The arm fails HIGH: ** 10 of 43 against a band of 2–7, decisive 0.124, on a')
    print('     population the owed count cannot see — both of `S10`\'s rows are DELIBERATE.')
    print('  Ⓔ ** Refined 7, adjudicated 5, against a central of 4: ** the excess is the')
    print('     over-inclusion the registration declared, and the refinement is registered for the')
    print('     next revision rather than scored here.')
    print('  Ⓖ ** And the span arm is not counted, for a measured reason: ** of its 2482 rows only 41')
    print('     have left the ledger and 33 of those are this seat\'s own stride — while a')
    print('     text-presence reading calls 567 stale that the ledger still carries, and that')
    print('     artefact lands 0.7072 in the longest tercile, ⛔ *** inside the registered band. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
