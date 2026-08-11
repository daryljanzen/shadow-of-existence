#!/usr/bin/env python3
"""check_receipts.py -- consistency gate for the receipt-citation system.
For every \\rcpt{key} cited across corpus/*.tex: assert an INDEX row's receipt stem == key AND the file
exists in receipts/. Also lists INDEX receipts NOT yet cited (the retrofit to-do). Exit 1 on any orphan."""
import re, os, glob, sys
here=os.path.dirname(__file__); root=os.path.join(here,'..')
idx=os.path.join(root,'receipts','INDEX.md')
index_stems={}
badcols=[]
# The INDEX carries TWO row formats: '| paper | ...' and '| `stem` | paper ... |'.  The
# second (the storyboard bake, 20 rows) was skipped here until r2376+c54.36, so a \rcpt{}
# naming one of them would have been reported as an orphan that was in fact registered.
for ln in open(idx, encoding='utf-8'):
    if not (ln.startswith('| P') or ln.startswith('| `')): continue
    parts=re.split(r'(?<!\\)\|', ln.rstrip('\n'))
    cells=[p.replace('\\|','|').strip() for p in parts[1:-1]]
    if len(cells)<4 or cells[0]=='paper': continue
    path=cells[3].strip('` ')
    if path.startswith('receipts/'): path=path[len('receipts/'):]
    stem=os.path.splitext(os.path.basename(path))[0]
    index_stems[stem]=path
    if len(cells)!=8:  # COLUMN LINT: a data row must have 8 columns; more = an unescaped '|' (escape math bars as \|)
        # PROMOTED TO A FAILURE at r2376+c54.83.  It was a WARNING, and a warning is not enough:
        # a mis-celled row makes cells[3] the wrong cell, so the appendix generator drops the
        # receipt ENTIRELY.  If the receipt is cited, check_compile catches it downstream as a
        # dead link -- but an UNCITED receipt vanishes from the reproducibility layer with
        # nothing downstream to notice.  Two rows were written this way at c54.83.
        badcols.append((stem, len(cells)))
        print(f"  [FAIL] INDEX row for {stem!r} has {len(cells)} columns (expect 8) -- an unescaped '|' math bar; escape it as \\|")
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
for _ln in open(idx, encoding='utf-8'):
    if not (_ln.startswith('| P') or _ln.startswith('| `')):
        continue
    _c = [x.replace('\\|', '|').strip() for x in re.split(r'(?<!\\)\|', _ln.rstrip('\n'))[1:-1]]
    if len(_c) != 8 or _c[0] == 'paper':
        continue
    _st = os.path.splitext(os.path.basename(_c[3].strip('` ')))[0]
    _origin[_st] = _c[7]
    _bound[_st] = _c[6]
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
CHECKS = re.compile(r'^\s*assert\b|fail\.append|allpass\s*&=|^\s*sys\.exit\(1\)'
                    r'|raise SystemExit\(1\)', re.M)
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
if badcols:
    print(f"\nFAIL: {len(badcols)} INDEX row(s) with a broken column count -- "
          f"the appendix generator silently DROPS these receipts.")
    sys.exit(1)
if orphans:
    print(f"\nFAIL: {len(orphans)} orphan citation(s)."); sys.exit(1)
print("\nAll \\rcpt{} citations resolve to an INDEX row + a file on disk.")
