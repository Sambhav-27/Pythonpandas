import quandl
import pandas as pd

#df = quandl.get("FMAC/HPI_AK", authtoken="AJPFiEaX-yyUPi6KdxrH")
#print(df.head())

#now to get code for all 50 states

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#following is a list of df
#print(fiddy_states)

#following is a df
#print(fiddy_states[0])

#following is a column of df// notice that index is not a column
#print(fiddy_states[0][0])

#now we want abb from row 1 not 0 cuz 0 is heading
for abbv in fiddy_states[0][0][1:]:
	print("FMAC/HPI_" + str(abbv))
