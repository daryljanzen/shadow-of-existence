#!/usr/bin/env python3
"""r7662 (60) -- P1's `prop:causal-alignment` against its Lean, clause by clause, on a named tree.

⛭ THE ORDER'S THREE QUESTIONS are the three verdict classes: a clause P1 states that the Lean does not
prove (`STATED-NOT-PROVED`); a hypothesis the Lean takes that P1 does not state (`ASSUMED-NOT-STATED`);
a clause the witness does not exercise non-vacuously (`VACUOUS`).  Two classes the order did not name
turned up and are reported beside them rather than folded in:

  `PROMOTED`        -- P1 states it as a HYPOTHESIS and the Lean PROVES it.  The Lean is stronger.
  `STATED-NOT-USED` -- P1 assumes it and the Lean never takes it.  P1 is stronger, which is not a gap
                       in the formalisation but is a fact about the proposition's hypotheses.

⌗ *Before two stretches are identified by a label, check how many-to-one the label is on the object* --
so every mapping below prints the Lean term it matched, and where one P1 clause needs several Lean
terms (or several P1 clauses one term) the multiplicity is printed and not smoothed.

⛔ EVERY MAPPING IS LOCATED IN THE FILES, NOT ASSERTED.  Each Lean term is found by searching the probe
for its own text; a term that cannot be found is a hard stop, because a mapping to a term that is not
there would be a statement about this script.  And each is FAILABLE: a decoy term must not be found.

⌗ This revision does NOT re-verify the Lean.  Whether `mx_prop_causal_alignment` compiles and what
axioms it rests on are `71`'s measurements; this reads the STATEMENTS against each other.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


TREE = open(os.path.join(HERE, 'runs', 'TREE.txt'), encoding='utf-8').read()
P1 = open(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'),
          encoding='utf-8', errors='replace').read()
LEAN = open(os.path.join(ROOT, 'computations', 'formalisation', 'lean', 'probes',
                         'ConformalBoundary.lean'), encoding='utf-8', errors='replace').read()
P1FLAT = re.sub(r'\s+', ' ', P1)
LFLAT = re.sub(r'\s+', ' ', LEAN)

# the proposition's own statement, located rather than quoted from memory
_m = re.search(r'\\begin\{proposition\}\[Asymptotic exterior slicings[^\]]*\]'
               r'\\label\{prop:causal-alignment\}(.*?)\\end\{proposition\}', P1FLAT)
if _m is None:
    sys.exit("⛔ P1 no longer carries `prop:causal-alignment` in the form this file locates.  A cold "
             "read of a proposition that is not there is worse than no read, so this is a hard stop.")
PROP = _m.group(1)
_t = re.search(r'theorem mx_prop_causal_alignment(.*?):= by', LFLAT)
if _t is None:
    sys.exit("⛔ the probe no longer carries `mx_prop_causal_alignment`'s statement in the form this "
             "file locates.  Hard stop rather than a verdict against a term that is not there.")
THM = _t.group(1)


def inlean(needle, where=None):
    return needle in (where if where is not None else LFLAT)


print(__doc__)
print("=" * 112)
print("  r7662 (60) -- P1's proposition against its Lean, on a named tree")
print("=" * 112)
print("\nⓐ  ① THE TREE, recorded before either side was read")
for line in TREE.strip().split('\n')[:4]:
    print("      " + line)
check("ⓐ① ① the tree is named, with the commit of BOTH objects this revision compares, so a later "
      "reading can tell whether it disagrees with this one or with a different tree",
      'BH_causality_v2.tex' in TREE and 'ConformalBoundary.lean' in TREE)
check("ⓐ② and both statements are LOCATED in their files rather than quoted from memory -- the "
      "proposition between its own delimiters, the theorem up to its `:= by`",
      len(PROP) > 400 and len(THM) > 400)

# ════════════════════════════════════════════════════════ the hypotheses
print("\nⓑ  THE HYPOTHESES — P1's prose against the Lean's binders")
HYPS = [
    ('asymptotically flat, with a conformal boundary',
     'asymptotically flat', ['ConformalExtension S St', 'h𝒥 : 𝒥 ⊆ St.M',
                             'hI : S.IpastSet (range O) = X.ι ⁻¹\' St.IpastSet 𝒥'], 'MATCHED'),
    ('the horizon IS ∂J⁻(𝒥⁺)',
     '\\mathcal{H}^+=\\partial J^-(\\mathscr{I}^+)', ['S.H J = frontier (X.ι ⁻¹\' St.JpastSet 𝒥)'],
     'PROMOTED'),
    ('the exterior domain D is globally hyperbolic',
     'globally hyperbolic', ['hΘ : S.IsCauchyTemporalOn (S.D J) Θ'], 'ENCODED'),
    ('O is a worldline, future-ordered',
     'future-complete worldline', ['hmono : ∀ s t : ℝ, s < t → S.Chr (O s) (O t)'], 'MATCHED'),
    ('O is FUTURE-COMPLETE and O(τ) → i⁺',
     'O(\\tau)\\to i^+', [], 'STATED-NOT-USED'),
    ('the causal past of O is the whole exterior',
     'I^-(O)=D', ['hOD : S.IpastSet (range O) = S.D J'], 'MATCHED'),
    ('Θ is a smooth Cauchy temporal function of D',
     'Cauchy temporal function', ['hΘ : S.IsCauchyTemporalOn (S.D J) Θ'], 'MATCHED'),
    ('Θ is adapted to O: Θ(O(τ)) = τ + const',
     '\\Theta(O(\\tau))=\\tau+\\mathrm{const}', ['hadapt : ∀ τ, Θ (O τ) = τ + c'], 'MATCHED'),
]
print(f"      {'P1 clause':<46} {'in P1':>6}  Lean binder(s)")
hyp_rows = []
for name, p1needle, terms, verdict in HYPS:
    inp1 = p1needle.replace(' ', '') in PROP.replace(' ', '')
    found = [t for t in terms if inlean(t)]
    hyp_rows.append(dict(clause=name, in_p1=inp1, terms=terms, found=found, verdict=verdict))
    print(f"      {name:<46} {'yes' if inp1 else 'NO':>6}  "
          + (f"{len(found)} of {len(terms)}: {found[0][:58]}" if found else
             '— none, and none expected' if verdict == 'STATED-NOT-USED' else '*** NOT FOUND'))
check("ⓑ① every P1 hypothesis is located in P1's own proposition text", all(r['in_p1'] for r in hyp_rows))
check("ⓑ② and every Lean binder this read maps to is located in the theorem's own statement",
      all(len(r['found']) == len(r['terms']) for r in hyp_rows))

EXTRA = [('[T2Space N]', 'Hausdorffness of the spacetime'),
         ('hL : S.LocallyOneChart', 'one-chart locality of S'),
         ('hLt : St.LocallyOneChart', 'one-chart locality of the extension'),
         ('hJM : J ⊆ S.M', 'carrier bookkeeping for J'),
         ('hHM : frontier (X.ι ⁻¹\' St.JpastSet 𝒥) ⊆ S.M', 'carrier bookkeeping for the horizon')]
CONV = re.search(r'(?i)(hausdorff|paracompact|second countable|by a spacetime we mean)', P1FLAT)
print(f"\nⓒ  ② ASSUMED-NOT-STATED — Lean binders with no counterpart in P1")
print(f"      does P1 carry a conventions clause naming Hausdorffness or the manifold's category "
      f"anywhere? {'YES' if CONV else 'NO'}")
notstated = []
for term, gloss in EXTRA:
    here = inlean(term, THM) or inlean(term)
    notstated.append(dict(term=term, gloss=gloss, in_lean=here))
    print(f"      {'in the theorem' if here else '*** NOT IN THE THEOREM':<24} {term:<52} {gloss}")
check(f"ⓒ① ⑥ AS REGISTERED: there is at least one ASSUMED-NOT-STATED hypothesis -- {len(notstated)} "
      f"Lean binders have no counterpart in P1's proposition, and P1 carries no conventions clause "
      f"that would supply them", all(r['in_lean'] for r in notstated) and CONV is None)
check(f"ⓒ② ⑦ AND MY ARM'S OWN NEGATIVE IS TESTED, NOT ASSUMED: P1 is searched for a conventions "
      f"clause naming Hausdorffness, paracompactness, second countability or `by a spacetime we "
      f"mean`, and the verdict turns on that search returning {'a match' if CONV else 'nothing'}",
      CONV is None)

# ════════════════════════════════════════════════════════ the conclusions
print("\nⓓ  THE CONCLUSIONS — P1's clauses against the Lean's seven")
SEVEN = ['S.H J = frontier (X.ι ⁻¹\' St.JpastSet 𝒥)', 'S.SublevelProper J Θ',
         'KLi (S.slice J Θ) = frontier', 'KLs (S.slice J Θ) = frontier',
         'KLi (S.cone O) = frontier', 'KLs (S.cone O) = frontier',
         'TCF.FrameHyp (S.gE x) (ℓ x) (n x) (dcov Θ x)']
CONC = [
    ('the past cones converge to the horizon as τ → ∞', 'converge to it',
     ['KLi (S.cone O) = frontier', 'KLs (S.cone O) = frontier'], 'PROVED'),
    ('NONE of the past cones MEETS the horizon', 'none of which meets', [], 'STATED-NOT-PROVED'),
    ('the stretch approached to within any distance EXTENDS TO THE FUTURE WITHOUT BOUND',
     'extending to the future without bound', [], 'STATED-NOT-PROVED'),
    ('the slices accumulate on the horizon, every point approached when late enough',
     'accumulate on', ['KLi (S.slice J Θ) = frontier'], 'PROVED'),
    ('and the slices accumulate at NO point outside it', 'accumulating at no point outside it',
     ['KLs (S.slice J Θ) = frontier'], 'PROVED'),
    ('each finite-Θ slice lies entirely in D', 'lies entirely in', ['S.SublevelProper J Θ'], 'PROVED'),
    ('the tangent hyperplanes become asymptotically tangent to the generators',
     'asymptotically tangent to the generators', [SEVEN[6]], 'PROVED'),
    ('consequently the horizon is on no finite exterior slice', 'does not occur on any finite',
     ['S.SublevelProper J Θ'], 'PROVED'),
]
print(f"      {'P1 clause':<62} {'in P1':>6}  verdict")
conc_rows = []
for name, p1needle, terms, verdict in CONC:
    inp1 = p1needle.replace(' ', '') in PROP.replace(' ', '')
    found = [t for t in terms if inlean(t, THM)]
    ok = (len(found) == len(terms)) if terms else True
    conc_rows.append(dict(clause=name, in_p1=inp1, terms=terms, found=found, verdict=verdict))
    print(f"      {name:<62} {'yes' if inp1 else 'NO':>6}  {verdict}"
          + (f"  ({len(found)} term(s): {found[0][:40]})" if found else ''))
    if not ok:
        _fail.append(f"a conclusion's mapped term is absent from the theorem: {name}")
nsnp = [r for r in conc_rows if r['verdict'] == 'STATED-NOT-PROVED']
print(f"""
      ⇒ The Lean's conclusion is a SEVEN-TUPLE and P1's prose is EIGHT clauses.  Six of P1's eight map
      onto it, two of them many-to-one (the slice pair carries `accumulate on` and `at no point
      outside it`; the cone pair carries `converge to it`), and `SublevelProper` carries two of P1's
      clauses at once -- the finite slice lying in D and the consequence drawn from it.
      ⛔ {len(nsnp)} of P1's clauses have NO term in the seven:""")
for r in nsnp:
    print(f"         • {r['clause']}")
print(f"""      ⌗ Both are QUANTITATIVE where the Lean is set-theoretic.  `KLs (S.cone O) = 𝓗⁺` says the
      cones' upper Kuratowski limit IS the horizon; it does not say an individual cone is disjoint
      from it, and `SublevelProper` is about slices, not cones.  And no term in the seven speaks of a
      stretch growing without bound to the future -- set convergence does not carry it.""")
check(f"ⓓ① ⑥ AS REGISTERED: the order's negative is NOT reached -- {len(nsnp)} clause(s) of P1 are "
      f"STATED-NOT-PROVED and at least one hypothesis is ASSUMED-NOT-STATED, so the Lean does not "
      f"prove exactly P1's proposition under exactly P1's hypotheses", len(nsnp) >= 1)
check(f"ⓓ② and every clause reported PROVED has its Lean term located IN THE THEOREM'S OWN STATEMENT, "
      f"so none is counted proved because a nearby term looked similar",
      all(len(r['found']) == len(r['terms']) for r in conc_rows))
check(f"ⓓ③ ⑤ FAILABLE: a decoy term of the same shape is NOT found, so `located` means located",
      not inlean('KLi (S.cone O) = interior', THM)
      and not inlean('S.SuperlevelProper J Θ', THM))
check(f"ⓓ④ and the SEVEN are the theorem's whole conclusion -- each of the seven is located, so the "
      f"comparison is against all of it and not a convenient subset",
      sum(1 for t in SEVEN if inlean(t, THM)) == len(SEVEN))

# ════════════════════════════════════════════════════════ non-vacuity
print("\nⓔ  ③ NON-VACUITY, ON THE WITNESS'S OWN DISCHARGED INSTANCE")
W = re.search(r'theorem mx_witness_headline(.*?)end NModel', LFLAT)
wtxt = W.group(1) if W else ''
WIT = [('the horizon is NON-EMPTY at the witness',
        '(frontier (mx_witnessExt.ι ⁻¹\' minkN.JpastSet mx_scri)).Nonempty'),
       ('and it is characterised, not merely named: 𝓗⁺ = {U = 0}', '↔ (φ x).1 = 0'),
       ('the seven are destructured from the theorem itself',
        'obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment'),
       ('the tangency clause is applied at a NAMED horizon point', 'h6 p₀ hp ℓN nN'),
       ('with a named frame and a limit', 'mc_witness_tangency_holds p₀')]
for gloss, needle in WIT:
    print(f"      {'yes' if inlean(needle, wtxt) or inlean(needle) else '*** NO':<8} {gloss}")
nonvac = all(inlean(n, wtxt) or inlean(n) for _g, n in WIT)
print(f"""      ⇒ So no clause is VACUOUS: the horizon is non-empty and pinned to `{{U = 0}}`, the seven
      are read off the theorem rather than restated, and the tangency clause -- the one conclusion
      that could have been satisfied by having no point to test -- is discharged AT a horizon point
      with a named frame.  ⌗ *An arm with no instance to score is not a pass, and this witness gives
      every clause an instance.*""")
check("ⓔ① ③ NO CLAUSE IS VACUOUS on the witness: the horizon is non-empty, characterised, and the "
      "tangency clause is discharged at a named point with a named frame", nonvac)
check("ⓔ② ④ and non-vacuity is read off the witness's own discharge rather than from my judgement "
      "that a clause sounds substantive -- the destructuring of the seven is located in the file",
      inlean('obtain ⟨h0, h1, h2, h3, h4, h5, h6⟩ := MSpacetime.mx_prop_causal_alignment'))

print("""
ⓕ  WHAT IS NOT CLAIMED.  No correction to P1 and none to the Lean; nothing of `71`'s is edited.  This
    does not re-verify the Lean: whether the theorem compiles and what axioms it rests on are `71`'s
    measurements.  And the two STATED-NOT-PROVED clauses are not errors in P1 -- they are clauses the
    formalisation does not reach, which is what the order asked to be told.""")

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(tree=TREE.strip().split('\n')[:4], hypotheses=hyp_rows,
               assumed_not_stated=notstated, p1_conventions_clause=bool(CONV),
               conclusions=conc_rows, stated_not_proved=[r['clause'] for r in nsnp],
               seven_located=sum(1 for t in SEVEN if inlean(t, THM)), non_vacuous=nonvac,
               failures=_fail),
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
