def load_dataset():
	return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createc1(dataset):
	# create a list of candidate 1-itemset
	c1 =[]
	for transaction in dataset:
		for item in transaction:
			if not [item] in c1:  # item is int [item] is list
				c1.append([item])

	c1.sort()
	return list(map(frozenset, c1))


def scanD(dataset, candidates, min_support):
	#returns candidates in dataset having atleast min_support
	sscnt = {}
	for tid in dataset:
		for can in candidates:
			if can.issubset(tid):
				sscnt.setdefault(can, 0)
				sscnt[can]+=1
	
	num_items = float(len(list(dataset)))
	

	retlist = []
	support_data = {}
	if num_items==0:
		return retlist, support_data

	for key in sscnt:
		support = sscnt[key]/num_items
		if support >= min_support:
			retlist.insert(0, key)
		support_data[key] = support
	return retlist, support_data




def aprioriGen(lk, k):
	retlist =[]
	lenlk = len(lk)
	for i in range(lenlk):
		for j in range(i+1, lenlk):
			L1 = list(lk[i])[:k-2]
			L2 = list(lk[j])[:k-2]
			L1.sort()
			L2.sort()
			if L1==L2:
				retlist.append(lk[i] | lk[j])  #| is union
	return retlist



def apriori(dataset, minsupport=0.5):
	c1 = createc1(dataset)
	# print(c1)
	
	D = list(map(set, dataset))
	# print(D, "\n\n")
	L1, support_data = scanD(D, c1, minsupport)
	#print(L1)
	L = [L1] #necessary
	k = 2
	while(len(L[k-2]) > 0):
		ck = aprioriGen(L[k-2], k)
		Lk, supk = scanD(D, ck, minsupport)
		support_data.update(supk)
		L.append(Lk)
		k+=1

	return L, support_data


L, support_data =apriori(load_dataset())
print(L, "\n\n", support_data)
