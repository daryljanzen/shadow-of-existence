#!/usr/bin/env python3
"""r7141+cc66.107 -- PARTITION THE PROSE-PIN BACKLOG BY WHAT THE COUNTED TEXT *IS*.

`r7139` found that `P15_CR_cosmology`'s pins are on an instrument's own SOURCE, where an exact count
is the correct form, while `L204`'s and `L221`'s are on PAPER PROSE, where a round count is a defect.
** So the discriminant is the text, not the family. **  This measures it over the whole remaining
backlog, before any of it is read -- which is what makes the backlog's real size reportable in
advance rather than after.

** METHOD, and its two halves are kept apart on purpose. **
  (1) TRACED.  For each unadjudicated `(receipt, expression)` the counted variable is resolved
      through the receipt's own bindings -- transitively, with multi-line bindings joined until the
      brackets balance, because the paper-join idiom spans lines -- until a read site names what was
      read: `*.tex` / `papers()` (PAPER), `*.py` / `rcpt(` / `__file__` (SOURCE), or `*.md` /
      `CORPUS_MAP` / a register (REGISTER).
  (2) HAND.  What tracing cannot reach is read by hand and recorded BELOW, one line each with its
      reason, so the two halves are never mixed in the counts.  ⌗ *A partition where the hand share
      is invisible is a partition nobody can check.*

⚑ ** AND THE PARTITION IS NOT TWO-WAY. **  Two buckets the order's `PAPER`-against-`SOURCE` framing
  does not have turned up and are reported rather than folded in:
  * REGISTER -- counts over the corpus's own governance files (`CORPUS_MAP`, `PROTECTED_OPEN`, the
    registers).  Neither paper prose nor instrument source, and its own question.
  * NOT-A-COUNT -- ** no text is read at all **:  `P10`'s `mr` is a dict of COMPUTED ratios, so
    `len(mr) == 6` counts dict entries, and `P14`'s `COEFF` is a coefficient table.  *Same class the
    `r7139` pass verdicted 4 of, and the `B41` precedent before it.*

Run from the repository root:  python3 computations/beyond_the_wall/r7141_cc66_paper_source_partition/partition.py
"""
import collections
import re
import sys

BASELINE = 'corpus/prose_pin_baseline.tsv'
NAME = re.compile(r'[A-Za-z_]\w*')
KW = {'len', 'sum', 're', 'findall', 'finditer', 'search', 'count', 'set', 'sorted', 'min', 'max',
      'all', 'any', 'int', 'float', 'str', 'list', 'dict', 'abs', 'round', 'check', 'gate', 'get',
      'most_common', 'values', 'keys', 'items', 'in', 'and', 'or', 'not', 'is', 'None', 'True',
      'False', 'open', 'print', 'range', 'enumerate', 'zip', 'tuple', 'encoding', 'errors',
      'replace', 'read', 'f', 'utf'}
PAPER = re.compile(r"\.tex\b|corpus/\*|papers\(\)|_p15_at|paper_body|_tex\(|appendix_receipts"
                   r"|BODIES|_BODY\b", re.I)
SOURCE = re.compile(r"\.py\b|__file__|rcpt\(|HIER_|two_arm|scripts/")
REG = re.compile(r"\.md\b|CORPUS_MAP|PO13|THE_DISPATCH|THE_LINE|CLAIMS|INDEX\.md|FOR_\d|FOR_CC"
                 r"|THE_STAGED|REGISTER|PROTECTED_OPEN", re.I)

#: what tracing could not reach, read by hand, with the reason.  Keyed on the expression, which is
#: unique within its receipt.
HAND = {
    'len(inc) <= 1':
        ('PAPER', r"`inc = re.findall(r'\\(?:input|include)\{...}')` -- LaTeX include directives, "
                  "so the text is a paper"),
    'tot == 86':
        ('PAPER', "built by `sweep(...)`, whose per-file tally is keyed on paper names -- the same "
                  "check reads `_by_file.get('CR_synthesis.tex')`"),
    'len(n23) == 19': ('PAPER', "the same `sweep(...)` over paper files"),
    'len(n123) == 5': ('PAPER', "the same `sweep(...)` over paper files"),
    'n_before > 0':
        ('SOURCE', r"`n_before = len(re.findall(r'\bcheck\(', old_src))` -- counts `check(` calls "
                   "in a receipt's own source at an earlier blob"),
    '_live_reads == 2':
        ('SOURCE', "`m1_new.count(\"open(os.path.join(ROOT, 'PROTECTED_OPEN.md')\")` -- counts a "
                   "LINE OF CODE in another receipt's source. ⌗ The string names a register, but "
                   "what is counted is the source that reads it"),
    'n_cmp >= 4':
        ('SOURCE', r"`len(re.findall(r'^ok\d\w* = ', src, re.M))` -- counts assignments in source"),
    "sum(where['branch point'].values()) > 250":
        ('PAPER', "`where[t] = {p: len(re.findall(t, b)) for p, b in B.items()}` with "
                  "`B = RB.BODIES_TEX`"),
    "len(where['branch point']) >= 15": ('PAPER', "the same `BODIES_TEX` sweep"),
    'n_cr > 10': ('PAPER', "`len(re.findall('causal reassignment', p7f))`, `p7f` being P07's body"),
    'prox < 60': ('PAPER', "accumulated over `body(f)` across the paper files"),
    'sum(len(v) for v in lost.values()) <= 12':
        ('REGISTER', "`lost` is the register rows a merge dropped -- governance files, not prose"),
    'check("cosmic variance occurs twenty-five times (24 before r6391), and the one in P15 is '
    'the FIRST", cosmic, 25)':
        ('PAPER', "`sum(len(re.findall(r'cosmic[- ]variance', t)) for t in BODIES.values())`"),
    'len(mr) == 6':
        ('NOT-A-COUNT', "`mr = {int(m): int(m) * float(Fraction(int(a), int(b)))}` is a dict of "
                        "COMPUTED ratios, so this counts dict entries, not matches in text"),
    'max(mr[m] for m in mr if m >= 5) / min(mr.values()) < 1.25':
        ('NOT-A-COUNT', "arithmetic over that computed dict"),
    'mr[3] / min(mr.values()) > 2': ('NOT-A-COUNT', "arithmetic over that computed dict"),
    'prior_body.count(\'no spacetime bundle\') >= 1':
        ('PAPER', "`prior_body` is a paper body read at an earlier blob"),
    '_ps_p15 > 0':
        ('PAPER', r"`len(re.findall(r'peak spacing', P15_BODY, re.I))`"),
    'check("the harness detects a gap of 0.010", gap, 0.010)':
        ('NOT-A-COUNT', "`gap = round(abs(n1[0] - n2[0]), 3)` -- a float difference between two "
                        "numeric readings, in the three-argument `check(label, got, want)` form. "
                        "No text is read at all"),
    "_d['principal congruence'] > 1200":
        ('PAPER', "`_d = {q: _near(q, 'Carter constant') ...}` over `range_paper.tex` and "
                  "`CR_framework.tex`. ⚑ A CHARACTER DISTANCE in a paper, not a tally -- so the "
                  "TEXT is paper and the verdict will likely be NOT-A-COUNT. The partition "
                  "classifies the text; NOT-A-COUNT here is reserved for sites that read no text"),
    "max(v for k, v in _d.items() if k != 'principal congruence') < 1200":
        ('PAPER', "the same `_near` distance map over the same two papers"),
}
#: prefix-matched, for the sites whose recorded expression is a whole `check(...)`/`COEFF[...]` line
HAND_PREFIX = [
    ('check("the control word is FOUND', 'PAPER', "the same paper-body sweep as its sibling"),
    ('check("x18 in all', 'PAPER', "`sum(w.values())`, `w` built from paper bodies"),
    ('check("P14 carries ten of them', 'PAPER', "`w.get('P14')` over the same paper tally"),
    ('check("x8 in all now', 'PAPER', "`sum(h.values())` over the same paper tally"),
    ('COEFF[', 'NOT-A-COUNT', "`COEFF` is a coefficient table of computed numbers, not a text tally"),
    ('check("cosmic variance occurs', 'PAPER', "paper-body sweep over `BODIES`"),
]


def logical_lines(src):
    """source lines joined until the brackets balance: the paper-join idiom spans lines"""
    out, buf, depth = [], '', 0
    for raw in src.split('\n'):
        buf = (buf + ' ' + raw.strip()) if buf else raw
        depth += (raw.count('(') + raw.count('[') + raw.count('{')
                  - raw.count(')') - raw.count(']') - raw.count('}'))
        if depth <= 0 and not buf.rstrip().endswith('\\'):
            out.append(buf)
            buf, depth = '', 0
    if buf:
        out.append(buf)
    return out


def bindings(src):
    d = collections.defaultdict(list)
    for line in logical_lines(src):
        m = re.match(r'^[ \t]*([A-Za-z_]\w*)\s*(?::[^=\n]+)?=\s*(.+)$', line)
        if m and not m.group(2).startswith('='):
            d[m.group(1)].append(m.group(2))
        m = re.match(r'^[ \t]*for\s+([A-Za-z_,\s]+?)\s+in\s+(.+?):', line)
        if m:
            for n in m.group(1).split(','):
                d[n.strip()].append(m.group(2))
    for m in re.finditer(r'^[ \t]*def\s+([A-Za-z_]\w*)\s*\([^)]*\)\s*:\n((?:(?:[ \t]+.*)?\n)+)',
                         src, re.M):
        d[m.group(1)].append(m.group(2))
    return d


def trace(expr, binds, depth=0, seen=None):
    seen = seen if seen is not None else set()
    if depth > 8:
        return None
    for pat, tag in ((PAPER, 'PAPER'), (SOURCE, 'SOURCE'), (REG, 'REGISTER')):
        if pat.search(expr):
            return tag
    for n in sorted(set(NAME.findall(expr)) - KW):
        if n in seen:
            continue
        seen.add(n)
        for b in binds.get(n, []):
            got = trace(b, binds, depth + 1, seen)
            if got:
                return got
    return None


def hand(expr):
    if expr in HAND:
        return HAND[expr]
    for pre, tag, why in HAND_PREFIX:
        if expr.startswith(pre):
            return tag, why
    return None, None


def main():
    rows = [l.rstrip('\n').split('\t') for l in open(BASELINE)
            if l.strip() and not l.startswith('#')]
    unread = [r for r in rows if '/' in r[0] and r[3] == 'UNADJUDICATED']
    cache, out, how = {}, [], collections.Counter()
    for rec, expr in ((r[0], r[1]) for r in unread):
        if rec not in cache:
            try:
                cache[rec] = bindings(open(rec, encoding='utf-8', errors='replace').read())
            except OSError:
                cache[rec] = {}
        tag = trace(expr, cache[rec])
        if tag:
            how['traced'] += 1
            out.append((tag, rec, expr, 'traced'))
            continue
        tag, why = hand(expr)
        if tag:
            how['hand-read'] += 1
            out.append((tag, rec, expr, f'hand: {why}'))
        else:
            how['UNRESOLVED'] += 1
            out.append(('UNRESOLVED', rec, expr, 'neither traced nor hand-read'))
    cnt = collections.Counter(t for t, _r, _e, _w in out)
    print()
    print('  PROSE-PIN BACKLOG, PARTITIONED BY WHAT THE COUNTED TEXT IS')
    print()
    print(f'    unadjudicated sites: {len(unread)}')
    for k in ('PAPER', 'SOURCE', 'REGISTER', 'NOT-A-COUNT', 'UNRESOLVED'):
        if cnt[k]:
            print(f'       {cnt[k]:3d}  {k}')
    print(f'\n    decided by: {dict(how)}')
    print()
    fam = collections.defaultdict(collections.Counter)
    for t, rec, _e, _w in out:
        fam[rec.split('/')[1]][t] += 1
    print('    by family (PAPER / SOURCE / REGISTER / NOT-A-COUNT):')
    for f in sorted(fam, key=lambda x: -sum(fam[x].values())):
        c = fam[f]
        print(f'       {sum(c.values()):3d}  {f:34s} '
              f'{c["PAPER"]}/{c["SOURCE"]}/{c["REGISTER"]}/{c["NOT-A-COUNT"]}')
    print()
    print('  ⌗ THE HAND SHARE, kept visible so the partition can be checked:')
    for t, rec, expr, why in out:
        if why.startswith('hand:'):
            print(f'       {t:12s} {rec.split("/")[-1][:40]:40s} {expr[:40]}')
            print(f'                    {why}')
    bad = cnt['UNRESOLVED']
    if bad:
        print(f'\n  ⛔ {bad} site(s) neither traced nor hand-read -- the partition is INCOMPLETE.')
        for t, rec, expr, _w in out:
            if t == 'UNRESOLVED':
                print(f'       {rec.split("/")[-1][:44]:44s} {expr[:44]}')
        return 1
    print()
    print(f'  ⇒ THE PAPER COUNT IS THE BACKLOG\'S REAL SIZE FOR THIS CLASS: {cnt["PAPER"]}, not '
          f'{len(unread)}.')
    print('    `SOURCE` is where `r7139` measured exactness to be load-bearing, `REGISTER` is a')
    print('    separate question over governance files, and `NOT-A-COUNT` is the instrument\'s own')
    print('    false-positive class.  ** None of those three is repair owed on paper prose. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
