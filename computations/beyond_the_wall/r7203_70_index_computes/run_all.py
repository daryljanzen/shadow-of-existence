"""Run every receipt an INDEX row names, once, from its own directory; stdout to OUT/<stem>.txt with an rc= trailer."""
import concurrent.futures as cf, os, re, subprocess, sys
ROOT = os.path.abspath(sys.argv[1]); OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
paths = set()
for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8'):
    if ln.startswith('| '):
        c = ln.split('|')
        if len(c) > 5:
            m = re.search(r'`([^`]+\.py)`', c[4])
            if m and os.path.exists(os.path.join(ROOT, 'receipts', m.group(1))): paths.add(m.group(1))
def run(rel):
    p = os.path.join(ROOT, 'receipts', rel); o = os.path.join(OUT, os.path.basename(rel)[:-3] + '.txt')
    if os.path.exists(o): return
    try:
        r = subprocess.run([sys.executable, os.path.basename(p)], cwd=os.path.dirname(p), capture_output=True, text=True, timeout=300)
        out, rc = r.stdout, r.returncode
    except subprocess.TimeoutExpired as e:
        out, rc = (e.stdout or b'').decode(errors='replace') if isinstance(e.stdout, bytes) else (e.stdout or ''), 'TIMEOUT'
    open(o, 'w').write(out + f'\nrc={rc}\n')
print(len(paths), 'receipts', flush=True)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(run, sorted(paths)))
print('done')
