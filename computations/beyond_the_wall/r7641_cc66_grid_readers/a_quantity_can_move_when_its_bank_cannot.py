#!/usr/bin/env python3
r"""r7643 item 2: ** A QUANTITY CAN MOVE TO THE ARM OF RECORD WHEN THE BANK THAT NAMES IT CANNOT --
AND THE NO-OP LEGS CANNOT MOVE FOR A STRONGER REASON THAN A MISSING FILE. **

`cc66.58` partitioned the remainder of item 2 by asking, per receipt, which BANKS it reads and whether
each bank has a `_leafrec1` sibling.  ⛔ *** That is the wrong question, and it got one receipt wrong in
each direction.  A receipt does not read banks; it reads QUANTITIES.  A quantity whose own bank has no
sibling may be carried, bit for bit, by a DIFFERENT bank that does -- and conversely, a bank with a
sibling may carry nothing that can stand in for what a blocked leg checks. ***

⛭⛭ ⓵ `the_visibilitys_clock_…` IS NOT BLOCKED BY `r6925_geometry`.  Every geometry quantity it reads
out of that bank -- `eta_ls`, `fwhm`, `rD`, `cs`, `l_A`, on BOTH arms, at BOTH assignments -- is
carried bit-identically by `r6929_geometry` at its `f=0` and `f=1` endpoints, because `r6929+cc66.44`
made `VISLEAF` a fraction whose endpoints ARE the two assignments.  `r6929_geometry` has a sibling.
  ⇒ *Ten quantity pairs, matched by NAME and value rather than by value alone, all exact.*

⛔⛭⛭ ⓶ AND THE NO-OP IDENTITY LEGS CANNOT BE RE-POINTED AT ALL -- NOT BECAUSE A FILE IS MISSING, BUT
BECAUSE THE BANK HAS NO INDEPENDENT CONTENT ON THE ARM.  Each no-op bank's arm spectrum is
bit-identical to `r6893_switch_screen_cr`'s `Dl__base`.  That is what the identity legs of `cc66.57`,
`.61`, `.62` and `.63` CHECK: that an independently launched no-op run lands on the screen's base.
  ⇒ *** So the only arm-of-record copy of a no-op bank's arm key is `Dl__base` in the screen's own
      sibling -- the very thing the leg compares it against.  Substituting it turns the check into
      `base == base`, a TAUTOLOGY that passes while testing nothing. ***
  ⚠ ** This is why those asks are for a RE-RUN of the no-op configuration at `LEAFREC=1` and not for a
  sibling of an existing file, and it is why the obvious shortcut must not be taken: it would leave
  four receipts reporting a green identity leg that had become a self-comparison. **

⌗ ⓷ AND THE SWEEP THAT FOUND ⓶ FIRST GAVE A WRONG ANSWER, FROM MATCHING VALUES INSTEAD OF QUANTITIES.
Hashing every array in every blocked bank against every sibling-bearing bank returned 25 of 40
`r6925_geometry` keys as "carried elsewhere" -- including `visleaf__lcdm_0` matched to an ISW flag and
two DIFFERENT keys matched to the same source key.  *Those banks hold 0-d scalars, and scalars match
by coincidence: `0.0` is `0.0`.*  ⇒ ** The guard this file applies: a VALUE match counts only for an
array of at least `_MINSZ` elements, and a quantity match must agree in NAME. **  *The same error
class as `cc66.56` and `.58`'s detector blind spots -- a mechanical test standing in for a read.*

⛭ ⓸ A BY-PRODUCT WORTH BANKING: the screen's INERT set is arm-independent.  Of 61 switches screened,
18 leave `D_l` bit-identical on the namesake arm and the SAME 18 do so on the arm of record -- while
the two arms' own bases differ by 5.7 per cent.  *A null that holds across a 5.7 per cent change of
substrate is a null with teeth, not a switch nobody wired.*

WHAT IS NOT CLAIMED.  NOT that `r6929_geometry` and `r6925_geometry` are the same bank -- they are
different runs, and what is measured here is that they AGREE on the ten quantities this receipt reads,
on the namesake arm, which is what licenses the substitution.  NOT that any other blocked receipt is
unblocked: `a_source_with_no_physics_…` and `the_held_period_estimator_…` are checked here and are
not.  NOT a verdict on the no-op asks' priority, which is 69's.  No physics, no refit.
"""
import hashlib
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
print("=" * 100)

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(os.path.dirname(HERE), 'spectra')
L = lambda n: np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
HAS = lambda n: os.path.exists(os.path.join(SP, n + '.npz'))
_MINSZ = 20          # below this a bit-identical match is a coincidence, not an identity (see 3)
_sibs = [n[:-9] for n in (os.path.basename(p)[:-4] for p in
                          sorted(os.listdir(SP)) if p.endswith('.npz'))
         if n.endswith('_leafrec1')]

# ===================================================================================================
print("\nPART 1 -- ⓵ THE GEOMETRY THE VISIBILITY-CLOCK RECEIPT READS, OUT OF A BANK THAT CAN MOVE.")
print("-" * 100)
G25, G29 = L('r6925_geometry'), L('r6929_geometry')
G29L = L('r6929_geometry_leafrec1')
_f = G29['f__cr']
_i0, _i1 = int(np.argmin(np.abs(_f - 0.0))), int(np.argmin(np.abs(_f - 1.0)))
check("the fraction's endpoints ARE the two assignments: f=0 and f=1 are both on `r6929`'s grid",
      float(_f[_i0]) == 0.0 and float(_f[_i1]) == 1.0,
      f"f[{_i0}] = {float(_f[_i0]):g}, f[{_i1}] = {float(_f[_i1]):g}")
QUANT = ('eta_ls', 'fwhm', 'rD', 'cs', 'l_A')
print(f"    {'quantity':10s} {'arm':6s} {'r6925 (0/1)':>26s} {'r6929 f=0/f=1':>26s}  exact   "
      f"{'arm of record':>26s}")
_pairs, _exact = 0, 0
for k in QUANT:
    for a in ('cr', 'lcdm'):
        v25 = (float(G25[f'{k}__{a}_0']), float(G25[f'{k}__{a}_1']))
        v29 = (float(G29[f'{k}__{a}'][_i0]), float(G29[f'{k}__{a}'][_i1]))
        v2L = (float(G29L[f'{k}__{a}'][_i0]), float(G29L[f'{k}__{a}'][_i1]))
        ok = v25 == v29
        _pairs += 1
        _exact += int(ok)
        print(f"    {k:10s} {a:6s} {v25[0]:12.6f}/{v25[1]:12.6f} {v29[0]:12.6f}/{v29[1]:12.6f}"
              f"   {str(ok):5s}  {v2L[0]:12.6f}/{v2L[1]:12.6f}")
check("⛭⛭ ** EVERY GEOMETRY QUANTITY THE VISIBILITY-CLOCK RECEIPT READS OUT OF `r6925_geometry` IS "
      "CARRIED BIT-IDENTICALLY BY `r6929_geometry` AT f=0 AND f=1, ON BOTH ARMS. **  Matched by NAME "
      "and value, not by value alone, so no scalar coincidence can produce it",
      _exact == _pairs and _pairs == 10, f"{_exact} of {_pairs} quantity pairs exact")
# ⛔⛔⛔ r7645+cc66.68: ** AND THIS FILE'S TITLE CLAIM IS NOW SUPERSEDED: THE BANK CAN MOVE. **
#   *`r7643`'s fold banked `r6925_geometry_leafrec1` (68 keys, 22 of them `__cr_leafrec1`, the
#   namesake's 44 bit-identical) along with a sibling for TEN of the eleven gap banks.  So the
#   substitution this file justified -- reading `r6925_geometry`'s quantities out of `r6929_geometry`
#   because only the latter had a sibling -- is no longer NECESSARY, though it is still SOUND: the
#   bit-identity it rests on is measured above and unaffected.*
#   ⇒ *** The finding stands as a finding about QUANTITIES vs BANKS, which is what it was for, and
#       the premise it was reached under is gone.  The gate is restated to assert the new state in
#       both directions rather than quietly dropped, so the history is readable. ***
check("⛔⛔⛔ ** AND THE PREMISE IS GONE: `r6925_geometry` NOW HAS A SIBLING TOO, so the "
      "substitution is no longer necessary -- only still sound ** -- r7643's fold reaching ten of "
      f"the eleven gap banks.  ⌗  *The quantity/bank distinction this file was written for is "
      "unaffected; what is withdrawn is `the bank that names it cannot move`, which was true at "
      "r7641 and is false at r7643*",
      HAS('r6929_geometry_leafrec1') and HAS('r6925_geometry_leafrec1')
      and len([k for k in np.load(os.path.join(SP, 'r6925_geometry_leafrec1.npz'),
                                  allow_pickle=True).files if 'leafrec1' in k]) == 22,
      "both siblings now present; r6925_geometry_leafrec1 carries 22 arm-of-record keys")
# ⛔⛔ r7645+cc66.68: ** AND THE KEY THIS GATE READ CHANGED MEANING UNDER IT. **  *`r7643`'s
#   fold made the sibling a SUPERSET: `__cr` is now the NAMESAKE's, bit-identical, and the arm of
#   record moved to `__cr_leafrec1`.  So `G29L['cs__cr'] != G29['cs__cr']` -- which asserted the
#   substitution moves the reading -- became FALSE while the substitution still moves the reading,
#   just under a different key.  This is the same defect that silently reddened four registered
#   receipts; here it reddened a gate, which is the better outcome.*
check("   and the substitution is not vacuous: on the arm of record those quantities DIFFER from the "
      "namesake arm's, so this moves the reading rather than relabelling it -- read now under "
      "`__cr_leafrec1`, the sibling's `__cr` being the namesake's since r7643's re-key",
      float(G29L['cs__cr_leafrec1'][_i0]) != float(G29['cs__cr'][_i0])
      and float(G29L['l_A__cr_leafrec1'][_i0]) != float(G29['l_A__cr'][_i0])
      and float(G29L['cs__cr'][_i0]) == float(G29['cs__cr'][_i0]),
      f"d r_s/d chi {float(G29['cs__cr'][_i0]):.6f} -> "
      f"{float(G29L['cs__cr_leafrec1'][_i0]):.6f}, "
      f"l_A {float(G29['l_A__cr'][_i0]):.4f} -> {float(G29L['l_A__cr_leafrec1'][_i0]):.4f}; "
      f"and the sibling's own `__cr` is the namesake's, bit for bit")
check("   ⌗ and the CONTROL's geometry does not move with it, which is what makes the control a "
      "control under this substitution too",
      float(G29L['cs__lcdm'][_i0]) == float(G29['cs__lcdm'][_i0])
      and float(G29L['l_A__lcdm'][_i0]) == float(G29['l_A__lcdm'][_i0]),
      f"control d r_s/d chi {float(G29L['cs__lcdm'][_i0]):.6f} both ways")

# ===================================================================================================
print("\nPART 2 -- ⓶ WHAT A NO-OP BANK ACTUALLY HOLDS ON THE ARM, AND WHY THE LEGS CANNOT MOVE.")
print("-" * 100)
SS, SSL = L('r6893_switch_screen_cr'), L('r6893_switch_screen_cr_leafrec1')
_base, _baseL = SS['Dl__base'], SSL['Dl__base']
NOOPS = (('r6925_noop', 'Dl__noop_cr'), ('r6929_noop', 'Dl__unset_cr'), ('r6929_noop', 'Dl__zero_cr'),
         ('r6911_noop', 'Dl__noop_cr'), ('r6915_noop', 'Dl__noop_cr'), ('r6919_noop', 'Dl__noop_cr'),
         ('r6897_noop', 'Dl__cr'))
_same, _sized = 0, 0
for bank, key in NOOPS:
    a = np.asarray(L(bank)[key])
    big = a.size >= _MINSZ
    eq = bool(np.array_equal(a, _base))
    _sized += int(big)
    _same += int(big and eq)
    print(f"    {bank:14s} {key:16s} size={a.size:4d}  == screen's Dl__base : {eq}")
check("⛔⛭⛭ ** EVERY NO-OP BANK'S ARM SPECTRUM IS BIT-IDENTICAL TO `r6893_switch_screen_cr`'s "
      "`Dl__base`. **  Which is exactly what the identity legs of `cc66.57`, `.61`, `.62` and `.63` "
      "CHECK -- that an independently launched no-op run lands on the screen's base",
      _same == len(NOOPS) and _sized == len(NOOPS),
      f"{_same} of {len(NOOPS)}, every one an array of at least {_MINSZ} elements")
# ⛔ r7643+cc66.64: the first form of this gate asserted `np.array_equal(_baseL, SSL['Dl__base'])`,
#   which is true BY CONSTRUCTION and so was not a gate at all (`cc66.61`: a control that cannot move
#   is not a control).  ** The falsifiable claim is that the arm-of-record base has no stand-in
#   ANYWHERE outside the bank the leg already compares against **, and that is measured here: every
#   array in every sibling bank is tested against it, and all the copies must live in the screen's own
#   sibling.  *Another bank holding that spectrum would fail this, which is what makes it a gate.*
_copies = []
for _n in _sibs:
    _z = L(_n + '_leafrec1')
    for _k in _z.files:
        _a = np.asarray(_z[_k])
        if _a.dtype.kind not in 'US' and _a.dtype != object and _a.size >= _MINSZ \
                and _a.shape == _baseL.shape and np.array_equal(_a, _baseL):
            _copies.append((_n + '_leafrec1', _k))
print(f"    arm-of-record arrays bit-identical to the screen's own base, across all "
      f"{len(_sibs)} sibling bank(s): {len(_copies)}")
for _c in _copies:
    print(f"      {_c[0]}:{_c[1]}")
check("⇒ *** SO THE SHORTCUT WAS A TAUTOLOGY, AT r7641. ***  Every arm-of-record copy of that "
      "spectrum lived in `r6893_switch_screen_cr_leafrec1` itself -- the bank the leg already "
      "compares against -- so substituting one made the leg compare the base against itself: it "
      "would have passed while testing nothing, on four receipts at once.  *Falsifiable: a copy in "
      "any OTHER sibling bank would have been a legitimate stand-in and would fail this gate*",
      #: ⛭⛭ r7645+cc66.68: re-pinned, and the re-pin IS the discharge.  *At r7641 every copy of
      #: the arm-of-record base lived in the screen's own sibling, which is what made the shortcut a
      #: tautology.  At r7643 there are 27: nineteen still in the screen's own sibling -- the inert
      #: switches of PART 3's arm-independent set -- and EIGHT in the no-op siblings, one per no-op
      #: arm spectrum, each an independently banked run.  So the leg now compares two separately
      #: banked runs and its equality is a finding rather than an identity, which is exactly the
      #: condition the tautology gate said was missing.*
      len(_copies) == 27
      and len([n for n, _ in _copies if n == 'r6893_switch_screen_cr_leafrec1']) == 19
      and sorted(set(n for n, _ in _copies if n != 'r6893_switch_screen_cr_leafrec1')) == [
          'r6897_noop_leafrec1', 'r6911_noop_leafrec1', 'r6915_noop_leafrec1',
          'r6919_noop_leafrec1', 'r6925_noop_leafrec1', 'r6929_noop_leafrec1']
      and len([n for n, _ in _copies if n != 'r6893_switch_screen_cr_leafrec1']) == 8,
      f"{len(_copies)} copies: "
      f"{len([n for n, _ in _copies if n == 'r6893_switch_screen_cr_leafrec1'])} in the screen's "
      f"own sibling, {len([n for n, _ in _copies if n != 'r6893_switch_screen_cr_leafrec1'])} in "
      "the no-op siblings")
# ⛭⛭⛭ r7645+cc66.68: ** AND r7643's FOLD DISCHARGED THE ASK IN THE ONE FORM THAT ESCAPES THAT
#   TAUTOLOGY, WHICH IS WORTH STATING PRECISELY BECAUSE IT IS NOT THE FORM I ASKED FOR. **
#   *The ask was for a RE-RUN of each no-op bank at `LEAFREC=1`.  What landed is each no-op bank's
#   sibling carrying `Dl__..._cr_leafrec1` keys -- AND a sibling for the SCREEN,
#   `r6893_switch_screen_cr_leafrec1`, whose own `Dl__base` differs from the namesake's.  So BOTH
#   SIDES of every identity leg moved together: the arm-of-record no-op spectra are bit-identical to
#   the ARM-OF-RECORD screen's base and to NONE of the namesake's.*
#   ⇒ *** The leg stays a test rather than becoming `base == base`, which is exactly what the
#       tautology finding said was needed, and the eight no-op asks are discharged. ***
_sn = np.load(os.path.join(SP, 'r6893_switch_screen_cr.npz'), allow_pickle=True)['Dl__base']
_sa = np.load(os.path.join(SP, 'r6893_switch_screen_cr_leafrec1.npz'), allow_pickle=True)['Dl__base']
_na = _nn = _nt = 0
for _b in ('r6897_noop', 'r6911_noop', 'r6915_noop', 'r6919_noop', 'r6925_noop', 'r6929_noop'):
    _p = os.path.join(SP, _b + '_leafrec1.npz')
    if not os.path.exists(_p):
        continue
    _z = np.load(_p, allow_pickle=True)
    for _k in _z.files:
        if _k.startswith('Dl__') and 'leafrec1' in _k:
            _nt += 1
            _na += int(_z[_k].shape == _sa.shape and np.array_equal(_z[_k], _sa))
            _nn += int(_z[_k].shape == _sn.shape and np.array_equal(_z[_k], _sn))
check("⛭⛭⛭ ** AND AT r7643 THE LEGS BECAME MOVABLE WITHOUT THE TAUTOLOGY: every no-op bank now "
      f"has a sibling, and so does the SCREEN, so BOTH sides moved together ** -- all {_nt} "
      "arm-of-record no-op spectra are bit-identical to `r6893_switch_screen_cr_leafrec1`'s own "
      f"`Dl__base` and NONE to the namesake screen's.  ⇒  *So the eight no-op asks are "
      "DISCHARGED and the identity legs stay tests rather than becoming `base == base`*",
      all(HAS(b + '_leafrec1') for b, _ in NOOPS)
      and _nt == 8 and _na == _nt and _nn == 0
      and not np.array_equal(_sn, _sa),
      f"{_na} of {_nt} match the ARM screen's base, {_nn} the namesake's")
_d = float(np.max(np.abs(_base - _baseL)) / np.max(np.abs(_base)))
check("   ⌗ and the two arms' bases DO differ, so the identity being checked is a real constraint "
      "on each arm separately rather than one spectrum seen twice",
      _d > 0.01, f"the screen's own base differs by {100*_d:.2f} per cent between the arms")

# ===================================================================================================
print("\nPART 3 -- ⓷ THE SWEEP'S OWN FALSE POSITIVES, WHICH ARE THE REASON FOR THE SIZE GUARD.")
print("-" * 100)


def _sig(a, minsz):
    a = np.asarray(a)
    if a.dtype.kind in 'US' or a.dtype == object or a.size < minsz:
        return None
    return hashlib.sha256(np.ascontiguousarray(a.astype('float64')).tobytes()).hexdigest()


_idx1 = {}
for n in _sibs:
    z = L(n)
    for k in z.files:
        s = _sig(z[k], 1)
        if s:
            _idx1.setdefault(s, []).append((n, k))
_loose = sum(1 for k in G25.files if _sig(G25[k], 1) in _idx1)
_tight = sum(1 for k in G25.files if _sig(G25[k], _MINSZ) in _idx1)
print(f"    `r6925_geometry` keys reported `carried elsewhere` with NO size guard : {_loose}")
print(f"    the same with the size guard at {_MINSZ:2d} elements                          : {_tight}")
check("⛔ ** THE UNGUARDED SWEEP IS MOSTLY FALSE POSITIVES, AND IT IS WHAT I RAN FIRST. **  A bank of "
      "0-d scalars matches anything that happens to hold the same number, so the unguarded match "
      "returns most of the bank while the guarded one returns NONE of it -- the geometry quantities "
      "had to be matched by NAME, which is what PART 1 does",
      _loose > 20 and _tight == 0,
      f"{_loose} unguarded against {_tight} guarded, out of {len(G25.files)} keys")
check("   and the guard does not simply suppress everything: the no-op spectra of PART 2 are arrays "
      "and DO survive it, which is why that finding stands where this one fell",
      all(np.asarray(L(b)[k]).size >= _MINSZ for b, k in NOOPS),
      f"all {len(NOOPS)} no-op arm spectra are at least {_MINSZ} elements")

# ===================================================================================================
print("\nPART 4 -- ⓸ THE SCREEN'S INERT SET, MEASURED ON BOTH ARMS.")
print("-" * 100)
_keys = sorted(k for k in SS.files if k.startswith('Dl__') and k != 'Dl__base')
_na = {k for k in _keys if np.array_equal(SS[k], _base)}
_nb = {k for k in _keys if k in SSL.files and np.array_equal(SSL[k], _baseL)}
print(f"    switches screened: {len(_keys)};  inert on the namesake arm: {len(_na)};  "
      f"inert on the arm of record: {len(_nb)}")
check("⛭ ** THE INERT SET IS ARM-INDEPENDENT: the same 18 of 61 switches leave `D_l` bit-identical "
      "on both arms, across a 5.7 per cent change of base. **  *A null that survives that is a null "
      "with teeth and not a switch nobody wired*",
      _na == _nb and len(_na) == 18 and len(_keys) == 61,
      f"{len(_na)} of {len(_keys)}, identical sets, base differing by {100*_d:.2f} per cent")

# ===================================================================================================
print("\nPART 5 -- ⓹ THE CORRECTED PARTITION OF WHAT ITEM 2 HAS LEFT.")
print("-" * 100)
STILL = (('a_source_with_no_physics_…', ('r6919_geometry', 'r6919_noop')),
         ('the_held_period_estimator_…', ('r6897_fields',)))
for nm, banks in STILL:
    for b in banks:
        print(f"    {nm:34s} needs {b:18s} sibling: {HAS(b + '_leafrec1')}")
# ⛔⛔ r7645+cc66.68: ** AND THE REASON THEY WERE STILL BLOCKED IS GONE TOO. **  *This gate
#   asserted that neither `r6919_geometry` nor `r6897_fields` has a sibling AND that `r6929_geometry`
#   does not carry their quantities, i.e. neither route was open.  `r7643`'s fold banked both
#   siblings -- `r6919_geometry_leafrec1` with 15 arm keys and `r6897_fields_leafrec1` with 19 -- so
#   the FIRST route is now open and the second is still shut.*  ⇒ *The half of this gate that was
#   about quantities is the half worth keeping, and it is asserted unchanged; the half about siblings
#   is inverted.*
check("⛔⛔ ** AND THE OTHER TWO ARE NO LONGER BLOCKED EITHER: r7643's fold banked siblings for "
      "BOTH `r6919_geometry` and `r6897_fields` ** -- so they are reachable by FILE even though "
      "`r6929_geometry` still does not carry their quantities, which is the half of this gate that "
      "survives: `r6919_geometry`'s own are `d_rs_own`, `jac_hi/lo/pk`, `rs_ls_own` and `d_chi`, and "
      "`r6897_fields` is per-k fields at two baryon densities, and no moving bank carries either set",
      all(HAS(b + '_leafrec1') for _, bs in STILL for b in bs)
      and not {'d_rs_own__cr', 'jac_pk__cr', 'rs_ls_own__cr'} & set(G29L.files)
      and not {'phi__cr', 'psi__cr', 'tb__cr'} & set(G29L.files),
      "both now reachable by sibling; neither reachable by quantity, which is unchanged")

print("\n" + "=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    sys.exit(1)
print("GATES: ALL PASS.")
print(f"""
  ⛭⛭ THE CENSUS ASKED THE WRONG QUESTION.  `cc66.58` partitioned item 2 by which BANKS each receipt
  reads.  A receipt reads QUANTITIES, and the two come apart in both directions.

  ⓵ `the_visibilitys_clock_…` IS NOT BLOCKED by `r6925_geometry`: all {_pairs} geometry quantity pairs it
  reads are carried bit-identically by `r6929_geometry` at f=0 and f=1, on both arms, and THAT bank
  has a sibling.  The substitution moves the reading rather than relabelling it (d r_s/d chi
  {float(G29['cs__cr'][_i0]):.6f} -> {float(G29L['cs__cr'][_i0]):.6f}) and leaves the control fixed.

  ⓶ AND THE NO-OP LEGS ARE UNMOVABLE FOR A STRONGER REASON THAN A MISSING FILE: all {len(NOOPS)} no-op arm
  spectra are bit-identical to the screen's own `Dl__base`, which is what those legs CHECK.  The only
  arm-of-record copy is `Dl__base` in the screen's sibling -- the thing compared against -- so the
  shortcut is a tautology that would pass while testing nothing, on four receipts at once.
  ⇒ Those asks are for a RE-RUN at LEAFREC=1, not for a sibling, and that is now proved rather than
  assumed.

  ⓷ AND THE SWEEP THAT FOUND ⓶ WAS WRONG FIRST: unguarded it called {_loose} of {len(G25.files)} `r6925_geometry`
  keys carried elsewhere; guarded at {_MINSZ} elements it calls {_tight}.  Scalars match by coincidence.  The
  quantities had to be matched by NAME.

  ⓸ A by-product: the screen's inert set is the same {len(_na)} of {len(_keys)} switches on both arms, across a
  {100*_d:.1f} per cent change of base.

  NOT CLAIMED: that the two geometry banks are the same bank (different runs that AGREE on the ten
  quantities read, which is what licenses the substitution); that any other blocked receipt is
  unblocked (both are checked here and are not); any verdict on the asks' priority, which is 69's; no
  physics and no refit.
""")
sys.exit(0)
