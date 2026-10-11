"""the DANGLING-PREDICATE test: a pinned span that begins with a finite verb, a participle or a
bare conjunction cannot name its own subject, so it passes on any sentence with that predicate."""
import json, re, collections, sys

FINITE = r"""is|are|was|were|be|been|being|has|have|had|does|do|did|can|could|may|might|must|
shall|should|will|would|needs?|carry|carries|carried|names?|named|naming|reach|reaches|reached|
remain|remains|remained|determine|determines|determined|puts?|put|moved?|moves|gives?|gave|given|
makes?|made|takes?|took|taken|states?|stated|says?|said|shows?|shown|leaves?|left|holds?|held|
starts?|started|sits?|sat|rests?|rested|lies?|lay|runs?|ran|acts?|acted|goes|went|comes?|came|
enters?|entered|returns?|returned|fixes|fixed|excluded|included|constrains?|constrained"""
LEAD = re.compile(r'^(?:' + FINITE.replace('\n','') + r'|and|or|but|so|then|than|that|which|with|without|'
                  r'for|from|into|onto|across|through|by|at|in|on|of|to|as|per|rather)\b',
                  re.I)
STRIP = re.compile(r'^[^A-Za-z]+')

def dangles(lit):
    """True when the span, read alone, carries a predicate with no subject of its own."""
    head = STRIP.sub('', lit)
    return bool(LEAD.match(head))

def rows(path='corpus/quote_pin_baseline.tsv'):
    for l in open(path, encoding='utf-8'):
        c = l.rstrip('\n').split('\t')
        if len(c) >= 7 and c[0].startswith('receipts/'):
            try: c[1] = json.loads(c[1])
            except Exception: continue
            yield c
