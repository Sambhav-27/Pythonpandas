import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

bridge_ht= {'meters': [10.23, 10.32, 10.11, 10.98, 10.89, 10.11, 6212.42, 10.28, 10.02]}

df = pd.DataFrame(bridge_ht)
df['STD'] = pd.rolling_std(df['meters'], 2) # rolling std with window size =2; add 1more col
print(df)

temp = df.describe()
#print(temp)
df2 = temp['meters']['std']
print(temp)
print(df2)

df = df[ (df['STD'] < df2) ]  #include only those rows with STD<df2
print(df)
#df.plot() # plots all columns
df['meters'].plot()  #plots specifc columns
plt.show()


