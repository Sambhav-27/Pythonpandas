import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import style
style.use('ggplot')

X = np.array([[1,2], [1.5,1.8], [5,8], [8,8], [1,0.6], [9,11]])

clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

print(labels)
colors = 2*["g.", "r.", "c.", "b.", "k."]
for i in range(len(X)):
	plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=25)
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=100, linewidths=5)


# t=labels[0]
# print(t)
# for i in range(len(X)):
# 	if(labels[i]==t):
# 		print(X[i][0], X[i][1])

plt.scatter(10,8)
print(clf.predict([[10,8]]))
plt.show()
