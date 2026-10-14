#!/usr/bin/env python3
"""Score the within-seat spread once both halves are read.  Nothing is pooled.

Expects, beside this file, one TSV per half:

    READ_half_A.tsv   # columns: receipt, literal, verdict, flag   (flag: FLAG or '')
    READ_half_B.tsv

and reports, per half and never pooled:

  * the OWEDNESS margin -- the fraction verdicted REPAIR-OWED, with a Wilson interval;
  * the FLAG margin -- the fraction carrying the judgement flag, likewise;
  * the SPREAD between halves on each margin, with a NEWCOMBE hybrid-score interval, which is
    `70`'s standing form.

Then it fires the registered refutation conditions by the numbers alone.
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
Z = 1.959963985  # 95 per cent, two-sided
# ⛔ r7323: the BAND and the POINT are WITHDRAWN -- kept here, not deleted, because the registration is
#   withdrawn in place.  A point of 16 sits inside its own 20.8-point half-width, so conditions ① and ②
#   below could not have been refuted by any result.  The registered quantity is now RECURRENCE, decided
#   on the interval; see PREREGISTRATION.md §R1.  Nothing this file COMPUTES changed.
BAND = (8.0, 24.0)          # WITHDRAWN at r7323
POINT = 16.0                # WITHDRAWN at r7323
SEVENTY = 30.0              # 70's measured within-unit owedness spread, the one-sided comparison point


def wilson(k, n):
    """Score interval for one proportion."""
    if n == 0:
        return 0.0, 0.0, 0.0
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return p, max(0.0, c - h), min(1.0, c + h)


def newcombe(k1, n1, k2, n2):
    """Hybrid score interval for p1 - p2 (Newcombe method 10)."""
    p1, l1, u1 = wilson(k1, n1)
    p2, l2, u2 = wilson(k2, n2)
    d = p1 - p2
    lo = d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return d, lo, hi


def read(half):
    p = os.path.join(HERE, f'READ_half_{half}.tsv')
    if not os.path.exists(p):
        return None
    rows = []
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        f = ln.rstrip('\n').split('\t')
        if len(f) < 3:
            continue
        rows.append((f[0], json.loads(f[1]), f[2].strip(),
                     (f[3].strip() if len(f) > 3 else '')))
    return rows


def margin(rows, which):
    if which == 'owed':
        k = sum(1 for _, _, v, _ in rows if v == 'REPAIR-OWED')
    else:
        k = sum(1 for _, _, _, g in rows if g.upper().startswith('FLAG'))
    return k, len(rows)


def main():
    a, b = read('A'), read('B')
    print()
    print('  WITHIN-SEAT SPREAD -- r7321+cc66, text 1a3c13a6, halves never pooled')
    # ⛔⛔ r7325: THE QUANTITY THIS FILE SCORES IS WITHDRAWN.  It computes a MARGIN between two agents
    #   reading DISJOINT halves, and r7325 item ① establishes that a reader arm needs pi_d, the share of
    #   keys whose two readings differ -- which disjoint halves cannot produce.  The arithmetic below is
    #   correct and its two repaired labels stand; what is withdrawn is that any verdict it prints
    #   answers the question.  Left runnable and unaltered, with the withdrawal printed, because the
    #   registration it serves is withdrawn IN PLACE and not edited out.
    print('  ⛔ THE QUANTITY BELOW IS WITHDRAWN AT r7325: a margin between DISJOINT halves cannot')
    print('     measure disagreement.  The figure that replaces it is pi_d, measured on this same')
    print('     frame from filed data in ../r7325_cc66_pi_d_between_pools/pi_d.py.')
    print()
    if a is None or b is None:
        missing = [h for h, r in (('A', a), ('B', b)) if r is None]
        print(f'  NOT YET READ: READ_half_{" and READ_half_".join(missing)}.tsv absent.')
        print('  The instrument is complete and the pre-registration is pushed; what is missing is')
        print('  the two fresh reads, which this seat may not perform -- see PREREGISTRATION.md.')
        return 2

    fired = []
    out = {}
    for name in ('owed', 'flag'):
        ka, na = margin(a, name)
        kb, nb = margin(b, name)
        pa, la, ua = wilson(ka, na)
        pb, lb, ub = wilson(kb, nb)
        d, lo, hi = newcombe(ka, na, kb, nb)
        out[name] = abs(d) * 100
        print(f'  {name.upper()} margin')
        print(f'    half A : {ka}/{na} = {pa:6.1%}   95% [{la:.1%}, {ua:.1%}]')
        print(f'    half B : {kb}/{nb} = {pb:6.1%}   95% [{lb:.1%}, {ub:.1%}]')
        print(f'    SPREAD : {abs(d) * 100:5.1f} points   Newcombe 95% '
              f'[{lo * 100:+.1f}, {hi * 100:+.1f}]')
        # ⛔ r7323: the old form of the second test was `not (lo <= 30 <= hi)`, a TWO-SIDED exclusion
        #   carrying a ONE-SIDED claim: at A 40/40 against B 0/38 the interval is [+87.3, +100.0] and the
        #   old line printed `excludes 30` for the widest spread the frame can hold.  Same shape as the
        #   disjunction defect this seat routed to 69 at r7315.  The arm that refutes 70's figure is the
        #   UPPER bound falling below it.
        # ⛔ r7323, SECOND repair, found by the same grid search as the first: `hi < 30` is a test on a
        #   SIGNED difference whose sign is a hash accident -- which half is A is arbitrary.  At
        #   A 16/40 against B 30/38 the difference is -38.9 points and `hi < 30` is TRIVIALLY true, so
        #   the widest spreads in the lower half of the frame would have read as refuting 70's figure.
        #   The claim is about the SIZE of the spread, so the bound must be on the magnitude: the
        #   largest |difference| the data allow at 95 per cent is max(|lo|, |hi|).
        clears = lo > 0 or hi < 0
        biggest = max(abs(lo), abs(hi)) * 100
        below = biggest < SEVENTY
        print(f'    {"clears zero" if clears else "DOES NOT clear zero"}; '
              f'largest |spread| the interval allows: {biggest:.1f} points, '
              f'{"BELOW 30" if below else "30 or more"}')
        if name == 'owed':
            verdict = ('RECURS BUT SMALLER THAN 70s' if clears and below
                       else 'RECURS' if clears
                       else "70s FIGURE REFUTED" if below
                       else 'INCONCLUSIVE')
            out['verdict'] = verdict
            out['clears'] = clears
            out['below'] = below
        print()

    o = out['owed']
    # r7323 §R4: the registered conditions.  ① and ② of the withdrawn band are NOT fired; they are
    #   printed below as withdrawn so the file shows what was replaced.
    if not out['clears'] and not out['below']:
        fired.append('1 the owedness interval contains both 0 and 30.0 -- INCONCLUSIVE, no claim either way')
    if out['clears']:
        fired.append(f'2 the owedness interval clears zero -- the spread RECURS at {o:.1f} points, and the '
                     'withdrawn band\'s compression argument is wrong')
    if out['below']:
        fired.append(f'3 the owedness interval\'s upper bound is below {SEVENTY} -- 70\'s figure does not '
                     'recur on this frame, and the reader arm sizes down')
    if out['flag'] <= o:
        fired.append(f'5 secondary refuted: flag spread {out["flag"]:.1f} <= owedness {o:.1f}')
    voided = []
    for h, rows in (('A', a), ('B', b)):
        k, n = margin(rows, 'owed')
        if n and not (0.40 <= k / n <= 0.80):
            voided.append(f'4 half {h} owed {k / n:.1%} outside 40-80% -- frame not reproducing')
    if voided:
        fired = voided + ['   ^ 4 VOIDS 1-3: a frame that is not reproducing has no spread to report']

    print(f'  REGISTERED QUANTITY: recurrence (r7323). owedness spread {o:.1f} points -> {out["verdict"]}')
    print(f'  withdrawn at r7323, shown not deleted: band {BAND[0]}-{BAND[1]}, point {POINT} '
          f'-- a point inside its own 20.8-point half-width')
    print(f'  refutation conditions fired: {len(fired)}')
    for f in fired:
        print(f'    - {f}')
    if not fired:
        print('    none -- which cannot happen under r7323: conditions 1, 2 and 3 partition the outcomes')
    return 0


if __name__ == '__main__':
    sys.exit(main())
