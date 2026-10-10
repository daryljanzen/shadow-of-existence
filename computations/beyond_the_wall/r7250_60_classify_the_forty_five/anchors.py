import json, re
row = open('/tmp/claude-0/po78.txt', encoding='utf-8').read()
ONES = ['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH','EIGHTH','NINTH','TENTH',
        'ELEVENTH','TWELFTH','THIRTEENTH','FOURTEENTH','FIFTEENTH','SIXTEENTH','SEVENTEENTH',
        'EIGHTEENTH','NINETEENTH']
W = {w: i + 1 for i, w in enumerate(ONES)}
W.update({'TWENTIETH': 20, 'THIRTIETH': 30, 'FORTIETH': 40})
for t, b in (('TWENTY', 20), ('THIRTY', 30), ('FORTY', 40)):
    for i, w in enumerate(ONES):
        W[f'{t}-{w}'] = b + i + 1
ORD = '|'.join(sorted(W, key=len, reverse=True))
# a filing: an ordinal introduced by A/AN/THE, or followed by a family noun
PAT = re.compile(rf'\b(?:A|AN|THE)\s+({ORD})\b|\b({ORD})\s+(?:MEMBER|CLASS|STATE|INSTANCE|'
                 rf'OPERATOR|BLINDNESS)', re.I)
segs = row.split('&#9670;')
hit = {}
for i, s in enumerate(segs):
    flat = re.sub(r'\s+', ' ', s).strip()
    for m in PAT.finditer(flat):
        n = W[(m.group(1) or m.group(2)).upper()]
        if 1 <= n <= 45:
            hit.setdefault(n, []).append((i, m.start()))
miss = [n for n in range(1, 46) if n not in hit]
print('covered:', len(hit), 'missing:', miss)
out = {}
for n, lst in sorted(hit.items()):
    i, p = lst[0]
    flat = re.sub(r'\s+', ' ', segs[i]).strip()
    out[n] = {'seg': i, 'n_hits': len(lst), 'text': flat[max(0, p - 60):p + 700]}
json.dump(out, open('/tmp/claude-0/anchors.json', 'w'), indent=1)
print('wrote', len(out), 'anchors')
