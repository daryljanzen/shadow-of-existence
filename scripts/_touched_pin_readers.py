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
    names = set(os.path.basename(f) for f in changed_files(ref))
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
                if any(nm in src for nm in names) and any(n in src for n in nums):
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
                if not any(nm in src for nm in names):
                    continue
                for lit in lits_re.findall(src):
                    if lit in blob:
                        hits.add(path)
                        break

    for h in sorted(hits):
        print(h)
    return 0


if __name__ == '__main__':
    sys.exit(main())
