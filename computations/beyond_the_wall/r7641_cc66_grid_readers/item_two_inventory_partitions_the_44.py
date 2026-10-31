#!/usr/bin/env python3
"""r7641 item 2, closing: the bank inventory, and the check that it leaves NO receipt unaccounted for.

Five instruments in `r7641_cc66_grid_readers/` have each measured one part of item ⑵.  This file does
the one thing none of them does: it asks whether the parts cover the whole.

** THE CLAIM UNDER TEST IS A PARTITION, WHICH IS THE ONLY KIND OF INVENTORY WORTH HANDING OVER. **
Every one of cc66's 44 P15 receipts falls into exactly one bucket, with no overlap and no remainder:

    RE-POINTED     -- it names `_leafrec1` somewhere, so it has been moved
    KEY-BLOCKED    -- it reads a two-arm bank's `cr` KEY, which no file bank can reach
    FILE-BLOCKED   -- it reads a `*_cr.npz` spectrum that has no `_leafrec1` sibling
    NO CR READ     -- it reads no cr-side bank at all, so there is nothing to move

*A receipt that is both re-pointed AND blocked would be a cross-arm defect, and a receipt in no bucket
would be one the inventory forgot.  Both are gated below.*

⚠ ** THE FILE TEST EXPANDS TEMPLATES, because a spectrum name need never appear in the source: **
`f'r6911_source_{t}.npz'` with `t` over the two arms produces `r6911_source_cr`, which a literal search
cannot see.  That is `bank_gap_sweep.py`'s own method and the lesson `cc66.46` paid for twice.
"""
import os
import re
import sys

BAR = "=" * 100
fail = []

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper',
                    'mine44.txt')
MINE44 = [ln.strip() for ln in open(MINE, encoding='utf-8') if ln.strip()]

#: the key-gap banks, and the one excluded as a form (`cc66.46`)
KEYGAPS_ALL = ('r6893_slice_check', 'r6897_fields', 'r6897_noop', 'r6911_noop', 'r6915_noop',
               'r6919_geometry', 'r6919_noop', 'r6925_geometry', 'r6925_noop', 'r6929_geometry',
               'r6929_noop')


def _key_gap_closed(g):
    """⛭ r7643: a key gap is CLOSED by a sibling file that keeps the key names and moves `__cr`.

    Four conditions, all required: the sibling exists, it carries the same `__cr` key names, those
    values MOVED, and the `__lcdm` values are IDENTICAL -- the bank's own statement that the control
    does not move.  *70's third bank closed `r6929_geometry` this way, which is a better form than
    the `__cr_leafrec1` entries I asked for, and which this file's first version could not see.*
    """
    import numpy as _np
    sp = os.path.join(SPEC, g + '_leafrec1.npz')
    if not os.path.exists(sp):
        return False
    a = _np.load(os.path.join(SPEC, g + '.npz'), allow_pickle=True)
    b = _np.load(sp, allow_pickle=True)
    #: ⛔⛭⛭ ** NUMERIC KEYS ONLY, AND THIS WAS A LATENT DEFECT THE ORDERED WORK WOULD HAVE
    #: TRIGGERED. **  The first version compared every `__cr` key with `.astype(float)`.  That held
    #: only because exactly ONE bank has a sibling and all of its `__cr` entries are numbers:
    #: `r6893_slice_check` carries `arm__cr = 'cr'`, a STRING, and the moment 70 banks a sibling for
    #: it -- which is the ask this file exists to price -- the comparison would have crashed rather
    #: than judged.  *Found by a perturbation that pointed the sibling path at the namesake, which
    #: made every gap take this branch and raised `could not convert string to float`.*
    #:   ⇒ *** Non-numeric keys are skipped, and a bank with no numeric key on either side returns
    #:       False -- "cannot judge" rather than "closed", which is the safe direction. ***
    def _num(z, k):
        try:
            _np.atleast_1d(z[k]).astype(float)
            return True
        except (ValueError, TypeError):
            return False

    #: ⛔ r7643+cc66.56: boundary-anchored, not a substring -- `'__cr' in k` misses `Dl__unset_cr`,
    #: `Dl__zero_cr`, `Dl__noop_cr`, `Dl__comb_cr_f0`, `Dl__inj_cr_f1`, which is most arm keys.  *The
    #: same defect as in `which_key_gaps_actually_block.py`, carried here by the copy.*
    _arm = re.compile(r'(^|_)cr($|_)')
    _ctl = re.compile(r'(^|_)lcdm($|_)')
    cr = [k for k in a.files if _arm.search(k) and k in b.files and _num(a, k) and _num(b, k)]
    lc = [k for k in a.files if _ctl.search(k) and k in b.files and _num(a, k) and _num(b, k)]
    if not cr or not lc:
        return False
    moved = any(not _np.allclose(_np.atleast_1d(a[k]).astype(float),
                                 _np.atleast_1d(b[k]).astype(float)) for k in cr)
    held = all(_np.allclose(_np.atleast_1d(a[k]).astype(float),
                            _np.atleast_1d(b[k]).astype(float)) for k in lc)
    return bool(moved and held)


KEYGAPS = tuple(g for g in KEYGAPS_ALL if not _key_gap_closed(g))
KEY_CLOSED = tuple(g for g in KEYGAPS_ALL if _key_gap_closed(g))
TMPL_RE = re.compile(r'__\{')
LIT_CR = re.compile(r"'([A-Za-z0-9_.]+_cr)\.npz'")
TMPL_CR = re.compile(r"f'([A-Za-z0-9_.]+)_\{\w+\}\.npz'")
DECLARE = ('arm is a KEY', 'ARM AS A KEY', 'arm as a key', 'KEY SUFFIX', 'key suffix')


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


def code_of(src):
    return "\n".join(ln for ln in src.splitlines() if not ln.lstrip().startswith('#'))


ROWS = []
for r in MINE44:
    f = os.path.join(RCPT, r + '.py')
    if not os.path.exists(f):
        continue
    src = open(f, encoding='utf-8').read()
    code = code_of(src)
    repointed = 'leafrec1' in code
    declared = any(p in src for p in DECLARE)
    # KEY test, localised to each bank's own variable -- `cc66.46`'s settled method
    keyb = []
    for g in KEYGAPS:
        if g not in src:
            continue
        m = re.search(r'(\w+)\s*=\s*np\.load\([^\n]*' + re.escape(g), code)
        var = m.group(1) if m else None
        lit = any((f"'{k}'" in code) for k in (g,)) and False
        tm = bool(var and re.search(re.escape(var) + r"\[f?['\"][^'\"]*__\{", code))
        lam = bool(var and re.search(r"lambda[^\n]*:\s*" + re.escape(var) + r"\[f['\"][^'\"]*__\{",
                                     code))
        cr_lit = bool(re.search(re.escape(g) + r"[^\n]*", code)) and bool(
            re.search(r"'[A-Za-z0-9_]*__cr'", code))
        if tm or lam or cr_lit or lit:
            keyb.append(g)
    # FILE test, with templates expanded over the arms
    stems = set(LIT_CR.findall(code)) | {p + '_cr' for p in TMPL_CR.findall(code)}
    fileb = sorted(s for s in stems
                   if os.path.exists(os.path.join(SPEC, s + '.npz'))
                   and not os.path.exists(os.path.join(SPEC, s + '_leafrec1.npz')))
    ROWS.append(dict(r=r, repointed=repointed, declared=declared, keyb=sorted(keyb), fileb=fileb,
                     any_cr=bool(stems or keyb)))

print(__doc__)
print(BAR)
print("  PART 1 -- THE FOUR BUCKETS")
print(BAR)
#: ⛭⛭ r7643: ** A FIFTH BUCKET, BECAUSE 70's THIRD BANK CREATED A STATE THIS FILE COULD NOT NAME. **
#: At `cc66.47` every receipt that read a cr bank was either re-pointed or blocked.  The third bank
#: closed `r6893_switch_screen_cr`, `r6925_visleaf_cr` and -- by a sibling file keeping the key names
#: -- `r6929_geometry`.  *So there are now receipts that read a cr bank, have every sibling they need,
#: and are simply NOT YET RE-POINTED.*  ⛔ *Without this bucket they fell into `NO CR READ`, which
#: said the opposite of the truth: the first run after the bank put two of them there.*
#:   ⇒ *** READY is the actionable list for `r7643`'s order item 2, and it is derived rather than
#:       typed: reads a cr stem, every stem has a sibling, no key gap, not re-pointed. ***
RE_P = [x for x in ROWS if x['repointed']]
KEY_B = [x for x in ROWS if not x['repointed'] and x['keyb'] and not x['declared']]
FILE_B = [x for x in ROWS if not x['repointed'] and x['fileb'] and not x['keyb']]
READY = [x for x in ROWS if not x['repointed'] and not x['keyb'] and not x['fileb'] and x['any_cr']]
NO_CR = [x for x in ROWS if not x['repointed'] and not x['keyb'] and not x['fileb']
         and not x['any_cr']]
OTHER = [x for x in ROWS if x not in RE_P + KEY_B + FILE_B + READY + NO_CR]
for nm, b in (('RE-POINTED', RE_P), ('KEY-BLOCKED', KEY_B), ('FILE-BLOCKED', FILE_B),
              ('NO BANK GAP', READY), ('NO CR READ', NO_CR), ('UNACCOUNTED', OTHER)):
    print(f"    {nm:14s} {len(b):3d}")
print(f"    {'TOTAL':14s} {len(ROWS):3d} of {len(MINE44)} named in mine44.txt")
check("⛭ THE BUCKETS PARTITION THE SET: every one of the 44 falls into exactly one, with no overlap "
      "and no remainder.  ⇒ ** An inventory that does not partition is one that has forgotten a "
      "receipt, and this is the only claim in it that cannot be checked receipt by receipt **",
      len(RE_P) + len(KEY_B) + len(FILE_B) + len(READY) + len(NO_CR) == len(ROWS) == len(MINE44)
      and not OTHER,
      f"{len(RE_P)}+{len(KEY_B)}+{len(FILE_B)}+{len(READY)}+{len(NO_CR)} = "
      f"{len(RE_P) + len(KEY_B) + len(FILE_B) + len(READY) + len(NO_CR)} against {len(ROWS)} rows "
      f"and {len(MINE44)} named; {len(OTHER)} unaccounted")
#: ⛔⛭⛭ ** AND THIS BUCKET IS NAMED FOR WHAT IT MEASURES, WHICH IS NOT "READY". **  My first version
#: called it READY and printed it as `r7643` item 2's work list.  *It is not: it means only that no
#: BANK gap stands in the way, and four of the sixteen are ones I established blocked for reasons no
#: sibling can fix --* `the_full_range_refit_…` and `the_refit_leaves_…` *on the grid's CENTRE
#: (`cc66.39`, `.41`),* `the_no_fit_confrontation_…` *on its own gate, the two confrontations having
#: collapsed to one file (`cc66.43`),* `the_refit_bound_figures_…` *on two of three configurations
#: (`cc66.43`), and* `the_windows_phase_spread_…` *held on 70's swap re-run (`cc66.26`).*
#:   ⇒ *** A partition over BANKS cannot see a block that is not about banks.  Printing this as a
#:       work list would have claimed sixteen re-points available when five are not. ***
print()
print("    NO BANK GAP -- no sibling is missing.  ⛔ NOT the same as ready: a non-bank block")
print("    (the grid's centre, a collapsed verification run, a paper-bound comparison, a held")
print("    re-run) is invisible to a partition over banks.  Five of these are known blocked:")
_KNOWN_NONBANK = ('the_full_range_refit', 'the_refit_leaves_the_background',
                  'the_no_fit_confrontation', 'the_refit_bound_figures',
                  'the_windows_phase_spread')
for x in sorted(READY, key=lambda y: y['r']):
    _nb = any(k in x['r'] for k in _KNOWN_NONBANK)
    print(f"      {'⛔' if _nb else '  '} {x['r'][4:74]}")
check("⛔⛭ AND THE FIVE KNOWN NON-BANK BLOCKS ARE INSIDE THIS BUCKET, which is why it is not a work "
      "list: a partition over banks cannot see the grid's centre, a collapsed verification run, a "
      "paper-bound comparison or a held re-run.  ⇒ ** Gated so the bucket cannot be read as "
      "'sixteen re-points available' when five of them are not **",
      sum(1 for x in READY if any(k in x['r'] for k in _KNOWN_NONBANK)) == 5,
      f"{sum(1 for x in READY if any(k in x['r'] for k in _KNOWN_NONBANK))} of "
      f"{len(READY)} are known non-bank blocks")
check("⛔ AND NO RECEIPT IS BOTH RE-POINTED AND BLOCKED BY A BANK IT CANNOT REACH, which would be "
      "the cross-arm defect this seat has refused three times -- except where it DECLARES the key "
      "read and gates it, which is `cc66.46`'s third verdict",
      all(x['declared'] for x in ROWS if x['repointed'] and (x['keyb'] or x['fileb'])),
      ", ".join(x['r'][4:40] for x in ROWS
                if x['repointed'] and (x['keyb'] or x['fileb']) and not x['declared'])
      or "none undeclared")

print()
print(BAR)
print("  PART 2 -- WHAT IS STILL BLOCKED, AND BY WHICH BANK")
print(BAR)
NEED = {}
for x in KEY_B + FILE_B:
    for b in x['keyb'] + x['fileb']:
        NEED.setdefault(b, []).append(x['r'])
print(f"    {'bank':26s} {'receipts':>8s}  kind")
for b in sorted(NEED, key=lambda k: (-len(NEED[k]), k)):
    kind = 'KEY -- a file bank cannot reach it' if b in KEYGAPS else 'FILE -- no sibling banked'
    print(f"    {b:26s} {len(NEED[b]):8d}  {kind}")
for b in sorted(NEED, key=lambda k: (-len(NEED[k]), k)):
    for r in sorted(NEED[b]):
        print(f"      {b:26s} {r[4:72]}")
check("⛭ AND THE INVENTORY NAMES A BANK FOR EVERY BLOCKED RECEIPT -- none is blocked by something "
      "unnamed, which is what makes this a priced ask rather than a complaint",
      all(x['keyb'] or x['fileb'] for x in KEY_B + FILE_B),
      f"{len(NEED)} distinct banks across {len(KEY_B) + len(FILE_B)} blocked receipts")
#: ⛔ ** THIS GATE WAS WRITTEN WRONG AND THE MEASUREMENT CORRECTED IT. **  I asserted
#: `r6893_switch_screen_cr` blocks TWO receipts "and they are the only two in that position".  It is
#: read by FOUR, of which two are also key-blocked and two are not.  *The two-of-four is the
#: interesting number -- those are the ones a single FILE would release -- and the four is the one I
#: would have got wrong.*
_ss = NEED.get('r6893_switch_screen_cr', [])
_ss_only = [r for r in _ss if not [x for x in ROWS if x['r'] == r][0]['keyb']]
print(f"    `r6893_switch_screen_cr` is read by {len(_ss)} blocked receipts, of which "
      f"{len(_ss_only)} are clear of every key gap:")
for r in sorted(_ss_only):
    print(f"      {r[4:76]}")
#: ⛔⛭⛭ ** AND THESE TWO GATES WERE FAIL-ON-SUCCESS, WHICH IS THE CLASS THIS SEAT HAS CATALOGUED
#: NINETEEN TIMES AND WROTE INTO ITS OWN INSTRUMENT ANYWAY. **  At `cc66.47` they pinned
#: `r6893_switch_screen_cr` and `r6925_visleaf_cr` as file gaps with NO sibling -- an assertion that
#: a bank is MISSING, which the ordered work could close and did, within the hour.  *Both went red on
#: 70's third bank for the best possible reason.*
#:   ⇒ *** Restated to pin the CLOSURE instead: the sibling is present, which only a de-banking could
#:       break -- and a de-banking is a thing worth catching. ***
check("⛭⛭ `r6893_switch_screen_cr` IS CLOSED BY 70's THIRD BANK.  ⛔ *At `cc66.47` this gate pinned "
      "it as a gap with no sibling -- fail-on-success, in the class this seat has catalogued "
      "nineteen times, written into its own instrument and fired within the hour.*  ⇒ ** Now it "
      "pins the closure, which only a de-banking could break **",
      os.path.exists(os.path.join(SPEC, 'r6893_switch_screen_cr_leafrec1.npz')),
      "sibling present")
check("⛭ AND SO IS `r6925_visleaf_cr`, the gap this partition itself turned up at `cc66.47` and "
      "which the third bank closed in the same pass -- same restatement, same reason",
      os.path.exists(os.path.join(SPEC, 'r6925_visleaf_cr_leafrec1.npz')),
      "sibling present")
#: ⛭ *and one file gap this inventory found that no earlier entry of mine had catalogued*
check("⛭ AND NO FILE GAP REMAINS: every `*_cr.npz` stem any of the 44 reads now has a `_leafrec1` "
      "sibling, so FILE-BLOCKED is empty and what is left is keys alone.  ⇒ ** Which is the use of "
      "a partition twice over: it found `r6925_visleaf_cr` at `cc66.47` and it is what measures the "
      "release now **",
      len(FILE_B) == 0,
      f"{len(FILE_B)} file-blocked")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
