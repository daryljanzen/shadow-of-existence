import re
files = {'BH_causality_v2.tex':'P1','janzen_circle_v3.tex':'P2','SdS-slicing-curve_v2.tex':'P3','modern_parallax.tex':'P4','groupoid_paper.tex':'P5','shadow_of_existence.tex':'P6','CR_framework.tex':'P7','slicing_operator.tex':'P8','range_paper.tex':'P9','canonical_time.tex':'P10','dynamics_paper.tex':'P11','algebroid_paper.tex':'P12','boundary_paper.tex':'P13','matter_sector_paper.tex':'P14','CR_cosmology.tex':'P15','cosmogenesis_paper.tex':'P16','geometric_core_paper.tex':'p0'}
key2paper = {'JanzenBHcausality':'P1','JanzenCausality':'P1','JanzenCircle':'P2','JanzenSlicing':'P3','JanzenModernParallax':'P4','JanzenParallax':'P4','JanzenGroupoid':'P5','JanzenShadowExistence':'P6','JanzenShadow':'P6','JanzenCRframework':'P7','JanzenFramework':'P7','JanzenOperator':'P8','JanzenRange':'P9','JanzenCanonicalTime':'P10','JanzenCanonical':'P10','JanzenDynamics':'P11','JanzenAlgebroid':'P12','JanzenBoundary':'P13','JanzenMatter':'P14','JanzenCRcosmology':'P15','JanzenCosmology':'P15','JanzenCosmogenesis':'P16','JanzenGeometricCore':'p0'}
order=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','p0']
cite=re.compile(r'\\cite[a-z]*\*?(?:\[[^\]]*\])?\{([^}]*)\}')
Md={a:{b:0 for b in order} for a in order}
for fn,src in files.items():
    clean='\n'.join(l for l in open(fn,encoding='utf-8',errors='replace').read().split('\n') if not l.lstrip().startswith('%'))
    for m in cite.finditer(clean):
        for k in m.group(1).split(','):
            t=key2paper.get(k.strip())
            if t and t!=src: Md[src][t]+=1
M=[[(-1 if a==b else Md[a][b]) for b in order] for a in order]
poleIdx={6,16}; diamonds={(0,3):"◇1",(3,0):"◇3"}
def shade(v):
    if v<=0: return "#ffffff"
    if v<=2: return "#eef4fa"
    if v<=6: return "#bcd6ee"
    if v<=12: return "#6ea3d6"
    if v<=20: return "#2f6fb3"
    return "#14416f"
def textcol(v): return "#ffffff" if v>=7 else "#28323c"
# build thead
th=['<th class="corner">i \\ j</th>']
for j,c in enumerate(order):
    th.append(f'<th class="{"poleh" if j in poleIdx else ""}">{c}</th>')
thead='<thead><tr>'+''.join(th)+'</tr></thead>'
rows=[]
for i,rlab in enumerate(order):
    pr='polerow' if i in poleIdx else ''
    cells=[f'<th class="{"poleh" if i in poleIdx else ""}">{rlab}</th>']
    for j in range(17):
        v=M[i][j]; pc='polecol' if j in poleIdx else ''
        if v==-1: cells.append(f'<td class="diag {pc}">—</td>'); continue
        if (i,j) in diamonds: cells.append(f'<td class="{pc}" style="background:{shade(1)};"><span class="lz">{diamonds[(i,j)]}</span></td>'); continue
        if v==0: cells.append(f'<td class="zero {pc}">·</td>'); continue
        cells.append(f'<td class="{pc}" style="background:{shade(v)};color:{textcol(v)}">{v}</td>')
    rows.append(f'<tr class="{pr}">'+''.join(cells)+'</tr>')
tbody='<tbody>'+''.join(rows)+'</tbody>'
print('<!--TABLE-->')
print(thead+tbody)
