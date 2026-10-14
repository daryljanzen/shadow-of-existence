#!/usr/bin/env python3
"""floor2.py -- THE_RULE's floor 2, measured on the LIVE quote-pin keys of the given receipts.

*A span meets floor 2 when it stands exactly once in the file it is checked against, compared the way
the checker compares.  So the comparison is made with `check_quote_pins`' own `_unmark` and never with a
reimplementation of it -- the whole point of `69`'s wording is that "unique under normalisation" is ONE
checkable thing.*
  ⌗ `_unmark` is many-to-one, so the normalised count can only RISE: a raw `str.count` is a LOWER BOUND
    on the rule's count, and this file reports both so the gap is visible rather than assumed away.
"""
import io, json, re, subprocess, sys, os, glob, importlib.util
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
_spec = importlib.util.spec_from_file_location('cqp', os.path.join(R, 'corpus', 'check_quote_pins.py'))
_m = importlib.util.module_from_spec(_spec); sys.modules['cqp'] = _m
try: _spec.loader.exec_module(_m)
except SystemExit: pass
_unmark = _m._unmark

LINE = re.compile(r'\s*\[QUOTE-PIN\]\[(PAPER|SOURCE|UNDECIDED)\]\[(SENTENCE|TOKEN)\]\[([A-Z,]*)\]\s+'
                  r'(\S+?):(\d+):(\d+)\s+(".*")$')


def body(f):
    b = '\n'.join(l for l in io.open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main(files):
    texts = {os.path.basename(f): re.sub(r'\s+', ' ', body(f))
             for f in glob.glob(os.path.join(R, 'corpus', '*.tex'))
             if not os.path.basename(f).startswith('appendix_receipts_')}
    un = {k: _unmark(v) for k, v in texts.items()}
    r = subprocess.run([sys.executable, 'scripts/mutate_assertions.py', '--quote', '--files', *files],
                       cwd=R, capture_output=True, text=True, env=dict(os.environ, NODE='ci'))
    rows = []
    for ln in r.stdout.splitlines():
        m = LINE.match(ln)
        if m:
            rows.append((m.group(4), json.loads(m.group(7)), m.group(2)))
    print(f'  floor 2 on {len(rows)} live key(s) across {len(files)} receipt(s)\n')
    fails = []
    for rc, lit, tier in rows:
        # the container is the paper that holds it; a span absent from every paper is not a paper pin
        hits = {k: (texts[k].count(lit), un[k].count(_unmark(lit))) for k in texts if lit in texts[k]}
        if not hits:
            continue
        for k, (raw, norm) in sorted(hits.items()):
            mark = '' if norm == 1 else '   <== FAILS floor 2'
            if norm != 1:
                fails.append((rc, lit, k, raw, norm))
            print(f'    {tier:8s} raw {raw:2d}  unmarked {norm:2d}  {k:24s} {lit[:46]!r}{mark}')
    print(f'\n  {len(rows)} key(s);  {len(fails)} fail floor 2')
    if fails:
        print('  ⛔ a span that stands more than once cannot say which place the claim is about.')
        return 1
    print('  every live span of these receipts stands exactly ONCE in the file it is checked against,')
    print('  measured through the checker\'s own normaliser rather than a reimplementation of it.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:] or sorted(glob.glob(os.path.join(R, 'receipts', 'P15_CR_cosmology', '*.py')))))
