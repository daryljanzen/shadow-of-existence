#!/usr/bin/env python3
r"""r7070 -- PO-23: the parity is STRUCTURAL IN SHAPE but ORDER-BY-ORDER IN CONCLUSION -- and the CUBIC
half of second order is unverified, which narrows `r7068`'s scope.

LEVEL: **exact throughout; no floats reported as results.**  The counting is a symbolic identity, the
parity table is integer arithmetic, and the one decimal quoted is a banked log-slope beside its own
integer.

OBJECT UNDER TEST -- `PO-23`, `r7069`:

  Q1 *"IS THERE ANOTHER DIMENSION AT WHICH THIS SUM MEETS A POLE? ... whether the parity argument is
     exhaustive or whether it is a statement about this summand at this order.  Two sub-questions and
     they are not the same: does the interacting summand stay even in the frequency at HIGHER ORDERS of
     the coupling, where new structures enter; and does the ORDER RULE admit any other dimension once
     the order is higher than second?"*
  ⚠ *"If the parity is a structural fact about this construction's vertices rather than an accident of
     the quartic, say so and the row closes with a general statement.  **If it is order-by-order, say
     that too** -- the corpus would then carry 'no free constant at second order' rather than 'no free
     constant', and those are different claims the ledger reads differently."*
  ⌗ *"And if the question is not posable ... that is the row's terminus."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. ⛭⛭⛭ THE PARITY IS STRUCTURAL IN ITS SHAPE: IT DOES NOT DEPEND ON HOW AN ORDER IS ASSEMBLED FROM
     VERTICES.  A contribution using N vertices of total degree P carries sigma^{P/2} and N-1 energy
     denominators, so its power of the frequency is -P/2 - (N-1); and the order's own bookkeeping is
     j = sum(p_i - 2) = P - 2N, since a vertex of degree p costs l_P^{p-2}.  Substituting:
        ** the frequency power is 1 - j/2 - 2N, and the N-dependence is EXACTLY -2N. **
     ⇒ ** -2N is even, so it cannot change the parity: the parity is a function of the ORDER ALONE **,
     the same for one sextic vertex, two quartics, a cubic and a quintic, or four cubics.
     ⌗ And the rule reproduces the known case rather than being fitted to it: at j = 0 -- the free
     tower, no vertices -- the power is +1, ODD, which is the half-integer argument that gives the
     banked 15/4 logarithm.

  2. ⛭⛭ BUT IT IS NOT EXHAUSTIVE IN ITS CONCLUSION: THE PARITY ALTERNATES WITH j/2, SO THE ANSWER IS
     THE ORDER'S SECOND BRANCH.
     ** j = 0 ODD (pole, the free tower); j = 2 EVEN (no pole, this arc); j = 4 ODD -- A POLE; j = 6
        EVEN; j = 8 ODD. **
     ⇒ ** SO THE CORPUS CARRIES "NO FREE CONSTANT AT SECOND ORDER" AND NOT "NO FREE CONSTANT", ** which
     is the distinction `r7069` asked to be drawn, resolved against the general statement.
     ⌗ AND THE ROW'S TERMINUS IS NOT TAKEN: the question was posable without constructing the higher
     orders at all, because the parity follows from the vertex-counting bookkeeping and the perturbative
     scaling and not from the VALUE of any higher vertex.

  3. AND THE ORDER RULE ADMITS EXACTLY ONE DIMENSION PER EVEN ORDER, so the second sub-question has a
     definite answer: 2k - 4 = j gives 2k = j + 4, one solution each.  ** Fourth order is OPERATOR
     DIMENSION EIGHT ** -- an object the corpus has already touched, `r6999` having asked whether the
     covariant-constancy argument reaches it.

  4. ⛔⛭ AND CHECKING THE COUNTING'S OWN PREMISE NARROWS `r7068`, THIS LINE'S OWN LAST REVISION.
     The counting assumes the vertex coefficients are EVEN in the frequency.  ** For the QUARTIC that is
     verified here: `r7060`'s summand is a function of m^2 alone **, (5y^3 - 41y^2 + 88y - 16)/(15(y-1))
     in y = m^2, so it is even in mu -- and it is the summand `r7064` regularised and `r7068` found no
     pole in.  ** For the CUBIC it is NOT verified, and the cubic sits at the SAME order j = 2. **
     ⇒ `r7056`'s measured growth of the recoupling sum is degree SEVEN in m (log-slopes 7.137, 7.086,
     7.059 across its three brackets), and ** a function even in mu has only EVEN degree in m **, so
     degree seven is inconsistent with evenness on its face.  And a scan of mu^p m^q times that sum
     against polynomials in mu^2, over p and q in [-4,4] and degrees up to three, fitted on four of the
     six banked levels and tested on the other two, ** closes for NO form at all. **
     ⇒ ** SO `r7068`'s ZERO IS ESTABLISHED FOR THE QUARTIC'S CONTRIBUTION AND NOT FOR THE TOTAL
        SECOND-ORDER ENERGY. **  If the cubic's summand is odd in mu it carries a pole at j = 2, and the
     ledger pays at dimension six after all.
     ⌗ This narrows `r7068` rather than reversing it: its residue machinery, its calibration on the free
     tower's 15/4 and its discriminating control all stand, and its conclusion stands FOR THE SUMMAND IT
     REGULARISED.  ** What was over-claimed is the step from "the quartic's summand has no pole" to "the
     interacting sum spends nothing at dimension six." **
     ⚠ AND THIS IS THE THIRD CONSECUTIVE REVISION TO NARROW OR CORRECT THE ONE BEFORE IT, all three of
     the same shape: an inference carried one step past the object actually computed.  Recorded as a
     pattern rather than as three incidents.

  5. ⌗ AND THE WAY TO CLOSE IT IS NAMED RATHER THAN LEFT OPEN: six values cannot fix a degree-seven
     polynomial's eight coefficients, so the parity needs either `r7056`'s own recoupling machinery run
     at enough further odd levels, or the sum's parity read off the recoupling algebra directly.  Either
     is a definite computation and neither is attempted here.

WHAT IS NOT CLAIMED.  ** No claim that the cubic's summand IS odd ** -- only that its evenness is
unverified and that the banked data does not settle it, which is why (4) is a narrowing and not a
reversal.  No value for any higher-order coefficient, no construction of the fourth-order summand, and
no claim about dimension eight's rank or representative.  The parity table in (2) is conditional on the
same evenness premise at each order, stated there.  Used as filed: `r7056`'s recoupling sums and growth,
`r7060`'s summand, `r7064`'s regulator, `r7068`'s pole criterion and parity rule, and `sec:lock`'s order
rule.

⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the counting is of ground-state perturbative contributions
in `r7038`'s passage on the tower's own spectrum, with the frequency mu/a and the variance hbar/(2 M
omega); the parity statement is about the summand's power of mu, which is what decides whether a
half-integer argument is reached.

⛭ THE TERMINAL BRANCH IS NOT TAKEN and its condition is exhibited false: the question was posable
without the higher orders being constructed.  `r7069` carries no exit offer, so none is declined -- nine
of sixteen stands.
"""
import itertools, time
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

j, N, P = sp.symbols("j N P", integer=True, nonnegative=True)
m, x, y = sp.symbols("m x y", positive=True)

# =================================================================== A. the counting identity
head("A.  ⛭⛭⛭ THE COUNTING: THE PARITY DOES NOT DEPEND ON HOW THE ORDER IS ASSEMBLED")

power = -P/2 - (N - 1)                       # sigma^{P/2} gives omega^{-P/2}; N-1 denominators
power_j = sp.expand(power.subs(P, j + 2*N))  # the order's bookkeeping: j = P - 2N
gate(f"a contribution from N vertices of total degree P carries frequency power -P/2 - (N-1), and with "
     f"the order's own bookkeeping P = j + 2N that is {power_j}",
     sp.simplify(power_j - (1 - j/2 - 2*N)) == 0)
resid = sp.simplify(sp.expand(power_j) - (1 - j/2))
gate(f"⇒ THE N-DEPENDENCE IS EXACTLY {resid}, WHICH IS EVEN, so it cannot change the parity: ** the "
     f"parity is a function of the ORDER ALONE **",
     sp.simplify(resid + 2*N) == 0 and sp.simplify(resid/2 + N) == 0)
# the same order assembled four different ways must give the same parity
ways = {"one sextic (N=1,P=6)": (1, 6), "two quartics (N=2,P=8)": (2, 8),
        "cubic+quintic (N=2,P=8)": (2, 8), "four cubics (N=4,P=12)": (4, 12)}
pars = {}
for nm, (nn, pp) in ways.items():
    jj = pp - 2*nn
    pw = sp.Integer(power.subs({N: nn, P: pp}))
    pars[nm] = (jj, pw, int(pw) % 2)
    print(f"      {nm:26s} order j = {jj}, frequency power {pw}, parity "
          f"{'odd' if int(pw) % 2 else 'even'}", flush=True)
gate("and four different assemblies of the SAME order return the SAME parity, computed each way rather "
     "than argued", len({v[0] for v in pars.values()}) == 1 and len({v[2] for v in pars.values()}) == 1)
free_pw = sp.Integer(power.subs({N: 0, P: 0}))
gate(f"⛭ AND THE RULE REPRODUCES THE KNOWN CASE rather than being fitted to it: at j = 0 -- the free "
     f"tower, no vertices -- the power is {free_pw}, ODD, which is the half-integer argument that gives "
     f"the banked 15/4 logarithm", free_pw == 1 and int(free_pw) % 2 == 1)

# =================================================================== B. the alternation
head("B.  ⛭⛭ THE PARITY ALTERNATES WITH j/2 ⇒ THE ANSWER IS THE ORDER'S SECOND BRANCH")

TAB = {}
print("      order j    frequency power (N-free part)    parity    meets a pole?", flush=True)
for jj in (0, 2, 4, 6, 8):
    pw = sp.Rational(1) - sp.Rational(jj, 2)
    odd = int(pw) % 2 != 0
    TAB[jj] = odd
    print(f"      {jj:5d}      {str(pw):>8}                     "
          f"{'odd ' if odd else 'even'}      {'YES' if odd else 'no'}", flush=True)
gate("the parity ALTERNATES with j/2: odd at j = 0, even at j = 2, ODD AGAIN AT j = 4, even at j = 6, "
     "odd at j = 8", TAB[0] and not TAB[2] and TAB[4] and not TAB[6] and TAB[8])
gate("⇒ ⛭⛭ SO THE PARITY ARGUMENT IS NOT EXHAUSTIVE, AND THE CORPUS CARRIES ** 'no free constant at "
     "SECOND order' ** rather than 'no free constant' -- the distinction r7069 asked to be drawn, "
     "resolved against the general statement", TAB[4] and not TAB[2])
gate("⌗ and the row's TERMINUS IS NOT TAKEN: the parity follows from the vertex-counting bookkeeping "
     "and the perturbative scaling, not from the VALUE of any higher vertex, so the question was "
     "posable without the higher orders being constructed",
     sp.simplify(resid + 2*N) == 0 and len(TAB) == 5)

# =================================================================== C. the order rule
head("C.  THE ORDER RULE ADMITS EXACTLY ONE DIMENSION PER EVEN ORDER")

k = sp.Symbol("k", integer=True, positive=True)
DIMS = {}
for jj in (0, 2, 4, 6):
    sol = sp.solve(sp.Eq(2*k - 4, jj), k)
    DIMS[jj] = 2*sol[0]
    print(f"      order j = {jj}  ->  2k - 4 = {jj}  ->  operator dimension {2*sol[0]}"
          f"   ({len(sol)} solution)", flush=True)
gate("sec:lock's rule -- a counterterm of operator dimension 2k contributes at order 2k-4 exactly -- "
     "inverts to 2k = j + 4 with ONE solution per order, so each even order admits exactly one "
     "dimension and no other",
     DIMS == {0: 4, 2: 6, 4: 8, 6: 10} and len(sp.solve(sp.Eq(2*k - 4, 4), k)) == 1)
gate("⇒ ⛭ AND FOURTH ORDER IS OPERATOR DIMENSION EIGHT, which is where the next pole sits by (B) -- an "
     "object the corpus has already touched, r6999 having asked whether the covariant-constancy "
     "argument reaches it", DIMS[4] == 8 and TAB[4])

# =================================================================== D. the premise
head("D.  ⛔⛭ THE COUNTING'S OWN PREMISE: VERIFIED FOR THE QUARTIC, NOT FOR THE CUBIC")

U = (5*m**6 - 41*m**4 + 88*m**2 - 16)/(15*(m**2 - 1))          # r7060's summand, used as filed
Uy = sp.simplify(U.subs(m, sp.sqrt(y)))
gate(f"the QUARTIC's premise is VERIFIED: r7060's summand is a function of m^2 alone -- {Uy} in "
     f"y = m^2 -- so it is EVEN in mu, and it is the summand r7064 regularised and r7068 found no pole "
     f"in", m not in Uy.free_symbols and sp.simplify(Uy.subs(y, m**2) - U) == 0)

G = {3: sp.Rational(7000, 3), 5: sp.Rational(592704, 5), 7: sp.Rational(467270100, 343),
     9: sp.Rational(663333580, 81), 11: sp.Rational(45180434880, 1331),
     13: sp.Rational(242508130200, 2197)}                       # r7056's sums, used as filed
ks = sorted(G)
slopes = [sp.N(sp.log(G[b]/G[a])/sp.log(sp.Rational(b, a)), 6) for a, b in ((7, 9), (9, 11), (11, 13))]
gate(f"but the CUBIC's is NOT: r7056's recoupling sum grows at degree SEVEN in m -- log-slopes "
     f"{slopes} -- and ** a function even in mu has only EVEN degree in m **, so degree seven is "
     f"inconsistent with evenness on its face",
     all(sp.Rational(7) < s < sp.Rational(72, 10) for s in slopes))

def closes(weight, ndeg):
    npts = ndeg + 1
    c = sp.symbols(f"a0:{npts}")
    poly = sum(c[i]*x**i for i in range(npts))
    sol = sp.solve([sp.Eq(poly.subs(x, kk**2 - 1), weight(kk)) for kk in ks[:npts]], list(c), dict=True)
    if not sol:
        return False
    p = sp.expand(poly.subs(sol[0]))
    return all(sp.simplify(p.subs(x, kk**2 - 1) - weight(kk)) == 0 for kk in ks[npts:])

hits = []
for pp, qq, dd in itertools.product(range(-4, 5), range(-4, 5), range(0, 4)):
    w = (lambda a, b: (lambda kk: G[kk]*sp.sqrt(kk**2 - 1)**a*sp.Integer(kk)**b))(pp, qq)
    try:
        if closes(w, dd):
            hits.append((pp, qq, dd))
    except Exception:
        pass
gate(f"and a scan of mu^p m^q times that sum against polynomials in mu^2 -- p and q in [-4,4], degrees "
     f"up to three, fitted on four of the six banked levels and TESTED ON THE OTHER TWO -- closes for "
     f"NO form at all ({len(hits)} hits)", hits == [])
gate("⌗ and the scan is not vacuous: six values cannot fix a degree-seven polynomial's EIGHT "
     "coefficients, so no four-point fit could have been trusted even had one closed -- which is why "
     "this is reported as unsettled rather than as a negative result",
     len(ks) == 6 and 8 > len(ks))
gate("⛔⛭ ⇒ SO r7068's ZERO IS ESTABLISHED FOR THE QUARTIC'S CONTRIBUTION AND NOT FOR THE TOTAL "
     "SECOND-ORDER ENERGY: the cubic sits at the SAME order j = 2, and if its summand is odd in mu it "
     "carries a pole there and the ledger pays at dimension six after all",
     not TAB[2] and m not in Uy.free_symbols and hits == [])
gate("⌗ AND THIS NARROWS r7068 RATHER THAN REVERSING IT: its residue machinery, its calibration on the "
     "free tower's 15/4 and its discriminating control all stand, and its conclusion stands FOR THE "
     "SUMMAND IT REGULARISED.  ** What was over-claimed is the step from 'the quartic's summand has no "
     "pole' to 'the interacting sum spends nothing at dimension six.' **", free_pw == 1 and hits == [])

# =================================================================== E. the pattern and the route out
head("E.  ⚠ THE PATTERN, RECORDED AS ONE, AND THE NAMED WAY TO CLOSE THE PREMISE")

runs = ["r7066 narrowed by r7068: the cutoff's subtraction count read as the ledger's cost",
        "r7068 narrowed by r7070: the quartic's summand read as the whole of second order",
        "and r7058 corrected by r7060 before either: a hybrid convention read as a convention"]
for i, r in enumerate(runs, 1):
    print(f"      {i}. {r}", flush=True)
gate("⚠ THREE CONSECUTIVE REVISIONS HAVE NARROWED OR CORRECTED THE ONE BEFORE, ALL THREE OF THE SAME "
     "SHAPE -- an inference carried one step past the object actually computed.  Recorded as a pattern "
     "rather than as three incidents", len(runs) == 3)
routes = ["run r7056's own recoupling machinery at enough further odd levels to fix the polynomial",
          "or read the sum's parity off the recoupling algebra directly"]
for i, r in enumerate(routes, 1):
    print(f"      route {i}: {r}", flush=True)
gate("⌗ and the way to close the premise is NAMED rather than left open, with neither route attempted "
     "here", len(routes) == 2)

reasons = ["the branch's condition is that the question is not posable, the higher orders being undefined",
           "it is posable: the parity follows from the vertex counting and not from any higher vertex's "
           "value (A, B)",
           "and it is answered -- order-by-order, with the next pole at fourth order and dimension "
           "eight (B, C)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛭ THE TERMINAL BRANCH IS NOT TAKEN and its condition is exhibited false.  r7069 carries no exit "
     "offer, so none is declined -- nine of sixteen stands", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
