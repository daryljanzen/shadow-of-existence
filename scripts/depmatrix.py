#!/usr/bin/env python3
# Authoritative corpus citation-matrix generator. Maintains P7 tab:dependency-matrix + BOOK_INTRO_cosmiCave/assets/dependency_matrix.html.
# Run from corpus/ ; resolver mirrors BIBKEY_ALIAS_MAP.md. Re-run after any citation change and paste the LATEX + HTML blocks.
import re
files = {'BH_causality_v2.tex':'P1','janzen_circle_v3.tex':'P2','SdS-slicing-curve_v2.tex':'P3','modern_parallax.tex':'P4','groupoid_paper.tex':'P5','shadow_of_existence.tex':'P6','CR_framework.tex':'P7','slicing_operator.tex':'P8','range_paper.tex':'P9','canonical_time.tex':'P10','dynamics_paper.tex':'P11','algebroid_paper.tex':'P12','boundary_paper.tex':'P13','matter_sector_paper.tex':'P14','CR_cosmology.tex':'P15','cosmogenesis_paper.tex':'P16','geometric_core_paper.tex':'P17'}
key2paper = {'JanzenBHcausality':'P1','JanzenCircle':'P2','JanzenSlicing':'P3','JanzenModernParallax':'P4','JanzenGroupoid':'P5','JanzenShadowExistence':'P6','JanzenCRframework':'P7','JanzenOperator':'P8','JanzenRange':'P9','JanzenCanonicalTime':'P10','JanzenDynamics':'P11','JanzenAlgebroid':'P12','JanzenBoundary':'P13','JanzenMatter':'P14','JanzenCRcosmology':'P15','JanzenCosmogenesis':'P16','JanzenGeometricCore':'P17'}
order=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17']
cite=re.compile(r'\\cite[a-z]*\*?(?:\[[^\]]*\])?\{([^}]*)\}')
M={a:{b:0 for b in order} for a in order}
for fn,src in files.items():
    clean='\n'.join(l for l in open(fn,encoding='utf-8',errors='replace').read().split('\n') if not l.lstrip().startswith('%'))
    for m in cite.finditer(clean):
        for k in m.group(1).split(','):
            t=key2paper.get(k.strip())
            if t and t!=src: M[src][t]+=1
labels={'P1':'P1 \; wedge','P2':'P2 \; circle','P3':'P3 \; slicing','P4':'P4 \; mod.\\ parallax','P5':'P5 \; groupoid','P6':'P6 \; shadow','P7':'\\textbf{P7 \; framework}','P8':'P8 \; operator','P9':'P9 \; range','P10':'P10 \; canon.\\ time','P11':'P11 \; dynamics','P12':'P12 \; algebroid','P13':'P13 \; boundary','P14':'P14 \; matter','P15':'P15 \; cosmology','P16':'P16 \; cosmogenesis','P17':'\\textbf{P17 \; core}'}
print("===== LATEX TABULAR ROWS =====")
for a in order:
    cells=[]
    bold = a in ('P7','P17')
    for b in order:
        if a==b: cells.append('--'); continue
        v=M[a][b]
        s='.' if v==0 else str(v)
        if (a,b)==('P1','P4'): s='$\\lozenge$'+ (str(v) if v else '')
        if (a,b)==('P4','P1'): s='$\\lozenge$'+ (str(v) if v else '')
        if bold and s!='--': s='\\textbf{'+s+'}'
        cells.append(s)
    print(labels[a]+' & '+' & '.join(cells)+'\\\\')
print("\n===== HTML M ARRAY =====")
for a in order:
    row=[]
    for b in order:
        row.append(-1 if a==b else M[a][b])
    print(' ['+','.join(f"{x:>2}" for x in row)+'],')

def _color(v):
    if v <= 2:  return ('#eef4fa','#28323c')
    if v <= 6:  return ('#bcd6ee','#28323c')
    if v <= 12: return ('#6ea3d6','#ffffff')
    if v <= 25: return ('#2f6fb3','#ffffff')
    return ('#14416f','#ffffff')
_poles=('P7','P17')
print("\n===== HTML STYLED TABLE (replace <table>...</table> in dependency_matrix.html) =====")
_h='<table><thead><tr><th class="corner">i \\ j</th>'
for b in order:
    _h+=f'<th class="{"poleh" if b in _poles else ""}">{b}</th>'
_h+='</tr></thead><tbody>'
for a in order:
    _h+=f'<tr class="{"polerow" if a in _poles else ""}"><th class="{"poleh" if a in _poles else ""}">{a}</th>'
    for b in order:
        pc='polecol' if b in _poles else ''
        if a==b:
            _h+=f'<td class="{"diag polecol" if a in _poles else "diag "}">\u2014</td>'
        elif (a,b) in (('P1','P4'),('P4','P1')):
            v=M[a][b]; bg=_color(v)[0]
            _h+=f'<td class="{pc}" style="background:{bg};"><span class="lz">\u25c7{v}</span></td>'
        elif M[a][b]==0:
            _h+=f'<td class="zero {pc}">\u00b7</td>'
        else:
            v=M[a][b]; bg,fg=_color(v)
            _h+=f'<td class="{pc}" style="background:{bg};color:{fg}">{v}</td>'
    _h+='</tr>'
_h+='</tbody></table>'
print(_h)
print("\n===== KEY TOTALS for caption checks =====")
print("P7 row (cites):", {b:M['P7'][b] for b in order if M['P7'][b]})
print("P17 row (cites):", {b:M['P17'][b] for b in order if M['P17'][b]})
print("P3 column total (most-drawn-on):", sum(M[a]['P3'] for a in order))
print("foundational feeds P7<-:", {x:M['P7'][x] for x in ['P1','P2','P3','P4','P5','P6']})
print("foundational dep edges: P6<-P1",M['P6']['P1'],"P3<-P2",M['P3']['P2'],"P5<-P2",M['P5']['P2'],"P5<-P3",M['P5']['P3'],"P5<-P4",M['P5']['P4'],"P6<-P4",M['P6']['P4'],"P6<-P5",M['P6']['P5'])

# ============================================================================
#  THE LEDGER BLOCK -- how many times each paper cites each knowledge ledger.
#
#  This is the second half of the reference system: the paper-by-paper matrix
#  above counts internal \cite edges, and this counts \ldg markers into the
#  eighteen knowledge ledgers.  Rows are LEDGERS, columns are PAPERS, so the
#  block sits under the matrix sharing its column headers and a column reads
#  top-to-bottom as one paper's whole draw -- its own sources, then the worked
#  mathematics behind them.
#
#  THE ROW SET IS READ FROM DISK, NEVER HARD-CODED.  Six further fields are
#  queued, so any constant here would acquire exactly the defect the gate at
#  r3522 was repaired for.  A zero is a finding and prints as a zero: a field
#  that legitimately gave a paper nothing must be legible as such, and the
#  landing tables carry the reason.
# ============================================================================
import os as _os, re as _re
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_IDX  = _os.path.join(_ROOT, 'corpus', 'ledgers_registry.md')

def _ledger_keys():
    keys, started = [], False
    for ln in open(_IDX, encoding='utf-8'):
        t = ln.strip()
        if not t.startswith('|'):
            continue
        if set(t) <= set('|-: '):
            started = True; continue
        if not started:
            continue
        cells = [c.strip() for c in t.strip('|').split('|')]
        if len(cells) >= 4:
            keys.append(cells[0].strip('`'))
    return keys

_LDG = _re.compile(r'\\ldg\{([^}]*)\}')

def _ldg_counts():
    counts = {}
    for fn, lab in files.items():
        path = _os.path.join(_ROOT, 'corpus', fn)
        if not _os.path.exists(path):
            continue
        body = open(path, encoding='utf-8', errors='replace').read()
        body = '\n'.join(l for l in body.split('\n') if not l.lstrip().startswith('%'))
        for k in _LDG.findall(body):
            counts[(k, lab)] = counts.get((k, lab), 0) + 1
    return counts

_keys = _ledger_keys()
_C = _ldg_counts()
_unknown = sorted({k for (k, _l) in _C} - set(_keys))

print("\n===== LEDGER BLOCK: rows = ledgers, columns = papers, entry = \\ldg markers =====")
if _unknown:
    print("  [FAIL] marker(s) naming a ledger absent from corpus/ledgers_registry.md:", ", ".join(_unknown))
_w = max(len(k) for k in _keys)
print(' ' * (_w + 2) + ' '.join(f'{b:>4}' for b in order))
for k in _keys:
    row = ''.join(f'{(_C.get((k,b),0) or 0):>5}' for b in order)
    print(f'  {k:<{_w}}{row}')
print("  " + "-" * (_w + 5 * len(order)))
print(f'  {"TOTAL":<{_w}}' + ''.join(f'{sum(_C.get((k,b),0) for k in _keys):>5}' for b in order))
print(f"\n  {sum(_C.values())} marker(s) across {len({l for (_k,l) in _C})} paper(s) "
      f"and {len({k for (k,_l) in _C})} of {len(_keys)} ledgers.")

print("\n===== LEDGER BLOCK, LATEX ROWS (append under tab:dependency-matrix) =====")
for k in _keys:
    cells = ' & '.join(('.' if _C.get((k, b), 0) == 0 else str(_C[(k, b)])) for b in order)
    print(f'\\textsf{{{k.replace("_", " ")}}} & {cells}\\\\')
