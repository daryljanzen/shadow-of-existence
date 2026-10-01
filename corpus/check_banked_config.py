#!/usr/bin/env python3
"""check_banked_config.py -- A BANKED SPECTRUM MUST CARRY THE CONFIGURATION IT WAS COMPUTED AT.

** THE ERROR THIS EXISTS FOR. **  `r7093`'s census had to ask which model each of `P15`'s 139 acoustic
figures was a figure of -- and found that NO banked spectrum records its own switches.  The `.npz` carry
`ls, Dl, l_A, D_M, r_s, arm` and nothing that says LEAFSCALES, ZSTART, STACKPERT or VISLEAF.  So the census
reconstructed every configuration from launchers, a README, receipt docstrings and, for forty-seven
artefacts, from the stored l_A alone.  `r7095` measured the cost: **0 of 215 carry a configuration; 162 can
be placed by a command or as control, 47 by fingerprint only, 6 not at all.**  And the question mattered:
on the default configuration the CR arm's contrast is 5.6 per cent BELOW the control and out of phase; on
the reported one it is 5.6 per cent above.  A figure whose model cannot be named cannot be compared.

** WHAT IT CHECKS. **  Every `.npz` in the repository's banks (`computations/beyond_the_wall/spectra/`,
`refit_grid/`, `refit_grid185/`) must EITHER
  (1) carry a `config` key: a JSON object naming the switches the instrument RESOLVED -- at least `ARM`
      and the four that define a model, `LEAFSCALES`, `ZSTART`, `STACKPERT`, `VISLEAF`, each with its
      resolved value (a default WRITTEN OUT: an omitted switch means whatever the default was at the run,
      and a later change of default would silently re-label it) -- at the top level or under `switches`;
  OR
  (2) be named in `corpus/banked_config_manifest.json` -- the artefacts that predate this gate -- with the
      SHA-256 of its bytes, its backfill grade and the evidence for it.

** WHY A CONTENT-HASHED MANIFEST, AND NOT THE OTHER RATCHETS (`r7097`, the design choice). **
  - A DATED baseline needs a date the repository does not keep: git stores no mtime, and a commit date is
    the LAST touch, so a re-banked file would inherit an old date.  It cannot tell new from rewritten.
  - The FINGERPRINT as a fallback would admit any NEW artefact whose l_A happens to fingerprint -- reopening
    the hole for exactly the class being closed.  So the fingerprint GRADES entries; it never ADMITS one.
  - A NAME-ONLY manifest is the symptom pin: it would pass a file regenerated in place, with new content and
    still no switches.
  ⇒ ** The hash makes it a ratchet.**  An entry admits THOSE BYTES.  It fails:
      NEW         a banked .npz with neither `config` nor a manifest entry;
      REWRITTEN   a manifest entry whose file's hash has changed -- a re-banked artefact must carry config;
      STALE       a manifest entry whose file is gone, or now carries `config` -- REMOVE it (`r7069`'s rule:
                  a fixed site must not stay behind as a silent permission);
      MALFORMED   a `config` that is not a JSON object carrying ARM and the four defining switches.
  So the manifest can only SHRINK, and what it says about each entry -- COMMAND / CONTROL / FINGERPRINT /
  UNPLACEABLE, with the evidence -- is a record of what was found, not an exemption: a FINGERPRINT entry is a
  reconstruction and says so; an UNPLACEABLE one says nothing is known.

** THE WRITING HALF IS NOT HERE. **  `ACOUSTIC_two_arm.py` writing `config` at save time is `cc66`'s (ordered
at `r7097`).  This gate is what makes that checkable rather than a habit.

    python3 corpus/check_banked_config.py
    python3 corpus/check_banked_config.py --list     # the manifest's entries by grade
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
BANKS = [os.path.join('computations', 'beyond_the_wall', d) for d in ('spectra', 'refit_grid', 'refit_grid185')]
MANIFEST = os.path.join(HERE, 'banked_config_manifest.json')
DEFINING = ('ARM', 'LEAFSCALES', 'ZSTART', 'STACKPERT', 'VISLEAF')


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def banked(root=ROOT):
    out = []
    for b in BANKS:
        d = os.path.join(root, b)
        if os.path.isdir(d):
            out += sorted(os.path.join(b, f) for f in os.listdir(d) if f.endswith('.npz'))
    return out


def config_of(path):
    """(present, problem) -- present is False when there is no `config`; problem names a malformation"""
    try:
        z = np.load(path, allow_pickle=False)
    except Exception as e:                     # an unreadable bank file is itself a failure
        return True, f'unreadable: {str(e)[:60]}'
    if 'config' not in z.files:
        return False, None
    try:
        c = json.loads(str(z['config']))
    except Exception:
        return True, '`config` is not JSON'
    if not isinstance(c, dict):
        return True, '`config` is not a JSON object'
    sw = c.get('switches', c)
    missing = [k for k in DEFINING if k not in sw]
    if missing:
        return True, f'`config` lacks {", ".join(missing)} (each must be written out, a default included)'
    return True, None


def main(root=ROOT):
    mpath = os.path.join(root, 'corpus', os.path.basename(MANIFEST))
    man = json.load(open(mpath, encoding='utf-8')) if os.path.exists(mpath) else None
    print()
    print('  BANKED CONFIG -- does every banked spectrum carry the configuration it was computed at?')
    print()
    if man is None:
        print(f'  [FAIL] {os.path.relpath(mpath, root)} is absent; the manifest is data and must exist')
        return 1
    if '--list' in sys.argv:
        by = {}
        for k, v in man['entries'].items():
            by.setdefault(v['grade'], []).append(k)
        for g, ks in sorted(by.items()):
            print(f'  {g}: {len(ks)}')
            for k in ks:
                print(f'      {k}   {man["entries"][k]["evidence"][:110]}')
        return 0
    files = banked(root)
    entries = man['entries']
    new, rewritten, stale, malformed, carried = [], [], [], [], 0
    for rel in files:
        present, problem = config_of(os.path.join(root, rel))
        if present:
            if problem:
                malformed.append((rel, problem))
            else:
                carried += 1
            if rel in entries:
                stale.append((rel, 'now carries `config` -- remove its manifest entry'))
            continue
        if rel not in entries:
            new.append(rel)
        elif sha(os.path.join(root, rel)) != entries[rel]['sha256']:
            rewritten.append(rel)
    for rel in entries:
        if rel not in files:
            stale.append((rel, 'no longer in the bank -- remove its manifest entry'))
    grades = {}
    for v in entries.values():
        grades[v['grade']] = grades.get(v['grade'], 0) + 1
    print(f'    {len(files)} banked .npz; {carried} carry `config`; {len(entries)} predate this gate in the manifest')
    print('    the manifest, by what is known of each: ' +
          ', '.join(f'{g} {n}' for g, n in sorted(grades.items(), key=lambda x: -x[1])))
    print('    ⌗ FINGERPRINT entries are reconstructions from l_A and r_s, not records; UNPLACEABLE ones say nothing is known.')
    print()
    bad = False
    for rel in new:
        bad = True
        print(f'    [FAIL] NEW        {rel}: no `config` and not in the manifest')
    for rel in rewritten:
        bad = True
        print(f'    [FAIL] REWRITTEN  {rel}: its bytes changed since the manifest -- a re-banked artefact must carry `config`')
    for rel, why in stale:
        bad = True
        print(f'    [FAIL] STALE      {rel}: {why}')
    for rel, why in malformed:
        bad = True
        print(f'    [FAIL] MALFORMED  {rel}: {why}')
    if bad:
        print()
        print('    ⛔ Bank new spectra with `config` written at save time (every switch the instrument read, each')
        print('       at its RESOLVED value).  Do not add a new artefact to the manifest: it lists what predates')
        print('       the gate, and it only shrinks.')
        print()
        return 1
    print('  every banked spectrum either carries its configuration or predates the gate unchanged; the manifest')
    print('  has no stale entry.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
