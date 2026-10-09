"""r7227+70.1 -- each subject the HEAD widening newly catches, classified by WHOSE number its head id is.

Buckets (post-band, id >= 3563; earlier ids are PRE-BAND and outside the band's question):
  OWN-CLAIM     the authoring seat holds the id's half: the seat's own number, correctly caught.
  REFERENCE     the id is the ORDER the commit answers -- a seat with a half writing the other half's id
                followed by an answering word, or any head id from a seat holding no half (cc66, 70, 69),
                which by declaration never numbers its own work bare.
  CROSS-CLAIM   a seat with a half writing the other half's id as its own work (no answering word).
  UNATTRIBUTED  no session maps to a seat, so whose number it is cannot be said; counted, not guessed.
"""
import json, re, sys, collections
r = json.load(open(sys.argv[1]))
ANSWER = re.compile(r"^r\d+(?:'s\b|\s+(?:reply|acknowledged|read|answered|routing|item|CI|CLOSED|accepted|"
                    r"Q\d|[⓵⓶⓷⓸⓹]|\(70\)|cc66\.\d))", re.I)
NOHALF = {'cc66', '70', '69'}
rows, c = [], collections.Counter()
for x in r['newly']:
    rid = int(re.match(r'^r(\d+)', x['subj']).group(1))
    seat, half = x['seat'], x['half']
    if rid < 3563:
        b = 'PRE-BAND'
    elif ANSWER.match(x['subj']):
        b = 'REFERENCE'          # an answering word decides first: a session's majority parity is
                                 # circular for a seat that only ever writes the orders it answers
    elif seat == 'unattributed':
        b = 'UNATTRIBUTED'
    elif seat in NOHALF or half is None:
        b = 'REFERENCE'
    elif rid % 2 == half:
        b = 'OWN-CLAIM'
    else:
        b = 'CROSS-CLAIM'
    c[b] += 1
    rows.append((b, seat, x['sha'], x['subj']))
with open(sys.argv[2], 'w') as f:
    f.write('bucket\tseat\tsha\tsubject\n')
    for row in sorted(rows):
        f.write('\t'.join(row) + '\n')
print(dict(c), 'total', sum(c.values()))
for row in sorted(rows):
    if row[0] in ('CROSS-CLAIM',):
        print('  ', row[0], row[1], row[2], row[3][:90])
ref_with_half = [row for row in rows if row[0] == 'REFERENCE' and row[1] not in NOHALF]
print('REFERENCE from seats WITH a half:', len(ref_with_half))
for row in ref_with_half: print('  ', row[1], row[2], row[3][:80])
