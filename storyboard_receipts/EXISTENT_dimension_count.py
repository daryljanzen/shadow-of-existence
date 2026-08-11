"""The EXISTENT is S_t: a 3-dimensional RIEMANNIAN manifold advancing in cosmic time.
What continuous symmetry can act on it, and can su(3)?"""
print("   THE EXISTENT (ontology index): S_t, a smooth THREE-dimensional RIEMANNIAN manifold (S_t,h_t),")
print("   advancing in cosmic time.  Spacetime (M,g) is THE REPRESENTATION, not an existent.")
print()
print("   su(3): smallest faithful real representation has dimension 6 (C^3 = R^6).")
print()
print("      acting on                       dimension   admits a faithful su(3)?")
for name,d in (("the layer's tangent space",3),("the substrate's rotation group SO(5)",5),
               ("the substrate dS_5",5),("the ambient M^6",6)):
    print("      %-32s %-11d %s"%(name,d,'yes (6 available)' if d>=6 else 'NO -- needs 6'))
print()
print("   => the layer, the EXISTENT, offers 3 dimensions.  The substrate's rotation group offers 5.")
print("      Both are below the 6 a faithful su(3) requires.  The layer closes HARDER than the substrate.")
print()
print("   and note what this does NOT say: it is a statement about a FAITHFUL action on those spaces,")
print("   not about a bundle over them.  A rank-3 complex bundle over a 3-manifold carries su(3) freely;")
print("   the corpus's point is that such a bundle is IMPOSED, not read off the geometry.")
