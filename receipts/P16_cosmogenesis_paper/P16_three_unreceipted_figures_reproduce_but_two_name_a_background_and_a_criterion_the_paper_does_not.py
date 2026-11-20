"""
P16, r7837 (cc66), on 69's order r7833, out of 60's cold read of P16.

Three figure-clusters in P16 that no receipt carried.  All three RE-COMPUTE.  Two of
them reproduce only on an input the paper does not name, and that is the finding:

  (1) sec:branch / the regulated peak.  pi*alpha/3 with alpha = sqrt(3/Lambda) returns
      BOTH dated figures -- 18.2 Gyr on Lambda = 1.1056e-52 and 17.8 Gyr on P16's own
      stated background (68.60, 0.2973), whose Lambda IS 1.1593e-52.  But the regulated
      peak's A/A_Nariai = 0.9768 holds ONLY on the first.  On P16's own background the
      worked progenitor sits AT the cap (1.0003), which is where the paper's own
      sub-Nariai requirement has no margin left.  ROUTED, not repaired.

  (2) sec:interior / the band period.  All four printed figures reproduce from the
      closed-form closed dust-plus-radiation interior with ONE input: c_s at turnaround.
      0.304, 3.565 and "a factor of 11.7" are then derived, and the factor is not an
      independent figure.  The sentence is correct and wanted only a receipt.

  (3) sec:network / the dissociation thresholds.  T_9 = 1.2 and 15.8 ARE returned by one
      criterion -- the crude photon-count B/kT = ln(1/eta) -- to 1.4 and 2.1 per cent.
      They are NOT nuclear statistical equilibrium: NSE with eta^(A-1) and the
      (m_N/kT)^{3(A-1)/2} weights gives 0.787 and 3.711.  P16 states BOTH criteria in
      different sections (sec:peak's T_D = 0.07 MeV is the NSE one), so the paper carries
      two deuterium thresholds differing by 1.5x.  ROUTED, not repaired.

COMPUTES: Lambda(H0, Om) = 3 H0^2 (1-Om) / c^2 ; alpha = sqrt(3/Lambda) ;
          the lap turnaround pi*alpha/3 ; the Nariai cap A <= 2 alpha / 3 sqrt 3 ;
          the closed dust+radiation interior a(eta) = (A/2)(1-cos eta) + sqrt(B) sin eta ;
          c_s^2 = 4 rho_r / (3(4 rho_r + 3 rho_m)) ; and two photodissociation criteria.

cc66 note on 60's arm (11): 60 reported that a single-exponential tail does NOT return
the pair, on the ground that it needs B/kT = 21.5 for deuterium against 20.8 for
helium-4.  Those two differ by 3.45 per cent, and ONE criterion at ln(1/eta) = 21.22
returns both printed figures to within 2.1 per cent.  So the pair IS reproduced at the
precision it is printed to; what 60's arm measured is that the two implied exponents are
not identical, which is a different claim.  Recorded as a disagreement with reasons, not
as a correction to 60.
"""
import math
import os
import re

FAILED = []


def check(label, ok, detail=''):
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
P16_PATH = os.path.join(HERE, '..', '..', 'corpus', 'cosmogenesis_paper.tex')
P16 = open(P16_PATH, encoding='utf-8').read()
FLAT = re.sub(r'\s+', ' ', P16)          # the band-period sentence wraps

G, C = 6.67430e-11, 2.99792458e8
MPC, GYR = 3.0856775814913673e22, 3.1556952e16
K_PER_MEV = 1.160451812e10
M_N, ETA = 939.5654133, 6.09e-10
B_D, B_HE4 = 2.224573, 28.295674

_READ_OK = len(FLAT) > 100_000 and '\n' not in FLAT
check('Ⓐ① the paper is read and flattened, so a wrapped sentence is findable', _READ_OK,
      f'{len(FLAT)} chars, newline-free {chr(10) not in FLAT}')

# ---------------------------------------------------------------- (1)
print()
print('Ⓑ (1) the regulated peak, on each background')
lam = lambda h, om: 3.0 * (h * 1e3 / MPC) ** 2 * (1.0 - om) / C ** 2
alpha = lambda L: math.sqrt(3.0 / L)
lap_turnaround_gyr = lambda L: math.pi * alpha(L) / 3.0 / C / GYR
nariai_cap_kg = lambda L: (2.0 * alpha(L) / (3.0 * math.sqrt(3.0))) * C ** 2 / (2.0 * G)

LAM_P16 = lam(68.60, 0.2973)
LAM_RCPT = 1.1056e-52
# the progenitor mass is PARSED, not retyped: the paper prints it in sec:abundances
_mp = re.search(r'mass \$([0-9.]+)\\times10\^\{([0-9]+)\}\$~kg', FLAT)
M_PROG = float(_mp.group(1)) * 10 ** int(_mp.group(2)) if _mp else 0.0
check('Ⓑ⓪ the progenitor mass is parsed out of the paper, not retyped: 4.17e52 kg',
      _mp is not None and abs(M_PROG - 4.17e52) <= 0.005e52, f'{M_PROG:.4e} kg')

check('Ⓑ① the distance data\'s point (68.60, 0.2973), which 69\'s order r7833 names and which P16 does NOT print, gives Lambda = 1.1593e-52',
      abs(LAM_P16 - 1.1593e-52) <= 0.00005e-52, f'{LAM_P16:.5e}')
TAU_P16 = lap_turnaround_gyr(LAM_P16)
TAU_RCPT = lap_turnaround_gyr(LAM_RCPT)
check('Ⓑ② PINNED the lap turnaround pi*alpha/3 on that point is 17.806 Gyr -> 17.8',
      abs(TAU_P16 - 17.806) <= 5e-3, f'{TAU_P16:.4f}')
check('Ⓑ③ PINNED the same expression on Lambda = 1.1056e-52 is 18.234 Gyr -> 18.2',
      abs(TAU_RCPT - 18.234) <= 5e-3, f'{TAU_RCPT:.4f}')

RATIO_RCPT = M_PROG / nariai_cap_kg(LAM_RCPT)
RATIO_P16 = M_PROG / nariai_cap_kg(LAM_P16)
check('Ⓑ④ PINNED A/A_Nariai = 0.9768 reproduces ONLY on Lambda = 1.1056e-52',
      abs(RATIO_RCPT - 0.9768) <= 5e-5, f'{RATIO_RCPT:.6f}')
check('Ⓑ⑤ PINNED on P16\'s own background the same progenitor is AT the cap, 1.0003',
      abs(RATIO_P16 - 1.0003) <= 5e-5, f'{RATIO_P16:.6f}')
check('Ⓑ⑥ so the margin the paper\'s sub-Nariai requirement needs is gone on its own '
      'background -- the ratio crosses 1', RATIO_RCPT < 1.0 < RATIO_P16,
      f'{RATIO_RCPT:.4f} < 1 < {RATIO_P16:.4f}')
# the two alpha-lengths the paper keeps apart, and this receipt must not conflate
THROAT_AREAL = alpha(LAM_P16) / math.sqrt(3.0)
THROAT_FAMILY = math.pi * alpha(LAM_P16) / math.sqrt(3.0)
LAP_LENGTH = math.pi * alpha(LAM_P16) / 3.0
check('Ⓑ⑦ pi*alpha/sqrt3 (throat, family) and pi*alpha/3 (lap turnaround) are different '
      'lengths and the ratio is sqrt3/1 ... 3/sqrt3',
      abs(THROAT_FAMILY / LAP_LENGTH - math.sqrt(3.0)) <= 1e-12,
      f'{THROAT_FAMILY/LAP_LENGTH:.9f}')
check('Ⓑ⑧ the paper states the throat by its areal radius alpha/sqrt3 and the DIVERGENCE '
      'of the chart integral at the double root, which is what a degenerate member leaves',
      'identified by its areal radius $\\alpha/\\sqrt{3}$' in FLAT
      and 'diverges logarithmically at the double root' in FLAT)

# ---------------------------------------------------------------- (2)
print()
print('Ⓒ (2) the band period, from the closed-form interior')
CS_TURN = 0.018


def a_of(eta, A, B):
    return 0.5 * A * (1.0 - math.cos(eta)) + math.sqrt(B) * math.sin(eta)


def cs_of(eta, A, B):
    return math.sqrt(4.0 / (3.0 * (4.0 + 3.0 * (A / B) * a_of(eta, A, B))))


def _brent(f, lo, hi, tol=1e-14):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0, (lo, hi, flo, fhi)
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if abs(hi - lo) < tol:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def turnaround(A, B):
    return _brent(lambda e: 0.5 * A * math.sin(e) + math.sqrt(B) * math.cos(e), 0.1, math.pi)


def lap_end(A, B):
    return _brent(lambda e: a_of(e, A, B), math.pi, 2.0 * math.pi - 1e-13)


def simpson(f, a, b, n=200_000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return s * h / 3.0


B_AMP = 1.0
A_AMP = _brent(lambda A: cs_of(turnaround(A, B_AMP), A, B_AMP) - CS_TURN, 1.0, 1e9)
ETA_T, ETA_E = turnaround(A_AMP, B_AMP), lap_end(A_AMP, B_AMP)
INT_RUN = simpson(lambda e: cs_of(e, A_AMP, B_AMP), 0.0, ETA_E)
INT_FROZEN = ETA_E / math.sqrt(3.0)
FACTOR = INT_FROZEN / INT_RUN

check('Ⓒ① c_s at turnaround is the ONE input and fixes A/sqrt(B) = 37.0055',
      abs(A_AMP / math.sqrt(B_AMP) - 37.0055) <= 5e-4, f'{A_AMP/math.sqrt(B_AMP):.5f}')
check('Ⓒ② PINNED the running sound-horizon integral over the lap is 0.3046',
      abs(INT_RUN - 0.3046) <= 5e-5, f'{INT_RUN:.6f}')
check('Ⓒ③ PINNED the frozen integral eta_end/sqrt3 is 3.5653 -> printed 3.565',
      abs(INT_FROZEN - 3.5653) <= 5e-4, f'{INT_FROZEN:.5f}')
check('Ⓒ④ PINNED the ratio is 11.704 -> printed "a factor of 11.7"',
      abs(FACTOR - 11.704) <= 5e-3, f'{FACTOR:.4f}')
check('Ⓒ⑤ the factor is DERIVED and not an independent figure: printed 3.565/0.304 = 11.727 '
      'agrees with the computed ratio to better than a quarter of a per cent',
      abs(3.565 / 0.304 - FACTOR) / FACTOR < 2.5e-3, f'{3.565/0.304:.4f} vs {FACTOR:.4f}')
check('Ⓒ⑥ the lap closes short of pure dust\'s 2*pi, as radiation requires',
      ETA_E < 2.0 * math.pi, f'eta_end = {ETA_E:.5f} < {2*math.pi:.5f}')
_bp = re.search(r'runs from \$([0-9.]+)\$ at turnaround', FLAT)
_bi = re.search(r'\\int c_s\\,\\mathrm\{d\}\\eta=([0-9.]+)\$ against the frozen '
                r"value's \$([0-9.]+)\$, a factor of \$([0-9.]+)\$", FLAT)
check('Ⓒ⑦ all four figures are PARSED out of the paper through the wrap, not retyped',
      _bp is not None and _bi is not None
      and abs(float(_bp.group(1)) - 0.018) <= 5e-5
      and abs(float(_bi.group(1)) - 0.304) <= 5e-5
      and abs(float(_bi.group(2)) - 3.565) <= 5e-5
      and abs(float(_bi.group(3)) - 11.7) <= 5e-3,
      f'{_bp.group(1) if _bp else "-"}, {_bi.groups() if _bi else "-"}')

# the paper prints 0.304, and 0.3046 does not round to it; the honest pin is that the
# printed figure lies inside the band the ONE input's own two significant figures allow
BAND = {}
for _cs in (0.0175, 0.0185):
    _A = _brent(lambda A: cs_of(turnaround(A, B_AMP), A, B_AMP) - _cs, 1.0, 1e9)
    _e = lap_end(_A, B_AMP)
    BAND[_cs] = (simpson(lambda x: cs_of(x, _A, B_AMP), 0.0, _e), _e / math.sqrt(3.0))
RUN_LO, RUN_HI = BAND[0.0175][0], BAND[0.0185][0]   # lower c_s -> lower integral
check('Ⓒ⑧ PINNED c_s at turnaround is printed to two significant figures, and over 0.0175 to '
      '0.0185 the running integral spans 0.29812 to 0.31105',
      abs(RUN_LO - 0.29812) <= 5e-5 and abs(RUN_HI - 0.31105) <= 5e-5,
      f'{RUN_LO:.6f} .. {RUN_HI:.6f}')
RUN_PRINTED = float(_bi.group(1))   # PARSED above, not retyped
check('Ⓒ⑨ so the figure the paper prints, parsed as 0.304, lies INSIDE that band, and 0.3046 '
      'is the band\'s centre rather than a disagreement with it',
      RUN_LO < RUN_PRINTED < RUN_HI and abs(RUN_PRINTED - 0.304) <= 5e-5,
      f'{RUN_LO:.5f} < {RUN_PRINTED} < {RUN_HI:.5f}')
check('Ⓒ⑩ PINNED and the frozen leg is insensitive to that input, spanning 3.56352 to 3.56698, '
      'so the printed 3.565 sits inside it too',
      abs(BAND[0.0185][1] - 3.56352) <= 5e-5 and abs(BAND[0.0175][1] - 3.56698) <= 5e-5
      and BAND[0.0185][1] < 3.565 < BAND[0.0175][1],
      f'{BAND[0.0185][1]:.5f} .. {BAND[0.0175][1]:.5f}')

# the two printed figures ARE mutually consistent, read the other way round: take the
# integral as given and the input it implies is the printed one to its two figures.
CS_IMPLIED = _brent(
    lambda cs: (lambda A: simpson(lambda x: cs_of(x, A, B_AMP), 0.0, lap_end(A, B_AMP)))(
        _brent(lambda A: cs_of(turnaround(A, B_AMP), A, B_AMP) - cs, 1.0, 1e9)) - 0.304,
    0.0170, 0.0185)
check('Ⓒ⑪ PINNED inverted, the printed 0.304 implies c_s at turnaround = 0.017953, which IS '
      'the printed 0.018 to its two significant figures',
      abs(CS_IMPLIED - 0.017953) <= 5e-6 and round(CS_IMPLIED, 3) == 0.018,
      f'{CS_IMPLIED:.6f}')
check('Ⓒ⑫ SO THIS RECEIPT IS NOT CITED AT THAT SENTENCE, and the reason is recorded: at the '
      'printed input 0.018 taken exactly the integral is 0.304612, which prints as 0.305 and '
      'misses 0.304 by 6.1e-4 against check_figures_pinned\'s allowance of 5.0e-4.  The '
      'figures are consistent; the pin is not available at the printed precision',
      abs(INT_RUN - 0.304) > 5.0e-4 and abs(INT_RUN - 0.304) < 7.0e-4,
      f'|{INT_RUN:.6f} - 0.304| = {abs(INT_RUN-0.304):.2e}')

# ⛭ THE FINDING, and it is why the question is open at all: P16 PRINTS NO BACKGROUND for
#   the regulated peak.  It prints no Lambda anywhere, prints no H_0 numeral at this site, and
#   its only printed matter density is 0.307 -- not the 0.2973 of the point 69's order names.
_om = re.search(r'\\Omega_\{m\}=([0-9.]+)', FLAT)
OM_PRINTED = float(_om.group(1)) if _om else 0.0
# the point the ORDER names, pinned as the order states it -- NOT as the paper's, which it is not
H0_ORDER, OM_ORDER = 68.60, 0.2973
check('Ⓑ⑪ PINNED the point 69\'s order r7833 names is H_0 = 68.60 with Om = 0.2973, and it is '
      'that pair, and no figure of the paper, that gives the 1.1593e-52 used above',
      abs(H0_ORDER - 68.60) <= 5e-3 and abs(OM_ORDER - 0.2973) <= 5e-5
      and abs(lam(H0_ORDER, OM_ORDER) - LAM_P16) <= 1e-60,
      f'Lambda({H0_ORDER}, {OM_ORDER}) = {lam(H0_ORDER, OM_ORDER):.5e}')
check('Ⓑ⑨ PINNED the only matter density P16 prints is 0.307, parsed out of the paper, and it '
      'is NOT the 0.2973 of the point the order names',
      _om is not None and abs(OM_PRINTED - 0.307) <= 5e-4 and abs(OM_PRINTED - 0.2973) > 5e-4,
      f'{OM_PRINTED}')
check('Ⓑ⑩ and P16 prints NO value of Lambda and neither 68.60 nor 0.2973 anywhere, so the '
      'background the regulated peak is computed on is stated by NO sentence of the paper',
      '68.60' not in FLAT and '0.2973' not in FLAT
      and not re.search(r'1\.1[0-9]*(e-52|\\times10\^\{-52\})', FLAT),
      'no Lambda, no 68.60, no 0.2973 in the paper')

# ---------------------------------------------------------------- (3)
print()
print('Ⓓ (3) the dissociation thresholds, two criteria kept apart')
mev = lambda t9: t9 * 1e9 / K_PER_MEV
t9 = lambda kt: kt * K_PER_MEV / 1e9
_m = re.search(r'T_9\\simeq([0-9.]+)\$ for deuterium and \$([0-9.]+)\$ for helium-4', FLAT)
check('Ⓓ① the printed pair is parsed out of the paper, not retyped', _m is not None)
T9_D_P, T9_HE_P = (float(_m.group(1)), float(_m.group(2))) if _m else (0.0, 0.0)

X_SINGLE = math.log(1.0 / ETA)
T9_D_CRUDE = t9(B_D / X_SINGLE)
T9_HE_CRUDE = t9(B_HE4 / X_SINGLE)
check('Ⓓ② PINNED one crude criterion B/kT = ln(1/eta) = 21.22 returns deuterium at '
      'T_9 = 1.217', abs(T9_D_CRUDE - 1.217) <= 5e-4, f'{T9_D_CRUDE:.5f}')
check('Ⓓ③ PINNED the SAME criterion returns helium-4 at T_9 = 15.475',
      abs(T9_HE_CRUDE - 15.475) <= 5e-4, f'{T9_HE_CRUDE:.5f}')
check('Ⓓ④ so the printed pair IS returned by one criterion, to 1.4 and 2.1 per cent',
      abs(T9_D_CRUDE - T9_D_P) / T9_D_P < 0.02 and abs(T9_HE_CRUDE - T9_HE_P) / T9_HE_P < 0.025,
      f'{abs(T9_D_CRUDE-T9_D_P)/T9_D_P*100:.2f}% and {abs(T9_HE_CRUDE-T9_HE_P)/T9_HE_P*100:.2f}%')

ZETA3 = 1.2020569031595943


def nse_t9(B, A, g_A):
    kt = 0.1
    for _ in range(400):
        lnW = (math.log(g_A) + 1.5 * math.log(A) - A * math.log(2.0)
               + (A - 1) * math.log(4.0 * ZETA3 / math.pi ** 2)
               - 1.5 * (A - 1) * math.log(2.0 * math.pi))
        x = (A - 1) * (math.log(1.0 / ETA) + 1.5 * math.log(M_N / kt)) + lnW
        kt_new = B / x
        if abs(kt_new - kt) < 1e-14:
            return t9(kt_new), x
        kt = kt_new
    return t9(kt), x


T9_D_NSE, X_D_NSE = nse_t9(B_D, 2, 3.0)
T9_HE_NSE, X_HE_NSE = nse_t9(B_HE4, 4, 1.0)
check('Ⓓ⑤ PINNED nuclear statistical equilibrium puts deuterium at T_9 = 0.787',
      abs(T9_D_NSE - 0.787) <= 5e-4, f'{T9_D_NSE:.5f}  (B/kT = {X_D_NSE:.3f})')
check('Ⓓ⑥ PINNED and helium-4 at T_9 = 3.711, which is NOT the printed 15.8',
      abs(T9_HE_NSE - 3.711) <= 5e-4, f'{T9_HE_NSE:.5f}  (B/kT = {X_HE_NSE:.3f})')
check('Ⓓ⑦ the two criteria disagree by 1.5x on deuterium and 4.2x on helium-4, so the '
      'sentence must say which it means',
      1.4 < T9_D_CRUDE / T9_D_NSE < 1.6 and 4.0 < T9_HE_CRUDE / T9_HE_NSE < 4.4,
      f'{T9_D_CRUDE/T9_D_NSE:.3f}x and {T9_HE_CRUDE/T9_HE_NSE:.3f}x')
check('Ⓓ⑧ and P16 ALREADY carries the NSE deuterium figure elsewhere: sec:peak\'s '
      'T_D = 0.07 MeV is T_9 = 0.812, within 3.2 per cent of the NSE value and NOT of '
      'the printed 1.2', '\\TD\\simeq0.07' in FLAT and abs(t9(0.07) - T9_D_NSE) / T9_D_NSE < 0.04,
      f'0.07 MeV = T_9 {t9(0.07):.4f} vs NSE {T9_D_NSE:.4f}')
# the disagreement with 60's arm (11), stated as arithmetic
X_D_IMPLIED = B_D / mev(T9_D_P)
X_HE_IMPLIED = B_HE4 / mev(T9_HE_P)
check('Ⓓ⑨ 60\'s ground is that the implied exponents differ -- 21.51 against 20.78 -- and '
      'they do, by 3.45 per cent; that is a different claim from "does not return the pair"',
      abs(X_D_IMPLIED - 21.51) <= 5e-3 and abs(X_HE_IMPLIED - 20.78) <= 5e-3,
      f'{X_D_IMPLIED:.3f} vs {X_HE_IMPLIED:.3f}, apart by '
      f'{abs(X_D_IMPLIED-X_HE_IMPLIED)/((X_D_IMPLIED+X_HE_IMPLIED)/2)*100:.2f}%')

print()
print('Ⓔ the figures this landing PRINTS, pinned so the row cannot drift from the receipt')
LN_INV_ETA = math.log(1.0 / ETA)
check('Ⓔ① PINNED ln(1/eta) = 21.22 at eta = 6.09e-10',
      abs(LN_INV_ETA - 21.22) <= 5e-3, f'{LN_INV_ETA:.5f}')
_td = re.search(r'\\TD\\simeq([0-9.]+)\$~MeV', FLAT)
TD_PRINTED = float(_td.group(1)) if _td else 0.0
T9_FROM_TD = t9(TD_PRINTED)
check('Ⓔ② PINNED the paper\'s T_D is parsed out of sec:peak as 0.07 MeV and is T_9 = 0.812',
      _td is not None and abs(TD_PRINTED - 0.07) <= 5e-5
      and abs(T9_FROM_TD - 0.812) <= 5e-4, f'{TD_PRINTED} MeV -> T_9 {T9_FROM_TD:.5f}')
KT_NSE_D = B_D / X_D_NSE
check('Ⓔ③ PINNED and the NSE deuterium threshold is 0.0678 MeV, which is the 0.07 the paper '
      'prints to its two decimals', abs(KT_NSE_D - 0.0678) <= 5e-5
      and abs(KT_NSE_D - 0.07) <= 5e-3, f'{KT_NSE_D:.6f} MeV')
RATIO_D_CRITERIA = T9_D_CRUDE / T9_D_NSE
check('Ⓔ④ PINNED the two criteria are apart by 1.55 on deuterium',
      abs(RATIO_D_CRITERIA - 1.55) <= 5e-3, f'{RATIO_D_CRITERIA:.5f}')

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} FAILED: ' + '; '.join(FAILED))
    raise SystemExit(1)
print('  all arms hold: three figure-clusters recomputed, two routed with their forks named.')
print('=' * 78)
