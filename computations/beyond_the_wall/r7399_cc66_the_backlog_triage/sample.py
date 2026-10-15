#!/usr/bin/env python3
"""r7399 ⑩ -- draw the registered sample and measure what the harvester cannot see.

The draw is `random.Random(7399).sample(sorted(sites), 40)`, fixed in REGISTRATION.md and pushed
before this ran, so it cannot be re-rolled.  The unit is the SITE, because ⑩ says "reading the
paragraph rather than the marker".

    python3 -I sample.py <repo-root>            # the 40, with their paragraphs
    python3 -I sample.py <repo-root> --reach    # the comment-line measurement (band ⒟)
"""
import os, random, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
BASELINE = os.path.join(ROOT, 'corpus', 'open_reference_baseline.tsv')
VOCABFILE = os.path.join(ROOT, 'corpus', 'open_vocabulary.tsv')
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]
_SENT = re.compile(r'(?<=[.!?])\s+')


def rows():
    out = []
    for line in open(BASELINE, encoding='utf-8').read().split('\n'):
        if not line or line.startswith('#') or '\t' not in line:
            continue
        f = line.split('\t')
        if f[0] == 'paper':
            continue
        out.append(f)                   # paper section expression source mechanism verdict sentence
    return out


def paras(stem, keep_comments=False):
    """Every paragraph of a paper.  keep_comments=True leaves the `%` lines in, which is the whole
    point of the reach measurement: body() drops them before anything else runs."""
    txt = open(os.path.join(ROOT, 'corpus', stem + '.tex'), encoding='utf-8',
               errors='replace').read()
    if not keep_comments:
        txt = '\n'.join(l for l in txt.split('\n') if not l.lstrip().startswith('%'))
    j = txt.find('\\begin{thebibliography}')
    txt = txt[:j] if j > 0 else txt
    return [re.sub(r'\s+', ' ', p) for p in re.split(r'\n\s*\n', txt)]


if '--reach' in sys.argv:
    live = []
    for line in open(VOCABFILE, encoding='utf-8').read().split('\n'):
        if not line or line.startswith('#') or '\t' not in line:
            continue
        f = line.split('\t')
        if f[0] == 'expression' or f[2] == 'NOT-AN-OPEN':
            continue
        live.append((f[0], re.compile(f[0], re.I)))
    print(f'# ⑩ ⒟ WHAT THE HARVESTER CANNOT SEE -- `%` comment lines, dropped by body() before any '
          f'test runs')
    print(f'#   vocabulary: {len(live)} live expression(s)')
    tot, perpaper = 0, []
    for num, stem in PAPERS:
        txt = open(os.path.join(ROOT, 'corpus', stem + '.tex'), encoding='utf-8',
                   errors='replace').read()
        clines = [l for l in txt.split('\n') if l.lstrip().startswith('%')]
        n = sum(1 for l in clines for _w, r in live if r.search(l))
        hits = sum(len(r.findall(' '.join(clines))) for _w, r in live)
        tot += hits
        perpaper.append((num, len(clines), n, hits))
    print(f'#   {"paper":6s} {"comment lines":>13s} {"lines w/ a marker":>18s} {"marker hits":>12s}')
    for num, nl, n, hits in perpaper:
        if hits:
            print(f'#   {num:6s} {nl:13d} {n:18d} {hits:12d}')
    print(f'#   TOTAL vocabulary matches inside comment lines: {tot}')
    print(f'#   ⇒ every one of them is OUTSIDE the 390 by construction, at any vocabulary.')
    sys.exit(0)

data = rows()
sites = sorted({(r[0], r[6]) for r in data})
print(f'# the population: {len(data)} keys over {len(sites)} sites')
pick = random.Random(7399).sample(sites, 40)
print(f'# the registered draw: random.Random(7399).sample(sorted(sites), 40) -> {len(pick)} sites')
print()
by = {}
for r in data:
    by.setdefault((r[0], r[6]), []).append(r)
cache = {num: paras(stem) for num, stem in PAPERS}
for i, (num, sent) in enumerate(sorted(pick, key=lambda t: ([p for p, _ in PAPERS].index(t[0]),
                                                            t[1])), 1):
    rs = by[(num, sent)]
    host = next((p for p in cache[num] if sent[:60] in re.sub(r'\s+', ' ', p)), '')
    print(f'=== {i:02d}  {num} §{rs[0][1]}  [{" ".join(sorted({r[2] for r in rs}))}] '
          f'[{rs[0][4]}]')
    print(f'SENT: {sent}')
    print(f'PARA: {host[:1400]}')
    print()
