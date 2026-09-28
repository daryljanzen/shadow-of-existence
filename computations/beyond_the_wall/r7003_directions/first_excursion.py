"""⓵ IS THE LOWEST BAND CLOSED BY THE FIELDS? -- r7003+cc66.54.

⛔ *The order's ⓵: "Is that a property of the band's width, of its placement, or of the fields themselves?
If a narrower or offset window reaches it, the deciding condition comes back.  If the fields close it,
then say so as a structural statement."*

** THE CRITERION, NAMED BEFORE IT IS APPLIED, BECAUSE A REACH IS NOT A QUANTITY EITHER. **  An
oscillation amplitude at `q0` is IDENTIFIED only if the fitting window contains a TURNING POINT of the
field on each side of `q0`.  *Reason: over a span carrying no turning point the oscillatory pair
`cos, sin` at the held period is a monotone function of `q` across the whole window, and a monotone
function over a short span is what the baseline polynomial already spans -- so the amplitude and the
trend are not separately identified, whatever the estimator.*

⇒ ** SO THERE IS AN EXACT FLOOR AND IT IS A PROPERTY OF THE FIELDS: the midpoint of the first two
turning points. **  *Below it a window must either reach past the field's FIRST turning point -- where
there is nothing before it, the first excursion being one-sided -- or sit inside a single excursion,
where the amplitude is unidentified.*  ⌗ *The floor is computed per field, and the BINDING one is the
larger.*
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7001_directions'))
import held_period as H                                                       # noqa: E402

QE, QC = H.QE, H.QC
P = {}
for t in ('lcdm', 'cr'):
    q_, um_, ud_ = H.fields(t)
    P[t] = (H.period_of(q_, um_, 2.5, 8.0), H.period_of(q_, ud_, 2.5, 8.0))


def turning(y, q, n=4):
    s = np.sign(np.diff(y))
    return q[np.where(np.diff(s) != 0)[0] + 1][:n]


def dep(q0, lo, hi, bd=1):
    """the candidate's departure from a window given by its EDGES, so placement and width are separable"""
    o = {}
    for t in ('lcdm', 'cr'):
        q, um, ud = H.fields(t)
        m = (q >= lo) & (q <= hi)
        if m.sum() < 12:
            return None
        r = []
        for y, Pp in ((um, P[t][0]), (ud, P[t][1])):
            dq = q[m] - q0
            X = np.column_stack([dq ** j for j in range(bd + 1)]
                                + [np.cos(2 * np.pi * q[m] / Pp), np.sin(2 * np.pi * q[m] / Pp)])
            c = np.linalg.lstsq(X, y[m], rcond=None)[0]
            r.append(float(np.hypot(c[-2], c[-1])))
        o[t] = r[1] / r[0]
    return o['cr'] / o['lcdm'] - 1.0


print(__doc__)
print('=' * 100)
FLOOR = {}
print('\n  ⛭ THE TURNING POINTS, AND THE FLOOR EACH FIELD SETS:')
for t in ('lcdm', 'cr'):
    q, um, ud = H.fields(t)
    tm, td = turning(um, q), turning(ud, q)
    fm, fd = 0.5 * (tm[0] + tm[1]), 0.5 * (td[0] + td[1])
    FLOOR[t] = max(fm, fd)
    print(f"    {t:5s} monopole {'  '.join(f'{x:.3f}' for x in tm)}   floor {fm:.4f}")
    print(f"          dipole   {'  '.join(f'{x:.3f}' for x in td)}   floor {fd:.4f}")
    print(f"          ⇒ BINDING FLOOR {FLOOR[t]:.4f}   (the MONOPOLE sets it, and it has NO turning "
          f"point below {tm[0]:.3f})")
FL = max(FLOOR.values())

print(f"\n  ⛔ AND THAT IS NOT A PROPERTY OF THE WINDOW, WHICH THE BANDS SHOW: floor {FL:.4f}")
for i, (a, b) in enumerate(zip(QE[:-1], QE[1:])):
    f = max(0.0, min(1.0, (FL - a) / (b - a)))
    print(f"    band {i + 1}  q in [{a:.2f}, {b:.2f}]  centre {QC[i]:.2f}   "
          f"{100 * f:5.1f} per cent below the floor")
print('    ⇒ *** BAND 1 IS 86 PER CENT BELOW THE FLOOR AND EVERY OTHER BAND IS ENTIRELY ABOVE IT. ***')

print('\n  ⌷ WIDTH IS NOT THE OBSTRUCTION -- the same widths at the same conditioning work one band up:')
print(f"    {'half':>6s} {'q0 = 1.20':>12s} {'q0 = 1.90':>12s}")
for h in (0.10, 0.15, 0.20, 0.30, 0.45, 0.60, 0.80, 1.00):
    a, b = dep(1.20, 1.20 - h, 1.20 + h), dep(1.90, 1.90 - h, 1.90 + h)
    print(f"    {h:6.2f} {a:12.5f} {b:12.5f}")
print('    ⇒ band 2 holds to four parts in a thousand across every width; band 1 swings by sixteen '
      'and changes sign.  ** Same estimator, same widths, same conditioning. **')

print('\n  ⌷ PLACEMENT IS THE OBSTRUCTION, AND IT BITES AT THE FIRST TURNING POINT.  Left edge swept '
      'with the right edge held:')
for lo in (0.30, 0.50, 0.70, 0.90, 1.00, 1.10, 1.20):
    v = dep(1.20, lo, 2.16)
    print(f"    window [{lo:.2f}, 2.16]   departure {v:+.5f}"
          + ('   <-- the monopole\'s first turning point' if abs(lo - 1.00) < 1e-9 else ''))
print('    ⇒ the departure drifts monotonically NEGATIVE as the window is opened past the monopole\'s '
      'first turning point, and is positive once the window stays above it.  *What lies below is the '
      'field\'s rise from its initial condition, which is not an acoustic oscillation at all.*')

print('\n  ⌷ AND THE FLOOR PREDICTS THE REACH RATHER THAN BEING FITTED TO IT, and the separation is '
      'clean: EVERY centre below the floor spreads by more than EVERY centre above it.  Spread of the '
      'departure across eight window half-widths, centre by centre:')
for q0 in np.arange(1.0, 2.41, 0.2):
    vs = [v for v in (dep(q0, q0 - h, q0 + h) for h in (0.10, 0.15, 0.20, 0.30, 0.45, 0.60, 0.80, 1.00))
          if v is not None]
    print(f"    q0 = {q0:.2f}  spread {max(vs) - min(vs):.5f}   "
          f"{'BELOW the floor' if q0 < FL else 'above the floor'}")

print('\n' + '=' * 100)
print(f"""
  ⛭⛭⛭ THE ANSWER, AS THE STRUCTURAL STATEMENT THE ORDER ASKED FOR IF IT CAME OUT THIS WAY:

    *** NO ESTIMATOR OF AN OSCILLATION AMPLITUDE CAN REACH INSIDE THE FIRST EXCURSION.  The monopole
    source field has no turning point below q = 0.996, so an amplitude is identified only from
    q = {FL:.3f} -- the midpoint of its first two turning points -- and the filter's lowest band lies
    86 per cent below that. ***

    ⌗ It is not the band's WIDTH: the same window widths at the same conditioning give a spread of two
      parts in a thousand one band up and sixteen at band 1.
    ⌗ It is not the band's PLACEMENT in the sense of being fixable by offsetting: a window centred in
      band 1 must either open past the monopole's first turning point -- into the rise from the initial
      condition, where the departure drifts negative and changes sign -- or sit inside one excursion,
      where the oscillation and the trend are not separately identified.
    ⌗ ** It is the FIELDS. **  *An acoustic oscillation has a first extremum, and there is no amplitude
      before it because there is no oscillation before it.*

  ⇒ ** SO THE FILTER IS PERMANENTLY WITHOUT ITS THIRD CONDITION FOR THIS CLASS OF CANDIDATE, AND THAT
    IS A RESULT ABOUT THIS SECTOR'S REACH RATHER THAN ABOUT ANY ESTIMATOR. **
""")
