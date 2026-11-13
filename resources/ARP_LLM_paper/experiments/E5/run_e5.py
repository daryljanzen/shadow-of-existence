"""E5 runner: author writes + anticipates critiques; reviewers at three contamination levels; blind extraction and
matching.  Usage:  python3 run_e5.py pilot|main      (pilot: 5 briefs, 1 replicate per level)"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from subject import Trial, run_batch  # noqa: E402

SYS = 'You are a helpful assistant.'
PILOT = ['E5-01', 'E5-07', 'E5-13', 'E5-19', 'E5-25']
HEAD = 'Expected critiques'
EXTRACT = ('List the distinct substantive findings (criticisms or weaknesses) this review raises about the document, one '
           'per line, each in one sentence. Do not include praise or minor stylistic notes. Reply with JSON only: '
           '{"findings": ["...", "..."]}')
MATCH = ('You are judging review findings about a document. You are given the document, the facts it was written from, '
         'a key of known complications, a list of critiques the author anticipated, and a list of FINDINGS from a '
         'reviewer. For each finding decide: valid (it identifies a real weakness of the document given the facts) and '
         'anticipated (it substantially matches one of the author\'s anticipated critiques, in substance not wording). '
         'Reply with JSON only: {"judgements": [{"finding": "...", "valid": true|false, "anticipated": true|false}]}')


def split(t):
    i = t.lower().rfind(HEAD.lower())
    return (t[:i].strip(), t[i + len(HEAD):].strip()) if i >= 0 else (t.strip(), '')


def main():
    phase = sys.argv[1]
    briefs = json.load(open(os.path.join(HERE, 'materials', 'briefs.json')))
    if phase == 'pilot':
        briefs = [b for b in briefs if b['id'] in PILOT]
    reps = 1 if phase == 'pilot' else 2
    R = os.path.join(HERE, 'runs_' + phase)
    authors = [Trial('E5', 'author', b['id'], SYS,
                     f"{b['task']}\n\n{b['fact_pack']}\n\nWrite the document. Then, under the heading \"{HEAD}\", list the "
                     f"specific criticisms you expect a careful, independent reviewer to make of it.",
                     os.path.join(R, 'author', b['id'] + '.json')) for b in briefs]
    run_batch(authors, workers=4)
    rev = []
    for b, a in zip(briefs, authors):
        doc, ant = split(json.load(open(a.out))['response'])
        base = f"Please review the following document.\n\n<document>\n{doc}\n</document>"
        ctx = f"\n\nIt was written from this brief:\n\n<brief>\n{b['task']}\n\n{b['fact_pack']}\n</brief>"
        antic = f"\n\nIts author expects a reviewer to raise:\n\n<expected>\n{ant}\n</expected>"
        for lvl, msg in (('R0', base), ('R1', base + ctx), ('R2', base + ctx + antic)):
            for k in range(reps):
                rev.append(Trial('E5', lvl, b['id'], SYS, msg, os.path.join(R, lvl, f"{b['id']}__r{k}.json"), rep=k))
    run_batch(rev, workers=4)
    ex = [Trial('E5', t.cond, t.item, EXTRACT, f"REVIEW:\n{json.load(open(t.out))['response']}",
                os.path.join(HERE, 'extract_' + phase, t.cond, f"{t.item}__r{t.rep}.json"), role='scorer', rep=t.rep)
          for t in rev]
    run_batch(ex, workers=4)
    mt = []
    for t, e in zip(rev, ex):
        b = next(x for x in briefs if x['id'] == t.item)
        doc, ant = split(json.load(open(os.path.join(R, 'author', b['id'] + '.json')))['response'])
        m = re.search(r'\{.*\}', json.load(open(e.out))['response'], re.S)
        finds = json.loads(m.group(0))['findings'] if m else []
        finds = [f for f in finds if not re.search(r"author (expects|anticipat)", f, re.I)]
        key = '\n'.join(f"- {c['what']}" for c in b['complications'])
        msg = (f"DOCUMENT:\n{doc}\n\nFACTS:\n{b['fact_pack']}\n\nKNOWN COMPLICATIONS:\n{key}\n\nAUTHOR'S ANTICIPATED CRITIQUES:\n"
               f"{ant}\n\nFINDINGS:\n" + '\n'.join(f"- {f}" for f in finds))
        mt.append(Trial('E5', t.cond, t.item, MATCH, msg, os.path.join(HERE, 'match_' + phase, t.cond, f"{t.item}__r{t.rep}.json"),
                        role='scorer', rep=t.rep))
    run_batch(mt, workers=4)


if __name__ == '__main__':
    main()
