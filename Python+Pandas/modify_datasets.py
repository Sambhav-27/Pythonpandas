import pandas as pd

df = pd.read_csv('wines.csv')

# a= {'id': [],'username':[]}
# for i in range(len(df)):
# 	if i==0:
# 		continue
# 	a['id'].append(i)
# 	#a['username'].append('user'+str(i))
# 	a['username'].append('user'+str(df['userId'][i]))

df1 = df[['id', 'name']]
# df1 = pd.DataFrame(a)
df1 = df1.head(1000)
print(df1)
df1.to_csv('wines2.csv', index=False)




# df = df1.join(df)
# # # df['new']= df['userId']*2
# df.rename(columns= {'movieId' : 'wine_id'}, inplace=True)

# df2 = pd.DataFrame({'wine_id':[]})
# df2['wine_id']= df['wine_id']
# df3 = pd.DataFrame({'rating':[]})
# df3['rating'] = df['rating'].astype(int)

# df1 = df1.join(df2)
# df1 = df1.join(df3)

# df4 = pd.read_csv('movies.csv')
# df5 = pd.DataFrame({'comment':[]})
# df5['comment']=df4['genres']
# df1 = df1.join(df5)
# #print(df.head())
# print(df1.head(10))
# df6 = df1.head(1000)

# df6.to_csv('movie_reviews2.csv', index=False)
