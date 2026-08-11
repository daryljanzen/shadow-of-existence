import re
files = {'BH_causality_v2.tex':'P1','janzen_circle_v3.tex':'P2','SdS-slicing-curve_v2.tex':'P3','modern_parallax.tex':'P4','groupoid_paper.tex':'P5','shadow_of_existence.tex':'P6','CR_framework.tex':'P7','slicing_operator.tex':'P8','range_paper.tex':'P9','canonical_time.tex':'P10','dynamics_paper.tex':'P11','algebroid_paper.tex':'P12','boundary_paper.tex':'P13','matter_sector_paper.tex':'P14','CR_cosmology.tex':'P15','cosmogenesis_paper.tex':'P16','geometric_core_paper.tex':'p0'}
key2paper = {'JanzenBHcausality':'P1','JanzenCausality':'P1','JanzenCircle':'P2','JanzenSlicing':'P3','JanzenModernParallax':'P4','JanzenParallax':'P4','JanzenGroupoid':'P5','JanzenShadowExistence':'P6','JanzenShadow':'P6','JanzenCRframework':'P7','JanzenFramework':'P7','JanzenOperator':'P8','JanzenRange':'P9','JanzenCanonicalTime':'P10','JanzenCanonical':'P10','JanzenDynamics':'P11','JanzenAlgebroid':'P12','JanzenBoundary':'P13','JanzenMatter':'P14','JanzenCRcosmology':'P15','JanzenCosmology':'P15','JanzenCosmogenesis':'P16','JanzenGeometricCore':'p0'}
order=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','p0']
cite=re.compile(r'\\cite[a-z]*\*?(?:\[[^\]]*\])?\{([^}]*)\}')
M={a:{b:0 for b in order} for a in order}
for fn,src in files.items():
    clean='\n'.join(l for l in open(fn,encoding='utf-8',errors='replace').read().split('\n') if not l.lstrip().startswith('%'))
    for m in cite.finditer(clean):
        for k in m.group(1).split(','):
            t=key2paper.get(k.strip())
            if t and t!=src: M[src][t]+=1
def shade(v):
    if v<=2: return '#eef4fa','#28323c'
    if v<=6: return '#bcd6ee','#28323c'
    if v<=12: return '#6ea3d6','#ffffff'
    if v<=20: return '#2f6fb3','#ffffff'
    return '#14416f','#ffffff'
poles={'P7','p0'}
out=[]
for a in order:
    rowcls=' class="polerow"' if a in poles else ' class=""'
    thcls='poleh' if a in poles else ''
    cells=[f'<th class="{thcls}">{a}</th>']
    for b in order:
        polec = b in poles
        pc=' polecol' if polec else ''
        if a==b:
            cells.append(f'<td class="diag{(" polecol" if polec else " ")}">—</td>'); continue
        v=M[a][b]
        if (a,b) in (('P1','P4'),('P4','P1')):
            bg,_=shade(v if v else 1)
            cells.append(f'<td class="{("polecol" if polec else "")}" style="background:{bg};"><span class="lz">◇{v}</span></td>'); continue
        if v==0:
            cells.append(f'<td class="zero {("polecol" if polec else "")}">·</td>'); continue
        bg,tc=shade(v)
        cells.append(f'<td class="{("polecol" if polec else "")}" style="background:{bg};color:{tc}">{v}</td>')
    out.append(f'<tr{rowcls}>'+''.join(cells)+'</tr>')
print('<tbody>'+''.join(out)+'</tbody>')
