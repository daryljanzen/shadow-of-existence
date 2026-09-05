#!/usr/bin/env python3
"""quotepin.py -- A QUOTATION PIN THAT DIAGNOSES ITS OWN BREAK.

** THE PROBLEM, and it is `L-249`'s class one step narrower. **  A receipt that quotes a paper
sentence and asserts it is present has exactly two states: green, and `FAIL`.  ** `FAIL` says nothing
about WHY. **  *The sentence may have been deleted, rewritten, moved to another file, or
strengthened into a claim the receipt would welcome -- and the reader of a red run cannot tell those
apart without going and looking.*

  ⇒ *** SO THE BREAK REPORTS ITSELF: "this text left `corpus/X.tex` at rNNNN -- <that commit's own
      subject line>" instead of "FAIL". ***

** ⌗ WHY THIS IS SEPARABLE WHERE THE CLASS IS NOT. **  `L-249` left a gate owed and said why it could
not be built: *"pins a live register" is not mechanically separable from "checks a live register"*, and
a gate needs that distinction.  ** This needs no such distinction. **  *It does not ask whether a check
SHOULD pin; it makes the pin self-describing when it breaks.*  ⌷ *The proposal is the observer line's
(r3107); the build is here.*

** ⚠ AND WHAT IT DELIBERATELY DOES NOT DO: decide what the replacement means. **  *It names the commit
that removed the text and that commit's subject.  Whether the new wording strengthens, weakens or
relocates the claim is a READING, and a helper that guessed would be `L-249`'s error in a new place --
a tool asserting what a person must judge.*  ⇒ ** The nearest-added-line hint below is printed as a
CANDIDATE and is never returned as a verdict. **

    from quotepin import pinned
    ok, why = pinned(SENTENCE, tex, 'corpus/CR_framework.tex')
    check('P7 states ...' if ok else why, ok)

Written r3108 (`L-250`).  Stated for reversal.
"""
import os
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
#: a revision id as this corpus writes them in commit subjects
_REV = re.compile(r'\b(r\d{3,5}[a-z]?|c54\.\d+)\b')


def _git(*a, root=None):
    return subprocess.run(['git'] + list(a), cwd=root or ROOT,
                          capture_output=True, text=True).stdout


def removing_commit(quote, path, root=None):
    """(sha, subject) of the commit that removed `quote` from `path`, or (None, None)

    ** `git log -S` counts OCCURRENCES, so the commit it names for a vanished string is the one
    where the count fell to zero. **  *That is the removal, which is what a broken pin needs.*
    ⌗ *`--` bounds it to the one file, so a copy of the sentence living elsewhere does not mask the
    removal from the file the receipt actually read.*
    """
    out = _git('log', '-S', quote, '--oneline', '--no-abbrev-commit', '--', path, root=root)
    lines = [l for l in out.split('\n') if l.strip()]
    if not lines:
        return None, None
    sha, _, subject = lines[0].partition(' ')
    return sha, subject


def candidate_replacement(sha, path, quote, root=None, n=1):
    """lines ADDED to `path` by `sha` that share the most words with `quote` -- A HINT, NOT A VERDICT

    *Printed so a reader has somewhere to look first.  ** It is a word-overlap score and nothing
    more, and it is labelled as a candidate wherever it is shown. ***
    """
    if not sha:
        return []
    diff = _git('show', '--unified=0', '--format=', sha, '--', path, root=root)
    added = [l[1:].strip() for l in diff.split('\n')
             if l.startswith('+') and not l.startswith('+++') and len(l) > 40]
    want = set(re.findall(r'[a-z]{4,}', quote.lower()))
    if not (added and want):
        return []
    scored = sorted(added, key=lambda l: -len(want & set(re.findall(r'[a-z]{4,}', l.lower()))))
    best = [l for l in scored[:n]
            if len(want & set(re.findall(r'[a-z]{4,}', l.lower()))) >= 3]
    return best


def pinned(quote, text, path, at=None, root=None, hint=True):
    """(ok, message) -- assert `quote` is in `text`, and DIAGNOSE the break when it is not

    `path` is the repo-relative file `text` was read from; it is what the diagnosis searches.
    `at`, when given, is a commit the quote is claimed to have been present at -- checked, so a pin
    to the wrong commit is reported as such rather than passing silently.
    """
    if quote in text:
        return True, f'present in {path}'

    sha, subject = removing_commit(quote, path, root=root)
    if sha is None:
        # ** NEVER THERE is a different finding from GONE, and conflating them would send a reader
        # ** hunting a removal that never happened. **
        # ⛔⛭ ** AND THERE IS A THIRD CASE THIS CONFLATED WITH THE FIRST -- r4127: NOT REACHABLE. **
        # *`git log -S` searches the history the clone HAS.  On a shallow clone it returns nothing
        # for a removal that certainly happened, and this message then reported "may never have
        # been in this file" -- a confident claim about the corpus drawn from a property of the
        # checkout.*  ** A tool that cannot tell "absent" from "beyond my horizon" states the
        # stronger of the two, and a reader acts on it. **
        if os.path.exists(os.path.join(root or ROOT, '.git', 'shallow')):
            return False, (f'⛔ NOT FOUND in {path}, and `git log -S` finds no commit that removed '
                           f'it -- **but THIS CLONE IS SHALLOW, so a removal outside the fetched '
                           f'window is invisible here and this is not evidence the text was never '
                           f'present.*  Re-run against a full clone before concluding anything.*')
        return False, (f'⛔ NOT FOUND in {path}, and `git log -S` finds NO commit that ever '
                       f'removed it -- so this text may never have been in this file.  '
                       f'*Check the quotation itself before checking the paper.*')
    rev = _REV.search(subject)
    where = rev.group(0) if rev else sha[:12]
    msg = (f'⌗ this text LEFT {path} at {where} -- "{subject.strip()[:90]}"  '
           f'(commit {sha[:12]})')
    if at:
        was = quote in _git('show', f'{at}:{path}', root=root)
        msg += f'\n           and it {"WAS" if was else "was NOT"} present at the pinned {at[:12]}'
        if not was:
            msg += '  ⛔ -- so the PIN is wrong, not only the paper'
    if hint:
        for cand in candidate_replacement(sha, path, quote, root=root):
            msg += f'\n           candidate replacement (a word-overlap HINT, not a verdict): '
            msg += f'"{cand[:110]}"'
    return False, msg
