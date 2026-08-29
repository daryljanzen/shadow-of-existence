#!/usr/bin/env python3
"""check_appendix_current.py -- IS EVERY GENERATED APPENDIX ACTUALLY THE ONE ITS INDEX GENERATES?

** WHY.  `make_receipt_appendix`'s own first line says: ** *"Single source of truth: the paper's
appendix can never drift from the ledger, ** because it is regenerated **."*  *** Nothing checked
that it HAD been. ***

** ⛭⛭ AND THE ONE INSTRUMENT THAT LOOKS NEARBY CANNOT SEE THIS. **  `check_compile` fails on a DEAD
LINK -- a `\\rcpt{}` in a paper body with no appendix entry to point at.  That catches a stale
appendix only when the new row is also CITED.
  ⇒ *** A row added to the INDEX and not yet cited produces no dead link, so the appendix simply
      lags, silently, for as long as nobody runs the generator by hand. ***  At c54.222 the last
      regeneration was r2727 and the INDEX had moved 49 revisions past it: `P10` was 30 lines short,
      `P14` 55, `P15` 80, and the corpus appendix 290.  ** That is r2376+c54.36's 105 dead links
      arriving again by the one route c54.36's fix does not cover. **

** ⌗ THE ONE DESIGN CHOICE, STATED.  This gate regenerates into a TEMPORARY directory and compares
bytes; it never writes into `corpus/`. **  *A gate that repaired what it measures would report green
on a tree nobody had looked at -- which is the stale-cache failure r2656+c54.208 found in the receipt
runner, and it is not worth reintroducing to save one command.*

Written c54.222 (`L-556`).  Stated for reversal.

================================================================================================
⛭⛭⛭ WIDENED TO BOTH RAILS, AND MADE UNABLE TO PASS VACUOUSLY -- r3538 (node 60), to 59's spec.
================================================================================================

** ① IT GATED ONE RAIL OF TWO. **  `TARGETS` was eighteen receipt appendices, hardcoded.  The `\\ldg`
rail landed at r3523 with its own generator (`make_ledger_appendix.py`), its own index
(`ledgers/INDEX.md`) and its own artefact (`corpus/appendix_ledgers_*.tex`), and NOTHING gated it --
so the rail built expressly to close the receipt generator's three scars could drift in exactly the
way this file exists to prevent.  *`make_all_appendices.py` does not regenerate it either, which
means the fix line this gate prints would not have fixed the L rail even had the gate noticed.*
Both rails are now declared in one table, and the fix line names both commands.

** ② AND A GATE THAT SKIPS WHAT IT CANNOT FIND REPORTS GREEN OVER NOTHING. **  The old loop read

        if not os.path.exists(live): continue

and `checked` counted only what it got to.  Delete every appendix and this printed *"0 appendices
regenerated and compared"* followed by *"every appendix matches what the INDEX generates"* -- and
returned 0.  ** That is the r3522 dependency-matrix failure exactly: it had been printing "every row
matches" over ZERO parsed rows for its whole life. **  A comparison count is not a verdict, and a
gate must be able to say how much it looked at.  So there are now FOUR anti-vacuity clauses, each
naming the way it can fail:

    (a) THE SOURCE IS PARSED INDEPENDENTLY, not taken from the generator.  This file counts the rows
        in each index itself.  A rail whose index parses to ZERO rows FAILS, and a rail below its
        declared floor FAILS -- the floors are a ratchet and may only be RAISED.  *A generator and
        its gate that share a parser share its blind spots; that is how the prefix row-filter ate
        receipts three times.*
    (b) A DECLARED APPENDIX THAT IS NOT ON DISK IS A FAILURE, not a skip.  The file count per rail
        has its own floor for the same reason.
    (c) EVERY REGENERATED OUTPUT MUST CARRY AT LEAST ONE `\\item[`.  Two empty files compare EQUAL:
        without this clause a generator that silently emitted nothing would pass against a live
        appendix that had also been emptied, and the byte-comparison would certify it.
    (d) ANY `corpus/appendix_*.tex` CLAIMED BY NO RAIL IS A FAILURE.  ** This is the defect in ①
        turned into a check, so the third rail cannot arrive ungated the way the second did. **
"""
import os
import glob
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ── THE RAILS.  name, generator, source index, filename glob, and how a filename maps to a scope.
#    The floors are a RATCHET: raise them when a rail grows, never lower them to make a run pass.
RECEIPT_SCOPES = {f"appendix_receipts_P{n:02d}.tex" if n < 10 else f"appendix_receipts_P{n}.tex":
                  f"P{n}" for n in range(1, 18)}
RECEIPT_SCOPES['appendix_receipts_corpus.tex'] = 'corpus'


def _ledger_scope(name):
    """appendix_ledgers_P17.tex -> P17 ; appendix_ledgers_corpus.tex -> corpus"""
    return name[len('appendix_ledgers_'):-len('.tex')]


RAILS = [
    dict(name='receipts  (\\rcpt)', gen='make_receipt_appendix.py',
         index=os.path.join(ROOT, 'receipts', 'INDEX.md'),
         pattern='appendix_receipts_*.tex', scope=RECEIPT_SCOPES.get,
         min_rows=600, min_files=18, fix='python3 corpus/make_all_appendices.py'),
    dict(name='ledgers   (\\ldg)', gen='make_ledger_appendix.py',
         # ⛭⛭ REPOINTED r3558: 59's r3551 moved the registry out of a directory it had no
         #   business creating -- `ledgers/INDEX.md` -> `corpus/ledgers_registry.md`.
         #   ** Clause (a) caught it on a REAL move rather than a mutation test: the gate said
         #   "its index IS NOT ON DISK -- nothing to compare against, and a comparison count of
         #   zero is not a pass". Without that clause the rail would simply have stopped being
         #   compared, and the gate would have reported green over one rail instead of two. **
         index=os.path.join(ROOT, 'corpus', 'ledgers_registry.md'),
         pattern='appendix_ledgers_*.tex', scope=_ledger_scope,
         # ⛭ r3554: RAISED 1 -> 2. 59's r3550 put the rail to work -- P3 now carries seven
         #   \ldg markers and its own Appendix L -- so the rail has two artefacts and a drop
         #   back to one is now a regression this floor can see. ** That is what a ratchet is
         #   for, and it only works if it is raised when the rail grows. **
         # ⛭ THE RATCHET, RAISED THREE TIMES IN ONE DAY AS THE RAIL GREW: 1 -> 2 (r3554,
         #   P3 got its Appendix L) -> 3 (r3558, p0 and P14) -> 14 (r3562, the marker pass
         #   completed at 45 markers across 14 papers). ** A floor that is not raised when
         #   the rail grows stops being a ratchet and becomes a comment: at min_files=3 this
         #   rail could have silently lost ELEVEN appendices and still passed. **
         min_rows=15, min_files=14,
         fix='python3 corpus/make_ledger_appendix.py P17 corpus/appendix_ledgers_P17.tex'),
]


def count_index_rows(path):
    """** PARSED HERE, not by the generator. **  Every pipe-row of the table that is neither the
    header nor the separator.  Deliberately has no predicate on a row's CONTENT: a prefix filter
    is what silently ate receipts at c54.36, c54.203 and c54.222, three times, each time from a
    row whose first cell was spelt in a way the filter had not met."""
    if not os.path.exists(path):
        return None
    lines = [ln.strip() for ln in open(path, encoding='utf-8', errors='replace')]
    pipe = [i for i, s in enumerate(lines) if s.startswith('|')]

    def is_sep(i):
        body = lines[i].strip('|').replace(' ', '')
        return bool(body) and set(body) <= set('-:|')

    # ⚠ THE HEADER IS FOUND STRUCTURALLY, and the first draft of this function did NOT do that.
    #   It tested `body.startswith('file|') or body.startswith('paper|')` -- a predicate on the
    #   header's SPELLING, in a function whose own docstring says a predicate on a row's spelling
    #   is what ate receipts three times.  ledgers/INDEX.md heads its table `| key | ledger file |`
    #   and the test missed it, counting 19 rows for 18 ledgers.  ** A header is the row directly
    #   above the separator; that is a fact about the table and not about anyone's wording. **
    seps = {i for i in pipe if is_sep(i)}
    headers = {i for i in pipe if i + 1 in seps}
    return sum(1 for i in pipe if i not in seps and i not in headers)


def main():
    print()
    print('  check_appendix_current -- is each generated appendix the one its INDEX generates now?')
    print()
    fails, tmp = [], tempfile.mkdtemp(prefix='appx.')
    claimed, fixes = set(), []
    try:
        for rail in RAILS:
            gen = os.path.join(HERE, rail['gen'])
            rows = count_index_rows(rail['index'])
            live = sorted(glob.glob(os.path.join(HERE, rail['pattern'])))
            claimed.update(os.path.basename(p) for p in live)

            # (a) the source, parsed here.
            src = os.path.relpath(rail['index'], ROOT)
            if rows is None:
                fails.append(f"{rail['name']}: its index {src} IS NOT ON DISK -- "
                             f"nothing to compare against, and a comparison count of zero is not a pass")
                continue
            if rows == 0:
                fails.append(f"{rail['name']}: {src} parses to ZERO rows. ** A gate that compares "
                             f"nothing must not report that everything matches. **")
                continue
            if rows < rail['min_rows']:
                fails.append(f"{rail['name']}: {src} parses to {rows} row(s), below the declared "
                             f"floor of {rail['min_rows']} -- either the index lost rows or the "
                             f"floor is a ratchet someone lowered")

            # (b) the artefacts, and there must be enough of them.
            if len(live) < rail['min_files']:
                fails.append(f"{rail['name']}: {len(live)} appendix file(s) on disk, below the "
                             f"declared floor of {rail['min_files']} -- a missing appendix is a "
                             f"FAILURE here and not a skip")

            checked, stale = 0, []
            for path in live:
                name = os.path.basename(path)
                scope = rail['scope'](name)
                if not scope:
                    fails.append(f"{rail['name']}: {name} matches the rail but maps to no scope")
                    continue
                out = os.path.join(tmp, name)
                p = subprocess.run([sys.executable, gen, scope, out], cwd=HERE,
                                   capture_output=True, text=True, errors='replace')
                if p.returncode or not os.path.exists(out):
                    fails.append(f"{name} -- the generator could not produce it: "
                                 f"{(p.stderr or p.stdout).strip()[-200:]}")
                    continue
                b = open(out, 'rb').read()
                # (c) an empty appendix compares EQUAL to an empty appendix.
                if b.count(b'\\item[') == 0:
                    fails.append(f"{name} -- regenerates to ZERO entries. ** Two empty files "
                                 f"compare equal, so this would otherwise pass. **")
                    continue
                checked += 1
                a = open(path, 'rb').read()
                if a != b:
                    da = len(b.split(b'\n')) - len(a.split(b'\n'))
                    stale.append((name, f'{da:+d} line(s)' if da else
                                  'same length, different bytes'))
            if stale:
                for name, d in stale:
                    fails.append(f"{name} is STALE -- its index would write {d}")
                fixes.append(rail['fix'])
            print(f"    {rail['name']:<20} {rows:>4} index row(s), {checked:>2} appendix/appendices "
                  f"regenerated and compared")

        # (d) a rail nobody declared is a rail nobody gates.
        for path in sorted(glob.glob(os.path.join(HERE, 'appendix_*.tex'))):
            name = os.path.basename(path)
            if name not in claimed:
                fails.append(f"{name} is an appendix NO RAIL CLAIMS -- ** it is generated by "
                             f"something, and nothing here checks that it was. ** Declare it in "
                             f"RAILS or say in its head that it is hand-written")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if fails:
        print()
        for m in fails:
            print(f'    [FAIL] {m}')
        print()
        print('    ⛭ ** A generated file that is not regenerated is a hand-maintained one that')
        print('       nobody is maintaining. **  *** And an appendix short of its index does not')
        print('       LOOK wrong -- it looks like a shorter appendix. ***')
        for f in dict.fromkeys(fixes):
            print(f'       Fix:  {f}')
        print()
        print('    ⚠ AND WHEN THE TWO SIDES DISAGREE, RUNNING THE FIX IS NOT AUTOMATICALLY RIGHT.')
        print('      At r3536 every one of 27 differing lines had the GENERATED side correct and')
        print('      the INDEX stale -- because the appendices sit in corpus/ and every corpus-wide')
        print('      sweep edits them while none reaches receipts/INDEX.md. Regenerating would have')
        print('      reinstated the deck/monodromy defect r3528-r3530 removed. ** This gate reports')
        print('      that the rails DIVERGE; it cannot tell you which side is right. Read the diff')
        print('      against the papers before you run the fix. **')
        print()
        return 1
    print()
    print('    every appendix on both rails matches what its index generates.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
