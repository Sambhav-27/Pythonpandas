import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation
# support vector machine; convert data b/w -1 and 1; to create tests and training sets
style.use('ggplot')


def create_label(cur_hpi, fut_hpi):
	if fut_hpi >cur_hpi:
		return 1
	else:
		return 0


def moving_average(values):
	return mean(values)


housing_data = pd.read_pickle('File2.pickle')

housing_data = housing_data.pct_change()
housing_data.replace([np.inf, -np.inf], np.nan, inplace = True)
housing_data.dropna(inplace=True)
housing_data['hpi_future'] = housing_data['Value'].shift(-1) # shift down

#print(housing_data[['hpi_future', 'Value']].head())

housing_data['label'] = list(map(create_label, housing_data['Value'], housing_data['hpi_future'])) #fun name followed by parameters
print(housing_data.head())

# housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['sp500'], 10, moving_average) # paras:- what data, window size, function
# print(housing_data.tail())

#S:\python_test\pandas7_mapping.py:33: FutureWarning: pd.rolling_apply is deprecated for Series and will be removed in a future version, replace with 
	#Series.rolling(center=False,window=10).apply(kwargs=<dict>,args=<tuple>,func=<function>)

# x= features; y= labels

x = np.array(housing_data.drop(['label', 'hpi_future'], 1))
x = preprocessing.scale(x)
y = np.array(housing_data['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
#i.e. train on 80% and test on 20%
clf = svm.SVC(kernel = 'linear')
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))