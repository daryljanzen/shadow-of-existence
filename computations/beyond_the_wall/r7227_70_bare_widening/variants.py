"""r7227+70.1 -- narrower variants of the widening, each scored on the classified newly-caught set."""
import re, csv, sys, collections
rows = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
V = {
 'HEAD (any text after the id)': r'^r\d{3,5}(?![\w+.])',
 'COLON (rNNNN:)': r'^r\d{3,5}:',
 'COLON or a claim word': r'^r\d{3,5}(?::|\s+(?:orders|pre-registration|PRE-REGISTRATION|addendum|amendment|amended|fixup|fix|repair|repaired|part|merged|\(follow-up\)|\(matrix\)|in progress|claim)\b)',
}
for name, pat in V.items():
    p = re.compile(pat); c = collections.Counter(r['bucket'] for r in rows if p.match(r['subject']))
    n = sum(c.values()); post = n - c['PRE-BAND']
    print(f'{name:32s} caught {n:3d}  REFERENCE {c["REFERENCE"]:3d} ({100*c["REFERENCE"]/max(post,1):4.1f}% of post-band)'
          f'  CROSS-CLAIM {c["CROSS-CLAIM"]}  OWN {c["OWN-CLAIM"]}  UNATTR {c["UNATTRIBUTED"]}')
    if name.startswith('COLON or'):
        for r in rows:
            if p.match(r['subject']) and r['bucket'] == 'REFERENCE': print('      ref:', r['seat'], r['sha'], r['subject'][:80])
