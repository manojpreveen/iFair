import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, label_binarize, StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

file='german.data'
names = ['existingchecking', 'duration', 'credithistory', 'purpose', 'creditamount',
         'savings', 'employmentsince', 'installmentrate', 'statussex', 'otherdebtors',
         'residencesince', 'property', 'age', 'otherinstallmentplans', 'housing',
         'existingcredits', 'job', 'peopleliable', 'telephone', 'foreignworker', 'classification']
data = pd.read_csv(file, names=names, delimiter=' ')

data['classification'].replace([1,2],[1,0],inplace=True)
data_nonsensitive=data.drop('age',axis=1)

# numerical variables labels
numvars = ['creditamount', 'duration', 'installmentrate', 'residencesince', 'existingcredits', 'peopleliable', 'age', 'classification']
# numvars_nonsensitive = ['creditamount', 'duration', 'installmentrate', 'residencesince',
#            'existingcredits', 'peopleliable', 'classification']

# Standardization
numdata_std = pd.DataFrame(StandardScaler().fit_transform(data[numvars].drop(['classification'], axis=1)))

# # numdata_nonsensitive = pd.DataFrame(StandardScaler().fit_transform(data_nonsensitive[numvars_nonsensitive
#                                                                                     ].drop(['classification'], axis=1)))

numdata_std['classification']=data['classification']

#categorical variables labels
catvars = ['existingchecking', 'credithistory', 'purpose', 'savings', 'employmentsince',
           'statussex', 'otherdebtors', 'property', 'otherinstallmentplans', 'housing', 'job',
           'telephone', 'foreignworker']
enc = OneHotEncoder(sparse=False, handle_unknown='ignore')
cat_data = pd.DataFrame(enc.fit_transform(data[catvars]))

data_sensitive = pd.concat([cat_data, numdata_std], axis = 1)
# data_nonsensitive = pd.concat([numdata_nonsensitive, cat_data], axis = 1)

msk = np.random.rand(len(data_sensitive)) < 0.8
train = data_sensitive[msk]
test = data_sensitive[~msk]

train.to_csv('PrunedTrain.csv', header=False)
test.to_csv('PrunedTest.csv', header=False)  
