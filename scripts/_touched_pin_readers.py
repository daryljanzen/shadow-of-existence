#!/usr/bin/env python3
"""_touched_pin_readers.py -- the receipts whose PINNED SENTENCES this tree touched in corpus/.

Helper for `run_touched_readers.sh`.  ** The affected set for a paper edit is not every receipt that
names the file -- that is 103 of 956 and does not finish before a push. **  It is every receipt with a
pinned literal in an ADDED or REMOVED line, which `corpus/quote_pin_baseline.tsv` already keys as (receipt, literal).

Prints one receipt path per line.  No argument reads the working tree (staged and unstaged); one
argument diffs against that ref.
"""
import io
import os
import re
import subprocess
import sys

MIN = 8          # a literal shorter than this matches too much to mean anything

# ⌗ THE STATED LIMIT, so it is not a silent gap: this reads `git diff`, which does not see UNTRACKED
#   files.  *That is outside the class rather than a hole in it -- a receipt cannot have pinned prose
#   from a corpus file that did not exist when the receipt was written.*  ⛔ What IS outside and is a
#   real limit: a receipt that reads a paper WITHOUT a pinned literal in the quote-pin baseline, since
#   this scope is that baseline's keys -- CLOSED at `r7151` by the third half below, which computes the
#   same test from the receipt source and needs no adjudication.  The heavy job remains the suite's
#   verdict.


def touched_lines(ref):
    """every line this tree ADDED or REMOVED under corpus/.

    ⛭ BOTH DIRECTIONS, AND THAT IS THE `r7141` LESSON RATHER THAN A PRECAUTION.  A first draft took
    REMOVED lines only, on the reading that the class is `a receipt quoting prose the gate rewrote`.
    ** But the `r7141` break was the opposite: the gate ADDED a citation, which made both arms of an
    exclusive disjunction true. **  Nothing was removed that the receipt depended on.  ⇒ *An addition
    can satisfy an arm exactly as a removal can break one, so the affected set is both.*
    ⌗ *It found the right receipt on removed lines alone only because the edit replaced the line it
    changed -- which is luck, and luck is not a scope.*
    """
    out = []
    cmds = [['git', 'diff', '-U0'] + ([ref] if ref else []) + ['--', 'corpus/']]
    if not ref:
        cmds.append(['git', 'diff', '-U0', '--cached', '--', 'corpus/'])
    for cmd in cmds:
        for ln in subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines():
            if ln[:1] in ('-', '+') and not ln.startswith('---') and not ln.startswith('+++'):
                out.append(ln[1:])
    return '\n'.join(out)


def changed_files(ref):
    cmds = [['git', 'diff', '--name-only'] + ([ref] if ref else []) + ['--', 'corpus/']]
    if not ref:
        cmds.append(['git', 'diff', '--cached', '--name-only', '--', 'corpus/'])
    out = []
    for cmd in cmds:
        out += [l for l in subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines() if l]
    return sorted(set(out))


# ⛭⛭⛭ r7163 (66) ON NODE 70's r7161+70.2 SEED: THE FOURTH MEMBER OF THE BLINDNESS SHAPE, AND THE
#   FIRST FOUND BY A PLANTED SEED RATHER THAN BY A BREAK ON `main`.
#   ** Every selector in this file requires a receipt to NAME the changed file.  A receipt that reads its
#   paper through `reach_baseline` names none -- it imports a module whose `bodies()` globs every
#   `corpus/*.tex` -- so it was invisible to this gate ALWAYS, not merely in a window. **
#   ⌈ Standing size: `13` registered importers, measured on the tree at r7163 and CORRECTED FROM THE `21`
#   this comment first carried.  70 recovered the command behind the `21` at r7163+70.1: it counted sources
#   matching the READ partition's `\breach_baseline\b|BODIES(_TEX)?\s*\[`, which matches any MENTION of
#   the module or a subscript of a `BODIES` table -- `22`, of which `21` have a trace recording a `.tex`
#   read.  ** So a mention count was labelled an import count, and the lesson is 70's own: a census figure
#   has to carry the predicate that produced it. **  (`18` is the same regex without the `BODIES[` half,
#   which is why a reconstruction from imports could not reach either number.)
#   ⇒ *An importer reads every paper, so for ANY paper change it counted as naming the changed one.*
#   ⛔ AND THAT IS THE PART THAT WAS WRONG, measured by 70 at r7163+70.1 and corrected below: it is a
#   widening with a false-positive CLASS, not merely a generous one.  Replayed over `main`'s last 30
#   paper-touching commits, it over-selects `9` importers on every commit that changed only the GENERATED
#   `appendix_receipts_*.tex` -- their traces show `bodies()` opens the 17 papers and no appendix.
#   ⇒ *** A receipt that reads every paper does not read every `.tex`, and the predicate below asks what
#       each one was SEEN to open instead of what its import implies. ***
#   ⌈ Proved in 70's throwaway worktree before it was routed here: with it the seed's `S2` goes IN and
#   `S1`, `S3`, `S4` are unchanged.
_RB_IMPORT = re.compile(r'^\s*(?:import reach_baseline|from reach_baseline )', re.M)


def _names_the_change(src, names):
    """Does this receipt read a changed corpus file -- by name, or by importing the reader that globs them?"""
    if any(nm in src for nm in names):
        return True
    return bool(any(nm.endswith('.tex') for nm in names) and _RB_IMPORT.search(src))


# ⛭ r7163+70.1 PROPOSAL (node 70) -- NOT A NAME TEST.  "Does this receipt read this file" answered by what it
#   was SEEN to open, widened by what its source CAN open:
#   ⓐ the trace: `receipts/READ_INDEX.json` records the file among the receipt's opened paths (`r`), or under a
#      directory it read whole (`d`) when it opened a file of that kind at all (a `d` over corpus/*.py gates
#      is not a paper read);
#   ⓑ the source, by the conventions r7163+70.1's census found: it names the file; imports `reach_baseline`
#      or loads it by path; globs / lists / walks `corpus/` itself; builds the path from the stem; or imports
#      -- transitively, inside the repo -- or runs as a python child, a module that does any of these.
#   ⓐ decides for a receipt traced at its current blob (plus a python child, which no trace sees); ⓑ decides
#   for a receipt the trace has not met at this blob.  ⓐ is what sees a path built from DATA, which no source
#   scan can; ⓑ is what sees a receipt landed since the trace, which no trace can.
_GLOBWALK = re.compile(r"(glob\.glob|glob\(|iglob|os\.listdir|os\.walk|scandir|\.rglob\(|\.iterdir\()")
_CORPUS_DIR = re.compile(r"""['"]corpus['"/]|corpus/|\bCORPUS\b""")
_RB_PATH = re.compile(r"reach_baseline\.py['\"]")
_IMPORTS = re.compile(r'^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))', re.M)
_CHILD = re.compile(r"""['"]([\w./-]+\.py)['"]""")
_READ_INDEX = None
_SRC = {}


def _src(p):
    if p not in _SRC:
        try:
            _SRC[p] = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            _SRC[p] = ''
    return _SRC[p]


def _index():
    global _READ_INDEX
    if _READ_INDEX is None:
        import json
        try:
            _READ_INDEX = json.load(io.open(os.path.join('receipts', 'READ_INDEX.json'), encoding='utf-8'))['receipts']
        except (OSError, ValueError, KeyError):
            _READ_INDEX = {}
    return _READ_INDEX


def _module(name, here):
    for d in (here, 'corpus', 'scripts', '.'):
        p = os.path.join(d, name.replace('.', '/') + '.py')
        if os.path.exists(p):
            return p
    return None


def _globs_corpus(s):
    L = s.splitlines()
    for i, ln in enumerate(L):
        win = '\n'.join(L[max(0, i - 1):i + 3])
        # a glob near the corpus DIRECTORY, or a glob for papers by their extension wherever it is rooted (a helper
        # living in corpus/ globs its own `dirname(__file__)` and never writes the word)
        if _GLOBWALK.search(ln) and not ln.lstrip().startswith('#') and (_CORPUS_DIR.search(win) or '*.tex' in win):
            return True
    return False


def _src_reaches(p, names, seen):
    if p in seen or len(seen) > 40:
        return False
    seen.add(p)
    s = _src(p)
    if any(nm in s for nm in names):
        return True
    tex = any(nm.endswith('.tex') for nm in names)
    if tex and (_RB_IMPORT.search(s) or _RB_PATH.search(s) or _globs_corpus(s)
                or any(re.search(r"['\"]" + re.escape(nm[:-4]) + r"['\"]", s) for nm in names if nm.endswith('.tex'))):
        return True
    here = os.path.dirname(p)
    for a, b in _IMPORTS.findall(s):
        q = _module(a or b, here)
        if q and _src_reaches(q, names, seen):
            return True
    if 'subprocess' in s:
        for sc in _CHILD.findall(s):
            q = next((c for c in (sc, os.path.join(here, sc)) if os.path.exists(c)), None)
            if q and q != p and _src_reaches(q, names, seen):
                return True
    return False


def _blob(p):
    import hashlib
    try:
        b = io.open(p, 'rb').read()
    except OSError:
        return ''
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def _child_reaches(p, names):
    s = _src(p)
    if 'subprocess' not in s:
        return False
    here = os.path.dirname(p)
    for sc in _CHILD.findall(s):
        q = next((c for c in (sc, os.path.join(here, sc)) if os.path.exists(c)), None)
        if q and q != p and _src_reaches(q, names, set()):
            return True
    return False


def _reads_the_change(path, src, names):
    """ⓐ for a receipt the trace has met UNCHANGED, the trace decides -- it saw which files were opened, so a glob
    that filters out the appendices is not widened back over them -- plus the one read a trace cannot see, a
    python child.  ⓑ for a receipt the trace has not met, or met at another blob, the source decides."""
    import fnmatch
    e = _index().get(path)
    if e and _blob(path).startswith(e.get('sha', '-')):
        if any(nm in src for nm in names):
            return True
        changed = [f for f in _changed_paths if os.path.basename(f) in names]
        r = e.get('r', [])
        if any(f in r for f in changed):
            return True
        for f in changed:
            kind = os.path.splitext(f)[1]
            if any(fnmatch.fnmatchcase(f, d) for d in e.get('d', [])) and any(
                    x.startswith('corpus/') and x.endswith(kind) for x in r):
                return True
        return _child_reaches(path, names)
    return _src_reaches(path, names, set())


_changed_paths = []

# ⛭⛭⛭ r7164 (66): NODE 70's `r7163+70.1` PREDICATE IS ADOPTED AS WRITTEN, AND IT REPLACES THIS GATE'S
#   r7163 WIDENING RATHER THAN SITTING BESIDE IT.  The selector is this seat's, so the call is this
#   seat's; what makes it an easy one is that the measurement condemns this seat's own patch.
#   ** WHAT 70 MEASURED, with five of eleven pre-registered predictions MISSED and every miss reported:
#   there are SIX ways a receipt reaches a paper and the gate saw one and a half. **  Of ten seeds planted
#   one per convention, `run_touched_readers` with the r7163 patch in missed `8 of 8` non-literal ones --
#   a glob over `corpus/*.tex`, an `os.listdir`, `reach_baseline` loaded by path through `importlib`, a
#   helper module in `corpus/` globbing its own directory, a sibling import, a python child, and a path
#   built as `PAPER + '.tex'`.  `receipt_scope --scope suite` missed `9 of 10`, the import control
#   included.  The trace saw `9 of 10`, missing only the child process.
#     ⇒ *** NO STATIC PREDICATE IS COMPLETE AND NO TRACE IS COMPLETE EITHER, so the predicate is both: a
#         path built from DATA is invisible to every source scan and the trace sees it; a read through a
#         python child is invisible to the trace and the source sees it; and a receipt that landed after
#         the trace was taken -- 105 of them, plus 75 edited since -- is invisible to the trace alone. ***
#   ** THE COST AND THE GAIN, replayed commit by commit rather than argued. **  Over `main`'s last 30
#   first-parent commits touching `corpus/*.tex`, each checked out and both selectors run against its
#   parent: `1,919` receipts run against today's `1,470`.  `507` added, of which `338` the trace confirms
#   opened a file that commit changed -- ** 11.3 true readers per commit that today's gate never asks **,
#   across about 90 distinct receipts, mostly the `L204`, `L221`, `L165` and `P15/C*` glob readers.  `58`
#   dropped, and all 58 are correct: they are this seat's over-selected importers on appendix-only commits.
#   The price is `16.9` more receipts run per commit and `0.6`s of scan against `0.2`s.
#   ⌗ *What it does not claim, in 70's words: not that the extra 338 would have been RED.  They read the
#     edited paper; whether a pinned literal moved is the intersection's job and that is unchanged.  The
#     replay shows only that today's gate never asked them.*
#   ⛔ ** THE ONE HOLE LEFT IS NAMED AND IT IS A PROCESS RULE, WHICH IS WHY NO CODE HERE CLOSES IT: ** a
#     NEW receipt whose path comes from data would be invisible to the source and absent from the trace.
#     The census finds zero such receipts today (`TABLE` 0, `COMPUTED-NAME` 1), and it closes by writing a
#     receipt's index entry when it lands -- `sweep_runner_reads.py --from <the new receipt>`, one run of
#     a receipt the gate runs anyway.  Routed by 70 as a rule rather than written as a patch, correctly.
#   ⌈ And the four `D-SUPERSET` artefacts 70 found by hand are why ⓐ's directory arm requires that the
#     receipt opened a file OF THAT KIND: a `d: corpus/*` entry recorded for a receipt that read most of
#     `corpus/` names every paper and opened only `corpus/*.py` gates.  Membership of a glob is not a read.


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else None
    blob = touched_lines(ref)
    bl = os.path.join('corpus', 'quote_pin_baseline.tsv')
    if not blob or not os.path.exists(bl):
        return 0
    hits = set()
    for row in io.open(bl, encoding='utf-8'):
        if row.startswith('#') or not row.strip():
            continue
        p = row.split('\t')
        if len(p) < 2:
            continue
        lit = p[1].strip()
        if len(lit) >= 2 and lit[0] == '"' and lit[-1] == '"':
            try:
                lit = lit[1:-1].encode().decode('unicode_escape')
            except Exception:
                lit = lit[1:-1]
        if len(lit) >= MIN and lit in blob:
            hits.add(p[0])
    # ⛭ AND THE NUMERIC HALF, ADDED r7145 BECAUSE THE SENTENCE HALF MISSED A REAL BREAK.
    #   The gate shipped at r7143 scoped on the quote-pin baseline, whose keys are SENTENCES.  At r7145
    #   this seat corrected a figure in a paragraph -- `|Delta eta| = 3.32` to the closed form -- and
    #   `P15_the_exact_transmission_ratios...` asserts that paragraph's 3.32, 4.19 and 15.4 by name.
    #   ** The gate reported green: the receipt has no pinned SENTENCE in the changed lines. **
    #   ⌗ *That was the limit the file stated one revision earlier, found by walking into it.*
#   ⛔ AND THE LIMIT THAT REMAINS AFTER BOTH HALVES, STATED BECAUSE THIS REVISION WALKED INTO IT TOO:
#   `P15_the_exact_transmission_ratios...` asserts `the paragraph's 3.32` in its LABEL and never names
#   `CR_cosmology.tex` anywhere in its source -- it measures its own quadrature and attributes the
#   figure to a paragraph it does not read.  ** No file-scoped gate can reach that: there is nothing to
#   scope on. **  ⇒ *The repair is not in this gate but in the receipt -- a label quoting a paper's
#   figure should READ that paper -- and the class `a receipt asserting a paper figure it never reads`
#   is measurable and routed as such.*
    #   ⇒ So a changed line's NUMERIC literals are matched against receipt source as well.  A number
    #   that appears coincidentally pulls in a receipt that does not depend on it, which costs runtime
    #   and not correctness -- the affordable error of the two.
    #   ⛔ AND THE MATCH IS AN INTERSECTION, NOT A UNION, BECAUSE THE UNION IS UNAFFORDABLE.
    #   Numbers alone pull 102 receipts on this change set -- `3.32` and `15.50` occur all over a corpus
    #   this size, so a bare numeric match costs the whole runtime the file-name scope cost.  ⇒ *A
    #   receipt that asserts a PAPER's figure must also NAME that paper, so the scope is the receipts
    #   that do both.*  ⌗ The stated cost: a receipt that reads the paper and happens to contain the
    #   number for another reason is run anyway, which is runtime and not correctness.
    nums = set(re.findall(r'(?<![\w.])\d+\.\d{2,}(?![\w])', blob))
    _changed_paths[:] = changed_files(ref)
    names = set(os.path.basename(f) for f in _changed_paths)
    if nums and names:
        for root, _dirs, files in os.walk('receipts'):
            for fn in files:
                if not fn.endswith('.py'):
                    continue
                path = os.path.join(root, fn)
                try:
                    src = io.open(path, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                if _reads_the_change(path, src, names) and any(n in src for n in nums):
                    hits.add(path)
    # ⛭⛭⛭ AND THE THIRD HALF, ADDED r7151 BECAUSE THIS GATE MISSED A BREAK FOR THE THIRD TIME AND
    #   THE CAUSE WAS ITS OWN STATED LIMIT RATHER THAN A NEW ONE.
    #   Both halves above key on `corpus/quote_pin_baseline.tsv`, which carries ADJUDICATED keys only.
    #   ** So a receipt's pins are invisible to this gate until somebody adjudicates them -- which is
    #   precisely the window where the gate is needed: the revision that LANDS a receipt and then edits
    #   the paper around it. **  At `r7149` node 60's `r7146` receipt pinned four clauses at
    #   `count == 1`, two of them the clauses its own row asked the gate to CHANGE; the gate changed
    #   both, the receipt went red on the success of its own work, and this scope reported green because
    #   the baseline held one row for that receipt and not those four.
    #   ⇒ *The repair takes the baseline out of the loop: a receipt that NAMES a changed corpus file
    #   and carries a string literal appearing in a CHANGED line is in scope, adjudicated or not.*
    #   ⌈ That is the quote-pin operator's own test, computed here from the receipt source, and it
    #   rides the walk the numeric half already pays for -- so it costs no extra traversal.
    if blob and names:
        lits_re = re.compile(r'["\']([^"\'\\\n]{%d,})["\']' % MIN)
        for root, _dirs, files in os.walk('receipts'):
            for fn in files:
                if not fn.endswith('.py'):
                    continue
                path = os.path.join(root, fn)
                if path in hits:
                    continue
                try:
                    src = io.open(path, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                if not _reads_the_change(path, src, names):
                    continue
                for lit in lits_re.findall(src):
                    if lit in blob:
                        hits.add(path)
                        break

    # ⛭⛭⛭ AND THE FOURTH HALF, ADDED r7169 BECAUSE THIS GATE CANNOT SELECT AN ABSENCE AND `main`
    #   WAS RED FOR TWO REVISIONS THAT THE GATE ITSELF PUSHED.
    #   Every half above asks whether a receipt's literal appears in a CHANGED line.
    #   ** An assertion about an ABSENCE has no sentence to change, so no edit can ever select it. **
    #   At `r7167` the gate wrote `Regge--Wheeler` into `CR_cosmology.tex` for an unrelated purpose and
    #   `B25_the_scattering_object_exists`, which asserted that string appears ZERO times in the papers,
    #   went red.  This scope reported green at `r7167` and again at `r7168`; CI's plain suite found it.
    #   ⇒ *The class is the CORPUS-WIDE READER: a receipt that globs `corpus/*.tex` rather than naming
    #   one paper, so that ANY paper edit can falsify it.  It is selected whenever any `.tex` changes,
    #   with no literal test, because the literal test is exactly what cannot see it.*
    #   ⌈ ** MEASURED BEFORE THE CHANGE: 47 of 973 registered receipts, and all 47 run in 33
    #   receipt-seconds -- about ten seconds of wall at four at a time. **  So there is no affordability
    #   argument here, which is the `r7155` bar this script is held to: the two-revision red was an
    #   omission and not a trade.
    #   ⌗ *And the pre-registration predicted 1--3 of the 47 would already be red on `main` besides
    #   `B25`.  MEASURED: ZERO.  Reported as a miss -- the class had been invisible for the selector's
    #   whole life and had broken exactly once, so this arm is mostly prospective.*
    #   ⛔⛔ AND IT WAS INVISIBLE TWICE OVER, WHICH IS THE PART WORTH CARRYING:
    #   `B25`'s two adjudicated keys are `"W=0 at every horizon"` and
    #   `"superpotential W=lambda sqrt(f)/r"`, and NONE of its 44 source literals of `MIN` length or
    #   more appears in `r7167`'s 19,400 characters of changed lines -- so every half above was
    #   correctly silent.  ** The string the receipt actually asserted about is `Regge`, five
    #   characters, below this file's own `MIN = 8` floor. **  ⇒ *The guard that keeps a short literal
    #   from matching too much is exactly what hid a five-character claim, so widening `MIN` is not the
    #   repair -- the repair is to stop asking about literals for a receipt whose subject is the whole
    #   corpus.*
    TEX_GLOB = re.compile(r'glob[^\n]{0,200}?\*\.tex', re.S)
    if any(n.endswith('.tex') for n in names):
        for root, _dirs, files in os.walk('receipts'):
            for fn in files:
                if not fn.endswith('.py'):
                    continue
                path = os.path.join(root, fn)
                if path in hits:
                    continue
                try:
                    src = io.open(path, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                if TEX_GLOB.search(src):
                    hits.add(path)

    for h in sorted(hits):
        print(h)
    return 0


if __name__ == '__main__':
    sys.exit(main())
