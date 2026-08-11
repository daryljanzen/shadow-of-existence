#!/usr/bin/env python3
"""audit_trail.py -- THE WAKE AUDITOR.  Compare two bundles of the working fork and report,
mechanically, what moved, what was added, what was dropped, and what was left behind.

    python3 scripts/audit_trail.py <older-tree> <newer-tree> [-o TRAIL_AUDIT_c54.NNN.md]

This is the instrument of the OBSERVER LINE (`ARC 15`, CONSOLIDATE §2).  The working fork runs
the live edge; this thread comes up behind it, audits the trail, absorbs the advances, and keeps
the programme coherent -- WITHOUT collaborating with it and without interrupting its pace.  Doing
that by hand once is a session; doing it every data point needs a machine, and comparability
across data points needs the SAME machine every time.

What it reports, in the order that matters:

  1. DROPPED   -- files present in the older tree and absent from the newer.  The first question,
                  because a drop is the one change that cannot be recovered from the newer tree.
  2. SHRANK    -- source files that lost bytes.  Not a verdict: a correct retirement shrinks a
                  file too.  It is a LOOK-SIGNAL, and each one is read.
  3. ADDED     -- new files, grouped by directory.
  4. TOUCHED / UNTOUCHED -- and the untouched list is the wake: every standing document the run
                  did not reach.
  5. STALENESS DELTA -- for each live document, how far behind it was then and is now.  A number
                  that GREW is a document the run left further behind than it found it.
  6. REGISTER DELTA -- leads struck, leads added, open count.
  7. PAPER FRONTIERS -- items that left each paper's sec:frontiers, since a frontier leaving a
                  list is a closure and closures are what the observer line watches hardest.

It renders no verdicts on the physics.  A wake report that graded the work would be the observer
crossing into the worker's seat, which is exactly what the prime directive forbids.

Written r2377.  Stated for reversal.
"""
import os, re, sys, hashlib, argparse

SRC_EXT = ('.md', '.tex', '.py', '.txt', '.sh', '.bib')
SKIP_EXT = ('.pdf', '.log', '.aux', '.out', '.toc', '.png', '.jpg', '.pkl', '.gz')

# ** r2384: THE DROPPED SECTION CRIED WOLF ON ITS FIRST REAL RUN, and the fix is here. **
#
# c54.134 -> c54.153 reported ** 58 DROPPED ** -- the loudest possible finding, in the section this
# report prints first and calls irrecoverable.  Read: all 58 were LaTeX build cruft (.aux/.log/.out),
# __pycache__ .pyc files, and two computation .log files.  ** Zero source content was dropped. **
#
# The cause is structural, not the fork's: `cut_bundle.sh` EXCLUDES build artefacts by design, and so
# do this line's own bundles.  So a correctly-cut bundle will ALWAYS appear to "drop" ~58 files, and
# the section that matters most would be noise on every single run -- which is the cry-wolf failure
# this whole audit has been repairing in other people's gates.
#
# Partitioned now: BUILD ARTEFACTS reported as a count and named only on request; SOURCE DROPS are
# the alarming category and are the only ones that can be irrecoverable.
BUILD_EXT = ('.aux', '.log', '.out', '.toc', '.bbl', '.blg', '.fls', '.fdb_latexmk',
             '.synctex.gz', '.pyc')


def is_build_artefact(rel):
    return rel.endswith(BUILD_EXT) or '__pycache__' in rel


def digest(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def tree(root):
    out = {}
    for dirpath, _, names in os.walk(root):
        for n in names:
            full = os.path.join(dirpath, n)
            out[os.path.relpath(full, root)] = full
    return out


def fork_rev(path):
    try:
        rs = [int(x) for x in re.findall(r'c54\.(\d+)',
              open(path, encoding='utf-8', errors='replace').read())]
    except OSError:
        return None
    return max(rs) if rs else None


def front(t):
    best = 0
    for rel, full in t.items():
        if rel.endswith('.md') and '/' not in rel:
            r = fork_rev(full)
            if r and r > best:
                best = r
    return best


def register(path):
    if not os.path.exists(path):
        return set(), set()
    s = open(path, encoding='utf-8', errors='replace').read()
    return (set(re.findall(r'\| \*\*(L-\d+)\*\* \|', s)),
            set(re.findall(r'\| ~~(L-\d+)~~ \|', s)))


def frontiers(path):
    if not os.path.exists(path):
        return []
    t = open(path, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\section\{[^}]*\}\\label\{sec:frontiers\}(.*?)'
                  r'(?=\\section|\\input|\\begin\{thebibliography\})', t, re.S)
    if not m:
        return []
    return re.findall(r'\\item(?:\\label\{[^}]*\})?\s*\\(?:emph|textbf)\{([^}]{0,95})', m.group(1))


# ** r2384: THE BASELINE MUST BE PRISTINE, AND THIS ALMOST WENT WRONG. **
#
# The tree used as the OLD side of an audit has to be the working fork's bundle as it arrived --
# not this line's working copy of it.  Checked before the next absorption: the c54.134 baseline on
# disk had SIX of this line's own instrument files copied into it during r2379 (five generators and
# ID_SPACE_CENSUS.md), from a one-off `cp` used to run the scripts against that tree.
#
# ** Diffing the next bundle against it would have reported those six as DROPPED BY THE FORK. **
# Drops are the first thing this report prints, and the one change that cannot be recovered from the
# newer tree -- so the falsest possible finding would have appeared at the top of the most trusted
# section.  Nothing was wrong with the fork's content; the contamination was entirely mine.
#
# So the audit now REFUSES a baseline carrying this line's instrument files, by name.  The fix is to
# re-extract the bundle rather than to reuse a working copy: a baseline is a record, and a record you
# have run scripts inside is no longer one.
OBSERVER_FILES = ['scripts/audit_trail.py', 'scripts/classify_documents.py',
                  'scripts/regen_teed_up.py', 'scripts/regen_burn_down.py',
                  'scripts/id_space_census.py', 'scripts/build_fork_span.py',
                  'scripts/regen_map_status.py', 'DOCUMENT_LEDGER.md', 'ID_SPACE_CENSUS.md',
                  'THE_STAGED_REVISIONS.md']


def baseline_is_pristine(root):
    found = [f for f in OBSERVER_FILES if os.path.exists(os.path.join(root, f))]
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('old'); ap.add_argument('new'); ap.add_argument('-o', default=None)
    a = ap.parse_args()
    contam = baseline_is_pristine(a.old)
    if contam and '--force' not in sys.argv:
        print(f'  [FAIL] the OLD tree is not a pristine bundle: it carries '
              f'{len(contam)} of this line\'s own file(s):')
        for c in contam:
            print(f'    {c}')
        print()
        print('  ** Diffing against it would report these as DROPPED BY THE FORK **, at the top of')
        print('     the one section whose findings cannot be recovered from the newer tree.')
        print('     Re-extract the bundle into a clean directory and point --old at that.')
        print('     (--force to override, which you should not need.)')
        return 1
    A, B = tree(a.old), tree(a.new)
    fa, fb = front(A), front(B)

    dropped_all = sorted(set(A) - set(B))
    dropped = [d for d in dropped_all if not is_build_artefact(d)]
    dropped_build = [d for d in dropped_all if is_build_artefact(d)]
    added = sorted(set(B) - set(A))
    changed, shrank, untouched = [], [], []
    for rel in sorted(set(A) & set(B)):
        if rel.endswith(SKIP_EXT):
            continue
        sa, sb = os.path.getsize(A[rel]), os.path.getsize(B[rel])
        if digest(A[rel]) != digest(B[rel]):
            changed.append((rel, sa, sb))
            if sb < sa:
                shrank.append((rel, sa, sb))
        elif rel.endswith('.md') and '/' not in rel:
            untouched.append(rel)

    o = []
    o.append('---')
    o.append('name: trail-audit')
    o.append('kind: RECORD')
    o.append(f'current: c54.{fb}')
    o.append(f'description: Mechanical audit of the working fork\'s trail, c54.{fa} → c54.{fb}. '
             f'Generated by scripts/audit_trail.py. Observation only — no verdict on the physics.')
    o.append('sources: [chat]')
    o.append('---')
    o.append('')
    o.append(f'# TRAIL AUDIT — c54.{fa} → c54.{fb}')
    o.append('')
    o.append(f'*Generated by `scripts/audit_trail.py`. **{fb - fa} revisions.** '
             f'{len(dropped)} dropped · {len(added)} added · {len(changed)} changed · '
             f'{len(untouched)} top-level documents untouched.*')
    o.append('')
    o.append('> **⌗ THE PRIME DIRECTIVE.** *This line observes; it does not collaborate. The working '
             'fork runs the live edge and its pace is the point. **This report renders no verdict on '
             'the physics** — a wake report that graded the work would be the observer crossing into '
             'the worker\'s seat. It reports what MOVED and what was LEFT, and nothing else.*')
    o.append('')

    o.append('## ① DROPPED — the one change that cannot be recovered from the newer tree')
    o.append('')
    if dropped:
        o.append(f'⛔ **{len(dropped)} SOURCE file(s) present at c54.{fa} and absent at c54.{fb}.** '
                 '*Each is read before anything else is done.*')
        o.append('')
        for d in dropped:
            o.append(f'- `{d}`')
    else:
        o.append('✔ **No source file was dropped.**')
    o.append('')
    if dropped_build:
        o.append(f'*⌗ Also absent: **{len(dropped_build)} build artefact(s)** — `.aux`/`.log`/`.out`, '
                 f'`__pycache__` and the like. **Not a finding**: `cut_bundle.sh` excludes build '
                 f'output by design, so a correctly-cut bundle always shows these. '
                 f'**They are counted and not listed, so they cannot drown the section above.***')
    o.append('')
    o.append('> **⌗ WHY THIS PARTITION EXISTS (r2384).** *The first real run of this report said '
             '**58 DROPPED** — the loudest possible finding, in the section printed first and called '
             'irrecoverable. **All 58 were build cruft and zero source content was lost.** A section '
             'that fires on every correctly-cut bundle is a section nobody reads, which is the '
             'cry-wolf failure this audit has spent its whole run repairing in other gates. '
             '**Fixed in the instrument, immediately, before the report was used.***')
    o.append('')

    o.append('## ② SHRANK — a look-signal, never a verdict')
    o.append('')
    o.append('*A correct retirement shrinks a file too. Each row is READ; the question is whether '
             'what left was recorded or merely cut.*')
    o.append('')
    if shrank:
        o.append('| file | was | now | delta |')
        o.append('|---|---|---|---|')
        for rel, sa, sb in sorted(shrank, key=lambda r: r[2] - r[1]):
            o.append(f'| `{rel}` | {sa:,} | {sb:,} | **{sb - sa:+,}** ({100.0 * (sb - sa) / sa:+.1f}%) |')
    else:
        o.append('**None.**')
    o.append('')

    o.append('## ③ ADDED')
    o.append('')
    bydir = {}
    for x in added:
        bydir.setdefault(os.path.dirname(x) or '(top level)', []).append(x)
    o.append('| directory | count |')
    o.append('|---|---|')
    for k in sorted(bydir):
        o.append(f'| `{k}` | {len(bydir[k])} |')
    o.append('')
    for k in sorted(bydir):
        if k == '(top level)':
            o.append(f'**New at top level:** ' + ', '.join(f'`{x}`' for x in bydir[k]))
            o.append('')

    o.append('## ④ THE WAKE — top-level documents the run did not reach')
    o.append('')
    o.append(f'**{len(untouched)} untouched** *(against {len([c for c in changed if "/" not in c[0] and c[0].endswith(".md")])} touched).*')
    o.append('')

    o.append('## ⑤ STALENESS DELTA — did the run leave a document further behind than it found it?')
    o.append('')
    o.append('| document | behind at c54.%d | behind at c54.%d | |' % (fa, fb))
    o.append('|---|---|---|---|')
    worse = 0
    for rel in sorted(set(A) & set(B)):
        if not (rel.endswith('.md') and '/' not in rel):
            continue
        ra, rb = fork_rev(A[rel]), fork_rev(B[rel])
        if ra is None or rb is None:
            continue
        la, lb = fa - ra, fb - rb
        if lb <= 6:
            continue
        mark = '**+%d**' % (lb - la) if lb > la else ('—' if lb == la else '%d' % (lb - la))
        if lb > la:
            worse += 1
        o.append(f'| `{rel}` | {la} | {lb} | {mark} |')
    o.append('')
    o.append(f'***{worse} document(s) ended the run further behind than they began it.*** '
             '*That is arithmetic, not blame: a fork advancing without touching a document leaves '
             'it behind by exactly the number of revisions it advanced.*')
    o.append('')

    la_, ls_ = register(os.path.join(a.old, 'THE_LIVE_ARC.md'))
    lb_, lsb = register(os.path.join(a.new, 'THE_LIVE_ARC.md'))
    o.append('## ⑥ REGISTER DELTA')
    o.append('')
    o.append('| | c54.%d | c54.%d |' % (fa, fb))
    o.append('|---|---|---|')
    o.append(f'| registered | {len(la_) + len(ls_)} | {len(lb_) + len(lsb)} |')
    o.append(f'| struck | {len(ls_)} | {len(lsb)} |')
    o.append(f'| open | {len(la_)} | {len(lb_)} |')
    o.append('')
    newly = sorted(lsb - ls_, key=lambda s: int(s[2:]))
    fresh = sorted((lb_ | lsb) - (la_ | ls_), key=lambda s: int(s[2:]))
    if newly:
        o.append(f'**Struck this span ({len(newly)}):** ' + ', '.join(f'`{x}`' for x in newly))
        o.append('')
    if fresh:
        o.append(f'**Newly registered ({len(fresh)}):** ' + ', '.join(f'`{x}`' for x in fresh))
        o.append('')

    o.append('## ⑦ PAPER FRONTIERS — items that left a published frontier list')
    o.append('')
    o.append('*A frontier leaving a list is a closure, and closures are what this line watches '
             'hardest. **The question is never whether the closure is right** — that is the '
             'worker\'s call — **but whether every document that carried the item knows.***')
    o.append('')
    any_move = False
    for tex in sorted(set(A) & set(B)):
        if not (tex.startswith('corpus/') and tex.endswith('.tex')):
            continue
        ia, ib = frontiers(A[tex]), frontiers(B[tex])
        if not ia and not ib:
            continue
        gone = [x for x in ia if x not in ib]
        new = [x for x in ib if x not in ia]
        if gone or new:
            any_move = True
            o.append(f'**`{tex}`** — {len(ia)} → {len(ib)} items')
            for g in gone:
                o.append(f'- **LEFT:** *{g}*')
            for n in new:
                o.append(f'- **NEW:** *{n}*')
            o.append('')
    if not any_move:
        o.append('*No frontier list changed.*')
        o.append('')

    o.append('---')
    o.append('')
    o.append('> **⌗ WHAT THIS REPORT DOES NOT DO.** *It does not judge the work, propose changes to '
             'the working fork, or route anything to it. **Findings go into this line\'s own '
             'register**, and reach the working fork only if the orchestrator carries them — the '
             'one exception being a catastrophe ahead of it, which is his call and not this '
             'script\'s.*')
    o.append('')

    out = a.o or os.path.join(a.new, f'TRAIL_AUDIT_c54.{fb}.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(o) + '\n')
    print(f'  wrote {out}')
    print(f'    c54.{fa} → c54.{fb}: {len(dropped)} dropped, {len(added)} added, '
          f'{len(changed)} changed, {len(untouched)} untouched, {worse} left further behind')
    return 0


if __name__ == '__main__':
    sys.exit(main())
