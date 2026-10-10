import json, re
row = open('/tmp/claude-0/po78.txt', encoding='utf-8').read()
segs = row.split('&#9670;')
flat = [re.sub(r'\s+', ' ', s).strip() for s in segs]
ONES = ['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH','EIGHTH','NINTH','TENTH',
        'ELEVENTH','TWELFTH','THIRTEENTH','FOURTEENTH','FIFTEENTH','SIXTEENTH','SEVENTEENTH',
        'EIGHTEENTH','NINETEENTH']
W = {w: i + 1 for i, w in enumerate(ONES)}
W.update({'TWENTIETH': 20, 'THIRTIETH': 30, 'FORTIETH': 40})
for t, b in (('TWENTY', 20), ('THIRTY', 30), ('FORTY', 40)):
    for i, w in enumerate(ONES):
        W[f'{t}-{w}'] = b + i + 1
ORD = '|'.join(sorted(W, key=len, reverse=True))
PAT = re.compile(rf'\b(?:A|AN|THE)\s+({ORD})\b|\b({ORD})\s+(?:MEMBER|CLASS|STATE|INSTANCE|'
                 rf'OPERATOR|BLINDNESS)', re.I)
first = {}
for i, s in enumerate(flat):
    for m in PAT.finditer(s):
        n = W[(m.group(1) or m.group(2)).upper()]
        if 1 <= n <= 45 and n not in first:
            first[n] = (i, m.start())
# member 40 is the ancestry blindness, filed by the r7229 recount rather than by an ordinal
m40 = re.search(r'ancestry blindness is', ' '.join(flat), re.I)
with open('/tmp/claude-0/dossier.txt', 'w', encoding='utf-8') as f:
    for n in range(1, 46):
        if n in first:
            i, p = first[n]
            f.write(f'\n\n##### MEMBER {n}  [seg {i}]\n' + flat[i][max(0, p - 80):p + 900])
        else:
            f.write(f'\n\n##### MEMBER {n}  [NO ORDINAL FILING — set by the r7229 recount]\n')
print('wrote dossier; anchored', len(first), 'of 45')
