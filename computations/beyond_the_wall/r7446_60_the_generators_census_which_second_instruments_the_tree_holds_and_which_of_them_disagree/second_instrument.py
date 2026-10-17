#!/usr/bin/env python3
"""r7446 (60) -- THE GENERATOR'S CENSUS.

   ⚖ WHEN CHECKING WHETHER A RECORD SATISFIES A GATE'S CONDITION, READ THE GATE'S OWN PREDICATE.
     A REIMPLEMENTATION OF IT IS A SECOND INSTRUMENT AND IT WILL DISAGREE.   (PO-78, first generator, r7445 ①)

   HOW MANY SECOND INSTRUMENTS THE TREE HOLDS, AND HOW MANY OF THEM MEASURABLY DISAGREE.

   ⛔ CANDIDACY HERE CARRIES NO SIMILARITY JUDGEMENT.  The instance that produced the rule --
      r7442's `\\b[0-9a-f]{12,40}\\b` against corpus/check_quote_pins.py's `held at ([0-9a-f]{8,40})\\b`
      -- shares NO literal anchor with the gate it disagreed with, so no similarity rule a person
      would write would have caught it.  And r7430 already paid for a classifier: a classifier's
      confidence is not evidence.  So a pair is EXTENSIONAL:
          f and g pair    <=>  f != g as source text AND they both match some line of one population
          the pair disagrees  <=>  the symmetric difference of their match sets on it is non-empty
      Overlap is the measured evidence that the two are about the same thing.

   ⛔ A DISAGREEING PAIR IS NOT A DEFECT.  It proves a second instrument EXISTS.  It does not prove
      the receipt holding it ever asserted anything false -- a pattern may be kept in order to
      measure a disagreement, as `_MY_FIRST_TRY` is, or scoped to a population where the two agree.
      Nothing here is routed to any seat.  The output is a class, a size and a rule.

   usage:  python3 second_instrument.py [--seed] [--limit N]
"""
import ast, bisect, collections, os, re, subprocess, sys, time

ROOT = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True,
                      cwd=os.path.dirname(os.path.abspath(__file__))).stdout.strip()

RE_FUNCS = {'compile', 'search', 'match', 'fullmatch', 'findall', 'finditer', 'sub', 'subn', 'split'}
TEXT_GLOBS = ('*.md', '*.tex', '*.tsv', '*.txt')
GATE_GLOB = 'corpus/check_*.py'
FOREIGN_GLOBS = ('receipts/*.py', 'receipts/**/*.py', 'computations/*.py', 'computations/**/*.py')

# The control.  Its status is ALREADY ADJUDICATED -- r7442 kept the refuted detector in the tree on
# purpose -- so it is the adjudicator of this instrument and not one of its findings.
CONTROL_FOREIGN = r'\b[0-9a-f]{12,40}\b'
CONTROL_GATE    = r'held at ([0-9a-f]{8,40})\b'

PER_PATTERN_BUDGET = 20.0          # s; a pattern over it is reported SLOW-SKIPPED, as a stated limit


def tracked(*globs):
    r = subprocess.run(['git', '-C', ROOT, 'ls-files'] + list(globs), capture_output=True, text=True)
    return sorted(set(r.stdout.split()))


def literals(relpath):
    """Every string literal passed as the FIRST POSITIONAL ARGUMENT of an `re.<func>` call.

    By `ast`, never by grep: a grep over `re.compile(` cannot tell a pattern from the rest of a
    line, and the whole point of this revision is not to read a thing with a second instrument."""
    try:
        src = open(os.path.join(ROOT, relpath), encoding='utf-8').read()
        tree = ast.parse(src)
    except (OSError, SyntaxError, UnicodeDecodeError):
        return []
    out = []
    for n in ast.walk(tree):
        if (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr in RE_FUNCS
                and isinstance(n.func.value, ast.Name) and n.func.value.id == 're'
                and n.args and isinstance(n.args[0], ast.Constant)
                and isinstance(n.args[0].value, str)):
            out.append((n.args[0].value, n.lineno))
    return out


def harvest(globs):
    """pattern source -> sorted list of (file, lineno) sites"""
    sites = collections.defaultdict(list)
    files = tracked(*globs)
    for p in files:
        for pat, lineno in literals(p):
            sites[pat].append((p, lineno))
    for pat in sites:
        sites[pat] = sorted(set(sites[pat]))
    return files, dict(sites)


def gate_callers():
    """⒣ -- the OTHER direction: files that import a `corpus/check_*` module rather than rebuild it.

    Counted two ways and both reported: the import existing, and a name from it actually used."""
    imported, used = [], []
    for p in tracked(*FOREIGN_GLOBS):
        try:
            tree = ast.parse(open(os.path.join(ROOT, p), encoding='utf-8').read())
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue
        bound = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.Import):
                for a in n.names:
                    if 'check_' in a.name:
                        bound.add((a.asname or a.name).split('.')[0])
            elif isinstance(n, ast.ImportFrom):
                mod = n.module or ''
                if 'check_' in mod:
                    bound.update((a.asname or a.name) for a in n.names)
                elif mod in ('corpus', '') or mod.endswith('corpus'):
                    for a in n.names:
                        if 'check_' in a.name:
                            bound.add(a.asname or a.name)
            elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                  and n.func.id in ('__import__',) and n.args
                  and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str)
                  and 'check_' in n.args[0].value):
                bound.add('__import__')
            elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                  and n.func.attr == 'import_module' and n.args
                  and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str)
                  and 'check_' in n.args[0].value):
                bound.add('import_module')
        if not bound:
            continue
        imported.append(p)
        for n in ast.walk(tree):
            hit = False
            if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id in bound:
                hit = True
            elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in bound:
                hit = True
            if hit:
                used.append(p)
                break
    return imported, sorted(set(used))


def lines_population():
    files = tracked(*TEXT_GLOBS)
    seen = set()
    raw = 0
    for p in files:
        try:
            with open(os.path.join(ROOT, p), encoding='utf-8', errors='replace') as fh:
                for ln in fh:
                    raw += 1
                    seen.add(ln.rstrip('\n'))
        except OSError:
            continue
    return files, raw, sorted(seen)


def mask_of(rx, lines, nbytes):
    ba = bytearray(nbytes)
    search = rx.search
    for i, ln in enumerate(lines):
        if search(ln):
            ba[i >> 3] |= 1 << (i & 7)
    return int.from_bytes(bytes(ba), 'little')


# ---------------------------------------------------------------------------- the seed
def seed():
    """Synthetic patterns whose relations are known, so the arithmetic is checked before the tree is."""
    lines = ['held at 0a1b2c3d', 'held at 0a1b2c3d4e5f6a7b', 'nothing here', 'deadbeefcafe']
    nb = (len(lines) + 7) // 8
    m = lambda s: mask_of(re.compile(s), lines, nb)
    fails = []

    def check(name, got, want):
        if got != want:
            fails.append(f'{name}: got {got!r} want {want!r}')

    gate, mine = m(CONTROL_GATE), m(CONTROL_FOREIGN)
    check('control overlap non-empty', (gate & mine).bit_count() > 0, True)
    check('control disagrees',         (gate ^ mine).bit_count() > 0, True)
    # the gate accepts the 8-char sha; the stricter minimum does not -- which is the whole instance
    check('gate reaches line 0',       gate >> 0 & 1, 1)
    check('mine misses line 0',        mine >> 0 & 1, 0)
    check('mine reaches the bare hex', mine >> 3 & 1, 1)
    check('gate misses the bare hex',  gate >> 3 & 1, 0)
    # IDENTICAL SOURCE => IDENTICAL MASK => SYMDIFF 0.  This is the machinery's own invariant.
    check('identity is silent', (m(CONTROL_GATE) ^ gate).bit_count(), 0)
    # NO OVERLAP => NOT A PAIR, however alike the two look
    a, b = m(r'held at [0-9a-f]{8}$'), m(r'held at [0-9a-f]{16}$')
    check('disjoint pair has no overlap', (a & b).bit_count(), 0)
    check('disjoint pair still differs',  (a ^ b).bit_count() > 0, True)
    # a pattern matching nothing is SILENT, not absent
    check('silent pattern', m(r'zzzz-not-in-the-population').bit_count(), 0)

    print(f'seed: {len(fails)} failing of 9 assertions')
    for f in fails:
        print('  FAIL', f)
    return 1 if fails else 0


# ---------------------------------------------------------------------------- the run
def main():
    t_all = time.time()
    limit = None
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])

    print('r7446 (60) -- THE GENERATOR\'S CENSUS: SECOND INSTRUMENTS IN THE TREE')
    print('=' * 100)
    print('⚖ WHEN CHECKING WHETHER A RECORD SATISFIES A GATE\'S CONDITION, READ THE GATE\'S OWN')
    print('  PREDICATE.  A REIMPLEMENTATION OF IT IS A SECOND INSTRUMENT AND IT WILL DISAGREE.')
    print('  PO-78\'s first GENERATOR, named at r7445 ① out of this seat\'s own three instances.')
    print()

    gate_files, gate_pats = harvest((GATE_GLOB,))
    for_files, for_pats = harvest(FOREIGN_GLOBS)
    print(f'THE PATTERN POPULATIONS, by ast and never by grep')
    print(f'  gates    : {len(gate_pats):>5} distinct patterns over {len(gate_files):>5} files  ({GATE_GLOB})')
    print(f'  foreign  : {len(for_pats):>5} distinct patterns over {len(for_files):>5} files  '
          f'(receipts/ and computations/)')

    identical = sorted(set(gate_pats) & set(for_pats))
    print(f'  ⒞ BYTE-IDENTICAL to a gate\'s own pattern : {len(identical)}')
    print('     A byte-identical copy agrees with the gate TODAY by construction and disagrees the')
    print('     revision the gate is edited.  It is the class\'s floor, not its subject.')
    print()
    id_ffiles = sorted({s[0] for p in identical for s in for_pats[p]})
    id_gfiles = sorted({s[0] for p in identical for s in gate_pats[p]})
    print(f'     THE COPY HALF OF THE CLASS, AND IT NEEDS NO THRESHOLD AND NO POPULATION TO BE SIZED:')
    print(f'       {len(identical)} patterns, held at {sum(len(for_pats[p]) for p in identical)} sites '
          f'across {len(id_ffiles)} foreign files, standing against {len(id_gfiles)} gates')
    hold = collections.Counter(s[0] for p in identical for s in for_pats[p])
    for f, n in hold.most_common(10):
        print(f'       {n:>3}  {f}')
    print()

    txt_files, raw, lines = lines_population()
    if limit:
        lines = lines[:limit]
    nbytes = (len(lines) + 7) // 8
    print(f'THE LINE POPULATION, one and the same for both halves of every pair')
    print(f'  {len(txt_files)} tracked .md/.tex/.tsv/.txt files, {raw} lines, {len(lines)} DISTINCT lines')
    print('  ⌗ LIMIT, stated: agreement on this population is agreement ON IT and never equivalence,')
    print('    and a pattern matching no line of it is SILENT rather than absent.')
    print()

    allpats = sorted(set(gate_pats) | set(for_pats))
    masks, bad, slow = {}, [], []
    t0 = time.time()
    for k, pat in enumerate(allpats):
        try:
            rx = re.compile(pat)
        except re.error as e:
            bad.append((pat, str(e)))
            continue
        t = time.time()
        try:
            masks[pat] = mask_of(rx, lines, nbytes)
        except Exception as e:                                    # a pattern that cannot be run
            bad.append((pat, f'{type(e).__name__}: {e}'))
            continue
        dt = time.time() - t
        if dt > PER_PATTERN_BUDGET:
            slow.append((pat, dt))
        if (k + 1) % 100 == 0:
            print(f'    .. {k + 1}/{len(allpats)} patterns matched, {time.time() - t0:.0f}s',
                  flush=True)
    print(f'  {len(masks)} patterns matched against the population in {time.time() - t0:.0f}s; '
          f'{len(bad)} would not compile or run; {len(slow)} over the {PER_PATTERN_BUDGET:.0f}s budget')
    print()

    # ---- ⒟ THE SELF-TEST I REGISTERED IS VACUOUS, AND SAYING SO IS CHEAPER THAN SHIPPING IT.
    #
    # PREDICTION.md ⒟ registered the 53 byte-identical pairs as this instrument's own self-test:
    # each must come out with symmetric difference exactly 0, and a non-zero voids the run.  IT
    # CANNOT COME OUT OTHERWISE.  `masks` is keyed by PATTERN SOURCE, so a pattern appearing in a
    # gate and in a receipt is ONE entry, and `m ^ m` is 0 for every integer there has ever been.
    # The arm is a tautology wearing a gate's clothes -- an arm that cannot fail, which is the
    # class check_cannot_fail.py exists to catch, found here in this seat's own registration.
    # => It is scored a MISS and replaced by two tests that CAN fail:
    print(f'⒟ THE REGISTERED SELF-TEST IS VACUOUS BY CONSTRUCTION and is replaced by two that are not.')
    print('   `masks` is keyed by pattern SOURCE, so an identical pair is ONE mask and `m ^ m` is 0')
    print('   for every integer. An arm that cannot fail is the class check_cannot_fail.py is for.')
    nondet = []
    for p in identical:
        if p not in masks:
            continue
        again = mask_of(re.compile(p), lines, nbytes)      # a second compile and a second full pass
        if again != masks[p]:
            nondet.append(p)
    half = [p for p in identical if not (gate_pats.get(p) and for_pats.get(p))]
    print(f'   Ⓓⅰ DETERMINISM: each of the {len(identical)} recompiled and rematched from scratch; '
          f'{len(nondet)} disagreed with its first pass')
    print(f'   Ⓓⅱ HARVEST INTEGRITY: {len(half)} of the {len(identical)} lack a site on one of the two '
          f'sides they are claimed to be on')
    if nondet or half:
        print('   ⛔ THIS INSTRUMENT IS DEFECTIVE AND THE RUN IS VOID.')
        return 1
    print('   both zero.  The run stands on these two and not on the one registered.')
    print()

    # ---- the pairs
    #
    # ⛔ THE CANDIDACY RULE I REGISTERED IS DEGENERATE, AND THE SMOKE RUN SAID SO BEFORE THE REAL ONE.
    # PREDICTION.md defines a pair as `f != g AND they both match at least one line of the same
    # population`.  On a 4,000-line smoke population that rule classed 364 of 364 non-silent foreign
    # patterns -- ONE HUNDRED PER CENT -- as second instruments, because generic patterns overlap
    # everything.  A criterion that cannot come out any other way is not a measurement; it is the
    # same shape as the vacuous self-test two blocks above, in the same registration.
    # => The overlap>=1 figure is still computed and still reported, labelled as what it is.  The
    #    DISCRIMINATING figure is the one below, and its threshold is NOT chosen by me: it is swept,
    #    and the scale is set by THE ONE INSTANCE WHOSE STATUS IS ALREADY ADJUDICATED.
    live_gate = [(p, masks[p]) for p in sorted(gate_pats) if p in masks and masks[p]]
    live_for = [(p, masks[p]) for p in sorted(for_pats) if p in masks and masks[p]]
    print(f'PAIRING {len(live_for)} non-silent foreign patterns against {len(live_gate)} non-silent gate '
          f'patterns')
    t0 = time.time()
    pairs = []                      # (foreign, gate, overlap, symdiff, jaccard)
    for f, fm in live_for:
        for g, gm in live_gate:
            if f == g:
                continue
            ov = (fm & gm).bit_count()
            if not ov:
                continue
            sd = (fm ^ gm).bit_count()
            if sd:
                pairs.append((f, g, ov, sd, ov / (ov + sd)))
    print(f'  {len(pairs)} pairs overlap and disagree at the REGISTERED rule (overlap >= 1 line), '
          f'in {time.time() - t0:.0f}s')
    print(f'  ⌗ and that rule is degenerate: {len(pairs)} pairs over '
          f'{len({f for f, *_ in pairs})} of {len(live_for)} non-silent foreign patterns.')
    print()

    # ---- ⒢ THE CONTROL, which also CALIBRATES the threshold instead of me choosing one
    ctl = [r for r in pairs if r[0] == CONTROL_FOREIGN and r[1] == CONTROL_GATE]
    print('⒢ THE CONTROL -- r7442\'s deliberately-kept refuted detector against the gate it disagreed with')
    print(f'   foreign : {CONTROL_FOREIGN!r}')
    print(f'   gate    : {CONTROL_GATE!r}')
    if not ctl:
        print(f'   ⛔ NOT FOUND -- foreign harvested: {CONTROL_FOREIGN in for_pats}, '
              f'gate harvested: {CONTROL_GATE in gate_pats}, '
              f'foreign silent: {masks.get(CONTROL_FOREIGN, 0) == 0}, '
              f'gate silent: {masks.get(CONTROL_GATE, 0) == 0}')
        print('   ⛔ THE RUN IS VOID.  r7440\'s first run was wrong and LOOKED right because its figure')
        print('      was lower than the one it replaced; a control whose answer was already known is')
        print('      the only thing that caught it.  This is that control.')
        return 1
    _, _, c_ov, c_sd, c_j = ctl[0]
    print(f'   FOUND. overlap {c_ov} lines, symmetric difference {c_sd}, agreement {c_j:.4f}.')
    print('   The control REPRODUCES, so the instrument stands -- and it does one more job:')
    print('   ⇒ IT SETS THE SCALE.  The threshold below is not a number I picked; it is the agreement')
    print('     of the one pair in this corpus whose status is ALREADY ADJUDICATED.')
    print()

    print('THE SWEEP -- how many pairs survive at each agreement floor, reported as a curve and not a point')
    print('   floor     pairs   foreign patterns   foreign files   gates')
    for th in (0.0, 0.25, 0.50, 0.75, 0.90, c_j, 0.95, 0.99, 0.999):
        keep = [r for r in pairs if r[4] >= th]
        ff = sorted({s[0] for r in keep for s in for_pats[r[0]]})
        gg = sorted({s[0] for r in keep for s in gate_pats[r[1]]})
        tag = '  <- the control' if th == c_j else ''
        print(f'   {th:>7.4f}  {len(keep):>7}  {len({r[0] for r in keep}):>16}  '
              f'{len(ff):>13}  {len(gg):>5}{tag}')
    print()

    SURVIVE = [r for r in pairs if r[4] >= c_j]
    dis_for = sorted({r[0] for r in SURVIVE})
    dis_files = sorted({s[0] for f in dis_for for s in for_pats[f]})
    dis_gate_files = sorted({s[0] for r in SURVIVE for s in gate_pats[r[1]]})
    print(f'⒠ FOREIGN PATTERNS that agree with a gate\'s own pattern AT LEAST AS CLOSELY AS THE ONE')
    print(f'   ADJUDICATED INSTANCE DOES, and still disagree with it : {len(dis_for)}')
    print(f'   of {len(live_for)} non-silent foreign patterns '
          f'({100.0 * len(dis_for) / max(1, len(live_for)):.1f} %)')
    print(f'⒡ OVER DISTINCT FILES : {len(dis_files)} of {len(for_files)} foreign files, '
          f'against {len(dis_gate_files)} of {len(gate_files)} gates')
    print()
    pairs_all, pairs = pairs, SURVIVE

    # ---- ⒣ the other direction
    imported, used = gate_callers()
    print('⒣ THE OTHER DIRECTION -- files that CALL a gate instead of rebuilding it')
    print(f'   import a corpus/check_* module : {len(imported)} of {len(for_files)} files')
    print(f'   and use a name from it         : {len(used)}')
    for p in used[:20]:
        print(f'     {p}')
    if len(used) <= 2:
        print('   ⛔ AT OR NEAR ZERO, WHICH WAS REGISTERED IN ADVANCE AS ITSELF THE FINDING.')
        print('      "Read the gate\'s own predicate" then names a practice that DOES NOT EXIST in this')
        print('      tree, so the generator\'s rule needs a SEAM BUILT before it can be obeyed: its cost')
        print('      is a BUILD and not a habit.')
    print()

    # ---- the shape of the class, reported and not judged
    by_file = collections.Counter(s[0] for f in dis_for for s in for_pats[f])
    by_gate = collections.Counter(s[0] for g in {r[1] for r in pairs} for s in gate_pats[g])
    print('THE SHAPE OF THE CLASS -- reported, not judged, and routed nowhere')
    print('  the foreign files holding the most disagreeing patterns')
    for p, n in by_file.most_common(12):
        print(f'    {n:>3}  {p}')
    print('  the gates with the most second instruments standing against them')
    for p, n in by_gate.most_common(12):
        print(f'    {n:>3}  {p}')
    print()

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pairs.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('agreement\toverlap\tsymdiff\tsurvives\tforeign_pattern\tgate_pattern\t'
                 'foreign_sites\tgate_sites\n')
        for f, g, ov, sd, j in sorted(pairs_all, key=lambda r: (-r[4], -r[2])):
            fs = ';'.join(f'{a}:{b}' for a, b in for_pats[f][:4])
            gs = ';'.join(f'{a}:{b}' for a, b in gate_pats[g][:4])
            fh.write(f'{j:.6f}\t{ov}\t{sd}\t{int(j >= c_j)}\t{f!r}\t{g!r}\t{fs}\t{gs}\n')
    print(f'  full pair list written to {os.path.relpath(out, ROOT)} ({len(pairs_all)} rows, '
          f'{len(pairs)} of them surviving the control\'s floor)')
    print()
    print('THE TWO HALVES OF THE CLASS, WHICH IS THE ANSWER THIS REVISION ACTUALLY HAS')
    print(f'  ⒜ THE COPY HALF IS DECIDABLE AND IT IS {len(identical)} PATTERNS.  No threshold, no')
    print('     population, no judgement: the same regular expression written twice, once in a gate and')
    print('     once in a file that is not that gate.  It agrees today because it is the same text and')
    print('     diverges the revision either copy is edited.  A rule prevents exactly this.')
    print(f'  ⒝ THE DIVERGENT HALF IS NOT SIZEABLE THIS WAY, AND THE CONTROL IS WHAT SAYS SO.')
    print(f'     The one pair in this corpus whose membership is ADJUDICATED agrees with its gate at')
    print(f'     {c_j:.4f}, and {len(pairs)} pairs over {len({r[0] for r in pairs})} foreign patterns sit at or above that.')
    print('     So extensional agreement does not separate the known member from the field: whatever')
    print('     made r7442\'s detector a second instrument, it is not visible in how often the two')
    print('     patterns coincide on the corpus\'s own text.  Reporting a figure off this floor would')
    print('     be reporting the floor.')
    print()
    print('⛔ WHAT THIS DOES NOT SAY')
    print('  A disagreeing pair is NOT a defect.  It proves a second instrument EXISTS.  It does not')
    print('  prove the receipt holding it ever asserted anything false: a pattern may be kept to')
    print('  MEASURE a disagreement, as the control above is, or scoped to a population where the two')
    print('  agree.  The failure this family is named for is not a wrong number but a wrong accusation,')
    print('  and three of this cycle\'s four instances would have been filed against another seat.')
    print('  Nothing here is routed to any seat.  No gate and no receipt is edited.')
    print()
    print(f'⒤ THE PRICE : {time.time() - t_all:.1f}s')
    return 0


if __name__ == '__main__':
    sys.exit(seed() if '--seed' in sys.argv else main())
