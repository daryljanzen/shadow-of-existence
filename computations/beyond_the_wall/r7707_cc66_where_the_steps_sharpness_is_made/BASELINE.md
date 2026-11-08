# `r7707+cc66` — THE PRICE, MEASURED BEFORE THE BLOCK EXISTS

Host: `P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_at_the_visibility.py`
on this tree at `main 986f657cd`, with no `r7707` block.

| rep | wall | verdict |
|---|---|---|
| 1 | **2227 ms** | rc 0, 46 PASS, 0 FAIL |
| 2 | **1990 ms** | rc 0 |
| 3 | **2020 ms** | rc 0 |

⇒ **baseline `2.08` s, spread `±0.12` s.** Three reps rather than one, because `r7705` registered a 5 s
trip-wire against a 331 s receipt and then watched it fire on 2.1 per cent of run-to-run noise. *On a 2 s
receipt the spread is 6 per cent, so a difference under about 0.25 s is not measurable here either — and
the registered 10 s bound is far outside it, which is why that bound is the right one to have registered.*

Registered: **under 10 s added.** If the block lands over that, it takes its own receipt and pays the
landing.
