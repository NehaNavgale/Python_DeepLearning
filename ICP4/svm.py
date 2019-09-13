# Support Vector Machine (SVM)

# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import classification_report

# Importing the dataset
dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
y = dataset['Type']

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

# # Feature Scaling
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# Fitting SVM to the Training set
classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#Calculating Accuracy
print(metrics.accuracy_score(y_test,y_pred))

print(classification_report(y_test,y_pred))
