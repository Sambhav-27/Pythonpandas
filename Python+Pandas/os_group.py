import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from math import sqrt
from sklearn import preprocessing
from matplotlib import style
style.use('ggplot')

#we can't calculate precision and accuracy in clustering(unsupervised). We have done this in movie recommender

#goals, meetings, how often you tag each other

# df = pd.read_csv(r'C:\Users\sambhav\Desktop\Oslabfinal\intersect.csv')
# df = df[['gender', 'age_o', 'dec_o', 'field', 'imprelig', 'from', 'income','go_out', 'sports', 'gaming', 'theater', 'music', 'shopping', 'clubbing']]
# print(df.head())
# df.to_csv('my_intersect.csv', index=True)
df = pd.read_csv(r'S:\python_test\my_intersect.csv')


def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df



df = handle_non_numerical_data(df)
# df.fillna(-99999, inplace=True)
df.dropna(inplace=True)
df = df.sample(frac=1).reset_index(drop=True)
print(df.head())



X = np.array(df.drop(['dec_o'], 1).astype(float))
# X = preprocessing.scale(X)
y = np.array(df['dec_o'])



x_train, x_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier(n_neighbors=20)

print(df.head())
clf.fit(x_train, y_train)

accuracy = clf.score(x_test, y_test)
# print(accuracy)


#############################

# X, y = make_blobs(n_samples=200, centers=3, n_features=2, random_state=0)
X = np.load("C:\\Users\\sambhav\\Desktop\\numpy_file_features.npy")
y = np.load("C:\\Users\\sambhav\\Desktop\\numpy_file_labels.npy")


#X = np.array(df[['field','income']])

clf = KMeans(n_clusters=3)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_
colors = ["g.", "r.", "c.", "b.", "k."]

print(X[:1])
xaxis=0
yaxis=1
# int(len(X)*0.2)
for i in range(200):
	print("\n\nCluster No.: ", labels[i], "\tColor: ", colors[labels[i]])
	plt.plot(X[i][xaxis], X[i][yaxis], colors[labels[i]], markersize=8)

plt.scatter(centroids[:,xaxis], centroids[:,yaxis], marker='x', s=10, linewidths=18)

p1=centroids[1,0]+0.5
p2=centroids[1,1]+0.8

w= clf.predict([[p1,p2]])
c=colors[w[0]][0]

plt.scatter(p1,p2, marker='1', color=c,  linewidths=25)
print("\n\nCluster No. for new point : ", w)


plt.show()














