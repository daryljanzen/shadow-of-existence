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
KEYGAPS = ('r6893_slice_check', 'r6897_fields', 'r6897_noop', 'r6911_noop', 'r6915_noop',
           'r6919_geometry', 'r6919_noop', 'r6925_geometry', 'r6925_noop', 'r6929_geometry',
           'r6929_noop')
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
RE_P = [x for x in ROWS if x['repointed']]
KEY_B = [x for x in ROWS if not x['repointed'] and x['keyb'] and not x['declared']]
FILE_B = [x for x in ROWS if not x['repointed'] and x['fileb'] and not x['keyb']]
NO_CR = [x for x in ROWS if not x['repointed'] and not x['keyb'] and not x['fileb']]
OTHER = [x for x in ROWS if x not in RE_P + KEY_B + FILE_B + NO_CR]
for nm, b in (('RE-POINTED', RE_P), ('KEY-BLOCKED', KEY_B), ('FILE-BLOCKED', FILE_B),
              ('NO CR READ', NO_CR), ('UNACCOUNTED', OTHER)):
    print(f"    {nm:14s} {len(b):3d}")
print(f"    {'TOTAL':14s} {len(ROWS):3d} of {len(MINE44)} named in mine44.txt")
check("⛭ THE BUCKETS PARTITION THE SET: every one of the 44 falls into exactly one, with no overlap "
      "and no remainder.  ⇒ ** An inventory that does not partition is one that has forgotten a "
      "receipt, and this is the only claim in it that cannot be checked receipt by receipt **",
      len(RE_P) + len(KEY_B) + len(FILE_B) + len(NO_CR) == len(ROWS) == len(MINE44)
      and not OTHER,
      f"{len(RE_P)}+{len(KEY_B)}+{len(FILE_B)}+{len(NO_CR)} = "
      f"{len(RE_P) + len(KEY_B) + len(FILE_B) + len(NO_CR)} against {len(ROWS)} rows and "
      f"{len(MINE44)} named; {len(OTHER)} unaccounted")
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
check("⛔ AND `r6893_switch_screen_cr` IS A FILE GAP NEITHER BANK CLOSED: four blocked receipts read "
      "it, and TWO of them are clear of every key gap -- so one file releases those two outright, "
      "while the other two also need their key banks.  ⇒ ** Measured after the first version of this "
      "gate asserted two and was wrong **",
      len(_ss) == 4 and len(_ss_only) == 2
      and not os.path.exists(os.path.join(SPEC, 'r6893_switch_screen_cr_leafrec1.npz')),
      f"{len(_ss)} read it, {len(_ss_only)} clear of key gaps")
#: ⛭ *and one file gap this inventory found that no earlier entry of mine had catalogued*
check("⛭ AND THE INVENTORY TURNED UP A FILE GAP I HAD NOT CATALOGUED: `r6925_visleaf_cr` is banked "
      "with no `_leafrec1` sibling and blocks two receipts.  ⇒ ** Which is the use of a partition: "
      "it names what a receipt-by-receipt walk had missed **",
      'r6925_visleaf_cr' in NEED and len(NEED['r6925_visleaf_cr']) == 2
      and os.path.exists(os.path.join(SPEC, 'r6925_visleaf_cr.npz'))
      and not os.path.exists(os.path.join(SPEC, 'r6925_visleaf_cr_leafrec1.npz')),
      f"{len(NEED.get('r6925_visleaf_cr', []))} receipts")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
