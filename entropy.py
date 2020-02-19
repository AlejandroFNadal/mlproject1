from Set import *
from math import log2
import numpy as np

def entropy_DF(df): #works with pandas dataframe
  classes=df['Class']
  L=df['Class'].unique()
  E=0 #contains entropy
  a=0 #a is index of count
  count=np.zeros(L.size,dtype=int) #number of elements of each class
  for x in classes:
    for clas in L:
      #count[a]=len(S.clas==clas)
      if x == clas:
        count[a]+=1
      a+=1
    a=0
  cc=classes.size
  for x in count:
    E=E+log2(int(x)/cc)*x/cc
  E=-E
  return E

def gini_index_list(S):
  classes=np.array([],dtype=int)
  for x in S:
    classes=np.append(classes,[x.clas])
  L=np.unique(classes)
  print(L)
  a=0 #a is index of count
  Gini=0 #contains gini index
  a=0 #a is index of count
  count=np.zeros(L.size,dtype=int) #number of elements of each class
  for x in classes:
    for clas in L:
      if x == clas:
        count[a]+=1
      a+=1
    a=0
  cc=classes.size
  Sum=0
  for x in count:
    Sum=Sum+(int(x)/cc)**2
  Gini=1-Sum
  return Gini

def gini_index(S):#it takes a list of elements
  print("Classes")
  print(S.getClasses())
  print("---")
  classes=S.getClasses()
  L=np.unique(classes) #each class
  Gini=0 #contains gini index
  a=0 #a is index of count
  count=np.zeros(L.size,dtype=int) #number of elements of each class
  for x in classes:
    for clas in L:
      if x == clas:
        count[a]+=1
      a+=1
    a=0
  cc=classes.size
  Sum=0
  for x in count:
    Sum=Sum+(int(x)/cc)**2
  Gini=1-Sum
  return Gini
