exec(open('gen2.py').read())
import pickle
fnargs,names,derivs=pickle.load(open('fa2.pkl','rb'))
fnargs.update(pickle.load(open('fa1.pkl','rb')))
UNF='simp only [kds_P, kds_D, kds_Q, kds_S, kds_X]'
Y1,Y2='(y 1)','(y 2)'
def c(n,rr=Y1,xx=Y2): return call(n,rr,xx)
o=[]
o.append(f"""/-- **Kerr–de Sitter** in Boyer–Lindquist form with `x = cos θ`, on `(t, r, x, φ)`:
`g = −(Δ_r/ρ²Ξ²)(dt − a(1−x²)dφ)² + (Δ_x(1−x²)/ρ²Ξ²)(a dt − (r²+a²)dφ)² + (ρ²/Δ_r)dr² + ρ²/(Δ_x(1−x²)) dx²`. -/
noncomputable def rn_kds (a M L : ℝ) (y : Fin 4 → ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![{c('kds_g00')}, 0, 0, {c('kds_g03')};
    0, {c('kds_g11')}, 0, 0;
    0, 0, {c('kds_g22')}, 0;
    {c('kds_g03')}, 0, 0, {c('kds_g33')}]
""")
HY="(hP : kds_P a (y 1) (y 2) ≠ 0) (hD : kds_D a M L (y 1) ≠ 0) (hQ : kds_Q a L (y 2) ≠ 0)\n    (hS : kds_S (y 2) ≠ 0) (hX : kds_X a L ≠ 0)"
IU="kds_i00 kds_i03 kds_i33 kds_i11 kds_i22 kds_g00 kds_g03 kds_g33 kds_g11 kds_g22".split()
o.append(f"""lemma kds_inv {{a M L : ℝ}} {{y : Fin 4 → ℝ}} {HY} :
    (rn_kds a M L y)⁻¹ = !![{c('kds_i00')}, 0, 0, {c('kds_i03')};
      0, {c('kds_i11')}, 0, 0;
      0, 0, {c('kds_i22')}, 0;
      {c('kds_i03')}, 0, 0, {c('kds_i33')}] := by
  refine Matrix.inv_eq_left_inv ?_
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rn_kds, Matrix.mul_apply, Fin.sum_univ_four]
  all_goals simp only [{', '.join(IU)}]
  all_goals field_simp
  all_goals simp only [kds_P, kds_D, kds_Q, kds_S]
  all_goals ring
""")
def T(A,B,C):
  key=(A,min(B,C),max(B,C))
  return c(names[key][0]) if key in names else '0'
rows=[]
for A in range(4):
  rows.append('![' + ', '.join('![' + ', '.join(T(A,B,C) for C in range(4)) + ']' for B in range(4)) + ']')
o.append("/-- The Christoffel table of `rn_kds`: twenty independent non-zero entries. -/\nnoncomputable def kds_T (a M L : ℝ) (y : Fin 4 → ℝ) : Fin 4 → Fin 4 → Fin 4 → ℝ :=\n  ![" + ',\n    '.join(rows) + ']\n')
# metric derivative facts
mh={'kds_g00':['hP','hX'],'kds_g03':['hP','hX'],'kds_g33':['hP','hX'],'kds_g11':['hD'],'kds_g22':['hQ','hS']}
def lemargs(nm,v,rr,xx,hs):
  ag=fnargs[nm]; la=[s for s in ARGS if s in ag or s==v]
  return ' '.join({r:rr,x:xx}.get(s,str(s)) for s in la)+' '+' '.join(hs)
md=[]
k=0
for nm in ['kds_g00','kds_g03','kds_g33','kds_g11','kds_g22']:
  for v in (r,x):
    if nm=='kds_g11' and v==x: hs=['hP'] 
    # hyps = denominators: recompute
    k+=1
    md.append((nm,v,k))
GN=' '.join(n for n,_ in names.values())
print('\n'.join(o))
pickle.dump(None,open('x.pkl','wb'))
o=[]
def hs_of(nm):
  e=None
  for k,(n,ee) in names.items():
    if n==nm: e=ee
  num,den=sp.fraction(e)
  return [atom_hyp[A] for A in [P,D,Q,S,X] if den.has(A)]
mhs={'kds_g00':['hP','hX'],'kds_g03':['hP','hX'],'kds_g33':['hP','hX'],'kds_g11':['hD'],'kds_g22':['hQ','hS']}
def dfact(nm,v,hs,pt):
  # pt: ('(y 1)','(y 2)')
  rr,xx=pt
  ag=fnargs[nm]; la=[s for s in ARGS if s in ag or s==v]
  argstr=' '.join({r:rr,x:xx}.get(s,str(s)) for s in la)
  return f"({nm}_d{v} {argstr} {' '.join(hs)}).deriv"
mfacts=[dfact(nm,v,mhs[nm],(Y1,Y2)) for nm in mhs for v in (r,x)]
o.append(f"""set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
lemma kds_Γ {{a M L : ℝ}} {{y : Fin 4 → ℝ}} {HY} (A B C : Fin 4) :
    kr_Γ (rn_kds a M L) y A B C = kds_T a M L y A B C := by
""" + ''.join(f"  have e{i} := {f}\n" for i,f in enumerate(mfacts)) + f"""  simp only [kr_Γ, kds_inv hP hD hQ hS hX]
  fin_cases A <;> fin_cases B <;> fin_cases C <;>
    simp [kr_pd, rn_kds, kds_T, Function.update_apply, Fin.sum_univ_four, {', '.join(f'e{i}' for i in range(len(mfacts)))}]
  all_goals (try simp only [{', '.join(IU)}, {', '.join(n for n,_ in names.values())}])
  all_goals field_simp
  all_goals {UNF}
  all_goals ring
""")
o.append("""/-- The data at a point: `ρ², Δ_r, Δ_x, 1 − x², Ξ ≠ 0`. -/
structure kds_Hyp (a M L : ℝ) (x : Fin 4 → ℝ) : Prop where
  hP : kds_P a (x 1) (x 2) ≠ 0
  hD : kds_D a M L (x 1) ≠ 0
  hQ : kds_Q a L (x 2) ≠ 0
  hS : kds_S (x 2) ≠ 0
  hX : kds_X a L ≠ 0

lemma kds_Hyp.U {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) : ∀ᶠ y in 𝓝 x, kds_Hyp a M L y := by
  have cP : Continuous fun y : Fin 4 → ℝ => kds_P a (y 1) (y 2) := by unfold kds_P; fun_prop
  have cD : Continuous fun y : Fin 4 → ℝ => kds_D a M L (y 1) := by unfold kds_D; fun_prop
  have cQ : Continuous fun y : Fin 4 → ℝ => kds_Q a L (y 2) := by unfold kds_Q; fun_prop
  have cS : Continuous fun y : Fin 4 → ℝ => kds_S (y 2) := by unfold kds_S; fun_prop
  filter_upwards [cP.continuousAt.eventually_ne h.hP, cD.continuousAt.eventually_ne h.hD,
    cQ.continuousAt.eventually_ne h.hQ, cS.continuousAt.eventually_ne h.hS] with y h1 h2 h3 h4
  exact ⟨h1, h2, h3, h4, h.hX⟩

lemma kds_pd {a M L : ℝ} {x : Fin 4 → ℝ} (h : kds_Hyp a M L x) (A B C d : Fin 4) :
    kr_pd (fun y => kr_Γ (rn_kds a M L) y A B C) x d = kr_pd (fun y => kds_T a M L y A B C) x d :=
  kr_pd_congr (h.U.mono fun _ hy => kds_Γ hy.hP hy.hD hy.hQ hy.hS hy.hX A B C)
""")
gfacts=[dfact(nm,v,hs_of(nm),('(x 1)','(x 2)')) for nm,v,_ in derivs]
o.append(f"""set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
/-- **Row 4a.** Kerr–de Sitter is vacuum-`Λ`: `R_μν = Λ g_μν`, all sixteen components. -/
theorem kds_vacuum {{a M L : ℝ}} {{x : Fin 4 → ℝ}} (h : kds_Hyp a M L x) (μ ν : Fin 4) :
    rn_Ric (rn_kds a M L) x μ ν = L * rn_kds a M L x μ ν := by
  have hP := h.hP; have hD := h.hD; have hQ := h.hQ; have hS := h.hS; have hX := h.hX
  have hΓ := kds_Γ hP hD hQ hS hX
""" + ''.join(f"  have f{i} := {f}\n" for i,f in enumerate(gfacts)) + f"""  fin_cases μ <;> fin_cases ν <;>
  · unfold rn_Ric kr_Riem
    simp only [Fin.sum_univ_four, kds_pd h, hΓ]
    simp [kds_T, kr_pd, Function.update_apply, rn_kds, {', '.join(f'f{i}' for i in range(len(gfacts)))}]
    all_goals (try simp only [{', '.join(IU)}, {', '.join(n for n,_ in names.values())}])
    all_goals field_simp
    all_goals {UNF}
    all_goals ring
""")
print('\n'.join(o))
o=[]
o.append(f"""set_option maxHeartbeats 0 in
set_option linter.unusedSimpArgs false in
lemma kds_const_curv_aux {{a M L : ℝ}} {{x : Fin 4 → ℝ}} (h : kds_Hyp a M L x) (hM : M = 0) (A B C D : Fin 4) :
    kr_Rlow (rn_kds a M L) x A B C D =
      L / 3 * (rn_kds a M L x A C * rn_kds a M L x B D - rn_kds a M L x A D * rn_kds a M L x B C) := by
  have hP := h.hP; have hD := h.hD; have hQ := h.hQ; have hS := h.hS; have hX := h.hX
  have hΓ := kds_Γ hP hD hQ hS hX
""" + ''.join(f"  have f{i} := {f}\n" for i,f in enumerate(gfacts)) + f"""  have hpd := kds_pd h
  subst hM
  fin_cases A <;> fin_cases B <;> fin_cases C <;> fin_cases D <;>
  · unfold kr_Rlow kr_Riem
    simp only [Fin.sum_univ_four, hpd, hΓ]
    simp [kds_T, kr_pd, Function.update_apply, rn_kds, {', '.join(f'f{i}' for i in range(len(gfacts)))}]
    all_goals (try simp only [{', '.join(IU)}, {', '.join(n for n,_ in names.values())}])
    all_goals field_simp
    all_goals {UNF}
    all_goals ring_nf
    all_goals simp

/-- **Row 4c.** The mass-free, rotation-only member (`M = 0`, any `a`) is maximally symmetric:
`R_{{abcd}} = (Λ/3)(g_ac g_bd − g_ad g_bc)`, all 256 components. -/
theorem kds_const_curv {{a L : ℝ}} {{x : Fin 4 → ℝ}} (h : kds_Hyp a 0 L x) (A B C D : Fin 4) :
    kr_Rlow (rn_kds a 0 L) x A B C D =
      L / 3 * (rn_kds a 0 L x A C * rn_kds a 0 L x B D - rn_kds a 0 L x A D * rn_kds a 0 L x B C) :=
  kds_const_curv_aux h rfl A B C D
""")
print('\n'.join(o))
