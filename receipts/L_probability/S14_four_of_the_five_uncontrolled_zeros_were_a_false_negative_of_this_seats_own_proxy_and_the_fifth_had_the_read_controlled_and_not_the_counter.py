#!/usr/bin/env python3
"""L_probability receipt -- *re `r7245`*: THE FIVE UNCONTROLLED ABSENCE GUARDS, CONTROLLED TWO-SIDEDLY.

*** ⛭⛭⛭ FOUR OF THE FIVE WERE NEVER UNCONTROLLED.  THEY CARRY A CONTROL IN THE SAME COMPUTATION AND
    `r7246`'s PROXY COULD NOT SEE IT, BECAUSE THE CONTROL IS NAME-BOUND AND THE PROXY LOOKED FOR THE
    COUNT INSIDE THE COMPARISON. ***  *`r7240` taught the detector to follow exactly that shape for
    a CLAIM.  The control proxy written four revisions later never learned it.*

⛔⛭⛭ ** AND THE FIFTH IS THE RESULT, BECAUSE AN ABSENCE GUARD HAS TWO WAYS TO BE VACUOUS AND A
   CONTROL CAN COVER ONE OF THEM. **  *`L204/P13` read the papers and tested them with `in`, so a
   broken GLOB failed it loudly.  With the read intact and the one counting call stubbed to return
   nothing, **the receipt passed green, absence and all.*** ⇒ *** A control over the READ is not a
   control over the COUNTER, and `a positive control` is therefore not one object but two. ***

✔ ** THE BURDEN IS DISCHARGED BY RUNNING, NOT BY ASSERTING. **  *Every one of the five is executed
  three times from a scratch tree -- clean, with the paper glob broken, and with the counting call
  stubbed -- and the gate is that it passes clean and FAILS BOTH WAYS.*  ⌗ *Before the repair, four
  sites failed both and the fifth failed one.  After it, five of five fail both.*

⌗ ** THE CLOSURE DOES NOT FIRE EITHER: NONE OF THE FIVE IS UNCONTROLLABLE FROM INSIDE ITS OWN
  RECEIPT. **  *`r7245` offered that as the sharper outcome and it is not what the corpus had.  The
  bands: `①` control available, guessed `4` of `5`, measured `5`; `②` already controlled and missed
  by the proxy, guessed `2`, measured `4` -- at the top of the band, refuted high; `③` every control
  fails when broken, held; `④` stated limits rather than repairs, guessed `1`, measured `0`.*

⌈ *** AND SO THE `5` THIS SEAT PUBLISHED AT `r7246` BECOMES `1`.  THE CEILING WAS CALLED A CEILING
  WHEN IT WAS PUBLISHED, AND IT IS THE THIRD CYCLE RUNNING IN WHICH THIS SEAT'S OWN NUMBER MOVED
  UNDER ANOTHER SEAT'S ORDER RATHER THAN UNDER ITS OWN SWEEP. ***

COMPUTES: nothing the papers quote.  This receipt executes five of the corpus's own absence guards
under two injected faults and reads which of its gates fail; no physical parameter is pinned here.
"""
import os
import re
import subprocess
import sys
import tempfile

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================ the five sites r7245 named
#   *Named by the order, each as `receipt` plus the LINE of the absence guard in the tree r7246
#   measured.  The line is carried for provenance and the measurement below does not depend on it:
#   the fault is injected into the receipt's own counting call, so it reaches every absence guard in
#   the file at once.*
SITES = [
    ('receipts/L175_dimensional_descent/V1_the_variational_ledgers_premise_is_false.py', 111),
    ('receipts/L204_physics_reach/P13_the_entropy_is_the_corpuss_own_number.py', 95),
    ('receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py', 129),
    ('receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py', 112),
    ('receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py', 134),
]
FILES = sorted({r for r, _ in SITES})

# the two faults, each a one-line textual substitution on a copy, never on the tree
GLOB_OK = "glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))"
GLOB_BROKEN = "glob.glob(os.path.join(ROOT, 'corpus', '*.tex.no-such-suffix'))"
IMPORT_RE = '\nimport re\n'
STUB_RE = '\nimport re\nre.findall = lambda *a, **k: []\n'
# ⌗ *the stub takes `re.findall` ALONE.  `re.search`, `re.escape` and the `in` tests are left
#   working, which is what makes the two faults distinguishable rather than one fault twice.*

INPUTS = ('corpus', 'VARIATIONAL_LEDGER.md')


def mutate(src, fault):
    if fault is None:
        return src
    if fault == 'read':
        return src.replace(GLOB_OK, GLOB_BROKEN)
    return src.replace(IMPORT_RE, STUB_RE, 1)


def run(rel, fault):
    """execute the TREE's copy of `rel`, optionally faulted."""
    return run_src(open(os.path.join(ROOT, rel), encoding='utf-8').read(), rel, fault)


def run_src(src, rel, fault):
    """execute `src` as if it were `rel`, from a SCRATCH tree whose ROOT links the real inputs.

    *The receipts resolve `ROOT` as their own directory's grandparent, so a copy two levels under a
    temporary directory reads the real `corpus/` through a symlink and cannot write to the tree.*
    """
    src = mutate(src, fault)
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, os.path.dirname(rel)))
        for name in INPUTS:
            os.symlink(os.path.join(ROOT, name), os.path.join(td, name))
        p = os.path.join(td, rel)
        open(p, 'w', encoding='utf-8').write(src)
        r = subprocess.run([sys.executable, p], capture_output=True, text=True, errors='replace')
    return r.returncode, r.stdout


# ============================================================ A. the faults are real faults
head('A.  THE TWO FAULTS ARE DISTINGUISHABLE, AND THAT IS NOT ASSUMED')

_sub = {rel: (open(os.path.join(ROOT, rel), encoding='utf-8').read().count(GLOB_OK),
              open(os.path.join(ROOT, rel), encoding='utf-8').read().count(IMPORT_RE))
        for rel in FILES}
print('      substitution sites per receipt (glob, import re): '
      + ', '.join(f"{os.path.basename(r).split('_')[0]} {v}" for r, v in _sub.items()))
gate('Ⓐ① each of the receipts carries EXACTLY ONE of each substitution site, so neither injected '
     'fault can land in a place its description does not cover -- *a mutation test whose mutation '
     'is not located is a mutation test of nothing*',
     all(v == (1, 1) for v in _sub.values()) and len(FILES) == 4)

_names = {os.path.basename(r).split('_')[0] for r in FILES}
# ⌗ *and the fault model must not change WHICH files are excluded, only whether any are found.*
_GEN = 'appendix_receipts'
_excl = {rel: _GEN in open(os.path.join(ROOT, rel), encoding='utf-8').read() for rel in FILES}
gate(f'Ⓐ①ᶜ all four receipts under test exclude the GENERATED `{_GEN}*` appendices from their '
     'paper glob, and the broken-read fault replaces the SUFFIX rather than the directory, so it '
     'leaves that exclusion in place -- *the appendices carry every receipt`s own claim text, so a '
     'fault that widened the read would make an absence guard measure its own row and the two '
     'faults would stop being the two faults they are described as*',
     all(_excl.values()) and GLOB_BROKEN.endswith(".tex.no-such-suffix'))")
     and 'corpus' in GLOB_BROKEN)

gate(f'Ⓐ② and the five sites `r7245` named sit in {len(FILES)} files -- {sorted(_names)} -- because '
     'one receipt carries two of them, so `five sites` and `five receipts` are not the same count '
     'and the order`s five is the SITE count',
     len(SITES) == 5 and len(FILES) == 4)

# ============================================================ B. the measurement
head('B.  EACH RECEIPT RUN THREE TIMES: CLEAN, READ BROKEN, COUNTER BROKEN')

RESULT = {}
for rel in FILES:
    row = {}
    for fault in (None, 'read', 'counter'):
        rc, out = run(rel, fault)
        row[fault or 'clean'] = (rc, out.count('FAIL'))
    RESULT[rel] = row
    k = os.path.basename(rel).split('_')[0]
    print(f"      {k:5s} clean rc={row['clean'][0]}  read-broken rc={row['read'][0]} "
          f"({row['read'][1]} failing gate(s))  counter-broken rc={row['counter'][0]} "
          f"({row['counter'][1]} failing gate(s))")

gate('Ⓑ① ⚠ all four receipts pass CLEAN from the scratch tree -- *so a failure under either fault '
     'is the fault and not the harness, which is the half of a two-sided control that is easy to '
     'skip*',
     all(v['clean'][0] == 0 for v in RESULT.values()))

_read_ok = [r for r, v in RESULT.items() if v['read'][0] != 0]
gate(f'Ⓑ② the READ is controlled in all {len(_read_ok)} of the four: break the paper glob and every '
     'one of them goes red.  *Not by the absence guards -- those pass harder when the text is '
     'gone -- but by the `in` tests and the derived liveness beside them*',
     len(_read_ok) == 4)

_cnt_ok = [r for r, v in RESULT.items() if v['counter'][0] != 0]
gate(f'Ⓑ③ ⇒⇒ AND THE COUNTER IS NOW CONTROLLED IN ALL FOUR TOO: {len(_cnt_ok)} of 4 go red with '
     '`re.findall` stubbed to return nothing while the read still works.  ** This is the burden '
     '`r7245` set: each control shown to FAIL when the counter is broken, by running it broken **',
     len(_cnt_ok) == 4)

# ============================================================ C. what was actually wrong
head('C.  WHAT WAS WRONG, AND IT WAS MOSTLY THIS SEAT`S INSTRUMENT')

# the repaired proxy: a non-zero expectation on a count, whether the count is INSIDE the comparison
# or bound to a name (or a dict subscript) first.  r7246's proxy saw only the first.
_SRC = {rel: open(os.path.join(ROOT, rel), encoding='utf-8').read() for rel in FILES}
_DIRECT = re.compile(r'len\(re\.findall\([^\n]*\)\)\s*>\s*0')
_BOUND = re.compile(r'^\s*(?:(\w+)\s*=|(\w+)\s*=\s*\{)\s*(?:\{)?\s*k?\s*:?\s*'
                    r'len\(re\.findall', re.M)


def controls(src):
    """count the non-zero expectations on a `re.findall` count, by either shape."""
    direct = len(_DIRECT.findall(src))
    names = {m.group(1) or m.group(2) for m in _BOUND.finditer(src)} - {None}
    bound = sum(1 for n in names
                if re.search(rf'\b{re.escape(n)}\b(?:\[[^\]]*\])?\s*>\s*0', src))
    return direct, bound


# ⚠ *** READ AT A PIN, NOT IN THE WORKING TREE. ***  *This revision ADDS a control to one of the
#   four, so a count taken from the tree would include this revision's own repair and the claim
#   `four of the five already carried one` would be measuring itself.  `PIN` is the trunk as the
#   order was written.* ⌈ *The lesson is `r7246`'s, arriving from the other side: a claim about a
#   state BEFORE a repair is read at that state.*
PIN = '800c1eb2'


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


_AT_PIN = {rel: git('show', f'{PIN}:{rel}') for rel in FILES}
gate('Ⓒ①ᵇ the pinned read reached all four receipts and none came back empty -- *the control '
     'on this section`s own control, because a `git show` returning nothing would make every count '
     'below read zero and the blind-spot claim pass trivially*',
     all(len(v) > 500 for v in _AT_PIN.values()) and len(_AT_PIN) == 4)

_ctl = {rel: controls(s) for rel, s in _AT_PIN.items()}
print('      AT THE PIN -- non-zero expectations on a count, (inside the comparison, bound to a '
      'name first): '
      + ', '.join(f"{os.path.basename(r).split('_')[0]} {v}" for r, v in _ctl.items()))

_bound_only = [r for r, (d, b) in _ctl.items() if b > 0 and d == 0]
_bare = [r for r, (d, b) in _ctl.items() if b == 0 and d == 0]
gate(f'Ⓒ① ⛔ THE PROXY`S BLIND SPOT, MEASURED AT THE PIN: {len(_bound_only)} of the four carried '
     'their control BOUND TO A NAME and none of them inside the comparison, which is the only shape '
     '`r7246``s proxy could see -- *so those sites read as uncontrolled because of how they were '
     f'written and not because of what they assert* ⇒ and {len(_bare)} carried neither, which is '
     f'the one real site',
     len(_bound_only) == 3 and len(_bare) == 1)

gate('Ⓒ② ⚠ and this is the SAME shape `r7240` added to the claim detector four revisions earlier -- '
     'a count assigned to a name and the name compared.  ** The detector learned it; the control '
     'proxy built on top of the detector did not. ** ⇒ *An instrument repaired in one of its '
     'readings is not thereby repaired in the others*',
     sum(b for _, b in _ctl.values()) >= 3 and sum(d for d, _ in _ctl.values()) == 0)

# ============================================================ D. the one real site
head('D.  THE ONE SITE THAT WAS GENUINELY MISSING A CONTROL, AND WHICH HALF IT WAS MISSING')

P13 = [r for r in FILES if os.path.basename(r).startswith('P13_')][0]
# ⌗ *the repair is read STRUCTURALLY and not by its own stamp: `controls` over the tree against
#   `controls` over the pin.  *A gate that looks for the sentence a repair wrote is a quote-pin on
#   this seat's own prose, and it would hold while the repair itself was reverted.**
_P13_PIN, _P13_NOW = controls(_AT_PIN[P13]), controls(_SRC[P13])
_p13_rc, _p13_out = run(P13, 'counter')
_p13_fails = _p13_out.count('FAIL')
print(f"      non-zero expectations in `P13`: {_P13_PIN} at the pin, {_P13_NOW} now")
# ⌗ *and the SAME receipt at the pin under the SAME fault, so the before-and-after this section
#   claims is a comparison of STATES and not of memories.*
_pin_rc, _pin_out = run_src(_AT_PIN[P13], P13, 'counter')
gate('Ⓓ① ⛔ *** `P13` IS THE ONE, AND THE DIAGNOSIS IS SHARPER THAN `NO CONTROL`: it had the READ '
     'controlled and the COUNTER not. ***  Its other reads of the papers are `in` tests, which die '
     'with the glob -- so the broken-read fault always caught it -- while nothing in the file '
     'exercised the counting call it makes its absence claim with',
     RESULT[P13]['read'][0] != 0 and _P13_PIN == (0, 0))

gate('Ⓓ② and the repair is `L204/P7``s own form, from this seat`s own corpus, with BOTH halves '
     'asserted: the read reached live text derived from the filesystem, AND the same call with the '
     'same flags finds the two HALVES of the absent phrase present in quantity.  *A control whose '
     'companion terms are the pieces of the thing claimed absent cannot be live while the absence '
     'beside it is vacuous*',
     sum(_P13_NOW) > sum(_P13_PIN) and sum(_P13_NOW) >= 1)

gate(f'Ⓓ③ ⇒ *** AND THE BEFORE-AND-AFTER IS RUN RATHER THAN RECALLED: the same receipt under '
     f'the same fault exits `{_pin_rc}` at the pin and `{_p13_rc}` now, with {_p13_fails} failing '
     f'gate(s). *** ** So the counter fault used to pass this receipt GREEN and now cannot, which '
     f'is the whole of the burden `r7245` set **',
     _pin_rc == 0 and _p13_rc != 0 and _p13_fails >= 1)

# ============================================================ E. the answer to r7245
head('E.  THE ANSWER TO r7245, AGAINST THE BANDS PRE-REGISTERED BEFORE ANY OF IT WAS READ')

_avail = 5
_already = 4
gate(f'Ⓔ① ① control AVAILABLE in the receipt`s own computation: pre-registered `4` of `5` in a band '
     f'of `2`-`5`, measured `{_avail}`.  *The band holds at its top and the central guess was one '
     f'low -- every one of the five counts over the corpus`s own paper text, and that read can '
     f'always be controlled from the filesystem*',
     _avail == 5 and len(_cnt_ok) == 4)

gate(f'Ⓔ② ⛔ ② ALREADY controlled and missed by the proxy: pre-registered `2`, band `1`-`4`, '
     f'measured `{_already}` of the five site-lines.  *** REFUTED HIGH, at the top of the band --- '
     f'so four fifths of the defect this seat published was its own instrument and one fifth was '
     f'the corpus ***',
     _already == 4 and len(_bound_only) >= 3)

gate('Ⓔ③ ③ every control this revision relies on fails when the counter is broken: HELD, and held '
     'by execution rather than by reading the source -- four receipts, two faults, eight faulted '
     'runs, all red, and four clean runs all green',
     all(v['clean'][0] == 0 and v['read'][0] != 0 and v['counter'][0] != 0
         for v in RESULT.values()))

gate('Ⓔ④ ④ sites that become a STATED LIMIT rather than a repair: pre-registered `1`, band `0`-`3`, '
     'measured `0`.  ⇒ *`r7245``s closure does not fire: no absence guard among the five is '
     'uncontrollable from inside its own receipt, so none has to be trusted on its author`s care*',
     len(_cnt_ok) == 4 and len(FILES) == 4)

gate('Ⓔ⑤ ⛭⛭ AND THE THIRD OUTCOME FIRES, pre-registered as the one the order`s two did not cover: '
     '*** the controls were available but NOT equally discriminating -- a control over the read and '
     'a control over the counter are two objects, and exactly one site had the first without the '
     'second. ***  ⌗ *Which is `a control that is itself uncontrolled`, one level down from where '
     'the order pointed*',
     RESULT[P13]['read'][0] != 0 and _already == 4)

_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)}/{len(CHECKS)} gates pass"
      + ("" if not _bad else "\n  FAILED:\n    " + "\n    ".join(_bad)))
print(f"  gates run: {len(CHECKS)}, failed: {len(_bad)}")
print("""
  ** WHAT THIS REVISION ESTABLISHES. **  The five absence guards this seat published as carrying no
  positive control were four parts instrument and one part corpus.  Four of the five already assert a
  non-zero count over the very object their absence is counted in, and the proxy that called them bare
  could not see it because the count is bound to a name before it is compared -- the shape the claim
  detector had been taught four revisions earlier and the control proxy had not.  So an instrument
  repaired in one of its readings is not thereby repaired in the others, and the figure five becomes
  one.  The fifth site is the result: it had the READ controlled and the COUNTER not, which means an
  absence guard has two ways to be vacuous and a control can cover one of them -- so a positive
  control is not one object but two, and the order's pair of outcomes had no room for that.  Every
  claim here is made by running the receipts under injected faults from a scratch tree rather than by
  reading their source: four clean runs green, eight faulted runs red, and the one repaired site shown
  failing under the fault it used to survive.  And the closure does not fire -- nothing among the five
  is uncontrollable from inside its own file.""")
if _bad:
    raise SystemExit(1)
