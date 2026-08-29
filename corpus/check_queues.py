#!/usr/bin/env python3
"""check_queues.py -- L-105, the sixth gate.  A field ledger's QUEUE can outlive its own
answers, and nothing checked it.

At c54.34 three of nine inherited queue items turned out to be stale text quoting a question
the same ledger later RAN: the Euclid protocol (PART XII, r1110), the SCTs (C5, r1888), and
the conformal boundary (supplied by P8).  A fourth had a premise the ledger's own later work
had falsified.

This flags any queue entry whose ledger elsewhere records a RUN of the same probe id.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
LEDGERS = [f for f in os.listdir(ROOT) if f.endswith('_LEDGER.md')]
QUEUE = re.compile(r'(?:untried queue|queue|NOT COMPUTED|not yet worked|§4d)', re.I)
RUN = re.compile(r'`?([A-Z]{1,2}\d+[a-z]?)`?\s*✔?\s*RUN', re.I)
PROBE = re.compile(r'`([A-Z]{1,2}\d+[a-z]?)`')

def main():
    stale, checked = [], 0
    print(f"  scanning {len(LEDGERS)} field ledgers for queue entries answered elsewhere")
    for f in sorted(LEDGERS):
        txt = open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read()
        ran = set(m.group(1) for m in RUN.finditer(txt))
        lines = txt.split('\n')
        for i, ln in enumerate(lines):
            # ** r2386: A QUOTATION OF A STALE QUEUE ENTRY IS NOT A STALE QUEUE ENTRY. **
            # This gate fired on an annotation that QUOTED the OPTICS 4d entry in order to record
            # that it had been answered -- "its 4d queue read: `O5` shows lambda -> 0 ..." -- so the
            # note ABOUT the defect was read AS the defect.  Third instance of that meta-pattern:
            # check_currency read a document's discussion of the fork as currency, and check_arcs
            # read an UNDATED-POSITION flag's own revision as the position's date.  ** A gate that
            # cannot tell a report from the thing reported punishes the act of recording. **
            #
            # A first attempt tried to PARSE quotation marks and skip quoted spans.  It was fragile
            # -- markdown emphasis, nested quotes and long spans all defeat it -- and a fragile
            # exemption in a gate is worse than none, because it fails silently in the direction of
            # passing.  ** So the exemption is DECLARED, not inferred **, exactly as `current: none`
            # and DECLARED-UNDATED are: a line that REPORTS a stale queue entry carries the marker
            # [REPORTED] and this gate skips it.  Declaring costs one token and cannot be
            # misparsed; inferring costs a heuristic that will be wrong on prose nobody has written
            # yet.
            if '[REPORTED]' in ln:
                continue
            bare = ln
            if not QUEUE.search(bare):
                continue
            checked += 1
            ln_for_codes = bare
            for pid in set(PROBE.findall(ln_for_codes)):
                # ⛭⛭ r3550 (node 60): ** THE SETTLED-WORD LIST PREDATES THE LANDING TABLES. **
                # The gathers from r3524 on put a disposition table in every field ledger, and its
                # vocabulary is not this list's.  `QUADRIC_GEOMETRY_LEDGER.md:66` is a landing ROW
                # -- "| **`D3` Segre bounces, with a reason** | **BOUNCED** | ... an honest answer to
                # the queue's own question first |" -- and it fired: the row MENTIONS a queue, names
                # a probe recorded RUN, and says BOUNCED, which this list did not know.
                #   ⇒ *** So the gate read a row REPORTING an adjudication as a queue entry awaiting
                #       one -- r2386's own meta-pattern, "a gate that cannot tell a report from the
                #       thing reported punishes the act of recording", arriving from the one
                #       direction r2386 could not have anticipated: a table format invented later. ***
                # ⌗ TWO WORDS ADDED AND NOT SIX, because this gate's own comment is right that a
                #   loose exemption fails silently in the direction of passing:
                #     · BOUNCED   -- fired; the probe RAN and the field bounced.  An adjudication.
                #     · WITHDRAWN -- in use at COMPLEX_ANALYSIS_LEDGER.md:250.  An adjudication.
                #   PART-LANDED and LANDED AS A BOUND need nothing: `\bLANDED\b` already matches
                #   inside them.  ** HELD and the two OWED forms are deliberately NOT added ** --
                #   `HELD` is ordinary English that a real queue line could carry ("held over"), and
                #   `SUBSTANCE OWED` / `POINTER OWED` say work REMAINS, which is the state this gate
                #   exists to look at.  Anything else declares itself with [REPORTED], as designed.
                if pid in ran and not re.search(
                        r'\b(RUN|LANDED|ANSWERED|SETTLED|RESOLVED|CLOSED|DONE|BOUNCED|WITHDRAWN)\b',
                        ln, re.I):
                    stale.append((f, pid, ln.strip()[:90]))
    print(f"  queue-ish lines examined: {checked}")
    print()
    if stale:
        print(f"  STALE QUEUE ENTRIES: {len(stale)}")
        for f, pid, ln in stale:
            print(f"    [FAIL] {f}: queue names `{pid}` which this ledger records as RUN")
            print(f"           {ln}")
        print()
        print("  A queue that outlives its own answers reads as live work and is not.")
        return 1
    print("  No queue entry names a probe its own ledger records as run.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
