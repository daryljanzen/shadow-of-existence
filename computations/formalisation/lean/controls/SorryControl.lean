import Mathlib

/-! POSITIVE CONTROL for `check_no_sorry.py`: a theorem that type-checks and proves nothing.
The checker must report this one as resting on `sorryAx`, or it is not a test. Never imported
by `ShadowFormal`. -/

theorem shadow_control_sorry : (1 : ℝ) = 2 := by
  sorry

#print axioms shadow_control_sorry
