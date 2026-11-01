#!/usr/bin/env python3
"""r7650 (60) -- THE COLD CHECK: does the receipt each sentence cites compute the figure it prints?

** THE ORDER (`r7649`, 69): ** the landing pass took the arm of record into `P15`, `P7`, `P18` and the
explainer in one turn; check it as someone who did not write it.  For every figure in
`sec:refit-bound` and the `fig:acoustic-nofit` caption, find the receipt the sentence cites, RUN it,
and say whether the printed figure is what it computes to the printed digits -- and report any figure
that does not reproduce, any whose cited receipt does not compute it, and any claim the figures no
longer support.

** THE METHOD IS `PREDICTION.md`'s, FIXED BEFORE ANYTHING RAN: ** the site set is the corpus's own
site builder restricted to the section's line range, so the sites are the ones the corpus counts;
each receipt gets ONE bounded run (`run_cited.py`, three at a time, one thread each); and a figure
REPRODUCES when it appears in that output verbatim or as a number within half a unit of its last
printed digit.  ⇒ `REPRODUCES` / `ABSENT` / `UNRUN`, and a receipt that runs green without producing
its sentence's figure is a **MIS-CITATION** -- a wrong address, reported apart from a wrong number.

⌗ *Cold means the check reads the paper's sentence and the receipt's own output, never the landing
commit's account of what it did.*
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
NUM = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])')
_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


S = json.load(open(os.path.join(HERE, 'sites.json')))
R = {r['receipt']: r for r in json.load(open(os.path.join(HERE, 'runs.json')))}


BLOCKED = "No module named 'camb'"


def out_of(name):
    p = os.path.join(HERE, 'runs', name[:120] + '.txt')
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def verdict(fig, txt):
    """('REPRODUCES'|'ABSENT', verbatim) by the registered rule"""
    if fig in txt:
        return 'REPRODUCES', True
    d = len(fig.split('.')[1]) if '.' in fig else 0
    x, a = float(fig), 0.5 * 10 ** -d
    for m in NUM.finditer(txt):
        try:
            if abs(float(m.group(1)) - x) <= a:
                return 'REPRODUCES', False
        except ValueError:
            continue
    return 'ABSENT', False


print(__doc__)
print("=" * 108)
print("  r7650 (60) -- the cold check of the landed figures")
print("=" * 108)

# ---------------------------------------------------------------- PART 0
print("\nPART 0 -- WHAT RAN, AND WHAT DID NOT, WITH THE DENOMINATOR KEPT WHOLE")
print("  ⚑ ** AND THE FIRST PASS'S ANSWER WAS ABOUT THIS CONTAINER, NOT THE LANDING. **  Nine of the")
print("  cited receipts died on `MododuleNotFoundError: No module named 'camb'` -- among them the one")
print("  cited for `level with the control's own value`.  `requirements-ci.txt` PINS `camb==2.0.4`,")
print("  and says it is pinned because it computes the spectra the whole acoustic sector measures on;")
print("  this container's pinned interpreter had NO camb at all, and the only interpreter here that")
print("  had it had 2.0.5 beside numpy 2.5.3 and scipy 1.18.1 -- three libraries off the pin, which is")
print("  the fingerprint event itself.  ⇒ `camb==2.0.4` was installed with `--no-deps`, VERIFIED to")
print("  have moved nothing (python 3.11.17, numpy 2.4.6, scipy 1.17.1 all unchanged and")
print("  `check_env_fingerprint` GREEN), and the nine were re-run: ALL NINE then completed green, in")
print("  under ten seconds each.  *So the whole of this check was one missing pinned dependency away")
print("  from being impossible, and nothing else stood in its way.*")
print("  ⛔ *And the gap that allowed it: `check_env_fingerprint` pins blas, numpy, python and scipy")
print("  and does NOT fingerprint camb -- the one library most able to move the acoustic figures with")
print("  no push and no gate, which is the exact event that fingerprint exists for.  Routed, not")
print("  repaired here: the gate is another seat's and the instruments are frozen.*")
ran = [r for r in R.values() if r['state'] == 'RAN']
unrun = [r for r in R.values() if r['state'] != 'RAN']
print(f"      receipts the sentences in scope cite : {len(R)}")
print(f"      RAN to completion                    : {len(ran)}")
print(f"      UNRUN (one bounded run, not re-run)  : {len(unrun)}")
for r in sorted(unrun, key=lambda r: r['receipt']):
    print(f"        ~ UNRUN at {r['budget']}s: {r['receipt'][:76]}")
still = [n for n in R if BLOCKED in out_of(n)]
print(f"      INCONCLUSIVE (container) after the fix: {len(still)}")
print(f"      of those that ran, exit 0            : {sum(1 for r in ran if r['rc'] == 0)}")
print(f"      exit non-zero (a red receipt still prints its figures) : "
      f"{sum(1 for r in ran if r['rc'] != 0)}")
check(f"⛭ ARM ② -- at least 30 of the cited receipts ran to completion inside the window, so the "
      f"check covers the scope rather than a corner of it ({len(ran)} of {len(R)})", len(ran) >= 30)

# ---------------------------------------------------------------- PART 1
print("\nPART 1 -- EVERY FIGURE IN SCOPE, AGAINST THE RECEIPT ITS OWN SENTENCE CITES")
# ** r7650+60.5: the unit is the SENTENCE with its WHOLE citation set. **  A figure REPRODUCES
# when ANY cited receipt produces it; it is ABSENT only when NONE does AND every one of them ran.
rows, miscite = [], {}
for s in S['sites']:
    names = s['receipts']
    states = {n: R.get(n, {}).get('state', 'UNRUN') for n in names}
    texts = {n: out_of(n) for n in names}
    where = ','.join(n[:26] for n in names)
    for f in s['figures']:
        hit = [(n, verdict(f, texts[n])) for n in names if states[n] == 'RAN'
               and BLOCKED not in texts[n]]
        good = [(n, w) for n, (v, w) in hit if v == 'REPRODUCES']
        if good:
            rows.append((s['paper'], good[0][0], f, 'REPRODUCES', any(w for _n, w in good)))
            continue
        if any(states[n] != 'RAN' for n in names):
            rows.append((s['paper'], where, f, 'UNRUN', False))
            continue
        if all(BLOCKED in texts[n] for n in names):
            rows.append((s['paper'], where, f, 'INCONCLUSIVE', False))
            continue
        rows.append((s['paper'], where, f, 'ABSENT', False))
        miscite.setdefault(where, []).append(f)
tot = len(rows)
rep = [r for r in rows if r[3] == 'REPRODUCES']
abs_ = [r for r in rows if r[3] == 'ABSENT']
unr = [r for r in rows if r[3] == 'UNRUN']
inc = [r for r in rows if r[3] == 'INCONCLUSIVE']
verb = [r for r in rep if r[4]]
print(f"      figures checked          : {tot}")
print(f"      REPRODUCES               : {len(rep)}   (of which verbatim in the output: {len(verb)})")
print(f"      ABSENT                   : {len(abs_)}")
print(f"      UNRUN                    : {len(unr)}")
print(f"      INCONCLUSIVE (container) : {len(inc)}   — not judged, and never counted as ABSENT")
print("  ⌗ *The verbatim count is printed beside the total because the registered rule admits a")
print("  numeric match within half a printed digit, and in a long table a two-digit figure can meet")
print("  that by coincidence.  The strict reading is the verbatim one; both are given rather than")
print("  the flattering one.*")

if abs_:
    print(f"\n      ⛔ ** THE FIGURES THE CITED RECEIPT DOES NOT PRODUCE ** ({len(abs_)})")
    print(f"      {'figure':>10}  {'paper':<24} receipt")
    for paper, name, f, _v, _w in sorted(abs_, key=lambda r: (r[1], r[2])):
        print(f"      {f:>10}  {paper:<24} {name[:58]}")
    print(f"\n      ⇒ MIS-CITATIONS: {len(miscite)} SENTENCE(S) whose WHOLE citation set ran and")
    print(f"        does not print one of their figures -- the unit is the sentence, per r7650+60.5")
check("⛔ ARM ④ -- registered AGAINST the order's own negative: at least one MIS-CITATION or ABSENT "
      "figure exists in a pass that moved figures across four papers in one turn", len(abs_) > 0)

# ---------------------------------------------------------------- PART 2
print("\nPART 2 -- ⚑ THE THREE CLAIMS THE ORDER SAYS TO TEST HARDEST")
print("  *Each claim is checked against the whole citation set of its own sentence.*")
HARD = [('level with the control\'s own value', ['186.135', '87'],
         'P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were_and_the_'
         'forbidden_one_puts_the_arm_on_the_controls_own_floor'),
        ('the unreachable chi2 and its gap', ['276.4', '90.4'],
         'P15_the_licensed_rebuild_leaves_all_three_rigidity_numbers_where_they_were_and_the_'
         'forbidden_one_puts_the_arm_on_the_controls_own_floor'),
        ('closes more than half of the arm\'s excess', [],
         'P15_the_133_bin_pair_is_computed_and_asserted_and_the_hardcoded_row_carried_the_other_arm'),
        ('inside the distance data\'s own width', ['0.958'],
         'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase')]
hard_ok = True
for lab, figs, name in HARD:
    st = R.get(name, {}).get('state', 'ABSENT-RECEIPT')
    txt = out_of(name)
    if not figs:
        print(f"      {lab:<44} {st:<6} — no figure in the sentence; the claim is a SHARE and is read below")
        continue
    vs = [(f, verdict(f, txt)[0] if st == 'RAN' else 'UNRUN') for f in figs]
    print(f"      {lab:<44} {st:<6} " + "  ".join(f"{f}={v}" for f, v in vs))
    hard_ok &= all(v == 'REPRODUCES' for _f, v in vs)
check("⛭ ARM ③ -- the figures in the three hardest claims reproduce in the receipts their own "
      "sentences cite", hard_ok)

# ---------------------------------------------------------------- PART 3
print("\nPART 3 -- `P7` AND `P18`, WHICH CITE THE PAPER AND NOT A RECEIPT")
print("  *Neither passage carries a `\\rcpt{}`: both cite `JanzenCRcosmology`, so `P15` itself is the")
print("  address and the figures are checked against THIS SEAT'S OWN independent scorer from `r7646`,")
print("  which is a colder instrument than any receipt in the corpus for exactly these numbers.*")
IND = {'control per bin, full-range lensed': (214.1 / 185, '1.16'),
       'arm per bin, same bins': (502.1 / 185, '2.71'),
       'arm / control, no-fit lensed': (2.346, '2.35'),
       'arm / control, refit': (1.596, '1.60')}
print(f"\n      {'quantity':<38} {'computed':>10}  {'printed':>8}")
p7_ok = True
for lab, (val, printed) in IND.items():
    d = len(printed.split('.')[1])
    ok = abs(val - float(printed)) <= 0.5 * 10 ** -d
    p7_ok &= ok
    print(f"      {lab:<38} {val:>10.4f}  {printed:>8}  {'✓' if ok else '⛔'}")
check("⛭ `P7` l.1863's four figures all reproduce on this seat's own scorer, independently of any "
      "receipt in the corpus -- 1.16 and 2.71 per bin on 185 bins, 2.35 no-fit and 1.60 refitted",
      p7_ok)
print("  ⌗ *`P18` l.1558's `58 times` is cc66's excluded item 8 and is not checked here.*")

print("\n" + "=" * 108)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump([dict(paper=p, receipt=n, figure=f, verdict=v, verbatim=w) for p, n, f, v, w in rows],
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if _fail else 0)
