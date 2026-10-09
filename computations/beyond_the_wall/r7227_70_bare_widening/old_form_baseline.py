"""r7227+70.1 -- the same classification applied to what the OLD BARE already catches, as the control.

If the dash form is mostly claims and the dash-less form is a third citations, then the dash is
doing semantic work by habit -- and widening across it imports the citations."""
import re, subprocess, collections, sys
sys.argv += ['/dev/null']
OLD = re.compile(r'^(r\d{3,5})\s*[—-]\s*(.*)$')
ANSWER = re.compile(r"^r\d+(?:'s\b|\s*[—-]?\s*(?:reply|acknowledged|read|answered|routing|item|CI|CLOSED|accepted|"
                    r"Q\d|[⓵⓶⓷⓸⓹]|\(70\)|cc66\.\d))", re.I)
SUFFIX = re.compile(r'^r\d{3,5}\+(cc\d+|\d+)\.')
out = subprocess.run(['git', 'log', '--all', '--format=%H%x1f%s%x1f%(trailers:key=Claude-Session,valueonly,separator=%x20)%x1e'],
                     capture_output=True, text=True).stdout
rows = [r.strip('\n').split('\x1f') for r in out.split('\x1e') if r.strip('\n')]
seat = collections.defaultdict(collections.Counter)
for h, s, sess in rows:
    m = SUFFIX.match(s.strip())
    if m and sess.strip(): seat[sess.strip()][m.group(1)] += 1
NOHALF = {'cc66', '70', '69'}
c = collections.Counter(); refs = []
for h, s, sess in rows:
    s = s.strip(); m = OLD.match(s)
    if not m or int(m.group(1)[1:]) < 3563: continue
    st = seat[sess.strip()].most_common(1)[0][0] if sess.strip() in seat else None
    if ANSWER.match(s) or st in NOHALF:
        c['REFERENCE'] += 1; refs.append((st, h[:8], s[:90]))
    else:
        c['NOT-A-REFERENCE'] += 1
print('old BARE, post-band:', dict(c), 'reference share %.1f%%' % (100 * c['REFERENCE'] / sum(c.values())))
for r in refs: print('  ', *r)
