#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `spectra/cc66_lowell_sweep.npz` IS NO LONGER UNPLACEABLE: A PRODUCER IS IN THE
REPOSITORY, EVERY ONE OF ITS EIGHT BANKED CONFIGURATIONS IS RE-DERIVED, AND THE BANK IS THAT
PRODUCER'S OUTPUT ROUNDED TO FOUR DECIMALS -- EXACTLY, ON ALL FIFTY-SIX VALUES. **

*** AND THE ENGINE IS NOT A SECOND COPY OF ANYTHING: the producer READS the arm-B harness out of the
registered receipt that owns it, because a duplicated engine can drift from the original silently --
which is the defect class this corpus keeps naming. ***

Built r7109+cc66.86 (node 66, code seat), answering the second half of `r7109` ⓷ for this artefact.

===================================================================================================
** WHAT WAS ASKED **
===================================================================================================

`70`'s provenance audit: *"a low-l sweep whose keys name their own configurations, partly
self-describing, with no producer in the repository ... **re-derive** (cc66's queue), or write its
producer into the repository.  It is load-bearing for a registered receipt and a published figure."*

** Both are done here, because each alone is weaker than it looks. **  A producer with no
re-derivation is a claim about a file; a re-derivation with no producer closes nothing the next time
the question is asked.

  PART 1  ** THE PRODUCER IS TRACKED, AND IT DOES NOT CARRY ITS OWN ENGINE. **  Asserted at source:
          `r7109_directions/rederive_lowell_sweep.py` parses the registered receipt and exec's only
          its arm-B definitions.  *If it had copied them, this check would say so.*
  PART 2  ** ITS CASE TABLE IS EXACTLY THE BANKED KEY SET -- no key unproduced, no case unbanked. **
          Set equality, not a count.
  PART 3  ** ONE CONFIGURATION IS RE-DERIVED LIVE, EVERY RUN. **  About 80 s.  *So the producer is
          EXERCISED by this receipt rather than vouched for; a producer that no longer runs would
          fail here and not in a comment.*
  PART 4  ** AND THE FULL EIGHT ARE READ FROM THE PRODUCER'S OWN TRACKED RECORD. **  The DECOUPLED
          variant is ~9 minutes a configuration, which no receipt should spend; the record is banked
          beside the producer that wrote it, so it is not a new unplaceable.
  PART 5  ** WHAT THE RESIDUAL IS, NAMED RATHER THAN TOLERATED. **  The bank stores four decimals.
          `round(live, 4)` equals the banked value identically; the raw difference is at most
          5e-5, which is half the last stored digit.  ** So the agreement is not "within tolerance":
          the bank IS the producer's output, rounded. **

===================================================================================================
** WHAT THIS DOES NOT CLAIM **
===================================================================================================

** It does not claim the sweep's PHYSICS is re-validated. **  That is the registered receipt's job
and it does it on every run.  This file closes a PROVENANCE question: that the banked numbers come
from code in this repository and can be made again.  ** And it does not claim the four-decimal
storage was a good choice **; it was not this seat's, it loses nothing that matters at these
multipoles, and it is named here so that the next reader does not mistake 5e-5 for a disagreement.

** COMPUTES: nothing of its own. ***  PART 3 runs the registered receipt's own arm-B harness at
   `BH0/BOM` = (67.40, 0.3150) with `ZEND=0 NTAU=150000 KLO=0.1 NLOW=480`, which is the banked
   `FROZEN_control_KLO_0_1` key's own name spelled as an environment.  *Every parameter is the
   banked key's; this file chooses none of them.*

SETTINGS: the configurations are the banked keys' own names.  ** No run here can move the figures:
the question is whether the repository can MAKE them, and it is answered by making them. **

rc=0 on success.  Run: python3 P15_the_lowell_sweep_is_reproduced_by_a_producer_in_the_repository_and_the_bank_is_that_producers_output_rounded.py
                       (numpy scipy, ~90 s)
"""
import ast
import json
import os
import subprocess
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
PRODUCER = os.path.join(BW, 'r7109_directions', 'rederive_lowell_sweep.py')
RECORD = os.path.join(BW, 'r7109_directions', 'lowell_rederive.json')
BANK = os.path.join(BW, 'spectra', 'cc66_lowell_sweep.npz')
OWNER = os.path.join(HERE, 'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
DP = 4                     # the bank's stored decimals, established in PART 5

# =====================================================================
print("=" * 100)
print("  PART 1 -- ** THE PRODUCER IS TRACKED, AND ITS ENGINE IS THE RECEIPT'S AND NOT A COPY **")
print("=" * 100)
INPUTS = [PRODUCER, RECORD, BANK, OWNER]
try:
    subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch'] + INPUTS,
                   check=True, capture_output=True)
    print(f"  all {len(INPUTS)} inputs are tracked by git in this checkout")
except subprocess.CalledProcessError as exc:
    fail.append("an input is not tracked by git: "
                + exc.stderr.decode('utf-8', 'replace').strip().split('\n')[0][:120])
except (OSError, FileNotFoundError):
    absent = [p for p in INPUTS if not os.path.exists(p)]
    if absent:
        fail.append(f"{len(absent)} input(s) absent and git unavailable to check tracking")
    else:
        print(f"  git unavailable here; all {len(INPUTS)} inputs exist (tracking unchecked)")

PSRC = open(PRODUCER, encoding='utf-8', errors='replace').read()
OSRC = open(OWNER, encoding='utf-8', errors='replace').read()
# ** the engine must be READ, not copied: the producer parses the receipt and exec's its definitions
reads = ('ast.parse(open(RECEIPT' in PSRC and "exec(compile(ast.Module" in PSRC)
print(f"  the producer parses the registered receipt and exec's its definitions: {reads}")
if not reads:
    fail.append("the producer no longer reads its engine out of the receipt -- it may have copied it")
# and the giveaway if it HAD copied it: the receipt's harness text appearing in the producer
_marker = "import os, sys, contextlib, io"          # the first line of the receipt's `_RUN` program
if _marker in OSRC and _marker in PSRC:
    fail.append("the receipt's arm-B program text appears in the producer -- the engine is DUPLICATED, "
                "which is what reading it out of the source exists to prevent")
else:
    print("  and the receipt's arm-B program text does NOT appear in the producer -- one engine, "
          "not two")
for _n in ('_RUN', 'def armB', 'def r0_of'):
    if _n not in OSRC:
        fail.append(f"the registered receipt no longer defines {_n} -- the engine has moved and the "
                    f"producer's reader will break")

# =====================================================================
print()
print("=" * 100)
print("  PART 2 -- ** THE CASE TABLE IS EXACTLY THE BANKED KEY SET **")
print("=" * 100)
SW = np.load(BANK)
KEYS = {k for k in SW.files if k != 'ells'}
# read the producer's CASES table out of its source rather than importing it (importing would run it)
_t = ast.parse(PSRC)
CASES = None
for _n in _t.body:
    if isinstance(_n, ast.Assign) and any(getattr(t, 'id', None) == 'CASES' for t in _n.targets):
        CASES = [e.elts[0].value for e in _n.value.elts]
if CASES is None:
    fail.append("the producer no longer carries a CASES table this receipt can read")
    CASES = []
print(f"  banked keys   ({len(KEYS)}): {sorted(KEYS)}")
print(f"  producer cases ({len(CASES)}): {sorted(CASES)}")
if set(CASES) != KEYS:
    fail.append(f"the producer's cases and the banked keys differ: "
                f"unproduced {sorted(KEYS - set(CASES))}, unbanked {sorted(set(CASES) - KEYS)}")
else:
    print("  ** set equality: every banked key has a case, and every case has a banked key **")
NVAL = sum(len(np.atleast_1d(SW[k])) for k in KEYS)
print(f"  {NVAL} banked values across {len(KEYS)} configurations")

# =====================================================================
print()
print("=" * 100)
print("  PART 3 -- ** ONE CONFIGURATION RE-DERIVED LIVE, SO THE PRODUCER IS EXERCISED **")
print("=" * 100)
LIVE_KEY = 'FROZEN_control_KLO_0_1'


def engine():
    tree = ast.parse(OSRC)
    want_assign = {'_RUN', 'C', 'NS', 'CTL', 'ADJ', 'R0'}
    want_func = {'r0_of', 'armB'}
    keep = []
    for n in tree.body:
        if isinstance(n, ast.Assign):
            names = set()
            for t in n.targets:
                if isinstance(t, ast.Name):
                    names.add(t.id)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    names |= {e.id for e in t.elts if isinstance(e, ast.Name)}
            if names & want_assign:
                keep.append(n)
        elif isinstance(n, ast.FunctionDef) and n.name in want_func:
            keep.append(n)
    ns = {'os': os, 'sys': sys, 'subprocess': subprocess, 'np': np,
          'HIER_DIR': os.path.join(ROOT, 'storyboard_receipts')}
    exec(compile(ast.Module(body=keep, type_ignores=[]), '<engine>', 'exec'), ns)
    return ns


_ns = engine()
_v, _meta = _ns['armB'](_ns['CTL'], ZEND=0, NTAU=150000, KLO=0.1, NLOW=480)
if _v is None:
    fail.append(f"the live re-derivation of {LIVE_KEY} did not run: {_meta}")
    print(f"  the live run FAILED: {_meta}")
else:
    _b = np.asarray(SW[LIVE_KEY], float)
    _v = np.asarray(_v, float)[:len(_b)]
    print(f"  live  {np.round(_v, 6)}")
    print(f"  bank  {_b}")
    _raw = float(np.max(np.abs(_v - _b)))
    _rnd = float(np.max(np.abs(np.round(_v, DP) - _b)))
    print(f"  ** worst |live - bank| = {_raw:.3e};  after rounding live to {DP} dp = {_rnd:.3e} **")
    if _rnd > 1e-9:
        fail.append(f"the live re-derivation does not round to the banked {LIVE_KEY} "
                    f"({_rnd:.3e} after rounding) -- the producer does not reproduce the bank")
    if _raw > 5e-5:
        fail.append(f"the live re-derivation is {_raw:.3e} from the bank, more than half the last "
                    f"stored digit -- the residual is not the bank's rounding")

# =====================================================================
print()
print("=" * 100)
print("  PART 4 -- ** AND THE FULL EIGHT, FROM THE PRODUCER'S OWN TRACKED RECORD **")
print("=" * 100)
REC = json.load(open(RECORD, encoding='utf-8'))
print(f"  {'configuration':>44} {'secs':>6} {'worst |live-bank|':>18} {'after rounding':>15}")
worst_raw = worst_rnd = 0.0
nval = 0
ncfg = 0
for k in sorted(KEYS):
    if k not in REC or 'live' not in REC[k]:
        fail.append(f"the record carries no re-derivation for the banked key {k}")
        continue
    lv = np.asarray(REC[k]['live'], float)
    bk = np.asarray(SW[k], float)[:len(lv)]
    raw = float(np.max(np.abs(lv - bk)))
    rnd = float(np.max(np.abs(np.round(lv, DP) - bk)))
    worst_raw, worst_rnd = max(worst_raw, raw), max(worst_rnd, rnd)
    nval += len(lv)
    ncfg += 1
    print(f"  {k:>44} {REC[k].get('secs', 0):>6.0f} {raw:>18.3e} {rnd:>15.3e}")
    # ** the record is checked against the BANK here, not trusted: a record claiming agreement
    #    while the bank says otherwise fails on this line and not on its own say-so.
    if rnd > 1e-9:
        fail.append(f"{k}: the recorded re-derivation does not round to the banked value "
                    f"({rnd:.3e})")
print(f"\n  ** {nval} values across {ncfg} of the bank's {len(KEYS)} configurations: "
      f"worst raw difference "
      f"{worst_raw:.3e}, and ZERO after rounding to {DP} dp **")
if nval != NVAL:
    fail.append(f"the record covers {nval} values against the bank's {NVAL}")
if worst_rnd > 1e-9:
    fail.append("some configuration does not reproduce after rounding -- the bank is not this "
                "producer's output")

# =====================================================================
print()
print("=" * 100)
print("  PART 5 -- ** WHAT THE RESIDUAL IS, NAMED RATHER THAN TOLERATED **")
print("=" * 100)
# the bank's stored precision, established from the bank itself and not assumed
_allb = np.concatenate([np.atleast_1d(np.asarray(SW[k], float)) for k in sorted(KEYS)])
# the FEWEST decimals that leave every banked value unchanged -- i.e. what the bank stores
_minimal = min((d for d in range(1, 9) if np.allclose(np.round(_allb, d), _allb, atol=1e-12)),
               default=99)
print(f"  every banked value is unchanged by rounding to {_minimal} decimals -- so the bank stores "
      f"{_minimal}")
if _minimal != DP:
    fail.append(f"the bank stores {_minimal} decimals, not the {DP} this receipt asserts against")
print(f"  half the last stored digit is {0.5 * 10 ** -_minimal:.1e}, and the worst raw difference is "
      f"{worst_raw:.3e}")
if not worst_raw <= 0.5 * 10 ** -_minimal:
    fail.append(f"the worst raw difference {worst_raw:.3e} exceeds half the last stored digit -- "
                f"then the residual is NOT the bank's rounding and this PART's reading is wrong")
print("  ⇒ ** so the agreement is not 'within tolerance': the bank IS the producer's output,")
print("     rounded to its own stored precision, on every value. **")

# =====================================================================
print()
print("=" * 100)
if fail:
    print(f"  FAIL -- {len(fail)} check(s) did not hold")
    for f in fail:
        print(f"    - {f}")
    print("=" * 100)
    sys.exit(1)
print("  ** ALL CHECKS HOLD. **  `cc66_lowell_sweep` is placed: a producer is in the repository, it")
print("  carries no second copy of the engine, its case table IS the banked key set, one")
print(f"  configuration is re-derived live on every run of this file, and all {len(KEYS)}")
print(f"  reproduce the bank EXACTLY at its own {_minimal}-decimal storage.  ** One of `70`'s two")
print("  load-bearing unplaceables is closed; `c54.182_clpp` is not, and is not claimed to be. **")
print("=" * 100)
sys.exit(0)
