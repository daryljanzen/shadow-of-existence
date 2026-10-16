#!/usr/bin/env python3
"""check_formalisation_join.py -- EVERY `DONE` ROW'S DECLARATION IS STILL DECLARED, ITS FILE IS STILL UNDER A
GATE, AND ITS RECEIPT STILL EXISTS.

** WHAT THE JOIN IS. **  `computations/formalisation/r7325_71_inventory/ROWS.tsv` carries the formalisation
inventory.  Node `71` adds two columns to it -- `receipt` (a path) and `decl` (a fully qualified Lean name,
and the file it is in) -- so a row can say *this claim is formalised, there, under that name*.

*** THE DEFECT THIS GATE EXISTS FOR.  Nothing in the corpus checks that a `.lean` file named in a cell still
declares the identifier named beside it.  A declaration renamed in a refactor leaves the cell asserting a
theorem under a name that no longer exists, and the cell goes on reading as though it were true. ***  That is
`r7411`'s rule -- a copy of a list is a claim about the list at the moment it was copied -- applied to a prose
cell instead of a lint line.

  ⌗ ** WHY THIS SEAT AND NOT `71`. **  *A seat should not write the gate that checks its own cells.*  `71`
  supplies, this seat checks, `66` publishes.  Ordered at `r7419` ① on `69`'s proposal.

** WHAT IT CHECKS, AND THERE ARE THREE CONDITIONS, ALL FROM THE ORDER. **
  ⓵ ** a `DONE` row's `decl` is DECLARED in the named file ** -- otherwise the cell is a dangling reference;
  ⓶ ** the named file is under a green `formalisation-*` workflow ** -- decided from each workflow's own
    `paths:` scope rather than from a filename convention, because a file under no workflow is a row that
    nothing could ever clear;
  ⓷ ** the `receipt` path EXISTS. **

⛔⛭⛭⛭ ** AND THE FIRST THING IT CHECKS IS THAT IT CAN SEE ANYTHING AT ALL, BECAUSE THE ORDER NAMED THAT TRAP
AND IT IS THIS CYCLE'S OWN DEFECT. **  *`r7419` ③, carrying `cc66`'s shape -- an instrument given less state
than its question needs will still answer:* **"A gate over `decl` cells that cannot see a Lean file's
declarations will not say so; it will pass."**
  ⌈ ⇒ *** So this gate REFUSES to report a clean join on a tree it could not read. ***  A positive control
    runs first: the reader must find declarations in the tree, and a file named by a row must parse to a
    non-empty declaration set before any row against it is called clean.  **Where it cannot read, it FAILS
    and says which file, and that is distinct from finding no dangling reference.**
  ⌊ *This is `r7422`'s finding one place over: an instrument that cannot distinguish its own silence from its
    own verdict.  `0` rows checkable and `0` dangling references found are different sentences, and this gate
    prints whichever is true rather than the one that reads better.*

    python3 corpus/check_formalisation_join.py
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ROWS = os.path.join('computations', 'formalisation', 'r7325_71_inventory', 'ROWS.tsv')
WF_DIR = os.path.join('.github', 'workflows')
LEAN_ROOT = os.path.join('computations', 'formalisation')

FAILED = []
NOTES = []


def fail(msg):
    FAILED.append(msg)
    print(f'    [FAIL] {msg}')


def note(msg):
    NOTES.append(msg)
    print(f'    ⌗ {msg}')


# ── the Lean reader ────────────────────────────────────────────────────────────────────────────────
#   Declaration HEADS, read from text.  ⚠ Not a parser: a declaration introduced by a macro or a
#   notation command is missed, which is why the reader is used as a CONTROL (it must find something)
#   and never as a census of what a file declares.
_DECL = re.compile(
    r'^\s*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+|noncomputable\s+|partial\s+|unsafe\s+|scoped\s+)*'
    r'(?:theorem|lemma|def|abbrev|instance|structure|inductive|class|axiom|opaque)\s+'
    r'([A-Za-z_À-ɏ][\wÀ-ɏ.\'!?]*)', re.M)
_NS = re.compile(r'^\s*namespace\s+([\w.\']+)', re.M)
_END = re.compile(r'^\s*end\s+([\w.\']+)\s*$', re.M)


def declarations(path):
    """every identifier the file declares, bare and namespace-qualified.  Returns None when the file
    cannot be read at all -- which is NOT the same as a file that declares nothing."""
    try:
        src = open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return None
    out, stack = set(), []
    for line in src.split('\n'):
        m = _NS.match(line)
        if m:
            stack.append(m.group(1))
            continue
        m = _END.match(line)
        if m and stack and stack[-1] == m.group(1):
            stack.pop()
            continue
        m = _DECL.match(line)
        if m:
            name = m.group(1)
            out.add(name)
            if stack:
                out.add('.'.join(stack + [name]))
    return out


def lean_files():
    out = []
    for d, _subdirs, fs in os.walk(os.path.join(ROOT, LEAN_ROOT)):
        for f in fs:
            if f.endswith('.lean'):
                out.append(os.path.relpath(os.path.join(d, f), ROOT))
    return sorted(out)


# ── the workflow scopes, read from the workflows' own `paths:` ─────────────────────────────────────
def workflow_scopes():
    """{workflow file: [path globs it declares]} for every `formalisation-*` workflow."""
    out = {}
    wd = os.path.join(ROOT, WF_DIR)
    if not os.path.isdir(wd):
        return out
    for f in sorted(os.listdir(wd)):
        if not (f.startswith('formalisation-') and f.endswith(('.yml', '.yaml'))):
            continue
        txt = open(os.path.join(wd, f), encoding='utf-8', errors='replace').read()
        globs = re.findall(r"^\s*-\s*'([^']+/\*\*[^']*)'", txt, re.M)
        globs += re.findall(r'^\s*-\s*"([^"]+/\*\*[^"]*)"', txt, re.M)
        out[f] = sorted(set(globs))
    return out


def covered_by(rel, scopes):
    """the workflows whose declared paths cover this file."""
    hit = []
    for wf, globs in scopes.items():
        for g in globs:
            prefix = g.split('**')[0]
            if rel.startswith(prefix):
                hit.append(wf)
                break
    return sorted(set(hit))


def read_rows():
    """(header, rows) or (None, None) when the inventory is not there."""
    p = os.path.join(ROOT, ROWS)
    if not os.path.exists(p):
        return None, None
    lines = [l.rstrip('\n') for l in open(p, encoding='utf-8', errors='replace') if l.strip()]
    if not lines:
        return None, None
    head = lines[0].split('\t')
    return head, [dict(zip(head, l.split('\t'))) for l in lines[1:]]


def main():
    print('=' * 100)
    print('  FORMALISATION JOIN -- is every DONE row\'s declaration still declared, its file still gated,')
    print('  and its receipt still there?')
    print('=' * 100)

    # ── ⓪ THE POSITIVE CONTROL, FIRST.  An instrument that cannot see its data must not answer. ──
    files = lean_files()
    seen = {f: declarations(os.path.join(ROOT, f)) for f in files}
    unreadable = sorted(f for f, d in seen.items() if d is None)
    total = len({n for d in seen.values() if d for n in d})
    print(f'\n  ⓪ THE POSITIVE CONTROL -- can this gate read declarations at all?')
    print(f'      `.lean` files found: {len(files)}')
    print(f'      distinct identifiers the reader extracts: {total}')
    for f in unreadable:
        fail(f'⓪ a `.lean` file in the tree CANNOT BE READ, so nothing about it can be cleared: {f}')
    if files and total == 0:
        fail('⓪ ⛔ THE READER FOUND NO DECLARATIONS IN ANY OF THE '
             f'{len(files)} FILES -- so this gate cannot see its own subject, and it says so rather '
             f'than reporting a clean join (r7419 ③, cc66\'s shape)')
    elif not files:
        fail('⓪ ⛔ NO `.lean` FILE EXISTS UNDER THE FORMALISATION TREE -- a gate over `decl` cells with '
             'no tree to read would pass vacuously, so it fails instead')
    else:
        print(f'    ✔ the reader sees {total} identifier(s), so a verdict about a `decl` cell is a '
              f'reading and not a silence')

    # ── ⓶ the workflow scopes ────────────────────────────────────────────────────────────────────
    scopes = workflow_scopes()
    print(f'\n  ⓶ THE WORKFLOW SCOPES -- read from each workflow\'s own `paths:`')
    for wf, globs in scopes.items():
        print(f'      {wf}: {globs}')
    if not scopes:
        fail('⓶ no `formalisation-*` workflow declares any path, so "under a green workflow" cannot be '
             'decided and no row could be cleared on it')
    ungated = [f for f in files if not covered_by(f, scopes)]
    print(f'      `.lean` files under at least one workflow: {len(files) - len(ungated)} of {len(files)}')
    for f in ungated:
        note(f'⓶ under NO `formalisation-*` workflow, so a row naming it could never be cleared: {f}')

    # ── the rows ─────────────────────────────────────────────────────────────────────────────────
    head, rows = read_rows()
    print(f'\n  THE INVENTORY')
    if head is None:
        fail(f'the inventory is not readable at {ROWS}, so the join cannot be checked')
        return _verdict(0, 0)
    print(f'      columns: {head}')
    have_decl, have_receipt = 'decl' in head, 'receipt' in head
    done = [r for r in rows if (r.get('status') or '').strip().upper() == 'DONE']
    print(f'      rows: {len(rows)};  `DONE` rows: {len(done)}')

    if not (have_decl and have_receipt):
        # ⛔ THE VACUITY STATE, NAMED.  This is not "no dangling reference found".
        missing = [c for c in ('receipt', 'decl') if c not in head]
        print(f'\n  ⛔⛭ ** NOT YET CHECKABLE, AND THAT IS A DIFFERENT SENTENCE FROM A CLEAN JOIN. **')
        print(f'      the inventory does not carry {missing} yet, so of {len(done)} `DONE` row(s), '
              f'** 0 are checkable **.')
        print(f'      *`71` supplies those columns; this gate is in place and will fire on the first '
              f'row that carries them.*  ⇒ ** 0 CHECKABLE is reported as 0 CHECKABLE, never as 0 '
              f'dangling references. **')
        return _verdict(0, len(done))

    checked = 0
    for r in done:
        idx = (r.get('index') or '?').strip()
        decl = (r.get('decl') or '').strip()
        rcpt = (r.get('receipt') or '').strip()
        if not decl and not rcpt:
            note(f'a `DONE` row carries neither cell yet, so it is not checkable: row {idx}')
            continue
        checked += 1
        # ⓷ the receipt path
        if not rcpt:
            fail(f'⓷ `DONE` row {idx} names a `decl` but no `receipt`')
        elif not os.path.exists(os.path.join(ROOT, rcpt)):
            fail(f'⓷ `DONE` row {idx}\'s `receipt` path does not exist: {rcpt}')
        # ⓵ the declaration, and ⓶ its file's gating
        if not decl:
            fail(f'⓵ `DONE` row {idx} names a `receipt` but no `decl`')
            continue
        f_rel, name = _split_decl(decl)
        if f_rel is None:
            fail(f'⓵ `DONE` row {idx}\'s `decl` names no `.lean` file, so the declaration has nowhere '
                 f'to be looked for: {decl!r}')
            continue
        f_abs = os.path.join(ROOT, f_rel)
        decls = declarations(f_abs) if os.path.exists(f_abs) else None
        if decls is None:
            fail(f'⓵ `DONE` row {idx}\'s file CANNOT BE READ, so its `decl` is UNVERIFIABLE rather '
                 f'than present: {f_rel}')
            continue
        if not decls:
            fail(f'⓵ `DONE` row {idx}\'s file parses to NO declarations, so a clean verdict on it '
                 f'would be a silence: {f_rel}')
            continue
        if name not in decls:
            fail(f'⓵ DANGLING REFERENCE -- `DONE` row {idx} names `{name}`, and {f_rel} declares '
                 f'{len(decls)} identifier(s), none of them that one')
        wf = covered_by(f_rel, scopes)
        if not wf:
            fail(f'⓶ `DONE` row {idx}\'s file is under NO `formalisation-*` workflow: {f_rel}')
    return _verdict(checked, len(done))


def _split_decl(cell):
    """(file, identifier) from a cell naming both.  The file is the `.lean` path in the cell; the
    identifier is the longest dotted token that is not the path."""
    m = re.search(r'([\w./\-]+\.lean)', cell)
    if not m:
        return None, cell.strip()
    path = m.group(1)
    rest = (cell[:m.start()] + ' ' + cell[m.end():]).replace(',', ' ').replace(':', ' ')
    toks = [t for t in rest.split() if re.fullmatch(r"[A-Za-z_][\w.']*", t or '')]
    name = max(toks, key=len) if toks else ''
    if not path.startswith('computations/'):
        for c in (os.path.join(LEAN_ROOT, path), os.path.join(LEAN_ROOT, 'lean', path)):
            if os.path.exists(os.path.join(ROOT, c)):
                path = c
                break
    return path, name


def _verdict(checked, done):
    print('\n' + '=' * 100)
    if FAILED:
        print(f'  ⛔ THE FORMALISATION JOIN GATE IS RED: {len(FAILED)} failure(s)')
        for x in FAILED:
            print(f'      - {x[:140]}')
        print('=' * 100)
        return 1
    if checked == 0:
        print(f'  ⌗ NOTHING IS CHECKABLE YET: {done} `DONE` row(s), 0 of them carrying both cells.')
        print(f'    ** That is reported as 0 CHECKABLE and not as a clean join. **  The reader sees the '
              f'tree, so the gate is live and will fire on the first row that carries them.')
    else:
        print(f'  ✔ the join holds: {checked} of {done} `DONE` row(s) checked, every `decl` declared in '
              f'its named file, every file under a `formalisation-*` workflow, every `receipt` present.')
    if NOTES:
        print(f'  ⌗ {len(NOTES)} note(s) above are reported and not charged.')
    print('=' * 100)
    return 0


# ── the gate's own seeds: the control the order asked for, kept rather than run once ───────────────
def seed():
    """⛭⛭⛭ `r7419` ③'s standing test, on constructed rows: ** run the gate against the remedy its own
    rule prescribes before landing it. **

    *Three cases, and the third is the one a gate written from the happy path gets wrong:* a `decl` that
    IS declared passes; one that is NOT fails as a dangling reference; and a Lean file that **cannot be
    read at all** fails AS UNREADABLE rather than passing.  ⌗ *Plus the vacuity case the inventory is in
    today: no columns at all must report `0` CHECKABLE and never a clean join.*"""
    import json          # noqa: F401  (kept for parity with the other seeded gates)
    import shutil
    import tempfile
    res = {}
    tmp = tempfile.mkdtemp(prefix='r7424_seed_')
    try:
        lean_d = os.path.join(tmp, LEAN_ROOT, 'lean')
        os.makedirs(lean_d, exist_ok=True)
        good = os.path.join(LEAN_ROOT, 'lean', 'Seed.lean')
        with open(os.path.join(tmp, good), 'w', encoding='utf-8') as fh:
            fh.write('namespace Seeded\n\ntheorem present_one : True := trivial\n\nend Seeded\n')
        d = declarations(os.path.join(tmp, good))
        res['S1. the reader finds a bare declaration'] = d is not None and 'present_one' in d
        res['S2. ...and its namespace-qualified form'] = d is not None and 'Seeded.present_one' in d
        res['S3. a declaration NOT in the file is absent from the reader\'s set'] = \
            d is not None and 'renamed_away' not in d

        # a file that cannot be read at all: a directory standing where the .lean should be
        unread = os.path.join(tmp, LEAN_ROOT, 'lean', 'Unreadable.lean')
        os.makedirs(unread, exist_ok=True)
        res['S4. a file that CANNOT BE READ returns None, which is not an empty set'] = \
            declarations(unread) is None
        res['S5. ...and None is distinguishable from a file that declares nothing'] = \
            declarations(unread) is None and declarations(os.path.join(tmp, good)) != None  # noqa: E711

        # the workflow scope reader
        wf_d = os.path.join(tmp, WF_DIR)
        os.makedirs(wf_d, exist_ok=True)
        with open(os.path.join(wf_d, 'formalisation-seed.yml'), 'w', encoding='utf-8') as fh:
            fh.write("on:\n  push:\n    paths:\n      - 'computations/formalisation/lean/**'\n")
        _root = globals()['ROOT']
        try:
            globals()['ROOT'] = tmp
            sc = workflow_scopes()
            res['S6. a `formalisation-*` workflow\'s own `paths:` is read'] = \
                sc.get('formalisation-seed.yml') == ['computations/formalisation/lean/**']
            res['S7. a file inside that scope reads as covered'] = bool(covered_by(good, sc))
            res['S8. a file outside it does not'] = not covered_by('receipts/x.py', sc)
            res['S9. and with NO workflow at all, nothing reads as covered'] = \
                not covered_by(good, {})
        finally:
            globals()['ROOT'] = _root
        # ── and the WHOLE GATE, against a constructed inventory.  ⛔ The seeds above test the
        #    READER; `r7419` ③ asked for the GATE run against the condition its rule needs, and a
        #    reader that works is not a gate that fires.  These build an inventory with the columns
        #    and run `main()` on it.
        inv_d = os.path.join(tmp, os.path.dirname(ROWS))
        os.makedirs(inv_d, exist_ok=True)
        rcpt = os.path.join(tmp, 'receipts', 'seed_receipt.py')
        os.makedirs(os.path.dirname(rcpt), exist_ok=True)
        open(rcpt, 'w').write('# seed\n')

        def run_on(rows_body):
            FAILED.clear()
            NOTES.clear()
            with open(os.path.join(tmp, ROWS), 'w', encoding='utf-8') as fh:
                fh.write('index\tclass\tstatus\treceipt\tdecl\n' + rows_body)
            _r = globals()['ROOT']
            try:
                globals()['ROOT'] = tmp
                import io as _io
                import contextlib as _cl
                buf = _io.StringIO()
                with _cl.redirect_stdout(buf):
                    rc = main()
                return rc, list(FAILED), buf.getvalue()
            finally:
                globals()['ROOT'] = _r
                FAILED.clear()
                NOTES.clear()

        rc_ok, f_ok, _ = run_on(f'1\tG\tDONE\treceipts/seed_receipt.py\t{good} Seeded.present_one\n')
        res['S10. a DONE row whose `decl` IS declared passes the WHOLE gate'] = rc_ok == 0 and not f_ok

        rc_d, f_d, _ = run_on(f'2\tG\tDONE\treceipts/seed_receipt.py\t{good} Seeded.renamed_away\n')
        res['S11. a DANGLING `decl` fails the whole gate, named as dangling'] = \
            rc_d == 1 and any('DANGLING' in x for x in f_d)

        _unread_rel = os.path.join(LEAN_ROOT, 'lean', 'Unreadable.lean')
        rc_u, f_u, _ = run_on(f'3\tG\tDONE\treceipts/seed_receipt.py\t{_unread_rel} Seeded.x\n')
        res['S12. an UNREADABLE Lean file fails AS UNVERIFIABLE, not as clean'] = \
            rc_u == 1 and any('CANNOT BE READ' in x for x in f_u)

        rc_m, f_m, _ = run_on('4\tG\tDONE\t\t\n')
        res['S13. a DONE row carrying neither cell is not charged and not cleared'] = rc_m == 0

        rc_r, f_r, _ = run_on(f'5\tG\tDONE\treceipts/gone.py\t{good} Seeded.present_one\n')
        res['S14. a `receipt` path that does not exist fails'] = \
            rc_r == 1 and any('receipt' in x and 'does not exist' in x for x in f_r)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    [{"ok" if v else "FAIL"}]  {k}')
    ok = all(res.values())
    print(f'\n  the reader tells a present declaration from an absent one, and an UNREADABLE file from '
          f'an empty one: {ok}')
    return 0 if ok else 1


if __name__ == '__main__':
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(main())
