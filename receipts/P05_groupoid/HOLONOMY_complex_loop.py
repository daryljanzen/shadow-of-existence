"""Transport the RESIDUE FORM around a Nariai point in the COMPLEX w-plane.
The roots return (splitting field, no monodromy) -- but the FORM's transport can accumulate.
A = -(1/2) G^{-1} dG with G_ii = 1/f'(r_i); f' has a simple zero at the double root -> simple pole in A.
ORIGIN: storyboard_receipts/HOLONOMY_complex_loop.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
al=1.0
def raw(w):
    M2=(2/(3*np.sqrt(3)))*al*np.sin(3*w)
    return np.roots([1,0,-al**2, M2*al**2])
def track_loop(centre, rad, N):
    ths=np.linspace(0,2*np.pi,N)
    ws=centre+rad*np.exp(1j*ths)
    out=[np.sort_complex(raw(ws[0]))]
    for w in ws[1:]:
        r=raw(w); prev=out[-1]; used=[False]*3; cur=np.zeros(3,dtype=complex)
        for i,p in enumerate(prev):
            j=min((j for j in range(3) if not used[j]), key=lambda j: abs(r[j]-p))
            cur[i]=r[j]; used[j]=True
        out.append(cur)
    return ws, np.array(out)
G=lambda r: np.diag(1.0/(3*r**2-al**2))     # complex now, not real part
for rad in (0.30, 0.15, 0.05):
    ws,R=track_loop(np.pi/6, rad, 6000)
    U=np.eye(3,dtype=complex)
    for i in range(len(ws)-1):
        G0,G1=G(R[i]),G(R[i+1]); Gm=0.5*(G0+G1); dG=G1-G0
        U=(np.eye(3)-0.5*np.linalg.solve(Gm,dG))@U
    d=np.diag(U)
    print("   radius %.2f : holonomy diag = %s"%(rad,'  '.join('%+.4f%+.4fi'%(x.real,x.imag) for x in d)))
    print("                |.| = %s    det = %+.4f%+.4fi"%('  '.join('%.4f'%abs(x) for x in d),
          np.linalg.det(U).real, np.linalg.det(U).imag))
    # r2376+c54.158 -- pins the result this receipt exists to report, the one THE_QUANTUM_JOINT
    # quotes as "the FORM picked up diag(1,-1,-1)": transporting the residue form once about the
    # Nariai point returns it with ONE diagonal entry at +1 and TWO at -1 (printed +1.0000,
    # -1.0008, -1.0008), all real to 4 places and of unit modulus, determinant +1 (printed
    # +1.0016).  Two facts are pinned at once -- that the holonomy is NOT the identity (the roots
    # do return, so a -1 here is the form's alone, which is the receipt's claim) and that it is
    # not something else either.  And it is pinned at all three radii 0.30 / 0.15 / 0.05, so it
    # is a holonomy of the loop CLASS and not an artefact of one contour.
    _dre = sorted(x.real for x in d)
    assert abs(_dre[2] - 1.0) < 5e-3, (rad, _dre)
    assert abs(_dre[0] + 1.0) < 5e-3 and abs(_dre[1] + 1.0) < 5e-3, (rad, _dre)
    assert max(abs(x.imag) for x in d) < 5e-3, (rad, d)
    assert abs(float(np.linalg.det(U).real) - 1.0016) < 5e-3, (rad, np.linalg.det(U))
    assert all(abs(abs(x) - 1.0008) < 5e-3 for x in d), (rad, [abs(x) for x in d])
    # and the PREMISE the conclusion rests on, which the receipt states and did not check: the
    # ROOTS themselves return to where they started around this loop (no monodromy -- the sky
    # angle is the splitting field), so the -1's above cannot be the roots' and must be the
    # form's.  Were the roots permuted here, the whole reading of the holonomy would collapse.
    assert float(np.max(np.abs(R[-1] - R[0]))) < 1e-9, (rad, R[0], R[-1])
print()
print("   roots return to themselves (splitting field) -- so any non-identity here is the FORM's,")
print("   not the roots'.  A phase of -1 on a component = the square root branch of 1/f' about a simple zero.")
