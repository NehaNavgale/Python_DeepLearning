import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm

# df = pd.read_csv('./dataset/dataset_183_adult.csv')
# X = df.values[:, 0:14]
# Y = df.values[:,14]
#
# X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)
#
#
# ### Naive Bayes ###
# gnb=GaussianNB()
# gnb.fit(X_train,y_train)
# y_pred=gnb.predict(X_test)
#
# ### SVM ###
# model = svm.SVC(kernel='rbf',max_iter=9000)
# model.fit(X_train, y_train)
# y_pred= model.predict(X_test)
#
#
# from sklearn.neighbors import KNeighborsClassifier
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train,y_train)
# knn.score(X_train,y_train)
# train_score = knn.score(X_train,y_train)
# test_score = knn.score(X_test,y_test)
#






#Loading Dataset
adults = pd.read_csv('./dataset/dataset_183_adult.csv')
train_data = adults.drop("class",axis=1)
label = adults['class']

#Finding the Missing Values
print(format(adults.isnull().sum()))

#Eliminating NAN values
adults.dropna(axis = 0, inplace= True)

#Converting non-numeric values to numeric
data_binary = pd.get_dummies(adults) #Convert categorical variable into dummy/indicator variables.

data_binary.head()
# print(data_binary)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data_binary,label)
performance = []

# creating Gaussin Naive Bayes object for classification
from sklearn.naive_bayes import GaussianNB

GNB = GaussianNB()

# Training Model
GNB.fit(x_train,y_train)
train_score = GNB.score(x_train,y_train)
# predicting Output
test_score = GNB.score(x_test,y_test)
print(f'Gaussian Naive Bayes : Training score - {train_score} - Test score - {test_score}')

performance.append({'algorithm':'Gaussian Naive Bayes', 'training_score':train_score, 'testing_score':test_score})

# creating KNN object for classification

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

knn.score(x_train,y_train)

train_score = knn.score(x_train,y_train)
test_score = knn.score(x_test,y_test)

print(f'K Neighbors : Training score - {train_score} - Test score - {test_score}')

performance.append({'algorithm':'K Neighbors', 'training_score':train_score, 'testing_score':test_score})

# creating SVM object for classification

from sklearn import svm

svc = svm.SVC(kernel='linear')


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(data_binary,label)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)
svc.fit(x_train_scaled,y_train)

train_score = svc.score(x_train_scaled,y_train)
test_score = svc.score(x_test_scaled, y_test)

print(f'SVM : Training score - {train_score} - Test score - {test_score}')

performance.append({'algorithm':'SVM', 'training_score':train_score, 'testing_score':test_score})