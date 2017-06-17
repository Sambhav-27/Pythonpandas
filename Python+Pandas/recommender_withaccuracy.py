import pandas as pd
import sqlite3
from math import sqrt
import random

# cnx = sqlite3.connect('db.sqlite3')
# cnx = sqlite3.connect('S:\python_test\winerama\db.sqlite3') 
# df = pd.read_sql_query("select * from reviews_review", cnx)
# df2 = pd.read_sql_query("select * from reviews_wine", cnx)

# # print(df.head(), "\n\n")
# # print(df2.head(), "\n\n")


df = pd.read_csv('S:\python_test\my_movie_reviews.csv')
df2 = pd.read_csv('S:\python_test\movies.csv')
df3 = pd.read_csv(r'S:\python_test\users.csv')

# print(df.head())
# print(df2.head())

dataset={}
t={}
for i in range(len(df)):
    t[df['wine_id'][i]]=df['rating'][i]
    #print(t)
    
    j=0
    if i<len(df)-1:
        j=i+1
    if df['user_name'][i]!=df['user_name'][j]:
        dataset[df['user_name'][i]]=t
        #print("\n")
        t={}
    



##### splitting in training and test data
train = {}
test = {}
for i in dataset:
    ds = dataset.get(i, None)
    t={}
    for j in range(int(0.2*len(ds))):
        x = random.choice(list(ds.keys()))
        y = ds.pop(x)
        t[x]=y
    train[i]=ds
    test[i]=t

##############################


def movie_name(movie_ids):
    for i in movie_ids:
        for j in range(len(df2)):
            if df2['id'][j]==i:
                print(df2['name'][j])

def single_name(iid):
    for j in range(len(df2)):
        if df2['id'][j]==iid:
            return df2['name'][j]



def reviewed_movies(user):
    movie_id=[]
    for i in range(len(df)):
        if df['user_name'][i]==user:
            movie_id.append(df['wine_id'][i])
    print("\n\nreviewed movies: ")
    #movie_name(movie_id)
    print(movie_id)
    return len(movie_id)





def pearson_correlation(person1, person2):
    both_rated = {}
    #print(person2)
    for item in train[person1]:
        if item in train[person2]:
            both_rated[item]=1

    n = len(both_rated)
    if n==0:
        return 0 # change it zero

    p1_sum = sum([train[person1][item] for item in both_rated])
    p2_sum = sum([train[person2][item] for item in both_rated])

    p1_sqsum = sum([pow(train[person1][item],2) for item in both_rated])
    p2_sqsum = sum([pow(train[person2][item],2) for item in both_rated])

    product = sum([train[person1][item] * train[person2][item] for item in both_rated])

    num = product - (p1_sum *p2_sum/n)
    denom = sqrt((p1_sqsum - pow(p1_sum,2)/n)*(p2_sqsum- pow(p2_sum,2)/n))
    if denom ==0:
        return 0
    else:
        return num/denom



def most_similar_users(person, number_of_users):
    scores = [(pearson_correlation(person, other_person), other_person) for other_person in train if other_person!=person ]
    scores.sort()
    scores.reverse()
    return scores[0:number_of_users]


def user_recommendations(person):
    totals ={}
    simsums = {}
    ranking_list = []
    for other in train:
        if other==person:
            continue
        sim = pearson_correlation(person, other)

        if sim <=0:
            continue
        for item in train[other]:
            if item not in train[person] or train[person][item] ==0:
                totals.setdefault(item,0)
                totals[item]+= train[other][item]*sim
                simsums.setdefault(item,0)
                simsums[item]+=sim

    rankings = [(total/simsums[item], item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()

    recommendation_list = [(item,score) for score, item in rankings]
    return recommendation_list


def movie_suggestion(user):      
    #no_of_reviews = reviewed_movies(user)
    #print(no_of_reviews)
    no_of_reviews=10
    if no_of_reviews<1:
        print("for user1")
        user ='user1'
    #print(most_similar_users(user, 30))
    x= user_recommendations(user)
    return x



def mae(user, predicted):
    original = test.get(user, None) # original is a dictionary; predicted is a list
    s=[]
    for i in predicted:
        s.append(i[0])
    diff =0
    n=0
    for i in original:
        if i not in s:
            continue
        k=s.index(i)
        diff += abs(original[i] - predicted[k][1])
        n+=1
    # print(diff, n)
    return diff/n



ans=0
n=10
for i in range(n):
    testuser = df3['name'][i]
    x = movie_suggestion(testuser)

    print('\nPredicted rating\t\t Item id\n')
    for j in x[:10]:
        # print(j[1], '\t', single_name(j[0])) 
        print(j[1], '\t\t\t', j[0])

    a = mae(testuser, x)
    ans+=a
    print("Average error for user ", i, ":  ", a)


print("\nMAE: ", ans/n)






















