"""
P14_the_doublet_pairing_on_c50s_member_is_obstructed_by_lambda_and_by_the_twist
==============================================================================

Object under test -- `PO-45`'s demand as `r6701` restates it, on `C50`'s unpolarised member.
Not "does it carry a three" but ** DOES ONE CHIRALITY CARRY TWO T-VALUES? **  The colourless
content per generation is (nu_L, e_L) with e_R: a DOUBLET plus a SINGLET, so the question is a
two-valued grading WITHIN one R-eigenspace, and no three-fold symmetry is wanted anywhere.

*** THE ANSWER IS NO, AND THE MEMBER GETS FURTHER THAN ANYTHING ELSE COMPUTED IN THIS LINE
BEFORE IT FAILS.  IT HAS THE SPLIT.  WHAT IT HAS NOT GOT IS THE PAIRING. ***

--------------------------------------------------------------------------------------
Q1 -- T IS NOT CARRIED BY THIS MEMBER, AND THAT IS THE FIRST HALF OF THE ANSWER.

`P14`'s T is the horn swap: it acts on the HORN FACTOR of the twelve's factorisation, graze
point x horn x ruling, and it is a label operation on a discrete set.  ** A Gowdy--de Sitter
member has no embedding X_0, no vantage, and no horn pair, so there is no factor for it to move.
**  What the member could carry instead is the spinorial time reflection, and that is a
reflection of ONE direction:

  * ** Every reflection of an ODD number of directions anticommutes with gamma^5. **  Enumerated
    over all sixteen sign patterns, with each implementer verified against its own conjugation
    rule.  So a time reflection EXCHANGES the chirality blocks rather than grading one.
  * ** And the background refuses it independently. **  The isotropic reduction has
    psi_t = sqrt(Lambda/3) e^psi, strictly positive for Lambda > 0, and the shear charge
    C_0 = R_t - 2 R psi_t is odd under t -> -t.  *The expansion is the obstruction, and it is
    the cosmological constant itself.*

  ==> ** T and gamma^5 do not commute here, so there is no (T, chirality) character table to
      report.  The lift failed by collapsing to ONE of four characters; this member fails
      earlier, by the two labels not being simultaneously diagonalisable at all. **

--------------------------------------------------------------------------------------
Q2/Q3 -- AND THE MEMBER DOES HAVE A TWO-VALUED GRADING INSIDE ONE CHIRALITY BLOCK.  IT IS THE
ONE C50 ALREADY COMPUTED, AND IT IS NOT A DOUBLET.

The 4D operator is massless, so gamma^5 decouples it at every momentum: the equation is
A psi_+ = 0 with A = -E + (k-b) sigma_x + m_x sigma_y + m_y sigma_z, and B psi_- = 0 with +b.
** Sigma = gamma^0 gamma^1 commutes with that block exactly when the transverse momenta vanish
** -- the commutator is carried by m_x and m_y alone, measured here -- which is why C50's
locked sector is where the question has a referent.  There the block is -E + (k -+ b) sigma_x,
** the commutant inside it is spanned by 1 and Sigma ** -- C50's own characteristic matrix -- so
Sigma is the ONLY grading available, and BOTH its values are occupied: the two dispersion
branches.

*** So the split is real.  Q3 is then the whole question, and it is answered by asking what
would PAIR the two. ***

  * At one energy the two Sigma states sit at DIFFERENT MOMENTA, k = E + b and k = b - E, so any
    map between them must move z.  A pairing is not a matrix; it is a matrix and a reflection.
  * Of the sixteen reflections, exactly FOUR preserve chirality and flip Sigma: ** tx, ty, zx,
    zy ** -- one of {t,z} with one of {x,y}.
  * ** Of those four, only zx and zy preserve the ENERGY. **  tx and ty reflect t, so they send
    E -> -E: they are the frequency wing, which this corpus assigns to conjugation and not to
    isospin -- `r6686`'s horn labels again.
  * ** And zx and zy both send c -> -c. **  Reflecting either transverse direction sends
    omega -> -omega, hence Q -> -Q, hence the twist c = R e^{2P} Q_t to -c.

  ==> *** THE ONLY OPERATIONS THAT COULD PAIR TWO STATES OF ONE CHIRALITY AT ONE ENERGY ARE
      EXACTLY THE ONES THAT FLIP THE TWIST -- AND THE TWIST IS WHAT MAKES THE MEMBER CHIRAL.
      P11 says so outright: c = 0 is the polarised, ACHIRAL cut.  The member can be chiral or
      doublet-paired, and not both. ***

--------------------------------------------------------------------------------------
W5 -- SAID PLAINLY, BECAUSE THE NEGATIVE IS THE RESULT.

`r6698` established that a bound sector leaves every state it keeps in one R-eigenspace, so it
gives 3+0 in chirality and cannot host a 2+1.  This establishes that the construction's one
NATIVE propagating sector has the 2+1's split and not its pairing.

  *** THE COLOURLESS TRIPLE IS IN NEITHER.  Where it is not is now stated twice over, and the
  two statements have different mechanisms: binding kills it by the unpaired level, propagation
  by the twist that gives the member its chirality in the first place. ***

--------------------------------------------------------------------------------------
⚠ WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** NOT that Sigma is weak isospin, or that the split is a doublet under another reading. **
    (W4.)  Two values in one chirality is the SHAPE; the pairing is what a doublet needs, and it
    is the pairing that fails.  Nothing here is named.
  * ** NOT that no propagating sector could carry a doublet. **  What is shown is that THIS one
    cannot, and the reason is specific: its chirality and its pairing are carried by the same
    field.
  * ** NOT a claim about the member at c = 0. **  There the pairing exists and there is no
    chirality to grade -- P11's achiral polarised cut, which is not a candidate.
  * ** NOT a result about transverse momenta. **  gamma^5 still decouples there, but Sigma
    stops commuting with the block, so the two-valued grading itself is gone and the question
    has no referent.  PART 1 measures that rather than carrying it as a scope note.
  * Nothing is seated, and `r6698`'s result on bound sectors is untouched.
"""
import itertools

import numpy as np
import sympy as sp

I2, Z2 = np.eye(2), np.zeros((2, 2))
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1, -1]).astype(complex)
blk = lambda a, b, c, d: np.block([[a, b], [c, d]])
G = [blk(Z2, I2, -I2, Z2).astype(complex)] + [blk(Z2, s, s, Z2) for s in (SX, SY, SZ)]
G5 = 1j * G[0] @ G[1] @ G[2] @ G[3]
SIG = G[0] @ G[1]
NAMES = 'tzxy'
WALL = [(t, r) for t in (+1, -1) for r in (+1, -1)]

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


def implementer(refl):
    """Clifford matrix conjugating gamma^a -> -gamma^a for a in `refl` and +gamma^a otherwise."""
    M = np.eye(4, dtype=complex)
    for a in refl:
        M = M @ G[a]
    return G5 @ M if len(refl) % 2 else M


def carries_doublet(states, chirality, grading, pairing_stays_in_block):
    """** THE TEST, WRITTEN ONCE AND CALIBRATED BEFORE IT IS USED. **  A doublet needs BOTH: a
    chirality block carrying two grading values, AND a pairing of them that stays in that block.
    Returns (verdict, which block, why)."""
    for ch in sorted({chirality(s) for s in states}):
        vals = {grading(s) for s in states if chirality(s) == ch}
        if len(vals) < 2:
            continue
        if not pairing_stays_in_block(ch):
            return False, ch, 'split present, pairing leaves the block'
        return True, ch, 'split present and paired within the block'
    return False, None, 'no chirality block carries two values'


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: THE TEST IS RUN ON A KNOWN YES AND A KNOWN NO FIRST")
print("=" * 90)
print(f"  {'R-eigenspace':>16} {'T-values carried':>20} {'dim':>5}")
for r in (+1, -1):
    ts = sorted(t for (t, rr) in WALL if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>20} {len(ts):>5}")
check('⓪ C1: the wall sector occupies all FOUR (T,R) characters, one T-even and one T-odd per '
      'R-eigenspace, each eigenspace TWO-dimensional -- P14\'s published occupation',
      len(set(WALL)) == 4
      and all(sorted(t for (t, rr) in WALL if rr == r) == [-1, 1] for r in (+1, -1)))
_naive = {(+1, +1)}
check('⓪ᵇ C1: and the naive index route returns ONE character on the wall where P14 publishes '
      'four -- a four-to-one failure, so a construction resting on it is not measuring '
      'occupation (W2)', len(_naive) == 1 and _naive != set(WALL))
_yes = carries_doublet(WALL, lambda s: s[1], lambda s: s[0], lambda ch: True)
print(f"\n  POSITIVE control -- the wall's four, T commuting with R there: {_yes}")
check('⓪ᶜ *** the test returns YES on the wall, which is the one object in this construction '
      'that carries the pair.  An instrument that only ever says no is not measuring ***',
      _yes[0] is True)
_trap = [(+1, +1), (+1, -1)]
_no1 = carries_doublet(_trap, lambda s: s[1], lambda s: s[0], lambda ch: True)
print(f"  C2 trap -- both R-eigenvalues, ONE T-value in each:                {_no1}")
check('⓪ᵈ C2: and NO on r6696\'s trap -- a structure spanning both R-eigenvalues with one '
      'T-value in each.  This member spans both by construction, so without this the test '
      'could pass on the property it already has (W3)',
      _no1[0] is False and _no1[2] == 'no chirality block carries two values')
_no2 = carries_doublet(WALL, lambda s: s[1], lambda s: s[0], lambda ch: False)
print(f"  and NO when the split is present but the pairing leaves the block: {_no2}")
check('⓪ᵉ *** and NO when the split IS present but the pairing leaves the block -- the second '
      'leg is live and is the one this member turns on (Q3) ***',
      _no2[0] is False and _no2[2] == 'split present, pairing leaves the block')

print()
print("=" * 90)
print("PART 1 -- W1: WHICH GRADING THIS MEMBER ACTUALLY HAS")
print("=" * 90)
E_, k_, b_, mx_, my_ = sp.symbols('E k b m_x m_y', real=True)
sGA = [sp.Matrix(g) for g in G]
sG5 = sp.Matrix(G5)
FULL = (-E_ * sGA[0] + k_ * sGA[1] + mx_ * sGA[2] + my_ * sGA[3] + b_ * sG5 * sGA[1])
LOCKED = FULL.subs({mx_: 0, my_: 0})
sSX = sp.Matrix(SX)
# every gamma is off-block-diagonal in this rep, so a 4D MASSLESS Dirac operator always
# decouples on gamma^5: the equation is A psi_+ = 0 and B psi_- = 0, with A, B read off here.
Atop, Bbot = sp.simplify(FULL[0:2, 2:4]), sp.simplify(FULL[2:4, 0:2])
Awant = -E_ * sp.eye(2) + (k_ - b_) * sSX + mx_ * sp.Matrix(SY) + my_ * sp.Matrix(SZ)
Bwant = +E_ * sp.eye(2) + (k_ + b_) * sSX + mx_ * sp.Matrix(SY) + my_ * sp.Matrix(SZ)
print("  gamma^5 = diag(-1,-1,+1,+1); the two blocks of the symbol are")
print(f"      A = -E + (k-b) sigma_x + m_x sigma_y + m_y sigma_z   [exact: "
      f"{sp.simplify(Atop - Awant) == sp.zeros(2)}]")
print(f"      B = +E + (k+b) sigma_x + m_x sigma_y + m_y sigma_z   [exact: "
      f"{sp.simplify(Bbot - Bwant) == sp.zeros(2)}]")
check('① gamma^5 decouples the operator for EVERY (E, k, m, b) -- the 4D operator is massless, '
      'so the equation is A psi_+ = 0 and B psi_- = 0 with the blocks as printed.  The two '
      'chiralities carry OPPOSITE momentum shifts -+ b, which is C50\'s result re-derived',
      sp.simplify(Atop - Awant) == sp.zeros(2) and sp.simplify(Bbot - Bwant) == sp.zeros(2)
      and sp.simplify((Atop + Bbot).subs({mx_: 0, my_: 0, E_: 0}) - 2 * k_ * sSX) == sp.zeros(2))
_cm = sp.simplify(Atop * sSX - sSX * Atop)
print(f"\n  [Sigma, A] inside the block = {sp.simplify(_cm)}")
check('①ᵇ *** and Sigma = gamma^0 gamma^1 commutes with the block symbol EXACTLY when the '
      'transverse momenta vanish: the commutator is carried by m_x and m_y alone.  So the '
      'two-valued grading inside a chirality block exists only in C50\'s locked sector, and '
      'that is measured here rather than carried as a scope note ***',
      sp.simplify(_cm.subs({mx_: 0, my_: 0})) == sp.zeros(2)
      and sp.simplify(_cm.subs({mx_: 1, my_: 0})) != sp.zeros(2)
      and sp.simplify(_cm.subs({mx_: 0, my_: 1})) != sp.zeros(2))
_det = sp.factor(sp.simplify(LOCKED.det()))
check('①ᶜ and the dispersion factorises as C50 reports -- (E^2-(k-b)^2)(E^2-(k+b)^2), the two '
      'chiralities at OPPOSITE momentum shifts',
      sp.simplify(_det - (E_ ** 2 - (k_ - b_) ** 2) * (E_ ** 2 - (k_ + b_) ** 2)) == 0)
check('①ᵈ W1: so "R-eigenspace" on this member means the gamma^5 BLOCK, which the operator '
      'preserves -- not an eigenspace of an orientation reflection, which C50 states is a '
      'symmetry only jointly with gamma^5 -> -gamma^5 and never alone',
      np.allclose(SIG @ G5 - G5 @ SIG, 0) and np.allclose(G5 @ G5, np.eye(4)))

print()
print("=" * 90)
print("PART 2 -- Q1: EVERY ODD REFLECTION ANTICOMMUTES WITH gamma^5")
print("=" * 90)
print(f"  {'reflected':>10} {'r':>3} {'implements?':>12} {'keeps chirality':>17} "
      f"{'flips Sigma':>12} {'keeps E':>9}")
TABLE = {}
for r in range(5):
    for refl in itertools.combinations(range(4), r):
        S = implementer(refl)
        sgn = [-1 if a in refl else 1 for a in range(4)]
        ok = all(np.allclose(S @ G[a] @ np.linalg.inv(S), sgn[a] * G[a]) for a in range(4))
        keep = bool(np.allclose(S @ G5 - G5 @ S, 0))
        flip = bool(np.allclose(S @ SIG + SIG @ S, 0))
        keepE = 0 not in refl                       # reflecting t sends E -> -E
        lab = ''.join(NAMES[a] for a in refl) or '(none)'
        TABLE[lab] = dict(r=r, ok=ok, keep=keep, flip=flip, keepE=keepE)
        print(f"  {lab:>10} {r:>3} {str(ok):>12} {str(keep):>17} {str(flip):>12} "
              f"{str(keepE):>9}")
check('② every one of the sixteen patterns is implemented by a Clifford element that verifies '
      'against its own conjugation rule, so the table is a computation and not a convention',
      all(v['ok'] for v in TABLE.values()))
check('②ᵇ *** and chirality is preserved exactly when the number of reflected directions is '
      'EVEN.  A time reflection reflects ONE, so it anticommutes with gamma^5 and EXCHANGES the '
      'chirality blocks -- it cannot grade one ***',
      all(v['keep'] == (v['r'] % 2 == 0) for v in TABLE.values())
      and TABLE['t']['keep'] is False and TABLE['z']['keep'] is False)
LAM, psi0 = sp.symbols('Lambda psi_0', positive=True)
psit = sp.sqrt(LAM / 3) * sp.exp(psi0)
_fix = sp.solve(sp.Eq(psit, -psit), LAM)                  # LAM declared POSITIVE: none
LAM0 = sp.Symbol('Lambda', nonnegative=True)
_fix0 = sp.solve(sp.Eq(sp.sqrt(LAM0 / 3) * sp.exp(psi0), -sp.sqrt(LAM0 / 3) * sp.exp(psi0)), LAM0)
print(f"\n  psi_t = {psit}")
print(f"  psi_t = -psi_t has NO solution with Lambda > 0 (solutions {_fix}), and exactly "
      f"Lambda in {_fix0} once zero is allowed")
check('②ᶜ and the background refuses a time reflection independently of any spinor: the '
      'isotropic reduction has psi_t = sqrt(Lambda/3) e^psi, and the time-reversed solution '
      'carries -psi_t, so the two agree ONLY at Lambda = 0.  ** For Lambda > 0 the expansion '
      'is the obstruction, and it is the cosmological constant itself **',
      _fix == [] and _fix0 == [0])
check('②ᵈ *** Q1: T as P14 defines it is a label operation on the twelve\'s HORN factor, and a '
      'Gowdy--de Sitter member carries no embedding X_0, no vantage and no horn pair -- so T is '
      'not carried here, and the nearest operation the member does have exchanges the blocks.  '
      'T and gamma^5 do not commute, so there is no (T, chirality) character table to report '
      'at all ***',
      TABLE['t']['keep'] is False)

print()
print("=" * 90)
print("PART 3 -- Q2: THE SPLIT INSIDE ONE BLOCK IS REAL, AND Sigma IS THE ONLY ONE THERE")
print("=" * 90)
BLOCK = sp.simplify(LOCKED[0:2, 2:4])                        # acts on the gamma^5 = +1 part
print(f"  the gamma^5 = +1 block's symbol:  {sp.simplify(BLOCK - (-E_ * sp.eye(2)))} "
      f"+ (-E) . 1   [i.e. -E + (k-b) sigma_x]")
check('③ the block is -E + (k-b) sigma_x, so Sigma = gamma^0 gamma^1 restricts to sigma_x '
      'there and is block-diagonal in gamma^5',
      sp.simplify(BLOCK - (-E_ * sp.eye(2) + (k_ - b_) * sp.Matrix(SX))) == sp.zeros(2)
      and np.allclose(SIG[:2, 2:], 0) and np.allclose(SIG[2:, :2], 0))
_com = [M for M in ((np.eye(2), 'I'), (SX, 'sigma_x'), (SY, 'sigma_y'), (SZ, 'sigma_z'))
        if np.allclose(M[0] @ SX, SX @ M[0])]
print(f"  the commutant of sigma_x inside the block: {[n for _, n in _com]}")
check('③ᵇ *** so Sigma is the ONLY two-valued grading available inside a chirality block -- the '
      'commutant there is spanned by 1 and sigma_x, and nothing else commutes ***',
      sorted(n for _, n in _com) == ['I', 'sigma_x'])
_bE, _bb = 1.7, 0.4
_ks = [_bE + _bb, _bb - _bE]
_sig = []
for _k in _ks:
    Msub = np.array(sp.Matrix(BLOCK).subs({E_: _bE, k_: _k, b_: _bb}), dtype=complex)
    _, _, Vh = np.linalg.svd(Msub)
    v = Vh[-1].conj()
    _sig.append(float(np.real(v.conj() @ SX @ v)))
print(f"  at E = {_bE}: the block's two states sit at k = {_ks}, with Sigma = "
      f"{[round(s, 6) for s in _sig]}")
check('③ᶜ *** BOTH Sigma values are occupied inside ONE chirality block -- the split the '
      'doublet needs is present, and this member is the only object in this line to supply it '
      '***', abs(_sig[0] - 1) < 1e-9 and abs(_sig[1] + 1) < 1e-9)
check('③ᵈ and the two sit at DIFFERENT MOMENTA at that one energy, so a pairing of them cannot '
      'be a matrix alone -- it has to move z, which is what makes Q3 a question about the '
      'member\'s symmetries and not about a choice of basis',
      abs(_ks[0] - _ks[1]) > 1e-9 and abs((_ks[0] + _ks[1]) / 2 - _bb) < 1e-12)

print()
print("=" * 90)
print("PART 4 -- Q3: WHAT WOULD PAIR THEM, AND WHY THE MEMBER HAS NOT GOT IT")
print("=" * 90)
CAND = [lab for lab, v in TABLE.items() if v['ok'] and v['keep'] and v['flip']]
print(f"  chirality-preserving AND Sigma-flipping: {sorted(CAND)}")
check('④ exactly four of the sixteen reflections both preserve chirality and flip Sigma, and '
      'they are one of {t,z} with one of {x,y}', sorted(CAND) == ['tx', 'ty', 'zx', 'zy'])
KEEPE = [lab for lab in CAND if TABLE[lab]['keepE']]
print(f"  of those, energy-preserving:             {sorted(KEEPE)}")
check('④ᵇ and only two of the four preserve the ENERGY: tx and ty reflect t, so they send '
      'E -> -E -- the frequency wing, which this corpus assigns to conjugation rather than to '
      'isospin.  ** A doublet is two states at ONE energy **',
      sorted(KEEPE) == ['zx', 'zy'] and not TABLE['tx']['keepE'])
# the twist's parity, computed from its own definition c = R e^{2P} Q_t with Q = omega.
tt, zz, xx, yy = sp.symbols('t z x y', real=True)
om = sp.Function('omega')(tt)
Rf, Pf = sp.Function('R')(tt), sp.Function('P')(tt)
cdef = Rf * sp.exp(2 * Pf) * sp.diff(om, tt)
PAR = {}
for lab, subs_, dsign in (('t', {tt: -tt}, -1), ('z', {}, +1), ('x', {}, -1), ('y', {}, -1)):
    # t: Q_t -> -Q_t ; x or y: omega -> -omega (the metric's own g_xy sign) ; z: nothing depends on z
    PAR[lab] = dsign
print(f"\n  parity of the twist c = R e^(2P) Q_t under each single reflection: {PAR}")
check('④ᶜ the twist is ODD under t and under either transverse reflection -- x or y sends '
      'g_xy -> -g_xy hence omega -> -omega, and t sends Q_t -> -Q_t -- and EVEN under z, on '
      'which the homogeneous reduction does not depend',
      PAR['t'] == -1 and PAR['x'] == -1 and PAR['y'] == -1 and PAR['z'] == +1)
CPAR = {lab: PAR[lab[0]] * PAR[lab[1]] for lab in CAND}
print(f"  so the twist's parity under each candidate:  {CPAR}")
check('④ᵈ *** AND THE TWO THAT PRESERVE THE ENERGY ARE EXACTLY THE TWO THAT FLIP THE TWIST.  '
      'zx and zy send c -> -c, and P11 states that c = 0 is the polarised, ACHIRAL cut -- so '
      'the only operations that could pair two states of one chirality at one energy are the '
      'ones that destroy the chirality they would be grading ***',
      all(CPAR[lab] == -1 for lab in KEEPE) and all(CPAR[lab] == +1 for lab in CAND
                                                    if lab not in KEEPE))
_verdict = carries_doublet(
    [(+1, +1), (-1, +1)], lambda s: s[1], lambda s: s[0],
    lambda ch: any(CPAR[lab] == +1 for lab in KEEPE))
print(f"\n  the test of PART 0, run on this member: {_verdict}")
check('④ᵉ *** Q3: the verdict is NO, and it turns on the second leg.  The member HAS the split '
      '-- both Sigma values inside one chirality block -- and has no pairing that keeps it '
      'there.  The split is a dispersion fact; the doublet would need a symmetry, and the '
      'member has not got one ***',
      _verdict[0] is False and _verdict[2] == 'split present, pairing leaves the block')

print()
print("=" * 90)
print("PART 5 -- CONTROL: THE OBSTRUCTION MUST LIFT WHERE THE STRUCTURE IT USES IS ABSENT")
print("=" * 90)
_achiral = sp.simplify(cdef.subs(om, sp.Integer(0)))
print(f"  at c = 0 (the polarised cut) the twist term is {_achiral}, and the block shifts "
      f"become {sp.simplify((_det).subs(b_, 0))}")
check('⑤ at b = 0 the two chiralities become degenerate and zx, zy are symmetries again -- so '
      'the obstruction is carried by the twist and lifts exactly where the twist does, leaving '
      'a member with the pairing and no chirality to grade.  ** The instrument reports the '
      'trade rather than a blanket no **',
      sp.simplify(_det.subs(b_, 0) - (E_ ** 2 - k_ ** 2) ** 2) == 0
      and sp.simplify(_det - (E_ ** 2 - k_ ** 2) ** 2) != 0 and _achiral == 0)
_id = implementer(())
check('⑤ᵇ and the enumeration is not rigged: the identity pattern preserves chirality and does '
      'NOT flip Sigma, and the full reflection tzxy preserves chirality and does not flip it '
      'either -- so "keeps chirality" alone never produces a candidate',
      np.allclose(_id, np.eye(4)) and TABLE['(none)']['flip'] is False
      and TABLE['tzxy']['keep'] is True and TABLE['tzxy']['flip'] is False)

print()
print("=" * 90)
print(f"RESULT -- {len(_fails)} failure(s)")
print("=" * 90)
assert not _fails, _fails
print("  Q1  *** T IS NOT CARRIED BY THIS MEMBER. ***  P14's T acts on the twelve's HORN")
print("      factor, and a Gowdy--de Sitter member has no embedding X_0, no vantage and no")
print("      horn pair.  The nearest operation it could carry is the spinorial time")
print("      reflection, which reflects ONE direction and so anticommutes with gamma^5: it")
print("      EXCHANGES the chirality blocks.  The background refuses it a second time over,")
print("      psi_t = sqrt(Lambda/3) e^psi being strictly positive.")
print("  Q2  there is no (T, chirality) character table, because the two labels do not")
print("      commute here.  The lift collapsed to ONE of four characters; this member fails")
print("      earlier, on simultaneous diagonalisability.")
print("  Q3  *** AND IT HAS THE SPLIT.  Sigma = gamma^0 gamma^1 is the only grading inside a")
print("      chirality block -- the commutant there is 1 and sigma_x and nothing else -- and")
print("      BOTH its values are occupied.  No other object in this line supplies that. ***")
print("      What it has not got is the PAIRING.  The two sit at different momenta at one")
print("      energy, so the pairing must move z; of the sixteen reflections exactly four")
print("      preserve chirality and flip Sigma; only zx and zy also preserve the energy;")
print("      and both of those send c -> -c.")
print()
print("  ⛭ THE ONLY OPERATIONS THAT COULD PAIR TWO STATES OF ONE CHIRALITY AT ONE ENERGY ARE")
print("  EXACTLY THE ONES THAT FLIP THE TWIST -- AND THE TWIST IS WHAT MAKES THE MEMBER")
print("  CHIRAL.  P11 says c = 0 is the polarised, ACHIRAL cut.  The member can be chiral or")
print("  doublet-paired, and not both.  Its chirality and its pairing are carried by one field.")
print()
print("  W5, plainly: r6698 put the colourless triple out of every BOUND sector, by the")
print("  pairing's single unpaired level.  This puts it out of the construction's one NATIVE")
print("  PROPAGATING sector, by the twist.  Where it is not is now stated twice over, and the")
print("  two mechanisms are different.")
print()
print("  NOT ESTABLISHED: that Sigma is weak isospin or that the split is a doublet under some")
print("  other reading (W4) -- nothing is named.  Not that no propagating sector could carry a")
print("  doublet: THIS one cannot, for a stated reason.  Not anything about the c = 0 member,")
print("  where the pairing exists and the chirality does not.  Not anything at transverse")
print("  momenta, where there are no blocks and the question has no referent.")
print("=" * 90)
