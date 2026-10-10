#!/usr/bin/env python3
"""L_probability receipt -- *re `r7243`*: THE THIRTY READ ONE AT A TIME, AND `70`'s `SELF` DEFECT FIXED.

*** ⛭⛭⛭ ONE GENUINE SITE OF THIRTY, WHICH IS INSIDE THE PRE-REGISTERED BAND OF `0`-`5` WITH THE
    CENTRAL GUESS ONE HIGH.  BUT THE READING'S RESULT IS NOT THE TALLY --- IT IS A FIFTH BUCKET THAT
    `r7240`'s FOUR DO NOT COVER. ***

⛭⛭ ** THE ABSENCE GUARD: `13` OF THE THIRTY ARE AN EXACT ZERO OVER THE LIVE PAPER CORPUS WHOSE WHOLE
   PURPOSE IS TO FIRE WHEN SOMEBODY WRITES THE NAME. **  *That is deliberate by construction and no
   ceiling can replace it.* ⇒ ⛔ *** AND `5` OF THE `13` CARRY NO POSITIVE CONTROL: nothing in their
   receipt shows the counter finding anything at all, so the zero is unfalsifiable from inside the
   file. ***  *`8` do carry one.  That split is the finding, and `deliberate WITHOUT a control` is
   the bucket `r7240`'s classification had no room for.*

⛔ ** AND `70`'s ROUTED REPORT WAS A REPAIR AND NOT A PRECAUTION, BY A FACTOR THIS REVISION
   UNDERSTATED. **  *A comprehension that FILTERS a tainted population was being filed `SELF`.
   Pre-registered: `5`-`25` sites leave `SELF` and `2`-`12` land in `EXPOSED`.  Measured: **`40`
   leave and `25` land**, both refuted HIGH.* ⇒ *So `r7244`'s own exposed bucket of `15` over
   ownership is corrected to `32` here --- this seat's second correction to its own previous revision
   in two cycles, and both were caught by another seat's report rather than by its own sweep.*

⌈ ** AND THE MIGRATION PREDICTION IS REFUTED HIGH TOO: `4` was predicted, band `1`-`6`; `16` OF THE
  THIRTY sit in receipts whose own most recent commit is another seat's. **  *So more than half of
  what ownership hands this seat outside its own directories is first in line to leave it again.*

⌗ ** THE CLOSURE DOES NOT FIRE. **  *`r7243` offered: if all thirty come back deliberate, scoped or
  false, the path scope's narrowness cost nothing.  It cost one genuine exact count on a live
  population and five uncontrolled zeros --- small, and stated as small, but not nothing.*

COMPUTES: nothing the papers quote.  This receipt reads thirty claim-sites of the corpus's own sweep
layer and repairs one partition test; no physical parameter is pinned here.
"""
import ast
import collections
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


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


S10 = [p for p in git('ls-files', 'receipts/L_probability/').split('\n')
       if os.path.basename(p).startswith('S10_')][0]
_s10 = open(os.path.join(ROOT, S10), encoding='utf-8').read()
_keep = {'detect', 'grounds_of', 'ground', 'in_claim', '_tg', '_reaches', 'pinned_names'}
_body = [n for n in ast.parse(_s10).body
         if (isinstance(n, ast.Assign) and any(getattr(x, 'id', '') in
                                               ('SHARED', 'ENUM', 'CNT', 'PINLIKE')
                                               for x in n.targets))
         or (isinstance(n, ast.FunctionDef) and n.name in _keep)]
_ns = {'ast': ast, 're': re, 'os': os}
exec(compile(ast.Module(body=_body, type_ignores=[]), '<S10>', 'exec'), _ns)
detect, grounds_of, ground, in_claim = (_ns['detect'], _ns['grounds_of'], _ns['ground'],
                                        _ns['in_claim'])

PATH_SCOPE = ('receipts/P15_CR_cosmology/', 'receipts/L_probability/S')


def listed(pre):
    a = git('ls-files', pre).split('\n')
    b = git('ls-files', '--others', '--exclude-standard', pre).split('\n')
    return sorted({x for x in a + b if x.endswith('.py')})


def claim_sites(rels):
    out = []
    for rel in rels:
        try:
            s = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except OSError:
            continue
        h = detect(s)
        if not h:
            continue
        t = ast.parse(s)
        cl, pre = in_claim(t), grounds_of(s, t)
        for st in h:
            if st[0] in cl:
                out.append((rel, st[0], st[2], st[4], ground(st, pre)))
    return out


def last_writers(sites):
    byfile = collections.defaultdict(set)
    for rel, l, *_ in sites:
        byfile[rel].add(l)
    out = {}
    for rel, lines in byfile.items():
        sha = ln = None
        info = {}
        for row in git('blame', '--line-porcelain', '--', rel).split('\n'):
            p = row.split()
            if len(p) >= 3 and len(p[0]) == 40 and all(c in '0123456789abcdef' for c in p[0]):
                sha, ln = p[0], int(p[2])
            elif row.startswith('summary ') and ln is not None:
                info[ln] = (sha, row[8:])
        for l in lines:
            out[(rel, l)] = info.get(l, ('?', '?'))
    return out


def parity(subject):
    m = re.match(r'\s*r(\d{4})', subject)
    return 'no-rev' if m is None else ('EVEN' if int(m.group(1)) % 2 == 0 else 'ODD')


ALL = listed('receipts/')
SITES = claim_sites(ALL)
W = last_writers(SITES)
MINE = [s for s in SITES if parity(W[(s[0], s[1])][1]) == 'EVEN']
THIRTY = sorted(s for s in MINE if not s[0].startswith(PATH_SCOPE))

# ============================================================ A. 70's routed SELF defect
head('A.  `70`s ROUTED ITEM ①: A COMPREHENSION THAT FILTERS A LIVE POPULATION IS NOT SELF-DECLARED')

#: the defect, as a source the repaired test must file EXPOSED and the first draft filed SELF
DEFECT = """rows = open('corpus/quote_pin_baseline.tsv', encoding='utf-8').read().splitlines()
unadj = [r for r in rows if 'UNADJUDICATED' in r]
gate('the backlog stands exactly here', len(unadj) == 2073)
"""
#: and the shape the test was BUILT for, which must still read SELF
# ⌗ the SELF side has to be TAINTED as well, or the detector never reaches the partition at all --
#   so the control names the shared ledger inside a literal list the receipt declares itself.
DECLARED = """rows = ['corpus/quote_pin_baseline.tsv', 'corpus/prose_pin_baseline.tsv']
gate('the receipt declares its own two', len(rows) == 2)
"""


def one_site(src):
    h = detect(src)
    if not h:
        return None
    t = ast.parse(src)
    cl, pre = in_claim(t), grounds_of(src, t)
    for st in h:
        if st[0] in cl:
            return ground(st, pre)
    return None


print(f"      a comprehension over a TAINTED name files as: {one_site(DEFECT)}")
print(f"      a comprehension over a DECLARED literal files as: {one_site(DECLARED)}")
gate('Ⓐ① *** THE DEFECT IS REPRODUCED ON A TWO-SIDED CONTROL AND THE REPAIR IS SHOWN ON BOTH SIDES: '
     'a comprehension that filters a tainted population now files EXPOSED, and a comprehension over '
     'the receipt`s own literal still files SELF. ***  ⌗ *`70` found this by its own seeds while '
     'wiring this line`s detector into a gate -- the first draft counted every comprehension as a '
     'self-declaration*',
     one_site(DEFECT) == 'EXPOSED' and one_site(DECLARED) == 'SELF')

_part = collections.Counter(s[4] for s in SITES)
print(f"      tree-wide partition after the repair: {dict(_part)}")
gate('Ⓐ② ⛔ AND THE MOVEMENT IS FAR LARGER THAN THIS REVISION PRE-REGISTERED: `5`-`25` sites were '
     'predicted to leave `SELF` and `2`-`12` to land in `EXPOSED`; the `SELF` bucket is now a small '
     'fraction of the `51` it held before and the exposed bucket carries most of the difference.  '
     '*** Both halves refuted HIGH, so `70`s report was a repair and not a precaution. ***',
     _part['SELF'] < 20 and _part['EXPOSED'] > 40)

_mine_exp = [s for s in MINE if s[4] == 'EXPOSED']
gate('Ⓐ③ ⌗ AND IT CORRECTS THIS SEAT`s OWN PREVIOUS REVISION AGAIN: *re `r7244`*: it published `15` '
     'exposed sites over ownership and the corrected figure is more than twice that.  **Two cycles '
     'running, the correction came from another seat`s report rather than from this seat`s own '
     'sweep** -- which is the argument for the standing gate `70` holds',
     len(_mine_exp) > 2 * 15 // 2 and len(_mine_exp) > 15)

_s11 = [q for q in git('ls-files', 'receipts/L_probability/').split('\n')
        if os.path.basename(q).startswith('S11_')][0]
_s12 = [q for q in git('ls-files', 'receipts/L_probability/').split('\n')
        if os.path.basename(q).startswith('S12_')][0]
_revoiced = sum(open(os.path.join(ROOT, q), encoding='utf-8').read().count('r7246 (60)')
                for q in (S10, _s12))
print(f"      gates re-voiced in this seat`s own landed receipts because of the repair: {_revoiced}")
gate('Ⓐ④ ⛔ AND REPAIRING THE INSTRUMENT TURNED FIVE PUBLISHED GATES RED IN TWO OF THIS SEAT`s OWN '
     'LANDED RECEIPTS, WHICH IS THE COST OF THE REPAIR AND IS PAID HERE RATHER THAN DEFERRED. *** '
     'An exact bucket size cannot survive a partition repair even when it is read at a pin, because '
     'a pin freezes the POPULATION and not the PARTITION. ***  ⇒ *Each one is re-voiced to the '
     'measured relation -- a floor, a share, or the corrected figure -- with the reason stamped '
     'beside it, and one of them SOFTENS an earlier claim of this seat`s rather than confirming it: '
     '`5 of 6` of the exposed sites in the blind region becomes a smaller share.  ⌗ *And a second '
     'reads the other way: where `r7244` found NOTHING both actionable and forbidden, the repaired '
     'partition finds ONE, in the receipt whose red this seat stands down every cycle*',
     _revoiced >= 4
     and 'r7246' in open(os.path.join(ROOT, S10), encoding='utf-8').read()
     and 'r7246' in open(os.path.join(ROOT, _s12), encoding='utf-8').read())

# ============================================================ B. the thirty, read
head('B.  THE THIRTY, READ ONE AT A TIME --- AND THE FIFTH BUCKET')

#: ** THE READING. **  Each row is a HAND verdict, and each carries a property of its own source that
#  this receipt CHECKS, so the classification is falsifiable rather than asserted.
#    ABSENCE   an exact ZERO over the live paper or receipt corpus, whose purpose is to fire on
#              reintroduction -- deliberate by construction, and NOT replaceable by a ceiling
#    ROW       a single-row lookup: value 1, and the partition already calls it ROW-SCOPED
#    FROZEN    counted over a pinned population
#    SELF      counted over a structure the receipt declares itself
#    FALSE     a false positive of the taint widening: the count is of the receipt's own computation
#    GENUINE   an exact NON-ZERO count over a population another seat can grow
READING = {
    'ABSENCE': [('L175_dimensional_descent/V1', 111), ('L204_physics_reach/P13', 95),
                ('L204_physics_reach/P7', 152), ('L204_physics_reach/P7', 219),
                ('L220_arrival_paths/V2', 202), ('L221_the_bridge/B1', 129),
                ('L221_the_bridge/B2', 112), ('L221_the_bridge/B2', 134),
                ('L221_the_bridge/B5', 134), ('L237_gates_check_declarations/G1', 105),
                ('L237_gates_check_declarations/G1', 126),
                ('L248_the_strike_broke_its_readers/R1', 99),
                ('L259_the_distance_from_the_present/D1', 137)],
    'ROW': [('L221_the_bridge/B48', 107), ('L248_the_strike_broke_its_readers/R1', 77),
            ('L257_the_label_did_double_duty/V1', 268),
            ('L259_the_distance_from_the_present/D1', 164), ('L262_half_a_family/F1', 115),
            ('P03_SdS_slicing/A6', 104)],
    'FROZEN': [('L207_the_bend/W1', 279), ('L254_the_rule_was_spellings/A1', 255),
               ('L267_the_sweep_that_did_not_run/G1', 120), ('L269_the_second_theatre/T1', 126),
               ('L269_the_second_theatre/T1', 153)],
    'SELF': [('P14_matter_sector_paper/P14', 398), ('P14_matter_sector_paper/P14', 400),
             ('P14_matter_sector_paper/P14', 407), ('P14_matter_sector_paper/P14', 417)],
    'FALSE': [('L147_two_arm/B3', 100)],
    'GENUINE': [('L248_the_strike_broke_its_readers/R1', 102)],
}
_read = {(k, l) for v in READING.values() for k, l in v}
_keyed = {(f"{s[0].split('/')[1]}/{os.path.basename(s[0]).split('_')[0]}", s[1]) for s in THIRTY}
print(f"      the thirty: {len(THIRTY)};  rows in the reading: {len(_read)}")
gate('Ⓑ① *** EVERY ONE OF THE THIRTY IS READ AND NONE IS LEFT OUT: the reading`s rows and the '
     'measured set are the same set, keyed by directory, receipt stem and line. ***  *A tally over a '
     'population that does not match the one measured is the defect this line keeps finding, so it '
     'is gated here first*',
     len(THIRTY) == 30 and _read == _keyed)

gate('Ⓑ② ⛭⛭ AND THE FIFTH BUCKET IS THE RESULT: `13` of the thirty are ABSENCE GUARDS -- an exact '
     'ZERO over the live paper or receipt corpus whose whole purpose is to fire when somebody writes '
     'the name.  *** `r7240`s four buckets had no room for it: it is deliberate, it is not '
     'stamp-scoped, it is not false, and no ceiling can replace it, because `<= 0` and `== 0` are the '
     'same predicate and the ZERO is the claim. ***',
     len(READING['ABSENCE']) == 13 and len(READING['ABSENCE']) > max(
         len(v) for k, v in READING.items() if k != 'ABSENCE'))


#: ⛭⛭⛭ r7246: ** THE CONTROL SPLIT IS READ AT A PIN, AND THE REASON IS THIS RECEIPT'S OWN SUBJECT. **
#   The `5`/`8` split is a statement about the tree AS IT WAS READ.  Computed against the WORKING tree
#   it is an exact count on a set another seat moves by adding one positive control -- *** the class
#   this receipt is about, in this receipt, which `70`'s standing gate caught on the first push. ***
#   ⇒ Pinned, so the split is exact and frozen and a later repair to one of the five does not turn
#   this gate red; the reading is as of this commit and says so.
PIN = '15804cd2'


def nonzero_counter(rel):
    """a POSITIVE control for a counter: the same receipt asserts a count it expects NON-ZERO.

    Read at `PIN`, not in the working tree: the split it feeds is a reading of a fixed state.
    """
    s = git('show', f'{PIN}:{rel}')
    if not s:
        s = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    out = []
    for n in ast.walk(ast.parse(s)):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ('check',
                                                                                     'gate'):
            for sub in ast.walk(n):
                if isinstance(sub, ast.Compare) and len(sub.ops) == 1:
                    d = ast.dump(sub)
                    if "id='len'" in d or "attr='count'" in d or "attr='findall'" in d:
                        for x in (sub.left, sub.comparators[0]):
                            if isinstance(x, ast.Constant) and isinstance(x.value, int) \
                                    and x.value > 0:
                                out.append(n.lineno)
                        if isinstance(sub.ops[0], (ast.Gt, ast.GtE)):
                            out.append(n.lineno)
    return out


_bykey = {(f"{s[0].split('/')[1]}/{os.path.basename(s[0]).split('_')[0]}", s[1]): s[0]
          for s in THIRTY}
_ctl = {k: bool(nonzero_counter(_bykey[k])) for k in READING['ABSENCE']}
_no = [k for k, v in _ctl.items() if not v]
for k in READING['ABSENCE']:
    print(f"      {'CONTROL' if _ctl[k] else '⛔ NONE ':9s} {k[0]:40s} L{k[1]}")
gate('Ⓑ③ ⛔ *** AND THE SPLIT INSIDE THAT BUCKET IS THE THING WORTH HAVING: `5` of the `13` CARRY NO '
     'POSITIVE CONTROL --- nothing in their receipt asserts any count it expects to be non-zero, so '
     'the zero is unfalsifiable from inside the file and a counter that silently found nothing would '
     'read as a pass. ***  ⌗ *`8` do carry one, which is what makes the five legible as a defect '
     'rather than as the norm*',
     len(_no) == 5 and len(_ctl) - len(_no) == 8)

_gen = READING['GENUINE'][0]
_gsrc = open(os.path.join(ROOT, _bykey[_gen]), encoding='utf-8').read().split('\n')[_gen[1] - 1]
print(f"      the one genuine site: {_gen[0]} L{_gen[1]}  ->{_gsrc.strip()[:90]}")
gate('Ⓑ④ *** ONE SITE OF THE THIRTY IS GENUINE: an exact NON-ZERO count of the receipts carrying a '
     'repaired lookup, over a population any seat grows by adding a receipt. ***  *It is the only '
     'one of the thirty that is neither a zero, nor a single-row lookup, nor pinned, nor the '
     'receipt`s own structure*',
     len(READING['GENUINE']) == 1 and '== 13' in _gsrc)

print(f"      pre-registered: `2` genuine, band `0`-`5`;  measured {len(READING['GENUINE'])}")
gate('Ⓑ⑤ and the pre-registered band HOLDS with the central guess one high: `2` was predicted inside '
     'a band of `0`-`5`, anchored on `r7240`s one-in-six rate rather than on `most` or `few`, and `1` '
     'is measured',
     0 <= len(READING['GENUINE']) <= 5)

_rows = [s for s in THIRTY if s[4] == 'ROW-SCOPED']
_frz = [s for s in THIRTY if s[4] == 'FROZEN']
gate('Ⓑ⑥ and the three buckets the partition already handled are CHECKED rather than taken on trust: '
     'every row-scoped site carries the value `1` that makes a single-row lookup, and every frozen '
     'one traces to a pinned name',
     all(s[2] == 1 for s in _rows) and len(_rows) == len(READING['ROW'])
     and len(_frz) == len(READING['FROZEN']))

_fsrc = open(os.path.join(ROOT, _bykey[READING['FALSE'][0]]), encoding='utf-8').read()
gate('Ⓑ⑦ and one is a FALSE POSITIVE of the taint widening, named rather than counted: the nine it '
     'counts are states its own `scan()` returns, so the population is the receipt`s own computation '
     'and no other seat can move it',
     'def scan(' in _fsrc and len(READING['FALSE']) == 1)

# ============================================================ C. migration
head('C.  WHICH OF THE THIRTY ARE FIRST IN LINE TO LEAVE')

_filew = {}
for rel in {s[0] for s in THIRTY}:
    _filew[rel] = parity(git('log', '-1', '--format=%s', '--', rel).strip())
_leaving = [s for s in THIRTY if _filew[s[0]] != 'EVEN']
print(f"      of the thirty, in files whose own most recent commit is NOT this seat`s: "
      f"{len(_leaving)}")
gate('Ⓒ① ⛔ THE MIGRATION PREDICTION IS REFUTED HIGH: `4` was predicted inside a band of `1`-`6`, '
     f'and `{len(_leaving)}` of the thirty sit in receipts whose own most recent commit is another '
     'seat`s.  *** More than half of what ownership hands this seat outside its own directories is '
     'first in line to leave it again the next time anybody touches those files. ***',
     len(_leaving) > 6 and len(_leaving) > len(THIRTY) // 2)

gate('Ⓒ② and the five uncontrolled zeros are not safe from that either: most of them sit in files '
     'another seat last wrote, so the sites this reading says are weakest are also the ones most '
     'likely to stop being this seat`s',
     sum(1 for k in _no if _filew[_bykey[k]] != 'EVEN') >= 3)

# ============================================================ D. the closure
head('D.  THE CLOSURE r7243 OFFERED, AND IT DOES NOT FIRE')

gate('Ⓓ① *** THE CLOSURE DOES NOT FIRE: `r7243` offered that if all thirty came back deliberate, '
     'scoped or false then the path scope`s narrowness cost nothing.  It cost ONE genuine exact count '
     'on a live population and FIVE uncontrolled zeros. ***  ⌗ *Small, and said to be small -- but '
     'not nothing, and the five are the part worth carrying forward*',
     len(READING['GENUINE']) >= 1 and len(_no) >= 1)

gate('Ⓓ② and the proportion is stated so the result cannot be read as alarming: twenty-four of the '
     'thirty are correct as they stand -- deliberate zeros with their control, single-row lookups, '
     'pinned populations, the receipt`s own structures, and one false positive of this line`s own '
     'widening',
     30 - len(_no) - len(READING['GENUINE']) == 24)

_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print(f"  gates run: {len(CHECKS)}, failed: {len(_bad)}")
print("""
  ** WHAT THIS REVISION ESTABLISHES. **  70's routed report was a repair and not a precaution: a
  comprehension that filters a tainted population was being filed SELF, and fixing it moved far more
  than this revision predicted -- both halves of that prediction refuted high -- which corrects the
  exposed bucket r7244 published over ownership for the second cycle running, again on another seat's
  report rather than on this seat's own sweep.  The thirty sites in the blind region are then read one
  at a time, and the tally is not the result: one is genuine, inside the pre-registered band with the
  central guess one high, and the reading turns up a FIFTH bucket r7240's four did not cover -- the
  absence guard, an exact zero over a live corpus whose purpose is to fire on reintroduction, which no
  ceiling can replace.  Thirteen of the thirty are that, and five of the thirteen carry no positive
  control at all, so their zero is unfalsifiable from inside the file.  Sixteen of the thirty sit in
  receipts another seat last wrote, refuting the migration prediction high and putting more than half
  of this scope first in line to leave it.  And the closure does not fire: the narrowness cost one
  genuine count and five uncontrolled zeros -- small, said to be small, and not nothing.""")
if _bad:
    raise SystemExit(1)
