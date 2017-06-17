import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
#pickling serializes the data and saves the byte streams

#now to get code for all 50 states

def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][0][1:]

#following is a list of df
#print(fiddy_states)

#following is a df
#print(fiddy_states[0])

#following is a column of df// notice that index is not a column
#print(fiddy_states[0][0])

def grab_initials():	
	main_df = pd.DataFrame
	#now we want abb from row 1 not 0 cuz 0 is heading
	for abbv in state_list():
		query = "FMAC/HPI_" + str(abbv)		
		df = quandl.get(query, authtoken="AJPFiEaX-yyUPi6KdxrH")		
		df.columns = [str(abbv)] # to rename the columns
		#df = df.pct_change() # pct change at every point
		df[abbv] = (df[abbv] - df[abbv][0]) /df[abbv][0] *100 # pct from first value

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)

	#print(main_df.head())

	fout = open('File1.pickle', 'wb') #if doesn't exists creates a file
	pickle.dump(main_df, fout)
	fout.close()


def HPI_benchmark(): # for entire country
	df = quandl.get('FMAC/HPI_USA', authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Value'] = (df['Value'] - df["Value"][0]) /df['Value'][0] *100
	return df




#grab_initials() # need to call this only once to write into file File1

fin = open('File1.pickle', 'rb') # if doesn't exists then error
hpi_data = pickle.load(fin)
benchmark = HPI_benchmark()
#print(hpi_data)

#modifying columns
#hpi_data['Tx2'] = hpi_data['TX'] *2 # adding extra colums

#print(hpi_data[['TX', 'Tx2']]) # printing specific columns by mentioning in a list

fig = plt.figure()
ax1= plt.subplot2grid((1,1), (0,0))
#hpi_data.plot(ax=ax1) # for all columns
#benchmark.plot(ax=ax1, color='k', linewidth=10)

TX1yr = hpi_data['TX'].resample('A', how='ohlc')
print(TX1yr.head())

hpi_data['TX'].plot(ax=ax1, label='Monthly TX hpi')
TX1yr.plot(ax = ax1);

#plt.legend().remove() #index
plt.legend(loc=4)
plt.show()




# generating correlation
#hpi_cor = hpi_data.corr()
#print(hpi_cor)
#print(hpi_cor.describe())
