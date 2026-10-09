"""r7227+70.1 -- what the widened BARE catches over every ref, and how much of it is innocent."""
import json, re, subprocess, collections, sys
OLD = re.compile(r'^(r\d{3,5})\s*[—-]\s*(.*)$')
HEAD = re.compile(r'^(r\d{3,5})(?![\w+.])\s*(?:[—-]\s*)?(.*)$')
ANY = re.compile(r'(?<![\w+.])(r\d{3,5})(?![\w+.])')
SUFFIX = re.compile(r'^r\d{3,5}\+(cc\d+|\d+)\.')
out = subprocess.run(['git', 'log', '--all', '--format=%H%x1f%s%x1f%(trailers:key=Claude-Session,valueonly,separator=%x20)%x1e'],
                     capture_output=True, text=True).stdout
rows = []
for rec in out.split('\x1e'):
    rec = rec.strip('\n')
    if not rec: continue
    h, s, sess = rec.split('\x1f')
    rows.append((h, s.strip(), sess.strip()))
# seat per session from suffixed subjects
sess_seat = collections.defaultdict(collections.Counter)
sess_par = collections.defaultdict(collections.Counter)
for h, s, sess in rows:
    if not sess: continue
    m = SUFFIX.match(s)
    if m: sess_seat[sess][m.group(1)] += 1
    m = HEAD.match(s)
    if m: sess_par[sess][int(m.group(1)[1:]) % 2] += 1
HALF = {'54': 0, '60': 0, 'cc54': 0, '57': 1, '59': 1, '61': 1, '64': 1, '66': 1, 'cc66': None, '70': None, '69': None}
def seat_of(sess):
    if sess in sess_seat:
        return sess_seat[sess].most_common(1)[0][0]
    return None
res = {'population': len(rows), 'old': 0, 'head': 0, 'any': 0, 'newly': [], 'any_only': []}
for h, s, sess in rows:
    o, hd, an = OLD.match(s), HEAD.match(s), ANY.search(s)
    res['old'] += bool(o); res['head'] += bool(hd); res['any'] += bool(an)
    if hd and not o:
        seat = seat_of(sess)
        if seat is not None:
            half = HALF.get(seat, 'undeclared')
        elif sess in sess_par:
            half = sess_par[sess].most_common(1)[0][0]; seat = f'bare-session(parity {half})'
        else:
            half = 'unattributed'; seat = 'unattributed'
        rid = int(hd.group(1)[1:])
        cross = (half is None) or (half in (0, 1) and rid % 2 != half)
        res['newly'].append(dict(sha=h[:8], subj=s[:110], seat=seat, half=half, cross=cross,
                                 shape=' '.join(s.split()[:2])))
    if an and not hd:
        res['any_only'].append(dict(sha=h[:8], subj=s[:140]))
json.dump(res, open(sys.argv[1], 'w'), indent=1, ensure_ascii=False)
print('population', res['population'], 'old', res['old'], 'head', res['head'], 'any', res['any'])
print('newly caught by HEAD', len(res['newly']), ' ANY-only (not HEAD)', len(res['any_only']))
shapes = collections.Counter(re.sub(r'r\d+', 'rN', x['shape']) for x in res['newly'])
print('shapes', shapes.most_common(15))
print('cross-seat', [ (x['sha'], x['seat'], x['subj'][:70]) for x in res['newly'] if x['cross']])
