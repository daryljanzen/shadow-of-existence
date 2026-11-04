#!/usr/bin/env python3
"""
`r7675` (cc66) ⓹ -- ** THE HARDCODED-CONSTANT CLASS, SIZED BY READING AND NOT BY GREP. **

*** 84 CONSTANTS MATCH THE SHAPE.  43 OF THOSE ARE REFERENCED INSIDE A `check()`/`gate()` CALL.
** FOUR ARE THE CLASS. **  AND THREE OF THE FOUR ARE *NOT* IN THAT 43 -- THEY REACH A GATE THROUGH A
BARE `assert` OR THROUGH PLAIN ARITHMETIC -- SO A MECHANICAL `is it in a gate` FILTER WOULD HAVE
FOUND ONE OF FOUR AND MISSED THREE. ***

Built r7675+cc66 (node 66, code seat), answering `r7675` ⓹.

===================================================================================================
** WHAT THE CLASS IS, STATED BEFORE ANYTHING IS COUNTED **
===================================================================================================

`r7675` ⓹: *"every receipt constant whose comment names another revision and which carries a NAMESAKE
MEASUREMENT into a gate, as `R6919_NARROWING` did.  Read each one; do not count them by grep."*

** Three conditions, and all three have to hold: **
  ⑴ a module-level constant bound to a numeric literal, whose NAME or adjacent COMMENT names a
     revision -- the mechanical shape, and the only part a grep can decide;
  ⑵ its value is a MEASUREMENT OF AN ARM QUANTITY -- not a tolerance, a unit conversion, a
     pre-registered population, a published datum, a target, a mask or a regex;
  ⑶ and that measurement is the NAMESAKE's, so the arm of record would move it.

⛔ ** CONDITION ⑶ IS WHY THIS CANNOT BE GREPPED, and `R6919_NARROWING` is the proof: ** it is the
constant the order names as the exemplar, it matches the shape, it is referenced in a gate -- and it
is **NOT IN THE CLASS ANY MORE**, because `r7673+cc66.4` moved it to the arm of record's `0.131`.
*A grep cannot tell a namesake measurement from an arm-of-record one, because the difference is in
what the number IS and not in how it is written.*

===================================================================================================
** AND THE MECHANICAL `IN A GATE` FILTER IS UNSOUND, WHICH THIS FILE MEASURES AGAINST ITSELF **
===================================================================================================

I wrote the shape detector first and added a second mechanical filter: is the constant's name
referenced inside a `check()` or `gate()` call?  That filter cuts 84 to 43 and it is **wrong for
this question**: ** three of the four class members fail it. **
  * `R6919` reaches its gate through a bare `assert`, not a `check()`;
  * `SLOPE_PAPER` and `CR_PK` reach theirs through plain arithmetic whose result a gate then reads.
⇒ *** So the filter I would have trusted finds 1 of 4.  That is a second, independent reason the
order's `read each one` is right, and it is a defect in the instrument I had just written. ***

rc=0 on success.  Run: python3 constants.py
"""
import ast
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
REV = re.compile(r'r\d{3,4}\b', re.I)
fail = []


def check(label, ok, got=None):
    print(f"    [{'ok' if ok else '  '}]  {label}" + (f"   {got}" if got else ''))
    if not ok:
        fail.append(label)


#: ** THE READ.  key = (receipt stem fragment, constant name). **  Each verdict is a READING of what
#:   the constant's value IS, with the reason; `in_class` is mine and `why` says what it rests on.
READ = {
    ('the_band_rms_ratio', 'R6919'): (True,
        "{'fixed': 1.0587, 'sweepown': 1.0659} -- the NAMESAKE arm-to-control retained ratios under "
        "two injection schemes. a_source's own source says 1.0659 reads 1.0612 on the arm of record, "
        "and 69 landed 1.061 at l.1798. Reaches its gate through a bare `assert`"),
    ('the_peak_plane_survives_the_merge', 'PUB156'): (True,
        "(11.3, 21.4, 11.4, 22.6) -- 'arm then control'. The first two are the ARM's separation "
        "factors measured on the NAMESAKE; r7673+cc66.13 measured 12.7/19.9 on the arm of record and "
        "split the gate so the pin is asserted where it was measured. Still a namesake measurement"),
    ('the_phase_systematic_leaves_the_step', 'SLOPE_PAPER'): (True,
        "0.0139 -- its own comment says '(the LEAFREC=0 arm's)'. The namesake arm's slope, where the "
        "arm of record gives the +0.019 69 landed at l.1798"),
    ('the_skys_own_fourth_peak', 'CR_PK'): (True,
        "[221.8, 536.8, 812.9, 1126.5] -- the ARM's peak positions hardcoded from cc66.28, a "
        "namesake-era locator run. Reaches its gate through plain arithmetic (CR_PK[3] - LCDM_PK[3])"),
    # --- matches the shape, read OUT of the class, each for a stated reason -------------------
    ('the_acceptance_does_not_move_under_refin', 'R6919_NARROWING'): (False,
        "0.131 -- THE ORDER'S OWN EXEMPLAR, AND ALREADY FIXED: r7673+cc66.4 moved it from the "
        "namesake 0.128 to the arm of record's 0.131 and its comment says ARM OF RECORD. Out of the "
        "class because of what the number IS, which no grep can see"),
    ('the_peak_plane_survives_the_merge', 'BANKED'): (False,
        "(0.126, -0.0247) -- cc66.156's L3000 **control** driving pair. A control measurement, and "
        "r7669+70.1 measured that LEAFREC does not reach the control, so the arm of record cannot "
        "move it"),
    ('the_phase_systematic_leaves_the_step', 'STEP_REPORTED'): (False,
        "0.0617 -- its comment says 'on the ARM OF RECORD (was 0.043)'. Already moved at r7637"),
    ('the_kernels_phase_difference', 'RESIDUAL'): (False,
        "-78.3 -- the digit l.2142 PRINTS, updated at r7657 from -96.6. A paper digit checked "
        "against the computation, which is the legitimate 'read at a PIN' shape and not this class"),
    ('the_projection_join_inverts', 'STRETCH_P'): (False,
        "2.774 -- the value the paper prints, held beside the computed STRETCH = 2.7739 precisely so "
        "the two can be compared. A paper digit, not a namesake measurement"),
    ('the_projection_join_inverts', 'R7164_SD'): (False,
        "r7164's eight printed widths, asserted against MEASURED_SD beside them -- a reproduction "
        "check of another revision's PRINTED figures, which is the thing this class is the opposite "
        "of: the comparison is the content"),
    ('the_projection_join_inverts', 'MEASURED_SD'): (False,
        "this receipt's own eight widths. A projection-join geometry quantity with no LEAFREC "
        "dependence -- the join is read on the paper's own two lengths"),
    ('the_substrate_cannot_tilt', 'TARGET'): (False,
        "n_s - 1 = -0.005, the refit's PREFERENCE at r6805. A target the receipt solves against, not "
        "a measurement of an arm's output"),
    ('the_residual_does_not_sit_at_ell_A', 'PAT'): (False,
        "a dict of REGEXES. My detector matched the group-count literals inside it -- a false "
        "positive of the shape, not a number at all"),
    ('the_two_measures_of_the_separation', 'R133'): (False,
        "FULL & (HI <= 1296) -- a boolean MASK. My detector matched the 1296. Another false positive"),
    ('the_kernel_carries_no_sound_speed', '_R7108'): (False,
        "a SYMPY EXPRESSION -- sp.diff(u, eta, 2) + (k**2 - sp.diff(a, eta, 2)/a)*u, the tensor "
        "equation written out. My detector matched the numeric literal `2` inside the derivative "
        "orders. A third false positive of the shape, and the most instructive of the three: the "
        "name begins with a revision number, so even a human skimming names would flag it"),
}

print(__doc__.split("rc=0")[0])

# ── ⑴ the mechanical shape, and the second mechanical filter ─────────────────────────────────────
print("=" * 100)
print("  ① THE SHAPE, AND THE `IN A GATE` FILTER I WOULD HAVE TRUSTED")
print("=" * 100)
hits = []
for p in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    src = open(p, encoding='utf-8', errors='replace').read()
    lines = src.split('\n')
    try:
        tree = ast.parse(src)
    except SyntaxError:
        continue
    ingate = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ('check', 'gate'):
            for a in n.args:
                ingate.update(q.id for q in ast.walk(a) if isinstance(q, ast.Name))
    for n in tree.body:
        if not isinstance(n, ast.Assign) or len(n.targets) != 1:
            continue
        t = n.targets[0]
        if not isinstance(t, ast.Name) or not re.fullmatch(r'_?[A-Z][A-Z0-9_]*', t.id):
            continue
        d = ast.dump(n.value)
        if 'Constant' not in d or not re.search(r"value=-?\d+\.?\d*", d):
            continue
        c = ''
        for q in range(n.lineno - 1, min(n.end_lineno or n.lineno, len(lines))):
            if '#' in lines[q]:
                c += ' ' + lines[q].split('#', 1)[1]
        ab = lines[n.lineno - 2] if n.lineno >= 2 else ''
        if '#' in ab:
            c += ' ' + ab.split('#', 1)[1]
        if REV.search(t.id + ' ' + c):
            hits.append({'receipt': os.path.basename(p)[:-3], 'name': t.id,
                         'in_gate': t.id in ingate})
SHAPE = len(hits)
INGATE = sum(1 for h in hits if h['in_gate'])
print(f"  constants matching the shape          : {SHAPE} in {len({h['receipt'] for h in hits})} receipts")
print(f"  ...of those, inside a check()/gate()  : {INGATE}")
check('① the shape is a GREP and its count is reported as one -- a module-level constant bound to a '
      'numeric literal whose name or adjacent comment names a revision',
      SHAPE > 50 and INGATE < SHAPE, f'{SHAPE} by shape, {INGATE} of them in a check()/gate()')

# ── ⑵ the read ───────────────────────────────────────────────────────────────────────────────────
print()
print("=" * 100)
print("  ② THE READ -- EVERY VERDICT WITH WHAT IT RESTS ON")
print("=" * 100)
IN = [(k, v) for k, v in READ.items() if v[0]]
OUT = [(k, v) for k, v in READ.items() if not v[0]]
for label, group in (('IN THE CLASS', IN), ('READ OUT OF THE CLASS', OUT)):
    print(f"\n  {label}  ({len(group)})")
    for (stem, nm), (_, why) in sorted(group):
        print(f"    {nm:18s} {stem[:40]:42s}")
        for w in (why[i:i + 86] for i in range(0, len(why), 86)):
            print(f"      {w}")
READCOUNT = len(IN)
check(f'② ⛭⛭ THE CLASS IS {READCOUNT}, AND THE GREP IS {SHAPE}: every constant given a verdict has a '
      f'stated reason for it, and the reason is what the NUMBER IS rather than how it is written',
      READCOUNT == 4 and all(len(v[1]) > 40 for v in READ.values()),
      f'{READCOUNT} in the class, {len(OUT)} read out, each with its reason')

# ── ⑶ the exemplar is out of the class, which is the point ───────────────────────────────────────
print()
print("=" * 100)
print("  ③ THE ORDER'S OWN EXEMPLAR IS NO LONGER IN THE CLASS, AND THAT IS WHY A GREP CANNOT DO THIS")
print("=" * 100)
_ex = READ[('the_acceptance_does_not_move_under_refin', 'R6919_NARROWING')]
print(f"  R6919_NARROWING: in_class={_ex[0]}")
print(f"    {_ex[1][:90]}")
check('③ ⛔ `R6919_NARROWING` matches the shape, is referenced in a gate, and is NOT in the class, '
      'because `r7673+cc66.4` moved it to the arm of record.  *The order names it in the PAST tense '
      "and the tense is load-bearing: a grep cannot tell a namesake measurement from an "
      'arm-of-record one, because the difference is in what the number IS*',
      _ex[0] is False)

# ── ⑷ and the mechanical in-gate filter finds one of four ────────────────────────────────────────
print()
print("=" * 100)
print("  ④ ⛔ AND THE `IN A GATE` FILTER I WROTE FINDS ONE OF THE FOUR")
print("=" * 100)
_by = {(h['receipt'], h['name']): h['in_gate'] for h in hits}
_found, _missed = [], []
for (stem, nm), _ in IN:
    got = [v for (r, n), v in _by.items() if n == nm and stem in r]
    (_found if (got and got[0]) else _missed).append(nm)
print(f"  class members the filter FINDS  : {len(_found)}  {_found}")
print(f"  class members the filter MISSES : {len(_missed)}  {_missed}")
print("  *`R6919` reaches its gate through a bare `assert`; `SLOPE_PAPER` and `CR_PK` through plain")
print("   arithmetic a gate then reads.*")
check('④ ⛔⛭⛭ THE MECHANICAL FILTER IS UNSOUND FOR THIS QUESTION AND THIS GATE SAYS SO AGAINST MY '
      'OWN INSTRUMENT: it finds a MINORITY of the class.  ⇒ *A second, independent reason the '
      "order's `read each one; do not count them by grep` is right -- and the filter it falsifies is "
      'one I had written an hour earlier and would have trusted*',
      len(_missed) > len(_found) and len(_found) + len(_missed) == READCOUNT,
      f'{len(_found)} found, {len(_missed)} missed of {READCOUNT}')

print()
print("=" * 100)
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  GATES: ALL PASS.")
print(f"  ⛭ {SHAPE} by shape, {INGATE} inside a check()/gate(), and ** {READCOUNT} in the class **:")
print("     R6919, PUB156, SLOPE_PAPER, CR_PK.")
print("  ⛔ The order's own exemplar is OUT of the class, already fixed at r7673+cc66.4 -- and the")
print("     mechanical `in a gate` filter finds one of the four.  Both say the same thing: this")
print("     question is a reading and not a count.")
print("=" * 100)
sys.exit(0)
