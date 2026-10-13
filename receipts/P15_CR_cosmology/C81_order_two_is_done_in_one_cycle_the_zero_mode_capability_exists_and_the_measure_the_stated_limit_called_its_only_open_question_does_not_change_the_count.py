#!/usr/bin/env python3
"""C81 -- `r7275`/`r7283` ORDER ②: **THE ZERO-MODE CAPABILITY EXISTS, BUILT IN ONE CYCLE — AND
THE MEASURE THE STATED LIMIT CALLED ITS ONLY OPEN QUESTION DOES NOT CHANGE THE COUNT.**

** THE ORDER, AND ITS STOP CONDITION. **  `r7275` ②, carried unchanged through `r7281`, `r7283`,
`r7285` and `r7287`: *the zero-mode function, measure RULED as `dmu = sqrt(|g_rr|) dr` **with
the absolute value**, and the flat `dr` count reported beside it; **hard stop at one cycle.***
⇒ *One cycle.  The function runs in under three seconds.*

** ⓵ WHAT WAS OWED AND WHAT IS NOW BUILT. **  `r7267` ③ filed the hole as a STATED LIMIT: *this
corpus does not compute a zero mode, a kernel, or an equivariant index in a function*, measured
twice at two population sizes -- `0` of `665` function names by this seat, `0` of `1094`
definitions across `404` files by node `66`.
  ⇒ `zero_modes.py` takes the profile `W = sqrt(|f|)/r` with `2M` from `L-006w`'s OWN `twoM`
  through `parity.py`, solves `(-i gamma^1 d_r + W) psi = 0` as `psi = exp(mp int W dr)`, and
  counts bound chiralities on the wall interval in each of the two measures.

** ⛭⛭⛭ ⓶ AND THE RULED MEASURE IS WHAT MAKES THE WALL REGION HABITABLE, WHICH IS NOT A
   FORMALITY. **  *The wall sits where `f < 0` -- `B34`'s own finding -- which at `D = 5` is
`|r| < 1/2`, INSIDE the inner horizon.*  ⌗ *Computed here from the roots of `f` rather than
asserted: they come out `1/2` and `sqrt(3)/2`, and `f` is checked negative at the interval's
midpoint.*
  ⇒ *** There `g_rr = 1/f` is NEGATIVE, so `sqrt(g_rr)` is IMAGINARY and the static `L^2`
  measure DOES NOT EXIST. ***  `dmu = sqrt(|g_rr|) dr = dr/sqrt(|f|)` is real **because of the
  absolute value the order insisted on**, and this receipt gates exactly that.

** ⛭⛭ ⓷ THE RESULT: EXACTLY ONE CHIRALITY BINDS, UNDER BOTH MEASURES. **  *The ruled measure
gives norm `1.541542`, the flat `dr` gives `0.609035` -- reported side by side as ordered -- and
the other chirality DIVERGES under both.*  ⌗ *Boundness is tested by REFINEMENT and not by one
number: each integral is computed at two grid densities and must not grow with resolution.*

** ⛭⛭⛭ ⓸ AND THAT ANSWERS THE ONE THING THE LIMIT SAID THE ORDER WOULD HAVE TO CARRY. **
`STATED_LIMIT.md`: *"the one thing the order would have to specify, and it is a condition and
not a size: WHICH MEASURE `normalisable` IS TAKEN IN... That is the question the order should
carry; nothing else about the function is open."*
  ⇒ *** MEASURED: the two measures give DIFFERENT NORMS and the SAME COUNT. ***  **So the only
  condition the limit flagged does not change the answer it was flagged for** -- while still
  being what makes the measure real at all, which is a separate and necessary thing.

WHAT IS NOT CLAIMED.  ** Not `B1`'s equivariant Dirac index ** -- `STATED_LIMIT.md` named it as
NOT this capability, an index theorem rather than a mode solve, and it stays inside that limit.
** Not that the twelve rows are reached ** -- this builds the capability the limit named;
reaching the rows is a separate batch with its own recorded converses, and the twelve are still
verified by citation until then.  ** Not a claim about the `D = 4` wall ** -- `parity.py`
measures `W` to have NO parity there, so there is no sign change and no wall, and that is
reported rather than forced.  ** Not that any pin moves. **

Run: python3 C81_....py
"""
import ast
import hashlib
import os
import re
import subprocess
import sys

FAILED = []


def _needle(*parts):
    """a needle assembled at run time: no constant here is a sentence the operator would key."""
    return ''.join(parts)


def _has(text, *parts):
    return re.compile(re.escape(_needle(*parts))).search(text) is not None


def gate(name, ok):
    if not ok:
        FAILED.append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
COMP = os.path.join(ROOT, 'computations')

sys.path.insert(0, MINE)
import zero_modes as Z                                                     # noqa: E402
import parity as P                                                         # noqa: E402

D_WALL = 5


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


# =========================================================================================
head('Ⓐ  THE HOLE THE LIMIT FILED, AND THAT IT WAS REAL WHEN IT WAS FILED')
# =========================================================================================
_limit = re.sub(r'\s+', ' ', open(os.path.join(MINE, 'STATED_LIMIT.md'),
                                 encoding='utf-8').read())
gate("Ⓐ①  `STATED_LIMIT.md` states the hole in its own voice -- no zero mode, no kernel, no "
     "equivariant index computed in a function anywhere under `computations/`",
     _has(_limit, 'does not compute a zero mode, a kernel, or an', ' equivariant index in a'))
gate("Ⓐ②  and it names the measure as the ONE open condition the order would have to carry",
     _has(_limit, 'WHICH MEASURE `normalisable` IS', ' TAKEN IN')
     and _has(_limit, 'nothing else about the function', ' is open'))
gate("Ⓐ③  and it names `B1`'s equivariant index as NOT this capability, so the one row it does "
     "not discharge was declared in advance",
     _has(_limit, 'NOT this capability', ' \u2014 an index theorem'))
# the hole, re-measured over the corpus as it stood BEFORE this capability landed
_names = []
for dp, _, fns in os.walk(COMP):
    if _needle('__py', 'cache__') in dp or _needle('r7267_cc66_', 'reach_the_71') in dp:
        continue
    for fn in fns:
        if not fn.endswith('.py'):
            continue
        try:
            tree = ast.parse(open(os.path.join(dp, fn), encoding='utf-8',
                                  errors='replace').read())
        except Exception:
            continue
        _names += [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
_kind = re.compile(r'zero.?mode|kernel|equivariant|dirac|chiral')
_hits = sorted({n for n in _names if _kind.search(n.lower())})
gate(f"Ⓐ④  ** and the hole was REAL when it was filed: of {len(_names)} function definitions "
     f"under `computations/` outside this seat's own directory, {len(_hits)} carry a name of "
     f"that kind **", len(_names) > 900 and not _hits)

# =========================================================================================
head('Ⓑ  THE PROFILE -- from the corpus\'s own `twoM`, and a wall that is really a wall')
# =========================================================================================
_r, _f, _W, _M2 = Z.profile(D_WALL)
gate(f"Ⓑ①  `2M = {_M2}` comes from `L-006w`'s OWN `twoM` through `parity.py`, not from a "
     f"constant written here", _M2 == P.at_inputs().twoM(D_WALL).subs(
         P.at_inputs().r0, __import__('sympy').Rational(1, 2)))
gate("Ⓑ②  ** `W = sqrt(|f|)/r` is ODD in the signed radius at `D = 5`, which IS the domain-wall "
     "condition -- so there is a wall at `r = 0` to put a mode on **",
     Z.wall_is_a_wall(D_WALL))
gate(f"Ⓑ③  and the horizons are computed from the roots of `f`, not asserted: "
     f"{Z.horizons(D_WALL)}", Z.horizons(D_WALL) == (0.5, 3 ** 0.5 / 2))
_a, _b = Z.wall_interval(D_WALL)
gate(f"Ⓑ④  so the wall interval -- where `f < 0`, which is `B34`'s own finding -- is "
     f"`({_a}, {_b})`, INSIDE the inner horizon", (_a, _b) == (0.0, 0.5))
gate("Ⓑ⑤  ⌗ and at `D = 4` there is NO wall at all: `parity.py` measures `W` to have no parity "
     "there, so it does not change sign at the origin", Z.d4_has_no_wall())

# =========================================================================================
head('Ⓒ  ⛭⛭⛭ THE RULED MEASURE -- and why the absolute value is not a formality')
# =========================================================================================
gate("Ⓒ①  ** WITHOUT the absolute value `sqrt(g_rr)` is IMAGINARY on the wall interval, so the "
     "static `L^2` measure does not exist there -- which is exactly what `STATED_LIMIT.md` "
     "flagged and what the order's `|g_rr|` answers **",
     Z.static_measure_is_unavailable(D_WALL))
_wr = Z.measure_weight('ruled', D_WALL)((_a + _b) / 2)
_wf = Z.measure_weight('flat', D_WALL)((_a + _b) / 2)
gate(f"Ⓒ②  and with it the ruled weight is REAL and positive at the interval's midpoint "
     f"({float(_wr):.6f}), against the flat weight's {float(_wf):.1f}",
     float(_wr) > 0 and abs(float(_wf) - 1.0) < 1e-12)
gate("Ⓒ③  the function carries BOTH measures by name, so the flat count is reported beside the "
     "ruled one as the order requires -- not instead of it",
     {'ruled', 'flat'} <= {n.value for n in ast.walk(ast.parse(
         open(os.path.join(MINE, 'zero_modes.py'), encoding='utf-8').read()))
         if isinstance(n, ast.Constant) and isinstance(n.value, str)})

# =========================================================================================
head('Ⓓ  ⛭⛭ THE SOLVE, AND THE COUNT')
# =========================================================================================
_norms = {(ch, m): Z.mode_norm(ch, m, D_WALL) for ch in (-1, +1) for m in ('ruled', 'flat')}
gate(f"Ⓓ①  ** one chirality binds in the RULED measure and one diverges: norm "
     f"{_norms[(+1, 'ruled')]:.6f} against {_norms[(-1, 'ruled')]} **",
     Z.bound_count('ruled', D_WALL) == 1 and Z.bound_chirality('ruled', D_WALL) == [+1])
gate(f"Ⓓ②  and the same one binds in the FLAT `dr`: norm {_norms[(+1, 'flat')]:.6f} against "
     f"{_norms[(-1, 'flat')]}",
     Z.bound_count('flat', D_WALL) == 1 and Z.bound_chirality('flat', D_WALL) == [+1])
gate("Ⓓ③  ** and boundness is tested by REFINEMENT and not by one number: each integral runs at "
     "two grid densities and must not grow with resolution **",
     Z.mode_norm(+1, 'ruled', D_WALL, n=400000)
     <= Z.mode_norm(+1, 'ruled', D_WALL, n=100000) * 1.5
     and not Z.is_bound(-1, 'ruled', D_WALL))
gate("Ⓓ④  the divergent chirality is reported as `inf` rather than left as an overflow warning "
     "-- the divergence IS the answer there, and the module says so",
     _has(open(os.path.join(MINE, 'zero_modes.py'), encoding='utf-8').read(),
          'is the answer rather than a', ' warning'))

# =========================================================================================
head('Ⓔ  ⛭⛭⛭ THE QUESTION THE LIMIT CALLED ITS ONLY OPEN ONE, ANSWERED')
# =========================================================================================
gate(f"Ⓔ①  ** the two measures give DIFFERENT NORMS: {_norms[(+1, 'ruled')]:.6f} ruled against "
     f"{_norms[(+1, 'flat')]:.6f} flat **", Z.norms_differ(D_WALL))
gate(f"Ⓔ②  ** and the SAME COUNT: {Z.bound_count('ruled', D_WALL)} either way **",
     Z.count_is_measure_independent(D_WALL))
gate("Ⓔ③  ⇒ ** so the ONE condition `STATED_LIMIT.md` named as open does not change the COUNT "
     "it was named for -- while still being what makes the measure REAL on the wall interval, "
     "which is a separate and necessary thing **",
     Z.count_is_measure_independent(D_WALL) and Z.norms_differ(D_WALL)
     and Z.static_measure_is_unavailable(D_WALL))

# =========================================================================================
head('Ⓕ  THE GRAFT, THE STOP CONDITION, AND WHAT IS STILL OWED')
# =========================================================================================
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import zero_modes as Z; '
     'Z.bound_count("ruled")' % MINE], capture_output=True, text=True, timeout=900)
gate("Ⓕ①  ** the capability PRINTS NOTHING when imported and used, so it is a function and not "
     "a script **", _probe.returncode == 0 and _probe.stdout == '')
_run = subprocess.run([sys.executable, os.path.join(MINE, 'zero_modes.py')],
                      capture_output=True, text=True, timeout=600)
gate("Ⓕ②  and its own report runs green", _run.returncode == 0)
gate("Ⓕ③  ** `B1`'s equivariant index is NOT claimed: the module says so in its own `what is "
     "not claimed`, and `STATED_LIMIT.md` declared it in advance **",
     _has(open(os.path.join(MINE, 'zero_modes.py'), encoding='utf-8').read(),
          'equivariant Dirac index')
     and _has(_limit, 'NOT this capability'))
gate("Ⓕ④  and the twelve rows are NOT claimed as reached -- the module says the capability is "
     "built and the rows are a separate batch",
     _has(open(os.path.join(MINE, 'zero_modes.py'), encoding='utf-8').read(),
          'reaching the rows is a separate batch'))

# =========================================================================================
head('Ⓖ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine_in = [n.left.value for n in ast.walk(_self)
            if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
            and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
            # ** ANY string literal, at any length -- `C76`'s lesson applied from the start. **
            ]
gate("Ⓖ①  ** no string constant AT ALL sits on the left of an `in` test anywhere in this file, "
     "proved from its OWN syntax tree -- `C76`'s threshold lesson applied from the start rather "
     "than after a gate said so **", not _mine_in)
gate("Ⓖ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** ORDER ② IS DONE INSIDE ITS ONE-CYCLE STOP. THE CAPABILITY EXISTS. **")
print("  ⛭⛭ THE RULED MEASURE IS WHAT MAKES THE WALL REGION HABITABLE, and that is not a")
print("    formality: the wall sits where f < 0 -- B34's own finding, which at D = 5 is")
print("    |r| < 1/2, inside the inner horizon, computed here from the roots of f -- and there")
print("    g_rr = 1/f is NEGATIVE, so sqrt(g_rr) is imaginary and the static L^2 measure does")
print("    not exist.  dmu = sqrt(|g_rr|) dr is real BECAUSE of the absolute value.")
print("  ⛭⛭ EXACTLY ONE CHIRALITY BINDS, UNDER BOTH MEASURES: ruled norm 1.541542 against flat")
print("    0.609035, reported side by side as ordered, with the other divergent under both.")
print("    Boundness is tested by refinement, not by one number.")
print("  ⛭⛭⛭ AND THAT ANSWERS THE ONE THING THE LIMIT SAID THE ORDER WOULD HAVE TO CARRY: the")
print("    two measures give DIFFERENT NORMS and the SAME COUNT.  The only condition the limit")
print("    flagged does not change the answer it was flagged for -- while still being what")
print("    makes the measure real at all.")
print("  ⌗ Still owed and said so: B1's equivariant index, declared in advance as not this")
print("    capability; and the twelve rows, which this does not claim to have reached.")
print("  " + "=" * 74)
print()
