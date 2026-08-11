#!/usr/bin/env python3
"""check_receipt_asserts.py -- the SEVENTEENTH gate: A RECEIPT THAT CANNOT FAIL.

** THIS GATE IS BUILT FROM THE WORKING FORK'S OWN FINDING, absorbed r2384 rather than rediscovered. **

`THE_ASSUMPTIONS_RETREATED_UPWARD` (the c54.114-c54.153 capstone) reports a systematic pass over all
twenty-eight cited receipts in the perturbation sector -- fourteen matched -- and says the sharpest
thing it returned was not a wrong link:

    ** "the dominant failure is not a wrong link but a RECEIPT THAT CANNOT FAIL: three receipts in
    one cluster contain no assertion at all, so `OK` certifies that Python exited zero.  That is how
    a claim of robustness -- 'stable under +-2% in r_0' -- rode inside a green receipt for two
    revisions; measured, the depths drift by 15%." **

`check_receipts` verifies that a \\rcpt{} citation resolves to an INDEX row and a file on disk.  It
cannot see this, and neither can any link checker: the link resolved, the file existed, the receipt
ran and passed, and there was nothing in it that could have come out false.

** THE CONVENTION, SETTLED HERE BECAUSE IT IS THIS LINEAGE'S TO SETTLE (r2385). **

`\rcpt{}` has never been defined tightly enough to adjudicate this, so it is defined now:

    ** \rcpt{X} means: the claim in this sentence is CHECKED by X, and X would FAIL if the claim
    were false. **

That is the whole of it, and three things follow.

  (a) A script that COMPUTES the quantity and prints it is not a receipt.  Printing 149 lines of a
      worked argument is a NOTE -- valuable, and the corpus has homes for notes (the field ledgers,
      the build records, retired/).  What makes an artefact a receipt is not that it ran but that it
      could have come out false.

  (b) So a cited transcript is not a "legitimate artefact cited wrongly" OR a "defect to fix" as an
      either/or.  ** The disposition is decided by whether the cited claim is computational. **  If
      it is, the receipt owes an assertion of THAT claim and gaining one is a two-line fix.  If it is
      not -- the sentence rests on a proof or a definition -- then \rcpt{} was the wrong citation and
      the sentence should point at the section, with the transcript kept as a note.

  (c) The convention is not retroactive blame.  It was maintained loosely for a long time and the
      loose reading is why 40 cited artefacts here cannot fail.  ** Defining it is what makes this
      gate mean something; without the definition the gate is an opinion about style. **

** AND THE TAXONOMY IS NOT NEW: `THE_RECEIPT_AUDIT.md` DEFINED IT AT r1324. **  This gate was written
before that file was read, and it was inventing words the corpus already had:

    OK  VERIFIED                     -- does exactly what it claims, core independently reconfirmed.
                                        No gate certifies this; it takes a reading.
    () CORE-REAL / VERDICT-OVERCLAIMS -- a correct NARROWER computation wrapped in a verdict asserting
                                        more.  Invisible to any gate: it is the fork's scalar-monodromy
                                        case (4pi/rho claimed, 2pi/rho computed) and adjudicating it is
                                        a judgement over two texts.
    X  VACUOUS / ASSERTED            -- the key check is a tautology, or the claim is taken as a label
                                        rather than derived.  ** THIS is what this gate mechanises. **
    ?  NOT FOUND                     -- the cited computation is not locatable.  check_receipts covers it.

So: this gate is the mechanical half of X, and nothing more.  ** A finding lands better in vocabulary
that exists than in vocabulary invented for it **, and the reason to read a document before building an
instrument for its subject is that the document usually already has the words.

** SO THIS GATE ASKS ONE MECHANICAL QUESTION: can this receipt fail? **  A receipt that can fail
contains at least one of: an `assert`, a comparison against a tolerance that raises or prints a
verdict, or an explicit FAIL/MISMATCH path.  A receipt with none of those is a script, not a check,
and a green run tells you only that the interpreter finished.

WHAT IT DOES NOT DO, and the boundary matters.  It does NOT ask whether the receipt asserts THE
THING CLAIMED -- the capstone's other finding, where P16 asserted the scalar monodromy 4pi/rho and
cited the receipt computing the tensor's 2pi/rho.  ** That question is a judgement over two texts and
no regex adjudicates it **, which is `check_citations`' and `check_paststate`' own rule.  This gate
takes the half that is decidable and says so.

** SUPERSEDED IN PART AT r2394 — READ THIS BEFORE TRUSTING ITS PASS. **

The working fork built `scripts/lint_assertions.py` over the same span and it is STRICTLY STRONGER on
the question this gate asks.  This gate tests for the PRESENCE of a failure path.  The lint tests
whether the condition could ever be false, and it was extended twice, both times because it missed
something real:

  * `check("tilt 45deg", True)` -- a local `check(label, condition)` helper that prints PASS/FAIL and
    folds into an `ok` flag.  ** Invisible to this gate: the file contains a call, not an assert, and
    may carry real assertions elsewhere. **
  * `sqrt(Rv**2-1) - sqrt(Rv**2-1) == 0` -- the difference form, true at every dimension.
  * `assert 3*2*2 == 12` -- a constant condition.  ** This gate counts it as a failure path. **  The
    fork's own base-rate ledger records these as "arithmetic dressed as claims, written by workers
    measured on a count."

So: this gate's rc=0 means every receipt HAS a check; it does NOT mean every check can fail.
`scripts/lint_assertions.py` is the one that answers the second, and it is run alongside.  Kept
rather than deleted because it is cheap, it covers the "no check of any kind" case directly, and
** a weaker gate that states its own boundary is worth more than a deleted one, provided the boundary
is stated where the pass is read. **

    python3 corpus/check_receipt_asserts.py

Exit 1 on any receipt with no failure path.  Written r2384.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
RDIR = os.path.join(ROOT, 'receipts')

# A receipt can fail if it contains one of these.  Deliberately broad on the positive side: the
# question is "could this ever come out false", and the corpus's receipts express that many ways.
CAN_FAIL = [
    (r'\bassert\b',                          'assert'),
    (r'\braise\b',                           'raise'),
    (r'\bsys\.exit\s*\(\s*1',                'exit 1'),
    (r'\bFAIL\b',                            'FAIL path'),
    (r'\bMISMATCH\b',                        'MISMATCH path'),
    (r'\bnp\.allclose\b|\bisclose\b|\bmath\.isclose\b', 'tolerance compare'),
    (r'\bif\s+abs\(',                        'abs() tolerance'),
    (r'✔|✗|PASS\b',                          'verdict token'),
]
# ...but a verdict token alone, with no comparison anywhere, is a print and not a check.
WEAK_ONLY = {'verdict token'}


def scan(path):
    try:
        src = open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return None
    # strip comments and docstrings so a receipt does not pass on the word "assert" in prose
    body = re.sub(r'"""(?:.|\n)*?"""', '', src)
    body = re.sub(r"'''(?:.|\n)*?'''", '', body)
    body = '\n'.join(l.split('#')[0] for l in body.split('\n'))
    found = [name for rx, name in CAN_FAIL if re.search(rx, body)]
    return found, len(src)


def cited_stems():
    """r2384: an UNCITED exploration that cannot fail is a script nobody leans on.  A CITED one is
    a paper claim with nothing behind it.  ** The gate fails on the second and reports the first. **
    Without this split it flags 101 files and the real number -- the ones a paper rests on -- is
    buried in them."""
    out = set()
    for f in glob.glob(os.path.join(HERE, '*.tex')):
        t = open(f, encoding='utf-8', errors='replace').read()
        out |= set(re.findall(r'\\rcpt\{([^}]+)\}', t))
    return out


def main():
    files = sorted(glob.glob(os.path.join(RDIR, '**', '*.py'), recursive=True))
    cited = cited_stems()
    if not files:
        print('  [FAIL] no receipts found under receipts/')
        return 1
    print()
    print('  RECEIPTS THAT CANNOT FAIL -- can each receipt ever come out false?')
    print()
    cannot, weak, ok = [], [], []
    for f in files:
        res = scan(f)
        if res is None:
            continue
        found, size = res
        rel = os.path.relpath(f, ROOT)
        if not found:
            cannot.append((rel, size))
        elif set(found) <= WEAK_ONLY:
            weak.append((rel, found))
        else:
            ok.append(rel)
    def stem(rel):
        return os.path.basename(rel)[:-3]
    cannot_cited = [(r, s2) for r, s2 in cannot if stem(r) in cited]
    cannot_uncited = [(r, s2) for r, s2 in cannot if stem(r) not in cited]
    print(f'  {len(files)} receipt(s): {len(ok)} carry a failure path, '
          f'{len(weak)} carry only a verdict token, {len(cannot)} carry none.')
    print(f'  of those {len(cannot)}: **{len(cannot_cited)} are CITED by a paper** '
          f'and {len(cannot_uncited)} are not.')
    print()
    if weak:
        print(f'  [WARN] {len(weak)} receipt(s) print a verdict with no comparison behind it:')
        for rel, found in weak[:20]:
            print(f'    {rel}')
        print( '    A printed ✔ with nothing compared is a claim, not a check.')
        print()
    if cannot_uncited:
        print(f'  [WARN] {len(cannot_uncited)} receipt(s) cannot fail and are NOT cited by any paper.')
        print( '    An uncited exploration that cannot fail is a script nobody leans on -- worth a')
        print( '    header saying EXPLORATION, not a defect.')
        print()
    if cannot_cited:
        print(f'  ⛔ CANNOT FAIL **AND CITED BY A PAPER**: {len(cannot_cited)}')
        for rel, size in cannot_cited[:40]:
            print(f'    [FAIL] {rel}  ({size} bytes, no assert / raise / tolerance / FAIL path)')
        print()
        print('  ** A receipt with no failure path is a script, not a check. **  A green run tells')
        print('     you the interpreter finished.  This is the working fork\'s own c54.153 finding:')
        print('     a robustness claim -- "stable under +-2% in r_0" -- rode inside a green receipt')
        print('     for two revisions, and measured, the depths drift by 15%.')
        print('     Fix: give each an assertion of the thing it is cited for, or say in its header')
        print('     that it is an EXPLORATION and not a receipt.')
        return 1
    if cannot_uncited:
        print('  No CITED receipt lacks a failure path.')
        print()
        return 0
    print('  Every receipt carries a path on which it could fail.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
