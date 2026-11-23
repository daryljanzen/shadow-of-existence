#!/usr/bin/env python3
r"""r7861+cc66 item ⑥ -- ** THE CALIBRATED REFERENCE'S FULL PROFILE, WHERE 60 CAN READ IT, AND CAMB's
`rdrag` ACROSS 60's OWN GRID. **

⛔ ** NOTHING IS RE-FITTED HERE. **  `r7853`'s profile already banked every field the order asks for,
one checkpoint per `(mode, sum)`, and re-running the fit would publish numbers that are not the ones
the landed `54.00` and `30.56` meV limits came from.  This assembles them and says so.

** WHAT IS COMPUTED: ** CAMB's drag-epoch sound horizon at `60`'s control and at each of `60`'s eight
grid displacements, read off their own `gen_pol_batched.sh` rather than guessed:
`lcdm` at `H0 = 67.40`, `Om = 0.3150`, `wb = 0.0224`, `ns = 0.965`, steps `2.0 / 0.0150 / 0.0008 /
0.020`; and the `cr` control beside it, since the grid carries both arms.
  ⌗ `60`'s grid is a STAR, not a box, so it has no corners in the literal sense.  The order's sense
  is the ends of the ruler's range, so every displacement is evaluated and the two EXTREMES are
  named.

Usage: python3 -I bank_calibrated_profile.py
Writes calibrated_profile.json and rdrag_grid.json beside this file.
"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# ⛔ THREE directory steps, not two: `HERE` is `<root>/computations/beyond_the_wall/<rev>`.  Two
#   steps lands on `computations/` and every path below it comes out doubled -- the same defect
#   `60`'s sweep hit at `r7858` and this seat hit again in its own audit today.  The assertion under
#   this line is what caught it both times, which is why it is an assertion and not care.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT5 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference', 'out5')
assert os.path.isdir(OUT5), f'the r7853 checkpoints must be on disk: {OUT5}'

# ** 60's grid, off `gen_pol_batched.sh` lines 18-20 -- not retyped from memory. **
GEN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness_does_not_'
                   'have', 'gen_pol_batched.sh')


def _gen_values():
    """the grid's own centres and steps, parsed out of 60's generator"""
    src = open(GEN).read()
    want = ('CR_H0', 'CR_OM', 'CR_WB', 'CR_NS', 'LC_H0', 'LC_OM', 'LC_WB', 'LC_NS',
            'S_H0', 'S_OM', 'S_WB', 'S_NS')
    out = {}
    for tok in src.replace('\n', ';').split(';'):
        tok = tok.strip()
        for w in want:
            if tok.startswith(w + '='):
                out[w] = float(tok.split('=', 1)[1])
    missing = [w for w in want if w not in out]
    if missing:
        raise SystemExit(f'⛔ REFUSED: 60\'s generator does not define {missing} -- the grid cannot '
                         f'be read, and inventing its steps would be worse than stopping')
    return out


G = _gen_values()
print(__doc__.split('Usage:')[0])
print('=' * 100)
print('  60\'s GRID, PARSED FROM THEIR OWN GENERATOR')
print('=' * 100)
print(f"      lcdm centre  H0 {G['LC_H0']:.4f}  Om {G['LC_OM']:.4f}  wb {G['LC_WB']:.4f}  "
      f"ns {G['LC_NS']:.4f}")
print(f"      cr   centre  H0 {G['CR_H0']:.4f}  Om {G['CR_OM']:.4f}  wb {G['CR_WB']:.4f}  "
      f"ns {G['CR_NS']:.4f}")
print(f"      steps        H0 {G['S_H0']:.4f}  Om {G['S_OM']:.4f}  wb {G['S_WB']:.4f}  "
      f"ns {G['S_NS']:.4f}")

# =================================================================================================
print()
print('=' * 100)
print('  ⑥ᵃ THE PROFILE, ASSEMBLED FROM `r7853`s OWN CHECKPOINTS -- READ, NOT RE-FITTED')
print('=' * 100)
ROWS = []
for p in sorted(glob.glob(os.path.join(OUT5, '*.json'))):
    d = json.load(open(p))
    d['checkpoint'] = os.path.basename(p)
    ROWS.append(d)
LIVE = [r for r in ROWS if not r['checkpoint'].startswith('cold_')]
COLD = [r for r in ROWS if r['checkpoint'].startswith('cold_')]
print(f"      {len(ROWS)} checkpoint(s): {len(LIVE)} on the warm-started profile, {len(COLD)} the "
      f"cold restarts the r7853 guard compared against")
BY = {}
for r in LIVE:
    BY.setdefault(r['mode'], []).append(r)
for m in sorted(BY):
    BY[m].sort(key=lambda r: r['sum'])

print()
print(f"      {'mode':8s} {'sum':>5s} {'total':>10s} {'dchi2':>8s} {'H0':>8s} {'Om':>7s} "
      f"{'omega_b':>8s} {'ns':>7s} {'tau':>7s} {'rd_used':>9s} {'rd_camb':>9s}")
for m in sorted(BY):
    base = min(r['total'] for r in BY[m])
    for r in BY[m]:
        print(f"      {m:8s} {r['sum']:5.2f} {r['total']:10.4f} {r['total'] - base:+8.4f} "
              f"{r['H0']:8.4f} {r['Om']:7.4f} {r['ombh2']:8.5f} {r['ns']:7.4f} {r['tau']:7.4f} "
              f"{r['rd_used']:9.4f} {r['rd_camb']:9.4f}")

# =================================================================================================
print()
print('=' * 100)
print('  ⑥ᵇ CAMB\'s DRAG-EPOCH SOUND HORIZON, AT 60\'s CONTROL AND ACROSS THEIR GRID')
print('=' * 100)
import camb                                                                   # noqa: E402


def rdrag(H0, Om, wb, ns):
    """CAMB's own `rdrag`.  Background and thermal history only -- no transfer is requested."""
    h2 = (H0 / 100.0) ** 2
    p = camb.set_params(H0=H0, ombh2=wb, omch2=Om * h2 - wb, mnu=0.0, omk=0.0,
                        tau=0.054, As=2.1e-9, ns=ns, WantTransfer=False, lmax=50)
    return float(camb.get_background(p).get_derived_params()['rdrag'])


PTS = [('lcdm control', G['LC_H0'], G['LC_OM'], G['LC_WB'], G['LC_NS']),
       ('H0p', G['LC_H0'] + G['S_H0'], G['LC_OM'], G['LC_WB'], G['LC_NS']),
       ('H0m', G['LC_H0'] - G['S_H0'], G['LC_OM'], G['LC_WB'], G['LC_NS']),
       ('OMp', G['LC_H0'], G['LC_OM'] + G['S_OM'], G['LC_WB'], G['LC_NS']),
       ('OMm', G['LC_H0'], G['LC_OM'] - G['S_OM'], G['LC_WB'], G['LC_NS']),
       ('WBp', G['LC_H0'], G['LC_OM'], G['LC_WB'] + G['S_WB'], G['LC_NS']),
       ('WBm', G['LC_H0'], G['LC_OM'], G['LC_WB'] - G['S_WB'], G['LC_NS']),
       ('NSp', G['LC_H0'], G['LC_OM'], G['LC_WB'], G['LC_NS'] + G['S_NS']),
       ('NSm', G['LC_H0'], G['LC_OM'], G['LC_WB'], G['LC_NS'] - G['S_NS']),
       ('cr control', G['CR_H0'], G['CR_OM'], G['CR_WB'], G['CR_NS'])]
RD = {}
print(f"      {'point':13s} {'H0':>8s} {'Om':>7s} {'omega_b':>8s} {'ns':>7s} {'rdrag/Mpc':>11s} "
      f"{'vs control':>11s}")
for name, h0, om, wb, ns in PTS:
    RD[name] = dict(H0=h0, Om=om, ombh2=wb, ns=ns, rdrag=rdrag(h0, om, wb, ns))
    d = RD[name]['rdrag'] - RD['lcdm control']['rdrag']
    print(f"      {name:13s} {h0:8.4f} {om:7.4f} {wb:8.5f} {ns:7.4f} {RD[name]['rdrag']:11.4f} "
          f"{d:+11.4f}")

_disp = [k for k in RD if k not in ('lcdm control', 'cr control')]
_hi = max(_disp, key=lambda k: RD[k]['rdrag'])
_lo = min(_disp, key=lambda k: RD[k]['rdrag'])
_rng = RD[_hi]['rdrag'] - RD[_lo]['rdrag']
_dwb = abs(RD['WBp']['rdrag'] - RD['WBm']['rdrag'])
_dom = abs(RD['OMp']['rdrag'] - RD['OMm']['rdrag'])
print()
print(f"      the two ENDS of the ruler over 60's grid: {_hi} at {RD[_hi]['rdrag']:.4f} and {_lo} "
      f"at {RD[_lo]['rdrag']:.4f}  -- range {_rng:.4f} Mpc")
print(f"      the levers: omega_b's step moves it {_dwb:.4f} Mpc, Om's step {_dom:.4f} Mpc")

json.dump(dict(grid=G, rdrag=RD, ends=dict(hi=_hi, lo=_lo, range_mpc=_rng),
               levers=dict(omega_b=_dwb, Om=_dom)),
          open(os.path.join(HERE, 'rdrag_grid.json'), 'w'), indent=1)
json.dump(dict(source='r7853 out5 checkpoints, assembled and NOT re-fitted',
               n_checkpoints=len(ROWS), n_live=len(LIVE), n_cold=len(COLD),
               profile={m: BY[m] for m in BY}, cold=COLD),
          open(os.path.join(HERE, 'calibrated_profile.json'), 'w'), indent=1)
print()
print(f"  written -> calibrated_profile.json, rdrag_grid.json")
