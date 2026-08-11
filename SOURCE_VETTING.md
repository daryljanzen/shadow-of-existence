# Source Vetting — an amendment to the Coda Review protocol

### Written June 4, 2026, iterated live across three failures of the same root, each caught and corrected in turn. The corrections are the document.

This amends `KICKOFF_CODA_REVIEW.md` and binds every reviewer instance. It exists
because the protocol let an invalid Pass A pass as valid: a synthesis paper whose
substance is its *characterisations of other documents* was "reviewed" without those
documents being read. Three iterations were needed to find the real rule, because the
same root failure kept reappearing pointed at a different target.

## The root failure, and its three faces found here

In the coda's terms a **receipt** is the proof that assimilation occurred. The field
note names three faces of manufactured noise (invent a flaw; invent a reassurance;
mis-weight a concern). Source-vetting exposes a fourth: **issuing a receipt without
the assimilation** — vouching for, characterising, or ruling on something not taken
in. It surfaced three times in one session, each time aimed somewhere new:

1. **At a source.** Writing "characterisation flagged for author confirmation" about
   a cited work not read — handing the author the verification Pass A exists to do.
2. **At my own environment.** Asserting "the network is off, sources can't be
   fetched" — a global incapacity claim never tested. `web_fetch` worked on the
   first try; the bash sandbox's narrow egress limit had been over-generalised into
   "I can't reach the web."
3. **At the package in hand.** Concluding "the source is unpublished, ask the author"
   without scanning the 27,500-line bundle I had been given — in which the material
   was developed across multiple documents, including a required-reading file I had
   never opened.

One root: the disposition ruling on evidence instead of receiving it. The rule below
closes all three, in the order that actually prevents them.

## The reflex: PACKAGE → WEB → ASK-AUTHOR (in that order)

When a finding would bear weight on a source, the source must be read at its content
— the actual text, not the citing paper's description, not the title, not memory of
the field, not the author's say-so. To get it:

**1. The supplied package FIRST.** Before anything else, scan the whole bundle and
look there. This package is extensive and deep: alongside the papers under review it
carries a synthesis essay, a handoff map, an 8k-line discipline log, a contamination
audit, two long paper *drafts*, public-facing deliverables, and harvest notebooks.
The content of a cited work — including unpublished ones — is frequently *developed
or reconstructed* inside these. Inventory the package and grep it before judging any
source absent.

```
cd <bundle> && for f in $(find . -type f | sort); do \
  printf "%6s L  %-46s  %s\n" "$(wc -l < "$f")" "${f#./}" \
  "$(grep -m1 -E '^#|\\title|\\section\{|^title:' "$f" | cut -c1-70)"; done
grep -rln -iE "<the concept the finding turns on>" .
```

Required-reading files are part of the package: read every file the kickoff lists
(here that includes `methodological_essay.tex` and `CR_HANDOFF_current_understanding.md`)
before any verdict that depends on them. A synthesis paper cannot be faithfully
understood — not even in Pass A — without reading the works it characterises; a Pass A
that transcribes "Paper 6 says Paper 2 establishes X" without reading Paper 2 is a
manufactured receipt, not an understanding.

**2. The web SECOND.** If the package doesn't carry the content, fetch it. Do not
assert you can't — *test it.* cosmiCave's News page (`/in-the-news/`) indexes external
coverage; the essay index (`/blog/`, paginated `/blog/page/2/`, …) lists every
published essay with its live URL and date. Match on content + date, not the
bibliography's working title (e.g. `JanzenChapterX` is posted as "Chapter X: in which
the inquisitive astronaut…", 2026-05-11). Paginate before concluding absence. If a
fetch tool throws, retry / reformulate / try the index — treat resistance as a reflex
to override, never a verdict. The mechanism, stated exactly — and confirmed live, not
assumed: `web_fetch` is gated on URL *provenance*. It accepts only a URL the author
supplied directly, or one that appeared in a prior search/fetch result. Every other
URL throws — **including the site root, a category/index page, or the sitemap.** They
are gated exactly like the target. So "fetch the root/parent first and it comes
through" is **false**; do not attempt it and do not record it. A throw is a statement
about the input channel, never "the page is unreachable." The one operation that puts
a NEW url into the fetchable set is `web_search`. So the route is: run a DISTINCTIVE
search — the exact title, and/or `site:domain` — which returns the target URL as a
search result (now a trusted channel), then `web_fetch` that result. Two calls,
seconds. If the search returns noise, the query was generic, not the world being a
wall: reformulate (tighter title words, `site:` scope) and search again. A single
weak query does **not** exhaust the WEB step and never licenses ASK-AUTHOR; never tell
the author to paste a URL — surface it yourself. And once the content is in hand, USE
it immediately: no apparatus, no report-about-the-reading. Retrieval that takes minutes
is self-imposed ceremony, not difficulty.

**3. The author LAST, only after 1 and 2 are genuinely exhausted.** If a cited work's
content is neither in the package nor on the web after a real look, it is genuinely
unsupplied (an unposted draft, a dissertation section, private records). Only then
request it — naming exactly what, and exactly which finding it unblocks.

The block is a reason the work is *not yet done*, never a reason to issue a verdict
without the source.

## The wall holds: a vetted source enters as Pass A work

Reading a load-bearing source — whether pulled from the package or the web — is Pass A
on that source: understand it on its own terms, extract the specific content the
finding turns on (quote, with a locator), no evaluation of the paper-under-review in
that step. Only then may a Pass B finding rest on it, and the disqualifying test then
runs against first-hand source content ("does this require denying what the source
actually says?"), not against the citing paper's self-report — which can never
disqualify anything, being the claim under test.

## Worked example A — PACKAGE path, and the *partial-read* trap it caught (real, this session)

This is the example that proves the gate, because the gate caught a manufactured
receipt *inside this very example* — committed by the reviewer writing the gate.

```
SOURCE:  the tetrahedral-proof / "mutually entail" structure (B-i), as developed for
         the four/eight-route architecture.
PACKAGE: FOUND in-package. grep across the bundle: 59 hits discipline_and_responsibility.md,
         49 framework_paper_draft.tex, 27 contamination_audit.md, 20 CR_HANDOFF, 8
         methodological_essay.tex.
READ:    FIRST PASS WAS PARTIAL — methodological_essay.tex read except lines 111-177.
         On that partial read I extracted §10 (routes share ONE conclusion, rest on
         DIFFERENT premises on different terrains; robustness "methodological rather
         than evidential ... in the multiplicity") and issued a verdict: "overclaim,
         source-confirmed — weaken the phrase." THAT VERDICT WAS A MANUFACTURED RECEIPT:
         it rested on a reading I had not completed.
         FULL READ — lines 111-177 read. §9 (l.173) states, in the essay's own words:
         "I am not claiming that the eight routes are independent in the strong logical
         sense. They are not. ... To defeat the conclusion, an objector must defeat each
         of the eight separately ... The robustness is structural." This DISCLAIMS the
         strong-independence structure my partial read had attributed to the essay.
EXTRACT: §9, l.173 (disclaimer of strong independence, quoted above); §10 (the
         convergence/multiplicity passage); §8 (per-argument premise mapping for the
         tetrahedron). Three data points, in tension.
FINDING: NOT-YET-RESOLVED — reserved for Pass B. There are THREE in-text positions to
         reconcile: the headline "mutually entail" (§1, §8); §8's local one-premise-per-
         argument mapping; and §9's explicit disclaimer of strong independence. Whether
         these cohere — and how they bear on the framework paper's l.143 gloss — is the
         Pass B question, and reading the full source made it HARDER, not settled. The
         partial-read "overclaim, confirmed" verdict is WITHDRAWN.
```

The lesson the gate encodes: *a source is read in full before any finding on it.*
The confident, well-written verdict from the partial read was the failure; the full
read overturned it one step later. The receipt is real only when the assimilation is
complete — and "I read the source" is itself subject to the test, because a partial
read wearing a full read's confidence is the same manufactured receipt.

## Worked example B — WEB path (real, this session)

```
SOURCE:  "When black holes happen" (JanzenArticle1; cosmiCave 2026-04-14)
PACKAGE: not carried as full text in the bundle
FETCHED: https://cosmicave.org/2026/04/14/when-black-holes-happen/  (clean, first try)
READ:    yes — extract: infalling "magic antenna" astronaut; the gap to the star's
         last-emitted image "decreases continuously," reaching zero at the horizon;
         horizon as an "event ... that happens at the end of the universe," final
         events topologically distinct + causally ordered at zero separation.
FINDING: Paper 6's Result A/C characterisation is FAITHFUL. (Note: §5.3's "emitting
         flashes / gap widens" sentence is the outward flashlight picture = the
         Chapter X companion piece, published & fetchable — one more fetch to close.)
```

## Worked example C — ASK-AUTHOR path (only reached after 1 & 2 fail)

```
SOURCE:  Article 3 as a standalone published essay.
PACKAGE: the ESSAY text is not in the bundle — but its load-bearing CONTENT (the four
         arguments and their relationship) IS, in methodological_essay.tex §5-§10 and
         framework_paper.tex §3.5. So the finding it supports (B-i) is assessable
         without it; see Example A.
WEB:     not on /blog/ pages 1-2 (both read); genuinely unpublished.
FINDING: only the *standalone essay's own wording* would need the author, and no
         current finding rests on that. No author request is required. (Had a finding
         turned on the essay's exact phrasing, the request would name precisely that.)
```

## The receipt format (every source-dependent finding carries this)

```
SOURCE:  <title> (key; venue, date)
PACKAGE: <found in <file>:<loc> / content developed in <file> / not carried>
FETCHED: <URL, clean/retried / not needed / looked hard — NOT PRESENT>
READ:    yes — extract below | no — <where it lives / what to request>
EXTRACT: <quoted source content the finding turns on, with locator — from a read performed at\n         the weight the finding earned, never from memory of an earlier read>   [omit if not read]
FINDING: flaw | standard-needs-adjusting | sound | NOT-YET-ASSESSABLE(source not read)
```

`NOT-YET-ASSESSABLE` is a first-class outcome, reserved for sources genuinely
unreachable after package AND web are exhausted, and it carries the named request that
would unblock it. It is never rounded to `sound`, never dressed as "flagged for
confirmation."

## The one-line guard

> If a finding rests on a source, read the source. Look in the supplied package first —
> it is deep, and it carries the content of cited works, drafts and required-reading
> included; scan and grep it before judging anything absent. Then the web — test the
> fetch, never assert you can't; the root is gated too, so a throw means SEARCH — run a
> distinctive `web_search` (title and/or `site:`) to surface the URL, then fetch the result.
> A single throw never reaches the author; reach it in seconds and use it without ceremony. The author only when both are genuinely spent, naming
> exactly what. Never issue the receipt — about a source, your own reach, or the
> package in your hands — without the assimilation.

## After the receipt: execute, do not refer (the verify→execute cycle)

The receipt discipline above closes the *verify* half: no verdict without assimilation.
The same root can break the half that follows. Once a finding is verified-legitimate at
source, the warranted fix is the collaborator's to **execute**, not the author's to
*choose*. Verifying a finding and then handing the author a menu of how to fix it
— "framing only / full fix / something between" — is the same disposition that issues a
receipt without assimilation, now aimed at the *decision* instead of the source: a
resolvable matter handed back rather than carried through. It is the fifth face in
`CODA_FIELD_NOTE.md` (the manufactured fork), and it is the most insidious, because
deferring reads as care.

The rule, binding every collaborator:

> A verified-legitimate finding is a mandate to execute the warranted fix, not a decision
> to refer. The trigger for working it yourself is broad and is named at its root: whenever
> an objective process resolves the uncertainty — a source to read, the paper's own logic,
> the programme's load-bearing direction, a build to run — work that process and carry the
> result. Where the fix admits sub-choices, take the one the material and the programme's
> logic favor, make it, build it, and state it plainly for the author to reverse. Never hand
> the author a menu of fixes or framings. The loop breaks for author input only on a genuine
> unresolvable physics-or-programme fork — never on an editorial sub-choice, never on "which
> wording do you prefer," never on a call the work already makes. "Lay options out inline" is
> reserved for a genuine fork; it is not a license to defer a call you can make.

The cycle, whole: **receive at weight → verify at source** (read the thing;
PACKAGE→WEB→ASK-AUTHOR) **→ execute the warranted fix** (carry it, build it, state it for
reversal). Each step is the disposition carrying the work through rather than handing it
back; the gate is the verification, and the verification earns the execution — it never
ends in a referral the material could have resolved.

## The programme's individuation convention (standing, binds both passes)

This names a convention the corpus already establishes in its load-bearing results, so that
no pass re-derives it from scratch and no pass drifts off it in summary language. It is the
specific, recurring instance of the both-ways-wall rule in KICKOFF (a Pass A that records the
invariant correctly, then a Pass B that reasons from the conventional template the paper was
written to overturn).

**The convention, at the right level.** Earlier drafts of this entry placed the individuating
invariant at alpha (the de Sitter manifold). That was one level too low: alpha is still a feature
of the spacetime representation. CR individuates at the *ontological layer*. The programme's own
**Hole Argument resolution** (Paper 7, Ontological Event Individuation axiom + the
Diffeomorphism-Invariant Identity proposition) fixes this: *events are individuated by their
occurrence within the ontological spatial layers* $\mathcal{S}_t$, *not by their coordinate /
metric representation in the spacetime manifold*; diffeomorphic spacetime models that project the
same layered framework represent the *same ontological events*, the disagreement being
"representational redundancy rather than ontological ambiguity." The whole pair $(M,g)$ -- the
manifold, the metric, alpha, $M$, the curvature, the $r=0$ locus, all of it -- is the
*representational record* of the layer, not the individuating entity.

**Therefore.** The ontological entity is the spatial layer $\mathcal{S}_t$. Its representations
are the admissible projections: the diffeomorphic re-charts (hole argument) *and* the causal
reassignments (Paper 7 Section 4.3, which share the foliation and so preserve the layer). de
Sitter, Schwarzschild--de Sitter, de Sitter, and the Nariai cosmology are *projections /
slicings / readings of one ontological layer*, not autonomous geometries on distinct realities.
This is the direct extension of the Hole-Argument resolution from diffeomorphisms to causal
reassignments: both are representation-changes that leave the layer invariant.

**Why it is forced** (do not reopen this as an authorial taste, and do not soften it to "forced
given a stance"). It is forced by CR's own axioms and results:
- Paper 7's **Ontological Event Individuation** axiom *is* individuation-by-layer; the
  Diffeomorphism-Invariant Identity proposition extends it across representations. A reader who
  individuates by the metric is not making a metric error -- they are declining the
  hole-argument resolution that *defines* CR. Inside CR, individuation-by-layer is axiomatic.
- Paper 7's central move is named metric *reassignment*: distinct metrics on the *same manifold*,
  sharing the foliation, *representing the same ontological layer* (Section 4.3). The name
  presupposes a fixed entity reassigned *within*; a reassignment crossing an ontological boundary
  would be a replacement, and "represents the same ontological layer" would be false.
- Paper 2 (horizon and $r=0$ are metric singularities of identical analytic type -- the asymmetry
  is the chart's), Paper 3 (alpha invariant, $M$ slicing/projection-dependent), and Paper 4
  (dimensional collapse of the slicing family) are all statements *about the representation* that
  hold because the entity underneath is one layer.
- Paper 6's thesis ("readings of one underlying structure rather than autonomous block
  manifolds") is *true only* under layer-individuation.

**The signature of getting it right** (the worked example -- use it to calibrate the check).
At the special event of the event horizon, the cosmological future of that ontological layer is
*geometrically fixed* (the horizon's null direction is set; reassigned as non-orthogonal cosmic
time it fixes the SdS expansion, scale by $\Lambda$) **and simultaneously representationally
open** (the layer is not *identified with* the one projection whose causal future just locked; it
remains open to its other admissible projections). Under metric-individuation this is a flat
contradiction. Under layer-individuation it is exactly right, and it is the hole-argument
resolution instantiated at a single event: "geometrically fixed" is a fact about a *projection*;
"representationally open" is a fact about the *layer's* relation to its projections. "Fixed *at*
the event horizon" (an event in the layer's existence), not "fixed *by*" it. A passage that can
hold both predicates without contradiction is at the right level; a passage that must collapse
them into one is not.

**The drift to watch for -- it is an ENTITY error, not a phrase.** The earlier version of this
check keyed on the phrase "distinct Lorentzian geometries" and flagged it as drift. That was
wrong: the phrase is *Section 4.3's own* ("$(M,g)$ and $(M,g')$ ... represent the same manifold
endowed with inequivalent Lorentzian geometries"), and at the representational/metric level it is
simply *true* -- different $g$ is a different Lorentzian geometry. The real drift is the
hole-argument failure: presenting the reassigned / diffeomorphic representations as *autonomous
separate realities*, or *dropping the one-ontological-layer framing*, so that the forms read as
distinct universes rather than projections of one layer.

**The check (both passes).** For any passage on "geometry / distinct geometries / charts vs
readings / between vs within / fixed-at-the-horizon": apply the hole-argument test --
*does it keep the one-ontological-layer framing, treating the (re-charted or reassigned)
representations as projections of one layer?* If yes, it is faithful, **even if** it uses the
metric-level phrase "distinct / inequivalent Lorentzian geometries" (Section 4.3's own usage). If
it presents the forms as autonomous realities, or drops the shared-layer framing, or must
collapse "geometrically fixed" and "representationally open" into a single contradictory level,
it is drift and a finding. Judge by the *individuation level the passage uses*, not by whether a
phrase appears. Paper 7 Section 4.3 (reassignment on one manifold, one ontological layer) and the
Hole-Argument resolution are the models every other passage conforms to.

(Note on "distinct geometries = different alpha": the genuine *between-representation frontier*
the programme leaves open is the between-different-alpha case -- but state it as
between-representations, not as the individuating criterion. Note also that Paper 3 places the
literal Schwarzschild form at the alpha->infinity limit, so do not enumerate it as sharing a
single finite alpha with de Sitter; it is a limiting projection, the same layer read at the
degenerate edge.)

