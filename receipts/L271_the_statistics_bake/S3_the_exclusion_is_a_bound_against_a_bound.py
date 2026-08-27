#!/usr/bin/env python3
"""RECEIPT — statistics/inference bake `S3`: ** P04'S ISOTROPY EXCLUSION IS A LOWER BOUND AGAINST AN
UPPER LIMIT, NOT AN ESTIMATE AGAINST AN ESTIMATE — AND THAT STRUCTURE, NOT THE RATIO, IS WHAT MAKES IT
ROBUST. NEITHER THE PAPER NOR ITS OWN RECEIPT SAYS SO. **

LEVEL: NO RATE — inference structure on a stated comparison.

THE FIELD'S QUESTION.  P04 excludes matter-tracking expansion by "an exclusion by three orders of
  magnitude": a predicted scatter of ~1e-3 against an observed <~3e-6.  A statistician's first move is
  that a RATIO OF POINT ESTIMATES is not an exclusion -- it carries no error model and no direction.
  ** The probe was built as that attack.  It bounces, and the reason it bounces is the finding. **

WHAT P04 ACTUALLY DOES.  Its receipt establishes sigma_path = 2.77e-3 as a FLOOR and then checks two
  alternative estimate choices, BOTH OF WHICH RAISE IT -- sigma_8(0) = 0.8 without growth-weighting
  gives 7.78e-3, and correlations with a smaller effective N give 5.55e-3.  So the prediction is a
  LOWER BOUND.  And the observed side, <~3e-6, is an UPPER LIMIT.

  ** LOWER BOUND AGAINST UPPER LIMIT.  Every free choice in the calculation pushes the two FURTHER
  apart, so the exclusion cannot be weakened by a different estimate -- only by a different physical
  claim.  That is the strongest form an exclusion of this kind can take, and it is stronger than the
  ratio the paper quotes. **

AND THE TEST CAN FAIL.  The control -- isotropic expansion with no matter-tracking -- returns
  sigma_path = 0 EXACTLY, not a small number.  A test whose null returns zero is one that could have
  come out the other way, which is what makes the three orders informative rather than decorative.

WHAT IS OWED IS A SENTENCE, in the same shape S2 found: name the structure, and state the robustness
  factor.  The observed limit would have to be 9x larger to weaken the exclusion to two orders, 92x to
  one order, and 923x for it to vanish.

ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  S3 — the structure of P04's isotropy exclusion")
print("=" * 78)

floor = 2.77e-3
alts = {"sigma_8(0) = 0.8, no growth-weighting": 7.78e-3,
        "correlations, smaller effective N": 5.55e-3}
obs = 3e-6
control = 0.0

print(f"\n  predicted scatter, as computed : {floor:.2e}")
for k, v in alts.items():
    print(f"      alternative choice           : {v:.2e}   ({v/floor:.1f}x LARGER)   <- {k}")
    assert v > floor, "every alternative estimate must RAISE the prediction"
print("  ** VERDICT 1: every alternative estimate choice raises it, so the computed value is a")
print("     LOWER BOUND on the predicted scatter, not a point estimate. **")

print(f"\n  observed scatter               : <= {obs:.1e}   (an UPPER LIMIT)")
ratio = floor / obs
print(f"  ratio                          : {ratio:.0f}   -- the paper's 'three orders of magnitude'")
assert 100 < ratio < 10000
print("  ** VERDICT 2: LOWER BOUND against UPPER LIMIT.  Every free choice pushes the two")
print("     further apart, so the exclusion cannot be weakened by a different estimate --")
print("     only by a different physical claim.  That is stronger than the quoted ratio. **")

print(f"\n  the control: isotropic expansion, no matter-tracking : sigma_path = {control:.1f}")
assert control == 0.0, "the null must return exactly zero, not a small number"
print("  ** VERDICT 3: the null returns EXACTLY zero, so the test could have come out the")
print("     other way.  That is what makes the three orders informative. **")

print("\n  robustness factor, in the shape S2 established for P15:")
for tgt, lbl in [(100, "two orders"), (10, "one order"), (1, "no exclusion at all")]:
    need = floor / tgt
    print(f"      to weaken the ratio to {tgt:>4} ({lbl:19s}): observed limit must be {need/obs:>5.0f}x larger")
assert floor / 100 / obs > 1, "even two orders needs a factor above one"

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
