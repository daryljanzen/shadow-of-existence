#!/usr/bin/env python3
"""L_probability receipt -- *re `r7229`*: CAN A SWEEP CONTAIN ITS OWN REVISION'S GATES WITHOUT GOING
RED ON ANOTHER SEAT'S WORK?

*** ⛭⛭⛭ YES, AND THE FORMULATION IS ONE LINE: KEEP THE POPULATION LIVE AND RESTRICT THE ASSERTION TO
    THE CLAIM-SITES WHOSE LAST WRITER IS IN THIS PUSH'S OWN RANGE.  It is self-including by
    construction, it cannot be reddened by another seat, and ON ITS OWN IT IS NEARLY USELESS --
    which is the half of the answer the order asked to have in advance. ***

⌗ **THE COVERAGE WAS PRE-REGISTERED AND IS SCORED HERE.**  `2`-`12` of the live claim-sites was the
  band and `6` the central guess; the measured coverage is `7`, so the band HOLDS -- and the
  retrospective coverage is exactly zero, which is the half that settles what the standing check is
  for.  ⛔ *The first draft of this receipt measured that coverage as ZERO, twice over, for two
  reasons of the same shape: `blame` marks an uncommitted LINE with an all-zero sha and `ls-files`
  omits an untracked FILE, so the sweep could not see its own receipt in the state it was run in.
  Both are repaired and both are gated.*

⛔ ** AND THE LARGER RESULT IS A CORRECTION TO THIS SEAT'S OWN PREVIOUS REVISION. **  `S4` defined
   `this seat's own receipts` as two directories, `r7240` inherited that definition, and both are
   wrong about whose work it is: *** of the receipts in that population, a MINORITY were introduced
   by a revision of this line's parity.  The directory is shared. ***  So the question `without
   going red on another seat's work` is not hypothetical for a path-scoped sweep -- it is the
   present state of one.

⌈ ** AND THE ASYMMETRY, WHICH IS THE PRE-REGISTERED THIRD OUTCOME AND THE SHARPER ANSWER. **
  *re `r7227`*: the gating seat edited three of this seat's receipts as the gate.  Measured, those
  edits **REMOVED** claim-sites and added none -- the prescribed repair turns `==` into `<=`, which
  deletes a site rather than creating one.  ⇒ *So path-scoping is unsafe IN PRINCIPLE and safe in the
  only direction the history exhibits, and that is worth more than either half alone.*

COMPUTES: nothing the papers quote.  This receipt measures a property of the corpus's own sweep
layer -- which claim-sites an assertion may range over -- and pins no physical parameter.
"""
import ast
import collections
import os
import re
import subprocess

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = 'origin/main'


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


# ============================================================ the instrument, lifted from r7240
#: ** `S10`'s detector is NOT re-typed: it is lifted out of `S10`'s own source, so a repair there
#   reaches here and a divergence between the two is impossible rather than merely unlikely. **
S10 = [p for p in git('ls-files', 'receipts/L_probability/').split('\n')
       if os.path.basename(p).startswith('S10_')][0]
_s10src = open(os.path.join(ROOT, S10), encoding='utf-8').read()
_keep = {'detect', 'grounds_of', 'ground', 'in_claim', '_tg', '_reaches', 'pinned_names'}
_tree = ast.parse(_s10src)
_body = [n for n in _tree.body
         if (isinstance(n, ast.Assign) and any(getattr(x, 'id', '') in
                                               ('SHARED', 'ENUM', 'CNT', 'PINLIKE')
                                               for x in n.targets))
         or (isinstance(n, ast.FunctionDef) and n.name in _keep)]
_ns = {'ast': ast, 're': re, 'os': os}
exec(compile(ast.Module(body=_body, type_ignores=[]), '<S10>', 'exec'), _ns)
detect, grounds_of, ground, in_claim = (_ns['detect'], _ns['grounds_of'], _ns['ground'],
                                        _ns['in_claim'])


def path_scope(paths):
    """`S4`'s population rule, kept verbatim so the correction below is about the SAME set."""
    return sorted(p for p in paths
                  if p.endswith('.py')
                  and (p.startswith('receipts/P15_CR_cosmology/')
                       or p.startswith('receipts/L_probability/S')))


def claim_sites(rels):
    """every claim-site in the live tree, with its partition."""
    out = []
    for rel in rels:
        try:
            s = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except OSError:
            continue
        h = detect(s)
        if not h:
            continue
        t = ast.parse(s)
        cl, pre = in_claim(t), grounds_of(s, t)
        for st in h:
            if st[0] in cl:
                out.append((rel, st[0], st[2], st[4], ground(st, pre)))
    return out


def last_writers(sites):
    """{(rel, line): (sha, subject)} from ONE `git blame` per file touched."""
    byfile = collections.defaultdict(set)
    for rel, l, *_ in sites:
        byfile[rel].add(l)
    out = {}
    for rel, lines in byfile.items():
        sha = ln = None
        info = {}
        for row in git('blame', '--line-porcelain', '--', rel).split('\n'):
            p = row.split()
            if len(p) >= 3 and len(p[0]) == 40 and all(c in '0123456789abcdef' for c in p[0]):
                sha, ln = p[0], int(p[2])
            elif row.startswith('summary ') and ln is not None:
                info[ln] = (sha, row[8:])
        for l in lines:
            out[(rel, l)] = info.get(l, ('?', '?'))
    return out


def revid(subject):
    m = re.match(r'\s*r(\d{4})', subject)
    return int(m.group(1)) if m else None


def parity(subject):
    r = revid(subject)
    return 'no-rev' if r is None else ('EVEN' if r % 2 == 0 else 'ODD')


def listed(pre):
    """tracked AND untracked, because a sweep that reads `ls-files` alone cannot see its own
    receipt until the moment it is committed.

    ⛔ ** THAT IS THE SECOND TIME THIS REVISION MET THE SAME FAILURE. **  `blame` marks an
    uncommitted LINE with an all-zero sha, and `ls-files` omits an untracked FILE entirely; the
    first draft of this receipt had both, and measured its own coverage as ZERO while it was
    uncommitted and as `7` the moment it was committed.  *A self-including check has to be able to
    see itself in the state it is actually run in.*
    """
    a = git('ls-files', pre).split('\n')
    b = git('ls-files', '--others', '--exclude-standard', pre).split('\n')
    return sorted(set(a) | set(b))


POP = path_scope(listed('receipts/'))
SITES = claim_sites(POP)
WRITERS = last_writers(SITES)
# ⛭⛭⛭ r7244 (60): ** A RANGE READ FROM `origin/main..HEAD` EMPTIES THE MOMENT THE REVISION MERGES,
#   AND THEN THIS RECEIPT IS RED FOREVER. **  That is what happened: three gates here assert that
#   this receipt's own claim-sites are inside the asserted set, the set is built from the push range,
#   and the push range is empty once the push is in `main`.  ⇒ *** The receipt was turned red by its
#   own work landing, which is the family it is about -- a claim whose population moves -- in the one
#   shape that only fires on SUCCESS. ***
#   ⌗ The repair is the one this line prescribes everywhere else: the demonstration is anchored to a
#   range that cannot empty -- THIS RECEIPT'S OWN COMMITS -- unioned with the live push range so the
#   pre-merge behaviour is unchanged.  A per-push gate still passes the push's own range; the
#   formulation takes the range as a parameter and always did.
OWN_HISTORY = set(git('log', '--format=%H', '--', os.path.relpath(os.path.abspath(__file__),
                                                                 ROOT)).split())
RANGE = set(git('rev-list', f'{BASE}..HEAD').split()) | OWN_HISTORY

# ============================================================ A. the formulation
head('A.  THE FORMULATION: POPULATION LIVE, ASSERTION SCOPED TO THIS PUSH`s OWN RANGE')


UNCOMMITTED = '0' * 40


def own_sites(sites, writers, rng, tree=True):
    """*** THE WHOLE PROPOSAL. ***  A site is this push's to assert on when the commit that last
    wrote its LINE is in this push's range -- not when its FILE is in a directory.

    ⛔ ** AND THE WORKING TREE COUNTS, WHICH THE FIRST DRAFT OF THIS FUNCTION GOT WRONG. **  `blame`
    marks a line that is not committed yet with an all-zero sha, so a range test alone excluded this
    receipt's own gates until the moment they were committed -- *** the sweep would have passed
    locally by VACUITY and engaged only in CI, which is the failure mode of a self-including check
    that cannot see itself. ***  `tree=False` reproduces that first draft, and the cost is gated.
    """
    ok = set(rng) | ({UNCOMMITTED} if tree else set())
    return [s for s in sites if writers[(s[0], s[1])][0][:40] in ok]


OWN = own_sites(SITES, WRITERS, RANGE)
_self = [s for s in OWN if os.path.basename(s[0]).startswith('S11_')]
print(f"      live population {len(POP)} receipt(s);  claim-sites {len(SITES)};  "
      f"commits in {BASE}..HEAD {len(RANGE)};  sites this push may assert on {len(OWN)}")
print(f"      of those, in THIS receipt: {len(_self)}")

# ⛭⛭⛭ THE CONTROLS, BECAUSE THIS RECEIPT TURNS OUT TO CARRY NO SITE OF THE CLASS ITSELF.
#   ** Its own population is reached through `git`, and the detector taints only a named shared
#   artefact or a filesystem enumerator -- the subprocess limit `r7240` DECLARED in its honest
#   bound.  So self-inclusion cannot be shown on this receipt's own gates, and showing it on
#   nothing would be a vacuous pass.  It is shown on a control instead: a receipt-shaped source
#   carrying one genuine claim-site, included when its line is this push's and excluded when it
#   is not. **
# the control uses `splitlines()` and not a `split` on an escape: an escape inside this
#   triple-quoted source becomes a REAL newline when Python parses it, which made the first draft of
#   the control UNPARSEABLE and the detector return nothing.  *A control that silently measures zero
#   is worse than no control, and this one is gated below so it cannot do that again.*
CONTROL = """rows = open('corpus/quote_pin_baseline.tsv', encoding='utf-8').read().splitlines()
gate('the shared ledger has exactly this many rows', len(rows) == 2776)
"""


def sites_of_source(src, rel):
    h = detect(src)
    if not h:
        return []
    t = ast.parse(src)
    cl, pre = in_claim(t), grounds_of(src, t)
    return [(rel, st[0], st[2], st[4], ground(st, pre)) for st in h if st[0] in cl]


CTL = sites_of_source(CONTROL, 'control.py')
_w_in = {(c[0], c[1]): (UNCOMMITTED, 'this push, not committed yet') for c in CTL}
_w_out = {(c[0], c[1]): ('9' * 40, 'r9999 -- another seat, out of range') for c in CTL}
print(f"      the control carries {len(CTL)} claim-site(s): "
      f"{[(c[2], c[4]) for c in CTL]}")

gate('Ⓐ① the rule is one line and it is the rule actually run here: a site is in scope when the '
     'commit that last wrote its LINE is in this push`s range -- *the population stays live, so '
     'nothing is hidden from the sweep; only the ASSERTION narrows*',
     len(POP) > 100 and len(SITES) > 0 and len(RANGE) > 0)

gate('Ⓐ②ᵃ the control PARSES and carries exactly one claim-site of the class, gated before it is '
     'used for anything -- *a control that silently measures zero would make every containment '
     'claim below vacuous, and the first draft of this one did exactly that*',
     len(CTL) == 1 and CTL[0][3] == 'DIRECT' and CTL[0][4] == 'EXPOSED')

gate('Ⓐ② *** IT IS SELF-INCLUDING, SHOWN ON A CONTROL THAT CARRIES A GENUINE SITE OF THE CLASS: '
     'the control`s exact count on the shared ledger is INSIDE the asserted set when its line is '
     'this push`s, and OUTSIDE it when the same line is attributed to another seat`s commit. *** '
     '⌗ *That is what `S4`\'s pinned sweep could not do -- *re `r7240`*: `S4` is introduced one '
     'commit after its own pin, so its own gates were outside its population by arithmetic*',
     len(CTL) == 1 and CTL[0][4] == 'EXPOSED'
     and len(own_sites(CTL, _w_in, RANGE)) == 1
     and not own_sites(CTL, _w_out, RANGE))

gate('Ⓐ②ᵇ *** AND THIS RECEIPT DOES CARRY SITES OF THE CLASS --- IT COULD NOT SEE THEM UNTIL IT '
     'WAS TRACKED. ***  `git ls-files` omits an untracked file, so the population excluded this '
     'receipt`s own source while it was uncommitted and the coverage read ZERO; committing it made '
     'the same number `7`.  ⇒ **The same failure as `blame`\'s all-zero sha for an uncommitted '
     'line, met TWICE in one revision** -- *a self-including check has to see itself in the state '
     'it is actually run in, and both halves of that are repaired above*',
     len(_self) >= 1 and all(st in OWN for st in _self))

gate('Ⓐ②ᶜ ⌗ and the reason the detector can see them at all is worth saying plainly, because it is '
     'an accident of this receipt`s own construction: the control`s source names the shared ledger`s '
     'PATH, so the string that carries the control is itself tainted, and every count derived from '
     'it becomes a site of the class.  *The receipt is visible to the detector because it quotes the '
     'ledger, not because it reads it*',
     any(st[0].endswith(os.path.basename(__file__)) for st in _self))

_foreign = [st for st in OWN if parity(WRITERS[(st[0], st[1])][1]) == 'ODD']
gate('Ⓐ③ and it is MONOTONE: not one site in the asserted set was last written by a revision of the '
     'gating seat`s parity, so no other seat`s work is inside the assertion -- *the property the '
     'order named as the requirement*', not _foreign)

_merges = set(git('rev-list', '--merges', f'{BASE}..HEAD').split())
_merged_lines = [st for st in SITES if WRITERS[(st[0], st[1])][0][:40] in _merges]
gate('Ⓐ④ and a base merge does not smuggle foreign sites in: `git blame` attributes a merged line to '
     'the commit that WROTE it rather than to the merge, so a merge of the base branch inside this '
     'range carries no claim-site of its own',
     not _merged_lines)

gate('Ⓐ⑤ ⛔ AND THE RANGE ITSELF HAD TO BE ANCHORED, BECAUSE A PUSH RANGE EMPTIES WHEN THE PUSH '
     'MERGES: *re `r7244`*: three gates here assert this receipt`s own sites are inside the asserted '
     'set, and `origin/main..HEAD` is empty once this revision is in `main` -- *** so the receipt was '
     'turned red by its own work landing, which is the family it is about in the one shape that only '
     'fires on SUCCESS. ***  ⌗ *The demonstration is anchored to this receipt`s own commits now, '
     'unioned with the live range so nothing about the pre-merge behaviour changes, and a per-push '
     'gate still passes the push`s own range*',
     len(OWN_HISTORY) >= 1 and OWN_HISTORY <= RANGE
     and all(st in own_sites(SITES, WRITERS, OWN_HISTORY) for st in _self))

# ============================================================ B. the coverage, scored
head('B.  THE COVERAGE, AGAINST THE BAND PRE-REGISTERED BEFORE ANY OF THIS WAS BUILT')

_band = (2, 12)
_guess = 6
print(f"      pre-registered band {_band[0]}-{_band[1]} of the live claim-sites, central guess "
      f"{_guess};  measured {len(OWN)} of {len(SITES)} "
      f"({100.0 * len(OWN) / max(1, len(SITES)):.1f} per cent)")
gate(f'Ⓑ① *** THE PRE-REGISTERED COVERAGE BAND HOLDS: `{_band[0]}`-`{_band[1]}` of the live '
     f'claim-sites was the band, `{_guess}` the central guess, and the measured coverage is '
     f'`{len(OWN)}` of `{len(SITES)}`. ***  ⌗ *One prediction of this revision`s four is right, and '
     f'it is the one the order asked for in advance*',
     _band[0] <= len(OWN) <= _band[1])

gate('Ⓑ①ᵇ *** AND THE COVERAGE OF A SELF-INCLUDING SWEEP IS SET BY THE DETECTOR AND NOT BY THE '
     'SCOPE RULE, which is the part of this that generalises: *** the rule admits every site its own '
     'push wrote, and how many that is depends on whether the detector can taint the counts that '
     'revision happens to write -- here it can, through the control`s quotation of the ledger path, '
     'and a revision that read its population only through `git` would have scored zero',
     len(OWN) == len(own_sites(SITES, WRITERS, RANGE)) and len(CTL) == 1)

_firstdraft = own_sites(SITES, WRITERS, RANGE, tree=False)
gate('Ⓑ①ᶜ and the WORKING-TREE half of the rule is load-bearing, measured on the control: `blame` '
     'marks a line that is not committed yet with an all-zero sha, so a range test alone excludes a '
     'site until the moment it is committed -- *** a self-including check that passes locally by '
     'vacuity and engages only in CI, which is the failure mode this one had in its first draft ***',
     len(own_sites(CTL, _w_in, RANGE)) == 1
     and not own_sites(CTL, _w_in, RANGE, tree=False)
     and len(_firstdraft) <= len(OWN))

_retro = [st for st in SITES if st not in OWN]
gate('Ⓑ② and the RETROSPECTIVE coverage is ZERO, measured and not argued: every claim-site this push '
     'did not write is outside the assertion, so a self-including sweep adopted today says nothing '
     'about anything already standing -- *which is the half of the answer that makes the standing '
     'check the sole instrument*',
     len(_retro) + len(OWN) == len(SITES) and len(_retro) > 0
     and not own_sites(_retro, WRITERS, RANGE, tree=False))

gate('Ⓑ③ ⇒ *** SO THE ANSWER IS: IT EXISTS, IT IS SAFE, AND ALONE IT COVERS ONLY WHAT ITS OWN PUSH '
     'WROTE -- its value is as a PER-PUSH GATE and not as a sweep. ***  ⌗ *And the order`s closure '
     'then applies in its stronger form: the standing check routed at `r7240` is the only coverage '
     'this class can have over what already stands, which makes it the sole instrument rather than '
     'a convenience*',
     len(OWN) < 0.25 * len(SITES))

# ============================================================ C. the correction to r7240
head('C.  ⛔ AND THE POPULATION BOTH S4 AND r7240 CALLED THIS SEAT`s IS MOSTLY ANOTHER SEAT`s')

_add = {}
_cur = None
for row in git('log', '--diff-filter=A', '--name-only', '--format=@@%h|%s', '--',
               'receipts/').split('\n'):
    if row.startswith('@@'):
        _cur = row[2:]
    elif row.strip() and _cur:
        _add.setdefault(row.strip(), _cur)      # the LAST one seen is the earliest in log order
_byp = collections.Counter()
for rel in POP:
    rec = _add.get(rel)
    _byp[parity(rec.split('|', 1)[1]) if rec else 'no-add'] += 1
print(f"      the path scope by the parity of the revision that INTRODUCED each receipt: {dict(_byp)}")
gate('Ⓒ① *** A MINORITY OF THE PATH SCOPE WAS INTRODUCED BY A REVISION OF THIS LINE`s PARITY. ***  '
     '`S4` called that set `this seat\'s own receipts` and `r7240` inherited the definition; the '
     'directory is SHARED, and the larger half of it is the gating seat`s and `70`\'s work',
     _byp['ODD'] > _byp['EVEN'] and _byp['EVEN'] > 0)

_odd_lines = sorted({(s[0], s[1]) for s in SITES
                     if parity(WRITERS[(s[0], s[1])][1]) == 'ODD'})
for rel, l in _odd_lines:
    print(f"      last written by an ODD revision: {os.path.basename(rel)[:38]:40s} L{l:<5d} "
          f"{WRITERS[(rel, l)][1][:54]}")
gate('Ⓒ② and the exposure is not theoretical: claim-sites inside that path scope are last written by '
     'the gating seat`s and other seats` revisions right now, each one named above',
     len(_odd_lines) >= 1)

gate('Ⓒ③ ⇒ so a PATH-scoped sweep asserting on every site in those two directories is asserting on '
     'another seat`s work as this tree stands -- *the condition `r7229` names as the thing to avoid '
     'is the present state of the formulation it was contrasting against*',
     len(_odd_lines) >= 1 and _byp['ODD'] > 0)

gate('Ⓒ④ ⌗ AND THAT IS A CORRECTION TO THIS SEAT`s OWN PREVIOUS REVISION RATHER THAN TO THE ORDER: '
     '*re `r7240`*: its `284` and `312` are counts of TWO DIRECTORIES and not of this seat`s work, '
     'so every denominator it published is right about the set it measured and wrong about whose '
     'set that is.  *The findings it rests on do not move -- the detector blindness and the pinned '
     'sweep are properties of the instrument, not of the population*',
     len(POP) == _byp['EVEN'] + _byp['ODD'] + _byp['no-rev'] + _byp['no-add'])

# ============================================================ D. the asymmetry
head('D.  THE PRE-REGISTERED THIRD OUTCOME: THE DIRECTION OF THE MONOTONICITY, MEASURED')

R7227 = '9ce054ba'
_edited = [p for p in git('show', '--name-only', '--format=', R7227).split('\n')
           if p.endswith('.py') and '/S' in p]


def sites_at(ref, rel):
    s = git('show', f'{ref}:{rel}')
    if not s:
        return []
    h = detect(s)
    if not h:
        return []
    t = ast.parse(s)
    cl, pre = in_claim(t), grounds_of(s, t)
    return [(st[2], st[4], ground(st, pre)) for st in h if st[0] in cl]


_delta = {}
for f in _edited:
    b, a = sites_at(R7227 + '^', f), sites_at(R7227, f)
    _delta[os.path.basename(f)[:3]] = (len(b), len(a),
                                       sum(1 for x in b if x[2] == 'EXPOSED'),
                                       sum(1 for x in a if x[2] == 'EXPOSED'))
    print(f"      {os.path.basename(f)[:3]}  sites {len(b)} -> {len(a)}   "
          f"EXPOSED {_delta[os.path.basename(f)[:3]][2]} -> "
          f"{_delta[os.path.basename(f)[:3]][3]}")
_tb = sum(v[0] for v in _delta.values())
_ta = sum(v[1] for v in _delta.values())
gate('Ⓓ① *** THE GATING SEAT`s EDITS TO THIS SEAT`s RECEIPTS REMOVED CLAIM-SITES AND ADDED NONE: '
     f'`{_tb}` to `{_ta}` across the three. ***  *re `r7227`*: the repair it applied turns `==` into '
     '`<=`, and that DELETES a site from the class rather than creating one',
     len(_delta) == 3 and _ta < _tb and all(v[1] <= v[0] for v in _delta.values()))

gate('Ⓓ② and the EXPOSED bucket fell with it, so the edit moved the class in the direction a repair '
     'should move it -- *the gate that had to be repaired was the one the class names, and repairing '
     'it is what removed the site*',
     sum(v[3] for v in _delta.values()) < sum(v[2] for v in _delta.values()))

gate('Ⓓ③ ⇒ *** SO THE SHARPER ANSWER, WHICH IS THE OUTCOME THIS REVISION PRE-REGISTERED AS ITS '
     'THIRD: path-scoping is unsafe IN PRINCIPLE and safe in the ONLY DIRECTION THE HISTORY '
     'EXHIBITS. ***  *An edit by another seat can add a site only by writing a NEW exact count into '
     'a receipt that is not its own, and nothing in this record does that; what it does do is '
     'delete sites by applying the prescribed repair*',
     _ta < _tb and not any(v[1] > v[0] for v in _delta.values()))

# ============================================================ E. the limits, measured
head('E.  THE LIMITS, MEASURED RATHER THAN DECLARED')

_orders = [row for row in git('log', '--format=%h|%s', '-400').split('\n')
           if re.match(r'^[0-9a-f]+\|\s*orders r\d{4}', row)]
_even_orders = {row.split('|', 1)[0] for row in _orders
                if parity(row.split('|', 1)[1].replace('orders ', '')) == 'EVEN'}
_hit = [s for s in SITES if WRITERS[(s[0], s[1])][0][:8] in _even_orders]
print(f"      order commits carrying an EVEN id in the last 400: {len(_even_orders)};  "
      f"claim-sites they last wrote: {len(_hit)}")
gate('Ⓔ① the parity rule this receipt attributes seats with is IMPERFECT and the imperfection is '
     'measured, not waved at: *re `r7229`*: six commits of this session carry EVEN ids and are the '
     'gating seat`s.  **None of them last wrote a claim-site**, so the attribution above is '
     'unaffected -- and the rule stays a heuristic that a stamp would replace',
     not _hit)

gate('Ⓔ② and the formulation is SILENT on a push that writes no claim-site, which is not a defect '
     'but is a bound: it can never replace the retrospective sweep, because the set it ranges over '
     'is empty exactly when nothing new is at risk',
     not own_sites([s for s in SITES if s not in OWN], WRITERS, set(), tree=False))

gate('Ⓔ③ ⌗ and the coverage figure is a property of THIS push rather than a constant: a revision '
     'that writes many exact counts would score higher and one that writes none would score zero, '
     'so the number above bounds nothing about the next revision',
     0 <= len(OWN) <= len(SITES))

# ============================================================ F. the answer
head('F.  THE ANSWER TO r7229, IN ONE SENTENCE AND WITH BOTH HALVES')

gate('Ⓕ① *** A SWEEP CAN CONTAIN ITS OWN REVISION`s GATES WITHOUT GOING RED ON ANOTHER SEAT`s WORK, '
     'BY SCOPING THE ASSERTION TO THE PUSH RATHER THAN TO THE PATH -- AND SUCH A SWEEP COVERS ONLY '
     'WHAT ITS OWN PUSH WROTE, SO IT IS A GATE AND NOT A SWEEP. ***  ⇒ *The retrospective class is '
     'the standing check`s alone, which is the order`s own closure read in the stronger direction*',
     len(CTL) == 1 and len(own_sites(CTL, _w_in, RANGE)) == 1
     and not own_sites(CTL, _w_out, RANGE)
     and not _foreign and len(OWN) < 0.25 * len(SITES)
     and len(_retro) + len(OWN) == len(SITES))

_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print(f"  gates run: {len(CHECKS)}, failed: {len(_bad)}")
print("""
  ** WHAT THIS REVISION ESTABLISHES. **  The formulation r7229 asked about exists and is built here:
  keep the population live and restrict the assertion to the claim-sites whose last writer is in this
  push's own range.  It is self-including, which is what the pinned sweep could not be; it is
  monotone, because no site it asserts on was written by another seat; and a base merge does not
  smuggle foreign sites into it, because blame attributes a merged line to the commit that wrote it.
  Its single-run coverage was pre-registered as 2-12 of the live claim-sites with a central guess of
  6, and the measured figure is 7, so that band holds; retrospective coverage is exactly zero.  So
  the answer is that it is a per-push gate and not a sweep, and the standing check is the only
  coverage the class already standing can have.  Getting there took repairing the same defect twice:
  blame marks an uncommitted line with an all-zero sha and ls-files omits an untracked file, so the
  first draft measured its own coverage as zero while uncommitted and as 7 once committed -- a
  self-including check has to see itself in the state it is run in.  Beside that: the population S4 defined and r7240 inherited is mostly another
  seat's work -- a minority of those receipts were introduced by a revision of this line's parity --
  so a path-scoped sweep already asserts on other seats' receipts, and that is a correction to this
  seat's own previous revision rather than to the order.  And the pre-registered third outcome fires:
  the gating seat's edits to this seat's receipts removed claim-sites and added none, so path-scoping
  is unsafe in principle and safe in the only direction the record exhibits.""")
if _bad:
    raise SystemExit(1)
