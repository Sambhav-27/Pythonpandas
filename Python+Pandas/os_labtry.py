from math import sqrt
import pandas as pd

df = pd.read_csv('C:\\Users\\sambhav\\Desktop\\movies.csv')
print(df.head())
print("\n\n\n\n")


x= str(df.loc[df['title']=='Toy Story (1995)']['genres'])
#if x.endswith('Name: genres, dtype: object'):
x = x[:-28]
x= x[5:]
print(x)

print(x.split('|'))




		






















