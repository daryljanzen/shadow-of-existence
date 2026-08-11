#!/usr/bin/env python3
"""check_withdrawn.py -- the NINTH gate, and it exists because the same failure happened twice
in the one place nobody looks.

** THE FAILURE. **  At c54.31 the matter sector withdrew the identification of a generation with
a hinge/wall: the walls' S_3 is a WITHIN-STATE index and the generations' own threeness is the
turnaround's deck Z_3.  At c54.60 a sweep propagated that to five companion papers.  At c54.86
the frontier audit found it still live in two places the sweep never looked:

  * P14's OWN ABSTRACT -- asserting the identification that P14's own section is titled after
    denying ("Which three the generations are seated on, and why it is not the hinges");
  * P7's frontier item 5 -- which STATES the revision and then, three sentences later, restates
    the withdrawn reading as current, so the paragraph contradicted itself.

** THE PATTERN, WHICH IS THE POINT. **  A result lands in the section that produced it and does
not reach the places that SUMMARISE -- abstracts, frontier lists, synthesis sections.  Those are
exactly where a reader goes first and exactly where a working node edits last.  The c54.60 sweep
fixed five bodies and no summaries.

** WHAT THIS GATE DOES. **  It carries a REGISTRY of withdrawn claims, each a phrase pattern plus
the markers that count as an adjacent correction.  A paper may still contain a withdrawn claim's
wording -- the corpus routinely quotes what it withdrew, and that is honest -- but only if a
revision marker follows within WINDOW characters.  A bare occurrence is a FAILURE.

** ADDING TO THE REGISTRY IS PART OF WITHDRAWING SOMETHING. **  When the corpus withdraws an
identification, the withdrawal is not finished until its phrase is registered here; otherwise the
next summary that quotes the old reading is invisible again.

Run it after any withdrawal, and in the standing gate sweep.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WINDOW = 900          # characters after a hit in which a correction still counts as adjacent

# --- THE REGISTRY -------------------------------------------------------------------------
# (label, phrase pattern, marker pattern, when and where it was withdrawn)
REGISTRY = [
    ("generations-are-the-hinges",
     r'(three generations one object read three ways'
     r'|the generations are \\emph\{one object read three ways\}'
     r'|which wall each binds at'
     r'|a generation (?:per|at each) (?:hinge|wall)'
     r'|family \$S_3\$|family S₃|the family \$S_\{?3\}?\$'
     # both word orders: the map writes "an S_3 family symmetry", the papers "the family S_3"
     r'|\$?S_?\{?3\}?\$? famil(?:y|ies)'
     r'|generations? via \$?S_?\{?3\}?\$?)',
     r'(has since been revised|withdraw|follows the revision|not the hinges|within-state'
     r'|turnaround\'?s deck|the within-state index|STALE|struck r\d+|superseded)',
     "withdrawn r2376+c54.31 by P14 sec:whichthree; propagated c54.60, c54.86"),
    # r2376+c54.105.  The binding-energy naturalness argument for the inherited radiation
    # amplitude.  Written from the CLAIM and not from the sentence, per THE_BASE_RATE's third
    # entry: the noun phrase alone, both word orders, and the contrast it was drawn against.
    # r2376+c54.149-150, registered c54.151.  THE FULL-LAP FLOQUET APPARATUS and every verdict
    # resting on it.  c54.143-148 propagated the progenitor from the closed ball's own a=0,
    # composed with the monodromy, and read a periodic map off the result -- attractors,
    # instability bands, a per-cycle multiplier, two exclusions of "the chain," a 420-mode comb.
    # c54.149 withdrew it (the construction supplies no such background); c54.150 declined to
    # reinstate it (the basis identification is unestablished either way).  ** THE WITHDRAWAL WAS
    # NOT REGISTERED HERE FOR TWO REVISIONS, AND IN THAT WINDOW THE_WORK CARRIED THREE OF ITS FOUR
    # AFFECTED CLOSURE ROWS AS STANDING RESULTS.  THE_BASE_RATE's fourteenth entry. **
    ("the-full-lap-floquet-apparatus",
     r'(\\lvert\\lambda\\rvert\s*=\s*1'
     r'|\|\\lambda\|\s*=\s*1'
     r'|\|lambda\|\^?2?\s*=\s*1'
     r'|per-cycle (?:amplification|multiplier|map)'
     r'|full-cycle map'
     r'|instability bands?'
     r'|stability bands?'
     r'|the transfer is unity'
     r'|cosmogenesis is not a chain'
     r'|the chain is excluded'
     r'|the comb (?:is|as) a prediction'
     r'|a complete cycle with a branch point at each end'
     r'|across a full cycle'
     r'|the cyclic structure of the excursion'
     r'|the output of the previous branch point)',
     r'(withdraw|WITHDRAWN|not reinstated|struck|STRUCK|c54\.149|c54\.150|c54\.151'
     r'|wrong background|no such object|no such epoch|does not hold|not established'
     r'|is not restored|stand withdrawn|the construction has no such)',
     "withdrawn r2376+c54.149, not reinstated c54.150; registered c54.151"),
    # r2376+c54.143, registered c54.151.  THE FIVE COMPOSITION UPPER BOUNDS and the spectral
    # KNEE they all turned on.  c54.132/133/138/141 bounded rho_r/rho_m from the observed
    # spectrum's flatness; four asked where the knee SITS rather than what curvature it leaves
    # where the spectrum is measured, and the fifth assumed the incoming perturbation is a free
    # oscillation.  ** The withdrawal stands; its GROUND has moved.  c54.143 argued from a
    # full-cycle attractor, which is itself withdrawn (see the entry above).  What survives is
    # that the construction SPECIFIES the incoming state -- an overdensity in a universe like
    # ours carries a processed adiabatic spectrum -- so it was never free to idealise. **
    ("the-leaked-branch-knee-and-the-five-composition-bounds",
     r'(the spectrum acquires a knee'
     r'|so that the spectrum has a knee'
     r'|bounds the progenitor\'s radiation fraction'
     r'|the progenitor\'s radiation fraction is (?:now )?bounded'
     r'|BOUNDED FROM BOTH SIDES'
     r'|the crossover to lie beyond it'
     r'|the observed spectrum bounds the (?:parent|progenitor))',
     r'(withdraw|WITHDRAWN|struck|STRUCK|c54\.14[13]|c54\.15[01]'
     r'|not a bound but a determination|is a determination|does not establish'
     r'|no bound (?:follows|exists)|an order of magnitude with a stated assumption)',
     "withdrawn r2376+c54.143 (five bounds); the ground itself revised c54.149-151; registered c54.151"),

    # r2376+c54.150, registered c54.151.  c54.149's OWN GROUND for calling the full lap
    # unphysical -- that the progenitor separated from its ambient expansion, so its past a = 0
    # is algebra rather than history.  ** In the standard spherical-collapse description the
    # patch's a = 0 IS the background's, at the same cosmic time; the separation is a late
    # feature of a history that starts with the ambient universe's.  So the apparatus is not
    # reinstated and this ground is not available either: what the two revisions bracket is the
    # unposed question about the construction's recursion. **
    ("the-full-lap-is-unphysical-because-the-ball-separated",
     r'(its past \$?a\s*=\s*0\$? is a mathematical extension'
     r'|not an epoch it lived through'
     r'|there is (?:no|only one) periodic map'
     r'|the ball separated, turned around and collapsed'
     r'|extending the closed-dust solution back(?:wards)? to \$?a\s*=\s*0\$? is)',
     r'(withdraw|WITHDRAWN|struck|STRUCK|c54\.150|c54\.151|spherical collapse'
     r'|the ambient universe\'s own beginning|the background\'s \$?a\s*=\s*0'
     r'|does not hold|too confident)',
     "withdrawn r2376+c54.150 (c54.149's ground, not the withdrawal it supported); registered c54.151"),

    # r2376+c54.146, registered c54.151.  THE SCALAR MONODROMY AS 2 pi/rho.  c54.131 computed the
    # crunch off-diagonal on z ~ a and the corpus carried the result for the scalar sector; the
    # true hydrodynamical variable z_S = a(a + 2B/3)/a' doubles it to 4 pi/rho.  ** 2 pi/rho is
    # CORRECT for tensors (z_T = a M_Pl/2 exactly, any content), so this pattern is written to
    # fire only where the sector is not named -- a correct statement of the value always says
    # 'tensor', or states the doubling, within the window. **
    ("the-monodromy-is-two-pi-over-rho-for-scalars",
     r'(the mixing is \$?2\\?pi ?[i]?/?\\?rho'
     r'|the mixing is 2 ?pi ?/ ?rho'
     r'|off-diagonal (?:is )?\$?-?2\\pi i/\\rho'
     r'|monodromy (?:is|of) \$?-?2\\pi i?/\\rho)',
     r'(tensor|4\\pi|4 ?pi|twice the tensor|doubl|z_T|z_\{?T\}?|scalar off-diagonal'
     r'|withdraw|WITHDRAWN|c54\.146|c54\.151)',
     "corrected r2376+c54.146: 2 pi/rho is the TENSOR value; the scalar is 4 pi/rho; registered c54.151"),

    ("radiation-of-order-the-matter-density-is-natural",
     r'(radiation of order the matter density'
     r'|of order the matter density is the natural'
     r'|matter density is the natural scale'
     r'|order unity,? (?:and )?not the small tuned value'
     r'|the small tuned value \\?\$?\\eta\\?\$? takes'
     r'|a handover carrying radiation of order)',
     r'(should be withdrawn|withdrawn|it is tempting to read|runs the other way'
     r'|no head start|superseded|struck r\d+|does not support|nine orders)',
     "withdrawn r2376+c54.105 by P15 sec:tensions: rho_r = rho_m at T ~ 0.8 eV, nine orders below "
     "the handover; O(1) there would mean eta ~ 0.5.  The corrected accounting is in P15 and P7."),
]

SKIP = ('appendix_receipts',)

# --- SECOND SCOPE, added the same revision it was needed -------------------------------------
# The gate began by scanning the PAPERS.  Run on the standing registers it immediately found the
# same withdrawn claim live in five forward-facing documents -- so a withdrawal that reaches the
# papers and not the registers is the failure one layer over, and the registers are what a
# working node reads to decide what to do next.
#
# HISTORICAL documents are exempt BY NAME and only by name: a fork record or a build ledger is a
# record of what was believed at the time, and rewriting it would destroy the record.  Everything
# else is forward-facing and must carry its correction.
REGISTER_DIR = os.path.abspath(os.path.join(HERE, '..'))
HISTORICAL = {
    'FORK_c54.md',                 # the fork's own running record
    'PHASE7_BUILD_LEDGER.md',      # a build ledger: what was believed while building
    'THE_LIVE_ARC.md',             # the arc records the withdrawal and its history
    'THE_BASE_RATE.md',            # the failure ledger, which must quote the failures
    'CORPUS_MAP.md',               # a map of the corpus's own text, quoting it
    'THE_FERMION_SECTOR_GEOMETRY.md',   # states the conflict that produced the withdrawal
    'MATTER_SECTOR_germ.md',       # the sector's germ: what was believed when it was seeded
    'THE_ARSENAL.md',              # a worked-items record
    'THE_RECEIPT_AUDIT.md',        # an audit of receipts as they stood
    'A5_fermion_sector_build.md',  # a build record: what was believed while the sector was built
}


# --- THE SELF-TEST, added r2376+c54.151 --------------------------------------------------------
# ** A GATE THAT HAS NEVER FAILED IS NOT EVIDENCE THAT IT WORKS. **  Three of the six registry
# entries below were added after the claims had already been struck from the corpus, so on the
# current tree they match nothing -- and a pattern that matches nothing is indistinguishable from
# a pattern that is broken.  Each entry therefore carries a KNOWN-POSITIVE string, taken verbatim
# from the text the withdrawal removed, and this gate fails if any pattern stops matching its own.
POSITIVES = {
    "generations-are-the-hinges": [
        "the generations are \\emph{one object read three ways}",
        "a generation per hinge",
    ],
    "the-full-lap-floquet-apparatus": [
        "the per-cycle map is a Floquet problem",
        "every physical mode lies in a stability band and $|\\lambda|=1$ to machine precision",
        "because the interior is a complete cycle with a branch point at each end",
        "Propagating the Frobenius basis across a full cycle",
        "here the cyclic structure of the excursion",
    ],
    "the-leaked-branch-knee-and-the-five-composition-bounds": [
        "so that the spectrum acquires a knee",
        "which bounds the progenitor's radiation fraction at maximum expansion",
        "THE PROGENITOR'S RADIATION FRACTION IS NOW BOUNDED FROM BOTH SIDES",
    ],
    "the-full-lap-is-unphysical-because-the-ball-separated": [
        "Its past $a=0$ is a mathematical extension of the closed-dust solution "
        "backwards, not an epoch it lived through.",
        "with one branch point there is no periodic map",
    ],
    "the-monodromy-is-two-pi-over-rho-for-scalars": [
        "the mixing is 2 pi / rho, and it is discontinuous at zero radiation",
        "the resulting monodromy is unipotent with off-diagonal $-2\\pi i/\\rho$",
    ],
    "radiation-of-order-the-matter-density-is-natural": [
        "radiation of order the matter density",
    ],
}


def selftest():
    """Every registered pattern must still match the text its withdrawal removed."""
    bad = []
    for label, phrase, _marker, _prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        cases = POSITIVES.get(label)
        if not cases:
            bad.append((label, "<no known-positive registered>"))
            continue
        for c in cases:
            if not pat.search(c):
                bad.append((label, c))
    print(f"  SELF-TEST -- {sum(len(v) for v in POSITIVES.values())} known-positive string(s) "
          f"across {len(REGISTRY)} registered withdrawal(s)")
    if bad:
        print("  ⛔ A REGISTERED PATTERN NO LONGER MATCHES THE TEXT IT WAS WRITTEN FOR:")
        for label, c in bad:
            print(f"     [{label}] {c[:100]}")
        print()
        return 1
    print("  every pattern still fires on its own known-positive.")
    print()
    return 0


def strip_comments(text):
    return '\n'.join(l for l in text.split('\n') if not l.lstrip().startswith('%'))


def main():
    texs = [t for t in sorted(glob.glob(os.path.join(HERE, '*.tex')))
            if not any(k in os.path.basename(t) for k in SKIP)]
    print()
    print(f"  WITHDRAWN-CLAIM SCAN -- {len(REGISTRY)} registered withdrawal(s) "
          f"x {len(texs)} paper(s)")
    print()
    if selftest():
        return 1
    bare = []
    quoted = 0
    for label, phrase, marker, prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        mrk = re.compile(marker, re.I)
        print(f"  ** {label} ** -- {prov}")
        for t in texs:
            body = strip_comments(open(t, encoding='utf-8', errors='replace').read())
            hits = list(pat.finditer(body))
            if not hits:
                continue
            ok = sum(1 for m in hits if mrk.search(body[m.end():m.end() + WINDOW]))
            quoted += ok
            n_bare = len(hits) - ok
            flag = '' if not n_bare else '   <-- BARE'
            print(f"     {os.path.basename(t):<34} {len(hits):>3} hit(s), "
                  f"{ok:>3} corrected{flag}")
            for m in hits:
                if not mrk.search(body[m.end():m.end() + WINDOW]):
                    ctx = body[max(0, m.start() - 90):m.end() + 90].replace('\n', ' ')
                    bare.append((os.path.basename(t), label, ctx))
        print()

    # --- the same scan over the forward-facing standing registers ---------------------------
    import glob as _glob
    regs = [r for r in sorted(_glob.glob(os.path.join(REGISTER_DIR, '*.md')))
            if os.path.basename(r) not in HISTORICAL]
    print(f"  STANDING REGISTERS -- {len(regs)} forward-facing document(s) "
          f"({len(HISTORICAL)} exempt as historical records)")
    # ** THE ROW IS THE UNIT IN A TABLE, added r2376+c54.151. **  The 900-character window is the
    # right scope for prose and the WRONG one for a markdown table: at c54.149 a withdrawal struck
    # ONE row of THE_WORK's closure table and left three others standing on identical grounds, and
    # every one of those three passed this gate because the struck row sat within the window.  So
    # when a hit lands on a table row -- a line beginning with '|' -- the correction must be in
    # THAT row.  *A row rests on grounds, not on its neighbours.*
    for label, phrase, marker, prov in REGISTRY:
        pat = re.compile(phrase, re.I)
        mrk = re.compile(marker, re.I)
        for r in regs:
            txt = open(r, encoding='utf-8', errors='replace').read()
            for m in pat.finditer(txt):
                ls = txt.rfind('\n', 0, m.start()) + 1
                le = txt.find('\n', m.end())
                le = len(txt) if le == -1 else le
                if txt[ls:ls + 1] == '|':
                    scope = txt[m.end():le]          # the rest of this table row only
                else:
                    scope = txt[m.end():m.end() + WINDOW]
                if not mrk.search(scope):
                    ctx = txt[max(0, m.start() - 90):m.end() + 90].replace('\n', ' ')
                    bare.append((os.path.basename(r), label, ctx))
    print()

    if bare:
        print(f"  ⛔ {len(bare)} BARE OCCURRENCE(S) -- a withdrawn claim stated with no adjacent")
        print(f"     correction.  The corpus may QUOTE what it withdrew; it may not ASSERT it.")
        print()
        for f, label, ctx in bare:
            print(f"     [{f}] ({label})")
            print(f"        ...{ctx}...")
        print()
        print("  Fix by stating the revision beside the phrase, or by rewording the phrase.")
        return 1

    print(f"  No bare occurrences.  ({quoted} quotation(s) of withdrawn wording, each carrying")
    print(f"  an adjacent correction -- which is the honest form and is why this gate does not")
    print(f"  simply ban the words.)")
    print()
    print("  ⌗ A withdrawal is not finished until its phrase is in this file's REGISTRY.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
