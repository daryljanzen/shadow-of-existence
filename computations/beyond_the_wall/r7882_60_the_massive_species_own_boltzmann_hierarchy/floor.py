# -*- coding: utf-8 -*-
"""r7882+60 arm Ⓠ⓸ᵃ — IS THE FLOOR UNDER THE MASSLESS LIMIT THE QUADRATURE'S?

`PREDICTION.md`'s declared amendment: *"re-run the same comparison at `NQ` doubled to `24`, mass
decade unchanged: the worst relative difference must fall by at least a factor `3` AND stay flat
across the decade to within a factor `2`."*

⛔ *WHY THIS ARM EXISTS.  `limit.py` reports the massless-limit residual as FLAT across a decade in
  the sum, and reads that flatness as a failure.  But a flat residual is exactly what a
  MASS-INDEPENDENT error looks like, and there is one in the comparison by construction: the
  massless map `Psi_l = -g M_l / 4` is inverted by a FINITE quadrature, so the on-against-off
  difference carries the `q`-grid's own representation error, which depends on `NQ` and not on the
  mass.  A shrink test cannot tell that floor from a defect.  Doubling the nodes can: the grid's
  error falls with the nodes and a residual defect does not.*

⌗ NOT RETYPED: the leg runner is `r7878`'s `one`, and the array comparison is `limit.py`'s own
  `worst_per_array`, imported.

    NODE=60 python3 floor.py
"""
import io
import json
import os
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7878 = os.path.join(_BTW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic'
                            '_sound_speed')
#: ⛔ *_R7878 goes in FRONT of _HERE: this directory has its OWN `switch_arms.py` and it would
#: otherwise shadow `r7878`'s, which is the one `one` lives in.  `limit` exists only here, so it is
#: still found.*
sys.path.insert(0, _HERE)
sys.path.insert(0, _R7878)
from switch_arms import one                                                     # noqa: E402
from limit import SUMS, CUR, worst_per_array                                    # noqa: E402

NODES = (12, 24)                 # the landed grid, and the same grid doubled
FALL = 3.0                       # the registered factor the floor must fall by
FLAT = 2.0                       # and the factor within which it must stay mass-independent


def main():
    print(__doc__)
    print('=' * 100)
    rec = {'nodes': {}, 'FALL': FALL, 'FLAT': FLAT}
    tmp = tempfile.mkdtemp(prefix='r7882_floor_')
    for nq in NODES:
        worst = {}
        for sm in SUMS:
            for tag, extra in (('off', dict(MNU=sm, NQ=str(nq))),
                               ('on', dict(MNU=sm, NQ=str(nq), NUHIER='1'))):
                rc, out = one(CUR, os.path.join(tmp, '%s_%s' % (sm, tag)), extra)
                if rc != 0:
                    raise SystemExit('  ⛔ NQ=%d %s/%s failed rc=%d:\n%s'
                                     % (nq, sm, tag, rc, out[-1500:]))
            row = worst_per_array(tmp, sm)
            worst[sm] = max(row.values())
        rec['nodes'][str(nq)] = worst
        print('\n  NQ = %d:  worst relative difference  %.3e at Sigma = %s,  %.3e at %s'
              % (nq, worst[SUMS[0]], SUMS[0], worst[SUMS[1]], SUMS[1]))

    lo, hi = (rec['nodes'][str(n)] for n in NODES)
    #: the two statements the arm makes, computed rather than eyeballed
    rec['fall'] = dict((sm, (lo[sm] / hi[sm]) if hi[sm] else None) for sm in SUMS)
    rec['flat'] = dict((str(n), (max(rec['nodes'][str(n)].values())
                                 / min(rec['nodes'][str(n)].values()))
                        if min(rec['nodes'][str(n)].values()) else None) for n in NODES)
    rec['fell'] = bool(all(rec['fall'][sm] is not None and rec['fall'][sm] >= FALL
                           for sm in SUMS))
    rec['stayed_flat'] = bool(all(rec['flat'][str(n)] is not None
                                  and rec['flat'][str(n)] <= FLAT for n in NODES))
    print('\n  the floor FELL by      %s  (registered: >= %.1f at BOTH sums)'
          % ('  '.join('%.1fx at %s' % (rec['fall'][sm], sm) for sm in SUMS), FALL))
    print('  and it stayed flat to  %s  (registered: <= %.1f at BOTH node counts)'
          % ('  '.join('%.2fx at NQ=%d' % (rec['flat'][str(n)], n) for n in NODES), FLAT))
    if rec['fell'] and rec['stayed_flat']:
        rec['verdict'] = 'the floor is the quadrature grid'
        print('\n  ⇒ ** ARM Ⓠ⓸ᵃ MET -- the floor under the massless limit is the q-grid\'s own')
        print('       representation error, it is NOT the mass and it is NOT a defect, so a shrink')
        print('       test cannot read this gate.  Ⓠ⓸ is read on Ⓠ⓸ᵇ. **')
    elif not rec['fell']:
        rec['verdict'] = 'the floor is NOT the quadrature grid'
        print('\n  ⇒ ** ARM Ⓠ⓸ᵃ NOT MET -- the floor does not fall with the nodes, so something')
        print('       mass-independent is still wrong in the hierarchy.  Ⓠ⓸ FAILS and no')
        print('       validation number is read. **')
    else:
        rec['verdict'] = 'the floor fell but became mass-dependent'
        print('\n  ⇒ ** ARM Ⓠ⓸ᵃ NOT MET -- the floor fell but is now mass-DEPENDENT, so the mass')
        print('       term is entangled with the grid.  That is its own defect, reported as one,')
        print('       and no validation number is read. **')
    rec['met'] = bool(rec['fell'] and rec['stayed_flat'])
    json.dump(rec, io.open(os.path.join(_HERE, 'floor.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote floor.json')
    return 0 if rec['met'] else 1


if __name__ == '__main__':
    sys.exit(main())
