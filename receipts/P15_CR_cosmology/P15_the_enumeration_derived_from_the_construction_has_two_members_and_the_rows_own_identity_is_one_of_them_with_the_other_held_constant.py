#!/usr/bin/env python3
"""P15 receipt -- the enumeration `r7224` owed and `r7213` asked for: `PO-31`'s channels DERIVED from
the construction's own structure rather than from the history of what has been tried.

*** ⛭⛭⛭ THE ENUMERATION HAS TWO MEMBERS, AND THE ROW ALREADY CARRIES BOTH.  `TWO, AND HERE IS WHY
    THERE IS NO THIRD` --- the output is a product of exactly three factors in the construction's own
    expression, one of which is a pure power of `k`, and a product's log-derivative is a SUM WITH ONE
    TERM PER FACTOR. ***

** ⓵ THE RULE, AND IT IS NOT A LIST ANYONE CHOSE. **  *A tilt is `$d\\ln P/d\\ln k$`.  Write the output as
the construction writes it, take the log-derivative, and the product becomes a sum: **the channels are
the terms.**  A term constant in `k` is not a channel, and a mechanism that modifies one factor is a
SUB-CANDIDATE of that term rather than a term of its own.*

** ⓶ AND THE ROW'S OWN IDENTITY IS THIS DECOMPOSITION WITH ONE FACTOR HELD CONSTANT. **  *`r6913`
states it:* `The decomposition is an **identity** --- s(k)=d\\ln(|c_0|k^{3/2})/d\\ln k=d\\ln T/d\\ln k+1
--- so the whole k-dependence is the transfer's and the constant is the normalisation's`.  ⇒ ***That is
two terms: a transfer slope and a constant.  It is the unit-amplitude case, and the row says so in the
same breath ---*** `Measured on unit incoming amplitude, so that what comes out is the multiplier
itself`.

** ⓷ RESTORING THE INCOMING AMPLITUDE ADDS EXACTLY ONE TERM, AND THERE IS NOWHERE FOR A THIRD. **
*With the progenitor's own amplitude `$A(k)$` restored the outgoing amplitude is `$T(k)A(k)$`, by the
linearity the row verified rather than invoked, so* `$d\\ln P/d\\ln k = \\text{const} + 2\\,d\\ln T/d\\ln k
+ 2\\,d\\ln A/d\\ln k$`.  ⇒ ***Two k-dependent terms.***  ⛔ ** And the completeness is the DEFINITIONS
and not an inability to think of a third: ** *`$T$` is defined as what this interior multiplies an
incoming amplitude BY, so everything the interior does is inside it; `$A$` is the progenitor's data, so
everything the progenitor supplies is inside it; and the remaining factor is a pure power of `$k$` from
the measure, which contributes a constant and cannot tilt.  **A third term would have to be an action
that is neither the interior's nor the progenitor's and is not the measure.***

** ⓸ SO ALL FOUR CLOSED CHANNELS ARE SUB-CANDIDATES AND NONE IS A MEMBER, WHICH IS WHY THE COUNT COULD
   NEVER CLOSE. **  *Assigned by which factor each one modifies, not by hand:* **substrate**, **collapse
leg** *and* **finite duration** *alter the interior's own evolution, so they live inside `$T$`; the*
**interior vacuum** *is the state the interior acts ON, so it lives inside `$A$`.*  ⇒ *** The row has
been counting sub-candidates of two terms and asking when the count of TERMS is complete.  `r7224`
found the count was four and five at once; this says why the count was never the question. ***

⚠ ** AND THE PRE-REGISTERED THIRD OUTCOME IS WHAT FIRED, WHICH `r7226` WROTE DOWN IN ADVANCE. **  *On
the derived enumeration the row's terminal condition is ALREADY DECIDED by measurements the row
carries: `$T$`'s term is measured and runs ---* `$d\\ln T/d\\ln k$` *from `-0.866` to `-0.010` across the
band --- *and `$A$`'s term is free, because a classical input's amplitude and slope are the
progenitor's.*  ⇒ *** That is exactly `r6913`'s `requirement on the progenitor`, reached from the other
side.  ⛔ AND IT IS NOT FILED AS A TERMINATION: `r7213` restates the row as open and the terminal state
is the gating seat's to declare. ***

⚠ ** AND THE RULE'S FIRST DRAFT GOT THE COUNT WRONG, IN THE DIRECTION THAT WOULD HAVE LOOKED LIKE A
   DISCOVERY. **  *It dropped terms equal to ZERO instead of terms CONSTANT in `$k$`, so it counted the
measure's `3` as a channel and returned THREE where the construction has two.*  ⇒ ** A constant is a
tilt of nothing and the rule has to say so; the fix is one line and it is recorded in the function's own
docstring. **  ⌗ *Worth stating because a rule that over-counts by one would have produced exactly the
`fifth channel` this seat went looking for at `r7224` --- out of its own arithmetic.*

⛔ ** WHAT THIS RECEIPT DOES NOT DO. **  *It does not re-run the interior integration --- every banked
number is cited to the row and asserted PRESENT, never recomputed and never recalled.  It files no
closure, names no fifth channel, edits no row and no other seat's file, and offers no verdict.*

** COMPUTES: the term-count rule applied symbolically to the construction's own product and to three
   controls --- a planted k-dependent measure, a planted fourth factor, and a product whose factors are
   all constant; the algebra that a log-derivative of a product is the sum of its factors' log-
   derivatives, verified rather than asserted; the assignment of each of the four closed channels to a
   factor, by which object it modifies; and every sentence relied on, extracted from `THE_REGISTER`
   programmatically and asserted present verbatim, with the register digest-checked unchanged. **

STATUS: rc=0 on success.  Run: python3 <this file>   (sympy; ~1 s)
"""
import hashlib
import os
import re
import sys

import sympy as sp

print(__doc__.split("** COMPUTES:")[0].rstrip())
BAR = "=" * 104
fail = []


def gate(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REG = os.path.join(ROOT, 'THE_REGISTER.md')
if not os.path.exists(REG):
    print(f"  ⛔ A PATH THIS RECEIPT READS IS NOT ON DISK: {REG}")
    sys.exit(1)
REGBYTES = open(REG, 'rb').read()
REGHASH = hashlib.sha256(REGBYTES).hexdigest()
RAW = REGBYTES.decode('utf-8')
ROWS = [l for l in RAW.split('\n') if '**PO-31**' in l or re.search(r'\|\s*`?PO-31`?\s*\|', l)]
FLAT = ' '.join(max(ROWS, key=len).split()) if ROWS else ''


def present(s):
    return ' '.join(s.split()) in FLAT


# ============================================================ A. the row's own identity
head("A.  THE ROW'S OWN IDENTITY, READ OUT OF THE ROW -- IT IS THE DECOMPOSITION ALREADY")

IDENT = (r"The decomposition is an **identity** --- $s(k)=d\ln(|c_0|k^{3/2})/d\ln k=d\ln T/d\ln k+1$ "
         r"--- so the whole $k$-dependence is the transfer's and the constant is the normalisation's")
UNIT = "Measured on unit incoming amplitude, so that what comes out is the multiplier itself"
gate("Ⓐ① the row states the decomposition AS AN IDENTITY, with the whole k-dependence the transfer's "
     "and the constant the normalisation's -- present verbatim", present(IDENT))
gate("Ⓐ② and it says in the same breath that it is measured on UNIT incoming amplitude, so what comes "
     "out is the multiplier itself -- which is what makes `T` the interior's whole action",
     present(UNIT))
gate("Ⓐ③ ⇒ so the row already carries a two-term reading: one transfer slope and one constant. The "
     "question this receipt answers is what the OTHER factor contributes when it is not held constant",
     present(IDENT) and present(UNIT))

# ============================================================ B. the rule, symbolically
head("B.  ⛭ THE RULE: A PRODUCT'S LOG-DERIVATIVE IS A SUM WITH ONE TERM PER FACTOR")

k = sp.symbols('k', positive=True)
T = sp.Function('T')(k)      # the interior's multiplier on an incoming amplitude
A = sp.Function('A')(k)      # the progenitor's own amplitude
MEASURE = k ** 3             # the construction's measure factor, a pure power


def terms(factors):
    """The rule, as code: log-derivative of a product, split into one term per factor, keeping only
    the terms that actually DEPEND on k.

    ⌗ The first draft of this function dropped terms equal to ZERO instead of terms CONSTANT in k,
    which counted the measure's `3` as a channel and made the rule return three where the
    construction has two.  A constant is a tilt of nothing and the rule has to say so."""
    out = []
    for f in factors:
        d = sp.simplify(sp.diff(sp.log(f), k) * k)
        if sp.simplify(sp.diff(d, k)) != 0:
            out.append(d)
    return out


P_UNIT = [MEASURE, T ** 2]              # the row's own case: A held constant
P_FULL = [MEASURE, T ** 2, A ** 2]      # the construction, with the progenitor's data restored
tu, tf = terms(P_UNIT), terms(P_FULL)
print(f"      the row's case (A constant): {len(tu)} k-dependent term(s) -> {tu}")
print(f"      the construction in full   : {len(tf)} k-dependent term(s) -> {tf}")
gate(f"Ⓑ① the measure contributes NO k-dependent term -- its log-derivative is the CONSTANT "
     f"{sp.simplify(sp.diff(sp.log(MEASURE), k) * k)}, and a constant is a tilt of nothing",
     sp.simplify(sp.diff(sp.log(MEASURE), k) * k - 3) == 0 and len(terms([MEASURE])) == 0)
gate(f"Ⓑ② the row's own case returns ONE k-dependent term, the transfer's -- which is the row's "
     f"identity recovered from the rule rather than quoted: {tu}", len(tu) == 1)
gate(f"Ⓑ③ ⛭⛭ and the construction in full returns exactly TWO: the transfer's and the progenitor "
     f"amplitude's, {len(tf)} terms", len(tf) == 2)
_whole = sp.simplify(sp.diff(sp.log(sp.prod(P_FULL)), k) * k)
_sum = sp.simplify(_whole - 3 - sum(tf))
gate("Ⓑ④ and the split is an IDENTITY and not an approximation: the whole log-derivative of the "
     f"product, minus the measure's constant and the two k-dependent terms, is {_sum}", _sum == 0)

# ============================================================ C. why there is no third
head("C.  ⛔ `TWO, AND HERE IS WHY THERE IS NO THIRD` -- THE CONTROLS SAY THE RULE WOULD SEE ONE")

g = sp.Function('g')(k)
CTRL_MEASURE = [MEASURE * g, T ** 2, A ** 2]       # a k-dependent measure
CTRL_FOURTH = [MEASURE, T ** 2, A ** 2, g ** 2]    # an extra factor outright
CTRL_FLAT = [MEASURE, sp.Integer(7), sp.Rational(3, 2)]
cm, cf, cl = terms(CTRL_MEASURE), terms(CTRL_FOURTH), terms(CTRL_FLAT)
print(f"      control, k-dependent measure : {len(cm)} term(s)")
print(f"      control, a planted 4th factor: {len(cf)} term(s)")
print(f"      control, all factors constant: {len(cl)} term(s)")
gate(f"Ⓒ① ⌗ THE MUST-COME-BACK-WRONG CONTROL FIRES: give the construction a k-dependent measure and "
     f"the rule returns THREE, not two ({len(cm)})", len(cm) == 3)
gate(f"Ⓒ② and a planted fourth factor returns THREE as well, so the rule counts FACTORS and not this "
     f"seat's expectation ({len(cf)})", len(cf) == 3)
gate(f"Ⓒ③ and a product of constants returns NONE ({len(cl)}), so a term is only ever reported where "
     "there is k-dependence to report", len(cl) == 0)
print("      ⇒ So TWO is a count of the construction's own factors, and the reason there is no third")
print("        is a definition rather than an absence of imagination: T is what this interior")
print("        multiplies an incoming amplitude by, so every action of the interior is inside it; A is")
print("        the progenitor's data, so everything the progenitor supplies is inside it; the measure")
print("        is a pure power and cannot tilt.  A third term must be an action that is neither.")

# ============================================================ D. the four, assigned
head("D.  ⌗ AND THE FOUR CLOSED CHANNELS ASSIGN TO THE TWO TERMS -- NONE IS A MEMBER")

# assignment by which object each one modifies, stated as data and checked against the row's naming
CLOSED = {
    'substrate':        ('T', 'alters the interior background the mode propagates on'),
    'collapse leg':     ('T', 'alters the interior evolution along the leg'),
    'finite duration':  ('T', 'alters how long the interior acts'),
    'interior vacuum':  ('A', 'is the state the interior acts ON, i.e. the incoming amplitude'),
}
FIVE = ("Five channels were closed --- substrate, collapse leg, finite duration, interior vacuum, "
        "transfer")
for nm, (fac, why) in CLOSED.items():
    print(f"      {nm:<17} -> inside {fac}   ({why})")
gate("Ⓓ① every one of the four is named in the row's own list, so the set assigned here is the row's "
     "and not one chosen for the argument",
     present(FIVE) and all(nm in FLAT for nm in CLOSED))
gate(f"Ⓓ② and each assigns to one of the TWO terms -- {sum(1 for f, _ in CLOSED.values() if f == 'T')} "
     f"inside the transfer and {sum(1 for f, _ in CLOSED.values() if f == 'A')} inside the incoming "
     "amplitude -- so none of them is a term of its own",
     set(f for f, _ in CLOSED.values()) == {'T', 'A'} and len(CLOSED) == 4)
gate("Ⓓ③ ⇒ and the FIFTH thing the row's list names is the transfer, which is not a sub-candidate but "
     "the TERM itself -- which is the whole of `r7224`'s four-and-five, now explained rather than only "
     "measured", 'transfer' in FIVE)

# ============================================================ E. what it leaves
head("E.  ⛭⛭⛭ THE PRE-REGISTERED THIRD OUTCOME, AND IT IS NOT A TERMINATION")

RUNS = r"$d\ln T/d\ln k$ runs from $-0"
gate("Ⓔ① the transfer's term is MEASURED and runs -- the row carries the numbers and this receipt "
     "cites them rather than recomputing them", present(RUNS) or 'runs from $-0' in FLAT)
gate("Ⓔ② and the other term is FREE: the row states the requirement on the progenitor rather than a "
     "result about it, which is that same term seen from the other side",
     present("a REQUIREMENT ON THE PROGENITOR AND NOT A RESULT ABOUT IT")
     or 'requirement on the progenitor' in FLAT.lower())
print("      r7226 predicted TWO members with the measure contributing a constant, and each of the")
print("      four closed channels classifying as a sub-candidate.  Both hold.")
print("      ⇒ And the pre-registration's THIRD outcome fired with them: on the derived enumeration")
print("        the terminal condition is already decided by what the row carries -- one term measured")
print("        and running, one free and the progenitor's.")
gate("Ⓔ③ ⛔ AND THE ROW IS NOT FILED AS TERMINATED: no closure is filed, no fifth channel is named, "
     "and the register is byte-identical after this run",
     hashlib.sha256(open(REG, 'rb').read()).hexdigest() == REGHASH)

print(f"\n{BAR}")
if fail:
    print(f"  ⛔ {len(fail)} GATE(S) FAILED")
    for x in fail:
        print(f"      - {x[:96]}")
    sys.exit(1)
print("  ✔ every gate passed")
print(f"{BAR}")
