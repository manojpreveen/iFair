import csv
import sklearn
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
from sklearn.linear_model import LogisticRegression
from csv import reader

TrainInput = []
with open('iFairDataTrain.csv', 'r') as obj:
    csv_reader = reader(obj)
    temp = list(csv_reader)
    for row in temp :
        TrainInput.append(row)

TrainOutput = []
with open('iFairTrainDataOutput.csv', 'r') as obj:
    csv_reader = reader(obj)
    temp = list(csv_reader)
    for row in temp :
        TrainOutput.append(row)

TestInput = []
with open('iFairDataTest.csv', 'r') as obj:
    csv_reader = reader(obj)
    temp = list(csv_reader)
    for row in temp :
        TestInput.append(row)

TestOutput = []
with open('iFairTestDataOutput.csv', 'r') as obj:
    csv_reader = reader(obj)
    temp = list(csv_reader)
    for row in temp :
        TestOutput.append(row)

#Accuracy
LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(TrainInput, TrainOutput)
PredictedOutput = LR.predict(TestInput)
print(PredictedOutput)
print(round(LR.score(TestInput,TestOutput), 4))

#yNN
input = []
k = 20
with open('PrunedTest.csv', 'r') as obj:
    csv_reader = reader(obj)
    temp = list(csv_reader)
    for row in temp:
        input.append(row)

input = np.array(input)
output = np.array(input[:, -1]).flatten()
input = input[:, :-1]
input = preprocessing.scale(input)
sensitive = input[:, -1]
non_sensitive = input[:, :-1]

nbrs = NearestNeighbors(n_neighbors = k+1, algorithm = 'auto').fit(non_sensitive)
distancesTrain, indices = nbrs.kneighbors(non_sensitive)

ynn = 0
for i in range(0, len(non_sensitive)) :
    for j in range(1,k+1) :
        x = PredictedOutput[i].astype(np.int)
        y = PredictedOutput[indices[i][j]].astype(np.int)
        ynn += abs(x-y)
ynn /= k
ynn /= len(non_sensitive)
ynn = 1 - ynn

print(ynn)

 


