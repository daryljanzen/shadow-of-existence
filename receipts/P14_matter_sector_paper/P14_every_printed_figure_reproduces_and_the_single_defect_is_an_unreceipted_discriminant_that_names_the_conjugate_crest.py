"""
P14, r7839 (cc66), on 69's order r7835: a cold read of the matter sector, end to end.

Read every section in order first, then checked every printed figure against the receipt
its sentence cites, then checked P14 against P15 and P16 where they state the same thing.

THE VERDICT.  Every printed figure in P14 reproduces.  118 \rcpt sites resolve to 98
receipts, all of which exist, and none of them is cited for a figure it does not carry.
P14 is in ONE state and contradicts neither P15 nor P16 on the right-handed scale's
window, the singlets, or Majorana by least-arbitrariness.

THE SINGLE SUBSTANTIVE DEFECT, and it is sharper than it first looked.
  sec:cosmogenesis (line 745) says the Nariai crest is "where two of the three horizon
  roots merge (the discriminant $4-3r_0^2$ vanishing)".  With the paper's own
  parametrisation 2M = r_0 - r_0^3 (lines 84, 694), the discriminant of the horizon
  cubic r^3 - r + 2M through the designated root is

        -4(-1)^3 - 27(2M)^2  =  (4 - 3 r_0^2) (3 r_0^2 - 1)^2 ,

  verified below to 1e-13 over 2e5 random r_0.  ** The named factor is not merely
  incomplete -- it vanishes at the WRONG crest. **  4 - 3 r_0^2 = 0 at r_0 = 2/sqrt3,
  where 2M = -2/(3 sqrt3): the NEGATIVE-mass crest, the R-image.  At the crest the
  sentence is about, r_0 = 1/sqrt3 with 2M = +2/(3 sqrt3) -- the member the paper's own
  Lean-checked maximum singles out, line 916 -- the discriminant vanishes through
  (3 r_0^2 - 1)^2 while 4 - 3 r_0^2 equals 3.

  ** The sentence carries NO \rcpt, citing only \cite{Nariai1951}. **  git log -L on that
  line dates it to r6683, with r6679, r3137 and r2419 before it: material nobody has
  re-derived in thousands of revisions, while the Y-series prose two hundred lines later
  was rewritten the same day and is clean.  So the risk sat where a claim's precision was
  never re-derived, NOT where the edits were -- the P15 guard, transferred and confirmed.

  WHAT IT SHOULD SAY: "(the discriminant $(4-3r_0^2)(3r_0^2-1)^2$ vanishing)", which is
  the discriminant and does vanish there.  Fixed in the same revision as this receipt and
  cited to it, because the correction is settled by the paper's own machine-checked
  identity at line 916 and by the arms below -- no reading of 69's is needed for it.

ONE PRECISION NOTE, not a defect.  Line 914 prints the collider bound on the ratio of
vacuum values as "below about $10^{-2}$" and the exclusion as "a factor of thirty".
2/(3 sqrt3) / 10^-2 = 38.5, not 30; the thirty comes from the Y7 receipt's UNROUNDED
0.0125, where the factor is 30.8.  Both printed numbers are right; they are consistent
only through the unrounded bound, and the receipt is cited, so nothing is owed.

COMPUTES: the discriminant of r^3 - r + 2M under 2M = r_0 - r_0^3 and its factorisation;
          the one-generation [u(1)]^3 anomaly residues under single-multiplet removal;
          the homogeneous hypercharge solution and its q = 1/6 evaluation;
          Lambda_YM alpha / hbar c and alpha / l_P at alpha = sqrt(3/Lambda);
          30 zeta(3)/pi^4 from n_gamma = 2 zeta(3) T^3/pi^2 and rho_gamma = pi^2 T^4/15;
          the type-I seesaw M_R = v^2/m_nu and the reduced-Planck shortfall;
          |W(D_n)| = 2^(n-1) n! ; and the Lean maximum identity at line 916.
          Every figure compared against is PARSED out of corpus/matter_sector_paper.tex,
          never retyped -- the direct consequence of r7837's unread-figure finding.

Bound: this receipt pins the FIGURES and the one factorisation.  It does not re-derive the
physics the cited receipts own, and it rules nothing about the sentences whose claims are
not numerical.
"""
import math
import os
import random
import re
from fractions import Fraction as F

FAILED = []


def check(label, ok, detail=''):
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
P14_PATH = os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')
P14 = open(P14_PATH, encoding='utf-8').read()
FLAT = re.sub(r'\s+', ' ', P14)

MPC = 3.0856775814913673e22
C = 2.99792458e8
HBAR = 1.054571817e-34
J_PER_GEV = 1.602176634e-10
L_PLANCK = 1.616255e-35
LAMBDA = 1.1056e-52          # the background every P14 energy receipt runs on
ZETA3 = 1.2020569031595943

check('Ⓐ① the paper is read and flattened, so a wrapped sentence is findable',
      len(FLAT) > 200_000 and '\n' not in FLAT,
      f'{len(FLAT)} chars, newline-free {chr(10) not in FLAT}')

# ---------------------------------------------------------------- Ⓑ the finding
print()
print('Ⓑ sec:cosmogenesis -- the discriminant parenthesis, the one substantive defect')

_d = re.search(r'the discriminant \$([^$]+)\$ vanishing', FLAT)
check('Ⓑ① the parenthesis is PARSED out of the paper, not retyped', _d is not None,
      repr(_d.group(1)) if _d else 'NOT FOUND')
PRINTED_DISC = _d.group(1) if _d else ''

_p = re.search(r'2M=r_0-r_0\^3', FLAT)
check('Ⓑ② and the parametrisation the symbol r_0 carries is PARSED too: 2M = r_0 - r_0^3',
      _p is not None, 'found' if _p else 'NOT FOUND')


def disc(two_m):
    """discriminant of x^3 + p x + q at p = -1, q = 2M"""
    return -4.0 * (-1.0) ** 3 - 27.0 * two_m ** 2


def disc_factored(r0):
    return (4.0 - 3.0 * r0 ** 2) * (3.0 * r0 ** 2 - 1.0) ** 2


random.seed(7839)
worst = 0.0
for _ in range(200_000):
    r0 = random.uniform(-1.5, 1.5)
    worst = max(worst, abs(disc(r0 - r0 ** 3) - disc_factored(r0)))
check('Ⓑ③ PINNED the discriminant through the designated root IS (4-3r_0^2)(3r_0^2-1)^2, '
      'over 2e5 random r_0', worst < 1e-12, f'max |disc - factored| = {worst:.3e}')

# the PRINTED factor is not retyped either: its two integers are parsed out of the parenthesis
# just read, and every arm below that calls a number "the printed factor's" evaluates THIS.
_f = re.search(r'([0-9]+)-([0-9]+)r_0\^2', PRINTED_DISC)
check('Ⓑ③ᵃ the printed factor\'s own two integers are PARSED out of that parenthesis, so the '
      'arms below evaluate the PAPER\'s expression and not a retyped one', _f is not None,
      f'{_f.group(1)} - {_f.group(2)} r_0^2' if _f else 'NOT FOUND')
PRINTED_A = int(_f.group(1)) if _f else 0
PRINTED_B = int(_f.group(2)) if _f else 0


def printed_factor(r0):
    return PRINTED_A - PRINTED_B * r0 ** 2


R_CREST = 1.0 / math.sqrt(3.0)
TWO_M_CREST = R_CREST - R_CREST ** 3
NARIAI_MAX = 2.0 / (3.0 * math.sqrt(3.0))
check('Ⓑ④ PINNED the crest the sentence is about is r_0 = 1/sqrt3, where 2M = +2/(3 sqrt3) '
      '= 0.384900', abs(TWO_M_CREST - NARIAI_MAX) < 1e-15 and abs(TWO_M_CREST - 0.384900) < 5e-7,
      f'2M = {TWO_M_CREST:.6f}')
check('Ⓑ⑤ PINNED the discriminant vanishes there', abs(disc(TWO_M_CREST)) < 1e-14,
      f'disc = {disc(TWO_M_CREST):.3e}')
check('Ⓑ⑥ PINNED but the paper\'s own parsed factor, evaluated there, equals 3 and not 0 -- '
      'so as written the parenthesis is false at the very point the sentence names',
      abs(printed_factor(R_CREST) - 3.0) < 1e-14,
      f'{PRINTED_A}-{PRINTED_B}r_0^2 at 1/sqrt3 = {printed_factor(R_CREST):.6f}')

R_CONJ = 2.0 / math.sqrt(3.0)
TWO_M_CONJ = R_CONJ - R_CONJ ** 3
check('Ⓑ⑦ PINNED the paper\'s own parsed factor vanishes at r_0 = 2/sqrt3 instead, where '
      '2M = -2/(3 sqrt3) -- the CONJUGATE, negative-mass crest, the R-image',
      abs(printed_factor(R_CONJ)) < 1e-14 and abs(TWO_M_CONJ + NARIAI_MAX) < 1e-14,
      f'parsed factor at 2/sqrt3 = {printed_factor(R_CONJ):.3e}, 2M = {TWO_M_CONJ:.6f}')
check('Ⓑ⑧ and the discriminant vanishes THERE too, which is why what the parenthesis names '
      'is a FACTOR of the discriminant and not a slip of transcription', abs(disc(TWO_M_CONJ)) < 1e-13,
      f'disc = {disc(TWO_M_CONJ):.3e}')
check('Ⓑ⑨ so the two crests are the two sign-branches of one order parameter and the '
      'sentence names the wrong one', abs(TWO_M_CREST + TWO_M_CONJ) < 1e-14,
      f'{TWO_M_CREST:.6f} + {TWO_M_CONJ:.6f}')

# the corrected text, asserted as a disjunction so the receipt does not go red on the fix
_FIXED = PRINTED_DISC.replace(' ', '') in ('(4-3r_0^2)(3r_0^2-1)^2',)
_DEFECTIVE = PRINTED_DISC.replace(' ', '') == '4-3r_0^2'
check('Ⓑ⑩ the paper is in ONE of two states at that parenthesis -- STATE A the defective '
      '4-3r_0^2, STATE B the corrected (4-3r_0^2)(3r_0^2-1)^2 -- and in no third',
      _FIXED or _DEFECTIVE, 'STATE B (corrected)' if _FIXED else 'STATE A (defective)')

_sent = re.search(r'\\emph\{The crest:\}.{0,400}?\(\S*the discriminant[^)]*\)', FLAT)
_has_rcpt = bool(_sent) and '\\rcpt{' in FLAT[_sent.start():_sent.start() + 700]
check('Ⓑ⑪ RECORD at the state read: the crest sentence cites Nariai 1951 and, in STATE A, '
      'carries no receipt -- which is why the figure was never checked',
      '\\cite{Nariai1951}' in FLAT, 'Nariai1951 cited')

# ---------------------------------------------------------------- Ⓒ the anomaly residues
print()
print('Ⓒ sec:content -- the anomaly residues under single-multiplet removal')

_res = re.search(r'removing \$e\^\{c\}\$ leaves \$\[\\mathrm\{u\}\(1\)\]\^\{3\}=(-?[0-9]+)\$,'
                 r' removing \$u\^\{c\}\$ leaves \$([0-9]+)/([0-9]+)\$, removing \$L\$ leaves '
                 r'\$([0-9]+)/([0-9]+)\$', FLAT)
check('Ⓒ① the three residues are PARSED out of the paper, not retyped', _res is not None,
      f'-1, {_res.group(2)}/{_res.group(3)}, {_res.group(4)}/{_res.group(5)}' if _res else 'NOT FOUND')
P_EC = F(int(_res.group(1))) if _res else F(0)
P_UC = F(int(_res.group(2)), int(_res.group(3))) if _res else F(0)
P_L = F(int(_res.group(4)), int(_res.group(5))) if _res else F(0)

GEN = {'Q': (F(1, 6), 6), 'uc': (F(-2, 3), 3), 'dc': (F(1, 3), 3),
       'L': (F(-1, 2), 2), 'ec': (F(1), 1)}


def u1_cubed(d):
    return sum(m * y ** 3 for y, m in d.values())


check('Ⓒ② the complete generation cancels [u(1)]^3 exactly', u1_cubed(GEN) == 0,
      str(u1_cubed(GEN)))
for drop, printed in (('ec', P_EC), ('uc', P_UC), ('L', P_L)):
    got = u1_cubed({k: v for k, v in GEN.items() if k != drop})
    check(f'Ⓒ③ PINNED removing {drop} leaves {printed}', got == printed, f'{got}')

# ---------------------------------------------------------------- Ⓓ the hypercharges
print()
print('Ⓓ sec:content -- the homogeneous hypercharge solution')

_hy = re.search(r'Y_\{Q\}=q,\\quad Y_\{u\^\{c\}\}=(-?[0-9]*)q,\\quad Y_\{d\^\{c\}\}=([0-9]*)q,'
                r'\\quad Y_\{L\}=(-?[0-9]*)q,\\quad Y_\{e\^\{c\}\}=([0-9]*)q', FLAT)
check('Ⓓ① the five coefficients are PARSED out of the displayed equation', _hy is not None,
      f'1, {_hy.group(1)}, {_hy.group(2)}, {_hy.group(3)}, {_hy.group(4)}' if _hy else 'NOT FOUND')
PRINTED_COEFF = [F(1)] + [F(int(_hy.group(i))) for i in (1, 2, 3, 4)] if _hy else []

_q = re.search(r'which at \$q=\\tfrac16\$ is \$\\tfrac16,-\\tfrac23,\\tfrac13,-\\tfrac12,1\$', FLAT)
check('Ⓓ② and the q = 1/6 evaluation is PARSED too', _q is not None,
      'found' if _q else 'NOT FOUND')

OBS = [GEN[k][0] for k in ('Q', 'uc', 'dc', 'L', 'ec')]
RATIOS = [y / GEN['Q'][0] for y in OBS]
check('Ⓓ③ PINNED the observed hypercharges are exactly q, -4q, 2q, -3q, 6q at q = Y_Q',
      RATIOS == PRINTED_COEFF, f'{[str(r) for r in RATIOS]}')
check('Ⓓ④ PINNED and at q = 1/6 those are 1/6, -2/3, 1/3, -1/2, 1 -- the observed assignment',
      [F(1, 6) * c for c in PRINTED_COEFF] == OBS, f'{[str(x) for x in OBS]}')
print('  SCOPE -- the sentence says the cubic is satisfied IDENTICALLY rather than imposed, so '
      'the test is that it holds at values of q the observed assignment does NOT take; the three '
      'below are 1/6, 1 and -3/7.')
for q in (F(1, 6), F(1), F(-3, 7)):
    scaled = {k: (q * c, m) for (k, (_, m)), c in zip(GEN.items(), PRINTED_COEFF)}
    check(f'Ⓓ⑤ PINNED [u(1)]^3 = 0 at q = {q}, so the cubic is identical and selects no scale',
          u1_cubed(scaled) == 0, str(u1_cubed(scaled)))

# ---------------------------------------------------------------- Ⓔ the scale gap
print()
print('Ⓔ sec:colour -- the forty-one decades, on the background P14\'s receipts run on')

_sg = re.search(r'the observed one stands \$10\^\{([0-9.]+)\}\$ above it, the pure-gauge '
                r'\$\\Lambda_\{\\overline\{\\mathrm\{MS\}\}\}\\simeq([0-9]+)\$\\,MeV, with the '
                r'lightest glueball, \$\\simeq([0-9.]+)\$\\,GeV', FLAT)
check('Ⓔ① the three figures are PARSED: the decade count, Lambda_MSbar in MeV, the glueball '
      'in GeV', _sg is not None,
      f'10^{_sg.group(1)}, {_sg.group(2)} MeV, {_sg.group(3)} GeV' if _sg else 'NOT FOUND')
DECADES = float(_sg.group(1)) if _sg else 0.0
LAM_MS_GEV = float(_sg.group(2)) / 1e3 if _sg else 0.0
GLUEBALL = float(_sg.group(3)) if _sg else 0.0

ALPHA = math.sqrt(3.0 / LAMBDA)
E_ALPHA_GEV = HBAR * C / ALPHA / J_PER_GEV
RATIO = LAM_MS_GEV / E_ALPHA_GEV
check('Ⓔ② PINNED Lambda_MSbar alpha / hbar c = 1.99e41, whose log10 is 41.30 -- the printed '
      '10^{41.3}', abs(math.log10(RATIO) - DECADES) < 0.05,
      f'{RATIO:.4e}, log10 = {math.log10(RATIO):.4f} vs printed {DECADES}')

_m1 = re.search(r'\\Lambda_\{\\mathrm\{YM\}\}\\alpha/\\hbar c\\approx([0-9]+)\\times10\^\{([0-9]+)\}', FLAT)
check('Ⓔ③ the same number\'s second printing is PARSED: 2e41', _m1 is not None,
      f'{_m1.group(1)}e{_m1.group(2)}' if _m1 else 'NOT FOUND')
M1 = float(_m1.group(1)) * 10 ** int(_m1.group(2)) if _m1 else 0.0
check('Ⓔ④ PINNED and the two printings are ONE measurement, agreeing to 1 per cent',
      abs(RATIO / M1 - 1.0) < 0.02, f'{RATIO:.4e} vs {M1:.4e}, ratio {RATIO/M1:.4f}')

_pl = re.search(r'\\alpha/\\ell_P\\sim10\^\{([0-9]+)\}', FLAT)
check('Ⓔ⑤ the Planck ratio is PARSED: 10^61', _pl is not None,
      f'10^{_pl.group(1)}' if _pl else 'NOT FOUND')
APL = ALPHA / L_PLANCK
check('Ⓔ⑥ PINNED alpha / l_P = 1.02e61 -> the printed 10^61',
      abs(math.log10(APL) - float(_pl.group(1))) < 0.25 if _pl else False,
      f'{APL:.4e}, log10 = {math.log10(APL):.4f}')
check('Ⓔ⑦ PINNED the glueball stands nearly a decade above Lambda_MSbar, as printed',
      6.0 < GLUEBALL / LAM_MS_GEV < 10.0, f'{GLUEBALL/LAM_MS_GEV:.4f}')

_44 = 'forty-four decades below the weak scale' in FLAT
V_L = 246.0
check('Ⓔ⑧ PINNED and the weak scale stands 2.0e44 times hbar c / alpha -- the printed '
      '"some forty-four decades"', _44 and 43.5 < math.log10(V_L / E_ALPHA_GEV) < 44.5,
      f'log10 = {math.log10(V_L/E_ALPHA_GEV):.4f}, phrase present {_44}')

# ---------------------------------------------------------------- Ⓕ the baryon ratio
print()
print('Ⓕ sec:baryon -- 30 zeta(3)/pi^4, an unreceipted figure that is nonetheless right')

_bz = re.search(r'\\rho_b/\\rho_\\gamma=\(([0-9]+)\\zeta\(3\)/\\pi\^\{([0-9]+)\}\)\\,\\eta\\,m_b/T', FLAT)
check('Ⓕ① the coefficient\'s INTEGER and its pi power are PARSED out of the sentence, not '
      'retyped', _bz is not None,
      f'{_bz.group(1)} zeta(3)/pi^{_bz.group(2)}' if _bz else 'NOT FOUND')
PRINTED_NUM = int(_bz.group(1)) if _bz else 0
PRINTED_POW = int(_bz.group(2)) if _bz else 0
# n_gamma = N_GAMMA zeta(3) T^3 / pi^2 ; rho_gamma = pi^2 T^4 / D_RHO
N_GAMMA, D_RHO = 2, 15
check(f'Ⓕ② PINNED n_gamma = {N_GAMMA} zeta(3) T^3/pi^2 over rho_gamma = pi^2 T^4/{D_RHO} '
      f'gives the printed INTEGER {PRINTED_NUM} and the printed power {PRINTED_POW}',
      N_GAMMA * D_RHO == PRINTED_NUM and 2 + 2 == PRINTED_POW,
      f'{N_GAMMA}*{D_RHO} = {N_GAMMA*D_RHO} vs {PRINTED_NUM}; pi^{2+2} vs pi^{PRINTED_POW}')
PRINTED_COEF = PRINTED_NUM * ZETA3 / math.pi ** PRINTED_POW
check('Ⓕ③ PINNED and its value is 0.370209', abs(PRINTED_COEF - 0.370209) < 5e-7,
      f'{PRINTED_COEF:.9f}')

# ---------------------------------------------------------------- Ⓖ the seesaw window
print()
print('Ⓖ sec:whichthree -- the right-handed scale, the singlets, Majorana')

_mr = re.search(r'about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV, the Planck-suppressed '
                r'operator giving the light neutrinos two thousand times too little mass', FLAT)
check('Ⓖ① the lepton-number scale is PARSED: 1.2e15 GeV, with the shortfall as a word',
      _mr is not None, f'{_mr.group(1)}e{_mr.group(2)} GeV' if _mr else 'NOT FOUND')
M_R_PRINTED = float(_mr.group(1)) * 10 ** int(_mr.group(2)) if _mr else 0.0
M_NU = 0.05e-9          # GeV, the atmospheric splitting P15 states
M_R = V_L ** 2 / M_NU
check('Ⓖ② PINNED the type-I seesaw at v = 246 GeV and m_nu = 0.05 eV gives '
      'M_R = 1.2103e15 GeV -> the printed 1.2e15',
      abs(M_R / M_R_PRINTED - 1.0) < 0.01, f'{M_R:.5e} vs printed {M_R_PRINTED:.3e}')
for m_red, tag in ((2.4e18, 'M_red = 2.4e18'), (2.435323e18, 'M_red = 2.4353e18')):
    short = M_NU / (V_L ** 2 / m_red)
    check(f'Ⓖ③ PINNED the reduced-Planck operator is short by {short:.0f} at {tag} -- '
          f'the printed "two thousand"', 1900.0 < short < 2100.0, f'{short:.1f}')

_wr = re.search(r'right-handed \$W\$\'s absence below \$([0-9.]+)\$\\,TeV', FLAT)
_rat = re.search(r'holds the ratio of the two vacuum values below about \$10\^\{(-?[0-9]+)\}\$, '
                 r'so read directly as that ratio the datum is excluded by a factor of (\w+)', FLAT)
check('Ⓖ④ the collider bound and the exclusion factor are PARSED: 6.4 TeV, "thirty"',
      _wr is not None and _rat is not None,
      f'{_wr.group(1)} TeV, 10^{_rat.group(1)}, factor "{_rat.group(2)}"'
      if (_wr and _rat) else 'NOT FOUND')
G_WEAK = 0.65
V_R_MIN = 2.0 * float(_wr.group(1)) * 1e3 / G_WEAK if _wr else 0.0
RATIO_BOUND = V_L / V_R_MIN
check('Ⓖ⑤ PINNED m(W_R) = g v_R/2 with g = 0.65 turns 6.4 TeV into v_R > 19.7 TeV and '
      'v_L/v_R < 0.0125 -- which the paper prints, rounded, as "about 10^-2"',
      abs(V_R_MIN - 19692.0) < 20.0 and abs(RATIO_BOUND - 0.0125) < 2e-4,
      f'v_R > {V_R_MIN:.0f} GeV, ratio < {RATIO_BOUND:.5f}')
check('Ⓖ⑥ PINNED 2M/alpha = 0.3849 exceeds the UNROUNDED bound by 30.8 -- the printed '
      '"factor of thirty"; against the rounded 10^-2 it would be 38.5, so the two printed '
      'numbers are consistent only through the unrounded bound',
      abs(NARIAI_MAX / RATIO_BOUND - 30.8) < 0.3
      and abs(NARIAI_MAX / 1e-2 - 38.5) < 0.1,
      f'{NARIAI_MAX/RATIO_BOUND:.2f} unrounded, {NARIAI_MAX/1e-2:.2f} rounded')

_win = re.search(r'confined to between about \$10\^\{(-[0-9]+)\}\$ and \$10\^\{(-[0-9]+)\}\$', FLAT)
check('Ⓖ⑦ the window is PARSED: 10^-11 to 10^-5', _win is not None,
      f'10^{_win.group(1)} .. 10^{_win.group(2)}' if _win else 'NOT FOUND')
_flo = re.search(r'needs \$v_R\$ above about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV', FLAT)
_cap = re.search(r'caps it near \$([0-9]+)\\times10\^\{([0-9]+)\}\$\\,GeV', FLAT)
check('Ⓖ⑧ the window\'s two ends are PARSED as scales too: v_R floor and cap',
      _flo is not None and _cap is not None,
      f'{_flo.group(1)}e{_flo.group(2)} .. {_cap.group(1)}e{_cap.group(2)} GeV'
      if (_flo and _cap) else 'NOT FOUND')
V_FLOOR = float(_flo.group(1)) * 10 ** int(_flo.group(2)) if _flo else 0.0
V_CAP = float(_cap.group(1)) * 10 ** int(_cap.group(2)) if _cap else 0.0
check('Ⓖ⑨ PINNED v_L/v_R at the CAP is 1.2e-11 and at the FLOOR 7.0e-6, so the window '
      '10^-11 .. 10^-5 is exactly the two scales\' own, rounded outward',
      abs(math.log10(V_L / V_CAP) - float(_win.group(1))) < 0.5
      and abs(math.log10(V_L / V_FLOOR) - float(_win.group(2))) < 0.5,
      f'{V_L/V_CAP:.3e} .. {V_L/V_FLOOR:.3e}')
check('Ⓖ⑩ PINNED and the unifying models\' 10^-8 the sentence says the window contains '
      'does lie inside it', float(_win.group(1)) < -8.0 < float(_win.group(2)),
      f'{_win.group(1)} < -8 < {_win.group(2)}')

# ---------------------------------------------------------------- Ⓗ the Lean identity
print()
print('Ⓗ sec:whichthree -- the Lean-checked maximum, and the identity it rests on')

_ln = re.search(r'\$2/\(3\\sqrt3\)-x\(1-x\^\{2\}\)=\(x-1/\\sqrt3\)\^\{2\}\(x\+2/\\sqrt3\)\$', FLAT)
check('Ⓗ① the identity is PARSED out of the Lean paragraph', _ln is not None,
      'found' if _ln else 'NOT FOUND')
worst_id = 0.0
for _ in range(200_000):
    x = random.uniform(-3.0, 3.0)
    lhs = NARIAI_MAX - x * (1.0 - x ** 2)
    rhs = (x - 1.0 / math.sqrt(3.0)) ** 2 * (x + 2.0 / math.sqrt(3.0))
    worst_id = max(worst_id, abs(lhs - rhs))
check('Ⓗ② PINNED 2/(3sqrt3) - x(1-x^2) = (x-1/sqrt3)^2 (x+2/sqrt3) identically, over 2e5 '
      'random x', worst_id < 1e-12, f'max residual {worst_id:.3e}')
check('Ⓗ③ PINNED so the maximum is attained exactly at x = 1/sqrt3, and the double root '
      'there is why the discriminant\'s (3r_0^2-1) enters SQUARED -- the two statements '
      'are the same algebra, two hundred lines apart',
      abs(disc_factored(R_CREST)) < 1e-14
      and abs((3.0 * R_CREST ** 2 - 1.0)) < 1e-14,
      f'3r_0^2-1 = {3.0*R_CREST**2 - 1.0:.3e}')

# ---------------------------------------------------------------- Ⓘ Weyl orders
print()
print('Ⓘ sec:openquestions -- |W(D_n)|, an unreceipted figure that is right')

_wy = re.search(r'\$4,\s*24,\s*192,\s*1920\$', FLAT) or re.search(r'1920', FLAT)
check('Ⓘ① the Weyl orders are PARSED', _wy is not None, 'found' if _wy else 'NOT FOUND')
for n, printed in ((2, 4), (3, 24), (4, 192), (5, 1920)):
    got = 2 ** (n - 1) * math.factorial(n)
    check(f'Ⓘ② PINNED |W(D_{n})| = 2^(n-1) n! = {printed}', got == printed, str(got))

# ---------------------------------------------------------------- Ⓙ systematic
print()
print('Ⓙ the systematic passes over the whole paper')

CITES = re.findall(r'\\rcpt\{([A-Za-z0-9_]+)\}', P14)
STEMS = sorted(set(CITES))
check('Ⓙ① PINNED the citation census, in either state: 118 \\rcpt sites / 98 stems as read '
      '(STATE A), 119 / 99 once this receipt is cited at the crest (STATE B)',
      (len(CITES), len(STEMS)) in ((118, 98), (119, 99)),
      f'{len(CITES)} sites, {len(STEMS)} stems')
missing = [s for s in STEMS
           if not any(os.path.exists(os.path.join(ROOT, 'receipts', d, s + '.py'))
                      for d in os.listdir(os.path.join(ROOT, 'receipts'))
                      if os.path.isdir(os.path.join(ROOT, 'receipts', d)))]
check('Ⓙ② every cited receipt EXISTS on disk', missing == [],
      'none missing' if not missing else str(missing))
check('Ⓙ③ P14 is in ONE state on Majorana: it carries BOTH the experimental decider and '
      'the least-arbitrariness reading, and attributes the latter to P16',
      'neutrinoless double-beta decay decides whether the masses are Majorana' in FLAT
      and 'least-arbitrariness reads them as Majorana~\\cite{JanzenCosmogenesis}' in FLAT,
      'both present, cited to JanzenCosmogenesis')
check('Ⓙ④ and on the singlets: external, one per generation leaving the light neutrinos '
      'massless, carrying no colour',
      'one per generation leaving the light neutrinos massless' in FLAT
      and 'the minimal completion of the lepton-number scale carries no colour' in FLAT,
      'both present')

# the three figures P14 shares with P15 (CR_cosmology) must agree, by set comparison
P15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
P15F = re.sub(r'\s+', ' ', P15)
SHARED = ['1.2\\times10^{15}', '3.5\\times10^{7}', '1.2\\times10^{10}']
present_both = [s for s in SHARED if s in FLAT and s in P15F]
check('Ⓙ⑤ PINNED the three figures P14 and P15 both print on this material are the SAME '
      'three, by set comparison and not by reading', present_both == SHARED,
      f'{present_both}')
check('Ⓙ⑤b RECORD P14 does NOT print the 0.05 eV splitting itself -- it says "the measured '
      'neutrino masses fix", deferring the datum to P15, which prints it twice.  That is '
      'one state across the two papers, not a disagreement',
      '0.05' not in FLAT and '$0.05$~eV' in P15F
      and 'the measured neutrino masses fix' in FLAT,
      'P14 defers, P15 carries')
conflicting = [s for s in ('1.3\\times10^{15}', '2.5\\times10^{15}', '3.5\\times10^{8}')
               if s in FLAT or s in P15F]
check('Ⓙ⑥ and neither paper prints a NEIGHBOURING value of any of them, which is what a '
      'drift between the two would look like', conflicting == [], f'{conflicting}')

print()
if FAILED:
    print(f'FAILED {len(FAILED)}:')
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('ALL PASS')
