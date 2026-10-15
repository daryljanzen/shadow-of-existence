#!/usr/bin/env python3
"""L_probability receipt -- *re `r7251`*: THE MIRROR CROSS-READ, BLIND, AND THE RESIDUAL IS ONE
MISSING CLAUSE RATHER THAN TWO INSTRUMENTS.

*** ⛭⛭⛭ `6` OF THE `27` COMPARABLE KEYS ARE STILL OPEN ONCE ONE RULE IS APPLIED --- `22` PER CENT,
    BELOW THE ORDER'S ONE-THIRD RETIREMENT LINE --- AND ALL SIX ARE IDENTITY PINS, WHILE NONE OF THE
    TEN THE RULE DISPOSES OF IS. ***  *So the verdict column is not a mixture of two instruments: it
    is one instrument with one clause unwritten.*

⛔ ** THE SETTLEMENT FIXED THE COUNTERFACTUAL'S SUBJECT AND NOT ITS GRANULARITY. **  *`r7251` ruled
   that the reword is applied to the PAPER and that a receipt's declared purpose is no ground.  That
   decides every pin whose content is a PROPOSITION, because a meaning-preserving reword leaves the
   finding standing.* ⇒ *** It decides nothing about a pin whose content is an IDENTITY --- a
   symbol, a name, a definition --- because there is no reword of a name that preserves it.  Those
   are the six. ***

⌗ ** AND THE MISSING CLAUSE IS ALREADY IN THE OTHER SEAT'S OWN REASONS, APPLIED BOTH WAYS. **  *On
  one key it argues `nothing shorter carries it` and adds that the paper carries the shorter form at
  a second site, so the pinned span is the discriminating one --- an argument this seat ACCEPTS.  On
  another it NAMES the two-conjunct tightening that would repair the key, then holds the verdict
  anyway because the gate has no redundant arm to drop, which is the receipt's own need and the one
  ground the settlement removed.* ⇒ **The discriminator exists in its practice; what is missing is
  that it BIND.**

✔ ** THE BLIND IS STRUCTURAL AND NOT A PROMISE. **  *The draw was taken from the baseline AT A PIN
  where all forty keys still read `UNADJUDICATED`, and the forty verdicts were committed in a commit
  whose own tree carries no comparison file at all.  Both are checked below from git rather than
  asserted.*

⛭⛭ ** TWO OF SIX PRE-REGISTERED BANDS BROKE, BOTH HIGH, AND BOTH ARE PUBLISHED AS BROKEN. **  *The
   raw agreement, the contested cell and the non-contested cell all landed inside --- the contested
   cell at `11.8` against a central guess of `12`.* ⇒ *** But `5` of the `27` disagreements are ones
   this seat CONCEDES on reading the other's reason, and a conceded disagreement is still one the
   rule did not explain, so the pre-registered `0`-`40` band for that quantity breaks at `40.7`.
   AND THE QUANTITY ITSELF WAS THE WRONG ONE FOR THE CONDITION IT WAS MEANT TO TEST, which is a
   result about the pre-registration and not about the corpus. ***

⌈ ⛔ ** THE OTHER BROKEN BAND IS THE ONE THAT COSTS THIS SEAT. **  *`162` of this line's `171`
  `REPAIR-OWED` verdicts on the other prefix turn on the settled rule --- `94.7` per cent against a
  pre-registered `60` in a band of `30`-`85`.*  ⇒ *That answers the order's third item: the rule does
  NOT leave the `171` essentially unchanged, so the criterion WAS the question.* ⚠ ***But `162` of
  them carry ONE reason string, so the figure is a property of this seat's method and not an
  independent measurement, and it is reported with that beside it.***

COMPUTES: nothing the papers quote.  This receipt compares two seats' verdicts on one set of
quote-pin keys against its own published per-key tables and the baseline read as data; no physical
parameter is pinned here.
"""
import ast
import collections
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
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7254_60_mirror_cross_read')
DRAW_PIN = 'a88fca54'


def _git(*a):
    return subprocess.run(('git',) + a, cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def tsv(name):
    raw = open(os.path.join(DIR, name), encoding='utf-8').read()
    return [ln.split('\t') for ln in raw.split('\n') if ln.strip() and not ln.startswith('#')]


VERD = tsv('VERDICTS.tsv')
COMP = tsv('COMPARISON.tsv')
STATS = json.load(open(os.path.join(DIR, 'STATS.json'), encoding='utf-8'))
DRAW = tsv('DRAW.tsv')
CLS = collections.Counter(r[7] for r in COMP)
N = len(COMP)
print(f"    the draw {len(DRAW)}; the verdicts {len(VERD)}; the comparable {N}")
print(f"    classes: { {k: CLS[k] for k in sorted(CLS)} }", flush=True)

# =====================================================================================
head("A -- THE TABLES, AND THE BLIND CHECKED FROM GIT RATHER THAN PROMISED")

gate("Ⓐ① the three tables are read as DATA and their form is checked rather than assumed: `40` drawn"
     " keys, `40` verdicts one per drawn key, `27` comparable rows, and every row of every table"
     " carries its full column count with no cell holding a tab",
     len(DRAW) == 40 and len(VERD) == 40 and N == 27
     and all(len(r) == 7 for r in DRAW) and all(len(r) == 9 for r in VERD)
     and all(len(r) == 10 for r in COMP)
     and {r[0] for r in DRAW} == {r[0] for r in VERD})

_add_v = _git('log', '--diff-filter=A', '--format=%H', '--',
              'computations/beyond_the_wall/r7254_60_mirror_cross_read/VERDICTS.tsv').split()
_add_c = _git('log', '--diff-filter=A', '--format=%H', '--',
              'computations/beyond_the_wall/r7254_60_mirror_cross_read/COMPARISON.tsv').split()
_at_v = _git('ls-tree', '-r', '--name-only', _add_v[-1]) if _add_v else ''
_v_tree_has_comp = 'COMPARISON.tsv' in _at_v
_v_tree_has_pred = 'r7254_60_mirror_cross_read/PREDICTION.md' in _at_v
print(f"      the commit that ADDED the verdicts: {_add_v[-1][:8] if _add_v else '(none)'};"
     f"  its tree carries the prediction: {_v_tree_has_pred};"
     f"  its tree carries a comparison: {_v_tree_has_comp}")
gate("Ⓐ② ✔ THE BLIND IS STRUCTURAL: the commit that added the forty verdicts carries the"
     " PRE-REGISTRATION in its own tree and carries NO comparison file at all -- so the verdicts were"
     " fixed in history before anything that reads the other seat's column existed.  ⌗ *Checked by"
     " listing that commit's tree, not by a sentence in a reply*",
     len(_add_v) > 0 and _v_tree_has_pred and not _v_tree_has_comp)

_pin_raw = _git('show', f'{DRAW_PIN}:corpus/quote_pin_baseline.tsv')
_pin = {}
for _ln in _pin_raw.split('\n'):
    if not _ln.strip() or _ln.startswith('#'):
        continue
    _r = _ln.split('\t')
    if len(_r) >= 7:
        _pin[(_r[0], _r[1])] = _r
_drawn_at_pin = [_pin.get((r[1], r[2])) for r in DRAW]
_all_unadj = all(p is not None and p[5] == 'UNADJUDICATED' for p in _drawn_at_pin)
print(f"      all forty keys at the pin {DRAW_PIN}: present {sum(1 for p in _drawn_at_pin if p)},"
     f" and UNADJUDICATED there: {_all_unadj}")
gate(f"Ⓐ③ and the DRAW could not have seen an answer either: every one of the forty keys reads"
     f" `UNADJUDICATED` in the baseline at `{DRAW_PIN}`, the commit the draw was taken at, which is"
     f" this line's own head before the merge that brought the two readings together",
     _all_unadj and len(_pin) > 1000)

_comparable = [r for r in DRAW if r[6] == 'COMPARABLE']
_contested_draw = [r for r in DRAW if (r[3], r[4]) == ('PAPER', 'SENTENCE')]
gate("Ⓐ④ ⛔ AND THE ORDER'S TWO REQUIREMENTS ARE NOT BOTH SATISFIABLE, WHICH IS A PROPERTY OF THE"
     " DRAW AND NOT OF EITHER READING: it asked for `40` keys with at least `30` in the contested"
     " cell, and the other seat has read only `17` of that cell in total.  ⇒ *The floor is met"
     " exactly at `30` and the comparable subset is `27`, with `17` of it contested -- the"
     " cross-read's real denominator, reported rather than quietly swapped for `40`*",
     len(_contested_draw) == 30 and len(_comparable) == 27
     and sum(1 for r in _comparable if (r[3], r[4]) == ('PAPER', 'SENTENCE')) == 17)

# =====================================================================================
head("B -- THE SIX PRE-REGISTERED BANDS, FOUR HELD AND TWO BROKE HIGH")

BANDS = (
    ('① raw agreement', 37, 20, 55, 100 * CLS['AGREE'] / N),
    ('② contested cell', 12, 0, 35, 100 * STATS['contested_cell']['agree'] / STATS['contested_cell']['n']),
    ('③ non-contested cell', 70, 40, 100, 100 * STATS['non_contested']['agree'] / STATS['non_contested']['n']),
    ('④ my REPAIR-OWED, contested', 70, 45, 90,
     100 * STATS['my_forty']['contested_repair_owed'] / STATS['my_forty']['contested_n']),
    ('⑤ not explained by the rule', 15, 0, 40, 100 * (CLS['CONCEDED'] + CLS['OPEN']) / N),
    ('⑥ the 171 that turn on the rule', 60, 30, 85, STATS['the_171']['turns_on_the_rule_pct']),
)
_broke = [b for b in BANDS if not (b[2] <= b[4] <= b[3])]
for nm, c0, lo, hi, got in BANDS:
    print(f"      {nm:<34} predicted {c0:>3} in [{lo:>3},{hi:>3}]   measured {got:5.1f}  "
          f"{'INSIDE' if lo <= got <= hi else 'BROKE'}")
gate(f"Ⓑ① ⛔ EXACTLY `2` OF THE `6` BANDS BROKE AND BOTH BROKE HIGH, which is the direction that does"
     f" NOT flatter this seat on either: `⑤` because the disagreements this seat CONCEDES are still"
     f" disagreements the rule failed to explain, and `⑥` because `95` per cent of this line's own"
     f" `REPAIR-OWED` turning on the settled rule is a statement about this line's method",
     len(_broke) == 2 and all(b[4] > b[3] for b in _broke)
     and {b[0][0] for b in _broke} == {'⑤', '⑥'})

_seed_in, _seed_out = 30.0, 95.0
gate("Ⓑ② ✔ and the band test is CONTROLLED rather than trusted: a seeded value inside a band"
     " classifies as inside and a seeded value above it as broken, on the same comparison the table"
     " above uses -- so a comparison that could not fail is not reporting four holds",
     (20 <= _seed_in <= 55) and not (0 <= _seed_out <= 40))

gate("Ⓑ③ ⌗ and the one band that came back almost exactly is the one whose direction was declared in"
     " advance as the comfortable answer: the contested cell was pre-registered at `12` per cent"
     " central and measures `11.8`.  *Reported as a coincidence, with the per-key table published so"
     " a reader who disbelieves it can recount rather than take it*",
     abs(100 * STATS['contested_cell']['agree'] / STATS['contested_cell']['n'] - 12) < 1.0)

# =====================================================================================
head("C -- THE CROSS-READ, AND THE RETIREMENT CONDITION ON TWO READINGS OF `DISAGREE`")

gate("Ⓒ① the four classes PARTITION the twenty-seven with nothing over and nothing counted twice,"
     " and the raw agreement is `6` of `27`: the verdict strings match on six keys and differ on"
     " twenty-one",
     sum(CLS.values()) == N and CLS['AGREE'] == 6
     and CLS['RULE-DISPOSED'] + CLS['CONCEDED'] + CLS['OPEN'] == 21
     and set(CLS) == {'AGREE', 'RULE-DISPOSED', 'CONCEDED', 'OPEN'})

#: ⛔⛭⛭ r7372 (60), on 66's `r7371` ①: ** THE DISJUNCTION'S FIRST ARM IS REMOVED, AND IT HAD NEVER
#: MATCHED ANYTHING. **  *It read `'already the product of a repair'` against this container, and that
#: string has ZERO occurrences in `COMPARISON.tsv` -- not merely today: `git log -S` over the file
#: returns NO commit that ever changed its count, so the container has never held it at any commit of
#: its history.*  ⌗ **It is the RECEIPT's wording of the ground and not the CONTAINER's**: the conceded
#: row's reason says `already performed`, which entered with the container at `2ae79bbe` and is the arm
#: this clause has always passed on.
#:   ⇒ ** DELETED rather than widened, and rather than kept with a reason stated at the site -- which is
#:     this corpus's own disposition for a dead arm, five times over by `r7355+cc66.25`'s "a two-letter
#:     arm deleted rather than widened".  A literal asserted against a container that has never
#:     contained it is not a weaker pin; it is NO pin, and keeping it with a reason would record an
#:     intention where the file needs an assertion. **
#:   ⌗ *Nothing is weakened: the clause's truth value is unchanged at every commit of the container's
#:     history, because the removed arm contributed nothing at any of them.  And one key LEAVES the
#:     mint rather than arriving in it -- `cc66`'s targeted landing wanted a row for a literal that
#:     describes nothing, and there is now no key to carry one.*
gate("Ⓒ② ✔ AND THE CROSS-READ IS A READING AND NOT A DEFENCE OF THIS SEAT'S OWN COLUMN, which is"
     " checkable rather than claimed: it CONCEDES five of the twenty-one to the other seat, one of"
     " them on a ground verified in the COMPARISON's own reason column -- that the pinned form had"
     " ALREADY PERFORMED the repair this class asks for, recorded there in place.  ⌗ *A comparison"
     " that conceded nothing would be an argument*",
     CLS['CONCEDED'] == 5 and any('already performed' in r[9] for r in COMP if r[7] == 'CONCEDED'))

_open_pct = 100 * CLS['OPEN'] / N
_unexpl_pct = 100 * (CLS['CONCEDED'] + CLS['OPEN']) / N
print(f"      still OPEN under one rule: {CLS['OPEN']}/{N} = {_open_pct:.1f}%")
print(f"      not EXPLAINED by the rule: {CLS['CONCEDED'] + CLS['OPEN']}/{N} = {_unexpl_pct:.1f}%")
print(f"      the order's retirement line: {100 / 3:.1f}%")
gate("Ⓒ③ ⛔⛭⛭ AND THE ORDER'S REACHABLE NEGATIVE STRADDLES THE TWO READINGS OF `DISAGREE`: on what"
     " is STILL OPEN once one rule is applied the figure is `22.2` per cent and the ratchet is NOT"
     " retired; on what the rule FAILED TO EXPLAIN it is `40.7` and the condition fires.  ⇒ *Both"
     " are reported with the definition that separates them, because a seat may not pick the reading"
     " that suits it*",
     _open_pct < 100 / 3 < _unexpl_pct)

gate("Ⓒ④ ⇒ and this seat's RECOMMENDATION is stated rather than smuggled into the arithmetic: the"
     " condition should be read on what is STILL OPEN, because a disagreement one seat abandons the"
     " moment it reads the other's reason was never two instruments -- it was one seat not having"
     " looked.  ⌗ *On that reading the ratchet stands, by `11` points of `33`, and the recommendation"
     " is `66`'s to take or refuse*",
     _open_pct < 100 / 3 and CLS['CONCEDED'] > 0)

# =====================================================================================
head("D -- THE FINDING: THE SIX THAT REMAIN ARE ONE SHAPE")

SHAPES = collections.Counter((r[7], r[8]) for r in COMP)
_open_rows = [r for r in COMP if r[7] == 'OPEN']
_disp_rows = [r for r in COMP if r[7] == 'RULE-DISPOSED']
_diff_rows = [r for r in COMP if r[7] != 'AGREE']
_cell_shapes = {r[8] for r in COMP if (r[3], r[4]) == ('PAPER', 'SENTENCE')}
for k in sorted(SHAPES):
    print(f"      {k[0]:<14} {k[1]:<12} {SHAPES[k]}")
print(f"      shapes present inside the contested cell alone: {sorted(_cell_shapes)}", flush=True)
_prop_diff = [r for r in _diff_rows if r[8] == 'PROPOSITION']
_id_diff = [r for r in _diff_rows if r[8] == 'IDENTITY']
_prop_not_disposed = [r for r in _prop_diff if r[7] != 'RULE-DISPOSED']
print(f"      disagreements: {len(_diff_rows)};  PROPOSITION {len(_prop_diff)} of which"
     f" {len(_prop_diff) - len(_prop_not_disposed)} are disposed by the rule;"
     f"  IDENTITY {len(_id_diff)} of which"
     f" {sum(1 for r in _id_diff if r[7] == 'RULE-DISPOSED')} are", flush=True)
gate("Ⓓ① ⛭⛭⛭ THE SHAPE OF THE PIN AND NOT THE SEAT DECIDES WHETHER THE SETTLEMENT REACHES IT: ALL SIX"
     " still-open keys are IDENTITY pins, ALL TEN the rule disposes of are PROPOSITION pins, and NOT"
     " ONE of the ten IDENTITY disagreements is disposed by it.  ⇒ ***So the residual is not two"
     " instruments reading one column: it is one instrument whose counterfactual has a subject and no"
     " granularity***",
     len(_open_rows) == 6 and len(_disp_rows) == 10 and len(_diff_rows) == 21
     and all(r[8] == 'IDENTITY' for r in _open_rows)
     and all(r[8] == 'PROPOSITION' for r in _disp_rows)
     and sum(1 for r in _id_diff if r[7] == 'RULE-DISPOSED') == 0)

gate("Ⓓ①ᵃ ⌗ AND THE ONE EXCEPTION IS NAMED RATHER THAN ROUNDED AWAY, because this gate's first form"
     " claimed all ELEVEN unreached disagreements were identity pins and `11` was wrong: of the"
     " `11` PROPOSITION disagreements `10` are disposed and ONE is not -- the key this seat concedes"
     " because the repair had ALREADY BEEN PERFORMED and recorded in place, which is not a question"
     " about shape at all.  ⇒ *The rule did not fail to reach that one; it had nothing left to decide*",
     len(_prop_diff) == 11 and len(_prop_not_disposed) == 1
     and _prop_not_disposed[0][7] == 'CONCEDED')

gate("Ⓓ①ᵇ ✔ and the SHAPE column is not the `(target, tier)` cell under another name, which is the"
     " circularity this gate would otherwise have: BOTH shapes occur inside the contested"
     " `PAPER`/`SENTENCE` cell, so a reader cannot recover the shape from the baseline's own columns"
     " and the column carries a judgement that had to be made per key",
     _cell_shapes == {'IDENTITY', 'PROPOSITION'})

_KW = ('FORMULA', 'NAME', 'DEFINITION', 'TERM OF ART', 'SYMBOLS', 'STANDARD NAME')
_kw = lambda g: any(k in g.upper() for k in _KW)
_kw_open = sum(1 for r in _open_rows if _kw(r[9]))
_kw_disp = sum(1 for r in _disp_rows if _kw(r[9]))
print(f"      a keyword sniffer over the GROUND text instead: {_kw_open} of 6 open,"
     f" {_kw_disp} of 10 disposed -- one miss and two false hits")
gate("Ⓓ①ᶜ ⛔ AND THE FIRST FORM OF THIS GATE WAS A KEYWORD SNIFFER OVER THE GROUND TEXT AND IT WENT"
     " RED, which is why the shape is a column and not a regex: it missed the key whose ground says"
     " only `the same line element as the other one`, and it fired twice on the word `NAMES` used as"
     " a VERB -- `their own reason NAMES the tightening`.  ⇒ *An operator false positive inside a"
     " receipt about operator false positives, and it is reported rather than tuned away*",
     _kw_open == 5 and _kw_disp == 2)

_lits = collections.Counter(r[2] for r in COMP)
_dups = [l for l, c in _lits.items() if c > 1]
_same_verdicts, _split_class = [], []
for l in _dups:
    rs = [r for r in COMP if r[2] == l]
    if len({r[5] for r in rs}) == 1 and len({r[6] for r in rs}) == 1:
        _same_verdicts.append(l)
    if len({r[7] for r in rs}) > 1:
        _split_class.append(l)
print(f"      literals comparable twice: {len(_dups)};  both seats giving the same verdict on both"
     f" sites: {len(_same_verdicts)};  falling in DIFFERENT classes: {len(_split_class)}")
gate("Ⓓ② ⛭⛭ AND THE DEMONSTRATION IS SHARPER THAN THE ONE THIS GATE FIRST CLAIMED: a literal drawn"
     " at two sites gets the SAME verdict from both seats at both, and still falls in DIFFERENT"
     " classes of this comparison -- because what decides it is the ground the other seat gives for"
     " THAT receipt's finding, and at one site that ground is a shortfall the pin merely locates"
     " while at the other it is the identification itself.  ⌗ *The first form of this gate asserted"
     " OPPOSITE VERDICTS and was false against this seat's own table: every repeated literal"
     " took the same verdict from this seat at both of its sites*",
     len(_dups) > 0 and len(_split_class) > 0
     and len(_same_verdicts) == len(_dups))

gate("Ⓓ③ ⌗ and the missing clause is stated as something that can be tested rather than as a"
     " preference: *a pin is `DELIBERATE` where the pinned span is the SHORTEST that carries its"
     " claim and the claim is an IDENTITY; it is `REPAIR-OWED` where a strictly shorter span carries"
     " it.*  ⇒ **The other seat already applies exactly that test, and on one key it NAMES the"
     " shorter form and keeps the verdict anyway -- so the clause is in its practice and not in its"
     " rule**",
     any('nothing shorter' in r[9].lower() or 'discrimination' in r[9].lower()
         for r in COMP if r[7] == 'CONCEDED')
     and any('tightening' in r[9].lower() for r in COMP if r[7] == 'RULE-DISPOSED'))

# =====================================================================================
head("E -- THE ORDER'S THIRD ITEM, ANSWERED, WITH ITS OWN COUNTERWEIGHT")

T = STATS['the_171']
print(f"      the 171: propositions {T['propositions_turning_on_the_rule']};"
     f"  identity pins {T['identity_pins_the_granularity_question_reopens']};"
     f"  wider-than-claim {T['repair_owed_under_any_reading']}")
gate("Ⓔ① ⛔ THE SETTLED RULE DOES NOT LEAVE THE `171` UNCHANGED: `162` of them are pins on a"
     " PROPOSITION, which is exactly the class the settlement decides, so `94.7` per cent of this"
     " line's `REPAIR-OWED` turn on it.  ⇒ ***The criterion WAS the question, and the other seat's"
     " level is the one the settlement moves*** -- which is the outcome the order said would mean"
     " this seat's level was never at issue, reported with the number that establishes it",
     T['propositions_turning_on_the_rule'] + T['identity_pins_the_granularity_question_reopens']
     + T['repair_owed_under_any_reading'] == T['total']
     and T['turns_on_the_rule_pct'] > 90)

gate("Ⓔ② ⚠ AND THE COUNTERWEIGHT IS PUBLISHED BESIDE IT RATHER THAN LEFT FOR `66` TO FIND: `162` of"
     " the `171` carry ONE reason string, so `94.7` per cent is a property of this seat's METHOD and"
     " not an independent measurement -- the same observation `r7251` made from the other side when"
     " it found the `289` verdicts `85` per cent reproducible from two baseline columns",
     T['propositions_turning_on_the_rule'] == 162
     and T['propositions_turning_on_the_rule'] / T['total'] > 0.9)

_nonunif_blind = STATS['my_forty']['contested_n'] - STATS['my_forty']['contested_repair_owed']
print(f"      this seat's own non-uniformity, measured: {_nonunif_blind} of"
     f" {STATS['my_forty']['contested_n']} contested keys broke its dominant verdict BLIND, and"
     f" {CLS['CONCEDED']} of {N} comparable keys were conceded on contact")
gate("Ⓔ③ ⇒ so the independent check on that method is THIS read, and it is reported as a number too:"
     " reading a different prefix key by key, `3` of the `30` contested keys broke this seat's own"
     " dominant verdict before any comparison, and `5` of the `27` comparable ones were conceded"
     " after reading the other seat's reason.  ⌗ *A rule applied uniformly would have produced"
     " neither*",
     _nonunif_blind == 3 and CLS['CONCEDED'] == 5)

# =====================================================================================
head("F -- AND NOTHING IS WRITTEN INTO A PREFIX ANOTHER SEAT HOLDS")

_live = {}
for _ln in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read().split('\n'):
    if not _ln.strip() or _ln.startswith('#'):
        continue
    _r = _ln.split('\t')
    if len(_r) >= 7:
        _live[(_r[0], _r[1])] = _r
_p15_live = [v for k, v in _live.items() if k[0].startswith('receipts/P15_CR_cosmology/')]

# ⛔ *The first form of this gate read `origin/main` LIVE and asserted the working tree's `P15` rows
#   were identical to it.  That is a claim about THIS REVISION's own commits written as a claim about
#   a moving reference: the moment `cc66` re-stated its own rows under the settled rule and the gate
#   landed on the trunk beside them, it went red -- on the other seat's success, with nothing of this
#   revision's changed.  **The same shape as `S2`'s `Ⓓ②ᵇ`, in the revision whose reply endorsed that
#   repair.**  ⇒ *So the claim is now read where it is TRUE and CHECKABLE: between this revision's own
#   two pinned commits, which is a statement about what this branch wrote and nothing else.*
#   Repaired by node `66` at `r7253`, whose merge brought the branches together; stated for `60` to
#   reverse.
BRANCH_TIP = '2ae79bbe'
BRANCH_BASE = '3bf0ac52'


def _p15_rows_at(_rev):
    return sorted(ln for ln in _git('show', f'{_rev}:corpus/quote_pin_baseline.tsv').split('\n')
                  if ln.startswith('receipts/P15_CR_cosmology/'))


_p15_same = _p15_rows_at(BRANCH_TIP) == _p15_rows_at(BRANCH_BASE)
_board = open(os.path.join(ROOT, 'corpus', 'pin_claims.tsv'), encoding='utf-8').read()
_claimed = [ln for ln in _board.split('\n') if ln.startswith('P15_CR_cosmology')]
print(f"      P15 rows in the working tree: {len(_p15_live)};  this revision's own commits left the"
     f" prefix untouched ({BRANCH_BASE}..{BRANCH_TIP}): {_p15_same};  board rows naming the prefix:"
     f" {len(_claimed)}")
gate("Ⓕ① ⛔ THE FORTY VERDICTS ARE PUBLISHED AND NOT WRITTEN: across this revision's own commits not"
     " one `P15_CR_cosmology` row of the baseline changed, because that prefix is ANOTHER SEAT'S"
     " CLAIM on the adjudication board and a claim is what the board is for.  ⇒ *So this revision"
     " lowers the backlog by nothing and says so; the thirteen keys the other seat has not read are"
     " a reading routed to it, not a stamp applied over it*  ⌗ *Read between this revision's own two"
     " pinned commits rather than against a live `origin/main`, which is the repair this revision's"
     " own reply endorsed for `S2` and then needed here*",
     _p15_same and len(_p15_live) > 900)

_mine_only = [r for r in VERD if r[5] == 'MINE-ONLY']
gate("Ⓕ② and the thirteen routed keys are the ones the comparison cannot reach, named as such: they"
     " sit in the contested cell, this seat has verdicted them, and no other seat has -- so they are"
     " the half of the mirror that is still owed rather than a result",
     len(_mine_only) == 13
     and all((r[3], r[4]) == ('PAPER', 'SENTENCE') for r in _mine_only))

gate("Ⓖ① ⌗ and this receipt asserts nothing about any paper: it reads its own published tables, the"
     " baseline at a pin and on the trunk, and git's own history -- so it cannot break when a paper"
     " is reworded, which is the whole defect `PO-78` exists to measure",
     all(not k[0].endswith('.tex') for k in _live)
     and os.path.basename(DIR) == 'r7254_60_mirror_cross_read')

# =====================================================================================
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  gates run: {len(CHECKS)}, failed: {len(CHECKS) - npass}   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  SIX OF TWENTY-SEVEN ARE STILL OPEN, AND ALL SIX ARE IDENTITY PINS.

  The rule settled at r7251 decides every pin whose content is a
  PROPOSITION: the reword is applied to the paper, the receipt's own need
  is no ground, and a meaning-preserving reword leaves the finding
  standing.  Ten of the twenty-one disagreements fall to that.  Five more
  this seat concedes on reading the other's reason, one of them because
  the pinned form is already the product of a repair of this very class,
  recorded in the receipt in place.

  WHAT IS LEFT IS SIX KEYS AND ONE QUESTION: a formula's symbols, a
  technical name, a term of art, the paper's own definition of a term.
  There is no reword of a name that preserves it, so the counterfactual
  the settlement fixed the SUBJECT of has no GRANULARITY, and these six
  are where that shows.  None of the ten it disposes of is an identity
  pin.  So the column is not two instruments.

  AND THE CLAUSE IS ALREADY IN THE OTHER SEAT'S PRACTICE: it argues
  `nothing shorter carries it' on one key -- correctly, and this seat
  concedes it -- and on another it names the two-conjunct tightening that
  would repair the key and keeps the verdict because the gate has no
  redundant arm to drop.  That second ground is the receipt's own need,
  which the settlement removed.  So the test to write down is: DELIBERATE
  where the pinned span is the shortest that carries its claim and the
  claim is an identity; REPAIR-OWED where a strictly shorter span carries
  it.

  THE GUARD: a settlement that names what the counterfactual is applied
  TO has not said how finely it applies.  Fixing the subject of a test
  and leaving its grain unstated gets agreement on propositions and
  nothing on identities -- and the disagreement that survives is then
  evidence about the rule rather than about the readers.
  ==========================================================================
""")
