"""r7093 (70) -- the configuration census: for every figure P15's acoustic sections quote from the two-arm
transfer, the artefact it was read from and that artefact's configuration.  Pre-registered in PREDICTION.md.
Nothing is run.

THE CONFIGURATIONS, recovered from the repository (no banked .npz records its own switches: the keys are
ls, Dl, l_A, D_M, r_s, arm).  Today's defaults, read at ACOUSTIC_two_arm.py source and unchanged since each switch
was introduced (LEAFSCALES at r6760, default '0', never changed):

  A  DEFAULT        LEAFSCALES unset (stacking rate), ZSTART unset (onset SOLVED for l_A = LATARG = 301.6)
                    -- spectra/c54.*, L814_*, L820_*, L824_*, L830_* (README commands carry neither switch);
                       fingerprint: CR l_A = 301.600 exactly, r_s = 135.46
  C  STACK+FIXED    LEAFSCALES unset, ZSTART=3e7, CRIC=branchpoint  -- spectra/r6784_*, r6794_* (README)
  B  LEAF+FIXED     LEAFSCALES=1, ZSTART=3e7  -- refit_grid*/launch.sh, refit_grid185/verify.sh, every
                    r6885..r7041 launcher; fingerprints: l_A 302.889 at the grid base, 301.799 at the refit minimum
  ?  UNRECORDED     a banked CR spectrum with no command in the repository; its stored l_A is reported as a
                    fingerprint against the three above

The STACKPERT and VISLEAF switches are at their defaults (0, 0) in every configuration above except the one-knob
VISLEAF variants (r6925_visleaf_cr, r6941_fine_cr_visleaf), which are named as such.

Usage:  python3 census.py     (writes census_table.md beside it, prints the summary and the seam paragraphs)
"""
import glob
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SPEC = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_marker_transposition as G                     # noqa: E402

TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
SPANS = {'tensions': (220, 301), 'envelope': (482, 522), 'envelope-consequence': (523, 592),
         'diffusion-scale': (593, 622), 'isw': (623, 644), 'residual-decomposition': (645, 687),
         'shear-coefficient': (688, 705), 'refit-bound': (706, 1825), 'instrument': (2101, 2113)}
IDX = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)
       + glob.glob(os.path.join(ROOT, 'storyboard_receipts', '**', '*.py'), recursive=True)}

A_PAT = re.compile(r'^(c54\.\d+|L8\d\d)_')
C_PAT = re.compile(r'^r67(84|94)_')
B_PAT = re.compile(r'^(cc66_r185_verify|cc66_refit_verify|r68[89]\d|r69\d\d|r70\d\d|cc66_cr_x_h686)')
B_BANKS = ('refit_grid185', 'refit_grid', 'r7041_directions', 'r7021_directions', 'r6885_directions')


def fingerprint(stem):
    p = os.path.join(SPEC, stem + '.npz')
    if not os.path.exists(p):
        return None
    try:
        z = np.load(p, allow_pickle=True)
        return float(z['l_A']) if 'l_A' in z.files else None
    except Exception:
        return None


def classify_artefact(stem):
    """the CR-side configuration of one banked artefact, and how it is known"""
    if stem.endswith('_lcdm') or '_lcdm_' in stem or stem.endswith('lcdm'):
        return 'CONTROL', 'control arm (no CR switch applies)'
    if A_PAT.match(stem):
        return 'A', 'spectra/README.md command: neither LEAFSCALES nor ZSTART set'
    if C_PAT.match(stem):
        return 'C', 'spectra/README.md command: ZSTART=3e7, LEAFSCALES unset'
    if B_PAT.match(stem):
        how = 'launcher: LEAFSCALES=1 ZSTART=3e7'
        if stem.startswith('cc66_cr_x_h686'):
            how = (f'command only in a receipt docstring (P15_the_anomalous_driving_..., `ARM=cr CRH0=68.60 CROM=0.2973 '
                   f'ZSTART=3e7 LEAFSCALES=1`); fingerprint l_A={fingerprint(stem):.3f} = the refit grid base (B)')
        return 'B', how
    if stem == 'cc66_fig_acoustic_numbers':
        return 'B', 'derived numbers: corpus/make_fig_acoustic_two_arm.py reads cc66_r185_verify_{lcdm,cr} (B)'
    lA = fingerprint(stem)
    return '?', (f'NO COMMAND in the repository; fingerprint l_A={lA:.3f} matches none of A/B/C'
                 if lA else 'NO COMMAND in the repository and no l_A')


def receipt_class(name):
    p = IDX.get(name)
    if not p:
        return 'MISSING', []
    s = open(p, encoding='utf-8', errors='replace').read()
    arts = []
    for stem in sorted(set(re.findall(r"([\w.\-]+)\.npz", s))):
        if os.path.exists(os.path.join(SPEC, stem + '.npz')):
            arts.append((stem,) + classify_artefact(stem))
    for b in B_BANKS:
        if b in s:
            arts.append((b + '/', 'B', 'launcher: LEAFSCALES=1 ZSTART=3e7'))
    for t in sorted(set(re.findall(r"/tmp/n66/[\w/.\-]*", s))):
        if 'r7041' in t:
            arts.append((t, 'B', 'launcher r7041_directions/launch_c.sh (B); the artefact is NOT IN THE REPOSITORY'))
        elif t.startswith('/tmp/n66/...') or 'refit' in t:
            arts.append((t, 'B', 'launcher refit_grid185/launch.sh (B); the artefact is NOT IN THE REPOSITORY'))
        else:
            arts.append((t, '?', 'NOT IN THE REPOSITORY'))
    if 'c54.170' in s and 'ARM=cr' in s:
        arts.append(('a c54.170 run, numbers typed in', 'A', 'receipt text: measured at c54.170, before LEAFSCALES existed'))
    cls = sorted({a[1] for a in arts if a[1] != 'CONTROL'})
    if not arts:
        return 'NONE', arts
    if not cls:
        return 'CONTROL', arts
    return '+'.join(cls), arts


def main():
    tex = open(TEX, encoding='utf-8').read()
    lines = tex.split('\n')
    groups = [(ln, names, claim, par) for (ln, names, claim, par) in G.groups(G.strip(tex))
              if any(a <= ln <= b for a, b in SPANS.values())]
    rc = {}
    for _, names, _, _ in groups:
        for n in names:
            if n not in rc:
                rc[n] = receipt_class(n)
    # ---- the table, one row per figure (a number in a group's claim) whose group reads a transfer artefact
    out = ['| line | section | figure | receipt(s) carrying it, else the group | CR configuration | how it is known |',
           '|---|---|---|---|---|---|']
    nfig = 0
    by = {}
    for ln, names, claim, _ in groups:
        sec = next(k for k, (a, b) in SPANS.items() if a <= ln <= b)
        for tok in G.tokens(claim):
            car = [n for n in names if IDX.get(n) and
                   G.carries(G.unquoted(open(IDX[n], encoding='utf-8', errors='replace').read()), tok)]
            src = car or names
            cls = sorted({rc[n][0] for n in src if rc[n][0] not in ('NONE', 'MISSING')})
            if not cls:
                continue
            nfig += 1
            label = '+'.join(cls)
            by[label] = by.get(label, 0) + 1
            how = '; '.join(sorted({f'{a[0]}: {a[2]}' for n in src for a in rc[n][1] if a[1] not in ('CONTROL',)}))[:300]
            out.append(f'| {ln} | {sec} | {tok} | {", ".join("`" + n[:55] + "`" for n in src)}'
                       f'{"" if car else " (group)"} | **{label}** | {how or "control only"} |')
    open(os.path.join(HERE, 'census_table.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    # ---- the summary
    print(f'acoustic sections: {", ".join(SPANS)}')
    print(f'marker groups in them: {len(groups)}; distinct receipts cited: {len(rc)}')
    cnt = {}
    for n, (c, _) in rc.items():
        cnt[c] = cnt.get(c, 0) + 1
    print('receipts by the CR configuration of what they read:')
    for c, k in sorted(cnt.items(), key=lambda x: -x[1]):
        print(f'  {k:3d}  {c}')
    print(f'figures (numbers in a group claim) resting on a transfer artefact: {nfig}; by configuration:')
    for c, k in sorted(by.items(), key=lambda x: -x[1]):
        print(f'  {k:3d}  {c}')
    print('artefacts whose command is not in a launcher or README, or which are not banked:')
    seen = set()
    for n, (c, arts) in rc.items():
        for a in arts:
            if ('NO COMMAND' in a[2] or 'NOT IN THE REPOSITORY' in a[2] or 'docstring' in a[2]) and a[0] not in seen:
                seen.add(a[0])
                print(f'  {a[0]:40s} {a[1]:2s}  {a[2]}   (read by {n[:60]})')
    # ---- the seam: paragraphs whose groups rest on DIFFERENT CR configurations
    print('\nTHE SEAM -- paragraphs citing receipts that rest on different CR configurations:')
    pars = {}
    for ln, names, claim, par in groups:
        for n in names:
            for c in rc[n][0].split('+'):
                if c in ('A', 'B', 'C', '?'):
                    pars.setdefault(par, {}).setdefault(c, set()).add((ln, n))
    for par, d in sorted(pars.items()):
        if len(d) > 1:
            lns = sorted({ln for v in d.values() for ln, _ in v})
            print(f'  paragraph at lines {lns[0]}-{lns[-1]}: ' +
                  '; '.join(f'{c}: ' + ', '.join(sorted({n[:48] for _, n in v})) for c, v in sorted(d.items())))
    mixed = [n for n, (c, _) in rc.items() if '+' in c]
    print('\nreceipts that themselves read more than one CR configuration:')
    for n in mixed:
        print(f'  {rc[n][0]:6s} {n}')


if __name__ == '__main__':
    main()
