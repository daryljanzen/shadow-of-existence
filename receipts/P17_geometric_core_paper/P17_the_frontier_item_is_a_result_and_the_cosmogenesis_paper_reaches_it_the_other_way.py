#!/usr/bin/env python3
"""
RECEIPT -- p0: ** ITEM 18 WORKED.  p0's FRONTIER ITEM 1 CARRIED ITS DATUM HALF AS AN OWING -- *"what is
owed there is its derivation from the progenitor collapse"* -- AND `L-150` HAD ALREADY ANSWERED IT IN
THE NEGATIVE AT r2433.  ** THE PAPER NOW STATES THE IMPOSSIBILITY AS A RESULT. **  ⛭⛭ AND THE
CROSS-REFERENCE THAT SHIPPED WITH THE FIRST DRAFT OF THIS PARAGRAPH WAS WRONG AND IS CORRECTED HERE:
P16 DRAWS THE SAME LINE BY A ** CONSERVATION LAW **, NOT BY PEAK SPACING. **

Built r2566+c54.207, lead `L-530`.  VEIN: `L-202` (p0 item 4, what the seam carries).

===================================================================================================
** THIS IS A PAPER-SIDE APPLICATION OF A STANDING RESULT, AND IT SAYS SO **
===================================================================================================

*The physics is not new here and this file does not re-derive it.*  `X1_the_ratio_is_a_clock_reading…`
(r2433) established that rho_r/rho_m is not the KIND of quantity a handover can carry: it scales as
1/a on either leg, so no single value exists to transmit, and a crossing multiplying both components
alike leaves the ratio unchanged.  ** What was owed was that p0 STOP CALLING IT AN OWING. **

  ⇒ *** A frontier closed by impossibility is a finding, and a frontier list that prints it as an
      outstanding task is misreporting the programme's own state. ***

===================================================================================================
** ⛭⛭ AND THE ONE THING THAT HAD TO BE CHECKED RATHER THAN WRITTEN — WHICH FAILED **
===================================================================================================

The first draft of this paragraph closed with a cross-reference to the cosmogenesis paper reading:
*"eta fixing the abundances and the peak heights while rho_r/rho_m fixes the peak spacing."*

  ** ⛔ THAT IS NOT WHAT P16 SAYS, AND ONE HALF OF IT IS NOT IN THE CORPUS AT ALL. **
  * "peak spacing" appears in **P15**, where it is the sound horizon against D_C -- ** it is nowhere
    attributed to rho_r/rho_m **;
  * and eta is READ FROM the peak heights by Planck; P16 does not say eta FIXES them.

** WHAT P16 ACTUALLY SAYS IS BETTER, AND IT IS AN INDEPENDENT SECOND REASON: **
  *"Total dissociation destroys nuclear binding, so the progenitor's composition is erased … It
  cannot destroy baryon number … So eta crosses the peak because it is protected, and the abundances
  do not because they are not."* -- ** two kinds of thing. **

  ⇒ *** SO THE CORPUS NOW HAS TWO INDEPENDENT REASONS THE RATIO IS NOT CARRIED, AND THEY AGREE:
      `L-150`'s (it is not constant along either leg, so there is nothing to carry) and P16's (the
      crossing destroys what would have fixed it).  The corrected clause states both. ***

  ⌗ ** This is the fourth time this session a routed or drafted cross-reference has failed on being
     checked against the source rather than the slip. **  *Recorded on that side of the base rate.*

===================================================================================================
** ⛔ WHAT IS NOT CLAIMED **
===================================================================================================

** Not a new derivation of anything ** -- the impossibility is `X1`'s and is cited, not re-run.  ** Not
that the seam frontier is closed ** -- `L-202` asks what the seam carries and stays open; what closes
is the DATUM half of p0's frontier item 1.  ** Not that P16's conservation-law reason and `L-150`'s
scaling reason are the same argument ** -- the point is that they are not, and agree.

SETTINGS: none.  Source checks only, against p0, P16, P15 and the standing receipt.

rc=0 on success.  Run: python3 P17_the_frontier_item_is_a_result_and_the_cosmogenesis_paper_reaches_it_the_other_way.py
                        (stdlib only; ~1 s)
"""
import os
import re
import sys

print(__doc__.split("rc=0")[0])

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
CORPUS = os.path.join(ROOT, 'corpus')
fail = []

P0 = open(os.path.join(CORPUS, 'geometric_core_paper.tex'), encoding='utf-8').read()
P16 = open(os.path.join(CORPUS, 'cosmogenesis_paper.tex'), encoding='utf-8').read()
P15 = open(os.path.join(CORPUS, 'CR_cosmology.tex'), encoding='utf-8').read()


def body(tex):
    """What the paper PRINTS.  Comment lines are corpus-shaped text that no reader and no gate
    ever sees, and PART 2 exists because one of them was mistaken for the paper.⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 0fcafd6** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

"""
    out = []
    for ln in tex.split('\n'):
        cut = re.search(r'(?<!\\)%', ln)
        out.append(ln[:cut.start()] if cut else ln)
    return '\n'.join(out)


P16_BODY, P15_BODY, P0_BODY = body(P16), body(P15), body(P0)

# =====================================================================
print("=" * 78)
print("PART 1 — THE OWING IS GONE FROM p0 AND A RESULT STANDS IN ITS PLACE")
print("=" * 78)
GONE = ("the old owing sentence is no longer in p0",
        r'What is owed\s*\n?there is its derivation from the progenitor collapse')
_ok_gone = re.search(GONE[1], P0, re.S) is None
print(f"  {'OK ' if _ok_gone else 'STILL THERE'}  {GONE[0]}")
if not _ok_gone:
    fail.append("p0 still prints the datum half as an owing — the revision did nothing")

WRITTEN = [
    ("the reversal is stated as such — what was written as owed is a result",
     r'what was written here as owed is a\s*\n?result, which is a different thing'),
    ("the standing receipt is cited rather than re-derived",
     r'\\rcpt\{X1_the_ratio_is_a_clock_reading_not_a_carried_datum\}'),
    ("the scaling reason is given",
     r'\\rho_r/\\rho_m\\propto1/a'),
    ("the multiplicative-crossing reason is given",
     r'a factor multiplying both components alike leaves the ratio unchanged'),
    ("and the impossibility is named as a finding",
     r'A frontier closed by impossibility is a finding'),
    ("⛭ the CORRECTED cross-reference is on the conservation law",
     r'what a handover carries is what a conservation law protects'),
    ("it names baryon number as the protected quantity",
     r'baryon number is conserved through it'),
    ("and states the two reasons as independent and agreeing",
     r'Two independent reasons, agreeing'),
]
for what, pat in WRITTEN:
    ok = re.search(pat, P0, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"p0 does not carry: {what}")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ⛭⛭ AND THE CROSS-REFERENCE, CHECKED AGAINST P16 RATHER THAN AGAINST THE DRAFT")
print("=" * 78)
P16_SAYS = [
    ("P16 states that dissociation destroys the composition",
     r"the\s*\n?progenitor's \\emph\{composition\} is erased"),
    ("P16 states that it cannot destroy baryon number",
     r'It cannot\s*\n?destroy baryon number'),
    ("P16 draws the conclusion in exactly those terms",
     r'\\eta\$ crosses the\s*\n?peak because it is protected'),
    ("and calls the distinction two kinds of thing",
     r'two kinds of thing'),
]
for what, pat in P16_SAYS:
    ok = re.search(pat, P16, re.I | re.S) is not None
    print(f"  {'OK ' if ok else 'MISSING'}  {what}")
    if not ok:
        fail.append(f"P16 does not say what the corrected clause attributes to it: {what}")

print()
print("  ⛔ AND THE DRAFT'S CLAIM, MEASURED — the reason it was corrected:")
_ps_p16 = len(re.findall(r'peak spacing', P16_BODY, re.I))
_ps_p15 = len(re.findall(r'peak spacing', P15_BODY, re.I))
_ps_p0 = len(re.findall(r'peak spacing', P0_BODY, re.I))
print(f"     'peak spacing' IN THE PRINTED BODY  ->  P16: {_ps_p16}   P15: {_ps_p15}   p0 (now): {_ps_p0}")
print("     *** The phrase is P15's and belongs to the sound horizon against D_C.  Attributing it to")
print("         rho_r/rho_m in P16 is a claim about a paper that does not print it. ***")
if _ps_p16 != 0:
    fail.append(f"'peak spacing' now appears {_ps_p16}x in P16's BODY — the correction's premise has changed")
if _ps_p0 != 0:
    fail.append("p0 still carries the withdrawn 'peak spacing' attribution")
if _ps_p15 == 0:
    fail.append("'peak spacing' is absent from P15's body too — the phrase's home cannot be identified")

print()
print("  ⛭⛭ AND WHERE THE DRAFT'S SENTENCE ACTUALLY CAME FROM, WHICH IS THE FINDING:")
_comment_only = len(re.findall(r'peak spacing', P16, re.I)) - _ps_p16
print(f"     'peak spacing' in P16's COMMENTS: {_comment_only}   in P16's BODY: {_ps_p16}")
_hdr = re.search(r'eta fixes the abundances and the CMB peak HEIGHTS, rho_r/rho_m\s*\n%\s*the peak SPACING',
                 P16)
print(f"     {'FOUND  ' if _hdr else 'ABSENT '} P16's header comment carries the draft's sentence almost verbatim")
print("     *** SO THE WRONG CROSS-REFERENCE WAS NOT INVENTED -- IT WAS READ OFF A NON-PRINTING")
print("         HEADER COMMENT AND CARRIED INTO A PAPER AS IF IT WERE THE PAPER. ***")
print("     ⚠ *A header comment is corpus-shaped text that no reader sees, no gate reads, and no")
print("        receipt pins -- and it is the natural place for a downstream writer to pick up a")
print("        claim the body never made.  Routed as its own lead rather than fixed here.*")
print("     ⛭⛭ AND IT HAD ALREADY PROPAGATED ONCE, WHICH IS WHAT MAKES IT A CLASS AND NOT A SLIP:")
_x1 = os.path.join(ROOT, 'receipts', 'L150_the_datum',
                   'X1_the_ratio_is_a_clock_reading_not_a_carried_datum.py')
_x1src = open(_x1, encoding='utf-8', errors='replace').read() if os.path.exists(_x1) else ''
_x1quotes = re.search(r'P16 distinguishes it from eta explicitly.{0,40}'
                      r'eta\s*\n?\s*fixes the abundances and the CMB peak HEIGHTS', _x1src, re.S) is not None
print(f"     {'FOUND  ' if _x1quotes else 'ABSENT '} `X1` (r2433) presents the header sentence as an EXPLICIT")
print("             statement of P16 -- so the unprinted claim was already being QUOTED as the paper's,")
print("             one hop before this draft picked it up.")
print("     ⇒ *** THE PATH IS: header comment -> a receipt's docstring, where it reads as a quotation")
print("         -> a paper. Two hops, and nothing in the tree measures the first. ***")
if not _x1quotes:
    fail.append("`X1` no longer quotes the header sentence — the propagation finding cannot be reproduced")

print()
print("  ⌗ AND WHETHER IT IS A CLASS ON THE INDEX SIDE, MEASURED RATHER THAN FEARED:")
_stems = set(re.findall(r'([A-Za-z0-9_]+)\.py',
                        open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()))
_disk = {f[:-3] for _r, _d, _fs in os.walk(os.path.join(ROOT, 'receipts')) for f in _fs if f.endswith('.py')}
_unindexed = sorted(_disk - _stems)
print(f"     receipts on disk: {len(_disk)}   with an INDEX row: {len(_disk) - len(_unindexed)}   "
      f"WITHOUT: {len(_unindexed)}")
print("     *`X1` had NO index row from r2433 until this revision -- so the receipt that closed the")
print("      programme's longest-standing target reached no printed appendix for 133 revisions, and")
print("      citing it here is what surfaced that.* ** Checked for a class: it was the only one. **")
if _unindexed:
    fail.append(f"{len(_unindexed)} receipt(s) still have no INDEX row: {_unindexed[:3]}")
print("     ⌗ *The comment is not FALSE -- P15 does tie the spacing to the sound horizon, which the")
print("        radiation content enters.  ** It is unprinted, which is a different defect. **")
if not _hdr:
    fail.append("P16's header comment no longer carries the sentence — the provenance finding "
                "cannot be reproduced and should be re-stated rather than left asserted")
if _comment_only == 0:
    fail.append("the comment/body split this part measures has vanished")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE STANDING RECEIPT p0 NOW LEANS ON IS REALLY THERE")
print("=" * 78)
X1 = os.path.join(ROOT, 'receipts', 'L150_the_datum',
                  'X1_the_ratio_is_a_clock_reading_not_a_carried_datum.py')
_ok_x1 = os.path.exists(X1)
print(f"  {'OK ' if _ok_x1 else 'MISSING'}  {os.path.relpath(X1, ROOT)}")
if not _ok_x1:
    fail.append("the receipt p0's new paragraph cites does not exist — the cite would print as a dead link")
else:
    _src = open(X1, encoding='utf-8', errors='replace').read()
    for what, pat in [("and it carries the 1/a scaling p0 now quotes", r'rho_r/rho_m goes as 1/a'),
                      ("and the no-single-value conclusion", r'no single value for a\s*\n?\s*handover to transmit')]:
        ok = re.search(pat, _src, re.I | re.S) is not None
        print(f"  {'OK ' if ok else 'MISSING'}  {what}")
        if not ok:
            fail.append(f"the cited receipt does not support p0's paragraph: {what}")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — p0 no longer prints the datum half as an owing; the paragraph states the")
print("impossibility as a result and cites the receipt that established it; the cross-reference to the")
print("cosmogenesis paper is the conservation-law line that paper actually draws, not the peak-spacing")
print("attribution the first draft carried; and 'peak spacing' is P15's phrase, absent from both.")
print("=" * 78)

# ============================================================================================
# GATE — r2566+c54.207, `L-530`.  ** This revision's whole content is a change of MODALITY -- an
# owing becoming a result -- so the pins are on the old modality being gone and on the borrowed
# authority being real:
#   (1) *** the old owing sentence asserted ABSENT ***.  ** If it survived anywhere, the frontier
#       list would still be misreporting the programme's state and the revision would have added a
#       paragraph without removing the error it was written to remove **;
#   (2) eight checks on the replacement, including the cite to the standing receipt -- ** p0 is
#       borrowing `L-150`'s result and must be seen to borrow it rather than to assert it **;
#   (3) *** four checks that P16 SAYS WHAT p0 NOW ATTRIBUTES TO IT ***.  ** The first draft
#       attributed something else and was wrong; this is the pin that would have caught it **;
#   (4) 'peak spacing' counted at ZERO in P16 and in p0 and NONZERO in P15 -- ** the withdrawn
#       attribution must not creep back, and the phrase's real home must stay identifiable **;
#   (5) and the cited receipt's existence AND two of its own conclusions -- ** a \rcpt{} to a file
#       that does not support the sentence is worse than no cite **.
#   NOT gated: any physics. ** None is new here; the impossibility is `X1`'s and the conservation
#   law is P16's. **
# ============================================================================================
assert _ok_gone, "p0 still prints the datum half as an owing"
for what, pat in WRITTEN:
    assert re.search(pat, P0, re.I | re.S), f"p0 does not carry: {what}"
for what, pat in P16_SAYS:
    assert re.search(pat, P16, re.I | re.S), f"P16 does not support the cross-reference: {what}"
assert _ps_p16 == 0 and _ps_p0 == 0 and _ps_p15 > 0, "the 'peak spacing' attribution is not where it belongs"
assert _hdr and _comment_only > 0, "the header-comment provenance of the withdrawn sentence cannot be reproduced"
assert _ok_x1, "the cited receipt is absent"
print(f"GATE c54.207 (r2566), `L-530`: p0's owing sentence is gone and the impossibility stands in its "
      f"place citing `X1` (r2433); the cross-reference is P16's conservation-law line, checked in P16's "
      f"own source; and 'peak spacing' is at {_ps_p16} in P16, {_ps_p0} in p0 and {_ps_p15} in P15, so "
      f"the first draft's attribution is withdrawn and cannot creep back — pinned against `FOR_54` "
      f"item 18 and `L-150`.")
