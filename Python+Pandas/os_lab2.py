import pandas as pd
import sqlite3
from math import sqrt
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
 'The Night Listener': 3.0,
 'Robinhood': 0.0,
 'Deadpool':1.0},

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

movie_list=['Lady in the Water','Snakes on a Plane','Just My Luck','Superman Returns','The Night Listener','You, Me and Dupree', 'Robinhood', 'Deadpool']


for user in dataset:    
    for movie in dataset[user]:
        if user=='Toby':
            plt.scatter(movie_list.index(movie),dataset[user][movie], color='r',marker='x', s=100, linewidths=3)
            continue
        plt.scatter(movie_list.index(movie),dataset[user][movie], color='g')
        



################################################################



def reviewed_movies(user):
    i=0
    print('reviewed movies by ', user, 'are: ')
    for movie in dataset[user]:
        print(movie)
        i+=1
    return i




def pearson_correlation(person1, person2):
    both_rated = {}
    #print(person2)
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item]=1

    n = len(both_rated)
    if n==0:
        return 0 # change it zero

    p1_sum = sum([dataset[person1][item] for item in both_rated])
    p2_sum = sum([dataset[person2][item] for item in both_rated])

    p1_sqsum = sum([pow(dataset[person1][item],2) for item in both_rated])
    p2_sqsum = sum([pow(dataset[person2][item],2) for item in both_rated])

    product = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

    num = product - (p1_sum *p2_sum/n)
    denom = sqrt((p1_sqsum - pow(p1_sum,2)/n)*(p2_sqsum- pow(p2_sum,2)/n))
    if denom ==0:
        return 0
    else:
        return num/denom

def most_similar_users(person, number_of_users):
    scores = [(pearson_correlation(person, other_person), other_person) for other_person in dataset if other_person!=person ]
    scores.sort()
    scores.reverse()
    return scores[0:number_of_users]




def user_recommendations(person):
    totals ={}
    simsums = {}
    ranking_list = []
    for other in dataset:
        if other==person:
            continue
        sim = pearson_correlation(person, other)

        if sim <=0:
            continue
        for item in dataset[other]:
            if item not in dataset[person] or dataset[person][item] ==0:
                totals.setdefault(item,0)
                totals[item]+= dataset[other][item]*sim
                simsums.setdefault(item,0)
                simsums[item]+=sim

    rankings = [(total/simsums[item], item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()

    recommendation_list = [(item,score) for score, item in rankings]
    return recommendation_list


def movie_suggestion(user):      
    no_of_reviews = reviewed_movies(user)
    print(no_of_reviews)
    if no_of_reviews<1:
        print("for user1")
        user ='Toby'
    # print(most_similar_users(user, 30))
    x= user_recommendations(user)[:10]   
    print("\n\nsuggested movies:")   
    return x



x = movie_suggestion('Toby')
print('\nMovie name\t\t Predicted rating\t\t movie index\n')
for i in x:
    print(i[0], '  ', i[1], '  ', movie_list.index(i[0]))
plt.show()

