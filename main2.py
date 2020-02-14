import pandas as pd
from entropy import *
from gain import *
a=pd.read_csv('training.csv', sep=",", names=['N','Attributes','Class']) 

print("Head of Dataset")
print(a.head())

print(gain_DF(a,1,1))
#si=2
#print([a['N'][i],a['Attributes'][i],a['Class'][i]])
#a=a.append([{'N':a['N'][1],'Attributes':a['Attributes'][1],'Class':a['Class'][1]}],ignore_index=True)
#print(a.tail())

