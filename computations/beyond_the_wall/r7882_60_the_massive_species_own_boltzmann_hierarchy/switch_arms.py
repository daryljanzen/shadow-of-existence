# -*- coding: utf-8 -*-
"""r7882+60 — THE SWITCH'S OWN ARMS, before any physics of it is read.

Three claims, each measured on OUTPUT rather than asserted:

  ① **OFF IS BYTE-IDENTICAL**, both ways of being off -- absent from the environment and `NUHIER=0`
     -- against `origin/main`'s instrument, every array compared element for element.
  ② **THE PREVIOUS REVISION'S SWITCH IS UNTOUCHED**: the fluid approximation at `NUPERT=1` with its
     defaults gives bit-identical output before and after this revision's diff.  *That is what makes
     the hierarchy an ADDITION and not a quiet re-plumbing of the sector.*
  ③ **IT REFUSES WHAT IT CANNOT RUN**: beside the fluid approximation, without the background
     switch, at zero sum, and with a grid or a cutoff too small to be one.

⌗ NOT RETYPED.  The leg runner and the array comparison are `r7878`'s own `one` and `same`,
  IMPORTED, so this file and that one decide identity the same way.
⌗ Cheap on purpose: `LMAXL=300 LSTEP=60`, the same coarse grid `r7878`'s arms used.  Identity is
  identity, and a coarse grid exercises every line the switch touches.

    NODE=60 python3 switch_arms.py
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7878 = os.path.join(_BTW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic'
                            '_sound_speed')
sys.path.insert(0, _R7878)
from switch_arms import REL, _REPO, one, same                                   # noqa: E402

PRE = os.path.join(_BTW, '_prelanded_ACOUSTIC_two_arm.py')
CUR = os.path.join(_BTW, 'ACOUSTIC_two_arm.py')
REFUSALS = {
    'beside the fluid approximation': dict(NUHIER='1', NUPERT='1'),
    'no NUFD': dict(NUHIER='1', NUFD='0'),
    'zero sum': dict(NUHIER='1', MNU='0.0'),
    'a grid of one node': dict(NUHIER='1', NQ='1'),
    'no quadrupole': dict(NUHIER='1', LMAXNU='1'),
    'a non-positive cut': dict(NUHIER='1', QMAXNU='0'),
}


def main():
    print(__doc__)
    print('=' * 100)
    src = subprocess.run(['git', 'show', 'origin/main:' + REL], cwd=_REPO,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if src.returncode != 0:
        raise SystemExit('  ⛔ could not read origin/main\'s instrument: %s'
                         % src.stdout.decode('utf-8', 'replace')[:300])
    pre, cur = src.stdout, io.open(CUR, 'rb').read()
    #: ⛔ *gated against the two being the same file: an arm that compares a file with itself
    #:   passes on nothing, which is worse than no arm.*
    if pre == cur:
        raise SystemExit('  ⛔ this revision has not changed the instrument: there is nothing to '
                         'measure, and an arm that passes on nothing is worse than no arm.')
    io.open(PRE, 'wb').write(pre)
    rec = {'differ_in_source': True,
           'landed_has_no_switch': b'NUHIER' not in pre,
           'patched_has_switch': cur.count(b'NUHIER = os.environ.get') == 1}
    #: ⚑ WHAT WAS SEARCHED, beside the claim: not a grep of the working tree but the whole of
    #: `origin/main`'s OWN BYTES for this instrument, read at source into `pre` above and tested
    #: for the switch's name over every byte of it.  The search is the file, not a recollection.
    print('  the landed instrument carries no such switch: %s'
          '  (searched: every one of the %d bytes of origin/main\'s own copy of this instrument,'
          ' read at source, for the name NUHIER)'
          % (rec['landed_has_no_switch'], len(pre)))
    try:
        tmp = tempfile.mkdtemp(prefix='r7882_arms_')
        try:
            # ── ① off, both ways ────────────────────────────────────────────────────────────────
            rec['off_rows'] = {}
            for tag, extra in (('absent', None), ('zero', dict(NUHIER='0'))):
                for label, script in (('landed', PRE), ('patched', CUR)):
                    rc, out = one(script, os.path.join(tmp, '%s_%s' % (tag, label)), extra)
                    if rc != 0:
                        raise SystemExit('  ⛔ %s/%s failed rc=%d:\n%s'
                                         % (tag, label, rc, out[-1200:]))
                ok, rows = same('%s_landed' % tag, '%s_patched' % tag, tmp)
                rec['off_rows'][tag] = rows
                print('  ① off (%s): every array identical: %s' % (tag, ok))
            rec['off_identical'] = all(r[b]['arrays_identical']
                                       for r in rec['off_rows'].values() for b in ('tt', 'pol'))
            # ── ② the previous revision's switch, untouched ─────────────────────────────────────
            _on = dict(NUPERT='1')
            for label, script in (('landed', PRE), ('patched', CUR)):
                rc, out = one(script, os.path.join(tmp, 'fluid_%s' % label), _on)
                if rc != 0:
                    raise SystemExit('  ⛔ fluid/%s failed rc=%d:\n%s' % (label, rc, out[-1200:]))
            ok, rows = same('fluid_landed', 'fluid_patched', tmp)
            rec['fluid_rows'], rec['fluid_identical'] = rows, bool(ok)
            print('  ② the fluid approximation at its defaults: bit-identical: %s' % ok)
            # ── ③ the refusals ──────────────────────────────────────────────────────────────────
            rec['refusals'] = {}
            for name, env in REFUSALS.items():
                rc, out = one(CUR, os.path.join(tmp, 'ref'), env)
                msg = [l for l in out.splitlines() if '⛔' in l]
                rec['refusals'][name] = {'rc': rc, 'refused': rc != 0,
                                         'message': (msg[0].strip() if msg else out[-200:])}
                print('  ③ %-32s rc=%d %s' % (name, rc, 'REFUSES' if rc != 0 else '** RAN **'))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    finally:
        if os.path.exists(PRE):
            os.remove(PRE)
    rec['all_pass'] = bool(rec['off_identical'] and rec['fluid_identical']
                           and rec['landed_has_no_switch'] and rec['patched_has_switch']
                           and all(v['refused'] for v in rec['refusals'].values()))
    print('\n  ⇒ %s' % ('all three arms pass' if rec['all_pass']
                        else '** NOT ALL THREE PASS -- the switch is not ready to be read **'))
    json.dump(rec, io.open(os.path.join(_HERE, 'switch_arms.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote switch_arms.json')
    return 0 if rec['all_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
