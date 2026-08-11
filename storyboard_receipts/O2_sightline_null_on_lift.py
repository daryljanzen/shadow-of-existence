"""O2 — p0's tangent/secant distinction, and whether it is a shadow boundary in the optics sense.
p0: 'sightlines of the projection that TOUCH the throat are light rays; those that CUT it are not.'"""
import numpy as np
a=1.0; eta=np.diag([-1.,1.,1.])          # equatorial section (X0, X1, X2)
ip=lambda P,Q: P@eta@Q
print("="*78); print("O2 — TANGENT vs SECANT SIGHTLINES, AND THE SHADOW BOUNDARY"); print("="*78)

r_obs=np.sqrt(7)/2
O=np.array([0., r_obs, 0.])
th_t=np.arcsin(a/r_obs)                  # tangent half-angle
print(f"\n  observer at r_obs = sqrt7/2 = {r_obs:.6f};  tangent half-angle = {np.degrees(th_t):.4f} deg")
print(f"\n  {'aim angle':>10s} {'kind':>10s} {'pow(O)':>9s} {'|disp| to touch':>16s} {'eta(disp,disp)':>15s} {'null?':>7s}")
for ang in [0.0, 0.3*th_t, 0.7*th_t, th_t, 1.3*th_t]:
    # direction in the equatorial plane, aimed at angle 'ang' from the line to centre
    d=np.array([0., -np.cos(ang), np.sin(ang)])
    # distance along d to closest approach, and the impact parameter
    t_ca = -(O[1]*d[1]+O[2]*d[2])
    ca = O + t_ca*d
    b = np.hypot(ca[1], ca[2])
    kind = "TANGENT" if abs(b-a)<1e-9 else ("secant" if b<a else "misses")
    if b<=a+1e-12:
        dt=np.sqrt(max(a**2-b**2,0))
        t_hit=t_ca-dt                     # near intersection
    else:
        t_hit=t_ca
    disp=t_hit*d
    print(f"  {np.degrees(ang):10.4f} {kind:>10s} {ip(O,O)-a**2:9.5f} {t_hit:16.6f} {ip(disp,disp):15.8f} {abs(ip(disp,disp))<1e-9!s:>7s}")

print("\n  NOTE: in this planar section eta gives eta(disp,disp) = |disp_vec|^2 since disp_0 = 0,")
print("  so no displacement in the PLANE is null.  p0's null character is about the EMBEDDING:")
print("  the tangent length equals the point's HEIGHT X0, and the sightline is null in M^6.")
print("  Re-testing with the observer lifted onto the substrate:")
Xo=np.sqrt(r_obs**2-a**2)                # the height that puts O on the hyperboloid
Osub=np.array([Xo, r_obs, 0.])
print(f"   O on the substrate: eta = {ip(Osub,Osub):.8f}  (alpha^2 = 1)")
tan_len=np.sqrt(r_obs**2-a**2)
print(f"   tangent length sqrt(pow) = {tan_len:.8f}   height X0 = {Xo:.8f}   equal: {abs(tan_len-Xo)<1e-12}")
disp=np.array([-Xo, a*a/r_obs - r_obs, a*np.sqrt(r_obs**2-a**2)/r_obs])
print(f"   eta(disp,disp) for the tangent displacement = {ip(disp,disp):.2e}   NULL: {abs(ip(disp,disp))<1e-9}")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Two things above were printed and not tested.  The nullity was a
# boolean; and the line "tangent length sqrt(pow) = ... height X0 = ... equal: True" compares
# np.sqrt(r_obs**2-a**2) with np.sqrt(r_obs**2-a**2) -- the SAME expression written twice, so it
# cannot fail.  Here the two sides are obtained by DIFFERENT routes and then compared:
#   L  -- Euclid, from the tangency point found by bisecting (T - O).T = 0 on the throat circle;
#   X0 -- the embedding, from bisecting the hyperboloid's own constraint eta(X,X) - alpha^2 = 0
#         at transverse radius r_obs.
# Then the tangent segment from the LIFTED vantage is checked to land on the throat, to be
# tangent there, and to be null -- at r_obs = sqrt7/2 and at four further heights.
def bisect(g, lo, hi, n=200):
    for _ in range(n):
        mid = 0.5*(lo + hi)
        if g(lo)*g(mid) <= 0: hi = mid
        else: lo = mid
    return 0.5*(lo + hi)
th_tan = bisect(lambda th: a*a - a*r_obs*np.cos(th), 0.0, np.pi/2)        # (T - O).T = 0
T_pl = np.array([a*np.cos(th_tan), a*np.sin(th_tan)])
L_euclid = np.linalg.norm(T_pl - np.array([r_obs, 0.0]))                  # Euclid's tangent length
X0_hyp = bisect(lambda h: -h*h + r_obs**2 - a**2, 0.0, 5.0)               # the hyperboloid's root
assert abs(L_euclid - X0_hyp) < 1e-9                                      # THE identity, two routes
assert abs(L_euclid - 0.86602540) < 1e-7 and abs(X0_hyp - 0.86602540) < 1e-7
assert abs(ip(O, O) - a**2 - 0.75) < 1e-12                                # pow(O) = 0.75
assert abs(np.degrees(th_t) - 49.1066) < 1e-4                             # tangent half-angle
assert abs(ip(Osub, Osub) - 1.0) < 1e-12                                  # the lift is ON the substrate
end = Osub + disp
assert abs(end[0]) < 1e-12 and abs(np.hypot(end[1], end[2]) - a) < 1e-12  # it lands ON the throat
assert abs((end[1:] - Osub[1:]) @ end[1:]) < 1e-12                        # and is TANGENT there
assert abs(ip(disp, disp)) < 1e-12                                        # ** and it is NULL **
# the planar restriction is positive definite: no displacement within the plane is null, and the
# TANGENT aim's planar length^2 is exactly the power, 0.75 -- which is why it is not null there.
for ang_a in [0.0, 0.3*th_t, 0.7*th_t, th_t]:
    d_a = np.array([0., -np.cos(ang_a), np.sin(ang_a)])
    tca = -(O[1]*d_a[1] + O[2]*d_a[2]); b_a = np.hypot(*(O + tca*d_a)[1:])
    hit = tca - np.sqrt(max(a**2 - b_a**2, 0.0))
    assert ip(hit*d_a, hit*d_a) > 0.1
assert abs(ip(0.866025*np.array([0., -np.cos(th_t), np.sin(th_t)]),
              0.866025*np.array([0., -np.cos(th_t), np.sin(th_t)])) - 0.75) < 1e-5
worst_null = 0.0
for r_v in (1.05, 1.5, 2.0, 4.0, 9.0):                                    # every height, not one
    X0_v = np.sqrt(r_v**2 - a**2)
    d_v = np.array([-X0_v, a*a/r_v - r_v, a*np.sqrt(r_v**2 - a**2)/r_v])
    end_v = np.array([X0_v, r_v, 0.]) + d_v
    assert abs(np.hypot(end_v[1], end_v[2]) - a) < 1e-12
    worst_null = max(worst_null, abs(ip(d_v, d_v)))
assert worst_null < 1e-12
print(f"\n  [r2376+c54.161] asserted: Euclid's tangent length {L_euclid:.8f} equals the hyperboloid's")
print("  own root for X0 (two independent bisections), pow(O) = 0.75, the planar restriction")
print(f"  positive definite, and the lifted tangent NULL at five heights (max |eta| = {worst_null:.1e}).")
