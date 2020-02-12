from entropy import entropy
import numpy as np
def gain(dataSet, Attr):
	ent=entropy(dataSet)
	i=0
	j=0
	#First, we need to obtain the number of unique values for the attribute. The attribute must be given as a number
	lonelyValues=np.unique(dataSet.attributes[Attr])
	sums=np.zeros(len(lonelyValues), dtype=int)
	subsets=[[],[],[],[]]
	for j in range(0,len(sums)): #check every possible value
		
		for i in range(0,dataSet.attributes.shape[0]): #
			if dataSet.attributes[Attr][i] == lonelyValues[j]:
				sums[j]=sums[j]+1
				subsets[j].append(dataSet.attributes[i])
	
	for j in range(0,len(sums)):
		right_term=right_term-(sums[j]/len(dataSet))*entropy(subsets[j])
	
	return ent-right_term
