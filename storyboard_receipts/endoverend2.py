import numpy as np
np.set_printoptions(precision=3, suppress=True)
eta=np.diag([-1.,1.,1.]); ip=lambda u,v:u@eta@v
A=np.array([1,1,0])/np.sqrt(2); B=np.array([-1.,-1+np.sqrt(2)/2,-np.sqrt(-0.5+np.sqrt(2))])
E=np.diag([-1.,1.,-1.])   # end-over-end = pi-spin about X1 = T.P2  (proper involution)

print("What end-over-end does to the worldline's ARROW (time-orientation):")
for tau in [-1.,0.,1.]:
    X=np.exp(tau)*A+np.exp(-tau)*B
    Xd=np.exp(tau)*A-np.exp(-tau)*B          # dX/dtau (up to 1/alpha), the arrow
    EXd=E@Xd
    print("  tau=%+.0f: arrow X0-comp = %+.3f  ->  E(arrow) X0-comp = %+.3f  (sign flipped: %s)"%(
        tau, Xd[0], EXd[0], np.sign(Xd[0])!=np.sign(EXd[0])))

print("\nSo end-over-end flips X0 = flips every worldline's time-arrow.")
print("Species read with a fixed future-convention = the wrap sense; flipping the arrow flips it.\n")

print("E on the two null asymptotes A,B:")
print("  E@A =",E@A,"   E@B =",E@B)
# is E@A a past-pointing (X0<0) null dir, i.e. the arrow of A reversed?
print("  A is future (A0=%+.2f); E@A has X0=%+.2f  => %s"%(A[0],(E@A)[0],
      'arrow reversed (future->past)' if (E@A)[0]<0 else 'still future'))

print("\n--- the involution CLASS: different paths, same species swap, different characters ---")
def refl(n): n=np.array(n,float); return np.eye(3)-2*np.outer(n,eta@n)/ip(n,n)
sig=refl(A-B)            # generator-swap: reflection, det -1, timelike axis
T=np.diag([-1.,1.,1.])   # horn flip: reflection, det -1, timelike
for nm,M in [("end-over-end (T.P)",E),("sigma (A<->B)",sig),("T (horn flip)",T)]:
    # does M reverse the arrow? test on tau=0 arrow (A-B direction)
    arrow=A-B; rev = np.sign((M@arrow)[0])!=np.sign(arrow[0])
    print("  %-20s det=%+.0f  reverses time-arrow? %s"%(nm,np.linalg.det(M),rev))
print("\n=> all three reverse the worldline's time-arrow (=> swap species), but they are")
print("   different kinds of map (proper PT vs reflections). 'R' is the whole involution")
print("   class that reverses the arrow / wrap sense; asking its single Lorentzian character")
print("   was malformed. Matter/antimatter = symmetric pair exchanged by ANY of these paths.")

print("\n--- 'end-over-end then swap colours = same figure' : E preserves the surface & pairs")
print("    every worldline with its arrow-reversed (opposite-species) partner ---")
print("  E maps hyperboloid to itself:", np.allclose([ip(E@np.array([np.sinh(s),np.cosh(s)*np.cos(t),np.cosh(s)*np.sin(t)]),
      E@np.array([np.sinh(s),np.cosh(s)*np.cos(t),np.cosh(s)*np.sin(t)]))
      for s in[-1,0,1] for t in[0,1,2]], 
      [ip(np.array([np.sinh(s),np.cosh(s)*np.cos(t),np.cosh(s)*np.sin(t)]),
          np.array([np.sinh(s),np.cosh(s)*np.cos(t),np.cosh(s)*np.sin(t)])) for s in[-1,0,1] for t in[0,1,2]]))
