
def gain(Set, Attr):
	ent=calc_entropy(Set)
	i=0
	j=0
	sums=[0,0,0,0]
	subsets[[],[],[],[]]
	values=["A","C","T","D"]
	for j in range(0,len(sums)):
		
		for i in range(0,len(Set)):
			if Set[i][Attr] == values[j]
				sums[j]++
				subsets[j].append(Set[i])
	
	for j in range(0,len(sums)):
		right_term=right_term-(sums[j]/len(Set))*calc_entropy(subset[j])
	
	return ent-right_term
