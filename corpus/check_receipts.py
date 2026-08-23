#!/usr/bin/env python3
"""check_receipts.py -- consistency gate for the receipt-citation system.
For every \\rcpt{key} cited across corpus/*.tex: assert an INDEX row's receipt stem == key AND the file
exists in receipts/. Also lists INDEX receipts NOT yet cited (the retrofit to-do). Exit 1 on any orphan."""
import re, os, glob, sys
here=os.path.dirname(__file__); root=os.path.join(here,'..')
sys.path.append(os.path.abspath(here))
import index_rows            # ** c54.222: the row filter lives ONCE now.  See its head. **
idx=os.path.join(root,'receipts','INDEX.md')
index_stems={}
badcols=[]
_norow=[]       # rows naming a `.py` that does not exist -- c54.222; see the note at the check below
_stem_rows={}   # stem -> [paths], to catch a stem registered at more than one row
# The INDEX carries TWO row formats: '| paper | ...' and '| `stem` | paper ... |'.  The
# second (the storyboard bake, 20 rows) was skipped here until r2376+c54.36, so a \rcpt{}
# naming one of them would have been reported as an orphan that was in fact registered.
# ** r2533+c54.203: THE PAPER COLUMN IS CASE-SENSITIVE HERE AND THE CORPUS IS NOT. **  This read
# ** `ln.startswith('| P')`, and the geometric core paper is written `p0` in LOWERCASE everywhere
# ** by the corpus's own convention -- so ALL NINE of its INDEX rows were invisible to this gate.
# ** Nobody hit it because no \rcpt{} had ever named one; c54.203's Higgs receipt is the first,
# ** and it read as an orphan while its row sat in the file. **
#   *A gate that skips a row silently reports the row's receipt as unregistered -- which is the
#    same shape as the duplicate-stem guard below: a gate blind to a row it should be policing.*
#
# ** ⛭⛭ c54.222 -- AND THE PAPER COLUMN WAS STILL DECIDING MEMBERSHIP.  The corpus writes an EM-DASH
# ** there for a receipt supporting no paper, so TWENTY rows were dropped here too. **  The predicate
# ** is gone, not patched a third time; `corpus/index_rows.py` holds it once for all five readers. **
#   ⇒ *** AND THE COLUMN LINT BELOW SAT INSIDE THIS LOOP, so it inherited the filter's blind spot and
#       reported green from inside it -- while TWO em-dash rows sat column-split since r2674.  A lint
#       downstream of a filter checks the rows the filter already liked. ***
for _r in index_rows.rows(resolve_paths=True, root=os.path.abspath(root)):
    cells=_r.cells
    path=_r.token
    if path.startswith('receipts/'): path=path[len('receipts/'):]
    stem=_r.stem
    _stem_rows.setdefault(stem, []).append(path)
    index_stems[stem]=path
    if len(cells)!=8:  # COLUMN LINT: a data row must have 8 columns; more = an unescaped '|' (escape math bars as \|)
        # PROMOTED TO A FAILURE at r2376+c54.83.  It was a WARNING, and a warning is not enough:
        # a mis-celled row makes cells[3] the wrong cell, so the appendix generator drops the
        # receipt ENTIRELY.  If the receipt is cited, check_compile catches it downstream as a
        # dead link -- but an UNCITED receipt vanishes from the reproducibility layer with
        # nothing downstream to notice.  Two rows were written this way at c54.83.
        badcols.append((stem, len(cells)))
        print(f"  [FAIL] INDEX row for {stem!r} has {len(cells)} columns (expect 8) -- an unescaped '|' math bar; escape it as \\|")
    # ** ⛔ c54.222 -- THE ROW-OUTWARD CHECK, WHICH THIS GATE HAD NEVER MADE. **  Everything below
    # validates CITATIONS INWARD: a \rcpt{} must reach a row and a file.  *** An UNCITED row naming a
    # file that does not exist was therefore checked by nothing -- and `X4_singularity_types.py` and
    # `X3_seam_schwarz_reflection.py` have never existed in ANY of the 486 commits reachable from any
    # ref, while both are printed into P3's, P7's and the corpus appendix marked `[OK]`. ***
    if _r.runnable and not _r.paths:
        _norow.append((_r.lineno, _r.token))
        print(f"  [FAIL] INDEX line {_r.lineno} registers {_r.token!r} -- NO SUCH FILE, searched "
              f"receipts/ and the repository root, globbed")
# --- DUPLICATE-STEM GUARD (added r2376+c54.182) -------------------------------------------
# index_stems[stem]=path SILENTLY COLLAPSES two rows sharing a stem: whichever row appears
# LATER in the file wins, so \rcpt{} resolution, the assertion census, and the origin/bound
# cells all read one row and never see the other -- and WHICH one is decided by file order,
# not by intent.  This is the receipt-layer twin of the ratchet hole: a gate blind to a row
# it should be policing.  Eighteen stems sat this way at c54.181 -- seventeen a storyboard
# origin plus its receipts/<paper>/ copy, one a plain double -- and the census counted each
# once purely because the copy happened to come later.  A stem is a KEY; it may be registered
# at exactly one row.  (A storyboard origin needs no INDEX row of its own: its receipts/ copy
# carries an `ORIGIN:` pointer and the ORIGIN drift guard below ties the two together.)
dup_stems={s: ps for s, ps in _stem_rows.items() if len(ps) > 1}
for _s in sorted(dup_stems):
    print(f"  [FAIL] stem {_s!r} registered at {len(dup_stems[_s])} rows ({', '.join(dup_stems[_s])}) "
          f"-- one stem, one registration; the later row silently shadows the earlier")
cited=set()
for tex in glob.glob(os.path.join(here,'*.tex')):
    for m in re.finditer(r'\\rcpt\{([^}]+)\}', open(tex).read()):
        cited.add((m.group(1), os.path.basename(tex)))
orphans=[]
for key,tex in sorted(cited):
    in_index = key in index_stems
    on_disk = in_index and os.path.exists(os.path.join(root,'receipts',index_stems[key]))
    tag = 'OK' if (in_index and on_disk) else ('NO INDEX ROW' if not in_index else 'FILE MISSING')
    print(f"  [{ 'PASS' if tag=='OK' else 'FAIL'}] \\rcpt{{{key}}} in {tex}: {tag}")
    if tag!='OK': orphans.append((key,tex,tag))
cited_keys={k for k,_ in cited}
uncited=[s for s in index_stems if s not in cited_keys]
print(f"\n  INDEX receipts not yet cited in any paper ({len(uncited)}):")
for s in sorted(uncited): print(f"    - {s}")

# --- ORIGIN drift guard (added r2376, c54) -------------------------------------------------
# A receipts/ copy carrying "ORIGIN: <path>" must not diverge in CODE from that origin.
# Docstrings may differ (the copy carries the registration header); executable content may not.
# This exists because a sweep updated an origin and left its cited copy stale -- silently.
import ast as _ast
def _code(p):
    t=open(p).read()
    try:
        m=_ast.parse(t)
        if m.body and isinstance(m.body[0],_ast.Expr) and isinstance(getattr(m.body[0],'value',None),_ast.Constant) \
           and isinstance(m.body[0].value.value,str):
            _ln=getattr(m.body[0],'end_lineno',None)
            if _ln: return '\n'.join(t.split('\n')[_ln:])
    except Exception: pass
    return t
_drift=[]
for _r,_d,_fs in os.walk(os.path.join(root,'receipts')):
    for _f in _fs:
        if not _f.endswith('.py'): continue
        _p=os.path.join(_r,_f); _t=open(_p).read()
        _m=re.search(r'ORIGIN:\s*([^\s,;]+\.py)', _t)
        if not _m: continue
        _o=os.path.join(root,_m.group(1))
        if not os.path.exists(_o): 
            _drift.append((_p,_m.group(1),'ORIGIN MISSING')); continue
        if ''.join(_code(_p).split()) != ''.join(_code(_o).split()):
            _adj = 'ORIGIN-DIVERGENCE:' in _t
            _drift.append((_p,_m.group(1),'ADJUDICATED (documented)' if _adj else 'CODE DIVERGES'))
_un=[d for d in _drift if d[2]=='CODE DIVERGES' or d[2]=='ORIGIN MISSING']
_ad=[d for d in _drift if d not in _un]
print(f"\n  ORIGIN drift guard: {len(_un)} unexplained, {len(_ad)} adjudicated")
for _p,_o,_w in _un: print(f"    [WARN] {os.path.relpath(_p,root)} vs {_o}: {_w}")
for _p,_o,_w in _ad: print(f"    [ok]   {os.path.relpath(_p,root)} vs {_o}: {_w}")

# --- UNCITED-RECEIPT DEBT (added r2376+c54.87) --------------------------------------------
# A receipt registered in the INDEX but cited by no paper is a banked result that never landed.
# check_supersession catches a LEAD answered by banked work; this catches banked work that
# reached no paper at all -- the same failure one level over.  Five such were found at c54.87,
# all built during the colour arc or the leads sweep, including one whose own INDEX label read
# "NOT cited in any paper".  Receipts built in the CURRENT fork (c54) FAIL; the older backlog is
# reported so it cannot quietly grow.
_origin = {}
_bound = {}
# ** r2555: a SECOND load site in this same file, missed when the first was fixed at c54.203. **
# The paper column is case-sensitive and the geometric core is `p0` lowercase, so this dict was
# built without p0's rows while the check above had been corrected.
#   ⇒ *** One fix per FILE is not one fix per LOAD SITE, and a file that loads the same table twice
#       can be half-fixed with nothing to show it. ***
# ** c54.222: which is exactly why both sites now call the same reader rather than the same STRING. **
for _r in index_rows.rows(root=os.path.abspath(root)):
    if not _r.well_formed:
        continue
    _origin[_r.stem] = _r.origin
    _bound[_r.stem] = _r.bound
# A PROCESS receipt records a sweep or a batch rather than a claim of a paper, so it is not
# owed a citation.  The opt-out must be written deliberately into the INDEX row's bound cell.
_PROCESS = 'NOT-A-PAPER-CLAIM'
# A landing that is SECTION-SIZED rather than a sentence may be deferred, but only by being
# REGISTERED as a lead -- the marker must name it, and check_burndown then polices the lead.
_DEFER = re.compile(r'LANDING REGISTERED AS (L-\d+)')
_deferred = {s_: _DEFER.search(_bound.get(s_, '')).group(1) for s_ in index_stems
             if s_ not in cited_keys and _DEFER.search(_bound.get(s_, ''))}
_arc_unc = sorted(s_ for s_ in index_stems
                  if s_ not in cited_keys and 'c54' in _origin.get(s_, '')
                  and _PROCESS not in _bound.get(s_, '') and s_ not in _deferred)
_old_unc = sorted(s_ for s_ in index_stems
                  if s_ not in cited_keys and 'c54' not in _origin.get(s_, ''))
print(f"\n  UNCITED-RECEIPT DEBT: {len(_arc_unc)} from the current fork, {len(_old_unc)} older")
for _s in _arc_unc:
    print(f"    [FAIL] {_s} -- registered this fork and cited by no paper")
if _deferred:
    print(f"    ({len(_deferred)} deferred, each naming the lead that owes the landing: "
          f"{', '.join(sorted(set(_deferred.values())))})")
if _old_unc:
    print(f"    (older backlog, reported not failed: {len(_old_unc)} -- "
          f"{', '.join(_old_unc[:5])}{' ...' if len(_old_unc) > 5 else ''})")

# =================================================================================================
# ** THE ASSERTION CENSUS, added r2376+c54.154. **
#
# ** WHY. **  The c54.153 receipt-vs-sentence pass read twenty-eight cited receipts against the
# sentences citing them and found fourteen matches.  The single mechanism behind most of the
# misses was not a wrong link: it was A RECEIPT THAT CANNOT FAIL.  Three receipts in one cluster
# contained no assertion at all -- print statements end to end -- so their `OK` status certified
# that Python exited zero and nothing more.  That is how P15's claim that its low-multipole depths
# are "stable under +/-2% in r_0" rode inside a green receipt, cited twice, for two revisions: the
# file set r_0 once, consumed it once, and PRINTED the stability claim as a string.  Measured when
# finally run, the depths drift by 15%.
#
# ** A RECEIPT WITH NO CHECK IS A PRINT STATEMENT WITH A FILENAME. **
#
# ** THE SHAPE OF THE RULE, and it is a RATCHET rather than a cliff. **  188 of 276 receipts had no
# check when this census was written -- two thirds of the reproducibility layer.  Failing all of
# them at once would make the gate unrunnable and would be a demand rather than an instrument.  So:
#   (i)  ANY receipt registered in THIS FORK must carry at least one check.  No new debt.
#   (ii) The TOTAL must not exceed the baseline recorded in receipts/ASSERTION_DEBT.txt, which is
#        rewritten downward as the backlog is worked and may never be rewritten upward.
# The debt is therefore visible, monotone decreasing, and owned.
# ** THE CHECK TEST IS TWO-PART FROM r2376+c54.179, AND THE OLD ONE HID A REAL DEFECT. **
# It read  `^\s*assert\b|fail\.append|allpass\s*&=|^\s*sys\.exit\(1\)|raise SystemExit\(1\)`  and had
# two blind spots that pulled in opposite directions:
#   TOO NARROW -- case-sensitive on `fail`, literal on `SystemExit(1)`, so a receipt using a `check()`
#     helper with an UPPERCASE failure list and `raise SystemExit(main())` read as carrying NO check.
#     Thirteen receipts were reported that way; node 56 broke a claim inside one and it returned rc=1.
#   TOO WIDE -- `allpass &=` counted as a check ON ITS OWN.  ** Bookkeeping is not acting: a receipt
#     that accumulates `allpass` and never reads it exits 0 however its checks came out. **  That is
#     exactly what `P15_expansion_law.py` did, registered and of this fork, for the whole assertion
#     sweep -- a broken claim printed two FAILs and returned rc=0, and this gate passed it.
# So a failure-collection idiom now counts only WITH a non-zero exit path; an explicit exit(1) still
# counts alone, since it IS the acting.  `scripts/lint_assertions.py` carries the same rule and the
# two are checked against each other below, because a rule in two places drifts.
# ** ⛭⛭ r3126 (`L-254`): THE RULE MOVED TO `corpus/acting_check.py` AND IS IMPORTED, NOT COPIED. **
# *It lived here and in `scripts/lint_assertions.py`, guarded by a TEXT COMPARISON -- a guard that
# reports a divergence after both copies are written and cannot prevent one.  `L-252` banked the
# alternative on a different pair: import from the instrument that defines it.*
#   ⇒ ** And the rule gained a THIRD clause, because the two it had were SPELLINGS and a rule made
#     of spellings misses the next spelling. **  *`P07_cube_root_two_is_the_2M_over_M` accumulates
#     `bad |= (not okN)` over four sympy comparisons and ends `sys.exit(1 if bad else 0)`; it was
#     reported as carrying "NO check at all".*  ⇒ *** The third clause asks the question the census
#     MEANS -- does a non-zero exit depend on the outcome of a comparison? ***
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('_ac', os.path.join(root, 'corpus', 'acting_check.py'))
_ac = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_ac)
_COLLECT, _NZEXIT, _EXPLICIT = _ac.COLLECT, _ac.NZEXIT, _ac.EXPLICIT


class _ChecksRule:
    """the rule, wearing re.compile's interface so the call sites below do not change"""

    def search(self, src):
        return _ac.carries_a_check(src)


CHECKS = _ChecksRule()
_DEBT_FILE = os.path.join(root, 'receipts', 'ASSERTION_DEBT.txt')
_nocheck = []
for _st in sorted(index_stems):
    _f = os.path.join(root, 'receipts', index_stems[_st])
    if not os.path.exists(_f):
        continue
    if not CHECKS.search(open(_f, encoding='utf-8', errors='replace').read()):
        _nocheck.append(_st)
_fork_nocheck = sorted(s_ for s_ in _nocheck if 'c54' in _origin.get(s_, ''))
# ** THE GRANDFATHERED LIST. **  36 receipts of this fork predate the rule.  They are NAMED here
# rather than covered by a number, because a named list cannot grow quietly and every entry is a
# to-do with an owner.  A fork receipt NOT on the list and carrying no check is a failure.
try:
    _txt = open(_DEBT_FILE).read()
    _baseline = int(_txt.split()[0])
    _grand = set(re.findall(r'(?m)^\s{4}-\s+(\S+)\s*$', _txt))
except Exception:
    _baseline, _grand = len(_nocheck), set(_fork_nocheck)
_new_debt = [s_ for s_ in _fork_nocheck if s_ not in _grand]
_settled = sorted(s_ for s_ in _grand if s_ not in _nocheck)
print(f"\n  ASSERTION CENSUS: {len(_nocheck)} of {len(index_stems)} registered receipt(s) carry NO "
      f"check at all (baseline {_baseline})")
print(f"    a receipt with no assertion is a print statement with a filename: its OK certifies")
print(f"    that Python exited zero.  THE_BASE_RATE's sixteenth entry.")
print(f"    of these, {len(_fork_nocheck)} are this fork's own, all named in the debt file")
for _s in _new_debt:
    print(f"    [FAIL] {_s} -- registered this fork with no check and not on the grandfathered list")
if len(_nocheck) > _baseline:
    print(f"    [FAIL] the debt ROSE from {_baseline} to {len(_nocheck)}; the baseline may only "
          f"be rewritten downward")
if _settled:
    print(f"    ({len(_settled)} grandfathered receipt(s) now carry checks and should be struck "
          f"from the debt file: {', '.join(_settled[:6])}{' ...' if len(_settled) > 6 else ''})")
if _new_debt or len(_nocheck) > _baseline:
    print(f"\nFAIL: the assertion census. A receipt that cannot fail is a print statement with a "
          f"filename, and the debt must not rise.")
    sys.exit(1)
if len(_nocheck) < _baseline:
    print(f"    (debt DOWN {_baseline - len(_nocheck)} this revision -- rewrite "
          f"receipts/ASSERTION_DEBT.txt to {len(_nocheck)})")

# --- THE HOLLOW-ASSERTION LINT, wired in r2376+c54.158 -------------------------------------------
# The assertion sweep is dispatchable, and that is exactly its danger: a worker asked to make a
# file "able to fail" can satisfy the count with a check that cannot.  scripts/lint_assertions.py
# classifies every assertion in the tree as HOLLOW / UNPINNED / PINNED and exits 1 on the first
# hollow one.  ** A hollow assertion is worse than none: it converts a known gap into an unknown
# one, and it makes the debt number above lie. **  So the census and the lint are one gate.
import subprocess as _sub
_lint = os.path.join(root, 'scripts', 'lint_assertions.py')
if os.path.exists(_lint):
    _r = _sub.run([sys.executable, _lint], capture_output=True, text=True)
    _tail = [l for l in _r.stdout.split('\n') if l.strip()][-6:]
    print()
    for _l in _tail:
        print(_l)
    if _r.returncode != 0:
        print("\nFAIL: the hollow-assertion lint. See the lines above.")
        sys.exit(1)

if _arc_unc:
    print(f"\nFAIL: {len(_arc_unc)} receipt(s) built in this fork reach no paper. "
          f"A result that lands in no paper is not banked, it is lost.")
    sys.exit(1)
if dup_stems:
    print(f"\nFAIL: {len(dup_stems)} stem(s) registered at more than one INDEX row -- a duplicate "
          f"stem is collapsed by file order, so one registration shadows the other unseen.")
    sys.exit(1)
if badcols:
    print(f"\nFAIL: {len(badcols)} INDEX row(s) with a broken column count -- "
          f"the appendix generator silently DROPS these receipts.")
    sys.exit(1)
if _norow:
    print(f"\nFAIL: {len(_norow)} INDEX row(s) register a `.py` that does not exist -- "
          f"the appendix prints them as [OK].")
    print("  ** A row is a claim that a computation EXISTS.  Checking citations inward never asks it. **")
    sys.exit(1)
if orphans:
    print(f"\nFAIL: {len(orphans)} orphan citation(s)."); sys.exit(1)
print("\nAll \\rcpt{} citations resolve to an INDEX row + a file on disk, and every registered row "
      "resolves to a file.")
