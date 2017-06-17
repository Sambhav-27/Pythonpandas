import re, string, scipy.io
from stemming.porter2 import stem
import numpy as np
from sklearn import neighbors, svm

def getVocabList():
	vocabList = []
	with open('vocab.txt','r') as f:
	    for line in f:
	        for word in line.split():
	        	if not word.isdigit():
	        		vocabList.append(word)	        		 
	return vocabList

def processEmail(email_contents):
	word_indices = []
	temp = []	
	ch = email_contents
	vocabList = getVocabList()
	ch = ch.lower()
	ch = re.sub("<[^<>]+>", " ", ch)
	ch = re.sub("[0-9]+", "number", ch) # replace all no.s with number
	ch = re.sub("http://[^\s]*", "httpaddr", ch)
	ch = re.sub("https://[^\s]*", "httpaddr", ch)
	ch = re.sub("[^\s]+@[^\s]+", "emailaddr", ch)
	ch = ch.replace("$", "dollar")	
	ch = re.sub("[^a-zA-Z0-9 ]", "",ch)
	ch = ' '.join(ch.split()) # remove all tabs etc
	ch = ch.split()
	for i in ch:
		temp.append(stem(i))
	ch = temp
	for i in ch:
		if i in vocabList:
			word_indices.append(vocabList.index(i)+1)
	
	x = np.zeros(len(vocabList))
	#print(word_indices)
	for i in word_indices:
		x[i-1] = 1
	return x #feature vector


def train_test():
	mat = scipy.io.loadmat('spamTrain.mat')
	mat2 = scipy.io.loadmat('spamTest.mat')
	X_train = mat['X']
	y_train = mat['y'].T[0]
	X_test = mat2['Xtest']
	y_test = mat2['ytest'].T[0]

	#print(y_test)

	clf = neighbors.KNeighborsClassifier()
	#clf = svm.SVR(kernel = 'poly')
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print("accuracy: ", accuracy)

	# example = np.array([[4,2,1,1,1,2,3,2,1],[40,2,1,2,2,2,3,2,1]])	
	
	a ='> Anyone knows how much it costs to host a web portal ?>Well, it depends on how many visitors youre expecting. This can beanywhere from less than 10 bucks a month to a couple of $100. Youshould checkout http://www.rackspace.com/ or perhaps Amazon EC2 ifyoure running something big..To unsubscribe yourself from this mailing list, send an email to: groupname-unsubscribe@egroups.com'
	example = processEmail(a)
	example = example.reshape(1, -1)
	prediction = clf.predict(example)
	print(prediction) # spam =1, non-spam=0

	

# a ='> Anyone knows how much it costs to host a web portal ?>Well, it depends on how many visitors youre expecting. This can beanywhere from less than 10 bucks a month to a couple of $100. Youshould checkout http://www.rackspace.com/ or perhaps Amazon EC2 ifyoure running something big..To unsubscribe yourself from this mailing list, send an email to: groupname-unsubscribe@egroups.com'
# x = processEmail(a)
# print(x)
train_test()


















