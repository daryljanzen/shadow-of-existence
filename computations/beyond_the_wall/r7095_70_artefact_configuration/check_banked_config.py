"""r7095 (70) Q1 -- a PROTOTYPE of the gate the order asks to be specified: a banked spectrum is admissible only if
its configuration is a property of the artefact.  Report mode; NOT registered (registering a gate is 66's call).

THE RULE (the specification, stated where it is tested):
  (1) at save time, ACOUSTIC_two_arm.py writes `config` into every .npz: a JSON string of EVERY environment switch
      the instrument reads, each with the value it RESOLVED to (a default written out, never left implicit), plus
      the instrument's own git blob hash.  An unset switch is recorded as its resolved default, so a later change of
      default cannot silently re-label an old run (the census's hazard: a command that omits a switch means
      whatever the default was AT THE RUN).
  (2) a reader refuses a banked .npz that carries no `config` -- UNLESS a backfill manifest beside the bank names
      it, with the grade of the evidence: COMMAND (a launcher or README row in the repository names its exact
      command) or FINGERPRINT (only l_A/r_s place it).  FINGERPRINT entries are readable but flagged inferred.
  (3) an artefact with neither is unreadable by the gate -- which is the point: it has no reproducible provenance.

What this script does:  for every .npz in the repository's banks, says whether it passes (1) today, and grades what
a backfill manifest could say for it; writes the manifest it COULD write (manifest_proposal.json, beside this file,
not into the bank).  Nothing is edited in the bank.

Usage:  python3 check_banked_config.py
"""
import glob
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
BANKS = [os.path.join(BW, d) for d in ('spectra', 'refit_grid', 'refit_grid185')]
README = open(os.path.join(BW, 'spectra', 'README.md'), encoding='utf-8').read()
SH = {p: open(p, encoding='utf-8', errors='replace').read()
      for p in glob.glob(os.path.join(BW, '**', '*.sh'), recursive=True)}
SWRE = re.compile(r'\b([A-Z][A-Z0-9_]{1,15})=([\w.+\-$:/{}<>]+)')

# configurations by fingerprint (the census's): CR l_A / r_s
# an onset SOLVED for a pinned l_A leaves l_A exactly at the pin (a round LATARG); a fixed onset leaves it free
FP = [('A (default: stacking, onset solved for l_A = 301.6)', lambda la, rs: abs(la - 301.600) < 1e-3),
      ('A-family (onset solved for a pinned l_A = LATARG)', lambda la, rs: abs(la * 10 - round(la * 10)) < 1e-6),
      ('B (LEAFSCALES=1 ZSTART=3e7)', lambda la, rs: 300.0 < la < 304.0 and 144.5 < rs < 147.0),
      ('superseded stacking ruler (l_A ~ 172)', lambda la, rs: 170.0 < la < 175.0)]


def command_for(stem, bank):
    """the exact command a launcher or README row in the repository gives for this artefact, or None"""
    # README rows: the backticked file name, then the command
    for line in README.splitlines():
        fam = re.findall(r'`([\w.\-<>]+)\.npz`', line) if line.startswith('|') else []
        if any(re.fullmatch(re.escape(f).replace('<PHI>', r'[\d.]+').replace('\\<PHI\\>', r'[\d.]+'), stem)
               or re.fullmatch(re.sub(r'<[A-Z]+>', '@@', f).replace('.', r'\.').replace('@@', r'[\w.]+'), stem)
               for f in fam if '<' in f):
            sw = dict(SWRE.findall(line))
            return ('spectra/README.md (family row)', line.strip()[:300], sw)
        if line.startswith('|') and f'`{stem}.npz`' in line:
            sw = dict(SWRE.findall(line))
            if 'ARM' in sw or 'same' in line:
                return ('spectra/README.md', line.strip()[:300], sw)
    tag = stem
    for p, s in SH.items():
        for line in s.splitlines():
            # launcher rows name the output tag as a word, with an ARM= environment on the same line
            if re.search(r'(?<![\w.])' + re.escape(tag) + r'(?![\w.])', line) and 'ARM' in line:
                return (os.path.relpath(p, ROOT), line.strip()[:300], dict(SWRE.findall(line)))
            # or through a $D/<tag>.npz / prefix scheme: r6941_fine_cr <- tag 'fine_cr' in r6941_directions
    m = re.match(r'(r\d{4})_(.+)$', stem)
    if m:
        d = os.path.join(BW, f'{m.group(1)}_directions')
        for p in glob.glob(os.path.join(d, '*.sh')):
            s = SH.get(p, '')
            if m.group(2) in s or stem in s:
                return (os.path.relpath(p, ROOT), f'{m.group(2)} in {os.path.basename(p)}', {})
            # banked under the directory's launcher by construction (one launcher, one CR environment)
        if os.path.isdir(d):
            ls = [p for p in glob.glob(os.path.join(d, '*.sh'))]
            if ls:
                return (os.path.relpath(ls[0], ROOT), f'the directory launcher (output name not literal)', {})
    if bank.endswith(('refit_grid', 'refit_grid185')):
        lp = os.path.join(bank, 'launch.sh')
        vp = os.path.join(bank, 'verify.sh')
        for p in (lp, vp):
            if os.path.exists(p):
                s = open(p, encoding='utf-8').read()
                k = stem.replace('verify_', '')
                for line in s.splitlines():
                    if re.search(r'(?<![\w])' + re.escape(stem) + r'(?![\w])', line) and 'ARM' in line:
                        return (os.path.relpath(p, ROOT), line.strip()[:300], dict(SWRE.findall(line)))
    return None


def fingerprint(z):
    if 'l_A' not in z.files or 'r_s' not in z.files:
        return None
    la, rs = float(z['l_A']), float(z['r_s'])
    arm = str(z['arm']) if 'arm' in z.files else '?'
    if arm == 'lcdm':
        return f'control arm (no CR switch applies)  [l_A {la:.3f}, r_s {rs:.3f}]'
    for name, f in FP:
        if f(la, rs):
            return f'{name}  [arm {arm}, l_A {la:.3f}, r_s {rs:.3f}]'
    return f'no known configuration  [arm {arm}, l_A {la:.3f}, r_s {rs:.3f}]'


rows = []
for bank in BANKS:
    for p in sorted(glob.glob(os.path.join(bank, '*.npz'))):
        stem = os.path.basename(p)[:-4]
        try:
            z = np.load(p, allow_pickle=True)
            files = z.files
        except Exception as e:
            rows.append((os.path.relpath(p, ROOT), 'UNREADABLE', str(e)[:80], None))
            continue
        has = 'config' in files
        cmd = command_for(stem, bank)
        fp = fingerprint(z)
        if has:
            grade = 'PASSES (carries config)'
        elif cmd:
            grade = 'COMMAND'
        elif fp and fp.startswith('control arm'):
            grade = 'CONTROL (no CR switch)'
        elif fp and not fp.startswith('no known'):
            grade = 'FINGERPRINT'
        elif fp:
            grade = 'FINGERPRINT (unplaced)'
        else:
            grade = 'NONE'
        rows.append((os.path.relpath(p, ROOT), grade, (cmd[0] + ': ' + cmd[1]) if cmd else (fp or ''), cmd[2] if cmd else None))

from collections import Counter
cnt = Counter(r[1] for r in rows)
print(f'banked .npz in the repository: {len(rows)}  ({", ".join(os.path.relpath(b, ROOT) for b in BANKS)})')
print(f'carrying a config today (passing rule (1)): {cnt.get("PASSES (carries config)", 0)}')
print('backfill grade for the rest:')
for g in ('COMMAND', 'CONTROL (no CR switch)', 'FINGERPRINT', 'FINGERPRINT (unplaced)', 'NONE', 'UNREADABLE'):
    print(f'  {cnt.get(g, 0):4d}  {g}')
print('\nthe artefacts a manifest could NOT place by command:')
for r in rows:
    if r[1] not in ('COMMAND', 'PASSES (carries config)'):
        print(f'  {r[1]:24s} {r[0]:70s} {r[2][:120]}')
man = {r[0]: dict(grade=r[1], evidence=r[2], switches=r[3]) for r in rows}
json.dump(man, open(os.path.join(HERE, 'manifest_proposal.json'), 'w'), indent=1, sort_keys=True)
print(f'\nmanifest_proposal.json written beside this file: {len(man)} entries (a proposal; nothing in the bank is edited)')
