import pandas as pd

df1 = pd.DataFrame( { 'hpi':[80,10,89,78],
					'int_rate':[2,3,1,4],
					'us_gdp':[50,100,11,12]},
					index = [2001,2002,2003,2004])

df2 = pd.DataFrame( { 'hpi':[80,10,89,718],
					'int_rate':[2,3,1,41],
					'us_gdp':[50,100,11,12]},
					index = [2005,2006,2007,2008])

df3 = pd.DataFrame( { 'hpi':[80,10,89,78],
					'unemployment':[12,13,11,14],
					'low_tier_hpi':[51,100,11,12]},
					index = [2001,2002,2003,2004])



#inner = intersection, outer= union; left using first's ; right
#print(pd.merge(df1, df2, on='hpi', how='outer')) # index is not honoured here
#print(pd.merge(df1, df3, on='hpi', how='outer')) # all columns are included
#print(pd.merge(df1, df2, on=['hpi', 'int_rate'], how='outer'))
# above line include all possible hpi and int_rate here 6 rows
df1.columns= ['x','y','z']
print(df1.join(df2)) # seems like for join columns should be unique
# join and concat and append

# in join columns are adder acc to index(left,right,inner,outer)