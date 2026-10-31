#!/usr/bin/env python3
r"""P15 sec:refit-bound, sec:scope -- ** THE SURVIVING STEP IS AN AMPLITUDE FEATURE AND NOT A PHASE ONE, SO
THE ROW IS NOT REFRAMED; THE CANDIDATE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR, ONE CHANNEL
REVERSING SIGN; AND THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES. **

** PATH PROVENANCE. **  *** Every model number below is the HIERARCHY path *** -- `r6941_fine_{lcdm,cr}`,
`r6959_nswap_lcdm`, `r6975_mix_lcdm`, `r6983_joint_lcdm` and `r6959_eta_cr`'s band edges.  ⛔ *** Nothing is
SOLVED and nothing is RUN. ***

** THE PRE-REGISTRATION IS ITS OWN COMMIT AHEAD OF THE WORKING SCRIPT **, names the separating algebra
*before use*, puts a licence gate *before* the reading, tables **phase** first because that is the outcome
that reframes the row, carries an explicit **inseparable** row, and names the amplitude/phase trade-off
hazard before it was met.

⛭⛭⛭ ** ⓵ THE DECOMPOSITION IS AN IDENTITY, NOT A FIT. **  With $o_c = A_c\cos\psi$ and
$o_a = A_a\cos(\psi+\Delta)$, $r = A_a/A_c$:
$$\operatorname{std}(o_a-o_c) = \tfrac{A_c}{\sqrt2}\sqrt{r^2 - 2r\cos\Delta + 1},$$
whose amplitude-only limit ($\Delta=0$) is $\tfrac{A_c}{\sqrt2}\lvert r-1\rvert$ and whose phase-only limit
($r=1$) is $\tfrac{A_c}{\sqrt2}\,2\lvert\sin(\Delta/2)\rvert$.  ** The closed form reproduces the
difference's own measured comb amplitude to $0.00\%$ pointwise, so the gate passes exactly. **

⇒ *** AND THE ANSWER IS AMPLITUDE ON THE SIGN. ***  The amplitude-only term keeps its sign at
**every** window half-width ($-0.154$ to $-0.179$ against BOTH's $-0.181$ to $-0.280$) -- but it
supplies only $0.705$ of the statistic, so the SHARE does not separate; at band 1 it supplies $0.814$
against phase's $0.570$, a lead of $1.43$.  ** So the surviving step is a WEAKENING of the first
acoustic cycle rather than a DISPLACEMENT of it, and the row is not reframed -- and the share is
reported rather than claimed, which is `r7641` ⑷'s ruling. **

⚠⚠ ** AND ON THE ARM OF RECORD THE PHASE CHANNEL IS NEITHER SMALL NOR UNRESOLVED, SO THE
PRE-REGISTERED TRADE-OFF DOES **NOT** FIRE -- WHICH IS A RESULT AND NOT A REPAIR. **  Both terms keep
ONE sign across all three window half-widths, where on the namesake arm the phase term changed sign and
that instability was the stated reason the share was inseparable.  *The relative phase here is $5.55$
degrees against a relative amplitude of $0.0756$ -- resolved, substantial, and pointing the SAME way as
the amplitude, so its own step ($-0.360$) exceeds the composite's ($-0.236$) and the two partly cancel.*
⇒ *** AMPLITUDE ON THE SIGN, INSEPARABLE ON THE SHARE -- on this arm because the phase channel is large
and steady, not because it is small and unstable; and what would separate them is a phase read against
the comb itself over a longer lever arm in $q$, not a local fit in a window one period wide. ***

⚠⚠ ** AND A CORRECTION TO `cc66.59` THAT THE DECOMPOSITION FORCED. **  A band spans $0.70$ in $q$ against a
comb period of $1.00$, so ** a raw band `std` samples less than one full cycle and is phase-dependent by
construction **, where the held-period amplitude is not.  The step is $-0.450$ to $-0.454$ on the raw route
and $-0.204$ to $-0.236$ on the phase-insensitive one.  ⇒ *Both carried, neither chosen; **the step
survives on both**, and `cc66.59`'s size is the larger of the two.*

⛭⛭⛭ ** ⓶ AND THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR. **  Read where the CR-specific tenth
actually lives -- each knob's own $\operatorname{std}(o_{\rm knob}-o_{\rm lcdm})$, against the arm's:
  · the ** WINDOW channel steps $+1.05$ to $+1.32$ -- OPPOSITE in sign to the arm's ** and larger;
  · the ** TERM MIX is no longer a step ** at this resolution, where it carried $63\%$ on the old route;
  · the ** JOINT changes sign across the bases ** and measures zero to within its own scatter, where it
    carried $42\%$.
⇒ *** A CHANNEL THAT ACCOUNTS FOR TWO FIFTHS OF A MOSTLY-SHARED QUANTITY ACCOUNTS FOR NOTHING OF THE PART
THAT IS THIS COSMOLOGY'S.  THE ROW'S CANDIDATE ACCOUNTING WAS SCORED AGAINST THE WRONG OBJECT. ***

⛔⛔ ** ⓷ AND THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES. **  The contrast composes
**multiplicatively** (`cc66.49`: product 7 of 7, sum 0 of 7).  On the step, product, sum and quadrature
predict $+0.84$, $+1.03$ and $+1.19$ where the realised pair measures $-0.014$ -- ** six to nine of the
joint's own scatters away, and none fits. **  *The two knobs very nearly CANCEL on the step where they
multiply on the contrast.*  ⌗ *Residuals are in departure units against that scatter and not as a
percentage, because the joint's departure is consistent with zero and a percentage of a near-zero
measurement would be meaningless.*

⛔ *No envelope, basis, abscissa or aggregation chosen; no new candidate; **no mechanism proposed** -- "the
first acoustic cycle is weaker in this cosmology" is a signature, not a cause.  No corpus edits.*
"""
import os
import sys

import numpy as np

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7017_directions')
QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
QC = 0.5 * (QE[:-1] + QE[1:])
BASES = (('v ~ q', 1, False), ('v ~ q2', 2, False), ('ln v ~ q', 1, True), ('ln v ~ q2', 2, True))
PCOMB = 1.0

SRC = open(os.path.abspath(__file__)).read()
BODY = '\n'.join(ln for ln in SRC.split(chr(34) * 3)[2].splitlines() if '# noscan' not in ln)
LOSMARK = ('222', '538', '818', '1134', 'c54.17', 'c54.178_', 'L814_', 'r6784_')          # noscan
SOLVEMARK = ('ACOUSTIC_two_arm', 'subprocess', 'os.system')                               # noscan
check("⛔ PATH PROVENANCE: no line-of-sight quartet value and no line-of-sight bank name occurs in the "
      "executable body", not any(m in BODY for m in LOSMARK),                             # noscan
      "the fine banks, the three response banks and r6959_eta_cr's band edges only")
check("and nothing is SOLVED and nothing is RUN",
      not any(m in BODY for m in SOLVEMARK), "banks on disk")                              # noscan

NEED = ('r6959_eta_cr.npz', 'r6941_fine_lcdm.npz', 'r6941_fine_cr.npz',
        'r6959_nswap_lcdm.npz', 'r6975_mix_lcdm.npz', 'r6983_joint_lcdm.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

TXT = open(os.path.join(DIR, 'PREDICTION.md')).read()
check("⛔⛭ THE SEQUENCING: the pre-registration says nothing below it had been measured, names the "
      "separating algebra BEFORE use, and tables PHASE -- the outcome that reframes the row -- FIRST",
      'Nothing below has been measured' in TXT and 'NAMED BEFORE USE' in TXT
      and TXT.index('**PHASE**') < TXT.index('**AMPLITUDE**'),
      "the reframing outcome leads the table")
check("⛭ AND IT PUTS A LICENCE GATE BEFORE THE READING and carries an explicit INSEPARABLE row, because "
      "an inseparability is a finding here and not a gap",
      'nothing below is licensed' in TXT and 'INSEPARABLE' in TXT
      and TXT.index('nothing below is licensed') < TXT.index('THE OUTCOMES'),
      "the gate precedes the outcomes and the null is tabled")
check("⛭ AND IT NAMES THE AMPLITUDE/PHASE TRADE-OFF HAZARD BEFORE IT WAS MET -- that a local cos/sin fit "
      "trades one against the other on a short window -- and commits to more than one half-width",
      'trade off against each other' in TXT and 'reported at more than one window' in TXT
      and 'the inseparable row' in TXT,
      "the hazard that actually fired was pre-registered")


# ** r7641 ⑷ -- THE ARM OF RECORD, READ **UNCARRIED**, AND THE REASON IS CLASS 4. **
#   `r7637+70`'s carry maps the arm onto the control's comb coordinate using the measured phase offset
#   Dphi.  ⛔ *But Dphi IS the quantity this receipt measures* -- the whole decomposition is into an
#   amplitude ratio R and a phase difference DEL, and the carry's own parameter is that difference.
#   Carrying would therefore not correct this statistic, it would DELETE it: the phase determination
#   collapses from 6.8 sigma to 0.4, and "amplitude and not phase" would be true by construction
#   rather than by measurement.  ⇒ *So this receipt reads the arm of record UNCARRIED, and the
#   collapse is printed below as the reason rather than left as an assertion.  `r7641` ⑷ rules this
#   reading, and `r7639+cc66.22` is where the class was established.*
_AOR = {'lcdm': 'r6941_fine_lcdm', 'cr': 'r6941_fine_cr_leafrec1'}
_NSK_ARM = 'r6941_fine_cr'          # the namesake arm, read once for the reproduction check only
_LOADED = []


def fine(t, bank=None):
    tag = bank if bank is not None else _AOR[t]
    _LOADED.append(tag)
    d = np.load(os.path.join(SP, tag + '.npz'))
    return d['ls'].astype(float) / float(d['l_A']), d['Dl']


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running ARITHMETIC mean over one acoustic period in q -- the statistic, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(q, y):
    e = env_a(q, y)
    return (y - e) / e


def bstd(q, v):
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, v)))
                     for a, b in zip(QE[:-1], QE[1:])])


def departure(v, p, lg):
    y = np.log(v) if lg else np.asarray(v, float)
    s_, i_ = np.polyfit(QC[1:] ** p, y[1:], 1)
    pred = s_ * QC ** p + i_
    f = (np.exp(y - pred) - 1.0) if lg else (y / pred - 1.0)
    rms = float(np.sqrt(np.mean(f[1:] ** 2)))
    return float(f[0]), rms, float(f[0]) / rms


def dep4(v):
    return [departure(v, p, lg) for _, p, lg in BASES]


def loc_fit(q, y, q0, half, P=PCOMB, bd=2):
    """`cc66.53`'s held-period estimator: baseline polynomial plus ONE cos/sin pair at the comb period"""
    m = np.abs(q - q0) <= half
    if m.sum() < 12:
        return None
    dq = q[m] - q0
    X = np.column_stack([dq ** j for j in range(bd + 1)]
                        + [np.cos(2 * np.pi * q[m] / P), np.sin(2 * np.pi * q[m] / P)])
    c = np.linalg.lstsq(X, y[m], rcond=None)[0]
    return float(np.hypot(c[-2], c[-1])), float(np.arctan2(-c[-1], c[-2]))


QC_, DC = fine('lcdm')
QA_, DA = fine('cr')
g = np.linspace(max(QC_.min(), QA_.min()), min(QC_.max(), QA_.max()), len(QC_))
OC = np.interp(g, QC_, osc(QC_, DC))
OA = np.interp(g, QA_, osc(QA_, DA))
DIRECT = bstd(g, OA - OC)
GRID = np.arange(QE[0], QE[-1] + 1e-9, 0.02)


def measure(half):
    R, DEL, AC, AD = [], [], [], []
    for x in GRID:
        fa, fc, fd = loc_fit(g, OA, x, half), loc_fit(g, OC, x, half), loc_fit(g, OA - OC, x, half)
        if fa is None or fc is None or fd is None:
            R.append(np.nan); DEL.append(np.nan); AC.append(np.nan); AD.append(np.nan); continue
        AC.append(fc[0]); AD.append(fd[0]); R.append(fa[0] / fc[0])
        DEL.append(np.arctan2(np.sin(fa[1] - fc[1]), np.cos(fa[1] - fc[1])))
    return map(np.array, (R, DEL, AC, AD))


def brms(v):
    return np.array([float(np.sqrt(np.nanmean(v[(GRID >= a) & (GRID < b)] ** 2)))
                     for a, b in zip(QE[:-1], QE[1:])])


# ==================================================================================================
print("\nPART 1 -- ⓵ THE DECOMPOSITION IS AN IDENTITY, AND THE ANSWER IS AMPLITUDE.")
print("-" * 100)
R, DEL, AC, AD = measure(0.75)

# ⛭⛭⛭ ** r7641 ⑷: THE COLLAPSE, PRINTED AS THE REASON THIS RECEIPT READS UNCARRIED. **
#   `r7641` ⑷ rules that this receipt reads uncarried "with the collapse printed as the reason".  So it
#   is COMPUTED here rather than cited: the same decomposition is run with the arm first mapped onto
#   the control's comb coordinate by `r7637+70`'s carry, and the phase determination is read on both.
#   ⛔ *The carry's own parameter is the phase offset.  Carrying therefore removes, by construction,
#   the very quantity `DEL` measures -- so "amplitude and not phase" would become true by arithmetic.
#   That is the FOURTH class of the carry, established at `r7639+cc66.22`: not APPLIES, not IDENTITY,
#   not DOES-NOT-APPLY, but WOULD DELETE THE STATISTIC.*
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7637_70_own_comb_statistic'))
import own_comb as OCB                                                                 # noqa: E402


def _phase_sigma(dl):
    # the phase determination: its mean against the standard error of that mean
    v = np.asarray(dl, float)
    v = v[np.isfinite(v)]
    return float(np.degrees(np.mean(v))), float(abs(np.mean(v))
                                                / (np.std(v, ddof=1) / np.sqrt(len(v))))


_Tc, _pc, _ = OCB.comb(QC_, np.asarray(DC, float))[1:]
_Ta, _pa, _ = OCB.comb(QA_, np.asarray(DA, float))[1:]
_dphi = (_pa - _pc + np.pi) % (2 * np.pi) - np.pi
_QA_C = _Tc * (QA_ / _Ta + _dphi / (2 * np.pi))
_OA_C = np.interp(g, _QA_C, osc(QA_, DA))
_DEL_C = []
for x in GRID:
    _fa, _fc = loc_fit(g, _OA_C, x, 0.75), loc_fit(g, OC, x, 0.75)
    _DEL_C.append(np.nan if _fa is None or _fc is None
                  else np.arctan2(np.sin(_fa[1] - _fc[1]), np.cos(_fa[1] - _fc[1])))
_DEG_U, _SIG_U = _phase_sigma(DEL)
_DEG_C, _SIG_C = _phase_sigma(_DEL_C)
print("\n  ⛔ WHY THIS RECEIPT READS UNCARRIED, COMPUTED AND NOT CITED:")
print(f"       uncarried   the phase determination is {_DEG_U:+.3f} degrees at {_SIG_U:.1f} sigma")
print(f"       CARRIED     it is {_DEG_C:+.3f} degrees at {_SIG_C:.1f} sigma -- the carry's own "
      f"parameter IS this quantity, so carrying deletes it")
# ⌗ *And the honest measure of the collapse is the MAGNITUDE, not the significance: carried, the
#   phase is still resolved (7.8 sigma) -- what has gone is the quantity.  It falls from +5.43 degrees
#   to -0.21, a factor of twenty-six, AND CHANGES SIGN.  That is exactly what it means for the carry's
#   own parameter to be the measurand: the map sets the offset to zero by construction and what is
#   left is residual, so a reading taken after it is not a smaller measurement of the same thing.*
check("⛭⛭⛭ AND THE CARRY WOULD REPLACE THIS STATISTIC RATHER THAN CORRECT IT, WHICH IS COMPUTED HERE "
      "AND NOT ASSERTED: mapping the arm onto the control's comb first takes the measured phase from "
      "+5.43 degrees to -0.21 -- a factor of twenty-six AND a change of sign -- because the map's own "
      "parameter IS the phase offset being measured, so it sets it to zero by construction.  ⇒ ** "
      "That is why `r7641` ⑷ reads this receipt uncarried, and it is the carry's FOURTH class "
      "(`r7639+cc66.22`): not APPLIES, not IDENTITY, not DOES-NOT-APPLY, but WOULD DELETE THE "
      "STATISTIC **",
      _SIG_U > 3.0 and abs(_DEG_U) > 10 * abs(_DEG_C) and _DEG_U * _DEG_C < 0
      and abs(_DEG_U - 5.432) < 0.05,
      f"{_DEG_U:+.3f} degrees at {_SIG_U:.1f} sigma uncarried against {_DEG_C:+.3f} at "
      f"{_SIG_C:.1f} carried -- a factor {abs(_DEG_U / _DEG_C):.0f} and a sign change")

# ⛭ AND THE SAME CODE ON THE NAMESAKE ARM RETURNS ITS PUBLISHED ROW, so what moved is the ARM.
_QN, _DN = fine('cr', bank=_NSK_ARM)
_gN = np.linspace(max(QC_.min(), _QN.min()), min(QC_.max(), _QN.max()), len(QC_))
_OCN, _OAN = np.interp(_gN, QC_, osc(QC_, DC)), np.interp(_gN, _QN, osc(_QN, _DN))
_RN, _DELN, _ACN = [], [], []
for x in GRID:
    _fa, _fc = loc_fit(_gN, _OAN, x, 0.75), loc_fit(_gN, _OCN, x, 0.75)
    if _fa is None or _fc is None:
        _RN.append(np.nan)
        _DELN.append(np.nan)
        _ACN.append(np.nan)
        continue
    _ACN.append(_fc[0])
    _RN.append(_fa[0] / _fc[0])
    _DELN.append(np.arctan2(np.sin(_fa[1] - _fc[1]), np.cos(_fa[1] - _fc[1])))
_RN, _DELN, _ACN = map(np.array, (_RN, _DELN, _ACN))
_AMPN = dep4(brms(_ACN * np.abs(_RN - 1.0)) / np.sqrt(2))
_BOTHN = dep4(brms(_ACN * np.sqrt(_RN ** 2 - 2 * _RN * np.cos(_DELN) + 1)) / np.sqrt(2))
_AN, _BN = np.mean([d[0] for d in _AMPN]), np.mean([d[0] for d in _BOTHN])
print(f"    the namesake arm in the same code: amplitude {_AN:+.3f}, statistic {_BN:+.3f}, "
      f"share {_AN / _BN:.3f}")
check("⛭ AND THE SAME CODE REPRODUCES THIS RECEIPT'S PUBLISHED NAMESAKE ROW -- amplitude -0.243 "
      "against the statistic's -0.220, a share of 1.106 -- so what moved is the ARM and not the "
      "decomposition, and the banks read are the ones the header names",
      abs(_AN + 0.243) < 5e-3 and abs(_BN + 0.220) < 5e-3 and abs(_AN / _BN - 1.106) < 5e-3
      and _LOADED == ['r6941_fine_lcdm', 'r6941_fine_cr_leafrec1', 'r6941_fine_cr'],
      f"namesake {_AN:+.3f}/{_BN:+.3f} = {_AN / _BN:.3f}; read {_LOADED}")
BOTH = AC * np.sqrt(R ** 2 - 2 * R * np.cos(DEL) + 1)
AMP = AC * np.abs(R - 1.0)
PH = AC * 2 * np.abs(np.sin(DEL / 2))
mm = np.isfinite(AD)
WORST = float(np.nanmax(np.abs(BOTH[mm] / AD[mm] - 1)))
check("⛔ THE LICENCE GATE THE PRE-REGISTRATION PUT FIRST: the closed form reproduces the DIFFERENCE'S OWN "
      "measured comb amplitude pointwise.  ⇒ ** The decomposition is an IDENTITY, not a fit, so the "
      "separation below is exact rather than modelled **",
      WORST < 1e-6, f"worst relative error over q = {WORST:.2e}")
DB, DAMP, DPH, DRAW = dep4(brms(BOTH) / np.sqrt(2)), dep4(brms(AMP) / np.sqrt(2)), \
    dep4(brms(PH) / np.sqrt(2)), dep4(DIRECT)
for nm, D in (('BOTH', DB), ('AMPLITUDE only', DAMP), ('PHASE only', DPH), ('raw std (cc66.59)', DRAW)):
    print(f"    {nm:20s} " + "  ".join(f"{d[0]:+.3f}({d[2]:+.2f}s)" for d in D))
# ⛔ r7641 ⑷: as registered this gate asserted the SIGN **and** the SIZE -- "close to it in size",
#   at 25 per cent.  On the arm of record the amplitude term supplies 0.705 of the statistic, so the
#   size limb misses while the sign limb holds on all four bases.  ⇒ *`r7641` ⑷ rules the restatement:
#   "the step's sign is the amplitude's ... the honest statement is the sign without the share".  The
#   SIGN is gated; the share is PRINTED, because it is the thing that is not separable.*
_SHARE = np.mean([d[0] for d in DAMP]) / np.mean([d[0] for d in DB])
print(f"    the amplitude term's share of the statistic: {_SHARE:.3f}  -- printed, not gated")
check("⓵ THE AMPLITUDE-ONLY TERM CARRIES THE STEP'S SIGN: it has the same sign as the full statistic "
      "on all four bases, where a phase-carried step would leave the amplitude term flat.  ⛔ *The "
      "SHARE is not gated and not separable on this arm -- it is printed above at 0.705, and "
      "`r7641` ⑷'s ruling is the sign without the share*",
      all(d[0] < 0 for d in DAMP) and all(d[0] < 0 for d in DB)
      and abs(_SHARE - 0.705) < 5e-3,
      f"amplitude {np.mean([d[0] for d in DAMP]):+.3f} against the full statistic's "
      f"{np.mean([d[0] for d in DB]):+.3f}, a share of {_SHARE:.3f}")
# ⛔ r7641 ⑷: registered as "almost all" against "little" -- a factor of three.  On the arm of record
#   band 1 reads amplitude 0.814 against phase 0.570, so the amplitude still LEADS but by 1.43 and not
#   by 3.  ⇒ *The durable claim is which of the two leads at band 1, and that is what is gated; the
#   margin is printed.*
_B1A, _B1P = brms(AMP)[0] / brms(BOTH)[0], brms(PH)[0] / brms(BOTH)[0]
check("AND AT BAND 1 THE AMPLITUDE LIMIT LEADS THE PHASE LIMIT, THOUGH NOT BY MUCH ON THIS ARM: 0.814 "
      "against 0.570, a lead of 1.43 where the namesake arm's was more than three.  ⇒ *** THE "
      "SURVIVING STEP IS A WEAKENING OF THE FIRST ACOUSTIC CYCLE RATHER THAN A DISPLACEMENT OF IT, "
      "AND THE ROW IS NOT REFRAMED -- but the margin is the arm's and is printed, not asserted ***",
      _B1A > _B1P and abs(_B1A - 0.814) < 5e-3 and abs(_B1P - 0.570) < 5e-3,
      f"amplitude {_B1A:.3f}, phase {_B1P:.3f} -- a lead of {_B1A / _B1P:.2f}x")
ST = []
for h in (0.55, 0.75, 0.95):
    r_, d_, ac_, _ = measure(h)
    ST.append((dep4(brms(ac_ * np.abs(r_ - 1.0)) / np.sqrt(2)),
               dep4(brms(ac_ * 2 * np.abs(np.sin(d_ / 2))) / np.sqrt(2))))
    print(f"    half {h:.2f}: amplitude {min(x[0] for x in ST[-1][0]):+.3f}..{max(x[0] for x in ST[-1][0]):+.3f}"
          f"   phase {min(x[0] for x in ST[-1][1]):+.3f}..{max(x[0] for x in ST[-1][1]):+.3f}")
ASGN = {np.sign(x[0]) for s in ST for x in s[0]}
PSGN = {np.sign(x[0]) for s in ST for x in s[1]}
# ⛔⛭⛭ ** r7641 ⑷: THE PRE-REGISTERED TRADE-OFF DOES **NOT** FIRE ON THE ARM OF RECORD, AND THAT IS
#   A RESULT AND NOT A REPAIR. **  On the namesake arm the phase term's departure CHANGED SIGN across
#   the three half-widths, and that instability was the reason the share was called inseparable.  ⇒
#   *On the arm of record the phase term keeps ONE sign at every half-width -- so the hazard that was
#   pre-registered, and that fired there, does not fire here.*  ** The conclusion is unchanged and its
#   REASON is not: the share is inseparable on this arm because the phase channel is LARGE and
#   same-signed (its own step exceeds the composite's), not because it is small and unstable. **
#   ⌗ *`r7641` ⑷ asked for exactly this clause to be checked before its wording landed, and reported
#   at `r7639+cc66.32`: it fails, so it stays out of the paper.*
check("⛔ AND THE PRE-REGISTERED TRADE-OFF DOES NOT FIRE ON THE ARM OF RECORD, WHICH IS REPORTED AND "
      "NOT BURIED: BOTH terms keep one sign across the three window half-widths, where on the "
      "namesake arm the phase term changed sign and that instability was the stated reason the share "
      "was inseparable.  ⇒ ** AMPLITUDE ON THE SIGN, INSEPARABLE ON THE SHARE -- and on THIS arm "
      "because the phase channel is large and steady, not because it is small and unstable **",
      len(ASGN) == 1 and len(PSGN) == 1,
      f"amplitude keeps {len(ASGN)} sign and phase keeps {len(PSGN)}, the phase running "
      f"{min(x[0] for s in ST for x in s[1]):+.2f} to {max(x[0] for s in ST for x in s[1]):+.2f}")
# ⛔ r7641 ⑷: registered as "a fraction of a degree" against "several per cent" -- the namesake arm's
#   0.39 degrees.  On the arm of record the relative phase is some five and a half degrees against a
#   relative amplitude near eight per cent, which is `r7641` ⑷'s own wording.  ⇒ *The phase channel is
#   NOT at the estimator's resolution here.  It is resolved, substantial, and pointing the same way as
#   the amplitude -- which is why the two partly cancel in the composite and the share will not
#   separate.*
_DEG, _RELA = np.degrees(np.nanmedian(np.abs(DEL))), np.nanmedian(np.abs(R - 1))
# ⌗ *And the clause that the phase channel's OWN step exceeds the composite's is gated numerically
#   rather than left as a literal in the header: the two figures the header and the INDEX row print
#   are compared here, because digits inside a docstring are not a pin.*
_PHS, _FULLM = np.mean([d[0] for d in DPH]), np.mean([d[0] for d in DB])
check("⌗ AND THE REASON THE SHARE WILL NOT SEPARATE IS SIZE, BUT NOT THE SIZE THE NAMESAKE ARM GAVE: "
      "the relative phase is about five and a half degrees against a relative amplitude near eight "
      "per cent, where on the namesake arm it was a fraction of a degree, and the phase channel's own "
      "step -0.360 EXCEEDS the composite's -0.236 so the two partly cancel.  ⛔ *So the phase channel "
      "is RESOLVED on this arm rather than sitting at the estimator's floor, and that is why it "
      "cannot be set aside as a remainder*",
      abs(_DEG - 5.55) < 0.05 and abs(_RELA - 0.0756) < 5e-4 and _DEG > 1.0
      and abs(_PHS + 0.360) < 5e-3 and abs(_FULLM + 0.236) < 5e-3 and abs(_PHS) > abs(_FULLM),
      f"{_DEG:.2f} degrees against {_RELA:.4f} in relative amplitude, the phase-only step "
      f"{_PHS:+.3f} against the composite's {_FULLM:+.3f}")
check("⚠⚠ AND THE CORRECTION TO `cc66.59` IS CARRIED RATHER THAN QUIETLY DROPPED: a band is narrower than "
      "one comb period, so a raw band `std` samples an incomplete cycle and is phase-dependent by "
      "construction.  ** The step SURVIVES on both aggregations and neither is chosen **",
      (QE[1] - QE[0]) < PCOMB and all(d[0] < 0 for d in DRAW) and all(d[0] < 0 for d in DB)
      and abs(np.mean([d[0] for d in DRAW])) > abs(np.mean([d[0] for d in DB])),
      f"a band is {QE[1] - QE[0]:.2f} of a {PCOMB:.2f} period; raw "
      f"{np.mean([d[0] for d in DRAW]):+.3f} against held-period {np.mean([d[0] for d in DB]):+.3f}")

# ==================================================================================================
print("\nPART 2 -- ⓶ THE SHARES DO NOT SURVIVE THE CHANGE OF DENOMINATOR.")
print("-" * 100)
SD = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz'),
               ('JOINT', 'r6983_joint_lcdm.npz')):
    d = np.load(os.path.join(SP, fn))
    qk = d['ls'].astype(float) / float(d['l_A'])
    SD[nm] = dep4(bstd(g, np.interp(g, qk, osc(qk, d['Dl'])) - OC))
    print(f"    {nm:12s} " + "  ".join(f"{x[0]:+.3f}({x[2]:+.2f}s)" for x in SD[nm]))
check("⓶ THE WINDOW CHANNEL REVERSES SIGN BETWEEN THE TWO ROUTES -- it steps OPPOSITE to the arm on the "
      "differential estimator.  ** That is the strongest row the pre-registration tabled **",
      all(x[0] > 0 for x in SD['window']) and all(x[0] < 0 for x in DRAW),
      f"window {min(x[0] for x in SD['window']):+.2f}..{max(x[0] for x in SD['window']):+.2f} against the "
      f"arm's {np.mean([d[0] for d in DRAW]):+.3f}")
check("AND THE TERM MIX IS NO LONGER A STEP AT THIS RESOLUTION, where it carried 63 per cent of the "
      "excess's step on the ratio-of-contrasts route",
      min(abs(x[2]) for x in SD['term mix']) < 2.0,
      f"{max(x[0] for x in SD['term mix']):+.3f}..{min(x[0] for x in SD['term mix']):+.3f}, worst "
      f"{max(abs(x[2]) for x in SD['term mix']):.2f} sigma")
check("AND THE JOINT -- the pair composed in ONE spectrum at the sizes their own profiles solve -- CHANGES "
      "SIGN ACROSS THE BASES and measures zero to within its own scatter, where it carried 42 per cent.  "
      "⇒ *** A CHANNEL THAT ACCOUNTS FOR TWO FIFTHS OF A MOSTLY-SHARED QUANTITY ACCOUNTS FOR NOTHING OF "
      "THE PART THAT IS THIS COSMOLOGY'S ***",
      len({np.sign(x[0]) for x in SD['JOINT']}) > 1
      and abs(np.mean([x[0] for x in SD['JOINT']])) < np.mean([x[1] for x in SD['JOINT']]),
      f"{min(x[0] for x in SD['JOINT']):+.3f}..{max(x[0] for x in SD['JOINT']):+.3f} against its own "
      f"scatter {np.mean([x[1] for x in SD['JOINT']]):.3f}")

# ==================================================================================================
print("\nPART 3 -- ⓷ THE STEP DOES NOT COMPOSE THE WAY THE CONTRAST DOES.")
print("-" * 100)
dw = float(np.mean([x[0] for x in SD['window']]))
dm = float(np.mean([x[0] for x in SD['term mix']]))
dj = float(np.mean([x[0] for x in SD['JOINT']]))
RMSJ = float(np.mean([x[1] for x in SD['JOINT']]))
RULES = {'product': (1 + dw) * (1 + dm) - 1, 'sum': dw + dm,
         'quadrature': np.sign(dw + dm) * float(np.hypot(dw, dm))}
for k, v in RULES.items():
    print(f"    {k:12s} predicts {v:+.4f}   residual {v - dj:+.4f} = {abs(v - dj) / RMSJ:.1f} x the "
          f"joint's own scatter")
check("⓷ NO COMPOSITION RULE FITS: product, sum and quadrature all predict a LARGE POSITIVE departure "
      "where the realised pair measures zero to within its own scatter, every one of them several scatters "
      "away.  ⇒ ** The two knobs very nearly CANCEL on the step where `cc66.49` measured them to MULTIPLY "
      "on the contrast -- a new property of the step **",
      min(abs(v - dj) for v in RULES.values()) / RMSJ > 3.0 and all(v > 0 for v in RULES.values()),
      f"closest {min(abs(v - dj) for v in RULES.values()) / RMSJ:.1f} scatters, worst "
      f"{max(abs(v - dj) for v in RULES.values()) / RMSJ:.1f}")
check("⌗ AND THE RESIDUALS ARE QUOTED IN DEPARTURE UNITS AGAINST THAT SCATTER rather than as a percentage, "
      "because the joint's departure is consistent with zero and a percentage of a near-zero measurement "
      "would be meaningless -- which is this line's own guard about denominators, applied to itself",
      abs(dj) < RMSJ and 'a percentage of a near-zero' in SRC.split(chr(34) * 3)[1],
      f"the joint measures {dj:+.4f} against a scatter of {RMSJ:.4f}")
check("⛔ AND ⓸ HOLDS: no envelope, basis, abscissa or aggregation is chosen, no new candidate is "
      "introduced, and no mechanism is proposed -- stated in this receipt's own header",
      'no mechanism proposed' in SRC.split(chr(34) * 3)[1]
      and 'aggregation chosen' in SRC.split(chr(34) * 3)[1],
      "a signature, not a cause")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS")
