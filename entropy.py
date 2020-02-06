from Set import *
from math import log2
def entropy(S):
  L=np.unique(S.clas)
  c1=len(S.clas==L[0])
  c2=len(S.clas==L[1])
  c3=len(S.clas==L[2])
  cc=S.clas.size
  l1=log2(c1/cc)*c1/cc
  l2=log2(c2/cc)*c2/cc
  l3=log2(c3/cc)*c3/cc
  E=-(l1+l2+l3)
  return E
  
