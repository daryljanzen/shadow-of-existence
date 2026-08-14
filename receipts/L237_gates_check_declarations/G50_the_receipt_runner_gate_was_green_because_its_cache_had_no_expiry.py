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
_x1 = os.path.join(ROOT, 'receipts', 'L150_the_datum',
                   'X1_the_ratio_is_a_clock_reading_not_a_carried_datum.py')
_p16 = os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex')
_ok_x1 = os.path.exists(_x1) and os.path.exists(_p16)
if _ok_x1:
    raw = io.open(_p16, encoding='utf-8', errors='replace').read()
    body = '\n'.join((ln[:m.start()] if (m := re.search(r'(?<!\\)%', ln)) else ln)
                     for ln in raw.split('\n'))
    S = 'eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m'
    in_raw = S in re.sub(r'\s+', ' ', raw)
    in_body = S in re.sub(r'\s+', ' ', body)
    asserted = S in io.open(_x1, encoding='utf-8', errors='replace').read()
    print(f"     `X1` asserts the string against P16      : {asserted}")
    print(f"     the string is in P16 read RAW            : {in_raw}   ** so the check passes **")
    print(f"     the string is in P16's printed BODY      : {in_body}   ** and the paper never says it **")
    if not (asserted and in_raw and not in_body):
        fail.append("the X1 instance no longer reproduces — the finding must be re-stated, not left asserted")
else:
    fail.append("X1 or P16 is missing — the instance cannot be checked")
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
    ("the runner STAMPS what it ran against", src_runner, r'TREE-DIGEST: \{tree_digest\(\)\}'),
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
_ran = 'pass,' in _p.stdout and _p.returncode == 0
_stamped = re.search(r'TREE-DIGEST:\s*([0-9a-f]{8,})', _p.stdout)
print(f"  a one-receipt run exits 0        : {_ran}")
print(f"  and carries its own digest       : {bool(_stamped)}"
      f"  ({_stamped.group(1) if _stamped else '—'})")
print(f"  which matches the tree here      : {bool(_stamped) and _stamped.group(1) == tree_digest()}")
print()
print("  *Before the de-shadowing this call died on `queue.SimpleQueue` without running a receipt.*")
if not _ran:
    fail.append(f"the runner still does not run: {(_p.stdout + _p.stderr).strip()[-200:]}")
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
#   (5) and *** the runner RUN ***, exiting 0 with a digest matching this tree.  ** An instrument
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
