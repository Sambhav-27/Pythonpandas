import numpy as np
from math import sqrt
import pandas as pd
from collections import Counter
import random



def k_nearest(dataset, predict, k=3): #accepts dict of data with key as groups; prediction data
	if k <= len(dataset): # if k should be greater than total groups
		print("Error")
	distances = []
	for i in dataset:
		for j in dataset[i]:
			d = np.linalg.norm(np.array(j) - np.array(predict)) #calculates eculedian dist b/w predict pt and each pt of dataset; linalg=linearalgebra;
			distances.append([d, i]) # append with their group

	distances = sorted(distances, key=lambda distances:distances[0])
	#for i in distances[:k]: # only first k elements are taken
	#	votes = [i[1]] #take group value of first k dist	
	votes = [i[1] for i in distances[:k]]
	result = Counter(votes).most_common(1)[0][0] # 1: how many top most common u want; [0][0]:cuz it comes like an array of list first 0 specifies which element and 2nd 0 its count
	confidence = Counter(votes).most_common(1)[0][1]/ k  #it is the count of most common ele and if it is equal to 1(i.e. all k neigbor voted in favor of same group) then confidence=1;
	return result

df = pd.read_csv("breast-cancer-wisconsin.data.txt")
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()  #list of list
#print(full_data)
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[],4:[]}
train_data = full_data[:-int(test_size*len(full_data))] # test data is last 20%
test_data = full_data[-int(test_size*len(full_data)):]

#separate train data as belonging to class 2 or class4
for i in train_data:
	train_set[i[-1]].append(i[:-1])
for i in test_data:
	test_set[i[-1]].append(i[:-1])


correct = 0
total = 0
for i in test_set:
	for j in test_set[i]:
		vote = k_nearest(train_set, j, k=5)			
		if i==vote:
			correct+=1
		total+=1


print('accuracy', correct/total)






