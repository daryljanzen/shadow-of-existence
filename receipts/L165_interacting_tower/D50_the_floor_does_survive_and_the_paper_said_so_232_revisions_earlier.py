#!/usr/bin/env python3
"""
RECEIPT -- `PO-6` / `L-165`: ⛔⛔ ** `D3` (r2651) CONCLUDED THAT $\\hat\\Gamma$'s FLOOR DOES NOT SURVIVE
THE CUBIC.  P10 HAS SAID THE OPPOSITE SINCE r2419 -- IN ITS OWN VOICE, IN THE SAME PARAGRAPH `D3`
QUOTES, WITH A PASSING RECEIPT: *"the cubic term's apparent unboundedness is an artefact of
truncation"*.  ⛭⛭ *** THE FLOOR SURVIVES, AND r2652's SUB-THRESHOLD QUESTION IS BUILT ON THE
TRUNCATION. *** **

Built r2668+c54.209, lead `L-542`.  VEIN: `L-165` (PO-6, what a quantum of this geometry is).
** KIND: LATENT ** -- *nothing here is new physics; the answer was in the paper and reading found it.*

===================================================================================================
** ⓪ HOW THIS WAS REACHED, AND IT IS THE CORPUS'S OWN RULE **
===================================================================================================

r2632's rule: ** CHECK THE SENTENCE AFTER THE ONE YOU QUOTE. **  `D3` quotes P10:

    *"At leading order $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$; but the cubic and higher
     self-interactions enter at the same inverse-square order at the origin ($\\pi_n^2\\phi_m/a^3$ in
     kind)..."*

** and stops there. **  Reading on, in the SAME paragraph:

    *"...the first of which admits a verdict here, and it is AFFIRMATIVE.  The DeWitt form carries
     exactly one negative direction and it is the conformal one ... on transverse-traceless momenta
     that term drops and the form is $\\mathrm{tr}((g\\pi)^2)$ ... hence positive definite for every
     non-degenerate spatial metric.  **So the cubic term's apparent unboundedness is an artefact of
     truncation**: $\\pi^2(1-\\lambda\\phi+\\cdots)$ is the expansion of $\\pi^2/(1+\\lambda\\phi)$,
     whose full coefficient is positive wherever the metric is non-degenerate."*

===================================================================================================
** ⓵ AND THE TWO OBJECTS ARE THE SAME SERIES, ONE TRUNCATED **
===================================================================================================

  ** $\\pi^2/(1+\\lambda\\phi) = \\pi^2 - \\lambda\\phi\\pi^2 + \\lambda^2\\phi^2\\pi^2 - \\cdots$ **

  *`D3`'s "square times a signed field" is the SECOND TERM of that expansion, read alone.*
  ⇒ *** A truncation of a positive function is not a statement about the function.  The polynomial
      $c+g_3\\phi$ goes negative; the object it truncates never does. ***

  PART 2 samples both on the same points:
    · `D3`'s form,  $\\gamma+\\pi^2(c+g_3\\phi)$      -> ** large and negative ** (D3 reports $-209$)
    · the resummed, $\\gamma+\\pi^2/(1+\\lambda\\phi)$ -> ** bounded below by $\\gamma$ **

===================================================================================================
** ⛭⛭ ⓶ AND THAT DISSOLVES r2652's SUCCESSOR QUESTION RATHER THAN ANSWERING IT **
===================================================================================================

r2652 asked: *does the interacting dynamics keep $\\hat\\Gamma$ above $-1/4$, or does the
sub-$(-1/4)$ region carry support?*  -- because $\\nu=\\sqrt{\\hat\\Gamma+1/4}$ is real only there,
and `D3`'s operator reached $-47.8$.

  ⇒ ** On non-degenerate metrics $\\hat\\Gamma\\ge\\gamma$, and P10 carries $\\gamma\\le1/4$ with
     $\\nu=\\sqrt{\\gamma+\\tfrac14}$ real -- so $\\gamma\\ge-1/4$ and the sub-threshold region is
     EMPTY. **
  ⇒⇒ *** THE QUESTION HAS NO OBJECT.  It is not answered here; it does not arise. ***

===================================================================================================
** ⛔ WHAT SURVIVES OF r2651–r2652, AND IT IS NOT NOTHING **
===================================================================================================

** ⓵ `D3`'s arithmetic is correct about the truncation ** -- $c+g_3\\phi$ does change sign, and if the
cubic were the whole coefficient the floor would indeed go.  *What fails is the identification of the
truncation with the operator.*
** ⓶ r2652's threshold mathematics is correct ** -- $\\nu$ real iff $\\hat\\Gamma\\ge-1/4$, and an
oscillatory endpoint would indeed lose the canonical extension.  *What fails is its premise.*
** ⓷ AND P10's POSITIVITY IS SCOPED, WHICH r2652's WORRY CORRECTLY POINTS AT: ** *it speaks only of
the INTERIOR.*  ⇒ ** At the degenerate boundary $1+\\lambda\\phi\\to0$ the coefficient blows up rather
than going negative, and P10 says so: *"the positivity speaks only of the interior, the degenerate
boundary being what the thermal condition above is for."*  Two jobs, neither substituting. **

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not that `PO-6` closes. **  *P10 names what stays open in the same breath -- **the ultraviolet
definition of the tower sums** -- and this file does not touch it.*
** Not that the floor is proved for the full interacting theory ** -- what is established is that the
CUBIC does not destroy it, which is the thing `D3` claimed it did.
** Not a criticism of reading the truncation ** -- the paper hands the truncated form first and the
resolution four sentences later, which is exactly the shape r2632's rule was written for.
** And not that `D3`/`D4` should be deleted ** -- *they run and they are internally sound; what they
need is their premise re-based.*  ⌗ ***This file does not touch them, and it does not touch `PO-6`'s
`PROTECTED_OPEN` row: that row is 56's band and a protected row.  Routed, not edited.***

SETTINGS: none -- no instrument, no spectra.  A symbolic expansion, the two forms sampled on identical
points, the standing receipt re-run, and the revision dates read from git.

rc=0 on success.  Run: python3 D50_the_floor_does_survive_and_the_paper_said_so_232_revisions_earlier.py
                        (sympy, numpy; ~4 s)
"""
import os
import re
import subprocess
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO OBJECTS ARE ONE SERIES, AND D3 READ ITS SECOND TERM")
print("=" * 78)
lam, phi, pim = sp.symbols('lambda phi pi', real=True)
full = pim ** 2 / (1 + lam * phi)
ser = sp.expand(sp.series(full, phi, 0, 3).removeO())
print(f"  full coefficient        : {full}")
print(f"  expanded about phi = 0  : {ser}")
_cubic = -lam * phi * pim ** 2
_has = sp.simplify(ser.coeff(phi, 1) - _cubic.coeff(phi, 1)) == 0
print(f"  ** the -lambda*phi*pi^2 term D3 reads in isolation is present : {_has} **")
# checked TERMWISE rather than by asking for a closed-form resummation: the claim is that the
# paper's series IS this function's expansion, and that is a statement about coefficients.
_terms = sp.series(full / pim ** 2, phi, 0, 8).removeO()
_alt = [sp.simplify(_terms.coeff(phi, k) - (-lam) ** k) for k in range(8)]
_resum_ok = all(t == 0 for t in _alt)
print(f"  coefficients of phi^k in 1/(1+lambda*phi), k = 0..7 : "
      f"{[sp.simplify(_terms.coeff(phi, k)) for k in range(4)]} ...")
print(f"  ** each equals (-lambda)^k, termwise, to eighth order : {_resum_ok} **")
if not _has:
    fail.append("the cubic term is not the first-order term of pi^2/(1+lambda phi) — the identification fails")
if not _resum_ok:
    fail.append("the expansion coefficients are not (-lambda)^k — the two objects are not one series")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ⛭⛭ AND THE SAME POINTS, BOTH WAYS")
print("=" * 78)
rng = np.random.default_rng(0)
P = rng.uniform(-10, 10, 200_000)
F = rng.uniform(-10, 10, 200_000)
gamma, c, g3, l = 0.25, 1.0, 1.0, 1.0
trunc = gamma + P ** 2 * (c + g3 * F)
ok = 1 + l * F > 0                       # the non-degenerate region
resum = gamma + P[ok] ** 2 / (1 + l * F[ok])
print(f"  D3's truncated  gamma + pi^2 (c + g3 phi)      : min = {trunc.min():10.2f}   ** negative **")
print(f"  the resummed    gamma + pi^2 / (1 + lambda phi): min = {resum.min():10.4f}   ** = gamma **")
print(f"  points sampled : {len(P):,}   of which non-degenerate: {ok.sum():,}")
print()
print(f"  ⇒ the resummed coefficient never goes below gamma = {gamma}")
print(f"  ⇒ and the -1/4 threshold r2652 turns on is cleared: {resum.min():.4f} >= -0.25 -> "
      f"{bool(resum.min() >= -0.25)}")
print("  *** SO THE SUB-(-1/4) REGION IS EMPTY ON NON-DEGENERATE METRICS, AND r2652's QUESTION")
print("      HAS NO OBJECT RATHER THAN AN ANSWER. ***")
if trunc.min() >= 0:
    fail.append("the truncated form did not go negative — D3's own observation does not reproduce")
if resum.min() < gamma - 1e-9:
    fail.append(f"the resummed form dipped to {resum.min()} below gamma — P10's positivity fails")
if resum.min() < -0.25:
    fail.append("the resummed form reaches below -1/4 — r2652's region is NOT empty and this file is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — P10 SAYS THIS IN ITS OWN VOICE, AND HAS SINCE r2419")
print("=" * 78)
P10 = open(os.path.join(CORPUS, 'canonical_time.tex'), encoding='utf-8', errors='replace').read()
SAYS = [
    ("P10 calls the unboundedness an artefact of truncation",
     r"the cubic term's apparent unboundedness is an artefact of\s*\n?truncation"),
    ("⛭ and gives the resummation explicitly",
     r'\\pi\^\{2\}\(1-\\lambda\\phi\+\\cdots\)\$ is the expansion of \$\\pi\^\{2\}/\(1\+\\lambda\\phi\)'),
    ("and states the verdict on the spectrum as AFFIRMATIVE",
     r'the first of which admits a verdict here, and it is affirmative'),
    ("citing a receipt for it",
     r'\\rcpt\{P10_gamma_hat_is_bounded_below\}'),
    ("the positivity is scoped to the interior, with the boundary named",
     r'the positivity speaks only of the interior, the degenerate\s*\n?boundary being what the thermal condition above is for'),
    ("and gamma itself is bounded above by 1/4, so gamma >= -1/4 is P10's own regime",
     r'\\gamma\\le\\tfrac14'),
]
for what, pat in SAYS:
    ok_ = re.search(pat, P10, re.I | re.S) is not None
    print(f"  {'OK ' if ok_ else 'MISSING'}  {what}")
    if not ok_:
        fail.append(f"P10 does not carry: {what}")

print()
_blame = subprocess.run(['git', 'log', '--format=%h %ad', '--date=short', '-S',
                         'artefact of truncation', '--', 'corpus/canonical_time.tex'],
                        cwd=ROOT, capture_output=True, text=True).stdout.strip().split('\n')
_added = _blame[-1] if _blame and _blame[0] else '(unknown)'
print(f"  the clause entered at : {_added}")
print("  `D3` was written at   : r2651")
print("  *** 232 revisions apart, in the paragraph D3 quotes. ***")
if 'artefact' in subprocess.run(['git', 'show', 'c01f56c:corpus/canonical_time.tex'],
                                cwd=ROOT, capture_output=True, text=True).stdout:
    print("  ✔ verified by reading r2419's own copy of the file, not by trusting the log")
else:
    fail.append("r2419's copy of P10 does not contain the clause — the dating cannot be reproduced")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE STANDING RECEIPT STILL PASSES, RUN HERE")
print("=" * 78)
STAND = os.path.join(ROOT, 'receipts', 'P10_canonical_time', 'P10_gamma_hat_is_bounded_below.py')
_r = subprocess.run([sys.executable, os.path.basename(STAND)], cwd=os.path.dirname(STAND),
                    capture_output=True, text=True, timeout=180)
print(f"  P10_gamma_hat_is_bounded_below.py : rc = {_r.returncode}   "
      f"{'** PASSES **' if _r.returncode == 0 else '** FAILS **'}")
_line = [l for l in _r.stdout.split('\n') if 'truncated min' in l]
if _line:
    print(f"     {_line[0].strip()}")
print()
print("  ⇒ *So the corpus held a passing receipt for the affirmative verdict throughout, and")
print("     `D3` reached the negative one without it being cited against.*")
if _r.returncode != 0:
    fail.append("the standing bounded-below receipt no longer passes — the correction cannot rest on it")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the cubic term is the first-order term of pi^2/(1+lambda*phi); sampled on")
print("identical points the truncation goes far negative and the resummed coefficient never falls")
print("below gamma; P10 states the artefact, the resummation, the affirmative verdict and its scope")
print("in its own voice, and has since r2419; and the receipt it cites still passes.")
print("=" * 78)

# ============================================================================================
# GATE — r2668+c54.209, `L-542`.  ** This file contradicts another node's recent conclusion, so
# every pin is on the contradiction being the PAPER's and not this line's:
#   (1) the cubic term shown to BE the first-order term of the resummed coefficient -- ** if it were
#       not, the two objects would be different and D3 would be reading its own operator **;
#   (2) *** both forms sampled on IDENTICAL points ***, with D3's own observation reproduced (the
#       truncation does go negative) before the resummed one is shown not to.  ** A correction that
#       cannot reproduce what it corrects is an assertion **;
#   (3) *** the resummed minimum pinned at or above -1/4 ***.  ** This is the gate's centre: r2652's
#       whole successor question is whether the sub-(-1/4) region carries support, and if the
#       resummed form ever reached below it, this file would be the wrong one **;
#   (4) six source checks in P10, including the affirmative verdict and the SCOPE clause -- ** the
#       scope matters, because r2652's worry is right about the boundary and wrong about the
#       interior, and a correction that flattened that would be trading one error for another **;
#   (5) the clause's date read from r2419's OWN COPY of the file rather than from the log; and
#   (6) the standing receipt RE-RUN here.  ** The claim is that the corpus already held a passing
#       affirmative verdict; if it no longer passes, the claim changes. **
#   NOT gated: the ultraviolet definition of the tower sums.  ** P10 leaves it open in the same
#   sentence and nothing here touches it -- `PO-6` does not close. **
# ============================================================================================
assert _has, "the cubic term is not the expansion's first-order term"
assert _resum_ok, "the expansion is not the alternating geometric series"
assert trunc.min() < 0, "D3's truncated form did not reproduce as negative"
assert resum.min() >= gamma - 1e-9, "the resummed coefficient fell below gamma"
assert resum.min() >= -0.25, "THE RESUMMED FORM REACHES BELOW -1/4 — r2652's region is not empty"
for what, pat in SAYS:
    assert re.search(pat, P10, re.I | re.S), f"P10 does not carry: {what}"
assert _r.returncode == 0, "the standing bounded-below receipt no longer passes"
print(f"GATE c54.209 (r2668), `L-542`: the cubic is the first-order term of pi^2/(1+lambda*phi); on "
      f"{len(P):,} identical points the truncation reaches {trunc.min():.1f} and the resummed "
      f"coefficient never falls below gamma = {gamma}, clearing the -1/4 threshold r2652 turns on; "
      f"P10 states the artefact, the resummation and the affirmative verdict in its own voice, added "
      f"at {_added} against `D3`'s r2651; and `P10_gamma_hat_is_bounded_below` still passes — pinned "
      f"against r2632's own rule, check the sentence after the one you quote.")
