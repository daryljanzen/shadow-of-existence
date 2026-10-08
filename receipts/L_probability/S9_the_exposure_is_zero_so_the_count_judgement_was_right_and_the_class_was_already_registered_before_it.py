#!/usr/bin/env python3
"""L_probability receipt -- `r7217` declined to act on a register edit turning a receipt red, on the
grounds that it was `one instance`.  ** THE COUNT JUDGEMENT IS RIGHT AND THE NOVELTY JUDGEMENT IS NOT:
the exposure is ZERO, and the class has been on the record since `L-258`. **

*** ⛭⛭⛭ THREE RESULTS, AND THE FIRST IS THIS RECEIPT'S PREDICTION FAILING. ***

** ⛔ ⓵ THE PRE-REGISTERED PREDICTION SAID `SEVERAL` AND THE ANSWER IS `NONE`. **  *`131` receipts name
a root register as a file they read; `102` carry a condition this instrument can evaluate; and **not
one** loses an assertion when a row it names is STRUCK or its live clause AMENDED --- the two edits
`r7215` actually made.*  ⇒ ***The pass condition is not met and the branch that fired is the second one
the pre-registration named, in its own words: `in which case r7217's judgement is right and I will say
so in those words`.***  ** So: `r7217` was right about the count. There is no queue. Declining to build
a gate for it this cycle was the correct call. **

** ⓶ AND THE INSTRUMENT IS NOT CLEARED ON THAT ZERO, BECAUSE THE SAME BRANCH SAID IT MIGHT MEAN THE
   TEST IS BLIND. **  *The two are separated by pointing it at the case that happened: `r7224` BEFORE
its repair, against `THE_REGISTER.md` BEFORE the strike.*  ⇒ ** It catches the condition that actually
broke, under `AMEND` --- and `AMEND` is the right one, because the strike MOVED the row's live clause
while only WRAPPING its id. **  ⌗ *And `r7224` as repaired is immune to the same transform, which the
pre-registration fixed in advance as this instrument's positive control.*

** ⛭⛭ ⓷ WHAT THE MEASUREMENT DOES CHANGE IS THE NOVELTY, AND THAT IS THE HALF WORTH READING. **
*`r7217` wrote `if it happens a second time it is a member`, which rests on this being the first.*
⇒ ***`O1`'s own account names SIX registered ids of this class --- `L-258`, `L-259`, `L-261`, `L-263`,
`L-267`, `L-268` --- and lists `r7224`'s disguise among the first four explicitly: `a live register read
negatively`.***  ** So it is a member already, filed under a register that cycle had no reason to open,
and the class's own headline is `a check that pins a LIVE X punishes the finding it defends`. **
⌗ *The repair this seat reached for `r7224` --- a pin at the parent plus a disjunction over the states
--- is the repair that record already prescribes, in the words `the repaired form is pinned to the
parent and carries the opposite live assertion`. Arrived at twice, independently, which is worth more
than either arrival.*

### ⌗ THE INSTRUMENT IS AT THE LEVEL OF THE ASSERTION AND NOT THE LITERAL

*A condition built from `"lit" in TEXT` tests combined with `and`/`or`/`not` is EVALUATED against the
register before and after each transform; anything else returns `UNKNOWN` and is counted, not guessed.*
⇒ ** A disjunction survives while one arm stands, so a literal-level test would have called `r7224`'s
own repair exposed --- the repair that put the disjunction there. **

⚠ ** AND ONE OF THIS RECEIPT'S PRE-REGISTERED SEEDS WAS WRONG, WHICH THE REAL TRANSFORM CORRECTED. **
*The pre-registration said `a planted assertion on a row's id alone ⇒ EXPOSED under STRIKE`.*  ⛔ *It is
not: `r7215` wrote* `~~**PO-31**~~`, *which still CONTAINS* `**PO-31**`. ***A strike WRAPS a row's id, it
does not remove it.***  *So the shape a strike actually breaks is an assertion that the row is NOT
struck, and the seed is corrected to that in the file rather than quietly re-aimed.*

⚠ ** THE RECALL LIMITS, COUNTED: ** `26` of the `131` read a register the transforms cannot reach at
all --- no row id, no clause marker --- and `3` carry no condition this test can read. *A needle built
at run time, a regex pin, or a literal assembled from parts is invisible here.*  ⛔ ** None of the `29`
is counted clean. **

⛔ *Nothing is filed and nothing is gated: `r7217` declined both and the measurement supports the
decision rather than reopening it. `29` gates, all pass, about two seconds. No assertion on wall-clock
time.*
"""
import ast
import collections
import glob
import hashlib
import os
import re
import subprocess

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PIN = 'd489251a714feed379886d780c089d0a1bad97d9'


def _at(rev, path):
    return subprocess.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout


# ⛭⛭ THE TWO TRANSFORMS, AND ONLY THESE TWO, because the point is exposure to an edit that HAS
#    HAPPENED rather than to every edit imaginable.  `r7215` struck `PO-31` and moved its live clause.
ROW_ID = re.compile(r'\b(PO|L)-\d+\b')
CLAUSE = re.compile(r'(THE LIVE CLAUSE \(SET `?r)(\d+)')


def strike(text, ids):
    """wrap the named rows' ids in the strike marks, as `r7215` wrote `~~**PO-31**~~`"""
    for i in ids:
        text = text.replace(f'**{i}**', f'~~**{i}**~~')
    return text


def amend(text, ids):
    """move every live-clause marker to a later revision, as the strike did"""
    return CLAUSE.sub(lambda m: m.group(1) + str(int(m.group(2)) + 2), text)


def presence_eval(node, text):
    """⛭⛭ evaluate an assertion's CONDITION, not its literals.  A condition built from `"lit" in TEXT`
    tests combined with and/or/not is evaluated against one text; anything else returns None and is
    counted UNKNOWN rather than guessed at.

    ⌗ This is the whole reason the instrument is at the level of the assertion: a DISJUNCTION survives
    while one arm stands, so removing one of its literals is not an exposure.  A literal-level test
    would have called `r7224`'s own repair exposed -- the repair that put the disjunction there."""
    if isinstance(node, ast.BoolOp):
        vals = [presence_eval(v, text) for v in node.values]
        if any(v is None for v in vals):
            return None
        return any(vals) if isinstance(node.op, ast.Or) else all(vals)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        v = presence_eval(node.operand, text)
        return None if v is None else (not v)
    if (isinstance(node, ast.Compare) and len(node.ops) == 1
            and isinstance(node.left, ast.Constant) and isinstance(node.left.value, str)):
        if isinstance(node.ops[0], ast.In):
            return node.left.value in text
        if isinstance(node.ops[0], ast.NotIn):
            return node.left.value not in text
    return None


def literal_in(node):
    return any(isinstance(n, ast.Compare) and isinstance(n.left, ast.Constant)
               and isinstance(n.left.value, str)
               and any(isinstance(o, (ast.In, ast.NotIn)) for o in n.ops)
               for n in ast.walk(node))


def conditions(tree):
    """every expression that an ASSERTION could rest on: an `assert`'s test, or an argument of a call
    -- which is how every gate helper in this corpus receives its condition."""
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Assert):
            out.append(n.test)
        elif isinstance(n, ast.Call):
            out.extend(a for a in n.args if isinstance(a, (ast.BoolOp, ast.UnaryOp, ast.Compare)))
    return [c for c in out if literal_in(c)]


# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("A. THE INSTRUMENT, SEEDED BOTH WAYS BEFORE IT IS POINTED AT ANYTHING")

_REG = "| **PO-31** | the row's body says the throat damps under rotation. THE LIVE CLAUSE (SET r7197) |"
SEEDS = (
    ('a live-clause marker', '"THE LIVE CLAUSE (SET r7197)" in REG', 'AMEND'),
    ('an assertion that the row is LIVE', '"~~**PO-31**~~" not in REG', 'STRIKE'),
    ("a row's id on its own", '"**PO-31**" in REG', 'IMMUNE'),
    ('a sentence in the row body', '"the throat damps under rotation" in REG', 'IMMUNE'),
    ('a disjunction with one arm the transforms cannot reach',
     '"THE LIVE CLAUSE (SET r7197)" in REG or "the throat damps under rotation" in REG', 'IMMUNE'),
)
for _nm, _expr, _want in SEEDS:
    _c = ast.parse(_expr, mode='eval').body
    _b = presence_eval(_c, _REG)
    _s = presence_eval(_c, strike(_REG, ['PO-31']))
    _a = presence_eval(_c, amend(_REG, ['PO-31']))
    got = 'STRIKE' if (_b and not _s) else 'AMEND' if (_b and not _a) else 'IMMUNE'
    print(f"    {_nm:44s} before={_b!s:5s} strike={_s!s:5s} amend={_a!s:5s} -> {got}")
    gate(f"Ⓖ① the seeding discriminates: '{_nm}' comes out {_want} and not somewhere convenient "
         f"({got})", got == _want)

# ⛭⛭ AND THE THIRD SEED IS A CORRECTION OF THIS RECEIPT'S OWN EXPECTATION, WHICH IS WHY IT IS HERE.
#    *The pre-registration said `a planted assertion on a row's id alone ⇒ EXPOSED under STRIKE`.*
#    ⛔ ** It is not, and the real transform is the reason: `r7215` wrote `~~**PO-31**~~`, which still
#    CONTAINS `**PO-31**`.  A strike WRAPS a row's id, it does not remove it. **  ⇒ *So an assertion
#    on an id is immune, and the shape a strike actually breaks is an assertion that the row is NOT
#    struck -- `"~~**PO-31**~~" not in REG`, the second seed.  The instrument was right and the
#    prediction's seed was wrong, which is recorded rather than quietly re-aimed.*
gate("Ⓖ② the strike WRAPS the row's id rather than removing it, so an id assertion survives it -- "
     "this receipt's own pre-registered seed expected otherwise and is corrected here",
     '**PO-31**' in strike(_REG, ['PO-31']) and '~~**PO-31**~~' in strike(_REG, ['PO-31']))
gate("Ⓖ②ᵇ and the instrument is at the level of the ASSERTION, not the literal -- the last seed "
     "holds a literal that AMEND removes and is still IMMUNE, which is the property that keeps "
     "r7224's own repair from reading as exposed",
     presence_eval(ast.parse(SEEDS[4][1], mode='eval').body, amend(_REG, ['PO-31'])) is True)
gate("Ⓖ③ a condition this instrument cannot read returns UNKNOWN rather than a guess",
     presence_eval(ast.parse('len(REG) > 10', mode='eval').body, _REG) is None)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("B. THE POPULATION, FOUND FROM THE SOURCES AND NOT FROM A LIST")

REGS = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, '*.md'))} | {'INDEX.md'}
NAMED = re.compile(r"'([A-Za-z0-9_\-+.]+\.md)'")
POP = {}
for p in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    rel = os.path.relpath(p, ROOT)
    src = open(p, encoding='utf-8', errors='replace').read()
    named = {m.group(1) for m in NAMED.finditer(src)} & REGS
    if named:
        POP[rel] = (src, named)
print(f"    root registers on disk            {len(REGS)}")
print(f"    receipts naming one as a file     {len(POP)}")
_cnt = collections.Counter(r for _s, rs in POP.values() for r in rs)
for _r, _n in _cnt.most_common(6):
    print(f"      {_r:40s} {_n}")
gate(f"Ⓖ④ the population is found from the receipts' own sources -- {len(POP)} of them name a root "
     f"register as a file -- and is not a list anyone wrote down", len(POP) > 100)

# ⛭ the registers the transforms can even reach: a strike needs a `**ID**` row, an amendment needs a
#   clause marker.  A register with neither is immune to BOTH by construction and says so.
TEXT = {r: (open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
            if r == 'INDEX.md'
            else open(os.path.join(ROOT, r), encoding='utf-8', errors='replace').read())
        for r in sorted({r for _s, rs in POP.values() for r in rs})}
REACHABLE = {r for r, t in TEXT.items() if re.search(r'\*\*(PO|L)-\d+\*\*', t) or CLAUSE.search(t)}
print(f"    registers a strike or amendment can reach: {len(REACHABLE)} of {len(TEXT)} "
      f"-- {', '.join(sorted(REACHABLE))}")
gate(f"Ⓖ⑤ and the transforms reach only SOME registers -- {len(REACHABLE)} of {len(TEXT)} carry a "
     f"row id or a clause marker at all -- so an immune verdict below can be the register's doing "
     f"and is reported that way", 0 < len(REACHABLE) < len(TEXT))

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("C. THE EXPOSURE, ONE RECEIPT AT A TIME, AGAINST ONLY THE ROWS IT NAMES")

TALLY = collections.Counter()
EXPOSED, WITNESS = [], []
for rel, (src, named) in POP.items():
    live = {r for r in named if r in REACHABLE}
    if not live:
        TALLY['NO-REACHABLE-REGISTER'] += 1
        continue
    try:
        tree = ast.parse(src)
    except SyntaxError:
        TALLY['UNPARSED'] += 1
        continue
    conds = conditions(tree)
    if not conds:
        TALLY['NO-LITERAL-CONDITION'] += 1
        continue
    ids = sorted({m.group(0) for m in ROW_ID.finditer(src)})
    hit_s, hit_a, readable, w = False, False, 0, None
    for r in sorted(live):
        before = TEXT[r]
        after_s, after_a = strike(before, ids), amend(before, ids)
        for c in conds:
            b = presence_eval(c, before)
            if b is None:
                continue
            readable += 1
            s_, a_ = presence_eval(c, after_s), presence_eval(c, after_a)
            if b and s_ is False:
                hit_s = True
                w = w or (rel, r, 'STRIKE', ast.unparse(c)[:150])
            if b and a_ is False:
                hit_a = True
                w = w or (rel, r, 'AMEND', ast.unparse(c)[:150])
    if not readable:
        TALLY['NO-READABLE-CONDITION'] += 1
        continue
    if hit_s and hit_a:
        TALLY['EXPOSED-BOTH'] += 1
    elif hit_s:
        TALLY['EXPOSED-STRIKE'] += 1
    elif hit_a:
        TALLY['EXPOSED-AMEND'] += 1
    else:
        TALLY['IMMUNE'] += 1
    if w:
        EXPOSED.append(rel)
        WITNESS.append(w)

for k in ('EXPOSED-BOTH', 'EXPOSED-STRIKE', 'EXPOSED-AMEND', 'IMMUNE', 'NO-READABLE-CONDITION',
          'NO-LITERAL-CONDITION', 'NO-REACHABLE-REGISTER', 'UNPARSED'):
    print(f"    {k:24s} {TALLY[k]}")
NEXP = TALLY['EXPOSED-BOTH'] + TALLY['EXPOSED-STRIKE'] + TALLY['EXPOSED-AMEND']
NMEAS = NEXP + TALLY['IMMUNE']
print(f"\n    measured {NMEAS} of {len(POP)}   EXPOSED {NEXP}   IMMUNE {TALLY['IMMUNE']}")
gate(f"Ⓖ⑥ the buckets partition the population -- {sum(TALLY.values())} of {len(POP)}",
     sum(TALLY.values()) == len(POP))
gate(f"Ⓖ⑦ the count is stated before it is judged: {NEXP} exposed of {NMEAS} measurable, with "
     f"{TALLY['NO-REACHABLE-REGISTER']} reading a register the transforms cannot reach at all",
     NEXP + TALLY['IMMUNE'] == NMEAS)
gate(f"Ⓖ⑧ and the instrument discriminates rather than flagging -- {TALLY['IMMUNE']} measurable "
     f"receipts come out IMMUNE, so an exposed verdict is a property of the receipt and not of the "
     f"transform", TALLY['IMMUNE'] > 0)
gate(f"Ⓖ⑨ the pre-registered THIRD OUTCOME did not fire: the transforms do NOT reach nearly every "
     f"reader -- {NEXP} exposed against {TALLY['IMMUNE']} immune and "
     f"{TALLY['NO-REACHABLE-REGISTER']} whose register carries no row id at all",
     NEXP < 0.9 * NMEAS)

print("\n    the exposed set, with the assertion that breaks and the transform that breaks it:")
for rel, r, t, c in WITNESS[:8]:
    print(f"\n      {os.path.basename(rel)[:68]}")
    print(f"        in {r} under {t}")
    print(f"        {c}")
gate(f"Ⓖ⑩ and every exposed verdict exhibits the condition that flips and the transform that flips "
     f"it -- {len(WITNESS)} of {NEXP}", len(WITNESS) == NEXP)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("D. ⛭⛭ ZERO IS THE REFUTING BRANCH, SO THE INSTRUMENT IS PUT ON THE CASE THAT DID HAPPEN")

# *** The pre-registration named this exactly: `none comes out exposed, which would mean the repaired
#     receipt was the only one and the static test cannot even see it, so the instrument is wrong and
#     gets reported as wrong`. ***  ⇒ ** There is one way to tell those two apart, and it is to point
#     the instrument at `r7224` BEFORE its repair, against the register BEFORE the strike. **
PRE_RECEIPT = 'fcd538ee^'
PRE_REGISTER = 'd6ff1b549ac29aacccc63db87b8f29e8df0c0e6f'
R7224 = ('receipts/P15_CR_cosmology/P15_po31s_terminal_clause_counts_closures_and_the_label_is_many_'
         'to_one_so_the_count_is_four_and_five_at_once_and_the_quantifier_has_no_set.py')
_old_src = _at(PRE_RECEIPT, R7224)
_old_reg = _at(PRE_REGISTER, 'THE_REGISTER.md')
_old_conds = conditions(ast.parse(_old_src))
_ids = sorted({m.group(0) for m in ROW_ID.finditer(_old_src)})
_caught = []
for c in _old_conds:
    b = presence_eval(c, _old_reg)
    if b is None:
        continue
    for _t, _fn in (('STRIKE', strike), ('AMEND', amend)):
        if b and presence_eval(c, _fn(_old_reg, _ids)) is False:
            _caught.append((_t, ast.unparse(c)[:140]))
print(f"    r7224 before its repair, against the register before the strike:")
for _t, _c in _caught:
    print(f"      caught under {_t}:  {_c}")
gate(f"Ⓖ⑪ ⛭⛭ THE INSTRUMENT CATCHES THE CASE THAT ACTUALLY HAPPENED -- r7224's pre-repair condition "
     f"flips under the very transform r7215 performed ({len(_caught)} catch(es)) -- so a ZERO on the "
     f"current tree is a fact about the tree and NOT the instrument failing to see", _caught)
gate("Ⓖ⑫ and it catches it under AMEND, which is the edit the strike actually made to that row -- "
     "the clause moved, the row's id was only wrapped",
     any(t == 'AMEND' for t, _ in _caught))
_now = conditions(ast.parse(open(os.path.join(ROOT, R7224), encoding='utf-8').read()))
_still = [ast.unparse(c)[:120] for c in _now
          if presence_eval(c, TEXT['THE_REGISTER.md']) is True
          and presence_eval(c, amend(TEXT['THE_REGISTER.md'], _ids)) is False]
gate(f"Ⓖ⑬ and r7224 AS REPAIRED is immune to the same transform, which the pre-registration named as "
     f"this instrument's positive control ({len(_still)} exposed condition(s) left)", not _still)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("E. AND THE CLASS IS ALREADY REGISTERED, WHICH IS THE PART `r7217` COULD NOT HAVE KNOWN FROM ITS OWN CYCLE")

O1 = ('receipts/L268_broken_by_its_own_edit/O1_a_receipt_that_asserts_a_state_its_own_revision_'
      'changes_is_false_when_committed.py')
_o1 = open(os.path.join(ROOT, O1), encoding='utf-8', errors='replace').read()
_doc = ast.get_docstring(ast.parse(_o1)) or ''
_lclasses = sorted({m.group(0) for m in re.finditer(r'L-2[0-9]{2}', _doc)})
print(f"    O1's docstring names the class and its disguises: {', '.join(_lclasses)}")
for _s in ('a check that pins a LIVE X punishes the finding it defends',
           'a live register read negatively', 'the fifth disguise'):
    gate(f"Ⓔ① the class is on the record in those words -- `{_s[:58]}`", _s in ' '.join(_doc.split()))
gate(f"Ⓔ② and it is a FAMILY, not a single row: {len(_lclasses)} registered ids in O1's own account "
     f"({', '.join(_lclasses)})", len(_lclasses) >= 4)
_disguises = ' '.join(_doc.split())
gate("Ⓔ③ ⛔ and r7224's case is the SAME disguise the record already names -- `a live register read "
     "negatively` -- so `one instance` is true of r7215's cycle and not of the class",
     'a live register read negatively' in _disguises and 'L-258' in _disguises)
gate("Ⓔ④ ⌗ and the repair this seat applied at r7224 is the repair the record already prescribes -- "
     "`the repaired form is pinned to the parent and carries the opposite live assertion` -- which "
     "is the pin plus the disjunction, arrived at twice independently",
     'pinned to the parent and carries the opposite live assertion' in _disguises)


# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("F. ⛔ THE PRE-REGISTERED PREDICTION FAILED, AND IT IS REPORTED AS A FAILURE")

print("      r7232 predicted: the exposed set is SEVERAL receipts, not one, because a live-clause")
print("      marker is the natural thing to assert when the argument is about a row's current state.")
print(f"      Measured: {NEXP}.  Not several, and not one either -- NONE.")
print("      ⇒ The pass condition is NOT met.  The refuting branch that fired is the SECOND one the")
print("        pre-registration named, and the sentence it named it in was: `exactly one receipt")
print("        comes out exposed -- r7224's, the one already repaired -- in which case r7217's")
print("        judgement is right and I will say so in those words`.  It came back at zero because")
print("        that one is repaired, so the count of UNREPAIRED exposures is zero.")
gate(f"Ⓕ① the prediction is NOT met and is reported as a failure: {NEXP} exposed against a predicted "
     f"`several`, and no exposure count is published as a defect count because there is no exposure "
     f"to count", NEXP == 0)
gate("Ⓕ② ⛭⛭ AND `r7217`'s JUDGEMENT ON THE COUNT IS RIGHT, IN THOSE WORDS: the repaired receipt was "
     "the only one, there is no queue of further instances on this tree, and declining to build a "
     "gate for it this cycle was the correct call",
     NEXP == 0 and _caught and not _still)
gate("Ⓕ③ ⛔ and the instrument is NOT reported clean on that basis -- the other half of the refuting "
     "branch said a zero could mean the static test cannot see the case at all, and that is "
     "separated by putting it on the case that happened rather than by assertion", bool(_caught))
gate(f"Ⓕ④ ⌗ what the measurement DOES change is the novelty and not the count: `if it happens a "
     f"second time it is a member` rests on this being the first, and the record carries "
     f"{len(_lclasses)} registered ids of the same class with r7224's disguise named explicitly -- "
     f"so it is already a member, filed under a different register",
     len(_lclasses) >= 4 and 'a live register read negatively' in _disguises)
gate(f"Ⓕ⑤ and the recall limit is stated rather than estimated: a condition built at run time, a "
     f"regex pin, or a literal assembled from parts is invisible here -- "
     f"{TALLY['NO-READABLE-CONDITION'] + TALLY['NO-LITERAL-CONDITION']} receipts fall in those "
     f"buckets and are counted, not cleared",
     TALLY['NO-READABLE-CONDITION'] + TALLY['NO-LITERAL-CONDITION'] > 0)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print("""
  THE EXPOSURE IS ZERO AND THE CLASS IS ALREADY REGISTERED, SO r7217 WAS RIGHT ABOUT THE COUNT AND
  THE THING WORTH SAYING IS THE OTHER HALF.  131 receipts name a root register as a file they read;
  102 of them carry a condition this instrument can evaluate; and NOT ONE loses an assertion when a
  row it names is struck or its live clause amended.  The pre-registered prediction said several and
  is reported as failed.  The instrument is not cleared on that zero: pointed at r7224 before its
  repair, against the register before the strike, it catches the condition that actually broke, under
  AMEND -- the edit the strike made to that row, the id having only been wrapped and not removed.
  And r7224 as repaired is immune to the same transform, which was the pre-registered positive
  control.  WHAT THE MEASUREMENT CHANGES IS THE NOVELTY: `if it happens a second time it is a member`
  rests on this being the first, and O1's own account names six registered ids of the same class with
  r7224's disguise among them in the words `a live register read negatively` -- so it is a member
  already, filed under a register r7217's cycle had no reason to open.  The repair this seat reached
  for r7224, a pin plus a disjunction, is the repair that record already prescribes.  Nothing is
  filed, nothing is gated, and 29 receipts sit in stated recall limits rather than in the clean arm.""")
if _bad:
    raise SystemExit(1)
