import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

dataset={
 'Lisa Rose': {
 'Lady in the Water': 2.5,
 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0,
 'Superman Returns': 3.5,
 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},

 'Gene Seymour': {'Lady in the Water': 3.0,
 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5,
 'Superman Returns': 5.0,
 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
 
 'Michael Phillips': {'Lady in the Water': 2.5,
 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5,
 'The Night Listener': 4.0},

 'Claudia Puig': {'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0,
 'The Night Listener': 4.5,
 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
 
 'Mick LaSalle': {'Lady in the Water': 3.0,
 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0,
 'Superman Returns': 3.0,
 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
 
 'Jack Matthews': {'Lady in the Water': 3.0,
 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0,
 'Superman Returns': 5.0,
 'You, Me and Dupree': 3.5},
 
 'Toby': {'Snakes on a Plane':4.5,
 'You, Me and Dupree':1.0,
 'Superman Returns':4.0}}

movie_list=['Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','The Night Listener','You, Me and Dupree']


for user in dataset:	
	for movie in dataset[user]:
		if user=='Toby':
			plt.scatter(movie_list.index(movie),dataset[user][movie], color='r',marker='x', s=100, linewidths=3)
			continue
		plt.scatter(movie_list.index(movie),dataset[user][movie], color='g')
		



plt.show()
