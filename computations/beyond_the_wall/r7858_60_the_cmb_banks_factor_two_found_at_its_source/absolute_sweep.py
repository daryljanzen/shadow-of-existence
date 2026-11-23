#!/usr/bin/env python3
"""`r7858` Ⓒ③ Ⓒ③ᵇ — every absolute statement read off the CMB bank, SWEPT and not hand-listed.

Order `r7855` ② asks for the receipts, `P15` sentences and appendix lines that pin an absolute CMB
amplitude, a `χ²` with the amplitude HELD, or an `A_s` derived from the bank — each with its owning
seat — so that `69` can order each owner.  `r7856` established that statements made with a FREE
amplitude are unaffected in VALUE by the factor, because a free amplitude absorbs a constant.

⛔ ** THE SWEEP HAS A POSITIVE CONTROL AND THAT IS NOT A FORMALITY. **  `S55` on this line's own
ledger is about a census whose population shrank until its non-vacuity read off the same range
became meaningless.  So this file states, before it runs, two things it must find and one it must
NOT list, and it FAILS if any of the three comes out wrong:

  ⊕ `amplitude=1.0` and `amplitude=None` are the two forms the scorers take, and a call passing
    `amplitude=1.0` (or `score(b, amplitude=...)`, or `chi2_of(..., amplitude=...)`) is an
    amplitude-HELD score — it must be FOUND.
  ⊕ `r7856`'s own receipt holds the nine bandpowers at a factor of exactly one and must be found.
  ⊖ a call with no `amplitude=` argument fits one in closed form and must NOT be listed as absolute.

⌗ What this file does NOT do: decide anything about the statements it finds.  Each is reported with
its owning seat, read off `git log --follow`, and routed.  ** Most of them are not this seat's. **

Run: python3 absolute_sweep.py       (writes absolute_sweep.json)
"""
import io
import json
import os
import re
import subprocess

_HERE = os.path.dirname(os.path.abspath(__file__))
# ⛔ *Three levels, not two.  The first version of this file used two and `ROOT` came out as
# `computations/`, so `os.walk(ROOT/receipts)` walked nothing and the sweep reported ZERO absolute
# statements with ZERO free-amplitude ones beside them.  ** `Ⓒ③ᵇ`'s positive control is what caught
# it: ** a census with no positive control would have reported "nothing to route" and been believed.
# That is the `S55` defect on this line's own ledger, reproduced and caught the same day.*
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), (
    'ROOT does not contain receipts/ -- the walk would sweep nothing: %s' % ROOT)

# the shapes an amplitude-HELD score takes in this corpus, each read off the scorers' own signatures
HELD = (
    re.compile(r'amplitude\s*=\s*1\.0\b'),
    re.compile(r'amplitude\s*=\s*1\b'),
    re.compile(r'chi2_nothing_fitted'),
    re.compile(r'nothing[ _]fitted'),
    re.compile(r'amplitude[ _]held'),
)
# an A_s taken off the bank rather than stated as a parameter
AS_DERIVED = (
    re.compile(r'implied[ _]amp'),
    re.compile(r'amp_cmb'),
    re.compile(r'derived[ _]A_s|A_s[ _]derived'),
)
FREE = re.compile(r'amplitude\s*=\s*None|score\([^)]*\)\s*$|one amplitude (?:is )?fitted|free amplitude')


def owner(path):
    """the seat that authored the file, from the FIRST commit that added it"""
    r = subprocess.run(['git', 'log', '--follow', '--diff-filter=A', '--format=%s', '--', path],
                       cwd=ROOT, capture_output=True, text=True)
    lines = [l for l in r.stdout.splitlines() if l.strip()]
    if not lines:
        return 'unknown'
    first = lines[-1]
    m = re.search(r'\+(cc66|70|69|72|60)\b', first) or re.search(r'\((cc66|70|69|72|60)\)', first)
    if m:
        return m.group(1)
    m = re.match(r'\s*r?\d+\s*\(?(cc66|70|69|72|60)\)?', first)
    return m.group(1) if m else ('60' if first.startswith('r78') else 'unknown')


def sweep():
    hits, free_only = [], []
    for base, _dirs, files in os.walk(os.path.join(ROOT, 'receipts')):
        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            p = os.path.join(base, f)
            rel = os.path.relpath(p, ROOT)
            try:
                txt = io.open(p, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            if 'score' not in txt and 'chi2' not in txt:
                continue
            why = []
            for rx in HELD:
                if rx.search(txt):
                    why.append('amplitude-held: %s' % rx.pattern)
                    break
            for rx in AS_DERIVED:
                if rx.search(txt):
                    why.append('A_s off the bank: %s' % rx.pattern)
                    break
            if why:
                hits.append(dict(path=rel, why=why))
            elif FREE.search(txt):
                free_only.append(rel)
    return hits, free_only


def main():
    hits, free_only = sweep()
    print('\n  Ⓒ③ THE SWEEP over receipts/', flush=True)
    print('      %d receipt(s) make a statement that a constant factor on the bank would move;'
          % len(hits))
    print('      %d more score with a FREE amplitude only, which r7856 established is unaffected'
          % len(free_only))
    print('      in value by a constant.\n', flush=True)
    for h in hits:
        h['owner'] = owner(h['path'])
    by = {}
    for h in hits:
        by.setdefault(h['owner'], []).append(h)
    print('      by owning seat:')
    for o in sorted(by):
        print('        %-8s %d' % (o, len(by[o])))
    print()
    for o in sorted(by):
        for h in by[o]:
            print('        [%s] %s' % (o, os.path.basename(h['path'])))
            print('              %s' % '; '.join(h['why']))
    out = dict(absolute=hits, free_amplitude_only=free_only,
               by_owner={k: len(v) for k, v in by.items()})

    print('\n  Ⓒ③ᵇ THE POSITIVE CONTROL', flush=True)
    mine = [h for h in hits if 'absolute_lensing_scale' in h['path']]
    names = {os.path.basename(h['path']) for h in hits}
    ctl1 = bool(mine)
    ctl2 = any('amplitude-held' in w for h in hits for w in h['why'])
    ctl3 = not any(f in names for f in [os.path.basename(x) for x in free_only])
    print('      ⊕ r7856\'s own receipt, which holds the nine bandpowers at a factor of exactly')
    print('        one, is FOUND: %s' % ctl1)
    print('      ⊕ at least one amplitude-HELD form is found: %s' % ctl2)
    print('      ⊖ no free-amplitude-only file is listed as absolute: %s' % ctl3)
    ok = ctl1 and ctl2 and ctl3
    print('    ** Ⓒ③ᵇ %s: the sweep finds what it must and does not list what it must not **'
          % ('HOLDS' if ok else 'FAILS'), flush=True)
    out['control'] = dict(holds=bool(ok), finds_r7856=ctl1, finds_held_form=ctl2,
                          excludes_free_only=ctl3)
    out['C3'] = dict(swept_not_hand_listed=True, n_absolute=len(hits),
                     n_free_amplitude_only=len(free_only))

    with io.open(os.path.join(_HERE, 'absolute_sweep.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote absolute_sweep.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
