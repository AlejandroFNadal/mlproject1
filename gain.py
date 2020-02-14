from entropy import *
import numpy as np
from Set import *

def listToSet(List):
	temp=Sets()
	for elem in List:
		temp.addElement(elem)
	return temp
def gain_DF(df, Attr, subfunction):#subfunction 1 Entropy, 2 Gini Index, 3 Misclassification Error
	if subfunction not in [1,2,3]:
			print("Incorrect subfunction parameter")
			return 0
	if subfunction==1:
		ent=entropy_DF(df)
	elif subfunction == 2:
		ent=gini_index(df)
	else:
		if subfunction == 3:
			pass
	i=0
	j=0
	#First, we need to obtain the number of unique values for the attribute. The attribute must be given as a number
	atts=df['Attributes']
	attColumn=atts.str.get(Attr)
	print("Deb")
	print(attColumn.size)
	lonelyValues=attColumn.unique() #get the unique values for the attribute
	print("Lonely values")
	print(lonelyValues)
	print("----")
	sums=np.zeros(len(lonelyValues), dtype=int) #get the count of how many times each attribute repeats in the column
	print("Sums")
	print(sums)
	print("---")
	subsets_list=[]# list of lists of elements
	subsets=[]
	for j in range(0,len(sums)): #check every possible value
		print("printing elements")
		temp_df=pd.DataFrame(columns=['N','Attributes','Class'])
		for i in range(1,attColumn.size): #check the entire column
			if attColumn[i] == lonelyValues[j]:
				sums[j]=sums[j]+1
				#print([df['N'][i],df['Attributes'][i],df['Class'][i]])
				temp_df=temp_df.append([{'N':df['N'][i],'Attributes':df['Attributes'][i],'Class':df['Class'][i]}],ignore_index=True)
		print(temp_df.shape)
		subsets_list.append(temp_df)
	right_term=0
	for j in range(0,len(sums)):
		print("sums j/len(attColumn")
		print(sums[j]/len(attColumn))
		print("---")
		print("entropy of subset")
		print(entropy_DF(subsets_list[j]))
		print("---")
		if subfunction == 1:
			right_term=right_term-(sums[j]/len(attColumn))*entropy_DF(subsets_list[j])
		elif subfunction == 2:
			right_term=right_term-(sums[j]/len(attColumn))*gini_index_list(subsets_list[j])
	return ent+right_term
def gain(dataSet, Attr,subfunction): #subfunction 1 Entropy, 2 Gini Index, 3 Misclassification Error
	if subfunction not in [1,2,3]:
		print("Incorrect subfunction parameter")
		return 0
	if subfunction==1:
		ent=entropy(dataSet)
	elif subfunction == 2:
		ent=gini_index(dataSet)
	else:
		if subfunction == 3:
			pass
	i=0
	j=0
	#First, we need to obtain the number of unique values for the attribute. The attribute must be given as a number
	attColumn=dataSet.getAttColumn(Attr)
	print("attcolumn")
	print(attColumn)
	print("--")
	lonelyValues=np.unique(attColumn) #get the unique values for the attribute
	print("Lonely values")
	print(lonelyValues)
	print("----")
	sums=np.zeros(len(lonelyValues), dtype=int) #get the count of how many times each attribute repeats in the column
	print("Sums")
	print(sums)
	print("---")
	subsets_list=[]# list of lists of elements
	subsets=[]
	for j in range(0,len(sums)): #check every possible value
		print("printing elements")
		temp_list=[]
		for i in range(0,attColumn.size): #check the entire column
			if attColumn[i] == lonelyValues[j]:
				sums[j]=sums[j]+1
				temp_list.append(dataSet.elements[i])
				#temp_Set.addElement(dataSet.elements[i])
		subsets_list.append(temp_list)
	for x in subsets_list:
		#temp_set=Sets()
		for y in x:
			y.printElement()
	##Hasta aca, tenemos las listas andando

	right_term=0
	for j in range(0,len(sums)):
		print("sums j/len(attColumn")
		print(sums[j]/len(attColumn))
		print("---")
		print("entropy of subset")
		print(entropy_list(subsets_list[j]))
		print("---")
		if subfunction == 1:
			right_term=right_term-(sums[j]/len(attColumn))*entropy_list(subsets_list[j])
		elif subfunction == 2:
			right_term=right_term-(sums[j]/len(attColumn))*gini_index_list(subsets_list[j])
	return ent+right_term
