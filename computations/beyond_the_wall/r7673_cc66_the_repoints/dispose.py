#!/usr/bin/env python3
"""
`r7673` (cc66) -- ** THE SPLIT, REGENERATED TO THE POST-`r7673` STATE: WHAT HAPPENED TO EACH OF THE
THIRTY, AND WHAT IS ACTUALLY LEFT. **  Answers `r7673` ⓸.

*** THE HEADLINE: OF THE THIRTY, TWO ARE LANDED IN THE PAPER, SEVEN ARE REPOINTED AND GREEN, ONE WAS
ALREADY DONE BEFORE THIS SEAT REACHED IT, THIRTEEN LEAVE THE LIST ON 70's MEASUREMENT, TWO MUST NOT
BE REPOINTED AT ALL, TWO ARE READY AND WAITING ONLY ON A MERGE, TWO ARE OPEN TO 69, AND ONE IS HELD
ON A BUILD 70 HAS PRICED.  ⇒ NOTHING ON THE LIST IS WAITING ON THIS SEAT. ***

===================================================================================================
** WHY THIS IS A NEW FILE AND NOT AN EDIT TO `r7671`'s OWN `SPLIT.md` **
===================================================================================================

`r7671`'s `SPLIT.md` is the record of a READING -- thirty items, each with a verdict anchored in its
own sentence, generated against a pre-registered prediction whose arms were scored on exactly that
population.  ** Rewriting it in place would overwrite the thing it is evidence of. **  So it stays,
`split.py` stays green beside it with its arms still scored on the thirty it registered against, and
this file carries the one axis that reading does not have: *** what has HAPPENED to each item since.
***  `r7671/SPLIT.md` is the reading; this is the state.

** AND THE DISPOSITIONS ARE NOT A SECOND OPINION ON THE VERDICTS. **  A verdict says what KIND of
item it is -- RE-GROUND, REBUILD, HELD.  A disposition says where it now stands.  *An item can be
REBUILD and DONE, or HELD and LEAVES; the two axes are independent and the gates below check that
the pairs that cannot occur do not occur.*

===================================================================================================
** THE THIRTEEN THAT LEAVE, WHICH IS THE LARGEST SINGLE MOVEMENT AND IS NOT THIS SEAT'S WORK **
===================================================================================================

`r7669+70.1` measured that ** LEAFREC does not touch the control, bit for bit and by construction:
on the control `Hphys` and `Hleaf` are one expression. **  Every one of `r7671`'s thirteen HELD items
was held for exactly that question -- its CR legs had already moved and its only remaining namesake
read was a control leg.  ⇒ *** A control-only namesake read IS the arm of record's control, so all
thirteen leave PO-87's list without a build and without a re-ground. ***

⌗ ** This is the item on which 69's order was right to make 70 measure rather than let this seat
assume. **  `r7671` priced three control legs as "to build"; on 70's answer none of them needs
building, and the thirteen items that would have waited on them do not exist as work.

rc=0 on success.  Writes SPLIT.md beside this file.  Run: python3 dispose.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
PRIOR = os.path.join(BW, 'r7671_cc66_the_split', 'SPLIT.md')
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
fail = []
out = []


def emit(line=''):
    print(line)
    out.append(line)


def check(label, ok, got=None):
    emit(f"    [{'ok' if ok else '  '}]  {label}" + (f"   {got}" if got else ''))
    if not ok:
        fail.append(label)


# the eight dispositions, and what each one means for whether anyone is waiting
LANDED = 'LANDED'      # the paper now carries it; the item has left the live census list
DONE = 'DONE'          # repointed by this seat in r7673, green, figures routed
ALREADY = 'ALREADY'    # was on the arm of record before this seat reached it
LEAVES = 'LEAVES'      # off the list on 70's control measurement -- no build, no re-ground
MUSTNOT = 'MUST-NOT'   # a repoint would destroy what the receipt measures; reason measured
READY = 'READY'        # 70's bank exists; waiting only on a merge
OPEN69 = 'OPEN-69'     # routed to 69 as a sentence; nothing for this seat to compute
HELD70 = 'HELD-70'     # waiting on a build 70 has priced and not made

#: key = the fragment of the receipt base name that identifies it in r7671's SPLIT.md
D = {
    'a_source_with_no_physics': (DONE, 'r7673+cc66.5/.7 -- repointed under r7645+cc66.68\'s key '
        'convention and green; six printed figures routed at .4 and FOUR MORE at .11, which that '
        'first route had omitted'),
    'derived_lensing_on_the_lcdm_arm': (LEAVES, 'its one spectrum is the control leg c54.178_lcdm'),
    'the_1p57_has_no_parameter_address': (LEAVES, 'arm read at ARMNPZ=cc66_r185_verify_cr_leafrec1; '
        'the only namesake left is refit_grid185/verify_lcdm, the control leg'),
    'the_acceptance_does_not_move_under_refinement': (LANDED, 'r7673+cc66.4 -- repointed onto 70\'s '
        'r7041_accept_*_leafrec1 banks; R6919_NARROWING moved to 0.131 and gate ⓻ added. No '
        'namesake load remains, so it has left the live census list'),
    'the_acoustic_contrast_is_not_in_the_source': (DONE, 'r7673+cc66.13 -- the SRCSAVE-inert leg to '
        'r6911_noop_leafrec1 at its arm-of-record keys. ZERO printed figures move: the leg asserts '
        'bit-identity, so its holding on both arms is what inert means. Left the live list'),
    'the_contrast_excess_is_symmetric': (LEAVES, 'every figure-bearing CR leg already moved; its two '
        'remaining namesake CR opens are declared gate reads; the only namesake FIGURE read is the '
        'control\'s fine bank'),
    'the_control_entered_the_regime': (LEAVES, 'all three figures the sentence prints are the '
        'control\'s'),
    'the_controls_base_log_is_banked': (MUSTNOT, 'its GRIDS table is a CONFIGURATION table, not an '
        'arm table: pairs.py ③/③ᵇ measured that refit_grid185_leafrec1 and grid_licensed_leafrec1 '
        'are ONE computation on all nine CR legs, so a repoint merges two of its three '
        'configurations and destroys the contrast it exists to make. Nothing it prints is in P15'),
    'the_cross_term_is_not_the_channel': (DONE, 'r7673+cc66.13 -- the PAIRSAVE-inert leg to '
        'r6915_noop_leafrec1 at its arm-of-record key. ZERO printed figures move, for the same '
        'reason. Left the live list'),
    'the_de_tilted_peak_set': (LEAVES, 'GO[cr] and GL[cr] are the _leafrec1 grids and its driving '
        'pair is c54.186_cr_L3000_leafrec1; what is left namesake is the control\'s'),
    'the_fit_has_the_controls_freedom': (LEAVES, '_grid_for(tag) already sends every cr* leg to '
        'refit_grid185_leafrec1; the control\'s is the only namesake read'),
    'the_joint_fit_leaves_the_gaussian': (LEAVES, 'its one spectrum is the control leg '
        'L820_lcdm_L2512_nk800'),
    'the_kernels_phase_difference': (OPEN69, 'RE-GROUND routed to 69 at r7671+cc66 in the one batch '
        'it asked for: the figure is an ALIASING artefact of the Bessel route, which no '
        're-derivation on either arm moves'),
    'the_licensed_configuration_moves_neither_statistic': (ALREADY, 'ALREADY on the arm of record '
        'before this seat reached it -- sections H and I read the three _leafrec1 grids through '
        '_AO_DIRS with the control\'s nine files linked in from refit_grid185 and the composition '
        'gated at H①. Its H⑦ also already carried the two-grid identity. r7671\'s verdict priced it '
        'off PART B\'s namesake reads and never read past them: corrected at r7673+cc66.12'),
    'the_low_multipole_depth_gap': (HELD70, 'cc66_lowell_sweep has no _leafrec1 sibling and its keys '
        'carry no LEAFREC dimension. 70 priced the build at r7673+70.2 (13 min point-only, or a '
        'HIER split-clock switch) and has not made it'),
    'the_lowell_sweep_is_reproduced': (OPEN69, 'RE-GROUND routed to 69: the claim is PROVENANCE, a '
        'statement about two implementations agreeing and not about which arm either ran on'),
    'the_model_difference_is_an_acoustic_contrast': (MUSTNOT, 'r7639 ⑵ wrote the reason in the file '
        'with numbers: the r6885 legs are pinned to the namesakes DELIBERATELY, and a per-arm '
        'repoint would read 2.529e-02, which measures nothing, where the namesake pair reads '
        'EXACTLY 0.0 -- so it would report a repair having FAILED where it records one having '
        'SUCCEEDED. Established at r7673+cc66.8'),
    'the_monopole_zero_point_is_not_the_channel': (DONE, 'r7673+cc66.11 -- repointed at the KEY: '
        'r6897_fields_leafrec1 at k__cr_leafrec1 and r6897_noop_leafrec1 at Dl__cr_leafrec1, both '
        'banks this receipt DECLARED itself blocked on at r7641 ⑴. _NAMESAKE_LEGS is now empty and '
        'gated. No printed figure moves: the 1.044 reads cc66_r185_verify_cr_leafrec1, already the '
        'arm of record, which r7671\'s own verdict got wrong'),
    'the_no_fit_confrontation_is_three_per_bin': (LEAVES, 'its SPEC table is explicit -- both CR '
        'entries are arm-of-record; the two namesake entries are the control legs'),
    'the_peak_plane_survives_the_merge': (DONE, 'r7673+cc66.13 -- both grids\' arm legs and all '
        'three lever legs repointed PER ARM, the control\'s staying namesake because no '
        'arm-of-record grid carries one. No printed figure moves. Two namesake-era pins split, and '
        'Ⓑ①\'s narrowing is routed to 69 as a JUDGEMENT about what r7223\'s burden is'),
    'the_phase_is_the_driving': (LEAVES, 'both figures the sentence prints are the CONTROL\'s. ⌗ 69 '
        'asked for it in the re-ground batch anyway because its header guard already states the '
        'namesake, and the proposed wording is carried in r7671\'s SPLIT.md'),
    'the_refit_leaves_the_background': (LEAVES, 'GRIDS[cr] is refit_grid_leafrec1_distances and '
        '_VER[cr] is arm-of-record; the control legs are the namesake side'),
    'the_residual_does_not_sit_at_ell_A': (READY, '70 reports at r7673+70.2 that nofit_figure_numbers '
        'is already on the arm of record. ⛔ That bank is on 70\'s branch (PR #623), not in this '
        'checkout, so this item is waiting on a MERGE and on nothing else'),
    'the_retention_is_the_combs_average': (READY, '70 banked r7041_accept_cr_leafrec1 at r7673+70.2 '
        'with a 53-key exact recipe check. ⛔ Same branch, same wait: a merge and nothing else'),
    'the_selection_does_not_truncate': (DONE, 'r7673+cc66.9 -- CRON/CROFF repointed per arm with a '
        'new gate ⓿ asserting 9 CR legs and 0 control legs in the arm-of-record grid. ONE printed '
        'digit moves: l.2283\'s 12.5 -> 12.63, routed to 69 as an edit it owes. ⌗ .11 corrected the '
        'characterisation: that digit moves with the REFIT POINT, not with LEAFREC'),
    'the_shared_fraction_does_not_mean_what_i_said': (LEAVES, 'BANK[cr] is '
        'cc66_r185_verify_cr_leafrec1, labelled THE ARM OF RECORD in the receipt; the control leg is '
        'the only namesake read'),
    'the_spacing_drift_is_made_in_the_projection': (DONE, 'r7673+cc66.13 -- section Ⓕ\'s two arm legs '
        'repointed per arm. THE DRIFT DOES NOT MOVE: D = +4.38 either way against the control\'s '
        '+4.42, with both namesake readings now printing beside the arm-of-record ones. That is the '
        'receipt\'s own claim holding where it was easiest to break'),
    'there_is_no_phase_residual': (LEAVES, 'BANK[cr] is cc66_r185_verify_cr_leafrec1, named '
        'explicitly; its one namesake CR read is a deliberate namesake-against-arm comparison'),
    'three_quarters_of_the_arms_residual': (LEAVES, '_AOR[cr] is cc66_r185_verify_cr_leafrec1; the '
        'remaining namesake figure read is _AOR[lcdm], the control leg'),
    'where_the_likelihood_sits': (LANDED, 'r7673 (69) -- NOT this seat\'s work: 69 moved its citation '
        'onto the method sentence (the receipt\'s F1, chi^2 = 206.4 over 215 bins), which does not '
        'depend on the arm. The RE-GROUND landed and the item left the live census list'),
}

print(__doc__.split("rc=0")[0])
emit('=' * 100)
emit('  THE POST-r7673 SPLIT -- every one of the thirty, its r7671 verdict, and where it now stands')
emit('=' * 100)

# ── read r7671's frozen reading, so the population is QUOTED and not retyped ─────────────────────
PRIORV = {}
for ln in open(PRIOR, encoding='utf-8'):
    m = re.match(r'  \[(\d\d)\] (REBUILD|RE-GROUND|HELD)\s+\(([^)]*)\)\s+(\S+)', ln)
    if m:
        PRIORV[m.group(4)] = (int(m.group(1)), m.group(2), m.group(3))
emit(f"  r7671's SPLIT.md, read as the frozen population: {len(PRIORV)} items")

MATCH = {}
for b in PRIORV:
    hits = [k for k in D if k in b]
    if len(hits) == 1:
        MATCH[b] = hits[0]
_unmatched = sorted(b for b in PRIORV if b not in MATCH)
_unused = sorted(k for k in D if k not in MATCH.values())

emit()
emit(f"  {'#':>3} {'r7671 verdict':>10} {'disposition':>11}  receipt")
emit('  ' + '-' * 98)
for b in sorted(PRIORV, key=lambda q: PRIORV[q][0]):
    n, verdict, why = PRIORV[b]
    dz, reason = D.get(MATCH.get(b), ('??', '(no disposition declared)'))
    emit(f"  [{n:02d}] {verdict:>10} {dz:>11}  {b[:66]}")
    emit(f"       r7671 read it as `{why}`")
    for _w in (reason[i:i + 92] for i in range(0, len(reason), 92)):
        emit(f"       {_w}")
emit()

check(f'① EVERY one of the {len(PRIORV)} items in r7671\'s frozen reading has exactly one '
      f'disposition, and no disposition is declared for an item outside it -- the population is '
      f'QUOTED out of SPLIT.md rather than retyped here',
      len(PRIORV) == 30 and not _unmatched and not _unused and len(MATCH) == 30,
      f'{len(MATCH)} matched of {len(PRIORV)}; {len(_unmatched)} without a disposition, '
      f'{len(_unused)} declared for nothing')

BY = {}
for b, k in MATCH.items():
    BY.setdefault(D[k][0], []).append(b)
emit('=' * 100)
emit('  ① THE TALLY, AND WHO IS WAITING ON WHOM')
emit('=' * 100)
_WAIT = {LANDED: 'nobody -- in the paper', DONE: 'nobody -- repointed and green',
         ALREADY: 'nobody -- was already done', LEAVES: 'nobody -- off the list on 70\'s measurement',
         MUSTNOT: '69, if it wants the alternative built', READY: 'a MERGE of 70\'s branch',
         OPEN69: '69 -- a sentence, not a computation', HELD70: '70 -- a build it has priced'}
for dz in (LANDED, DONE, ALREADY, LEAVES, MUSTNOT, READY, OPEN69, HELD70):
    g = sorted(BY.get(dz, []))
    emit(f"  {dz:>9}  {len(g):>2}   waiting on {_WAIT[dz]}")
_tot = sum(len(v) for v in BY.values())
check(f'② the eight dispositions PARTITION the thirty -- {_tot} of {len(PRIORV)}, nothing '
      f'double-counted and nothing left out', _tot == 30, f'{_tot} of 30')

# ⛔ the claim this file exists to make
_cc66 = len(BY.get(DONE, [])) + len(BY.get(LANDED, []))
check('③ ⛔⛭⛭ ** NOTHING ON PO-87\'s LIST IS WAITING ON THIS SEAT. **  Every item is landed, '
      'repointed and green, already done, off the list on 70\'s measurement, measured as a repoint '
      'that must not be made, waiting on a merge of 70\'s branch, routed to 69 as a sentence, or '
      'held on a build 70 has priced.  ⌗ *The two READY items are the only ones this seat takes '
      'next, and they are blocked on a merge rather than on work*',
      not BY.get('??') and len(BY.get(READY, [])) == 2 and len(BY.get(HELD70, [])) == 1,
      f'{_cc66} moved by this seat or landed; {len(BY.get(READY, []))} ready on a merge, '
      f'{len(BY.get(HELD70, []))} held on a build')

# ⛭ the thirteen, checked against r7671's own verdicts rather than counted by hand
_held71 = sorted(b for b in PRIORV if PRIORV[b][1] == 'HELD')
_leaves = sorted(BY.get(LEAVES, []))
emit()
emit('=' * 100
     )
emit("  ② THE THIRTEEN THAT LEAVE ARE EXACTLY r7671's THIRTEEN HELD, WHICH IS THE CHECK ON 70's")
emit('     MEASUREMENT HAVING ANSWERED THE QUESTION THEY WERE HELD FOR')
emit('=' * 100)
emit(f"      r7671 HELD: {len(_held71)}      disposed LEAVES: {len(_leaves)}      "
     f"same set: {_held71 == _leaves}")
check('④ ⛭⛭ the set that LEAVES is the SAME SET r7671 held, compared as sets and not as counts -- '
      'so 70\'s answer discharged exactly the question those thirteen were held for, and no item '
      'has been quietly moved into or out of that class.  ⛔ *If they merely AGREED IN NUMBER this '
      'gate would pass on a coincidence, which is why it is a set comparison*',
      _held71 == _leaves and len(_leaves) == 13,
      f'{len(_leaves)} leave, {len(_held71)} were held, identical: {_held71 == _leaves}')

# ⛭ and a DONE item must actually read an arm-of-record path in its live source
emit()
emit('=' * 100)
emit('  ③ AND `DONE` IS CHECKED AGAINST THE RECEIPT, NOT TAKEN FROM THIS FILE')
emit('=' * 100)
_bad = []
for b in sorted(BY.get(DONE, []) + BY.get(LANDED, []) + BY.get(ALREADY, [])):
    p = os.path.join(RCPT, b + '.py')
    if not os.path.exists(p):
        _bad.append((b, 'receipt absent'))
        continue
    src = ''.join(l for l in open(p, encoding='utf-8') if not l.lstrip().startswith('#'))
    body = src.split('"""', 2)[-1] if src.count('"""') >= 2 else src
    if '_leafrec1' not in body:
        _bad.append((b, 'no _leafrec1 outside its docstring and comments'))
for b, r in _bad:
    emit(f"      ⛔ {b[:70]}: {r}")
check(f'⑤ every item disposed LANDED, DONE or ALREADY reads an arm-of-record path or key in its '
      f'LIVE source -- docstring and comments stripped first, so a claim made only in prose does '
      f'not satisfy this gate.  {len(BY.get(DONE, [])) + len(BY.get(LANDED, [])) + len(BY.get(ALREADY, [])) - len(_bad)} of '
      f'{len(BY.get(DONE, [])) + len(BY.get(LANDED, [])) + len(BY.get(ALREADY, []))} pass',
      not _bad, f'{len(_bad)} failed' if _bad else 'all pass')

# ⛭ and MUST-NOT must be a measurement, not a preference
check('⑥ ⛔ both MUST-NOT items name a MEASURED reason and not a preference: one is r7639 ⑵\'s own '
      'numbers written in the receipt (2.529e-02 against an exact 0.0), the other is pairs.py\'s '
      'nine-leg identity.  *A seat declining to do ordered work owes a number, and these are the '
      'two numbers*',
      len(BY.get(MUSTNOT, [])) == 2
      and all(any(t in D[MATCH[b]][1] for t in ('2.529e-02', 'nine CR legs', 'ONE computation'))
              for b in BY.get(MUSTNOT, [])),
      f"{len(BY.get(MUSTNOT, []))} MUST-NOT items, each with its measurement named")

emit()
emit('=' * 100)
if fail:
    emit(f'  FAIL -- {len(fail)} check(s) did not hold')
    for f in fail:
        emit(f'    - {f}')
    emit('=' * 100)
    sys.exit(1)
emit('  GATES: ALL PASS.')
emit('  ⛭ Of the thirty: 2 LANDED, 7 DONE, 1 ALREADY, 13 LEAVES, 2 MUST-NOT, 2 READY, 2 OPEN-69,')
emit('     1 HELD-70.  ** Nothing is waiting on this seat. **')
emit('  ⛔ AND THE LARGEST MOVEMENT IS NOT THIS SEAT\'S: the thirteen that leave do so on 70\'s')
emit('     measurement that LEAFREC does not touch the control -- which is why 69 was right to')
emit('     order it measured rather than let this seat price three control builds on an assumption.')
emit('=' * 100)
with open(os.path.join(HERE, 'SPLIT.md'), 'w', encoding='utf-8') as fh:
    fh.write('# `r7673` (cc66) — THE POST-`r7673` SPLIT: what happened to each of the thirty\n\n')
    fh.write('*Generated by `dispose.py`. Supersedes `r7671_cc66_the_split/SPLIT.md` as the list of\n'
             'what is LEFT; that file stays as the record of the READING this is the state of.*\n\n')
    fh.write('```\n' + '\n'.join(out) + '\n```\n')
sys.exit(0)
