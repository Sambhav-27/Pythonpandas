import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

a = { 'Day' :[1,2,3,4,5,6],                 
	  'Visitors': [23,45,12,122,23,56],
	  'Bounce_rate' :[67,78,78,53,88,56] }	# python dictionary

df = pd.DataFrame(a)
print(df.head(2), "\n\n\n")

# to set index i.e. S.No.  index is no more now a column
df.set_index('Day', inplace=True) 
#df= df.set_index('Day')


#for accessing specific columns
print(df['Visitors'])
print(df.Visitors)
print(df[['Visitors', 'Bounce_rate']])


#to covert to a list/array
print(df.Visitors.tolist()) # only takes one column
print(np.array(df.Bounce_rate))
print(np.array(df[['Bounce_rate', 'Visitors']]))

