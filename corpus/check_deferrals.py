#!/usr/bin/env python3
"""check_deferrals.py -- THE DEFERRAL GATE: fail the turn if any live document contains a written
deferral to Daryl.

** WHY A GATE AND NOT ANOTHER RULE. **  THE_PLAN already carries the rule, absolute, since r1885:

    *** THE GATE NEVER WRITES A DEFERRAL TO DARYL INTO ANY DOCUMENT. ***  Not in the plan, not in a
    ledger, not in a paper, not in a map.  If something genuinely needs him, it is said TO HIM, IN THE
    TURN, and it is not parked in a file where it becomes a standing excuse.
    *** A written "Daryl's call" is a deferral that outlives the moment and gets quoted back as
    authority.  That is what makes it worse than simply asking. ***

** AND THE PROGRAMME HAS NOW CAUGHT IT SEVEN TIMES. **  r269 (a whole operation, physics paused:
"ontology is unassigned" diagnosed as WRONG ON THE MERITS); r1711 (deferred to an item while
auditing the document that said it); r1885 (wrote a fresh one and quoted it back as his instruction);
r2495 (filed the rule AGAIN as a scrap); r2524 (recorded the Higgs as a principled decline -- Daryl:
"I've met nodes trying to bury that"); r2529 (deferred on L-174 (1) AND praised another node for the
same move in the wisdom ledger); and the phrase "the conversion is Daryl's" reached ** 41 uses ** while
all of that was being written.

  ⇒ *** A WRITTEN RULE WAS THE r1885 REMEDY.  IT HAS FAILED FIVE TIMES SINCE.  This is the gate. ***

** WHAT IT CHECKS. **  Every live document for phrases that assign a decision to Daryl in writing.
** Live ** means: not `retired/`, not `_dig/`, not archived work directories -- those are the RECORD, and
rewriting a record to look better is a different failure.

** THE TWO EXEMPTIONS, NAMED RATHER THAN PATTERN-MATCHED, because an allowlist is exactly how this
survives: **
  1. ** PROTECTED_OPEN.md's exit procedure. **  "① Daryl closes it.  ② Its object is named, all four
     checks are written into a kill receipt, and Daryl authorises."  ** That is a PROCEDURE with named
     conditions for how a protected row LEAVES a register -- a safeguard against a node unilaterally
     killing an open problem.  It does not tell anyone not to WORK anything. **
  2. ** THE_PLAN.md's r1885 section and this file. **  The RECORD of the failure, including Daryl's own
     words.  ** Deleting the record is how the pattern gets to happen an eighth time. **

⚠ ** AND THE EXEMPTIONS ARE FILE-SCOPED AND EXACT. **  Not "any file mentioning the procedure" -- these
two paths, and nothing else inherits them.

    python3 corpus/check_deferrals.py
    python3 corpus/check_deferrals.py --all    # show every hit, exempt or not

Written r2531, after Daryl: "Stop fucking blocking shit in my fucking name."  Stated for reversal.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** the phrases that assign a decision in writing. **
# ** r2832: a QUOTATION of a deferral -- in a ledger scrap recording that one was found and
# removed, or in a row's note explaining what a mangled sentence originally said -- is not a
# live deferral.  *** The gate flagged its own repair record.  Skip lines that quote the
# phrase inside quotation marks. ***
QUOTED = re.compile(r'["\u201c\u201d][^"\u201c\u201d]{0,120}Daryl' + chr(39) + r'?s[^"\u201c\u201d]{0,40}["\u201c\u201d]', re.I)
# ** r4261: the same skip, for the ROLE nouns the patterns below now carry.  A ledger row quoting a
# removed comment, or a vetting rule quoting the failure it forbids, is a RECORD of a deferral and
# not one -- and three of the role-noun hits were exactly that. **
QUOTED_ROLE = re.compile(
    r'["\u201c\u201d][^"\u201c\u201d]{0,160}(?:the (?:author|orchestrator)|ask(?:ed)? (?:for )?the (?:author|orchestrator))'
    r'[^"\u201c\u201d]{0,60}["\u201c\u201d]', re.I)

PATTERNS = [
    re.compile(r"Daryl'?s call", re.I),
    # ** NOT a bare possessive.  "Daryl's words", "Daryl's correction", "Daryl's lead" are the RECORD
    # of him -- catching those would push toward deleting his own contributions from the corpus, which
    # is the opposite failure.  Only the ASSIGNMENT OF A DECISION is caught. **
    # ** r2782: the suffix was OPTIONAL, so bare "is Daryl's" matched any POSSESSIVE.
    #   *** It fired on r2638's "the drawing is Daryls" -- an attribution of AUTHORSHIP,
    #   not a deferral of a DECISION.  A gate that flags true sentences drives edits to
    #   them, which is the r2779 lesson.  The deferral verb is now REQUIRED. ***
    # ** r2826: the verb list was a NARROW SELECTOR -- it missed call/supply/schedule/
    # name/steer/confirm/reconcile/enact/pay/update/overrule/launch/firm-up/grab, and
    # 199 live deferrals had accumulated behind it.  *** Match ANY verb after
    # "Daryl's to", and the "for Daryl to <verb>" form, which was not matched at all. ***
    re.compile(r"is Daryl'?s\s+to\s+\w+", re.I),
    re.compile(r"\bDaryl'?s\s+to\s+\w+", re.I),
    re.compile(r"\bfor Daryl to\s+\w+", re.I),
    re.compile(r"\bpending on Daryl\b", re.I),
    re.compile(r"\bawait(?:s|ing)?\s+Daryl\b", re.I),
    re.compile(r"the owner'?s call", re.I),
    re.compile(r"the verdict is\s+(?:yours|Daryl)", re.I),
    re.compile(r"conversion is Daryl", re.I),
    re.compile(r"left to Daryl", re.I),
    re.compile(r"Daryl'?s to (?:set|say|decide|make|take|seat|time)", re.I),
    re.compile(r"(?:not|never) (?:mine|ours|the gate'?s) to (?:decide|call|seat|time|set)", re.I),
    # ** r4261: the gate named the PERSON and missed the ROLE.  P12's sec:weyl-a3 carried a live
    # deferral for ~1700 revisions -- "the finder asked for the author on it and so do I" -- and
    # every pattern above needs the literal token "Daryl".  A node that writes "the author" or
    # "the orchestrator" instead of the name defers just as durably and passes the gate.
    # ** THE NARROWING IS DELIBERATE AND WAS MEASURED. **  A broad role-noun pattern returns 41
    # hits, and most are the RULE rather than a violation -- "state it plainly for the author to
    # reverse", "never offload them to the orchestrator".  A pattern that cannot tell the rule
    # from the breach of it is not a measurement.  So: only the forms that ASSIGN A DECISION, and
    # "to reverse" is excluded by construction, being the reversal convention and not a deferral.
    re.compile(r"\bthe (?:author|orchestrator)'?s call\b", re.I),
    re.compile(r"\bthe (?:author|orchestrator)'?s to\s+\w+", re.I),
    re.compile(r"\bask(?:ed|ing|s)?\s+(?:for\s+)?the (?:author|orchestrator)\b", re.I),
    re.compile(r"\b(?:left|leave[sd]?|defer(?:red|ring|s)?)\s+to the (?:author|orchestrator)\b", re.I),
    re.compile(r"\bawait(?:s|ing)?\s+the (?:author|orchestrator)\b", re.I),
    re.compile(r"\bfor the (?:author|orchestrator) to\s+(?!reverse\b)\w+", re.I),
]

# ** archived record -- rewriting it to look better is a different failure. **
ARCHIVE = ('retired/', '_dig/', 'c24_work/', 'storyboard_receipts/', 'forks/c19fork/', '.git/')

# ** the two named exemptions.  FILE-SCOPED AND EXACT. **
EXEMPT = {
    'PROTECTED_OPEN.md':            'the stated exit procedure for a protected row (a safeguard, not a block)',
    'THE_PLAN.md':                  'the r1885 record of this failure, including Daryl\'s own words',
    'corpus/check_deferrals.py':    'this gate',
    'ONTOLOGY_FOUNDATION_INDEX.md': 'exists BECAUSE of the r269 correction; every hit quotes the phrase '
                                    'in order to REJECT it',
    # ** r4261: the two credo documents STATE this rule -- "never offload them to the orchestrator",
    # "carry the calls the source settles" -- so a role-noun pattern reads the rule as its own breach.
    # Same precedent as THE_PLAN's r1885 section: the record of the failure is not the failure. **
    'capstones/THE_CODA.md':        'the seats section, which is where this rule is stated',
    'capstones/CODA_FIELD_NOTE.md': 'the dated casebook of this failure, including its fifth face',
}

# ** DATED LOGS -- records of what past revisions did.  Rewriting a log to look better is falsifying
# the record, which is a different failure from the one this gate exists to catch.  Named and exact,
# like the exemptions: nothing is excluded by pattern. **
LOGS = (
    'FORK_c54.md',
    'CORPUS_MAP.md',
    'PHASE7_BUILD_LEDGER.md',
    'CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md',
    'RECALL_ACROSS_COMPACTION_full-transcript.md',
    'CREDO_birth_transcript.md',
    'DEMONSTRATING_THE_WAY_full-transcript.md',
    'C40_HARVEST_r1064-r1087.md',
    'CR_intake_notebook.md',
    'FIGURE_WORK_LOG.md',
    'THE_CLOSURE_LEDGER.md',
    'SYNTHESIS_FIGURE_STORYBOARD.md',
    'P3_SWING_ONTOLOGY_hinge-and-door.md',
    'E1_CITATION_CATALOGUE.md',
)


def live_files():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for fn in files:
            if not fn.endswith(('.md', '.py', '.tex')):
                continue
            p = os.path.relpath(os.path.join(base, fn), ROOT)
            if any(p.startswith(a) or ('/' + a) in ('/' + p) for a in ARCHIVE):
                continue
            out.append(p)
    return sorted(out)


def main():
    show_all = '--all' in sys.argv
    print()
    print('  check_deferrals -- is a decision assigned to Daryl in writing anywhere live?')
    print()

    bad, exempt_hits, scanned = [], 0, 0
    for rel in live_files():
        scanned += 1
        try:
            t = open(os.path.join(ROOT, rel), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        hits = []
        for pat in PATTERNS:
            for m in pat.finditer(t):
                # ** r2832: skip a QUOTED deferral -- a ledger scrap recording that one was found
                # and removed, or a note explaining what a mangled sentence originally said.
                # *** The gate was flagging its own repair record. ***
                ctx = t[max(0, m.start()-140):m.end()+40]
                if QUOTED.search(ctx) or QUOTED_ROLE.search(ctx):
                    continue
                line = t[:m.start()].count('\n') + 1
                hits.append((line, m.group(0)))
        if not hits:
            continue
        if rel in LOGS:
            exempt_hits += len(hits)
            if show_all:
                print(f'    log     {rel}  ({len(hits)} hit(s)) -- dated record of past work')
            continue
        if rel in EXEMPT:
            exempt_hits += len(hits)
            if show_all:
                print(f'    exempt  {rel}  ({len(hits)} hit(s)) -- {EXEMPT[rel]}')
            continue
        for line, txt in hits:
            bad.append((rel, line, txt))

    print(f'  {scanned} live file(s) scanned; {exempt_hits} hit(s) in the {len(EXEMPT)} named '
          f'exemptions and {len(LOGS)} named logs.')
    print()
    if bad:
        for rel, line, txt in bad[:40]:
            print(f'  [FAIL] {rel}:{line}  "{txt}"')
        if len(bad) > 40:
            print(f'  ... and {len(bad)-40} more')
        print()
        print('  ⛔ A DECISION IS ASSIGNED TO DARYL IN WRITING.  THE_PLAN, since r1885:')
        print('     ** "THE GATE NEVER WRITES A DEFERRAL TO DARYL INTO ANY DOCUMENT.  If something')
        print('     genuinely needs him, it is said TO HIM, IN THE TURN, and it is not parked in a file')
        print('     where it becomes a standing excuse." **')
        print('  ⇒ ** A written deferral outlives the moment and gets quoted back as authority.  That is')
        print('    what makes it worse than simply asking. **')
        print('  ⌗ If the material decides, DECIDE.  If a judgement genuinely remains, SAY SO IN THE')
        print('    TURN and leave the file alone.')
        return 1

    print('  no written deferrals in live documents.')
    print()
    print('  ⌗ THE TWO NAMED EXEMPTIONS, and why they are not blocks:')
    for k, v in EXEMPT.items():
        print(f'     {k} -- {v}')
    print('  ⚠ They are FILE-SCOPED and EXACT.  Nothing else inherits them, because an allowlist is')
    print('    exactly how this pattern survives.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
