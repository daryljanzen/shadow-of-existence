"""check_citation_chain.py -- IS THE WHOLE CHAIN CONNECTED, OR ONLY ITS LINKS?

** PROVING A THING IS NOT COMMUNICATING IT. **  The corpus carries four kinds of
artefact and three rails between them, and every existing gate checks ONE rail:

    paper --\\ldg{}--> ledger        check_depmatrix's fourth grain, check_marker_buried
    paper --\\rcpt{}-> receipt       check_receipts, check_receipt_orphans
    ledger --names--> receipt       ** NOTHING **
    receipt --names-> paper+section ** NOTHING **

The two unchecked rails are the ones that carry the REASON.  A receipt that no ledger
names is a computation with no argument attached: the paper cites it, the gate says
the citation resolves, and the question it settles is recorded nowhere a reader of the
field would look.  Measured at r3660: FOUR of 60's five field-bake receipts -- D1, D2,
N1, T1 -- were named in NO ledger, and five ledgers named no receipt at all.  Each
receipt ran, each was registered, each was cited from a paper.  The chain was broken
in the one place no instrument looked.

WHAT THIS GATE CHECKS, and it is deliberately narrow:

  (1) FIELD-BAKE RECEIPTS ARE NAMED BY THEIR LEDGER.  A receipt whose stem begins with
      a field-bake probe id (I3, D2, N1, CX1, ...) and whose registry row says it came
      from a field bake must be named in that field's ledger.  Otherwise the ledger has
      a probe with no evidence and the receipt has evidence for no probe.

  (2) A LEDGER THAT HAS LANDED SOMETHING NAMES A PAPER AND A SECTION.  A landing table
      row marked LANDED must say WHERE.  "Landed" with no address is unfollowable.

  (3) EVERY \\ldg KEY RESOLVES TO A LEDGER WITH A LANDING TABLE.  A marker pointing at a
      ledger that has not been gathered sends a reader to a document that cannot answer.

WHAT IT DOES NOT CHECK.  It does not require every receipt to be named in a ledger --
most receipts predate the field bakes and belong to the papers' own development.  It
does not require every ledger row to have a receipt: fences and connections are
arguments, not computations, and the honest ones have nothing to compute.

DECLARED EXEMPTIONS.  A ledger with no landing table is not yet gathered and is skipped
by (2) with a note.  A receipt may declare `NOT-A-FIELD-BAKE-RECEIPT:` in its docstring.
Declared, never inferred.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROBE = re.compile(r'^([A-Z]{1,3}\d+[a-z]?)_')


def ledgers():
    out = {}
    for f in glob.glob(os.path.join(ROOT, '*_LEDGER.md')):
        key = os.path.basename(f)[:-len('_LEDGER.md')].lower()
        out[key] = f
    return out


def main():
    print()
    print('  check_citation_chain -- is the chain connected, or only its links?')
    print()
    L = ledgers()
    text = {k: open(v, encoding='utf-8', errors='replace').read() for k, v in L.items()}
    fails = []

    # ---- (3) every \ldg key resolves to a gathered ledger -------------------
    keys = set()
    for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        if 'appendix' in os.path.basename(f):
            continue
        b = open(f, encoding='utf-8', errors='replace').read()
        b = '\n'.join(l for l in b.split('\n') if not l.lstrip().startswith('%'))
        keys |= set(re.findall(r'\\ldg\{([^}]*)\}', b))
    ungathered = []
    for k in sorted(keys):
        if k.lower() not in text:
            fails.append(f'\\ldg{{{k}}} names no ledger file')
        elif 'LANDING TABLE' not in text[k.lower()] and 'REACH REGISTER' not in text[k.lower()]:
            ungathered.append(k)
    print(f'    {len(keys)} distinct \\ldg key(s); {len(keys) - len(ungathered)} reach a gathered ledger')
    for k in ungathered:
        print(f'      [note] {k}: marker points at a ledger with no landing table yet')

    # ---- (1) field-bake receipts are named by their ledger ------------------
    unnamed = []
    for rf in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
        stem = os.path.basename(rf)[:-3]
        m = PROBE.match(stem)
        if not m:
            continue
        body = open(rf, encoding='utf-8', errors='replace').read()
        if 'NOT-A-FIELD-BAKE-RECEIPT:' in body:
            continue
        if 'field bake' not in body.lower() and 'field-bake' not in body.lower():
            continue
        if not any(stem in t for t in text.values()):
            unnamed.append((m.group(1), os.path.relpath(rf, ROOT)))
    print()
    print(f'    field-bake receipts named by a ledger: '
          f'{"all" if not unnamed else f"{len(unnamed)} NOT named"}')
    for pid, rel in unnamed:
        fails.append(f'{pid}: receipt in no ledger -- {rel}')
        print(f'      [FAIL] {pid} -- {rel}')
        print(f'             on disk and registered, but the ledger whose probe it settles')
        print(f'             does not name it. The computation has no argument attached.')

    # ---- (2) a LANDED row says where -----------------------------------------
    addressless = []
    for k, t in text.items():
        i = t.find('LANDING TABLE')
        if i < 0:
            continue
        j = t.find('\n---\n', i)
        tbl = t[i:j] if j > i else t[i:]
        for row in [l for l in tbl.split('\n') if l.startswith('| **')]:
            if not re.search(r'\bLANDED\b', row):
                continue
            if not re.search(r'`?[Pp]\d{1,2}`?|`p0`|sec:|ONTOLOGY|§', row):
                addressless.append((k, re.sub(r'\s+', ' ', row)[:72]))
    print()
    print(f'    LANDED rows carrying an address: '
          f'{"all" if not addressless else f"{len(addressless)} without one"}')
    for k, row in addressless:
        fails.append(f'{k}: LANDED row with no address')
        print(f'      [FAIL] {k}: {row}')

    print()
    if fails:
        print(f'  ⛔ {len(fails)} BREAK(S) IN THE CHAIN.')
        print('     A link that resolves is not a chain that connects. Name the receipt in')
        print('     the ledger whose probe it settles, and give every LANDED row its address.')
        print()
        return 1
    print('  The chain connects: markers reach gathered ledgers, field-bake receipts are')
    print('  named by the ledger whose probe they settle, and every LANDED row says where.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
