"""measure.py -- r7170+70.1 (70) PO-85 M1-M4: citing sites, joinable sites, graded and attributable sites.

  python3 measure.py              # on the working tree
Prints the counts, and writes sites.json (every citing site with its grade tags) and ungraded_sample.txt (20
ungraded sites, seeded, for the hand read of the lexicon's misses -- the r3932 rule).
"""
import json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7043_70_citation_sweep'))
import trace_citations as T  # noqa: E402

OWN = {'BH_causality_v2': 'BHcausality', 'CR_cosmology': 'CRcosmology', 'CR_framework': 'CRframework',
       'CR_synthesis': 'Synthesis', 'SdS-slicing-curve_v2': 'Slicing', 'algebroid_paper': 'Algebroid',
       'boundary_paper': 'Boundary', 'canonical_time': 'CanonicalTime', 'cosmogenesis_paper': 'Cosmogenesis',
       'dynamics_paper': 'Dynamics', 'geometric_core_paper': 'GeometricCore', 'groupoid_paper': 'Groupoid',
       'janzen_circle_v3': 'Circle', 'matter_sector_paper': 'Matter', 'modern_parallax': 'ModernParallax',
       'range_paper': 'Range', 'shadow_of_existence': 'ShadowExistence', 'slicing_operator': 'Operator'}
LEX = {
    'THEOREM': r'\bprov(?:e|es|ed|en|ing)\b|\bproof\b|\btheorem\b|\bproposition\b|\blemma\b|\bderiv(?:e|es|ed|ation)\b|\bestablish(?:es|ed)?\b|\bshow(?:s|n|ed)?\b',
    'MEASURED': r'\bmeasur(?:e|es|ed|ement)\b|\bcomput(?:e|es|ed|ation)\b|\bnumerical(?:ly)?\b',
    'CONJECTURE': r'\bconjectur\w*|\bexpect(?:s|ed)?\b|\bargu(?:e|es|ed)\b|\bpropos(?:e|es|ed)\b|\bsuggest(?:s|ed)?\b|\bhypothes\w*',
    'OPEN': r'\bopen\b|\btest(?:s|ed|able)?\b|\buntested\b|not settled|\bheld to\b|falsif\w*|would discriminate',
}
LOC = re.compile(r'\\cite[pt]?\[[^\]]+\]\{Janzen|\b(?:Theorem|Proposition|Lemma|Corollary|Conjecture|Prop\.|Thm\.)~?\s*(?:\\ref\{|\d)')
CITE = re.compile(r'\\cite[pt]?(?:\[[^\]]*\])?\{([^}]*)\}')
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z\\$(])')


def sites(root):
    out = []
    for stem, own in OWN.items():
        p = os.path.join(root, 'corpus', stem + '.tex')
        if not os.path.exists(p):
            continue
        t = T.strip(open(p, encoding='utf-8', errors='replace').read())
        for s in SENT.split(t):
            keys = [k.strip() for m in CITE.finditer(s) for k in m.group(1).split(',')]
            other = sorted({k for k in keys if k.startswith('Janzen') and k != 'Janzen' + own and k != 'JanzenThesis'})
            if not other:
                continue
            flat = ' '.join(s.split())
            tags = sorted(g for g, rx in LEX.items() if re.search(rx, flat, re.I))
            out.append(dict(paper=stem, cites=other, joinable=bool(LOC.search(flat)), grades=tags,
                            ncite=len(set(keys)), text=flat[:600]))
    return out


def main(root=ROOT):
    S = sites(root)
    n = len(S)
    j = sum(s['joinable'] for s in S)
    g = sum(bool(s['grades']) for s in S)
    a = sum(bool(s['grades']) and s['ncite'] == 1 for s in S)
    print(f'  M1 citing sites (cross-paper, appendices excluded): {n}')
    print(f'  M2 joinable (a locator or a numbered result of the cited paper): {j}  ({100*j/n:.1f} %)')
    print(f'  M3 graded (a lexicon word in the sentence): {g}  ({100*g/n:.1f} %)')
    for k in LEX:
        print(f'       {k:<11} {sum(k in s["grades"] for s in S)}')
    print(f'  M4 attributable (graded, one citation in the sentence): {a}  ({100*a/n:.1f} %)')
    json.dump(S, open(os.path.join(HERE, 'sites.json'), 'w'), indent=0, ensure_ascii=False)
    rnd = random.Random(7170)
    ung = [s for s in S if not s['grades']]
    with open(os.path.join(HERE, 'ungraded_sample.txt'), 'w', encoding='utf-8') as f:
        for s in rnd.sample(ung, min(20, len(ung))):
            f.write(f"[{s['paper']} -> {','.join(s['cites'])}] {s['text']}\n\n")
    with open(os.path.join(HERE, 'joinable.txt'), 'w', encoding='utf-8') as f:
        for s in S:
            if s['joinable']:
                f.write(f"[{s['paper']} -> {','.join(s['cites'])}] grades={s['grades']} {s['text']}\n\n")


if __name__ == '__main__':
    main()
