import numpy as np
from Set import *
from entropy import *
from gain import *
from element import *
a=np.genfromtxt('mitcheldata.csv',delimiter=',',skip_header=True,dtype=int)
classColumn=a.shape[1] -1 #Get the last column, that is the class

#print("Entire dataset")
#print(a)

data=Set()
data.clas=a[:,classColumn] #Get the last column
data.attributes=a[:,1:classColumn] #Get the attributes
print("A.shape[0]")
print(a.shape[0])
for i in range(0,a.shape[0]): 
    tempObj=Element(a[i][0],a[i][1:classColumn],a[i][classColumn])
    data.elements.append(tempObj)

print("data elements")
print(data.elements)
print("-----")
#print(gain(data,2))
#print(data.attributes)
#print("Classes")
#print(data.clas)
print(entropy(data))