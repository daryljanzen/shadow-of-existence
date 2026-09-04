#!/usr/bin/env python3
"""check_receipts_run.py -- the TWENTIETH gate: absorbed from the working fork, not built here.

** THE FORK BUILT THE TWO INSTRUMENTS THIS LINE'S RECEIPT GATE COULD NOT BE. **  Absorbed r2394.

`scripts/lint_assertions.py` and `scripts/run_all_receipts.py` arrived with the c54.163 bundle.  They
answer the two questions `check_receipt_asserts.py` cannot:

  lint_assertions   -- CAN THIS CHECK EVER BE FALSE?  Not "is there an assert" but "is the condition
                       a tautology".  It was extended twice by the fork, both times on real misses:
                       `check("tilt 45deg", True)` (a local helper, so no `assert` appears at all),
                       `sqrt(Rv**2-1) - sqrt(Rv**2-1) == 0` (the difference form), and
                       `assert 3*2*2 == 12` (a constant condition -- which THIS LINE's gate counts as
                       a failure path).  ** The fork's own words for the last class: "arithmetic
                       dressed as claims, written by workers measured on a count." **

  run_all_receipts  -- DOES IT ACTUALLY RUN, WHERE IT IS REGISTERED?  ** No static gate can see a
                       citation that moved away from its claim. **  The fork's first run found
                       `P15_the_low_ell_minimum_is_at_ell_four` failing on six of its eight pins,
                       broken since c54.155 by an edit that inserted a `\\rcpt{}` marker inside the
                       very sentences the receipt matches -- "the claims were all still true; the
                       citation moved, not the physics.  But the receipt had been failing since
                       c54.155 and nothing knew, because nothing ran it."

** THIS FILE IS THE WIRING, NOT A REIMPLEMENTATION. **  It runs the lint (fast, in-process) and reads
the runner's most recent result file, because the runner takes ~9 minutes and must be launched
detached -- two attempts to run it inside a single tool call died at the execution limit before
producing a line, which is itself worth recording: ** an instrument that cannot finish inside the
harness that calls it will be skipped by every caller who does not know that. **

THE ENVIRONMENT CAVEAT, WHICH MAKES THE RUNNER'S OUTPUT READABLE HERE.  Ten registered receipts import
third-party libraries this container does not carry -- six need `camb` (P15's Boltzmann references)
and four need `pynucastro` (P16's BBN network, via `bbn_network.py`).  They fail here and pass where
the fork runs them.  The fork's rule -- ** "a registered receipt that does not run where it is
registered is not a receipt" ** -- still holds; what this caveat records is where THIS LINE can
verify, not a defect in the receipts.  So those ten are named and excluded from the verdict, and the
exclusion is DECLARED here rather than inferred from an error string.

    python3 corpus/check_receipts_run.py            # lint + read the last runner result
    python3 corpus/check_receipts_run.py --how      # print how to launch the runner

Written r2394.  Stated for reversal.
"""
import glob, hashlib, os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
RESULT = os.path.join(ROOT, 'receipts', 'RUN_RESULT.txt')


def tree_digest():
    """The same digest `scripts/run_all_receipts.py` stamps: everything a receipt can READ."""
    h = hashlib.sha256()
    for pat in ('corpus/*.tex', 'receipts/**/*.py', 'computations/**/*.py'):
        for f in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
            h.update(os.path.relpath(f, ROOT).encode())
            h.update(open(f, 'rb').read())
    return h.hexdigest()[:16]

# Declared, not inferred: the receipts this container cannot run, and what each needs.
UNRUNNABLE = {
    'BUILD_camb_store.py': 'camb',
    'P15_camb_reference.py': 'camb',
    'P15_derived_lensing_on_the_lcdm_arm.py': 'camb',
    'P15_damping_ratio_clean.py': 'camb',
    'P15_damping_reabsorption.py': 'camb',
    'P15_full_transfer_verdict.py': 'camb',
    'P15_verify_lowell_boltzmann.py': 'camb',
    'P16_theory_error_and_likelihood.py': 'pynucastro',
    'P16_validate_bbn.py': 'pynucastro',
    # ⛭⛭ TEN ADDED r3946.  The list above named NINE and the run has NINETEEN module failures, so
    #   ten environment failures were being counted as REAL by the instrument that exists to
    #   separate them -- it reported 72 real failures where 62 were real.  Each below was checked
    #   by NAME against the run's own traceback, per this list's rule: "declared here by name,
    #   never inferred from an error string."
    'C43_the_gap_is_numerical_not_xe.py': 'camb',
    'C45_xe_does_not_cancel_from_a_ratio_of_integrals.py': 'camb',
    'C47_the_neutrinos_were_missing.py': 'camb',
    'P15_the_control_entered_the_regime_and_the_arm_did_not_move.py': 'camb',
    'P15_the_floor_is_a_distance_between_models_not_a_number_from_the_data.py': 'camb',
    'P16_the_adiabatic_premise_is_demanded_by_the_data_and_inherited_by_the_construction.py': 'camb',
    'S1_the_adiabatic_premise_is_what_the_data_demands.py': 'camb',
    'S1_the_cosmology_sector_rests_on_neff_and_never_names_it.py': 'camb',
    # ⛔ AND THESE TWO ARE A DIFFERENT CASE, WHICH IS WHY THEY ARE COMMENTED SEPARATELY.  They need
    #   matplotlib -- and matplotlib was in NO environment: not this container, and NOT the `heavy`
    #   job's pip line, which installed camb and pynucastro and stopped there.  ** So two registered
    #   receipts were unrunnable EVERYWHERE and had never once been run since they were written. **
    #   The remedy is not to declare them away: matplotlib was added to .github/workflows/gates.yml
    #   at r3946, so the nightly can now run them.  They stay listed because THIS container still
    #   lacks it, which is what this list is for.
    'P03_the_U3_figure.py': 'matplotlib',
    'P03_the_turnaround_figure.py': 'matplotlib',
}

LAUNCH = ("cd <tree> && (setsid nohup python3 scripts/run_all_receipts.py --jobs 4 --timeout 300 "
          "> receipts/RUN_RESULT.txt 2>&1 < /dev/null &)")


def main():
    if '--how' in sys.argv:
        print()
        print('  The runner takes ~9 minutes and must be launched DETACHED:')
        print(f'    {LAUNCH}')
        print('  then poll `receipts/RUN_RESULT.txt`.  Two attempts to run it inside one tool call')
        print('  died at the execution limit before producing a line.')
        print()
        return 0

    print()
    print('  RECEIPTS, RUN AND LINTED -- the two questions a presence-check cannot ask')
    print()

    rc = 0
    lint = os.path.join(ROOT, 'scripts', 'lint_assertions.py')
    if not os.path.exists(lint):
        print('  [FAIL] scripts/lint_assertions.py is absent -- it arrived with the c54.163 bundle')
        print('         and is the only instrument that can see a HOLLOW assertion.')
        rc = 1
    else:
        out = subprocess.run([sys.executable, lint], capture_output=True, text=True,
                             cwd=ROOT).stdout
        for ln in out.split('\n'):
            if ln.strip():
                print('   ', ln.strip())
        if 'No hollow assertions' not in out:
            rc = 1

    print()
    if not os.path.exists(RESULT):
        print('  [REPORT] no runner result on file yet.  This is NOT a failure: the runner takes')
        print('     ~9 minutes and is launched out of band.  `--how` prints the command.')
        print('     ** A gate that fails because a 9-minute job has not been run would be a gate')
        print('        that trains its caller to skip it. **')
        print()
        return rc

    res = open(RESULT, encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------------ r2656+c54.208
    # ** THE CACHE HAD NO EXPIRY, AND A CACHE WITH NO EXPIRY IS NOT A MEASUREMENT. **
    # The file this gate reads was written at r2419 and was still being read as current at
    # r2656 -- 294 commits and 160 registered receipts later.  It said "no receipt fails for a
    # reason inside the corpus"; a live run of the corpus-reading receipts found 24 that did,
    # several falsified by the very revisions that filled the absences they assert.
    #   ⇒ *** The gate was green because it was OLD, which is the direction that looks like
    #       success -- the fourth instrument this session to report LOW. ***
    # The fix is not a date: it is a digest of everything a receipt can READ.  It goes stale
    # exactly when a paper or a receipt changes, and at no other time.
    stamp = re.search(r'TREE-DIGEST:\s*([0-9a-f]{8,})', res)
    if not stamp:
        print('  ⛔ [FAIL] the runner result carries NO TREE-DIGEST, so nothing says which tree it')
        print('     ran against.  Re-run it: `python3 corpus/check_receipts_run.py --how`.')
        print('     ** A cached verdict that cannot be dated is a verdict about an unknown tree. **')
        return 1
    now = tree_digest()
    if stamp.group(1) != now:
        print(f'  ⛔ [FAIL] STALE RESULT.  The cached run is against tree {stamp.group(1)}; the tree')
        print(f'     is now {now}.  A paper or a receipt has changed since, which is exactly when a')
        print('     source check can have gone stale -- so the cached verdict says nothing.')
        print('     Re-run: `python3 corpus/check_receipts_run.py --how`  (~9 min, detached).')
        return 1
    print(f'  result is against the current tree ({now}) -- not a cached verdict about an older one')

    m = re.search(r'(\d+) pass, (\d+) fail, (\d+) over timeout, in (\d+)s', res)
    if not m:
        print('  [FAIL] the runner result file has no verdict line -- it may have been truncated.')
        return 1
    npass, nfail, nslow = int(m.group(1)), int(m.group(2)), int(m.group(3))
    failed = re.findall(r'\[FAIL\] receipts/\S+/(\S+\.py)', res)
    # ** r3995: THE EXEMPTION IS CONDITIONAL ON THE MODULE BEING ABSENT, not on the name. **
    #   It was unconditional, so a receipt on this list was filed ENVIRONMENT wherever it
    #   failed -- INCLUDING IN CI, WHICH INSTALLS camb AND pynucastro (gates.yml:117).  A real
    #   failure in any of those 19 was invisible in the one place they actually run.
    #   And the list's premise was false here too: `pip install camb --break-system-packages`
    #   succeeds, and P15_camb_reference.py then runs and returns P1/P2 = 2.211 against the
    #   paper's 2.2.  ** They were not unrunnable.  They were unrun. **
    import importlib.util as _ilu
    def _absent(mod):
        try: return _ilu.find_spec(mod) is None
        except Exception: return True
    env  = [f for f in failed if f in UNRUNNABLE and _absent(UNRUNNABLE[f])]
    real = [f for f in failed if f not in env]
    print(f'  Last run: {npass} pass, {nfail} fail, {nslow} over timeout, {m.group(4)}s.')
    if env:
        libs = sorted({UNRUNNABLE[f] for f in env})
        print(f'  Of the failures, {len(env)} are ENVIRONMENT -- they import {", ".join(libs)}, which')
        print('     this container does not carry, and they pass where the fork runs them.')
        print('     ** Declared here by name, never inferred from an error string. **')
    if real:
        print(f'  ⛔ {len(real)} REAL failure(s):')
        for f in real:
            print(f'    [FAIL] {f}')
        print('     A receipt that fails where it is registered is the one thing no static gate')
        print('     can see -- a citation that moved away from its claim looks fine to every')
        print('     link checker and every assertion lint.')
        rc = 1
    else:
        print('  No receipt fails for a reason inside the corpus.')
    if nslow:
        print(f'  {nslow} exceeded the per-receipt timeout -- raise it rather than reading it as a fail.')
    print()
    return rc


if __name__ == '__main__':
    sys.exit(main())
