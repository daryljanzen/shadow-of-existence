#!/usr/bin/env python3
"""r7418 (60) -- THE REFUTATION SAT BELOW THE CAUSE IT REFUTES.  Four arms, all registered in
`PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ 2 occurrences outside the
two named blocks (band 0-8), ⒝ 1 of them inside asserted or printed text (floor 1, KNOWN, band 1-4),
⒞ NOT AN ARM -- a direct read, both blocks having been read before registering, ⒟ exact 0
receipt-running jobs at a default-depth checkout.

⛭ The refuted mechanism is `r7370`'s and the measurement that refuted it is `r7374`'s.  Neither is
restated here: the vocabulary this scans for is lifted from `r7370`'s own comment, and ⒟ re-reads the
workflow at TODAY's trunk rather than trusting `r7374`'s three commits -- `r7406`'s standing rule, that
a remedy is run against the condition its own argument needs before it is landed.

    python3 -I cost.py
"""
import argparse
import os
import re
import subprocess
import time

import yaml

FRAME = '3a922041'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

S39 = 'receipts/L_probability/S39_the_routed_collision_item_is_an_answer_read_as_a_claim_and_the_prevention_was_already_in_use.py'
S56 = ('receipts/L_probability/S56_a_pin_is_only_as_good_as_what_resolves_it_and_one_reference_over_'
       'resolved_while_the_other_under_resolved_so_both_wanted_the_fact_committed_beside_the_'
       'measurement.py')

# ── the refuted mechanism's OWN vocabulary, lifted from `r7370`'s comment rather than invented ──────
#   "On a shallow clone that walk stops at the horizon"; "reporting green over 8 per cent of the
#   corpus's revision history"; and `fetch-depth` **cited as the thing that truncates a map** -- the
#   knob `r7374` read to refute it.  ⚠ The third limb is narrowed to the registered wording: the first
#   build matched a bare `fetch-depth` anywhere, which is WIDER than `PREDICTION.md` registered, and
#   the wide count is reported beside the registered one rather than substituted for it.
VOCAB = [
    re.compile(r'\bshallow\b[^\n]{0,40}\b(clone|checkout|fetch|clones)\b', re.I),
    re.compile(r'\b(clone|checkout|fetch)\b[^\n]{0,40}\bshallow\b', re.I),
    re.compile(r'\bfetch-depth\b[^\n]{0,80}\b(truncat|empt|map|walk|horizon|reach)', re.I),
    re.compile(r'\b(truncat|empt|map|walk|horizon|reach)[^\n]{0,80}\bfetch-depth\b', re.I),
    re.compile(r"8\s*per\s*cent\s*of\s*the\s*corpus'?s?\s*revision\s*history", re.I),
]
VOCAB_WIDE = VOCAB + [re.compile(r'\bfetch-depth\b', re.I)]

# ── the ADJUDICATION, beside the registered count rather than instead of it ─────────────────────────
#   An occurrence CARRIES the refuted cause only if it attributes the collision gate's walked map --
#   or `S39`'s red -- to shallowness.  Everything else the vocabulary catches is a DIFFERENT and sound
#   claim: a receipt saying it needs a full clone, a gate reporting that this clone is shallow, a
#   quote-pin row whose pinned literal happens to be `"fetch-depth: 0"`.
CARRIES = re.compile(r'(_SESSION|collision gate|walk|walked|horizon|S39|session marker|'
                     r'revision history)', re.I)

A_CENTRAL, A_BAND = 2, (0, 8)
B_CENTRAL, B_BAND, B_FLOOR = 1, (1, 4), 1
D_POINT = 0

RESULT = {}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


_KEEP = ('.py', '.md', '.tsv', '.csv', '.txt', '.json', '.yml', '.yaml', '.tex', '.sh', '.log')


def tracked_text(sha=None):
    """every tracked text file that could carry the mechanism, as (path, source), READ AT `sha`
    (default `FRAME`, the pre-registration commit) or live when `sha` is `'LIVE'`.

    ⌗ `r7368` ②: the scan is scored at the registration commit and the live reading printed beside it,
    because this revision EDITS the files it measures.  The candidate list comes from `git grep` at the
    same sha so the two readings are built the same way."""
    at = FRAME if sha is None else sha
    if at == 'LIVE':
        files = [f for f in git('ls-files').split('\n') if f.endswith(_KEEP)]
        read = lambda f: open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read()  # noqa: E731
        cand = set(git('grep', '-l', '-I', '-i', '-e', 'shallow', '-e', 'fetch-depth',
                       '--', *_KEEP and ['.']).split('\n'))
    else:
        files = [f for f in git('ls-tree', '-r', '--name-only', at).split('\n')
                 if f.endswith(_KEEP)]
        read = lambda f: git('show', f'{at}:{f}')  # noqa: E731
        cand = set(git('grep', '-l', '-I', '-i', '-e', 'shallow', '-e', 'fetch-depth',
                       at).split('\n'))
        cand = {c.split(':', 1)[1] for c in cand if ':' in c}
    out = []
    for f in files:
        if f not in cand:
            continue
        src = read(f)
        if src:
            out.append((f, src))
    return out


def named_blocks(src, path):
    """the line span of the ONE header block in each named receipt that the order already names --
    from the first line of `r7370`'s cause to the last line before its `r7374` refutation.

    Returned as a set of 1-based line numbers so an occurrence inside it is EXCLUDED from ⒜ by
    position and not by filename: a second occurrence elsewhere in the same file still counts."""
    lines = src.split('\n')
    if path == S39:
        start = next((i for i, ln in enumerate(lines, 1)
                      if 'r7370: ** THE SHAS WERE PINNED' in ln), None)
        stop = next((i for i, ln in enumerate(lines, 1) if 'r7374: ** AND THE CAUSE' in ln), None)
    elif path == S56:
        start = next((i for i, ln in enumerate(lines, 1)
                      if 'Ⓒ THE UNDER-RESOLVING HALF' in ln), None)
        stop = next((i for i, ln in enumerate(lines, 1)
                     if 'CORRECTED AT `r7374`' in ln), None)
    else:
        return set(), (None, None)
    if start is None or stop is None:
        return set(), (start, stop)
    return set(range(start, stop)), (start, stop)


# ── ⒝'s classifier: is this line inside text the instrument ASSERTS or PRINTS? ──────────────────────
#   ⛔ The first build walked back up the physical lines counting brackets and classified `.tsv` data
#   rows and `.md` prose as `print(` arguments -- the TENTH instance of this phase's detector family,
#   and the first where the detector reached a file it has no syntax for at all.  ⇒ The classification
#   is now made from the PARSE TREE for a `.py` file and is REFUSED for anything else: a line in a
#   `.tsv`, `.md`, `.tex` or `.yml` file is prose or data and can assert nothing.
import ast          # noqa: E402
import io           # noqa: E402
import tokenize     # noqa: E402

_ASSERTERS = ('check', 'head', 'gate', 'print')


def classify(path, src):
    """{line -> kind} for a `.py` file: `check`/`head`/`gate`/`print` for a line inside one of those
    calls' argument lists, `comment` for a `#` line, `docstring` for a bare-expression string, and
    `code` otherwise.  A non-`.py` file gets `{}` and every hit in it reads `prose/data`."""
    if not path.endswith('.py'):
        return {}
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {}
    kinds = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) \
                and isinstance(node.value.value, str):
            for ln in range(node.lineno, (node.end_lineno or node.lineno) + 1):
                kinds.setdefault(ln, 'docstring')
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        f = node.func
        name = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else '')
        if name not in _ASSERTERS:
            continue
        for ln in range(node.lineno, (node.end_lineno or node.lineno) + 1):
            kinds[ln] = name
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type == tokenize.COMMENT:
                kinds[tok.start[0]] = 'comment'
    except (tokenize.TokenError, IndentationError):
        pass
    return kinds


def occurrences(sha=None):
    """(all, outside_named, asserted, wide) -- every line matching the refuted mechanism's vocabulary,
    with its position relative to the two named blocks and its kind from the parse tree.

    ⌗ This revision's OWN directory is excluded: `PREDICTION.md` and this file quote the refuted cause
    in order to name it, and counting them would be the detector reading its own description."""
    mine = 'computations/beyond_the_wall/r7418_60_'
    allhits, outside, asserted, wide = [], [], [], []
    for path, text in tracked_text(sha):
        if path.startswith(mine):
            continue
        if not any(p.search(text) for p in VOCAB_WIDE):
            continue
        lines = text.split('\n')
        named, _span = named_blocks(text, path)
        kinds = classify(path, text)
        for i, ln in enumerate(lines, 1):
            hit = any(p.search(ln) for p in VOCAB)
            hit_wide = hit or any(p.search(ln) for p in VOCAB_WIDE)
            if not hit_wide:
                continue
            kind = kinds.get(i, 'code' if path.endswith('.py') else 'prose/data')
            rec = (path, i, kind, CARRIES.search(ln) is not None, ln.strip()[:130])
            if hit_wide and not hit:
                if i not in named:
                    wide.append(rec)
                continue
            allhits.append(rec)
            if i not in named:
                outside.append(rec)
                if kind in _ASSERTERS:
                    asserted.append(rec)
    return allhits, outside, asserted, wide


# ── FORM 3: the BLOCK-level discriminator, because the vocabulary alone does not discriminate ───────
#   ⛔ `⒜` as registered is a VOCABULARY detector, and the vocabulary of `r7370`'s false cause is the
#   vocabulary of a TRUE claim everywhere else in this corpus: a shallow clone really does break a
#   receipt that reads history, and a dozen gates say so soundly.  ⇒ *** A detector keyed on the words
#   of a false claim cannot tell it from the true claim that shares them ***, which is `r7406`'s
#   discrimination problem one level out and the NINTH instance of this phase's family: the
#   defect and its sound twin are the same sentence.
#   ⇒ FORM 3 asks for the SUBJECT as well as the mechanism, at BLOCK level rather than per line --
#   a run of consecutive comment lines, one docstring, or one asserting call -- because `r7370`'s cause
#   names its subject on a different line from the word `shallow`.
SUBJECT = re.compile(r'(_SESSION|session marker|same_line|_same_line|Ⓑ①|collision gate|'
                     r'\bS39\b|walked map|that same map)', re.I)
#   ⚠ The first build's `DISOWNS` missed `r7374`'s own docstring, which disowns the cause in the words
#   *"Three measurements say it cannot be that"* -- no form of `false`, `refuted` or `corrected` in it.
#   ⇒ A disowning is recognised by its FUNCTION and not by one phrasing, so the alternation carries the
#   measurement-beats-cause form too.  The miss is reported rather than quietly patched: it is the same
#   failure as `⒜`'s, a detector keyed on the words of the thing instead of on what the thing does.
DISOWNS = re.compile(r'(is FALSE|was false|CORRECTED AT|AND THE CAUSE|refuted|'
                     r'the reason beside it|cannot be that|say it cannot be|'
                     r'the cause (written|beside))', re.I)


def blocks(path, text, kinds):
    """(first_line, last_line, kind, joined_text) for each candidate block: a maximal run of
    consecutive `comment` lines, each maximal run of `docstring` lines, and each asserting call."""
    lines = text.split('\n')
    out, i = [], 1
    n = len(lines)
    while i <= n:
        k = kinds.get(i, 'code' if path.endswith('.py') else 'prose/data')
        if k in ('comment', 'docstring') or k in _ASSERTERS:
            j = i
            while j + 1 <= n and kinds.get(j + 1) == k:
                j += 1
            out.append((i, j, k, '\n'.join(lines[i - 1:j])))
            i = j + 1
        else:
            i += 1
    return out


def form3(sha=None):
    """blocks that name BOTH the mechanism and r7370's own subject, and do not themselves disown the
    cause.  ⌗ This revision's own directory is excluded, as in `⒜`."""
    mine = 'computations/beyond_the_wall/r7418_60_'
    hits = []
    for path, text in tracked_text(sha):
        if path.startswith(mine):
            continue
        if not any(p.search(text) for p in VOCAB):
            continue
        kinds = classify(path, text)
        named, _span = named_blocks(text, path)
        for a, b, k, body in blocks(path, text, kinds):
            if not any(p.search(body) for p in VOCAB):
                continue
            if not SUBJECT.search(body):
                continue
            disowns = DISOWNS.search(body) is not None
            inside_named = bool(set(range(a, b + 1)) & named)
            hits.append({'path': path, 'lines': (a, b), 'kind': k, 'disowns': disowns,
                         'named': inside_named,
                         'head': body.strip().split('\n')[0][:120]})
    return hits


def window(sha=None):
    """⒞ the inheritance window: lines from the first statement of the false cause to the first line
    of its refutation, in each receipt.  A DIRECT READ, not an arm."""
    at = FRAME if sha is None else sha
    out = {}
    for path in (S39, S56):
        src = (open(os.path.join(ROOT, path), encoding='utf-8', errors='replace').read()
               if at == 'LIVE' else git('show', f'{at}:{path}'))
        _named, (start, stop) = named_blocks(src, path)
        # the SECOND carrier, where there is one: the block below the refutation that still states
        # the refuted cause.  Its distance from the refutation is the figure the repair cites.
        _lines = src.split('\n')
        second = next((i for i, ln in enumerate(_lines, 1)
                       if 'SECOND PASS' in ln), None)
        out[os.path.basename(path).split('_')[0]] = {
            'cause_at': start, 'refutation_at': stop,
            'window': (stop - start) if (start and stop) else None,
            'second_carrier_at': second,
            'below_refutation_by': (second - stop) if (second and stop) else None,
            'total_lines': len(_lines),
        }
    return out


def fetch_depths():
    """⒟ every JOB in the workflow, its checkout depth, and whether it runs a receipt -- read at
    TODAY's trunk.  `r7374` read this at three commits, none of them today's; `r7406`'s rule says the
    remedy is run against the condition its own argument needs.

    ⛔ The first build split the file on two-space mapping keys and so counted `pull_request`, `push`,
    `schedule` and `workflow_dispatch` -- the `on:` TRIGGERS -- as jobs, four of them at "default
    depth" because a trigger has no checkout.  *The eleventh detector instance in this phase, and the
    plainest: it read the container's indentation instead of its structure, which is this seat's own
    `r7403` rule turned on itself.*  ⇒ It parses the YAML and reads `jobs:` only."""
    wf = open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'),
              encoding='utf-8', errors='replace').read()
    doc = yaml.safe_load(wf)
    out = {}
    for name, job in (doc.get('jobs') or {}).items():
        steps = job.get('steps') or []
        depth = None
        for st in steps:
            if 'checkout' in str(st.get('uses', '')):
                depth = str(((st.get('with') or {}).get('fetch-depth', 'DEFAULT')))
        body = yaml.safe_dump(job)
        runs_receipt = bool(re.search(r'run_all_receipts\.py|run_fast_job\.sh|receipts/', body))
        out[name] = {'fetch_depth': depth, 'runs_receipt': runs_receipt}
    return out


def report(tag, sha):
    """one reading -- at `FRAME` or live -- printed in full."""
    allhits, outside, asserted, wide = occurrences(sha)
    f3 = form3(sha)
    win = window(sha)
    carr = [r for r in outside if r[3]]
    live3 = [h for h in f3 if not h['disowns'] and not h['named']]

    print('\n' + '-' * 100)
    print(f'READING: {tag}')
    print('-' * 100)

    print(f'\n⒜ THE REACH, AS REGISTERED -- vocabulary occurrences OUTSIDE the two named blocks: '
          f'{len(outside)}, against central {A_CENTRAL} and band {A_BAND[0]}-{A_BAND[1]}')
    print(f'    (total anywhere, named blocks included: {len(allhits)};  '
          f'the wide `fetch-depth` limb the registration does NOT license adds {len(wide)} more)')
    print(f'    ⇒ ** FAR OUTSIDE THE BAND, and the reason is the arm and not the corpus: ** the '
          f'registered detector is keyed on the VOCABULARY of `r7370`\'s false cause, and that '
          f'vocabulary is the vocabulary of a TRUE claim everywhere else -- a shallow clone really '
          f'does break a receipt that reads history, and {len(outside) - len(carr)} of the '
          f'{len(outside)} say exactly that, soundly.')
    print(f'    ⌗ loose subject match on the same lines: {len(carr)} -- still not a '
          f'discriminator, which is why FORM 3 exists.')
    print('    ⚠ *the LIVE figure RISES above the frame\'s, and that is the repair working rather '
          'than failing: the refuted account is KEPT as a record, so its words are still there -- '
          'which is itself why a vocabulary count cannot be the instrument here.*')

    print(f'\n⒜ FORM 3 -- BLOCKS naming the MECHANISM *and* `r7370`\'s own SUBJECT: {len(f3)}; '
          f'{len([h for h in f3 if h["named"]])} inside the two blocks the order names, '
          f'{len([h for h in f3 if h["disowns"]])} disowning the cause in their own text, '
          f'⇒ ** {len(live3)} stating it as LIVE outside what the order names **')
    for h in f3:
        tag3 = ('NAMED' if h['named'] else ('disowns' if h['disowns'] else '⛔ LIVE'))
        print(f'      [{tag3:7}] {h["path"]}:{h["lines"][0]}-{h["lines"][1]} [{h["kind"]}]')
        print(f'                {h["head"]}')

    print(f'\n⒝ THE ASSERTION -- vocabulary occurrences in text the instrument ASSERTS or PRINTS: '
          f'{len(asserted)}, against central {B_CENTRAL}, floor {B_FLOOR} (KNOWN) and band '
          f'{B_BAND[0]}-{B_BAND[1]}')
    for path, i, kind, carries, ln in asserted:
        print(f'      {path}:{i}  [{kind}(]{"  ⛔CARRIES" if carries else ""}')
    _a3 = [h for h in live3 if h['kind'] in _ASSERTERS]
    print(f'    ⇒ ** and FORM 3 puts {len(_a3)} of the LIVE blocks inside an ASSERTING call **, '
          f'which is the figure the arm was for: a comment records a belief, a clause states a '
          f'property of the object.')

    print('\n⒞ THE WINDOW -- a DIRECT READ and not an arm (both blocks were read before registering)')
    for k, v in win.items():
        if v['cause_at'] is None or v['refutation_at'] is None:
            print(f'      {k}: the TWO-BLOCK SHAPE IS GONE -- neither anchor is present, so there '
                  f'is no window: the measurement and the cause are one block '
                  f'({v["total_lines"]} lines in the file)')
            continue
        print(f'      {k}: cause stated at line {v["cause_at"]}, refuted at line '
              f'{v["refutation_at"]}  ⇒  window {v["window"]} line(s) of a '
              f'{v["total_lines"]}-line file')
        if v['second_carrier_at']:
            print(f'            ⛔ and a SECOND carrier at line {v["second_carrier_at"]} -- '
                  f'{v["below_refutation_by"]} line(s) BELOW the refutation, which the refutation '
                  f'therefore never reaches')

    return {'A_OUTSIDE': len(outside), 'A_ALL': len(allhits), 'A_WIDE_EXTRA': len(wide),
            'A_LOOSE_SUBJECT': len(carr),
            'B_ASSERTED': len(asserted),
            'F3_BLOCKS': len(f3), 'F3_LIVE': len(live3),
            'F3_LIVE_ASSERTING': len(_a3),
            'F3_LIVE_SITES': [(h['path'], h['lines'], h['kind']) for h in live3],
            'C_WINDOW': win}


def main(live=False):
    t0 = time.time()
    print('=' * 100)
    print('r7418 (60) -- THE REFUTATION SAT BELOW THE CAUSE IT REFUTES')
    print(f'  frame {FRAME};  bands registered in PREDICTION.md at that commit, before this ran')
    print('=' * 100)

    at_frame = report(f'AT THE FRAME {FRAME} -- the scored reading', None)
    RESULT['FRAME'] = at_frame
    if live:
        RESULT['LIVE'] = report('LIVE -- the same reading on this worktree, after the repair', 'LIVE')

    depths = fetch_depths()
    shallow_receipt_jobs = sorted(n for n, d in depths.items()
                                  if d['runs_receipt'] and d['fetch_depth'] != '0')
    print(f'\n⒟ THE REMEDY AGAINST ITS OWN RULE -- receipt-running jobs at a default-depth '
          f'checkout, read at TODAY\'s trunk: {len(shallow_receipt_jobs)}, against point '
          f'prediction {D_POINT}')
    for name in sorted(depths):
        d = depths[name]
        print(f'      {name}: fetch-depth {d["fetch_depth"] or "DEFAULT"}, '
              f'runs a receipt: {d["runs_receipt"]}')
    if shallow_receipt_jobs:
        print(f'    ⛔ {shallow_receipt_jobs} -- the refuted cause is LIVE and must be KEPT, not '
              f'demoted')
    else:
        print('    ⇒ the refuted cause has no job it could act on, at today\'s trunk as at '
              '`r7374`\'s three commits.  ** The demotion is licensed by a figure re-read rather '
              'than inherited, which is `r7406`\'s rule on a comment repair. **')

    RESULT['D_SHALLOW_RECEIPT_JOBS'] = shallow_receipt_jobs
    RESULT['D_JOBS'] = depths
    RESULT['SECONDS'] = round(time.time() - t0, 1)
    print(f'\n  price: {RESULT["SECONDS"]} s')
    return RESULT


if __name__ == '__main__':
    _ap = argparse.ArgumentParser(description=__doc__)
    _ap.add_argument('--live', action='store_true',
                     help='print the LIVE reading beside the scored one at FRAME')
    main(live=_ap.parse_args().live)
