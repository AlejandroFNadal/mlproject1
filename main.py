import numpy as np
from Set import *
from entropy import *
a=np.genfromtxt('mitcheldata.csv',delimiter=',',skip_header=True,dtype=int)
classColumn=a.shape[1] -1 #Get the last column, that is the class

#print("Entire dataset")
#print(a)

data=Set()
data.clas=a[:,classColumn] #Get the last column

#print("Classes")
#print(data.clas)

print(entropy(data))