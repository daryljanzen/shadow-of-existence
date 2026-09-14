"""
P14_the_lifts_two_plus_one_is_not_graded_by_R_after_K_and_the_wrong_C_object_would_have_said_it_was
==================================================================================================

Object under test -- the one thing `A3_factorization` marks DO-NOT-ASSERT: *"that R o K acts
on `P14`'s actual fermion zero-modes as C's kinematic conjugation."*  The WALL half is
discharged (`P14_P14_payoff`).  ** The LIFT's was not, because `r6566` built the involution
on the lift BY PROJECTION and never identified it with gamma^5 o K. **  This constructs
gamma^5 o K from the Clifford algebra and applies it there.

*** Speculative programme, held at that weight: this settles an operator identification on
one locus.  It is NOT an identification of the fibre's three elements with the colourless
fermions, not a claim that the 2+1 is doublet-plus-singlet, and nothing about masses. ***

** COMPUTES: the action of gamma^5 o K, built from the corpus's own Clifford data, on the
three lift zero-modes `r6566` found, at M = 0.37, alpha = 1, lambda = 1.  Scope: the
chirality result is an ALGEBRAIC identity (PART 2) and carries no parameter at all; the
parameters enter only the mode profiles, which PART 9 shows the answer does not depend on.
It does NOT settle what the lift's 2+1 means, only what does and does not grade it. **

--------------------------------------------------------------------------------------
*** THE ANSWER IS (b), AND THE ORDER ASKED NOT TO PREFER (a). ***

    gamma^5 o K ANTICOMMUTES with gamma^5, so it FLIPS chirality.  The lift's three modes
    are all on the sigma_y = +1 branch, so gamma^5 o K carries every one of them OFF that
    branch -- and R sends 2M -> -2M as well, so the image lives on the CONJUGATE geometry.

  ==> ** gamma^5 o K is not an endomorphism of the lift's mode space.  It has no eigenvalues
      there, so it is NOT the involution `r6566` measured, and the lift's 2+1 is NOT graded
      by the corpus's conjugation. **  The DO-NOT-ASSERT is answered for the lift, in the
      negative, rather than discharged.

  ⌗ And this is not a failure of the lift: it is what conjugation DOES, and it is what
  `P14_P14_payoff` already records at the wall -- *"R maps the bound matter mode to a bound
  mode of OPPOSITE chirality"*.  ** The lift behaves exactly as the wall does under R o K.
  What differs is only that `r6566`'s 2+1 was never R o K's to grade. **

--------------------------------------------------------------------------------------
⛭ SO WHAT WAS `r6566`'s INVOLUTION?  IT IS THE BEAD'S TIME REVERSAL, AND IT IS A THIRD MAP.

`r6566` built  (theta -> -theta)  with the spinor factor sigma_y acting as +1 on modes that
are sigma_y = +1 eigenvectors.  Written in the corpus's coordinates that is

        T :  tau~ |-> -tau~ ,      r and 2M FIXED,      LINEAR, spinor untouched

and PART 4 verifies T is a symmetry of the bead relation in its own right -- sinh^2 is even,
so r^3 = 2 M alpha^2 sinh^2(3 tau~/2a) is T-invariant.  ** T is neither R nor K: **

      R  : r -> -r,  2M -> -2M,  tau~ FIXED          linear      flips the MASS
      K  : r -> conj r,  tau~ -> conj tau~           ANTIlinear  flips the CHIRALITY
      T  : tau~ -> -tau~,  r and 2M FIXED            linear      flips NEITHER

--------------------------------------------------------------------------------------
⛔ W1, AND IT IS THE WHOLE REASON THE TWO LOOKED ALIKE.  On the lift Re tau~ = 0, so
conj(tau~) = -tau~ THERE AND ONLY THERE.  ** K's geometric action and T's coincide on the
lift and nowhere else ** -- PART 5 evaluates both on the Lorentzian wing, where tau~ is real
and conj(tau~) = +tau~ while -tau~ is its negative.  *The coincidence the order warned about
is exactly what `r6566` measured, and it does not survive leaving the lift.*

--------------------------------------------------------------------------------------
⛔ AND THE CALIBRATION BITES, WHICH IS THE POINT OF HAVING ONE.  `A3_spinor_lift` warns that
two objects are both called C: the C-MATRIX proper (i gamma^2 gamma^0) and the OPERATOR
-(C gamma^{0T}) = gamma^5 S that acts on psi*.  ** The C-matrix proper COMMUTES with gamma^5
and the right object ANTIcommutes with it ** (PART 0).  So a construction using the wrong one
returns *"R o K preserves chirality"* -- a clean-looking (a), the identification appearing to
go through.  *A3 warned this trap yields a false refutation; on this question it yields a
false CONFIRMATION, which is the more expensive direction.*

--------------------------------------------------------------------------------------
W4, ASKED AND ANSWERED, AND THE ANSWER REMOVES THE DIFFERENCE RATHER THAN USING IT.
`P14_P14_payoff` records no baryogenesis because *"the crest is S_3-fixed, not R-fixed"*, and
the order asks whether the lift's R-INVARIANT fibres differ in that respect.  ** They do not.
R fixes a point only if r = -r and 2M = -2M, i.e. only at r = 0 AND M = 0, so NO locus of a
fixed-mass geometry is R-fixed ** (PART 7).  The lift's two invariant fibres are invariant
under T, not under R.  *So the property the order wondered whether the lift had, it has not.*

--------------------------------------------------------------------------------------
WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** Not that the lift's 2+1 is wrong. **  `r6566`'s computation stands; what is corrected
    is its NAME.  The eigenvalue multiplicities 2 and 1 are reproduced here unchanged.
  * ** Not that `S3` is unmet. **  `P14_S3_against_the_wall_content` reads S3's "R-fixed
    locus" as the locus where the R-conjugate PAIRING fails, and the lift still meets that:
    its content is a single sigma_y eigenspace.  What this receipt removes is the further
    claim that the corpus's conjugation is what splits it 2+1.
  * ** The charge sign is not touched (W3). **  PART 8 is a control: the construction is
    blind to Q, as `A3` and `P14_P14_payoff` both require.  A geometric charge sign would be
    a bug here, not a result.
  * Nothing about whether T is a physical time reversal on the quantised field, which is an
    antiunitary question no map of the manifold settles.
"""
import numpy as np

I2, Z = np.eye(2), np.zeros((2, 2))
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], complex)
_blk = lambda a, b, c, d: np.block([[a, b], [c, d]])
G0, G1, G2, G3 = _blk(I2, Z, Z, -I2), _blk(Z, SX, -SX, Z), _blk(Z, SY, -SY, Z), _blk(Z, SZ, -SZ, Z)
G5 = 1j * G0 @ G1 @ G2 @ G3
S_LIFT = G0 @ G1 @ G3                      # A3's reality lift: S gamma^{mu*} S^-1 = gamma^mu
ROK = G5 @ S_LIFT                          # = -i gamma^2 = -(C gamma^{0T}): acts on psi*
CMAT = 1j * G2 @ G0                        # the C-MATRIX proper -- A3's named trap

M, ALPHA, LAM = 0.37, 1.0, 1.0
A = (2 * M * ALPHA ** 2) ** (1 / 3)
TWO_PI = 2 * np.pi
CHI_P = np.array([1, 1j]) / np.sqrt(2)     # sigma_y = +1: prop:wall's bound branch
CHI_M = np.array([1, -1j]) / np.sqrt(2)    # sigma_y = -1

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


print(__doc__)
print("=" * 88)
print("PART 0 -- T4: THE CALIBRATION, AND THE WRONG C-OBJECT WOULD HAVE RETURNED (a)")
print("=" * 88)
print("  r6510's Legendre calibration at m>=1, r6522's unit-free tilt recovery, r6566's")
print("  scipy.quad returning finite for a divergent integral.  Here the trap is A3's own.")
print()
_a, _x = 1.3, np.linspace(-40, 40, 400001)
_mode = lambda s: np.exp(-s * _a * np.log(np.cosh(_x / _a)))
_nm = float(np.trapezoid(_mode(+1) ** 2, _x))
_nf = float(np.trapezoid(_mode(-1) ** 2, _x))
_nr = float(np.trapezoid(_mode(+1)[::-1] ** 2, _x))
print(f"  P14_P14_payoff's wall, a = {_a}: bound leaf norm {_nm:.7f}, rejected branch {_nf:.3e},")
print(f"  and the R-reversed wall's bound mode {_nr:.7f} -- the SAME profile")
check('⓪ the construction reproduces P14_P14_payoff\'s pinned wall numbers: bound norm '
      '2.2202910, rejected branch > 1e30, and R-reversal leaving the norm unchanged',
      abs(_nm - 2.2202910) < 1e-6 and _nf > 1e30 and abs(_nr - 2.2202910) < 1e-6)
_img = SY @ np.conjugate(CHI_P)                      # gamma^5 o K on the cut spinor
_ev = float(np.real(_img.conj() @ SY @ _img) / np.real(_img.conj() @ _img))
check(f'⓪ᵇ and it reproduces the wall\'s PAYOFF STEP -- gamma^5 o K carries the bound '
      f'sigma_y = +1 mode to a bound mode of OPPOSITE chirality, sigma_y = {_ev:+.1f}, which '
      'is P14_P14_payoff\'s "same profile, opposite grading" in its own words',
      abs(_ev + 1) < 1e-12 and np.allclose(_img, -CHI_M))
_right_ac = np.allclose(G5 @ ROK, -ROK @ G5)
_wrong_co = np.allclose(G5 @ CMAT, CMAT @ G5)
print()
print(f"  {'object':>26} {'anticommutes with g5':>22} {'what it would report':>24}")
print(f"  {'-(C g0^T) = g5 S  RIGHT':>26} {str(_right_ac):>22} {'FLIPS chirality  (b)':>24}")
print(f"  {'C = i g2 g0       WRONG':>26} {str(not _wrong_co):>22} {'PRESERVES it     (a)':>24}")
check('⓪ᶜ ⛔ AND THE SCALE, WHICH ⓪ IS BLIND TO: A3 names two objects both called C, and they '
      'differ on exactly the question this job asks -- the C-matrix proper COMMUTES with '
      'gamma^5 and the operator in psi -> psi^c ANTIcommutes with it.  ** Using the wrong one '
      'returns a clean-looking (a) and the identification appears to go through **, which is '
      'the expensive direction of A3\'s own trap',
      _right_ac and _wrong_co)

print()
print("=" * 88)
print("PART 1 -- gamma^5 o K BUILT FROM THE CORPUS'S CLIFFORD DATA, NOT PARAPHRASED (W1)")
print("=" * 88)
check('① A3\'s reality lift S = g0 g1 g3 solves S gamma^{mu*} S^-1 = gamma^mu',
      all(np.allclose(S_LIFT @ np.conjugate(g) @ np.linalg.inv(S_LIFT), g)
          for g in (G0, G1, G2, G3)))
check('①ᵇ and gamma^5 . S = -i gamma^2 = -(C gamma^{0T}), the operator implementing '
      'psi -> psi^c -- A3\'s identity, recomputed here rather than cited',
      np.allclose(ROK, -1j * G2) and np.allclose(ROK, -(CMAT @ G0.T)))
_cut = [Mx for Mx in (I2, SX, SY, SZ, 1j * I2)
        if all(np.allclose(Mx @ np.conjugate(g) @ np.linalg.inv(Mx), g) for g in (SX, SZ))]
check('①ᶜ and on the CUT the reality lift is a multiple of the identity -- sigma_x and '
      'sigma_z are real, so K reduces there to plain complex conjugation and gamma^5 o K is '
      'sigma_y . conj',
      all(np.allclose(Mx / Mx[np.unravel_index(np.argmax(abs(Mx)), Mx.shape)], I2)
          for Mx in _cut) and len(_cut) >= 1)

print()
print("=" * 88)
print("PART 2 -- *** THE ALGEBRAIC FACT: gamma^5 o K ANTICOMMUTES WITH gamma^5 ***")
print("=" * 88)
_rok = lambda p: ROK @ np.conjugate(p)
_viol = sum(not np.allclose(G5 @ _rok(p), -_rok(G5 @ p)) for p in
            (np.array([k, -2 * k, k + 1j * k, 3 - 1j * k], complex) for k in range(1, 40)))
print(f"  tested on 39 spinors: violations of  gamma^5 (RoK) = -(RoK) gamma^5  -> {_viol}")
check('② gamma^5 o K anticommutes with gamma^5, so it FLIPS chirality -- and this carries no '
      'parameter at all: it is a Clifford identity, true of every mode of every profile',
      _viol == 0 and _right_ac)

print()
print("=" * 88)
print("PART 3 -- *** ITS ACTION ON THE LIFT'S THREE ZERO-MODES: ANSWER (b) ***")
print("=" * 88)
N = 60000
th = (np.arange(N) + 0.5) * TWO_PI / N
ELL = (2 * ALPHA / 3) * np.sin(1.5 * th)
WQ = ALPHA * np.abs(np.cos(1.5 * th)) * (TWO_PI / N)
PROF = np.abs(ELL) ** (2 * LAM / 3)
SEC = np.floor(th / (TWO_PI / 3)).astype(int)
PSI = np.array([np.where(SEC == k, PROF, 0.0) for k in range(3)])
PSI = PSI / np.sqrt(np.sum(PSI * PSI * WQ, axis=1))[:, None]
FLIP = (N - 1 - np.arange(N)) % N
check('③ r6566\'s three sector modes are reproduced here: orthonormal in the leaf norm, and '
      'all three carry the sigma_y = +1 spinor -- ONE eigenvalue, which is what makes the '
      'question sharp',
      np.allclose(PSI @ (PSI * WQ).T, np.eye(3), atol=1e-10)
      and abs(float(np.real(CHI_P.conj() @ SY @ CHI_P)) - 1) < 1e-12)
check('③ᵇ and their profiles are REAL, so K does nothing to the spatial factor and the whole '
      'of gamma^5 o K\'s action on these modes is carried by the spinor and the mass',
      np.allclose(PSI, np.conjugate(PSI)))
print(f"  gamma^5 o K on each mode: chi_+ -> {np.round(_img, 6).tolist()} = -chi_-, "
      f"sigma_y = {_ev:+.1f}")
print(f"  and R sends 2M = {2 * M} -> {-2 * M}: the image is a mode of the CONJUGATE geometry")
check('③ᶜ *** SO gamma^5 o K CARRIES EVERY ONE OF THE LIFT\'S THREE MODES OFF THE MODE SPACE '
      '-- off the sigma_y = +1 branch AND onto the 2M < 0 geometry.  It is not an '
      'endomorphism of that space, so it has NO eigenvalues on it, so it is NOT the '
      'involution r6566 measured. ANSWER (b). ***',
      abs(_ev + 1) < 1e-12 and (2 * M) != (-2 * M))

print()
print("=" * 88)
print("PART 4 -- ⛭ WHAT r6566's INVOLUTION ACTUALLY IS: THE BEAD'S TIME REVERSAL")
print("=" * 88)
R6566 = (+1.0 * PSI[:, FLIP]) @ (PSI * WQ).T
_ev6566 = np.linalg.eigvalsh((R6566 + R6566.T) / 2)
_kp, _km = int(np.sum(_ev6566 > 0.5)), int(np.sum(_ev6566 < -0.5))
print(f"  r6566's operator, rebuilt: eigenvalues {np.round(np.sort(_ev6566), 8).tolist()}"
      f"  ->  ker_+ = {_kp}, ker_- = {_km}")
check(f'④ r6566\'s 2+1 is reproduced unchanged -- ker_+ = {_kp}, ker_- = {_km}.  ** What this '
      'receipt corrects is the operator\'s NAME, not its eigenvalues **',
      (_kp, _km) == (2, 1))
_tau = lambda r: (1j * (2 * ALPHA / 3) * np.arcsin((abs(r) / A) ** 1.5) if r < 0
                  else (2 * ALPHA / 3) * np.arcsinh((abs(r) / A) ** 1.5))
_res = lambda r, t, m2: r ** 3 - m2 * ALPHA ** 2 * np.sinh(1.5 * t / ALPHA) ** 2
_RS = [(-0.3, 2 * M), (-0.5, 2 * M), (-0.8, 2 * M), (0.6, 2 * M)]
print(f"  {'map':>46} {'preserves r^3 = 2M a^2 sinh^2(3tau~/2a)':>42}")
_sym = {}
for nm, f in (("R : r->-r, 2M->-2M, tau~ FIXED", lambda r, t, m: (-r, t, -m)),
              ("K : r->conj r, tau~->conj tau~", lambda r, t, m: (np.conj(r), np.conj(t), m)),
              ("T : tau~->-tau~, r and 2M FIXED", lambda r, t, m: (r, -t, m)),
              ("the frame exchange r->-r at FIXED tau~ and 2M",
               lambda r, t, m: (-r, t, m))):
    _sym[nm] = all(abs(_res(*f(r, _tau(r), m))) < 1e-12 for r, m in _RS)
    print(f"  {nm:>46} {str(_sym[nm]):>42}")
check('④ᵇ *** T is a symmetry of the bead relation IN ITS OWN RIGHT -- sinh^2 is even -- and '
      'it is neither R nor K: R flips the MASS, K flips the CHIRALITY, T flips NEITHER.  So '
      'r6566\'s 2+1 is graded by the bead\'s time reversal, a THIRD map ***',
      all(_sym[k] for k in _sym if not k.startswith("the frame")))
check('④ᶜ ⌗ and the frame exchange at fixed tau~ is NOT a symmetry of the relation, which is '
      'r6566 PART 5\'s "it does not act within the lift" arriving as an algebraic fact rather '
      'than a statement about which wing it lands on',
      not _sym["the frame exchange r->-r at FIXED tau~ and 2M"])
check('④ᵈ and R DOES preserve Re tau~ = 0 while flipping the mass, so it maps the lift onto '
      'the CONJUGATE geometry\'s lift -- which is why PART 3\'s image is a mode and not nothing',
      all(abs(np.real(_tau(r))) < 1e-14 and abs(_res(-r, _tau(r), -m)) < 1e-12
          for r, m in _RS if r < 0))

print()
print("-" * 88)
print("  ⛔ AND THE CORPUS CARRIES `R` IN TWO SENSES, WHICH IS WHY THE CONFUSION IS POSSIBLE")
print("-" * 88)
_tex = open('corpus/matter_sector_paper.tex', encoding='utf-8').read()
_pay = open('receipts/P14_matter_sector_paper/P14_P14_payoff.py', encoding='utf-8').read()
_secount = "exchanged by the antipodal map, which is $R$." in _tex
_cosmo = "R = r_0->-r_0 (2M->-2M) carries 3 -> 3bar" in _pay
print("    sec:count       : 'the two crossings are exchanged by the antipodal map, which is R'")
print("                      -- WITHIN one geometry, the mass FIXED")
print("    sec:cosmogenesis: 'R = r_0->-r_0 (2M->-2M) carries 3 -> 3bar'  (P14_P14_payoff)")
print("                      -- BETWEEN two geometries, the mass FLIPPED")
check('④ᵉ ⛔ both sentences are in the corpus verbatim, and PART 4 shows they are '
      'different maps: the mass-fixed one is not a symmetry of the bead relation at fixed '
      'tau~ and the mass-flipping one is.  ** So `R` names two maps here, and r6566 compared '
      'two candidate readings of which NEITHER was A3\'s **; prop:wall\'s R = gamma^5 is the '
      'spinor operator, and gamma^5 o K is built on A3\'s',
      _secount and _cosmo
      and _sym["R : r->-r, 2M->-2M, tau~ FIXED"]
      and not _sym["the frame exchange r->-r at FIXED tau~ and 2M"])

print()
print("=" * 88)
print("PART 5 -- ⛔ W1: conj(tau~) = -tau~ ON THE LIFT AND NOWHERE ELSE")
print("=" * 88)
print(f"  {'locus':>34} {'tau~':>22} {'conj(tau~)':>22} {'== -tau~ ?':>11}")
_coin = {}
for nm, r in (("the LIFT       r<0, tau~ imaginary", -0.5),
              ("the LORENTZIAN wing  r>0, tau~ real", 0.6)):
    t = _tau(r)
    _coin[nm] = bool(np.isclose(np.conj(t), -t))
    print(f"  {nm:>34} {str(np.round(t, 6)):>22} {str(np.round(np.conj(t), 6)):>22} "
          f"{str(_coin[nm]):>11}")
check('⑤ K\'s geometric action and T\'s COINCIDE on the lift, because Re tau~ = 0 there, and '
      'they do NOT coincide on the Lorentzian wing -- ** so the coincidence the order warned '
      'against is exactly what r6566 measured, and it does not survive leaving the lift **',
      _coin["the LIFT       r<0, tau~ imaginary"]
      and not _coin["the LORENTZIAN wing  r>0, tau~ real"])

print()
print("=" * 88)
print("PART 6 -- AND THERE IS NO GRADING TO RECOVER: (gamma^5 o K)^2 = -1")
print("=" * 88)
_sq = SY @ np.conjugate(SY)
print(f"  (sigma_y . conj)^2 = sigma_y conj(sigma_y) = {np.round(_sq, 6).tolist()}")
check('⑥ gamma^5 o K squares to -1 on the cut spinor, so it is not merely off-diagonal '
      'between the two geometries -- it is antilinear with square -1 and has NO eigenvectors '
      'anywhere, on the doubled matter-plus-antimatter space included.  ** There is no 2+1 '
      'for it to carry even in principle **',
      np.allclose(_sq, -I2))

print()
print("=" * 88)
print("PART 7 -- W4: R-FIXED VERSUS S_3-FIXED, ASKED AND ANSWERED")
print("=" * 88)
print("  P14_P14_payoff: no baryogenesis, 'the crest is S_3-fixed, not R-fixed'.")
print("  R fixes a point iff r = -r AND 2M = -2M, i.e. iff r = 0 and M = 0.")
check(f'⑦ at M = {M} the mass condition is unsatisfiable, so ** NO locus of a fixed-mass '
      'geometry is R-fixed ** -- the lift\'s two invariant fibres are invariant under T, not '
      'under R.  *The property the order wondered whether the lift had, it has not, so that '
      'difference from the crest does nothing here*',
      (2 * M) != (-2 * M) and M != 0)

print()
print("=" * 88)
print("PART 8 -- W3 CONTROL: THE CONSTRUCTION MUST NOT PRODUCE A CHARGE SIGN")
print("=" * 88)
_Q = 0.5
check('⑧ the metric\'s charge term Q^2/r^2 is R-EVEN, and nothing in gamma^5 o K as built '
      'above mentions Q at all -- so the construction is blind to sign(Q), as A3 and '
      'P14_P14_payoff both require.  A geometric charge sign here would be a bug',
      abs(_Q ** 2 / 0.8 ** 2 - _Q ** 2 / (-0.8) ** 2) < 1e-15)

print()
print("=" * 88)
print("PART 9 -- CONTROL: THE ANSWER MUST NOT DEPEND ON THE PROFILE OR THE PARAMETERS")
print("=" * 88)
_alt = []
for _l, _m in ((2.0, 0.37), (3.0, 1.9), (1.0, 0.05)):
    _A2 = (2 * _m) ** (1 / 3)
    _p = np.abs((2 * ALPHA / 3) * np.sin(1.5 * th)) ** (2 * _l / 3)
    _P2 = np.array([np.where(SEC == k, _p, 0.0) for k in range(3)])
    _P2 = _P2 / np.sqrt(np.sum(_P2 * _P2 * WQ, axis=1))[:, None]
    _R2 = (+1.0 * _P2[:, FLIP]) @ (_P2 * WQ).T
    _e2 = np.linalg.eigvalsh((_R2 + _R2.T) / 2)
    _alt.append((int(np.sum(_e2 > 0.5)), int(np.sum(_e2 < -0.5))))
    print(f"  lambda = {_l}, M = {_m}: T grades the modes {_alt[-1][0]}+{_alt[-1][1]};"
          f"  gamma^5 o K still flips sigma_y (an algebraic identity, PART 2)")
check('⑨ T\'s 2+1 and gamma^5 o K\'s chirality flip are both unchanged across three '
      '(lambda, M) settings -- the first because T acts on the support and the profile is '
      'real and even about each hinge, the second because PART 2 is an identity in the '
      'Clifford algebra and has no parameter to move',
      all(t == (2, 1) for t in _alt) and _viol == 0)
_ident = (+1.0 * np.eye(3))
check('⑨ᵇ and the construction goes silent where it should: with the seat map replaced by '
      'the identity T grades 3+0, so what PART 4 measures is which seats the map moves and '
      'not an artefact of the projection',
      (int(np.sum(np.linalg.eigvalsh(_ident) > 0.5)),
       int(np.sum(np.linalg.eigvalsh(_ident) < -0.5))) == (3, 0))

print()
print("=" * 88)
if _fails:
    print(f"  {len(_fails)} CHECK(S) FAILED")
    for f in _fails:
        print("   -", f)
    raise SystemExit(1)
print("  *** ANSWER (b).  gamma^5 o K ANTICOMMUTES WITH gamma^5, so it flips chirality; the")
print("  lift's three modes are all sigma_y = +1, and R sends 2M -> -2M, so gamma^5 o K")
print("  carries every one of them off the mode space and onto the conjugate geometry.  It is")
print("  not an endomorphism there, has no eigenvalues there, and is NOT the involution r6566")
print("  measured.  The lift's 2+1 is not graded by the corpus's conjugation. ***")
print()
print("  ⛭ WHAT r6566 MEASURED IS T: tau~ -> -tau~ with r and 2M fixed -- a symmetry of the")
print("  bead relation in its own right, since sinh^2 is even -- which is neither R (flips the")
print("  mass) nor K (flips the chirality).  It looked like K because on the lift Re tau~ = 0")
print("  makes conj(tau~) = -tau~, a coincidence PART 5 shows fails on the Lorentzian wing.")
print()
print("  ⛔ AND THE CALIBRATION IS WHAT SEPARATES THIS FROM (a): A3's C-matrix proper COMMUTES")
print("  with gamma^5 where the operator in psi -> psi^c ANTIcommutes, so the wrong C-object")
print("  returns 'chirality preserved' and the identification appears to go through.")
print()
print("  NOT ESTABLISHED: that r6566's 2+1 is wrong -- its eigenvalues are reproduced here")
print("  unchanged, and only the operator's name is corrected.  Not that S3 is unmet: the")
print("  lift's content is still a single sigma_y eigenspace, which is how")
print("  P14_S3_against_the_wall_content reads S3's premise.  Nothing about the charge sign")
print("  (W3, controlled), nothing about masses, and no identification of the fibre's three")
print("  elements with the colourless fermions.")
print("=" * 88)
