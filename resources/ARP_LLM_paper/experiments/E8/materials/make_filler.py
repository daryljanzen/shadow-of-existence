"""E8 filler for PLAIN (r7758, on 60's read): eight documents, each matched in length to the curriculum document at the
same turn, carrying no disposition and no method -- descriptive natural and local history, with no argument about
evidence, reasoning, reviewing, collaboration or decisions.  Written once by a fresh subject context, committed before
any E8 trial; records in filler_raw/.  Usage: python3 make_filler.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(EXP, 'harness'))
from subject import Trial, run_batch  # noqa: E402
SYS = 'You are a writer of plain, descriptive encyclopaedia-style prose.'
RULE = ('Write descriptive prose only: what things are, where, when, how they work physically, how they changed over time. '
        'Do NOT discuss evidence, research methods, how to reason, how to judge claims, reviewing, teamwork, collaboration, '
        'decision-making, advice, or controversies and debates. No lists, no headings beyond a title, no questions to the reader. '
        'Invent a fictional place where needed; do not cite studies or numbers from studies.')
# (turn, topic, target words, parts): the first matches the 8,840-word paper, written in four sequential parts
PLAN = [(1, 'the natural and settlement history of a fictional river valley, the Aldern, from its geology to its villages, mills and bridges', 8840, 4),
        (2, 'the seasons of a fictional coastal salt marsh and the birds that use it', 1278, 1),
        (3, 'how a fictional stone lighthouse on a northern headland was built and kept', 1299, 1),
        (4, 'the life of a fictional working orchard through one year', 1289, 1),
        (5, 'the trades of a fictional nineteenth-century market town street, shop by shop', 1323, 1),
        (6, 'a fictional mountain pass road and the inns along it', 1327, 1),
        (7, 'the weather of a fictional upland moor across a year', 1291, 1),
        (8, 'the history of a fictional canal, its locks and boats', 1528, 1)]
T = []
for turn, topic, words, parts in PLAN:
    per = words // parts
    for k in range(parts):
        part = (f' This is part {k + 1} of {parts} of one continuous article; write only this part, continuing the account in order'
                f' (part 1 begins at the valley\'s geology; part {parts} ends with the present day).') if parts > 1 else ''
        T.append(Trial('E8', 'filler', f'doc{turn}_p{k + 1}', SYS,
                       f'Write about {per} words on {topic}.{part} {RULE}', os.path.join(HERE, 'filler_raw', f'doc{turn}_p{k + 1}.json'), role='materials'))
run_batch(T, workers=4)
docs = []
for turn, topic, words, parts in PLAN:
    text = '\n\n'.join(json.load(open(os.path.join(HERE, 'filler_raw', f'doc{turn}_p{k + 1}.json')))['response'].strip() for k in range(parts))
    docs.append(dict(turn=turn, target_words=words, words=len(text.split()), text=text))
json.dump(docs, open(os.path.join(HERE, 'filler.json'), 'w'), indent=1, ensure_ascii=False)
print([(d['turn'], d['target_words'], d['words']) for d in docs])
