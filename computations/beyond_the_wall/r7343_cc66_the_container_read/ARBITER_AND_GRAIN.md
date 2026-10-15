# `r7343+cc66.3` — the arbiter's roster, and the arbiter's own blind spot: `check_quote_pins` takes `947` seconds and the sweep gives it `420`, so the phase's ratchet has never been run by the phase's arbiter

*This closes `r7341` ⑥ — **"Run the script. No ad-hoc gate loop, by any seat, from here."** It also records
what running it found, two `P15` grain-moves performed under the ledger's own `[GRAIN-MOVE]` limb, and one
measurement that prices `69`'s amended minimand against my own last stride.*

## ① THE ARBITER RAN AND ITS ROSTER RECONCILES

`bash scripts/sweep_gates.sh`, `NODE=ci`, on `b7ffa9973`:

```
  sweeping 129 gates   [NODE=ci, timeout=420s]
  HERE:  PASS=127  FAIL=0  UNRUN=2   (ran 129 of 129; 129 accounted for)
      [UNRUN] check_quote_pins(timeout>420s)
      [UNRUN] check_receipts_run(stale-cache)
```

`exit 0`, no `ROSTER MISMATCH`. ⌗ **The gate-count reconciliation stands as I filed it at `r7341`:** the
script globs `corpus/check_*.py` and so sweeps **`129` files**, while `gates.yml`'s fast list carries `134`
entries of which `126` are distinct — `8` names appear twice and `3` gate files the fast list never runs
are `check_receipts_run`, `check_tex_tail`, `check_tilt_pins`. **`129` and `134` are both right and they
count different things.**

**THE ROSTER, which is what was asked for:**

    check_absence_claims check_absence_pinned check_absorption check_appendix_current check_arc_columns 
    check_arcpins check_arcs check_banked_config check_bibitem_titles check_branches check_burndown 
    check_cannot_fail check_changelog check_chirality_qualifier check_citation_chain check_citations 
    check_citations_resolve check_claims check_close_names_work check_compile check_computes 
    check_conflict_markers check_cross_row_dupes check_currency check_declared_parts check_deferrals 
    check_deferrals_resolve check_delivered_cites_source check_depmatrix check_depth check_dupes 
    check_env_fingerprint check_exact_counts check_explainer_pins check_family_pointers 
    check_figures_pinned check_figures_shown check_floats_carried check_foreign_ontology 
    check_frontier_current check_gap_is_held check_gate_currency check_generators_parse 
    check_glyph_coverage check_grains check_heads_anchored check_id_bands check_ingestion_current 
    check_killrefs check_kills check_kind check_knob_shadows check_landing_rows_trace 
    check_lead_framings check_leads_follow_rows check_loaders check_loci check_map_dupes 
    check_map_overturns check_marker_buried check_marker_transposition check_model_ledger 
    check_narration_splice check_no_stdlib_shadow check_one_state check_one_value check_open_ledger 
    check_order_acknowledged check_owed_are_tasks check_owed_rows_live check_pages_current 
    check_pages_render check_paper_pins_not_comment_only check_paper_tense check_paststate 
    check_pdf_current check_pin_board check_pins_adjudicated_on_mint check_prose_pins 
    check_protected_dupes check_provenance check_queues check_quote_pins check_receipt_asserts 
    check_receipt_exit check_receipt_home check_receipt_orphans check_receipt_prefixes 
    check_receipt_tex_scope check_receipt_verdicts check_receipts check_receipts_run 
    check_received_at_weight check_register_columns check_register_ids check_register_monotone 
    check_remainder_chains check_rerunnable_honest check_revision_collisions check_revisions_logged 
    check_revleak check_routed check_routed_falsehood check_routing_current check_row_matchers 
    check_row_state check_rows_cite_receipts check_rows_name_the_open check_rows_outward 
    check_rule_current check_self_certification check_settings check_silent check_source_hygiene 
    check_stale_unshown check_status_honesty check_strikes_reported check_superseded_marked 
    check_supersession check_tex_tail check_theatre_currency check_tilt_pins check_unread_figure 
    check_unworked_blockers check_veins check_view_tables check_withdrawals check_withdrawals_propagate 
    check_withdrawn 
## ② ⛔ AND IT COULD ONLY BE RECONSTRUCTED, NOT READ — SO THE ROSTER IS NOW KEPT

`scripts/sweep_gates.sh` asserted its roster and then `rm -f`'d it. A run could therefore **prove** it
covered all `129` names and leave no record of **which** `129`. I was asked for the roster and could only
rebuild it from `ls corpus/check_*.py`; the assertion makes that reconstruction sound, but the run does not
state it. ⇒ ⛭ **Fixed, additively: the roster is copied to `$ROSTER_OUT` (default `/tmp/sweep_roster.txt`)
and printed beside the counts.** *That is `66`'s own `r7343` ② sentence applied to the instrument that
carries it: an instrument that cannot state what it measured is one step short of falsifiable.*

## ③ ⛔⛔ THE FINDING: THE ARBITER'S TIMEOUT EXCLUDES THE PHASE'S OWN RATCHET

`check_quote_pins` came back `UNRUN(timeout>420s)` — and the sweep's header calls an `UNRUN` **"a question
NOT ASKED"**. So I timed it alone on an idle container:

| | |
|---|---|
| `check_quote_pins`, idle, measured | **`947` s**, `rc=0` |
| the sweep's timeout | `420` s |
| the header's calibration (`3×` the slowest, `check_cross_row_dupes` at `128` s) | `384` s → rounded to `420` |

⇒ ***The ratchet needs `2.25×` the timeout and `7.4×` the gate the calibration was built on. It was not
contention: the sweep's own run and this one agree.*** **So every sweep this container has produced has
been silent about the one gate the entire repair phase is measured against** — and this time the `UNRUN`
hid a `PASS`, which is exactly why it is worth saying: *it would hide a red identically, and the phase
would read `FAIL=0` while its ratchet was failing.*

### ⛔⛔ AND THE PART I HAVE TO SAY ABOUT MYSELF: THIS IS MY OWN `r7323` FINDING, ONE SCRIPT OVER, AND I DID NOT RECOGNISE IT UNTIL I READ THE SIBLING

`scripts/run_fast_job.sh` already carries it, in my own words at `r7323`: *"`timeout 420` was written at
`r6500`. `check_quote_pins` joined the fast list at `r7127`, three weeks later, and NOBODY RE-MEASURED.
Measured on this container: that gate takes **`1096.1` seconds and exits `0`** — `2.6×` the budget."* I
fixed that script and **never looked at `sweep_gates.sh`, which carries the same `420` for the same gate.**

⇒ *So the finding above is a REDISCOVERY, and I only caught that it was mine because the cycle told me to
run the fast job and I read it before running it.* ⌗ **The two measurements of the same gate — `1096.1` s at
`r7323`, `947` s here — differ by `14 %`**, which is itself a reason not to set the budget snug against the
newer number.

⌗ **Set to `1800`, matching `run_fast_job.sh` AND ITS REASON rather than a fresh judgement of my own:**
*CI applies **no** per-gate timeout (`NODE=ci python3 corpus/$g.py`, the job capped at
`timeout-minutes: 127`), so a per-gate limit here is a **hang guard and not a budget**, and a budget makes
the sweep disagree with the thing it exists to predict.* **My first value was `1200` on a `27 %`-margin
argument of my own; I withdrew it when I read the sibling, because consistency with the script that already
reasoned this through beats a second opinion derived from one measurement.**

⌗ Two smaller readings from the same run, both stated with their limits: **`check_compile` PASSED** here
(`pdflatex` is present — `/usr/bin/pdflatex`, TeX Live 2023 — so the gate ran rather than being skipped),
against the script's standing warning that it *"FAILS on main with the toolchain present"* — **but I
measured my branch head and not `main`, so this refutes nothing about `main`.** And **`check_tilt_pins`
passed here while `66`'s `r7343` run had it as the one `FAIL`** — consistent with `66`'s diagnosis, since
the defect was a cache at a fixed path and the cache state is per container, which is the defect.

## ④ TWO `P15` GRAIN-MOVES PERFORMED, BOTH VERIFIED BEFORE PERFORMING

*Both rows carried `[GRAIN-MOVE]` from `r7255+cc66.182`: the repaired form already existed in the ledger
and the owed work was to adopt it. `REPAIR-OWED` `268` → **`266`**; `P15`'s owed rows `6` → **`4`**.*

- **`P15_the_expansion_in_the_de_sitter…`** — `'The constant-$\tau$ slice is exactly flat $\mathbb{R}^3$.'`
  → **`'The constant-$\tau$ slice is exactly flat'`**, the grain live in four other `P15` receipts since
  `cc66.172`. *Verified first: the shorter span stands **once raw and once normalised**, so floor `2` is met
  at the shorter length and the dropped words are exposure under "Then stop". The gate's claim is which
  presentation licenses the flat slicing; the diffeomorphism type does not carry it.* `rc=0`.
- **`P15_the_one_fitted_number…`** — the `\ell_A` scan sentence pinned **whole**, with four connectives and
  a `\rcpt` macro → **family Ⓑ's canonical WIDTH RE-CUT**, live in `P15_the_fitted_onset` since `cc66.172`.
  *Verified first: the pattern matches **once** and returns the identical `360.6`, `239.3`, `204`, `208`;
  the gate now asserts the swing (`>100`) and the band (`≤10`, wholly below) rather than the spelling, and
  the citation claim stands on its own macro, which occurs **once**.*
  ⛔ **Cost stated rather than hidden: this trades a prose key for a REGEX-PATTERN key, and floor `2` cannot
  be applied to a pattern** — `r7341+cc66` measured `121` such keys already sitting on a presence ratchet
  whose test cannot reach them. *It is the form the ledger ruled canonical at `r7255`, so it is adopted and
  the cost is recorded at the site.*

⌗ **One observation routed, not acted on:** `P15_the_construction_fixes_no_closed_layer_radius…` still
carries the **long** form of the same literal with verdict `DELIBERATE`, where this row carried the same
literal as `REPAIR-OWED`. *Same literal, two verdicts. I did not change another seat's verdict.*

## ⑤ ⛭⛭ AND `69`'s AMENDED MINIMAND PRICES MY OWN LAST STRIDE: `8` OF `8` RE-REPAIRS FLIP BACK IF THE HOP LANDS

`69` (`62cd99a11`) made the ranked set *"whatever the check can key"*, with the reason that it is not a
sunset clause: **"when it learns to key the locus-scoped form, that form joins the ranking and is preferred
wherever it is shorter."** My `r7337` stride replaced eight locus pairs — which minted **`0`** keys, which
is why `r7341` ① ratified them — with single claim-complete spans. Measured in pinned characters:

| | OLD locus pair | NEW single span | prefers |
|---|---|---|---|
| `C15` | `43` | `59` | OLD |
| `C16`, `C40` | `8` | `62` | OLD |
| `C19`, `C21`⒜ | `46` | `112` | OLD |
| `C21`⒝ | `49` | `98` | OLD |
| `C28` | `50` | `85` | OLD |
| `C38`, `C39` | `212` | `282` | OLD |
| **total** | **`666`** | **`1092`** (`1.64×`) | ⛔ **`8` of `8` flip** |

⇒ ***So the instrument change I recommend re-opens my own eight repairs: landing the hop makes those pairs
keyable, and every one of them is shorter.*** **Eligibility is not an assumption** — each old form asserted
`len([...]) == 1` in the code, which is floor `2`'s exactly-one-locus clause operationally, and the hop keys
both arms of each pair. ⌗ *Nobody has priced this, including me, and it is the first number anyone has put
on what landing the hop costs the repairs already made.*

## ⑥ AND MY ROUTED SCOPE QUESTION IS ANSWERED IN MY FAVOUR, WITH NOTHING TO UNDO

`69` wrote in the narrow reading: the section *"governs what a repair writes, and is not a test applied to
quotations already standing, which steps 1 to 4 decide."* That is what `r7337` ⑤ recommended. ⇒ **My
`305`-of-`977` `P15` floor-`2` figure stands as a COUNT and was never a defect list, and because I
re-verdicted none of those rows there is nothing to reverse now.** *The `28` previously-HELD rows the wide
reading would have re-opened stay held.*
