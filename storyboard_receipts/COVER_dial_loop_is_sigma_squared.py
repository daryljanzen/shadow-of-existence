"""How does a loop in the DIAL project to the MASS plane?  2M = (2/3sqrt3) a sin 3w.
Near a branch point sin3w = +-1 the map is critical, so the projection winds twice."""
import numpy as np
al=1.0; M2=lambda w:(2/(3*np.sqrt(3)))*al*np.sin(3*w)
c=np.pi/6; rad=0.15; N=2000
ths=np.linspace(0,2*np.pi,N); ws=c+rad*np.exp(1j*ths)
vals=M2(ws)-M2(c)                      # displacement from the critical value
ang=np.unwrap(np.angle(vals))
print("   loop in w: ONE turn about w = pi/6")
print("   image in the 2M-plane winds by %.4f rad = %.3f turns"%(ang[-1]-ang[0],(ang[-1]-ang[0])/(2*np.pi)))
# r2376+c54.158 -- pins the receipt's one computed claim and its printed figure: ONE turn of w
# about the critical point w = pi/6 projects to TWO turns in the 2M-plane -- 12.5664 rad = 2.000
# turns.  This is the whole of P5 rem:perroot as this receipt argues it: the projection is 2-to-1
# there, so one w-loop is sigma^2.  At a REGULAR point of the map the winding would be 1.0000
# turn (6.2832 rad); a winding of 2 is exactly what a simple critical point gives, and nothing
# about the numerics forces it -- the same code at a non-critical centre returns one turn.
assert abs((ang[-1]-ang[0]) - 12.5664) < 1e-3, ang[-1]-ang[0]
assert abs((ang[-1]-ang[0])/(2*np.pi) - 2.0) < 1e-4
assert abs(np.angle(vals[0]) - np.angle(vals[-1])) < 1e-6      # the image loop CLOSES
print()
print("   near sin3w = 1:  2M - 2M_crit  ~  -(9/2)(w - pi/6)^2   -> QUADRATIC, so the map is 2-to-1")
print("   => one w-loop = TWO turns in 2M = sigma^2 = identity in the deck group.")
print("      which is why r2323 found the ROOTS return (sigma^2 = id) ...")
print("      ... while the FORM picked up diag(1,-1,-1): a SQUARE-ROOT effect the roots cannot see.")
print()
print("   and the square roots in question: the transport carries sqrt(G_ii) = sqrt(1/f'(r_i)),")
print("   whose PRODUCT is 1/sqrt(Delta).  The corpus already uses exactly that square root:")
print("   'Delta = 4 - 27(2M)^2 is not a square, so the Galois group is the full S_3' (Harris 1979).")
print("   => V_4 is the PER-ROOT resolution of the same square root the corpus invokes in the product.")
