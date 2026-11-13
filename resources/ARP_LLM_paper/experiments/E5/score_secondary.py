"""E5 registered secondaries (b) and (c), built at r7755 as blind scorer passes.  Usage: python3 score_secondary.py main"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from subject import Trial, run_batch  # noqa: E402
from run_e5 import split  # noqa: E402
HANDLING = ('You are judging a document against a key of complications in the facts it was written from. For each '
            'complication, decide whether the document HANDLES it (meets the stated good handling in substance) or '
            'MISHANDLES it (omits it, gets it wrong, or handles it materially worse than the stated good handling). Reply '
            'with JSON only: {"complications": {"1": "HANDLES|MISHANDLES", ...}}')
FOUND = ('You are given a key of complications in a decision document, and a list of FINDINGS a reviewer raised about '
         'the document. For each complication, decide whether any finding identifies that specific complication (in '
         'substance, not wording). Reply with JSON only: {"found": {"1": true|false, ...}}')
RAISED = ('You are given a list of CRITIQUES someone expected a reviewer to raise about a document, and the FINDINGS '
          'actual reviewers raised. For each expected critique, decide whether any finding raises it in substance. '
          'Reply with JSON only: {"raised": {"1": true|false, ...}}')
tag = sys.argv[1]; R = os.path.join(HERE, 'runs_' + tag)
briefs = {b['id']: b for b in json.load(open(os.path.join(HERE, 'materials', 'briefs.json')))}
def findings(lvl, b, r):
    m = re.search(r'\{.*\}', json.load(open(os.path.join(HERE, f'extract_{tag}', lvl, f'{b}__r{r}.json')))['response'], re.S)
    fs = json.loads(m.group(0))['findings'] if m else []
    return [f for f in fs if not re.search(r"author (expects|anticipat)", f, re.I)]
def key(b):
    return '\n'.join(f"{c['c']}. {c['what']}" for c in briefs[b]['complications'])
T = []
for b in briefs:
    doc, ant = split(json.load(open(os.path.join(R, 'author', b + '.json')))['response'])
    good = '\n'.join(f"{c['c']}. {c['what']} GOOD HANDLING: {c['good_handling']}" for c in briefs[b]['complications'])
    T.append(Trial('E5', 'doc', b, HANDLING, f"FACTS:\n{briefs[b]['fact_pack']}\n\nKEY:\n{good}\n\nDOCUMENT:\n{doc}",
                   os.path.join(HERE, f'handling_{tag}', b + '.json'), role='scorer'))
    ants = [a.strip(' -*0123456789.)\t') for a in ant.splitlines() if a.strip(' -*#\t') and len(a.strip()) > 12]
    alist = '\n'.join(f"{i + 1}. {a}" for i, a in enumerate(ants))
    for lvl in ('R0', 'R1', 'R2'):
        fl = [f for r in (0, 1) for f in findings(lvl, b, r)]
        T.append(Trial('E5', lvl, b, RAISED, f"CRITIQUES:\n{alist}\n\nFINDINGS:\n" + '\n'.join(f'- {f}' for f in fl),
                       os.path.join(HERE, f'raised_{tag}', 'x' + str('R0R1R2'.index(lvl) // 2), b + '.json'), role='scorer'))
        for r in (0, 1):
            T.append(Trial('E5', lvl, b, FOUND, f"KEY:\n{key(b)}\n\nFINDINGS:\n" + '\n'.join(f'- {f}' for f in findings(lvl, b, r)),
                           os.path.join(HERE, f'found_{tag}', 'x' + str('R0R1R2'.index(lvl) // 2), f'{b}__r{r}.json'), role='scorer'))
run_batch(T, workers=4)
