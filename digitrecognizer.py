# import libraries
import os.path
import numpy as np
from sklearn import neighbors

# change directory to where you downloaded training and test data
os.chdir("C:\\Users\\Terence\\Downloads") 

# create empty arrays which will store features and labels of training set
x=[]
y=[]

# Open training set and add the labels to the y array and the features to the x array.
# Since this is a csv, I find the first comma which gives me the first column of data.
# The first column is the labels. 
# All the data after that can be added as a 1 by 784 array representing all the features of that sample
# Note that I replace "\n" because the end of each line has '\n'
# Also note, I did it this way before I realized python had an import csv library

with open("train.csv","r") as f:
	next(f)
	for line in f:
		y.append(line[:line.find(",")])
		line = line.replace("\n","")
		x.append(line[line.find(",")+1:].split(","))e.find(",")+1:].split(","))

# Create an empty array for the features of the test sample
testx = []

# Add the features of the test sample into the above array
with open("test.csv","r") as t:
	next(t)
	for line in t:
		testx.append(line.replace("\n","").split(","))

#create numpy arrays for training and test features and labels
XTrain = np.array(x)
YTrain = np.array(y)
XTest = np.array(testx)

#instantiate the classifier
knn = neighbors.KNeighborsClassifier()

#fit the data
knn.fit(XTrain,YTrain)

#predict the data, warning this takes a while...30+minutes
pred = knn.predict(XTest)

# At this point pred will be an array of predictions for each set of features
# Also note that I could have split my training data into 75% training and 25% testing 
# and estimated my predictive power as such:
# XTrain = np.array(x[:30000])
# YTrain = np.array(y[:30000])
# XTest = np.array(x[30000:])
# YTest = np.array(x[30000:])
# knn.fit(XTrain,YTrain).score(XTest,YTest)
#
# This would have output 0.96633333333333338, which is to say that it estimated ~96.63% correctly.
# There was a total of 42000 training samples so since I split it into 30,000 and 12,000 
# as above, that means this classifier correctly predicted 11596 of the 12000 digits.

# The Kaggle competition requires that you write it to a CSV file before submitting
# Therefore what follows is writing the data into the format required.

f = open("predictions.csv","w")
f.write('ImageId,Label\n")

for i in range(0,28000):
	f.write(str(i+1)+","+str(pred[i])+"\n")

f.close()