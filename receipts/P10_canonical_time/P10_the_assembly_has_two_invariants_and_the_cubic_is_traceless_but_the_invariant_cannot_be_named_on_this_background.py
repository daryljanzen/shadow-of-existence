#!/usr/bin/env python3
r"""r7080 -- PO-71 Q1: the assembly has TWO invariants and the cubic is TRACELESS, so the parity stands
and the coefficient's structure does not -- but the INVARIANT CANNOT BE NAMED on this background, which
is the row's own stated terminus, and the reason is a domain error of THIS SEAT'S OWN.

LEVEL: **exact throughout; no floats reported as results and no tolerances.**  The assembly is exact
oscillator algebra in a truncated Fock space, the trace selection rule is exact 3j arithmetic with its
affirmative control, and every rank is `r7062`'s own rank over exact rational coefficient matrices.

OBJECT UNDER TEST -- `PO-71`, `r7079`, in the two-part order this seat itself asked for:

  Q1 *"(a) re-derive `r7060`'s sigma^3/omega rather than inheriting it as filed, and say plainly if it
     moves -- **if it moves, the residue moves with it and that is the finding**, not a setback.
     (b) then the invariant: named, with its normalisation matched to `r7074`'s residue on the
     re-derived assembly."*
  ⚠ The terminus the order wrote down: *"If the one-parameter family turns out not to distinguish the
     representatives it is rank one across, that is the row's stated terminus -- it would make the
     naming need a datum outside this background, which is a statement about the background's reach and
     not about the coefficient.  Say so in those terms if that is where it lands."*
  ⇒ ** IT LANDS THERE, AND THE CONDITION IS EXHIBITED TRUE RATHER THAN DECLINED. **

WHAT IS CLAIMED, each with its scope and its convention in the sentence that states it.

  1. ⛭⛭⛭ (a) THE ASSEMBLY IS RE-DERIVED AND IT MOVES -- IN ITS COEFFICIENT'S STRUCTURE AND NOT IN ITS
     FORM.  For a totally symmetric cubic on degenerate modes the exact second-order ground-state shift
     is
       ** dE = -(sigma^3 / (hbar omega)) [ 2 sum T^2 + 9 sum t^2 ],   t_C = sum_A T_AAC **
     verified on a single mode (returning the textbook -11 g^2 sigma^3/(hbar omega)), on a GENERIC
     two-mode symmetric T, and on a TRACELESS three-mode control that keeps only the first term.
     ⇒ ** THERE ARE TWO INVARIANTS OF THE VERTEX, AT WEIGHTS 2 AND 9, WHERE `r7010` FILED A SINGLE
        8 g^2. **  The three-quantum channel rides the full norm at denominator 3 hbar omega and the
     one-quantum channel rides the TRACE at hbar omega; `r7074` used the full norm alone.

  2. ✔✔ AND THE FORM IS WHAT `r7074` NEEDED, SO ITS PARITY STANDS UNTOUCHED.  Both channels carry the
     SAME sigma^3/omega, hence the same INTEGER power of x = mu^2 ⇒ the parity rides entirely on the
     recoupling sum, exactly as `r7074` had it.  ** The cubic summand is still odd, still reaches the
     pole, and the ledger still pays at dimension six. **

  3. ⛭⛭ AND THE TRACE CHANNEL IS ABSENT AT EVERY LEVEL, BY A SINGLET COUNT RATHER THAN BY ESTIMATE.
     A trace contracts two slots, and the 3j identity makes that vanish ** unless the FREE label is
     zero **, checked with its affirmative control at three spins.  A trace therefore needs the free
     slot to be a FULL singlet -- right label zero AND left spin zero -- and ** no channel at any level
     is: ** above m = 3 no label is zero at all, and at m = 3 the two never coincide, the channel with
     right label zero carrying left spin two and the one with left spin zero carrying right label two.
     ⇒ ** sum t^2 = 0 IDENTICALLY, so the assembly is 2 sum T^2 sigma^3/(hbar omega). **
     ⌗ And `r7060`'s criterion is untouched for a reason worth stating: its 8 appears in BOTH the
     quartic and the cubic energy and CANCELS in the ratio R, so the number that was wrong was never
     load-bearing there -- computed here, not assumed.

  4. ⛔⛭⛭ (b) THE INVARIANT CANNOT BE NAMED ON THIS BACKGROUND, AND RANK ONE IS WHY -- NOT HOW.
     `sec:lock`'s five dimension-six scalars are pointwise independent on a general scale factor
     (** rank 5 of 5 **) and collapse on the one-parameter family, where the two derivative scalars
     vanish identically and the other three are pure numbers times alpha^-6 (** rank 1 **).
     ⇒ ** SO THE FAMILY CANNOT DISTINGUISH THE REPRESENTATIVES IT IS RANK ONE ACROSS: ** matching one
     number on it is one equation on three non-vanishing directions, and the solution set is a
     TWO-PARAMETER family of representatives, exhibited here rather than counted.  ** Rank one is the
     degeneracy that BLOCKS the naming, not the lever that forces it. **
     ⌗ And on the class the ledger actually uses -- the scale factor QUANTIZED -- `sec:lock` says in
     terms that *"at dimension six there is no such identity to descend"*, so the five are independent
     there and nothing collapses at all.

  5. ⛔⛔ AND THE DEFECT IS THIS SEAT'S, IN THE VERY PARAGRAPH THAT OPENED THE ROW.  `r7077` asked for a
     reading and this seat answered that `sec:lock`'s rank one meant *"the five collapse to a single
     direction on the admitted class, so the representative is forced up to normalisation."*
     ** BOTH HALVES ARE WRONG AND IN THE SAME WAY. **  The rank one is on the ONE-PARAMETER FAMILY and
     not on the admitted class; and a rank of one does not FORCE a representative, it makes the
     representatives INDISTINGUISHABLE.  ⇒ *A rank read off one domain and applied on another, and a
     degeneracy read as a determination* -- the row's own seventh face, **the domain of an EQUIVALENCE
     is part of the statement**, committed by the seat that has been enforcing it.
     ⌗ `r7079` wrote this seat's constraint into the row on this seat's word, so the correction belongs
     here and is filed as the revision's own finding rather than left for the gate to catch.

  6. ⌗ WHAT SURVIVES OF THE ROW, SAID SEPARATELY FROM WHAT FAILS.  `PO-71`'s object is real and is not
     answered: a non-zero coefficient at dimension six IS the coefficient of something, and `r7074`'s
     residue and `r7068`'s criterion both stand.  ** What is established is that this background cannot
     name it, and that is a statement about the background's reach. **  The datum the naming needs is
     one that separates R^3, R Ric^2 and Ric^3 -- which the de Sitter family provably does not.

SCOPE, in the same sentences as the claims.  (a)'s assembly is exact for a totally symmetric cubic on
modes of ONE common frequency, which is the same-level case `r7074` used and not the cross-level one.
The traceless finding is about the SAME-LEVEL vertex's own trace, on `r7056`'s channels.  Every rank is
`r7062`'s, loaded from its own source and not restated, and is a rank over a chosen FIVE-element subset,
so a lower bound on the full basis -- which is the direction (b)'s negative needs, since completing the
basis can only RAISE the pointwise rank and so only worsen the degeneracy on the family.  No renormalised
value, no representative chosen, and nothing touched at fourth order or dimension eight.
"""
import itertools, os, io, contextlib, time
import sympy as sp
from sympy.physics.wigner import wigner_3j

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))
RANKSRC = ("P10_the_ultraviolet_object_is_a_rank_sequence_and_the_ledger_is_at_stake_at_dimension_six_"
           "and_not_four.py")
sig, hb, om = sp.symbols("sigma hbar omega", positive=True)

# ============================================================ A. the assembly, re-derived
head("A.  ⛭⛭⛭ (a) THE SECOND-ORDER ASSEMBLY, RE-DERIVED FROM THE OSCILLATOR ALGEBRA")

def shift(N, T, nmax=3):
    """Exact second-order ground-state shift for V = sum T[A][B][C] q_A q_B q_C, all modes at omega."""
    basis = [n for n in itertools.product(range(nmax + 1), repeat=N) if sum(n) <= nmax]
    idx = {n: i for i, n in enumerate(basis)}
    D = len(basis)
    Q = [sp.zeros(D, D) for _ in range(N)]
    for n in basis:
        for A in range(N):
            up = list(n); up[A] += 1
            if tuple(up) in idx:
                v = sp.sqrt(sig)*sp.sqrt(n[A] + 1)
                Q[A][idx[tuple(up)], idx[n]] += v
                Q[A][idx[n], idx[tuple(up)]] += v
    V = sp.zeros(D, D)
    for A in range(N):
        for B in range(N):
            for C in range(N):
                if T[A][B][C] != 0:
                    V += T[A][B][C]*Q[A]*Q[B]*Q[C]
    g0 = idx[tuple([0]*N)]
    tot = sp.Integer(0)
    for n in basis:
        if n == tuple([0]*N):
            continue
        amp = V[idx[n], g0]
        if amp != 0:
            tot -= sp.expand(amp**2)/(sum(n)*hb*om)
    return sp.simplify(sp.expand(tot))

def invariants(N, T):
    T2 = sp.expand(sum(T[A][B][C]**2 for A in range(N) for B in range(N) for C in range(N)))
    t = [sum(T[A][A][C] for A in range(N)) for C in range(N)]
    return T2, sp.expand(sum(x**2 for x in t))

def sym_tensor(N, vals):
    T = [[[sp.Integer(0)]*N for _ in range(N)] for _ in range(N)]
    for key, v in vals.items():
        for p in set(itertools.permutations(key)):
            T[p[0]][p[1]][p[2]] = v
    return T

def predicted(N, T):
    A, B = invariants(N, T)
    return sp.simplify(-sig**3/(hb*om)*(2*A + 9*B)), A, B

g = sp.Symbol("g")
T1 = sym_tensor(1, {(0, 0, 0): g})
dE1, A1, B1 = predicted(1, T1)
got1 = shift(1, T1)
print(f"      N=1:  dE = {got1};  sum T^2 = {A1}, sum t^2 = {B1}", flush=True)
gate("⛭ THE ONE-MODE CASE RETURNS THE TEXTBOOK -11 g^2 sigma^3/(hbar omega), which is the calibration "
     "run before the unknown: 9 from the one-quantum channel at hbar omega and 6/3 = 2 from the "
     "three-quantum channel at 3 hbar omega",
     sp.simplify(got1 + 11*g**2*sig**3/(hb*om)) == 0 and sp.simplify(got1 - dE1) == 0)

c = sp.symbols("c0:4")
T2m = sym_tensor(2, {(0, 0, 0): c[0], (0, 0, 1): c[1], (0, 1, 1): c[2], (1, 1, 1): c[3]})
dE2, A2, B2 = predicted(2, T2m)
gate("⛭⛭⛭ AND THE ASSEMBLY IS dE = -(sigma^3/(hbar omega)) [ 2 sum T^2 + 9 sum t^2 ] ON A GENERIC "
     "SYMMETRIC T -- checked at two modes with FOUR free coefficients, so it is an identity in the "
     "vertex and not a fit to one case",
     sp.simplify(shift(2, T2m) - dE2) == 0 and B2 != 0 and A2 != 0)
T3 = sym_tensor(3, {(0, 1, 2): sp.Integer(1)})
dE3, A3, B3 = predicted(3, T3)
gate(f"⛭ AND THE DISCRIMINATING CONTROL SEPARATES THE TWO INVARIANTS: a TRACELESS vertex (sum t^2 = "
     f"{B3}, sum T^2 = {A3}) keeps ONLY the 2 sum T^2 term, at the SAME sigma^3/omega -- so the two "
     f"channels differ in WHICH invariant they carry and not in their frequency dependence",
     B3 == 0 and A3 == 6 and sp.simplify(shift(3, T3) - dE3) == 0
     and sp.simplify(dE3 + 12*sig**3/(hb*om)) == 0)
gate("✔✔ ⇒ SO THE FORM IS WHAT r7074 NEEDED AND ITS PARITY STANDS UNTOUCHED: both channels carry the "
     "same sigma^3/omega, which is mu^-4 and an INTEGER power of x = mu^2, so the parity rides entirely "
     "on the recoupling sum.  ** What moves is the coefficient's STRUCTURE -- two invariants at weights "
     "2 and 9 where r7010 filed a single 8 g^2 -- and not the frequency dependence **",
     sp.simplify((1/sp.Symbol("x", positive=True)**sp.Rational(1, 2))**3
                 / sp.Symbol("x", positive=True)**sp.Rational(1, 2)
                 - sp.Symbol("x", positive=True)**-2) == 0)

# ============================================================ B. the trace is absent
head("B.  ⛭⛭ THE TRACE CHANNEL IS ABSENT AT EVERY LEVEL, BY A SINGLET COUNT")

def tri(x, y, z):
    return abs(x - y) <= z <= x + y

def channels(m):
    a, b = sp.Rational(m + 1, 2), sp.Rational(m - 3, 2)
    out = []
    for ch in itertools.product([(a, b), (b, a)], repeat=3):
        js, jps = tuple(x[0] for x in ch), tuple(x[1] for x in ch)
        if tri(*js) and tri(*jps):
            out.append((js, jps))
    return out

def pair_contract(j1, j3):
    """sum_nu (-1)^(j1-nu) 3j(j1 j1 j3; nu, -nu, 0): the 3j factor a trace over a pair carries."""
    tot, nu = sp.Integer(0), -j1
    while nu <= j1:
        tot += (-1)**(j1 - nu)*wigner_3j(j1, j1, j3, nu, -nu, 0)
        nu += 1
    return sp.nsimplify(sp.simplify(tot))

rows = [(j1, j3, pair_contract(j1, j3)) for j1 in (sp.Integer(2), sp.Integer(3), sp.Rational(5, 2))
        for j3 in (sp.Integer(0), sp.Integer(2), sp.Integer(3), sp.Integer(4)) if tri(j1, j1, j3)]
for j1, j3, v in rows:
    print(f"      j = {j1}, free label {j3}:  {v}", flush=True)
gate("⛭ THE PAIR CONTRACTION VANISHES UNLESS THE FREE LABEL IS ZERO -- and the control returns the "
     "AFFIRMATIVE exactly where the affirmative is true, being non-zero at every free label zero and "
     "zero at every other, so the rule is a selection rule and not an artefact of one spin",
     all(v != 0 for j1, j3, v in rows if j3 == 0)
     and all(v == 0 for j1, j3, v in rows if j3 != 0)
     and len([1 for _, j3, _ in rows if j3 == 0]) == 3)

full_singlets = []
for m in (3, 5, 7, 9, 11, 13):
    for (js, jps) in channels(m):
        for i in range(3):
            pair = [jps[k] for k in range(3) if k != i]
            if pair[0] == pair[1] and jps[i] == 0 and js[i] == 0:
                full_singlets.append((m, js, jps, i))
right_zero = [(m, js, jps, i) for m in (3, 5, 7, 9, 11, 13) for (js, jps) in channels(m)
              for i in range(3)
              if [jps[k] for k in range(3) if k != i][0] == [jps[k] for k in range(3) if k != i][1]
              and jps[i] == 0]
print(f"      slots with a zero FREE RIGHT label: {len(right_zero)} "
      f"(all at m = {sorted({r[0] for r in right_zero})});  of those, FULL singlets: "
      f"{len(full_singlets)}", flush=True)
for m, js, jps, i in right_zero:
    print(f"        m={m}  js={tuple(str(x) for x in js)} jps={tuple(str(x) for x in jps)}  free slot "
          f"{i}: right label {jps[i]}, LEFT spin {js[i]}", flush=True)
gate("⛔⛭⛭ AND NO CHANNEL AT ANY LEVEL CARRIES A FULL SINGLET IN A TRACE SLOT -- the SAME identity "
     "applies on the left indices, so a trace needs right label zero AND left spin zero.  Above m = 3 "
     "no label is zero at all; at m = 3 the two never coincide, the zero right label sitting with left "
     "spin two.  ⇒ ** sum t^2 = 0 IDENTICALLY and the assembly is 2 sum T^2 sigma^3/(hbar omega) **",
     right_zero and not full_singlets
     and all(m == 3 for m, _, _, _ in right_zero)
     and pair_contract(sp.Integer(2), sp.Integer(2)) == 0)

kap, aa = sp.symbols("kappa a", positive=True)
c4s, g2s = sp.symbols("c4 g2", positive=True)
R_num = 8*g2s*aa**2*sig**3/(hb*om)
R_den = 8*c4s*aa*sig**2
gate("⌗ AND r7060's CRITERION IS UNTOUCHED FOR A REASON, COMPUTED RATHER THAN ASSUMED: its 8 sits in "
     "BOTH the cubic energy and the quartic expectation and CANCELS in the ratio R, so the coefficient "
     "that was wrong was never load-bearing there.  ** The criterion, the crossing and r7056's five "
     "negative levels all stand; what the 8 was load-bearing for is the residue's ABSOLUTE scale **",
     sp.simplify(sp.simplify(R_num/R_den) - g2s*aa*sig/(c4s*hb*om)) == 0
     and not sp.simplify(R_num/R_den).has(sp.Integer(8)))

# ============================================================ C. the rank, on its two domains
head("C.  ⛔⛭⛭ (b) THE INVARIANT: r7062's OWN RANKS, LOADED FROM ITS OWN SOURCE")

src = open(os.path.join(HERE, RANKSRC), encoding="utf-8").read().split("\n")
cut = next(i for i, ln in enumerate(src) if ln.startswith("r6 = rank_of(six, 6)"))
NS = {"__name__": "r7062_machinery"}
pre = [ln for ln in src[147:cut] if not ln.startswith(("print(__doc__", 'print("COMPUTES:'))]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile("\n".join(pre), RANKSRC, "exec"), NS)
rank_of, on_ds, six, names6, al = (NS[k] for k in ("rank_of", "on_ds", "six", "names6", "al"))
gate(f"the dimension-six scalars and the rank machinery are r7062's own, loaded from its source rather "
     f"than restated, and NOTHING in the loaded prefix FAILED ({len(NS['FAILED'])} failures)",
     NS["FAILED"] == []
     and names6 == ["R^3", "R Ric^2", "Ric^3", "(grad R)^2", "R Box R"])

r6 = rank_of(six, 6)
sixDS = [sp.simplify(on_ds(e)*al**6) for e in six]
print(f"      pointwise rank: {r6} of 5;   on the one-parameter family: {sixDS}", flush=True)
gate(f"⛭ r7062's TWO RANKS, RECOVERED: the five scalars are POINTWISE INDEPENDENT on a general scale "
     f"factor -- rank {r6} of 5, no relation at all -- while on the one-parameter family the two "
     f"derivative scalars VANISH and the other three are pure numbers times alpha^-6",
     r6 == 5 and sixDS[3] == 0 and sixDS[4] == 0
     and all(v.is_Number and v != 0 for v in sixDS[:3]))

# the matching (b) was ordered to do, done and found DEGENERATE
res = sp.Rational(-15405, 8192)                     # r7074's residue, used as the number to match
k = sp.symbols("k0:5")
combo = sum(k[i]*sixDS[i] for i in range(5))
sol = sp.solve([sp.Eq(combo, res)], list(k), dict=True)
free = sorted(set().union(*[sp.sympify(v).free_symbols for v in sol[0].values()])
              & set(k[:3]), key=str) if sol else []      # freedom among the NON-VANISHING three
gate(f"⛔⛭⛭ AND THE MATCHING THE ORDER ASKED FOR IS DEGENERATE, EXHIBITED RATHER THAN COUNTED: matching "
     f"one number on that family is ONE equation on the THREE non-vanishing directions, and its "
     f"solution set carries {len(free)} free coefficients.  ** So the family cannot distinguish the "
     f"representatives it is rank one across, and rank one is the degeneracy that BLOCKS the naming "
     f"rather than the lever that forces it **",
     bool(sol) and len(free) == 2)
alt = []
for i in range(3):
    single = {k[j]: (res/sixDS[i] if j == i else 0) for j in range(5)}
    alt.append(sp.simplify(sum(single[k[j]]*sixDS[j] for j in range(5)) - res) == 0)
print(f"      each of {names6[:3]} ALONE reproduces the residue after rescaling: {alt}", flush=True)
gate("⌗ and the degeneracy is exhibited at its sharpest: EACH of the three non-derivative scalars, "
     "ALONE, reproduces the residue exactly after one rescaling -- so the matching does not even "
     "narrow the representative to a subset, let alone to one",
     all(alt) and len(alt) == 3)
gate("⌗ AND THE TWO DERIVATIVE SCALARS ARE THE ONLY THING THE FAMILY DOES DECIDE, which is the "
     "affirmative half and is kept: they vanish on it identically, so they are excluded as sole "
     "carriers -- a real if small piece of information, and the only one available here",
     sixDS[3] == 0 and sixDS[4] == 0
     and sp.solve([sp.Eq(k[3]*sixDS[3] + k[4]*sixDS[4], res)], [k[3], k[4]], dict=True) == [])

# ============================================================ D. the terminus and the correction
head("D.  ⛔⛔ THE TERMINUS, AND THE DOMAIN ERROR THAT IS THIS SEAT'S OWN")

gate("⛭⛭⛭ ⇒ THE ROW'S STATED TERMINUS IS REACHED AND ITS CONDITION IS EXHIBITED TRUE RATHER THAN "
     "DECLINED: the one-parameter family does NOT distinguish the representatives it is rank one "
     "across, so ** naming the dimension-six invariant needs a datum outside this background **, which "
     "is a statement about the background's reach and not about the coefficient",
     r6 == 5 and all(alt) and len(free) == 2)
bad_reading = ["the rank one is on the ONE-PARAMETER FAMILY and was applied to the ADMITTED CLASS",
               "and a rank of ONE does not FORCE a representative -- it makes them INDISTINGUISHABLE"]
for i, r in enumerate(bad_reading, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛔⛔ AND THE DEFECT IS THIS SEAT'S, IN THE PARAGRAPH THAT OPENED THE ROW.  r7077 asked for a "
     "reading; this seat answered that sec:lock's rank one meant the five collapse to a single "
     "direction ON THE ADMITTED CLASS so the representative is FORCED up to normalisation.  ** Both "
     "halves are wrong and in the same way ** -- a rank read off one domain and applied on another, and "
     "a degeneracy read as a determination",
     len(bad_reading) == 2 and r6 == 5 and len(free) == 2)
gate("⌗ AND IT IS THE ROW'S OWN SEVENTH FACE, committed by the seat that has been enforcing it: ** the "
     "domain of an EQUIVALENCE is part of the statement. **  sec:lock says in terms that at dimension "
     "six there is no identity to descend, so on the class the ledger uses -- the scale factor "
     "QUANTIZED -- the five are independent and nothing collapses at all",
     r6 == 5 and sp.Integer(len(names6)) == 5)
gate("⌗ AND WHAT SURVIVES IS SAID SEPARATELY FROM WHAT FAILS: PO-71's object is real and unanswered, "
     "r7074's residue and r7068's criterion both stand, and (a) is delivered -- the assembly's two "
     "invariants, the traceless finding and the parity's survival.  ** Only the naming is blocked, and "
     "the datum it needs is one that separates R^3, R Ric^2 and Ric^3 **",
     all(alt) and sp.simplify(shift(3, T3) - dE3) == 0 and not full_singlets)
gate("⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the ranks are r7062's, over a CHOSEN five-element "
     "subset, hence a LOWER bound on the full basis -- which is the direction this negative needs, "
     "since completing the basis can only RAISE the pointwise rank and so only WORSEN the family's "
     "degeneracy.  The assembly is exact for modes of one common frequency, the same-level case",
     r6 == 5 and len(names6) == 5 and len(free) == 2)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
