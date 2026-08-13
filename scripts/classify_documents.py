#!/usr/bin/env python3
"""classify_documents.py -- ARC 14 step 0.  Classify every top-level document into one of the
four kinds, and emit DOCUMENT_LEDGER.md.

    ① SOURCE  -- the one hand-maintained state document (the lead register)
    ② VIEW    -- generated from a source; must carry a regenerator and a --check
    ③ METHOD  -- rules, guards, canon; timeless by construction
    ④ RECORD  -- frozen; lives in retired/ or is marked RECORD at its head

The classification is DECLARED, not guessed: each file carries `kind:` in its frontmatter, or
appears in the explicit tables below.  Anything that matches neither is reported UNCLASSIFIED,
and the unclassified count is the step's own done-test.  A guess would be exactly the
"pre-grading a document you have not opened" move the arc forbids.

    python3 scripts/classify_documents.py            # write DOCUMENT_LEDGER.md
    python3 scripts/classify_documents.py --live     # print the LIVE set, one path per line
    python3 scripts/classify_documents.py --check    # exit 1 if anything is unclassified

Written r2377.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

SOURCE = {'THE_LIVE_ARC.md': 'the lead register — the one live edge'}

VIEW = {
    'WHATS_TEED_UP.md':      ('THE_LIVE_ARC.md', 'scripts/regen_teed_up.py'),
    'DOCUMENT_LEDGER.md':    ('(the tree)',      'scripts/classify_documents.py'),
}

# ③ METHOD -- rules/guards/canon.  Timeless: they say how to work, not what is open.
METHOD = {
    'README.md', 'INTRODUCTION.md', 'THE_METHOD.md', 'THE_ARSENAL.md', 'THE_ARSENAL_INDEX.md',
    'THE_OPERATING_MANUAL.md', 'ONTOLOGY_FOUNDATION_INDEX.md', 'NOTATION_GLOSSARY.md',
    'JARGON_LEDGER.md', 'BIBKEY_ALIAS_MAP.md', 'THE_BASE_RATE.md', 'PROTECTED_OPEN.md',
    'SOURCE_VETTING.md', 'DISPATCHING_COWORK.md', 'VISION_FIELD_GUIDE.md',
    'GEOMETRY_PHYSICS_TAXONOMY.md', 'FOUNDATIONAL_DEPENDENCY_MAP.md',
}

# ④ RECORD -- frozen by kind.  Matched by prefix/suffix as well as by name.
RECORD_PREFIX = ('BUNDLE_r', 'gate_session_notes', 'RETIRED_', 'CREDO_', 'RECALL_ACROSS_COMPACTION',
                 'CAPSTONE_', 'PUZZLE_', 'C40_', 'DEMONSTRATING_THE_WAY_full', 'FORK_HISTORY',
                 'HISTORICAL_CONTEXT_', 'SPINUP_FAILURE_FORENSIC', 'KICKOFF_')
RECORD_EXACT = {'BUNDLE_README.md', 'REVISION_r2118.patch', 'THE_CONSOLIDATION_LEDGER.md',
                'PROGRAMME_UNFINISHEDNESS_CATALOGUE.md', 'RETIRED_PLANNING_THREADS.md'}

# state-carrying documents: hand-maintained today, and the arc's targets.
# kind is recorded as the kind they SHOULD be, with `now` saying what they are.
STATE = {
    'THE_PLAN.md':                                    'the work, route and destination',
    'CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md': 'the consolidation plan and the arcs',
    'INDEX.md':                                       'what is in the programme, and where',
    'CORPUS_MAP.md':                                  'the changelog',
    'FORK_c54.md':                                    "the c54 fork's own record",
    'OPEN_PROBLEMS_MAP.md':                           'the work-clusters and the runway',
    'THE_OPEN_PROBLEMS_LEDGER.md':                    'the seven families and their clue-maps',
    'THE_BURN_DOWN.md':                               "the register's accounting",
    'THE_WEAVE.md':                                   'the per-paper orchestration grid',
    'ENTRY_POINT_REGISTER.md':                        'what the corpus advertises',
    'THE_EVOLUTION_MAP.md':                           'what is standing and citable',
    'THE_CLOSURE_LEDGER.md':                          'the closure self-check ledger',
    'FIGURE_SWEEP.md':                                'the figure programme state',
    'STATE_programme.md':                             'where the programme stands',
    'STATE_matter_sector.md':                         'where the matter sector stands',
    'PHASE7_BUILD_LEDGER.md':                         'the Phase-7 build record',
    'THE_DISSOLUTION_CENSUS.md':                      'the six dissolution clusters',
    'PHYSICAL_VALUES_LEDGER.md':                      'the physical values and their provenance',
    'THE_RECEIPT_AUDIT.md':                           'the receipt audit',
    'THE_FERMION_SECTOR_GEOMETRY.md':                 'the fermion sector read in the geometry',
}

FIELD_LEDGERS = {
    'COMBINATORICS_LEDGER.md', 'COMPLEX_ANALYSIS_LEDGER.md', 'CONFORMAL_GEOMETRY_LEDGER.md',
    'QUADRIC_GEOMETRY_LEDGER.md', 'OPTICS_LENSING_LEDGER.md', 'CATEGORY_THEORY_LEDGER.md',
    'VARIATIONAL_LEDGER.md', 'FIGURE_THEOREM_LEDGER.md',
}


def front_kind(path):
    """A file may declare `kind:`, `current:`, `job:` and `class:` in its frontmatter.

    `job:` absorbs CONSOLIDATE §5's function (retired r2378).  That section's rule is the one this
    ledger runs on and is restated at the head of the generated file: BEING INDEXED IS A JOB, NOT A
    STATUS -- a resource that turns out to have no job is retired instead.  §5 held exactly one row
    by r2378, so the row became a declared field on the file itself and the section retired.

    `class:` discharges CONSOLIDATE §5b's standing owed item -- "a pointer in each of the six naming
    the class and this table, so meeting one is meeting all six" -- MECHANICALLY, by grouping them
    here, rather than by hand-editing six files with prose that would then go stale.  §5b itself is
    NOT absorbed and stays: it carries the question each instrument answers and when to read it, and
    its own text says why a merge would be wrong -- "each is read at a different moment, and filing
    by subject would destroy the filing by moment."
    """
    try:
        head = open(path, encoding='utf-8', errors='replace').read(2500)
    except OSError:
        return None, None, None, None
    k = re.search(r'^kind:\s*(\S+)', head, re.M)
    c = re.search(r'^current:\s*c54\.(\d+)', head, re.M)
    j = re.search(r'^job:\s*(.+)$', head, re.M)
    cl = re.search(r'^class:\s*(.+)$', head, re.M)
    return ((k.group(1) if k else None), (int(c.group(1)) if c else None),
            (j.group(1).strip() if j else None), (cl.group(1).strip() if cl else None))


def body_rev(path):
    try:
        rs = [int(x) for x in re.findall(r'c54\.(\d+)',
              open(path, encoding='utf-8', errors='replace').read())]
    except OSError:
        return None
    return max(rs) if rs else None


def classify():
    rows = []
    # capstones/ is scanned too: r2378 found the sixth whole-corpus instrument living there,
    # so a top-level-only scan reported its own declared class as 5 of 6.
    for path in sorted(glob.glob(os.path.join(ROOT, '*.md')) +
                       glob.glob(os.path.join(ROOT, '*.patch')) +
                       glob.glob(os.path.join(ROOT, '*.txt')) +
                       glob.glob(os.path.join(ROOT, 'capstones', '*.md'))):
        name = os.path.relpath(path, ROOT)
        declared, declared_cur, job, klass = front_kind(path)
        body = body_rev(path)
        declared_job = job
        if declared:
            kind, job = declared.upper(), (job or '(declared in frontmatter)')
        elif name in SOURCE:
            kind, job = 'SOURCE', SOURCE[name]
        elif name in VIEW:
            kind, job = 'VIEW', f'view of {VIEW[name][0]} via `{VIEW[name][1]}`'
        elif name in METHOD:
            kind, job = 'METHOD', 'rules / guards / canon'
        # ** r2440: THE RULE THAT CLOSED A CI OUTAGE THIS LINE CAUSED AND DID NOT SEE. **
        # At r2427 the duplicate sweep was found to have deleted twenty-nine live top-level files, and
        # they were restored from the fork's pristine tree -- correctly.  ** They were never classified. **
        # So `--check` has exited 1 on every push since, and because the workflow's `fast` job runs the
        # register checks under `set -e`, ** the fifteen text gates and the hollow-assertion lint never
        # executed in CI at all for twelve revisions ** -- while this line reported "twenty gates rc=0"
        # from running them ONE AT A TIME in its own container, where each exit code is seen separately.
        # ⇒ ** A gate suite run by hand and a gate suite run under `set -e` are different instruments. **
        # Found by node 53 on a pristine clone, which is the only place it was visible.
        #
        # THE CLASSIFICATION IS A RULE RATHER THAN A LIST, because a list of twenty-seven filenames is a
        # list that goes stale: ** a top-level document that ALSO exists in retired/ is the fork's own
        # retired working note, kept in both places because the fork does not retire by moving. **
        # (That is the same fact whose misreading caused the deletion -- so the rule and the bug have one
        # root, and naming it here is what stops the next node re-deriving it.)
        elif name == 'FOLD52_ASSESSMENT.md':
            # the fork's assessment of the abandoned 52/53 ACOUSTIC line; frontmatter carries a
            # `description:` but no `kind:`.  Named here rather than annotated into the fork's file,
            # so there is no cross-line annotation to keep alive through the next absorption.
            kind, job = 'RECORD', ("the fork's assessment of the abandoned 52/53 ACOUSTIC line -- "
                                   "what it holds, what to take, and what could not be verified")
        elif os.path.exists(os.path.join(ROOT, 'retired', name)) and os.sep not in name:
            kind, job = 'RETIRED', ("the fork's retired working note, carried at top level and in "
                                    "retired/ both; this line neither owns nor maintains it")
        elif name.startswith('capstones/'):
            kind, job = 'METHOD', (job or 'the why-layer — read at spin-up steps 8 and 8b')
        elif name in RECORD_EXACT or name.startswith(RECORD_PREFIX):
            kind, job = 'RECORD', 'frozen record'
        elif name in STATE:
            kind, job = 'STATE', STATE[name]
        elif name in FIELD_LEDGERS:
            kind, job = 'STATE', 'field ledger — probes and their verdicts'
        else:
            kind, job = 'UNCLASSIFIED', ''
        rows.append((name, kind, job if not declared_job else declared_job, declared_cur, body, klass))
    return rows


INDEX_BEGIN = '<!-- INDEX-INVENTORY BEGIN -- generated by scripts/classify_documents.py; do not hand-edit -->'
INDEX_END = '<!-- INDEX-INVENTORY END -->'


def write_index_block(rows, front):
    """ARC 14 step 3: INDEX's document inventory becomes a GENERATED view.

    INDEX.md's rows carried "what a thing is and where it lives" by hand, and its own banner history
    admits the failure twice over: "a currency banner that does not move when the document does is the
    stale-header class the programme sweeps for", and "the banner's own class is the one r1746's
    header-vs-body check exists for, and it went stale again inside the session that installed the
    check."  ** A document that has diagnosed its own staleness twice and stayed hand-maintained is
    asking to be generated. **

    What stays hand-written: the navigation tree, the front matter and the corpus table -- those are
    STRUCTURE, not state.  What is generated: the inventory of every top-level document with its kind
    and its job, which is exactly the classifier's output.
    """
    path = os.path.join(ROOT, 'INDEX.md')
    if not os.path.exists(path):
        return
    # RETIRED added r2440 with the retired-duplicate rule above.  ** The first draft added the rule
    # and not the sort key, and the script raised KeyError('RETIRED') -- caught here rather than in CI,
    # which is the point: a classifier that cannot ORDER a class it can ASSIGN is half a classifier. **
    # ** r2566: a KeyError here takes down the whole document classification and, through it, every
    # gate that reads INDEX.md.  A `kind:` this dict does not know is well-formed input the loader
    # REJECTED -- the silent-discard class's loud cousin, and the fix is the same shape: know the
    # convention, and fail SOFT on one you do not. **
    order = {'SOURCE': 0, 'VIEW': 1, 'STATE': 2, 'METHOD': 3, 'RECORD': 4, 'PLAN': 5,
             'RETIRED': 6, 'UNCLASSIFIED': 7}
    o = [INDEX_BEGIN, '']
    o.append('## ⌗ THE DOCUMENT INVENTORY — generated')
    o.append('')
    o.append(f'*Generated by `scripts/classify_documents.py` at fork front **c54.{front}** — '
             f'**{len(rows)} top-level documents**. **Do not hand-edit.** A document\'s kind and job '
             f'are declared in its own frontmatter, so they travel with the file. '
             f'The full table with currency is [`DOCUMENT_LEDGER.md`](DOCUMENT_LEDGER.md).*')
    o.append('')
    o.append('> **⌗ WHY THIS BLOCK IS GENERATED (r2381).** *This file\'s rows were hand-maintained, and '
             'its own banner history diagnoses the failure twice: **"a currency banner that does not '
             'move when the document does is the stale-header class the programme sweeps for"**, and '
             '**"the banner\'s own class is the one r1746\'s header-vs-body check exists for, and it '
             'went stale again inside the session that installed the check."** ***A document that has '
             'diagnosed its own staleness twice and stayed hand-maintained is asking to be '
             'generated.*** The navigation tree, front matter and corpus table below stay '
             'hand-written — those are **structure**, not state.*')
    o.append('')
    for k in ('SOURCE', 'VIEW', 'STATE', 'METHOD', 'RECORD'):
        sel = [r for r in rows if r[1] == k]
        if not sel:
            continue
        o.append(f'### {k} ({len(sel)})')
        o.append('')
        o.append('| document | job |')
        o.append('|---|---|')
        for n, _, job, _, _, _ in sorted(sel, key=lambda r: r[0]):
            j = (job or '—')
            j = j if len(j) < 300 else j[:300] + '…'
            o.append(f'| `{n}` | {j} |')
        o.append('')
    o.append(INDEX_END)
    block = '\n'.join(o)
    t = open(path, encoding='utf-8', errors='replace').read()
    if INDEX_BEGIN in t:
        pre, rest = t.split(INDEX_BEGIN, 1)
        post = rest.split(INDEX_END, 1)[1] if INDEX_END in rest else ''
        t = pre + block + post
    else:
        anchor = '\n## Front matter'
        i = t.find(anchor)
        t = (t[:i] + '\n\n' + block + '\n' + t[i:]) if i > 0 else (t.rstrip() + '\n\n' + block + '\n')
    open(path, 'w', encoding='utf-8').write(t)
    return len(rows)


def main():
    rows = classify()
    front = max([r[4] for r in rows if r[4] is not None] + [0])
    live_kinds = ('SOURCE', 'VIEW', 'STATE')

    if '--live' in sys.argv:
        for n, k, _, _, _, _ in rows:
            if k in live_kinds:
                print(n)
        return 0

    unclassified = [r[0] for r in rows if r[1] == 'UNCLASSIFIED']
    if '--check' in sys.argv:
        if unclassified:
            print(f'  [FAIL] {len(unclassified)} document(s) unclassified')
            for u in unclassified:
                print(f'    {u}')
            return 1
        print(f'  all {len(rows)} top-level documents classified')
        return 0

    counts = {}
    for _, k, _, _, _, _ in rows:
        counts[k] = counts.get(k, 0) + 1
    out = []
    out.append('---')
    out.append('name: document-ledger')
    out.append('kind: VIEW')
    out.append(f'current: c54.{front}')
    out.append('description: ARC 14 step 0 — every top-level document, its kind, its job and its '
               'currency. GENERATED by scripts/classify_documents.py; do not hand-edit.')
    out.append('sources: [chat]')
    out.append('---')
    out.append('')
    out.append('# THE DOCUMENT LEDGER')
    out.append(f'*Generated by `scripts/classify_documents.py` at fork front **c54.{front}**. '
               '**Do not hand-edit** — declare `kind:` in a file\'s own frontmatter, or add it to '
               'the tables in the script.*')
    out.append('')
    out.append('> **⌗ THE RULE THIS LEDGER RUNS ON** *(carried forward from `CONSOLIDATE` §5, retired '
               'r2378 under `RG-1` when the section held one row).* ***Being indexed is a JOB, not a '
               'STATUS: a resource that turns out to have no job is retired instead.*** *A document\'s '
               'job is declared in its own frontmatter as `job:`, so it travels with the file and '
               'cannot be separated from it.*')
    out.append('')
    out.append('**The four kinds** *(`ARC 14 · THE SINGLE EDGE`, `CONSOLIDATE` §2)*: '
               '**① SOURCE** the one hand-maintained state document · **② VIEW** generated, with a '
               '`--check` · **③ METHOD** timeless rules · **④ RECORD** frozen. '
               '**STATE** marks a document that carries state and is *not yet* one of the four — '
               'these are the arc\'s targets, and the count falling is the arc\'s own burn-down.')
    out.append('')
    out.append('| kind | count |')
    out.append('|---|---|')
    for k in ('SOURCE', 'VIEW', 'STATE', 'METHOD', 'RECORD', 'UNCLASSIFIED'):
        if k in counts:
            out.append(f'| **{k}** | {counts[k]} |')
    out.append('')
    classes = {}
    for n, k, job, dcur, body, klass in rows:
        if klass:
            classes.setdefault(klass, []).append(n)
    if classes:
        out.append('## ⌗ DECLARED CLASSES')
        out.append('')
        out.append('*A `class:` in a file\'s frontmatter groups it with its kin here. This discharges '
                   '`CONSOLIDATE` §5b\'s standing owed item — *"a pointer in each of the six naming the '
                   'class, so meeting one is meeting all six"* — **mechanically**, rather than by '
                   'hand-editing six files with prose that would then go stale. **§5b itself is not '
                   'absorbed and stays**: it carries the question each instrument answers and when to '
                   'read it, and its own text says why a merge would be wrong — *"each is read at a '
                   'different moment, and filing by subject would destroy the filing by moment."*')
        out.append('')
        for c in sorted(classes):
            out.append(f'**`{c}`** ({len(classes[c])}) — ' +
                       ' · '.join(f'`{x}`' for x in sorted(classes[c])))
            out.append('')
    out.append('## ⌗ EVERY DOCUMENT')
    out.append('')
    out.append('| document | kind | job | declared current | newest c54 in body | lag |')
    out.append('|---|---|---|---|---|---|')
    # RETIRED added r2440 with the retired-duplicate rule above.  ** The first draft added the rule
    # and not the sort key, and the script raised KeyError('RETIRED') -- caught here rather than in CI,
    # which is the point: a classifier that cannot ORDER a class it can ASSIGN is half a classifier. **
    # ** r2566: a KeyError here takes down the whole document classification and, through it, every
    # gate that reads INDEX.md.  A `kind:` this dict does not know is well-formed input the loader
    # REJECTED -- the silent-discard class's loud cousin, and the fix is the same shape: know the
    # convention, and fail SOFT on one you do not. **
    order = {'SOURCE': 0, 'VIEW': 1, 'STATE': 2, 'METHOD': 3, 'RECORD': 4, 'PLAN': 5,
             'RETIRED': 6, 'UNCLASSIFIED': 7}
    for n, k, job, dcur, body, klass in sorted(rows, key=lambda r: (order.get(r[1], 99), r[0])):
        dc = f'c54.{dcur}' if dcur is not None else '—'
        bd = f'c54.{body}' if body is not None else '—'
        lag = ''
        if k in live_kinds:
            basis = dcur if dcur is not None else body
            lag = str(front - basis) if basis is not None else 'never'
        out.append(f'| `{n}` | {k} | {job} | {dc} | {bd} | {lag} |')
    out.append('')
    out.append('> **⚠ THE LAG COLUMN IS A LOOK-SIGNAL, NOT A VERDICT.** *It reads the newest fork '
               'revision the file mentions, which any mention satisfies — a document can be made to '
               'look current by writing ABOUT the fork. **`declared current` is the honest column**, '
               'set only by the pass that actually brings a file current. And a forward document is '
               'ahead of the corpus by construction: "stale" is a word for the corpus, never for the '
               'instrument examining it.*')
    out.append('')
    path = os.path.join(ROOT, 'DOCUMENT_LEDGER.md')
    open(path, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(f'  wrote DOCUMENT_LEDGER.md: {len(rows)} documents, front c54.{front}')
    n = write_index_block(rows, front)
    if n:
        print(f'  wrote INDEX.md inventory block: {n} documents')
    for k in ('SOURCE', 'VIEW', 'STATE', 'METHOD', 'RECORD', 'UNCLASSIFIED'):
        if k in counts:
            print(f'    {k:<14} {counts[k]}')
    if unclassified:
        print(f'\n  UNCLASSIFIED ({len(unclassified)}) — each must be READ and dispositioned, '
              f'one at a time (ARC 14 step 4):')
        for u in unclassified:
            print(f'    {u}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
