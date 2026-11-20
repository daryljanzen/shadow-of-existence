"""
P18, r7841+cc66.1, on 69's order r7841: a cold read of CR_synthesis (the synthesis), end to end.

Read all ten sections in order before touching anything, then checked every printed figure
against the paper or receipt its sentence cites, then checked that P18 states each companion's
result as that companion NOW states it.

WHY P18 IS NOT P14, AND WHY THE r7839 METHOD DOES NOT TRANSFER.  P18 carries 3271 lines and
ZERO \rcpt sites against P14's 118 over 98 receipts, with 343 \cite sites instead, and it has
no receipts appendix at all.  It restates results it does not own, so the chain is
P18 -> companion paper -> that paper's receipt.  "Check every figure against the receipt its
sentence cites" has no purchase here, and assuming it did would be the first way to get this
read wrong.  Every figure compared against below is therefore PARSED out of BOTH
corpus/CR_synthesis.tex and the companion's own .tex.

TWO SUBSTANTIVE DEFECTS, both of them STALENESS -- a clause right when written and since
superseded -- which is the class this read registered in advance as the modal one.

  (1) sec:acoustic and the handover subsection carried a SUPERSEDED ACOUSTIC CLUSTER.
      P18 printed peaks 220.0 / 536.3 / 811.6 / 1125.1 with heights 2.291 / 2.349.  P15 now
      publishes, on the rate the universe has, peaks 220.2 / 536.9 / 811.2 / 1123.9 with
      comb 298.5 and heights P1/P2 = 2.207 and P1/P3 = 2.249, and gives the geometric-part
      reading a comb of 299.1 and heights 2.291 / 2.349 and NO PEAK LIST AT ALL.  The four
      printed peaks are P15's GRID-CONVERGENCE figures (220.03, 536.27, 811.58, 1125.02),
      not its published locations.
      ** AND THE DEFECT UNDERSTATED THE CONSTRUCTION'S OWN RESULT. **  Against the sky's
      2.221 and 2.262 the published pair sits 0.63 and 0.57 per cent away; the pair P18
      printed sits 3.2 and 3.8 per cent away -- about five times worse -- so P18 reported the
      construction agreeing with the sky less well than P15 says it does, in the section
      whose argument is that the geometric-part distance is the WRONG one.
      ** The second site was the worse of the two **: it dropped the qualifier entirely and
      called them "this arm's peaks", in the passage about what the derivation returns.

  (2) sec:displace's REGISTER COUNT is sourced to a RETIRED DOCUMENT and understates the
      evidence rail by nearly half.  P18 offered "an evidence rail of several hundred
      receipts" in a paragraph insisting "the register is not an illustration but a count".
      The only other place in the repository carrying that count cluster -- "196 formal
      environments.  Fourteen named theorems and six axioms.  684 receipt files" -- is
      retired/WHAT_THE_FRAMEWORK_DELIVERS.md.  Measured live below: over twelve hundred
      receipt files and INDEX rows.  A count offered as the price of disqualifying the
      framework cannot be half the real one.

WHAT IS CLEAN, each checked and closed rather than assumed:
  * the comb 298.5 / 298.4 -- P15 prints both, so P18 matches it as P15 now states it;
  * the four abundances -- P16's headline display matches P18 figure for figure, and the
    2.50e-5 elsewhere in P16 is a different run (the right-handed-neutrino comparison);
  * the regulated peak -- P18 states only the density, verbatim with P16, and does not
    restate the throat and extremum radii 69 landed at r7835, so nothing there is stale;
  * the discriminant -- P18 states it qualitatively in four places and never writes the
    4-3r_0^2 form, so r7839's P14 defect did NOT propagate here;
  * the Virgo gas probe -- P18's "out to 24-26 degrees from M87" matches the r7831
    computation verbatim in substance.  ** The looser statement is the RECEIPT's **, whose
    print line calls 24-26 degrees a width; recorded, and not P18's to answer.

COMPUTES: the slice-curvature identity -f'/2 = r K_G with K_G = 1/alpha^2 - M/r^3 and its
          flat locus r^3 = M alpha^2 ; the Hubble--Eddington radius (3GM/Lambda c^2)^(1/3) ;
          the marginal rate (2M/r + r^2/alpha^2) and its minimum and turnaround ;
          the pencil r^3 + alpha^2(c-1) r + 2M alpha^2 and the omega-rotation residue ;
          the TT floor from k^2 = L(L+2) - 2 ; Lambda_YM alpha / hbar c and alpha / l_P ;
          the Bekenstein--Hawking gauge count pi (alpha/l_P)^2 ; the type-I seesaw ;
          the turnover matter fraction from rho_m = 2 rho_Lambda ; and the live register
          counts measured off the tree.

Bound: this receipt pins P18's FIGURES and its agreement with its companions.  It does not
re-derive the physics the companions own, and it rules nothing about P18's readings, which
are stated as readings.
"""
import math
import os
import re
import subprocess

FAILED = []


def check(label, ok, detail=''):
    print(('  [ok]   ' if ok else '  [FAIL] ') + label + (('   ' + detail) if detail else ''))
    if not ok:
        FAILED.append(label)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))


def flat(name):
    return re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', name), encoding='utf-8').read())


P18 = flat('CR_synthesis.tex')
P15 = flat('CR_cosmology.tex')
P16 = flat('cosmogenesis_paper.tex')
P14 = flat('matter_sector_paper.tex')

check('Ⓐ① all four papers are read and flattened, so a wrapped sentence is findable',
      min(len(P18), len(P15), len(P16), len(P14)) > 100_000,
      f'P18 {len(P18)}, P15 {len(P15)}, P16 {len(P16)}, P14 {len(P14)} chars')

_RC = len(re.findall(r'\\rcpt\{', P18))
_CI = len(re.findall(r'\\cite\{', P18))
check('Ⓐ② PINNED P18 carries ZERO \\rcpt sites and 343 \\cite sites, which is why the chain '
      'is P18 -> companion -> receipt and the P14 method does not transfer',
      # r7845 (69): STATE B -- r7843+cc66.1 gave P18 its first receipt sites, both citing the section-10
      #   counts receipt; every OTHER figure still runs P18 -> companion -> receipt, which is the claim.
      _CI == 343 and (_RC == 0 or set(re.findall(r'\\rcpt\{([^}]*)\}', P18)) == {
          'P18_section_tens_counts_measured_four_hold_under_the_papers_own_convention_and_two_have_no_enumerable_subject'}),
      f'{_RC} rcpt, {_CI} cite')

# the abstract's own word for the count is PARSED, and the dissertation entry that the
# word excludes is identified by its own key rather than assumed to exist.
WORDS = {'five': 5, 'nine': 9, 'ten': 10, 'eleven': 11,
         'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
         'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
_abs = re.search(r'every claim is drawn from one of ([a-z]+)\s+papers', P18)
ABSTRACT_N = WORDS.get(_abs.group(1)) if _abs else None
_BIB = len(re.findall(r'\\bibitem\{Janzen', P18))
_DISS = len(re.findall(r'\\bibitem\{Janzen[A-Za-z]*(?:Thesis|Diss)', P18))
check('Ⓐ③ PINNED the abstract\'s own word for the count is PARSED and equals the Janzen '
      'bibliography less its dissertation entry, which is found by its own key',
      ABSTRACT_N is not None and _DISS == 1 and _BIB - _DISS == ABSTRACT_N,
      f'abstract says {_abs.group(1) if _abs else None} = {ABSTRACT_N}; '
      f'{_BIB} Janzen bibitems less {_DISS} dissertation = {_BIB - _DISS}')

# ---------------------------------------------------------------- Ⓑ defect (1)
print()
print('Ⓑ (1) sec:acoustic -- the superseded acoustic cluster')

# P15's PUBLISHED arm figures, parsed out of P15 itself
_p15pk = re.search(r'the peaks fall at \$([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and '
                   r'\$([0-9.]+)\$ against the sky\'s \$([0-9.]+)\$, \$([0-9.]+)\$, '
                   r'\$([0-9.]+)\$ and \$([0-9.]+)\$', P15)
check('Ⓑ① P15\'s published arm peaks are PARSED out of P15, not retyped',
      _p15pk is not None,
      ' / '.join(_p15pk.groups()[:4]) if _p15pk else 'NOT FOUND')
P15_ARM = [float(x) for x in _p15pk.groups()[:4]] if _p15pk else []
SKY_PK = [float(x) for x in _p15pk.groups()[4:]] if _p15pk else []

_p15ht = re.search(r'the height ratios \$P_\{1\}/P_\{2\}=([0-9.]+)\$ and \$P_\{1\}/P_\{3\}=([0-9.]+)\$'
                   r' against the sky\'s \$([0-9.]+)\$ and \$([0-9.]+)\$', P15)
check('Ⓑ② and P15\'s published arm height ratios are PARSED too', _p15ht is not None,
      ' / '.join(_p15ht.groups()) if _p15ht else 'NOT FOUND')
P15_HT = [float(_p15ht.group(1)), float(_p15ht.group(2))] if _p15ht else []
SKY_HT = [float(_p15ht.group(3)), float(_p15ht.group(4))] if _p15ht else []

_p15geo = re.search(r"With the projection's distance on the rate's geometric part the same locator "
                    r'returns a comb of \$([0-9.]+)\$ and height ratios of \$([0-9.]+)\$ and '
                    r'\$([0-9.]+)\$', P15)
check('Ⓑ③ and P15\'s GEOMETRIC-PART reading is parsed: a comb and two heights, '
      'and NO peak list', _p15geo is not None,
      f'comb {_p15geo.group(1)}, heights {_p15geo.group(2)}/{_p15geo.group(3)}'
      if _p15geo else 'NOT FOUND')
P15_GEO_HT = [float(_p15geo.group(2)), float(_p15geo.group(3))] if _p15geo else []

# the GRID-CONVERGENCE figures P18's defective cluster was rounded from
_p15grid = re.search(r'wavenumber grid---returns peaks at \$([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and \$([0-9.]+)\$',
                     P15)
check('Ⓑ④ PINNED and P15\'s GRID-CONVERGENCE peaks -- the figures the defective cluster was '
      'rounded from -- are parsed as 220.03 / 536.27 / 811.58 / 1125.02',
      _p15grid is not None
      and [round(float(x), 1) for x in _p15grid.groups()] == [220.0, 536.3, 811.6, 1125.0],
      ' / '.join(_p15grid.groups()) if _p15grid else 'NOT FOUND')

# P18's own cluster, parsed at whatever state the paper is in
_p18pk = re.search(r'with peaks at \$([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and \$([0-9.]+)\$'
                   r' against the sky', P18) \
    or re.search(r"geometric part peaks at \$([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and "
                 r'\$([0-9.]+)\$ against the sky', P18)
check('Ⓑ⑤ P18\'s own peak cluster is PARSED out of P18 at whatever state it is in',
      _p18pk is not None, ' / '.join(_p18pk.groups()) if _p18pk else 'NOT FOUND')
P18_PK = [float(x) for x in _p18pk.groups()] if _p18pk else []

_p18arm = re.search(r'the derivation is the two-arm transfer that propagates the modes, '
                    r"which returns this arm's peaks at \$([0-9.]+)\$, \$([0-9.]+)\$, "
                    r'\$([0-9.]+)\$ and \$([0-9.]+)\$', P18)
check('Ⓑ⑥ and the second site -- "this arm\'s peaks", the one that dropped the qualifier -- '
      'is parsed separately', _p18arm is not None,
      ' / '.join(_p18arm.groups()) if _p18arm else 'NOT FOUND')
P18_ARM = [float(x) for x in _p18arm.groups()] if _p18arm else []

_p18ht = re.search(r'\$P_\{1\}/P_\{2\}=([0-9.]+)\$ and \$P_\{1\}/P_\{3\}=([0-9.]+)\$', P18)
P18_HT = [float(_p18ht.group(1)), float(_p18ht.group(2))] if _p18ht else []
check('Ⓑ⑦ and P18\'s height ratios at that site are parsed', _p18ht is not None,
      ' / '.join(_p18ht.groups()) if _p18ht else 'NOT FOUND')

_STATE_B = (P18_PK == P15_ARM and P18_ARM == P15_ARM and P18_HT == P15_HT)
_STATE_A = ([round(x, 1) for x in P18_PK] == [220.0, 536.3, 811.6, 1125.1]
            and P18_HT == P15_GEO_HT)
check('Ⓑ⑧ the paper is in ONE of two states and in no third -- STATE A the superseded '
      'cluster, STATE B P15\'s published arm figures at both sites',
      _STATE_A or _STATE_B, 'STATE B (corrected)' if _STATE_B else 'STATE A (superseded)')

# the consequence, which holds whichever state the paper is in
d_pub = [abs(P15_HT[i] - SKY_HT[i]) / SKY_HT[i] * 100 for i in range(2)] if P15_HT else []
d_geo = [abs(P15_GEO_HT[i] - SKY_HT[i]) / SKY_HT[i] * 100 for i in range(2)] if P15_GEO_HT else []
check('Ⓑ⑨ PINNED THE CONSEQUENCE: against the sky the PUBLISHED heights sit 0.63 and 0.57 '
      'per cent away and the geometric-part pair 3.2 and 3.8, so the superseded cluster '
      'understated the construction\'s own agreement by about five times',
      abs(d_pub[0] - 0.63) < 0.005 and abs(d_pub[1] - 0.57) < 0.005
      and abs(d_geo[0] - 3.15) < 0.05 and abs(d_geo[1] - 3.85) < 0.05,
      f'published {d_pub[0]:.2f}% / {d_pub[1]:.2f}%; geometric {d_geo[0]:.2f}% / {d_geo[1]:.2f}%')
check('Ⓑ⑩ and the published pair is nearer the sky on BOTH ratios, which is why the '
      'attribution mattered rather than being cosmetic',
      d_pub[0] < d_geo[0] and d_pub[1] < d_geo[1],
      f'{d_pub[0]:.2f}<{d_geo[0]:.2f} and {d_pub[1]:.2f}<{d_geo[1]:.2f}')

_comb = re.search(r'a comb of \$([0-9.]+)\$ against the sky\'s \$([0-9.]+)\$', P18)
check('Ⓑ⑪ RECORD the comb 298.5 against 298.4 is NOT a defect: P15 prints both, so P18 '
      'states it as P15 now states it',
      _comb is not None and _comb.group(1) == '298.5' and _comb.group(2) == '298.4'
      and '298.5' in P15 and '298.4' in P15,
      f'{_comb.group(1)} / {_comb.group(2)}, both in P15' if _comb else 'NOT FOUND')

# ---------------------------------------------------------------- Ⓒ defect (2)
print()
print('Ⓒ (2) sec:displace -- the register count, and where it came from')

_rail = re.search(r'an evidence rail of ([a-z\s]+?)\s+receipts', P18)
check('Ⓒ① P18\'s own words for the evidence rail\'s size are PARSED, not retyped',
      _rail is not None, repr(_rail.group(1)) if _rail else 'NOT FOUND')
RAIL = _rail.group(1).strip() if _rail else ''

N_PY = len([1 for d, _, fs in os.walk(os.path.join(ROOT, 'receipts'))
            for f in fs if f.endswith('.py')])
N_ROWS = len([1 for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8')
              if ln.startswith('| ')])
check('Ⓒ② PINNED the live tree carries over twelve hundred receipt files and over twelve '
      'hundred INDEX rows, measured here rather than quoted',
      N_PY > 1200 and N_ROWS > 1200, f'{N_PY} .py files, {N_ROWS} INDEX rows')

_retired = os.path.join(ROOT, 'retired', 'WHAT_THE_FRAMEWORK_DELIVERS.md')
_rtxt = open(_retired, encoding='utf-8').read() if os.path.exists(_retired) else ''
_r684 = re.search(r'(\d+) formal environments\. Fourteen named theorems and six axioms\. '
                  r'(\d+) receipt files', _rtxt)
check('Ⓒ③ PINNED the ONLY other source of that count cluster is a RETIRED document, and it '
      'says 196 environments and 684 receipt files',
      _r684 is not None and _r684.group(1) == '196' and _r684.group(2) == '684',
      f'{_r684.group(1)} environments, {_r684.group(2)} receipt files'
      if _r684 else 'NOT FOUND in retired/')
check('Ⓒ④ PINNED so the retired figure is less than three fifths of the live count, which '
      'is what makes "several hundred" wrong rather than merely round',
      _r684 is not None and int(_r684.group(2)) / N_PY < 0.6,
      f'684 / {N_PY} = {684 / N_PY:.3f}')
check('Ⓒ⑤ the paper is in ONE of two states at that clause and in no third -- STATE A '
      '"several hundred", STATE B a count that covers the live tree',
      RAIL in ('several hundred', 'over twelve hundred'),
      f'STATE {"A (stale)" if RAIL == "several hundred" else "B (corrected)"}: {RAIL!r}')
check('Ⓒ⑥ RECORD the clause is load-bearing rather than decorative: the same paragraph says '
      'the register "is not an illustration but a count"',
      'the register is not an illustration but a count' in P18, 'phrase present')

# ---------------------------------------------------------------- Ⓓ the identities
print()
print('Ⓓ sec:oneradius -- the slice-curvature identity and its locus, recomputed')

ALPHA, M = 1.0, 0.03

def f_sds(r):
    return 1.0 - 2.0 * M / r - r ** 2 / ALPHA ** 2

def fprime(r, h=1e-7):
    return (f_sds(r + h) - f_sds(r - h)) / (2.0 * h)

def K_G(r):
    return 1.0 / ALPHA ** 2 - M / r ** 3

worst = 0.0
for i in range(1, 400):
    r = 0.05 + i * 0.004
    worst = max(worst, abs(-fprime(r) / 2.0 - r * K_G(r)))
check('Ⓓ① PINNED -f\'/2 = r K_G identically, over 400 radii', worst < 1e-6,
      f'max residual {worst:.2e}')

R_FLAT = (M * ALPHA ** 2) ** (1.0 / 3.0)
check('Ⓓ② PINNED both sides vanish at r^3 = M alpha^2',
      abs(K_G(R_FLAT)) < 1e-12 and abs(fprime(R_FLAT)) < 1e-6,
      f'r = {R_FLAT:.6f}, K_G = {K_G(R_FLAT):.2e}')

_rhe = re.search(r'r_\{\\mathrm\{HE\}\} = \(3GM/\\Lambda\s*c\^\{2\}\)\^\{1/3\}', P18)
check('Ⓓ③ the Hubble--Eddington form is PARSED out of P18, and (3GM/Lambda c^2)^(1/3) is '
      '(M alpha^2)^(1/3) because alpha^2 = 3/Lambda',
      _rhe is not None
      and abs((3.0 * M / (3.0 / ALPHA ** 2)) ** (1 / 3) - R_FLAT) < 1e-12,
      'parsed and identical' if _rhe else 'NOT FOUND')

rate2 = lambda r: 2.0 * M / r + r ** 2 / ALPHA ** 2
rmin = min((rate2(0.05 + i * 0.0005) , 0.05 + i * 0.0005) for i in range(1, 2000))[1]
check('Ⓓ④ PINNED the marginal rate 2M/r + r^2/alpha^2 passes its MINIMUM at the same locus',
      abs(rmin - R_FLAT) < 2e-3, f'minimum at {rmin:.4f} against {R_FLAT:.4f}')

R_TA = -((2.0 * M * ALPHA ** 2) ** (1.0 / 3.0))
check('Ⓓ⑤ PINNED and the comoving TURNAROUND is the different locus -(2M alpha^2)^(1/3), '
      'where the rate vanishes', abs(rate2(R_TA)) < 1e-12,
      f'r = {R_TA:.6f}, rate^2 = {rate2(R_TA):.2e}')

# the pencil, and the omega-rotation residue P14 also carries
_pen = re.search(r'r\^\{3\}\+\\alpha\^\{2\}\(c-1\)\\,r\+2M\\alpha\^\{2\}=0', P18)
check('Ⓓ⑥ the pencil is PARSED out of P18', _pen is not None,
      'found' if _pen else 'NOT FOUND')
w = complex(-0.5, math.sqrt(3) / 2)
worst_w = 0.0
for i in range(1, 300):
    r = 0.01 * i
    lhs = (w * r) ** 3 - ALPHA ** 2 * (w * r) + 2 * M * ALPHA ** 2
    rhs = (r ** 3 - ALPHA ** 2 * r + 2 * M * ALPHA ** 2) + ALPHA ** 2 * r * (1 - w)
    worst_w = max(worst_w, abs(lhs - rhs))
check('Ⓓ⑦ PINNED the deck rotation leaves the horizon cubic at alpha^2 r (1 - omega), which '
      'is P14\'s own (omega r)^3 - omega r + 2M = r(1 - omega) in alpha = 1 units',
      worst_w < 1e-12, f'max residual {worst_w:.2e}')

# ---------------------------------------------------------------- Ⓔ the tower
print()
print('Ⓔ the graviton tower\'s floor and its degeneracy')

_mu = re.search(r"tower's floor at \$\\mu_\{2\}=\\sqrt6\$", P18)
check('Ⓔ① the tower floor is PARSED out of P18 as mu_2 = sqrt6', _mu is not None,
      'found' if _mu else 'NOT FOUND')
k2 = lambda L: L * (L + 2) - 2
check('Ⓔ② PINNED k^2 = L(L+2) - 2 at the lowest transverse-traceless member L = 2 gives 6, '
      'so the floor is sqrt6 = 2.449490', k2(2) == 6 and abs(math.sqrt(k2(2)) - 2.449490) < 5e-7,
      f'k^2 = {k2(2)}, mu = {math.sqrt(k2(2)):.6f}')
# ⛔ A MEMBERSHIP TEST IS NOT A PIN.  "ten at the floor" occurs TWICE in the flattened
# paper -- the second split across a line break, so grep, sed and a line-wise count all
# see one -- and `in` is satisfied by either, so changing one site reddened nothing.  The
# COUNT is pinned instead, and the word is PARSED rather than tested for.
_floor = re.findall(r'([a-z]+) at the floor', P18)
_z0 = re.search(r'the spectral zeta at zero is \$([0-9]+)\$ exactly', P18)
check('Ⓔ③ PINNED the floor degeneracy is worded at TWO places, both of them the same '
      'PARSED word, and the one-scale section\'s zeta(0) is that same integer -- a '
      'self-dual and an anti-self-dual five',
      len(_floor) == 2 and len(set(_floor)) == 1 and _z0 is not None
      and WORDS.get(_floor[0]) == int(_z0.group(1)) == 5 + 5,
      f'{_floor} at the floor; zeta(0) = {_z0.group(1) if _z0 else "?"}')
check('Ⓔ④ and L = 2 is the lowest member because k^2 vanishes only at L = 1, which carries '
      'no transverse-traceless content', k2(1) == 1 and k2(0) == -2,
      f'k^2(1) = {k2(1)}, k^2(0) = {k2(0)}')

# ---------------------------------------------------------------- Ⓕ the scales
print()
print('Ⓕ the one-scale ledger\'s own numbers')

MPC, C, HBAR, J_GEV, L_P = 3.0856775814913673e22, 2.99792458e8, 1.054571817e-34, 1.602176634e-10, 1.616255e-35
LAM = 1.1056e-52
al = math.sqrt(3.0 / LAM)
E_al = HBAR * C / al / J_GEV

_dec = re.search(r'\\Lambda_\{\\mathrm\{YM\}\}\\alpha/\\hbar c\\approx([0-9]+)\\times10\^\{([0-9]+)\}', P14)
check('Ⓕ① the gauge-scale ratio is PARSED out of P14, which P18 restates as "forty-one '
      'decades"', _dec is not None,
      f'{_dec.group(1)}e{_dec.group(2)}' if _dec else 'NOT FOUND')
ratio = 0.238 / E_al
check('Ⓕ② PINNED Lambda_MSbar alpha / hbar c = 1.99e41, so log10 = 41.30 and "some '
      'forty-one decades" is right', abs(math.log10(ratio) - 41.30) < 0.05
      and 'forty-one decades' in P18, f'{ratio:.4e}, log10 = {math.log10(ratio):.3f}')

# BOTH exponents are parsed: P14's for alpha/l_P, and P18's own for the gauge count.
_pl = re.search(r'\\alpha/\\ell_P\\sim10\^\{([0-9]+)\}', P14)
_bh = re.search(r'=3\\pi/\\Lambda\\ell_\{P\}\^\{2\}\$, of order \$10\^\{([0-9]+)\}\$', P18)
apl = al / L_P
check('Ⓕ③ PINNED alpha / l_P reproduces P14\'s PARSED exponent, and pi (alpha/l_P)^2 '
      'reproduces P18\'s OWN PARSED exponent for the Bekenstein--Hawking gauge count',
      _pl is not None and _bh is not None
      and abs(math.log10(apl) - int(_pl.group(1))) < 0.25
      and abs(math.log10(math.pi * apl ** 2) - int(_bh.group(1))) < 0.6,
      f'alpha/l_P = {apl:.3e} against P14\'s 10^{_pl.group(1) if _pl else "?"}; '
      f'pi(alpha/l_P)^2 = {math.pi * apl ** 2:.3e} against P18\'s '
      f'10^{_bh.group(1) if _bh else "?"}')
check('Ⓕ④ PINNED and pi(alpha/l_P)^2 = 3 pi / Lambda l_P^2 identically, as P18 writes it',
      abs(math.pi * apl ** 2 / (3.0 * math.pi / (LAM * L_P ** 2)) - 1.0) < 1e-12,
      'identical to 1e-12')

# ---------------------------------------------------------------- Ⓖ cross-paper
print()
print('Ⓖ does P18 state each companion\'s result as that companion NOW states it?')

_ab18 = re.search(r'returns \$Y_p=([0-9.]+)\$ against an observed \$([0-9.]+)\$, '
                  r'\$D/H=([0-9.]+)\\times10\^\{-5\}\$ against \$([0-9.]+)\\times10\^\{-5\}\$', P18)
_ab16 = re.search(r'Y_p = ([0-9.]+)\\ \(\\text\{obs \}([0-9.]+)\),\\qquad D/H = '
                  r'([0-9.]+)\\times10\^\{-5\}\\ \(\\text\{obs \}([0-9.]+)\\times10\^\{-5\}\)', P16)
check('Ⓖ① P18\'s and P16\'s abundance figures are BOTH parsed, from their own sentences',
      _ab18 is not None and _ab16 is not None,
      f'P18 {_ab18.groups() if _ab18 else None} / P16 {_ab16.groups() if _ab16 else None}')
check('Ⓖ② PINNED they agree figure for figure, so the abundances are stated as P16 now '
      'states them', _ab18 is not None and _ab16 is not None
      and _ab18.groups() == _ab16.groups(), 'identical' if (_ab18 and _ab16) else 'unchecked')

_peak18 = re.search(r'the Planck density over \$6\\pi\$ one Planck time before the branch point '
                    r'and free of the progenitor\'s mass', P18)
_peak16 = re.search(r'a density of \$\\rho_\{\\rm Planck\}/6\\pi\$ one Planck time before the '
                    r"branch point and free of the progenitor's mass", P16)
check('Ⓖ③ PINNED the regulated peak is stated in P18 verbatim with P16 -- the density, one '
      'Planck time before the branch point, free of the progenitor\'s mass',
      _peak18 is not None and _peak16 is not None, 'both present')
check('Ⓖ④ RECORD and P18 does NOT restate the throat and extremum radii 69 landed in P16 at '
      'r7835, so there is nothing there to be stale',
      '1.50' not in P18 and '1.89' not in P18 and 'R_s' not in P18,
      'no 1.50, no 1.89, no R_s in P18')

# ⛔ AND THE SAME CLASS AGAIN: `fig in P18 and fig in P14` passed for the lepton-number
# scale while P14 carried it TWICE, so moving one site reddened nothing -- and `in` cannot
# tell a figure in its own role from the same digits somewhere else.  Each of the three is
# PARSED out of ITS OWN SENTENCE in BOTH papers, and the two readings compared as numbers.
_SITES = (
    ('the lepton-number scale',
     r'M\\simeq([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV',
     r'about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV, the Planck-suppressed'),
    ('the nucleosynthesis floor on v_R',
     r'below, at about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV',
     r'needs \$v_R\$ above about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV'),
    ('the doublets\' angle cap',
     r'above, near \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV',
     r"doublets' below about \$([0-9.]+)\\times10\^\{([0-9]+)\}\$\\,GeV"),
)
PARSED = {}
for name, pat18, pat14 in _SITES:
    m18, m14 = re.search(pat18, P18), re.search(pat14, P14)
    v18 = float(m18.group(1)) * 10 ** int(m18.group(2)) if m18 else None
    v14 = float(m14.group(1)) * 10 ** int(m14.group(2)) if m14 else None
    PARSED[name] = v18
    check(f'Ⓖ⑤ PINNED {name} is parsed from its OWN sentence in each paper and the two '
          f'readings are the same number',
          v18 is not None and v14 is not None and v18 == v14,
          f'P18 {v18:.3e} against P14 {v14:.3e}' if (v18 and v14) else
          f'P18 {v18}, P14 {v14}')

V, MNU = 246.0, 0.05e-9
_ln = PARSED['the lepton-number scale']
check('Ⓖ⑥ PINNED and the PARSED lepton-number scale is what a type-I seesaw returns from '
      'the electroweak scale and the measured neutrino mass, v^2/m_nu, to one per cent',
      _ln is not None and abs(V * V / MNU / _ln - 1.0) < 0.01,
      f'v^2/m_nu = {V * V / MNU:.4e} GeV against the papers\' {_ln:.3e}'
      if _ln else 'scale not parsed')
_CAP = PARSED['the doublets\' angle cap']
_FLOOR = PARSED['the nucleosynthesis floor on v_R']
_decades = math.log10(_CAP / _FLOOR)
check('Ⓖ⑥b PINNED COMPUTED and the window the two PARSED bounds leave is five and three '
      'quarter decades wide, so the right-handed scale is bracketed rather than fixed',
      abs(_decades - 5.757) < 0.01,
      f'{_FLOOR:.2e} to {_CAP:.2e} GeV is {_decades:.3f} decades')


_f18 = re.search(r'the three states add at least \$([0-9.]+)\$ to \$N_\{\\rm eff\}\$ '
                 r'whatever the right-handed \$W\$ weighs', P18)
_f16 = re.search(r'light Dirac partners and add at least \$([0-9.]+)\$ to '
                 r'\$N_\{\\mathrm\{eff\}\}\$', P16)
check('Ⓖ⑦ PINNED the N_eff floor is PARSED out of each paper\'s own "add at least" '
      'sentence, the two are the same number, and P18 keeps it a FLOOR -- "whatever the '
      'right-handed W weighs" -- which is what makes it P16\'s result and not a point value',
      _f18 is not None and _f16 is not None
      and float(_f18.group(1)) == float(_f16.group(1))
      ,
      f'P18 {_f18.group(1) if _f18 else "?"} against P16 {_f16.group(1) if _f16 else "?"}, '
      f'stated as a floor in both')

check('Ⓖ⑧ PINNED P18 states the discriminant qualitatively in four places and NEVER writes '
      'the 4-3r_0^2 form, so r7839\'s P14 defect did not propagate',
      len(re.findall(r'discriminant', P18)) == 5 and '4-3r_0^2' not in P18,
      f'{len(re.findall(r"discriminant", P18))} mentions, no 4-3r_0^2 form')

# ---------------------------------------------------------------- Ⓗ the turnover
print()
print('Ⓗ the growth-normalisation pivot')

_piv = re.search(r'\\rho_m/\\rho_\\Lambda=2', P18)
check('Ⓗ① the pivot is PARSED out of P18 as rho_m/rho_Lambda = 2', _piv is not None,
      'found' if _piv else 'NOT FOUND')
# read ONCE: evaluating the same pattern twice reads to the pin operator as a
# disjunction of two arms, which this is not.
_pv = re.search(r'the value \$([0-9]+)/([0-9]+)\$', P18)
check('Ⓗ② PINNED acceleration turns where rho + 3p = 0, i.e. rho_m = 2 rho_Lambda, and the '
      'matter FRACTION there is 2/3 -- the value P18 says the balance is taken about',
      _pv is not None and abs(2.0 / (2.0 + 1.0) - 2.0 / 3.0) < 1e-15
      and [int(g) for g in _pv.groups()] == [2, 3],
      'rho_m = 2 rho_Lambda gives Omega_m = 2/3, which is the PARSED printed pivot')

# ---------------------------------------------------------------- Ⓘ the Virgo chain
print()
print('Ⓘ sec:frontier -- the Virgo gas probe, and the angle recomputed from the radii')

_v18 = re.search(r"resolving Virgo's profile to \$([0-9]+)\^\{\\circ\}\$--"
                 r"\$([0-9]+)\^\{\\circ\}\$ from M87", P18)
_res = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7831_cc66_PO93_the_baryonic_mass_at_virgos_turnaround_radius', 'RESULT.md')
_rtx = open(_res, encoding='utf-8').read() if os.path.exists(_res) else ''
# the computation wraps mid-phrase and quotes with '> ', so it is flattened ONCE here
# and every span read against it below is read against the flattened form.
_RTXF = re.sub(r'\s+', ' ', _rtx.replace('> ', ''))
_vc = re.search(r"Virgo's infall region out to `≈ ([0-9]+)°`–`([0-9]+)°` from M87", _RTXF)
check('Ⓘ① PINNED the gas-probe angles are PARSED out of BOTH P18 and the r7831 computation '
      'and are the same pair -- not tested for membership, which passed on the wrong '
      'figures once already',
      _v18 is not None and _vc is not None and _v18.groups() == _vc.groups(),
      f'P18 {_v18.groups() if _v18 else None} against the computation '
      f'{_vc.groups() if _vc else None}')
check('Ⓘ② PINNED and the computation says "out to" that angle, an OUTER RADIUS, which is '
      'what P18 renders -- so P18 is right here and this is not a defect of P18\'s',
      'infall region out to `≈ 24°`–`26°` from M87' in _RTXF,

      'computation says "out to", matching P18')

# the angle is DERIVABLE from the two radii P18 prints in the same passage, so the three
# figures pin each other instead of resting on the citation alone.
_core = re.search(r'between the \$([0-9.]+)\$~Mpc core and the \$([0-9]+)\$~Mpc of the '
                  r'infall region', P18)
_dist = re.search(r'([0-9.]+)`? Mpc', '')  # placeholder, Virgo's distance is parsed below
_D = re.search(r'arctan\(([0-9.]+)/([0-9.]+)\)', _rtx)
check('Ⓘ③ P18\'s core and infall radii are PARSED out of its own Virgo sentence, and the '
      'distance the computation projects them at is parsed out of the computation',
      _core is not None and _D is not None,
      f'core {_core.group(1)} Mpc, infall {_core.group(2)} Mpc, '
      f'distance {_D.group(2)} Mpc' if (_core and _D) else 'NOT FOUND')
if _core and _D and _v18:
    R_CORE, R_INF, DIST = float(_core.group(1)), float(_core.group(2)), float(_D.group(2))
    a_inf = math.degrees(math.atan(R_INF / DIST))
    a_core = math.degrees(math.atan(R_CORE / DIST))
    r_outer = math.tan(math.radians(int(_v18.group(2)))) * DIST
    check('Ⓘ④ PINNED COMPUTED the probe\'s LOWER angle is the angular size of the infall '
          'radius P18 prints, at the distance the computation projects from -- so the '
          'angle is derived from the radii rather than only cited',
          abs(a_inf - int(_v18.group(1))) < 0.2,
          f'arctan({R_INF}/{DIST}) = {a_inf:.2f} deg against the printed '
          f'{_v18.group(1)} deg')
    check('Ⓘ⑤ PINNED COMPUTED and the UPPER angle reaches just past that edge rather than '
          'anywhere else, which is what makes the pair a span and not two readings',
          R_INF < r_outer < R_INF * 1.15,
          f'tan({_v18.group(2)} deg) x {DIST} = {r_outer:.2f} Mpc against the infall '
          f'edge {R_INF} Mpc')
    check('Ⓘ⑥ PINNED COMPUTED and the CORE radius subtends the few degrees the existing '
          'reach covers, which is the contrast the open item rests on',
          abs(a_core - 6.86) < 0.05 and a_core < int(_v18.group(1)) / 3.0,
          f'arctan({R_CORE}/{DIST}) = {a_core:.2f} deg, against a probe at '
          f'{_v18.group(1)}-{_v18.group(2)} deg')

_rcp = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_stellar_half_of_po93s_gate_is_measured_at_the_turnaround_radius'
                    '_and_the_gas_half_is_not.py')
_rcx = open(_rcp, encoding='utf-8').read() if os.path.exists(_rcp) else ''
check('Ⓘ⑦ RECORD the looser statement is the RECEIPT\'s, whose print line calls the same '
      '24-26 degrees a WIDTH where the computation makes it an outer radius -- recorded and '
      'routed, not P18\'s to answer -- OR, STATE B, repaired at r7843 (69) to an outer radius',
      ('24-26 deg wide' in _rcx) or ('out to ~24-26 deg from M87' in _rcx),
      'receipt print line says "wide"' if '24-26 deg wide' in _rcx else 'repaired: "out to ... from M87"')

# ⛔ WHAT WAS HERE BEFORE WAS NOT A CHECK.  Four arms asserted that the Virgo bound figures
# 1.70, 2.35, 1.85 and 6.4 were "printed identically in P18 and in JanzenSlicing", on `in`
# tests -- and P18 DOES NOT PRINT THAT RATIO AT ALL.  Its 1.70 is the damping exponent on
# the power in the acoustic section.  The arms passed on unrelated digits in both files.
# Replaced above, and the true statement is pinned instead:
_virgo_only = [n for n in ('$1.9$~Mpc', 'under a fifth of the baryons', 'past $1.2$~Mpc')
               if n in P18 and not any(n in t for t in (P15, P16, P14))]
check('Ⓘ⑧ RECORD P18 is the SOLE corpus carrier of its Virgo profile figures, so they rest '
      'on their external citations and no companion can be compared against -- stated '
      'rather than papered over with an `in` test that would pass on any digits',
      len(_virgo_only) == 3, f'{len(_virgo_only)}/3 carried only by P18')

# ---------------------------------------------------------------- Ⓙ the absolute pins
print()
print('Ⓙ every figure this revision PRINTS, pinned against its own value')

# ⛔ WHY THIS SECTION EXISTS AND IS NOT REDUNDANT.  Every arm above compares one PARSED
# reading against another, which is what the order asks: does P18 state the companion's
# result as the companion NOW states it.  But a RELATIONAL pin passes if BOTH sides drift
# TOGETHER -- rewrite P15 and P18 to the same wrong cluster and Ⓑ⑧ stays green.  And a
# figure this revision prints beside its own citation claims the receipt would FAIL if it
# were wrong.  So each is pinned here against its value, well inside half its last digit.
#   ⌗ Written UNROLLED, with every figure INLINE.  A first cut held them in tuples and
#     compared `TUPLE[i]` in a loop; check_figures_pinned substitutes a NAMED SCALAR but
#     not a tuple element, so all nineteen still read UNPINNED while the receipt was green.
#     The gate was right to: a loop over a tuple is harder for a READER to check too.
_A = P15_ARM if len(P15_ARM) == 4 else [0.0] * 4
_H = P15_HT if len(P15_HT) == 2 else [0.0] * 2
_S = SKY_HT if len(SKY_HT) == 2 else [0.0] * 2
_G = P15_GEO_HT if len(P15_GEO_HT) == 2 else [0.0] * 2
_V = [float(g) for g in _p15grid.groups()] if _p15grid else [0.0] * 4
_R = [round(v, 1) for v in _V]

check('Ⓙ① PINNED P15 publishes its first peak at 220.2', abs(_A[0] - 220.2) < 1e-9, f'{_A[0]}')
check('Ⓙ① PINNED P15 publishes its second peak at 536.9', abs(_A[1] - 536.9) < 1e-9, f'{_A[1]}')
check('Ⓙ① PINNED P15 publishes its third peak at 811.2', abs(_A[2] - 811.2) < 1e-9, f'{_A[2]}')
check('Ⓙ① PINNED P15 publishes its fourth peak at 1123.9', abs(_A[3] - 1123.9) < 1e-9, f'{_A[3]}')
check('Ⓙ② PINNED P15 publishes P1/P2 at 2.207', abs(_H[0] - 2.207) < 1e-9, f'{_H[0]}')
check('Ⓙ② PINNED P15 publishes P1/P3 at 2.249', abs(_H[1] - 2.249) < 1e-9, f'{_H[1]}')
check('Ⓙ③ PINNED the sky\'s P1/P2 is 2.221', abs(_S[0] - 2.221) < 1e-9, f'{_S[0]}')
check('Ⓙ③ PINNED the sky\'s P1/P3 is 2.262', abs(_S[1] - 2.262) < 1e-9, f'{_S[1]}')
check('Ⓙ④ PINNED the geometric part\'s P1/P2 is 2.291', abs(_G[0] - 2.291) < 1e-9, f'{_G[0]}')
check('Ⓙ④ PINNED the geometric part\'s P1/P3 is 2.349', abs(_G[1] - 2.349) < 1e-9, f'{_G[1]}')
check('Ⓙ⑤ PINNED the geometric part\'s comb is 299.1',
      _p15geo is not None and abs(float(_p15geo.group(1)) - 299.1) < 1e-9,
      f'{_p15geo.group(1) if _p15geo else "?"}')
check('Ⓙ⑥ PINNED the grid-convergence run\'s first peak is 220.03', abs(_V[0] - 220.03) < 1e-9, f'{_V[0]}')
check('Ⓙ⑥ PINNED the grid-convergence run\'s second peak is 536.27', abs(_V[1] - 536.27) < 1e-9, f'{_V[1]}')
check('Ⓙ⑥ PINNED the grid-convergence run\'s third peak is 811.58', abs(_V[2] - 811.58) < 1e-9, f'{_V[2]}')
check('Ⓙ⑥ PINNED the grid-convergence run\'s fourth peak is 1125.02', abs(_V[3] - 1125.02) < 1e-9, f'{_V[3]}')
check('Ⓙ⑦ PINNED COMPUTED the grid run\'s first three peaks round to 220.0, 536.3 and '
      '811.6 -- EXACTLY the first three the paper printed, which is what identifies the '
      'superseded cluster\'s source',
      abs(_R[0] - 220.0) < 1e-9 and abs(_R[1] - 536.3) < 1e-9 and abs(_R[2] - 811.6) < 1e-9,
      f'{_R[:3]}')
check('Ⓙ⑧ PINNED COMPUTED and the FOURTH rounds to 1125.0, where the paper printed 1125.1 '
      '-- one unit in the last printed place above it. ** So the superseded cluster was '
      'three grid figures rounded and a MIS-ROUNDED fourth, not a clean copy of anything. **',
      abs(_R[3] - 1125.0) < 1e-9 and abs(1125.1 - _R[3] - 0.1) < 1e-9,
      f'grid rounds to {_R[3]}, paper printed 1125.1')
check('Ⓙ⑨ PINNED the comb is 298.5 against the sky\'s 298.4',
      _comb is not None and abs(float(_comb.group(1)) - 298.5) < 1e-9
      and abs(float(_comb.group(2)) - 298.4) < 1e-9,
      f'{_comb.group(1) if _comb else "?"} / {_comb.group(2) if _comb else "?"}')
check('Ⓙ⑩ PINNED and a JOINT drift is what these arms catch and the relational ones do '
      'not: P18\'s cluster is pinned to P15\'s published one AND P15\'s to its own value, '
      'so rewriting both to one wrong cluster reddens HERE even while Ⓑ⑧ stays green',
      P18_PK == [220.2, 536.9, 811.2, 1123.9]
      or P18_PK == [220.0, 536.3, 811.6, 1125.1],
      f'P18 carries {P18_PK}')

print()
if FAILED:
    print(f'FAILED {len(FAILED)}:')
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('ALL PASS')
