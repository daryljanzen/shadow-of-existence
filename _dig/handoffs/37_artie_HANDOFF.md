# Handoff — shadow-of-existence corpus findings (for judge/incorporate node)

**Repo:** https://github.com/daryljanzen/shadow-of-existence
**Base commit studied:** `f7e03626c12643e1a5b621abb3fb88f6fadf7c38` (`r2429 — one programme: line/54 merged into main…`)
**Produced by:** an upstream study node (read P1–P9, P15, P16 at source + whole-corpus mechanical sweep).
**Your job:** judge these findings independently, then incorporate the one that is ready. Do **not** trust this
document over the source — every claim below is checkable against the repo with the scripts in §4.

There are exactly two findings. One is ready to commit. One is a question for the author and must **not** be
auto-applied.

---

## 1. CC-2 — READY TO COMMIT (mechanical, verified, high confidence)

**Defect:** Four `\bibitem` entries are empty — the citation key is present and *is* referenced by `\cite` in
the same file, but the bibliography line has no text, so the reference renders broken.

**Fix:** append the canonical entry text to each. The text is **not invented** — for each key it is attested
*verbatim* in 10–13 of the other papers' bibliographies inside this same corpus (see §4 to reproduce the count).

Each site is currently the literal line `\bibitem{KEY}` with nothing after it, immediately followed by the next
`\bibitem`. Append the text so the line becomes `\bibitem{KEY} <text>`.

| # | File | Empty key | Append this text |
|---|------|-----------|------------------|
| 1 | `corpus/slicing_operator.tex` | `JanzenGroupoid` | `D.~Janzen, \emph{The Schwarzschild--de Sitter description groupoid: generators, relations, and Schwarzschild as the asymmetric realisation}, companion paper (P5).` |
| 2 | `corpus/boundary_paper.tex` | `JanzenCircle` | `D.~Janzen, \emph{The Schwarzschild and de Sitter circle: the intrinsic geometry of one homogeneous ring---the event horizon and the curvature singularity at $r=0$ its two poles}, companion paper (P2).` |
| 3 | `corpus/CR_cosmology.tex` | `JanzenAlgebroid` | `D.~Janzen, \emph{General relativity's constraint algebra as the symmetric-space structure of a de Sitter substrate: the action Lie algebroid of the symmetry-reducible sector, and the problem of time's ``wrong sign'' as the substrate's coset signature}, companion paper (P12).` |
| 4 | `corpus/shadow_of_existence.tex` | `JanzenAlgebroid` | (same long P12 text as #3) |

**Confidence notes for the judge:**
- `JanzenGroupoid` and `JanzenCircle` fill texts are each 13× identical across the corpus — zero ambiguity.
- `JanzenAlgebroid` has three variant wordings in the wild; the **10× majority long form** above is canonical
  (a 1× short form and a 1× medium form also exist — do **not** use those). P16's own bib (`cosmogenesis_paper.tex`)
  uses exactly this long form.
- These are the **only** four empty bibitems in the entire corpus.

---

## 2. CC-1 — RAISE WITH AUTHOR, DO NOT AUTO-APPLY

**Observation:** several sites write "**finite-curvature branch point $r=0$**", which conflates two distinct
loci the corpus otherwise keeps apart:
- **r = 0** — an *infinite*-curvature locus (the P2 ring-continuation branch point). P7 §two-boundaries:
  "$r=0$ remains a genuine **infinite-curvature** locus."
- **the Nariai seam α/√3** — a *finite*-curvature locus (f = 0 = f′ double root, where the causal reassignment
  welds). P7 §general-reach: "the **finite-curvature** cosmogenesis branch point — the degenerate Nariai member."

So P7 *itself* carries both adjectives, attached to different loci. The flagged sites weld the seam's adjective
("finite-curvature") onto the r=0 label. P16 §266 even states outright that the seam-radius and the r=0 crossing
are "**two readings of one radius and not one event**."

**Sites:** `corpus/slicing_operator.tex:420`, `corpus/cosmogenesis_paper.tex:266`, `corpus/CR_cosmology.tex:1002`,
`THE_OPEN_PROBLEMS_LEDGER.md:53`; plus established load-bearing usage at `cosmogenesis_paper.tex:170` and `:62`.

**Why this is NOT a linter fix:** it is not a typo to drop a word from. It asks which locus the phrase is meant
to name, and the answer is entangled with a section (`CR_cosmology.tex:1002`) that is on the programme's live edge
(the acoustic-front / STATE frontier-1 reframe, revisions c54.16x). Deciding it wrong would corrupt physics, not
tidy wording.

**The question to route to the author (D. Janzen):** *Where "finite-curvature branch point $r=0$" appears — is
the intended referent the finite-curvature Nariai seam or the infinite-curvature r=0 locus, and is the compound
phrase "finite-curvature $r=0$" ever intended as written?* Await his call before any edit here.

---

## 3. Negative results (also verified — the corpus is otherwise clean)

Whole-corpus mechanical sweep (all `corpus/*.tex`) found:
- Cited-but-undefined bibliography keys: **0**
- Duplicate `\label` definitions: **0**
- Undefined `\ref` / `\eqref`: **0**

The corpus is mechanically pristine apart from CC-2. If you find more of these classes, the base commit differs
from the one named above — re-sync first.

---

## 4. Reproduce the verification yourself (do not take my word)

Run from repo root. **(a) empty bibitems + undefined cites:**
```python
import re, glob, os
for f in sorted(glob.glob('corpus/*.tex')):
    s=open(f,encoding='utf-8',errors='replace').read()
    cited={k.strip() for m in re.finditer(r'\\cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\{([^}]*)\}',s) for k in m.group(1).split(',') if k.strip()}
    parts=re.split(r'(\\bibitem\s*(?:\[[^\]]*\])?\{[^}]*\})',s); bib={}
    for i,p in enumerate(parts):
        mm=re.match(r'\\bibitem\s*(?:\[[^\]]*\])?\{([^}]*)\}',p)
        if mm:
            tail=re.split(r'\\end\{thebibliography\}',parts[i+1] if i+1<len(parts) else '')[0]
            bib[mm.group(1).strip()]=tail.strip()
    empty=[k for k,v in bib.items() if len(v)<3]; undef=sorted(cited-set(bib))
    if empty or undef: print(os.path.basename(f),'EMPTY',empty,'UNDEF',undef)
```
Expect exactly the four EMPTY hits above, no UNDEF.

**(b) confirm each fill text is corpus-attested (majority = canonical):**
```python
import re, glob
from collections import Counter
for key in ['JanzenGroupoid','JanzenCircle','JanzenAlgebroid']:
    c=Counter()
    for f in glob.glob('corpus/*.tex'):
        s=open(f,encoding='utf-8',errors='replace').read()
        parts=re.split(r'(\\bibitem\s*(?:\[[^\]]*\])?\{[^}]*\})',s)
        for i,p in enumerate(parts):
            mm=re.match(r'\\bibitem\s*(?:\[[^\]]*\])?\{([^}]*)\}',p)
            if mm and mm.group(1).strip()==key:
                t=' '.join(re.split(r'\\end\{thebibliography\}',parts[i+1] if i+1<len(parts) else '')[0].split())
                if len(t)>3: c[t]+=1
    print(key, c.most_common(1))
```

---

## 5. Recommended incorporation order
1. Apply **CC-2** (4 edits). Rebuild the bibliographies / recompile the affected papers; confirm no
   "undefined citation" warnings remain for those keys.
2. **Hold CC-1** as an open question tagged for the author. Do not touch those sites until adjudicated.
