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
GAPS_ALL = ('r6893_slice_check', 'r6897_fields', 'r6897_noop', 'r6911_noop', 'r6915_noop',
            'r6919_geometry', 'r6919_noop', 'r6925_geometry', 'r6925_noop', 'r6929_geometry',
            'r6929_noop')
#: ⛔⛭⛭ r7643+cc66.56: ** THE ARM-KEY TEST WAS A SUBSTRING, AND IT MISSED MOST ARM KEYS. **
#:   `'__cr' in k` matches `rD__cr`, `arm__cr` and `eta_ls__cr_0` -- and silently misses every key
#:   whose arm tag sits AFTER another token: `Dl__unset_cr`, `Dl__zero_cr`, `Dl__noop_cr`,
#:   `Dl__comb_cr_f0`, `Dl__inj_cr_f1`.  *Five of the nine arm keys in the first sample measured.*
#:   ⇒ *** So the closure test below verified that `X__cr` keys MOVED and never looked at
#:       `X__<tag>_cr` keys at all; and a claim of mine at `cc66.53` -- that `r6929_noop` and
#:       `r6925_noop` "carry no `__cr` keys at all, so they never blocked" -- was made with the same
#:       narrow test and is FALSE: both carry `Dl__zero_cr`, `Dl__unset_cr` or `Dl__noop_cr`.
#:       This file's own `GAPS_ALL` had them right all along and I believed the ad-hoc test over the
#:       instrument, which is the lesson worth more than the fix. ***
#:   ⛭ *The replacement is boundary-anchored rather than longer: `cr` must start the key or follow an
#:   underscore, and must end the key or precede one.  `Dl__combvl` and `Dl__crust` are the negative
#:   controls -- neither is an arm key and a looser `'cr' in k` would take both.*
ARM_RE = re.compile(r'(^|_)cr($|_)')
#: ⛔ *And the boundary regex must be applied to KEY LITERALS and not to whole source, which the first
#: version of this widening got wrong: `(^|_)cr($|_)` matches the BANK NAMES and arm labels a receipt
#: is full of -- `r6893_switch_screen_cr`, `cc66_cr_x_h686_pol`, `F['cr']` -- so run over `_code_of`
#: it scored 2 of the 3 CLEAR receipts as carrying an arm key when none of them reads one.*
#:   ⇒ *A looser test is not a safer test.  The key-shaped literals are extracted first.*
KEYLIT_RE = re.compile(r"['\"]([A-Za-z_][A-Za-z0-9_]*__[A-Za-z0-9_]+)['\"]")


def _armkeys_in(code):
    return [k for k in KEYLIT_RE.findall(code) if ARM_RE.search(k)]

CTL_RE = re.compile(r'(^|_)lcdm($|_)')
_ARM_SEEN = ('Dl__unset_cr', 'Dl__zero_cr', 'Dl__noop_cr', 'Dl__comb_cr_f0', 'Dl__inj_cr_f1',
             'rD__cr', 'eta_ls__cr_0', 'arm__cr')
NOT_A_GAP = 'r6929_scan_cr'
#: ** A KEY GAP IS CLOSED BY A SIBLING FILE THAT KEEPS THE KEY NAMES AND MOVES THE `__cr` VALUES. **
#: Tested, not assumed: the sibling must exist, carry the same `__cr` key names, hold DIFFERENT
#: values in them, and hold IDENTICAL `__lcdm` values -- the last being the bank's own statement that
#: the control does not move.  *All four, or it is not a closure.*
CLOSED_BY_SIBLING = []
#: ⛭⛭⛭ r7645+cc66.68: ** AND THERE ARE NOW TWO CLOSURE FORMS, NOT ONE. **
#:   *`r7641`'s sibling kept the `__cr` key NAMES and moved their values -- form **A**.  `r7643`'s
#:   fold REPLACED that with a SUPERSET -- form **B**: `__cr` and `__lcdm` both bit-identical to the
#:   namesake's, plus new `__cr_leafrec1` keys carrying the arm of record.  Form B is the better form
#:   for auditing, because one file answers "what did each arm do"; and it is the form that broke
#:   four registered receipts silently, because a reader that re-points by changing the FILE and
#:   keeping the key gets the NAMESAKE back with every gate passing.*
#:   ⇒ *** So `_closed` must recognise both and SAY WHICH, and this file's PART 0 reading -- that
#:       one gap was closed and the rest were open -- is superseded by measurement below. ***
FORM = {}


def _closed(g):
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

    def _eq(k, k2=None):
        return _np.allclose(_np.atleast_1d(a[k]).astype(float),
                            _np.atleast_1d(b[k2 or k]).astype(float))

    cr = [k for k in a.files if ARM_RE.search(k) and k in b.files and _num(a, k) and _num(b, k)]
    lc = [k for k in a.files if CTL_RE.search(k) and k in b.files and _num(a, k) and _num(b, k)]
    if not cr or not lc:
        return False
    held = all(_eq(k) for k in lc)
    if not held:
        return False
    #: form A -- the key names stay and the arm's values move
    if any(not _eq(k) for k in cr):
        FORM[g] = 'A'
        return True
    #: form B -- a SUPERSET: `__cr` held too, and new `__cr_leafrec1` keys carry the arm of record
    ins = [k for k in b.files if 'leafrec1' in k and _num(b, k)]
    if ins:
        #: and the inserted keys must actually DIFFER from the namesake entries they shadow, or the
        #: sibling has added names and no information.  *Keys with no namesake counterpart (the
        #: `_0`/`_1` geometry pairs) count as inserted and are not required to differ from anything.*
        pairs = [(k.replace('_leafrec1', ''), k) for k in ins]
        shadow = [(n, k) for n, k in pairs if n in a.files and _num(a, n)]
        if not shadow or any(not _eq(n, k) for n, k in shadow):
            FORM[g] = 'B'
            return True
    return False


for _g in GAPS_ALL:
    if _closed(_g):
        CLOSED_BY_SIBLING.append(_g)
#: ⛭⛭ r7645+cc66.68: ** THE DETECTOR'S SUBJECT AND THE ASK'S PRICE ARE NOW TWO DIFFERENT SETS. **
#:   *Until `r7643` they were one set, because one bank had closed and ten were open.  `r7643`'s fold
#:   closed TEN of the eleven, and keeping `GAPS` as the OPEN set made the detector score only the
#:   one bank still open: the verdict map collapsed from eleven readers to one, both
#:   independently-known cases dropped out of it, and the reach gate at the end of this file -- which
#:   ranges over `GAPS` -- passed VACUOUSLY over a single bank that has no sibling.*
#:   ⇒ *** A gate that passes because its set emptied is worse than one that fails, and this is the
#:       second time this file has had to record that its own set definition moved under a gate. ***
#:   So the DETECTOR scores `GAPS_ALL` -- which bank a receipt reads by key does not change when a
#:   sibling lands -- and `GAPS_OPEN` carries the shrinking ask.
GAPS = GAPS_ALL
GAPS_OPEN = tuple(g for g in GAPS_ALL if g not in CLOSED_BY_SIBLING)


#: ⛭ r7645+cc66.68: the readings the form-B gates below need, kept as functions so each gate
#: reads a measurement rather than a literal.
def _scalar(stem, key):
    z = np.load(os.path.join(SPEC, stem + '.npz'), allow_pickle=True)
    return float(np.atleast_1d(z[key]).astype(float)[0])


def _eq_cr_identical(g):
    """every `__cr`-side key of the namesake is bit-identical in the sibling -- form B's signature"""
    a = np.load(os.path.join(SPEC, g + '.npz'), allow_pickle=True)
    b = np.load(os.path.join(SPEC, g + '_leafrec1.npz'), allow_pickle=True)
    ks = [k for k in a.files if ARM_RE.search(k) and k in b.files]
    return bool(ks) and all(np.array_equal(a[k], b[k]) for k in ks)


def _noop_identity():
    """⛭⛭⛭ ** THE TEST THAT DECIDES WHETHER THE NO-OP ASKS ARE REALLY DISCHARGED. **

    *`cc66.64` proved every no-op bank's arm spectrum is BIT-IDENTICAL to `r6893_switch_screen_cr`'s
    own `Dl__base`, so substituting a sibling into those receipts' identity legs would have turned
    `base == base` into a tautology that passes while testing nothing.  What form B raises is whether
    BOTH SIDES moved together: if the arm-of-record no-op keys match the ARM-OF-RECORD screen's base
    and not the namesake's, the identity is reproduced on the new arm and the leg is still a test.*
    Returns (matched_arm, matched_namesake, total).
    """
    sn = np.load(os.path.join(SPEC, 'r6893_switch_screen_cr.npz'), allow_pickle=True)
    sa = np.load(os.path.join(SPEC, 'r6893_switch_screen_cr_leafrec1.npz'), allow_pickle=True)
    bn, ba = sn['Dl__base'], sa['Dl__base']
    ma = mn = tot = 0
    for g in ('r6897_noop', 'r6911_noop', 'r6915_noop', 'r6919_noop', 'r6925_noop', 'r6929_noop'):
        p = os.path.join(SPEC, g + '_leafrec1.npz')
        if not os.path.exists(p):
            continue
        z = np.load(p, allow_pickle=True)
        for k in z.files:
            if k.startswith('Dl__') and 'leafrec1' in k:
                tot += 1
                ma += int(z[k].shape == ba.shape and np.array_equal(z[k], ba))
                mn += int(z[k].shape == bn.shape and np.array_equal(z[k], bn))
    return ma, mn, tot
MINE44 = [ln.strip() for ln in open(MINE, encoding='utf-8') if ln.strip()]
#: hoisted because an f-string expression may not contain a backslash (py3.11)
TMPL_RE = re.compile(r'__\{')
#: ⛭ *and the widened form, used everywhere the narrow one was: a key TEMPLATE is an indexed f-string
#: carrying both a separator and a placeholder, wherever in the string the placeholder sits.*
TMPLKEY_RE = re.compile(r'\[f[\'\"]([^\'\"]*)[\'\"]\]')
_TMPL_SEEN = ('{n}__{t}', 'Dl__noop_{t}', 'Dl__xsonly_{t}', 'ls__noop_{t}')


def _is_keytmpl(s):
    """a key TEMPLATE carries both a separator and a placeholder, wherever the placeholder sits"""
    return '__' in s and '{' in s


def _tmplkeys_in(code):
    return [s for s in TMPLKEY_RE.findall(code) if _is_keytmpl(s)]


#: ⛔⛭ r7643+cc66.58, found by perturbing this file's own new gate: ** THE RULE WAS IMPLEMENTED TWICE
#:   -- once in the verdict loop and once in `_tmplkeys_in` -- so reverting the verdict path left the
#:   gate green and only the COUNTS moved. **  *A gate that pins a copy of the rule does not pin the
#:   rule.*  ⇒ *Both now call `_is_keytmpl`, so a revert reddens the detector gate itself.*
#: ⛔ *And the bank-presence boundary is pinned SYNTHETICALLY below, because reverting it changes no
#:   verdict today -- which is what latent means, and a latent defect with no gate is the one that
#:   comes back.*
_PRESENT_RE = (lambda g, s: bool(_re_present(g, s)))


def _re_present(g, s):
    return re.search(re.escape(g) + r'(?![A-Za-z0-9_])', s)

KEYS = {}
for g in GAPS_ALL + (NOT_A_GAP,):
    z = np.load(os.path.join(SPEC, g + '.npz'), allow_pickle=True)
    KEYS[g] = sorted(z.files)

print(__doc__)
print(BAR)
print("  PART 0 -- WHICH KEY GAPS 70's THIRD BANK CLOSED, AND BY WHICH MECHANISM")
print(BAR)
for g in GAPS_ALL:
    sib = os.path.exists(os.path.join(SPEC, g + '_leafrec1.npz'))
    print(f"    {g:20s} sibling file: {str(sib):5s}  closed by it: "
          f"{g in CLOSED_BY_SIBLING}{'  form ' + FORM[g] if g in FORM else ''}")
_FB = sorted(g for g in CLOSED_BY_SIBLING if FORM.get(g) == 'B')
_FA = sorted(g for g in CLOSED_BY_SIBLING if FORM.get(g) == 'A')
check("⛭⛭⛭ ** THE FOLD HAS NOW CLOSED ALL ELEVEN KEY GAPS, EVERY ONE IN FORM B (a SUPERSET), "
      "AND NOT ONE IN THE FORM r7641 USED **: `__cr` and `__lcdm` both bit-identical to the "
      "namesake's, plus `__cr_leafrec1` keys that carry the arm of record.  ⇒ ** So the ask this "
      "file exists to price is FULLY DISCHARGED: `r6893_slice_check`, the last one open at "
      "`r7645+cc66.69b`, was banked by 70 and closes in the same form as the other ten. **  ⌗ The "
      "population this ranges over is FIXED at eleven and is asserted to be, so `open == []` is a "
      "claim about a known set and not a gate whose set has emptied -- the vacuity this file was "
      "repaired for at `cc66.69b`, when the ask was still shrinking.",
      len(GAPS_ALL) == 11 and len(_FB) == 11 and _FA == []
      and sorted(GAPS_ALL) == sorted(_FB)
      and sorted(set(GAPS_ALL) - set(CLOSED_BY_SIBLING)) == [],
      f"form B: {len(_FB)}; form A: {len(_FA)}; population: {len(GAPS_ALL)}; open: "
      f"{sorted(set(GAPS_ALL) - set(CLOSED_BY_SIBLING))}")
check("⛔ ** AND FORM B IS THE ONE THAT BROKE FOUR REGISTERED RECEIPTS SILENTLY **, because a "
      "reader that re-points by changing the FILE and keeping the key gets the NAMESAKE back with "
      "every gate passing: `r6929_geometry_leafrec1`'s `l_A__cr` is 301.7986, the namesake's, where "
      "`r7641`'s file held 302.9431 there.  *Measured, not recalled: the re-keyed sibling's `__cr` "
      "is bit-identical to its namesake's on every key*",
      _eq_cr_identical('r6929_geometry')
      and abs(_scalar('r6929_geometry_leafrec1', 'l_A__cr') - 301.7986427684055) < 5e-7
      and abs(_scalar('r6929_geometry_leafrec1', 'l_A__cr_leafrec1') - 302.9430505935752) < 5e-7,
      "`__cr` held, `__cr_leafrec1` moved")
check("⛭ ** AND THE LAST ONE IS CLOSED THE SAME WAY THE OTHERS WERE: ** `r6893_slice_check` was "
      "open for a DIFFERENT reason from the rest -- no sibling file at all, rather than a sibling "
      "that could not be read for the arm -- and 70 has now banked it.  *So the two reasons a gap "
      "could stay open, a missing file and an unreadable key, are both exhausted, and this file's "
      "price is zero for the first time since `r7641`.*",
      os.path.exists(os.path.join(SPEC, 'r6893_slice_check_leafrec1.npz'))
      and 'r6893_slice_check' in CLOSED_BY_SIBLING
      and FORM.get('r6893_slice_check') == 'B',
      f"r6893_slice_check sibling exists, closed in form {FORM.get('r6893_slice_check')}")
_NA, _NN, _NT = _noop_identity()
check("⛭⛭⛭ ** AND THE NO-OP IDENTITY IS REPRODUCED ON THE ARM OF RECORD, so those legs are "
      "still TESTS and not tautologies **: all "
      f"{_NT} arm-of-record no-op spectra are bit-identical to `r6893_switch_screen_cr_leafrec1`'s "
      f"own `Dl__base` and NONE to the namesake screen's, whose base differs.  ⇒ *cc66.64 proved "
      "substituting a sibling would make `base == base` a tautology; form B moved BOTH sides "
      "together, so the pairing survives the move*",
      _NT == 8 and _NA == _NT and _NN == 0
      and not np.array_equal(
          np.load(os.path.join(SPEC, 'r6893_switch_screen_cr.npz'),
                  allow_pickle=True)['Dl__base'],
          np.load(os.path.join(SPEC, 'r6893_switch_screen_cr_leafrec1.npz'),
                  allow_pickle=True)['Dl__base']),
      f"{_NA} of {_NT} match the ARM screen's base, {_NN} the namesake's")

print()
print(BAR)
print("  PART 1 -- EACH GAP BANK'S OWN KEYS, SPLIT BY ARM")
print(BAR)
for g in GAPS:
    cr = [k for k in KEYS[g] if re.search(r'(^|_)cr(_|$)|__cr$|_cr_', k) and 'lcdm' not in k]
    #: ⛭⛭ r7643: ** 70's THIRD BANK CLOSED A KEY GAP WITH A SIBLING FILE, WHICH IS A BETTER FORM THAN
    #: THE ONE I ASKED FOR AND WHICH THIS TEST DID NOT ANTICIPATE. **  I asked for `__cr_leafrec1`
    #: ENTRIES; `r6929_geometry_leafrec1.npz` instead keeps the key NAMES and holds the arm of
    #: record's values in them (l_A__cr 301.799 -> 302.943, D_M__cr 14017.04 -> 14133.95), with the
    #: `__lcdm` side bit-identical.  *A reader re-points by changing the FILE and keeping the key,
    #: rather than changing every key string -- so the gap is closed and this test, keyed on the
    #: presence of an arm-of-record KEY, would have gone on calling it open.*
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
        #: ⛔ r7643+cc66.58: boundary-anchored, not a substring -- `g in src` is satisfied by
        #: `g + '_leafrec1'`, so a receipt RE-POINTED onto a gap bank's sibling would still score as
        #: reading the gap.  *Latent while no bank in `GAPS` has a sibling -- by construction, since a
        #: sibling is what takes it out of `GAPS` -- and live the moment one is banked and a reader is
        #: moved onto it, which is the whole of the ask.*
        if not _re_present(g, src):
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
        #: ⛔⛭⛭ r7643+cc66.58: ** THE TEMPLATE TEST REQUIRED THE PLACEHOLDER TO FOLLOW `__`
        #: IMMEDIATELY, AND THAT IS THE SAME BLIND SPOT AS THE KEY TEST'S, IN THE MECHANISM BUILT TO
        #: CATCH WHAT LITERALS MISS. **  `var[f'...__{...}']` saw `f'{n}__{t}'` and MISSED
        #: `f'Dl__noop_{t}'`, `f'Dl__xsonly_{t}'`, `f'ls__noop_{t}'` -- every template whose
        #: placeholder sits after another token.
        #:   ⇒ *** And unlike `cc66.56`'s widening this one MOVES VERDICTS: two receipts scored CLEAR
        #:       read `r6911_noop` and `r6915_noop`'s cr side by exactly that form, undeclared, from
        #:       banks with no sibling.  5/3/3 becomes 7/3/1. ***
        #:   ⛭ *The rule is now what it always should have been: the indexed key string carries BOTH a
        #:   key separator `__` and a placeholder `{`.  `Dl__base` has no placeholder and `{x}` has no
        #:   separator, so neither is a key template.*
        tmpl = False
        if var:
            _ks = (re.findall(re.escape(var) + r'\[f[\'\"]([^\'\"]*)[\'\"]\]', code)
                   + re.findall(r'lambda[^\n]*:\s*' + re.escape(var)
                                + r'\[f[\'\"]([^\'\"]*)[\'\"]\]', code))
            tmpl = any(_is_keytmpl(s) for s in _ks)
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
      all(not _armkeys_in(_code_of(r)) and not _tmplkeys_in(_code_of(r)) for r in CLEAR),
      f"{sum(1 for r in CLEAR if _armkeys_in(_code_of(r)) or _tmplkeys_in(_code_of(r)))}"
      f" of {len(CLEAR)} clear receipts carry it in code")
check("⛔⛭⛭ the arm-key test is BOUNDARY-ANCHORED, and the substring form it replaces is measurably "
      "wrong rather than merely narrower: `'__cr' in k` misses every key whose arm tag follows another "
      "token, which is five of the eight real arm keys sampled here -- and the boundary form still "
      "rejects the two negative controls a looser `'cr' in k` would take.  ⌗ *No verdict in this file "
      "moves: the one bank with a sibling carries only `X__cr` keys, so the defect was LATENT and not "
      "live, which is stated rather than dressed up as a correction*",
      all(ARM_RE.search(k) for k in _ARM_SEEN)
      and sum(1 for k in _ARM_SEEN if '__cr' not in k) == 5
      and not ARM_RE.search('Dl__combvl') and not ARM_RE.search('Dl__crust')
      and not _armkeys_in("z['Dl__combvl']") and _armkeys_in("z['Dl__unset_cr']") == ['Dl__unset_cr'],
      f"{sum(1 for k in _ARM_SEEN if '__cr' not in k)} of {len(_ARM_SEEN)} sampled arm keys are "
      f"invisible to the substring form")
check("⛔⛭⛭ the KEY-TEMPLATE test is placeholder-anywhere, and the `__{` form it replaces is "
      "measurably wrong rather than merely narrower: three of the four sampled templates are "
      "invisible to it, and they are the ones two CLEAR-scored receipts used to read `r6911_noop` and "
      "`r6915_noop`'s cr side.  ⇒ ** This is the SECOND defect of this family in this file, after the "
      "arm-key substring at `cc66.56` -- and unlike that one it MOVED VERDICTS, 5/3/3 to 7/3/1. **  "
      "⛔ *The `CLEAR` verdicts' second check used the same narrow rule, so a second way built from "
      "the first way's regex family is not an independent read*",
      all('__' in s and '{' in s for s in _TMPL_SEEN)
      and sum(1 for s in _TMPL_SEEN if not TMPL_RE.search(s)) == 3
      and not _is_keytmpl('Dl__base') and not _is_keytmpl('{t}')
      and not _is_keytmpl('{n}_{t}')
      and _tmplkeys_in("NOOP[f'Dl__noop_{t}']") == ['Dl__noop_{t}']
      and _tmplkeys_in("z[f'Dl__base']") == []
      and _tmplkeys_in("z[f'{t}']") == []
      and _re_present('r6929_noop', "np.load('r6929_noop.npz')") is not None
      and _re_present('r6929_noop', "np.load('r6929_noop_leafrec1.npz')") is None,
      f"{sum(1 for s in _TMPL_SEEN if not TMPL_RE.search(s))} of {len(_TMPL_SEEN)} sampled key "
      f"templates are invisible to the `__{{` form")
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
check("⛔⛭⛭ THE VERDICT COUNTS ARE PINNED, AND THEY MOVED TWICE -- ONCE WHEN 70's THIRD BANK LANDED "
      "AND ONCE WHEN THIS FILE'S OWN TEMPLATE TEST WAS REPAIRED: 7 BLOCKED, 3 DECLARED, 1 CLEAR of "
      "**11** readers.  ⛔ *The 5 / 3 / 3 this gate pinned from `cc66.46` to `cc66.57` was measured "
      "with a template test that required the placeholder to follow `__` immediately, so it could not "
      "see `f'Dl__noop_{t}'` -- and two receipts reading `r6911_noop` and `r6915_noop`'s cr side by "
      "that form were scored CLEAR.  The counts before the bank, 7 / 3 / 3 of 13, were measured the "
      "same way and are not a baseline either.*  ⇒ ** A pinned count caught the move both times; what "
      "it cannot catch is a METHOD that is wrong in the same way on both sides of the pin, which is "
      "why the detector itself is now gated below **.  ⛔⛭ *And the family split in this same pin was "
      "GUESSED at 3 / 4 on the first attempt and is 5 / 2 -- the third time this file has recorded "
      "that error and the second time on itself.  The run says it; I did not read the run.*  "
      "⛔⛔ ** AND THEY MOVED A THIRD TIME AT r7645+cc66.68, TO 9 / 3 / 1 OF 13 WITH THE FAMILY "
      "SPLIT 7 / 2 -- and this time NOTHING IN THE CORPUS MOVED: the detector's SUBJECT did. **  "
      "*`GAPS` used to be the OPEN gaps, so a bank closing silently removed it, and every receipt "
      "that read only it, from the count -- a count that shrinks when the problem is SOLVED and also "
      "when it is merely RENAMED, and cannot tell those apart.  r7643's fold closed ten of eleven "
      "and would have taken this count to 1 / 0 / 0 of 1.  The detector now scores `GAPS_ALL` and "
      "`GAPS_OPEN` carries the ask, so this count measures READERS and PART 0 measures CLOSURE.*  "
      "⇒ *** A pinned count caught the move all three times; what it could not catch was its own "
      "set definition drifting under it. ***",
      len(VERDICT) == 13 and len(BLOCKED) == 9 and len(DECLARED) == 3 and len(CLEAR) == 1
      and len(_by_family) == 7 and len(_needs_more) == 2,
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
#: ⛔⛭ r7643+cc66.58: ** THE EXAMPLE THIS GATE PINNED WAS AN ARTEFACT OF THE NARROW TEMPLATE TEST. **
#:   It asserted that `a_source_with_no_physics_…` is attributed to `r6919_geometry` ALONE where a
#:   file-wide search also names `r6919_noop`.  *Under the repaired test the LOCALISED search names
#:   both, because `r6919_noop` IS indexed by a template on its own variable -- in the
#:   `f'Dl__noop_{t}'` form the narrow rule could not see.  So the distinction was the defect's, not
#:   the localisation's.*
#:   ⇒ *** The localisation is still load-bearing, and the gate is re-pinned on the case where it
#:       actually bites: `the_combs_resolution_…` has NO template attribution at all once localised,
#:       where a file-wide search would name `r6925_noop` and `r6929_noop` by template.  Those two do
#:       block it -- by LITERAL -- so the file-wide rule would get the right banks for the wrong
#:       reason and label the mechanism `[both]` where it is `[literal]`.  An ask is priced on what
#:       the receipt does, so the mechanism has to be right too. ***
_comb = [r for r in VERDICT if 'combs_resolution' in r]
if _comb:
    _ch = VERDICT[_comb[0]][0]
    _ctm = sorted(g for g, (_c, _l, tm) in _ch.items() if tm)
    _clit = sorted(g for g, (c, _l, _t) in _ch.items() if c)
    print(f"    `the_combs_resolution_…`: template attribution {_ctm or 'none'}; literal {_clit}")
    check("⛭ AND THE LOCALISATION IS LOAD-BEARING FOR THE MECHANISM, re-pinned on the case where it "
          "bites: `the_combs_resolution_…` has NO template attribution once the search is localised "
          "to each bank's own variable, where a file-wide one would name `r6925_noop` and "
          "`r6929_noop` by template.  Both DO block it, by literal -- so the file-wide rule would "
          "reach the right banks by the wrong mechanism and label the ask `[both]` where it is "
          "`[literal]`.  ⛔ *The example this gate carried until `cc66.58` was an artefact of the "
          "narrow template test and is recorded as one above*",
          #: ⛭⛭ r7645+cc66.68: re-pinned with the set split.  *`r6929_geometry` is back in
          #: the scored set and this receipt DOES read it by template, so localisation now attributes
          #: exactly that one bank that way.  The gate's content is unchanged and is now stated as the
          #: EXCLUSION rather than as an empty list: the two NOOP banks must be ABSENT from the
          #: template attribution and PRESENT in the literal one, because a file-wide search would
          #: name them by template and label the ask `[both]` where it is `[literal]`.*
          _ctm == ['r6929_geometry']
          and set(_clit) == {'r6925_noop', 'r6929_geometry', 'r6929_noop'}
          and not ({'r6925_noop', 'r6929_noop'} & set(_ctm)),
          f"template {_ctm}; literal {_clit}")

check("⛭ THE ASK HAS A COUNT: re-running the `{geometry,noop}` family with `__cr_leafrec1` entries "
      "clears every receipt blocked only by it, and the rest name exactly what else they need.  ⇒ "
      "** That is the whole of item ⑵'s remaining key-gap half, priced **",
      len(_by_family) + len(_needs_more) == len(BLOCKED) and len(BLOCKED) > 0,
      f"{len(_by_family)} + {len(_needs_more)} against {len(BLOCKED)} blocked")
_REACHED = [g for g in GAPS_ALL
            if os.path.exists(os.path.join(SPEC, g + '_leafrec1.npz'))
            and any('leafrec1' in k for k in
                    np.load(os.path.join(SPEC, g + '_leafrec1.npz'), allow_pickle=True).files)]
#: ⛭⛭⛭ r7645+cc66.68: ** AND THIS GATE IS THE EXACT INVERSE OF WHAT IT SAID, which is the whole
#:   point of having pinned it. **  *From `cc66.46` to `cc66.67` it asserted that NONE of these gaps
#:   had been reached by a second bank -- true then, and the reason item ⑵ still had a key-gap half.
#:   `r7643`'s fold reached TEN of the eleven.  It is written over `GAPS_ALL` rather than the open
#:   set so that it cannot pass by the set emptying, and it is two-sided on the count.*
#: ⛭⛭⛭ r7649+cc66.78: ** AND IT HAS MOVED ONE FURTHER, FOR THE SECOND AND LAST TIME: ELEVEN OF
#:   ELEVEN. **  *`70` banked `r6893_slice_check` with an arm-of-record key, which was the single
#:   gap `r7643`'s fold had left standing and the reason this gate pinned TEN.  The reach set is now
#:   the whole of `GAPS_ALL`, so the exclusion that named `r6893_slice_check` is gone and the count
#:   is pinned at eleven.  The population is pinned ALONGSIDE the reach -- `len(GAPS_ALL) == 11` --
#:   because a reach gate written as `_REACHED == GAPS_ALL` passes on an EMPTY `GAPS_ALL`, which is
#:   the same vacuity this file was repaired for at `cc66.69b`: the equality has to be anchored to
#:   the population's own size or it is satisfied by there being nothing to reach.*
check("⛭⛭⛭ ** THE FOLD HAS NOW REACHED ALL ELEVEN KEY GAPS WITH AN ARM-OF-RECORD KEY, which is the "
      "exact inverse of what this gate asserted from cc66.46 to cc66.67 ** -- `r7643`'s fold "
      "reached ten, and `70`'s banking of `r6893_slice_check`, the one it had left, closes the "
      "last.  ⇒ *Written over GAPS_ALL and pinned to its size so it cannot pass by the population "
      "emptying, which is how it passed vacuously once this revision before the set split*",
      len(GAPS_ALL) == 11 and sorted(_REACHED) == sorted(GAPS_ALL) and len(_REACHED) == 11,
      f"{len(_REACHED)} of {len(GAPS_ALL)} reached; not reached: "
      f"{sorted(set(GAPS_ALL) - set(_REACHED))}")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
