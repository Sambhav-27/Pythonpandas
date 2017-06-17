import numpy as np
import pandas as pd
import re
from collections import defaultdict
from stemming.porter2 import stem
from sklearn import neighbors, svm

df = pd.read_csv("twitter_data.csv", encoding = 'latin1')

def normalize_text(s):
	s = str(s)
	s = s.lower()
	s = re.sub("[^a-zA-Z0-9 ]", "",s)
	##### stemming ##########
	s = ' '.join(s.split())
	return s

df['text_norm'] = [normalize_text(s) for s in df['text']]
df['description_norm'] = [normalize_text(s) for s in df['description']]


# print(np.any(np.isnan(df['gender:confidence']))) # check if atleat a value is nana
# gender_confidence = df['gender:confidence']
# [np.where(np.invert(np.isnan(df['gender:confidence'])))[0]]
# print((gender_confidence

df = df[df['gender:confidence']==1]
#print(df.shape)