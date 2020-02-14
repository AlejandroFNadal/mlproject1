import numpy as np
from Set import *
from entropy import *
from gain import *
from element import *
import pandas as pd

a=pd.read_csv('mitcheldata.csv',header=0,index_col=0, sep=",") 
#header =0 overrides the column names, index_col=0 makes the first column to be an index
a=np.genfromtxt('mitcheldata.csv',delimiter=',',skip_header=True,dtype=int)
classColumn=a.shape[1] -1 #Get the last column, that is the class

#print("Entire dataset")
#print(a)

data=Sets()
data.clas=a[:,classColumn] #Get the last column
data.attributes=a[:,1:classColumn] #Get the attributes
print("A.shape[0]")
print(a.shape[0])
for i in range(0,a.shape[0]): #run the matrix going down
    tempObj=Element(a[i][0],a[i][1:classColumn],a[i][classColumn])#id, atts and class
    data.elements.append(tempObj)

print("Entropy of complete Set")
print(entropy(data))
print("---")
print(gain(data,1,1))
