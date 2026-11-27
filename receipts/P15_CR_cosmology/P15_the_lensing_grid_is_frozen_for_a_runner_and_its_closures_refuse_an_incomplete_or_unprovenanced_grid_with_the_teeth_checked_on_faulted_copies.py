# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE LENSING GRID IS FROZEN FOR A RUNNER AND ITS CLOSURES REFUSE -- AN INCOMPLETE GRID, A
POINT THAT CANNOT SHOW WHAT IT IS, A BANDPOWER THAT DISAGREES WITH THIS CONTAINER'S, AND A FROZEN
LIST THAT HAS DRIFTED FROM THE COMMAND IT WAS READ OFF; AND THE TEETH ARE CHECKED BY PLANTING EACH
FAULT RATHER THAN BY ARGUING THAT THEY WOULD BITE.

COMPUTES: nothing physical. This is the handoff artefact order `r7885` (69) item ① asked for, and
what it pins is the SPECIFICATION: that the frozen point list is the landed generator's own numbers
rather than a transcription of them; that the provenance record it demands is exactly the record the
limit read's gate actually compares; that each of the five closures standing between a runner and a
`refs/ci` ref fires on a planted fault and does NOT fire on a perturbation inside its own registered
accept bar; and that the dispatch script is idempotent, resolves its output directory before it
changes directory, and has a dry-run mode.
** IT PINS AS RESULTS: ** the list is `10` points, five sums on each of two arms, with `lcdm` at
`67.40`/`0.3150`/`0.0224`/`0.965` and `cr` at `68.570730`/`0.291246`/`0.021643`/`1.015066`, every
one of those eight numbers read out of `r7884`'s generator and compared, not typed; the resolution
`NQ = 12`, `LMAXNU = 12`, `QMAXNU = 20`; the seven provenance switches, which are the same seven the
limit read's `Ⓛ⓹` compares; and the measured cost `2100` s of wall clock and `8189` s of CPU per
point on about `3.95` cores, which is what makes `JOBS=1` a measurement and not a preference.
⛔ ** AND IT PINS THAT THE CLOSURES HAVE TWO SIDES: ** a bandpower moved by `1e-05` turns the
cross-machine control RED in its registered refuse state, and a bandpower moved by `1e-11` -- inside
the registered accept bar -- leaves it GREEN. A control that refused everything would pass a
one-sided test and be worthless, so both directions are measured here.
⛔ ** AND IT PINS WHAT THIS REVISION IS NOT: ** no limit is read, no workflow is wired, and no job
split is chosen. The cost is stated so that `70` can choose one.

    python3 <this file>
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
D = os.path.join(BW, 'r7886_60_the_lensing_grid_launch_for_the_runner')
R7884 = os.path.join(BW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector')
GEN = os.path.join(R7884, 'gen_phiphi_nuhier.sh')
LIMITS = os.path.join(R7884, 'limits_nuhier.py')
FAILS = []
NARMS = 0


def text(p):
    with io.open(p, encoding='utf-8') as fh:
        return fh.read()


def flat(p):
    return ' '.join(text(p).split())


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


def verify(out, ref=None):
    """run the directory's own verifier and hand back its exit code and the labels that failed"""
    cmd = [sys.executable, os.path.join(D, 'verify_grid.py'), out]
    if ref:
        cmd += ['--ref', ref]
    r = subprocess.run(cmd, capture_output=True, cwd=BW)
    o = r.stdout.decode('utf-8', 'replace')
    failed = set(re.findall(r'FAILED: (Ⓒ[^\s]+)', o))
    state = re.search(r'=> (Ⓒ⓸[^\n]*)', o)
    return r.returncode, failed, (state.group(1) if state else ''), o


SPEC = json.load(io.open(os.path.join(D, 'points.json'), encoding='utf-8')) \
    if os.path.exists(os.path.join(D, 'points.json')) else {}
BANK = os.path.join(BW, 'bank', SPEC.get('out_dir_name', 'phiphi_grid'))

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE FROZEN LIST IS THE LANDED GENERATOR\'S OWN NUMBERS, NOT A TRANSCRIPTION OF THEM')

pts = SPEC.get('points', [])
bysum = {}
for p in pts:
    bysum.setdefault(p['arm'], set()).add(round(float(p['mnu']), 6))
check('Ⓐ① the frozen list is `10` points -- five sums on each of the two arms, the five the switch '
      'can run at',
      len(pts) == 10 and bysum.get('lcdm') == bysum.get('cr') == {0.06, 0.15, 0.3, 0.45, 0.6},
      '%d point(s); %s' % (len(pts), {k: sorted(v) for k, v in sorted(bysum.items())}))

GSRC = text(GEN)


def gennum(nm):
    m = re.search(r'\b%s=([0-9.]+)' % nm, GSRC)
    return m.group(1) if m else None


_pairs = [('CR_H0', 'cr', 'CRH0'), ('CR_OM', 'cr', 'CROM'), ('CR_WB', 'cr', 'WBH2'),
          ('CR_NS', 'cr', 'NS'), ('LC_H0', 'lcdm', 'LH0'), ('LC_OM', 'lcdm', 'LOM'),
          ('LC_WB', 'lcdm', 'WBH2'), ('LC_NS', 'lcdm', 'NS')]
_agree, _seen = 0, []
for nm, arm, key in _pairs:
    g = gennum(nm)
    vals = {p['env'].get(key) for p in pts if p['arm'] == arm}
    _seen.append('%s=%s' % (nm, g))
    if g is not None and vals == {g}:
        _agree += 1
check('Ⓐ② all EIGHT cosmological numbers in the frozen list are read out of `r7884`\'s generator '
      'and agree with it. ⌗ *`points.json` was GENERATED from that file rather than typed, which is '
      'why this arm can be an equality and not a tolerance*',
      _agree == 8, '%d of 8 agree: %s' % (_agree, ' '.join(_seen)))

_res = {k: {p['env'].get(k) for p in pts} for k in ('NQ', 'LMAXNU', 'QMAXNU', 'LMAXL', 'LSTEP')}
check('Ⓐ③ the resolution is the one `r7882`\'s convergence gates fixed and the order restated -- '
      '`NQ = 12`, `LMAXNU = 12`, `QMAXNU = 20` -- on every point, with the projection settings '
      'unchanged',
      _res['NQ'] == {'12'} and _res['LMAXNU'] == {'12'} and _res['QMAXNU'] == {'20'}
      and _res['LMAXL'] == {'2000'} and _res['LSTEP'] == {'8'},
      '%s' % {k: sorted(v) for k, v in sorted(_res.items())})

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE PROVENANCE DEMANDED HERE IS THE RECORD THE LIMIT READ ACTUALLY COMPARES')

NEED = SPEC.get('provenance_required', {})
LSRC = text(LIMITS)
_l5 = LSRC[LSRC.index('Ⓛ⓹'):] if 'Ⓛ⓹' in LSRC else ''
_read_by_gate = {k for k in ('NUHIER', 'NQ', 'LMAXNU', 'QMAXNU') if "sw.get('%s')" % k in _l5}
check('Ⓑ① the four switches the limit read\'s `Ⓛ⓹` compares are all demanded by this frozen '
      'specification, read off that gate\'s own source rather than assumed to match',
      _read_by_gate == {'NUHIER', 'NQ', 'LMAXNU', 'QMAXNU'}
      and _read_by_gate <= set(NEED),
      'gate reads %s; spec demands %s' % (sorted(_read_by_gate), sorted(NEED)))

check('Ⓑ② and the specification demands THREE MORE than that gate does -- the background switch, '
      'the Fermi-Dirac switch and the primordial normalisation -- so a point records which object '
      'it is and not only which hierarchy settings it ran',
      {'BVEL', 'NUFD', 'PRIMNORM'} <= set(NEED) and len(NEED) == 7,
      '%d key(s): %s' % (len(NEED), sorted(NEED)))

_banked = sorted(f[:-5] for f in os.listdir(BANK)
                 if f.endswith('.json')) if os.path.isdir(BANK) else []
_ok = 0
for k in _banked:
    sw = json.load(io.open(os.path.join(BANK, k + '.json'), encoding='utf-8')).get('switches', {})
    if all(str(sw.get(a)) == str(b) for a, b in NEED.items()):
        _ok += 1
check('Ⓑ③ and every point banked in this checkout carries all seven, so the demand is met by the '
      'artefacts and not only stated in a file',
      bool(_banked) and _ok == len(_banked), '%d of %d banked point(s)' % (_ok, len(_banked)))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE CLOSURES ARE REFUSALS, AND EACH ONE IS SHOWN TO FIRE BY PLANTING ITS FAULT')

_rc, _failed, _state, _out = verify(BANK)
_complete = len(_banked) == 10
check('Ⓒ① the verifier\'s verdict on the real grid matches the grid\'s actual state. ⛔ *Two states '
      'are enumerated because this grid is BEING FILLED: while it is short, `Ⓒ⓵` must be among the '
      'refusals; once it is whole, `Ⓒ⓵` must pass. A receipt pinned to one of those would redden '
      'the moment the grid it describes was finished*',
      ('Ⓒ⓵' in _failed and _rc != 0) if not _complete else ('Ⓒ⓵' not in _failed),
      '%d banked => %s; rc=%d; failed %s'
      % (len(_banked), 'INCOMPLETE, refusal required' if not _complete else 'COMPLETE, must pass',
         _rc, sorted(_failed) or 'none'))

check('Ⓒ② with the grid as it stands, the provenance, shape and no-drift closures all PASS, so the '
      'refusal above is the completeness one alone and not a verifier that refuses everything',
      not ({'Ⓒ⓶', 'Ⓒ⓷', 'Ⓒ⓹'} & _failed), 'failed %s' % (sorted(_failed) or 'none'))

_tmp = tempfile.mkdtemp(prefix='r7886_teeth_')
try:
    # tooth one: a point that cannot show what it is
    t1 = os.path.join(_tmp, 'drop')
    shutil.copytree(BANK, t1)
    _f = sorted(f for f in os.listdir(t1) if f.endswith('.json'))[0]
    _j = json.load(io.open(os.path.join(t1, _f), encoding='utf-8'))
    _j['switches'].pop('NQ', None)
    json.dump(_j, io.open(os.path.join(t1, _f), 'w', encoding='utf-8'), indent=1, sort_keys=True)
    _rc1, _fail1, _s1, _ = verify(t1, ref=BANK)
    check('Ⓒ③ TOOTH -- drop ONE switch from ONE point\'s record and the provenance closure turns '
          'red, naming the point and the key',
          'Ⓒ⓶' in _fail1, 'failed %s' % sorted(_fail1))

    # tooth two: a bandpower outside the registered report bar
    t2 = os.path.join(_tmp, 'far')
    shutil.copytree(BANK, t2)
    _j2 = json.load(io.open(os.path.join(t2, _f), encoding='utf-8'))
    _j2['bandpowers'][3] *= (1.0 + 1e-05)
    json.dump(_j2, io.open(os.path.join(t2, _f), 'w', encoding='utf-8'), indent=1, sort_keys=True)
    _rc2, _fail2, _s2, _ = verify(t2, ref=BANK)
    check('Ⓒ④ TOOTH -- move ONE bandpower by `1e-05`, outside the registered report bar, and the '
          'cross-machine control turns red IN ITS REGISTERED REFUSE STATE',
          'Ⓒ⓸' in _fail2 and 'REFUSED' in _s2, 'failed %s; state %r' % (sorted(_fail2), _s2))

    # the OTHER side: a perturbation inside the accept bar must NOT fire
    t3 = os.path.join(_tmp, 'near')
    shutil.copytree(BANK, t3)
    _j3 = json.load(io.open(os.path.join(t3, _f), encoding='utf-8'))
    _j3['bandpowers'][3] *= (1.0 + 1e-11)
    json.dump(_j3, io.open(os.path.join(t3, _f), 'w', encoding='utf-8'), indent=1, sort_keys=True)
    _rc3, _fail3, _s3, _ = verify(t3, ref=BANK)
    check('Ⓒ⑤ AND THE OTHER SIDE -- move a bandpower by `1e-11`, INSIDE the registered accept bar, '
          'and the control does NOT fire. ⛔ *A control that refused every perturbation would pass '
          'Ⓒ④ and be worthless; this is the arm that separates a gate from a tripwire*',
          'Ⓒ⓸' not in _fail3 and 'ACCEPTED' in _s3, 'failed %s; state %r' % (sorted(_fail3), _s3))

    # tooth three: the frozen list drifting from the command it was read off
    t4 = os.path.join(_tmp, 'drift')
    os.makedirs(t4)
    _d4 = json.loads(json.dumps(SPEC))
    for p in _d4['points']:
        if p['arm'] == 'lcdm':
            p['env']['LH0'] = '67.41'
    io.open(os.path.join(D, 'points.json.bak'), 'w', encoding='utf-8').write(
        json.dumps(SPEC, indent=1, sort_keys=True) + '\n')
    io.open(os.path.join(D, 'points.json'), 'w', encoding='utf-8').write(
        json.dumps(_d4, indent=1, sort_keys=True) + '\n')
    try:
        _rc4, _fail4, _s4, _ = verify(BANK)
    finally:
        shutil.move(os.path.join(D, 'points.json.bak'), os.path.join(D, 'points.json'))
    check('Ⓒ⑥ TOOTH -- move ONE cosmological number in the frozen list away from the generator\'s '
          'and the no-drift closure turns red, so the list cannot silently diverge from the command '
          'it was read off',
          'Ⓒ⓹' in _fail4, 'failed %s' % sorted(_fail4))
finally:
    shutil.rmtree(_tmp, ignore_errors=True)

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  THE DISPATCH SCRIPT: IDEMPOTENT, ABSOLUTE BEFORE IT MOVES, AND DRY-RUNNABLE')

LSH = os.path.join(D, 'launch.sh')


def launch(env_extra, cwd=BW):
    e = dict(os.environ, **env_extra)
    r = subprocess.run(['bash', LSH], capture_output=True, cwd=cwd, env=e)
    return r.stdout.decode('utf-8', 'replace')

_rel = os.path.relpath(BANK, BW)
_o1 = launch({'PPOUT': _rel, 'ONLY': _banked[0] if _banked else 'lcdm_S006'})
#: ⛭ re-count AFTER the call, and accept either count: a point may land between the two reads while
#:   the grid is being filled on this machine.  Pinning the number read at import would make this arm
#:   lose a race rather than measure the defect.
_now = len([f for f in os.listdir(BANK) if f.endswith('.json')]) if os.path.isdir(BANK) else 0
_said = re.search(r'(\d+) of 10 banked', _o1)
check('Ⓓ① a RELATIVE output directory is resolved BEFORE the script changes directory, so the skip '
      'test and the count look in the right place. ⛔ *This was a live defect: after the `cd` a '
      'relative path resolved elsewhere, an already-banked point would have been re-run, and the '
      'tail line said "0 of 10 banked" with the points on disk*',
      ('skip %s' % (_banked[0] if _banked else '')) in _o1
      and _said is not None and int(_said.group(1)) in (len(_banked), _now),
      'through %r it counted %s, the directory holds %d'
      % (_rel, _said.group(1) if _said else None, _now))

check('Ⓓ② and it ran NOTHING in that invocation, because the only point selected was already '
      'banked -- which is what idempotent means here',
      '0 point(s) run this invocation' in _o1)

_tmp2 = tempfile.mkdtemp(prefix='r7886_dry_')
try:
    _o2 = launch({'PPOUT': _tmp2, 'MAXP': '0'})
    check('Ⓓ③ `MAXP=0` is a genuine DRY RUN: it names the point it would run next and runs none, so '
          'the wiring can be checked without spending the `35` minutes a point costs',
          'would run' in _o2 and '0 point(s) run this invocation' in _o2
          and not [f for f in os.listdir(_tmp2) if f.endswith('.json')],
          '%r' % [l.strip() for l in _o2.splitlines() if 'would run' in l])
finally:
    shutil.rmtree(_tmp2, ignore_errors=True)

_lsh = text(LSH)
check('Ⓓ④ and the dispatch calls the LANDED driver rather than carrying a copy of it: the point '
      'driver it invokes is `r7846`\'s, named in the frozen specification',
      'phiphi_point.py' in _lsh and 'r7846' in _lsh and 'r7846' in SPEC.get('driver', ''),
      SPEC.get('driver', '').split('/')[-2][:46])

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE COST IS THE MEASURED ONE, WHICH IS WHAT MAKES `JOBS=1` A MEASUREMENT')

C = SPEC.get('cost_per_point', {})
check('Ⓔ① the frozen specification carries the MEASURED per-point cost -- `2100` s of wall clock '
      'and `8189` s of CPU on about `3.95` cores -- and `1` job per run beside it',
      C.get('wall_seconds') == 2100 and C.get('cpu_seconds') == 8189
      and abs(float(C.get('cores_used', 0)) - 3.95) < 5e-03
      and SPEC.get('jobs_per_run') == 1,
      '%s, jobs_per_run=%s' % (C, SPEC.get('jobs_per_run')))

check('Ⓔ② and the cost implies the job limit matters: ten points at that wall time is over five '
      'hours, which is why the specification tells `70` to split the list rather than assume one '
      'job holds it',
      10 * float(C.get('wall_seconds', 0)) > 5 * 3600
      and ('ONLY' in _lsh and 'MAXP' in _lsh),
      '%.1f h for ten points sequentially' % (10 * float(C.get('wall_seconds', 0)) / 3600.0))

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  WHAT IS NOT CLAIMED, WRITTEN DOWN')

RES = flat(os.path.join(D, 'RESULT.md'))
check('Ⓕ① the record states that no limit is read in this revision, so the handoff cannot be read '
      'as having produced one',
      '**No limit is read.** That is item ②' in RES)

check('Ⓕ② and that the workflow is NOT wired here -- that is `70`\'s -- so this directory is a '
      'handoff and not a claim to have done `70`\'s part',
      'It does not wire the workflow' in RES)

check('Ⓕ③ and the two defects the closures\' own execution exposed are recorded rather than '
      'quietly fixed -- the gate that claimed more than it measured, and the miscount that would '
      'have been INVISIBLE on a runner where the output path happens to be absolute',
      'reported "`10` point(s)" when only `6` existed to examine' in RES
      and 'a RELATIVE `PPOUT` resolved wrong after the `cd`' in RES
      and 'invisible on a runner' in RES
      and 'Neither defect was visible in the source. Both took one execution.' in RES)

check('Ⓕ④ and the record carries BOTH sides of the control, the accept side marked as the row that '
      'matters most, so a reader cannot take the bite tests alone for a working gate',
      'inside* the accept bar | `Ⓒ⓸` | **GREEN**' in RES
      and 'only' in RES and 'they are not tripwires' in RES)

check('Ⓕ⑤ and the count the closures saw is written down as a TIMESTAMP rather than as the grid\'s '
      'state, so the record does not go stale as the remaining points land',
      'that figure is a TIMESTAMP, not a state' in RES)

check('Ⓕ⑥ ⛔ and the record states that `70` WIRED THE RUNNER FIRST, from the same generator, so this '
      'handoff is not claimed to be what unblocked it',
      'WIRED IT FIRST' in RES and 'about nine minutes before' in RES
      and 'was not what unblocked' in RES)

check('Ⓕ⑦ ⛔ and it states that `70`\'s per-point gate is a SUPERSET of three of these closures -- '
      '`21` recorded keys against `7` -- rather than presenting these as the stricter ones',
      'superset of `Ⓒ⓶`, `Ⓒ⓷` and `Ⓒ⓵` here' in RES and '`21` keys against my `7`' in RES)

check('Ⓕ⑧ ⛔ and it states that the no-drift closure is answered BETTER by `70` NOT HAVING ONE, '
      'because reading the generator at run time leaves no frozen copy to drift -- a point against '
      'this directory\'s own design, written down rather than left out',
      'is answered better by not existing' in RES)

check('Ⓕ⑨ and the three things that DO survive as additive are named and bounded, the first of them '
      'the one item ② actually turns on',
      'What survives as additive, and it is narrower than this directory' in RES
      and 'the tie from the provenance record to the limit read' in RES.lower()
      and 'item ① is largely redundant' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
