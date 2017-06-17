import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
style.use('ggplot')

dataset = { 'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]] }


def k_nearest(dataset, predict, k=3):
	if k <= len(dataset): # if k should be greater than total groups
		print("Erorr")
	distances = []
	for i in dataset:
		for j in dataset[i]:
			d = np.linalg.norm(np.array(j) - np.array(predict)) #calculates eculedian dist b/w predict pt and each pt of dataset; linalg=linearalgebra;
			distances.append([d, i]) # append with their group

	distances = sorted(distances, key=lambda distances:distances[0])
	#for i in distances[:k]: # only first k elements are taken
	#	votes = [i[1]] #take groups of first k dist
	votes = [i[1] for i in distances[:k]]
	result = Counter(votes).most_common(1)[0][0] # 1: how many top most common u want; [0][0]:cuz it comes like an array of list
	return result

predict = [5,6]
result = k_nearest(dataset, predict, k=3)
print(result)

for i in dataset:
		for j in dataset[i]:
			plt.scatter(j[0],j[1], s=20, color=i)#x,y,point radius,color
plt.scatter(predict[0], predict[1], s=100)
plt.show()