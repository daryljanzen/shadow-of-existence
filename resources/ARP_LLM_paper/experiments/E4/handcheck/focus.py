import re, sys
def blocks(r):
    parts = re.split(r'\n(?=\*\*\d|\d\.\s|#+\s|\*\*[A-Z])', r)
    return parts
for p in sys.argv[1:]:
    t = open(f'packets/{p}.txt').read()
    q = t.split('QUESTION:\n')[1].split('\n\nCANDIDATE A')[0]; a = t.split('CANDIDATE A:\n')[1].split('\n\nCANDIDATE B')[0]
    b = t.split('CANDIDATE B:\n')[1].split('\n\nRESPONSE')[0]; r = t.split('RESPONSE:\n', 1)[1]
    qw = set(w for w in re.findall(r'[a-z0-9]{4,}', (q + ' ' + a + ' ' + b).lower()))
    best = max(blocks(r), key=lambda x: len(qw & set(re.findall(r'[a-z0-9]{4,}', x.lower()))))
    notes = [l for l in r.split('\n') if re.search(r'notes?|summary|earlier', l, re.I) and l not in best][:3]
    print(f'######## {p}\nQ: {q}\nA: {a}\nB: {b}\nBLOCK: {best.strip()[:900]}\nNOTES-LINES: ' + ' || '.join(n.strip()[:220] for n in notes) + '\n')
