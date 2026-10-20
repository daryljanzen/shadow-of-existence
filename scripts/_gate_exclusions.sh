# _gate_exclusions.sh -- THE SINGLE SOURCE for which gates a local batch skips, and why.
#
# ** WHY THIS FILE EXISTS, AND IT IS THIS ROW'S FOURTH OBJECT TO EXIST IN TWO COPIES. **
# `r7457` ③: `turn_gates.sh` and `scripts/run_touched_readers.sh` both excluded `check_quote_pins`
# for the same reason and each held its OWN statement of it.  When `r7453+70.2` re-measured the gate
# (595 s here, 186-279 s in CI, against a `947` that was one container on one date) and
# `sweep_gates.sh` turned out to be in no workflow at all, correcting one copy left the other
# asserting two false things -- *and nothing in the tree would have caught that.*
#   ⌗ `PO-78` records the exclusion reason as the fourth object in this row to exist in more than one
#   copy, after the page list, the row headline and the reader set.  The generator is `r7441`'s rule
#   turned on opinions instead of data: ** a copy of a reason is a claim about the reason at the
#   moment it was copied. **
#
# ** WHY SOURCING, AND NOT A DATA FILE OR A GREP. **  `r7457` ⓑ: `turn_gates.sh` runs gates at source
# time, so sourcing IT to borrow `reason_for` would execute the batch; and one script GREPPING another
# is parsing an instrument's source to learn its opinion.  A data file would have forced the NEEDS
# half back into a hand list -- it is a tested precondition, not a string -- so the single source is a
# FUNCTION file that both scripts source and neither restates.
#
# Read by: scripts/turn_gates.sh, scripts/run_touched_readers.sh   (`grep -ln _gate_exclusions scripts/*.sh`)

# ** NEEDS: a precondition the script TESTS, replacing an exclusion that estimated it. **
#   A gate listed here is skipped only while its test fails, and the skip prints the test.
#   This set cannot grow silently: when the precondition is met the gate runs.  That is the
#   difference between an environment fact and a cost guess.
needs_unmet() {
  case "$1" in
    check_compile)          command -v pdflatex >/dev/null 2>&1 || { echo "no pdflatex here"; return 0; } ;;
    check_sitemap_resolves) [ -d _site ] || { echo "no assembled _site here"; return 0; } ;;
  esac
  return 1
}

# name:reason -- reason is printed, so an exclusion cannot be silent.
#   ⌗ 70's structural answer (r7453+70.2), kept here because this is now the only place it lives:
#   derivation YES for the environment half (NEEDS above), NO for the cost half.  One gate measured
#   947, 595, 279 and 186 seconds across two containers and three dates, so a declared cost is one
#   value of a quantity that has at least two at any moment.  Cost entries stay HAND-WRITTEN AND
#   STATE BOTH VALUES WITH THEIR DATE; a live timeout already prints any gate over it by name.
EXCLUDE_NAMES="check_quote_pins check_receipts_run"
reason_for() {
  case "$1" in
    check_quote_pins)      echo "595s here, 186-279s in CI (70, r7453+70.2) -- over a 280s local timeout; the fast job asks it every push" ;;
    check_receipts_run)    echo "a TRIGGER, not a cost: red whenever the tree digest moves (139s; the 9-minute figure described the RE-RUN, not the gate)" ;;
    # r7435: the one gate whose subject is the DEPLOYED site.  `_site/` is built
    #   by `pages.yml` and exists nowhere in a working tree, so the turn batch
    #   was asking it about a directory that is never here.  It is NOT taught to
    #   exit 0 on a missing `_site`: a gate that passes when its subject is
    #   absent is the vacuous pass its own sitemap-presence assertion exists to
    #   prevent, and moving that hole up one level is not closing it.
    check_sitemap_resolves) echo "needs the assembled _site and is the deploy job's question, not the turn's" ;;
    *)                     echo "no reason recorded -- THIS IS A DEFECT, add one" ;;
  esac
}
