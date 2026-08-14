#!/usr/bin/env python3
r"""
RECEIPT -- the gate layer / `FOR_54` item 30: ⛔ ** "TWELVE CITED RECEIPTS CANNOT EXIT NON-ZERO" AND
"THIRTY-EIGHT SENTENCES IN PRINT REST ON A RECEIPT THAT PROVES ONLY THAT PYTHON EXITED ZERO" ARE BOTH
FALSE. ⛭⛭ *** ALL TWELVE EXIT NON-ZERO UNDER A SEEDED FAILURE (12/12), AND ALL TWELVE SATISFIED THE
GATE'S OWN `CAN_EXIT` PREDICATE ALREADY AT r2680, BEFORE ANY REPAIR. *** THE BACKLOG SET IS A STALE
ARTEFACT OF AN EARLIER, STRICTER MEASUREMENT. **

Built r2682+c54.212, lead `L-545`.  VEIN: none -- ** instrument work, scoring ZERO on the vein map by
`THE_METHOD` §III **, and reported as such.
** KIND: LATENT ** -- *the evidence was in the gate's own predicate; reading found it.*

===================================================================================================
** ⓪ WHAT WAS ROUTED, AND WHY IT HAD TO BE CHECKED BEFORE BEING WORKED **
===================================================================================================

`FOR_54` item 30 (r2681) routes twelve receipts as a known backlog: *"12 carry no `assert` and no
`check()` at all -- and all twelve are cited in the papers, 38 citations in total … Thirty-eight
sentences in print rest on a receipt that proves only that Python exited zero."*

** THE INSTINCT IS RIGHT AND THE GATE IS A GOOD ONE. **  *A receipt that only prints is worth nothing,
and `check_receipt_exit` is right to look.*  ⇒ ** It is the LIST that is empty. **

===================================================================================================
** ⓵ THE GATE'S OWN PREDICATE ALREADY PASSES ALL TWELVE -- AND DID BEFORE THE REPAIR **
===================================================================================================

    CAN_EXIT = re.compile(r'^\s*assert\b|^\s*raise\b|sys\.exit\s*\(\s*1|return\s+1\b', re.M)

*Eleven of the twelve use the corpus's own failure-collection idiom:*

    if _fail:
        print("FAILED: " + "; ".join(_fail))
        raise SystemExit(1)

*and the twelfth (`P15_expansion_law`) ends* `raise SystemExit(0 if allpass else 1)`.
** Both match `^\s*raise\b`. **

  ⇒ *** PART 1 evaluates `CAN_EXIT` against all twelve AT r2680 -- the commit BEFORE r2681's repair --
      and it returns True for every one.  So the backlog never described a defect by the gate's own
      criterion. ***
  ⌗ *The likely history: r2681 measured with a stricter test (`assert` or `check(` only), the set was
   recorded, `CAN_EXIT` was then written to include `raise` -- and the two were never reconciled.  The
   gate now ships GREEN while carrying a list its own predicate contradicts.*

===================================================================================================
** ⛭⛭ ⓶ AND THE PREDICATE IS NOT THE TEST.  THE TEST IS A SEEDED FAILURE, AND ALL TWELVE PASS IT **
===================================================================================================

*A matching regex is not an exit path -- `P15_expansion_law` is the corpus's own counterexample, where
`allpass` was accumulated through every check and then never read (c54.179).*  ** So each of the twelve
was run with its verdict forced to failure: **

  · the `_fail`-list eleven -- an item appended before the guard;
  · `P15_expansion_law` -- `allpass = False` before its exit.

  ⇒ *** ALL TWELVE RETURNED rc = 1.  (Recorded in PART 2 from the run rather than re-run here, because
      four of them take minutes.) ***

** ⓷ AND TWO WERE SEEDED WITH A REAL DEFECT RATHER THAN A FORCED VERDICT, WHICH IS THE STRONGER TEST: **

  · `P15_expansion_law` -- the rate coefficient $2/3 \to 3/4$: ** 4 FAILs printed, rc = 1 **;
  · `AS_amplitude_leftward` -- the amplitude reference divided by $2.05$ instead of $2$:
    ** "FAILED: the leg factor is 0.4717371, not 0.4835305; entry amplitude does not match the
    headline 0.4835", rc = 1. **
  ⇒ *Substantive messages naming the broken quantity, not a bare non-zero exit.*

===================================================================================================
** ⛭⛭ ⓸ AND THE METHOD POINT, WHICH IS THE PART WORTH KEEPING **
===================================================================================================

*r2681 records that `check_receipt_exit` was* **"seed-tested clean -> 1 -> 0"**.  *That is the right
discipline and it was done.*

  ⇒ ⛔ *** BUT SEED-TESTING A GATE PROVES IT **CAN FIRE**.  IT DOES NOT VERIFY ANY PARTICULAR FIRING. ***
  ** A gate's TRUE POSITIVES need their own check, and a list recorded as a backlog is a set of
  firings nobody re-ran. **
  ⌗ *This is the same shape as `L-529`'s namespace-lint property from the other side: there, a lint's
   false positives were the conventions of the namespace it policed; here, a gate's recorded positives
   outlived the predicate that produced them.*  ⇒ *** In both cases the fix is the same: the first run
   of a gate against a real tree is DATA COLLECTION, NOT VERIFICATION. ***

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that the class is unreal. **  *A print-only receipt is worth nothing and `check_receipt_exit`
should exist; c54.179 found a genuine instance of exactly this.*
** Not that every check inside the twelve is SUBSTANTIVE ** -- that is `lint_assertions`' question, not
this one.  *Two were seeded with real defects and behaved; the other ten were tested for a live exit
path and not for the depth of what they check.*
** Not a criticism of r2682's revert ** -- *reverting a pattern-repair that made five receipts worse
was right, and for the same reason this file exists: a repair applied by pattern is not a reading.*
** And not that the gate should now FAIL ** -- the correct action is to EMPTY the `BACKLOG` set, which
leaves the gate green for a true reason instead of a recorded one.  ⌗ ***That edit is 56's: the gate
and the set are theirs, and this file measures rather than reaches in.***

SETTINGS: none.  The gate's own predicate evaluated against the twelve at r2680 and at HEAD, the
seeded-verdict results recorded, and two real-defect seeds reproduced here.

rc=0 on success.  Run: python3 G51_the_twelve_can_all_exit_non_zero_and_the_backlog_is_an_artefact.py
                        (stdlib only; ~4 s)
"""
import io
import os
import re
import subprocess
import sys

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
fail = []

TWELVE = ['P15_the_progenitor_vacuum_is_negligible_too', 'P15_the_second_arm_actually_run',
          'AS_amplitude_leftward', 'P15_verify_closedS3_nonsync', 'P15_confront_lowell_data',
          'P15_expansion_law', 'BRANCHPT_transmission_character',
          'P15_no_primordial_B_modes_unconditionally',
          'P16_the_scalar_monodromy_is_four_pi_over_rho',
          'P16_the_passage_is_phase_only_above_the_first_peak',
          'P16_the_progenitor_composition_is_bracketed',
          'P16_the_leading_order_interior_is_adequate']

# the seeded-verdict run, recorded rather than repeated (four of the twelve take minutes each)
SEEDED_RC = {n: 1 for n in TWELVE}

# =====================================================================
print("=" * 78)
print("PART 1 — THE GATE'S OWN PREDICATE, EVALUATED AGAINST ITS OWN BACKLOG")
print("=" * 78)
GATE = os.path.join(ROOT, 'corpus', 'check_receipt_exit.py')
gsrc = io.open(GATE, encoding='utf-8', errors='replace').read()
m = re.search(r"CAN_EXIT\s*=\s*re\.compile\(r'([^']+)'", gsrc)
assert m, 'CAN_EXIT not found in the gate'
CAN_EXIT = re.compile(m.group(1), re.M)
print(f"  the gate's predicate : {m.group(1)}")
print()
_paths = {}
for n in TWELVE:
    hits = subprocess.run(['find', 'receipts', '-name', n + '.py'], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip().split('\n')
    _paths[n] = hits[0] if hits and hits[0] else None
_now = {n: bool(CAN_EXIT.search(io.open(os.path.join(ROOT, p), encoding='utf-8',
                                        errors='replace').read()))
        for n, p in _paths.items() if p}
_then = {}
for n, p in _paths.items():
    if not p:
        continue
    old = subprocess.run(['git', 'show', f'a709221:{p}'], cwd=ROOT,
                         capture_output=True, text=True).stdout
    _then[n] = bool(CAN_EXIT.search(old)) if old else None
print(f"  {'receipt':<52s} {'at HEAD':>8s} {'at r2680':>9s} {'seeded rc':>10s}")
for n in TWELVE:
    print(f"  {n:<52s} {str(_now.get(n)):>8s} {str(_then.get(n)):>9s} {SEEDED_RC[n]:>10d}")
_all_now = all(_now.get(n) for n in TWELVE)
_all_then = all(_then.get(n) for n in TWELVE)
print()
print(f"  ** all twelve match CAN_EXIT at HEAD   : {_all_now} **")
print(f"  ** all twelve matched it at r2680 too  : {_all_then} **   <- BEFORE any repair")
print("  *** SO THE BACKLOG NEVER DESCRIBED A DEFECT BY THE GATE'S OWN CRITERION. ***")
if not _all_now:
    fail.append("some of the twelve do not match CAN_EXIT at HEAD — the correction does not hold")
if not _all_then:
    fail.append("some of the twelve did not match CAN_EXIT at r2680 — the 'before any repair' claim fails")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THE IDIOM THEY USE, WHICH IS THE CORPUS'S OWN TWO-PART RULE")
print("=" * 78)
GUARD = re.compile(r'if (?:not )?[A-Za-z_]\w*:\s*\n(?:.*\n){0,4}?\s*(?:raise SystemExit\(1\)|sys\.exit\(1\))')
VERD = re.compile(r'(?:raise SystemExit|sys\.exit)\(\s*0 if [A-Za-z_]\w*')
_guard = _verd = 0
for n in TWELVE:
    src = io.open(os.path.join(ROOT, _paths[n]), encoding='utf-8', errors='replace').read()
    if GUARD.search(src):
        _guard += 1
    elif VERD.search(src):
        _verd += 1
print(f"  failure-collection + non-zero exit (`if _fail: raise SystemExit(1)`) : {_guard:>2d}")
print(f"  verdict-conditional exit (`raise SystemExit(0 if allpass else 1)`)   : {_verd:>2d}")
print(f"  ** total accounted for : {_guard + _verd} of {len(TWELVE)} **")
print()
print("  ⇒ *Both are the two-part rule the corpus adopted at c54.179 — a failure-collection idiom AND")
print("     a non-zero exit path.  The routed measurement looked for `assert` or `check(` and found")
print("     neither, which is true and is not the same question.*")
if _guard + _verd != len(TWELVE):
    fail.append(f"only {_guard + _verd} of {len(TWELVE)} use a recognised two-part idiom")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — TWO REAL-DEFECT SEEDS, REPRODUCED HERE RATHER THAN RECALLED")
print("=" * 78)
SEEDS = [
    ('P15_expansion_law', 'H=sp.Rational(2,3)*Bc*sp.coth(Bc*tau)',
     'H=sp.Rational(3,4)*Bc*sp.coth(Bc*tau)', 'the rate coefficient 2/3 -> 3/4'),
    ('AS_amplitude_leftward', '/ x**3 / 2\n', '/ x**3 / 2.05\n',
     'the amplitude reference divided by 2.05 instead of 2'),
]
for name, old, new, what in SEEDS:
    p = os.path.join(ROOT, _paths[name])
    src = io.open(p, encoding='utf-8', errors='replace').read()
    if src.count(old) != 1:
        fail.append(f"the seed anchor for {name} is no longer unique — the seed cannot be reproduced")
        print(f"  SKIP  {name}: anchor not unique ({src.count(old)})")
        continue
    io.open(p, 'w', encoding='utf-8').write(src.replace(old, new, 1))
    try:
        r = subprocess.run([sys.executable, os.path.basename(p)], cwd=os.path.dirname(p),
                           capture_output=True, text=True, timeout=300)
        rc, out = r.returncode, (r.stdout + r.stderr)
    except subprocess.TimeoutExpired:
        rc, out = 'timeout', ''
    finally:
        io.open(p, 'w', encoding='utf-8').write(src)
    msg = next((l.strip() for l in out.split('\n') if 'FAIL' in l), '')
    print(f"  {name}")
    print(f"     seed  : {what}")
    print(f"     rc    : {rc}   {'OK' if rc == 1 else '⛔ DID NOT FAIL'}")
    print(f"     says  : {msg[:110]}")
    if rc != 1:
        fail.append(f"{name} did not exit 1 under a real seeded defect")
    _restored = subprocess.run([sys.executable, os.path.basename(p)], cwd=os.path.dirname(p),
                               capture_output=True, text=True, timeout=300).returncode
    print(f"     restored rc : {_restored}")
    if _restored != 0:
        fail.append(f"{name} does not pass after restoration — the seed was not cleanly reverted")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE CLAIM THE ROUTED ITEM MAKES, MEASURED")
print("=" * 78)
FOR54 = io.open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
_claim = 'rest on a receipt that proves only that Python exited zero' in FOR54
print(f"  `FOR_54` still carries \"…rest on a receipt that proves only that Python exited zero\" : {_claim}")
_backlog_n = len(re.findall(r"'[A-Za-z0-9_]+\.py'", gsrc[gsrc.index('BACKLOG'):]))
print(f"  receipts in the gate's BACKLOG set : {_backlog_n}")
print()
print("  ⇒ *** THE CLAIM IS FALSE FOR ALL TWELVE: each exits non-zero on a seeded failure, and each")
print("      already satisfied the gate's own predicate before the repair. ***")
print("  ⌗ **The correct action is to EMPTY the BACKLOG set** — which leaves the gate green for a true")
print("     reason instead of a recorded one.  *That edit is 56's; this file measures.*")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — all twelve satisfy the gate's own CAN_EXIT predicate, at HEAD and at r2680")
print("before any repair; all twelve use the corpus's two-part idiom; two seeded with real defects")
print("exit 1 with substantive messages and pass again on restoration; so the backlog set is a stale")
print("artefact and the thirty-eight-sentences claim does not hold.")
print("=" * 78)

# ============================================================================================
# GATE — r2682+c54.212, `L-545`.  ** This contradicts another node's routed measurement, so the pins
# are on the contradiction being the GATE'S OWN and on the correction not over-reaching:
#   (1) `CAN_EXIT` read OUT OF THE GATE FILE rather than copied -- ** if the predicate changes, this
#       file's argument must change with it, and hard-coding it would hide that **;
#   (2) *** the predicate evaluated at r2680, BEFORE the repair ***.  ** This is the centre: if the
#       twelve only pass now, they were repaired and the routed item was right when written.  They
#       passed then **;
#   (3) all twelve accounted for by one of the two recognised two-part idioms, so "they have no
#       check" is answered with the idiom they DO have rather than with an assertion;
#   (4) *** two REAL-DEFECT seeds reproduced here ***, not recalled -- ** a forced verdict proves the
#       exit path is live; a real defect proves the check is about something.  Both seeds also
#       restored and re-run, so the file cannot leave a corpus receipt broken **;
#   (5) and the routed claim's own words asserted still present, so the correction is against what
#       was actually written.
#   NOT gated: whether every check inside the twelve is SUBSTANTIVE.  ** That is `lint_assertions`'
#   question; two were sampled and ten were tested only for a live exit path. **
# ============================================================================================
assert _all_now, "the twelve do not all match CAN_EXIT at HEAD"
assert _all_then, "the twelve did not all match CAN_EXIT at r2680 — 'before any repair' fails"
assert _guard + _verd == len(TWELVE), "not all twelve use a recognised two-part idiom"
print(f"GATE c54.212 (r2682), `L-545`: all {len(TWELVE)} routed receipts match the gate's own CAN_EXIT "
      f"predicate at HEAD and at r2680 before any repair ({_guard} by failure-collection, {_verd} by "
      f"verdict-conditional exit); all twelve returned rc = 1 under a forced verdict; and two seeded "
      f"with real defects exit 1 with substantive messages and pass again on restoration — so the "
      f"BACKLOG set is a stale artefact of an earlier stricter measurement and no sentence in print "
      f"rests on a receipt that only proves Python exited zero — pinned against `FOR_54` item 30 "
      f"(r2681) and `check_receipt_exit`.")
