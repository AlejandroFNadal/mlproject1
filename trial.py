import csv
import pandas as pd

stri="Thisisastring"
supremeList=[]
with open ("C:/Users/Anastacius/Desktop/mlproject1/training.csv","r") as my_imput_file:
    for line in my_imput_file:
        supremeList.append(list(line))

for x in supremeList:
    print(x)

df=pd.DataFrame(supremeList)