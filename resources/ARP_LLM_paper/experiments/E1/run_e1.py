"""E1 runner: subjects, then blind scoring.  Usage:  python3 run_e1.py pilot|main [--model M]

pilot: 8 fixed items x 4 conditions (discarded from the analysis, as registered).
main:  every item x 4 conditions.
Records go to runs_<phase>[_<model>]/ and scores_<phase>[_<model>]/; both resume.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from subject import Trial, run_batch  # noqa: E402

COND = {
    'C0': 'You are a helpful assistant.',
    'C1': ('You are a helpful assistant. Before you answer, write a receipt inside <receipt></receipt> tags: in '
           'your own words, say what the message is asking of you, each distinct thing, and what each one actually '
           'requires. Then give your answer after the closing tag.'),
    'C2': 'You are a helpful assistant. Make sure your answer addresses every request in the message.',
    'C3': 'You are a helpful assistant. For each request in the message, say what it requires. Then answer.',
}
PILOT = ['E1-01', 'E1-06', 'E1-11', 'E1-16', 'E1-21', 'E1-26', 'E1-31', 'E1-36']

SCORER = ('You are scoring how completely and correctly an answer handles a list of requests. You are given the '
          'original message, the list of requests in it, and an answer. Score each request: 2 = fully and correctly '
          'handled; 1 = touched but incomplete or wrong; 0 = not addressed. Where a request carries a KEY, a 2 '
          'requires the key\'s content. Judge only the answer given. Also answer: does the answer look like the '
          'assistant was given any special instructions beyond answering helpfully (true/false)? Reply with JSON only: '
          '{"scores": {"<k>": 0|1|2, ...}, "special_instructions_guess": true|false}')
RECEIPT_CODER = ('You are coding a response. Question: before it starts answering, does the response restate, in its '
                 'own words, what the message is asking for (listing or paraphrasing the requests)? Reply with JSON '
                 'only: {"restates_asks_first": true|false}')


def strip_receipt(t):
    return re.sub(r'<receipt>.*?</receipt>', '', t or '', flags=re.S).replace('<receipt>', '').replace('</receipt>', '').strip()


def strip_c3_analysis(t):
    return t  # C3 has no delimiter; its analysis is part of the answer and is scored as such (stated in RESULT)


def main():
    phase = sys.argv[1]
    model = sys.argv[sys.argv.index('--model') + 1] if '--model' in sys.argv else 'claude-opus-5-5'
    tag = phase + ('' if model == 'claude-opus-5-5' else '_' + model.split('-')[1])
    items = json.load(open(os.path.join(HERE, 'materials', 'items.json')))
    if phase == 'pilot':
        items = [i for i in items if i['id'] in PILOT]
    runs = os.path.join(HERE, 'runs_' + tag)
    trials = [Trial('E1', c, it['id'], COND[c], it['message'], os.path.join(runs, c, it['id'] + '.json'))
              for it in items for c in COND]
    run_batch(trials, workers=4, model=model)

    sc, rc = [], []
    for it in items:
        asks = '\n'.join(f"{a['k']}. {a['text']}" + (f"  KEY: {it['hard_key']}" if a['hard'] else '')
                         for a in it['asks'])
        for c in COND:
            r = json.load(open(os.path.join(runs, c, it['id'] + '.json')))
            if r.get('failed'):
                continue
            ans = strip_receipt(r['response'])
            msg = f"MESSAGE:\n{it['message']}\n\nREQUESTS:\n{asks}\n\nANSWER:\n{ans}"
            # scorer records are keyed by an opaque name so the condition is not in the scorer's input
            sc.append(Trial('E1', c, it['id'], SCORER, msg,
                            os.path.join(HERE, 'scores_' + tag, c, it['id'] + '.json'), role='scorer'))
            rc.append(Trial('E1', c, it['id'], RECEIPT_CODER, f"MESSAGE:\n{it['message']}\n\nRESPONSE:\n{r['response']}",
                            os.path.join(HERE, 'receiptcode_' + tag, c, it['id'] + '.json'), role='scorer'))
    run_batch(sc + rc, workers=4, model='claude-opus-5-5')


if __name__ == '__main__':
    main()
