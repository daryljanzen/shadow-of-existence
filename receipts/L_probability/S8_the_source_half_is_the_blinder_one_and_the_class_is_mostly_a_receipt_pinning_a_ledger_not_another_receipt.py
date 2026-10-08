#!/usr/bin/env python3
"""L_probability receipt -- `PO-78`, THE HALF `r7228` EXCLUDED: the `1,154` quote-pin keys that target
a SOURCE rather than a paper, read by `r7228`'s own reversal instrument, sliced out of its pinned source
and executed here rather than copied.

*** ⬭⬭⬭ TWO FINDINGS, AND THE SECOND ONE RENAMES THE CLASS. ***

** ⓵ THE SOURCE HALF IS THE BLINDER ONE, AND THE DIFFERENCE IS DISTINGUISHABLE. **  *Of the `326`
readable source keys only `56` -- **`17.2%`** -- would go red if the clause they quote were turned
round, against the paper half's `279` of `1,140`, **`24.5%`**.*  ⇒ ** `z = 2.77`, `p = 0.0057` on a
two-proportion test. **  *On the looser measure it holds the same way: `82.8%` of readable source keys
survive at least ONE reversal of their own clause against the paper half's `75.5%`.*

⇒ ***So `one in four would notice` is a fact about PAPERS and not about pinning in general.*** *That
was the pre-registered prediction and the `indistinguishable` branch -- which would have made `r7228`'s
framing the wrong frame -- is the one that did not fire.*

** ⓶ AND THE LARGEST EXCLUSION IS AN ANSWER RATHER THAN A GAP: THE CLASS IS MOSTLY A RECEIPT PINNING
   A LEDGER. **  *`469` of the `1,154` keys are `ABSENT` -- their literal is in no receipt but the one
   that pins it.  The pre-registration fixed the haystack as the RECEIPT TREE, so a key absent from it
   points somewhere else, and the cheap thing to do is look.*  ⇒ ** In a `120`-key sample, `72` are
   found in the project's own registers or instrument modules --- `56` in a register against `28` in a
   module. **  ⌗ ***`a receipt pinning another receipt's source` is not what this half mostly is.  It is
   a receipt pinning a LEDGER,*** *and the baseline's `SOURCE` label means only `the trace did not name
   a `.tex``.*

### ⌗ WHY A DIFFERENCE HERE CANNOT BE A DIFFERENCE BETWEEN TWO INSTRUMENTS

**The transforms, the clause extractor, the site cap, the markup pattern and `classify` itself are
SLICED OUT of `r7228`'s source at the pinned commit and executed, not copied** -- `L-254`'s banked
lesson, that a rule in two places drifts and a text comparison between two copies reports the
divergence only after both are written.  *A digest gate on that slice goes red if the block moves.*

⌗ *The site FINDING is this receipt's own, because a per-file loop over a `13 MB` tree is `2.3x` the
cost of the same scan on bytes.  **That is not the rule that decides a verdict, and the equivalence is
MEASURED rather than asserted:** with both new filters switched off, this receipt's byte locator and
`r7228`'s own `classify` return identical tallies on all eight shared buckets of a `60`-key sample.*

### ⓷ TWO FILTERS THE PAPER HALF DID NOT NEED, BOTH DECLARED

* **the pinning receipt's own file.**  *A source key's literal is IN the receipt that pins it, by
  construction -- the string sits in its own source.*  ⇒ *Counting that site makes every key
  self-satisfying; on the sample the `ABSENT` bucket moves `2 → 27` when it is removed.*
* **code is not a clause.**  *A site is PROSE in the module docstring or on a line beginning `#`;
  anything else is CODE.  `218` keys of `1,154` have no prose site at all --- a fifth of the half, so
  the pre-registered THIRD OUTCOME, the code bucket swallowing the population, did not fire.*
  ⚠ ** A gate label is prose sitting in a code position and this rule calls it CODE.  Stated as the
  rule's limit rather than hidden. **

⚠ ** THE EXCLUSIONS, COUNTED: ** `469` `ABSENT`, `218` `CODE`, `122` `SATURATED` (more than twenty
foreign sites, a pin on the FILE), `17` `UNFLIPPABLE`, `2` `MARKUP`.  *`326` readable of `1,154`, and
every rate above is against that denominator and says so.*

⌗ ***Two things this receipt got wrong first, recorded because a buried near-miss is worth nothing.***
*Its first draft re-derived the `ABSENT` list with a second full scan of the `13 MB` tree, for a list the
first pass had computed and thrown away --- `7.6` of `19` seconds.*  *And the obvious one-pass
alternative, a single compiled alternation of all `1,154` literals, was tried and runs in `43` seconds
against `6`: recorded so the next seat does not spend an afternoon on it.*

⛔ *No verdict is filed on any baseline key and no file outside this one is written.  `17` gates, all
pass, about thirteen seconds.  No assertion on wall-clock time.*
"""
import collections
import hashlib
import json
import os
import random
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
PIN = '94c63709496d76076836371475ea850d03759408'
BASELINE = 'corpus/quote_pin_baseline.tsv'
PAPERS = ('BH_causality_v2', 'janzen_circle_v3', 'SdS-slicing-curve_v2', 'modern_parallax',
          'groupoid_paper', 'shadow_of_existence', 'CR_framework', 'slicing_operator', 'range_paper',
          'canonical_time', 'dynamics_paper', 'algebroid_paper', 'boundary_paper',
          'matter_sector_paper', 'CR_cosmology', 'cosmogenesis_paper', 'geometric_core_paper',
          'CR_synthesis')
S7 = ('receipts/L_probability/S7_the_paper_pins_are_read_by_reversing_the_clause_they_quote_and_'
      'only_one_in_four_would_notice.py')


def _run(*a):
    return subprocess.run(a, cwd=ROOT, capture_output=True, text=True, check=True).stdout


def _at(rev, path):
    return _run('git', 'show', f'{rev}:{path}')


# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("A. THE INSTRUMENT IS r7228's, IMPORTED FROM ITS SOURCE AT THE PIN AND NOT COPIED")

# ⛭⛭ `L-254`'s banked lesson, applied: a rule in two places DRIFTS, and a text comparison between two
#    copies reports a divergence only after both are written.  So the transforms, the clause extractor,
#    the site cap, the markup pattern and `classify` itself are SLICED OUT of `r7228`'s own source at
#    the pinned commit and executed here.  ⇒ ** If that block changes, this receipt's digest gate goes
#    red rather than this receipt quietly measuring a different instrument. **
_s7 = _at(PIN, S7).split('\n')
_a = next(i for i, l in enumerate(_s7) if l.startswith('CLAUSE_DELIM = '))
while _a > 0 and _s7[_a - 1].startswith('#'):
    _a -= 1
_b = next(i for i, l in enumerate(_s7) if i > _a and l.startswith('# \u2500'))
BLOCK = '\n'.join(_s7[_a:_b]).rstrip() + '\n'
BLOCK_SHA = 'b40eb4d05a3989761c94105a63347ac7964d3d9f07ff956269e60c9667f644a9'
_got = hashlib.sha256(BLOCK.encode()).hexdigest()
print(f"    sliced r7228 lines {_a + 1}..{_b}  {len(BLOCK)} chars  sha256 {_got[:12]}")
gate(f"Ⓖ① the instrument is r7228's own block, byte-identical at the pin -- so a difference between the "
     f"two halves below cannot be a difference between two instruments ({_got[:12]})",
     _got == BLOCK_SHA)

I = {'re': re, 'collections': collections, 'json': json}
exec(compile(BLOCK, S7 + ' (sliced)', 'exec'), I)
WANT = ('CLAUSE_DELIM', 'WINDOW', 'SITE_CAP', 'AUX', 'NEGATED', 'UNNEG', 'ANTONYM', 'QUANTIFIER',
        'MARKUP', 'clause_at', 'reversals', 'read_baseline', 'classify')
gate(f"Ⓖ② and it brings every name the measurement needs -- {len(WANT)} of them, none redefined here",
     all(n in I for n in WANT))
clause_at, reversals, read_baseline, classify = (I['clause_at'], I['reversals'], I['read_baseline'],
                                                 I['classify'])
MARKUP, SITE_CAP, AUX = I['MARKUP'], I['SITE_CAP'], I['AUX']
gate(f"Ⓖ③ the site cap is the one r7228 used, {SITE_CAP}, and the antonym and quantifier tables are the "
     f"same sizes ({len(I['ANTONYM'])}/{len(I['QUANTIFIER'])})",
     SITE_CAP == 20 and len(I['ANTONYM']) == 40 and len(I['QUANTIFIER']) == 9)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("B. THE TWO POPULATIONS, AND THE HAYSTACK THE SOURCE HALF NEEDS")

_bl = _at(PIN, BASELINE)


def rows_of(target):
    out = []
    for ln in _bl.split('\n'):
        if not ln.strip() or ln.startswith('#'):
            continue
        f = ln.split('\t')
        if len(f) >= 6 and f[2] == target:
            out.append((f[0], json.loads(f[1]), f[3], f[4], f[5]))
    return out


PAPER_ROWS, SOURCE_ROWS = rows_of('PAPER'), rows_of('SOURCE')
print(f"    PAPER-targeted keys   {len(PAPER_ROWS)}")
print(f"    SOURCE-targeted keys  {len(SOURCE_ROWS)}")
gate(f"Ⓖ④ the two halves are 1489 and 1154 keys of the pinned baseline, which is the whole of it "
     f"({len(PAPER_ROWS)} + {len(SOURCE_ROWS)})",
     len(PAPER_ROWS) == 1489 and len(SOURCE_ROWS) == 1154)

# ⛭⛭ THE HAYSTACK IS THE RECEIPT TREE, read from the working tree rather than through a thousand
#    `git show` calls -- and then PUT BACK to the pin's state for any file that differs, so the
#    population is the pin's as a FACT and not as a hope.
#    ⌗ The first draft only ASSERTED that the tree matched the pin and went red the moment this push
#      also repaired another receipt -- which is a real event, not a reason to widen the assertion.
_diff = [l for l in _run('git', 'diff', '--name-only', PIN, '--', 'receipts/').split('\n')
         if l.endswith('.py')]
SELF = os.path.relpath(os.path.abspath(__file__), ROOT)
SRC = {}
for dirpath, _dirs, names in os.walk(os.path.join(ROOT, 'receipts')):
    for n in sorted(names):
        if n.endswith('.py'):
            q = os.path.relpath(os.path.join(dirpath, n), ROOT)
            SRC[q] = open(os.path.join(ROOT, q), encoding='utf-8', errors='replace').read()
_PINNED = {l for l in _run('git', 'ls-tree', '-r', PIN, '--name-only', '--', 'receipts/').split('\n')
           if l.endswith('.py')}
_restored, _dropped = [], []
for q in sorted(set(_diff) | (set(SRC) - _PINNED)):
    if q in _PINNED:
        SRC[q] = _at(PIN, q)
        _restored.append(q)
    else:
        SRC.pop(q, None)
        _dropped.append(q)
print(f"    tracked sources differing from the pin: {_diff or 'none'}")
print(f"    restored to the pin's content: {len(_restored)}   dropped as added since: {len(_dropped)}")
gate(f"Ⓖ⑤ the haystack IS the pin's receipt tree, not merely asserted to be -- {len(_restored)} "
     f"differing file(s) put back to their pinned content and {len(_dropped)} added since the pin "
     f"dropped, leaving {len(SRC)} sources against the pin's {len(_PINNED)}",
     set(SRC) == _PINNED and all(SRC[q] == _at(PIN, q) for q in _restored))
gate(f"Ⓖ⑤ᵇ and this receipt is one of the dropped, because a receipt has no business inside the "
     f"population it measures ({SELF in _dropped})", SELF in _dropped)

TEX = {p: _at(PIN, f'corpus/{p}.tex') for p in PAPERS}
print(f"    receipt sources       {len(SRC)}  ({sum(len(v) for v in SRC.values()):,} characters)")
print(f"    paper bodies          {len(TEX)}  ({sum(len(v) for v in TEX.values()):,} characters)")
gate(f"Ⓖ⑥ and the source half's haystack is the larger object by four and a half times, which is part "
     f"of why it was left out of r7228 rather than folded in "
     f"({sum(len(v) for v in SRC.values()) // sum(len(v) for v in TEX.values())}x)",
     sum(len(v) for v in SRC.values()) > 4 * sum(len(v) for v in TEX.values()))

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("C. THE PAPER HALF RE-DERIVED ON THIS TREE, BECAUSE A COMPARISON AGAINST A NUMBER THAT MOVED IS NONE")

PT = classify(PAPER_ROWS, TEX)[0]
_pread = PT['REVERSAL'] + PT['REVERSAL-PARTIAL'] + PT['DISCRIMINATING']
print(f"    readable {_pread}   discriminating {PT['DISCRIMINATING']}   reversal {PT['REVERSAL']}   "
      f"partial {PT['REVERSAL-PARTIAL']}")
gate(f"Ⓖ⑦ r7228's published paper-half numbers come back UNCHANGED on the merged tree -- 279 of 1140 "
     f"readable discriminating, 442 surviving all four ({PT['DISCRIMINATING']} of {_pread}, "
     f"{PT['REVERSAL']})",
     PT['DISCRIMINATING'] == 279 and _pread == 1140 and PT['REVERSAL'] == 442)


# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("D. THE SOURCE HALF, WITH TWO FILTERS THE PAPER HALF DID NOT NEED")

# ⛭⛭ FILTER ONE: THE PINNING RECEIPT'S OWN FILE.  ** A source key's literal is IN the receipt that
#    pins it, by construction ** -- the string sits in its own source.  Counting that site would make
#    every key self-satisfying, so the pinner's own file is removed from its own haystack.  *The paper
#    half had no such site and needed no such filter.*
# ⛭⛭ FILTER TWO: CODE IS NOT A CLAUSE.  A source carries prose AND code.  A site is PROSE when it lies
#    in the module DOCSTRING or on a line whose first non-space character is `#`; anything else is CODE
#    -- an identifier, a path, an f-string, a gate label.  ⚠ ** A gate label is prose sitting in a code
#    position and this rule calls it CODE.  Stated as the rule's limit rather than hidden. **
# ⌗ The locating is done on BYTES, which is 2.3x the speed of the same scan on `str` over 13 MB, and
#   the char offset each verdict needs is then taken inside the ONE file the byte scan named.  The rule
#   that decides a verdict is untouched by that; `Ⓖ⑩` measures the equivalence rather than claiming it.
_names = sorted(SRC)
_SB = {p: SRC[p].encode('utf-8', 'replace') for p in _names}
_parts, _offs, _pos = [], [], 0
for p in _names:
    _parts.append(_SB[p])
    _offs.append((_pos, p))
    _pos += len(_SB[p]) + 3
    _parts.append(b'\n\x00\n')
BLOB = b''.join(_parts)
_starts = [o for o, _ in _offs]


def files_with(lit, cap):
    """the files holding this literal, by one byte scan; stops once the cap cannot matter"""
    import bisect
    b, out, k = lit.encode('utf-8', 'replace'), [], BLOB.find(lit.encode('utf-8', 'replace'))
    while k >= 0:
        i = bisect.bisect_right(_starts, k) - 1
        out.append(_offs[i][1])
        if len(out) > cap:
            break
        k = BLOB.find(b, k + 1)
    return out


def _prose_spans(text):
    """the module docstring's span and every comment LINE's span, computed once per file"""
    spans = []
    a = text.find('"""')
    if a >= 0:
        b = text.find('"""', a + 3)
        if b > a:
            spans.append((a, b + 3))
    pos = 0
    for ln in text.split('\n'):
        if ln.lstrip().startswith('#'):
            spans.append((pos, pos + len(ln)))
        pos += len(ln) + 1
    return spans


_PS = {}


def is_prose(path, off):
    if path not in _PS:
        _PS[path] = _prose_spans(SRC[path])
    return any(a <= off < b for a, b in _PS[path])


def measure(rows, exclude_self=True, prose_only=True):
    """r7228's verdict rule, over sites the byte scan found"""
    t = collections.Counter()
    rev, disc, code, absent = [], [], [], []
    for rec, lit, tier, flags, verdict in rows:
        if MARKUP.search(lit):
            t['MARKUP'] += 1
            continue
        # ⌗ the scan stops as soon as the cap cannot be met: the cap is on FOREIGN sites, so the
        #   pinner's own count is added to it rather than guessed at with a loose margin
        _own = SRC.get(rec, '').count(lit) if exclude_self else 0
        hits = files_with(lit, SITE_CAP + _own + 1)
        sites = []
        for p in dict.fromkeys(hits):
            if exclude_self and p == rec:
                continue
            k = SRC[p].find(lit)
            while k >= 0:
                sites.append((p, k))
                k = SRC[p].find(lit, k + 1)
        if len(sites) > SITE_CAP:
            t['SATURATED'] += 1
            continue
        if not sites:
            t['ABSENT'] += 1
            absent.append((rec, lit))
            continue
        pros = [s for s in sites if is_prose(*s)] if prose_only else sites
        if not pros:
            t['CODE'] += 1
            code.append((rec, lit, sites[0]))
            continue
        allsurv, anysurv, moved, w = True, False, 0, None
        for p, off in pros:
            c = clause_at(SRC[p], off, off + len(lit))
            if lit not in c:
                continue
            for name, fl in reversals(c).items():
                moved += 1
                if lit in fl:
                    anysurv = True
                    w = w or (p, name, c, fl)
                else:
                    allsurv = False
        if moved == 0:
            t['UNFLIPPABLE'] += 1
        elif allsurv:
            t['REVERSAL'] += 1
            rev.append((rec, lit, w, flags))
        elif anysurv:
            t['REVERSAL-PARTIAL'] += 1
        else:
            t['DISCRIMINATING'] += 1
            disc.append((rec, lit, flags))
    return t, rev, disc, code, absent


ST, REV, DISC, CODE, ABSENT_KEYS = measure(SOURCE_ROWS)
for k in ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'CODE', 'UNFLIPPABLE', 'MARKUP',
          'ABSENT', 'SATURATED'):
    print(f"    {k:18s} {ST[k]}")
SREAD = ST['REVERSAL'] + ST['REVERSAL-PARTIAL'] + ST['DISCRIMINATING']
SLIM = ST['CODE'] + ST['UNFLIPPABLE'] + ST['MARKUP'] + ST['ABSENT'] + ST['SATURATED']
gate(f"Ⓖ⑧ the buckets partition the source half -- {SREAD} readable plus {SLIM} excluded is "
     f"{len(SOURCE_ROWS)}", SREAD + SLIM == len(SOURCE_ROWS))

# ⛭ THE LOCATOR IS NOT THE RULE, AND THE EQUIVALENCE IS MEASURED RATHER THAN ASSERTED.
_sample = random.Random(7230).sample(SOURCE_ROWS, 60)
_mine = measure(_sample, exclude_self=False, prose_only=False)[0]
_theirs = classify(_sample, SRC)[0]
SHARED = ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'UNFLIPPABLE', 'MARKUP', 'ABSENT',
          'SATURATED', 'NO-CLAUSE')
_off = {k: (_mine[k], _theirs[k]) for k in SHARED if _mine[k] != _theirs[k]}
print(f"    equivalence on 60 sampled keys, both filters OFF, on the eight buckets both compute: "
      f"{'identical' if not _off else _off}")
gate(f"Ⓖ⑨ with both filters off, this receipt's byte locator and r7228's own per-file `classify` "
     f"return the SAME tally on a 60-key sample -- so every difference below is one of the two "
     f"declared filters and not the site finding", not _off)
_noself = measure(_sample, exclude_self=False)[0]['ABSENT']
_self = measure(_sample)[0]['ABSENT']
gate(f"Ⓖ⑩ and the self-site filter is not cosmetic: on that sample the ABSENT bucket goes {_noself} "
     f"-> {_self} when the pinning receipt's own file is removed from its own haystack, which is the "
     f"site every source key has by construction", _self > _noself)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("E. THE COMPARISON, WHICH IS THE WHOLE POINT, AND IT IS DECIDED BY A NUMBER")

import math

P1, N1 = PT['DISCRIMINATING'], _pread
P2, N2 = ST['DISCRIMINATING'], SREAD
R1, R2 = P1 / N1, P2 / N2
_pool = (P1 + P2) / (N1 + N2)
_se = math.sqrt(_pool * (1 - _pool) * (1 / N1 + 1 / N2))
Z = (R1 - R2) / _se
PVAL = math.erfc(abs(Z) / math.sqrt(2))
print(f"    PAPER   would go red  {P1:4d} of {N1:5d}   {100 * R1:5.1f}%")
print(f"    SOURCE  would go red  {P2:4d} of {N2:5d}   {100 * R2:5.1f}%")
print(f"    two-proportion z = {Z:.2f},  p = {PVAL:.4f}")
gate(f"Ⓖ⑪ THE SOURCE HALF IS THE BLINDER ONE, as pre-registered: {100 * R2:.1f}% of its readable keys "
     f"would go red against the paper half's {100 * R1:.1f}%", R2 < R1)
gate(f"Ⓖ⑫ and the difference is DISTINGUISHABLE rather than eyeballed -- z = {Z:.2f}, p = {PVAL:.4f} "
     f"on a two-proportion test, so `indistinguishable` is the refuting outcome that did NOT fire "
     f"and the finding is about PAPERS versus SOURCES, not about pinning in general", PVAL < 0.05)
_s1 = (PT['REVERSAL'] + PT['REVERSAL-PARTIAL']) / N1
_s2 = (ST['REVERSAL'] + ST['REVERSAL-PARTIAL']) / N2
print(f"    survive at least one reversal:  PAPER {100 * _s1:.1f}%   SOURCE {100 * _s2:.1f}%")
gate(f"Ⓖ⑬ and it holds on the looser measure too -- {100 * _s2:.1f}% of readable source keys survive "
     f"at least one reversal of their own clause against the paper half's {100 * _s1:.1f}%", _s2 > _s1)
gate(f"Ⓖ⑭ the THIRD OUTCOME did NOT fire: the code bucket is {ST['CODE']} of {len(SOURCE_ROWS)}, which "
     f"is a fifth of the half and not a swallowing, so the comparison is well posed and the rate is "
     f"publishable", ST['CODE'] < len(SOURCE_ROWS) / 3)

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("F. THE EXCLUSIONS, AND WHAT THE LARGEST OF THEM TURNS OUT TO BE")

print(f"    ABSENT      {ST['ABSENT']:4d}  not in any receipt but its own pinner")
print(f"    SATURATED   {ST['SATURATED']:4d}  more than {SITE_CAP} sites -- a pin on the FILE")
print(f"    CODE        {ST['CODE']:4d}  every site in code rather than in docstring or comment")
print(f"    UNFLIPPABLE {ST['UNFLIPPABLE']:4d}  no declared transform moves the clause")
print(f"    MARKUP      {ST['MARKUP']:4d}  the literal quotes a reference key or a label")

# ⛭⛭ THE ABSENT BUCKET IS NOT A GAP, IT IS AN ANSWER TO `WHAT DOES A SOURCE PIN POINT AT?`
#    The pre-registration fixed the haystack as the RECEIPT TREE.  A key absent from it is pointing
#    somewhere else, and the cheapest way to find out where is to look.
_other = {}
for _d, _pat in (('scripts', 'scripts'), ('corpus', 'corpus')):
    for _dp, _dn, _ns in os.walk(os.path.join(ROOT, _pat)):
        for _n in _ns:
            if _n.endswith('.py'):
                _r = os.path.relpath(os.path.join(_dp, _n), ROOT)
                _other[_r] = open(os.path.join(ROOT, _r), encoding='utf-8', errors='replace').read()
_regs = {}
for _r in sorted(os.listdir(ROOT)) + ['receipts/INDEX.md']:
    _p = os.path.join(ROOT, _r)
    if _r.endswith('.md') and os.path.isfile(_p):
        _regs[_r] = open(_p, encoding='utf-8', errors='replace').read()
_MODB = b'\n\x00\n'.join(v.encode('utf-8', 'replace') for v in _other.values())
_REGB = b'\n\x00\n'.join(v.encode('utf-8', 'replace') for v in _regs.values())
# ⌗ the ABSENT keys are the ones the main pass already found; re-deriving them cost a second full
#   scan of the tree in this receipt's first draft, for a list it had thrown away.
_abs_keys = ABSENT_KEYS
_samp = random.Random(7231).sample(_abs_keys, min(120, len(_abs_keys)))
_in_mod = sum(1 for _r, _l in _samp if _l.encode('utf-8', 'replace') in _MODB)
_in_reg = sum(1 for _r, _l in _samp if _l.encode('utf-8', 'replace') in _REGB)
_in_either = sum(1 for _r, _l in _samp
                 if _l.encode('utf-8', 'replace') in _MODB or _l.encode('utf-8', 'replace') in _REGB)
print(f"\n    of {len(_samp)} sampled ABSENT keys ({len(_abs_keys)} in the bucket):")
print(f"      found in scripts/ or corpus/ modules  {_in_mod}")
print(f"      found in a root REGISTER or the INDEX {_in_reg}")
print(f"      found in one or the other             {_in_either}  "
      f"({100 * _in_either / len(_samp):.0f}%)")
gate(f"Ⓖ⑮ the ABSENT bucket is not a measurement gap but a fact about where source pins POINT: "
     f"{100 * _in_either / len(_samp):.0f}% of a {len(_samp)}-key sample is found in the project's own "
     f"registers or instrument modules, which the pre-registered haystack excludes by construction",
     _in_either > 0.5 * len(_samp))
gate(f"Ⓖ⑯ and the registers dominate the modules in that sample ({_in_reg} against {_in_mod}), so "
     f"`a receipt pinning another receipt` is NOT what the source half mostly is -- it is a receipt "
     f"pinning a LEDGER", _in_reg > _in_mod)

head("AND EVERY REVERSAL VERDICT CARRIES THE CLAUSE IT SURVIVES")
gate(f"Ⓖ⑰ every one of the {len(REV)} source-half reversal verdicts exhibits a reversed clause that "
     f"CHANGED and still contains the literal",
     all(w and lit in w[3] and w[2] != w[3] for _, lit, w, _ in REV))


def window(a, b, span=56):
    i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), 0)
    lo = max(0, i - span)
    return (('...' if lo else '') + a[lo:i + span].replace('\n', ' '),
            ('...' if lo else '') + b[lo:i + span].replace('\n', ' '))


for rec, lit, w, flags in REV[:3]:
    before, after = window(w[2], w[3])
    print(f"\n    {os.path.basename(rec)[:70]}")
    print(f"      pins    {lit!r}")
    print(f"      in      {os.path.basename(w[0])[:70]}")
    print(f"      clause  {before!r}")
    print(f"      {w[1]:7s} {after!r}")
    print("      ⇒ the clause now says something that file does not, and the pin is still green")

# ──────────────────────────────────────────────────────────────────────────────────────────────────
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print("""
  THE SOURCE HALF OF THE REVERSAL CLASS IS THE BLINDER ONE AND THE CLASS IS MOSTLY NOT WHAT ITS NAME
  SAYS.  Of 326 readable source-targeted quote-pin keys, 56 -- 17.2% -- would go red if the clause
  they quote were turned round, against the paper half's 279 of 1,140 at 24.5%; z = 2.77, p = 0.0057,
  so the difference is distinguishable and `one in four would notice` is a fact about PAPERS rather
  than about pinning.  82.8% of readable source keys survive at least one reversal against the paper
  half's 75.5%.  The instrument is r7228's own block, sliced from its pinned source and digest-gated,
  so the difference cannot be between two instruments; the faster byte locator is this receipt's and
  its equivalence to r7228's own classify is measured, identical on all eight shared buckets of a
  60-key sample.  Two filters the paper half did not need are declared: the pinning receipt's own
  file, which every source key's literal sits in by construction, and code-versus-prose, whose 218
  keys are a fifth of the half so the pre-registered third outcome did not fire.  AND THE LARGEST
  EXCLUSION IS AN ANSWER: of 469 ABSENT keys, 72 of a 120-key sample are found in the project's own
  registers or instrument modules, 56 in a register against 28 in a module -- so this half is mostly
  a receipt pinning a LEDGER and not another receipt's source, and the baseline's SOURCE label means
  only that the trace did not name a .tex.  Nothing is adjudicated and nothing outside this file is
  written.""")
if _bad:
    raise SystemExit(1)
