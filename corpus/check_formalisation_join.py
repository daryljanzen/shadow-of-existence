#!/usr/bin/env python3
"""check_formalisation_join.py -- EVERY PAIR A `decl` CELL CLAIMS IS STILL DECLARED IN THE FILE IT NAMES, THAT
FILE IS STILL UNDER A WORKFLOW WHOSE RECORD SAYS GREEN, AND EVERY `receipt` PATH STILL EXISTS.

** WHAT THE JOIN IS. **  `computations/formalisation/r7325_71_inventory/ROWS.tsv` carries the formalisation
inventory.  Node `71`'s `receipt` and `decl` columns let a row say *this claim is formalised, there, under
those names* -- and nothing else in the corpus checks that the names are still there.  A declaration renamed
in a refactor leaves the cell asserting a theorem under a name that no longer exists, and the cell goes on
reading as though it were true.  That is `r7411`'s rule -- *a copy of a list is a claim about the list at the
moment it was copied* -- applied to a prose cell instead of a lint line.

  ⌗ ** WHY THIS SEAT AND NOT `71`. **  *A seat should not write the gate that checks its own cells.*  `71`
  supplies, this seat checks, `66` publishes.  Ordered at `r7419` ① on `69`'s proposal.

⛔⛭⛭⛭ ** AND THE FIRST VERSION OF THIS GATE WAS RED ON CORRECT DATA, WHICH IS WHY IT NOW OWNS NO READER OF
`71`'s FORMAT AT ALL. **  `r7424` carried its own cell parser, `_split_decl`: the first `.lean` path in the
cell and the longest dotted token anywhere in it.  A `decl` cell is a `|`-separated list of GROUPS, each a
file with its own name list, so that reading agrees on a one-group cell and MISPAIRS a multi-group one.
`r7423` measured the consequence over the whole population: the gate checked **one pair per row**, and every
one of its `7` dangling references was a later group's name asserted against the FIRST group's file.
  ⌈ ⇒ *** The cause is not a bug in a regex.  `r7419` ① asked for "the name OR NAMES and THE FILE" -- names
    plural, file singular -- so the order chose neither reading, and two instruments each invented one.
    `66`'s words: ** a format with no stated grammar is a key with no declared `K`. ** ***
  ⌊ *And the half that is mine is narrower: handed a cell I could not parse unambiguously, my parser PICKED
    A READING AND REPORTED A VERDICT, when the one honest output was that the cell had no stated grammar.*
    ⇒ *** A PARSER THAT GUESSES IS AN INSTRUMENT THAT CANNOT TELL ITS OWN SILENCE FROM ITS OWN VERDICT ***
    -- `PO-78`'s family arriving inside the gate I had built to catch it.  **⇒ A seat that does not own a
    format must not carry a private reader of it.**

** SO THE GRAMMAR AND THE CHECK BOTH COME FROM ONE PLACE: `scripts/decl_cells.py` (`71`, `r7423`). **  This
gate calls `parse_decl`, `parse_receipt`, `read_rows` and `check_pairs` and implements none of them, so the
gate, the published page and any audit cannot diverge by construction.  *What this file still owns is its own
`declarations()` -- not as a second verdict but as the POSITIVE CONTROL, which must answer a different
question (**can this instrument see any declaration at all**) precisely so that it can catch the shared
reader returning empty.*

** WHAT IT CHECKS -- THREE CONDITIONS, ALL FROM THE ORDER, OVER EVERY PAIR AND NEVER ONE PER ROW. **
  ⓵ ** every `(file, name)` pair a `decl` cell claims is DECLARED in that pair's own file **;
  ⓶ ** that file is under a `formalisation-*` workflow (⓶ᵃ, from the workflow's own `paths:`) whose RECORD
    says the workflow passed on this exact tree (⓶ᵇ, three-way) **;
  ⓷ ** every `receipt` path the row names EXISTS. **

⛔⛭ ** CONDITION ⓶ᵇ IS CARRIED THREE-WAY, AND `UNANSWERABLE` NEVER PASSES. **  *`70` measured at
`r7419+70.2` that "is this file under a GREEN workflow" is **not** answerable from the tree -- the
`formalisation-*` workflows are invisible to `READ_INDEX`, `0` of `1107` entries being a `.lean` path -- and
`r7423` ③ authorised the record that makes it local.*  So this gate reads `scripts/lean_record.py`, whose
answer is `GREEN`, `NOT-GREEN` or `UNANSWERABLE`, and **adopted at `r7423` ④ in `70`'s own words: a condition
the gate cannot evaluate must SAY SO, not succeed.**
  ⌈ ⇒ *** An `UNANSWERABLE` record FAILS this gate.  That is `r7417` ②'s reason applied to a condition rather
    than to a population, and it is the same rule as `r7421` ③'s, since an unanswerable condition is a gate
    that cannot tell its silence from its verdict. ***
  ⌈ ⇒ *And the CHARGE is made once per WORKFLOW and not once per pair.  Built per pair first, it emitted
    **263 all but identical failures for ONE unreachable ref** -- a condition that is a property of a
    workflow reported once per row being the same category error this revision repairs.  The STATE is
    per file (`green_state`); the charge is `record_charges`, which carries the population it covers.*
  ⌊ ⚠ *The cost, registered and not hidden: the condition reads a remote ref, so an unreachable network turns
    this gate red.  That is the correct trade under the ruling -- "I could not reach the record" is exactly
    unanswerable -- but it is a cost, and `r7425` ④ fixes its form: **a failure message must name an address
    the remedy can be written to**, so the `UNANSWERABLE` message carries `refs/ci/lean/<workflow>` and the
    command that writes it.*

⛭⛭⛭ ** AND IT PROVES IN ITS OWN RUN THAT IT COULD HAVE FIRED -- FOR BOTH CONDITIONS. **  `r7421` ③, promoted
as a standing rule: *a gate whose population can be empty must prove IN ITS OWN RUN that it could have fired*
(`70`: **"after it, a zero is a measured zero"**).  `r7424` put that control in a `--seed` mode, which is not
what the rule asks -- *a separate mode can be skipped, left unwired, or pass on a tree where the real run does
nothing* -- so `r7426` moved it in-run, and `r7428` ⑴ sharpens its target to the error class the data can
actually carry and my own parser manufactured (**a well-formed pair pointing at the WRONG FILE**), ⑵ makes it
fail in both directions, and ⑶ extends it to condition `⓶ᵇ`, whose non-green population is also empty today.

    python3 corpus/check_formalisation_join.py
    python3 corpus/check_formalisation_join.py --seed
"""
import contextlib
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import decl_cells as dc            # noqa: E402  -- 71's grammar AND check, r7423; this gate owns neither
import lean_record as lr           # noqa: E402  -- 70's three-way record reader, r7423 ③

ROWS_REL = os.path.join('computations', 'formalisation', 'r7325_71_inventory', 'ROWS.tsv')
WF_DIR = os.path.join('.github', 'workflows')
TREE = os.path.join('computations', 'formalisation')

GREEN, NOT_GREEN, UNANSWERABLE, UNSCOPED = 'GREEN', 'NOT-GREEN', 'UNANSWERABLE', 'UNSCOPED'

FAILED = []
NOTES = []


def fail(msg):
    FAILED.append(msg)
    print(f'    [FAIL] {msg}')


def note(msg):
    NOTES.append(msg)
    print(f'    ⌗ {msg}')


# ── the POSITIVE CONTROL's reader, and it is not the gate's verdict ────────────────────────────────
#   ⚠ Declaration HEADS read from text; a declaration introduced by a macro or a notation command is
#   missed.  It exists to answer *can this instrument see anything at all*, which the shared reader
#   cannot be asked about itself -- a reader returning an empty set would otherwise read as a file
#   that declares nothing.  ⌗ It also tracks `namespace` by MATCHING `end`, which is why it can
#   measure the shared reader's qualification strength in `Ⓠ` below without being a second verdict.
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
    for d, _subdirs, fs in os.walk(os.path.join(ROOT, TREE)):
        for f in fs:
            if f.endswith('.lean'):
                out.append(os.path.relpath(os.path.join(d, f), ROOT))
    return sorted(out)


# ── ⓶ᵃ the workflow scopes, read from the workflows' own `paths:` ──────────────────────────────────
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
            if rel.startswith(g.split('**')[0]):
                hit.append(wf)
                break
    return sorted(set(hit))


# ── ⓶ᵇ the RECORD, three-way, and `UNANSWERABLE` is a failure and not a pass ───────────────────────
def workflow_records(scopes):
    """{workflow stem: (GREEN | NOT-GREEN | UNANSWERABLE, why)} -- never two-way.

    ⛭ `r7423` ④, `70`'s ruling adopted.  The verdict comes from `scripts/lean_record.py`, which
    compares the workflow's own `push: paths:` object ids at this tree against the record's key -- so a
    record whose key no longer matches is STALE and reads `UNANSWERABLE`, never `GREEN`."""
    out = {}
    for wf in sorted(scopes):
        stem = wf[:-4] if wf.endswith('.yml') else wf.rsplit('.', 1)[0]
        if stem not in getattr(lr, 'WORKFLOWS', ()):
            out[stem] = (UNANSWERABLE,
                         f'`scripts/lean_record.py` keeps no record for this workflow, so whether it '
                         f'passed on this tree cannot be read here -- the remedy is written to '
                         f'refs/ci/lean/{stem} by its own workflow\'s record step')
            continue
        try:
            v, why = lr.status(stem)
        except Exception as e:                                    # noqa: BLE001
            v, why = UNANSWERABLE, f'the record could not be read ({type(e).__name__}: {e})'
        if v not in (GREEN, NOT_GREEN, UNANSWERABLE):
            v, why = UNANSWERABLE, f'the record reader returned {v!r}, which is not one of the three'
        if v == UNANSWERABLE:
            why = (f'{why}  ⇒ the remedy is written to refs/ci/lean/{stem}:  python3 '
                   f'scripts/lean_record.py --write {stem} --conclusion success --run <id> --event push')
        out[stem] = (v, why)
    return out


def green_state(rel, scopes, records):
    """(GREEN | NOT-GREEN | UNANSWERABLE | UNSCOPED, detail) for one `.lean` path -- the STATE, which is
    not the same thing as the charge.

    A file under two workflows must be green under BOTH, and a worse state decides.  A MEASURED bad
    state is reported ahead of an unmeasured one, because `NOT-GREEN` says more than `UNANSWERABLE`
    does -- but neither passes."""
    wfs = covered_by(rel, scopes)
    if not wfs:
        return UNSCOPED, 'inside no `formalisation-*` scope, so no run could ever clear it'
    seen = []
    for wf in wfs:
        stem = wf[:-4] if wf.endswith('.yml') else wf.rsplit('.', 1)[0]
        v, why = records.get(stem, (UNANSWERABLE, f'no record was read for {stem}'))
        seen.append((v, stem, why))
    for want in (NOT_GREEN, UNANSWERABLE):
        for v, stem, why in seen:
            if v == want:
                return v, f'{stem}: {why}'
    return GREEN, '; '.join(f'{st}: {w}' for _v, st, w in seen)


# ── ⛔⛭⛭ AND THE `⓶ᵇ` CHARGE IS MADE ONCE PER WORKFLOW, NOT ONCE PER PAIR ──────────────────────────
#   `r7428` built it per pair first and MEASURED the result by forcing the record unreachable: the
#   gate emitted **263 all but identical failures** for ONE unreachable ref.
#   ⇒ *** A condition that is a property of a WORKFLOW reported once per row is the same category error
#     this revision repairs -- a charge inherited into a population it is not about. ***  The state is
#   per file (`green_state`); the CHARGE is per workflow, and it carries the population it affects so
#   the single cause is named once and the blast radius is a count rather than 263 lines.
def record_charges(records, scopes, files_in_use):
    """[message, ...] -- one per workflow whose record does not say GREEN, with what it covers.

    ⛭ This is the ONE function `main` and the in-run seeds both call, so the seeded three-way cases
    cannot travel a different route from the real ones."""
    out = []
    # ⛔⛭⛭ IT ITERATES THE SCOPES AND NOT THE RECORDS, AND SEED `S32` IS WHY.
    #   Written first as `for stem, (v, why) in records.items()`, which means *every workflow I happen
    #   to hold a verdict for* -- so a workflow IN SCOPE with NO record read produced no charge at all
    #   and passed in silence.  ⇒ *** The population that owes a verdict is the SCOPES; the records are
    #   only the answers I happen to have, and iterating the answers makes a missing answer invisible.
    #   That is this family's defect inside the function written to repair a category error. ***
    for wf in sorted(scopes):
        stem = wf[:-4] if wf.endswith('.yml') else wf.rsplit('.', 1)[0]
        v, why = records.get(stem, (UNANSWERABLE,
                                    f'no record was read for `{stem}` at all, which is not the same as '
                                    f'a record that says it passed  ⇒ the remedy is written to '
                                    f'refs/ci/lean/{stem}'))
        if v == GREEN:
            continue
        hit = sorted(f for f in files_in_use if wf in covered_by(f, scopes))
        where = (f'{len(hit)} claimed `.lean` file(s) sit under it'
                 if hit else 'no claimed `.lean` file sits under it')
        if v == NOT_GREEN:
            out.append(f'⓶ᵇ NOT-GREEN -- `{stem}`\'s record says it did NOT pass on this tree, and '
                       f'{where}: {why}')
        else:
            out.append(f'⓶ᵇ UNANSWERABLE, WHICH IS NOT A PASS -- whether `{stem}` passed on this tree '
                       f'cannot be evaluated here, so this gate says so rather than succeeding '
                       f'(`r7423` ④, `70`\'s ruling), and {where}: {why}')
    return out


def read_rows(root=None):
    """(header, rows) or (None, None) -- from `71`'s reader, so the gate and the page agree on the
    POPULATION too.  ⛭ `r7428`: my own reader admitted one body line this one rejects (a trailing `#`
    convention comment carrying no tabs), so the two disagreed by one phantom row.  Harmless today and
    still two readers of one file disagreeing about its population, which is this revision's defect in
    miniature."""
    p = os.path.join(root or ROOT, ROWS_REL)
    if not os.path.exists(p):
        return None, None
    try:
        return dc.read_rows(p)
    except (OSError, IndexError):
        return None, None


# ── running the gate against a SEEDED TREE, which the shared module must be told about too ─────────
@contextlib.contextmanager
def rooted(root):
    """point BOTH this gate and `71`'s module at `root`.

    ⛔⛭ `r7428`: registered as the trap this revision was most likely to fall into, and it is this
    cycle's own recurring mistake in its fourth form.  *The shared module resolves a cell's path
    against **its own** `ROOT` and MEMOISES by relative path* -- so a seed that redirected the gate's
    root and not the module's would have read the real tree while reporting on a seeded one.  ⇒ **A
    control measuring the wrong tree proves nothing about the run**, so the cache is cleared on the way
    in and restored on the way out."""
    g = globals()
    old = (g['ROOT'], dc.ROOT, dc.LEAN_ROOT, dict(dc._cache))
    try:
        g['ROOT'] = root
        dc.ROOT = root
        dc.LEAN_ROOT = os.path.join(root, 'computations', 'formalisation', 'lean')
        dc._cache.clear()
        yield
    finally:
        g['ROOT'], dc.ROOT, dc.LEAN_ROOT = old[:3]
        dc._cache.clear()
        dc._cache.update(old[3])


def _no_file_why(rel, root):
    """⛔ `no-file` from the shared reader covers two findings and this gate must not collapse them:
    *a path with nothing at it* is a dangling path, and *a path with something unreadable at it* is
    UNVERIFIABLE.  This refines the MESSAGE and never the verdict."""
    for cand in (os.path.join(root, 'computations', 'formalisation', 'lean', rel),
                 os.path.join(root, rel)):
        if os.path.exists(cand):
            return (f'something is present at {os.path.relpath(cand, root)} but cannot be read as a '
                    f'file, so the pair is UNVERIFIABLE rather than absent')
    return 'no file is present at that path under the formalisation tree or the repository root'


def _asserts_done(r):
    """does this row ASSERT that the claim is formalised?  Read from the status string, not from a list.

    `71`'s grammar: an empty `decl` cell is no claim at all, and is the correct state for `ROW: A
    DIFFERENT KIND`, `LIBRARY GAP` and `GENERIC-METRIC IDENTITY`.  ⚠ `LIMIT OF A DONE ROW` contains the
    word and does not assert it, which is why this is a prefix test and not a substring one."""
    return (r.get('status') or '').strip().upper().startswith('DONE')


def check_row(r, scopes, root=None):
    """(failures, counted, pairs) for ONE row -- the one path the real rows and every in-run seed take.

    ⛭ `r7426` factored this out precisely so a seeded row cannot travel a different route from a real
    one (*a control that exercises a COPY of the logic proves the copy*), and `r7428` keeps that while
    moving every judgement inside it to `71`'s module."""
    root = root or ROOT
    out = []
    idx = (r.get('index') or '?').strip()
    try:
        pairs = dc.parse_decl(r.get('decl'))
    except dc.DeclCellError as e:
        # ⛔ the module RAISES rather than returning a short list, and a gate that let that through as
        #    an empty result would reintroduce the very defect the module exists to prevent.
        out.append(f'⓵ row {idx}\'s `decl` cell DOES NOT PARSE, which is an error and not an empty '
                   f'claim: {e}')
        return out, True, 0
    rcpts = dc.parse_receipt(r.get('receipt'))
    if not pairs and not rcpts:
        return [], False, 0
    for p in rcpts:
        if not os.path.exists(os.path.join(root, p)):
            out.append(f'⓷ row {idx}\'s `receipt` path does not exist: {p}')
    if not pairs:
        # ⛔⛭ `r7428` CAUGHT THIS BY RUNNING THE WIDENED GATE BEFORE LANDING IT, and it is the same
        #    mistake as the one this revision repairs: `r7424` charged "a `receipt` and no `decl`" over
        #    `DONE` rows only, where it fires `0` times; widening to every claiming row made it fire
        #    **22** times, and all 22 are `LIBRARY GAP`, `ROW: A DIFFERENT KIND` and `GENERIC-METRIC
        #    IDENTITY` rows -- *exactly the three classes `71`'s stated grammar says must carry an EMPTY
        #    `decl` cell*, "since a cell there could otherwise name a theorem that does not carry the
        #    row."  ⇒ ** A condition inherited into a wider population is a claim about that population
        #    and not about the one it was written for. **
        #    ⌗ So the charge is scoped to the rows that ASSERT the claim is formalised, read from the
        #    status string itself rather than from a hand-written list of exempt classes -- `r7412`'s
        #    eighth defect being a hand list that was missing members.
        if _asserts_done(r):
            out.append(f'⓵ row {idx} asserts `{(r.get("status") or "").strip()}` and names a '
                       f'`receipt`, but carries NO `decl`, so nothing records where the claim is '
                       f'formalised  ⇒ the remedy is written to that row\'s `decl` cell in {ROWS_REL}')
        return out, True, 0
    if not rcpts:
        out.append(f'⓷ row {idx} names a `decl` but no `receipt`')

    # ⓵ -- EVERY pair, from `71`'s own check.  `r7423` ①: checking one pair per row was 34 % of the
    #      population and every red it produced was its own mispairing.
    seen_files = set()
    for _idx, path, name, verdict in dc.check_pairs([r]):
        if verdict == 'no-file':
            out.append(f'⓵ row {idx}: `{name}` is claimed in {path}, and {_no_file_why(path, root)}')
            continue
        if verdict == 'not-declared':
            abs_p = dc.lean_path(path)
            seen = dc.declared_names(path) or set()
            out.append(f'⓵ DANGLING REFERENCE -- row {idx} claims `{name}` in {path}, which declares '
                       f'{len(seen)} identifier(s), none of them that one  ⇒ the remedy is written to '
                       f'that row\'s `decl` cell in {ROWS_REL}, or to '
                       f'{os.path.relpath(abs_p, root) if abs_p else path}')
            continue
        # ⓶ᵃ -- the pair's OWN file, not the row's first file, and once per distinct file.
        abs_p = dc.lean_path(path)
        rel = os.path.relpath(abs_p, root) if abs_p else path
        if rel in seen_files:
            continue
        seen_files.add(rel)
        if not covered_by(rel, scopes):
            out.append(f'⓶ᵃ row {idx}\'s file is inside no `formalisation-*` scope, so no run could '
                       f'ever clear it: {rel}  ⇒ the remedy is written to a `formalisation-*` '
                       f'workflow\'s own `paths:` in {WF_DIR}')
    return out, True, len(pairs)


# ── ⛭⛭⛭ THE IN-RUN SEEDS, `r7421` ③ as a STANDING RULE, sharpened at `r7423` ③ ─────────────────────
#   ⚖ ** A gate whose population can be empty must prove IN ITS OWN RUN that it could have fired. **
#   ⌈ `70`'s formulation, which is the test: ** after it, a zero is a measured zero. **
#   ⌊ *The seeds are SYNTHETIC: they live in a temporary tree, are counted in nothing, and are reported
#     on their own lines, because a control that changes the verdict it controls is not a control.*
#
#   ⛔⛭ `r7428` SHARPENS THE TARGET, in `66`'s words: *"seed a pair that is well-formed but points at
#   the WRONG FILE, since that is the error class the data can actually carry and the one your first
#   parser manufactured."*  `r7426` seeded a name declared NOWHERE, which is the easy class.
#   ⇒ *** AND IT MUST FAIL IN BOTH DIRECTIONS. ***  A seed that only fires is satisfied by a gate that
#     fires on everything; a seed that only stays silent, by a gate that fires on nothing.  So the same
#     seeded tree carries a CORRECTLY PAIRED MULTI-GROUP CELL -- the exact case `_split_decl` got wrong
#     -- and the run fails if that one produces anything.
#   ⇒ *** AND IT NOW COVERS CONDITION `⓶ᵇ` TOO, WHICH NOBODY ORDERED. ***  `r7421` ③ is promoted
#     GENERALLY, and `⓶ᵇ`'s non-green population is empty on today's tree exactly as `⓵`'s was: both
#     records read `GREEN`, so a run that never exercises `NOT-GREEN` or `UNANSWERABLE` cannot show the
#     ruling is honoured rather than merely written down.
def in_run_seeds():
    """[(label, ok, detail), ...] -- every one must hold, or this run must not report on the real rows."""
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix='fj_inrun_')
    res = []
    try:
        d = os.path.join('computations', 'formalisation', 'lean', '_InRunSeed')
        os.makedirs(os.path.join(tmp, d), exist_ok=True)
        right, other = os.path.join(d, 'Right.lean'), os.path.join(d, 'Other.lean')
        # ⌗ the seeded file carries a named `section` inside its `namespace` on purpose: that shape is
        #   what `r7428` found the shared reader loses (see `Ⓠ`), so the seed exercises it.
        with open(os.path.join(tmp, right), 'w', encoding='utf-8') as fh:
            fh.write('namespace Seeded\n\nsection Inner\n\ntheorem seeded_right : True := trivial\n\n'
                     'end Inner\n\nend Seeded\n')
        with open(os.path.join(tmp, other), 'w', encoding='utf-8') as fh:
            fh.write('namespace Seeded\n\ntheorem seeded_other : True := trivial\n\nend Seeded\n')
        rcpt = os.path.join('receipts', '_in_run_seed.py')
        os.makedirs(os.path.join(tmp, 'receipts'), exist_ok=True)
        open(os.path.join(tmp, rcpt), 'w').write('# in-run seed\n')
        sc = {'formalisation-inrunseed.yml': ['computations/formalisation/lean/**']}
        rec_green = {'formalisation-inrunseed': (GREEN, 'seeded green')}

        def run(cell):
            with rooted(tmp):
                got, _counted, _n = check_row(
                    {'index': 'SEED', 'status': 'DONE', 'receipt': rcpt, 'decl': cell}, sc, root=tmp)
            return got

        # ⑴ WELL-FORMED, WRONG FILE -- the error class the data can carry.
        wrong = run(f'{right}: Seeded.seeded_other')
        hit = [m for m in wrong if 'DANGLING' in m]
        res.append(('⑴ a well-formed pair pointing at the WRONG FILE fires as a dangling reference',
                    len(hit) == 1, hit[0] if hit else f'nothing fired; got {wrong}'))
        # ⑵ CORRECTLY PAIRED MULTI-GROUP -- the case `_split_decl` got wrong, and it must be SILENT.
        ok_cell = f'{right}: Seeded.seeded_right | {other}: Seeded.seeded_other'
        quiet = run(ok_cell)
        res.append(('⑵ ...and a CORRECTLY PAIRED MULTI-GROUP cell is silent, so the seed is not rigged '
                    'to fire', not quiet, 'no failure, as required' if not quiet else f'got {quiet}'))
        # ⑶⑷⑸ CONDITION ⓶ᵇ, three-way, through the SAME charge function the real run uses.
        in_use = {right, other}
        for label, rec, want_charge in (
                ('⑶ a GREEN record clears the workflow condition', GREEN, False),
                ('⑷ a NOT-GREEN record FAILS it', NOT_GREEN, True),
                ('⑸ an UNANSWERABLE record FAILS it, and does not pass', UNANSWERABLE, True)):
            with rooted(tmp):
                got = record_charges({'formalisation-inrunseed': (rec, f'seeded {rec}')}, sc, in_use)
            good = (len(got) == 1 and rec in got[0]) if want_charge else not got
            res.append((label, good, got[0][:130] if got else 'no ⓶ᵇ charge, as required'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return res


def main(records=None):
    print('=' * 100)
    print('  FORMALISATION JOIN -- is every pair a `decl` cell claims still declared in the file that')
    print('  pair names, is that file under a workflow whose record says GREEN, and is every `receipt`')
    print('  path still there?')
    print('=' * 100)

    # ── ⓪ THE POSITIVE CONTROL, FIRST.  An instrument that cannot see its data must not answer. ──
    files = lean_files()
    seen = {f: declarations(os.path.join(ROOT, f)) for f in files}
    unreadable = sorted(f for f, s in seen.items() if s is None)
    total = len({n for s in seen.values() if s for n in s})
    print('\n  ⓪ THE POSITIVE CONTROL -- can this gate see declarations at all?')
    print(f'      `.lean` files found: {len(files)}')
    print(f'      distinct identifiers the control reader extracts: {total}')
    for f in unreadable:
        fail(f'⓪ a `.lean` file in the tree CANNOT BE READ, so nothing about it can be cleared: {f}')
    if files and total == 0:
        fail(f'⓪ ⛔ THE CONTROL READER FOUND NO DECLARATIONS IN ANY OF THE {len(files)} FILES -- so this '
             f'gate cannot see its own subject, and it says so rather than reporting a clean join '
             f'(`r7419` ③, `cc66`\'s shape: an instrument given less state than its question needs will '
             f'still answer)')
    elif not files:
        fail('⓪ ⛔ NO `.lean` FILE EXISTS UNDER THE FORMALISATION TREE -- a gate over `decl` cells with '
             'no tree to read would pass vacuously, so it fails instead')
    else:
        print(f'    ✔ the control sees {total} identifier(s), so a verdict about a `decl` cell is a '
              f'reading and not a silence')

    # ── ⓪ᵇ THE IN-RUN SEEDS, for BOTH conditions.  `r7421` ③, no flag, every ordinary run. ──
    print('\n  ⓪ᵇ THE IN-RUN SEEDS -- this run proving, on the real row path, that it could have fired')
    seeds = in_run_seeds()
    for label, ok, detail in seeds:
        print(f'    {"✔" if ok else "⛔"} {label}')
        print(f'        {detail[:150]}')
    if all(ok for _l, ok, _d in seeds):
        print(f'    ⇒ ** so a zero from this run is a MEASURED zero ** (`r7421` ③, `70`\'s words), for '
              f'the dangling-reference condition AND for the workflow condition, and the seeds are '
              f'synthetic -- counted in nothing below.')
    else:
        for label, ok, detail in seeds:
            if not ok:
                fail(f'⓪ᵇ ⛔ AN IN-RUN SEED DID NOT BEHAVE, so this run cannot show what it could have '
                     f'detected and must not report on the real rows -- {label}: {detail[:160]}')

    # ── ⓶ᵃ the workflow scopes ───────────────────────────────────────────────────────────────────
    scopes = workflow_scopes()
    print('\n  ⓶ᵃ THE WORKFLOW SCOPES -- read from each workflow\'s own `paths:`, never from a filename')
    for wf, globs in scopes.items():
        print(f'      {wf}: {globs}')
    if not scopes:
        fail('⓶ᵃ no `formalisation-*` workflow declares any path, so "under a green workflow" cannot be '
             'decided and no row could be cleared on it')
    ungated = [f for f in files if not covered_by(f, scopes)]
    print(f'      `.lean` files inside at least one scope: {len(files) - len(ungated)} of {len(files)}')
    for f in ungated:
        note(f'⓶ᵃ inside NO `formalisation-*` scope, so a row naming it could never be cleared: {f}')

    # ── ⓶ᵇ the RECORD, three-way ─────────────────────────────────────────────────────────────────
    if records is None:
        records = workflow_records(scopes)
    print('\n  ⓶ᵇ THE RECORD -- did each workflow pass on THIS tree?  three-way, and `UNANSWERABLE` is '
          'not a pass')
    for stem, (v, why) in sorted(records.items()):
        print(f'      {stem}: {v}')
        print(f'        {why[:170]}')
    if not records:
        note('⓶ᵇ no workflow stem to read a record for, which `⓶ᵃ` has already charged')

    # ── the rows ─────────────────────────────────────────────────────────────────────────────────
    head, rows = read_rows()
    print('\n  THE INVENTORY')
    if head is None:
        fail(f'the inventory is not readable at {ROWS_REL}, so the join cannot be checked')
        return _verdict(0, 0, 0)
    print(f'      columns: {head}')
    have_decl, have_receipt = 'decl' in head, 'receipt' in head

    if not (have_decl and have_receipt):
        # ⛔ THE VACUITY STATE, NAMED.  This is not "no dangling reference found".
        missing = [c for c in ('receipt', 'decl') if c not in head]
        print(f'      rows: {len(rows)}')
        print('\n  ⛔⛭ ** NOT YET CHECKABLE, AND THAT IS A DIFFERENT SENTENCE FROM A CLEAN JOIN. **')
        print(f'      the inventory does not carry {missing} yet, so ** 0 pairs are checkable **.')
        print(f'      *`71` supplies those columns; this gate is in place and will fire on the first '
              f'row that carries them.*  ⇒ ** 0 CHECKABLE is reported as 0 CHECKABLE, never as 0 '
              f'dangling references. **')
        return _verdict(0, len(rows), 0)

    claimants = [r for r in rows
                 if not (dc._empty(r.get('decl')) and dc._empty(r.get('receipt')))]
    bystatus = {}
    for r in claimants:
        bystatus[(r.get('status') or '').strip().upper()] = \
            bystatus.get((r.get('status') or '').strip().upper(), 0) + 1
    print(f'      rows: {len(rows)};  rows carrying a `decl` or a `receipt`: {len(claimants)}')
    print(f'      their statuses: {dict(sorted(bystatus.items()))}')
    nodecl = [r for r in claimants if dc._empty(r.get('decl'))]
    if nodecl:
        _st = sorted({(r.get('status') or '').strip() for r in nodecl})
        _bad = [r for r in nodecl if _asserts_done(r)]
        print(f'      rows carrying a `receipt` and NO `decl`: {len(nodecl)}, in {len(_st)} status '
              f'class(es) {_st}')
        print(f'        of which {len(_bad)} ASSERT the claim is formalised and are charged; the rest '
              f'are the empty-cell state `71`\'s grammar prescribes and are not')
    # ⛭ `r7428`: EVERY row carrying a claim, not only the `DONE` ones.  `r7423`'s order is "all pairs",
    #   and a cell that names a declaration makes a claim whatever the row's status -- a dangling
    #   reference in a `LIMIT OF A DONE ROW` row is the same dangling reference.
    checked = pairs = 0
    in_use = set()
    for r in claimants:
        got, counted, n = check_row(r, scopes)
        checked += 1 if counted else 0
        pairs += n
        try:
            for _p, _n in dc.parse_decl(r.get('decl')):
                _a = dc.lean_path(_p)
                in_use.add(os.path.relpath(_a, ROOT) if _a else _p)
        except dc.DeclCellError:
            pass
        for m in got:
            fail(m)
    print(f'      ⇒ `(file, name)` pairs checked: {pairs} over {checked} row(s), naming '
          f'{len(in_use)} distinct `.lean` file(s)')
    # ⓶ᵇ -- charged ONCE per workflow, with the population it covers.  See `record_charges`.
    for m in record_charges(records, scopes, in_use):
        fail(m)
    _qualification_note(claimants)
    return _verdict(checked, len(claimants), pairs)


# ── Ⓠ ⛔⛭⛭ WHAT THE SHARED CHECK ACTUALLY CHECKS, WHICH IS LESS THAN IT READS ───────────────────────
#   `r7428` found this while complying with the order, and it is in the instrument the order adopted.
#   `decl_cells.check_pairs` clears a pair when the qualified name is in the file's declaration set
#   ** OR when the name's LAST COMPONENT is **.  That fallback is load-bearing, and the reason is a
#   defect one layer down: the module pops its namespace stack on ANY `end <ident>`, so a named
#   `section ... end Inner` inside a `namespace` closes the namespace, and every declaration after the
#   first section is recorded BARE ONLY.
#   ⇒ *** So for the pairs that clear on the fallback, the NAMESPACE HALF OF THE QUALIFIED NAME IS NOT
#     BEING CHECKED: `A.lean: Wrong.foo` clears whenever `foo` is declared anywhere in `A.lean`. ***
#   ⌈ This gate does NOT substitute its own verdict -- that is the private reader the order removed, and
#     doing it again would be the same mistake with the sign flipped.  It MEASURES the strength of the
#     verdict it reports, because a gate that reads stronger than it is cannot tell its own silence from
#     its own verdict either.
#   ⌊ The patch is `66`'s and `71`'s to take: pop only on a MATCHING `end`, which the control reader
#     here already does; routed with the measurement rather than applied to another seat's module.
def _qualification_note(claimants):
    strict = fallback = confirmed = 0
    unconfirmed = []
    for r in claimants:
        try:
            pr = dc.parse_decl(r.get('decl'))
        except dc.DeclCellError:
            continue
        for path, name in pr:
            ds = dc.declared_names(path)
            if ds is None or (name not in ds and name.split('.')[-1] not in ds):
                continue
            if name in ds:
                strict += 1
                continue
            fallback += 1
            abs_p = dc.lean_path(path)
            ctl = declarations(abs_p) if abs_p else None
            if ctl and name in ctl:
                confirmed += 1
            else:
                unconfirmed.append((r.get('index'), path, name))
    if not fallback:
        print(f'      Ⓠ every cleared pair is cleared on its FULLY QUALIFIED name: {strict}')
        return
    note(f'Ⓠ of the cleared pairs, {strict} clear on the fully qualified name and {fallback} clear ONLY '
         f'on the name\'s last component -- so for those {fallback}, the namespace half of the claim is '
         f'not what was checked')
    note(f'Ⓠ the cause is in the shared reader and not in the data: it pops its namespace stack on any '
         f'`end <ident>`, so a named `section` inside a `namespace` closes the namespace.  An '
         f'independent control reader that pops only on a MATCHING `end` confirms {confirmed} of those '
         f'{fallback} as fully qualified after all')
    for idx, path, name in unconfirmed:
        note(f'Ⓠ and {len(unconfirmed)} pair(s) NO reader confirms as qualified, which is a question for '
             f'`71`\'s column rather than for the reader -- row {idx}: `{name}` in {path}')
        break
    if confirmed == fallback:
        note('Ⓠ ⇒ so the inventory is correct entire on the strict reading too, and the fallback is '
             'masking the reader\'s own `end` handling rather than a fault in the data.  Routed to `66` '
             'with the patch; NOT applied here, because a private reader is what this revision removed')


def _verdict(checked, claimants, pairs):
    print('\n' + '=' * 100)
    if FAILED:
        print(f'  ⛔ THE FORMALISATION JOIN GATE IS RED: {len(FAILED)} failure(s)')
        for x in FAILED:
            print(f'      - {x[:140]}')
        print('=' * 100)
        return 1
    if pairs == 0:
        print(f'  ⌗ NOTHING IS CHECKABLE YET: {claimants} row(s), 0 `(file, name)` pair(s) among them.')
        print('    ** That is reported as 0 CHECKABLE and not as a clean join. **  The control reader '
              'sees the tree, so the gate is live and will fire on the first pair that appears.')
    else:
        print(f'  ✔ the join holds: {pairs} `(file, name)` pair(s) over {checked} of {claimants} '
              f'claiming row(s) -- every pair declared in ITS OWN file, every file under a workflow '
              f'whose record says GREEN on this tree, every `receipt` present.')
    if NOTES:
        print(f'  ⌗ {len(NOTES)} note(s) above are reported and not charged.')
    print('=' * 100)
    return 0


# ── the gate's own seeds: `r7419` ③'s standing test, kept rather than run once ─────────────────────
def seed():
    """⛭⛭⛭ ** run the gate against the remedy its own rule prescribes before landing it. **

    *These are NOT the in-run seeds and do not replace them (`r7421` ③ is explicit that the standing
    test catches a gate that fires wrongly and the in-run one catches a gate that does not fire at all
    -- **both, not either**).  They cover what an in-run seed cannot: an unreadable file, the scope
    reader, the record provider's own branches, and the WHOLE GATE against a constructed inventory.*"""
    import shutil
    import tempfile
    res = {}
    tmp = tempfile.mkdtemp(prefix='r7428_seed_')
    try:
        lean_d = os.path.join(tmp, 'computations', 'formalisation', 'lean')
        os.makedirs(lean_d, exist_ok=True)
        good = os.path.join('computations', 'formalisation', 'lean', 'Seed.lean')
        with open(os.path.join(tmp, good), 'w', encoding='utf-8') as fh:
            fh.write('namespace Seeded\n\nsection Inner\n\ntheorem present_one : True := trivial\n\n'
                     'end Inner\n\ntheorem present_two : True := trivial\n\nend Seeded\n')
        other = os.path.join('computations', 'formalisation', 'lean', 'Other.lean')
        with open(os.path.join(tmp, other), 'w', encoding='utf-8') as fh:
            fh.write('namespace Seeded\n\ntheorem elsewhere : True := trivial\n\nend Seeded\n')

        # ── the CONTROL reader (⓪'s instrument, not the verdict) ──────────────────────────────────
        d = declarations(os.path.join(tmp, good))
        res['S1. the control reader finds a bare declaration'] = d is not None and 'present_one' in d
        res['S2. ...and its namespace-qualified form'] = d is not None and 'Seeded.present_one' in d
        res['S3. a declaration NOT in the file is absent from its set'] = \
            d is not None and 'renamed_away' not in d
        res['S4. ...and a named `section`\'s `end` does NOT close the namespace, so a declaration '
            'AFTER it is still qualified'] = d is not None and 'Seeded.present_two' in d
        unread = os.path.join(tmp, 'computations', 'formalisation', 'lean', 'Unreadable.lean')
        os.makedirs(unread, exist_ok=True)
        res['S5. a file that CANNOT BE READ returns None, which is not an empty set'] = \
            declarations(unread) is None
        res['S6. ...and None is distinguishable from a file that declares nothing'] = \
            declarations(unread) is None and declarations(os.path.join(tmp, good)) is not None

        # ── the scope reader ──────────────────────────────────────────────────────────────────────
        wf_d = os.path.join(tmp, WF_DIR)
        os.makedirs(wf_d, exist_ok=True)
        with open(os.path.join(wf_d, 'formalisation-seed.yml'), 'w', encoding='utf-8') as fh:
            fh.write("on:\n  push:\n    paths:\n      - 'computations/formalisation/lean/**'\n")
        with rooted(tmp):
            sc = workflow_scopes()
        res['S7. a `formalisation-*` workflow\'s own `paths:` is read'] = \
            sc.get('formalisation-seed.yml') == ['computations/formalisation/lean/**']
        res['S8. a file inside that scope reads as covered'] = bool(covered_by(good, sc))
        res['S9. a file outside it does not'] = not covered_by('receipts/x.py', sc)
        res['S10. and with NO workflow at all, nothing reads as covered'] = not covered_by(good, {})

        # ── ⛭ `rooted()` -- the trap this revision was most likely to fall into ───────────────────
        _real = dc.declared_names('computations/formalisation/lean/ShadowEngine.lean')
        with rooted(tmp):
            _seeded = dc.declared_names(good)
        res['S11. `rooted()` redirects `71`\'s module too, so a seed reads the SEEDED tree'] = \
            _seeded is not None and 'present_one' in _seeded
        res['S12. ...and restores it, so the real tree is readable after'] = \
            dc.declared_names('computations/formalisation/lean/ShadowEngine.lean') == _real

        # ── the three-way record provider, on its own branches ────────────────────────────────────
        with rooted(tmp):
            rec_unknown = workflow_records(sc)
        res['S13. a workflow `lean_record` keeps no record for reads UNANSWERABLE, never GREEN'] = \
            rec_unknown.get('formalisation-seed', ('', ''))[0] == UNANSWERABLE
        res['S14. ...and its message NAMES the ref the remedy is written to (`r7425` ④)'] = \
            'refs/ci/lean/formalisation-seed' in rec_unknown.get('formalisation-seed', ('', ''))[1]
        _st = lr.status
        try:
            lr.status = lambda *a, **k: (_ for _ in ()).throw(RuntimeError('seeded unreachable'))
            lr.WORKFLOWS = tuple(lr.WORKFLOWS) + ('formalisation-seed',)
            with rooted(tmp):
                rec_raise = workflow_records(sc)
            v, why = rec_raise.get('formalisation-seed', ('', ''))
            res['S15. a record read that RAISES reads UNANSWERABLE and not GREEN'] = v == UNANSWERABLE
            res['S16. ...and still names the ref AND the command that writes it'] = \
                'refs/ci/lean/formalisation-seed' in why and '--write formalisation-seed' in why
        finally:
            lr.status = _st
            lr.WORKFLOWS = tuple(w for w in lr.WORKFLOWS if w != 'formalisation-seed')

        # ── the state machine ─────────────────────────────────────────────────────────────────────
        _g = {'formalisation-seed': (GREEN, 'g')}
        res['S17. GREEN clears, NOT-GREEN and UNANSWERABLE do not, UNSCOPED is its own state'] = (
            green_state(good, sc, _g)[0] == GREEN
            and green_state(good, sc, {'formalisation-seed': (NOT_GREEN, 'n')})[0] == NOT_GREEN
            and green_state(good, sc, {})[0] == UNANSWERABLE
            and green_state('receipts/x.py', sc, _g)[0] == UNSCOPED)

        # ── and the WHOLE GATE, against a constructed inventory ───────────────────────────────────
        inv_d = os.path.join(tmp, os.path.dirname(ROWS_REL))
        os.makedirs(inv_d, exist_ok=True)
        rcpt_rel = os.path.join('receipts', 'seed_receipt.py')
        os.makedirs(os.path.join(tmp, 'receipts'), exist_ok=True)
        open(os.path.join(tmp, rcpt_rel), 'w').write('# seed\n')

        def run_on(rows_body, records=None):
            FAILED.clear()
            NOTES.clear()
            with open(os.path.join(tmp, ROWS_REL), 'w', encoding='utf-8') as fh:
                fh.write('index\tclass\tstatus\treceipt\tdecl\n' + rows_body)
            try:
                import contextlib as _cl
                import io as _io
                buf = _io.StringIO()
                with rooted(tmp), _cl.redirect_stdout(buf):
                    rc = main(records=records if records is not None else _g)
                return rc, list(FAILED), buf.getvalue()
            finally:
                FAILED.clear()
                NOTES.clear()

        rc, f, _ = run_on(f'1\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.present_one\n')
        res['S18. a row whose pair IS declared passes the WHOLE gate'] = rc == 0 and not f

        rc, f, _ = run_on(f'2\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.renamed_away\n')
        res['S19. a DANGLING pair fails the whole gate, named as dangling'] = \
            rc == 1 and any('DANGLING' in x for x in f)

        # ⛔⛭ THE REGRESSION GUARD FOR `r7423` ①: a correctly paired MULTI-GROUP cell must pass, and
        #    the pair in the SECOND group must be checked against the SECOND group's file.
        rc, f, _ = run_on(f'3\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.present_one | {other}: '
                          f'Seeded.elsewhere\n')
        res['S20. a CORRECTLY PAIRED multi-group cell passes -- the case `_split_decl` reddened'] = \
            rc == 0 and not f
        rc, f, out = run_on(f'4\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.present_one | {other}: '
                            f'Seeded.not_there\n')
        res['S21. ...and a bad pair in the SECOND group is caught against the SECOND group\'s file'] = \
            rc == 1 and any('DANGLING' in x and 'Other.lean' in x for x in f)
        rc, f, out = run_on(f'5\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.elsewhere | {other}: '
                            f'Seeded.elsewhere\n')
        res['S22. a WELL-FORMED pair pointing at the WRONG FILE is caught (`r7423` ③\'s class)'] = \
            rc == 1 and len([x for x in f if 'DANGLING' in x]) == 1 and 'Seed.lean' in ''.join(f)
        res['S23. ...and every pair is counted, not one per row'] = '2 over 1 row' in out

        _unread_rel = os.path.join('computations', 'formalisation', 'lean', 'Unreadable.lean')
        rc, f, _ = run_on(f'6\tG\tDONE\t{rcpt_rel}\t{_unread_rel}: Seeded.x\n')
        res['S24. a Lean path that is not a readable file fails AS UNVERIFIABLE, not as clean'] = \
            rc == 1 and any('UNVERIFIABLE' in x for x in f)
        rc, f, _ = run_on(f'7\tG\tDONE\t{rcpt_rel}\tcomputations/formalisation/lean/Gone.lean: '
                          f'Seeded.x\n')
        res['S25. ...and a path with NOTHING at it fails as absent, which is a different sentence'] = \
            rc == 1 and any('no file is present' in x for x in f)

        rc, f, _ = run_on('8\tG\tDONE\t\t\n')
        res['S26. a row carrying neither cell is not charged and not cleared'] = rc == 0

        rc, f, _ = run_on(f'9\tG\tDONE\treceipts/gone.py\t{good}: Seeded.present_one\n')
        res['S27. a `receipt` path that does not exist fails'] = \
            rc == 1 and any('receipt' in x and 'does not exist' in x for x in f)

        rc, f, _ = run_on(f'10\tG\tDONE\t{rcpt_rel}\tno_colon_here\n')
        res['S28. a `decl` cell that DOES NOT PARSE fails as a parse error, not as an empty claim'] = \
            rc == 1 and any('DOES NOT PARSE' in x for x in f)

        rc, f, _ = run_on(f'11\tG\tLIMIT OF A DONE ROW\t{rcpt_rel}\t{good}: Seeded.renamed_away\n')
        res['S29. a NON-`DONE` row\'s pair is checked too (`r7423`: ALL the pairs)'] = \
            rc == 1 and any('DANGLING' in x for x in f)

        # ── ⛔ and the ruling itself: `UNANSWERABLE` must never pass ───────────────────────────────
        ok_row = f'12\tG\tDONE\t{rcpt_rel}\t{good}: Seeded.present_one\n'
        rc, f, _ = run_on(ok_row, records={'formalisation-seed': (UNANSWERABLE, 'seeded unreachable')})
        res['S30. ⛔ a row that is otherwise CLEAN does NOT pass when the record is UNANSWERABLE'] = \
            rc == 1 and any('UNANSWERABLE, WHICH IS NOT A PASS' in x for x in f)
        rc, f, _ = run_on(ok_row, records={'formalisation-seed': (NOT_GREEN, 'seeded failure')})
        res['S31. ...and does not pass when the record says NOT-GREEN either'] = \
            rc == 1 and any(x.startswith('⓶ᵇ NOT-GREEN') for x in f)
        rc, f, _ = run_on(ok_row, records={})
        res['S32. ...and a MISSING record is UNANSWERABLE rather than absent of condition'] = \
            rc == 1 and any('UNANSWERABLE' in x for x in f)

        # ── the in-run seeds, shown to discriminate rather than to answer True ────────────────────
        for label, ok, _d in in_run_seeds():
            res[f'S33+. the IN-RUN seed: {label}'] = ok
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    [{"ok" if v else "FAIL"}]  {k}')
    bad = [k for k, v in res.items() if not v]
    print(f'\n  {len(res)} assertion(s), {len(bad)} failing')
    return 0 if not bad else 1


if __name__ == '__main__':
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(main())
