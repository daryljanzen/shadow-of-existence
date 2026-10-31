#!/usr/bin/env python3
"""r7641 item 2, closing: WHICH of the key-arm gaps actually block, per receipt.

`bank_gap_sweep.py` ended with the check it could not make: *"13 of my 44 read at least one key-arm
bank with no arm-of-record counterpart"* and *"A READER IS NOT AUTOMATICALLY BLOCKED ... up to 13 need
the per-receipt key check before they can be called clear."*  This file makes that check.

** THE TEST, AND WHY IT IS A KEY TEST AND NOT A FILE TEST. **  These banks carry both arms inside ONE
file, as key suffixes -- `rD__cr` beside `rD__lcdm`.  70's second bank is a FILE bank: it adds
`<name>_leafrec1.npz` siblings.  *A sibling file cannot reach an arm that lives as a key, which is the
distinction `cc66.17` asked to be put to 70 and which the second bank does not address.*  So for each
(receipt, bank) pair the question is which ARM's keys the receipt actually indexes:

  * it reads only `__lcdm` keys  -> CONTROL-ONLY, and the receipt is CLEAR (`cc66.8`'s case);
  * it reads `__cr` keys         -> BLOCKED, because that arm has no arm-of-record key to move to.

Keys are matched as LITERALS against each bank's own key list, so nothing is matched by pattern: a
receipt is credited with a key only if that exact key name appears in its source.

⛔⛭⛭ ** AND THE DECLARED FAILURE DIRECTION IS NOT HYPOTHETICAL -- IT FIRED ON THE FIRST RUN. **  A
literal-only key match scored `the_held_period_estimator_…` CLEAR.  It is BLOCKED, and `cc66.17`
already measured it so.  Its keys are built by f-string:

    g = lambda n, t: F[f'{n}__{t}']        # l.102, with t over ('lcdm', 'cr')

so no literal `__cr` appears anywhere in the file, and neither a key-literal match nor a `__cr`
substring check can see it.  ⇒ *** The fix is the one `bank_gap_sweep.py` already applies to FILE
names and this file failed to apply to KEYS: a template is expanded over the values its placeholder
can actually take, and a bank indexed by a `__{...}` template counts as read on BOTH arms unless the
placeholder is provably control-only.  That over-flags, which is the safe direction for a gap list. ***
  ⌗ *The second-way `__cr` substring check ALSO misfired, in the opposite direction: it flagged two
  receipts whose only `__cr` is in a COMMENT of mine explaining that the bank's arm is a key.  So it
  is applied to code with comment lines stripped.*
"""
import os
import re
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper',
                    'mine44.txt')

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


#: the thirteen the sweep named, minus the one that IS the arm of record (`r6929_scan_cr_leafrec1`,
#: a form rather than a gap -- that file is the arm, so there is nothing in it to re-point).
#: ⛭ `r6929_scan_cr` is NOT in this list, and that is a measured exclusion rather than an omission:
#: it carries 60 cr-side keys and ZERO control-side ones -- it is a CR-ONLY file, not a two-arm file --
#: and it HAS an arm-of-record sibling.  *So it is a FORM and not a gap, as `cc66.39` reported, and
#: including it would have scored two receipts blocked by a bank the second bank already cleared.*
#: PART 1 gates that distinction rather than leaving it to this comment.
GAPS = ('r6893_slice_check', 'r6897_fields', 'r6897_noop', 'r6911_noop', 'r6915_noop',
        'r6919_geometry', 'r6919_noop', 'r6925_geometry', 'r6925_noop', 'r6929_geometry',
        'r6929_noop')
NOT_A_GAP = 'r6929_scan_cr'
MINE44 = [ln.strip() for ln in open(MINE, encoding='utf-8') if ln.strip()]
#: hoisted because an f-string expression may not contain a backslash (py3.11)
TMPL_RE = re.compile(r'__\{')

KEYS = {}
for g in GAPS + (NOT_A_GAP,):
    z = np.load(os.path.join(SPEC, g + '.npz'), allow_pickle=True)
    KEYS[g] = sorted(z.files)

print(__doc__)
print(BAR)
print("  PART 1 -- EACH GAP BANK'S OWN KEYS, SPLIT BY ARM")
print(BAR)
for g in GAPS:
    cr = [k for k in KEYS[g] if re.search(r'(^|_)cr(_|$)|__cr$|_cr_', k) and 'lcdm' not in k]
    lc = [k for k in KEYS[g] if 'lcdm' in k]
    sib = os.path.exists(os.path.join(SPEC, g + '_leafrec1.npz'))
    print(f"    {g:20s} {len(KEYS[g]):3d} keys: {len(cr):2d} cr-side, {len(lc):2d} control-side"
          f"   sibling file: {sib}")
_nag = KEYS[NOT_A_GAP]
print(f"    {NOT_A_GAP:20s} {len(_nag):3d} keys: "
      f"{sum(1 for k in _nag if 'lcdm' not in k and 'cr' in k):2d} cr-side, "
      f"{sum(1 for k in _nag if 'lcdm' in k):2d} control-side   sibling file: "
      f"{os.path.exists(os.path.join(SPEC, NOT_A_GAP + '_leafrec1.npz'))}   <- NOT A GAP")
check("every bank in the gap set carries BOTH arms inside one file as key suffixes -- which is what "
      "makes it a key gap rather than a file gap -- and `r6929_scan_cr` is EXCLUDED because it "
      "carries no control side at all and has a sibling: a CR-only file is the arm, so there is "
      "nothing in it to re-point",
      all(any('lcdm' in k for k in KEYS[g]) for g in GAPS)
      and not any('lcdm' in k for k in _nag)
      and os.path.exists(os.path.join(SPEC, NOT_A_GAP + '_leafrec1.npz')),
      f"{sum(1 for g in GAPS if any('lcdm' in k for k in KEYS[g]))} of {len(GAPS)} carry a control "
      f"side; {NOT_A_GAP} carries {sum(1 for k in _nag if 'lcdm' in k)}")

print()
print(BAR)
print("  PART 2 -- THE PER-RECEIPT KEY CHECK THE SWEEP LEFT OWED")
print(BAR)
VERDICT = {}
for r in MINE44:
    f = os.path.join(RCPT, r + '.py')
    if not os.path.exists(f):
        continue
    src = open(f, encoding='utf-8').read()
    code = "\n".join(ln for ln in src.splitlines() if not ln.lstrip().startswith('#'))
    #: ** THE TEMPLATE TEST, which is what the literal-only version missed. **  A key built as
    #: `f'{n}__{t}'` names no arm in the source, so a receipt that indexes a gap bank anywhere AND
    #: contains a `__{` key template counts as reading BOTH arms.  *Over-flagging is the safe
    #: direction for a gap list, and it is the method `bank_gap_sweep.py` already uses for files.*
    #: ⛔⛭ ** AND THE TEMPLATE TEST IS LOCALISED TO EACH BANK'S OWN VARIABLE, which the first version
    #: was not. **  A file-wide `__{` search flagged `the_monopole_zero_point_…` and
    #: `the_two_readings_…` -- both already LANDED on the arm of record, both of which read
    #: `r6897_fields` on its control side and use a template for a DIFFERENT bank.  *An over-flag is
    #: the safe direction for a gap list but useless for pricing an ask, so the variable holding each
    #: bank is found from its own `np.load` and the template is looked for on THAT name.*
    hits = {}
    for g in GAPS:
        if g not in src:
            continue
        var = None
        m = re.search(r'(\w+)\s*=\s*np\.load\([^\n]*' + re.escape(g), code)
        if m:
            var = m.group(1)
        cr = [k for k in KEYS[g]
              if 'lcdm' not in k and 'cr' in k and (f"'{k}'" in code or f'"{k}"' in code)]
        lc = [k for k in KEYS[g] if 'lcdm' in k and (f"'{k}'" in code or f'"{k}"' in code)]
        #: a template counts only where it indexes THIS bank's variable -- `VAR[f'…__{…}']` -- or
        #: where a one-line lambda over that variable does, which is how `cc66.52` writes it.
        tmpl = False
        if var:
            tmpl = bool(re.search(re.escape(var) + r'\[f?[\'\"][^\'\"]*__\{', code)) or \
                bool(re.search(r'lambda[^\n]*:\s*' + re.escape(var) + r'\[f[\'\"][^\'\"]*__\{',
                               code))
        hits[g] = (cr, lc, tmpl)
    #: ⛭⛭ ** AND THERE ARE THREE VERDICTS, NOT TWO, WHICH THE FIRST TWO VERSIONS OF THIS FILE BOTH
    #: GOT WRONG. **  A receipt can read a key-gap bank's `cr` side KNOWINGLY -- saying so in its own
    #: header and gating the inference in the safe direction -- and such a receipt is not blocked:
    #: `the_monopole_zero_point_…` landed on the arm of record at `cc66.28` on exactly that basis,
    #: calling `g('eta_ls_w','cr')` with `r6897_fields` declared bank-blocked beside it.
    #:   ⇒ *So a cr-side read counts as BLOCKED only where the receipt does NOT declare it.  The
    #:   declaration is the criterion because the defect being looked for is an UNDECLARED cross-arm
    #:   read, and a declared one is a priced caveat.*
    declared = any(ph in src for ph in
                   ('arm is a KEY', 'ARM AS A KEY', 'arm as a key', 'whose arm is a KEY',
                    'its arm is a KEY'))
    if hits:
        reads_cr = sorted(g for g, (cr, _, t) in hits.items() if cr or t)
        blocked = [] if declared else reads_cr
        VERDICT[r] = (hits, blocked, reads_cr, declared)
print(f"    {'receipt':46s} {'reads':>5s}  blocked by")
for r in sorted(VERDICT):
    hits, blocked, reads_cr, declared = VERDICT[r]
    if not reads_cr:
        _v = "-- CLEAR (control-side keys only)"
    else:
        _tm = any(h[2] for h in hits.values())
        _lit = any(h[0] for h in hits.values())
        _why = ' [' + ('template' if _tm and not _lit else
                       'literal' if _lit and not _tm else 'both') + ']'
        _v = ("DECLARED: " if declared else "BLOCKED: ") + ", ".join(reads_cr) + _why
    print(f"    {r[4:50]:46s} {len(hits):5d}  {_v}")
BLOCKED = {r for r, (_, b, _c, _d) in VERDICT.items() if b}
DECLARED = {r for r, (_, b, c, d) in VERDICT.items() if c and d}
CLEAR = {r for r, (_, _b, c, _d) in VERDICT.items() if not c}
print(f"\n    {len(VERDICT)} of the 44 read a key-gap bank: {len(BLOCKED)} BLOCKED, "
      f"{len(DECLARED)} DECLARED (knowing, gated, landed), {len(CLEAR)} CLEAR")
def _code_of(r):
    return "\n".join(ln for ln in open(os.path.join(RCPT, r + '.py'), encoding='utf-8')
                      .read().splitlines() if not ln.lstrip().startswith('#'))


check("⌗ AND THE CLEAR VERDICTS ARE CHECKED A SECOND WAY: no receipt scored clear contains `__cr` or "
      "a `__{` key template in its CODE.  ⛔ *Comment lines are stripped, because the first version "
      "flagged two receipts whose only `__cr` is in a comment of mine saying the bank's arm is a "
      "key -- a false alarm in a register costs more than the error*",
      all('__cr' not in _code_of(r) and not TMPL_RE.search(_code_of(r)) for r in CLEAR),
      f"{sum(1 for r in CLEAR if '__cr' in _code_of(r) or TMPL_RE.search(_code_of(r)))}"
      f" of {len(CLEAR)} clear receipts carry it in code")
check("⛔⛭ AND BOTH KNOWN CASES ARE SCORED CORRECTLY NOW, which is what settles the method: "
      "`the_held_period_estimator_…` is BLOCKED -- `cc66.17` measured that independently, and the "
      "literal-only matcher got it wrong because its keys are `f'{n}__{t}'` -- while "
      "`the_monopole_zero_point_…` is DECLARED, not blocked, because it LANDED on the arm of record "
      "at `cc66.28` with `r6897_fields` named bank-blocked in its own text and the one cross-bank "
      "inference gated in the safe direction",
      any('held_period_estimator' in r for r in BLOCKED)
      and any('monopole_zero_point' in r for r in DECLARED)
      and not any('monopole_zero_point' in r for r in BLOCKED),
      f"held_period_estimator {'blocked' if any('held_period_estimator' in r for r in BLOCKED) else 'NOT blocked'}, "
      f"monopole_zero_point {'declared' if any('monopole_zero_point' in r for r in DECLARED) else 'NOT declared'}")

print()
print(BAR)
print("  PART 3 -- SO WHAT ONE BANK ASK BUYS, WITH A COUNT ATTACHED")
print(BAR)
FAMILY = tuple(g for g in GAPS if g.endswith(('_geometry', '_noop')))
_by_family = {r for r, (_, b, _c, _d) in VERDICT.items() if b and all(g in FAMILY for g in b)}
_needs_more = {r for r, (_, b, _c, _d) in VERDICT.items() if b and any(g not in FAMILY for g in b)}
print(f"    the `{{geometry,noop}}` family: {', '.join(FAMILY)}")
print(f"    receipts blocked ONLY by that family, so one ask clears them: {len(_by_family)}")
for r in sorted(_by_family):
    print(f"      {r[4:76]}")
print(f"    receipts needing something else as well: {len(_needs_more)}")
for r in sorted(_needs_more):
    print(f"      {r[4:60]:60s} also {', '.join(g for g in VERDICT[r][1] if g not in FAMILY)}")
#: ⛔⛭ ** THE THREE COUNTS ARE PINNED, because this file reached them through THREE wrong versions
#: and each wrong version produced a different, plausible count. **  Literal-only matching gave
#: 5 blocked / 8 clear; a file-wide template search gave 10 / 3; localising the template without the
#: DECLARED category gave 10 / 3 again with two landed receipts among the blocked.  *A count that
#: moves with the method and is not pinned is a number nobody can audit, and this one is going into a
#: bank ask.*
check("⛔⛭ THE VERDICT COUNTS ARE PINNED: 7 BLOCKED, 3 DECLARED, 3 CLEAR of the 13 readers, and 5 of "
      "the 7 cleared by the one family ask.  ⇒ ** Pinned because three earlier versions of this file "
      "each gave a different plausible count, and the number is going into a bank ask **",
      len(BLOCKED) == 7 and len(DECLARED) == 3 and len(CLEAR) == 3
      and len(_by_family) == 5 and len(_needs_more) == 2,
      f"{len(BLOCKED)} blocked, {len(DECLARED)} declared, {len(CLEAR)} clear; "
      f"{len(_by_family)} by the family, {len(_needs_more)} needing more")
#: ⛔⛭⛭ ** AND TWO OF THIS FILE'S OWN REFINEMENTS TURN OUT TO BE INERT, WHICH PERTURBATION FOUND AND
#: ASSERTION WOULD NOT HAVE. **  De-localising the template test to a file-wide search changes no
#: receipt's VERDICT -- every receipt carrying a `__{` template uses it on the gap bank in question --
#: and not stripping comment lines changes none either, because the two receipts whose only `__cr` is
#: a comment read the bank's cr side anyway and are DECLARED.  *So both refinements are right in
#: principle and currently make no difference.*
#:   ⇒ *** The localisation IS load-bearing for one thing, though -- which bank gets NAMED -- and that
#:       is pinned here so the refinement is not merely decorative: file-wide, `a_source_with_no_
#:       physics_…` is attributed to `r6919_geometry` AND `r6919_noop`; localised, only to
#:       `r6919_geometry`, because `r6919_noop` is never indexed by a template on its own variable. ***
_asrc = [r for r in VERDICT if r.startswith('P15_a_source_with_no_physics')]
if _asrc:
    _ab = VERDICT[_asrc[0]][2]
    print(f"    bank attribution for `a_source_with_no_physics_…`: {', '.join(_ab)}")
    check("⛭ AND THE LOCALISATION IS LOAD-BEARING FOR THE BANK ATTRIBUTION, pinned so the refinement "
          "is not decorative: `a_source_with_no_physics_…` is attributed to `r6919_geometry` ALONE, "
          "where a file-wide template search also names `r6919_noop` -- which it never indexes by a "
          "template on its own variable.  ⇒ ** This is what a bank ask is costed from, so the "
          "attribution has to be right and not merely conservative **",
          _ab == ['r6919_geometry'], ", ".join(_ab))

check("⛭ THE ASK HAS A COUNT: re-running the `{geometry,noop}` family with `__cr_leafrec1` entries "
      "clears every receipt blocked only by it, and the rest name exactly what else they need.  ⇒ "
      "** That is the whole of item ⑵'s remaining key-gap half, priced **",
      len(_by_family) + len(_needs_more) == len(BLOCKED) and len(BLOCKED) > 0,
      f"{len(_by_family)} + {len(_needs_more)} against {len(BLOCKED)} blocked")
check("⛔ AND NONE OF THEM WAS REACHED BY THE SECOND BANK, which is the point: it is a FILE bank, "
      "and not one of these gaps has an arm-of-record SIBLING that would help, nor an "
      "arm-of-record KEY",
      not any(os.path.exists(os.path.join(SPEC, g + '_leafrec1.npz'))
              and any('leafrec1' in k for k in
                      np.load(os.path.join(SPEC, g + '_leafrec1.npz'), allow_pickle=True).files)
              for g in GAPS),
      "no gap bank gained an arm-of-record key")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
