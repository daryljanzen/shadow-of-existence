#!/usr/bin/env python3
"""
RECEIPT -- the gate layer: ** I SHIPPED A WARNING TO ANOTHER NODE AND DID NOT RUN IT AGAINST MYSELF.
RUNNING IT FOUND THAT MY WARNING WAS NOT A CLASS -- ONE INSTANCE, ALREADY KNOWN -- AND THAT THE
CONTROL I HAD TO BUILD TO SHOW THAT FOUND SOMETHING LARGER: ⛭⛭ *** `check_receipts_run` REPORTED "NO
RECEIPT FAILS FOR A REASON INSIDE THE CORPUS" FROM A CACHE WRITTEN 294 COMMITS EARLIER, WHILE 24 OF
120 CORPUS-READING RECEIPTS WERE FAILING. *** **

Built r2656+c54.208, lead `L-541`.  VEIN: none -- ** instrument work, scoring ZERO on the vein map by
`THE_METHOD` §III **, and reported as such.

===================================================================================================
** ⓪ WHY THIS TURN STARTED HERE, AND IT IS r2656's OWN RULE **
===================================================================================================

r2656: *"When you write down a failure another node will make, run the check against yourself before
shipping the warning.  A failure mode you can describe precisely is one you're already committing."*

** I HAD SHIPPED EXACTLY SUCH A WARNING ONE REVISION EARLIER. **  `L-535` routed to 56: *a claim can
live in a `%` header comment, where no reader sees it and no gate reads it* -- and I closed it with
*"I have no standing to sweep your headers."*  ⇒ ** That is the deflection the rule names. **  The
sweep needed no standing; it is a measurement, not an edit.

===================================================================================================
** ⓵ THE WARNING, RUN AGAINST THE WHOLE TREE -- AND IT IS NOT A CLASS **
===================================================================================================

  ** 158,062 characters of comment text across the seventeen papers ** -- about one paper's worth.
  *So the surface is real.*  ** The propagation is not. **

  METHOD: strip every comment from every `.tex`, run all 120 corpus-reading receipts, ** and compare
  against the SAME RUN ON THE UNSTRIPPED TREE ** (PART 1).  A receipt that fails only when comments
  go is a receipt whose check is satisfied by text the paper does not print.

    stripped-tree failures  27
    baseline failures       24        <- the control
    ** comment-dependent     3 **, of which TWO check comments BY DESIGN
       (`P15_the_locus…` checks a header STATUS block; `P17_the_frontier_item…` checks the
        provenance of the very sentence that raised `L-535`)
    ⇒ *** ONE accidental instance: `X1`, the one already on the record. `L-535` is an INSTANCE and
        not a class, and this file says so. ***

⚠ ** AND I GOT THIS WRONG FIRST. **  *The 27 was reported to myself as the finding before any control
existed.  `P11_CR_fixes_the_place_not_the_couplings` failed on the STRIPPED tree and on the plain one
alike -- its absence claim about `N_eff` had been falsified by my own c54.205 paragraph.*  ⇒ ** An
experiment with no control returns the size of the tree, not the size of the effect. **  *Recorded on
the unfavourable side of `THE_BASE_RATE`: the instrument built to check a warning needed the same
discipline the warning was about.*

===================================================================================================
** ⛭⛭ ⓶ AND THE CONTROL IS WHERE THE REAL FINDING WAS **
===================================================================================================

  *** 24 OF 120 CORPUS-READING RECEIPTS FAIL ON THE CURRENT TREE, RIGHT NOW. ***

  ** AND THE WIRED GATE SAYS THEY DO NOT. **  `check_receipts_run` prints:
      *"Last run: 264 pass, 8 fail … No receipt fails for a reason inside the corpus."*

  ⇒ ** IT IS READING `receipts/RUN_RESULT.txt`, WHICH WAS LAST WRITTEN AT r2419. **
     *HEAD is r2656.*  ** 294 commits.  276 registered receipts then; 436 now. **
     ⇒⇒ *** A CACHE WITH NO EXPIRY IS NOT A MEASUREMENT.  The gate was green because it was OLD,
         which is the direction that looks like success -- and r2654 had already named that pattern:
         "four instrument corrections in this session alone, every one reporting LOW." ***

  ⌗ *And several of the 24 are red because a paper CORRECTLY moved: `L-527` named $N_{\\rm eff}$ in
   P16, which falsifies three receipts asserting it is at zero everywhere.*  ** That is a receipt
   doing its job.  What is wrong is that nothing re-ran it, so the falsification sat unread. **

===================================================================================================
** ⓷ AND THE SECOND DEFECT, WHICH WOULD HAVE HIDDEN THE FIRST **
===================================================================================================

  ** `scripts/queue.py` SHADOWS THE STDLIB `queue`. **  Run as `python3 scripts/run_all_receipts.py`,
  `scripts/` goes first on `sys.path`, and `concurrent.futures` imports `queue`:

      AttributeError: module 'queue' has no attribute 'SimpleQueue'

  *The runner dies in its first second, before one receipt runs.*
    · `RUN_RESULT.txt` last written **r2419**
    · `scripts/queue.py` added **r2615**  ⇒ ** the runner has been unrunnable for 41 commits **
  ⇒ *** SO THE STALENESS (253 commits) PREDATES THE SHADOW, AND THE SHADOW MADE IT UNFIXABLE FOR THE
      LAST 41 -- and a crash presents as "no verdict line", which reads as NOT YET RUN rather than as
      BROKEN. ***
  ⌗ *Fixed HERE by dropping the script's own directory from `sys.path`.*  ** The hazard is general --
   any script there that touches threads inherits it -- and the rename is the observer line's call,
   so it is routed rather than done under them. **

===================================================================================================
** ⓸ THE FIX, AND IT IS NOT A DATE **
===================================================================================================

  `run_all_receipts` now stamps ** TREE-DIGEST ** -- a hash of everything a receipt can READ
  (`corpus/*.tex`, `receipts/**/*.py`, `computations/**/*.py`).  `check_receipts_run` recomputes it
  and ** FAILS on a mismatch or on its absence **.
  ⇒ *Deliberately not the git HEAD: an exact-HEAD match would fail on every commit touching a
   register file, and a gate that fails for nothing trains its caller to skip it.  Hashing only what
   a receipt can read goes stale exactly when the verdict could be wrong, and never otherwise.*

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that the 24 are wrong. **  *Most are stale ABSENCE claims falsified by revisions that filled
the absence -- correct behaviour, unread.  Triage is the ingestion's, not this file's.*
** Not that `L-535` was a false alarm ** -- the instance is real and the comment surface is 158k
characters; what is withdrawn is the word CLASS.
** Not that `scripts/queue.py` should be renamed ** -- that is routed, not done.
** And not that this gate now proves the receipts pass ** -- it proves the number on file is about
the tree in front of it.

SETTINGS: none.  Two full runs of the 120 corpus-reading receipts (stripped and control), the digest
recomputed here, and both staleness failure modes seeded.

rc=0 on success.  Run: python3 G50_the_receipt_runner_gate_was_green_because_its_cache_had_no_expiry.py
                        (stdlib only; ~5 s)
"""
import glob
import hashlib
import io
import os
import re
import subprocess
import sys

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
fail = []

# =====================================================================
print("=" * 78)
print("PART 1 — THE COMMENT SURFACE IS REAL AND THE PROPAGATION IS NOT")
print("=" * 78)
full = trail = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
    if 'appendix_receipts' in f:
        continue
    for ln in io.open(f, encoding='utf-8', errors='replace').read().split('\n'):
        m = re.search(r'(?<!\\)%', ln)
        if not m:
            continue
        if ln.lstrip().startswith('%'):
            full += len(ln)
        else:
            trail += len(ln[m.start() + 1:])
print(f"  full-line comment text : {full:>8,} chars   -- the corpus's standard idiom DOES drop these")
print(f"  trailing comment text  : {trail:>8,} chars   -- it does NOT, and they are provenance notes")
print(f"  TOTAL comment surface  : {full + trail:>8,} chars   ** about one paper's worth **")
if full + trail < 50_000:
    fail.append(f"the comment surface is only {full + trail} chars — the premise has changed")

print()
print("  ⇒ AND THE ONE ACCIDENTAL INSTANCE, still checkable in its own source:")
# ** r6931+70.1: THE INSTANCE IS NOW READ AT THE LAST TREE THAT CARRIED IT, AND ITS RETIREMENT AT
#    HEAD IS ASSERTED.  Class (c), STALE -- the finding is unchanged and the corpus text it was about
#    moved for its own reason. **  `0960c7aa` (r6772+66.30, "P16 brought to the same reading,
#    masthead included") rewrote the `%` masthead comment of `cosmogenesis_paper.tex`: eta is now
#    "the ONE datum of the same handover", the peak SPACING is "computed from the rate", and the
#    sentence `eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m the peak SPACING` is
#    gone from the RAW file as well as the body.  *So the live three-way test (asserted / in raw /
#    not in body) could no longer be satisfied -- not because the instance was mis-measured, but
#    because the comment that satisfied X1 was rewritten.*
#    ⇒ The finding is about r2656's tree: ONE receipt whose check was satisfied by comment text the
#      paper never printed.  That is a fact about history, so it is read from history --
#      `01c1a672` (the first parent of `0960c7aa`, the last tree carrying the sentence) -- with the
#      SAME three conditions, none relaxed.  ** And the present is asserted in its own direction:
#      the sentence is absent from P16's raw source at HEAD, so no check can be silently satisfied
#      by it any more -- X1 reading it now FAILS loudly, which is the surface doing its job. **
#      (X1's own repair is its family's, not this file's; X1 is NOT read live here, because an edit
#      to X1 must not decide whether r2656's instance existed.)
_X1_REL = 'receipts/L150_the_datum/X1_the_ratio_is_a_clock_reading_not_a_carried_datum.py'
_P16_REL = 'corpus/cosmogenesis_paper.tex'
_PIN = '01c1a672b299'          # first parent of 0960c7aa (r6772+66.30)


def _git_show(rev, rel):
    r = subprocess.run(['git', 'show', f'{rev}:{rel}'], cwd=ROOT, capture_output=True,
                       text=True, errors='replace')
    return r.stdout if r.returncode == 0 else None


S = 'eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m'


def _strip_comments(raw):
    return '\n'.join((ln[:m.start()] if (m := re.search(r'(?<!\\)%', ln)) else ln)
                     for ln in raw.split('\n'))


_x1_then = _git_show(_PIN, _X1_REL)
_p16_then = _git_show(_PIN, _P16_REL)
_p16_now_path = os.path.join(ROOT, _P16_REL)
_ok_x1 = _x1_then is not None and _p16_then is not None and os.path.exists(_p16_now_path)
if _ok_x1:
    asserted = S in _x1_then
    in_raw = S in re.sub(r'\s+', ' ', _p16_then)
    in_body = S in re.sub(r'\s+', ' ', _strip_comments(_p16_then))
    raw_now = io.open(_p16_now_path, encoding='utf-8', errors='replace').read()
    in_raw_now = S in re.sub(r'\s+', ' ', raw_now)
    print(f"     at {_PIN} (last tree before r6772+66.30):")
    print(f"       `X1` asserts the string against P16    : {asserted}")
    print(f"       the string is in P16 read RAW          : {in_raw}   ** so the check passed **")
    print(f"       the string is in P16's printed BODY    : {in_body}   ** and the paper never said it **")
    print(f"     at HEAD, the string is in P16 RAW        : {in_raw_now}   ** the comment was rewritten "
          f"at 0960c7aa, so nothing is satisfied by it now **")
    if not (asserted and in_raw and not in_body):
        fail.append("the X1 instance no longer reproduces at its pinned tree — the finding must be "
                    "re-stated, not left asserted")
    if in_raw_now:
        fail.append("the comment-only sentence is back in P16's raw source — re-measure the instance")
else:
    fail.append("X1 or P16 is missing at the pinned tree — the instance cannot be checked")
print()
print("  *** ONE instance, already on the record.  `L-535` is an INSTANCE, not a class. ***")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ⛭⛭ THE CACHE THE WIRED GATE READS, AND WHETHER IT CAN NOW GO STALE UNSEEN")
print("=" * 78)


def tree_digest():
    h = hashlib.sha256()
    for pat in ('corpus/*.tex', 'receipts/**/*.py', 'computations/**/*.py'):
        for f in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
            h.update(os.path.relpath(f, ROOT).encode())
            h.update(open(f, 'rb').read())
    return h.hexdigest()[:16]


RUNNER = os.path.join(ROOT, 'scripts', 'run_all_receipts.py')
GATE = os.path.join(ROOT, 'corpus', 'check_receipts_run.py')
src_runner = io.open(RUNNER, encoding='utf-8', errors='replace').read()
src_gate = io.open(GATE, encoding='utf-8', errors='replace').read()
WIRED = [
    # ⛔⛭ AMENDED r4524, AND THE REVISION THAT BROKE IT WAS MINE.  r4512 made the runner resumable
    #    and hoisted the digest into a variable -- `_digest = tree_digest()` then
    #    `print(f"  TREE-DIGEST: {_digest}")` -- so a check pinned to the literal expression
    #    `TREE-DIGEST: {tree_digest()}` failed on a runner that still does exactly what the check is
    #    about.  *The wiring is the claim; the spelling of the f-string is not.*
    #    ⇒ The source probe accepts the value through a variable, AND -- better than reading source
    #      at all -- the wiring is now RUN: a real invocation's stamp is compared against the digest
    #      computed independently here.  ** An instrument that reads a file has not run it, which is
    #      the sentence this whole gate exists under. **
    ("the runner STAMPS what it ran against", src_runner,
     r'TREE-DIGEST: \{(?:tree_digest\(\)|_?digest)\}'),
    ("the runner computes the digest over what a receipt can READ", src_runner,
     r"for pat in \('corpus/\*\.tex', 'receipts/\*\*/\*\.py'"),
    ("⛭ the gate RECOMPUTES it and compares", src_gate, r"now = tree_digest\(\)"),
    ("the gate FAILS on a mismatch", src_gate, r'STALE RESULT'),
    ("the gate FAILS when no digest is present at all", src_gate, r'NO TREE-DIGEST'),
    ("and the runner is de-shadowed from scripts/queue.py", src_runner,
     r"sys\.path\[:\] = \[p for p in sys\.path if os\.path\.abspath\(p or '\.'\) != _HERE\]"),
]
for what, hay, pat in WIRED:
    ok = re.search(pat, hay) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"the fix is not wired: {what}")

# ** AND THE WIRING, RUN RATHER THAN READ. **  The runner is invoked with a filter that matches no
# receipt, so it costs nothing and still prints its header; the digest it stamps must equal the one
# computed here from the same definition.  *A source probe can only say the line is present.*
_own = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'run_all_receipts.py'),
                       '--only', '__g50_matches_no_receipt__'],
                      cwd=ROOT, capture_output=True, text=True, errors='replace', timeout=300)
_m = re.search(r'TREE-DIGEST:\s*([0-9a-f]{8,})', _own.stdout)
_h = hashlib.sha256()
for _pat in ('corpus/*.tex', 'receipts/**/*.py', 'computations/**/*.py'):
    for _f in sorted(glob.glob(os.path.join(ROOT, _pat), recursive=True)):
        _h.update(os.path.relpath(_f, ROOT).encode())
        _h.update(open(_f, 'rb').read())
_want = _h.hexdigest()[:16]
print(f"  {'OK ' if (_m and _m.group(1) == _want) else 'MISSING'}  ⛭ and the stamp is the digest it "
      f"computed, RUN not read: runner said {_m.group(1) if _m else '(none)'}, recomputed {_want}")
if not _m or _m.group(1) != _want:
    fail.append("the runner's stamped digest does not match the digest recomputed from its own "
                "definition -- the wiring is present in source and wrong in fact")

print()
print("  ⛔ AND THE SHADOW ITSELF, which is why the runner could not be re-run at all:")
_shadow = os.path.exists(os.path.join(ROOT, 'scripts', 'queue.py'))
print(f"     scripts/queue.py exists and shadows the stdlib `queue` : {_shadow}")
_r = subprocess.run([sys.executable, '-c',
                     'import sys; sys.path.insert(0, %r); import queue; print(queue.__file__)'
                     % os.path.join(ROOT, 'scripts')], capture_output=True, text=True)
_shadowed = 'scripts/queue.py' in _r.stdout
print(f"     with scripts/ first on sys.path, `import queue` resolves to a corpus file : {_shadowed}")
if _shadow and not _shadowed:
    fail.append("scripts/queue.py exists but no longer shadows — the diagnosis must be re-stated")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE RUNNER ACTUALLY RUNS NOW, VERIFIED BY RUNNING IT")
print("=" * 78)
_p = subprocess.run([sys.executable, RUNNER, '--only', 'L150_the_datum',
                     '--jobs', '2', '--timeout', '60'],
                    cwd=ROOT, capture_output=True, text=True, timeout=240)
# ** r6931+70.1: "THE RUNNER RUNS" IS NOW ASSERTED AS THE RUNNER'S OWN ACCOUNTING, NOT AS ANOTHER
#    RECEIPT'S EXIT CODE.  Class (c), STALE -- the finding (the runner is de-shadowed and runs) is
#    unchanged; what moved was the one receipt this check borrowed. **  The old predicate was
#    `'pass,' in stdout and returncode == 0`.  Since r6476 the runner exits 1 whenever a receipt in
#    its filter FAILS, so on `--only L150_the_datum` it was really asserting that X1 passes -- and X1
#    has failed since the r6772+66.x handover rewrite (`507d2e99`, `89d23854`, `0960c7aa`), measured
#    here by running this file in worktrees: GREEN at b96e1a49 (r6502) and 2290a528 (r4287), RED at
#    91751daa (r6774) and after.  *This file's own docstring disclaims exactly that: "not that this
#    gate now proves the receipts pass".*
#    ⛔ AND THE BORROWING IS WHAT FED `check_receipts_run` ITS WRONG VERDICT (r6921/r6923): red, this
#      file printed the one-family runner's `0 pass, 1 fail, 0 over timeout` into the suite's
#      captured output, and the unanchored pattern read it.  So G50 has been emitting that line only
#      since ~r6772, not since 2026-08-14.
#    ⇒ The check now demands MORE of the runner than before, not less: (i) no crash -- no Traceback,
#      no `SimpleQueue`; (ii) the verdict line found by the gate's OWN anchored pattern
#      `(?m)^  N pass, N fail, N over timeout`; (iii) that verdict COVERS the registered set the
#      runner announced for the filter (pass+fail+slow == N registered, N >= 1); and (iv) the exit
#      code AGREES with the verdict -- 0 iff nothing failed or overran, 1 otherwise.  A runner that
#      crashed, printed nothing, under-counted, or exited 0 over a failure fails every one of these.
#      X1's own verdict is REPORTED, not asserted -- its family owns it.
_crash = ('Traceback' in _p.stderr) or ('SimpleQueue' in (_p.stdout + _p.stderr))
_v = re.search(r'(?m)^  (\d+) pass, (\d+) fail, (\d+) over timeout, in (\d+)s', _p.stdout)
_reg = re.search(r'RUN-ALL-RECEIPTS -- (\d+) registered receipt', _p.stdout)
_np, _nf, _ns = (int(_v.group(1)), int(_v.group(2)), int(_v.group(3))) if _v else (None,) * 3
_nreg = int(_reg.group(1)) if _reg else None
_covers = bool(_v and _reg and _nreg >= 1 and _np + _nf + _ns == _nreg)
_rc_agrees = bool(_v) and _p.returncode == (0 if (_nf == 0 and _ns == 0) else 1)
_ran = (not _crash) and _covers and _rc_agrees
print(f"  the runner ran without crashing  : {not _crash}")
print(f"  its anchored verdict line        : "
      f"{(str(_np) + ' pass, ' + str(_nf) + ' fail, ' + str(_ns) + ' over timeout') if _v else '(none)'}"
      f"  of {_nreg} registered")
print(f"  and the verdict covers the set   : {_covers}")
print(f"  and its exit code ({_p.returncode}) agrees  : {_rc_agrees}")
print(f"  (X1 itself {'passes' if _v and _nf == 0 else 'FAILS'} at this tree -- reported, not "
      f"asserted: that is L150's finding, not this file's)")
_stamped = re.search(r'TREE-DIGEST:\s*([0-9a-f]{8,})', _p.stdout)
print(f"  and carries its own digest       : {bool(_stamped)}"
      f"  ({_stamped.group(1) if _stamped else '—'})")
print(f"  which matches the tree here      : {bool(_stamped) and _stamped.group(1) == tree_digest()}")
print()
print("  *Before the de-shadowing this call died on `queue.SimpleQueue` without running a receipt.*")
if not _ran:
    # one line, ' / '-joined: never re-emit a runner verdict at line start inside this file's output
    fail.append("the runner does not run and account for its set: "
                + ' / '.join(l.strip() for l in (_p.stdout + _p.stderr).split('\n') if l.strip())[-200:])
if not _stamped or _stamped.group(1) != tree_digest():
    fail.append("the runner's stamp does not match the digest computed here")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the comment surface is one paper's worth and its propagation is one known")
print("instance; the runner stamps the tree it ran against and the gate fails on a mismatch or an")
print("absent stamp; the stdlib shadow that made the runner unrunnable is removed; and the runner")
print("runs, in place, carrying a digest that matches this tree.")
print("=" * 78)

# ============================================================================================
# GATE — r2656+c54.208, `L-541`.  ** The defect here was a GREEN GATE, so every pin is on the new
# gate's ability to be RED, and on the diagnosis staying reproducible rather than remembered:
#   (1) the comment surface measured, not recalled -- ** if it had collapsed, `L-535`'s premise
#       would be gone and this file would be arguing about nothing **;
#   (2) *** the X1 instance reproduced end to end ***: the string asserted, present in the RAW file,
#       ABSENT from the printed body.  ** All three are needed; any one of them changing turns the
#       finding into a memory **;
#   (3) six wiring checks, of which the load-bearing two are that the gate FAILS on a mismatch and
#       FAILS on an absent stamp -- ** the old gate's only failure mode was a truncated file, which
#       is why a 294-commit-old result read as current **;
#   (4) the stdlib shadow demonstrated by resolving `import queue` in a subprocess, not asserted;
#   (5) and *** the runner RUN ***, its anchored verdict covering its set and its exit code agreeing
#       with that verdict (r6931+70.1; was "exiting 0"), with a digest matching this tree.  ** An instrument
#       that cannot finish is indistinguishable from one that has not been started, and that
#       ambiguity is what kept this hidden for 41 commits. **
#   SEEDED SEPARATELY (both fired): a result file with a WRONG digest claiming "436 pass, 0 fail"
#   -> FAIL; and the actual r2419 file that had been read as current -> FAIL.
#   NOT gated: the 24 failing receipts.  ** Their triage is the ingestion's, and this file's claim
#   is that the number is now VISIBLE, not that it is zero. **
# ============================================================================================
assert full + trail >= 50_000, "the comment surface has collapsed — the premise is gone"
assert _ok_x1, "the X1 instance cannot be checked"
for what, hay, pat in WIRED:
    assert re.search(pat, hay), f"the fix is not wired: {what}"
assert _ran, "the receipt runner still does not run"
assert _stamped and _stamped.group(1) == tree_digest(), "the runner's stamp does not match this tree"
print(f"GATE c54.208 (r2656), `L-541`: {full + trail:,} characters of comment text across the papers "
      f"and ONE receipt whose check is satisfied by it; `RUN_RESULT.txt` was written at r2419 and read "
      f"as current at r2656, 294 commits and 160 registered receipts later, while 24 of 120 "
      f"corpus-reading receipts were failing; the runner now stamps TREE-DIGEST {tree_digest()} and "
      f"the gate fails on a mismatch or an absent stamp, both seeded; and the stdlib `queue` shadow "
      f"that made the runner unrunnable since r2615 is removed — pinned against r2656's own rule.")
