#!/usr/bin/env python3
"""check_marker_transposition.py -- A RECEIPT MARKER ON THE WRONG PARAGRAPH.

** THE ERROR THIS EXISTS FOR, AND IT HAPPENED TWICE IN ONE PASSAGE. **  `P10` `sec:lock`
was rewritten six times in nine revisions.  Twice, a receipt added to it was cited in the
wrong place:
  - `r7061` found the two-mode shift (200/63, 19/27) closing under a pair of receipts that
    compute none of it.  `r7008`, which computes all of it, was cited ninety lines later.
  - `r7065` found -4/3 closing under four receipts that compute none of it.  The regulator
    receipt was cited a hundred and fifty lines EARLIER, on the anchors paragraph.
The gate's own diagnosis (`r7067`): *when a revision adds a receipt to a passage it has
just rewritten, the marker goes where the edit was made rather than where the number is.*

** WHAT THIS CHECKS -- ONE SHAPE, NARROWER THAN A MIS-CITATION, WHICH IS WHAT MAKES IT CHEAP. **
It flags a TRANSPOSITION: a distinctive number in one `\\rcpt` group's claim that
  (a) NONE of that group's receipt sources carries, and
  (b) the source of a receipt cited in a DIFFERENT group within +-N lines does.
So the right receipt is in the paper, on the wrong paragraph.  The claim window is the text
since the previous marker group.  Distinctive numbers:
  - fractions, carried as p/q, Rational(p, q) or Fraction(p, q);
  - decimals of three or more significant digits, carried as literals;
  - integers of three or more digits that are not years.

** THE LIMITS, STATED BEFORE IT WAS BUILT. **
  - SOURCE ONLY: nothing is run, so a number that a receipt only prints at run time is
    invisible here.  The on-demand companion receipt covers that case.
  - Common small integers are excluded, so a transposition carried only by one is missed.
  - The +-N window is a choice.  It is set from the two known cases and printed on every run.

** CALIBRATION IS A CONDITION OF THE GATE PASSING. **  Every run re-finds both motivating
cases at their own commits, via `git show`.  A gate that cannot find the two errors that
made it is not a gate.

** THE BASELINE IS A RECORD OF ADJUDICATIONS, NOT A LIST OF EXEMPTIONS (`r7069`). **  Each
entry is a SITE -- paper, own group, number, carrier -- with what was read and the verdict.
Two things fail the gate:
  - a flag that is not in the baseline: NEW;
  - a baseline entry whose flag no longer fires: STALE, and it must be REMOVED.  A fixed
    site must not stay behind as a silent permission to regress.

Built r7069+70 (node 70), pre-registered at
computations/beyond_the_wall/r7069_70_transposition_gate/PREDICTION.md.
"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BASE = os.path.join(HERE, 'marker_transposition_baseline.tsv')
N_WINDOW = 200          # lines; set from the two calibration cases (printed below) with margin
RARITY = 12             # a number carried by more receipt sources than this is not distinctive; the
                        # calibration tokens are carried by at most 9 (printed below), so 12 keeps them

CALIBRATION = [
    # commit, paper, token, carrier short-name prefix, expected own-group member
    ('a3705946', 'canonical_time.tex', '200/63', 'P10_the_vertex_numbers_are_exact',
     'P10_the_same_level_sum_is_orthogonality'),
    ('a3705946', 'canonical_time.tex', '19/27', 'P10_the_vertex_numbers_are_exact',
     'P10_the_same_level_sum_is_orthogonality'),
    ('3f8fc14a', 'canonical_time.tex', '-4/3', 'P10_the_construction_own_regulator',
     'P10_the_cubic_normalisation_is_written_down'),
]


# ------------------------------------------------------------------ reading the paper
def strip(tex):
    """comments out (line count kept), bibliography dropped"""
    tex = '\n'.join(re.sub(r'(?<!\\)%.*$', '', ln) for ln in tex.split('\n'))
    return re.split(r'\\begin\{thebibliography\}', tex)[0]


GROUP = re.compile(r'\\rcpt\{[^}]*\}(?:[\s,;.~]*\\rcpt\{[^}]*\})*')


def groups(tex):
    """[(line, [receipt names], claim window, paragraph index)] in paper order"""
    out, prev = [], 0
    for m in GROUP.finditer(tex):
        names = re.findall(r'\\rcpt\{([^}]*)\}', m.group(0))
        para = len(re.findall(r'\n[ \t]*\n', tex[:m.start()]))
        out.append((tex.count('\n', 0, m.start()) + 1, names, tex[prev:m.start()], para))
        prev = m.end()
    return out


YEAR = re.compile(r'^(18|19|20)\d\d$')


def tokens(claim):
    """the distinctive numbers a claim states, as canonical strings"""
    s = re.sub(r'\\(?:ref|eqref|label|cite[a-z]*|rcpt|ldg|url|href)\{[^}]*\}', ' ', claim)
    s = re.sub(r'\\(?:,|;|!|:| )', '', s).replace('{,}', '')
    toks, spans = [], []

    def frac(m, p, q):
        neg = s[max(0, m.start() - 1):m.start()] in ('-', '−') or \
            s[max(0, m.start() - 2):m.start()].strip() in ('-', '−')
        toks.append(('-' if neg else '') + f'{int(p)}/{int(q)}')
        spans.append((m.start(), m.end()))

    for m in re.finditer(r'\\[dt]?frac\{(\d+)\}\{(\d+)\}', s):
        frac(m, m.group(1), m.group(2))
    for m in re.finditer(r'\\[dt]?frac(\d)(\d)(?!\d)', s):
        frac(m, m.group(1), m.group(2))
    for m in re.finditer(r'(?<![\d.\w/])(\d+)/(\d+)(?![\d/])', s):
        if not any(a <= m.start() < b for a, b in spans):
            frac(m, m.group(1), m.group(2))
    for m in re.finditer(r'(?<![\d.\w])(\d+\.\d+)(?![\d.])', s):
        if not any(a <= m.start() < b for a, b in spans) and len(m.group(1).replace('.', '').lstrip('0')) >= 3:
            toks.append(m.group(1))
            spans.append((m.start(), m.end()))
    for m in re.finditer(r'(?<![\d.\w/{])(\d{3,})(?![\d./}])', s):
        if not any(a <= m.start() < b for a, b in spans) and not YEAR.match(m.group(1)):
            toks.append(m.group(1))
    return sorted(set(toks))


def unquoted(src):
    """a receipt's source without the lines that QUOTE a paper: a pin carries the paper's number
    as text and computes nothing, so it cannot be the receipt a number was transposed from"""
    return '\n'.join(l for l in src.split('\n') if '$' not in l and 'TEX' not in l and '\\\\' not in l)


def carries(src, tok):
    if '/' in tok:
        neg = tok.startswith('-')
        p, q = tok.lstrip('-').split('/')
        sign = r'-\s*' if neg else r'(?:-\s*)?'
        return bool(re.search(rf'(?<![\d.]){sign}{p}\s*/\s*{q}(?![\d])', src) or
                    re.search(rf'(?:Rational|Fraction|F)\(\s*{sign}{p}\s*,\s*{sign if neg else ""}{q}\s*\)', src))
    return bool(re.search(rf'(?<![\d.]){re.escape(tok)}(?![\d])', src))


# ------------------------------------------------------------------ the check
def flags(tex, source_of, rare):
    """[(own-group key, token, carrier, own line, carrier line)] for one paper"""
    gs = groups(strip(tex))
    out = []
    for i, (ln, names, claim, para) in enumerate(gs):
        own = [source_of(n) for n in names]
        own = [s for s in own if s is not None]
        if not own:
            continue
        for tok in tokens(claim):
            if any(carries(s, tok) for s in own):
                continue
            for j, (ln2, names2, _, para2) in enumerate(gs):
                # the same paragraph cites the carrier, so nothing is transposed: only a receipt cited in
                # ANOTHER paragraph is a candidate -- both calibration cases cross paragraphs
                if j == i or abs(ln2 - ln) > N_WINDOW or para2 == para:
                    continue
                for n2 in names2:
                    if n2 in names:
                        continue
                    s2 = source_of(n2)
                    if s2 is not None and carries(unquoted(s2), tok) and rare(tok):
                        out.append(('+'.join(sorted(names)), tok, n2, ln, ln2))
    return out


def live_sources():
    idx = {}
    for d in ('storyboard_receipts', 'receipts'):          # receipts/ wins a name clash
        for p in glob.glob(os.path.join(ROOT, d, '**', '*.py'), recursive=True):
            idx[os.path.basename(p)[:-3]] = p
    cache = {}

    def source_of(name):
        if name not in cache:
            p = idx.get(name)
            cache[name] = open(p, encoding='utf-8', errors='replace').read() if p else None
        return cache[name]
    return source_of


def rarity_counter():
    """how many receipt sources (quotations excluded) carry a token, at the live tree"""
    srcs = [unquoted(open(p, encoding='utf-8', errors='replace').read())
            for d in ('receipts', 'storyboard_receipts')
            for p in glob.glob(os.path.join(ROOT, d, '**', '*.py'), recursive=True)]
    cache = {}

    def df(tok):
        if tok not in cache:
            cache[tok] = sum(1 for s in srcs if carries(s, tok))
        return cache[tok]
    return df


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True).stdout


def historic_sources(commit):
    idx = {}
    for d in ('storyboard_receipts', 'receipts'):
        for p in git('ls-tree', '-r', '--name-only', commit, d).split('\n'):
            if p.endswith('.py'):
                idx[os.path.basename(p)[:-3]] = p
    cache = {}

    def source_of(name):
        if name not in cache:
            p = idx.get(name)
            cache[name] = git('show', f'{commit}:{p}') if p else None
        return cache[name]
    return source_of


def baseline():
    if not os.path.exists(BASE):
        return None
    out = {}
    for l in open(BASE, encoding='utf-8'):
        if not l.strip() or l.startswith('#'):
            continue
        f = l.rstrip('\n').split('\t')
        out[tuple(f[:4])] = f[4:]
    return out


def main():
    listing = '--list' in sys.argv
    print()
    print('  MARKER TRANSPOSITION -- is each number cited where it is computed?')
    print(f'    window: +-{N_WINDOW} lines')
    print()
    ok = True

    # ---- calibration, at the two motivating commits
    have_history = bool(git('cat-file', '-t', 'a3705946').strip())
    if not have_history:
        print('  [FAIL] the calibration commits are not in this clone -- a gate that cannot re-find the')
        print('         two errors that made it does not pass.  (CI checks out with fetch-depth 0.)')
        return 1
    dist = []
    df = rarity_counter()
    rare = lambda t: df(t) <= RARITY
    print(f'    rarity: a number carried by more than {RARITY} receipt sources is not distinctive; the '
          f'calibration numbers are carried by {sorted(df(c[2]) for c in CALIBRATION)}')
    for commit, paper, tok, carrier, member in CALIBRATION:
        tex = git('show', f'{commit}:corpus/{paper}')
        fl = flags(tex, historic_sources(commit), rare)
        hit = [f for f in fl if f[1] == tok and f[2].startswith(carrier) and member in f[0]]
        if hit:
            dist.append(abs(hit[0][3] - hit[0][4]))
            print(f'    [ok]   calibration {commit} {paper}: {tok} re-found -- own group lacks it, '
                  f'{carrier[:34]}... carries it {abs(hit[0][3]-hit[0][4])} lines away')
        else:
            ok = False
            print(f'    [FAIL] calibration {commit} {paper}: {tok} NOT re-found')
    if dist:
        print(f'    calibration distances {sorted(dist)}; window {N_WINDOW} (the largest plus a margin)')
    print()

    # ---- current corpus
    src = live_sources()
    found = {}
    for p in sorted(glob.glob(os.path.join(HERE, '*.tex'))):
        paper = os.path.basename(p)
        if paper.startswith('appendix_'):
            continue
        for key, tok, carrier, ln, ln2 in flags(open(p, encoding='utf-8').read(), src, rare):
            found.setdefault((paper, key, tok, carrier), (ln, ln2))
    if listing:
        for (paper, key, tok, carrier), (ln, ln2) in sorted(found.items()):
            print(f'{paper}\t{key}\t{tok}\t{carrier}\t<verdict>\t<read>\t# own at {ln}, carrier at {ln2}')
        return 0
    base = baseline()
    if base is None:
        print(f'  [FAIL] {os.path.relpath(BASE, ROOT)} is absent; the baseline is data and must exist')
        return 1
    new = sorted(k for k in found if k not in base)
    stale = sorted(k for k in base if k not in found)
    print(f'    {len(found)} flag(s) at current main; {len(base)} adjudicated in the baseline')
    held = {}
    for k in base:
        if k in found:
            v = base[k][0].split(' -- ')[0] if base[k][0].startswith('TRANS') else base[k][0]
            held[v] = held.get(v, 0) + 1
    for v, c in sorted(held.items(), key=lambda x: -x[1]):
        print(f'    [held] {c:3d}  {v}')
    if new:
        ok = False
        print()
        print(f'  ⛔ {len(new)} NEW TRANSPOSITION FLAG(S):')
        for paper, key, tok, carrier in new:
            ln, ln2 = found[(paper, key, tok, carrier)]
            print(f'    [FAIL] {paper}:{ln}  {tok} -- none of the group closing it carries it; '
                  f'{carrier} (cited at line {ln2}) does')
        print('     ⌗ Put the marker beside the number it computes, or -- if this is not a')
        print('       transposition -- adjudicate it in the baseline with what was read and why.')
    if stale:
        ok = False
        print()
        print(f'  ⛔ {len(stale)} STALE BASELINE ENTR(Y/IES) -- the flag no longer fires, so REMOVE the entry:')
        for k in stale:
            print(f'    [FAIL] {k[0]}: {k[2]} carried by {k[3][:60]}')
        print('     ⌗ A fixed site left in the baseline is a silent permission to regress there (r7069).')
    print()
    if ok:
        print('  no new transposition, no stale adjudication, and both calibration cases re-found.')
        print()
        return 0
    return 1


if __name__ == '__main__':
    sys.exit(main())
