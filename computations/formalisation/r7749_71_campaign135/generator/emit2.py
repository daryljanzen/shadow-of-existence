exec(open('genc.py').read())
import pickle
fnargs,mder,gder,GN,RN=pickle.load(open('p1.pkl','rb'))
def call(name,rr='(y 2)',pp='(y 3)'):
  return '('+name+' '+argstr(fnargs[name],rr,pp)+')'
def fact(rec,rr,pp):
  name,v,la,hyps=rec
  return f"({name}_d{v} {argstr(la,rr,pp)} {' '.join(hyps)}).deriv"
o=[]
o.append(f"""/-- The separable (Carter) cut `eq:carter` on `(τ, σ, r, p)`, with `Δ_r = R(r)` and `Δ_p = P(p)`:
`Σ/Δ_r dr² + Σ/Δ_p dp² + (1/Σ)[Δ_r(dτ − p²dσ)² − Δ_p(dτ + r²dσ)²]`. -/
noncomputable def rn_car (R P : ℝ → ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![{call('car_g00')}, {call('car_g01')}, 0, 0;
    {call('car_g01')}, {call('car_g11')}, 0, 0;
    0, 0, {call('car_g22')}, 0;
    0, 0, 0, {call('car_g33')}]
""")
NZ="(hS : car_S (y 2) (y 3) ≠ 0) (hR0 : R (y 2) ≠ 0) (hP0 : P (y 3) ≠ 0)"
GD="car_g00 car_g01 car_g11 car_g22 car_g33".split(); ID="car_i00 car_i01 car_i11 car_i22 car_i33".split()
o.append(f"""lemma car_inv {{R P : ℝ → ℝ}} {{y : Fin 4 → ℝ}} {NZ} :
    (rn_car R P y)⁻¹ = !![{call('car_i00')}, {call('car_i01')}, 0, 0;
      {call('car_i01')}, {call('car_i11')}, 0, 0;
      0, 0, {call('car_i22')}, 0;
      0, 0, 0, {call('car_i33')}] := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rn_car, Matrix.mul_apply, Fin.sum_univ_four]
  all_goals simp only [{', '.join(ID+GD)}]
  all_goals field_simp
  all_goals simp only [car_S]
  all_goals ring
""")
def T(a,b,c):
  k=(a,min(b,c),max(b,c))
  return call(GN[k]) if k in GN else '0'
rows=['![' + ', '.join('![' + ', '.join(T(a,b,c) for c in range(4)) + ']' for b in range(4)) + ']' for a in range(4)]
o.append("/-- The Christoffel table of `rn_car`. -/\nnoncomputable def car_T (R R1 P P1 : ℝ → ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=\n  ![" + ',\n    '.join(rows) + ']\n')
mf=[fact(rec,'(y 2)','(y 3)') for rec in mder]
GNs=', '.join(sorted(set(GN.values())))
o.append(f"""set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
lemma car_Γ {{R R1 P P1 : ℝ → ℝ}} (hR : ∀ t, HasDerivAt R (R1 t) t) (hP : ∀ t, HasDerivAt P (P1 t) t)
    {{y : Fin 4 → ℝ}} {NZ} (A B C : Fin 4) :
    kr_Γ (rn_car R P) y A B C = car_T R R1 P P1 y A B C := by
""" + ''.join(f"  have e{i} := {f}\n" for i,f in enumerate(mf)) + f"""  simp only [kr_Γ, car_inv hS hR0 hP0]
  fin_cases A <;> fin_cases B <;> fin_cases C <;>
    simp [kr_pd, rn_car, car_T, Function.update_apply, Fin.sum_univ_four, {', '.join(f'e{i}' for i in range(len(mf)))}]
  all_goals (try simp only [{', '.join(ID+GD)}, {GNs}])
  all_goals field_simp
  all_goals simp only [car_S]
  all_goals ring
""")
o.append("""/-- The data: `R′ = R1`, `R1′ = R2`, `P′ = P1`, `P1′ = P2` everywhere; `Σ, R, P ≠ 0` at the point. -/
structure car_Hyp (R R1 R2 P P1 P2 : ℝ → ℝ) (x : Fin 4 → ℝ) : Prop where
  hR : ∀ t, HasDerivAt R (R1 t) t
  hR1 : ∀ t, HasDerivAt R1 (R2 t) t
  hP : ∀ t, HasDerivAt P (P1 t) t
  hP1 : ∀ t, HasDerivAt P1 (P2 t) t
  hS : car_S (x 2) (x 3) ≠ 0
  hR0 : R (x 2) ≠ 0
  hP0 : P (x 3) ≠ 0

lemma car_Hyp.U {R R1 R2 P P1 P2 : ℝ → ℝ} {x : Fin 4 → ℝ} (h : car_Hyp R R1 R2 P P1 P2 x) :
    ∀ᶠ y in 𝓝 x, car_S (y 2) (y 3) ≠ 0 ∧ R (y 2) ≠ 0 ∧ P (y 3) ≠ 0 := by
  have cS : Continuous fun y : Fin 4 → ℝ => car_S (y 2) (y 3) := by unfold car_S; fun_prop
  have cR : Continuous R := continuous_iff_continuousAt.2 fun t => (h.hR t).continuousAt
  have cP : Continuous P := continuous_iff_continuousAt.2 fun t => (h.hP t).continuousAt
  have cR' : Continuous fun y : Fin 4 → ℝ => R (y 2) := cR.comp (continuous_apply 2)
  have cP' : Continuous fun y : Fin 4 → ℝ => P (y 3) := cP.comp (continuous_apply 3)
  filter_upwards [cS.continuousAt.eventually_ne h.hS, cR'.continuousAt.eventually_ne h.hR0,
    cP'.continuousAt.eventually_ne h.hP0] with y h1 h2 h3
  exact ⟨h1, h2, h3⟩

lemma car_pd {R R1 R2 P P1 P2 : ℝ → ℝ} {x : Fin 4 → ℝ} (h : car_Hyp R R1 R2 P P1 P2 x) (A B C d : Fin 4) :
    kr_pd (fun y => kr_Γ (rn_car R P) y A B C) x d = kr_pd (fun y => car_T R R1 P P1 y A B C) x d :=
  kr_pd_congr (h.U.mono fun _ hy => car_Γ h.hR h.hP hy.1 hy.2.1 hy.2.2 A B C)
""")
def cx(n): return call(n,'(x 2)','(x 3)')
o.append(f"""/-- The Ricci tensor of the separable cut, in terms of `R, R′, R″, P, P′, P″`. -/
noncomputable def car_RicM (R R1 R2 P P1 P2 : ℝ → ℝ) (x : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![{cx('car_Ric00')}, {cx('car_Ric01')}, 0, 0;
    {cx('car_Ric01')}, {cx('car_Ric11')}, 0, 0;
    0, 0, {cx('car_Ric22')}, 0;
    0, 0, 0, {cx('car_Ric33')}]
""")
gf=[fact(rec,'(x 2)','(x 3)') for rec in gder]
RNs="car_Ric00 car_Ric01 car_Ric11 car_Ric22 car_Ric33"
o.append(f"""set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
/-- **The Ricci tensor of `eq:carter`** for arbitrary structure functions, from the coordinate Riemann tensor. -/
theorem car_Ric {{R R1 R2 P P1 P2 : ℝ → ℝ}} {{x : Fin 4 → ℝ}} (h : car_Hyp R R1 R2 P P1 P2 x) :
    rn_Ric (rn_car R P) x = car_RicM R R1 R2 P P1 P2 x := by
  have hR := h.hR; have hR1 := h.hR1; have hP := h.hP; have hP1 := h.hP1
  have hS := h.hS; have hR0 := h.hR0; have hP0 := h.hP0
  have hΓ := car_Γ hR hP hS hR0 hP0
""" + ''.join(f"  have f{i} := {f}\n" for i,f in enumerate(gf)) + f"""  ext μ ν
  fin_cases μ <;> fin_cases ν <;>
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, car_pd h, hΓ]
    simp [car_T, kr_pd, Function.update_apply, car_RicM, {', '.join(f'f{i}' for i in range(len(gf)))}]
    all_goals (try simp only [{GNs}, {RNs.replace(' ',', ')}])
    all_goals field_simp
    all_goals (try simp only [car_S])
    all_goals ring
""")
print('\n'.join(o))
