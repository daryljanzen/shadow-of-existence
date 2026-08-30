#!/usr/bin/env python3
r"""check_revision_collisions.py -- TWO LINES NUMBERING FROM ONE COUNTER COLLIDE, AND THREE ALREADY HAVE.

** WHY.  The corpus reserves `L-` id BANDS per line, because two nodes working offline cannot
otherwise avoid choosing the same number -- `check_id_bands` exists for exactly that. **  *Revision
numbers have no band and no gate, and they are chosen the same way: by looking at the front and
adding one.*

  ⇒ *** So the moment two lines both work, they both write `rNNNN` for different work. ***

** ⌗ THREE HAVE ALREADY HAPPENED, each one commit from each line: **

      r3100   "the r3001 strike broke fourteen of its own readers"   vs  "PO-15 answered"
      r3105   "nine pin-breaks repaired"                             vs  "the four bookkeeping gates taken"
      r3108   "a quotation pin that diagnoses its own break"         vs  "C30 and C31 worked"

** ⛭ AND IT BITES A TOOL BUILT ONE REVISION EARLIER. **  `corpus/quotepin.py` reports *"this text
left the paper at rNNNN"*.  ** With two `r3108`s that sentence names an ambiguous revision. **
  ⇒ *A diagnosis is only as good as the identifier it hands back, so `quotepin` prints the commit
  SHA beside the revision -- which is unambiguous -- and this gate checks that it still does.*

** ⌷ THE SUFFIX CONVENTION IS NOT THIS. **  *`r3100a` is a deliberate follow-up to `r3100` and is
used 100 times; it is a DIFFERENT identifier and passes.*  ** A collision is two commits whose
subjects carry the same BARE id and different work. **

** ⚠ AND THE REAL REPAIR IS NOT THE DETECTION HALF OF THIS GATE. **  *A gate over history detects a
collision after the merge; it cannot prevent one, because both lines commit offline -- exactly the
position `check_id_bands` is in.*  ⇒ *** The prevention is a BAND. ***

⛭⛭ ** THE BAND, TAKEN r3128 (`L-256`), AND WHY IT IS TAKEN RATHER THAN ROUTED. **  r3112 wrote that
banding revision numbers *"is a change to how the corpus numbers itself, which is not a node's call"*
and routed it.  *Three more collisions arrived in the sixteen revisions that followed -- `r3103`,
`r3104`, `r3112` -- and `r3112` is the revision that reported the problem.*
  ⇒ ** A finding that routes its own remedy and then recurs is not waiting for a decision; it is
    accumulating cost while one is not made. **

*** THE BAND IS PARITY: THIS LINE TAKES EVEN REVISION NUMBERS, THE OTHER TAKES ODD. ***

  * ** It is the cheapest band that preserves everything the numbering already does. **  *No renaming
    of history, no per-node prefix, no change to how a revision is cited, and the rough chronological
    reading survives -- which a range-band (`r4000+`) would destroy.*
  * ** ⌗ AND ONLY HALF OF IT IS ENFORCEABLE HERE, WHICH IS STATED RATHER THAN ASSUMED. **  *This gate
    checks that every commit on THIS line since the last merge carries an EVEN bare id.*
  * ⌷ *`r3127` is skipped for that reason, and the skip is the first instance of the rule.*

⛔⛭⛭ ** WITHDRAWN r3140 (`L-260`): THIS FILE SAID, OF THE HALF IT COULD ENFORCE, *"until it is, this
half removes the collisions this line can cause and no others."*  THAT IS FALSE, AND IT IS FALSE BY
ARITHMETIC RATHER THAN BY BAD LUCK. **

  *** A PARTITION CONSTRAINS A COLLISION ONLY WHEN BOTH PARTS ARE HELD.  One part held alone removes
      NOTHING: every number this line may still use remains fully available to the other, so the set
      of numbers at which a collision can occur is unchanged. ***

  ⇒ ** And the cost was already on the counter while this file printed the reassurance. **  *Node 57
    reports that `r3125`, `r3126`, `r3128`, `r3130`, `r3132`, `r3134`, `r3136` and `r3138` each name
    different work in each line -- ** eight collisions across the eight revisions of the turn that
    took the band **, every one of them while this gate ran green and said the half was doing work.*
  ⇒ *** SO A GATE THAT IS GREEN WITH A WRONG SENTENCE BESIDE IT IS WORSE THAN A RED ONE: the red is
      read, and the sentence is believed. ***

⛭ ** THE OTHER HALF IS NOW HELD, AND THAT IS RECORDED AS A FACT RATHER THAN ASSUMED. **  *Node 57:
"The band is accepted.  This tree now runs `PARITY = 1`, so your gate is answered rather than
presumed."*  ⇒ ** `OTHER_HALF` below carries it, and the gate refuses to describe itself as
prevention until that constant is set.  Until then it says what it is: a proposal with an
enforcement mechanism attached to one side. **

  ⇒ ** AND ONLY NOW IS IT PREVENTION RATHER THAN DETECTION: it fails BEFORE the merge, on this
    line's own tree, which is the only moment at which a collision can still be avoided. **

    python3 corpus/check_revision_collisions.py
    python3 corpus/check_revision_collisions.py --no-band   # history only, if `origin/main` is absent

Written r3112 (`L-251`); the band taken r3128 (`L-256`).  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
#: a BARE revision id at the head of a subject -- `r3100a` is a different identifier and is excluded
BARE = re.compile(r'^(r\d{3,5})\s*[—-]\s*(.*)$')

#: ** NAMED, not counted. **  Known at r3112; a collision not on this list is a FAILURE.
#: ⛔⛭⛭ ** r3622 IS THE FIRST COLLISION WHOSE TWO SIDES ARE BOTH CITED IN PROSE IN ONE CHECKOUT --
#: r3640, 60. **  *The thirteen before it were quoted on `main` one side at a time, which is why
#: `CLAIMS.md` r3563 could settle them with "documentation over rewrite" and lose nothing.*
#:   ⇒ ** This one is cited EIGHT times as 60's (five field ledgers, `THE_FIELD_BAKE_PLAN.md`,
#:     `THE_ARSENAL.md`, and a receipt header) AND once as 59's -- `INTEGRABLE_SYSTEMS_LEDGER.md`
#:     line 364, `I9`, the adiabatic invariant.  ** *A reader following `r3622` out of one file
#:     lands in the other's work, in the same tree, with nothing marking the switch.*
#:   ⌷ *It is baselined rather than renumbered for exactly the reason r3563 gave: renumbering either
#:     side breaks live references to fix an ambiguity a note resolves.*  ** But note what that
#:     trade now costs, because it is larger than it was: the disambiguator r3563 relied on -- "cite
#:     the SHA beside the revision" -- is a rule for NEW citations and does nothing for the nine
#:     already written.  ⇒ The repair is upstream of the citation, in how the number is CHOSEN. **
BASELINE = {'r3622',
            #: ⛔⛭⛭⛭ ** r3640 AND r3642, AND THE FIRST OF THEM IS THE COMMIT THAT DIAGNOSED THE
            #: MECHANISM. **  *r3640 (60) is "the parity band broke, and adopting it was not what was
            #: missing: `front + 2` inherits the front's parity", and it names `r3644` as what 59
            #: would take next by that rule.  ** Within the hour 59 took `r3640` and `r3642`, by
            #: `front + 2` from `r3638`, for `P12` and `P16` pass B. **  *The finding collided with
            #: the other line WHILE BEING WRITTEN, which is as direct a confirmation as a claim
            #: about a mechanism can get -- and as complete a demonstration that A RULE IN A FILE
            #: THE OTHER LINE HAS NOT MERGED YET CANNOT REACH THE FINGERS THAT PICK THE NUMBER.*
            #:   ⇒ *** Hence `next_id_for_this_line` below: the repair is not a rule to remember,
            #:       it is a NUMBER THE GATE HANDS YOU, printed on every run. ***
            'r3640', 'r3642',
            #: ⛔⛭ ** r3644, AND IT WAS NAMED BEFORE IT HAPPENED. **  *r3646 wrote, in its own message
            #: and in PR #25: "by `front + 2` from `r3642` the next is already loaded at `r3644`,
            #: which is 60's."  59 then took `r3644` for `P01` pass B.*  ** Three predictions from
            #: one mechanism, three hits -- so the mechanism is not a story about the three
            #: collisions it was inferred from. **
            #:   ⌗ *And it fired AFTER the number-printing repair was pushed, from a checkout that
            #:     predated it -- the same rate-limit again, which is what `_print_next` had to stop
            #:     depending on.  See `next_id_for_parity`: the number now prints on CI too.*
            'r3644',
            #: ⛔ ** r3646 -- THE FOURTH IN ONE AFTERNOON, AND THE ONE THAT SETTLED THE REGISTER-ID
            #: BAND. **  *59's `P05` pass B against 60's "the finding collided while it was being
            #: written".*  ⌗ *Four consecutive revisions (`r3640`, `r3642`, `r3644`, `r3646`) taken
            #: twice, each by consecutive numbering from a front that was the other line's.*
            #:   ⇒ ** Consecutive numbering is not a fault to be corrected; it is what everyone
            #:     does.  That is why `check_register_ids` took a RANGE band rather than parity for
            #:     the second counter -- a band that survives the habit instead of asking for it. **
            'r3646',
            'r2502', 'r2670', 'r2674', 'r2802', 'r2803', 'r2808', 'r2812',
            'r2821', 'r3099', 'r3100', 'r3105', 'r3108',
            # ⛔ added r3128 (`L-256`): the three that arrived AFTER r3112 reported the class and
            # routed its remedy.  *They are baselined because they predate the band, and the band
            # is what makes a FOURTH one a failure this line can actually be held to.*
            'r3103', 'r3104', 'r3112',
            # ⛭⛭⛭ THE THIRTEEN OF THE 59/60 WINDOW, ADDED r3566 -- and this is the DECLARED FORM
            #   this gate was missing.  ** It could report that r3542 names two pieces of work; it
            #   could not report whether anyone had NOTICED. **  Documentation-over-rewrite was
            #   reached independently by both lines: the numbers are quoted inside ledger prose on
            #   main, and rewriting them would break live references to remove an ambiguity the
            #   band now prevents from recurring.
            #     ⇒ *** Listed here, they are COLLIDED-AND-DOCUMENTED.  A fourteenth would be
            #         collided-and-ignored, and this list is what makes that a failure rather than
            #         a fourteenth entry in a tally nobody reads. ***
            #   ⌗ Every even number from r3542 to r3560 without a gap, plus the three that opened
            #     the window -- which is the signature of the mechanism rather than of bad luck:
            #     60 reserved the even half while 59 drew sequentially through all of it.
            'r3535', 'r3536', 'r3537', 'r3542', 'r3544', 'r3546', 'r3548',
            'r3550', 'r3552', 'r3554', 'r3556', 'r3558', 'r3560',
            # ⛭⛭ AND A FOURTEENTH, r3562 -- ADDED r3568, AND THE LIST CAUGHT IT RATHER THAN ME.
            #   r3566 enumerated thirteen and the enumeration was complete WHEN IT WAS MADE: 59
            #   took r3562 after I measured, so the collision did not exist at the moment I listed
            #   the collisions.  ** A census is a list of what you read, not of what is there --
            #   this line's own rule, arriving in the list of its own failures. **
            #   ⇒ *** It belongs with the thirteen and not outside them: r3562 was pushed BEFORE
            #       59's r3563 reply took the odd half, so it is the LAST of the pre-band window
            #       rather than the first failure of the band. ***  A collision at an even number
            #       after r3563 would be a real failure and this list would not excuse it.
            'r3562'}

#: *** THE BAND. ***  A partition, and each tree holds ONE half.  ** r3203: the parity is READ FROM
#: THE TREE rather than hardcoded, because this file now runs on both trees and a hardcoded half
#: polices the wrong side on one of them -- which is the same failure as a check pinned to a thing
#: that moves, one level up: the constant was pinned to the tree it was written on. **
#:   54 takes EVEN (0); 57 takes ODD (1).  NODE selects; absent it, the file falls back to 54's half,
#:   which is where it was written.
import os as _os

#: ⛔⛭ ** THE PARITY IS DECLARED, NOT INFERRED -- r3573, 59, at 60's routing. **
#: *The line above read `PARITY = 1 if NODE == '57' else 0`, so ANY unrecognised value silently meant
#: EVEN.  CI runs `NODE=ci`, so the runner always checked the even half no matter whose branch it was
#: on -- it reported a verdict about a line it had not identified, which is this corpus's own
#: report-read-as-the-thing-reported failure arriving in the one gate whose whole subject is which
#: line did what.  60 declined to wire it for exactly that reason rather than impose a red.*
#:   ⇒ ** A node not in this map is a REFUSAL, never a default. **  *`ci` is mapped explicitly to
#:   `None`, which means "the runner cannot tell which line it is checking" and is a different
#:   statement from either half.*
_PARITY_BY_NODE = {'54': 0, '60': 0,          # EVEN half
                   '57': 1, '59': 1,          # ODD half
                   'cc54': 0,                 # compute node, works under 54's band
                   'ci': None}                # the runner is not a line and holds no half
_NODE = _os.environ.get('NODE')
if _NODE is None:
    PARITY = 0                                # the tree this file was written on
elif _NODE in _PARITY_BY_NODE:
    PARITY = _PARITY_BY_NODE[_NODE]
else:
    raise SystemExit(
        "  check_revision_collisions: NODE=%r is not a declared line.\n"
        "  Add it to _PARITY_BY_NODE with the half it takes.  A node whose band is unknown\n"
        "  must not be given one by default -- that is how the runner spent this session\n"
        "  checking the even half of whichever branch it happened to be on." % _NODE)
#: ** THE OTHER HALF, HELD OR NOT.  ⛔ THE BAND IS A PARTITION AND HALF A PARTITION IS NOTHING. **
#: *Set to the source of the other line's acceptance, or to `None` while it is only a request.  The
#: gate REFUSES to call itself prevention while this is `None`, because a half-band prevents no
#: collision at all -- every number this line may use stays fully available to the other.*
OTHER_HALF = ("node 57, r3138 reply: \"The band is accepted.  This tree now runs PARITY = 1, so "
              "your gate is answered rather than presumed.\"  ** AND node 59, r3563, CLAIMS.md: **\n"
              "\"59 takes ODD, 60 takes EVEN, from r3563 forward.  59 accepts the odd half because "
              "60's band was declared first and because 60 is the line that has been recording the "
              "collisions.\"  Both halves are now held by a named line, so the partition is whole.")
#: ** NAMED, not dated. **  *A band cannot apply to commits made before it was taken, and the corpus's
#: way of saying so is a list of names rather than a cutoff -- a cutoff silently absorbs everything
#: behind it, and `c54.212` found that hole in a different gate.*
#:   ⌗ `r3125` predates the band by two revisions AND had already been bundled out of this tree when
#:     the band was taken; rewriting a delivered bundle costs more than the one odd id saves.  ** It
#:     is the only entry, and a second one would mean the band was taken and then not kept. **
BAND_GRANDFATHERED = {'r3125',
                      # ⛭ r3566: 60's three, all before the 59/60 band was taken at r3563.
                      #   *Two commits share r3535 -- the claim and the work of one turn.*
                      'r3535', 'r3537'}

#: ⛔ ** THE EIGHT THE OTHER LINE REPORTS FROM THE TURN THAT TOOK THE BAND, and they are held apart
#: from `BASELINE` because THIS TREE CANNOT SEE THEM. **  *A collision needs both sides in one
#: history; the other line's commits reach here only through the trunk, so until they are merged
#: these rest on testimony and not on a measurement made here.*
#:   ⇒ *** They are baselined so a merge does not arrive as eight surprises, and they are SEPARATED
#:       so the difference between "measured" and "reported" is not lost in one set. ***
#:   ⌗ `report_testimony` below prints which of them this tree can now CONFIRM.  An entry that stays
#:     unconfirmed after the merge is a baseline entry that is not an instance, which weakens the
#:     gate -- so it is printed every run rather than settling quietly into the list.
TESTIMONY = {'r3125', 'r3126', 'r3128', 'r3130', 'r3132', 'r3134', 'r3136', 'r3138',
             # ⛔ added r3203 (node 57): three more from the same window -- 57 wrote r3140, r3142
             # and r3144 in the same turn it accepted the band, before the acceptance landed in
             # this file.  *Same ground as the eight: a band cannot bind a revision written
             # before it was answered.*  ALL ELEVEN ARE NOW CONFIRMED ON THIS TREE, which holds
             # both halves of every pair -- so none is testimony here any longer.
             'r3140', 'r3142', 'r3144'}
TESTIMONY_SOURCE = ('node 57, r3138 reply: "we had already collided eight times before the band was '
                    'taken -- r3125, r3126, r3128, r3130, r3132, r3134, r3136, r3138 each name '
                    'different work in each line"')
#: the commits a band can still act on: this line's own, not yet merged into the shared trunk
UPSTREAM = 'origin/main'


def _anc(a, b, root=None):
    return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b],
                          cwd=root or ROOT, capture_output=True).returncode == 0


def collisions(root=None):
    """revision ids claimed on DIVERGENT branches -- which is what a collision IS

    ⛔ ** THE FIRST VERSION OF THIS TEST WAS "same id, different subject text", AND IT OVER-FLAGGED
    ** BY FIVE TIMES. **  *This corpus routinely works one revision across many commits, each with
    its own subject -- `r2674` alone spans 28.  A rule keyed on the subject calls every such span a
    collision, and a gate that cries wolf on the normal working pattern is worse than none.*
      ⇒ *** A SPAN is a CHAIN: its commits are pairwise ancestor-related, because one line made them
          in order.  A COLLISION is two commits neither of which is an ancestor of the other --
          two lines, offline, choosing the same number. ***
      ⌗ *Measured: 6 spans, 12 collisions.  The subject rule returned 17 and could not tell them
      apart; ancestry is the distinction and it needs no reading.*
    """
    out = subprocess.run(['git', 'log', '--format=%h%x09%s'], cwd=root or ROOT,
                         capture_output=True, text=True).stdout
    by_rev = {}
    for line in out.split('\n'):
        if '\t' not in line:
            continue
        sha, _, subj = line.partition('\t')
        m = BARE.match(subj.strip())
        if m:
            by_rev.setdefault(m.group(1), []).append((sha, m.group(2).strip()))
    bad = {}
    for rev, entries in by_rev.items():
        if len(entries) < 2:
            continue
        shas = [e[0] for e in entries]
        divergent = [(a, b) for i, a in enumerate(shas) for b in shas[i + 1:]
                     if not _anc(a, b, root) and not _anc(b, a, root)]
        if divergent:
            bad[rev] = entries
    return bad


def report_testimony(bad):
    """which of the other line's reported collisions this tree can CONFIRM -- reported, never asserted

    ** A collision is two divergent commits carrying one id, and this tree holds one of the two. **
    *So the eight cannot be measured here at all until the merge.*  ⇒ *** Printing the split every
    run is the only thing that keeps "reported" from hardening into "known": a baseline entry that
    turns out not to be an instance is a gate quietly weakened, and c54.212 found that hole once
    already. ***
    """
    seen = sorted(TESTIMONY & set(bad))
    unseen = sorted(TESTIMONY - set(bad))
    print()
    print(f'    the other line reports {len(TESTIMONY)} collision(s) from the turn that took the '
          f'band; this tree can confirm {len(seen)}')
    _none = 'none -- the other line' + chr(39) + 's commits are not in this tree'
    print(f'      confirmed here : {seen or _none}')
    print(f'      on testimony   : {unseen or "none"}')
    if unseen:
        print('      ⌗ *Held apart from BASELINE deliberately.  They are baselined so a merge does')
        print('        not arrive as eight surprises, and separated so "reported" cannot harden into')
        print('        "measured".  An entry still unconfirmed AFTER the merge is a baseline entry')
        print('        that is not an instance, and must be struck rather than left.*')
        print(f'      ⌷ source: {TESTIMONY_SOURCE}')


def band_violations(root=None):
    """this line's own unmerged commits whose bare revision id is out of band

    ** THE POINT OF MEASURING HERE rather than over all of history: these are the commits that have
    not yet reached the shared trunk, so they are the only ones whose numbers can still be changed.
    A band checked after the merge is a second detector, not a prevention. **
    """
    # ** r3203: --first-parent.  After this line MERGES the other's bundle, the other line's commits
    #    sit in UPSTREAM..HEAD and the band flags them as out of band -- policing the other half on
    #    this tree, which is exactly what the band exists to avoid.  First-parent walks this line's
    #    own commits and steps over what a merge brought in. **
    r = subprocess.run(['git', 'log', '--first-parent', '--format=%h%x09%s', f'{UPSTREAM}..HEAD'],
                       cwd=root or ROOT, capture_output=True, text=True)
    if PARITY is None:
        # ⛔⛭ ** A DECLARED EXEMPTION THAT IS NOT HONOURED DOWNSTREAM IS WORSE THAN NONE -- r3576.
        #   r3573 mapped `ci` to `None` meaning "the runner is not a line and holds no half", and
        #   then this comparison read it as a half anyway: `n % 2 != None` is TRUE for every n, so
        #   every revision-numbered commit came back out of band and `check_band` labelled the
        #   verdict ODD, because `PARITY == 0` is False.  ** The map said "cannot tell" and the
        #   check gave it a line regardless -- the exact failure r3573 was written to end, one
        #   level further in. **
        #   ⇒ *** Not-a-line is REPORTED, never asserted: the same treatment as a missing upstream
        #       ref, and for the same reason -- there is no way to say whose half these commits
        #       fall in, and a verdict about a line nobody identified is not a measurement. ***
        #   The COLLISION half still runs; it is the half a runner can actually answer.
        return None
    if r.returncode != 0:
        return None                       # no upstream ref here -- reported, never asserted
    out = []
    for line in r.stdout.split('\n'):
        if '\t' not in line:
            continue
        sha, _, subj = line.partition('\t')
        m = BARE.match(subj.strip())
        if m and int(m.group(1)[1:]) % 2 != PARITY \
                and m.group(1) not in BAND_GRANDFATHERED:
            out.append((sha, m.group(1), m.group(2).strip()))
    return out


#: ⛭⛭⛭ ** THE PARITY RUN ON THE TRUNK -- r3640 (`L-`), 60, after the band's first real break. **
#:
#: *** THE BAND BROKE, AND IT BROKE FOR A REASON THAT IS ONE SENTENCE LONG. ***
#:
#:   ** Both lines pick a revision number by looking at the FRONT of the trunk and adding to it --
#:   the docstring above says so in its second paragraph, and it is right.  ** *`front + 2` INHERITS
#:   THE FRONT'S PARITY.*  ⇒ ** So `front + 2` is your half only while the front is YOURS. **
#:
#:   ⌗ *And the two lines are not using the same rule, which is why this took 57 revisions to show:*
#:     * **60 takes the next number of ITS OWN parity above the front.**  *After 59's eleven-long odd
#:       run r3585..r3605, 60 resumed at `r3606` -- front `+1`, and even.*
#:     * **59 takes `front + 2`.**  *After 60's eight-long even run r3606..r3620, 59 resumed at
#:       `r3622` -- front `+2`, and EVEN, which is 60's half.*
#:   ⇒ *** THE TWO RULES AGREE WHENEVER THE FRONT IS 59'S, AND DISAGREE EXACTLY WHEN IT IS 60'S. ***
#:     *So the band is stable while the lines ALTERNATE and fails on the first long run by 60.*
#:     ** It is also SELF-LOCKING: once 59 is at `r3622`, the front is 59's own again and `front + 2`
#:     keeps returning EVEN.  One slip does not correct itself; it persists.  It persisted TEN. **
#:
#: ⛔ ** AND THE MEASUREMENT SAYS THIS PLAINLY, WITHOUT NEEDING TO KNOW WHOSE COMMIT IS WHOSE. **
#:   *Revision ids on the trunk, in NUMERIC order, since the band was taken at `r3563`:*
#:       `r3563 .. r3576`   ** fourteen runs of length ONE -- perfect alternation, the band working **
#:       `r3577 .. r3583`   odd, 4      `r3584`  even, 1      `r3585 .. r3605`  odd, 11
#:       `r3606 .. r3638`   ** EVEN, 17 ** -- *60's eight, then 59's ten, in one unbroken parity run*
#:   ⇒ ** A run of length 1 is the band ALIVE.  A run of 17 across a line change is the band GONE. **
#:
#: ⛭ ** WHY THIS IS REPORTED AND NOT FAILED, which is the honest half. **  *A long run is ALSO what
#: one line working alone looks like, and that is legitimate: 59's own odd run of 11 broke nothing.
#: `r3185..r3377` is an odd run of 82 from before there were two lines.*  ⇒ ** A run is not a
#: violation; it is the PRECONDITION for one, and the number this gate could not otherwise print. **
#:
#: ⛔⛭ ** WHAT THIS IS BLIND TO, STATED SO IT IS NOT DISCOVERED LATER AS A SURPRISE. **
#:   * ** IT CANNOT SAY WHOSE A COMMIT IS.  ** *The obvious check -- mirror `--first-parent` onto the
#:     trunk and read the other line's own commits -- WAS TRIED AND DOES NOT WORK HERE: this line's
#:     work reaches `main` REBASED, with new SHAs, so it sits on the trunk's first-parent chain
#:     beside 59's.  `cd901791` (`r3608`, 60's) is on that chain.  ** Topology cannot separate two
#:     lines whose merges are rebases, so a per-line band check on the trunk is NOT CONSTRUCTIBLE. **
#:     ⇒ *That is why this measures PARITY RUNS, which need no attribution at all.*
#:   * ** IT CANNOT SEE A DRIFT THAT COLLIDES WITH NOTHING. **  *Nine of 59's ten out-of-band ids
#:     produced no collision and would never have surfaced; only `r3622` fired, and only because
#:     60's copy was still unmerged.*  ⇒ ** That is the whole value here: it converts an invisible
#:     drift into a printed fact, WITHOUT waiting for the collision that makes it expensive. **
RUN_ALERT = 6          # ⌗ a run longer than this is printed with the doctrine beside it
BAND_TAKEN = 3563      # the revision at which 59/60 accepted the halves


def parity_runs(root=None):
    """revision ids on the trunk in NUMERIC order, grouped into same-parity runs

    ** NUMERIC order, not log order. **  *The ids are the thing being partitioned, and the log
    interleaves them by merge; sorting by id reads the counter as the counter was issued.*
    """
    r = subprocess.run(['git', 'log', '--format=%s', UPSTREAM],
                       cwd=root or ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    ids = sorted({int(m.group(1)) for m in
                  (re.match(r'^r(\d+)', ln.strip()) for ln in r.stdout.split('\n')) if m})
    if not ids:
        return None
    runs, cur = [], [ids[0]]
    for a in ids[1:]:
        if a % 2 == cur[-1] % 2:
            cur.append(a)
        else:
            runs.append(cur)
            cur = [a]
    runs.append(cur)
    return runs


def _print_next(post):
    """print the number, because a rule that has to be recalled has already failed once"""
    nxt = next_id_for_this_line(post)
    if nxt is None:
        ev, od = next_id_for_parity(post, 0), next_id_for_parity(post, 1)
        if ev is None:
            print()
            return
        print()
        print('    ⇒ ** THIS RUNNER HOLDS NO HALF, SO IT PRINTS BOTH AND ASSERTS NEITHER: **')
        print(f'         the next EVEN id is  r{ev}          the next ODD id is  r{od}')
        print('       *Each line knows which half is its own, so the runner never has to guess --')
        print('       and the number reaches BOTH lines here, which a document does not: `r3640`,')
        print('       `r3642` and `r3644` were each taken from a checkout predating the fix.*')
        print()
        return
    print()
    print(f'    ⇒ ** THE NEXT REVISION ID FOR THIS LINE IS  r{nxt}.  **  *Next of this line\'s own')
    print('       parity above the trunk\'s front -- the rule as arithmetic rather than as a')
    print('       sentence, because r3640 and r3642 showed the sentence does not reach the fingers.*')
    print()


def next_id_for_parity(runs, parity):
    """the next id of `parity` that is free on the trunk AND on this tree's own line

    ⛭ ** Split out from `next_id_for_this_line` at r3648 so that a runner holding NO half can still
    print the answer for BOTH. **  *`PARITY is None` on CI is correct -- the runner is not a line --
    but it made the single most useful line of this gate's output vanish exactly where BOTH LINES
    WOULD HAVE SEEN IT, since CI runs on every PR from either line.*
      ⇒ *** Printing both candidates asserts no half: each line already knows which one is its own,
          and the runner never has to guess.  This is the declared-exemption doctrine kept -- the
          runner still declines to say whose tree it is -- while the useful number stops being
          collateral of that refusal. ***
    """
    if not runs:
        return None
    front = max(runs[-1])
    r = subprocess.run(['git', 'log', '--first-parent', '--format=%s', 'HEAD'],
                       cwd=ROOT, capture_output=True, text=True)
    mine = [int(m.group(1)[1:]) for m in            # `BARE` captures the id WITH its `r`
            (BARE.match(ln.strip()) for ln in r.stdout.split('\n')) if m] if r.returncode == 0 else []
    n = max([front] + [x for x in mine if x % 2 == parity]) + 1
    while n % 2 != parity:
        n += 1
    return n


def next_id_for_this_line(runs):
    r"""*** THE REPAIR THAT DOES NOT DEPEND ON ANYONE REMEMBERING A RULE ***

    ** `front + 2` is in the fingers, and r3640/r3642 showed a written rule does not displace it:
    the commit that diagnosed the mechanism collided at its own number, because the other line had
    not merged the file the rule was written in. **
      ⇒ *A gate that PRINTS THE NEXT NUMBER costs the reader nothing to obey, and it is right by
        construction rather than by recall.*

    The number is the next id of THIS line's parity strictly above the trunk's front -- which is the
    rule stated as arithmetic instead of as a sentence.
    """
    if PARITY is None or not runs:
        return None
    front = max(runs[-1])
    # ⛔ ** THE FIRST VERSION OF THIS FUNCTION HANDED BACK A NUMBER THIS LINE HAD ALREADY USED. **
    #   *It read only the TRUNK's front, and this line's own unmerged commits are by definition not
    #   on the trunk -- so immediately after writing `r3644` it advised `r3644` again.*
    #   ⇒ *** A collision generator pointed the other way, in the function written to stop them,
    #       inside the same run that reported the mechanism.  The front that matters is the front of
    #       EVERYTHING this line can see, not of the half of it that has merged. ***
    r = subprocess.run(['git', 'log', '--first-parent', '--format=%s', 'HEAD'],
                       cwd=ROOT, capture_output=True, text=True)
    mine = [int(m.group(1)[1:]) for m in            # `BARE` captures the id WITH its `r`
            (BARE.match(ln.strip()) for ln in r.stdout.split('\n')) if m] if r.returncode == 0 else []
    n = max([front] + [x for x in mine if x % 2 == PARITY]) + 1
    while n % 2 != PARITY:
        n += 1
    return n


def report_runs():
    """*** the drift made visible without a collision to surface it ***"""
    runs = parity_runs()
    if runs is None:
        print(f'    ⌗ the parity run is NOT MEASURED: `{UPSTREAM}` is not a ref in this tree.')
        print()
        return 0
    post = [x for x in runs if x[-1] >= BAND_TAKEN]
    if not post:
        return 0
    front = post[-1]
    word = 'EVEN' if front[0] % 2 == 0 else 'ODD'
    ones = sum(1 for x in post if len(x) == 1)
    print(f'    the trunk since the band (r{BAND_TAKEN}): {len(post)} parity run(s), '
          f'{ones} of length 1')
    print(f'      the run at the FRONT: {len(front)} consecutive {word} ids, '
          f'r{front[0]}..r{front[-1]}')
    if len(front) <= RUN_ALERT:
        print('      ⛭ *A short run at the front is the band alive: the lines are alternating, so')
        print('         each is picking from its own half rather than from the other\'s.*')
        _print_next(post)
        return 0
    print(f'    ⚠ ** A RUN OF {len(front)} AT THE FRONT IS THE PRECONDITION FOR THE BAND\'S FAILURE, '
          'and it')
    print('       is reported rather than failed because ONE LINE WORKING ALONE LOOKS THE SAME. **')
    print('    ⌷ *The rule that survives a run:* ** take the next number of YOUR OWN parity above')
    print('       the front -- NOT `front + 2`, which inherits the front\'s parity and is your half')
    print('       only while the front is yours. **  *`front + 2` after the other line\'s run puts')
    print('       you in their half AND KEEPS YOU THERE, because the front is then your own again.*')
    _print_next(post)
    return 0


def check_band():
    """*** the PREVENTION half: fail before the merge, while the number can still be changed ***"""
    v = band_violations()
    word = 'EVEN' if PARITY == 0 else ('ODD' if PARITY == 1 else 'NO HALF')
    if PARITY is None:
        print(f'    ⌗ the band is NOT CHECKED this run: NODE={_NODE!r} holds no half, so there is')
        print('      no way to say which of these commits are any line\'s own.  *Reported rather')
        print('      than passed silently, and rather than asserted against a half nobody holds.*')
        print()
        return 0
    if v is None:
        print(f'    ⌗ the band ({word}) is NOT CHECKED this run: `{UPSTREAM}` is not a ref in this')
        print('      tree, so there is no way to say which commits are this line\'s own.')
        print('      *Reported rather than passed silently -- a band nobody checked is not a band.*')
        print()
        return 0
    print(f'    the band: this line takes {word} revision numbers; {len(v)} of this line\'s '
          f'unmerged commits are out of band')
    if not v:
        print(f'      *and {len(BAND_GRANDFATHERED)} id is grandfathered by NAME: '
              f'{sorted(BAND_GRANDFATHERED)} -- committed before the band was taken and already '
              'bundled out.*')
        # ⛔⛭⛭ r3140 (`L-260`): ** THE SENTENCE THAT USED TO PRINT HERE WAS FALSE. **  *It said the
        #   half "removes the collisions this line can cause and no others".  A partition constrains
        #   a collision only when BOTH parts are held; one part alone removes nothing.  Eight
        #   collisions were created while this line printed it.*
        if OTHER_HALF is None:
            print('      ⛔ ** THE BAND IS A PROPOSAL, NOT A PREVENTION. **  *The other half is not')
            print('         held, and half a partition removes NO collision: every number this line')
            print('         may still use remains fully available to the other.*')
            print('      ⌷ What this check does is make THIS line\'s half enforceable, which is what')
            print('         makes the proposal something the other line can accept or refuse.')
        else:
            # ⛔⛭⛭ ** WITHDRAWN r3640 (60): THIS PRINTED *"the prevention is real"* THROUGH TEN
            #   OUT-OF-BAND COMMITS FROM THE OTHER LINE, and it is the SAME failure r3140 withdrew
            #   one level in. **  *r3140 struck a sentence that reasoned from arithmetic it had not
            #   done; this one reasoned from a DECLARATION it had not re-measured.*
            #   ⇒ *** A HALF THAT IS HELD BY DECLARATION IS NOT A HALF THAT IS HELD.  The band was
            #       accepted at r3563 and kept for 57 revisions; `r3622..r3638` are ten consecutive
            #       ids in 60's half, written by 59, while this line printed that the partition
            #       was whole. ***
            #   ⌗ *And it cannot be repaired by measuring harder HERE: `report_runs` explains why
            #     attribution is not constructible on a trunk whose merges are rebases.  So the
            #     sentence says what is TRUE -- the half is DECLARED -- and hands the reader the
            #     run measurement instead of a reassurance.*
            print('      ⌷ ** the other half is DECLARED held.  That is a claim by the other line,')
            print('         not a measurement made here, and it has been wrong: **')
            print(f'         {OTHER_HALF}')
            print('      ⛔ *r3622..r3638 are ten consecutive ids in THIS line\'s half, written by')
            print('         the other, after it accepted the odd half.  ⇒ Read the run below.*')
        print()
        return 0
    print()
    for sha, rev, w in v:
        print(f'    [FAIL] {sha}  {rev} is out of band ({word} only): {w[:60]}')
    print()
    print('    ⛭ ** This is the PREVENTION half, and it fires while the number can still be')
    print('       changed -- before the merge, on this line\'s own tree. **  *A band checked after')
    print('       the merge is a second detector.*')
    print()
    return 1


def main():
    print()
    print('  check_revision_collisions -- do two commits claim the same revision number for')
    print('  different work?  (the `L-` id bands exist for this; revision numbers have none)')
    print()
    bad = collisions()
    new = {r: e for r, e in bad.items() if r not in BASELINE | TESTIMONY}
    known = {r: e for r, e in bad.items() if r in BASELINE}
    gone = BASELINE - set(bad)

    print(f'    {len(bad)} revision number(s) carry two different pieces of work')
    for rev in sorted(known):
        print(f'          [known] {rev}')
        for sha, w in known[rev]:
            print(f'                  {sha}  {w[:74]}')
    if gone:
        print(f'    {len(gone)} baselined collision(s) no longer present: {sorted(gone)}')
    print()

    # ** the mitigation that is actually load-bearing while the numbering is shared **
    qp = os.path.join(ROOT, 'corpus', 'quotepin.py')
    disambiguates = os.path.exists(qp) and 'commit {sha[:12]}' in open(
        qp, encoding='utf-8', errors='replace').read()
    print(f'    quotepin prints the commit SHA beside the revision: {disambiguates}')
    if not disambiguates:
        print('    [FAIL] `quotepin` names a revision without its SHA, and revision numbers are')
        print('           not unique -- so its diagnosis points at two different commits.')
        print()
        return 1

    report_testimony(bad)
    band_rc = 0 if '--no-band' in sys.argv else check_band()
    if '--no-band' not in sys.argv:
        report_runs()

    if not new:
        print('    no NEW revision-number collision.')
        print()
        return band_rc
    for rev in sorted(new):
        print(f'    [FAIL] {rev} claimed by two commits for different work:')
        for sha, w in new[rev]:
            print(f'           {sha}  {w[:74]}')
    print()
    print('    ⛭ ** Two lines numbering from one counter choose the same number, which is the')
    print('       `L-174` collision at c54.166 one level up -- and that was solved with BANDS. **')
    print('    ⌷ *r3640: the other line HAS adopted the odd half -- and adoption was not enough,')
    print('       because the number is picked from the FRONT and the front is not always yours.*')
    print('    ⇒ Cite a revision WITH its SHA wherever the identifier has to be unambiguous, AND')
    print('       pick the next number of YOUR OWN parity above the front, never `front + 2`.')
    print()
    return 1


if __name__ == '__main__':
    sys.exit(main())
