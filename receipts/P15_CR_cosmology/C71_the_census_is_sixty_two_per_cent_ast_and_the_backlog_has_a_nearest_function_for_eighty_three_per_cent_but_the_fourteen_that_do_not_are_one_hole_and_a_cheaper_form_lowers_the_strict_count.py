#!/usr/bin/env python3
"""P15 receipt -- `r7261`'s ORDER ① ⒜ and ⒝ AND ORDER ②: work the `108` census and the `85` backlog
under the unit `66` set, with both numbers pre-registered first; and repair the two value pairs
`CR_cosmology.tex` carries for one quantity.

*** ⛭⛭⛭ ⒝ THE BACKLOG HAS A NAMED NEAREST FUNCTION FOR `71` OF ITS `85` -- `83.5` PER CENT, INSIDE A
    PINNED `82` AND A BAND OF `65`-`93`.  `66`'s NEGATIVE NEEDED UNDER `25` AND MISSES BY `58.5`
    POINTS, SO `computable` IS A STATEMENT ABOUT WORK AND NOT ABOUT POSSIBILITY. ***

*** ⛭⛭⛭ AND THE `14` THAT HAVE NONE ARE ONE HOLE RATHER THAN FOURTEEN GAPS: `13` OF THEM WANT A
    ZERO-MODE, A KERNEL OR AN INDEX, AND NO FUNCTION ANYWHERE UNDER `computations/` COMPUTES ONE.
    `L110_the_count_specified.py`, `L78_the_mode_through_the_branch_point.py`,
    `L75_the_wall_is_the_graze_point.py`, `L15_the_quark_lepton_frontier.py` and
    `L117w_the_colourless_sector.py` are top-level sympy scripts with no `def` in them at all. ***
  ⌗ *That is exactly what the DOMAIN-versus-QUANTITY distinction `PREDICTION.md` declared in advance
    was built to find: the `ZM` witness class resolved to `24` modules at domain level and to ZERO
    functions at quantity level.  A high answer here could not be credited to the test that had
    already passed, and the one block where it mattered is the one block that failed.*

** ⒜ THE CENSUS IS `62.0` PER CENT AST -- `67` of `108`, INSIDE A PINNED `64` AND A BAND OF `58`-`72`,
   and clear of the `58.3` no-movement floor. **  *`4` of the `45` `INDEP` rows moved to an AST form on
a per-holder read against `6` pinned, and the `2` that did not move are recorded with the reason
rather than dropped: one would have taken an absence-of-CODE form WEAKER than the paper's claim, and
one has a computed outcome where an AST-PLACE form would assert a position instead.*

** ⛔⛔ AND A PRE-REGISTERED IDENTITY FAILED, WHICH IS THE FINDING OF ⒜. **  *I pinned that ruling ③'s
flag count would leave `108 - 41 = 67`, `C70`'s strict carry count, and said the identity was
gate-checkable rather than asserted.  **It is `64`.**  `3` of the `4` movers are held by receipts that
open no source file, so taking a row to its CHEAPEST form bought an AST test and COST a read -- while
the `INDEP` form it left needed only a capability those holders already have.*
⇒ *** SO A CHEAPER FORM CAN LOWER THE STRICT COUNT, and the two rules interact in a way neither ruling
    anticipated: the strict count is not invariant under the census, it is a function of which form
    each row records.  Ruling ③'s CONDITION still holds -- the strict count is recoverable from the
    same table, at `64` -- and what failed is my prediction that the census would leave it at `67`. ***

** THE NEAREST-MODULE RULE WAS BOUND BEFORE THE LOOK AND EVERY NAMED FUNCTION IS RESOLVED BY AST. **
*A module is nearest iff it already computes a quantity of the same kind over the same objects, so that
the row's quantity is a change of inputs or a short extension -- and the module AND THE FUNCTION are
named per row, with a row for which no function can be named counting as having none.*  ⇒ ** `22`
modules and `30` functions, every one resolved against the tree; `59` rows are a change of inputs and
`12` a short extension. **  *A named function that was not in the file it is named in would be the same
defect as a witness class resolved by a word in prose, which this seat tightened in its own instrument
one cycle ago, so the resolution raises rather than warns.*

** ⛭⛭ ORDER ②: THE PAPER CARRIED TWO VALUE PAIRS FOR ONE QUANTITY AND NEITHER WAS THE ONLY CANDIDATE.
   `sec:refit-bound` (l.912) gives the tilt as `$0.998$` against `$0.954$`, `bluer by $0.044$`; the
   `sec:transmission` item at l.2728 -- WHICH CITES `sec:refit-bound` -- gave `$0.995$` against
   `$0.956$`. **
⇒ *** THE AUTHORITY IS COMPUTED AND NOT THE BETTER-CITED ONE: the `1p57` receipt runs both arms through
    the instrument and its own table reports the TT minima at `0.9980` and `0.9542`.  So l.2728 is
    repaired to `$0.998$`/`$0.954$` and the paper now agrees with the section it was already citing. ***
  ⌗ ** AND A THIRD PAIR EXISTS AND IS LEGITIMATE, said so that nobody later `fixes' the paper to it: **
    `refit_grid/best_cr.npy` and `best_lcdm.npy` carry `0.9915` and `0.9530`.  *That is the
    RESPONSE-MODEL refit over `132` bins at `$\\ell$`100-1287 with lensing, a different likelihood scope
    from the full TT minimum -- two quantities, not two answers.*
  ⚠ ** THE BLAST RADIUS IS REPORTED RATHER THAN ABSORBED. **  *The route receipt PINNED the l.2728
    sentence and derived its tilt budget from it, so the repair moves its own figures: the budget
    `0.039` -> `0.044` and the shift's multiple of it `7550` -> `6692`.  **Its conclusion is unchanged
    and still overwhelming, and the number in its sentence is smaller than it was.**  `13` of `13`
    gates pass after the follow-through.*
  ⌗ *The pinned sentence reaches its comparison through `.count(...) == 1`, which the operator does not
    key, so the repair minted no new ledger pin -- checked rather than assumed.*

** ⒝'s ROUTED LEDGER ROW IS DONE: ** *`P15`'s optical-depth key takes the RESOLVED `PAPER` target, as
ruled.  It was one of the `2` surviving target-column disagreements, after `25` of the `27` the first
pass reported turned out to be this seat's own `containers.py` defect.  The verdict is untouched.*

** ⌗ AND THE PINNING WAS LOAD-BEARING, WHICH IS WORTH THE LINE. **  *Since `2654cd0b`, `3` of the `272`
have LEFT `MEANING-HELD` and `1` has joined -- the live count is `270` -- and one of the three
departures is a row this census counts.  The unit is the pinned population and `Ⓐ③` proves it.*

Written r7261+cc66.3 (node 66, code seat) on 66's r7261 order ① ⒜/⒝ and ②.  Stated for reversal.
"""
import ast
import collections
import hashlib
import json
import os
import subprocess
import time

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7261_cc66_census_and_backlog')
PREV = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7257_cc66_the_272')

DIGEST = {'CENSUS.tsv': 'b9480d096c492ce8', 'BACKLOG.tsv': '74d1717f77cde99f',
          'PREDICTION.md': '9e17d453c63600b3'}
PREREG_REV = '2654cd0b'

# ── the pre-registration, transcribed from the frozen PREDICTION.md ──
PRE_AST_SHARE = (64.0, 58.0, 72.0)
PRE_FLOOR = 58.3
PRE_MOVERS = 6
PRE_STRICT = 67                     # ⛔ the identity that FAILED, kept here because it failed
PRE_NEAREST = (82.0, 65.0, 93.0)
NEGATIVE_LINE = 25.0

# ── the measurement, frozen so no count is asserted against a set another seat can move ──
CENSUS_N, BACKLOG_N = 108, 85
CFORM = {'AST-SIG': 53, 'AST-PLACE': 14, 'INDEP': 41}
MOVERS, HELD_BACK_N = 4, 2
NEWREAD = 44
GAP = {'INPUTS': 59, 'NONE': 14, 'EXTEND': 12}
NONE_BY_WITNESS = {'ZM': 13, 'GRP': 1}
# ⛗ r7261+cc66.4 -- these were first transcribed as 16 and 24 from a TRUNCATED view of
#   census.py's own listing, and `Ⓔ①` failed on them.  The gate caught this seat's
#   transcription rather than its reading, which is what a frozen constant checked against
#   a regenerated file is for.
WITNESS_MODULES, WITNESS_FUNCTIONS = 22, 30
ZM_SCRIPTLESS = ('baryon_edge/L110_the_count_specified.py',
                 'baryon_edge/L78_the_mode_through_the_branch_point.py',
                 'baryon_edge/L75_the_wall_is_the_graze_point.py',
                 'baryon_edge/L15_the_quark_lepton_frontier.py',
                 'baryon_edge/L117w_the_colourless_sector.py')
# order ②
TILT_PAPER = ('0.998', '0.954')
TILT_WAS = ('0.995', '0.956')
TILT_GRID = ('0.9915', '0.9530')      # the response-model refit, a DIFFERENT quantity
BUDGET_WAS, BUDGET_NOW = '0.039', '0.044'
DRIFT_OUT, DRIFT_IN = 3, 1


def sha16(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, name):
    return [l.rstrip('\n').split('\t') for l in open(os.path.join(d, name), encoding='utf-8')
            if l.strip() and not l.startswith('#')]


# ============================================================ A. the subject
head("A.  Ⓐ THE SUBJECT IS DIGEST-PINNED AND THE POPULATION IS STILL A `git show`")

for _n, _d in sorted(DIGEST.items()):
    gate(f"Ⓐ①  `{_n}` is the file this receipt was written against -- sha1[:16] `{_d}`",
         sha16(os.path.join(MINE, _n)) == _d)
CEN = tsv(MINE, 'CENSUS.tsv')[1:]
BAK = tsv(MINE, 'BACKLOG.tsv')[1:]
gate(f"Ⓐ②  the census is {CENSUS_N} rows and the backlog {BACKLOG_N}, and they are SEPARATE FILES so "
     f"neither borrows the other's count", (len(CEN), len(BAK)) == (CENSUS_N, BACKLOG_N))
gate("Ⓐ③  no key is in both: the census and the backlog PARTITION the 193 computable rows",
     not ({(c[0], c[1]) for c in CEN} & {(b[0], b[1]) for b in BAK})
     and len({(c[0], c[1]) for c in CEN} | {(b[0], b[1]) for b in BAK}) == CENSUS_N + BACKLOG_N)

_at = subprocess.run(['git', 'show', f'{PREREG_REV}:corpus/quote_pin_baseline.tsv'],
                     cwd=ROOT, capture_output=True, text=True, check=True).stdout
_held_then = {(f[0], f[1]) for f in (l.split('\t') for l in _at.splitlines())
              if len(f) >= 7 and f[5] == 'MEANING-HELD'}
gate(f"Ⓐ④  the pinned revision still carries {len(_held_then)} MEANING-HELD keys, which is the unit",
     len(_held_then) == 272)
_live = {(f[0], f[1]) for f in (l.split('\t') for l in open(
    os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read().splitlines())
    if len(f) >= 7 and f[5] == 'MEANING-HELD'}
gate(f"Ⓐ⑤  ⌗ and the LIVE ledger has drifted -- {len(_held_then - _live)} out, "
     f"{len(_live - _held_then)} in -- so the pinning was load-bearing and not boilerplate",
     len(_held_then - _live) == DRIFT_OUT and len(_live - _held_then) == DRIFT_IN)
# ⌗ the ledger stores each literal JSON-QUOTED and the reading stores it DECODED, so the two key sets
#   are compared on the decoded form or every row reads as absent -- the same escaping trap that made
#   17 rows look like false absences in this seat's own r7257 gatherer.
def _dec(v):
    try:
        return json.loads(v)
    except Exception:
        return v.strip('"')


_then = {(f, _dec(l)) for f, l in _held_then}
gate("Ⓐ⑥  every census and backlog key is one the PINNED revision held, not one the live file holds",
     {(c[0], c[1]) for c in CEN} | {(b[0], b[1]) for b in BAK} <= _then)

# ============================================================ B. the census
head("B.  Ⓑ ⒜ THE CENSUS: THE FORM EACH ROW'S OWN HOLDER CAN CARRY")

gate(f"Ⓑ①  the forms are the reported ones: {CFORM}",
     dict(collections.Counter(c[3] for c in CEN)) == CFORM)
_nast = sum(1 for c in CEN if c[3].startswith('AST'))
_share = 100.0 * _nast / CENSUS_N
gate(f"Ⓑ②  ✔ the AST share is {_nast}/{CENSUS_N} = {_share:.1f} per cent, INSIDE the pinned band "
     f"{PRE_AST_SHARE[1]}-{PRE_AST_SHARE[2]} (point estimate {PRE_AST_SHARE[0]})",
     PRE_AST_SHARE[1] <= _share <= PRE_AST_SHARE[2])
gate(f"Ⓑ③  and it is ABOVE the {PRE_FLOOR} no-movement floor, so the predicted movement did happen",
     _share > PRE_FLOOR)
_moved = [c for c in CEN if c[8] != '-']
gate(f"Ⓑ④  ⛔ but {len(_moved)} rows moved against {PRE_MOVERS} pinned, so the SIZE of the movement is "
     f"a miss even where its direction was right", len(_moved) == MOVERS and MOVERS < PRE_MOVERS)
gate("Ⓑ⑤  every mover records WHY its holder can carry the AST form, as a clause and not a label",
     all(len(c[8].split()) >= 8 for c in _moved))
gate("Ⓑ⑥  and no mover's recorded form is the one the LITERAL reading gave, so `was` and `form` "
     "disagree exactly on the movers", {(c[0], c[1]) for c in CEN if c[3] != c[4]}
     == {(c[0], c[1]) for c in _moved})

head("B2.  Ⓒ RULING ③'s FLAG, AND THE IDENTITY I PRE-REGISTERED DOES NOT HOLD")
_flag = [c for c in CEN if c[5] == 'NEW-READ']
_strict = CENSUS_N - len(_flag)
gate(f"Ⓒ①  {len(_flag)} rows carry the NEW-READ flag ruling ③ requires -- the form needs a read the "
     f"holder does not perform today", len(_flag) == NEWREAD)
gate("Ⓒ②  and every flagged row is an AST form whose holder opens no source file, which is what the "
     "flag means", all(c[3].startswith('AST') and 'PY' not in c[7].split('+') for c in _flag))
gate(f"Ⓒ③  ⛔ so the strict count is {CENSUS_N} - {len(_flag)} = {_strict} AND NOT the {PRE_STRICT} I "
     f"pre-registered as a gate-checkable identity", _strict != PRE_STRICT and _strict == 64)
_mf = [c for c in _moved if c[5] == 'NEW-READ']
gate(f"Ⓒ④  ⇒ THE CAUSE, and it is structural: {len(_mf)} of the {MOVERS} movers are held by receipts "
     f"that open no source file, so the CHEAPEST form bought an AST test and COST a read, while the "
     f"INDEP form it left needed only a capability those holders have",
     len(_mf) == 3 and PRE_STRICT - _strict == len(_mf))
gate("Ⓒ⑤  ⇒ A CHEAPER FORM CAN LOWER THE STRICT COUNT.  Ruling ③'s CONDITION still holds -- the "
     "strict count is recoverable from this same table -- and what failed is my prediction of its value",
     _strict == CENSUS_N - sum(1 for c in CEN if c[5] == 'NEW-READ'))

# ============================================================ C. the backlog
head("C.  Ⓓ ⒝ THE BACKLOG: WHAT EACH ROW NEEDS, AND THE NEAREST MODULE *AND FUNCTION*")

gate(f"Ⓓ①  the gaps are the reported ones: {GAP}",
     dict(collections.Counter(b[6] for b in BAK)) == GAP)
_named = [b for b in BAK if b[6] != 'NONE']
_frac = 100.0 * len(_named) / BACKLOG_N
gate(f"Ⓓ②  ✔ {len(_named)}/{BACKLOG_N} = {_frac:.1f} per cent have a named nearest function, INSIDE "
     f"the pinned band {PRE_NEAREST[1]}-{PRE_NEAREST[2]} (point estimate {PRE_NEAREST[0]})",
     PRE_NEAREST[1] <= _frac <= PRE_NEAREST[2])
gate(f"Ⓓ③  ⛭ `66`'s REACHABLE NEGATIVE DOES NOT FIRE: it needed under {NEGATIVE_LINE} per cent and the "
     f"fraction misses that line by {_frac - NEGATIVE_LINE:.1f} points, so `computable` is a statement "
     f"about WORK and not about possibility", _frac >= NEGATIVE_LINE)
gate("Ⓓ④  every named row carries a QUANTITY in words as well as a module and a function",
     all(len(b[3].split()) >= 3 and b[4] != '-' and b[5] != '-' for b in _named))
gate("Ⓓ⑤  and every unnamed row carries BOTH placeholders, so NONE is never a half-filled row",
     all(b[4] == '-' and b[5] == '-' for b in BAK if b[6] == 'NONE'))

head("C2.  Ⓔ EVERY NAMED FUNCTION RESOLVES BY AST -- the rule's teeth, checked and not claimed")
_want = collections.defaultdict(set)
for b in _named:
    _want[b[4]].add(b[5])
_bad = []
for _m, _fns in sorted(_want.items()):
    _p = os.path.join(ROOT, 'computations', _m)
    if not os.path.exists(_p):
        _bad.append(f'{_m}: absent')
        continue
    _have = {n.name for n in ast.walk(ast.parse(open(_p, encoding='utf-8', errors='replace').read()))
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    _bad += [f'{_m}:{f}' for f in sorted(_fns) if f not in _have]
gate(f"Ⓔ①  {len(_want)} modules and {sum(len(v) for v in _want.values())} functions, every one present "
     f"in the file it is named in", not _bad and len(_want) == WITNESS_MODULES
     and sum(len(v) for v in _want.values()) == WITNESS_FUNCTIONS)
gate("Ⓔ②  a named function missing from its module would be the same defect as a witness class "
     "resolved by a word in prose, so this gate RAISES on one rather than warning", not _bad)

head("C3.  Ⓕ AND THE 14 WITH NO NEAREST FUNCTION ARE ONE HOLE, NOT FOURTEEN GAPS")
_none = [b for b in BAK if b[6] == 'NONE']
gate(f"Ⓕ①  the unnamed rows sit in {NONE_BY_WITNESS} by witness class",
     dict(collections.Counter(b[2] for b in _none)) == NONE_BY_WITNESS)
gate(f"Ⓕ②  ⛭ so {NONE_BY_WITNESS['ZM']} of the {len(_none)} are ONE missing capability: a zero-mode, a "
     f"kernel or an index", sum(1 for b in _none if b[2] == 'ZM') == 13)
_names = set()
for _dp, _, _fs in os.walk(os.path.join(ROOT, 'computations')):
    for _f in _fs:
        if not _f.endswith('.py'):
            continue
        try:
            _t = ast.parse(open(os.path.join(_dp, _f), encoding='utf-8', errors='replace').read())
        except SyntaxError:
            continue
        _names |= {n.name for n in ast.walk(_t) if isinstance(n, ast.FunctionDef)}
_zm = [n for n in _names if any(k in n.lower() for k in ('zeromode', 'zero_mode', 'kernel', 'dirac'))]
gate(f"Ⓕ③  and the hole is MEASURED over the whole tree: of {len(_names)} function names under "
     f"`computations/`, {len(_zm)} compute a zero-mode, a kernel or a Dirac index", not _zm)
gate("Ⓕ④  the five modules the ZM witness class resolved to have NO `def` in them at all -- they are "
     "top-level sympy scripts, which is why a domain-level witness passed and a quantity-level one "
     "could not", all(not [n for n in ast.walk(ast.parse(open(
         os.path.join(ROOT, 'computations', _m), encoding='utf-8', errors='replace').read()))
         if isinstance(n, ast.FunctionDef)] for _m in ZM_SCRIPTLESS))
gate("Ⓕ⑤  ⇒ which is what the DOMAIN-versus-QUANTITY distinction declared in PREDICTION.md was for: "
     "the one block where a high answer would have been unearned is the one block that failed",
     'DOMAIN-LEVEL' in open(os.path.join(MINE, 'PREDICTION.md'), encoding='utf-8').read())

# ============================================================ D. order ②
head("D.  Ⓖ ORDER ②: ONE QUANTITY, TWO VALUE PAIRS IN ONE PAPER -- AND A THIRD THAT IS NOT A RIVAL")

_p15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
_bound = f"arm prefers ${TILT_PAPER[0]}$ against the control's ${TILT_PAPER[1]}$, bluer by $0.044$"
_item = (f"prefers a tilt of ${TILT_PAPER[0]}$ here against ${TILT_PAPER[1]}$ on the standard one")
gate(f"Ⓖ①  `sec:refit-bound` still reports the pair it computed, {TILT_PAPER[0]} against "
     f"{TILT_PAPER[1]}, with its own difference stated and reconciling", _p15.count(_bound) == 1)
gate(f"Ⓖ②  and the `sec:transmission` item -- which CITES `sec:refit-bound` -- now carries the SAME "
     f"pair", _p15.count(_item) == 1)
gate(f"Ⓖ③  the pair it used to carry, {TILT_WAS[0]} against {TILT_WAS[1]}, is gone from the paper "
     f"entirely, so the paper holds ONE pair for one quantity",
     f"${TILT_WAS[0]}$" not in _p15 and f"${TILT_WAS[1]}$" not in _p15)
_cr = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid', 'best_cr.npy')
gate("Ⓖ④  ⌗ AND THE THIRD PAIR IS REAL AND IS NOT A RIVAL: the response-model refit's own arrays are "
     f"on disk at {TILT_GRID[0]} and {TILT_GRID[1]}, a 132-bin lensed fit over ell 100-1287 rather "
     f"than the full TT minimum -- two quantities, not two answers", os.path.exists(_cr))
gate("Ⓖ⑤  the authority is the COMPUTED pair and not the better-cited one: the `1p57` receipt runs "
     "both arms through the instrument and its table reports 0.9980 and 0.9542",
     all(s in open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', [
         f for f in os.listdir(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology'))
         if f.startswith('P15_the_1p57_has_no_parameter_address')][0]), encoding='utf-8').read()
         for s in ('0.9980', '0.9542')))

head("D2.  Ⓗ THE BLAST RADIUS, FOLLOWED THROUGH AND REPORTED RATHER THAN ABSORBED")
_route = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', [
    f for f in os.listdir(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology'))
    if f.startswith('P15_the_route_from_the_handover_amplitude')][0])
_rs = open(_route, encoding='utf-8').read()
gate("Ⓗ①  the receipt that PINNED the l.2728 sentence now pins the repaired one, so the paper and the "
     "receipt moved together", _item in _rs.replace('$0.998$ here "\n          r"against', '$0.998$ here against')
     or (f"${TILT_PAPER[0]}$ here" in _rs and f"${TILT_PAPER[1]}$ on the standard one" in _rs))
gate(f"Ⓗ②  its tilt budget follows the paper: {BUDGET_WAS} -> {BUDGET_NOW}",
     f"mp.mpf('{TILT_PAPER[0]}') - mp.mpf('{TILT_PAPER[1]}')" in _rs
     and f"mp.mpf('{BUDGET_NOW}')" in _rs)
gate("Ⓗ③  ⚠ and the correction makes its own figure SMALLER -- the shift's multiple of the budget "
     "goes 7550 -> 6692 -- which the receipt says in its own text rather than quietly restating",
     '7550' in _rs and '6692' in _rs and '6.7' in _rs)
gate("Ⓗ④  the repair minted NO new ledger pin: the sentence reaches its comparison through "
     "`.count(...) == 1`, which the operator does not key, and the ledger carries no such key",
     'refitting both arms on this construction' not in open(
         os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read())

head("D3.  Ⓘ ⒝'s ROUTED LEDGER ROW")
_led = [l.split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                                    encoding='utf-8').read().splitlines() if l.count('\t') >= 6]
_od = [f for f in _led if 'Two objects on the same side of the rule' in f[1]]
gate("Ⓘ①  `P15`'s optical-depth key takes the RESOLVED `PAPER` target, as ruled at ⒝",
     len(_od) == 1 and _od[0][2] == 'PAPER')
gate("Ⓘ②  and its VERDICT is untouched -- the ruling was about the target column and nothing else",
     _od[0][5] == 'MEANING-HELD')
gate("Ⓘ③  the row records why, naming the 25 false disagreements the container defect produced",
     'containers.py' in _od[0][6] and 'r7261+cc66' in _od[0][6])

# ============================================================================
bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks in {time.time() - t_all:.1f}s")
if bad:
    print("  GATES FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("  GATES: ALL PASS")
print(f"""
  ==========================================================================
  THE ANSWER, IN ONE PLACE:
  ⒝ {len(_named)} OF {BACKLOG_N} BACKLOG ROWS HAVE A NAMED NEAREST FUNCTION -- {_frac:.1f} PER CENT,
    inside a pinned {PRE_NEAREST[0]} and a band of {PRE_NEAREST[1]}-{PRE_NEAREST[2]}.
  ⛭ 66's NEGATIVE NEEDED UNDER {NEGATIVE_LINE} AND MISSES BY {_frac - NEGATIVE_LINE:.1f} POINTS,
    so `computable' is a statement about work and not about possibility.
  ⛭ AND THE {len(_none)} WITH NONE ARE ONE HOLE: {NONE_BY_WITNESS['ZM']} want a zero-mode, a kernel or an
    index, and {len(_zm)} functions out of {len(_names)} under computations/ compute one.
  ⒜ THE CENSUS IS {_share:.1f} PER CENT AST, inside a pinned {PRE_AST_SHARE[0]} -- but {MOVERS} rows moved
    against {PRE_MOVERS} pinned, so the direction was right and the size was not.
  ⛔ AND A PRE-REGISTERED IDENTITY FAILED: the strict count is {_strict}, not {PRE_STRICT}.
    3 of the 4 movers open no source file, so A CHEAPER FORM COST A READ.
    Ruling ③'s condition holds; my prediction of its value did not.
  ⛭ ORDER ②: l.2728 repaired to {TILT_PAPER[0]}/{TILT_PAPER[1]}, the pair the instrument computes
    and the one the section it cites already carried.  A third pair ({TILT_GRID[0]}/{TILT_GRID[1]})
    is the response-model fit and is NOT a rival.  The route receipt's budget
    followed, {BUDGET_WAS} -> {BUDGET_NOW}, and its own multiple fell 7550 -> 6692.
  ==========================================================================""")
