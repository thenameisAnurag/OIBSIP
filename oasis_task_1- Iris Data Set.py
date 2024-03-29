# -*- coding: utf-8 -*-
"""Oasis Task -1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mgYfd8vXXqSwZkLJxM1xjoc1AipufhBh

Name - Anurag Mishra

#Task 1:

 Iris flower has three species; setosa, versicolor, and virginica, which differs according to their
measurements. Now assume that you have the measurements of the iris flowers according to
their species, and here your task is to train a machine learning model that can learn from the
measurements of the iris species and classify them.
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Iris.csv')

data.head()

data['Species'].value_counts()

"""# Preprocessing Data set
Checking the Null Values
"""

data.isnull().sum()

"""## Visualising the data"""

#Scatter Plot
species=['Iris-setosa','Iris-versicolor','Iris-virginica']
color=['red','green','yellow']
for i in range(3):
  x=data[data['Species']==species[i]] #itreation of loop through all the species
  plt.scatter(x['SepalLengthCm'],x['PetalWidthCm'],c=color[i],label=species[i])
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalWidthCm')
plt.legend()
plt.show()

for i in range (3):
  x=data[data['Species']==species[i]]
  plt.scatter(x['PetalLengthCm'],x['SepalLengthCm'],c = color[i],label=species[i])
plt.xlabel('PetalLengthCm')
plt.ylabel('SepalLengthCm')
plt.legend()
plt.show()

"""# Corelation Matrix
(Finding the Realtionship of each variable)
"""

data.corr()

"""# Modeling the data
Standerdising the code
"""

from sklearn.preprocessing import StandardScaler
scale=StandardScaler()

X=(data.drop('Species',axis=1))

#target variable
Y =data['Species']

X.head()

"""# Splitting the data - 80% training and 20% testing"""

from sklearn.model_selection import train_test_split
X_test, X_train , Y_test,Y_train=train_test_split(X,Y,test_size=0.2)

X_train=scale.fit_transform(X_train)
X_test=scale.fit_transform(X_test)

"""# Classification Using KNN"""

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X_train,Y_train)

Y_pred = knn.predict(X_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy*100)

"""# Classification Using SVM"""

from sklearn.svm import SVC
model=SVC()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy*100)

"""# Classification Using Decsion Tree"""

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy*100)

"""# Classification Using Random Forest"""

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy*100)

"""# Classification Using Logistic Regression"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy:", accuracy*100)

