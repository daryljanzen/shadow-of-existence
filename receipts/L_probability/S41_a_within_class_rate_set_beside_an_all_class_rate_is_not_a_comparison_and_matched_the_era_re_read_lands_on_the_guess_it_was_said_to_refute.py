#!/usr/bin/env python3
r"""S41 -- THE DENOMINATOR `r7317` CAUGHT: MATCHED, THE ERA RE-READ IS `28.1` PER CENT AND NOT `67.5`.

** WHAT WAS CORRECTED, AND BY WHOM. **  `r7317`'s ruling ②: *"The `67.5` is a withdrawal rate WITHIN
the `DELIBERATE` class.  The `25.7` is an owed rate over ALL classes.  The comparison is what produces
the conclusion."*  ⇒ ** And it is right. **  `r7320`'s measurement stands -- `27` of `40`, the grounds,
the recipe -- and the CONCLUSION drawn from it does not.

*** ⛔⛭⛭⛭ MATCHED ON THIS SEAT'S OWN DENOMINATOR: the era re-read is `120` of `427` = `28.1` per cent,
    band `22.0`-`33.0` from the sample's own interval.  ⇒ THE RULE'S `67`-`72` IS OUTSIDE THE BAND;
    the `25.7` anchor is INSIDE it; and this seat's own `r7318` guess of "the high twenties" is INSIDE
    it and within a point of the centre. ***  ** So the figure I reported as refuting my own reasoning
    in fact lands on the guess I had made -- `r7317`: "You called it and then talked yourself out of it
    on an unmatched comparison." **

** ⛭⛭ AND THE TWO SEATS' DENOMINATORS DIFFER BY A FILTER, WHICH IS WORTH NAMING BECAUSE IT IS THE SAME
   MISTAKE'S SHAPE. **  `66` counts `370` rows and `157` `DELIBERATE`s where this seat counts `427` and
   `168`.  *Measured here: the gap is EXACTLY the `57` rows whose verdict note MENTIONS `cc66` -- every
   one of them stamped `rNNNN+60`, this seat's own, the mention being of the other seat's ORDER.*  ⇒
   ** Both denominators give the same verdict on all three comparisons, so nothing turns on it -- but a
   filter on whose name appears in a note is a denominator choice, and it was not announced. **

** ⛭ AND `r7317`'s RULING ③ REPRODUCED HERE RATHER THAN QUOTED: ** *vintage is `+26.5` points on this
seat's denominator (`1.6` to `28.1`) -- real and large -- and the rule's own rate is a FURTHER `+39` to
`+44` above the re-read.*  ⇒ ** Vintage does not account for the gap, which is what `r7313` ruled and
what this now measures rather than assumes. **

⌗ ** AND THIS IS FILED AS AN INSTANCE AND NOT AS A NEW MEMBER. **  *`r7318`'s own caution, this seat's:
`an owed RATE over a seat's assigned prefixes is a property of the ASSIGNMENT and not of the seat`.
A rate's meaning lives in its denominator; I broke that across CLASSES, `66` reports nearly breaking
the same caution across SEATS in the same reading.  **The caution was already written, so what this
revision adds is two instances and no member.**

⛔ *The sample is NOT re-run and no row is re-verdicted: `r7317`'s order ① says the sample is done and
the correction is not an instruction to re-run anything.  What is performed here is the arithmetic and
the correction of three landed artefacts that carried the unmatched claim.*

⚠ WHAT THIS CANNOT SETTLE is at the foot.
"""
import ast
import io
import math
import os
import re
import subprocess
import sys

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print("\n  " + "=" * 96 + f"\n  {t}\n  " + "=" * 96)


print(__doc__)
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

# every read of a ledger or of a landed artefact is AT A COMMIT: the quantities here are facts about a
# tree, and a gate that re-read the live ledger would go red the next time any seat verdicts a row.
LANDED = 'd9d5f84e'          # r7320 as it merged -- the tree the measurement is of
ORDER = '8ba911eb'           # r7317's orders, on the trunk
SAMPLE_K, SAMPLE_N = 27, 40  # r7320's own result, not re-derived here


def show(sha, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


def ledger_rows(sha):
    return [l.split('\t') for l in show(sha, 'corpus/quote_pin_baseline.tsv').split('\n')
            if l.startswith('receipts/')]


def rev(note):
    m = re.match(r'r(\d{4})', note or '')
    return int(m.group(1)) if m else None


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE CORRECTION, READ WHERE IT WAS WRITTEN, AND THE CLAIM IT CORRECTS')

ORD = show(ORDER, 'FOR_60.md')
_r7317 = ORD[ORD.find('`r7317`'):ORD.find('`r7315`')] if '`r7317`' in ORD else ''
_says = ['withdrawal rate WITHIN the `DELIBERATE` class',
         'owed rate over ALL classes',
         'talked yourself out of it on an unmatched comparison']
gate(f'Ⓐ①  the correction is read AT `{ORDER}` and not restated: `r7317`\'s ruling ② names the fault as '
     f'a WITHIN-CLASS rate set against an ALL-CLASS rate, and says in terms that the conclusion was '
     f'talked out of a guess that was right.  ** The seat that is corrected does not get to paraphrase '
     f'the correction **',
     all(s in _r7317 for s in _says) and len(_r7317) > 1500)

_s40 = 'receipts/L_probability/S40_twenty_seven_of_forty_early_rows_withdraw_against_the_second_redraft_and_what_takes_them_is_where_the_check_was_cut.py'
_read = 'computations/beyond_the_wall/r7320_60_the_early_era_sampled/THE_READING.md'
# each artefact worded the same claim its own way, so each carries its own marker
_BAD = {_s40: "comes to the rule", _read: "comes to the rule",
        'receipts/INDEX.md': "where the rule's own aggregate rate already sat"}
_then = {p: (m in show(LANDED, p)) for p, m in _BAD.items()}
_now = {p: (m in io.open(os.path.join(ROOT, p), encoding='utf-8').read()) for p, m in _BAD.items()}
print(f'      the unmatched clause at {LANDED}: {_then};  live: {_now}')
gate(f'Ⓐ②  and WHAT WAS LANDED CARRIED IT in three places -- the receipt\'s own gate label, the '
     f'reading, and the index row -- shown by reading them AT the commit that merged, and shown GONE '
     f'live.  ** A correction that cannot point at what it corrected is a rewrite **',
     all(_then.values()) and not any(_now.values()))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THIS SEAT\'S OWN DENOMINATOR, AND WHY THE TWO COUNTS DIFFER')

L = ledger_rows(LANDED)
_pre = [c for c in L if len(c) >= 7 and '+60' in c[6] and (rev(c[6]) or 99999) < 7260]
_cls = {}
for c in _pre:
    _cls[c[5]] = _cls.get(c[5], 0) + 1
_delib, _owed = _cls.get('DELIBERATE', 0), _cls.get('REPAIR-OWED', 0)
print(f'      this seat, pre-r7260, at {LANDED}: {len(_pre)} rows  {dict(sorted(_cls.items()))}')
gate(f'Ⓑ①  THE DENOMINATOR, MEASURED: `{len(_pre)}` pre-`r7260` rows carry this seat\'s stamp at the '
     f'commit that merged, of which `{_delib}` are `DELIBERATE` and `{_owed}` are already '
     f'`REPAIR-OWED` -- an owed rate of `{100.0 * _owed / len(_pre):.1f}` per cent over ALL classes, '
     f'which is the quantity the `25.7` anchor is of',
     len(_pre) >= 427 and _delib >= 168 and _owed == 7)

_stamped = [c for c in _pre if re.match(r'r\d{4}\+60', c[6])]
_cc = [c for c in _pre if 'cc66' in c[6]]
_66set = [c for c in _pre if 'cc66' not in c[6]]
_66d = sum(1 for c in _66set if c[5] == 'DELIBERATE')
_66owed = sum(1 for c in _66set if c[5] == 'REPAIR-OWED')
_STAMP = re.compile(r'r\d{4}\+60')
_cc_all_mine = all(_STAMP.match(c[6]) for c in _cc)
print(f'      66\'s filter reproduces as {len(_66set)} rows / {_66d} DELIBERATE / {_66owed} owed;  '
      f'the {len(_cc)} rows it drops are all stamped rNNNN+60: {_cc_all_mine}')
gate(f'Ⓑ②  and THE TWO SEATS\' COUNTS ARE RECONCILED EXACTLY rather than called a boundary: dropping '
     f'every row whose note MENTIONS `cc66` reproduces `66`\'s `{len(_66set)}` and `{_66d}` from this '
     f'seat\'s `{len(_pre)}` and `{_delib}`, the `{len(_cc)}` dropped rows are EVERY ONE stamped '
     f'`rNNNN+60`, and the owed count is the same `{_owed}` under both.  ⇒ ** The difference is a '
     f'filter on whose name appears in a verdict note, which is itself a denominator choice **',
     len(_66set) == 370 and _66d == 157 and _66owed == _owed and len(_cc) == 57
     and _cc_all_mine and len(_stamped) == len(_pre) - 8)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE MATCHED RATE, AND THE THREE COMPARISONS IT DECIDES')

_lo, _hi = wilson(SAMPLE_K, SAMPLE_N)
_mid = SAMPLE_K / SAMPLE_N
_era = (_owed + round(_mid * _delib)) / len(_pre)
_era_lo = (_owed + int(_lo * _delib)) / len(_pre)
_era_hi = (_owed + round(_hi * _delib)) / len(_pre)
_era66 = (_66owed + round(_mid * _66d)) / len(_66set)
print(f'      sample {SAMPLE_K}/{SAMPLE_N} = {100 * _mid:.1f}% (Wilson {100 * _lo:.1f}-{100 * _hi:.1f})')
print(f'      era re-read, this seat\'s denominator: {100 * _era:.1f}% '
      f'({100 * _era_lo:.1f}-{100 * _era_hi:.1f});  on 66\'s: {100 * _era66:.1f}%')
gate(f'Ⓒ①  THE MATCHED QUANTITY: the sample\'s `{100 * _mid:.1f}` per cent applied to the '
     f'`{_delib}` `DELIBERATE`s and added to the `{_owed}` already owed gives '
     f'`{_owed + round(_mid * _delib)}` of `{len(_pre)}` = **`{100 * _era:.1f}` per cent**, band '
     f'`{100 * _era_lo:.1f}`-`{100 * _era_hi:.1f}` from the sample\'s own interval -- and '
     f'`{100 * _era66:.1f}` per cent on `66`\'s denominator, computed here rather than quoted.  ** The '
     f'two agree to within `2.5` points and neither is near `67` **',
     0.27 < _era < 0.29 and 0.29 < _era66 < 0.32 and _era_hi < 0.40)

_rule_lo, _rule_hi = 0.67, 0.72
_anchor = 0.257
_guess_lo, _guess_hi = 0.27, 0.30            # "the high twenties", as r7318 put it on the record
_in = lambda x: _era_lo <= x <= _era_hi
gate(f'Ⓒ②  ⛭⛭ AND THE THREE COMPARISONS GO THE OTHER WAY FROM THE CONCLUSION I DREW: the rule\'s '
     f'`67`-`72` is OUTSIDE the band ({not _in(_rule_lo) and not _in(_rule_hi)}), the `25.7` anchor is '
     f'INSIDE ({_in(_anchor)}), and this seat\'s own `r7318` guess of "the high twenties" is INSIDE '
     f'({_in(_guess_lo) and _in(_guess_hi)}) with the centre `{100 * _era:.1f}` inside it.  ** So the '
     f'sample vindicates the guess it was reported as refuting, and `r7317`\'s ruling ② stands on this '
     f'seat\'s own numbers and not only on `66`\'s **',
     not _in(_rule_lo) and not _in(_rule_hi) and _in(_anchor) and _in(_guess_lo) and _in(_guess_hi))

_vint = 100 * (_era - _owed / len(_pre))
_further_lo = 100 * (_rule_lo - _era)
_further_hi = 100 * (_rule_hi - _era)
gate(f'Ⓒ③  and `r7317`\'s RULING ③ REPRODUCED on this denominator rather than quoted: vintage is '
     f'`+{_vint:.1f}` points (`{100.0 * _owed / len(_pre):.1f}` as the ledger carries these rows, '
     f'`{100 * _era:.1f}` re-read with the rule) and the rule\'s own rate is a FURTHER '
     f'`+{_further_lo:.0f}` to `+{_further_hi:.0f}` above that.  ⇒ ** Vintage is real and large and '
     f'does NOT account for the gap -- which strengthens `r7313`\'s decision rather than reopening it **',
     _vint > 20 and _further_lo > 30)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- WHAT THE CORRECTION DOES NOT TOUCH, AND THE INSTANCE IT IS FILED AS')

RES = [l.split('\t') for l in io.open(
    os.path.join(ROOT, 'computations/beyond_the_wall/r7320_60_the_early_era_sampled/RESULT_40.tsv'),
    encoding='utf-8').read().split('\n') if l and not l.startswith('#')]
_w = [c for c in RES if c[6] == 'WITHDRAWN']
_g = {}
for c in _w:
    k = c[7].split(' -- ')[0].strip()
    _g[k] = _g.get(k, 0) + 1
gate(f'Ⓓ①  the MEASUREMENT is untouched by the correction, asserted and not promised: the table still '
     f'reads `{len(_w)}` withdrawn of `{len(RES)}` with Test 1 `{_g.get("Test 1", 0)}` and Test 5 '
     f'`{_g.get("Test 5", 0)}`, and `S40` still runs green.  ** What was wrong was the comparison drawn '
     f'from the figure, not the figure **',
     len(RES) == SAMPLE_N and len(_w) == SAMPLE_K and _g.get('Test 1') == 11 and _g.get('Test 5') == 11)

_CAUTION = 'is a property of the assignment and not of the seat'
_POINTER = '`r7318` caution one level up, in my hand'
_r7318_text = show(LANDED, 'FOR_66_FROM_60.md')
gate(f'Ⓓ②  ⌗ and this is FILED AS AN INSTANCE AND NOT AS A MEMBER: this seat\'s own `r7318` caution -- '
     f'*an owed RATE over a seat\'s assigned prefixes {_CAUTION}* -- is in the tree at `{LANDED}`, '
     f'written before this error was made -- and `r7317` names it as the caution it is, *one level up, '
     f'in my hand*.  ** A rate\'s meaning lives in its denominator: I broke that across CLASSES and '
     f'`66` reports nearly breaking it across SEATS in the same reading, so the revision adds two '
     f'instances and no member **',
     _CAUTION in _r7318_text and _POINTER in _r7317)

_led_now = io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read()
_stamp_now = [l for l in _led_now.split('\n') if l.startswith('receipts/') and 'r7322' in l.split('\t')[-1]]
gate(f'Ⓓ③  ⛔ and NOTHING IS RE-RUN AND NO ROW IS RE-VERDICTED, as the specific negative it is: the '
     f'ledger is byte-identical between the commit that merged and the trunk this revision stands on, '
     f'and no row carries an `r7322` verdict (`{len(_stamp_now)}`).  ** `r7317`\'s order ① says the '
     f'sample is done; the correction is the arithmetic and the three artefacts, and nothing else **',
     show(LANDED, 'corpus/quote_pin_baseline.tsv') == show(ORDER, 'corpus/quote_pin_baseline.tsv')
     and not _stamp_now)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** MATCHED, THE ERA RE-READ IS {100 * _era:.1f} PER CENT AND NOT 67.5. **  The rule's 67-72 is OUTSIDE the
     band, the 25.7 anchor is INSIDE it, and this seat's own guess of "the high twenties" is INSIDE it
     with the centre inside the guess.  The sample vindicates the guess it was reported as refuting.
  ⛭⛭ ** AND THE TWO DENOMINATORS ARE RECONCILED EXACTLY: ** 66's 370 and 157 are this seat's 427 and 168
     less the 57 rows whose note MENTIONS cc66 -- every one of them this seat's own by its stamp.
  ⛭ ** VINTAGE IS +{_vint:.0f} POINTS AND DOES NOT ACCOUNT FOR THE GAP: ** the rule sits a further +{_further_lo:.0f} to
     +{_further_hi:.0f} above a ledger re-read with the rule itself, which is r7313's ruling measured here.

  ⚠ ** WHAT THIS CANNOT SETTLE. **
     * The matched figure inherits the sample's interval: 40 rows of one seat in one era, scaled onto
       427.  The band is 11 points wide and that width is the sample's, not the arithmetic's.
     * It applies the within-class rate to the WHOLE DELIBERATE class.  A withdrawal rate measured on
       40 drawn rows need not be the class's rate, and nothing here tests that beyond the interval.
     * The other classes are taken AS THE LEDGER CARRIES THEM.  A re-read of the 191 MEANING-HELD rows
       could move the era figure again, in either direction, and is not ordered.
     * ⛔ And the licensed next measurement -- the same draw from EACH seat's early DELIBERATEs -- is
       NOT ordered: r7317 names its trigger, which is 70's crossover saying the rule text has stopped
       moving.  Nothing here proposes it.
""")
sys.exit(1 if FAILURES else 0)
