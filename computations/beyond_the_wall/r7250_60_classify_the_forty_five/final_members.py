import json, re
row = re.sub(r'\s+', ' ', open('/tmp/claude-0/po78.txt', encoding='utf-8').read())
ONES = ['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH','EIGHTH','NINTH','TENTH',
        'ELEVENTH','TWELFTH','THIRTEENTH','FOURTEENTH','FIFTEENTH','SIXTEENTH','SEVENTEENTH',
        'EIGHTEENTH','NINETEENTH']
W = {w: i + 1 for i, w in enumerate(ONES)}
W.update({'TWENTIETH': 20, 'THIRTIETH': 30, 'FORTIETH': 40})
for t, b in (('TWENTY', 20), ('THIRTY', 30), ('FORTY', 40)):
    for i, w in enumerate(ONES):
        W[f'{t}-{w}'] = b + i + 1
ORD = '|'.join(sorted(W, key=len, reverse=True))
PAT = re.compile(rf'\b(?:A|AN|THE)\s+({ORD})(?:\s+BLINDNESS)?\s+MEMBER\b'
                 rf'|\b({ORD})\s+MEMBERS?\b'
                 rf'|\b(?:A|AN|THE)\s+({ORD})\s+INSTANCE OF THE BLINDNESS'
                 rf'|\b(?:A|AN|THE)\s+({ORD})\s*(?:,|\bAT\b|\bIS\b|\.)', re.I)
NEG = re.compile(r'NOT A |NOT ITSELF|IS WITHDRAWN|NEAR-MISS|FOLDED INTO|RECURRENCE AND NOT'
                 r'|RECURRING AND NOT|rather than added as', re.I)
filed = {}
for m in PAT.finditer(row):
    w = next(g for g in m.groups() if g).upper()
    n = W[w]
    if not 1 <= n <= 45 or n in filed:
        continue
    if NEG.search(row[max(0, m.start() - 110):m.start() + 30]):
        continue
    filed[n] = row[m.start():m.start() + 300]

# the row enumerates its own first four, and the fifth/sixth by shape rather than by ordinal
HAND = {
 1: 'ROW’S OWN ENUMERATION (seg 82): "a receipt reading a paper the gate then edits"',
 2: 'ROW’S OWN ENUMERATION (seg 82): "a scope keyed on an adjudicated baseline"',
 4: 'ROW’S OWN ENUMERATION (seg 82): "a selector keyed on a filename"',
 6: 'FILED WITHOUT AN ORDINAL (seg 81): "THE SHARPEST MEMBER OF THE BLINDNESS FAMILY YET" '
    '--- the citation sweep cannot detect its own findings being fixed; the row contrasts it '
    'with "the four earlier members are instruments blind to a DEFECT ... This one is blind '
    'to the REPAIR"',
 40: 'NO ORDINAL FILING: the count reached forty by the r7229 arithmetic recount --- '
     '"the ancestry blindness is $40$. THIRTY-SIX plus four is FORTY"',
}
rows = []
for n in range(1, 46):
    src = 'ordinal filing in the row' if n in filed else 'hand-resolved from the row'
    txt = filed.get(n, HAND.get(n, 'UNRESOLVED'))
    rows.append((n, src, re.sub(r'\t', ' ', txt)))
miss = [n for n, s, t in rows if t == 'UNRESOLVED']
print('resolved:', 45 - len(miss), 'unresolved:', miss)
with open('computations/beyond_the_wall/r7250_60_classify_the_forty_five/MEMBERS.tsv',
          'w', encoding='utf-8') as f:
    f.write('# the forty-five blindness-family members, each anchored to the register row\n')
    f.write('# n\tsource\tthe row\'s own filing text (truncated)\n')
    for n, s, t in rows:
        f.write(f'{n}\t{s}\t{t[:300]}\n')
