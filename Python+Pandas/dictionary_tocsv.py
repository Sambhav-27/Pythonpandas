from math import sqrt
import pandas as pd

df = pd.read_csv('eucledian_dataset.csv')
#print(df)

dataset={}
t={}

for i in range(len(df)):
	t[df['movie'][i]]=df['rating'][i]
	#print(t)
	
	j=0
	if i<len(df)-1:
		j=i+1
	if df['user'][i]!=df['user'][j]:
		dataset[df['user'][i]]=t
		#print("\n")
		t={}
	

#print(dataset, "\n\n")


def similarity_score(person1, person2):
	both_viewed={}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1

	if len(both_viewed)==0:
		return 0;

	sum_dis = []
	for item in dataset[person1]:
		if item in dataset[person2]:
			sum_dis.append(pow(dataset[person1][item] - dataset[person2][item], 2))
	sum_dis = sum(sum_dis)
	return 1/(1+sqrt(sum_dis))

def pearson_correlation(person1, person2):
	both_rated = {}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item]=1

	n = len(both_rated)
	if n==0:
		return 0

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

	recommendation_list = [item for score, item in rankings]
	return recommendation_list

print(most_similar_users('Lisa Rose', 3))
print(user_recommendations('Toby'))























