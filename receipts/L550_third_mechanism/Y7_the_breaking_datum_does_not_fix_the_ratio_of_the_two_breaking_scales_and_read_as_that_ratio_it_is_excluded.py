"""Y7 -- the construction's parity-breaking datum does not fix how far apart the two breaking scales
stand, and read directly as that ratio it is excluded by the right-handed W's absence.

Y6: the construction breaks P through one real P-odd number, the member's mass, whose field-theoretic
twin is a real P-odd singlet splitting the two Higgs doublets' masses oddly.  The lead: on the member
the cosmology is forced to, 2M/alpha = 2/(3 sqrt3); does that number fix v_L/v_R?

Computed here:
  (1) the forced (Nariai) member's mass in units of the one length, 2M/alpha = 2/(3 sqrt3) = 0.385, is the
      bound of the order parameter over the admissible offsets (P17), and its seam radius is
      r_N/alpha = 1/sqrt3: the construction's dimensionless parity-breaking data are of order one.
  (2) the measured side: with the right-handed W excluded below 6.4 TeV (ATLAS 2023) and, for a doublet
      H_R under exact P (g_R = g_L), m(W_R) = g v_R / 2, v_R > 2 m(W_R)/g = 19.7 TeV, so with v_L = 246 GeV
      the ratio v_L/v_R < 0.0125.
  (3) read directly as that ratio, 2M/alpha puts v_R at 639 GeV and m(W_R) at 208 GeV; its square at
      1.66 TeV and 540 GeV; r_N/alpha lower still -- each excluded, the first by a factor of 31 in the
      ratio.  CONTROL: the unifying minimal parity models' scale v_R ~ 1e10 GeV gives 2.5e-8 and passes.
  (4) and the geometry sets no energy that could stand in for either scale: every energy its own data
      form is a multiple of hbar c / alpha = 1.2e-33 eV (alpha = sqrt(3/Lambda)), 44 decades below v_L.

So the datum fixes the KIND of breaking (Y6) and not its SIZE: the ratio of the two vacuum values is
fixed where the left--right-symmetric models fix it, by their scalar potential, bounded below by the
collider and placed near 1e-8 by unification in the minimal models.

Bound: the readings tested in (3) are the direct ones (the datum, its square, the seam radius); a
function chosen to land inside the bound would be a fit, not a reading, and is not tested; g = 0.65 at
the TeV scale; the doublet relation m(W_R) = g v_R/2 (a triplet gives g v_R/sqrt2 and a bound on v_R
lower by sqrt2, which changes no verdict here).

COMPUTES: closed-form numbers at alpha = sqrt(3/Lambda), Lambda = 1.1056e-52 m^-2.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

V_L = 246.22          # GeV
M_WR_MIN = 6400.0     # GeV, ATLAS 2023
G = 0.65              # SU(2) coupling at the TeV scale
LAMBDA = 1.1056e-52   # m^-2
HBARC_EV_M = 1.9732698e-7


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def main():
    print()
    print('  Y7 -- the datum and the ratio of the two scales')
    print()
    two_m = 2 / (3 * math.sqrt(3))
    r_n = 1 / math.sqrt(3)
    u = [i / 10000 * 2 / math.sqrt(3) for i in range(-10000, 10001)]
    bound = max(abs(x - x ** 3) for x in u)
    check(f'(1) 2M/alpha on the forced member = {two_m:.4f}, the bound of |r0 - r0^3| over |r0| <= 2/sqrt3 '
          f'(scanned max {bound:.4f}); r_N/alpha = {r_n:.4f}', abs(bound - two_m) < 1e-6)

    vr_min = 2 * M_WR_MIN / G
    ratio_max = V_L / vr_min
    check(f'(2) v_R > 2 m(W_R)/g = {vr_min / 1e3:.1f} TeV, so v_L/v_R < {ratio_max:.4f}',
          abs(vr_min / 1e3 - 19.7) < 0.05 and abs(ratio_max - 0.0125) < 0.00005)

    readings = {'2M/alpha': two_m, '(2M/alpha)^2': two_m ** 2, 'r_N/alpha': r_n}
    out = []
    for name, x in readings.items():
        vr = V_L / x
        out.append((name, x, vr, G * vr / 2))
    check('(3) read as v_L/v_R: ' + '; '.join(f'{n} = {x:.3f} -> v_R {vr:.0f} GeV, m(W_R) {mw:.0f} GeV'
                                            for n, x, vr, mw in out)
          + f' -- all below {M_WR_MIN / 1e3:.1f} TeV; the first exceeds the bound on the ratio by {two_m / ratio_max:.0f}x',
          all(mw < M_WR_MIN for *_, mw in out) and [round(mw) for *_, mw in out] == [208, 540, 139]
          and round(two_m / ratio_max) == 31)
    hh = V_L / 1e10
    check(f'CONTROL (3): v_R ~ 1e10 GeV gives v_L/v_R = {hh:.1e}, inside the bound', hh < ratio_max and abs(hh - 2.5e-8) < 0.05e-8)

    alpha = math.sqrt(3 / LAMBDA)
    e_alpha = HBARC_EV_M / alpha
    dec = math.log10(V_L * 1e9 / e_alpha)
    check(f'(4) hbar c / alpha = {e_alpha:.2e} eV, {dec:.1f} decades below v_L', abs(e_alpha - 1.2e-33) < 0.05e-33 and abs(dec - 44.3) < 0.05)

    p = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the reading: "the datum does not fix how far apart the two breaking scales stand"',
          'the datum does not fix how far apart the two breaking scales stand' in p)
    check('P14 carries the number: "$2M/\\alpha=2/(3\\sqrt3)$ on the member the cosmology is forced to"',
          '$2M/\\alpha=2/(3\\sqrt3)$ on the member the cosmology is forced to' in p)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
