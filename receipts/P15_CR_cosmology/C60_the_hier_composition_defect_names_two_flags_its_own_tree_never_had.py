#!/usr/bin/env python3
r"""
C60 — ** r3512's `HIER` COMPOSITION DEFECT IS NOT THERE, AND HAS NOT BEEN SINCE IT WAS WRITTEN. **
The two flags its remedy names are absent from the tree it was written against, and the asymmetry it
counted is `sound_phase`, which is on neither spectrum path.

** WHAT WAS ASKED, AND BY WHOM. **  `C59` closed `PO-24`'s first step on the CONTROL arm and stated
its own scope in one sentence: *"The clock operations are no-ops on the control ($\mathrm{Jac}\equiv
1$), so r3512's `HIER` composition defect cannot touch this result --- and stays LIVE for the CR arm,
which is the first thing the next step must settle."*  `THE_REGISTER`'s `PO-24` row, `INDEX`, and both
appendices carry the same deferral.  ** So a live defect stands between the CR arm and the
polarisation path, and the polarisation path is where the control's $2.197$ was measured. **  This
receipt is that settlement, and it comes out the other way.

** WHAT r3512 RECORDED. **  `PO13_WORKING_STATE`, "THE COMPOSITION DEFECT — checked, r3512":

    *`evolve_hier` and `_project` (lines 828-977) reference the clock operations **once**:
    `Jac_of(e) if LEAFPERT`. The main path references **two**.* => ***`HIER=1` does not know
    `SRCSTACK` or `DIFFLEAF`.***

and the remedy it set as gate 3 of four: *"give the hierarchy's gravitational source the stacking
clock and its diffusion the leaf, the same LGF assignment the main path carries.  Without this, step
4 is void."*  Step 4 is the CR run.

** HALF ONE: THE REMEDY NAMES TWO FLAGS THAT ARE NOT IN r3512's OWN TREE. **  `SRCSTACK` and
`DIFFLEAF` appear zero times in `ACOUSTIC_two_arm.py` at `95559d53`, the commit r3512 IS.  Its
forty-two `os.environ.get` flags are enumerated below and neither is among them.  ⌗ *They were real
on ANOTHER LINE:* `6beeca84` carries twelve `SRCSTACK` references and three `DIFFLEAF`, and
`cb5ec460` --- "full consistent `HIER` composition" --- is r3512's gate 3 actually performed, there.
** `6beeca84` is not an ancestor of `95559d53`.**  Two nodes were working the same instrument on two
lines, and the inventory was compiled across them while the defect was checked against one.

** HALF TWO: THE ASYMMETRY IT COUNTED IS `sound_phase`, WHICH IS ON NEITHER SPECTRUM PATH. **  In
r3512's own tree, and in the tree today, the four `Jac_of` sites are: the `CRPHI=entryleaf`
initial-condition diagnostic, `evolve`'s RHS, `sound_phase`, and `evolve_hier`'s RHS.  `sound_phase`
is called ONCE in the whole file and that call is inside `qscan()` --- the `QSCAN=1` diagnostic, which
computes no spectrum.  ** So the like-for-like count is one and one: **

     path                 ODE right-hand sides carrying the clock      projection
     LOS   (default)      evolve                     1                 los_spectrum   0
     HIER  (polarisation) evolve + evolve_hier        1 + 1             _project       0

  ⇒ The two-segment path applies the chain rule once per segment, which is what a change of
    independent variable requires, and neither projection applies it --- which is also right: the
    projection is the COMOVING RULER's, on the stacking clock (`sound_phase`'s own docstring says so,
    and warns against unifying the two horizons).

** HALF THREE: THE TWO RIGHT-HAND SIDES ARE CHARACTER-IDENTICAL WHERE THE CLOCK ENTERS. **  Not a
count --- the same bytes.  `evolve` line 576 and `evolve_hier` line 959 are both

    `        return out.ravel() * (float(Jac_of(e)) if LEAFPERT else 1.0)`

and their rate selections, line 536 and line 916, are both

    `        Hc, Rb = float(Hl_of(e) if LEAFPERT else Hc_of(e)), float(Rb_of(e))`

and every other clock-or-source operation in the file --- `Phi2_of` (`PHASEONLY`), `Gf_of` (`GSRC`)
and the four density-fraction splines --- is referenced in both.

** HALF FOUR: AND IT MOVES.  ** Asserted by running it: on `ARM=cr`, where $\mathrm{Jac}\not\equiv1$,
toggling `LEAFPERT` changes the state `evolve_hier` returns.  The hierarchy is not ignoring the clock
operation.  On the control the same toggle is provably inert because $\mathrm{Jac}\equiv1$ makes both
branches of the conditional the same number, which is why the control could never have caught this
either way --- r3512 was right about that.

*** => THE CR ARM IS NOT GATED ON A COMPOSITION FIX.  `C59`'s deferral is discharged. ***

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · This establishes that the named defect is absent.  ** It does NOT establish that the HIER path is
    correct **, and it produces no CR number, no peak position and no height ratio.
  · It says nothing about r3512's gate order 1, 2 and 4 --- validating $\Pi$ on the control, the
    `PISRC` subtraction, and the CR run --- which remain to be done and are PO-13 Run 1's business.
  · NOT CLAIMED: that r3512 was careless.  Two lines of work on one file is a corpus-mechanics
    failure, not a reading failure, and the inventory it left is still the best one there is.
  ⌗ *And one thing this receipt needs is itself a finding: it reads git history, as forty-one other
    registered receipts already do, while the workflow job that runs every receipt checks out
    shallow.  Asserted below as a fact about `.github/workflows/gates.yml` at this commit.*

** COMPUTES: occurrence counts and call-site locations of the clock operations in
  computations/beyond_the_wall/ACOUSTIC_two_arm.py at HEAD and at 95559d53; the flag inventory at
  95559d53; byte-equality of the two right-hand sides' clock lines; and ONE numeric check -- that
  evolve_hier's returned state on ARM=cr differs when LEAFPERT is toggled, on a 4-mode grid. **

STATUS: ✔✔
RUN: python3 C60_the_hier_composition_defect_names_two_flags_its_own_tree_never_had.py
RUNTIME: ~1 min (one instrument import, one two-segment evolution on 4 modes, run twice)
ORIGIN: built r4122 (node 60) discharging C59's named deferral, on 61's PO-13 assignment.
"""
import io
import contextlib
import importlib.util
import os
import re
import subprocess
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 78
FAIL = []


def check(cond, msg):
    print(("  ✔ " if cond else "  ✘ ") + msg)
    if not cond:
        FAIL.append(msg)


_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.normpath(os.path.join(_HERE, '..', '..'))
_REL = os.path.join('computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
_INSTR = os.path.join(_ROOT, _REL)
assert os.path.exists(_INSTR), _INSTR
SRC = open(_INSTR).read()
R3512 = '95559d53'          # the commit r3512 IS
OTHER = '6beeca84'          # the parallel line, where SRCSTACK/DIFFLEAF were real


def git(*a):
    r = subprocess.run(['git'] + list(a), cwd=_ROOT, capture_output=True, text=True)
    return r.returncode, r.stdout


# ** the history this receipt reads must BE there.  A shallow clone would make every assertion in
#    PART 1 vacuously about an empty string, which is the hollow-assertion failure the fork names. **
_rc, _ = git('cat-file', '-e', R3512 + '^{commit}')
if _rc != 0:
    print(f"\n  ⛔ commit {R3512} is not in this clone -- the history PART 1 reads is absent.")
    print("     This receipt reads git history; a shallow checkout cannot run it.  NOT a pass.")
    sys.exit(1)

# =====================================================================================
print(BAR); print("PART 1 — THE TWO FLAGS THE REMEDY NAMES ARE NOT IN THE TREE IT WAS WRITTEN AGAINST")
print(BAR)
_rc, OLD = git('show', f'{R3512}:{_REL}')
check(_rc == 0 and len(OLD) > 10000, f"{R3512}:{_REL} read, {len(OLD.splitlines())} lines")

for name in ('SRCSTACK', 'DIFFLEAF'):
    n_old, n_now = OLD.count(name), SRC.count(name)
    check(n_old == 0, f"`{name}` occurs {n_old} times in the instrument at {R3512} (r3512's own tree)")
    check(n_now == 0, f"`{name}` occurs {n_now} times in the instrument at HEAD")

FLAGS = sorted(set(re.findall(r"environ\.get\(\s*'([A-Z0-9_]+)'", OLD)))
print(f"\n    the {len(FLAGS)} os.environ flags present at {R3512}:")
for i in range(0, len(FLAGS), 6):
    print("      " + "  ".join(f"{f:<12}" for f in FLAGS[i:i + 6]))
check('SRCSTACK' not in FLAGS and 'DIFFLEAF' not in FLAGS,
      "neither flag is among them, so the inventory row naming them was not read from this tree")

# ⌗ and they WERE real, on a line that is not this one.
_rc, OTH = git('show', f'{OTHER}:{_REL}')
check(_rc == 0 and OTH.count('SRCSTACK') > 0,
      f"{OTHER} carries SRCSTACK x{OTH.count('SRCSTACK')} and DIFFLEAF x{OTH.count('DIFFLEAF')}")
_rc, _ = git('merge-base', '--is-ancestor', OTHER, R3512)
check(_rc != 0, f"{OTHER} is NOT an ancestor of {R3512} — two lines, not one")
_rc, _ = git('merge-base', '--is-ancestor', R3512, 'HEAD')
check(_rc == 0, f"{R3512} IS an ancestor of HEAD — r3512 is on this line, and its remedy's flags never were")

# =====================================================================================
print(); print(BAR); print("PART 2 — THE ASYMMETRY IT COUNTED IS `sound_phase`, ON NEITHER SPECTRUM PATH")
print(BAR)


def spans(text):
    """(name -> (first line, last line)) for every top-level def, 1-indexed and inclusive."""
    lines = text.splitlines()
    starts = [(i + 1, m.group(1)) for i, ln in enumerate(lines)
              for m in [re.match(r'def ([A-Za-z_][A-Za-z0-9_]*)\(', ln)] if m]
    out = {}
    for j, (ln, nm) in enumerate(starts):
        out[nm] = (ln, (starts[j + 1][0] - 1) if j + 1 < len(starts) else len(lines))
    return out


def jac_lines(text, name):
    lo, hi = spans(text)[name]
    return [i for i, ln in enumerate(text.splitlines()[lo - 1:hi], start=lo) if 'Jac_of(' in ln]


for tag, text in (("HEAD", SRC), (R3512, OLD)):
    sp = spans(text)
    ev, eh = jac_lines(text, 'evolve'), jac_lines(text, 'evolve_hier')
    sf, lo_, pr = jac_lines(text, 'sound_phase'), jac_lines(text, 'los_spectrum'), jac_lines(text, '_project')
    print(f"\n    {tag}:  evolve {ev}   evolve_hier {eh}   sound_phase {sf}   "
          f"los_spectrum {lo_}   _project {pr}")
    # `evolve` carries a SECOND site, in the CRPHI=entryleaf initial-condition diagnostic; it is
    # gated on `_leaf`, not on LEAFPERT, and is not the equation of motion.
    rhs_ev = [i for i in ev if 'LEAFPERT' in text.splitlines()[i - 1]]
    rhs_eh = [i for i in eh if 'LEAFPERT' in text.splitlines()[i - 1]]
    check(len(rhs_ev) == 1 and len(rhs_eh) == 1,
          f"{tag}: evolve's RHS carries the clock once ({rhs_ev}), evolve_hier's once ({rhs_eh})")
    check(len(lo_) == 0 and len(pr) == 0,
          f"{tag}: NEITHER projection carries it — los_spectrum {len(lo_)}, _project {len(pr)}")
    check(len(sf) == 1, f"{tag}: sound_phase carries it once ({sf}) — the second site on 'the main path'")
    calls = [i for i, ln in enumerate(text.splitlines(), 1)
             if re.search(r'(?<!def )\bsound_phase\(', ln)]
    inq = [i for i in calls if sp['qscan'][0] <= i <= sp['qscan'][1]]
    check(len(calls) == 1 and len(inq) == 1,
          f"{tag}: sound_phase is CALLED once, at line {calls}, inside qscan() "
          f"(lines {sp['qscan'][0]}-{sp['qscan'][1]}) — the QSCAN=1 diagnostic, which computes no spectrum")

print("\n  ⇒ counting sound_phase as 'the main path' is what made one and one read as two and one.")

# =====================================================================================
print(); print(BAR); print("PART 3 — THE TWO RIGHT-HAND SIDES ARE THE SAME BYTES WHERE THE CLOCK ENTERS")
print(BAR)
L = SRC.splitlines()
sp = spans(SRC)
rhs = sorted(i for i in jac_lines(SRC, 'evolve') + jac_lines(SRC, 'evolve_hier')
             if 'LEAFPERT' in L[i - 1])
check(len(rhs) == 2, f"two RHS clock lines, at {rhs}")
check(L[rhs[0] - 1] == L[rhs[1] - 1],
      f"lines {rhs[0]} and {rhs[1]} are character-identical: {L[rhs[0]-1].strip()!r}")
# ** the same expression appears in a COMMENT at line 175, quoting it.  Match the statement,
#    not the string: r3737's prose is about this line and is not this line. **
sel = [i for i, ln in enumerate(L, 1)
       if ln.strip().startswith('Hc, Rb =') and 'Hl_of(e) if LEAFPERT else Hc_of(e)' in ln]
check(len(sel) == 2 and L[sel[0] - 1] == L[sel[1] - 1],
      f"the rate selections at {sel} are character-identical: {L[sel[0]-1].strip()!r}")


def ops(name):
    lo, hi = sp[name]
    body = "\n".join(L[lo - 1:hi])
    return {o for o in ('Jac_of', 'Hl_of', 'Hc_of', 'Phi2_of', 'Gf_of',
                        'Og_of', 'On_of', 'Ob_of', 'Oc_of') if o in body}


miss = ops('evolve') - ops('evolve_hier')
check(not miss, f"every clock-or-source operation in evolve is also in evolve_hier "
                f"(evolve {len(ops('evolve'))}, evolve_hier {len(ops('evolve_hier'))}, missing {sorted(miss)})")
check('SRCSTACK' not in SRC and 'DIFFLEAF' not in SRC,
      "and there is no split assignment for the hierarchy to be inconsistent WITH")

# =====================================================================================
print(); print(BAR); print("PART 4 — AND IT MOVES: evolve_hier HONOURS THE CLOCK ON THE ARM WHERE IT IS NOT 1")
print(BAR)
os.environ['ARM'] = 'cr'
os.environ['NK'] = '260'
_spec = importlib.util.spec_from_file_location("ACOUSTIC_two_arm_c60", _INSTR)
AT = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(AT)

_j = [float(AT.Jac_of(e)) for e in (200.0, 300.0, 449.0, 800.0)]
check(max(abs(j - 1.0) for j in _j) > 1e-3,
      f"ARM=cr: Jac_of is not 1 — {[round(x, 5) for x in _j]} at eta = 200, 300, 449, 800")
check(AT.LEAFPERT, "LEAFPERT is on by default (r3409), so this is the configuration the CR arm runs")

e_sw = AT.eta_switch()
kb = np.array([0.01, 0.02, 0.04, 0.08])
E1 = np.linspace(AT.ETA_ON + 1.0, e_sw, 24, endpoint=False)
E2 = np.linspace(e_sw + 1.0, e_sw + 120.0, 24)


def two_segment():
    t1 = np.concatenate([E1, [e_sw]])
    with contextlib.redirect_stdout(io.StringIO()):
        s1, nk, NVf = AT.evolve(kb, t_eval=t1, e_end=e_sw)
        Y1 = s1.y.T.reshape(len(t1), nk, NVf)
        s2 = AT.evolve_hier(kb, E2, e_sw, Y1[-1])
    return s2.y.T.reshape(len(E2), nk, AT.NVH)[-1].copy()


Y_leaf = two_segment()
AT.LEAFPERT = False
Y_stack = two_segment()
AT.LEAFPERT = True
den = np.maximum(np.abs(Y_leaf), np.abs(Y_stack))
rel = float(np.max(np.abs(Y_leaf - Y_stack)[den > 1e-30] / den[den > 1e-30]))
check(rel > 1e-6, f"toggling LEAFPERT moves evolve_hier's returned state by {rel:.3e} "
                  f"relative — the hierarchy is NOT ignoring the clock operation")
print("  ⌗ On ARM=lcdm the same toggle is inert by construction and not by measurement: `C59`")
print("    asserts Jac_of == 1 to 1e-12 there, which makes both branches of the conditional the")
print("    same number.  That is why the control cannot catch a composition fault — r3512 was")
print("    right about that, and it is the one part of it that stands.")

# =====================================================================================
print(); print(BAR); print("PART 5 — THE FINDING THIS RECEIPT MADE BY NEEDING IT: HISTORY IN A SHALLOW JOB")
print(BAR)
WF = os.path.join(_ROOT, '.github', 'workflows', 'gates.yml')
wf = open(WF).read()
users = sorted({os.path.relpath(os.path.join(dp, f), _ROOT)
                for dp, _, fs in os.walk(os.path.join(_ROOT, 'receipts'))
                for f in fs if f.endswith('.py')
                if re.search(r"'git'\s*,\s*'show'", open(os.path.join(dp, f)).read())})
check(len(users) >= 2, f"{len(users)} registered receipts call `git show` on a named commit")
for u in users[:8]:
    print(f"      {u}")
heavy = wf[wf.index('  receipts:'):]
co = heavy[heavy.index('actions/checkout'):heavy.index('actions/checkout') + 160]
check('fetch-depth' not in co.split('- run:')[0],
      "the `receipts` job's checkout does not request history, while the gates job's does "
      "(`fetch-depth: 0`, line 30)")
print("  ⌗ Reported, not repaired here: this receipt is one of the affected files, so repairing")
print("    the workflow from inside it would be the verifier editing its own subject.")

# =====================================================================================
print(); print(BAR)
if FAIL:
    print(f"⛔ {len(FAIL)} CHECK(S) FAILED")
    for m in FAIL:
        print("   - " + m)
    print(BAR)
    sys.exit(1)
print("""VERDICT.  ** r3512's `HIER` composition defect is not in this instrument and was not in the
instrument r3512 was written against. **  Its remedy names `SRCSTACK` and `DIFFLEAF`, which occur
zero times in `ACOUSTIC_two_arm.py` at `95559d53`; they were real on `6beeca84`, which is not an
ancestor of it.  And the count that produced the asymmetry --- "the main path references two" ---
included `sound_phase`, a phase accumulator called once in the whole file, from inside the `QSCAN=1`
diagnostic, which computes no spectrum.  ** Like for like, each ODE right-hand side carries the clock
exactly once, in the same bytes, and neither projection carries it at all. **

** SO `C59`'s DEFERRAL IS DISCHARGED AND THE CR ARM IS NOT GATED ON A COMPOSITION FIX. **  What
gates it is convergence in $k$, which is PO-13 Run 1 and is a different question.

** AND THE FAILURE MODE IS A CORPUS-MECHANICS ONE, NOT A READING ONE. **  Two nodes held the same
instrument on two lines; an inventory compiled across both was checked against one.  ⌗ *A flag
inventory is a claim about a FILE AT A COMMIT --- c54.226 --- and this one was written as a claim
about an instrument.  The remedy that followed was specified against flags the reader could not have
run, and four documents carried the resulting deferral for two hundred revisions.*""")
print(BAR)
