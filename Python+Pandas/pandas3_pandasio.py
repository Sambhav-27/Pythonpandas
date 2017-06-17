import pandas as pd

df = pd.read_csv('S:\python_test\ZILL-Z77006_MPC.csv')
print(df.head())

df.set_index('Date', inplace=True)

#to save to a new csv file
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

#to rename columns
df.columns = ['New_name'] # here list all columns
df.rename(columns= { 'New_name' : 'New_name2'}, inplace=True) #for specific columns
print(df.head())


# to remove header names in csv
df.to_csv('newcsv3.csv', header=False)
# to read back with names a csv without headers
df = pd.read_csv('newcsv3.csv', names=['Date', 'New_name2'], index_col=0)
print(df.head())