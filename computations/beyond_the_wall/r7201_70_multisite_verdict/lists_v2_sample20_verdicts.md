# E3 precision — a seeded sample of 20 v2 collections (`random.seed(7201)`, `lists_v2_sample20.tsv`), read by hand

- **PIN** means the strings are tested against text another seat owns (`in`, `.count`, `re.search`, a `\rcpt{}`
  marker), which is the `r7197` object.
- **NOT** means labels, table rows, filenames, configuration tags or variant names.

| # | receipt | collection | verdict |
|---|---|---|---|
| 1 | `P15_the_refit_bound_figures…` | `CFG` | NOT: configuration tags |
| 2 | `S50_the_counterterm_basis…` | `STANDING` | **PIN**: "standing-sentence checks" against p0's text |
| 3 | `P15_the_four_dimensional_treatment…` | `HARM` | NOT: harmonic labels |
| 4 | `P10_the_coefficient_is_zero…` | `reasons` | NOT: printed reasons |
| 5 | `P15_all_three_projections…` | `LOSMARK` | **PIN**: `m in BODY` (a source text) |
| 6 | `P08_the_selection_principle…` | `ANSWERS` | NOT |
| 7 | `P03_batch1_cheap_owed` | `TESTS` | NOT: test-name labels |
| 8 | `P15_the_seam_sec_envelope_means…` | `_ONEPT_ARMS` | **PIN**: `b15.count(a)` against P15 |
| 9 | `V1_a_translation_table…` | `SURVEYED` | NOT: filenames |
| 10 | `K45_span_and_nariai` | `rows` | NOT: labelled table |
| 11 | `P03_winding_and_closure` | `checks` | NOT |
| 12 | `P15_the_corpus_places_every_perturbation_source…` | `OWED` | **PIN**: `_p15_then.count(ph) == 1` |
| 13 | `P15_the_two_data_are_one` | `here` | **PIN**: `h in _p7n` |
| 14 | `P1_the_transplanckian_claim…` | `QUALIFIED` | **PIN**: `re.search(QUALIFIED[1], P1)` |
| 15 | `S1_the_stability_bracket…` | `CITES` | UNCLEAR: literature identifiers, matched indirectly |
| 16 | `P14_the_compact_faces_four…` | `_has_singlet` | NOT |
| 17 | `S6_an_unread_figure…` | `TABLE` | NOT |
| 18 | `P15_the_free_streaming_knob…` | `READS_ARM` | NOT: column names |
| 19 | `P15_the_first_peak_figure…` | `VARIANTS` | NOT |
| 20 | `P10_sec_lock_quotes…` | `N` | **PIN** (token tier): `'\rcpt{' + N[k] in tex` |

**7 PIN, 12 NOT, 1 UNCLEAR: about 35% precision.**  Every PIN is a loop or index variable reaching one of the
operator's own site forms (`in`, `.count`, `re.search`, `.find`).  ⇒ *The precise build is not v2's route rule.  It
is the operator resolving a loop variable, or a constant subscript, back to the module-level string collection it
ranges over, and keying each string as `(receipt, string)`.*
