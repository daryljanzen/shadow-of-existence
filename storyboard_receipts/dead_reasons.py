"""
dead_reasons.py -- THE INSTRUMENT STAGE 8 WAS BLOCKED ON.  (r1090)

THE PROBLEM (CODA_FIELD_NOTE face 31, which fired THREE times on r1088):
  When a CLAIM is corrected, the text changes and everyone sees it.
  When a REASON is corrected and the claim SURVIVES, nothing looks wrong:
        "C is not R"  was true before the weld and after it.
        Only the BECAUSE changed.
  So a claim-level sweep -- "does this paper still say X?" -- returns CLEAN over a
  corpus whose every reason has rotted. That is the r1063 null in a new costume:
  the check cannot see the class of defect present.

THE INSTRUMENT:
  A reason, unlike an understanding, LEAVES TEXT. When a reason dies it leaves a
  fingerprint -- the specific phrases it was written in. Those are greppable.
  So: when you kill a reason, REGISTER ITS CORPSE. Every later pass greps for it.

HOW TO USE IT:
  python3 dead_reasons.py                 # sweep the corpus, report every hit
  python3 dead_reasons.py --list          # just show the register
  Add an entry the moment you kill a reason. That is the whole discipline: the
  registering is a SEPARATE ACT from the correcting, and face 31 is what happens
  when you do the second and skip the first.

WHAT THIS CANNOT DO, said plainly so nobody reports clean on it (THE_METHOD s4b):
  It finds dead reasons that were WRITTEN DOWN in registered language. It cannot find
  a dead reason that (a) was never registered, (b) is paraphrased past the fingerprint,
  or (c) lives in an instance's head rather than on disk -- which is EXACTLY where all
  three r1088 firings lived. So this is a NET, not a proof. A clean sweep here means
  "no registered corpse found in registered language", and NOTHING MORE. Say that,
  never "clean".
"""
import re, sys, pathlib

# ---------------------------------------------------------------------------
# THE REGISTER. One entry per reason that DIED while its claim SURVIVED.
#   killed   : the dead because, in the words it was written in
#   survives : the claim that is still true (this is the camouflage)
#   because  : the reason that replaced it
#   finger   : regexes that betray the corpse in text
#   ok       : paths where the phrase is legitimate (the register itself, the
#              field note recording the death, a ledger keeping the negative)
# ---------------------------------------------------------------------------
REGISTER = [
    dict(id="DR1", killed="'C != R because R is mass-ODD and C is mass-EVEN'",
         survives="C != R", because="LINEARITY: R is linear, C is antilinear",
         note="the weld (r1073, Daryl): |2M| is the physical mass and R PRESERVES it; only "
              "the SIGN flips, and the sign is the relational branch label. A label was "
              "compared to a mass.",
         finger=[r"mass-odd.{0,80}mass-even", r"mass-even.{0,80}mass-odd",
                 r"R is mass-odd", r"C is mass-even"]),
    dict(id="DR2", killed="'Q->-Q FIXES species'",
         survives="C != (Q->-Q)", because="LINEARITY; and Q->-Q is only C's EVEN FACE",
         note="the weld: Q->-Q IS the species flip. species=sign(r) was deployed against "
              "the physical identity it exists to encode.",
         finger=[r"Q\s*(?:\\mapsto|↦|->)\s*-\s*Q[^.]{0,60}fix(?:es)?\s+(?:every\s+)?species",
                 r"fixes species"]),
    dict(id="DR3", killed="'charge is the R-even datum' (UNQUALIFIED)",
         survives="the metric's charge term is R-even", because="TRUE OF THE METRIC, FALSE OF THE "
              "POTENTIAL: A_t=Q/r is R-ODD, so A->-A and F->-F -- R flips the charge as seen",
         note="weld.py. The metric is the one object built to be blind to the charge's sign.",
         finger=[r"charge is the \$?R\$?-even datum(?!.{0,40}metric)"]),
    dict(id="DR4", killed="'every GEOMETRIC REFLECTION is linear'",
         survives="C is no isometry, and closes from the field",
         because="every substrate ISOMETRY is real and linear -- the premise covers L1 only",
         note="rem:C-scope, r1088. not-an-isometry != not-geometric: tau~->conj(tau~) is "
              "antilinear AND geometric, at L2. This phrase is the overdraw itself.",
         finger=[r"every geometric reflection is linear"]),
    dict(id="DR5", killed="'the discrete orientation parity, THE ONE RESIDUE it leaves'",
         survives="the wall stands; no continuous colour",
         because="the residue is LARGER by the L2 antilinear face; the perimeter was drawn "
                 "at the isometry group's edge and L2 was never weighed",
         note="rem:C-scope. Fired inside P13 itself: sec:meaning carried this after the "
              "morning's correction. Face 31, third firing.",
         finger=[r"the one residue it leaves"]),
    dict(id="DR6", killed="'R negates the roots THEREFORE it is the diagram automorphism' (UNQUALIFIED)",
         survives="R IS the diagram automorphism, and carries 3 -> 3bar",
         because="A2-SPECIFIC: -1 is not in W(A2), so negation is OUTER; Aut(A2)/W has order "
                 "2, so negation and D generate the same Z2 (negation = w0 o D)",
         note="closure_i_check.py. In A1, B2, G2 -- every rank-2 system but A2 -- -1 IS Weyl, "
              "negation is INNER, and it conjugates NOTHING. The step reads general and is not.",
         finger=[r"negates the roots[^.]{0,50}(?:diagram automorphism|hence|therefore)"]),
    dict(id="DR7", killed="'the ruling-swap is one of R's four faces' (as if it CHARACTERISED R)",
         survives="R does swap the two null rulings; the four faces are one Z2",
         because="GENERIC: every orientation-reversing isometry swaps them -- T does too, "
                 "species-PRESERVING. The species content is what separates R.",
         note="ruling_swaps.py, which the glossary cited as a nonexistent 'r_swap.py'. "
              "Read the four faces as four things this one map DOES, not four things that "
              "IDENTIFY it.",
         finger=[r"swaps the two null rulings(?!.{0,120}generic)"]),
    dict(id="DR8", killed="'30 degrees arrives from PURE COMBINATORICS, with no reference to the slicing'",
         survives="both 30s are 360/(3x4), and the 3 is the same 3",
         because="the FOURS DIFFER: the dial's 4 is forced (a sine's quarter period); the "
                 "kaleidoscope's 4 is CHOSEN -- every n coprime to 3 closes evenly",
         note="thirty_degrees.py. It rhymes on its 3 and coincides on its 4.",
         finger=[r"pure\s+combinatorics"]),
    dict(id="DR9", killed="'the M-cancellation IS the corpus's generation result'",
         survives="K is M-free along the bead; M sets the SCALE not the SHAPE",
         because="DIFFERENT QUANTIFIERS: 'every root returns the same 2M' is over the three "
                 "roots at FIXED M; 'K is M-free' is over M at FIXED w. Neither implies the other.",
         note="M_cancellation.py. The over-correction inside a concession, one turn after "
              "being caught.",
         finger=[r"M-cancellation[^.]{0,60}generation result",
                 r"generation result[^.]{0,60}M-cancellation"]),
    dict(id="DR10", killed="'R CARRIES the bead's expansion leg onto its conjugate branch'",
         survives="the bead's two halves are species-conjugate",
         because="R FIXES r=0 (the branch point) and EXCHANGES THE REGIONS. A map is not a "
                 "path, and the legs are NOT mirrors (cosh vs sinh) -- P7's own caption says so.",
         note="closure_iv_check.py. And the asymmetry is the CONTENT: were the legs mirrors "
              "there would be no asymmetry for the cosmogenesis to carry.",
         finger=[r"carries the bead's expansion leg"]),
    dict(id="DR11", killed="'the conjugate pair IS particle+antiparticle' (the FS reading, ASSERTED)",
         survives="tau~->conj(tau~) is antilinear, geometric, fixes the photon's axis, swaps the wings",
         because="that is the SHAPE of a conjugation. Whether the wings ARE a particle/anti "
                 "pair is [6*]: on species=sign(r) BOTH wings lie at r<0 and the exchange "
                 "moves nothing.",
         note="Storyboard [6*]. Rode into P13 in THREE places on r1088 before being stripped.",
         finger=[r"Feynman--?St\\?\"?uckelberg particle\$?\\?leftrightarrow\$?antiparticle relation"]),
    dict(id="DR12", killed="'C is field-level' / 'the charge face is field-level' (UNQUALIFIED)",
         survives="only the charge SIGN is field-level (odd in A_t=Q/r, the metric Q^2-blind)",
         because="the closure (r1089/A3) enlarged the residue: C's KINEMATIC face is geometric "
                 "(R o K, the complex-analytic tau~<->conj tau~), C=(Q->-Q)_field o (R o K)_geometric; "
                 "only the electric-charge SIGN closes from the field. 'C field-level' unqualified is "
                 "the pre-closure reading, and is dead.",
         note="Killed r1089. Rode into CPT_COHERENCE_SWEEP Delta2/Delta6, the P13 card guard, and the "
              "arc A4 note; stripped r1101-r1102. Registered r1103 (cowork).",
         finger=[r"charge face is field-level", r"\bC is therefore field-level",
                 r"Dirac C is field-level", r"\bC-field-level"]),
]

# paths where a corpse is legitimately quoted (registering, recording, or keeping it)
ALLOW = ("storyboard_receipts/dead_reasons.py", "CODA_FIELD_NOTE.md", "BUNDLE_",
         "C40_HARVEST", "TIDAL_SHIFT_PLAN", "SYNTHESIS_FIGURE_STORYBOARD.md",
         "storyboard_receipts/")

ROOT = pathlib.Path(__file__).resolve().parent.parent

def sweep():
    files = [p for p in ROOT.rglob("*") if p.suffix in (".tex", ".md")
             and "__pycache__" not in str(p)]
    hits, checked = [], 0
    for entry in REGISTER:
        for pat in entry["finger"]:
            rx = re.compile(pat, re.I | re.S)
            for f in files:
                rel = str(f.relative_to(ROOT))
                if any(a in rel for a in ALLOW):
                    continue
                checked += 1
                try: text = f.read_text(errors="ignore")
                except Exception: continue
                for m in rx.finditer(text):
                    line = text[:m.start()].count("\n") + 1
                    ctx = re.sub(r"\s+", " ", text[max(0,m.start()-70):m.end()+70])
                    # Is the corpse LIVE, or is it being MARKED dead? A correction quotes the
                    # phrase it kills, so the net cannot tell the two apart on the phrase alone.
                    # HEURISTIC, and it is only that: look for a correction marker nearby.
                    near = text[max(0, m.start()-400):m.end()+400]
                    marked = bool(re.search(MARKERS, near, re.I))
                    hits.append((entry["id"], rel, line, ctx, marked))
    return hits

# markers that suggest the phrase is being QUOTED IN ORDER TO KILL IT, not asserted.
# This is a heuristic and it can be fooled in both directions: a correction phrased
# without any of these words reads as live; a live reason sitting near an unrelated
# "WRONG" reads as marked. It TRIAGES; it does not decide. Read every hit.
MARKERS = (r"⚠|⛔|✘|CORRECTED|SUPERSEDED|RETIRED|WRONG|DEAD|dead reason|does not follow|"
           r"overdraw|stale|refuted|struck|~~|NOT the argument|no longer|was the reversal|"
           r"rigged|logged not deleted|kept, not deleted|the negatives are the map")

if "--list" in sys.argv:
    print(f"THE DEAD-REASONS REGISTER — {len(REGISTER)} entries\n" + "="*78)
    for e in REGISTER:
        print(f"\n[{e['id']}]  DEAD: {e['killed']}")
        print(f"       SURVIVES (the camouflage): {e['survives']}")
        print(f"       THE LIVE BECAUSE: {e['because']}")
        print(f"       {e['note']}")
    sys.exit(0)

print("SWEEPING the corpus for registered dead reasons in registered language...\n")
hits = sweep()
if not hits:
    print("  NO REGISTERED CORPSE FOUND IN REGISTERED LANGUAGE.")
    print("  ** That is NOT 'clean'. ** This net catches only reasons that were (a) killed,")
    print("     (b) registered, and (c) still phrased in the registered words. It CANNOT see")
    print("     an unregistered death, a paraphrase, or a reason living in an instance's head")
    print("     -- which is where all three r1088 firings lived. Report it as what it is.")
else:
    live   = [h for h in hits if not h[4]]
    marked = [h for h in hits if h[4]]
    print(f"  {len(hits)} hit(s): {len(live)} UNMARKED, {len(marked)} apparently marked.\n")
    print("  " + "="*74)
    print(f"  UNMARKED — {len(live)} — no correction marker nearby. READ EACH.")
    print("  " + "="*74)
    for i, (eid, rel, line, ctx, _) in enumerate(live, 1):
        print(f"  {i}. [{eid}]  {rel}:{line}")
        print(f"       ...{ctx}...\n")
    if not live:
        print("     (none)\n")
    print("  " + "="*74)
    print(f"  APPARENTLY MARKED — {len(marked)} — a correction marker sits nearby, so these")
    print("  are probably the corpse being QUOTED IN ORDER TO KILL IT, which is the")
    print("  negatives-are-the-map rule working. NOT verified; the marker test is a")
    print("  heuristic and can be fooled both ways.")
    print("  " + "="*74)
    for eid, rel, line, _, _ in marked:
        print(f"     [{eid}]  {rel}:{line}")
    print()
    print("  For every hit: is the REASON still the live one? THE CLAIM BEING TRUE PROVES")
    print("  NOTHING — that is the camouflage. And a marked hit is a GUESS, not a pass.")
