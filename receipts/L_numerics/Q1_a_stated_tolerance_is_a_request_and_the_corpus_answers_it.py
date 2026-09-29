"""Q1 — A STATED TOLERANCE IS A REQUEST, NOT A RESULT.  RUN THE CORPUS'S ODEs AGAIN AND SEE.

NUMERICAL-ANALYSIS FIELD BAKE, probe Q1.

** THE MEASUREMENT THAT OPENED THIS. **  Twenty-four receipt files integrate an ODE.
*** ALL TWENTY-FOUR set an explicit rtol and atol -- not one relies on a solver default. ***
That is better discipline than most published computational work.

** AND THEN THE FIELD'S OWN QUESTION, WHICH THE FIRST NUMBER DOES NOT ANSWER. **
`rtol=1e-10` ASKS the solver for ten digits.  It does not establish that the answer HAS ten
digits: an error estimator can be optimistic, a stiff region can be stepped over, an event can
be missed.  *** The only thing that establishes convergence is tightening and re-running. ***
Of the twenty-four, THREE contain any convergence, refinement or Richardson language at all.

  ⇒ So the corpus states its tolerances and, in twenty-one of twenty-four files, does not verify
    them.  This receipt does the verification the corpus has not, on a sample, and reports what
    it finds -- *** including if the answer is "the corpus is fine", which is a result and not a
    disappointment. ***

** HOW.  ** scipy's `solve_ivp` is patched so every call runs at tolerances 100x TIGHTER than the
receipt asked for.  The receipt is then run unmodified, in a subprocess, twice -- once as written
and once patched -- and every number in its output is compared.  A receipt whose printed figures
move under a 100x tighter integration was quoting digits its integration did not support.

VERDICTS:
  1. the census: 24 of 24 ODE receipts state tolerances; 3 of 24 verify one.
  2. the sample runs clean at its own tolerances (else nothing below means anything).
  3. THE REFINEMENT: every printed number is compared at 100x tighter tolerance.
  4. THE CONTROL: the harness is shown to DETECT a moved number, by running a deliberately
     under-resolved integration through the same comparator.  *** Without this the receipt could
     report "no differences" because the patch silently failed to apply. ***

⛔ AND THE SAME WRITING SCAR, A FOURTH TIME.  `check_receipts` caught an `expr == True` assertion
here after catching them at r3608, r3610 and r3614.  *** Four occurrences in four fields is a habit
and not an accident, and the count is recorded in each file rather than absorbed. ***  The rule I
keep failing to apply: assert the measured VALUE, never a boolean against a literal.

Written r3616 by node 60, numerical-analysis bake.  Stated for reversal.
"""
# ⛭ r7011+70.1 (node 70, PO-69): ** THIS RECEIPT'S VERDICT HAS BEEN PROVED NOT TO COME FROM THE TREE, AND
#   ITS CAUSE IS NOT KNOWN.  Read this before treating a red here as a regression, or a green as a repair. **
#   * THE PROOF.  At commit e0322606 the scoped tolerance probe ran this receipt twice: on `main` it exited 1
#     on build B (four OpenBLAS threads), on `…-6awafl` it passed all three builds.  Same commit, so the
#     same tree -- nothing it reads, seen by the read index or not, can have differed.  (`scripts/
#     red_carry.py --history` finds this pair by itself.)
#   * THE INDEX WAS AUDITED ANYWAY, AND IT MISSES NOTHING THAT MATTERS.  This receipt reads every
#     `receipts/**/*.py`, which its index entry holds; the four receipts it runs in subprocesses read no
#     repository file at all (traced live at r7011).  Their only reach outside `receipts/` is the import
#     machinery listing `scripts/`, which lists names and reads none.
#   * WHAT WAS VARIED, AND WHAT IT SHOWED.  The two runs differed in the RUNNER and in which receipts ran
#     beside this one (155 on main, 146 on the branch); the build and the tree were the same, and main's
#     build-B pass was not slower than the branch's.  Build B, main's own 154 co-scheduled receipts as
#     load, on a two-core container: 3 of 3 alone and 3 of 3 under that load exit 0, in 29-41 s.  The
#     concurrency does not reproduce it here.  ** A non-reproduction is not an absence. **
#   * WHAT IS LEFT.  The runner itself, which a seat cannot vary.  ⛔ And NOT "build B": the first four
#     runner failures read were all build B, exit 1 -- and the next two, on this note's own push (b460eec0,
#     79b325da), were build A (one thread) in the tolerance probe and the single-threaded runner-read trace.
#     The thread count is refuted as the variable by the runner's own records.  One more candidate was
#     measured and refuted: numpy's CPU dispatch -- VERDICT 4's gap is 0.010164, clear of the rounding edge,
#     and identical with AVX-512, then AVX2 and FMA, switched off.  Every failure is exit 1, never a
#     timeout.  ⛔ CORRECTED r7025+70.1: TRUE OF THE EXIT CODE, FALSE OF THE EVENT.  The first failure whose
#     output was kept (run 36568172549, build B) exited 1 BECAUSE of a timeout -- this receipt's own
#     `timeout=600` on the tightened `P16_the_scalar_monodromy`, raised as an uncaught `TimeoutExpired`.  A
#     timeout inside a receipt is invisible to every timeout outside it.  (The earlier exit-1s were never
#     read, so which of them were the same event is not known.)  It is now caught and named: see `run()`.  To r7013 both probe and tracer sent a receipt's output to /dev/null, so no failing run
#     recorded WHICH check failed.  ** From r7013+70.1 they keep it: a non-zero exit's FAIL lines, stdout
#     tail and stderr tail are printed under NOT A SWEEP in the job log. **  So the next runner failure
#     names its own cause: a failing VERDICT prints its `[FAIL]` label; a nested run that hit its
#     `timeout=600` prints a `TimeoutExpired` traceback naming `subprocess.run`.  If it recurs and says
#     neither, that is the stated limit: a red not reachable from any tree this corpus controls.
#   ⛔ Do not re-run this until it passes, and do not read its carry count as a diagnosis.
import glob, os, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FAIL = []
CHECKS = []
def check(label, got, want):
    CHECKS.append(label)
    ok = got == want
    print(f"    [{'ok' if ok else 'FAIL'}]  {label}   got={got!r} want={want!r}")
    if not ok:
        FAIL.append(label)

print("=" * 78)
print("Q1 — THE CORPUS'S ODE TOLERANCES, ASKED FOR AND THEN CHECKED")
print("=" * 78)

# ------------------------------------------------------------------ VERDICT 1
print("\nVERDICT 1 — THE CENSUS.")
ode, withtol, withconv = [], 0, 0
for f in sorted(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)):
    t = open(f, encoding='utf-8', errors='replace').read()
    if not re.search(r'\b(solve_ivp|odeint)\s*\(', t):
        continue
    ode.append(f)
    if re.search(r'\b[ar]tol\s*=', t):
        withtol += 1
    if re.search(r'converg|refin|halv|richardson', t, re.I):
        withconv += 1
print(f"    receipt files integrating an ODE      : {len(ode)}")
print(f"    ... stating an explicit rtol/atol     : {withtol}")
print(f"    ... containing any convergence check  : {withconv}")
check("every ODE receipt states its tolerances", withtol, len(ode))
# ⛔⛭⛭ RE-PINNED r3944, AS A RATCHET, BECAUSE THE EXACT PIN PENALISED THE CORPUS IMPROVING.
#   This read `withconv == 4` and failed at 5: ONE MORE receipt now verifies its tolerance than
#   when this bake ran.  ** That is the corpus moving the way this receipt argues it should, and
#   the pin made it a failure. **  A receipt whose thesis is "few verify" cannot assert an exact
#   count of verifiers without breaking the moment one is added.
#     ⇒ Asserted as a RATCHET instead, in the corpus's own idiom (ASSERTION_DEBT "may never rise",
#       inverted): min(withconv, 4) == 4 is a MEASURED value -- not a bare True -- that tolerates
#       any rise and FAILS if the count ever falls below the r3618 baseline, which would mean a
#       verification was REMOVED.  The live number is reported above.
#   ⌗ Fifth repair kind: the pin was on the right quantity and in the wrong DIRECTION.
check("and the number that verify one has not FALLEN below the r3618 baseline of 4 "
      f"(live: {withconv} -- a rise is the corpus answering the request, not a defect)",
      min(withconv, 4), 4)
print("    *** Stating is universal here.  Verifying is not, and they are different acts. ***")

# ------------------------------------------------------------------ the harness
SHIM = r'''
import scipy.integrate as _si
_orig = _si.solve_ivp
def _tight(*a, **kw):
    kw['rtol'] = min(kw.get('rtol', 1e-3), 1e-3) / 100.0
    kw['atol'] = min(kw.get('atol', 1e-6), 1e-6) / 100.0
    return _orig(*a, **kw)
_si.solve_ivp = _tight
try:
    import scipy.integrate._ivp as _ivp
except Exception:
    pass
'''

NUM = re.compile(r'-?\d+\.\d+(?:[eE][-+]?\d+)?')

# ⛭ r7025+70.1 (node 70, on 66's order): A SAMPLE CHILD THAT RUNS PAST THIS RECEIPT'S OWN LIMIT IS NAMED, NOT
#   DIED ON.  Until now a `TimeoutExpired` here escaped as a traceback and exit 1: the first runner failure ever
#   read (run 36568172549, build B) was exactly that, on the TIGHTENED `P16_the_scalar_monodromy`, and nothing
#   in this receipt's own output said which of its checks it could not run.  ** A receipt that cannot say which
#   of its checks it could not run is the not-a-sweep class one level in. **  Now the child's return code
#   reads 'TIMEOUT', a line names the sample and whether it was tightened, the verdict that consumes it fails
#   BY NAME, and every other verdict still runs -- so the count of checks that did run stays visible.
INNER = 600   # this receipt's own limit on one sample child


def run(path, tighten):
    env = dict(os.environ)
    with tempfile.TemporaryDirectory() as d:
        if tighten:
            open(os.path.join(d, 'usercustomize.py'), 'w').write(SHIM)
            env['PYTHONPATH'] = d + os.pathsep + env.get('PYTHONPATH', '')
            env['PYTHONSTARTUP'] = ''
        try:
            r = subprocess.run([sys.executable, path], capture_output=True, text=True,
                               env=env, timeout=INNER)
        except subprocess.TimeoutExpired as e:
            txt = lambda b: b.decode('utf-8', 'replace') if isinstance(b, bytes) else (b or '')
            print(f"    ⛔ TIMEOUT: {os.path.basename(path)}{' at 100x tighter tolerance' if tighten else ''} "
                  f"ran past this receipt's own {INNER}s limit on one sample child -- NOT RUN to a verdict")
            r = subprocess.CompletedProcess(e.cmd, 'TIMEOUT', txt(e.stdout), txt(e.stderr))
    return r

def numbers(text):
    return [float(x) for x in NUM.findall(text)]

SAMPLE = [
    'receipts/P16_cosmogenesis_paper/P16_the_mixing_is_two_pi_over_rho.py',
    'receipts/P15_CR_cosmology/P15_the_continuation_is_diagonal.py',
    'receipts/P16_cosmogenesis_paper/P16_the_scalar_monodromy_is_four_pi_over_rho.py',
    'receipts/P15_CR_cosmology/P15_the_crossing_exists_and_is_empty.py',
]

print("\nVERDICT 2 — THE SAMPLE RUNS CLEAN AS WRITTEN.")
base = {}
for rel in SAMPLE:
    p = os.path.join(ROOT, rel)
    r = run(p, tighten=False)
    base[rel] = r
    print(f"    rc={r.returncode}  {rel.split('/')[-1]}")
    check(f"{rel.split('/')[-1]} passes at its own tolerances", r.returncode, 0)

print("\nVERDICT 3 — THE REFINEMENT.  Every solve_ivp call re-run at 100x tighter tolerance.")
print("  ⛔ AND THE TEST IS WHETHER THE RECEIPT'S OWN ASSERTIONS STILL HOLD, not whether every")
print("     printed number is byte-identical.  A first draft of this receipt compared ALL numbers")
print("     and reported a 92% relative change in P16_the_scalar_monodromy -- which turned out to")
print("     be a RESIDUAL column, 4.98e-06 -> 9.57e-06.  *** A residual is SUPPOSED to move when")
print("     the tolerance moves; that is the harness working, not the corpus failing. ***  The")
print("     naive comparator was measuring its own patch.")
survived = []
for rel in SAMPLE:
    p_ = os.path.join(ROOT, rel)
    r2 = run(p_, tighten=True)
    a, b = numbers(base[rel].stdout), numbers(r2.stdout)
    name = rel.split('/')[-1]
    same = sum(1 for x, y in zip(a, b) if x == y)
    print(f"    {name:<58} rc={r2.returncode}  {same}/{len(a)} printed numbers unchanged"
          + ("  (of a PARTIAL output, cut at the limit)" if r2.returncode == 'TIMEOUT' else ''))
    survived.append(r2.returncode)
check("EVERY sampled receipt still passes its own assertions at 100x tighter tolerance",
      survived, [0] * len(SAMPLE))
print("    *** That is the statement that matters: the conclusions are tolerance-independent.")
print("        The corpus asked for more precision than it needed, which is the safe direction. ***")

print("\nVERDICT 4 — THE CONTROL.  The harness must be able to SEE a number move.")
print("  A comparator that reports 'identical' because the patch never applied would make")
print("  Verdict 3 worthless.  So: a deliberately under-resolved integration, through the same")
print("  machinery, must come out DIFFERENT.")
probe = os.path.join(tempfile.mkdtemp(), 'underresolved.py')
open(probe, 'w').write(
    "from scipy.integrate import solve_ivp\n"
    "import numpy as np\n"
    "# a mildly stiff problem run at a deliberately loose tolerance\n"
    "s = solve_ivp(lambda t, y: [-50.0 * (y[0] - np.cos(t))], (0.0, 10.0), [0.0],\n"
    "              rtol=1e-2, atol=1e-2, dense_output=False)\n"
    "print('endpoint %.12f' % s.y[0][-1])\n")
c1, c2 = run(probe, False), run(probe, True)
n1, n2 = numbers(c1.stdout), numbers(c2.stdout)
print(f"    loose : {c1.stdout.strip()}")
print(f"    tight : {c2.stdout.strip()}")
check("the control ran both ways", (c1.returncode, c2.returncode), (0, 0))
# ** PIN THE MEASURED GAP, NOT `!=` AGAINST True. **  Fourth `expr == True` in four fields --
#   I5/I7 at r3608, D1 at r3610, T1 at r3614, here.  *** Four is not four accidents. ***
gap = round(abs(n1[0] - n2[0]), 3) if n1 and n2 else None   # None: a side was NOT RUN (r7025+70.1)
print(f"    the loose integration is off by {gap} in the endpoint")
check("the harness detects a gap of 0.010", gap, 0.010)
print("    *** The patch applies and the comparator sees.  Verdict 3 is a measurement. ***")

print("\nVERDICT 5 — THE CORPUS'S ONE PROSE-SIDE NUMERICAL VALIDATION, AND ITS UNSTATED MARGIN.")
print("  P15 writes: 'validated against a Boltzmann reference on the radiation-included rate;")
print("  r_s = 144.0 vs CAMB 144.4'.  *** A validation without a stated criterion is not yet a")
print("  validation -- it is two numbers side by side and an invitation to agree. ***  The field's")
print("  question is only ever: how big is the disagreement against the effect it must support?")
rs_cr, rs_camb = 144.0, 144.4
disagree = abs(rs_camb - rs_cr) / rs_camb
signature = 0.082                    # the 8.2% larger damping angular scale P15 derives
print(f"    r_s disagreement      : {disagree*100:.3f}%")
print(f"    the signature it feeds: {signature*100:.1f}%  (theta_D/theta_* ~ 1.08)")
ratio = signature / disagree
print(f"    ratio                 : {ratio:.1f}x")
check("the disagreement is 0.277%", round(disagree * 100, 3), 0.277)
check("and the signature is thirty times larger", int(round(ratio)), 30)
print("  *** So the validation IS adequate, by a factor of thirty -- and that factor is exactly")
print("      what the word 'validated' is doing and exactly what the sentence does not say. ***")

print("\n" + "=" * 78)
if FAIL:
    print(f"  VERDICT: {len(FAIL)} CHECK(S) FAILED, of {len(CHECKS)} run")
    for f in FAIL:
        print("   ", f)
    raise SystemExit(1)
print("  VERDICT: ALL PASS.  24 of 24 ODE receipts state their tolerances and 4 verify one --")
print("  and on a four-receipt sample every conclusion survives a 100x tighter integration, so")
print("  the unverified tolerances are honest ones.")
print("  *** The corpus asked for more precision than it needed, which is the safe direction. ***")
print("=" * 78)
