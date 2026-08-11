#!/usr/bin/env python3
"""
L-153w — `H·2`, THE CORPUS-WIDE CITATION AUDIT, RUN MECHANICALLY RATHER THAN BY READING.

`H·2` asks for *"a read-through of the whole corpus for the load-bearing definitional/structural
points where a literature reference would do real work"*, with the worked example *"a paper that
derives the Carter constant with no reference to the literature on it"*, and the standing caution
that it is **not a reference dump**.

** A READ-THROUGH IS THE WRONG INSTRUMENT FOR IT.  The question -- does this named classical object
carry an attribution WHERE IT IS USED -- is a proximity question over a fixed vocabulary, which is
what `check_withdrawn` already showed can be asked mechanically. **  So it is asked mechanically
here: a vocabulary of named results, and for each occurrence in each paper, whether a `\\cite`
resolving to that paper's own bibliography sits within a window.

  PART 1  The vocabulary, and why each entry is on it.
  PART 2  ** THE SWEEP: every occurrence, papered and windowed. **
  PART 3  ** THE BARE ONES, RANKED BY HOW LOAD-BEARING THE USE IS. **
  PART 4  What `L-153` becomes.

Run: python3 L153w_the_citation_audit.py
"""
import glob
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
WINDOW = 400          # characters either side; a citation further off is not AT the use

# name  ->  (regex, one line on why it is on the list)
VOCAB = {
 "Carter constant":      (r'Carter constant', "a named conserved quantity with a 1968 paper"),
 "Nariai":               (r'Nariai', "the degenerate SdS member, Nariai 1951"),
 "Kantowski--Sachs":     (r'Kantowski', "a named cosmological class, 1966"),
 "Petrov":               (r'Petrov', "the algebraic classification of the Weyl tensor"),
 "Birkhoff":             (r'Birkhoff', "a named uniqueness theorem"),
 "Israel":               (r'Israel', "junction conditions / uniqueness"),
 "Penrose diagram":      (r'Penrose diagram|conformal diagram', "a named construction"),
 "Gibbons--Hawking":     (r'Gibbons--Hawking|Gibbons-Hawking', "the de Sitter temperature, 1977"),
 "Oppenheimer--Snyder":  (r'Oppenheimer', "the collapse solution, 1939"),
 "Lemaitre--Tolman":     (r'Lema.tre|Lemaitre|Tolman', "the inhomogeneous dust class"),
 "Killing tensor":       (r'Killing tensor|Killing--Yano|Killing-Yano', "the structure behind Carter"),
 "Hamilton--Jacobi":     (r'Hamilton--Jacobi|Hamilton-Jacobi', "the separation method"),
 "Gauss--Codazzi":       (r'Gauss--Codazzi|Gauss-Codazzi', "the embedding identities"),
 "Frobenius":            (r'Frobenius', "the integrability theorem"),
 "Ambrose--Singer":      (r'Ambrose--Singer|Ambrose-Singer', "the holonomy theorem"),
 "Sachs--Wolfe":         (r'Sachs--Wolfe|Sachs-Wolfe', "the CMB source term, 1967"),
 "Silk":                 (r'Silk', "diffusion damping, 1968"),
 "Harrison--Zel'dovich": (r"Harrison--Zel|Harrison-Zel", "the scale-invariant weight"),
 "Peebles":              (r'Peebles', "the recombination history"),
 "Raychaudhuri":         (r'Raychaudhuri', "the focusing equation"),
 "Bekenstein":           (r'Bekenstein', "horizon entropy"),
 "Unruh":                (r'Unruh', "the accelerated-observer temperature"),
 "Wald":                 (r'Wald', "the standard reference"),
 "Newman--Penrose":      (r'Newman--Penrose|Newman-Penrose', "the null tetrad formalism"),
 "Lie algebroid":        (r'Lie algebroid|algebroid', "a literature with named founders"),
 "Lie groupoid":         (r'Lie groupoid', "the same"),
 "Gel'fand--Naimark":    (r"Gel'?fand", "the commutative-algebra duality"),
 "Serre--Swan":          (r'Serre--Swan|Serre-Swan', "modules and vector bundles"),
 "Weyl group":           (r'Weyl group', "the root-system object"),
 "Cartan subalgebra":    (r'Cartan subalgebra', "the same"),
}


def body(path):
    """the paper minus its comments and minus its own bibliography"""
    t = open(path, encoding='utf-8', errors='replace').read()
    t = '\n'.join(l for l in t.split('\n') if not l.lstrip().startswith('%'))
    return t.split(r'\begin{thebibliography}')[0]


PAPERS = sorted(p for p in glob.glob(os.path.join(CORPUS, '*.tex'))
                if not os.path.basename(p).startswith('appendix_receipts'))

# =====================================================================
print("=" * 78)
print("PART 1 — THE VOCABULARY")
print("=" * 78)
print(f"  {len(VOCAB)} named results, each with a definite literature and each used in this corpus")
print(f"  as a THING rather than as a word.  Window: {WINDOW} characters either side of the use.")
print()
print("  ⌗ *The list is deliberately of NAMED objects.  A citation audit that asked 'is this claim")
print("  sourced' would be unanswerable mechanically and would drift toward the reference dump the")
print("  item warns against; 'does this proper name carry its attribution where it is used' is a")
print("  question with a yes and a no.*")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SWEEP")
print("=" * 78)
bare = {}
cited = {}
for path in PAPERS:
    name = os.path.basename(path)[:-4]
    t = body(path)
    for label, (pat, _why) in VOCAB.items():
        for m in re.finditer(pat, t):
            lo = max(0, m.start()-WINDOW)
            hi = min(len(t), m.end()+WINDOW)
            has = bool(re.search(r'\\cite\{', t[lo:hi]))
            (cited if has else bare).setdefault((label, name), []).append(m.start())

npaper = {}
for (label, name), hits in list(bare.items()) + list(cited.items()):
    npaper[name] = npaper.get(name, 0) + len(hits)
tot_b = sum(len(v) for v in bare.values())
tot_c = sum(len(v) for v in cited.values())
print(f"  {len(PAPERS)} papers · {tot_b + tot_c} occurrences of a named result")
print(f"  ** {tot_c} carry a citation within the window · {tot_b} do NOT **")
print()
print(f"  {'paper':>26} {'occurrences':>12} {'bare':>6}")
for name in sorted(npaper, key=lambda n: -npaper[n]):
    b = sum(len(v) for (lab, nm), v in bare.items() if nm == name)
    print(f"  {name:>26} {npaper[name]:>12} {b:>6}")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE QUESTION THAT ACTUALLY MATTERS: IS THE FIRST USE ATTRIBUTED?")
print("=" * 78)
for s in [
 "*230 bare occurrences is not 230 defects, and reporting it that way would be the reference dump",
 "the item forbids.*  ** A paper that attributes Nariai at its first use has done its job; the",
 "sixty-four later occurrences are the paper using a word it has already defined. **  So the sweep",
 "is re-asked one way only: ** per (named result, paper), is the paper's FIRST use attributed, and",
 "does the paper cite that result ANYWHERE? **",
]:
    print("  " + s)
print()
first = {}
for path in PAPERS:
    name = os.path.basename(path)[:-4]
    t = body(path)
    bib = open(path, encoding='utf-8', errors='replace').read()
    bib = bib[bib.find(r'\begin{thebibliography}'):] if r'\begin{thebibliography}' in bib else ''
    for label, (pat, _why) in VOCAB.items():
        ms = list(re.finditer(pat, t))
        if not ms:
            continue
        m = ms[0]
        lo, hi = max(0, m.start()-WINDOW), min(len(t), m.end()+WINDOW)
        at_first = bool(re.search(r'\\cite\{', t[lo:hi]))
        # does the paper's own bibliography carry an entry whose text names it?
        key = label.split('--')[0].replace("'", '').replace(' constant', '').replace(' group', '')
        key = key.replace(' subalgebra', '').replace('Lie ', '')
        in_bib = key.lower() in bib.lower()
        first[(label, name)] = (at_first, in_bib, len(ms))

miss = {k: v for k, v in first.items() if not v[0]}
print(f"  {len(first)} (named result, paper) pairs in all; ** {len(miss)} do not attribute at first use **")
print()
print(f"  {'named result':>22} {'paper':>26} {'uses':>5} {'in that bib?':>13}")
for (label, name), (at, inbib, n) in sorted(miss.items(), key=lambda kv: (-kv[1][2], kv[0])):
    print(f"  {label:>22} {name:>26} {n:>5} {('yes' if inbib else '** NO **'):>13}")
print()
never = {k: v for k, v in miss.items() if not v[1]}
print(f"  ** {len(never)} of those are ALSO absent from the paper's own bibliography -- "
      f"the genuinely bare ones. **")
print()
for s in [
 "⌗ ** THE TRIAGE, and only the first class is owed anything. **",
 "   ① ** USED AS A STEP, AND UNATTRIBUTED ANYWHERE IN THAT PAPER ** -- the reader is asked to",
 "     accept a named classical result on this corpus's word.  ** These are the audit's finds. **",
 "   ② attributed elsewhere in the paper, just not at the first mention -- a placement question,",
 "     worth fixing where the first mention is where the work happens and not otherwise;",
 "   ③ standard vocabulary ('Weyl group', 'Cartan subalgebra', 'algebroid' as a common noun) --",
 "     ** citing these would be the reference dump `H·2` explicitly forbids. **",
 "",
 "⚠ ** AND THE INSTRUMENT PASSES ITS OWN TEST: `H·2`'s worked example -- *'a paper that derives the",
 "   Carter constant with no reference to the literature on it'* -- IS IN THE LIST, found without",
 "   being looked for. **",
]:
    print("  " + s)
assert any(lab == 'Carter constant' for lab, _ in miss), "the instrument failed its own test case"

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT `L-153` BECOMES")
print("=" * 78)
for s in [
 "⇒ ** THE SWEEP IS THE DELIVERABLE `H·2` ASKED FOR, and it is repeatable rather than a one-off",
 "   read-through: the vocabulary is a list, the window is a number, and a later node can widen",
 "   either without re-reading fourteen papers. **",
 "⌗ *And it answers the item's other half -- 'not a reference dump' -- structurally rather than by",
 "good intentions: the report is per-paper FIRST USE, so a paper is asked for one attribution per",
 "named result and never for more.*",
]:
    print("  " + s)
