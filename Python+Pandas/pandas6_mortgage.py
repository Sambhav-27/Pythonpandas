import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][0][1:]



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

	fout = open('File1.pickle', 'wb') #if doesn't exists creates a file
	pickle.dump(main_df, fout)
	fout.close()


def HPI_benchmark(): # for entire country
	df = quandl.get('FMAC/HPI_USA', authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Value'] = (df['Value'] - df["Value"][0]) /df['Value'][0] *100
	df.rename(columns={'Value':'Benchmark'}, inplace=True)
	return df

def get_mortgage(): # for entire country
	df = quandl.get('FMAC/MORTG', trim_start="1975-01-01", authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Value'] = (df['Value'] - df["Value"][0]) /df['Value'][0] *100

	df = df.resample('1D').mean()
	df = df.resample('M').mean() # to resample to end of month
	return df


def sp500_data(): # for entire country
	df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Adjusted Close'] = (df['Adjusted Close'] - df["Adjusted Close"][0]) /df['Adjusted Close'][0] *100
	df = df.resample('M').mean()
	df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
	df = df['sp500']
	return df

def gdp_data(): # for entire country
	df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Value'] = (df['Value'] - df["Value"][0]) /df['Value'][0] *100
	df = df.resample('M').mean()
	df.rename(columns={'Value':'GDP'}, inplace=True)
	df = df['GDP']
	return df

def us_unemployment(): # for entire country
	df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken="AJPFiEaX-yyUPi6KdxrH")
	df['Unemployment Rate'] = (df['Unemployment Rate'] - df["Unemployment Rate"][0]) /df['Unemployment Rate'][0] *100
	df = df.resample('1D').mean()
	df = df.resample('M').mean()	
	return df



#grab_initials() # need to call this only once to write into file File1

fin = open('File1.pickle', 'rb') # if doesn't exists then error
hpi_data = pickle.load(fin)
m30 = get_mortgage()
hpi_bench = HPI_benchmark()

sp500 = sp500_data()
us_gdp = gdp_data()
unemp = us_unemployment()

hpi = hpi_data.join([m30, unemp, us_gdp, sp500, hpi_bench])

print(hpi)
print(hpi.corr())

hpi.to_pickle('File2.pickle')



