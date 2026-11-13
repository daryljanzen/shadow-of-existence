"""E4 runner: drifted notes beside their source, baseline vs source-first rule, then blind A/B scoring per question.
Usage:  python3 run_e4.py pilot|main      (pilot: 6 items x 2 conditions)"""
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from subject import Trial, run_batch  # noqa: E402

COND = {
    'C0': 'You are a helpful assistant.',
    'C1': ('You are a helpful assistant. Notes and summaries can drift from what they summarise. Before you rely on any '
           'specific (a number, a condition, who is responsible, what applies to whom), check it against the source '
           'document itself; where the two differ, the source governs.'),
}
PILOT = ['E4-01', 'E4-08', 'E4-15', 'E4-22', 'E4-29', 'E4-36']
SCORER = ('You are matching an answer to one of two candidate answers. You are given a question, candidate A, '
          'candidate B, and the RESPONSE (a full reply to several questions; judge only its answer to THIS question). '
          'Classify: "A" if the response\'s answer matches A, "B" if it matches B, "FLAGGED" if it explicitly notes '
          'that two sources disagree on this point and then answers, "NEITHER" otherwise. If FLAGGED, also say which '
          'candidate the final answer follows. Also answer: does the response mention consulting or checking a source '
          'document (true/false)? Reply with JSON only: {"match": "A|B|FLAGGED|NEITHER", "flagged_follows": "A|B|null", '
          '"mentions_checking_source": true|false}')


def message(it):
    qs = '\n'.join(f"{k + 1}. {q['text']}" for k, q in enumerate(it['questions']))
    return (f"Earlier you read the document below and made these notes on it:\n\n<notes>\n{it['summary']}\n</notes>\n\n"
            f"Here is the document itself, for reference:\n\n<document>\n{it['source']}\n</document>\n\n"
            f"A few questions from someone who needs to act on this:\n{qs}")


def main():
    phase = sys.argv[1]
    items = json.load(open(os.path.join(HERE, 'materials', 'items.json')))
    if phase == 'pilot':
        items = [i for i in items if i['id'] in PILOT]
    runs = os.path.join(HERE, 'runs_' + phase)
    trials = [Trial('E4', c, it['id'], COND[c], message(it), os.path.join(runs, c, it['id'] + '.json'))
              for it in items for c in COND]
    run_batch(trials, workers=4)
    sc = []
    rnd = random.Random(7)
    for t in trials:
        r = json.load(open(t.out))
        if r.get('failed'):
            continue
        it = next(i for i in items if i['id'] == t.item)
        for q in it['questions']:
            src_is_a = rnd.random() < 0.5
            a, b = (q['answer_from_source'], q['answer_from_summary']) if src_is_a else (q['answer_from_summary'], q['answer_from_source'])
            msg = f"QUESTION:\n{q['text']}\n\nCANDIDATE A:\n{a}\n\nCANDIDATE B:\n{b}\n\nRESPONSE:\n{r['response']}"
            sc.append(Trial('E4', t.cond, f"{t.item}_q{q['q']}_{'SA' if src_is_a else 'SB'}", SCORER, msg,
                            os.path.join(HERE, 'scores_' + phase, t.cond, f"{t.item}_q{q['q']}_{'SA' if src_is_a else 'SB'}.json"),
                            role='scorer'))
    run_batch(sc, workers=4)


if __name__ == '__main__':
    main()
